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

    plt.subplot(2, 1, 1)
    plt.title("Loss")
    plt.plot(x, metrics["train_losses"], label="Train Losses")
    plt.plot(x, metrics["test_losses"], label="Test Losses")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.title("Accuracy")
    plt.plot(x, metrics["train_accuracies"], label="Train Accuracies")
    plt.plot(x, metrics["test_accuracies"], label="Test Accuracies")
    plt.legend()

    plt.show()