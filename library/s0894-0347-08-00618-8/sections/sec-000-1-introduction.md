---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8 — 24 sections: Front matter; Introduction; A plethora of negative dependence"
---
Introduction
521
2.
A plethora of negative dependence properties and conjectures
524
2.1.
Negative dependence concepts
524
2.2.
Strongly Rayleigh measures
529
2.3.
Symmetric homogenization
530
2.4.
Measures on countably inﬁnite sets
530
2.5.
Towards a theory of negative dependence: Problems and solutions
531
3.
Negative dependence in mathematics and physics
533
3.1.
Real stable polynomials and transcendental entire functions
533
3.2.
Hadamard-Fischer inequalities and GKK-matrices
535
3.3.
Determinantal probability measures
537
3.4.
Graphs, Laplacians, spanning trees and the random cluster model
538
3.5.
Interacting particle systems and exclusion evolutions
540
4.
Negative dependence theory for strongly Rayleigh measures
541
4.1.
Symmetric homogenization via G˚arding hyperbolic polynomials
541
4.2.
Stability implies negative association
544
4.3.
Stochastic domination and truncations
545
4.4.
The partial symmetrization procedure
549
5.
Preservation of negative dependence by symmetric exclusion processes 551
6.
Almost exchangeable measures
553
7.
Negative results on negative dependence
561
Acknowledgements
564
References
565
1. Introduction
Let µ : 2[n] →R, [n] = {1, . . . , n}, be a function attaining non-negative values
and satisfying 
S∈2[n] µ(S) = 1. The function µ is said to satisfy the positive lattice
Received by the editors July 17, 2007.
2000 Mathematics Subject Classiﬁcation. Primary 62H20; Secondary 05B35, 15A15, 15A22,
15A48, 26C10, 30C15, 32A60, 60C05, 60D05, 60E05, 60E15, 60G55, 60K35, 82B31.
Key words and phrases. Negative association, stable polynomials, hyperbolic polynomials,
determinants, matrices, spanning trees, matroids, probability measures, stochastic domination,
interacting particle systems, exclusion processes.
c
⃝2008 American Mathematical Society
Reverts to public domain 28 years from publication
521
522
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
condition [30, 65] if
(PLC)
µ(S)µ(T) ≤µ(S ∪T)µ(S ∩T)
for all S, T ⊆[n]. The corresponding probability measure (also denoted by µ) on
2[n] deﬁned by µ(A) = 
S∈A µ(S) is said to be positively associated if

Fdµ

Gdµ ≤

FGdµ
for any pair of increasing functions F, G on 2[n]. The latter is a strong correlation
inequality that yields many others as well as distributional limit theorems for models
of statistical mechanics such as the ferromagnetic Ising model or certain urn models
[63]. A fundamental result in the theory of positively associated random variables,
namely the FKG theorem [30], asserts that PLC implies positive association. This
is a powerful tool that allows veriﬁcation of (global) correlation inequalities from
the PLC property, which is a local condition and therefore often easier to check.
There are many important examples of negatively dependent “repelling” random
variables in probability theory, combinatorics, stochastic processes and statistical
mechanics: uniform random spanning tree measures [16], symmetric exclusion pro-
cesses [52, 55], random cluster models (with q < 1) [33, 42, 65], balanced and
Rayleigh matroids [20, 29, 68, 70, 72], competing urns models [26], etc; see, e.g.,
[45, 65] and the references therein for a discussion of some of these examples and
several others. To add to this list, in §3 we show that both the inequalities char-
acterizing multi-aﬃne real stable polynomials [8, 9, 15] and Hadamard-Fischer-
Kotelyansky type inequalities in matrix theory [28, 40, 39] may in fact be viewed
as natural manifestations of negative dependence properties.
The reverse of the PLC inequality gives the so-called negative lattice condition
(NLC)
µ(S)µ(T) ≥µ(S ∪T)µ(S ∩T)
for all S, T ⊆[n], while the usual deﬁnition of negative association for a probability
measure µ on 2[n] is the “negative” analog of positive association [65], namely the
inequality

Fdµ

Gdµ ≥

