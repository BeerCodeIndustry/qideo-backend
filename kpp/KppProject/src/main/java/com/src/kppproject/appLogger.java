package com.src.kppproject;

import org.apache.logging.log4j.Level;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class appLogger {

    private static final Logger logger = LogManager.getLogger(appLogger.class);

    public static void setLog(Level lvl, String message) {
        logger.log(lvl, message);
    }
}
