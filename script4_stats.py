def get_client_stats(amounts):
    if len(amounts) == 0:
        print("No data provided")
        return
    # yahan se normal code chalega
    total = sum(amounts)
    average = total / len(amounts)
    return total, average
result = get_client_stats([1000, 2000, 3000])
print(result)
result2 = get_client_stats([])
print(result2)