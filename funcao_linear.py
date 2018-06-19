import tensorflow as tf


def gerar_pesos(n_features, n_labels):
    """ Gera tensor de pesos com valores aleatórios

    Parâmetros
    ----------
    n_features: número de atributos
    n_labels: número de rótulos

    Retorna
    -------
    w: Tensor de pesos
    """
    # TODO: Retornar pesos
    w = tf.Variable(tf.truncated_normal((n_features, n_labels)))
    return w

def gerar_vies(n_labels):
    """ Gera tensor de vieses preenchido com zeros

    Parâmetros
    ----------
    n_labels: número de rótulos
    
    Retorna
    -------
    b: tensor de vieses
    """
    # TODO: Retornar vieses
    b = tf.Variable(tf.zeros(n_labels))
    return b

def linear(x, w, b):
    """ Calcula a função linear

    Parâmetros
    ----------
    x: tensor com valores de entrada
    w: tensor de pesos
    b: tensor de vieses

    Retorna
    -------
    linear: função linear
    """
    # TODO: Linear Function (xW + b)
    linear = tf.add(tf.matmul(x, w), b)
    return linear
