import sys
from operator import attrgetter

class Node:
    def __init__(self,char,frequencies):
        self.char = char
        self.frequencies = frequencies
        self.left = None
        self.right = None

    def __str__(self):
        return "char: " + self.char + " fre: " + str(self.frequencies)

    def set_right(self, right):
        self.right = right

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_char(self):
        return self.char

    def set_char(self):
        return self.char

    def get_frequencies(self):
        return self.frequencies

    def set_frequencies(self, frequencies):
        self.frequencies = frequencies


class Tree:
    def __init__(self, value):

        if not len(value) == 2:
            self.root = None
            return
        self.root = Node(value[0],value[1])
        self.encode_cache = {}

    def get_root(self):
        return self.root

    def set_root(self, node):
        self.root =node

    def get_cache(self):
        return self.encode_cache



def _calc_atleast_number_of_digit(original_str):

    if original_str == None:
        return None

    _char_set = set()
    for char in original_str:
        _char_set.add(char)

    _base = 2
    _power = 0
    _calc_result = 0

    while _calc_result <  len(_char_set):
        _power = _power + 1
        _calc_result = _base ** _power

    return _power

def _get_binary_code_for_haffman(digit):
    digit = digit - 1
    bin_code = format(digit, 'b')
    return bin_code


def _buildTree(sorted_char_count):


    # Create dummy.
    dummy_root = ['root', 0]
    tree = Tree(dummy_root)
    root_node = tree.get_root()

    if len(sorted_char_count) == 1:
        one = sorted_char_count[0]
        root_node.set_left(Node(one[0], one[1]))
        return tree

    nodes = []
    for char_count in sorted_char_count:
         nodes.append(Node(char_count[0], char_count[1]))

    # for node in nodes:
    #     print(node.get_char() + " : " + str(node.get_frequencies()))

    while len(nodes) >= 2:
        most_smallest_node = nodes[0]
        second_smaller_node = nodes[1]

        parent_frequencies = most_smallest_node.get_frequencies() \
                            + second_smaller_node.get_frequencies()

        # Parent node don't have char. So it is always defined to have a blank.
        new_node = Node('',parent_frequencies)

        new_node.set_left(most_smallest_node)
        new_node.set_right(second_smaller_node)

        # Remove char and frequencies list which is already coped with.
        nodes.pop(0)
        nodes.pop(0)
        nodes.append(new_node)

        # Re:sort
        #sorted_char_count = sorted(nodes, key = lambda k:k[1])
        nodes = sorted(nodes, key = attrgetter('frequencies'))

    tree.set_root(nodes[0])
    return tree


def _get_encode_value(node, target_char, code, cache):

    if node == None:
        return None
    if node.get_char() == target_char:
        return code

    right_value = _get_encode_value(node.get_right(), target_char, code + '1',cache)

    if right_value != None:
        if cache != None:
            cache[right_value] = target_char
        return right_value

    left_value = _get_encode_value(node.get_left(), target_char, code + '0',cache)

    if left_value != None:
        if cache != None:
            cache[left_value] = target_char
        return left_value

def _get_encode_value_of_tree(target_char, tree):

    if tree == None or not isinstance(tree, Tree):
        return None;

    value = _get_encode_value(tree.get_root(), target_char, '', tree.get_cache())
    return value


def huffman_encoding(data):
    char_count = []

    if None == data:
        return None, None
    if '' == data:
        return '', ''
    data = str(data)

    for char in data:
        char_count.append((char , data.count(char)))
    # Sort by frequencies.
    sorted_char_count = sorted(list(set(char_count)), key = lambda k:k[1])
    tree = _buildTree(sorted_char_count)

    encoded_value = ''

    for char in data:
        encoded_value += _get_encode_value_of_tree(char, tree)

    return encoded_value, tree


def huffman_decoding(data,tree):

    if data == None or tree == None or not isinstance(tree, Tree):
        return None
    encoded_cache = tree.get_cache()
    if tree.get_cache() == None:
        return None

    decoded_value = ''
    bits = ''
    for bit in data:
        bits += bit
        if bits in encoded_cache:
            decoded_value += encoded_cache[bits]
            bits = ''

    return decoded_value

    pass


if __name__ == "__main__":

    # Test Case 1
    a_great_sentence = "The bird is the word"

    sentense = '----------------------------------------' \
    'Test Case 1: sentence = {}'.format(a_great_sentence) \
    + '----------------------------------------'
    print(sentense)

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Expected: The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Expected: The content of the encoded data is: 1010111111101101000000001010110000011011010011111111011001111011001010

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Expected: The size of the encoded data is: 69
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    # Expected: The content of the decoded data is: The bird is the word


    # Test Case 2
    a_great_sentence = None
    sentense = '----------------------------------------' \
    'Test Case 2: sentence = {}'.format(a_great_sentence) \
    + '----------------------------------------'
    print(sentense)

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Expected: The content of the encoded data is: None

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    # Expected: The content of the decoded data is: None

    # Test Case 3
    a_great_sentence = '1'
    sentense = '----------------------------------------' \
    'Test Case 3: sentence = {}'.format(a_great_sentence) \
    + '----------------------------------------'
    print(sentense)

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Expected: The size of the encoded data is: 24
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Expected: The content of the encoded data is: 0

    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Expected: The size of the encoded data is: 50

    print ("The content of the decoded data is: {}\n".format(decoded_data))
    # Expected: The content of the decoded data is: 1


    # Test Case 4
    a_great_sentence = 'AAAAAMMMMSSSSOSk2459CCCn22199SSSSSSS'
    sentense = '----------------------------------------' \
    'Test Case 4: sentence = {}'.format(a_great_sentence) \
    + '----------------------------------------'
    print(sentense)

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Expected: The size of the encoded data is: 40
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Expected: The content of the encoded data is: 100100100100100010010010010111111110111111011010010111010101000101110111011101000010010110000000011111111111111

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Expected: The size of the encoded data is: 85
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    # Expected: The content of the decoded data is: AAAAAMMMMSSSSOSk2459CCCn22199SSSSSSS
