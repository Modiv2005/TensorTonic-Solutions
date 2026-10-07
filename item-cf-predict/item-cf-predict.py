def item_cf_predict(user_ratings: list, item_similarities: list, target: int) -> float:
    """
    Returns the similarity-weighted rating prediction.
    """
    weighted_sum = 0.0
    similarity_sum = 0.0

    for i in range(len(user_ratings)):
        # Skip the target item
        if i == target:
            continue

        # Include only rated items with positive similarity
        if user_ratings[i] > 0 and item_similarities[i] > 0:
            weighted_sum += item_similarities[i] * user_ratings[i]
            similarity_sum += item_similarities[i]

    # No qualifying items
    if similarity_sum == 0:
        return 0.0

    return float(weighted_sum / similarity_sum)