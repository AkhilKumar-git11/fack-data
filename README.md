# Fake User Generator API 😄

Need fake users but don’t want fake headaches?
This API gives you realistic fake user data in one request.
Perfect for testing, demos, learning, and side projects.

---

## Base URL
https://fack-data.onrender.com

---


## How do I start?
Simple. Get an API key first.

### Get API Key
POST /generate-key

**You’ll get something like this:**
```json
{
  "api_key": "your_api_key_here"
}

Keep this key safe. It’s your ticket to Hollywood 🎟️

Generate a fake user:
GET /fake-user

Authentication:
Yes, we need your API key (no key, no fake people 😅).

Header:
x-api-key: YOUR_API_KEY

Optional magic:
seed (integer)
Use the same seed and you’ll get the same fake user every time.
Great for testing without surprises.

Example request (curl):
curl -H "x-api-key: YOUR_API_KEY" https://fack-data.onrender.com/fake-user?seed=42

Example response:

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "country": "United States"
}

Rate limit:
100 requests per day (free tier).
Enough for learning, testing, and breaking things responsibly 😉

Try it live (Swagger UI):
https://fack-data.onrender.com/docs

No signup. No UI. Just data.
Happy coding 🚀


**Response**
```json
{
  "api_key": "your_api_key_here"
}
