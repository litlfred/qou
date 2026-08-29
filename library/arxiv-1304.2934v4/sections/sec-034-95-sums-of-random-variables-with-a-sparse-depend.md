---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-034-95-sums-of-random-variables-with-a-sparse-depend
section_title: "Sums of random variables with a sparse dependency graph"
section_number: 9.5
pages: 78-81
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
plication of Theorem 9.7 is the following general result on sums of weakly dependent
random variables, to be compared with [Pen02, §2.3]. Let Xn = ∑Nn
i=1 Yi be a sum of
random variables, where the Yi’s have a dependency graph of degreeDn− 1, and sat-
isfy‖Yi‖∞ ≤ A for some A≥ 0 (independent of i). We also assume that Xn is not
deterministic, so that its variance is non-zero.
Theorem 9.19. We assume that the dependency graph of (Yi)1≤i≤Nn is sparse, in the sense
that limn→∞ Dn
Nn = 0.
(1) There exists a positive constant C such that, for all r≥ 2,
⏐⏐⏐κ(r)
(
Xn
Dn
)⏐⏐⏐≤ (Cr)r Nn
Dn .
(2) Consider the bounded sequences
σ2
n = Dn
Nn
κ(2)
( Xn
Dn
)
; Ln = σ3
n
Dn
Nn
κ(3)
( Xn
Dn
)
.
If they have limits σ2 > 0 and L, then
Xn− E[Xn]
Dn σn
( Dn
Nn
)1/3
MOD-φ CONVERGENCE, I 79
converges in the mod-Gaussian sense with parameters tn = ( Nn/Dn)1/3 and limiting
function ψ(z) = exp(Lz3/6).
(3) If furthermore,
σ2
n = σ2
(
1 + o
(
(Dn/Nn)1/3
))
,
then the variable
Xn− E[Xn]
Dn σ
( Dn
Nn
)1/3
converges in the mod-Gaussian sense with parameters (Nn/Dn)1/3 and limiting func-
tion ψ(z) = exp(Lz3/6) (the difference with the previous item is that σn has been
replaced by σ).
Of course, if (2) holds, then the results of this paper imply that
• Xn/(σn
√NnDn) satisﬁes a central limit theorem, with a normality zone of size
o
((
Dn
Nn
)1/6)
;
• furthermore, for x > 0,
P[Xn− E[Xn]≥ (Nn)2/3 (Dn)1/3 σn x] = e−( Nn
Dn )
1/3 x2
2
x
√
2π(Nn/Dn)1/3 exp
( Lx3
6
)
(1 + o(1))
(48)
and a similar result holds for negative deviations.
The same holds replacing σn by σ if one has the assumption on the speed of conver-
gence of σn towards σ, given in the third item of Theorem 9.19. If, moreover, the cumu-
lants of Xn satisfy (26), then (48) still holds when we replace x by a positive sequence
xn tending to inﬁnity with xn = o(Nn/Dn)1/12 — see Proposition 5.2.
order of ﬂuctuations
moderate deviations (0 < x):
P
[
Xn−E[Xn]
σ (Nn)2/3(Dn)1/3≥ x
]
≃
exp(−( Nn
Dn )1/3 x2
2 )
x
√
2π( Nn
Dn )1/3
exp
(
Lx3
6
)
;
central limit theorem (y≪ ( Nn
Dn )1/6):
P
[
Xn−E[Xn]
σ√Nn Dn
≥ y
]
≃ P[NR(0, 1)≥ y].
O((Nn)2/3(Dn)1/3)
O((Nn)1/2(Dn)1/2)
FIGURE 11. Panorama of the ﬂuctuations of a sum of Nn random vari-
ables that have a sparse dependency graph, of degree Dn− 1 with
limn→∞ Dn
Nn = 0.
80 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
Notice that in the case of independent random variables, Dn = 1 and we recover the
mod-Gaussian convergence of Example 2.2.
In the next Sections, we shall study some particular cases of Theorem 9.19. We will
see that most computations are related to the asymptotic analysis of the ﬁrst cumulants
of Xn.
10. S UBGRAPH COUNT STATISTICS IN ERDÖS -R ÉNYI RANDOM GRAPHS
In this section, we consider Erdös-Rényi model Γ(n, pn) of random graphs. A ran-
dom graph Γ with this distribution is described as follows. Its vertex set is [n] and for
each pair{i, j}⊂ [n] with i⁄= j, there is an edge between i and j with probability pn.
Moreover, all these events are independent. We are then interested in the following
random variables, called subgraph count statistics . If γ is a ﬁxed graph of size k, then
X(n)
γ is the number of copies of γ contained in the graph Γ(n, pn) (a more formal deﬁ-
nition is given in the next paragraph). This is a classical parameter in random graph
theory; see, e.g., the book of S. Janson, T. Łuczak and A. Ruci ´ nski [JŁR00].
The ﬁrst result on this parameter was obtained by P . Erdös and A. Rényi,cf. [ER60].
They proved that, if γ belongs to some particular family of graphs (called balanced),
one has a threshold: namely,
lim
n→∞
P[X(n)
γ > 0] =
{
0 if pn = o
(
n−1/m(γ)
)
;
1 if n−1/m(γ) = o(pn),
where m(γ) =|E(γ)|/|V(γ)|. This result was then generalized to all graphs by B. Bol-
lobás [Bol01], but the parameterm(γ) is in general more complicated than the quotient
above. Consider the case n−1/m(γ) = o(pn), when the graph Γ(n, pn) contains with
high probability a copy of γ. It was then proved by A. Ruci ´ nski (see [Ruc88]) that, un-
der the additional assumption n2(1− pn)→ ∞, the ﬂuctuations of X(n)
γ are Gaussian.
This result can be obtained using dependency graphs; see e.g. [JŁR00, pages 147-152].
Here, we consider the case where pn = p is a constant sequence (0 < p < 1). The
possibility of relaxing this hypothesis is discussed in Subsection 10.3.3. Denoteαn = n2
and βn = nk−2, where k is the number of vertices of γ. It is easy to check that
E[X(n)
γ ] = c αn βn ; Var (X(n)
γ ) = σ2 αn (βn)2
for some positive constants c and σ — see, e.g., [JŁR00, Lemma 3.5]. Hence, Ruci ´ nski’s
central limit theorem asserts that, if T∼ x√αn for some ﬁxed real x, then
lim
n→∞
P
[
X(n)
γ − E[X(n)
γ ]
βn
≥ T
]
= 1√
2π
∫ x/σ
−∞
e−u2/2du.
Using Theorem 9.7, we shall extend this result to a framework wherex tends to inﬁnity,
but not to quickly: (αn)1/2≪ T≪ (αn)3/4.
Theorem 10.1. Let 0 < p < 1 and γ be a graph with k vertices. We consider X(n)
γ the number
of copies of γ contained in Erdös-Rényi random graph Γ(n, p). Let αn and βn be deﬁned as
above.
MOD-φ CONVERGENCE, I 81
(1) The renormalized variable (X(n)
γ − E[X(n)
γ ])/(α1/3
n βn) converges mod-Gaussian with
parameters tn = σ2 α1/3
n and limiting function ψ(z) = exp
( L
6 z3)
, where σ and L are
computed in Section 10.3.2. The convergence takes place on the whole complex plane
with speed of convergence o(α−1/3
n ).
(2) Therefore, (X(n)
γ − E[X(n)
γ ])/(α1/2
n βn) converges in distribution towards a Gaussian
law, with normality zone o (α1/6
n ). Moreover, the deviation probabilities at the edge of
the normality zone and at a slightly larger scale are given as follows: is x n is a positive
sequence bounded away from 0 with xn = o
(
α1/12
n ), then
P
[
X(n)
γ − E[X(n)
γ ]
α1/2
n βn
≥ σ2α1/6
n xn
]
= e− (xn)2(αn)1/3 σ2
2
xn(αn)1/6σ
√
2π
e
L(xn)3
6 (1 + o(1)).
P
[
X(n)
γ − E[X(n)
γ ]
α1/2
n βn
≤− σ2α1/6
n xn
]
= e− (xn)2(αn)1/3 σ2
2
xn(αn)1/6σ
√
2π
e
−L(xn)3
6 (1 + o(1)).
A similar result has been obtained by H. Döring and P . Eichelsbacher in [DE13b,
Theorem 2.3]. However,
• their result is less precise as they only obtain the equivalence of the logarithms
of the relevant quantities (in particular, when we look at the logarithm, the sec-
ond factor of the right-hand side is negligible);
• and they cover a smaller zone of deviation.
Unfortunately, we cannot get deviation results when xn∼ tα1/3
n for some real num-
ber t; this would amount to evaluate P[X(n)
γ > (1 + ε) E[X(n)
γ ]]. For large deviations
equivalents of
log P[X(n)
γ > (1 + ε) E[X(n)
γ ]],
there is a quite large literature, see [CV11, Theorem 4.1] and [Cha12] for recent results
in this ﬁeld. As we consider deviations of a different scale, our result is neither im-
plied by, nor implies these results. Note, however, that their large deviation results are
equivalents of the logarithm of the probability, while our statement is an equivalent for
the probability itself.
