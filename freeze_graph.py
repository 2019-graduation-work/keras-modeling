from tensorflow import keras
model = keras.models.load_model('C:/Users/hhj73/Desktop/2019-2/졸업프로젝트2/data/trained_model2.h5', compile=False)

export_path = 'C:/Users/hhj73/Desktop/2019-2/졸업프로젝트2/data/tmp'
# keras.experimental.export_saved_model(model, './savedmodel.pb')
model.save(export_path, save_format="tf")