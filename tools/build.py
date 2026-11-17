"""Render an episode. Usage: python tools/build.py 002 [preview.png]"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import epic
root = pathlib.Path(__file__).resolve().parent.parent
epic.build(root / "episodes" / sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
print("Built episode", sys.argv[1])
