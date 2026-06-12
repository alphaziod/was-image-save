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

# Installation guide

This patch expects an existing WAS Node Suite installation.

It does not replace the full WAS Node Suite. It only replaces the `WAS_Image_Save` class inside:

`ComfyUI/custom_nodes/was-ns/WAS_Node_Suite.py`

The patch script creates a backup before modifying the file.

## Requirements

You need:

- ComfyUI already installed
- WAS Node Suite already installed in `ComfyUI/custom_nodes/was-ns`
- Git
- Python 3

## Windows

Open PowerShell.

Go to your ComfyUI custom nodes folder:

`cd C:\path\to\ComfyUI\custom_nodes`

Clone this patch repo:

`git clone https://github.com/alphaziod/was-image-save.git`

Apply the patch to your WAS Node Suite file:

`cd was-image-save`

`python install_patch.py C:\path\to\ComfyUI\custom_nodes\was-ns\WAS_Node_Suite.py`

If Python is not found, try:

`py install_patch.py C:\path\to\ComfyUI\custom_nodes\was-ns\WAS_Node_Suite.py`

Then restart ComfyUI.

## macOS

Open Terminal.

Go to your ComfyUI custom nodes folder:

`cd /path/to/ComfyUI/custom_nodes`

Clone this patch repo:

`git clone https://github.com/alphaziod/was-image-save.git`

Apply the patch:

`cd was-image-save`

`python3 install_patch.py /path/to/ComfyUI/custom_nodes/was-ns/WAS_Node_Suite.py`

If Git is missing and you use Homebrew:

`brew install git`

Then restart ComfyUI.

## Linux: Debian / Ubuntu

Install Git and Python if needed:

`sudo apt update`

`sudo apt install -y git python3`

Go to your ComfyUI custom nodes folder:

`cd /path/to/ComfyUI/custom_nodes`

Clone this patch repo:

`git clone https://github.com/alphaziod/was-image-save.git`

Apply the patch:

`cd was-image-save`

`python3 install_patch.py /path/to/ComfyUI/custom_nodes/was-ns/WAS_Node_Suite.py`

Then restart ComfyUI.

## Linux: Fedora

Install Git and Python if needed:

`sudo dnf install -y git python3`

Go to your ComfyUI custom nodes folder:

`cd /path/to/ComfyUI/custom_nodes`

Clone this patch repo:

`git clone https://github.com/alphaziod/was-image-save.git`

Apply the patch:

`cd was-image-save`

`python3 install_patch.py /path/to/ComfyUI/custom_nodes/was-ns/WAS_Node_Suite.py`

Example with a common local path:

`python3 install_patch.py ~/AI/ComfyUI/custom_nodes/was-ns/WAS_Node_Suite.py`

Then restart ComfyUI.

## Linux: Arch

Install Git and Python if needed:

`sudo pacman -S --needed git python`

Go to your ComfyUI custom nodes folder:

`cd /path/to/ComfyUI/custom_nodes`

Clone this patch repo:

`git clone https://github.com/alphaziod/was-image-save.git`

Apply the patch:

`cd was-image-save`

`python install_patch.py /path/to/ComfyUI/custom_nodes/was-ns/WAS_Node_Suite.py`

Then restart ComfyUI.

## Linux: NixOS

Temporary shell method:

`nix-shell -p git python3`

Then:

`cd /path/to/ComfyUI/custom_nodes`

`git clone https://github.com/alphaziod/was-image-save.git`

`cd was-image-save`

`python3 install_patch.py /path/to/ComfyUI/custom_nodes/was-ns/WAS_Node_Suite.py`

Then restart ComfyUI.

If you manage ComfyUI declaratively, keep this repo as a patch step in your setup instead of editing the Nix store directly.

## Verify

After patching, restart ComfyUI and check that the node is still named:

`Image Save`

The node should now be able to reload the latest real saved image from its output folder when the upstream image chain is bypassed.

## Restore backup

The patch script creates a backup next to the original file, with a name like:

`WAS_Node_Suite.py.bak-was-image-save-YYYYMMDD-HHMMSS`

To restore manually, copy that backup over `WAS_Node_Suite.py`, then restart ComfyUI.

## Important

This is a patch for an existing WAS Node Suite installation.

It is not meant to replace the full WAS Node Suite.
