"""
abc=(1,3,5,7,9,8,6,4,2,0)
for var in abc:
    print(abc)

xyz=1
while xyz<10:
    print(xyz)
    xyz+=2
"""
"""xyz=1
while xyz<10:
    xyz+=1
    if xyz==5:
        continue
    print(xyz)
"""
#using class use encoder and decoder, like encoder a to b convert, and decoder b to a convert, in which can use any opps concepts to cal encoder and decoder.make a pattern likw first encoder then decoder and so on.
"""class Codec:
    def __init__(self, shift=1):
        self.shift = shift

    def encode(self, text):
        result = []
        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result.append(chr((ord(ch) - base + self.shift) % 26 + base))
            else:
                result.append(ch)
        return "".join(result)

    def decode(self, text):
        result = []
        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result.append(chr((ord(ch) - base - self.shift) % 26 + base))
            else:
                result.append(ch)
        return "".join(result)


class PatternRunner:
    def __init__(self, codec):
        self.codec = codec

    def run(self, text, cycles):
        current = text
        for i in range(cycles):
            if i % 2 == 0:
                current = self.codec.encode(current)
                print(f"Encoder {i//2 + 1}: {current}")
            else:
                current = self.codec.decode(current)
                print(f"Decoder {i//2 + 1}: {current}")
        return current


codec = Codec(1)
runner = PatternRunner(codec)

start_text = "abcXYZ"
final_text = runner.run(start_text, 6)

print("Final:", final_text)"""


