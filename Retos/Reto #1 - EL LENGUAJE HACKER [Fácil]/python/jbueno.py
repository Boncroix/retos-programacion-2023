'''
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
'''

traductor = {
    "a" : "4",
    "b" : "I3",
    "c" : "[",
    "d" : ")",
    "e" : "3",
    "f" : "|=",
    "g" : "&",
    "h" : "#",
    "i" : "1",
    "j" : ",_|",
    "k" : ">|",
    "l" : "1",
    "m" : "/\\/\\",
    "n" : "^/",
    "ñ" : "^/~",
    "o" : "0",
    "p" : "|*",
    "q" : "(_,)",
    "r" : "I2",
    "s" : "5",
    "t" : "7",
    "u" : "(_)",
    "v" : "\\/",
    "w" : "\\/\\/",
    "x" : "><",
    "y" : "j",
    "z" : "2",
    "1" : "l",
    "2" : "R",
    "3" : "mi",
    "4" : "A",
    "5" : "S",
    "6" : "b",
    "7" : "t",
    "8" : "B",
    "9" : "gramo",
    "0" : "oh",
}


text = str(input("Introduzca el texto que quiere traducir: ").lower())
text1 = ''
for i in text:
    if i in traductor:
        char = traductor[i]
    else:
        print(f'{i} no se encuentra en diccionario')
    text1 += char  

print (text1)