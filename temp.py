import langchain

#print("import ho raha hai")

from pathlib import Path

path = Path("project")

result = path / "data" / "raw"

print(result)
print(type(result))

REPO_ROOT = Path(__file__).resolve()

print(REPO_ROOT)