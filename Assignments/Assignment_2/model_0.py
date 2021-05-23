import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures


class BatchGradientDescent:
    converge_condition = 0.0001

    def __init__(self, x, y, learning_rate, number_of_iteration=None, init_theta=None):
        """
        :param x: columns of independent variable
        :param y: one column of dependent variable
        :param learning_rate: the scalar multiplied with the gradient every step
        :param number_of_iteration: if not specified the break condition is convergence
        :param init_theta: initial arguments, default value is a column of zeros
        """
        self.x = x
        self.y = y
        self.lr = learning_rate
        self.ni = number_of_iteration
        self.theta = init_theta if init_theta else np.array([0] * x.shape[1]).reshape([x.shape[1], 1])
        self.history = [
            (
                self.theta.flatten(),
                self.gradient().flatten(),
                self.cost()
            )
        ]
        self.epoch = 0

    def forecast(self):
        return np.dot(self.x, self.theta)

    def cost(self):
        return np.mean((self.forecast() - self.y) ** 2)

    def test(self, x, y):
        return np.mean((np.dot(x, self.theta) - y) ** 2)

    def gradient(self):
        error = self.forecast() - self.y
        tile_error = np.tile(error, self.theta.shape[0])
        return np.mean(2 * tile_error * self.x, axis=0)

    def train(self):
        while True:
            # Compute gradient
            grad = self.gradient()
            grad = grad.reshape(-1, 1)
            # Update parameters
            self.theta = self.theta - self.lr * grad.reshape(-1, 1)
            # Calculate the loss
            loss = self.cost()
            # Decide break
            if self.ni:
                if self.epoch == self.ni:
                    break
            else:
                if self.history[-1][-1]-loss <= self.converge_condition:
                    break
            self.epoch += 1
            # Store the parameter, the gradient, the loss
            self.history.append((self.theta.flatten(), self.gradient().flatten(), loss))
        return self.history

    def plot_loss_history(self):
        plt.plot(
            [i for i in range(self.epoch + 1)],
            [line[2] for line in self.history]
        )
        plt.xlabel("number of iteration")
        plt.ylabel("loss")
        plt.show()

    @property
    def loss_history(self):
        return [line[2] for line in self.history]

    @property
    def loss_final(self):
        return self.history[-1][2]

    @property
    def theta_final(self):
        return self.theta


def k_fold(x, y, k, lr, ni):
    """
    :param x: original dataset independent variables
    :param y: original dataset dependent variable
    :param k: number of slice
    :param ni: number of iteration
    :param lr: learning rate
    :return: performance on train set, performance on test set
    """
    length_of_test = int(x.shape[0]/k)
    x_slices = [x[i*length_of_test: (i+1)*length_of_test-1, :] for i in range(k)]
    y_slices = [y[i*length_of_test: (i+1)*length_of_test-1, :] for i in range(k)]
    performance_train = []
    performance_test = []
    for i in range(k):
        x_test = x_slices[i]
        y_test = y_slices[i]
        # vertical concatenate
        x_train = np.concatenate([x_slices[j] for j in range(k) if j != i], axis=0)
        y_train = np.concatenate([y_slices[j] for j in range(k) if j != i], axis=0)

        model = BatchGradientDescent(x_train, y_train, lr, ni)
        model.train()

        performance_train.append(model.loss_final)
        performance_test.append(model.test(x_test, y_test))

        print(k_fold, f"fold {i} finished, {k} in total")
    return np.mean(performance_train), np.mean(performance_test)


def k_fold_validation(x, y, k, lr, ni):
    train_performances = []
    test_performances = []
    for n in range(10, ni, 10):
        train_p, test_p = k_fold(x, y, k, lr, n)
        train_performances.append(train_p)
        test_performances.append(test_p)

    axis = [i for i in range(10, 100, 10)]
    plt.plot(
        axis,
        train_performances,
        label="performance on train set"
    )
    plt.plot(
        axis,
        test_performances,
        label="performance on test set"
    )
    plt.legend()
    plt.xlabel("degree of polynomial")
    plt.ylabel("convergence loss")
    plt.title(f"{k}-Fold Cross Validation at different number of iteration")
    plt.show()
    return train_performances, test_performances
