---
doc_id: arxiv-1105.0091v1
doc_title: "A central limit theorem for the characters of the infinite symmetric group and of the infinite Hecke algebra"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-4
source_pdf: 1105.0091v1.pdf
source_sha256: 7d6f72e016b25027
toc_source: outline
doc_brief: "A central limit theorem for the characters of the infinite symmetric group and of the infinite Hecke algebra — In this paper, we review the representation theory of the inﬁnite symmetric group, and"
---
E-mail: meliot@phare.normalesup.org
Abstract In this paper, we review the representation theory of the inﬁnite
symmetric group, and we extend the works of Kerov and Vershik by proving
that the irreducible characters of S∞always satisfy a central limit theorem.
Hence, for any point of the Thoma simplex, the corresponding measures on
the levels Yn of the Young graph have a property of gaussian concentration.
By using the Robinson-Schensted-Knuth algorithm and the theory of Pitman
operators, we relate these results to the properties of certain random per-
mutations obtained by riﬄe shuﬄes, and to the behaviour of random walks
conditioned to stay in a Weyl chamber.
Keywords Asymptotics of Young diagrams, central limit theorems,
combinatorial Hopf algebras, representation theory of symmetric groups,
random walks in a Weyl chamber, Markov traces of Hecke algebras.
Mathematics Subject Classiﬁcation (2000) 60B15,20C32,20C08,05E05,05E10
arXiv:1105.0091v1  [math.RT]  30 Apr 2011
2
Pierre-Loïc Méliot
Noname manuscript No.
(will be inserted by the editor)
A central limit theorem for the characters of the inﬁnite
symmetric group and of the inﬁnite Hecke algebra
Pierre-Loïc Méliot
the date of receipt and acceptance should be inserted later
For n ≥0, we denote by Sn the symmetric group of order n, that is
to say the group of permutations of [[1, n]] = {1, 2, . . . , n}. We also denote
by S∞the inductive limit S∞
n=0 ↑Sn. The representation theory of S∞is
quite diﬃcult, because it is a wild group, i.e., an inﬁnite group with factor
representations of type II or III. However, the classiﬁcation of the ﬁnite factor
representations of S∞is entirely known since the works of E. Thoma (cf.
[Tho64]). Hence, these representations are labelled by the pairs ω = (α, β) of
non-increasing sequences of non-negative real numbers
α = (α1 ≥α2 ≥· · · ≥αn ≥· · · )
;
β = (β1 ≥β2 ≥· · · ≥βn ≥· · · )
such that P∞
i=1 αi + P∞
i=1 βi ≤1. Moreover, if χω is the normalized character
of S∞corresponding to ω, and if σ ∈S∞is a product of disjoint cycles of
lengths l1, . . . , lr ≥2, then
χω(σ) =
r
Y
j=1
 ∞
X
i=1
(αi)lj + (−1)lj−1
∞
X
i=1
(βi)lj
!
.
Now, if one considers a restriction χω
|Sn of χω to a ﬁnite symmetric group,
it is not in general an irreducible character of Sn, and one can expand it as a
linear combination
χω
|Sn =
X
λ∈Yn
Pn,ω[λ] χλ
of the normalized irreducible characters of Sn. The sum runs over the set Yn
of (isomorphism classes of) irreducible representations of Sn, which happen
The Gaspard–Monge Institute of electronics and computer science, University of Marne-La-
Vallée Paris-Est, 77454 Marne-la-Vallée Cedex 2, France
A central limit theorem for the characters of S∞and H (S∞)
3
to correspond bijectively to the integer partitions of size n, that is to say
the non-decreasing sequences of positive integers that sum to n:
Yn =
(
λ = (λ1 ≥λ2 ≥· · · ≥λr)

 |λ| =
r
X
i=1
λi = n
)
.
Hence, for any pair ω = (α, β) and any integer n, one obtains a probability
measure Pn,ω on Yn. It has been shown by Kerov and Vershik (see [KV81a,
KV81b]) that these systems of probability measures, called coherent systems,
satisfy a law of large numbers. Thus, the irreducible characters χλ (viewed as
random functions on the symmetric groups) and the renormalized coordinates
of the random partitions λ under Pn,ω both converge in probability. In this
paper, we will reﬁne this result by showing that the convergence is always
gaussian, see our main Theorems 17, 18 and 25.
The article is organized as follows. In the ﬁrst part of the paper, we recall
the results of E. Thoma, using extensively the formalism of symmetric func-
tions. In Section 2, we explain how coherent systems of measures are related to
models of random permutations obtained by generalized riﬄe shuﬄes; here we
use well-known arguments from the theory of symmetric and quasi-symmetric
functions. In §3, we present a “method of non-commutative moments” that is
due to Kerov and Olshanski (see [KO94,IO02,Śni06b]), and that is extremely
useful in the setting of asymptotic representation theory of the symmetric
groups.
We apply this method in Sections 4 and 5 to reprove the law of large num-
bers of Kerov and Vershik and to establish our central limit theorems. The
arguments are exactly those that the author used with V. Féray in [FM10]
for the asymptotic study of the q-Plancherel measures; in our general setting,
they shall seem somewhat simpler. However, when looking at the ﬂuctua-
tions of the rows and columns of the random partitions taken with respect
to the probability Pn,ω, new diﬃculties arise when some coordinates of the
parameter ω in the Thoma simplex are equal. We address these diﬃculties
in Section 6 by using and generalizing arguments due to N. O’Connell (cf.
[O’C03], see also [Lit95,OY02,BBO05,Bia09]); hence, we relate a random walk
on Y = F
n∈N Yn whose marginale laws are the Pn,ω’s, to a multidimensional
random walk conditioned to stay in a Weyl chamber. This link ensures that the
ﬂuctuations of rows or columns corresponding to the same parameter are the
same as those of the eigenvalues of a gaussian hermitian matrix. Incidentally,
the link between random partitions and random walks provides a new proof
of some results of Section 5, in particular Theorem 19.
Finally, in §7, we explain how our results behave with respect to the quan-
tization of the symmetric group, that is to say that we replace S∞by its
Hecke algebra H (S∞). In particular, we perform all the computations in the
4
Pierre-Loïc Méliot
case when the irreducible character of Hq(S∞) is the so-called Jones-Ocneanu
trace ([Jon87]) of parameter z = −(1 −q)(1 −t), thereby providing an asymp-
totic study of a (q, t)-deformation of the Plancherel measures of the symmetric
groups.
We have tried to make this paper accessible to a wide audience, and self-
contained. In particular, we will recall many well-known results on symmetric
groups, symmetric functions and (free) quasi-symmetric functions.
Acknowledgements The author would like to express his gratitude to P. Biane, M. Boże-
jko, V. Féray, S. Giraudo, F. Hivert, A. Nikeghbali, J.-C. Novelli, P. Śniady, J.-Y. Thibon
and A. Vershik for various discussions or suggestions.
