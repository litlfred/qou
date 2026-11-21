---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-029
section_title: "Page 29"
section_number: null
pages: 29-29
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Pick points a = ε1 < · · · < εn = b dividing I into subintervals of length ≤2ε.
Then, by the Lipschitz condition, the ball ∥σ∥≤2ε contains the intersections of
V (xi, ε)’s. Hence the required claim reduces to the following one:
Fix x ∈I and ε > 0. Then V (x, ε) contains a neighborhood of 0 in the weak
topology.
Let us remark that functions σ ∈Σ are uniformly bounded, ∥σ∥≤(b −a)/2.
Hence the weak topology on Σ will not change if we take, as functionals, integrals
with arbitrary continuous functions F.
Now let us take a continuous function
F(x) ≥0, concentrated in the ε/2–neighborhood of x and such that
R
F(y)dy = 1.
We claim that

Z
σ(x)F(x)dx
 ≤ε/2 ⇒σ ∈V (x, ε).
Indeed, assume that σ /∈V (x, ε), i.e., |σ(x)| > ε. Without loss of generality
we may assume that σ(x) > ε. Then, for any y such that |x −y| ≤ε/2, we have
σ(y) > ε/2, hence
R
σ(y)F(y) > ε/2, which proves our claim.
□
Proof of Theorem 5.5. This immediately follows from Theorem 5.4 and Lemmas
5.6, 5.7.
□
§6. The central limit theorem for characters
For any f ∈A, we denote by f (n) the random variable deﬁned on the probability
space (Yn , Mn) and obtained by restricting f to Yn.
By the symbol
d
−→we will denote convergence of random variables in distribu-
tion, see, e.g. [Sh].
The aim of this section is to prove the following result.
Theorem 6.1 (Central limit theorem for characters).
Choose a sequence {ξk}k=2,3,... of independent standard Gaussian random vari-
ables. As n →∞, we have



p#
k
(n)
nk/2



k=2,3,...
d
−→{
√
kξk}k=2,3,...
(6.1)
In more detail, for any ﬁxed N = 2, 3, . . ., the joint distribution of N −1 random
variables
p#
k
(n)
√
k nk/2 ,
2 ≤k ≤N,
weakly tends, as n →∞, to the standard Gaussian measure on RN−1. Note that
we could take equally well in (6.1) the random variables
nk/2
√
k
χλ
(k,1n−k)
dim λ
,
2 ≤k ≤N,
where λ ∈Yn is the random Plancherel diagram.
The proof of Theorem 6.1 will be given after some preparation work, based on
Propositions 4.11, Proposition 4.12, and Corollary 4.13.
29
