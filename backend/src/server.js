import dotenv from "dotenv";
import path from "path";
import { fileURLToPath } from "url";
import connectDB from "./config/database.js";
import app from "./app.js";

// Resolve __dirname for ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Load environment variables from .env file
dotenv.config({ path: path.resolve(__dirname, "../.env") });

const startServer = async () => {
    try {
        // Connect to MongoDB
        await connectDB();

        // Handle application-level errors
        app.on("error", (error) => {
            console.error("ERROR", error);
            throw error;
        });

        // Start the server
        const PORT = process.env.PORT || 8000;
        app.listen(PORT, () => {
            console.log(`Server is running on port: ${PORT}`);
        });
    } catch (error) {
        console.error("MONGODB Connection failed", error);
        process.exit(1); // Exit the process on failure
    }
};

startServer();