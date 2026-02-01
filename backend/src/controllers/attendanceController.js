import Attendance from "../models/Attendance.model.js";
import AttendanceSession from "../models/AttendanceSession.model.js";

export const startSession = async (req, res) => {
  try {
    const session = await AttendanceSession.create(req.body);
    res.status(201).json(session);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

export const markAttendance = async (req, res) => {
  try {
    const { sessionId, studentId, status } = req.body;

    const record = await Attendance.create({
      session: sessionId,
      student: studentId,
      status,
    });

    res.status(201).json(record);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

export const getSessionAttendance = async (req, res) => {
  try {
    const records = await Attendance.find({ session: req.params.id })
      .populate("student");

    res.json(records);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};