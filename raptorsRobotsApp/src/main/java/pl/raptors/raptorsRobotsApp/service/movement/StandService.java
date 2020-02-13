package pl.raptors.raptorsRobotsApp.service.movement;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Service;
import pl.raptors.raptorsRobotsApp.domain.movement.Pose;
import pl.raptors.raptorsRobotsApp.domain.movement.Stand;
import pl.raptors.raptorsRobotsApp.domain.type.ParkingType;
import pl.raptors.raptorsRobotsApp.domain.type.StandStatus;
import pl.raptors.raptorsRobotsApp.domain.type.StandType;
import pl.raptors.raptorsRobotsApp.repository.movement.StandRepository;
import pl.raptors.raptorsRobotsApp.service.CRUDService;

import java.util.List;
import java.util.Optional;


@Service
public class StandService implements CRUDService<Stand> {

    @Autowired
    StandRepository standrepository;

    @Override
    public Stand addOne(Stand stand) {
        return standrepository.save(stand);
    }

    @Override
    public Stand getOne(String id) {
        return standrepository.findById(id).orElse(null);
    }

    @Override
    public List<Stand> getAll() {
        return standrepository.findAll();
    }

    @Override
    public Stand updateOne(Stand stand) {
        return standrepository.save(stand);
    }

    @Override
    public void deleteOne(Stand stand) {
        standrepository.delete(stand);
    }

    @Override
    public void deleteAll(List<Stand> standList) {
        for (Stand stand : standList) {
            this.deleteOne(stand);
        }
    }

    public void deleteByID(String id) {
        Optional<Stand> standDB = standrepository.findById(id);
        Stand stand = standDB.get();
        standrepository.delete(stand);
    }

    List<Stand> getByPose(Pose pose) {
        return standrepository.findAllByPose(pose);
    }

    public List<Stand> getByParkingType(ParkingType parkingType) {
        return standrepository.findAllByParkingType(parkingType);
    }

    public List<Stand> getByStandType(StandType standType) {
        return standrepository.findAllByStandType(standType);
    }

    public List<Stand> getByStandStatus(StandStatus standStatus) {
        return standrepository.findAllByStandStatus(standStatus);
    }
}