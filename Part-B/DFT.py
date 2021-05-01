import ctypes
import numpy as np

library = ctypes.CDLL('./dft3.so')

library.connect()

x = np.array([0.0,
0.0006713867,
0.001373291,
0.0020751953,
0.0027770996,
0.0034484863,
0.0041503906,
0.004852295,
0.005554199,
0.0062561035,
0.0069274902,
0.0076293945,
0.008331299,
0.009033203,
0.00970459,
0.010406494,
0.011108398,
0.011779785,
0.012481689,
0.013183594,
0.0138549805,
0.014556885,
0.015258789,
0.015930176,
0.01663208,
0.017303467,
0.018005371,
0.018707275,
0.019378662,
0.020080566,
0.020751953,
0.021453857])
y = x.astype(complex)
# x= complex(4,3)
z = library.DFT(y)
# y =  library.addition(5,2)
print(z)
