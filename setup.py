from setuptools import setup, find_packages

setup(name="YOLOV",
      version="1.0.0",
      description="YOLOV",
      license='MIT',
      author="Diego De Quintal",
      authoer_email="diego.dequintal@newtoms.com",
      url='https://github.com/diegodequintal/Yolov5',
      packages=['MOT16_eval','yolov5','yolov5.models','yolov5.models.hub','yolov5.utils','yolov5.data','yolov5.utils.aws','yolov5.utils.flask_rest_api','yolov5.utils.google_app_engine','yolov5.utils.loggers','yolov5.utils.loggers.wandb','yolov5.data.images','yolov5.data.hyps','yolov5.data.scripts','deep_sort','deep_sort.configs','deep_sort.deep', 'deep_sort.deep.reid', 'deep_sort.deep.reid.configs', 'deep_sort.deep.reid.docs', 'deep_sort.deep.reid.docs', 'deep_sort.deep.reid.docs','deep_sort.deep.reid.docs.figures','deep_sort.deep.reid.docs.pkg','deep_sort.deep.reid.projects','deep_sort.deep.reid.projects.DML','deep_sort.deep.reid.projects.OSNet_AIN','deep_sort.deep.reid.projects.attribute_recognition','deep_sort.deep.reid.projects.attribute_recognition.datasets','deep_sort.deep.reid.projects.attribute_recognition.models','deep_sort.deep.reid.scripts','deep_sort.deep.reid.tools','deep_sort.deep.reid.torchreid','deep_sort.deep.reid.torchreid.data.datasets','deep_sort.deep.reid.torchreid.data','deep_sort.deep.reid.torchreid.data.datasets.image','deep_sort.deep.reid.torchreid.data.datasets.video','deep_sort.deep.reid.torchreid.engine','deep_sort.deep.reid.torchreid.engine.image','deep_sort.deep.reid.torchreid.engine.video','deep_sort.deep.reid.torchreid.losses','deep_sort.deep.reid.torchreid.metrics','deep_sort.deep.reid.torchreid.metrics.rank_cylib','deep_sort.deep.reid.torchreid.models','deep_sort.deep.reid.torchreid.optim','deep_sort.deep.reid.torchreid.utils','deep_sort.deep.reid.torchreid.utils.GPU-Re-Ranking','deep_sort.deep.reid.torchreid.utils.GPU-Re-Ranking.extension','deep_sort.deep.reid.torchreid.utils.GPU-Re-Ranking.extension.adjacency_matrix','deep_sort.deep.reid.torchreid.utils.GPU-Re-Ranking.extension.propagation', 'deep_sort.utils'],
      include_package_data=True,
      package_data={
        "": ["*.yaml", "*.sh", "*.jpg", "*.gif", "*.md", "*.rst", "*"]
      }
)
