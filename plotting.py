import matplotlib.pyplot as plt

def plot_metrics(metrics: dict):
    """
    Plots a metrics dictionary. A metrics dictionary should have these keys:

    metrics["train_losses"] = []\n
    metrics["train_accuracies"] = []\n
    metrics["test_losses"] = []\n
    metrics["test_accuracies"] = []\n
    """

    x = range(0, len(metrics["train_losses"]))

    plt.figure(figsize=(15, 6))

    # This code is fucknig awesome
    i = 1
    if "train_losses" in metrics:
        plt.subplot(2, 1, i)
        plt.title("Loss")
        plt.plot(x, metrics["train_losses"], label="Train Losses")
        plt.plot(x, metrics["test_losses"], label="Test Losses")
        plt.legend()
        i += 1

    if "train_accuracies" in metrics:
        plt.subplot(2, 1, i)
        plt.title("Accuracy")
        plt.plot(x, metrics["train_accuracies"], label="Train Accuracies")
        plt.plot(x, metrics["test_accuracies"], label="Test Accuracies")
        plt.legend()
        i += 1
    plt.show()