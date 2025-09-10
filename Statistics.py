class Statistics:
    @staticmethod
    def mean(data):
        return sum(data) / len(data)

    @staticmethod
    def median(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    @staticmethod
    def variance(data, sample=False):
        mean_val = Statistics.mean(data)
        squared_diffs = [(x - mean_val) ** 2 for x in data]

        if sample:
            return sum(squared_diffs) / (len(data) - 1)
        else:
            return sum(squared_diffs) / len(data)
