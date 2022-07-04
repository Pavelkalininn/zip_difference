from typing import Tuple
from zipfile import ZipFile


def difference_check(
        filename_1: str,
        filename_2: str
) -> Tuple[list, list, list]:

    def __difference_check(
            _file_headers_1: dict,
            _file_headers_2: dict
    ) -> list:

        _unique_values = []
        for _key, _value in _file_headers_1.items():
            if _key in _file_headers_2 and _value == _file_headers_2[_key]:
                identical.append(_key)
            else:
                _unique_values.append(_key)
        return _unique_values

    identical = []
    with ZipFile(filename_1, 'r') as zip_1, ZipFile(filename_2, 'r') as zip_2:
        first_file_headers = {
            info.filename: info.CRC for info in zip_1.infolist()
        }
        second_file_headers = {
            info.filename: info.CRC for info in zip_2.infolist()
        }
        unique_in_archive_1 = __difference_check(
            first_file_headers, second_file_headers
        )
        unique_in_archive_2 = __difference_check(
            second_file_headers, first_file_headers
        )

    return identical, unique_in_archive_1, unique_in_archive_2


def read_input() -> Tuple[str, str]:
    first_file_url = input().strip()
    second_file_url = input().strip()
    return first_file_url, second_file_url


if __name__ == '__main__':
    identical_result, archive_1, archive_2 = difference_check(
        *read_input()
    )
    print(
        '\nidentical', '\n'.join(identical_result),
        '\nUnique in archive1.zip', '\n'.join(archive_1),
        '\nUnique in archive2.zip', '\n'.join(archive_2),
        sep='\n'
    )
    input()
