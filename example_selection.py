from database import Database
import numpy as np


file_acc = r'H:\NGAWest2\V2.2\Acceleration.hdf5'
file_vel = r'H:\NGAWest2\V2.2\Velocity.hdf5'
file_disp = r'H:\NGAWest2\V2.2\Displacement.hdf5'
file_spec = r'H:\NGAWest2\V2.2\Spectra.hdf5'
file_info = r'H:\NGAWest2\V2.2\Info.hdf5'
selector = Database(r'results')
selector.import_files(file_acc, file_vel, file_disp, file_spec, file_info)
selector.target_spectra(r"spec_data\DBE_AS.txt")
selector.scaling_approach('c', para=(0, 2))
selector.matching_rules(rules=['full', 'c', 'c'], para=[None, (0, 3), (0, 0.5)], weight=[1, 1.5, 1])
selector.constrain_range(magnitude=(5, 20), vs30=(0, 1000), component=['H1', 'H2'], duration=(25, 100), N_events=1)
selected_records, records_info = selector.run(20)
selected_records.sort(key=lambda x: int(x.split('_')[0][3:]))
selector.get_results(files=selected_records, file_SF_error=records_info)

