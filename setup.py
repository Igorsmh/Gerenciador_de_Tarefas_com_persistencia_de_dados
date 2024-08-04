import sys
import os
from cx_Freeze import setup, Executable


arquivos = ['tasks_icon.ico']

config = Executable(
    script='app.py',
    icon='tasks_icon.ico'
)

setup(
    name="DestravaDev",
    version="1.0",
    description="Gerenciador de Tarefas",
    author="Igor",
    options = {"build_exe": {"include_files": arquivos}},
    executables=[config]
)