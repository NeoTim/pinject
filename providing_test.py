
import unittest

import providing


class DefaultGetArgNamesFromProviderFnNameTest(unittest.TestCase):

    def test_non_provider_prefix_returns_nothing(self):
        self.assertEqual(
            [],
            providing.default_get_arg_names_from_provider_fn_name('some_foo'))

    def test_single_part_name_returned_as_is(self):
        self.assertEqual(
            ['foo'],
            providing.default_get_arg_names_from_provider_fn_name('new_foo'))

    def test_multiple_part_name_returned_as_is(self):
        self.assertEqual(
            ['foo_bar'],
            providing.default_get_arg_names_from_provider_fn_name('new_foo_bar'))

    def test_alternate_prefixes_are_allowed(self):
        self.assertEqual(
            ['foo'],
            providing.default_get_arg_names_from_provider_fn_name(
                'provide_foo'))

    def test_provider_fn_name_can_start_with_underscore(self):
        self.assertEqual(
            ['foo'],
            providing.default_get_arg_names_from_provider_fn_name('_new_foo'))
