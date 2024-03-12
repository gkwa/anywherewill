import importlib.metadata


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

    return 0
