---
doc_id: noniterativeroth2
doc_title: "A PROOF OF ROTH’S THEOREM ON ARITHMETIC PROGRESSIONS"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: noniterativeroth2.pdf
source_sha256: 83bbcdf45da069e5
toc_source: undetermined
doc_brief: "A PROOF OF ROTH’S THEOREM ON ARITHMETIC PROGRESSIONS — We present a proof of Roth’s theorem that follows a slightly diﬀerent structure to the usual proofs, in that there is not much iteration."
---
4
ERNIE CROOT AND OLOF SISASK
[7], whose proof consists of a simple averaging procedure, will help us make use of this
information.
Lemma 3.1. [2] For any 1 ⩽M ⩽N, and for any set T ′ ⊆[N], we have
Λ(T ′) ≫|T ′|/N −r3(M)/M
M 2
.
We will be using
M = ⌊(log p/ log log p)1/8⌋.
Now we observe that if
|T ′| < 4|S|/3,
and N is suﬃciently large, then we would have that
|T| < 3|S|/2.
Clearly, then, there exists s ∈S such that the arithmetic progression s, s−x, s−2x ∈S,
since otherwise we would have g(n) ⩽2/3 for all n ∈Fp, which would imply that
|S| =
X
n∈Fp
g(n) ⩽(2/3)|T| < |S|,
a contradiction. But if S contains the progression s, s −x, s −2x, that also is a contra-
diction, because we assumed that it is free of such progressions. It must therefore be
the case that
|T ′| ⩾4|S|/3,
from which it follows that
4|S|/3N −r3(M)/M ⩽|T ′|/N −r3(M)/M
≪
M 2Λ(T ′)
≪
(log log p/ log p)1/4.
In other words,
r3(N)/N = |S|/N ⩽3r3(M)/4M + O((log log p/ log p)1/4).
So, r3(N)/N is asymptocially decreasing to 0, whence κ = 0.
4. Acknowledgements
We would like to thank Ben Green for pointing out that we can take B to be a three
term progression for our argument – in a previous draft we took B to be a 20-term
arithmetic progression, due to a small ineﬃciency in one part of our proof.
