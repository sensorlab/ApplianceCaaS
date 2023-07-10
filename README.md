# ApplianceCaaS

ApplianceCaaS is a containerised classification service using a machine learning model trained on the UK-DALE NILM dataset. The model is saved in pickle format as `nilm_classifier.pkl`.

## Usage

The service accepts a 2D Python list of shape (n, 600) in JSON format, where n is the number of samples and 600 is the length of each sample. It returns a 1D Python list of length n with the predictions, also in JSON format. The model classifies 9 different appliance signals in disaggregated form, returning a number from 0 to 8 corresponding to each appliance in the following order: computer monitor, laptop computer, television, washer dryer, microwave, boiler, toaster, kettle, fridge.

The service listens on TCP port 2524.

Here's an example of sending a Python list using a POST request:

```python
import requests
import json

data = [[...], [...], ...]  # Your 2D list of shape (n, 600)
response = requests.post('http://localhost:2524', json=json.dumps(data))
predictions = json.loads(response.text)
```

## Source

The model in this service comes from our [NILM classification repository](https://github.com/sensorlab/ApplianceClassification).

## Citation

If you use our scripts in your research, please cite:

OGRIZEK, Leo, BERTALANIČ, Blaž, CERAR, Gregor, MEŽA, Marko, FORTUNA, Carolina. Designing a machine learning based non-intrusive load monitoring classifier. V: ŽEMVA, Andrej (ur.), TROST, Andrej (ur.). Zbornik tridesete mednarodne Elektrotehniške in računalniške konference ERK 2021 = Proceedings of the 30th International Electrotechnical and Computer Science Conference ERK 2021 : Portorož, Slovenija, 20. - 21. september 2021.
