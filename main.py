from inference import SegmentModel

sg = SegmentModel()

seg_image = sg.get_prediction(image_path='test.jpg')