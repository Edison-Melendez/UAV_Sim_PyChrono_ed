from acsl_pychrono.executor.simulate_mission import simulateMission
from acsl_pychrono.simulation.simulation import Simulation
import acsl_pychrono.config.config as Cfg
from acsl_pychrono.control.logging import Logging

def runSingleSimulation():
  mis_cfg = Cfg.MissionConfig()
  veh_cfg = Cfg.VehicleConfig()
  env_cfg = Cfg.EnvironmentConfig()
  wrp_prms = Cfg.WrapperParams()

  # # You can modify the default parameters here or in config/config.py
  # mis_cfg.add_payload_flag = False
  # wrp_prms.my_ball_density = 78.5

  sim_cfg = Cfg.SimulationConfig(
    mission_config=mis_cfg,
    vehicle_config=veh_cfg,
    environment_config=env_cfg,
    wrapper_params=wrp_prms
  )

  git_info = Logging.getGitRepoInfo()

  sim = Simulation(sim_cfg)
  simulateMission(sim, git_info)