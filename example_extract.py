from Database import Database


file_acc = r'H:\NGAWest2\V2.2\Acceleration.hdf5'
file_vel = r'H:\NGAWest2\V2.2\Velocity.hdf5'
file_disp = r'H:\NGAWest2\V2.2\Displacement.hdf5'
file_spec = r'H:\NGAWest2\V2.2\Spectra.hdf5'
file_info = r'H:\NGAWest2\V2.2\Info.hdf5'
Database.import_files(file_acc, file_vel, file_disp, file_spec, file_info)
Database.extract_records(r'C:\Users\admin\Desktop\results',
                          RSN_list=[179, 184, 766, 803, 959, 1048, 1063, 1082, 1084, 1158, 1244, 1605, 4894, 5825, 5827, 6911, 8063, 8130, 8161, 8506],
                          components=['H1', 'H2'],
                          type_='A')



