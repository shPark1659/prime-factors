class PrimeFactor:
    @staticmethod
    def of(num):
        result = []
        if num > 1:
            if num == 4:
                result.append(2)
                result.append(2)
            else:
                result.append(num)
        return result
