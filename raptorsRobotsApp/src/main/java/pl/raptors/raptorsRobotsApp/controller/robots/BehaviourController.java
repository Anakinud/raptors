package pl.raptors.raptorsRobotsApp.controller.robots;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import pl.raptors.raptorsRobotsApp.domain.robots.Behaviour;
import pl.raptors.raptorsRobotsApp.service.robots.BehaviourService;

import javax.validation.Valid;
import java.util.List;

@RestController
@CrossOrigin(origins = "http://localhost:4200")
@RequestMapping("/robots/behaviours")
public class BehaviourController {

    @Autowired
    BehaviourService behaviourService;

    @GetMapping("/all")
    public List<Behaviour> getAll() {
        return behaviourService.getAll();
    }

    @PostMapping("/add")
    public Behaviour add(@RequestBody @Valid Behaviour behaviour) {
        if (behaviour.getId() != null) {
            return behaviourService.updateOne(behaviour);
        } else {
            return behaviourService.addOne(behaviour);
        }
    }

    @PostMapping("/update")
    public Behaviour update(@RequestBody @Valid Behaviour behaviour) {
        return behaviourService.updateOne(behaviour);
    }

    @GetMapping("/{id}")
    public Behaviour getOne(@PathVariable String id) {
        return behaviourService.getOne(id);
    }

    @DeleteMapping("/delete")
    public void delete(@RequestBody @Valid Behaviour behaviour) {
        behaviourService.deleteOne(behaviour);
    }
}
