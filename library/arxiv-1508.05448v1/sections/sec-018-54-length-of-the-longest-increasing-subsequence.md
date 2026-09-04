---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-018-54-length-of-the-longest-increasing-subsequence
section_title: "Length of the Longest Increasing Subsequence"
section_number: 5.4
pages: 110-112
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
doc_brief: "Concentration of Measure Techniques and Applications — 23 sections: Biographical Sketch; Acknowledgments; Abstract"
---
Consider a permutationπ∈Sn. An increasing subsequence i1,i 2,...,i k of a permuta-
tioni↦→π(i) is a subsequence such thati1 <··· <i k andπ(i1)<π (i2)<··· <π (ik).
We will be concerned with determining the length of the longest increasing subse-
quence in a given permutation. Denote the length of the longest increasing subse-
quence of π by𝓁(π).
The following example is due to [Aldous and Diaconis, 1995]. Consider the per-
mutation given by
7 2 8 1 3 4 10 6 9 5
102
where π(1) = 4, π(2) = 2, π(3) = 5, etc. Then a longest increasing subsequence is
given by
1 3 4 6 9
In this case 𝓁(π) = 5.
Notice that the longest increasing subsequence is not necessarily unique.
2 3 4 6 9
is also an increasing subsequence of length 5. The longest increasing subsequence
problem goes back to Ulam [Ulam, 1961]. Ulam asked what is the distribution of the
length of the longest monotone (increasing or decreasing) subsequence of a uniform
random permutation. While we will not go into the history here, a detailed account
of Ulam’s problem and Monte Carlo methods can be found in [Hammersley, 1972].
Quite a bit of progress has been made concerning the distribution of the length
of the longest increasing subsequence, provided that the permutation is uniformly
distributed. Hammersley [Hammersley, 1972] showed that E𝓁(π)∼ c√n, where n is
the length of the permutation and c is a constant. Vershik and Kerov [Vershik and
Kerov, 1977] and Logan and Shepp [Logan and Shepp, 1977] proved that the constant
c is equal to 2. Their methods of proof relied on hard analysis of the asymptotics of
Young tableau. Aldous and Diaconis [Aldous and Diaconis, 1999] give an interacting
particle process argument for c = 2. In addition, Baik, Deift, and Johansson [Baik
et al. , 1999] showed that the ﬂuctuations of the length of the longest increasing
subsequence for a uniform permutation are Tracy-Widom, on the order of n1/6. More
speciﬁcally, they show that
𝓁n− 2√n
n1/6
d
− →χ
where χ is a random variable with Tracy Widom distribution. The distribution
103
function for the Tracy Widom distribution is
F (t) = exp
(
−
∫ ∞
t
(x−t)u2(x)dx
)
where u(x) is the solution of the Painlev´ e equation
uxx = 2u3 +xu
See [Baik et al., 1999] for more background on the Tracy Widom distribution.
Much less is known about the distribution of the length of the longest increasing
subsequence of a random permutation distributed according to the Mallows measure.
In [Mueller and Starr, 2013], Mueller and Starr proved a weak law of large numbers
result analogous to the Vershik-Kerov and Logan-Shepp results for the uniform case.
To continue this work, we would like to bound the ﬂuctuations of the length of the
longest increasing subsequence of a Mallows permutation. As a ﬁrst step in this
direction, we use the modiﬁed Fisher-Yates algorithm to generate a random Mallows
