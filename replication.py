### Pattern Count

def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

### Frequent Words

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    for Pattern in freq:
        for i in range(n-k+1):
            deck = Text[i:i+k]
            if deck == Pattern:
                freq[Pattern] +=1
    return freq

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words

### Reverse Complemenet

def Reverse(Pattern):
    return Pattern[::-1]

def Complement(Pattern):
    compdict = {"A":"T",
              "T":"A",
              "G":"C",
              "C":"G"}
    complement = ""
    for i in Pattern:
        complement += compdict.get(i)
    return complement

def ReverseComplement(Pattern):
    return Reverse(Complement(Pattern))

### Pattern Matching

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    k = len(Pattern)
    for i in range(len(Genome)-k+1):
        if Genome[i:i+k] == Pattern:
            positions.append(i)
    return positions


### Symbol Array - to count instance of "symbol" in "Genome"
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

### The right way to do it
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

### Skew Array - return array of G vs C score
def SkewArray(Genome):
    Skew = {}
    Skew[0] = 0
    n = len(Genome)
    for i in range(n):
        if Genome[i] == "G":
            Skew[i+1] = Skew[i] + 1
        elif Genome[i] == "C":
            Skew[i+1] = Skew[i] - 1
        else:
          Skew[i+1] = Skew[i]
    return list(Skew.values())

### Minimum Skew - get the position of maximum C (ori)
def MinimumSkew(Genome):
    positions = [] # output variable
    sa = SkewArray(Genome)
    mini = min(sa)
    for i in range(len(sa)):
        if sa[i] == mini:
            positions.append(i)
    return positions


### Hamming distance
def HammingDistance(p, q):
    hamming = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hamming += 1
    return hamming

### Approx pattern matching - return positions that match within a H dist
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    for i in range(len(Text)-len(Pattern)+1):
        sample = Text[i:i+len(Pattern)]
        if HammingDistance(sample, Pattern) <= d:
            positions.append(i)
    return positions
