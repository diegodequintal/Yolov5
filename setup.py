from setuptools import setup, find_packages

setup(name="Yolov5Model",
      version="1.0.0",
      description="Yolov5",
      license='MIT',
      author="Diego De Quintal",
      authoer_email="diego.dequintal@newtoms.com",
      url='https://github.com/diegodequintal/Yolov5',
      packages=['yolov5', 'yolov5.models','yolov5.data','yolov5.utils','deep_sort']
)
