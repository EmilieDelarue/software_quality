import unittest


def my_split(string, operator):
    my_list=[]
    temp_string = ""
    for ch in string: #parcours chaque caratère du string
        if ch == operator:
            if temp_string:
               my_list.append(temp_string) 
               temp_string = ""
        else:
            temp_string += ch #creation string temporaire
    if temp_string:
        my_list.append(temp_string)
    return my_list


class TestSplit(unittest.TestCase):

    def test_my_split(self):
        a="hello world"
        self.assertEqual(my_split(a," "), ['hello', 'world'])
        self.assertTrue(type(my_split(a," ")), list)
        self.assertEqual(len(my_split(a," ")), 2) 
    
    def test_my_split_one_string(self):
        b="jkljfkqs_jfklmjqs-fjqk"
        self.assertEqual(my_split(b," "), ['jkljfkqs_jfklmjqs-fjqk'])
        self.assertEqual(len(my_split(b," ")), 1)
        self.assertEqual(my_split(b,"_"), ['jkljfkqs','jfklmjqs-fjqk'])
        self.assertEqual(len(my_split(b,"_")), 2)
        self.assertTrue(type(my_split(b," ")), list)
    
    def test_my_split_with_two_space(self):
        c="aaa  bbb"
        self.assertEqual(my_split(c," "), ['aaa','bbb'])
        self.assertTrue(type(my_split(c," ")), list)
        self.assertEqual(len(my_split(c," ")), 2)
    
    def test_my_split_another_string(self):
        d="1+3"
        self.assertEqual(my_split(d,"+"), ["1","3"])
    

if __name__ == '__main__':
    unittest.main()      