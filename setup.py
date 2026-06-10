import cx_Freeze

executaveis = [cx_Freeze.Executable(script="main.py", icon="bases/icone.png", target_name="BeyondTheLanterns.exe")]

cx_Freeze.setup(
    name="Beyond The Lanterns",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["bases", "recursos", "log.dat"]}},  executables=executaveis)