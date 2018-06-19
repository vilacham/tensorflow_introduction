def batches(size, features, labels):
	""" Cria mini-lotes de atributos e rótulos

	Parâmetros
	----------
	size: Tamanho do mini-lote
	features: Lista de atributos
	labels: Lista de rótulos

	Retorna
	-------
	batches: Mini-lotes de (features, labels)
	"""
	# Garante que features e labels são compatíveis
	assert len(features) == len(labels)

	# Cria lista vazia para armazenar mini-lotes
	batches = []

	# Preenche a lista com mini-lotes
	for i in range(0, len(features), size):
		batch = [features[i:i + size], labels[i:i + size]]
		batches.append(batch)

	# Retorna lista de mini-lotes
	return batches