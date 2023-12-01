class FilterError(Exception):
    '''Missing `user_id` to check filters.'''

    def __init__(self, user_id):
        error_msg = f'`user_id` has to be a str not {type(user_id)}.'
        super().__init__(error_msg)
