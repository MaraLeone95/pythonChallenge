
alphabet1 = "abcdefghijklmnopqrstuvwxyz .'()://" #future dictionary keys
alphabet2 = "cdefghijklmnopqrstuvwxyzab .'()://" #future dictionary values

#the text I want to translate
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "map.html"

#First way
#returns a transposed string
def transpose_alphabet(str):
    alphabets = dict(zip(alphabet1, alphabet2)) #returns a dictionary with corresponding elements from two strings
    newstr = ""
    for l in str:
        l = alphabets[l]
        newstr += l
    return newstr

solution1 = transpose_alphabet(text)
print("The translation using the first way is: ", solution1)


#Second way
#creates a mapping between the elements in the two alphabets
new_corr_dict = url.maketrans(alphabet1, alphabet2)

#translates the string according to the new mapping
newstr = url.translate(new_corr_dict)
print("The solution to the 1st level using the second way is: ", newstr)



