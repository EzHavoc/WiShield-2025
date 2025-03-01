require("dotenv").config();

module.exports = {
  PORT: process.env.PORT || 5000,

  // Supabase Credentials
  SUPABASE_URL: process.env.SUPABASE_URL || "https://avtvxuanogqzkiozfimg.supabase.co",
  SUPABASE_KEY: process.env.SUPABASE_KEY || "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF2dHZ4dWFub2dxemtpb3pmaW1nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDA4MTQ2NDIsImV4cCI6MjA1NjM5MDY0Mn0.RQpjLp5izFpdiGNws5H2AubNrjSdjR697tiZY2BtCNI",

  // Authentication
  JWT_SECRET: process.env.JWT_SECRET || "your_secret_key",
  JWT_EXPIRATION: process.env.JWT_EXPIRATION || "1h",

  // Security & Encryption
  ENCRYPTION_KEY: process.env.ENCRYPTION_KEY || "your_256_bit_key",
  ENCRYPTION_IV: process.env.ENCRYPTION_IV || "your_16_byte_iv",

  // WebSocket
  WS_PORT: process.env.WS_PORT || 8080,

  // API Keys (if using third-party services)
  VIRUSTOTAL_API_KEY: process.env.VIRUSTOTAL_API_KEY || "",
  GOOGLE_SAFE_BROWSING_KEY: process.env.GOOGLE_SAFE_BROWSING_KEY || "",
};
