import mongoose from "mongoose";

const connectDB = async () => {
  try {
    console.log("URI RECEIVED =>", JSON.stringify(process.env.MONGODB_URI));

    const connectionInstance = await mongoose.connect(
      process.env.MONGODB_URI
    );

    console.log(
      `MongoDB connected !! Host: ${connectionInstance.connection.host}`
    );
  } catch (error) {
    console.log("MongoDB connection failed", error);
    process.exit(1);
  }
};

export default connectDB;