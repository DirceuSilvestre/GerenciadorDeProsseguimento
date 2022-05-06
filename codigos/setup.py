import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter", "time", "segundajanela"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Gerenciador de Prosseguimento",
    version="0.1",
    description="""Aplicação para gerenciar onde você parou em cada conteudo consumido.
    Crie a categoria de conteudo, como Serie, Aula, Livro, Quadrinho. 
    E dentro de cada categoria salve o nome da obra com sua temporada, capitulo, ediçao, e etc.""",
    options={"build_exe": build_exe_options},
    executables=[Executable("principal.py", base=base)]
)