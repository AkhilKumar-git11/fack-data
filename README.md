# Fake User Generator API 😄

![Made with FastAPI](https://img.shields.io/badge/Made%20with-FastAPI-009688?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)
![Free Tier](https://img.shields.io/badge/Free%20Tier-100%2Fday-blue?style=for-the-badge)

Need fake users but don’t want fake headaches?  
This API gives you **realistic fake user data** in one request.

Perfect for:
- Testing 🧪
- Demos 🎬
- Learning 📚
- Side projects 🚀

---

## 🌍 Base URL
https://fack-data.onrender.com

---

## 🚀 How do I start?

Simple. Get an API key first.

---

## 🔑 Get API Key

**Endpoint**
POST /generate-key

**Response**
```json
{
  "api_key": "your_api_key_here"
}
```
Keep this key safe. It’s your ticket to Hollywood 🎟️

## 👤 Generate a Fake User
**Endpoint**
```sql
GET /fake-user  
```
## 🔐 Authentication:
Yes, we need your API key (no key, no fake people 😅).

## ✨ Optional Magic
**Query Parameter**
```bash
seed (integer)
```
Same seed = same fake user every time.
Perfect for testing without surprises 🎯

## 📌 Example Request (curl)
```bash
 curl -H "x-api-key: YOUR_API_KEY" \
 https://fack-data.onrender.com/fake-user?seed=42
```
## 📦 Example Response
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "country": "United States"
}
```
## ⏱️ Rate Limit
**100* requests per day (free tier)
Enough for learning, testing, and breaking things responsibly 😉

## 🧪 Try It Live
**Swagger UI (playground):**
```arduino
https://fack-data.onrender.com/docs
```
No signup. No UI. Just data.
## Happy coding 🚀
