// import express from "express";
// import cors from "cors";
// import dotenv from "dotenv";
// import { GoogleGenAI } from "@google/genai";

// dotenv.config();
// const app = express();
// app.use(cors());  // ✅ Allow frontend requests
// app.use(express.json());  // ✅ Parse JSON request bodies

// const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// app.post("/chat", async (req, res) => {
//     try {
//         console.log("Received request:", req.body); // Debugging log

//         const { message } = req.body;
//         if (!message) {
//             return res.status(400).json({ reply: "Message is required!" });
//         }

//         const response = await ai.models.generateContent({
//             model: "gemini-2.0-flash",
//             contents: message,
//         });

//         console.log("AI Response:", response); // Debugging log

//         res.json({ reply: response.text || "No response from AI." });
//     } catch (error) {
//         console.error("AI Error:", error); // Log the actual error
//         res.status(500).json({ reply: "Error processing request." });
//     }
// });

// const PORT = process.env.PORT || 5001;
// app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}/chat`));
import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import { GoogleGenerativeAI } from "@google/generative-ai"; // ✅ correct import

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

// ✅ Initialize Gemini AI
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

app.post("/chat", async (req, res) => {
    try {
        const { message } = req.body;

        if (!message) {
            return res.status(400).json({ reply: "Message is required!" });
        }

        const model = genAI.getGenerativeModel({ model: "gemini-pro" });
        const result = await model.generateContent(message);
        const text = result.response.text(); // ✅ Get the generated text

        console.log("✅ AI Response:", text);
        res.json({ reply: text });
    } catch (error) {
        console.error("❌ AI Error:", error.message);
        res.status(500).json({ reply: "Error processing request." });
    }
});

const PORT = process.env.PORT || 5001;
app.listen(PORT, () => {
    console.log(`🚀 Server running on http://localhost:${PORT}/chat`);
});
