import numpy as np
import matplotlib.pyplot as plt

from neupy import algorithms


plt.style.use('ggplot')

np.random.seed(0)

input_train = np.reshape(np.linspace(0, 2 * np.pi, 100), (100, 1))
input_test = np.reshape(np.sort(2 * np.pi * np.random.random(50)), (50, 1))

target_train = np.sin(input_train)
target_test = np.sin(input_test)

cmac = algorithms.CMAC(
    quantization=100,
    associative_unit_size=10,
    step=0.2,
    verbose=True,
    show_epoch='4 times'
)
cmac.train(input_train, target_train, epochs=100)
predicted_test = cmac.predict(input_test)

plt.plot(input_train, target_train)
plt.plot(input_test, predicted_test)
plt.show()