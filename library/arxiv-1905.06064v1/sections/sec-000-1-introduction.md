---
doc_id: arxiv-1905.06064v1
doc_title: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1905.06064v1.pdf
source_sha256: 3ffe25c8ee62779d
doc_brief: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS — We develop a regularity theory for extremal knots of scale invariant knot ener- gies deﬁned by J. O’hara in 1991."
---
2. A new energy Eα,p 4
3. Regularity theory for Eα,p-critical maps: Proof of Theorem I 10
4. Extremal cases α = 4 andα = 0, and no M¨obius invariance for p = 2 17
Appendix A. A new norm for Wβ,p 22
Appendix B. Computations 26
References 26
1. I ntroduction
For αp≥ 4, p≥ 2, the O’hara knot energies 1Oα,p named after their inventor J. O’hara
[38, 39] are deﬁned for closed Lipschitz curvesγ : R/Z→ R3 from the circle R/Z into the
three-dimensional space R3 by
(1.1) Oα,p(γ) =
∫
R/Z
∫
R/Z
( 1
|γ(x)−γ(y)|α− 1
Dγ(x,y )α
) p
2
|γ′(x)||γ′(y)| dx dy.
Here,Dγ(x,y ) denotes the intrinsic distance betweenγ(x) andγ(y) along the curveγ.
A striking property of an O’hara knot energy is its self-repulsive eﬀect which is in contrast
to other geometric energies like e.g. Bernoulli’s bending energy. Namely, curves with
self-intersections have inﬁnite energy.
The original deﬁnition of the O’hara knot energies in [38, 39] was motivated by the idea
of calculating the potential energy of electric charge equidistributed on the given curve.
He adapted ideas in the work of Fukuhara [20] who attempted to use energies to ﬁnd espe-
cially nice representatives of a given knot class. The subject has found applications in other
parts of mathematics and the sciences. Knot energies can help to model repulsive forces of
ﬁbres, whenever self-interaction of strands should be avoided. In fact, there is some indi-
cation that DNA molecules seek to attain a minimum state of a suitable energy [36]. There
1In this paper we divert from the usual notation of the literature by writing p
2 instead of p for the simple
reason that the case p = 2 (in the knot literature: p = 1) corresponds to the Hilbert-space case of an L2-energy.
1
arXiv:1905.06064v1  [math.AP]  15 May 2019
2 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
have been several attempts to employ self-avoiding energies for mathematical models in
microbiology, see e.g. [4] and references therein for links to polymer science and protein
science. Moreover, attraction phenomena may be modeled by a corresponding positive
gradient ﬂow [40]. Self-repulsive terms can also be used to penalize self-penetration of
physical objects, e.g. in elasticity theory [32].
From the analytical point of view, one important driving force in this ﬁeld is the hope that
knot energies might lead to a very natural proof of the Smale conjecture. In one of its many
equivalent forms this conjecture states that the space of circles is a deformation retract of
all Jordan curves. This conjecture was proven by Hatcher [23]. If it could be shown that, in
the unknot class, circles are the only critical knots of one of the O’hara energies this could
be used to construct a deformation retract proving Smale’s conjecture in a straightforward
way.
Of course, the central analytic questions for a variational energy are the questions of ex-
istence of minimizers, their regularity, and - if possible - even a list or classiﬁcation of all
minimizers. There are two diﬀerent regimes, analytically: ifαp> 4 the energy is sensitive
to scaling γ↦→ λγ, i.e. the size of the knot. Fixing the length of the curve (to ensure
existence of minimizers) one ﬁnds that the energy is sub-critical, e.g. in the sense that
sequences of knots with bounded energy (up to a subsequence) converge in the ambient
isotopy class.
Forαp = 4 the energyOα,p is invariant under scalings γ↦→ λγ. In this case the energy
Oα,p measures only the physical shape and does not take into account the size of the knot
γ. This is the critical (and thus analytically most challenging) case, e.g. in the sense that
sequences of knots with bounded energy may exhibit bubbling phenomena.
Let us also remark that in the (generally in this paper excluded) case αp< 4 the energy is
not repulsive any more, i.e. self-intersections are permissible.
In this work we will concentrate on the critical case whereαp = 4. We draw our motivation
from the results known in the special case α = 2 and p = 2, in which the O’hara energy
O2,2 is called M ¨obius energy. Namely, the following was shown in the groundbreaking
work by Freedman, He, and Wang [19].
Theorem 1.1 (Freedman-He-Wang).
(1) Minimizers of the M¨ obius energyO2,2 exist within any prime knot class.
(2) Any local minimizer ofO2,2 is of class C1,1 when parametrized by arclength.
Here, a knot class is the ambient isotopy class of an embedded curve. A knot is called a
prime knot if it cannot be decomposed into two non-trivial knots. Otherwise it is called a
composite knot, cf. [15]. Kusner and Sullivan conjectured that there are no minimizers in
composite knot classes, supporting their intuition with numerical experiments [33]. It is
an interesting fact that the existence in prime knot classes corresponds to what is known
for minimizing harmonic maps [41] where minimizers exist in generators of the homotopy
group and may not exist in other elements of the homotopy group.
The main result of this work is the following regularity theorem extending Freedman, He,
Wang’s result to the caseαp = 4. The question of existence will be treated in the forth-
coming paper [9].
Theorem I. Ifαp = 4, p ≥ 2, then any critical knot γ ofOα,p parametrized by constant
speed is of class C1,σ for someσ> 0. In particular this holds for local minimizers.
Before we explain the main ideas behind the proof of Theorem I let us gather further facts
about O’hara energies.
Known results for O’hara energies. Forαp≥ 4, p≥ 2, circles are the global minimizers
of all O’hara energies among curves of ﬁxed length [1]. Regarding minimizers in a given
knot class: for the scaling-dependent case αp > 4, O’hara [38, 39] proved the existence
of minimizers in any knot class. His argument relies on the fact that for αp > 4 the knot
O’HARA KNOT ENERGIES I 3
energies are coercive on the space of embedded C1,β curves and lower semi-continuous
with respect to C1 convergence. This can nowadays be derived from the classiﬁcation of
curves of ﬁnite energy in [5]: curves with a uniform bound onOα,p are uniformly bounded
in the fractional Sobolev space W1+α
2− 1
p,p which continuously embeds into C1+β for β =
α
2− 2
p > 0, ifαp> 4. Observe that this embedding fails ifαp = 4.
Adapting arguments of O’hara and Freedman, He, and Wang, the existence of symmetric
but non-minimizing critical points was proven in [21, 6] for both, the non scale-invariant
caseαp> 4 and the M¨obius energy (α, p) = (2, 2) (in that case only in prime knot classes).
This extends previous work of Kim and Kusner on torus knots [31] and of Cantarella, Fu,
Mastin, Royal on symmetric critical knots for the rope-length [16].
Forα >2, p = 2 it was proven in [10] that critical knots are C∞; analyticity of solutions
was shown in [44]. Furthermore, C∞-smoothness of critical knots of the M ¨obius energy
O2,2 is due to He [24], under a C1,1 initial regularity assumption, and under only ﬁnite
energy assumption this was obtained in [8]. Analyticity in this case was shown in [11].
In a series of papers Ishizeki and Nagasawa [27, 28, 29, 30] showed and analyzed vari-
ous decomposition results for the M ¨obius energy and more generally O’hara energies, see
also [37].
Main ideas behind Theorem I. A ﬁrst na¨ıve attempt of proving Theorem I would be to
try to extend the geometric arguments in [19]. This attempt is thwarted, however, because
their proof crucially exploits the M ¨obius invariance of the energy O2,2. But this means
that there is no hope of extending these arguments: indeed in Section 4 we present strong
numerical evidence for the following conjecture.
Conjecture 1.2. The energyOα,p is M¨ obius invariant if and only if(α, p) = (2, 2).
The underlying strategy behind the proof of Theorem I is thus completely di ﬀerent from
[19]. We relate critical knots of Oα,p to harmonic maps. To achieve this we deﬁne a new
energyEα,p in (2.4) with the following property: if a constant-speed parametrized knot γ
is a critical knot ofOα,p, then the unit tangent u := γ′
|γ′| is a critical map of the energyEα,p
restricted to maps into the unit sphere S2,u : R/Z→ S2, cf. Theorem 3.1.
The energyEα,p has a nonlinear, nonlocal Lagrangian; andEα,p is comparable to aW
1
p,p(R/Z)-
seminorm, where W
1
p,p denotes the fractional Sobolev space. Critical maps of the W
1
p,p-
seminorm are called W
1
p,p-harmonic maps. As a consequence, the described reformulation
allows us to interpret critical knotsγ ofOα,p-energies as (essentially) fractional harmonic-
type maps u into the sphere S2.
Fractional harmonic maps have been studied ﬁrst by Da Lio and Rivi `ere [18, 17] in the
form of W
1
2,2-harmonic maps. These maps are in turn generalizations of classical har-
monic maps, as treated e.g. on two-dimensional domains by H ´elein [26]. This theory was
extended to W1/p,p-harmonic maps into spheres by the third-named author in [42], see also
[35]. We will further extend this theory to the case ofEα,p-harmonic maps into spheres, see
Theorem 3.1. In view of our identiﬁcation of critical knots γ for the O’hara energyOα,p
with a critical map u = γ′
|γ′| with respect to the energyEα,p we obtain Theorem I.
Let us remark, that the strategy of interpreting γ′ as a solution to a fractional harmonic-
type map equation has already been proven successful in [8] for the case of the M ¨obius
energy (α, p) = (2, 2) – i.e. the Hilbert-space case.
Remark 1.3. A minor technical adaptation of the arguments in this article leads to the
corresponding statement of Theorem I for so-called open knots, γ : R→ R3, which are
critical points of the energy
(1.2) Oα,p
o (γ) =
∫
R
∫
R
( 1
|γ(x)−γ(y)|α− 1
Dγ(x,y )α
) p
2
|γ′(x)||γ′(y)| dx dy.
4 SIMON BLATT, PHILIPP REITER, AND ARMIN SCHIKORRA
Notation. We will use fairly standard notation: B will denote intervals in R. In estimates
we write a≼ b if a≤ C b for some multiplicative constant C. We write a≿ b if b≼ a, and
a≈ b if a≼ b and b≼ a.
We work with two types of critical points of energy functionals, which for the convenience
of the reader we label diﬀerently: we will denote as critical knots the critical (i.e. station-
ary) pointsγ : R/Z→ R3 of the O’hara energyOα,p. As critical maps we will denote the
critical points u : R/Z→ S2 of the (yet to be deﬁned) energy functionalEα,p.
Acknowledgments. Financial support is acknowledged as follows
• FWF Austrian Science Fund, grant no P 29487-N32 (SB)
• German Research Foundation (DFG) through grant no. RE-3930/1-1 (PR)
• German Research Foundation (DFG) through grant no. SCHI-1257/3-1 (AS)
• Simons foundation through grant no. 579261 (AS)
• Daimler and Benz foundation, grant no 32-11/16 (AS)
Part of this work was carried out while A.S. was a Heisenberg fellow.
2. A new energyEα,p
