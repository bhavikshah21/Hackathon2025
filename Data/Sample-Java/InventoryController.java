@RestController
@RequestMapping("/api/inventory")
public class InventoryController {

    @Autowired
    private PricingService pricingService;

    @GetMapping("/items")
    public List<String> getItems() {
        // Simulate DB connection
        String connectionString = "jdbc:mysql://localhost:3306/inventorydb";
        return List.of("item1", "item2");
    }

    @PostMapping("/add")
    public String addItem(@RequestBody String itemName) {
        return "Added: " + itemName;
    }

    @GetMapping("/price")
    public double getPrice(@RequestParam String item) {
        return pricingService.fetchPrice(item);
    }
}
