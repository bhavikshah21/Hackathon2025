using Microsoft.AspNetCore.Mvc;
using System.Data.SqlClient;

namespace InventoryAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class InventoryController : ControllerBase
    {
        [HttpGet("items")]
        public IActionResult GetItems()
        {
            string connectionString = "Server=localhost;Database=InventoryDB;User Id=sa;Password=your_password;";
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                // fetch items
            }
            return Ok(new[] { "item1", "item2" });
        }

        [HttpPost("add")]
        public IActionResult AddItem(string itemName)
        {
            // logic to add item
            return Ok("Item added: " + itemName);
        }
    }
}
