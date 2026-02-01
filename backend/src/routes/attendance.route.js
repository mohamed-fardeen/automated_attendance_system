import express from "express";
import {
  startSession,
  markAttendance,
  getSessionAttendance,
} from "../controllers/attendanceController.js";

const router = express.Router();

router.post("/session", startSession);
router.post("/mark", markAttendance);
router.get("/session/:id", getSessionAttendance);

export default router;