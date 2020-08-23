def normalize_path(path) -> str:
    result = path

    if result[-1] != "/":

        result = f"{result}/"

    return result


def to_bytes(mes) -> bytes:

    if isinstance(mes, bytes):
        return mes

    result = mes.encode()
    return result




