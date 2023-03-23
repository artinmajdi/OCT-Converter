import os
import imageio
import cv2
import matplotlib.pyplot as plt
import numpy as np

VIDEO_TYPES = ['.avi', '.mp4', ]
IMAGE_TYPES = ['.png', '.bmp', '.tiff', '.jpg', '.jpeg']

class FundusImageWithMetaData(object):
    """ Class to hold the fundus image and any related metadata, and enable saving.

    Attributes:
        image (np.array): Fundus image.
        laterality (str): Left or right eye.
        patient_id (str): Patient ID.
        DOB (str): Patient date of birth.
    """

    def __init__(self, image, laterality=None, patient_id=None, patient_dob=None):
        self.image = image
        self.laterality = laterality
        self.patient_id = patient_id
        self.DOB = patient_dob


    def save(self, filepath):
        """Saves fundus image.

        Args:
            filepath (str): Location to save volume to. Extension must be in IMAGE_TYPES.
        """
        extension = os.path.splitext(filepath)[1]
        if extension.lower() in IMAGE_TYPES:
            cv2.imwrite(filepath, self.image)
        elif extension.lower() == '.npy':
            np.save(filepath, self.image)
        else:
            raise NotImplementedError(
                f'Saving with file extension {extension} not supported'
            )
