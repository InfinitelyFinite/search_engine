from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        # Storing into a variable so don't need to copy and paste long list every time
        # If you want to store search results into a variable like this, make sure you pass a copy of it when
        # calling a function, otherwise the original list (ie the one stored in your variable) might be
        # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)

    def test_search(self):
        expected_empty_search_results = []
        self.assertEqual(search(""), expected_empty_search_results)
        expected_sujal_search_results = []
        self.assertEqual(search("sujal"), expected_sujal_search_results)
        expected_french_search_results = ['French pop music']
        self.assertEqual(search("french"), expected_french_search_results)
        expected_fReNcH_search_results = ['French pop music']
        self.assertEqual(search("fReNcH"), expected_fReNcH_search_results)
        expected_MUSIC_search_results = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']
        self.assertEqual(search("MUSIC"), expected_MUSIC_search_results)

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_1_integration(self, input_mock):
        keyword = 'dog'
        advanced_option = 1
        keyword_2 = 10

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option, keyword_2])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced()+ str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(keyword_2) + "\n" + "\nHere are your articles: ['Guide dog', 'Endoglin', 'Sun dog']\n"

        # Test whether calling display_results() with given user input equals expected printout
        
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_2_integration(self, input_mock):
        keyword = 'dog'
        advanced_option = 2
        keyword_2 = 10

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option, keyword_2])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced()+ str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(keyword_2) + "\n" + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football']\n"

        # Test whether calling display_results() with given user input equals expected printout
        
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_3_integration_single_word(self, input_mock):
        keyword = 'dog'
        advanced_option = 3
        keyword_2 = 3

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option, keyword_2])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced()\
         + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(keyword_2) + "\n" + "\nHere are your articles: Black dog (ghost)\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_3_integration_no_result(self, input_mock):
        keyword = 3
        advanced_option = 3
        keyword_2 = 3

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option, keyword_2])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + str(keyword) + '\n' + print_advanced()\
         + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(keyword_2) + "\n" + "\nNo articles found\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_4_integration_no_exist(self, input_mock):
        keyword = 'dog'
        advanced_option = 4
        keyword_2 = 'Golden'

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option, keyword_2])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced()\
         + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + keyword_2 + "\n" + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n" + "Your favorite article is not in the returned articles!\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)


    @patch('builtins.input')
    def test_advanced_option_4_integration_exist(self, input_mock):
        keyword = 'dog'
        advanced_option = 4
        keyword_2 = 'tokyo'

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option, keyword_2])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced()\
         + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + keyword_2 + "\n" + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n" + "Your favorite article is in the returned articles!\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_option_5_integration(self, input_mock):
        keyword = 'dog'
        advanced_option = 5
        keyword_2 = 'cat'

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option, keyword_2])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced()\
         + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + keyword_2 + "\n" + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'Voice classification in non-classical music']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)


# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
