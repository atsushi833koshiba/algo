import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
          sha = hashlib.sha256()

          hash_str = (str(self.previous_hash) + str(self.timestamp) + str(self.data)).encode('utf-8')

          sha.update(hash_str)

          return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def get_previous_hash(self):
        return self.previous_hash

    def get_data(self):
        return self.data

class BlockChain:

    def __init__(self):
        #self.previous = None
        self.previous = None
        #self.chain = {}
        self.chain = []

    def add(self, raw_data):
        now_utc = datetime.datetime.now(datetime.timezone.utc)

        if self.previous == None:
            # Create first block.
            self.previous = Block(now_utc, raw_data, 0)
            #self.chain[self.previous.get_previous_hash()] = self.previous
            self.chain.append(self.previous)
            return
        # In the case of existing fist block already.
        block = Block(now_utc, raw_data, self.previous.get_hash())
        self.chain.append(block)
        self.previous = block

    def get_chain(self):
        return self.chain


def test_case1_block_chain():

    block_chain = BlockChain()
    block_chain.add("first")
    block_chain.add("second")
    block_chain.add("third")

    for block in block_chain.get_chain():
        statement = "data: {}, hash: {}, previous_hash: {}"\
        .format(block.get_data(), block.get_hash(), block.get_previous_hash())
        print(statement)
        """
        Expected:
        But, hash and previous_hash depend on time when it is executed.
        So, following is an example.

        data: first, hash: 72893e671e0ee2a660dc32ddbb8a6fbe05d3e30a240d39be77e03410860c26d4, previous_hash: 0
        data: second, hash: 099861d064dc3b6375ccf8bcab3ad82f01b32361d621e5ae5296b3e438415495, previous_hash: 72893e671e0ee2a660dc32ddbb8a6fbe05d3e30a240d39be77e03410860c26d4
        data: third, hash: be14c10ccb20176c51fd1befa1c37358d2caf7572b4ce3ce995f14c0d5390cdd, previous_hash: 099861d064dc3b6375ccf8bcab3ad82f01b32361d621e5ae5296b3e438415495
        """

def test_case2_block_chain():

    block_chain = BlockChain()
    for i in range(1000):
        block_chain.add("block_num" + str(i))

    for block in block_chain.get_chain():
        statement = "data: {}, hash: {}, previous_hash: {}"\
        .format(block.get_data(), block.get_hash(), block.get_previous_hash())
        print(statement)
        """
        Expected:
        But, hash and previous_hash depend on time when it is executed.
        So, following is an example.

        (omitted for too long sentences)

        data: block_num988, hash: b312d6a4c2a1e9db52bde902cf11c93e42f5516756180d1bf158e68619124e2c, previous_hash: 3fc757699a71d9012c759d923cf78179e799cb681be88ec81d07d86a47fbe26a
        data: block_num989, hash: 0fd0207abdfaea53b54d2abba88f753a6b04ba4864a4d0d50dad1a404b08ec80, previous_hash: b312d6a4c2a1e9db52bde902cf11c93e42f5516756180d1bf158e68619124e2c
        data: block_num990, hash: 41952314ced2664fe222b1358b89525ede1604870caffaf84fd4519b0ff1b374, previous_hash: 0fd0207abdfaea53b54d2abba88f753a6b04ba4864a4d0d50dad1a404b08ec80
        data: block_num991, hash: cfdc8271700b8d2b02a00ce9cb3cfd37770983692b30f8544e58a732f9f6f546, previous_hash: 41952314ced2664fe222b1358b89525ede1604870caffaf84fd4519b0ff1b374
        data: block_num992, hash: 76a22b12b92ccdc5a8df59a1520d8dd68f5b8da2d0adf5d0eeb0750654a7d9fa, previous_hash: cfdc8271700b8d2b02a00ce9cb3cfd37770983692b30f8544e58a732f9f6f546
        data: block_num993, hash: 935c8aaa2ef74b711d4a4bbf93c5160292daaa60ce16ce9ad47306c8d5eb2b5c, previous_hash: 76a22b12b92ccdc5a8df59a1520d8dd68f5b8da2d0adf5d0eeb0750654a7d9fa
        data: block_num994, hash: a83fca3bd9a358f1d0f11acf419971797a95b95fdaeb3db561326827e9a57974, previous_hash: 935c8aaa2ef74b711d4a4bbf93c5160292daaa60ce16ce9ad47306c8d5eb2b5c
        data: block_num995, hash: 3c3a37cd7d3bff4e7a54eed488e29db5acd3dad884486b41c314cd41c3783fe1, previous_hash: a83fca3bd9a358f1d0f11acf419971797a95b95fdaeb3db561326827e9a57974
        data: block_num996, hash: c901f99247726efbc1aa44e376b842e8d3463ce239552b88ed298f308f27e1a0, previous_hash: 3c3a37cd7d3bff4e7a54eed488e29db5acd3dad884486b41c314cd41c3783fe1
        data: block_num997, hash: 16f3647f5694c7580ffa4b115b213c61ed2618fefa300be6ce6d77a0d7b33ed8, previous_hash: c901f99247726efbc1aa44e376b842e8d3463ce239552b88ed298f308f27e1a0
        data: block_num998, hash: a0be08070c63be4d46abeb97fd19b75ecd88f347279ec8cb81021a025e7f0a3b, previous_hash: 16f3647f5694c7580ffa4b115b213c61ed2618fefa300be6ce6d77a0d7b33ed8
        data: block_num999, hash: 6ba3a74215226dd12d0a22a5f38bf6ef0a94631bdce5cd78b663cc612bc3f5a3, previous_hash: a0be08070c63be4d46abeb97fd19b75ecd88f347279ec8cb81021a025e7f0a3b
        """

def test_case3_block_chain():

    block_chain = BlockChain()
    block_chain.add("only_one")

    for block in block_chain.get_chain():

        statement = "data: {}, hash: {}, previous_hash: {}"\
        .format(block.get_data(), block.get_hash(), block.get_previous_hash())
        print(statement)
        """
        Expected:
        But, hash depend on time when it is executed.
        On the other hand, previous_hash is 0 constantly because of having only one block.
        So, following is an example.

        data: only_one, hash: ae16a6e9410bc2d129f5f7962b7739e25330fe4b9c26d9e079219d2610b646fd, previous_hash: 0
        """

def test_case4_block_chain():

    block_chain = BlockChain()
    block_chain.add(None)

    for block in block_chain.get_chain():

        statement = "data: {}, hash: {}, previous_hash: {}"\
        .format(block.get_data(), block.get_hash(), block.get_previous_hash())
        print(statement)
        """
        Expected:
        I allow block to have None in data.
        In this case, data becomes None.
        But, hash depend on time when it is executed.
        On the other hand, previous_hash is 0 constantly because of having only one block.
        So, following is an example.

        data: None, hash: 8697133a7cefc91bff784eb16b6730750249e12d0c5744977b29c70cd516fa08, previous_hash: 0
        """

test_case1_block_chain()
test_case2_block_chain()
test_case3_block_chain()
test_case4_block_chain()
