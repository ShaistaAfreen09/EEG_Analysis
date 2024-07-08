# eegnet_classification.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, DepthwiseConv2D, BatchNormalization, Activation, Dropout, Flatten, Dense
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def EEGNet(input_shape, num_classes):
    model = Sequential([
        Conv2D(16, (1, 51), padding='same', input_shape=input_shape),
        BatchNormalization(),
        Activation('elu'),
        DepthwiseConv2D((2, 1), padding='valid'),
        BatchNormalization(),
        Activation('elu'),
        Dropout(0.25),
        Flatten(),
        Dense(num_classes, activation='softmax')
    ])
    return model

def evaluate_model(model, test_data, test_labels):
    predictions = model.predict(test_data)
    y_pred = np.argmax(predictions, axis=1)
    accuracy = accuracy_score(test_labels, y_pred)
    precision = precision_score(test_labels, y_pred, average='weighted')
    recall = recall_score(test_labels, y_pred, average='weighted')
    f1 = f1_score(test_labels, y_pred, average='weighted')
    
    return accuracy, precision, recall, f1

# Example usage
if __name__ == "__main__":
    input_shape = (64, 100, 1)  # Example input shape
    num_classes = 2  # Example number of classes
    
    model = EEGNet(input_shape, num_classes)
    model.summary()
