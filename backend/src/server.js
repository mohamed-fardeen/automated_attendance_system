import dotenv from "dotenv";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// load .env from backend folder
dotenv.config({ path: path.resolve(__dirname, "../.env") });


import connectDB from "./config/database.js";
import app from "./app.js";

dotenv.config({
    path: 'backend/.env'
});

const startServer = async () =>{
    try {
        await connectDB();

        app.on("error", (error) => {
            console.log("ERROR",error);
            throw error;
        });

        app.listen(process.env.PORT || 8000, () => {
            console.log('Server is running on port: `${process.env.PORT}`');
        });
    } catch (error) {
        console.log("MONGODB Connection failed",error);
        
    }
}

startServer();