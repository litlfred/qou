---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-021-223-measure
section_title: "Measure"
section_number: 2.2.3
pages: 27-30
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian S tokes theorem have been addressed."
---
the boundary ∂S, and the imposed boundary conditions are free.
It should be noted that the surface integral on the RHS of Eqs.34 a nd 35
depends on the curvature F as well as on the connectionA entering the covariant
derivatives, which is reminiscent of the path dependence of the cur vature F in
the operator approach.
A quite diﬀerent formulation of the holomorphic approach to the non-Abelian
Stokes theorem has been proposed in [Lun97].
Appendix For completness of our derivations, we will remind the reader a few
standard facts being used above. First of all, we assume the following (non-quite
standard, but convinient) deﬁnition
|z ⟩
def
= eza++¯za+ 1
2 |z|2
|0 ⟩ = eza+
e¯za |0 ⟩
= eza+
|0 ⟩ =
∞∑
k=0
(zna+)n
n! |0 ⟩ =
∞∑
k=0
zn
√
n!
|n ⟩,
where |0 ⟩is the Fock vacuum, i.e. ˆa |0 ⟩ = 0, and the Baker-Campbell-Hausdorﬀ
formula has been applied in the ﬁrst line. We could also treat |z ⟩ as a coherent
state for the Heisenberg group. We can easily calculate
⟨¯z | z⟩ =
∞∑
m,n=0
¯zmzn
√
m! n!
⟨m | n⟩ =
∞∑
n=0
(¯zz)n
n! = e¯zz .
The identity operator is of the form
I =
∫
|z ⟩ ⟨¯z | e−¯zz d¯z dz
2πi .
Really,
I |z′ ⟩ =
∫
|z ⟩ ⟨¯z| z′⟩e−¯zz d¯z dz
2πi =
∫
|z ⟩e¯zz ′−¯zz d¯z dz
2πi
=
∫
|z ⟩δ(z′ − z) dz = |z′ ⟩.
All these formulas for a single pair of creation and annihilation operat ors ob-
viously apply to a more general situation of dim R pairs. The matrix elements
27
are
⟨
¯z
⏐
⏐
⏐ˆA
⏐
⏐
⏐z
⟩
=
⟨
0
⏐
⏐
⏐e
∑
k ¯zkˆak
∑
a
Aa∑
k,l
T a
klˆa+
k ˆale
∑
k zkˆa+
k
⏐
⏐
⏐0
⟩
=
⟨
0
⏐
⏐
⏐e
∑
k ¯zkˆak
∑
a
Aa∑
k,l
T a
kl¯zkzle
∑
k zkˆa+
k
⏐
⏐
⏐0
⟩
=
⟨
¯z
⏐
⏐
⏐
∑
a
Aa∑
k,l
T a
kl¯zkzl
⏐
⏐
⏐z
⟩
= ⟨¯z |¯zAz | z⟩,
where we have used the formula
[
ˆa, ezˆa+]
∓
= zezˆa+
.
Now
⟨
1k
⏐
⏐
⏐
(
1 + iǫ ˆA
)⏐
⏐
⏐1l
⟩
= δkl + iǫ
⟨
0
⏐
⏐
⏐
⏐
⏐
⏐
ˆak
∑
a
Aa∑
i,j
T a
ijˆa+
i ˆajˆa+
l
⏐
⏐
⏐
⏐
⏐
⏐
0
⟩
= δkl + iǫ
∑
a
AaT a
kl = (1 + iǫA)kl.
Also,
⟨1k| z ⟩ = zk.
2.2.3 Measure
The described theory possesses the following “topological” gauge s ymmetry:
δz(x) = θ(x), δ ¯z(x) = ¯θ(x), (36)
where θ(x) and ¯θ(x) are arbitrary except at the boundary ∂S where they vanish.
The origin of the symmetry 36 will become clear when we convert the a ction 32
into a line integral. Integrating by parts in Eq.32 and using the Abelian S tokes
theorem we obtain
Scl = i
∮
∂S
¯zDiz dxi,
or in a parametrized form
Scl = i
∮
∂S
¯zDtz dt.
28
To covariantly quantize the theory we shall introduce the BRS oper ator s. Ac-
cording to the form of the topological gauge symmetry 36, the ope rator s is
easily deﬁned by
s z = φ, s ¯z = ¯χ, sφ = 0, s ¯χ = 0,
s¯φ = ¯β, sχ = β, s ¯β = 0, sβ = 0,
where φ and ¯χ are ghost ﬁelds in the representation R, associated to θ and ¯θ,
respectively, ¯φ and χ are the corresponding antighosts, and ¯β, β are Lagrange
multipliers. All the ﬁelds possess a suitable Grassmann parity correla ted with
the parity of ¯z and z. Obviously s2 = 0, and we can gauge ﬁx the action in
Eq.32 in a BRS-invariant manner by simply adding the following s-exact term:
S′ = s
(∫
S
(¯φ△z ± ¯z△χ
)
d2σ
)
=
∫
S
(¯β△z ± ¯φ△φ ± ¯χ△χ + ¯z△β
)
d2σ.
The upper (lower) sign stands for the ﬁelds ¯z, z of bosonic (fermionic) statistics.
Integration after the ghost ﬁelds yields some numerical factor an d the quantum
action
S = Scl +
∫
S
(¯β△z + ¯z△β
)
d2σ. (37)
If necessary, one can insert √g into the second term, which is equivalent to
change of variables. Thus the partition function is given by
Z =
∫
eiS D¯z Dz D ¯β Dβ,
with the boundary conditions: ¯β|∂S = β|∂S = 0.
One can observe that the job the ﬁelds ¯β and β are supposed to do consists
in eliminating a redundant integration inside S. The gauge-ﬁxing condition
following from Eq.37 imposes the following constraints
△z = 0, △¯z = 0.
Since values of the ﬁelds z and ¯z are ﬁxed on the boundary ∂S = C, we deal
with the two well-deﬁned 2-dimensional Dirichlet problems. The solutio ns of
29
the Dirichlet problems ﬁx values of z and ¯z inside S. Another, more singular
gauge-ﬁxing, is proposed in [Bro92].
The issue of the measure has been also discussed in [HU00].
