import mongoose from "mongoose";

const attendanceSessionSchema = new mongoose.Schema(
  {
    class: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Class",
      required: true,
    },

    subject: {
      type: String,
      required: true,
    },

    date: {
      type: Date,
      default: Date.now,
    },

    startedBy: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
    },

    isActive: {
      type: Boolean,
      default: true,
    },
  },
  { timestamps: true }
);

export default mongoose.model("AttendanceSession", attendanceSessionSchema);