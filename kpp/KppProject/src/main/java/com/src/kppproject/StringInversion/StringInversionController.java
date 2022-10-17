package com.src.kppproject.StringInversion;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class StringInversionController {

    @GetMapping("/")
    public String homeView(){
        return "home_page";
    }

    @GetMapping("/stringReverse")
    public String stringReverseView(@RequestParam(required = false, defaultValue = "") String value1,
                                    @RequestParam(required = false, defaultValue = "") String value2,
                                    Model model) throws IllegalArgumentException{
        String name;
        String result_inversion;

        if(!value1.equals("")){
            result_inversion = new StringInversionService().reverse(value1);
            name = "value2";
        }else{
            result_inversion = new StringInversionService().reverse(value2);
            name = "value1";
        }
        
        model.addAttribute(name, result_inversion);

        return "home_page";
    }
}
