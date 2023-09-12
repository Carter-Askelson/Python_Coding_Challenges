import array
from collections import deque
from heapq import heapify, heappop
import random
import time
import timeit

""" 
#Array
new_array = array.array('i', (0, 4, 5, 1))
print("Array")
print(new_array)
print()

#List
new_list = ["Lauren", "Gracie", "Gwen"]
print("List")
print(new_list)
print()

#Stack
new_stack = deque(["Whitney", "Tyra"])
print("Stack")
print(new_stack)
print(new_stack.pop())
print(new_stack)
print()

#Queue
new_queue = deque(["Greg", "Susie"])
print("Queue")
print(new_queue)
print("Adding John and Kim, poping first item")
new_queue.append("John")
new_queue.append("Kim")
print(new_queue.popleft())  
print(new_queue)
print()

#Linked List
new_linked = deque(["Lyra", "Bonbon"])
print("Linked List")
print(new_linked)
print("Adding Carrot Top and Caramel to the front")
new_linked.appendleft("Carrot Top")
new_linked.appendleft("Caramel")
print(new_linked) 
print("Reverse Linked List") 
new_linked.reverse()
print(new_linked)
print("Linked List Rotated 2 to the right")
new_linked.rotate(2)
print(new_linked)
print()
 """
# More traditional way of making a Linked List
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __srt__ (self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)


#Hash Tables
""" new_hash_table = {"old" : "Carter",
                  "medium": "Cameron",
                  "young": "Logan"}
print("Hash Table")
print(new_hash_table)
print("print old value and remove young value")
print(new_hash_table["old"])
del new_hash_table["young"]
print(new_hash_table)
print() """

