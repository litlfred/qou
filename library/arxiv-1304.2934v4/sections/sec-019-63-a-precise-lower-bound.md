---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-019-63-a-precise-lower-bound
section_title: "A precise lower bound"
section_number: 6.3
pages: 47-48
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
P[Xn∈ tnB], and in view of the classical theory of large deviations, this lower bound
should be related to open sets and to the exponent F(Bo). Unfortunately, the result
takes a less interesting form than Theorem 6.3. If B is a Borelian subset of R, denote Bδ
the union of the open intervals (x, x + κ) of width κ≥ δ that are included into B. The
interior O = Bo is a disjoint union of a countable collection of open intervals, and also
the increasing union⋃
δ>0 Bδ.
b O
Fφ
3
FIGURE 7. In some problematic situations, one is only able to prove a
non-precise lower bound for large deviations.
However, the topology of Bo may be quite intricate in comparison to the one of the
Bδ’s, as some points can be points of accumulation of open intervals included inB and
of width going to zero (see Figure 7). This phenomenon prevents us to state a precise
lower bound when one of this point of accumulation is a = sup(Bo∩ (−∞, η′(0)]) or
b = inf(Bo∩ [η′(0), +∞)). Nonetheless, the following is true:
Theorem 6.4. For an admissible Borelian set B,
lim inf
δ→0
lim inf
n→∞
(√
2πtn exp(tnF(Bδ)) P[Xn∈ tnB]
)
≥



∑a∈(Bo)min
ψ(h(a))
(1−e−|h(a)|)
√
η′′(h(a))
∑a∈(Bo)min
ψ(h(a))
|h(a)|
√
η′′(h(a)) ,
with the usual distinction of lattice/non-lattice cases. In particular, the right-hand side in
Theorem 6.3 is the limit of √2πtn exp(tnF(B)) P[Xn∈ tnB] as soon as F (Bδ) = F(B) for
some δ > 0.
Proof. Again we deal with the non-lattice case, and we suppose for instance that the
set (Bo)min consists of one point b = inf(Bo∩ [η′(0), +∞)), the other situations being
entirely similar. As δ goes to 0, Bδ increases towards Bo = ⋃
δ>0 Bδ, so the inﬁmum
F(Bδ) decreases and the quantity
L(δ) = lim inf
n→∞
(√
2πtn exp(tnF(Bδ)) P[Xn∈ tnB]
)
is decreasing in δ. Actually, if bδ = inf(Bδ∩ [η′(0), +∞)), then for δ small enough
F(Bδ) = F(bδ), so limδ→0 F(Bδ) = F(Bo) by continuity of F. On the other hand,
R(δ) = ψ(h(bδ))
h(bδ)
√
η′′(h(bδ))
48 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
tends to the same quantity with b instead of bδ. Hence, it sufﬁces to show that for δ
small enough, L(δ)≥ R(δ). However, by deﬁnition of Bδ, the open interval (bδ, bδ + δ)
is included into B, so
P[Xn∈ tnB]≥ P[Xn∈ tnBδ]≥ P[Xn > tnbδ]− P[Xn≥ tn(bδ + δ)]
≥
(
ψ(h(bδ)) e−tnF(bδ)
h(bδ)
√
2πtnη′′(h(bδ))
− ψ(h(bδ + δ)) e−tnF(bδ+δ)
h(bδ + δ)
√
2πtnη′′(h(bδ + δ))
)
(
1 + o(1)
)
≥ ψ(h(bδ)) e−tnF(bδ)
h(bδ)
√
2πtnη′′(h(bδ))
(
1 + o(1)
)
since the second term on the second line is negligible in comparison to the ﬁrst term —
F(bδ + δ) > F(bδ). This ends the proof. □
7. E XAMPLES WITH AN EXPLICIT GENERATING FUNCTION
The general results of Sections 3 and 6 can be applied in many contexts, and the
main difﬁculty is then to prove for each case that one has indeed the estimate on the
Laplace transform given by Deﬁnition 1.1. Therefore, the development of techniques
to obtain mod- φ estimates is an important part of the work. Such an estimate can
sometimes be established from an explicit expression of the Laplace transform (hence
of the characteristic function); we give several examples of this kind in Section 7.1. But
there also exist numerous techniques to study sequences of random variables without
explicit expression for the characteristic function: complex analysis methods in num-
ber theory (Section 7.2) and in combinatorics (Section 7.3), localization of zeros (Section
8) and dependency graphs (Sections 11, 10 and 9) to name a few. These methods are
known to yield central limit theorems and we show how they can be adapted to prove
mod-convergence. We illustrate each case with one or several example(s).
In this section, we detail examples for which the mod- φ convergence has already
been proved before (cf. [JKN11, DKN11]) or follows easily from formulas in the litera-
ture.
