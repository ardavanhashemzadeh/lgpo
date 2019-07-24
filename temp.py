with disable_file_system_redirection():
    def copyADMX():
        win10ADMXdpath = os.path.join(win10path, 'ADMX/')
        if not os.path.exists(win10ADMXdpath):
            return 'cant find ADMX'
        try:
            src_files = os.listdir(win10ADMXdpath)
            for file_name in src_files:
                full_file_name = os.path.join(win10ADMXdpath, file_name)
                if (os.path.isfile(full_file_name)):
                    shutil.copy(full_file_name, r'C:/rdtesting/')
            return 'ADMX Success'
        except Exception as e:
            return e.message
