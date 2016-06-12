__author__ = 'pridemai'

class KnapsackData:
    def __init__(self, pname, weeks, profit):
        self.project_name = pname
        self.weeks=weeks
        self.profit = profit
f = open("KnapsackData1.txt").read()
data = [KnapsackData(l.split(" ")[0], int(l.split(" ")[1]), int(l.split(" ")[2])) for l in f.split("\r\n")]
# _max_weight = None
# _number_of_items = 0
# _list_of_weights = []
# _list_of_values =[]


# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(max_weight, object_weights, object_values, number_of_objects):

    K = [[0 for w in range(max_weight+1)] for j in range(number_of_objects+1)]
    # for j in range(1, number_of_objects):
    #     for w in range(1, max_weight):
    #         if object_weights[j] > max_weight:
    #             K[w][j]=K[w][j-1]
    #         else:
    #             K[w][j]= max(K[w-object_weights[j]][j-1]+object_values[j],K[w][j-1])
    # # #
    # Build table K[][] in bottom up manner
    for j in range(number_of_objects+1):
        for w in range(max_weight+1):
            if j==0 or w==0:
                K[j][w] = 0
            elif object_weights[j-1] <= w:
                K[j][w] = max(object_values[j-1] + K[j-1][w-object_weights[j-1]],  K[j-1][w])
            else:
                K[j][w] = K[j-1][w]
    #
    # return K[number_of_objects][max_weight]
    return K[number_of_objects][max_weight]
# Driver program to test above function
object_values =[30,14,16,9]
object_weights =  [6,3,4,2]
max_weight = 10
n = len(object_values)
print(knapSack(max_weight,object_weights,object_values, n))

# # data = [3,2,3,8,13,10,12,5]
# longest_sequence=[]
# data= "zebras"
# class ReccuranceCharacter:
#     def __init__(self, value, score, previous):
#         self.value = value
#         self.score = score
#         self.previous = previous
#     def __unicode__(self):
#         return ""
# _max_score = 1
#
# _max_pos = 0
# _max_val = None
# index =1
# # while index < len(data):
# d= {}
# i = 0
#
# while i < len(data):
#     if i == 0:
#         d[index] = ReccuranceCharacter(data[i], 1, -1)
#         # longest_sequence.append(ReccuranceCharacter(data[i], 1,-1))
#         # _max_val=data[i]
#         # _max_pos = i
#         i = i+1
#     else:
#         pass
#         j = i
#         has_place = False
#
#         #see if it's greater than the last one
        # if True:
        #     #if it's not, iterate through to see where it belongs
        #     j = i
        #     has_place = False
        #     while j > 0:
        #         if data[i] >= data[j-1]:
        #             if data[i] > _max_val and _max_val > data[j-1]:
        #                 print "first piece hit"
        #                 has_place=True
        #                 j = j-1
        #                 longest_sequence.append(ReccuranceCharacter(data[i],longest_sequence[_max_pos].score+1,longest_sequence[_max_pos].previous+1 ))
        #                 _max_val=data[i]
        #                 _max_pos = i
        #                 break
        #             elif data[i] > _max_val:
        #                 print "middle piece hit"
        #                 has_place=True
        #                 _max_val=data[i]
        #                 _max_pos = i
        #                 longest_sequence.append(ReccuranceCharacter(data[i],longest_sequence[j-1].score+1,1 if longest_sequence[j-1].previous == -1 else longest_sequence[j-1].previous+1 ))
        #                 break
        #             elif data[i] > data[j-1]:
        #                 has_place=True
        #                 longest_sequence.append(ReccuranceCharacter(data[i],longest_sequence[j-1].score+1,1 if longest_sequence[j-1].previous == -1 else longest_sequence[j-1].previous+1 ))
        #                 break
        #         else:
        #             j = j-1
        #     if not has_place:
        #         longest_sequence.append(ReccuranceCharacter(data[i], 1, -1))
        # else:
        #     #if it's not, iterate through to see where it belongs
        #     j = i
        #     has_place = False
        #     while j > 0:
        #         if data[i] >= data[j-1]:
        #             if data[i] > _max_val and _max_val > data[j-1]:
        #                 j = j-1
        #                 _max_val=data[i]
        #                 _max_pos = i
        #
        #             elif data[i] > _max_val or data[i] > data[j-1]:
        #                 has_place=True
        #                 longest_sequence.append(ReccuranceCharacter(data[i],longest_sequence[j-1].score+1,longest_sequence[j-1].previous+1 ))
        #                 break
        #
        #         else:
        #             j = j-1
        #     if not has_place:
        #         longest_sequence.append(ReccuranceCharacter(data[i], 1, -1))
        # i = i+1
