import math

def sobel_edges(image: list) -> list:
    """
    Returns the zero-padded Sobel gradient magnitude at every pixel.
    """
    Kx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]

    Ky = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]

    rows = len(image)
    cols = len(image[0])

    # Create zero-padded image
    padded = [[0] * (cols + 2) for _ in range(rows + 2)]

    for i in range(rows):
        for j in range(cols):
            padded[i + 1][j + 1] = image[i][j]

    result = [[0.0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            gx = 0
            gy = 0

            for a in range(3):
                for b in range(3):
                    pixel = padded[i + a][j + b]
                    gx += Kx[a][b] * pixel
                    gy += Ky[a][b] * pixel

            result[i][j] = math.sqrt(gx * gx + gy * gy)

    return result