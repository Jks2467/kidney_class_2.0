import numpy as np
import os
import tensorflow as tf


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = tf.keras.models.load_model(os.path.join("artifacts", "training", "trained_model.h5"))
        img = tf.keras.preprocessing.image.load_img(self.filename, target_size=(224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array)
        class_index = int(np.argmax(predictions))

        class_map = {
            0: "cyst",
            1: "normal",
            2: "stone"
        }

        return class_map.get(class_index, "unknown")