from fastapi import FastAPI

app = FastAPI()

inventory = {
					1: {
						"name": "Milk",
						"price": 10,
						"brand": "vinamink"
	
						},
					2: {
						"name": "bread",
						"price": 15,
						"brand": "Kinh Do"
						},
					3: {
						"name": "car",
						"price": 1000000,
						"brand": "Rolls-Royce"
						}		
				}

@app.get("/get-by-name")
async def get_item(name: str):
	for item_id in inventory:
		if inventory[item_id]["name"] == name:
			return inventory[item_id]
	


