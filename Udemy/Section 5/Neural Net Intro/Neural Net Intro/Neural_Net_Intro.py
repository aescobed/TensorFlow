
import tensorflow as tf

# Using the estimator API 



# Using only one feature in the feature column

feature_cols = [tf.feature_column.numeric_column('x', shape=[1])]

estimator = tf.estimator.LinearRegressor(feature_columns=feature_cols)




x_train, x_eval, y_train, y_eval = train_test_split(x_data, t_true, test_size=0.3, random_state=101)

print(x_train.shape)
