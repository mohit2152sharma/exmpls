import os
import sys


def get_md_files(dir: str):
    file_dir = os.path.join(dir, "notes")
    return [
        os.path.join(file_dir, f)
        for f in os.listdir(file_dir)
        if f.endswith(".md") and not f.startswith("README")
    ]


def create_content(files):
    cntnt = []
    for file in files:
        with open(file, "r") as f:
            txt = f.read()
            heading = txt.splitlines()[0].split("#")[-1].strip()
            cntnt.append((heading, txt.strip()))

    return cntnt


def create_readme(cntnt, project_dir: str):
    lang = project_dir.split("-")[0].title()
    sting = f"# {lang} Examples\n"
    for h, t in cntnt:
        sting += f"\n\n<details>\n\n<summary>{h}</summary>\n\n{t}\n\n</details>"

    readme_file = os.path.join(project_dir, "README.md")
    with open(readme_file, "w") as f:
        f.write(sting)
    print(f"successfully written to {readme_file}")


if __name__ == "__main__":
    project_dir = sys.argv[-1]
    files = get_md_files(project_dir)
    print(f"{files=}")
    cntnt = create_content(files)
    create_readme(cntnt, project_dir)
