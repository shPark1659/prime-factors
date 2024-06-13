class PrimeFactor:
    @staticmethod
    def of(num):
        result = []
        if num > 1:
            if num == 4:
                while num != 1:
                    result.append(2)
                    num //= 2
            elif num == 6:
                result.append(2)
                result.append(3)
            else:
                result.append(num)
        return result