FGdµ
for any pair of increasing functions F, G on 2[n] depending on disjoint sets of coor-
dinates (note that the latter condition is important since by the Cauchy-Schwarz
inequality F and F are always positively correlated). However, negative dependence
is not nearly as robust as positive dependence. In particular, the NLC inequality
fails to imply negative association (see Example 2.1), and there is no known local-
to-global tool comparable to the FKG theorem in the theory of positive association.
Thus, no corresponding theory of negatively dependent events exists as yet, but,
as explained in [65], there certainly is a need for such a theory. In op. cit. Peman-
tle made a systematic study of measures on Boolean lattices with various negative
dependence properties. He proved certain relations between them and conjectured
numerous others, so as to pave the way for a theory of negative dependence. How-
ever, most open problems and conjectures are unresolved to this day, and the scope
of the positive results so far is quite restricted.
In this paper we introduce the class of strongly Rayleigh probability measures by
means of purely geometric conditions on the zero sets of their generating polyno-
mials that amount to the real stability of the latter (Deﬁnitions 2.9–2.10). As we
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS
523
show in §3, this class contains several important examples such as distributions at
time t ≥0 for symmetric exclusion processes generated by product or deterministic
measures [55] (or, more generally, by strongly Rayleigh measures), and determinan-
tal probability measures induced by positive contractions [5, 57]. Measures of the
latter type include e.g. uniform random spanning tree measures [16, 57] and arise
naturally in a variety of contexts pertaining to fermionic/determinantal point pro-
cesses and their continuous scaling limits, eigenvalues of random matrices, number
theory, non-intersecting paths, transfer current matrices, orthogonal polynomial
ensembles, etc.; see the discussion in §3.3 and the references therein. Note that the
topological dimension of the class of strongly Rayleigh probability measures on 2[n]
is 2n −1 ([10, Remark 3.1]) whereas the class of determinantal probability measures
has dimension n2, so the former is much larger than the latter. Of course, there are
also many examples of measures that satisfy some negative dependence property
but are not in the strongly Rayleigh class, e.g. Counterexample 1 in §7 and the
random cluster measure [33] whenever the graph contains a cycle; see §3.4.
The geometry underlying strongly Rayleigh measures provides us with power-
ful tools, such as fundamental complex analytic and geometric results of G˚arding
and Grace-Szeg¨o-Walsh, combinatorial/probabilistic results of Feder-Mihail, matrix
theoretic methods, and recent developments in the theory of stable polynomials
[7, 8, 9, 15] that we use in §4 to develop a complete theory of negative dependence
for this class of measures. Indeed, we show that strongly Rayleigh measures enjoy
all virtues of negative dependence, including the strongest form of negative asso-
ciation (CNA+). In particular, this allows us to prove several conjectures made
by Liggett [55], Pemantle [65], and Wagner [72], respectively, and to recover and
extend Lyons’ main results [57] on negative association and stochastic domination
for determinantal probability measures induced by positive contractions. Moreover,
we deﬁne a partial order on the set of strongly Rayleigh measures (by means of the
notion of proper position for multivariate stable polynomials studied in [7, 8, 9, 15])
and use it to settle Pemantle’s questions and conjectures on stochastic domination
for truncations of “negatively dependent” measures [65].
A series of conjectures, ﬁrst appearing in print in [65, Conjecture 4] but of ob-
scure folklore origin, states that the various negative dependent properties studied
in loc. cit. give rise to so-called ultra log-concave rank sequences (see §2.1 below for
the deﬁnition). Subsequently, in [72] one of these conjectures was coined “The Big
Conjecture” since it would imply the validity of Mason’s long-standing conjecture in
enumerative graph/matroid theory [62] for a large class of matroids. In §7 we con-
struct the ﬁrst counterexamples in the literature to all of these conjectures except
Mason’s, which once again conﬁrms the delicate nature of negative dependence.
After this work was made publicly available on www.arxiv.org, other counterex-
amples to some of these conjectures were reported [48, 60]. Markstr¨om [60] proved
that negative association does not imply unimodality, and Kahn-Neiman [48] later
showed that not even strong negative association (CNA+) implies unimodality.
Note that the rank sequence of the CNA+ measure constructed in Counterexample
1 of §7 is neither ultra nor strong log-concave but it is log-concave.
The problem of describing natural negative dependence properties that are pre-
served by symmetric exclusion evolutions has attracted some attention in the theory
of interacting particle systems and Markov processes [52, 54, 55]. In §4.4 we prove
524
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
that the class of strongly Rayleigh measures is invariant under partial symmetriza-
tion (this and several other properties fail, for example, for Rayleigh measures). As
a consequence, in §5 we provide an answer to the aforementioned problem and show
that if the initial distribution of a symmetric exclusion process is strongly Rayleigh,
then so is the distribution at time t ≥0; therefore, by the results in §4.2, the latter
distribution is strongly negatively associated (CNA+). In particular, this solves an
open problem of Pemantle [65] and Liggett [55] stating that the distribution of a
symmetric exclusion process at time t ≥0 with non-random/deterministic initial
conﬁguration is negatively associated, and shows that the same is actually true
whenever the initial distribution is strongly Rayleigh. In a later paper [56], Liggett
has applied these results to prove convergence to the normal and Poisson laws for
various functionals of the symmetric exclusion process.
In §6 we establish equivalences between several negative dependence properties
for the class of almost symmetric/exchangeable measures that we deﬁne in §2.1.
This extends Pemantle’s corresponding theorem for symmetric measures and con-
ﬁrms his conjecture on strong negative association (CNA+) in the almost exchange-
able case. The results in §6 are also useful in §7, as they allow us to show that the
examples we construct there provide counterexamples to the series of conjectures on
ultra log-concave rank sequences proposed in [65, 72] to which we already alluded.
We note that Corollary 6.6 in §6 was subsequently proved by diﬀerent methods in
[48], where it was additionally shown that almost exchangeable measures satisfy
the (strong) Feder-Mihail property.
The aforementioned connections between the negative dependence properties
satisﬁed by strongly Rayleigh measures and the geometry of zero sets of their gen-
erating polynomials are much in the same spirit as e.g. Rota’s philosophy about
the ubiquity of zeros of polynomials in combinatorics [67]. In the present context,
these connections actually prove to have fruitful consequences for both the theory
of negative dependence and the theory of real stable and hyperbolic polynomials, as
they give new insight and further potential applications in these and related areas.
