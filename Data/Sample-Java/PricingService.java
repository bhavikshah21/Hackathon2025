@Service
public class PricingService {
    public double fetchPrice(String item) {
        // Call external API
        String pricingUrl = "https://api.pricing-service.com/getPrice";
        return 100.0; // mock price
    }
}
