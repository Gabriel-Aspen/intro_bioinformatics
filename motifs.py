# Input:  A set of kmers Motifs
# Output: Count(Motifs)
def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    count = Count(Motifs)
    for base in count:
        profile[base] = []
        for i in count[base]:
            profile[base].append(i/t)
    return profile

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    cons = Consensus(Motifs)
    error = 0
    k = len(Motifs[0])
    for row in Motifs:
        for base in range(k):
            if row[base] != cons[base]:
                error +=1
    return error

# Input:  String Text and profile matrix Profile
# Output: Probability of text based on profile
def Pr(Text, Profile):
    pro = 1
    for i in range(len(Text)):
        pro = pro*Profile[Text[i]][i]
    return pro

#Input: sting of bases, k and a 4 x k profile matrix
# Output: The kmer in text with the highest probability
def ProfileMostProbableKmer(text, k, profile):
    max_prob = -1
    x = 0
    for i in range(len(text)-k+1):
        sample_kmer = text[i:i+k]
        kmer_prob = Pr(sample_kmer, profile)
        if kmer_prob > max_prob:
            max_prob = kmer_prob
            x = i
    return text[x:x+k]

def GreedyMotifSearch(Dna,k,t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for m in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][m:m+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
