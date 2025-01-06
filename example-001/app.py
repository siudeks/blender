import logging
import bpy
import os
from os.path import exists


def run():
  all_objects = bpy.data.objects
  for obj in all_objects:
    print(obj)
    logging.info(obj)
    bpy.data.objects.remove(obj, do_unlink=True)


    # # new general project in blender and sets it active
    # project = bpy.ops.wm.window_new_main()

    # # remove all existing objects
    # bpy.ops.object.select_all(action="SELECT")
    # bpy.ops.object.delete(use_global=False)

    # # add new camera
    # bpy.ops.object.camera_add(
    #     location=[10.0, 0.0, 0.0],
    #     rotation=[0.6799, 0, 0.8254],
    #     enter_editmode=True,
    # )
    # bpy.data.cameras[0].lens = 18

    # # create plane and load image inside the plane
    

    # # file = "piotrkow-tryb-001\piotrkow-tryb-001.blend"
    # # abs_file = os.path.abspath(file)
    # # assert exists(abs_file), "File not found: %s" % abs_file

    # # # bpy.ops.wm.open_mainfile(filepath=abs_file)
    # # # window = bpy.ops.wm.window_new()
    # # bpy.ops.mesh.primitive_cube_add(size=4)
    # cube_obj = bpy.context.active_object
    # print("done")

if __name__ == '__main__':
    logging.info("aaaaaaaaaaaaaa")
    run()
