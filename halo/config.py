import os

ORIG_DATASET = "food-11"

GEN_PATH = "generated"

TRAIN = "training"
TEST = "evaluation"
VAL = "validation"

CLASSES = ["Bread", "Dairy product", "Dessert", "Egg", "Fried food",
           "Meat", "Noodles/Pasta", "Rice", "Seafood", "Soup",
           "Vegetable/Fruit"]

BATCH_SIZE = 32

LE_PATH = os.path.sep.join(["output", "le.cpickle"])
OUTPUT_PATH = "output"

MODEL_PATH = os.path.sep.join([OUTPUT_PATH, "food11.model"])

UNFROZEN_PLOT_PATH = os.path.sep.join([OUTPUT_PATH, "unfrozen.png"])
WARMUP_PLOT_PATH = os.path.sep.join([OUTPUT_PATH, "warmup.png"])
