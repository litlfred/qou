---
doc_id: arxiv-hep-th-0206161v1
doc_title: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-7
source_pdf: 0206161v1.pdf
source_sha256: 9530c40215baa02d
toc_source: inferred
doc_brief: "SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING — 24 sections: Front matter; Jourdain:; Introduction"
---
The dynamics of gauge theories is a long and fascinating subject. The dynamics of
supersymmetric gauge theories is a subject with shorter history. However, more facts are
known about susy theories, and with better precision [2] yet with rich enough applications
both in physics and mathematics. In particular, the solution of Seiberg and Witten [3]
of N = 2 gauge theory using the constraints of special geometry of the moduli space of
vacua led to numerous achievements in understanding of the strong coupling dynamics
of gauge theory and as well as string theory backgrounds of which the gauge theories in
question arise as low energy limits.
The low energy eﬀective Wilsonian action for the
massless vector multiplets (al) is governed by the prepotential F(a; Λ), which receives one-
loop perturbative and instanton non-perturbative corrections (here Λ is the dynamically
generated scale):
F(a; Λ) = Fpert(a; Λ) + Finst(a; Λ)
(1.1)
In spite of the fact that these instanton corrections were calculated in many indirect ways,
their gauge theory calculation is lacking beyond two instantons[4][5]. The problem is that
the instanton measure seems to get very complicated with the growth of the instanton
charge, and the integrals are hard to evaluate.
The present paper attempts to solve this problem via the localization technique, pro-
posed long time ago in [1][6][7]. Although we tried to make the paper readable to both
mathematicians and physicists we don’t expect it to be quite understandable without some
background material, which we suggest to look up in [3][8][9].
Notations.
Let G be a semi-simple Lie group, T is maximal torus, g = Lie(G) its
Lie algebra, t = Lie(T) its Cartan subalgebra, W = N(T)/T denote its Weyl group,
U = (t ⊗C)/W denotes the complexiﬁed space of conjugacy classes in g. We consider the
1
moduli space Mk(G) of framed G-instantons: the anti-self-dual gauge ﬁelds A, F +
A = 0, in
the principal G-bundle P over the 4-sphere S4 = IR4 ∪∞with
k = −
1
8hπ2
Z
IR4 tr FA ∧FA
(1.2)
considered up to the gauge transformations g : A 7→g−1Ag + g−1dg, s.t. g(∞) = 1. We
also consider several compactiﬁcations of the space Mk(G): the Uhlenbeck compactiﬁcation
˜
Mk(G) and the Gieseker compactiﬁcation f
Mk for G = U(N) or SU(N). In the formula
(1.2) we use the trace in the adjoint representation, and h stands for the dual Coxeter
number of G.
Field theory description. We calculate vacuum expectation value of certain gauge
theory observables. These observables are annihilated by a combination of the super-
charges, and their expectation value is not sensitive to various parameters, the energy
scale in particular. Hence, one can do the calculation in the ultraviolet, where the
theory is weakly coupled and the instantons dominate. Or, one can do the calculation
in the infrared, and relate the answer to the prepotential of the eﬀective low-energy
theory. By equating these two calculations we obtain the desired formula.
Mathematical description. We study G×T2 equivariant cohomology of the moduli
space f
Mk, where G acts by rotating the gauge orientation of the instantons at inﬁnity,
and T2 is the maximal torus of SO(4) – the group of rotations of IR4 which also acts
naturally on the moduli space2. Let p : f
Mk →pt be the map collapsing the moduli
space to a point. We consider the following quantity:
Z(a, ǫ1, ǫ2; q) =
∞
X
k=0
qk
I
e
Mk
1
(1.3)
where
H
1 denotes the localization of the pushforward p∗1 of 1 ∈H∗
G×T2( f
Mk) in
H∗
G×T2(pt) = C[U, ǫ1, ǫ2]. We denote the coordinates on t by a and the coordinates
on the Lie algebra of T2 by ǫ1, ǫ2.
In explicit calculations3 we represent 1 by a
cohomologically equal form which allows to replace
H
1 by an ordinary integral:
I
f
Mk
1 =
Z
f
Mk
exp ω + µG(a) + µT2(ǫ1, ǫ2)
(1.4)
2 Throughout the paper we mostly consider the SU(N) instantons (or U(N) noncommutative
instantons). We use the notation f
Mk,N when we want to emphasize that the gauge group is
U(N).
3 For G = SU(N) we actually use a = (a1, . . . , aN) s.t. P
l al = 0
2
where ω is a symplectic form on g
Mk, invariant under the G × T2 action, and µG, µT2
are the corresponding moment maps.
Our ﬁrst claim is
Z(a, ǫ1, ǫ2; q) = exp
Finst(a, ǫ1, ǫ2; q)
ǫ1ǫ2

(1.5)
where the function Finst is analytic in ǫ1, ǫ2 near ǫ1 = ǫ2 = 0.
We also have the following explicit expression for Z in the case4 ǫ1 = −ǫ2 = ¯h for5
G = SU(N) :
Z(a, ¯h, −¯h; q) =
X⃗
k
q|k|
Y
(l,i)̸=(n,j)
aln + ¯h (kl,i −kn,j + j −i)
aln + ¯h (j −i)
(1.6)
Here aln = al −an, the sum is over all colored partitions:⃗k = (k1, . . ., kN), kl = {kl,1 ≥
kl,2 ≥. . .kl,nl ≥kl,nl+1 = kl,nl+2 = . . . = 0},
|⃗k| =
X
l,i
kl,i ,
and the product is over 1 ≤l, n ≤N, and i, j ≥1.
Already (1.6) can be used to make rather powerful checks of the Seiberg-Witten solution.
But the checks are more impressive when one considers the theory with fundamental mat-
ter. To get there one studies the bundle V over g
Mk of the solutions of the Dirac equation
in the instanton background. Let us consider the theory with Nf ﬂavors. It can be shown
that the gauge theory instanton measure calculates in this case (cf. [11]):
Z(a, m, ǫ1, ǫ2; q) =
X
k
qk
I
f
Mk
EuG×T2×U(Nf )(V ⊗M)
(1.7)
where M = CNf is the ﬂavor space, where acts the ﬂavor group U(Nf), m = (m1, . . ., mNf )
are the masses = the coordinates on the Cartan subalgebra of the ﬂavor group Lie algebra,
and ﬁnally EuG×T2×U(Nf ) denotes the equivariant Euler class.
4 in the general case we also have a formula, but it looks less transparent
5 a simple generalization to SO and Sp cases will be presented in [10]
3
The formula (1.6) generalizes in this case to:
Z(a, m, ǫ1, ǫ2; q) =
X⃗
k

