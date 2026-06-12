# was-image-save

Exact extracted `Image Save` node class from my modified `was-ns/WAS_Node_Suite.py`.

This repository does **not** contain the full WAS Node Suite.

It contains only:

- `WAS_Image_Save.py`: exact extracted class
- `install_patch.py`: helper to patch the class back into an existing `was-ns/WAS_Node_Suite.py`
- `LICENSE`: original license kept for attribution/compliance

Source extraction:

- class: `WAS_Image_Save`
- source file: `/home/saya/AI/ComfyUI/custom_nodes/was-ns/WAS_Node_Suite.py`
- source lines: 7339-7634
- length: 296 lines

## Usage

Clone this repository, then patch your local WAS Node Suite file:

python install_patch.py /path/to/ComfyUI/custom_nodes/was-ns/WAS_Node_Suite.py

The script creates a backup before replacing the class.
