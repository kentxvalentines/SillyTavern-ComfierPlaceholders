# This file is intended to prevent ComfyUI from throwing an import error 
# if this SillyTavern extension is placed in the ComfyUI custom_nodes directory.
# SillyTavern-ComfierPlaceholders is primarily a SillyTavern extension, but this 
# allows ComfyUI to load it without crashing or displaying errors.

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
