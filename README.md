## This is a Hackerrank medium level problem
---------------------------------------------
## Problem statement
---------------------
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:
* floor((L)^1/2)<=row<=column<=ceil((L)^1/2)

For example, the sentence 
* s = if a man was ment to stay on the ground god would have given us roots

after removing spaces is 54 characters long. (54)^1/2 is between 7 and 8, so it is written in the form of a grid with 7 rows and 8 columns.

* ifmanwas  
* meanttos          
* tayonthe  
* groundgo  
* dwouldha  
* vegivenu  
* sroots

If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. rows X columns .
The encoded message is obtained by displaying the characters in a column, inserting a space, and then displaying the next column and inserting a space, and so on. For example, the encoded message for the above rectangle is:

* imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

You will be given a message to encode and print.