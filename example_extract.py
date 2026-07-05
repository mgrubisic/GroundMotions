from database import Database


file_acc = r'H:\NGAWest2\V2.5\Acceleration.hdf5'
file_vel = r'H:\NGAWest2\V2.5\Velocity.hdf5'
file_disp = r'H:\NGAWest2\V2.5\Displacement.hdf5'
file_spec = r'H:\NGAWest2\V2.5\Spectra.hdf5'
file_info = r'H:\NGAWest2\V2.5\Info.hdf5'
Database.import_files(file_acc, file_vel, file_disp, file_spec, file_info)
Database.extract_records(r'C:\Users\admin\Desktop\results',
                          RSN_list=[953, 960, 1602, 1787, 169, 174, 1111, 1116, 1158, 1148, 900, 848, 752, 767, 1633, 721, 725, 829, 1244, 1485, 68, 125],
                          components=['H1'],
                          type_='A')
