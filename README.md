# was-image-save

Focused fork / patch of the `Image Save` node from WAS Node Suite.

This is **not** the full WAS Node Suite.

This repo contains only the modified `WAS_Image_Save` class and a small patch helper.

## What this fork changes

This fork keeps the exact saved image available through the node.

When the `images` input is missing or the previous part of the workflow is bypassed, the node can reload the latest real image saved in its output folder and return it again as an `IMAGE`.

That makes it possible to restart or continue a ComfyUI generation from the exact point you want, without having to rerun the full chain before this saver node.

## Why

In large ComfyUI workflows, especially with upscales, detailers, color correction, or optional bypass groups, sometimes you want to skip the expensive part that already produced the image.

This patched `Image Save` node lets the workflow continue from the last real saved image instead of losing the image because the upstream nodes were bypassed.

Useful for:

- bypassing the chain before the saver
- restarting from a saved intermediate/final image
- keeping the exact image available after a workflow interruption
- continuing detailer/upscale/color passes without regenerating the base image
- avoiding dependence on ComfyUI preview/history memory only

## Contents

- `WAS_Image_Save.py`  
  Exact extracted modified `WAS_Image_Save` class.

- `install_patch.py`  
  Helper script that patches the class back into an existing `was-ns/WAS_Node_Suite.py`.

- `LICENSE`  
  Original license kept for attribution/compliance.

## Source

Extracted from a modified `was-ns/WAS_Node_Suite.py`.

- class: `WAS_Image_Save`
- original node name in ComfyUI: `Image Save`
- extracted source lines: 7339-7634
- length: 296 lines

## Usage

Clone this repository:

git clone https://github.com/alphaziod/was-image-save.git

Then patch your local WAS Node Suite file:

python install_patch.py /path/to/ComfyUI/custom_nodes/was-ns/WAS_Node_Suite.py

The script creates a backup before replacing the class.

Restart ComfyUI after patching.

## Important

This is a patch for an existing WAS Node Suite installation.

It is not meant to replace the full WAS Node Suite.
