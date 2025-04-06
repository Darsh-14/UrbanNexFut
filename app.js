// import express from "express";
// import cors from "cors";
// import dotenv from "dotenv";
// import { GoogleGenerativeAI } from "@google/genai";
// import path from "path";
// import { fileURLToPath } from "url";

// dotenv.config();
// const app = express();
// const PORT = process.env.PORT || 8080;

// // Handle ESM __dirname/__filename
// const __filename = fileURLToPath(import.meta.url);
// const __dirname = path.dirname(__filename);

// // Middleware
// app.use(cors());
// app.use(express.json());
// app.use(express.static(path.join(__dirname, "public"))); // serve static files

// // Gemini AI setup
// const API_KEY = process.env.GEMINI_API_KEY;
// if (!API_KEY) {
//     throw new Error("❌ GEMINI_API_KEY is missing in .env file");
// }
// const genAI = new GoogleGenerativeAI(API_KEY);

// // Chat endpoint
// app.post("/chat", async (req, res) => {
//     try {
//         const { prompt } = req.body;
//         if (!prompt) return res.status(400).json({ error: "No prompt provided" });

//         const model = genAI.getGenerativeModel({ model: "gemini-pro" });
//         const result = await model.generateContent(prompt);
//         const response = await result.response;

//         const text = response.text();
//         if (!text) return res.status(500).json({ error: "AI response empty" });

//         res.json({ response: text });
//     } catch (err) {
//         console.error("❌ AI Error:", err.message);
//         res.status(500).json({ error: "Server error: " + err.message });
//     }
// });

// // Routes for static pages
// app.get("/", (req, res) => res.sendFile(path.join(__dirname, "public", "home.html")));
// app.get("/about", (req, res) => res.sendFile(path.join(__dirname, "public", "about.html")));
// app.get("/services", (req, res) => res.sendFile(path.join(__dirname, "public", "services.html")));
// app.get("/contact", (req, res) => res.sendFile(path.join(__dirname, "public", "contact.html")));
// app.get("/map", (req, res) => res.sendFile(path.join(__dirname, "public", "map.html")));
// app.get("/add-zone", (req, res) => res.sendFile(path.join(__dirname, "public", "add_zone.html")));

// // 404 fallback
// app.use((req, res) => {
//     res.status(404).sendFile(path.join(__dirname, "public", "404.html"));
// });

// // Start server
// app.listen(PORT, () => {
//     console.log(`✅ Server running at http://localhost:${PORT}`);
// });
