import express from "express";
import authRoutes from "./routes/auth.js";
import studentRoutes from "./routes/students.js";
import attendanceRoutes from "./routes/attendance.route.js";
import classRoutes from "./routes/classes.js";

const app = express();


// Middleware
app.use(express.json());

// Example route
app.get("/", (req, res) => {
    res.send("API is running...");
});

app.use("/api/auth", authRoutes);
app.use("/api/students", studentRoutes);
app.use("/api/attendance", attendanceRoutes);
app.use("/api/classes", classRoutes);

export default app;

