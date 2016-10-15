
def edit_distance3(str1, str2):
    ed_table = [[None for j in range(len(str2)+1)]
                for i in range(len(str1)+1)]

    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):

            if i == 0:
                ed_table[i][j] = j

            elif j == 0:
                ed_table[i][j] = i

            elif str1[i-1] == str2[j-1]:
                ed_table[i][j] = ed_table[i-1][j-1]

            else:
                ed_table[i][j] = 1 + min(
                    ed_table[i-1][j-1],
                    ed_table[i][j-1],
                    ed_table[i-1][j],
                )
    return ed_table[-1][-1]
