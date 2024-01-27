# TODO: pop item, only error_msg  comes
# TODO: pop item, return and print difference


class RoseDictionary:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        self._iter_keys = iter(self.data)
        return self

    def __next__(self):
        if self._iter_keys is not None:
            try:
                key = next(self._iter_keys)
                return key, self.data[key]
            except StopIteration:
                self._iter_keys = None
                raise StopIteration
        else:
            raise StopIteration

    def pop_item(self, raise_error=False, error_msg="" , default = ""):
        try:
            key, value = self.data.popitem()
            return key, value
        except:
            if raise_error:
                if error_msg:
                    return f"KeyError: '{error_msg}'"
                else:
                    return f"KeyError: 'error_msg'"
            else:
                if default:
                    return default
                else:
                    if error_msg:
                        return error_msg
                    else:
                        return 'Dictionary was empty and no default value/message was specified.'

    def get_item(self, key, raise_error=False, default="", error_msg=""):
        if key in self.data:
            return self.data[key]
        elif raise_error:
            if error_msg:
                return f'KeyError: {error_msg}'
            else:
                return f'KeyError: error_msg'
        else:
            if default:
                return default
            else:
                return "Value was not found and no default value/message was specified."
