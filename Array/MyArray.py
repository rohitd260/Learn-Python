#import the array module
import array as arr

#try ro create the array without array module
another_arr = [1,2,3]
print(type(another_arr))  #print type as list

#created the array with array modules
create_arr = arr.array('i',[1,2,3])
print(type(create_arr))  #print type as array hence imported assay module
