import importlib.metadata
import sys

from . import main2


def get_project_name():
    try:
        return importlib.metadata.metadata("anywherewill")["Name"]
    except importlib.metadata.PackageNotFoundError:
        return None


def main() -> int:
    project_name = get_project_name()
    if project_name:
        print("Project name:", project_name)
    else:
        print("Project name not found.")

    out = main2.render_template("extended.j2")
    sys.stdout.write(out)

    return 0
