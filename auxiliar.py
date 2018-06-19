from tensorflow.examples.tutorials.mnist import input_data

def mnist_features_labels(n_labels):
    """ Obtem os primeiros <n> exemplos do MNIST

    Parâmetros
    ----------
    n_labels: números de rótulos

    Retorna
    -------
    mnist_features: lista de atributos
    mnist_labels: lista de rótulos
    """
    mnist_features = []
    mnist_labels = []
    mnist = input_data.read_data_sets('/datasets/ud730/mnist', one_hot=True)

    # Para garantir que o código seja executado mais rápido no
    # notebook, vamos obter apenas 10000 imagens
    for mnist_feature, mnist_label in zip(*mnist.train.next_batch(10000)):
        # Adiciona atributos e rótulos se eles estiverem nas 
        # primeiras <n> classes
        if mnist_label[:n_labels].any():
            mnist_features.append(mnist_feature)
            mnist_labels.append(mnist_label[:n_labels])

    return mnist_features, mnist_labels