#Binary Trees
class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def breadth_first_search(self, n):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.key == n:
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next
            next = []
        return False
    
    def invert(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                temp = node.left_child
                node.left_child = node.right_child
                node.right_child = temp
            current = next
            next = []

""" new_tree = BinaryTree(1)
new_tree.insert_left(2)
new_tree.insert_right(3)
new_tree.insert_left(4)
new_tree.left_child.insert_right(6)
new_tree.insert_right(5)
print(new_tree.breadth_first_search(3))
print() """




#Binary Heaps
""" new_heap = ['G', 'S', 'C', 'W', 'L', 'M']
print("List before making it a heap")
print(new_heap)
heapify(new_heap)
print("Heap")
print(new_heap)
print("Heap after popping")
heappop(new_heap)
print(new_heap) """


#Anagram detector

def anagram_detector(word1, word2):
    isAnagram = True
    hashtable = {}
    if word1.length() == word2.length():
        for i in word1.lower():
            hashtable.update({i: i})
        for i in word2.lower():
            if i not in hashtable:
                isAnagram = False
        if isAnagram:
            print(word1 + " and " + word2 + " are anagrams of eachother.")
        else:
            print(word1 + " and " + word2 + " are not anagrams of eachother.")
    else:
        print(word1 + " and " + word2 + " are not anagrams of eachother.")

def palindrome_detector(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if word1 == word2[::-1]:
        return True
    else:
        return False
    
def caesar__cipher_encrypt(uncoded_message, increment_amount = 3):
    result = []
    
    for char in uncoded_message:
        if char.isalpha():
            # Determine whether it's uppercase or lowercase
            is_upper = char.isupper()
            
            # Convert the character to its Unicode code point
            code_point = ord(char)
            
            # Increment the code point by the specified amount
            code_point += increment_amount
            
            # Check for overflow and wrap around if necessary (z -> a or Z -> A)
            if is_upper:
                if code_point > ord('Z'):
                    code_point -= 25
            else:
                if code_point > ord('z'):
                    code_point -= 25   
            
            # Convert the updated code point back to a character
            updated_char = chr(code_point)
            result.append(updated_char)
        else:
            # If the character is not an alphabet character, add it unchanged
            result.append(char)
    
    # Join the characters back together to form the final string
    return ''.join(result)

def caesar_cipher_decrypt(coded_message):
    counter = 0
    print("Encoded Message")
    print(coded_message)
    print()
    print("Manual Scan required to find uncoded Message")
    print("Attempts to break Cipher:")
    
    while counter != 26:
        #Example
        #encoded_message = caesar__cipher_encrypt("Nasus is Susan backwards", random.randint(1, 26))
        #caesar_cipher_decrypt(encoded_message)
        
        result = []
    
        for char in coded_message:
            if char.isalpha():
                # Determine whether it's uppercase or lowercase
                is_upper = char.isupper()
                
                # Convert the character to its Unicode code point
                code_point = ord(char)
                
                # Unincrement the code point by the specified amount
                code_point -= counter
                
                
                # Check for overflow and wrap around if necessary (z -> a or Z -> A)
                if is_upper:
                    if code_point < ord('A'):
                        code_point += 25
                else:
                    if code_point < ord('a'):
                        code_point += 25

                # Convert the updated code point back to a character
                updated_char = chr(code_point)
                result.append(updated_char)
            else:
                # If the character is not an alphabet character, add it unchanged
                result.append(char)
        print("".join(result))
        counter += 1



def duplicate_list_finder(list):
    #example
    #newlist = [1,1,2,2,2,2,2,2,3,3,3,3,3,4]
    #duplicate_list_finder(newlist)      
    duplicate_counter = 0
    hashmap = {}
    for i in list:
        if i not in hashmap:
            hashmap.update({i: 1})
        else:
            duplicate_counter += 1

    print("There are " + str(duplicate_counter) + " duplicates in this list.")


def anagram_generator(word):
    #example
    #anagram_generator("mlp")
    new_word = str(word).lower()
    hashtable = {}
    current_loop = 1
    key_list = []
    value_list = []
    word_length = len(new_word)

    #set up to get proper positions of values to iterate over
    word_length_counter = 0
    current_taken_positions = []
    while word_length_counter < word_length:
        current_taken_positions.append(word_length_counter)
        word_length_counter += 1

    #first round to get values
    position_counter = 0
    for i in new_word:
        hashtable.update({str(current_taken_positions[position_counter]): i})
        position_counter += 1
        
    #adds every single unique anagram to a hashtable
    while current_loop != word_length or word_length == 0:
        #resets the values for each loop 
        key_list.clear()
        value_list.clear()
        
        for i in hashtable.keys():
            if len(i) == current_loop:
                key_list.append(i)
        for i in hashtable.values():
            if len(i) == current_loop:
                value_list.append(i)
        current_loop += 1
        value_position = 0
        
        #goes through the loop to add additional values to the string and checks to see if that combination is in the hashmap or not
        for i in key_list:
            position_counter = 0
            current_value = value_list[value_position] 
            
            for k in new_word:
                
                if str(position_counter) not in i:
                    newkey = i + str(position_counter)
                    
                    if newkey not in hashtable:
                        new_value = current_value + k
                        hashtable.update({newkey: new_value})
                
                position_counter += 1
            value_position += 1
            
    #prints every single unique anagram to the console
    print("All Anagrams possible of: " + word)
    for i in hashtable.values():
            if len(i) == word_length:
                print(i)
    


def zero_sorter(number_list):
    change = True
    while change:
        change = False
        counter = 0
        while counter < len(number_list) - 1:
            if number_list[counter] == 0 and number_list[counter + 1] != 0:
                new_val = number_list[counter + 1]
                number_list[counter + 1] = number_list[counter]
                number_list[counter] = new_val
                change = True
            counter += 1

def fast_zero_sorter(number_list):
    zero_count = 0
    current_len = len(number_list)
    counter = 0
    while counter < current_len:
        if number_list[counter] == 0:
            zero_count += 1
            number_list.pop(counter)
            current_len -= 1
            counter -= 1
        counter += 1

    while zero_count != 0:
        number_list.append(0)
        zero_count -= 1

""" # Measure the execution time with timeit
execution_time_zero_sorter = timeit.timeit(lambda: zero_sorter([0, 1, 2, 3, 5, 0, 0, 0, 5, 4, 4, 698, 1, 6, 5, 0, 0, 0, 60, 1, 0, 0, 1, 2, 3]), number=1)
execution_time_fast_zero_sorter = timeit.timeit(lambda: fast_zero_sorter([0, 1, 2, 3, 5, 0, 0, 0, 5, 4, 4, 698, 1, 6, 5, 0, 0, 0, 60, 1, 0, 0, 1, 2, 3]), number=1)

# Print the execution time in seconds
print(f"zero_sorter Execution time: {execution_time_zero_sorter:.10f} seconds")
print(f"fast_zero_sorter Execution time: {execution_time_fast_zero_sorter:.10f} seconds") """


def fizzbuzz():
    counter = 1
    while counter <= 100:
        if counter % 3 == 0 and counter % 5 == 0:
            print("FizzBuzz")
        elif counter % 3 == 0:
            print("Fizz")
        elif counter % 5 == 0:
            print("Buzz")
        else:
            print(counter)
        counter += 1
    

def greatest_common_factor(num1 = 1, num2 = 1):
    if num1 != 0 or num2 != 0:
        gcf = 1
        num1_factors = single_greatest_common_factor(num1)
        num2_factors = single_greatest_common_factor(num2)
        for i in num1_factors:
            if i in num2_factors:
                gcf = i


        if gcf == 1:
            print("No Common Factor")
        else:
            print("The Greatest Common Factor of " + str(num1) + " and " + str(num2) + " is: " + str(gcf))

    else:
        print("function cannot be passed '0' as one of its arguments.")

def single_greatest_common_factor(num):
    counter = 1
    factors = []
    half = num // 2
    while counter <= half:
        if num % counter == 0:
            factors.append(counter)
        counter += 1
    return factors

greatest_common_factor(12, 20)
