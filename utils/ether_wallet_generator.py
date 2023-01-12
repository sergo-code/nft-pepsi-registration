import web3
from mnemonic import Mnemonic


def get_mnemonic():
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=128)
    return words


def get_public_address(words):
    web3.Account.enable_unaudited_hdwallet_features()
    account = web3.Account.from_mnemonic(words)
    return account.address


if __name__ == '__main__':
    mnemonic_phrase = get_mnemonic()
    address = get_public_address(mnemonic_phrase)

    print('Mnemonic phrase:', mnemonic_phrase)
    print('Public address:', address)
