---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
This claim, which seems plausible from (0.1) and (0.2) can be substantially reﬁned,
see [BDJ], [AD].
The Gaussian process ∆(x) can be deﬁned by a random trigonometric series.
Let ξ2, ξ3, . . . be independent standard real Gaussian random variables (each ξk
has mean 0 and variance 1), and set x = 2 cos θ, where 0 ≤θ ≤π. Then
∆(x) = ∆(2 cos θ) = 1
π
∞
X
k=2
ξk
√
k
sin(kθ).
(0.3)
For any smooth test function ϕ on R, the smoothed series
1
π
∞
X
k=2
ξk
√
k
Z 2
−2
sin(kθ)ϕ(x)dx,
θ = arccos(x/2)
(0.4)
converges and is a Gaussian random variable. In this way we get a Gaussian measure
on the space of distributions with support on [−2, 2], or a generalized Gaussian
process. Its trajectories are not ordinary functions but generalized functions.
History of the result. The law of large numbers (the concentration near the
curve Ω) was independently obtained by Logan and Shepp [LoS] and by Vershik
and Kerov [VeK1]. Their papers appeared in 1977. Later, in 1985, Vershik and
Kerov published a detailed version of their work, [VeK3], containing stronger re-
sults. In [LoS] and [VeK3], the question about the second term of the asymptotics,
corresponding to the central limit theorem, was posed.
Such a theorem was obtained by Kerov and announced in his short note [Ke1],
1993. There Kerov also outlined the scheme of the proof. The note [Ke1] contained
a number of fruitful ideas, one of which (introduction of “good” coordinates in
the set of Young diagrams) was largely developed in the joint note by Kerov and
Olshanski [KO], 1994.
For an intermediate result of [Ke1], which is of independent interest, an elegant
proof was suggested by Hora [Ho], 1998. Note that Hora’s approach diﬀers from
that of Kerov.
A few years ago we started to persuade Kerov to write a detailed exposition of his
central limit theorem. Our discussions resulted ﬁrst in the joint paper by Ivanov
and Kerov [IK], 1999, which clariﬁed and developed one of the steps of Kerov’s
proof.1
Then Kerov found a simpler derivation of the theorem, which also made apparent
that the subject is connected with the concept of free cumulants and a theorem due
to Biane [Bi1]. In the end of 1999 Kerov sent us two short work notes with a
description of the new approach.
About the same time he gave a talk on this
subject at Vershik’s seminar in St. Petersburg. He also started writing a detailed
paper on this subject but had time only to ﬁnish the preliminary section.
In the present paper we give a detailed exposition of Kerov’s central limit the-
orem. Our aim was to reconstruct from his notes the “new approach” of 1999.2
This was not easy: for a long time we could not understand the meaning of some
1It concerns the stable structure constants for convolution of conjugacy classes in symmetric
groups. This topic was also discussed in [KO].
2It should be pointed out that the “old approach” of 1993 is also correct: we were able to
directly check all the claims of [Ke1].
3
