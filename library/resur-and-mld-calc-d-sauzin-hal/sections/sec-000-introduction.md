---
doc_id: resur-and-mld-calc-d-sauzin-hal
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-4
source_pdf: Resur_and_Mld_Calc_D_SAUZIN_HAL.pdf
source_sha256: b33f24cc76102f33
doc_brief: "HAL Id: hal-04253203 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 9 sections: Introduction"
---
2 “Simple” version of Resurgence Theory . . 1
2.1 Simple Ω-resurgent series . . . . . . 2
2.2 Stability under product and nonlin-
ear operations . . . . . . . . . . . . . 3
2.3 Alien operators. Alien derivations . 3
2.4 Freeness of the alien derivations and
ﬁrst hint of mould calculus . . . . . 4
3 Simple resurgent functions obtained by
Borel-Laplace summation . . . . . . . . . . 5
3.1 Borel-Laplace summation . . . . . . 5
3.2 Transseries, symbolic Stokes auto-
morphism . . . . . . . . . . . . . . . 6
4 The algebra
▽
R of general resurgent singu-
larities . . . . . . . . . . . . . . . . . . . . . 7
4.1 Relaxing the constraint on the loca-
tion of singularities. . . . . . . . . . 7
4.2 Examples from mathematical physics. 8
4.3 Relaxing the constraint on the na-
ture of singularities. . . . . . . . . . 8
5 Mould Calculus . . . . . . . . . . . . . . . . 10
5.1 The mould algebra . . . . . . . . . . 10
5.2 The hyperlogarithmic mould. . . . . 11
5.3 Mould aspects of the MZV world . . 12
6 Applications . . . . . . . . . . . . . . . . . . 12
1File: Resur_and_Mld_Calc_D_SAUZIN_HAL.tex 2023-
10-23
Keywords: resurgence, alien derivation, analytic con-
tinuation, asymptotic expansion, Laplace transform, alge-
braic combinatorics, Hopf algebra, perturbative quantum
ﬁeld theory, non-pertubative physics, deformation quanti-
zation, multizeta values.
1 Introduction
Resurgence Theory, founded in the late 1970s by the
French mathematician Jean ´Ecalle in the context of
dynamical systems, has recently become a ﬁxture in
the mathematical physics research literature, with a
burst of activity in applications ranging from quan-
tum mechanics, wall-crossing phenomena, ﬁeld the-
ory and gauge theory to string theory. See [Woo23]
for a non-technical account of the importance taken
by Resurgence in current research in Quantum Field
Theory.
The theory may be seen as a reﬁnement of the Borel-
Laplace summation method designed to encompass
the transseries which naturally arise in a variety of
situations. Typically, a resurgent series is a diver-
gent power series in one indeterminate that appears as
the common asymptotic expansion to several analytic
functions that diﬀer by exponentially small quantities.
The so-called ‘alien derivations’ are tools designed to
handle these exponentially small discrepancies at the
level of the series themselves. In the context of lo-
cal analytic dynamical systems, they have allowed for
quite a concrete description of various moduli spaces.
Together with Resurgence, ´Ecalle also put forward
Mould Calculus, a rich combinatorial environment
of Hopf-algebraic nature, designed to deal with the
inﬁnite-dimensional free associative algebras gener-
ated by the alien derivations, but whose scope goes
much beyond; for instance, it provides remarkable
tools for the study of the so-called ‘multiple zeta val-
ues’ (MZV).
2 “Simple” version of Resurgence
Theory
Resurgence theory [´Eca81; ´Eca85] deals with a certain
C-algebra
▽
R over C endowed with a family of C-linear
derivations
∆ω∈ DerC
(▽
R
)
, (1)
where ω runs over the Riemann surface of the loga-
rithm. For the sake of simplicity, we begin by limiting
ourselves to a subalgebra,
▽
Rs
Ω ⊂
▽
R [´Eca81; MS16],
easier to describe because it is isomorphic to a subal-
gebra ~Rs
Ω of formal series in one indeterminate.
2.1 Simple Ω-resurgent series
It is convenient to denote the indeterminate by z−1
because our formal series will appear as asymptotic
expansions at inﬁnity of functions analytic in certain
unbounded domains. Let us ﬁx a rank-1 lattice Ω
of C. We shall sometimes use the notations ‘ ω1’ for a
generator of Ω and
ωk :=kω 1, k ∈ Z (2)
for the elements of Ω.
Deﬁnition 1. The space ~Rs
Ω of simple Ω-resurgent
series is deﬁned as the set of all formal series ~ϕ(z) =∑
n≥0cnz−n∈ C[[z−1]] such that the Borel transform
ˆϕ(ζ) =
∑
n≥0
cn+1
ζn
n! (3)
has positive radius of convergence, deﬁnes a function
that has (possibly multivalued) analytic continuation
along any pathγ starting close enough to 0 and avoid-
ing Ω, and all the branches of the analytic continuation
of ˆϕ(ζ) have at worst ‘simple singularities’.
By ‘simple singularities’, we mean that, if ζ1 is the
endpoint of a pathγ as above and we denote by contγˆϕ
the analytic continuation of ˆϕ along γ, and if ω is a
point of Ω nearest toζ1 (so that contγˆϕ is holomorphic
on the line-segment [ζ1,ω [; see Fig. 1), one must have
contγˆϕ(ω +ξ) = a0
2πiξ +ˆχ(ξ)logξ
2πi +F (ξ), (4)
where a0 is a complex number and both functions ˆχ
and F extend analytically through ξ = 0.
Deﬁning
B : C[[z−1]]→ Cδ⊕ C[[ζ]], B~ϕ :=c0δ +ˆϕ (5)
(here δ is just a symbol representing the image of 1),
we have
C{z−1}⊂ ~Rs
Ω = B−1(ˆRs
Ω
)
⊂ C[[z−1]] (6)
Figure 1: The path γ avoids Ω and ends atζ1, nearω.
with ˆRs
Ω := the set of all c0δ +ˆϕ∈ Cδ⊕ C{ζ} such
that ˆϕ extends analytically to the universal cover of
C− Ω and has at worst simple singularities.
The ﬁrst inclusion in (6) means that convergent se-
ries are always resurgent: if the radius of convergence
of ~ϕ(z) happens to be positive, then ˆϕ(ζ) extends to
an entire function of ζ, thus the above deﬁnition is
satisﬁed with any Ω.
Examples of divergent simple Ω-resurgent series. The
Euler series ~ϕE(z) :=∑
p≥0(−1)pp!z−p−1 (formal so-
lution to the equation− dϕ
dz +ϕ =z−1) and the Stirling
series~ϕS(z) := 1
12z−1− 1
360z−3+ 1
1260z−5+··· (asymp-
totic expansion of log
( 1√
2πz
1
2−zezΓ(z)
)
as|z|→∞
with|argz|≤ π−ε) have Borel transforms
ˆϕE(ζ) = 1
1 +ζ, ˆϕS(ζ) =ζ−2
(ζ
2 cothζ
2− 1
)
(7)
meromorphic with simple poles in Ω = Z or 2πiZ.
But the typical Borel transforms found in prac-
tice are multivalued, as is the case for instance
for exp( ~ϕS(z)) ∈ ~Rs
2πiZ (asymptotic expansion of
1√
2πz
1
2−zezΓ(z)), whose Borel transform can be ex-
pressed in terms of the Lambert W function [Sau21].
In the latter example, the Borel transform has a prin-
cipal branch regular atζ = 0 but the other branches of
its analytic continuation are singular at 0. A more el-
ementary example of the same phenomenon is oﬀered
by Li2(ζ) :=−
∫ζ
0 log(1−ξ) dξ
ξ ∈ ˆRs
Z.
The growth of the coeﬃcients of a resurgent series
~ϕ(z) is at most factorial, because B~ϕ∈ Cδ⊕ C{ζ}
implies that there exist C,M > 0 such that |cn| ≤
CMnn!. Such series are said to be 1 -Gevrey. If the
radius of convergence of ~ϕ(z) is zero, we may hope
to get information on its divergence by studying the
singularities of its Borel transform. This will be done
by means of ´Ecalle’s alien operators (see below).
2
2.2 Stability under product and nonlinear op-
erations
It is obvious that ~Rs
Ω is a C-vector space stable under
d
dz (note that B maps diﬀerentiation to multiplication
by−ζ). Much less obviously, it is also stable under
multiplication and is thus a subalgebra of C[[z−1]].
This is due to the compatibility of the process of an-
alytic continuation with the convolution
ˆϕ∗ ˆψ(ζ) :=
∫ ζ
0
ˆϕ(u)ˆψ(ζ−u) du (8)
and to the fact that B maps the standard (Cauchy)
product of formal series ~ϕ~ψ to B~ϕ∗ B~ψ, where δ =
B1 is a unit for the convolution: one can indeed check
that ˆRs
Ω is stable under convolution [ ´Eca81; CNP93;
Sau13].
The algebra ~Rs
Ω is also stable under nonlinear op-
erations like substitution into a convergent series, or
composition of the form ~ϕ◦(Id +~ψ). For instance, the
exponential of any simple Ω-resurgent series and—if it
has nonzero constant term—its multiplicative inverse
are simple Ω-resurgent series; also, {Id +~ψ| ~ψ∈ ~Rs
Ω}
is a group for composition [ ´Eca81] (details can be
found in [Sau15]).
