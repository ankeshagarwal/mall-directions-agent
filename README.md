# Mall Directions Customer Service Agent

A smart customer service agent that helps customers navigate and find stores within a shopping mall.

## Features

- 🗺️ **Directions & Navigation**: Get turn-by-turn directions to any store
- 🏪 **Store Information**: Find store details, categories, and operating hours
- 🔍 **Store Search**: Search stores by category (fashion, food, electronics, etc.)
- 📱 **Emergency Help**: Quick access to emergency contacts and help desk locations
- 🎯 **Amenities**: Discover nearby cafes, restrooms, and rest areas
- 🗺️ **Mall Map**: View overall mall layout and floor information

## Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/ankeshagarwal/mall-directions-agent.git
cd mall-directions-agent

# Install dependencies
pip install -r requirements.txt
```

### Running the Agent

**Command Line Interface:**
```bash
python mall_agent.py
```

**Web API:**
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Chat Interface
```
POST /api/chat
Body: {"message": "Where is Nike?"}
```

### Get All Stores
```
GET /api/stores
```

### Get Specific Store Info
```
GET /api/store/<store_name>
```

### Get Directions
```
POST /api/directions
Body: {"store": "Nike", "from": "current location"}
```

### Search by Category
```
GET /api/category/<category>
Example: /api/category/Fashion
```

### Emergency Contacts
```
GET /api/emergency
```

### Mall Map
```
GET /api/map
```

## Example Queries

- "Where is Nike?"
- "Tell me about Apple Store"
- "I'm looking for food"
- "Find a fashion store"
- "Show me the mall map"
- "Where are the restrooms?"
- "Emergency contact"

## Supported Stores

- Nike (Sports)
- Zara (Fashion)
- Apple Store (Electronics)
- Starbucks (Cafe)
- McDonald's (Fast Food)
- Sephora (Beauty)
- LEGO Store (Toys)
- H&M (Fashion)
- Cinema (Entertainment)
- Toys R Us (Toys)

## Architecture

- **mall_agent.py**: Core agent logic and store database
- **app.py**: Flask web API server
- **config.py**: Configuration settings
- **requirements.txt**: Python dependencies

## Future Enhancements

- Real-time store availability status
- Integration with mall's WiFi and location tracking
- Multi-language support
- Integration with store mobile apps
- Event and promotion notifications
- Accessibility features for people with disabilities
- Mobile app version

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - See LICENSE file for details

## Support

For issues or questions, please open a GitHub issue or contact the development team.
