import mongoose from "mongoose";

const studentSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
    },

    registerNumber: {
      type: String,
      required: true,
      unique: true,
    },

    email: {
      type: String,
    },

    class: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "Class",
      required: true,
    },
  },
  { timestamps: true }
);

export default mongoose.model("Student", studentSchema);