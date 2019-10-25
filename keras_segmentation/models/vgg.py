import keras
from keras.models import *
from keras.layers import *
from .config import IMAGE_ORDERING

def get_my_vgg(input_height=512,input_width=512):
	img_input = Input(shape=(input_height,input_width , 3 ))
	#layer A
	A = Conv2D(64, (3, 3), activation='relu', padding='same', name='A_c1', data_format='channels_last' )(img_input)
	A = Conv2D(64, (3, 3), activation='relu', padding='same', name='A_c2', data_format='channels_last' )(x)
	A = MaxPooling2D((2, 2), strides=(2, 2), name='A_MP', data_format='channels_last' )(x)
	A1 = A

	#Layer B
	A = Conv2D(128, (3, 3), activation='relu', padding='same', name='B_c1', data_format='channels_last' )(x)
	A = Conv2D(128, (3, 3), activation='relu', padding='same', name='B_c2', data_format='channels_last' )(x)
	A = MaxPooling2D((2, 2), strides=(2, 2), name='B+MP', data_format='channels_last' )(x)
	B1 = A

	#Layer C
	A = Conv2D(256, (3, 3), activation='relu', padding='same', name='C_c1', data_format='channels_last' )(x)
	A = Conv2D(256, (3, 3), activation='relu', padding='same', name='C_c2', data_format='channels_last' )(x)
	A = Conv2D(256, (3, 3), activation='relu', padding='same', name='C_c3', data_format='channels_last' )(x)
	A = MaxPooling2D((2, 2), strides=(2, 2), name='C_MP', data_format='channels_last' )(x)
	C1 = A

	#Layer D
	A = Conv2D(512, (3, 3), activation='relu', padding='same', name='D_c1', data_format='channels_last' )(x)
	A = Conv2D(512, (3, 3), activation='relu', padding='same', name='D_c2', data_format='channels_last' )(x)
	A = Conv2D(512, (3, 3), activation='relu', padding='same', name='D_c3', data_format='channels_last' )(x)
	A = MaxPooling2D((2, 2), strides=(2, 2), name='D_MP', data_format='channels_last' )(x)
	D1 = A

	# Block 5
	A = Conv2D(512, (3, 3), activation='relu', padding='same', name='E_C1', data_format='channels_last' )(x)
	A = Conv2D(512, (3, 3), activation='relu', padding='same', name='E_c2', data_format='channels_last' )(x)
	A = Conv2D(512, (3, 3), activation='relu', padding='same', name='E_c3', data_format='channels_last' )(x)
	A = MaxPooling2D((2, 2), strides=(2, 2), name='C_MP', data_format='channels_last')(x)
	E1 = A
	
	return img_input, [A1,B1,C1,D1,E1]
