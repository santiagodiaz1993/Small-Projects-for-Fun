#!/usr/bin/env python
# coding=utf-8
""" implementing support vector machine from scratch """

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")


class SupportVectorMachine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.colors = {1: "r", -1: "b"}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1, 1, 1)

    def fit(self, data):
        self.data = data
        # { ||w||: [w, b]}
        opt_dict = {}
        transform = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)
        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None

        # support vectors yi(xi,w+b) = 1
        step_sizes = [
            self.max_feature_value * 0.1,
            self.max_feature_value * 0.01,
            # this is the point where it starts to become very
            # expensive
            self.max_feature_value * 0.001,
        ]

        # this one is extremely expensive
        b_range_multiple = 5
        b_multiple = 5
        latest_optimum = self.max_feature_value * 10

        for step in step_sizes:
            w = np.array([latest_optimum, latest_optimum])
            # we can do this because convex
            optimized = False
            while not optimized:
                for b in np.arrange(
                    -1 * (self.max_feature_value * b_range_multiple),
                    self.max_feature_value * b_range_multiple,
                    step * b_multiple,
                ):
                    for transformation in transform:
                        w_t = w * transformation
                        found_options = True
                        # weakest link in the SCM findamentally SMO attempts
                        # to fix this a bit
                        # yi(xi.w + b) >= 1
                        for i in self.data:
                            for xi in self.data[i]:
                                yi = i
                                if not yi * (np.dot(w_t, xi) + b) >= 1:
                                    found_options = False
                    if found_options:
                        opt_dict[np.linalg.norm(w_t)] = [w_t, b]

            if w[0] < 0:
                optimized = True
                print("Optimized a step")
            else:
                w = w - step

    norms = sorted([n for n in opt_dict])
    # ||w|| : [w, b]
    opt_choice = opt_dict(norms[0])
    self.w = opt_choice[0]
    self.b = opt_choice[1]
    latest_optimum = opt_choice[0][0] + step * 2

    def predict(self, features):
        # sign( x.w+b)
        classfication = np.sign(np.dot(np.array(features), self.w) + self.b)
        return classfication


data_dict = {
    -1: np.array([[1, 7], [2, 8], [3, 8]]),
    1: np.array([5, 1], [6, -1], [7, 3]),
}
