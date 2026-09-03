---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — W e introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polyno mials that amount"
---
2. A Plethora of Negative Dependence Properties and Conjecture s 4
2.1. Negative Dependence Concepts 4
2.2. Strongly Rayleigh Measures 9
2.3. Symmetric Homogenization 10
2.4. Measures on countably inﬁnite sets 10
2.5. Towards a Theory of Negative Dependence: Problems and Solut ions 11
3. Negative Dependence in Mathematics and Physics 13
3.1. Real Stable Polynomials and Transcendental Entire Functions 1 3
3.2. Hadamard-Fischer Inequalities and GKK-Matrices 15
3.3. Determinantal Probability Measures 17
3.4. Graphs, Laplacians, Spanning Trees and the Random Cluster Mo del 18
3.5. Interacting Particle Systems and Exclusion Evolutions 20
4. Negative Dependence Theory for Strongly Rayleigh Measures 21
4.1. Symmetric Homogenization via G ˚ arding Hyperbolic Polynomials 21
4.2. Stability Implies Negative Association 24
4.3. Stochastic Domination and Truncations 25
4.4. The Partial Symmetrization Procedure 29
5. Preservation of Negative Dependence by Symmetric Exclusion Pr ocesses 31
6. Almost Exchangeable Measures 33
7. Negative Results on Negative Dependence 41
References 45
2000 Mathematics Subject Classiﬁcation. Primary 62H20; Secondary 05B35, 15A15, 15A22,
15A48, 26C10, 30C15, 32A60, 60C05, 60D05, 60E05, 60E15, 60G 55, 60K35, 82B31.
Key words and phrases. Negative association, stable polynomials, hyperbolic pol ynomials,
determinants, matrices, spanning trees, matroids, probab ility measures, stochastic domination,
interacting particle systems, exclusion processes.
1
2 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
1. Introduction
Let µ : 2 [n] → R, [ n] = {1, . . . , n}, be a function attaining nonnegative values
and satisfying∑
S∈2[n] µ(S) = 1. The function µ is said to satisfy the positive lattice
condition [30, 65] if
µ(S)µ(T ) ≤ µ(S ∪ T )µ(S ∩ T ) (PLC)
for all S, T ⊆ [n]. The corresponding probability measure (also denoted by µ) on
2[n] deﬁned by µ(A) =∑
S∈A µ(S) is said to be positively associated if
∫
F dµ
∫
Gdµ ≤
∫
F Gdµ
for any pair of increasing functions F, G on 2 [n]. The latter is a strong correlation
inequality that yields many others as well as distributional limit theore ms for models
of statistical mechanics such as the ferromagnetic Ising model or certain urn models
[63]. A fundamental result in the theory of positively associated ran dom variables,
namely the FKG theorem [30], asserts that PLC implies positive associa tion. This
is a powerful tool that allows veriﬁcation of (global) correlation ineq ualities from
the PLC property, which is a local condition and therefore often ea sier to check.
There are many important examples of negatively dependent “repelling” random
variables in probability theory, combinatorics, stochastic process es and statistical
mechanics: uniform random spanning tree measures [16], symmetric exclusion pro-
cesses [52, 55], random cluster models (with q < 1) [33, 42, 65], balanced and
Rayleigh matroids [20, 29, 68, 70, 72], competing urns models [26], et c; see, e.g.,
[45, 65] and references therein for a discussion of some of these e xamples and several
others. To add to this list, in §3 we show that both the inequalities characterizing
multi-aﬃne real stable polynomials [8, 9, 15] and Hadamard-Fischer- Kotelyansky
type inequalities in matrix theory [28, 40, 39] may in fact be viewed as n atural
manifestations of negative dependence properties.
The reverse of the PLC inequality gives the so-called negative lattice condition
µ(S)µ(T ) ≥ µ(S ∪ T )µ(S ∩ T ) (NLC)
for all S, T ⊆ [n], while the usual deﬁnition of negative association for a probability
measure µ on 2 [n] is the “negative” analog of positive association [65], namely the
inequality ∫
F dµ
∫
Gdµ ≥
∫
F Gdµ
for any pair of increasing functions F, G on 2 [n] depending on disjoint sets of coor-
dinates (note that the latter condition is important since by the Cau chy-Schwarz
inequality F and F are always positively correlated). However, negative dependence
is not nearly as robust as positive dependence. In particular, the N LC inequality
fails to imply negative association (see Example 2.1), and there is no known local-
to-global tool comparable to the FKG theorem in the theory of pos itive association.
Thus, no corresponding theory of negatively dependent events e xists as yet but, as
explained in [65], there certainly is a need for such a theory. In op. cit. Pemantle
made a systematic study of measures on Boolean lattices with variou s negative
dependence properties. He proved certain relations between the m and conjectured
numerous others, so as to pave the way for a theory of negative d ependence. How-
ever, most open problems and conjectures are unresolved to this day, and the scope
of the positive results so far is quite restricted.
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 3
In this paper we introduce the class of strongly Rayleigh probability measures by
means of purely geometric conditions on the zero sets of their gene rating polyno-
mials that amount to the real stability of the latter (Deﬁnitions 2.9–2 .10). As we
show in §3, this class contains several important examples such as distribut ions at
time t ≥ 0 for symmetric exclusion processes generated by product or det erministic
measures [55] (or, more generally, by strongly Rayleigh measures) , and determinan-
tal probability measures induced by positive contractions [5, 57]. M easures of the
latter type include e.g. uniform random spanning tree measures [16 , 57] and arise
naturally in a variety of contexts pertaining to fermionic/determina ntal point pro-
cesses and their continuous scaling limits, eigenvalues of random mat rices, number
theory, non-intersecting paths, transfer current matrices, o rthogonal polynomial
ensembles, etc; see the discussion in §3.3 and references therein. Note that the
topological dimension of the class of strongly Rayleigh probability mea sures on 2 [n]
is 2 n − 1 ([10, Lemma 4.1]) whereas the class of determinantal probability me asures
has dimension n2, so the former is much larger than the latter. Of course, there ar e
also many examples of measures that satisfy some negative depend ence property
but are not in the strongly Rayleigh class, e.g. Counterexample 1 in §7 and the
random cluster measure [33] whenever the graph contains a cycle, see §3.4.
The geometry underlying strongly Rayleigh measures provides us wit h power-
ful tools – such as fundamental complex analytic and geometric res ults of G ˚ arding
and Grace-Szeg¨ o-Walsh, combinatorial/probabilistic results of Feder-Mihail, matrix
theoretic methods, and recent developments in the theory of sta ble polynomials
[7, 8, 9, 15] – that we use in §4 to develop a complete theory of negative depen-
dence for this class of measures. Indeed, we show that strongly R ayleigh measures
enjoy all virtues of negative dependence, including the strongest form of negative
association (CNA+). In particular, this allows us to prove several c onjectures made
by Liggett [55], Pemantle [65], and Wagner [72], respectively, and to re cover and
extend Lyons’ main results [57] on negative association and stocha stic domination
for determinantal probability measures induced by positive contra ctions. Moreover,
we deﬁne a partial order on the set of strongly Rayleigh measures ( by means of the
notion of proper position for multivariate stable polynomials studied in [7, 8, 9, 15]),
and use it to settle Pemantle’s questions and conjectures on stoch astic domination
for truncations of “negatively dependent” measures [65].
A series of conjectures, ﬁrst appearing in print in [65, Conjecture 4] but of ob-
scure folklore origin, states that the various negative dependent properties studied
in loc. cit. give rise to so-called ultra log-concave rank sequences (see §2.1 below for
the deﬁnition). Subsequently, in [72] one of these conjectures wa s coined “The Big
Conjecture” since it would imply the validity of Mason’s long-standing c onjecture in
enumerative graph/matroid theory [62] for a large class of matro ids. In §7 we con-
struct the ﬁrst counterexamples in the literature to all of these c onjectures except
Mason’s, which once again conﬁrms the delicate nature of negative d ependence.
After this work was made publically available on www.arxiv.org other counterex-
amples to some of these conjectures have been reported [48, 60 ]. Markstr¨ om [60]
proved that negative association does not imply unimodality and Kahn -Neiman [48]
later showed that not even strong negative association (CNA+) imp lies unimodality.
Note that the rank sequence of the CNA+ measure constructed in Counterexample
1 of §7 is neither ultra nor strong log-concave but it is log-concave.
4 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
The problem of describing natural negative dependence propertie s that are pre-
served by symmetric exclusion evolutions has attracted some atte ntion in the the-
ory of interacting particle systems and Markov processes [52, 54, 55]. In §4.4 we
prove that the class of strongly Rayleigh measures is invariant unde r partial sym-
metrization (this and several other properties fail for e.g. Rayleig h measures). As a
consequence, in §5 we provide an answer to the aforementioned problem and show
that if the initial distribution of a symmetric exclusion process is stro ngly Rayleigh,
then so is the distribution at time t ≥ 0; therefore, by the results in §4.2, the latter
distribution is strongly negatively associated (CNA+). In particular , this solves an
open problem of Pemantle [65] and Liggett [55] stating that the distr ibution of a
symmetric exclusion process at time t ≥ 0 with non-random/deterministic initial
conﬁguration is negatively associated, and shows that the same is a ctually true
whenever the initial distribution is strongly Rayleigh. In a later paper [56], Liggett
has applied these results to prove convergence to the normal and Poisson laws for
various functionals of the symmetric exclusion process.
In §6 we establish equivalences between several negative dependence properties
for the class of almost symmetric/exchangeable measures that we deﬁne in §2.1.
This extends Pemantle’s corresponding theorem for symmetric mea sures and con-
ﬁrms his conjecture on strong negative association (CNA+) in the a lmost exchange-
able case. The results in §6 are also useful in §7, as they allow us to show that the
examples we construct there provide counterexamples to the ser ies of conjectures
on ultra log-concave rank sequences proposed in [65, 72] that we already alluded
to. We note that Corollary 6.6 in §6 was subsequently proved by diﬀerent methods
in [48], where it was additionally shown that almost exchangeable measu res satisfy
the (strong) Feder-Mihail property.
The aforementioned connections between the negative dependen ce properties
satisﬁed by strongly Rayleigh measures and the geometry of zero s ets of their gen-
erating polynomials are much in the same spirit as e.g. Rota’s philosophy about
the ubiquity of zeros of polynomials in combinatorics [67]. In the pres ent context,
these connections actually prove to have fruitful consequences for both the theory
of negative dependence and the theory of real stable and hyperb olic polynomials, as
they give new insight and further potential applications in these and related areas.
