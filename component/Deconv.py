from __future__ import absolute_import, division


import tensorflow as tf
from keras.layers import Conv2D
from keras.initializers import RandomNormal
from __future__ import absolute_import, division

import numpy as np
from scipy.ndimage.interpolation import map_coordinates as sp_map_coordinates
import tensorflow as tf
from .utils import *
class ConvOffset2D(Conv2D):
    """ConvOffset2D"""

    def __init__(self, filters, init_normal_stddev=0.01, **kwargs):
        self.filters = filters
        super(ConvOffset2D, self).__init__(
            self.filters * 2, (3, 3), padding='same', use_bias=False,
            # TODO gradients are near zero if init is zeros
            kernel_initializer='zeros',
            # kernel_initializer=RandomNormal(0, init_normal_stddev),
            **kwargs
        )

    def call(self, x):

        x_shape = x.get_shape() #(?, 32, 25, 50)
        print("x_shape = x.get_shape()")
        print(x_shape)
        offsets = super(ConvOffset2D, self).call(x)   #(?, 64, 25, 50)
        print("offsets = super(ConvOffset2D, self).call(x)")
        print(offsets.shape)
        offsets = self._to_bc_h_w_2(offsets, x_shape)  #(?, 32, 25, 2)
        print("offsets = self._to_bc_h_w_2(offsets, x_shape)")
        print(offsets.shape)
        x = self._to_bc_h_w(x, x_shape) #(?, 32, 25)
        print("x = self._to_bc_h_w(x, x_shape)")
        print(x.shape)
        x_offset = tf_batch_map_offsets(x, offsets) #(?, ?)
        print("x_offset = tf_batch_map_offsets(x, offsets)")
        print(x_offset.shape)
        x_offset = self._to_b_h_w_c(x_offset, x_shape) #(?, 32, 25, 50)
        print(" x_offset = self._to_b_h_w_c(x_offset, x_shape)")

        return x_offset

    def compute_output_shape(self, input_shape):
        return input_shape

    @staticmethod
    def _to_bc_h_w_2(x, x_shape):

        """(b, 2c, h , w) -> (b*c, h, w, 2)"""
        x = tf.reshape(x, (-1, int(x_shape[2]), int(x_shape[3]), 2))
        return x

    @staticmethod
    def _to_bc_h_w(x, x_shape):

        x = tf.reshape(x, (-1, int(x_shape[2]), int(x_shape[3])))
        return x

    @staticmethod
    def _to_b_h_w_c(x, x_shape):

        x = tf.reshape(
            x, (-1, int(x_shape[3]), int(x_shape[1]), int(x_shape[2]))
        )
        x = tf.transpose(x, [0, 2, 3, 1])
        return x

        return  offsets