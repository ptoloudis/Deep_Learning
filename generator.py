import random

def generate_negative_samples(user_interactions, num_negatives):
    """
    Generate negative samples for each user in the testing set.
    Args:
    user_interactions (dict): Dictionary containing user-item interactions.
    num_negatives (int): Number of negative samples to generate per user.
    Returns:
    dict: Dictionary containing user IDs as keys and lists of negative item IDs as values.
    """

    negative_samples = {}
    for user in user_interactions:
        items = user_interactions[user]
        negatives = []
        # Generate negative samples
        while len(negatives) < num_negatives:
            item = random.randint(1, num_items) # Randomly select an item
            if item not in items and item not in negatives:
                negatives.append(item)
        negative_samples[user] = negatives

    return negative_samples

def save_negative_samples(negative_samples, filename):
    """
    Save negative samples to a file.
    Args:
    negative_samples (dict): Dictionary containing user IDs as keys and lists of negative item IDs as values.
    filename (str): Name of the file to save the negative samples.
    """
    with open(filename, 'w') as file:
        for user, negatives in negative_samples.items():
            line = f"{user} {' '.join(map(str, negatives))}\n"
            file.write(line)


# Read the MovieLens dataset and create user-item interactions

user_interactions = {}

num_items = 1682 # Number of items in the MovieLens dataset
with open('u.data', 'r') as file:

 for line in file:
    user, item, _, _ = line.strip().split('\t')
    user = int(user)
    item = int(item)

    if user not in user_interactions:
        user_interactions[user] = []
    user_interactions[user].append(item)

# Generate negative samples for each user in the testing set

num_negatives = 100 # Number of negative samples per user

negative_samples = generate_negative_samples(user_interactions, num_negatives)

# Save the negative samples to a file

save_negative_samples(negative_samples, 'u.data.negative')