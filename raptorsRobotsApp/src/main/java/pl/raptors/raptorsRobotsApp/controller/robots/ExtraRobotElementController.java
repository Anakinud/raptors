package pl.raptors.raptorsRobotsApp.controller.robots;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import pl.raptors.raptorsRobotsApp.domain.robots.ExtraRobotElement;
import pl.raptors.raptorsRobotsApp.service.robots.ExtraRobotElementService;

import javax.validation.Valid;
import java.util.List;

@RestController
@CrossOrigin(origins = "http://localhost:4200")
@RequestMapping("/robots/extra-elements")
public class ExtraRobotElementController {

    @Autowired
    ExtraRobotElementService extraRobotElementService;

    @GetMapping("/all")
    public List<ExtraRobotElement> getAll() {
        return extraRobotElementService.getAll();
    }

    @PostMapping("/add")
    public ExtraRobotElement add(@RequestBody @Valid ExtraRobotElement extraRobotElement) {
        if (extraRobotElement.getId() != null) {
            return extraRobotElementService.updateOne(extraRobotElement);
        } else {
            return extraRobotElementService.addOne(extraRobotElement);
        }
    }

    @PostMapping("/update")
    public ExtraRobotElement update(@RequestBody @Valid ExtraRobotElement extraRobotElement) {
        return extraRobotElementService.updateOne(extraRobotElement);
    }

    @GetMapping("/{id}")
    public ExtraRobotElement getOne(@PathVariable String id) {
        return extraRobotElementService.getOne(id);
    }

    @DeleteMapping("/delete")
    public void delete(@RequestBody @Valid ExtraRobotElement extraRobotElement) {
        extraRobotElementService.deleteOne(extraRobotElement);
    }
}
