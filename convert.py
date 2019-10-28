import tensorflow as tf




saved_model_dir = 'C:/Users/hhj73/Desktop/2019-2/졸업프로젝트2/data/tmp/'
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS,
                                       tf.lite.OpsSet.SELECT_TF_OPS]
tflite_model = converter.convert()
open('C:/Users/hhj73/Desktop/2019-2/졸업프로젝트2/data/tmp/converted_model.tflite', 'wb').write(tflite_model)

# converter.post_training_quantize = True
# tflite_buffer = converter.convert()
# open('./model.tflite', 'wb').write(tflite_buffer)