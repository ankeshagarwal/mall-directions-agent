import json
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class Store:
    name: str
    floor: int
    section: str
    category: str
    coordinates: Tuple[float, float]

class MallDirectionsAgent:
    def __init__(self):
        self.stores = self.load_stores()
        self.elevators = self.load_elevators()
        self.rest_areas = self.load_rest_areas()
    
    def load_stores(self) -> Dict[str, Store]:
        """Load store information from database"""
        return {
            "Nike": Store("Nike", 1, "A", "Sports", (10, 15)),
            "Zara": Store("Zara", 1, "B", "Fashion", (25, 20)),
            "Apple Store": Store("Apple Store", 2, "A", "Electronics", (10, 30)),
            "Starbucks": Store("Starbucks", 1, "Food Court", "Cafe", (5, 40)),
            "McDonald's": Store("McDonald's", 1, "Food Court", "Fast Food", (8, 42)),
            "Sephora": Store("Sephora", 2, "B", "Beauty", (28, 25)),
            "LEGO Store": Store("LEGO Store", 2, "C", "Toys", (45, 20)),
            "H&M": Store("H&M", 1, "C", "Fashion", (40, 15)),
            "Cinema": Store("Cinema", 3, "D", "Entertainment", (50, 40)),
            "Toys R Us": Store("Toys R Us", 1, "D", "Toys", (50, 10)),
        }
    
    def load_elevators(self) -> List[Dict]:
        """Load elevator locations"""
        return [
            {"id": "E1", "location": (20, 25), "floors": [1, 2, 3]},
            {"id": "E2", "location": (35, 35), "floors": [1, 2, 3]},
        ]
    
    def load_rest_areas(self) -> List[Dict]:
        """Load rest area locations"""
        return [
            {"name": "Central Lounge", "floor": 1, "location": (25, 35)},
            {"name": "Upper Level Lounge", "floor": 2, "location": (25, 35)},
        ]
    
    def get_store_info(self, store_name: str) -> Dict:
        """Get information about a specific store"""
        store = self.stores.get(store_name)
        if store:
            return {
                "name": store.name,
                "floor": store.floor,
                "section": store.section,
                "category": store.category,
                "coordinates": store.coordinates,
                "status": "Open",
                "hours": "10:00 AM - 10:00 PM"
            }
        return {"error": f"Store '{store_name}' not found"}
    
    def find_stores_by_category(self, category: str) -> List[Dict]:
        """Find all stores in a specific category"""
        results = []
        for store in self.stores.values():
            if store.category.lower() == category.lower():
                results.append({
                    "name": store.name,
                    "floor": store.floor,
                    "section": store.section,
                    "coordinates": store.coordinates
                })
        return results
    
    def get_directions(self, from_location: str, to_store: str) -> Dict:
        """Get directions from one location to a store"""
        target_store = self.stores.get(to_store)
        if not target_store:
            return {"error": f"Store '{to_store}' not found"}
        
        directions = {
            "destination": to_store,
            "floor": target_store.floor,
            "section": target_store.section,
            "route": self.calculate_route(from_location, to_store),
            "estimated_time": "5-10 minutes",
            "nearby_amenities": self.get_nearby_amenities(target_store.floor)
        }
        return directions
    
    def calculate_route(self, from_location: str, to_store: str) -> List[str]:
        """Calculate the route to a store"""
        target_store = self.stores.get(to_store)
        if not target_store:
            return []
        
        route = []
        route.append(f"Go to Section {target_store.section} on Floor {target_store.floor}")
        
        if target_store.floor > 1:
            route.insert(0, "Take the nearest elevator")
        
        route.append(f"Look for {to_store} store")
        
        return route
    
    def get_nearby_amenities(self, floor: int) -> List[str]:
        """Get nearby amenities on a specific floor"""
        amenities = []
        for store in self.stores.values():
            if store.floor == floor and store.category in ["Cafe", "Fast Food"]:
                amenities.append(f"{store.name} ({store.category})")
        return amenities
    
    def get_emergency_contacts(self) -> Dict:
        """Get emergency contacts and help desk locations"""
        return {
            "security": "Dial 911 or visit any security station",
            "help_desk": {"floor": 1, "section": "Main Entrance", "phone": "1-800-MALL-HELP"},
            "medical": {"floor": 2, "section": "C", "description": "Medical office available"},
            "restrooms": "Located on each floor near central lounges"
        }
    
    def get_mall_map(self) -> Dict:
        """Get overall mall map and layout"""
        return {
            "total_floors": 3,
            "ground_floor_highlights": "Entry, food court, cinemas",
            "floor_1": "Shopping stores, restaurants, kids play area",
            "floor_2": "Premium brands, beauty, tech stores",
            "floor_3": "Cinema, entertainment, arcade",
            "parking": "Basement levels 1-3",
            "accessibility": "Wheelchair ramps and elevators on all floors"
        }
    
    def chat(self, user_query: str) -> str:
        """Main chat interface for customer queries"""
        query_lower = user_query.lower().strip()
        
        # Direction queries
        if "where is" in query_lower or "find" in query_lower or "locate" in query_lower:
            for store_name in self.stores.keys():
                if store_name.lower() in query_lower:
                    return json.dumps(self.get_directions("current location", store_name), indent=2)
        
        # Store info queries
        if "tell me about" in query_lower or "info about" in query_lower:
            for store_name in self.stores.keys():
                if store_name.lower() in query_lower:
                    return json.dumps(self.get_store_info(store_name), indent=2)
        
        # Category queries
        if "looking for" in query_lower or "need" in query_lower:
            if "food" in query_lower or "eat" in query_lower:
                return json.dumps(self.find_stores_by_category("Fast Food"), indent=2)
            elif "clothes" in query_lower or "fashion" in query_lower:
                return json.dumps(self.find_stores_by_category("Fashion"), indent=2)
            elif "electronics" in query_lower or "tech" in query_lower:
                return json.dumps(self.find_stores_by_category("Electronics"), indent=2)
            elif "beauty" in query_lower or "makeup" in query_lower:
                return json.dumps(self.find_stores_by_category("Beauty"), indent=2)
        
        # Emergency queries
        if "emergency" in query_lower or "help" in query_lower or "security" in query_lower:
            return json.dumps(self.get_emergency_contacts(), indent=2)
        
        # Map queries
        if "map" in query_lower or "layout" in query_lower or "floors" in query_lower:
            return json.dumps(self.get_mall_map(), indent=2)
        
        # Default response
        return "I'm here to help! You can ask me:\n" \
               "- 'Where is [store name]?'\n" \
               "- 'Tell me about [store name]'\n" \
               "- 'I'm looking for [category]'\n" \
               "- 'Show me the mall map'\n" \
               "- 'Emergency contact'\n" \
               "What would you like to know?"

if __name__ == "__main__":
    agent = MallDirectionsAgent()
    
    # Test interactions
    test_queries = [
        "Where is Nike?",
        "Tell me about Apple Store",
        "I'm looking for food",
        "Show me the mall map",
        "Emergency contact"
    ]
    
    for query in test_queries:
        print(f"\nUser: {query}")
        print(f"Agent: {agent.chat(query)}")
