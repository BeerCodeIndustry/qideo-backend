package com.src.kppproject.StringInversion;
import org.apache.logging.log4j.Level;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
import com.src.kppproject.appLogger;

@Component
@Service
public class StringInversionService {
    public String reverse(String str) {
        if(str.equals("")){
            appLogger.setLog(Level.ERROR, "Illegal arguments in StringInversion: empty");
            throw new IllegalArgumentException("Illegal arguments in StringInversion: empty");

        }
        char[] array = str.toCharArray();
        String result = "";
        for (int i = array.length - 1; i >= 0; i--) {
            result = result + array[i];
        }
        return result;
    }
}
