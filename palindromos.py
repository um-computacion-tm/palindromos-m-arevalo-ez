def palindromo(cadena):
    
    if cadena[0] == cadena[-1]:
        x = 1
        x += 1
        if x == 2:
            return "YES"
        else:
            palindromo(cadena[1:-2:])
    else:
        return "NO"

if __name__ == "__main__":
    input()