import numpy as np

class NPZ():
    def __init__(self, r_path, r_file, npz_filename):
        self.r_path = r_path
        self.r_file = r_file
        self.npz_filename = npz_filename

        self.read_npz = self.r_path + self.r_file + "/" + self.npz_filename
        self.dut_name = self.r_file.split('_')[1]
        self.time_str = self.r_file.split('.')[-1]
        # ----------------------------------------------------
        self.npy_file = {'traceset': [], 'dataset': [], 'key': []}
        self.npy_file['traceset'] = np.load(self.read_npz)['trace']
        self.npy_file['dataset'] = np.load(self.read_npz)['data']
        self.npy_file['key'] = np.load(self.read_npz)['key']

    def save2npy(self):
        np.save(f"{self.r_path}{self.r_file}/{self.dut_name}_traceset_{self.time_str}.npy",
                self.npy_file['traceset'])
        np.save(f"{self.r_path}{self.r_file}/{self.dut_name}_dataset_{self.time_str}.npy",
                self.npy_file['dataset'])
        np.save(f"{self.r_path}{self.r_file}/{self.dut_name}_key_{self.time_str}.npy",
                self.npy_file['key'])

class NPY():
    def __init__(self, r_path, r_file, npy_tracename, npy_dataname, npy_keyname, parametername):
        self.r_path = r_path
        self.r_file = r_file
        self.npy_tracename = npy_tracename
        self.npy_dataname = npy_dataname
        self.npy_keyname = npy_keyname
        self.parametername = parametername

        self.npz_file = {'traceset': [], 'dataset': [], 'key': [], 'parameter': []}  # .npy
        self.npz_file['traceset'] = self.r_path + self.r_file + "/" + self.npy_tracename
        self.npz_file['dataset'] = self.r_path + self.r_file + "/" + self.npy_dataname
        self.npz_file['key'] = self.r_path + self.r_file + "/" + self.npy_keyname
        self.npz_file['parameter'] = self.r_path + self.r_file + "/" + self.parametername
        # ----------------------------------------------------
        self.traceset = np.load(self.npz_file['traceset'])
        self.dataset = np.load(self.npz_file['dataset'])
        self.key = np.load(self.npz_file['key'])[0]

        file = open(self.npz_file['parameter'], 'r')
        parameters = {}
        for line in file.readlines():
            line = line.strip()
            k = line.split(': ')[0]
            v = line.split(': ')[1]
            parameters[k] = v
        file.close()
        # ----------------------------------------------------
        parameters_list = list(parameters.items())
        self.parameters_arr = np.array(parameters_list)
        self.dut_name = self.r_file.split('_')[1]
        self.time_str = self.r_file.split('_')[-1]

    def save2npz(self):
        np.savez(f"{self.r_path}{self.r_file}/{self.dut_name}_traceset_{self.time_str}.npz",
                 trace=self.traceset, data=self.dataset, key=self.key, parameter=self.parameters_arr)
