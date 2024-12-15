# -*- coding: utf-8 -*-
"""CPU - Deep Learning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IvucSPSzYkI3aJvp2XXWRHzu7bBGz_0F
"""

!pip install darts

from darts import TimeSeries
from google.colab import files
import pandas as pd
import io
import matplotlib.pyplot as plt

uploaded = files.upload()

df = pd.read_excel(io.BytesIO(uploaded['CPU_Univariate.xlsx']))
df.head()

cases = df[df.columns[[0]]]

from darts.utils.timeseries_generation import datetime_attribute_timeseries

cases = TimeSeries.from_dataframe(cases)
type(cases)

from darts.models import TransformerModel, NBEATSModel, NHiTSModel, TCNModel, RNNModel, BlockRNNModel, DLinearModel, NLinearModel, TiDEModel, TFTModel, TSMixerModel

"""Horizon 1:"""

n = 1
train, test = cases[:-n], cases[-n:]

NBEATS = NBEATSModel(input_chunk_length = 30, output_chunk_length = 13)
NBEATS.fit(train, epochs = 100, verbose = True)
pred_NBEATS = NBEATS.predict(1)
pred_NBEATS.to_csv('NBEATS_1.csv', encoding = 'utf-8-sig')
files.download('NBEATS_1.csv')

NHiTS = NHiTSModel(input_chunk_length = 30, output_chunk_length = 13)
NHiTS.fit(train, epochs = 100, verbose = True)
pred_NHiTS = NHiTS.predict(1)
pred_NHiTS.to_csv('NHiTS_1.csv', encoding = 'utf-8-sig')
files.download('NHiTS_1.csv')

Transformer = TransformerModel(input_chunk_length = 30, output_chunk_length = 13)
Transformer.fit(train, epochs = 100, verbose = True)
pred_Transformer = Transformer.predict(1)
pred_Transformer.to_csv('Transformer_1.csv', encoding = 'utf-8-sig')
files.download('Transformer_1.csv')

TCN = TCNModel(input_chunk_length = 30, output_chunk_length = 13)
TCN.fit(train, epochs = 100, verbose = True)
pred_TCN = TCN.predict(1)
pred_TCN.to_csv('TCN_1.csv', encoding = 'utf-8-sig')
files.download('TCN_1.csv')

NLinear = NLinearModel(input_chunk_length = 30, output_chunk_length = 13)
NLinear.fit(train, epochs = 100, verbose = True)
pred_NLinear = NLinear.predict(1)
pred_NLinear.to_csv('NLinear_1.csv', encoding = 'utf-8-sig')
files.download('NLinear_1.csv')

DLinear = DLinearModel(input_chunk_length = 30, output_chunk_length = 13)
DLinear.fit(train, epochs = 100, verbose = True)
pred_DLinear = DLinear.predict(1)
pred_DLinear.to_csv('DLinear_1.csv', encoding = 'utf-8-sig')
files.download('DLinear_1.csv')

"""Horizon 3:

"""

n = 3
train, test = cases[:-n], cases[-n:]

NBEATS = NBEATSModel(input_chunk_length = 30, output_chunk_length = 13)
NBEATS.fit(train, epochs = 100, verbose = True)
pred_NBEATS = NBEATS.predict(3)
pred_NBEATS.to_csv('NBEATS_3.csv', encoding = 'utf-8-sig')
files.download('NBEATS_3.csv')

NHiTS = NHiTSModel(input_chunk_length = 30, output_chunk_length = 13)
NHiTS.fit(train, epochs = 100, verbose = True)
pred_NHiTS = NHiTS.predict(3)
pred_NHiTS.to_csv('NHiTS_3.csv', encoding = 'utf-8-sig')
files.download('NHiTS_3.csv')

Transformer = TransformerModel(input_chunk_length = 30, output_chunk_length = 13)
Transformer.fit(train, epochs = 100, verbose = True)
pred_Transformer = Transformer.predict(3)
pred_Transformer.to_csv('Transformer_3.csv', encoding = 'utf-8-sig')
files.download('Transformer_3.csv')

TCN = TCNModel(input_chunk_length = 30, output_chunk_length = 13)
TCN.fit(train, epochs = 100, verbose = True)
pred_TCN = TCN.predict(3)
pred_TCN.to_csv('TCN_3.csv', encoding = 'utf-8-sig')
files.download('TCN_3.csv')

NLinear = NLinearModel(input_chunk_length = 30, output_chunk_length = 13)
NLinear.fit(train, epochs = 100, verbose = True)
pred_NLinear = NLinear.predict(3)
pred_NLinear.to_csv('NLinear_3.csv', encoding = 'utf-8-sig')
files.download('NLinear_3.csv')

DLinear = DLinearModel(input_chunk_length = 30, output_chunk_length = 13)
DLinear.fit(train, epochs = 100, verbose = True)
pred_DLinear = DLinear.predict(3)
pred_DLinear.to_csv('DLinear_3.csv', encoding = 'utf-8-sig')
files.download('DLinear_3.csv')

"""Horizon 6:"""

n = 6
train, test = cases[:-n], cases[-n:]

NBEATS = NBEATSModel(input_chunk_length = 30, output_chunk_length = 13)
NBEATS.fit(train, epochs = 100, verbose = True)
pred_NBEATS = NBEATS.predict(6)
pred_NBEATS.to_csv('NBEATS_6.csv', encoding = 'utf-8-sig')
files.download('NBEATS_6.csv')

NHiTS = NHiTSModel(input_chunk_length = 30, output_chunk_length = 13)
NHiTS.fit(train, epochs = 100, verbose = True)
pred_NHiTS = NHiTS.predict(6)
pred_NHiTS.to_csv('NHiTS_6.csv', encoding = 'utf-8-sig')
files.download('NHiTS_6.csv')