q¯hNf |k| Y
(l,i)
Nf
Y
f=1
Γ( al+mf
¯h
+ 1 + kl,i −i)
Γ( al+mf
¯h
+ 1 −i)
×
×
Y
(l,i)̸=(n,j)
aln + ¯h (kl,i −kn,j + j −i)
aln + ¯h (j −i)
(1.8)
Again, we claim that
Finst(a, m, ǫ1, ǫ2; q) = ǫ1ǫ2 logZ(a, m, ǫ1, ǫ2; q)
(1.9)
is analytic in ǫ1,2.
The formulae (1.6)(1.8) were checked against the Seiberg-Witten solution [12]. Namely,
we claim that
Finst(a, m, ǫ1, ǫ2)|ǫ1=ǫ2=0 = the instanton part of the prepotential of the low-energy
eﬀective theory of the N = 2 gauge theory with the gauge group G and Nf fundamental
matter hypermultiplets.
Mathematical formulation. The latter statement means that Finst is related to
periods of a family of curves. More precisely, consider the following family of curves6
Σu (here we formulate things for G = SU(N) but the generalization to general G is
well-known [12] ):
w + Λ2N−Nf Q(λ)
w
= P(λ) =
N
Y
l=1
(λ −αl)
(1.10)
where Q(λ) = QNf
f=1(λ+mf). The base of the family (1.10) is the space U = CN−1 ∋u
of the polynomials P (we set P
l αl = 0).
Consider the region Upert ⊂U where
|αl|, |αl −αn| ≫|Λ|, |mf|. In Upert we can pass from the local coordinates (αl) to the
local coordinates (al) given by:
al =
1
2πi
I
Al
λdw
w
(1.11)
6 Λ, mf are ﬁxed for the family
4
where the cycle Al can be described as encircling the cut on the λ plane connecting
the points α±
l = αl + o(Λ) which solve the equations:
±2ΛN−
Nf
2 Q
1
2 (α±
l ) = P(α±
l )
(1.12)
The sum P
l Al vanishes in the homology of Σu, therefore we get N −1 independent
coordinates, as we should have. Now, deﬁne the dual coordinates
aD
l =
1
2πi
I
Bl
λdw
w
(1.13)
where Bl encircles the cut connecting α+
l and α−
(l+1)modN. Then, one can show [3][12]
that
X
l
dal ∧daD
l = 0
on U, and as a consequence, there exists a (locally deﬁned) function, called prepoten-
tial, F(a; m, Λ) such that
X
l
aD
l dal = dF(a)
(1.14)
In the region Upert the prepotential has the expansion:
F(a; m, Λ) = Fpert(a) + Finst(a)
Fpert(a) = 1
2
X
l̸=n
(al −an)2 log
al −an
Λ

−
X
l,f
(al + mf)2log
al + mf
Λ

(1.15)
where Finst is a power series in Λ. Our claim is that
Finst deﬁned by the formula (1.15) coincides with Finst(a, m, ǫ1, ǫ2)|ǫ1=ǫ2=0.
We have checked this claim by an explicit calculation for up to ﬁve instantons, against the
formulae in [13].
There is also a generalization of (1.6) to the case of adjoint matter. It is presented in the
main body of the paper.
*
*
*
This paper is a short version of a longer manuscript [10], which will contain various details.
In this paper we mostly state the results.
5
The paper is organized as follows. In the next section we describe the physical idea
of our calculation. We deﬁne the observable of interest, and sketch two calculations of its
expectation value – in the weak coupling regime in the ultraviolet, and the infrared low-
energy eﬀective theory calculation. The section 3 provides more details on the instanton
calculation and generalizes the pure gauge theory calculation to the case of the theories
with matter. We also discuss explicit low instanton charge calculations. In the section 4
we discuss our results from the M-theory viewpoint, consider some generalizations, present
our conjectures and describe future directions.
Acknowledgements.
This paper would have never seen the light without the nu-
merous conversations of the author with A. Losev.
We also beneﬁted from discus-
sions/collaborations with A. Givental, G. Moore, A. Okounkov, S. Shatashvili, A. Vain-
shtein, H. Braden, S. Cherkis, K. Froyshov, V. Kazakov, I. Kostov, A. Marshakov and
A. Morozov over the last ﬁve years. We are especially grateful to T. Hollowood for reading
the manuscript and sending us his comments, in particular for pointing out an important
typo.
We are most grateful to T. Piatina for providing the opportunity to accomplish this
work, and for inspiring us during the diﬃcult moments of research (especially between the
third and the fourth instantons).
Research was supported in part by RFFI grant 01-01-00549 and by the grant 00-15-
96557 for the support of scientiﬁc schools.
The results of this paper were presented at the EURESCO school “Particle physics
and gravitation” held at Bad Herrenalb. We thank H. Nicolai for the invitation and for
organizing a nice school.
