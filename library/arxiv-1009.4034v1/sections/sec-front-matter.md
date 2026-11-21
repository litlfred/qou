---
doc_id: arxiv-1009.4034v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-2
source_pdf: 1009.4034v1.pdf
source_sha256: 8f8d6d786b60c279
toc_source: outline
doc_brief: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2 — In this article, we show that Kerov’s central limit theorem related to the ﬂuctuations of Young diagrams under the"
---
KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL
MEASURES OF PARAMETER α = 1/2
PIERRE-LOÏC MÉLIOT
Abstract. In this article, we show that Kerov’s central limit theorem related to the ﬂuctuations of
Young diagrams under the Plancherel measure extends to the case of Schur-Weyl measures, which are
the probability measures on partitions associated to the representations of the symmetric groups Sn on
tensor products of vector spaces V ⊗n (see [Bia01]). The proof is inspired by the one given in [IO02] for
the Plancherel measure, and it relies on the combinatorics of the algebra of observables of diagrams; we
shall also use Śniady’s theory of cumulants of observables (cf. [Ś06]).
Given a ﬁnite group G and a ﬁnite-dimensional complex linear representation V of G, the decomposition
in irreducible components V = L
λ∈b
G mλ Vλ yields a probability measure on the set bG of isomorphism
classes of irreducible representations of G:
PV
h
λ ∈bG
i
= mλ dim Vλ
dim V
In particular, when G = Sn is the symmetric group of permutations of [[1, n]], a reducible representation of
Sn yields a probability measure on the set Pn = bSn of integer partitions of size n. When V = CSn is the
(left) regular representation, one obtains the so-called Plancherel measure, which has been extensively
studied in the n →∞asymptotic; see for instance [IO02].
In this paper, we focus on the Schur-
Weyl measures that correspond to the representations (CN)n ↶Sn, where Sn acts on the right by
permutation of the letters of the simple tensors:
(v1 ⊗v2 ⊗· · · ⊗vn) · σ = vσ(1) ⊗vσ(2) ⊗· · · ⊗vσ(n)
By Schur-Weyl reciprocity, the probability measure on partitions associated to this representation is
also a probability measure on irreducible representations of GL(N, C). The ﬁrst order asymptotic of
these measures when n1/2 ≃cN and n goes to inﬁnity has been determined by P. Biane in [Bia01]; we
shall recall this in §1, and by using the Robinson-Schensted-Knuth correspondence, we will also give a
“combinatorial model” for these probability measures.
The asymptotics of the Plancherel measures on partitions correspond to the case c = 0, and for
Plancherel measures, S. Kerov has shown that Young diagrams deviate from their limit shape by a
(generalized) gaussian process ([Ker93], [IO02]). Consequently, it was natural to ask whether such a
result extends to the case of Schur-Weyl measures with parameter c > 0. We have found out that it is
indeed the case, and that the central limit theorem for Schur-Weyl measures is up to a translation on
the x-axis the same as for Plancherel measures. This is the main result of this paper, see Theorem 14
in §6. Notice that our result is the “Schur-Weyl dual” of a result of Lytova and Pastur related to the
deviation of the empirical spectral measure of Wishart matrices from the Marčenko-Pastur distribution,
cf. [LP09]. In order to prove Theorem 14, we shall follow the approach of V. Ivanov and G. Olshanski
([IO02]), and we shall therefore use the algebra O of observables of diagrams. These objects are in
some sense “polynomial functions on partitions” (see [KO94]), and in the setting of random partitions,
their expectations play the same role as the moments for real or complex random variables. Moreover, P.
Śniady has developed in [Ś06] a theory of cumulants of observables of diagrams that allow to prove
results of gaussian concentration. These facts are recalled in §2 and §4, and we will also compute certain
observables of the limit shapes Ωc of the Young diagrams under Schur-Weyl measures with parameters
α = 1/2, c > 0, cf. §3.
1
arXiv:1009.4034v1  [math.RT]  21 Sep 2010
2
PIERRE-LOÏC MÉLIOT
The core of the proof of our central limit theorem is contained in §5, and it is shown that Chebyshev
polynomials of the second kind yield random variables related to the second order asymptotic of the
Schur-Weyl measures, and that are asymptotically centered independant gaussian variables. Our proof
is slightly diﬀerent from the one given in [IO02, §7] for Plancherel measures, because in the setting of
Schur-Weyl measures, one cannot use the so-called Kerov degree on observables.
Hence, one has to
use instead the weight ﬁltration on observables, and the arguments of Ivanov and Olshanski that relie
on Kerov’s degree will be replaced by a somewhat nasty trick, see Lemma 12. Thus, our calculations
present quite miraculous simpliﬁcations, and these simpliﬁcations can be summarized by the following
fact: Chebyshev polynomials of the second kind do play a hidden and nethertheless prominent role in the
combinatorics of observables of diagrams. We ought to say that we do not understand completely the
reasons of the universality of Kerov’s central limit theorem; in this paper, we only show that calculations
can be performed in a more general setting than previously known, but as for now we do not know why.
