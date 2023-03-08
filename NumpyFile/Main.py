import numpy as np
import time
import os, sys
import json

from Tool.Transfer import NPZ, NPY
from Tool.ReadFile import ONE_FILE, FILES
from Tool.PlotPrint import PLOT_FIGURE, PRINT_DATA

def main(settings: dict):

    transfer_file = settings["transfer_file"]
    original_file_type = settings["original_file_type"]  # 0 for npz / 1 for npy
    read_npyfile = settings["read_npyfile"]
    read_files = settings["read_files"]  # read each .npy file for one trace
    r_path = settings["r_path"]
    r_file = settings["r_file"]
    npz_filename = settings["npz_filename"]
    npy_tracename = settings["npy_tracename"]
    npy_dataname = settings["npy_dataname"]
    npy_keyname = settings["npy_keyname"]
    parametername = settings["parametername"]
    path = r_path + r_file
    print("File path: ", path)

    # Read N traces, Trim, Save trim
    ntrace = settings["ntrace"]
    trim_trace = settings["trim_trace"]
    save_trim_data = settings["save_trim_data"]
    # ---------- Plot & Print ----------
    plot_trace = settings["plot_trace"]
    print_data = settings["print_data"]
    ptrace = settings["ptrace"]
    vrange = settings["vrange"]
    # ----------------------------------


    if transfer_file:
        if original_file_type == 1:
            npz = NPZ(r_path, r_file, npz_filename)
            npz.save2npy()
        elif original_file_type == 2:
            npy = NPY(r_path, r_file, npy_tracename, npy_dataname, npy_keyname, parametername)
            npy.save2npz()

    if read_npyfile:
        a_file = ONE_FILE(r_path, r_file, npy_tracename, npy_dataname, npy_keyname)
        traceset = a_file.get_trace()
        dataset = a_file.get_data()
        key = a_file.get_key()
        pf = PLOT_FIGURE(r_file, traceset, ptrace, vrange)
        pd = PRINT_DATA(traceset, dataset)
        if plot_trace:
            fig_path = path + "/fig_output"
            pf.plot_data(fig_path)
        if print_data:
            pd.print_data()
        if trim_trace:
            trim_traceset, trim_dataset = a_file.trim_data(ntrace)
            if save_trim_data:
                a_file.save_data()
            if print_data:
                pd.set_data(trim_traceset, trim_dataset)
                pd.print_data()

    if read_files:
        gf = FILES(path, r_path, r_file)
        file_arr = gf.get_files()
        gf.save_file()

if __name__ == "__main__":
    start_time = time.time()
    setting_file_name = "Settings.json"
    if os.path.isfile(setting_file_name):
        setting_file = json.load(open(setting_file_name, 'r'))
        main(setting_file)
    else:
        print("Settings.json NOT FOUND! No settings for the execution of Main.py.")
    print("--- Execution time : %s second ---" % (time.time() - start_time))

