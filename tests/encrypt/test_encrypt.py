import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Invalid key type
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('Trybe', 'A')

    # Invalid message type
    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(20, 2)

    # Testando a criptografia com índice ímpar
    assert encrypt_message("hello", 2) == "oll_eh"

    # Testando a criptografia com índice par
    assert encrypt_message("hello", 3) == "leh_ol"

    # Testando índice maior que o comprimento da mensagem
    assert encrypt_message("hello", 10) == "olleh"

    # Testando a criptografia com índice igual ao comprimento da mensagem
    assert encrypt_message("world", 5) == "dlrow"

    # Testando a criptografia com índice zero (deve inverter a mensagem)
    assert encrypt_message("python", 0) == "nohtyp"

    # Testando a criptografia com índice 1 (deve inverter a mensagem)
    assert encrypt_message("example", 1) == "e_elpmax"
