# 🖼️ FastAPI Image Converter

This is a FastAPI-based web service that takes an image URL, downloads the image, resizes and compresses it, and returns a base64-encoded version of the image. Optional parameters allow for customization of image size, format, and quality.

## 🚀 Features

- Convert an image from URL to Base64
- Resize image to a specified maximum size
- Change output image format (JPEG, PNG, etc.)
- Customize compression quality
- Easy to extend or integrate

---

## 📦 Requirements

- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pillow (PIL)](https://pillow.readthedocs.io/)
- [Requests](https://docs.python-requests.org/)

### Install dependencies

```bash
pip install fastapi[all] pillow requests
```

---

## 🛠️ Usage

### Start the server

```bash
uvicorn main:app --reload
```

### Health Check

`GET /`

```bash
curl http://localhost:8000/
```

✅ Response:
```json
"The Health Check is successful yay!!!"
```

---

### Convert Image

`POST /image`

#### ✅ Request Body (JSON)

```json
{
  "image_url": "https://example.com/sample.jpg",
  "max_size": [300, 300],           // Optional
  "image_format": "JPEG",           // Optional
  "quality": 50                     // Optional
}
```

#### ✅ Sample Response

```json
{
  "base64_image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD..."
}
```

---

## 📂 Project Structure

```
.
├── main.py         # FastAPI app
└── README.md       # You're here!
```

---

## 🧠 Customization Ideas

- Accept image files via `multipart/form-data`
- Add logging and monitoring
- Enable rate-limiting or auth
- Deploy to a cloud platform (e.g., Vercel, Render, AWS)

---

## 💡 License

MIT License – free to use, modify, and share.

---

## ✨ Author

Made with ❤️ using FastAPI.