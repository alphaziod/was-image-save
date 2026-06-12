from pathlib import Path
import shutil
import sys
from datetime import datetime

if len(sys.argv) != 2:
    raise SystemExit("Usage: python install_patch.py /path/to/WAS_Node_Suite.py")

target = Path(sys.argv[1]).expanduser().resolve()
node_file = Path(__file__).with_name("WAS_Image_Save.py")

if not target.exists():
    raise SystemExit(f"Target not found: {target}")

if not node_file.exists():
    raise SystemExit(f"Node file not found: {node_file}")

lines = target.read_text(errors="replace").splitlines()
new_class = node_file.read_text(errors="replace").splitlines()

start = None
for i, line in enumerate(lines):
    if line.startswith("class WAS_Image_Save:"):
        start = i
        break

if start is None:
    raise SystemExit("class WAS_Image_Save not found in target")

end = len(lines)
for i in range(start + 1, len(lines)):
    if lines[i].startswith("class ") and not lines[i].startswith("class WAS_Image_Save:"):
        end = i
        break

stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup = target.with_name(target.name + f".bak-was-image-save-{stamp}")
shutil.copy2(target, backup)

patched = lines[:start] + new_class + lines[end:]
target.write_text("\n".join(patched) + "\n")

print(f"Patched: {target}")
print(f"Backup : {backup}")
print(f"Replaced lines: {start + 1}-{end}")
