import numpy as np
import os, sys

class ONE_FILE():
    def __init__(self, r_path, r_file, npy_tracename, npy_dataname, npy_keyname):
        self.r_path = r_path
        self.r_file = r_file
        self.npy_tracename = npy_tracename
        self.npy_dataname = npy_dataname
        self.npy_keyname = npy_keyname

        self.npy_file = {'traceset': [], 'dataset': [], 'key': []}  # .npy
        self.npy_file['traceset'] = self.r_path + self.r_file + "/" + self.npy_tracename
        self.npy_file['dataset'] = self.r_path + self.r_file + "/" +  self.npy_dataname
        self.npy_file['key'] = self.r_path + self.r_file + "/" + self.npy_keyname
        # ----------------------------------------------------
        self.traceset = np.load(self.npy_file['traceset'])
        self.dataset = np.load(self.npy_file['dataset'])
        self.key = np.load(self.npy_file['key'])[0]

    def get_trace(self):
        return self.traceset

    def get_data(self):
        return self.dataset

    def get_key(self):
        return self.key

    def trim_data(self, ntrace):
        self.trim_traceset = self.traceset[0:ntrace]
        self.trim_dataset = self.dataset[0:ntrace]
        return self.trim_traceset, self.trim_dataset

    def save_data(self):
        dut_name = self.r_file.split('_')[1]
        time_str = self.r_file.split('_')[-1]
        np.save(f"{self.r_path}{self.r_file}/{dut_name}_trim_traceset_{time_str}.npy", self.trim_traceset)
        np.save(f"{self.r_path}{self.r_file}/{dut_name}_trim_dataset_{time_str}.npy", self.trim_dataset)

class FILES():
    def __init__(self, path, r_path, r_file):
        self.path = path
        self.r_path = r_path
        self.r_file = r_file

        self.dut_name = self.r_file.split("_")[0]
        self.time_str = self.r_file.split("_")[-1]
        self.time_str = self.time_str[0:13]

        files = os.listdir(self.path)
        files.sort()
        file_list = []
        for file in files:
            f_name = file
            filename = self.path + "/" + f_name
            file_list.append(filename)
        # ----------------------------------------------------
        samples = len(np.load(file_list[0]))
        self.file_arr = np.zeros(shape=(len(file_list), samples), dtype='float16')
        for i in range(self.file_arr.shape[0]):
            f = np.load(file_list[i])
            self.file_arr[i] = f

    def get_files(self):
        return self.file_arr

    def save_file(self):
        np.save(f"{self.r_path}{self.dut_name}_traceset_{self.time_str}.npy", self.file_arr)
