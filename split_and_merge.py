import cv2
import cv2_imshow  # Usar cv2_imshow en lugar de cv2.imshow para mostrar imágenes
import numpy as np

def split(image, min_size, threshold):
    """Divide la imagen en regiones más pequeñas si la varianza supera un umbral."""
    M, N = image.shape
    if M <= min_size or N <= min_size:
        return [image]
    elif np.var(image) > threshold:
        return (
            split(image[:M // 2, :N // 2], min_size, threshold) +
            split(image[:M // 2, N // 2:], min_size, threshold) +
            split(image[M // 2:, :N // 2], min_size, threshold) +
            split(image[M // 2:, N // 2:], min_size, threshold)
        )
    else:
        return [image]

def merge(regions):
    """Fusiona regiones adyacentes si son suficientemente similares (este es un ejemplo simplificado)."""
    # En este ejemplo, simplemente devolvemos las regiones originales sin fusionarlas.
    return regions  # Esto es solo un placeholder

def split_and_merge(image_path, min_size, threshold):
    image = cv2.imread(image_path, 0)  # Carga la imagen en escala de grises
    if image is None:
        print("Error: no se pudo cargar la imagen desde", image_path)
        return

    # Aplicar el método Split and Merge
    split_regions = split(image, min_size, threshold)
    merged_regions = merge(split_regions)

    # Visualizar las regiones resultantes
    result = np.zeros_like(image)
    #for i, region in enumerate(merged_regions):
    #    result[np.where(region > 0)] = i * 30  # Asignar un valor de intensidad diferente a cada región

    cv2_imshow(image)  # Usar cv2_imshow en lugar de cv2.imshow
    cv2_imshow(result)  # Usar cv2_imshow en lugar de cv2.imshow

# Parámetros
image_path = 'data/capi.jpg'  # Cambia esto por la ruta a tu imagen
min_size = 5  # Mínimo tamaño de la región
threshold = 20  # Umbral para la varianza

# Ejecutar el algoritmo
split_and_merge(image_path, min_size, threshold)