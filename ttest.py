import version5.support_functions as psf

elements_number = 4
weights = []  # Initial weights for the first two elements

# The function we are testing
def get_valid_weight(file, weights: list, elements_number: int, current_index: int) -> float:

    if current_index == elements_number - 1:
        remaining_weight = round(1 - sum(weights), 2)
        print(f"Assigning remaining weight of {remaining_weight} to {file}.")
        return remaining_weight

    else :
        remaining_stocks = elements_number - len(weights)
        while True:
            weight = psf.get_percentage(f"Weight of {file}: ")
            total_weight = round(sum(weights) + weight, 2)
            
            if total_weight >= 1:
                print(f"The last :{remaining_stocks} stocks in portfolio, can not have 0.00 percente.")
                print("Please Try again")
                continue
            else:
                return weight
        
# Loop through the elements to assign valid weights
for i in range(elements_number):  # Starts from index 2 (as you already have 0.4 and 0.2)
    file_name = f"Stock {i + 1}"  # Dynamically create stock name
    current_index = i  # Set current index
    
    # Run the function and get the valid weight
    weight = get_valid_weight(file_name, weights, elements_number, current_index)
    
    if weight is None:
        print("Please restart the process and ensure the total weight is 1.")
        break  # Break the loop if the last stock's weight cannot be assigned
    
    # Append the weight to the list
    weights.append(weight)

    print(f"Final valid weight for {file_name}: {weight}")

# Final result
print(f"All weights: {weights}")