Transformer = TransformerModel(input_chunk_length = 30, output_chunk_length = 13)
Transformer.fit(train, epochs = 100, verbose = True)
pred_Transformer = Transformer.predict(6)
pred_Transformer.to_csv('Transformer_6.csv', encoding = 'utf-8-sig')
files.download('Transformer_6.csv')

TCN = TCNModel(input_chunk_length = 30, output_chunk_length = 13)
TCN.fit(train, epochs = 100, verbose = True)
pred_TCN = TCN.predict(6)
pred_TCN.to_csv('TCN_6.csv', encoding = 'utf-8-sig')
files.download('TCN_6.csv')

NLinear = NLinearModel(input_chunk_length = 30, output_chunk_length = 13)
NLinear.fit(train, epochs = 100, verbose = True)
pred_NLinear = NLinear.predict(6)
pred_NLinear.to_csv('NLinear_6.csv', encoding = 'utf-8-sig')
files.download('NLinear_6.csv')

DLinear = DLinearModel(input_chunk_length = 30, output_chunk_length = 13)
DLinear.fit(train, epochs = 100, verbose = True)
pred_DLinear = DLinear.predict(6)
pred_DLinear.to_csv('DLinear_6.csv', encoding = 'utf-8-sig')
files.download('DLinear_6.csv')

"""Horizon 12:"""

n = 12
train, test = cases[:-n], cases[-n:]

NBEATS = NBEATSModel(input_chunk_length = 30, output_chunk_length = 13)
NBEATS.fit(train, epochs = 100, verbose = True)
pred_NBEATS = NBEATS.predict(12)
pred_NBEATS.to_csv('NBEATS_12.csv', encoding = 'utf-8-sig')
files.download('NBEATS_12.csv')

NHiTS = NHiTSModel(input_chunk_length = 30, output_chunk_length = 13)
NHiTS.fit(train, epochs = 100, verbose = True)
pred_NHiTS = NHiTS.predict(12)
pred_NHiTS.to_csv('NHiTS_12.csv', encoding = 'utf-8-sig')
files.download('NHiTS_12.csv')

Transformer = TransformerModel(input_chunk_length = 30, output_chunk_length = 13)
Transformer.fit(train, epochs = 100, verbose = True)
pred_Transformer = Transformer.predict(12)
pred_Transformer.to_csv('Transformer_12.csv', encoding = 'utf-8-sig')
files.download('Transformer_12.csv')

TCN = TCNModel(input_chunk_length = 30, output_chunk_length = 13)
TCN.fit(train, epochs = 100, verbose = True)
pred_TCN = TCN.predict(12)
pred_TCN.to_csv('TCN_12.csv', encoding = 'utf-8-sig')
files.download('TCN_12.csv')

NLinear = NLinearModel(input_chunk_length = 30, output_chunk_length = 13)
NLinear.fit(train, epochs = 100, verbose = True)
pred_NLinear = NLinear.predict(12)
pred_NLinear.to_csv('NLinear_12.csv', encoding = 'utf-8-sig')
files.download('NLinear_12.csv')

DLinear = DLinearModel(input_chunk_length = 30, output_chunk_length = 13)
DLinear.fit(train, epochs = 100, verbose = True)
pred_DLinear = DLinear.predict(12)
pred_DLinear.to_csv('DLinear_12.csv', encoding = 'utf-8-sig')
files.download('DLinear_12.csv')

"""Horizon 24:"""

n = 24
train, test = cases[:-n], cases[-n:]

NBEATS = NBEATSModel(input_chunk_length = 30, output_chunk_length = 25)
NBEATS.fit(train, epochs = 100, verbose = True)
pred_NBEATS = NBEATS.predict(24)
pred_NBEATS.to_csv('NBEATS_24.csv', encoding = 'utf-8-sig')
files.download('NBEATS_24.csv')

NHiTS = NHiTSModel(input_chunk_length = 30, output_chunk_length = 25)
NHiTS.fit(train, epochs = 100, verbose = True)
pred_NHiTS = NHiTS.predict(24)
pred_NHiTS.to_csv('NHiTS_24.csv', encoding = 'utf-8-sig')
files.download('NHiTS_24.csv')

Transformer = TransformerModel(input_chunk_length = 30, output_chunk_length = 25)
Transformer.fit(train, epochs = 100, verbose = True)
pred_Transformer = Transformer.predict(24)
pred_Transformer.to_csv('Transformer_24.csv', encoding = 'utf-8-sig')
files.download('Transformer_24.csv')

TCN = TCNModel(input_chunk_length = 30, output_chunk_length = 25)
TCN.fit(train, epochs = 100, verbose = True)
pred_TCN = TCN.predict(24)
pred_TCN.to_csv('TCN_24.csv', encoding = 'utf-8-sig')
files.download('TCN_24.csv')

NLinear = NLinearModel(input_chunk_length = 30, output_chunk_length = 25)
NLinear.fit(train, epochs = 100, verbose = True)
pred_NLinear = NLinear.predict(24)
pred_NLinear.to_csv('NLinear_24.csv', encoding = 'utf-8-sig')
files.download('NLinear_24.csv')

DLinear = DLinearModel(input_chunk_length = 30, output_chunk_length = 25)
DLinear.fit(train, epochs = 100, verbose = True)
pred_DLinear = DLinear.predict(24)
pred_DLinear.to_csv('DLinear_24.csv', encoding = 'utf-8-sig')
files.download('DLinear_24.csv')