# health_dashboard.py
import streamlit as st
import aiohttp
import asyncio
import time

# List of your microservice endpoints
ENDPOINTS = {
    "Python Parser": "http://localhost:8001/health",
    "Java Parser": "http://localhost:8002/health",
    "CSharp Parser": "http://localhost:8003/health",
    "Generic Parser": "http://localhost:8004/health",
    "Embedder Service": "http://localhost:8010/health",
    "Orchestrator": "http://localhost:9000/health",
    "Chatbot": "http://localhost:9020/health"
}

# Ping each endpoint asynchronously
async def check_endpoint(name, url):
    status = "⏳ Checking..."
    response_time = "-"
    try:
        start = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=3) as resp:
                if resp.status == 200:
                    status = "✅ OK"
                else:
                    status = f"⚠️ Status {resp.status}"
        response_time = f"{(time.time() - start):.2f}s"
    except Exception as e:
        status = "❌ Unreachable"
    return name, status, response_time

async def check_all():
    tasks = [check_endpoint(name, url) for name, url in ENDPOINTS.items()]
    return await asyncio.gather(*tasks)

def display():
    st.title("🚦 API Health Dashboard")
    st.caption("Monitors all microservices for availability")
    refresh_interval = st.slider("Refresh every (seconds)", 2, 30, 5)

    placeholder = st.empty()
    while True:
        results = asyncio.run(check_all())
        with placeholder.container():
            st.markdown("### Service Status")
            st.table({
                "Service": [r[0] for r in results],
                "Status": [r[1] for r in results],
                "Response Time": [r[2] for r in results]
            })
        time.sleep(refresh_interval)

if __name__ == '__main__':
    display()
