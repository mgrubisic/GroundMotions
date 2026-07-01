import sys
from pathlib import Path
sys.path.append(Path(__file__).parent.parent.as_posix())
from Database import Database


file_acc = r'H:\NGAWest2\V2.2\Acceleration.hdf5'
file_vel = r'H:\NGAWest2\V2.2\Velocity.hdf5'
file_disp = r'H:\NGAWest2\V2.2\Displacement.hdf5'
file_spec = r'H:\NGAWest2\V2.2\Spectra.hdf5'
file_info = r'H:\NGAWest2\V2.2\Info.hdf5'
Database.import_files(file_acc, file_vel, file_disp, file_spec, file_info)
Database.check_database()
