class Blockchain(object):
    def __init__(self) -> None:
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Creates a new block and adds it to the chain
        pass

    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hash a given block
        pass

    @property
    def last_block(self):
        # Return the latest block in the chain
        pass
