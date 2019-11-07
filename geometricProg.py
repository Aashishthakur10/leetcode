def isGeometricProgression(sequence):
    mult = sequence[0]/sequence[1]
    for i in range(1, len(sequence)-1):
        if sequence[i]/sequence[i+1] != mult:
            return False

    return True

if __name__ == '__main__':
    print(isGeometricProgression([27, 9, 3, 1]))