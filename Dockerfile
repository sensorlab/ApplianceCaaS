FROM jupyter/scipy-notebook
RUN pip install flask
COPY nilm_classifier.py ./nilm_classifier.py
COPY nilm_classifier.pkl ./nilm_classifier.pkl

ENTRYPOINT python3 nilm_classifier.py