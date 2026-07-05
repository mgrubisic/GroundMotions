import sys
from pathlib import Path
sys.path.append(Path(__file__).parent.parent.as_posix())
from database import Database


file_acc = r'H:\NGAWest2\V2.5\Acceleration.hdf5'
file_vel = r'H:\NGAWest2\V2.5\Velocity.hdf5'
file_disp = r'H:\NGAWest2\V2.5\Displacement.hdf5'
file_spec = r'H:\NGAWest2\V2.5\Spectra.hdf5'
file_info = r'H:\NGAWest2\V2.5\Info.hdf5'
Database.import_files(file_acc, file_vel, file_disp, file_spec, file_info)
Database.check_database()
