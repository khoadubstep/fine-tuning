import halo.config as cfg
from imutils import paths
import shutil
import os

for split in (cfg.TRAIN, cfg.TEST, cfg.VAL):
    print("[INFO] processing '{} split'...".format(split))
    splitPath = os.path.sep.join([cfg.ORIG_DATASET, split])
    imagePaths = list(paths.list_images(splitPath))

    for imagePath in imagePaths:
        filename = imagePath.split(os.path.sep)[-1]
        label = cfg.CLASSES[int(filename.split("_")[0])]

        dirPath = os.path.sep.join([cfg.GEN_PATH, split, label])

        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        imageGenPath = os.path.sep.join([dirPath, filename])
        shutil.copy2(imagePath, imageGenPath)
