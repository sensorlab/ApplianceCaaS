# ApplianceCaaS

This is a containerised classification service using a machine learning model trained on the UK-DALE NILM dataset (sklearn classifier saved in pickle format as nilm_classifier.pkl). 

The service takes a 2D python list of shape (n, 600) in json format, where n is the number of samples and 600 is the length of each sample on tcp port 2524 and returns a 1D python list of length n with the predictions, in json format. The model is trained to classify 9 different appliance signals in disaggregated form, and returns a number from 0 to 8 corresponding to each appliance in the following order: computer monitor, laptop computer, television, washer dryer, microwave, boiler, toaster, kettle, fridge.

The model in this dataset comes from our [NILM classification repository](https://github.com/sensorlab/ApplianceClassification)

If you are using our scripts in your research, please cite.
OGRIZEK, Leo, BERTALANIČ, Blaž, CERAR, Gregor, MEŽA, Marko, FORTUNA, Carolina. Designing a machine learning based non-intrusive load monitoring classifier. V: ŽEMVA, Andrej (ur.), TROST, Andrej (ur.). Zbornik tridesete mednarodne Elektrotehniške in računalniške konference ERK 2021 = Proceedings of the 30th International Electrotechnical and Computer Science Conference ERK 2021 : Portorož, Slovenija, 20. - 21. september 2021.
