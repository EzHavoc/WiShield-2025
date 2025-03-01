// middleware/securityMiddleware.js
import { scanNetwork } from "../utils/networkScanner.js";
import PrivacyLog from "../models/PrivacyLog.js";
import { io } from "../../server.js";

export const detectThreats = async (req, res, next) => {
  try {
    const networkData = await scanNetwork();
    if (networkData.includes("00:11:22:33:44:55")) {
      // Example rogue AP MAC
      const log = new PrivacyLog({
        userId: req.user.id,
        ipAddress: req.ip,
        violationType: "Rogue AP detected",
      });
      await log.save();
      io.emit("privacy-alert", log);
    }
    next();
  } catch (error) {
    res.status(500).json({ message: "Network scanning failed" });
  }
};
