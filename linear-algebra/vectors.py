from typing import List
import math

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """Add corresponding vectors"""
    assert len(v) == len(w), "Vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtract corresponding vectors"""
    assert len(v) == len(w), "Vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding vectors"""
    # Check that all vectors are not empty
    assert vectors, "No vectors provided!"

    # Check that vectors are all the same size
    num_elements = len(vectors[0])
    assert all(
        len(vector) == num_elements for vector in vectors
    ), "All vector must be the same size"

    # The i_th element of result_vector is a sum of every vector[i]
    return [sum(vector[i] for vector in vectors for i in range(num_elements))]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiple every elements by c"""
    return [c * v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Compute the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot(v: Vector, w: Vector) -> Vector:
    """Compute dot product"""
    assert len(v) == len(w), "Vector must be the same length for dot product"
    return [v_i * w_i for v_i, w_i in zip(v, w)]


def sum_of_squared(v: Vector) -> float:
    return dot(v, v)


def magnitude(v: Vector) -> float:
    """Compute magnitude of a vector"""
    return math.sqrt(sum_of_squared(v))


def squared_distance(v: Vector, w: Vector) -> float:
    """Compute squared distances between 2 vectors
    Assume that:
        v = (v_1  v_2  ...  v_n)
        w = (w_1  w_2  ...  w_n)
    Squared distance between 2 vectors is computed as below:
        squared_distance = (v_1 - w_1)**2 + (v_2 - w_2)**2 +... (v_n - w_n)**2
    """
    return sum_of_squared(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    """Compute distances between 2 vectors
    Assume that:
        v = (v_1  v_2  ...  v_n)
        w = (w_1  w_2  ...  w_n)
    Distance between 2 vectors is computed as below:
    distance = math.sqrt((v_1 - w_1)**2 + (v_2 - w_2)**2 +...+ (v_n - w_n)**2)
    """
    return math.sqrt(squared_distance(v, w))
