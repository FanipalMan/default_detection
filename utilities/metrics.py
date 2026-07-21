
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (fbeta_score, confusion_matrix, average_precision_score, 
                             classification_report)


def calculate_f2_score(y_true, y_pred):
    return fbeta_score(y_true, y_pred, beta=2)

def calculate_average_precision(y_true, y_pred):
    return average_precision_score(y_true, y_pred)

def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        cm, 
        annot=True, 
        fmt='d', 
        cmap='Blues', 
        xticklabels=['Predicted Negative', 'Predicted Positive'], 
        yticklabels=['Actual Negative', 'Actual Positive']
    )
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()

def evaluate_model(y_true, y_pred):
    f2 = calculate_f2_score(y_true, y_pred)
    avg_precision = calculate_average_precision(y_true, y_pred)

    print(f"F2 Score: {f2:.4f}")
    print(f"Average Precision: {avg_precision:.4f}")

    print(classification_report(y_true, y_pred))

    plot_confusion_matrix(y_true, y_pred)