print ""
# for c in data:
#     #base case
#     if index==0:
#         longest_sequence.append(ReccuranceCharacter(c, 1, -1))
#         _max_val = c
#         _max_pos=index
#         index = index+1
#     else:
#         if c > longest_sequence[index-1].value:
#             if c > _max_val:
#                 longest_sequence.append(ReccuranceCharacter(c, longest_sequence[_max_pos].score+1, _max_pos))
#                 _max_val = c
#                 _max_pos=index
#             else:
#                 i = index
#                 has_previous = False
#                 while i > 0:
#                     if c < longest_sequence[i -1].value:
#                         longest_sequence.append(ReccuranceCharacter(c, longest_sequence[i -1].score+1, longest_sequence[i -1].previous+1))
#                         has_previous = True
#                         break
#                     else:
#                         i = i-1
#                 if not has_previous:
#                     longest_sequence.append(ReccuranceCharacter(c, 1,-1))
#
#             index = index+1
#             # longest_sequence.append(ReccuranceCharacter(c, longest_sequence[i -1].score+1, longest_sequence[index -1].previous+1))
#             pass
#         else:
#             i = index
#             has_previous = False
#             while i > 0:
#                 if c > longest_sequence[i -1].value:
#                     longest_sequence.append(ReccuranceCharacter(c, longest_sequence[i -1].score+1, longest_sequence[i -1].previous+1))
#                     has_previous = True
#                     break
#                 else:
#                     i = i-1
#             if not has_previous:
#                 longest_sequence.append(ReccuranceCharacter(c, 1,-1))
#
#             index = index+1        # if c < longest_sequence[index-1].value:
        #     i = index
        #     has_previous = False
        #     while i > 0:
        #         if c > longest_sequence[i -1].value:
        #             longest_sequence.append(ReccuranceCharacter(c, longest_sequence[i -1].score+1, longest_sequence[i -1].previous+1))
        #             has_previous = True
        #             break
        #         else:
        #             i = i-1
        #     if not has_previous:
        #         longest_sequence.append(ReccuranceCharacter(c, 1,-1))
        # else:
        #     if c > _max_val:
        #         i  = index
        #         longest_sequence.append(ReccuranceCharacter(c, longest_sequence[_max_pos].score+1, _max_pos))
        #         _max_pos = index
        #         _max_val = c
        #     else:
        #         longest_sequence.append(ReccuranceCharacter(c, longest_sequence[index-1].score+1,longest_sequence[index-1].previous+1 if longest_sequence[index-1].previous > -1 else longest_sequence[index-1].previous+2))
        # index = index+1



print ""

# values=[]
# scores = []
# prevs = []
# index = 0
# for c in data:
#     # #go over it once
#     if len(longest_sequence) == 0 :
#         longest_sequence.append(ReccuranceCharacter(c, 1, -1))
#         index = index+1
#     else:
#         if c >= longest_sequence[index-1].value:
#             longest_sequence.append(ReccuranceCharacter(c, longest_sequence[index-1].score+1, longest_sequence[index-1].score))
#
#         else:
#             i = index
#             has_previous = False
#             while i > 0 :
#                 if c > data[i-1]:
#
#                     longest_sequence.append(ReccuranceCharacter(c, longest_sequence[i].score,longest_sequence[index-1].previous))
#                     has_previous = True
#                     break
#                 else:
#                      i = i -1
#             if not has_previous:
#                 longest_sequence.append(ReccuranceCharacter(c, 1, -1))
#             index = index+1
#             pass
#     #         longest_sequence.append(ReccuranceCharacter(c, longest_sequence[index-1].score+1, longest_sequence[index-1].score))
#     #         index = index+1
#     #     else:
#
# highest_score = 1
# highest_score_index = i = 0
# for l in longest_sequence:
#     if l.score >= highest_score:
#         highest_score = l.score
#         highest_score_index = i
#     i = i+1
# longest_sequence[highest_score_index].previous =longest_sequence[highest_score_index].score
#
#
# i = longest_sequence[highest_score_index].previous
# s = " "+str(longest_sequence[highest_score_index].value)+" "
# while i  > 0:
#     s = s+" "+str(longest_sequence[i].value)+" "
#     i= longest_sequence[i].previous
#
# print s
#
# final = [None]*len(longest_sequence)

#
# # while i < len(longest_sequence):
# for rc in longest_sequence:
#     if (final[rc.score-1] is None) or (final[rc.score-1].value < rc.value ):
#         final[rc.score-1] = rc
#         i = i+1




# print ''.join(longest_sequence)