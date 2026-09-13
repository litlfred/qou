---
doc_id: arxiv-1202.5426v2
doc_title: "Hard analysis meets critical knots Stationary points of the M öbius energy are smooth S. Blatt∗ Φ. Reiter∗∗ A. Schikorra∗∗∗"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1202.5426v2.pdf
source_sha256: 6c7668ad72e33b4b
doc_brief: "Hard analysis meets critical knots Stationary points of the M öbius energy are smooth S. Blatt∗ Φ. Reiter∗∗ A. Schikorra∗∗∗ — 5 sections: Front matter; Introduction; Euler-Lagrange equation: Proof of"
---
2. Euler-Lagrange equation: Proof of Theorem I 5
3. Initial regularity: Proof of Theorem III 16
4. Bootstrapping: Proof of Theorem IV 32
A. Appendix 37
∗Simon Blatt, Mathematics Institute, Zeeman Building, University of Warwick, Coventry CV4 7AL, United King-
dom, S.Blatt@warwick.ac.uk
∗∗Philipp Reiter, Abteilung f¨ ur Angewandte Mathematik, Universit¨ at Freiburg, Hermann-Herder-Straße 10, 79104
Freiburg i. Br., Germany,reiter@mathematik.uni-freiburg.de
∗∗∗Armin Schikorra, Max-Planck Institute for Mathematics in t he Sciences, Inselstr. 22, 04103 Leipzig, Germany,
armin.schikorra@mis.mpg.de
1
1. Introduction
To ﬁnd nice geometric representatives within a given knot cl ass, several new energies have
been invented in the last two decades. The earliest knot ener gy for smooth curves was the
so-called M¨ obius energyintroduced by Jun O’Hara in [O’H91],
E(2)(γ) :=
∫
R/ Z
1/ 2∫
−1/ 2
( 1
|γ(u +w)−γ(u)|2− 1
dγ(u +w, u)2
)⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐γ′(u)
⏐⏐⏐dw du
which was later on extended to the family of energies
E(α,p)(γ) :=
∫
R/ Z
1/ 2∫
−1/ 2
( 1
|γ(u +w)−γ(u)|α− 1
dγ(u +w, u)α
)p ⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐γ′(u)
⏐⏐⏐dw du
forα,p∈ [1,∞), see [O’H94]. Here dγ(u+w, u) denotes the intrinsic distance betweenγ(u+w)
andγ(u) on the curveγ. More precisely,
dγ(u +w, u) := min(L (γ|[u, u+w]), L (γ)− L (γ|[u, u+w])) (1.1)
provided|w|≤ 1
2 where L (γ) :=
∫1
0 |γ′(θ)| dθis the length ofγ.
Crucially using the M¨ obius invariance of this knot energy,Michael Freedman, Zheng-Xu He,
and Zhenghan Wang [ FHW94] were able to show that there are minimizers of the M¨ obius
energy within every prime knot class and that these are in fac t of class C1, 1. More precisely,
they could show that if γis a local minimizer with respect to the L∞-topology, and if γis
parametrized by arc length, then γis C1, 1. Together with a bootstrapping argument due to
He [ He00], one then obtains that local minimizers of the M¨ obius ener gy are smooth, also
see [Rt10].
Unfortunately, motivated by numerical evidence, Rob Kusne r and John Sullivan were led to
conjecture that there are no minimizers within composite kn ot classes [KS97]. In contrast to
that, there are minimizers of the energies E(α,p) in the case that jp > 2 as shown in [O’H94].
In this article, we will prove that even only stationary poin ts of the M¨ obius energy are of
class C∞ under the mildest condition one can think of: that E(2)(γ) is ﬁnite - an assumption
which, as shown in a recent work of the ﬁrst author [ Bla12], is equivalent to assuming that γ
is an injective curve of class H
3
2 (R/ Z, Rn). Our motivation to do so is twofold: First of all, of
course, this is a much stronger result than the smoothness oflocal minimizers as stated above.
Secondly, the M¨ obius invariance is not essential for proving smoothness of local minimizers
as we do not need it in our arguments. Thus there is the chance t o study other, possibly
not M¨ obius invariant, critical knot energies, using the te chniques developed in this article.
Additionally, our arguments are not restricted to the one-d imensional situation but can be
applied to arbitrary dimensions.
2
The price we pay is that, instead of the very appealing geomet ric argument in [ FHW94],
we have to adapt some sophisticated techniques originally d eveloped by Tristan Rivi` ere and
Francesca Da Lio [DLR11a, DLR11b, DL11] and the third author [Sch12, Sch11] to deal with
n
2- harmonic maps into manifolds.
The ﬁrst task in order to prove this result, is to derive the Eu ler-Lagrange equation for such
stationary points. In [ FHW94], it was shown that for simple closed curves γ∈ C1, 1(R/ Z, Rn)
and h∈ C1, 1(R/ Z, Rn) we have
δE(2)(γ; h) := lim
τց0
E(2)(γ+τh)− E(2)(γ)
τ
=
∫
R/ Z
∫
R/ Z

γ′(u)h′(u)− ⟨γ(u)−γ(v), h(u)−h(v)⟩
|γ(u)−γ(v)|2
|γ(u)−γ(v)|2
|γ′(v)||γ′(u)| dv du.
We will show that this formula is still valid under the weaker assumption thatγ∈ H3/ 2(R/ Z,
Rn) withγ′∈ L∞, i.e., for arc-length parametrized γwe only assume that the M¨ obius energy
is ﬁnite. We call a curve regular if there is a positive constant c = c(γ) with|γ′(x)|≥ c for all
x∈ R/ Z.
Theorem I (E(2) ∈C1(H3/2
ir ∩H1,∞)). The energy E (2) is continuously diﬀerentiable on the
space of injective and regular curves belonging to H 3/ 2∩ H1,∞. Furthermore, if γ∈ H3/ 2 is
injective and parametrized by arc-length andϕ∈ H3/ 2∩ H1,∞ the ﬁrst variation
δE(2)(γ;ϕ) := lim
τ→0
E(2)(γ+τϕ)− E(2)(γ)
τ
exists and equals
2 lim
εց0
/iintegdisplay
Uε
(⟨γ′(u),ϕ′(u)⟩−⟨γ(u +w)−γ(u),ϕ(u +w)−ϕ(u)⟩
|γ(u +w)−γ(u)|2
) dw du
|γ(u +w)−γ(u)|2
where
Uε:= R/ Z×
(
[− 1
2,−ε]∪ [ε,1
2]
)
. (1.2)
Though the space H3/ 2∩ H1,∞ seems somewhat artiﬁcial at ﬁrst sight, it just guarantees t hat
we do not use bad parametrizations of our curves. The proof ofthis result is similar to [BR12].
We will then use the resulting Euler-Langrange equation for stationary points of the M¨ obius
energy to prove that these points are smooth:
Theorem II (Stationary points are smooth). Any stationary pointγ∈ H
3
2 (R/ Z, Rn) of E(2),
i.e., any curveγ∈ H
3
2 (R/ Z, Rn) for which
δE(2)(γ; h) = 0 for all h∈ C∞(R/ Z, Rn),
belongs to C∞ when parametrized by arc-length.
3
In [BR12], improving a previous result [ Rt12], the smoothness of stationary points of ﬁnite
energy was already shown for the case of E(α) := E(α,1), α∈ (2, 3), instead of the M¨ obius
energy. It is worth noting, that those energies lead to a subcritical Euler-Langrage equation,
and that in some sense the regularity theory can be based on Sobolev embeddings for fractional
Sobolev and Besov spaces. In contrast to this, the Euler-Lag range equation of the M¨ obius
energy is critical. As for well-known critical geometric equations – like the E uler-Lagrange
equation of the Willmore functional, see, e.g., [Sim93, Riv08], or harmonic maps on R2, see,
e.g., [H´ el91, Riv07], – one has ﬁrst to ﬁnd a way to gain an εof additional regularity (via
gaining a δof additional integrability) and then start a bootstrappin g argument. That is, in a
quite natural way, the proof of Theorem II is an immediate consequence of two technically
independent steps:
Theorem III (Initial regularity). Letγ∈ H
3
2 (R/ Z, Rn),γ′∈ Sn−1, be a stationary point of
the M¨ obius energy, i.e. satisfyingδE(2)(γ,ϕ) = 0 for allϕ∈ C∞(R/ Z, Rn). Then γ∈ C1,α, for
someα> 0, andγ∈ H
3
2, p(R/ Z, Rn) for some p > 2.
Theorem IV (Bootstrapping). For some p > 2, let γ∈ H
3
2, p(R/ Z, Rn), γ′ ∈ Sn−1, be a
stationary point of the M¨ obius energy. Thenγis smooth.
Theorem III is proven in Section3, Theorem IV in Section 4. While Theorem IV relies mainly
on bringing together Sobolev embeddings and standard commu tator estimates for Bessel po-
tential spaces with techniques developed in [Bla12], some very delicate estimates are needed
to get anything more than the critical and initial regularit y H
3
2 for stationary points as stated
in Theorem III.
Both theorems rely on a decomposition of the ﬁrst variation d ating back to [ He00, For-
mula (4.5)] which already proved to be helpful in the analysi s of the functionals E(α) forα∈
(2, 3) (cf. [BR12]) and the gradient ﬂow of the energies E(α) forα∈ [2, 3) [Bla11a, Bla11b].
For f,g : R→ Rn,ε>0 let
Qε( f,g ) :=
1∫
0
∫
[− 1
2, 1
2 ]\(−ε,ε)
(
⟨f′(u),g ′(u)⟩w2−⟨f (u +w)− f (u),g (u +w)−g(u)⟩
)dw
w4 du,
(1.3)
T1( f,g ) :=−
1∫
0
1
2∫
− 1
2
⟨f′(u), g′(u)⟩
( 1
| f (u +w)− f (u)|2− 1
|w|2
)
dw du, (1.4)
4
and
T2( f,g ) :=
1∫
0
1
2∫
− 1
2
⟨f (u +w)− f (u), g(u +w)−g(u)⟩
( 1
| f (u +w)− f (u)|4− 1
|w|4
)
dw du.
(1.5)
From Theorem I we deduce that a critical knot γ∈ H
3
2 (R/ Z, Rn), parametrized by arc length,
satisﬁes
Q(γ,h) := lim
ε→0
Qε(γ,h) = T1(γ,h) + T2(γ,h) for all h∈ C∞(R/ Z). (1.6)
This is the form of the Euler-Lagrange equation, with which w e will work in the proofs of
Theorem III and Theorem IV.
Let us conclude this introduction by remarking that, in cont rast to stationary points of E(α,1),
for p > 1 we do not expect stationary points of E(α,p) to be C∞-smooth: The resulting Euler-
Lagrange equation should be in some sense a nonlocal degener ate elliptic equation. Keeping
in mind the regularity theory for elliptic degenerate equat ions, one might expect nevertheless
that stationary points are at least a bit more regular than anarbitrary ﬁnite-energy curve alone.
Acknowledgements. The ﬁrst author was supported by Swiss National Science Foun da-
tion Grant Nr. 200020 125127 and the Leverhulm trust. The second author was suppor ted
by DFG Transregional Collaborative Research Centre SFB TR 7 1. The third author has re-
ceived funding from the European Research Council under the European Union’s Seventh
Framework Programme (FP7/2007-2013) / ERC grant agreement no 267087, DAAD PostDoc
Program (D/10/50763) and the Forschungsinstitut f¨ ur Mathematik, ETH Z¨ urich. He would
like to thank Tristan Rivi` ere and the ETH for their hospitality.
