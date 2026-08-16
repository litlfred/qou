---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-061-43-reﬁnement-as-a-twisted-mass-parameter
section_title: "Reﬁnement as a twisted mass parameter"
section_number: 4.3
pages: 63-67
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
Now, let us discuss the physical interpretation of the gener al setup considered in this section
and the corresponding interpretation of the classical acti on S0(u,t ).
As we already reviewed in the beginning of this section, compactiﬁcation of type II string
theory on a toric Calabi-Yau 3-fold X is a natural arena for a “geometric engineering” of
N = 2 supersymmetric gauge theories in the remaining four spac e-time dimensions. In this
setup, BPS states of the “eﬀective” four-dimensional gauge t heory are simply the closed BPS
states from the vantage point of the Calabi-Yau 3-fold X. Moreover, counting reﬁned closed
BPS states means that, from the viewpoint of the 4d N = 2 theory, we keep track of their
spin j3.
– 62 –
Much of our interest comes from counting open reﬁned BPS states in a slight generaliza-
tion of this setup, with a D4-brane added:
space-time: R4 × X
∪ ∪
D4-brane: R2 × L
(4.37)
Since the extra D4-brane here is supported on a special Lagra ngian submanifold L ⊂ X, it
preserves half of the supersymmetry and, as explained in [34], yields a “geometric engineering”
of a half-BPS surface operator in N = 2 gauge theory on R4 (see [80, 32, 81] for a purely ﬁeld
theoretic deﬁnition of surface operators). In a special cas e when X is the conifold and LK
is the Lagrangian submanifold associated to a knot K, the system (4.37) becomes identical
to the physical setup (3.32) discussed in section 3, after co mpactiﬁcation on a circle from
M-theory to type IIA string theory.
From the viewpoint of theN = 2 gauge theory onR4, the generating function of open BPS
invariantsZ open
BPS that plays a central role in this section can be interpreted a s the instanton
partition function of the gauge theory in the presence of a su rface operator [34, 82, 83, 84],
much like its “closed” counterpartZ closed
BPS is the K-theory version of the equivariant instanton
counting on R4 without surface operators [12, 85]. Let SO(2)1 ×SO(2)2 be the rotation
symmetry of R4 preserved by the surface operator in (4.37), such that SO(2)2 is the rotation
symmetry along the R2 ⊂ R4 and SO(2)1 is the rotation symmetry of its normal bundle.
Note, from the viewpoint of the Euclidean N = (2, 2) theory on the surface operator, SO(2)2
is a rotation symmetry (part of the two-dimensional Poincar´ e group), whileSO(2)1 is a global
R-symmetry. In fact, both symmetries in this brane system we re already discussed in section
3.1.1, where we gave them a name U(1)P and U(1)F , respectively. In particular, the global
R-symmetry is:
U(1)F ∼
= SO(2)1 (4.38)
If, as usual, we denote by ǫ1 and ǫ2 the equivariant parameters for SO(2)1 and SO(2)2,
respectively, then the generating functions Z closed
BPS andZ open
BPS are known to have the following
form, see e.g. [86, 87]:
Z closed
BPS (ǫ1,ǫ 2) = exp
( 1
ǫ1ǫ2
F(ǫ1,ǫ 2)
)
(4.39)
= exp
( 1
ǫ1ǫ2
F (0) + ǫ1 +ǫ2
ǫ1ǫ2
F (1) +...
)
and
Z open
BPS (ǫ1,ǫ 2) = exp
( 1
ǫ2
~W +...
)
(4.40)
where F (0) is the prepotential of the four-dimensional N = 2 theory and ~W is the twisted su-
perpotential of the two-dimensional N = (2, 2) theory on the surface operator. In particular,
as explained in [83] (see also [88, 89, 84]), the twisted supe rpotential is given by the integral
– 63 –
of the Seiberg-Witten diﬀerential vdu = logy dx
x over a path:
~W(u) =
∫ u
vdu (4.41)
on the curve A(x,y ) = 0.
Now, let us explain how our discussion in this paper comparesto the Nekrasov-Shatashvili
limit and its relation to quantum integrable systems. There are some similarities and some
diﬀerences, and both are important. First, the limit conside red in [13] in our notations is
ǫ1 = 0 with ǫ2 playing the role of the quantization parameter (in the quant um integrable
system). This is very similar to the limit (2.5) and the discu ssion in this section, where
ℏ = −ǫ2 also plays the role of the quantization parameter and the onl y essential diﬀerence
is that ǫ1 (equivalently,q1 =eǫ1) is allowed to take any ﬁnite values, so that for small ℏ we
havet = − q1
q2
∼ −q1. In this respect, what we consider can be viewed as a reﬁnemen t of the
Nekrasov-Shatashvili limit, cf. Figure 9.
There is an important diﬀerence, however, which has to do withthe fact that [13] consider
the partition function of the 4d gauge theory or, from the van tage point of the Calabi-Yau
3-fold X, the generating function of closed BPS invariants (4.39). In particular, the Yang-
Yang function of the quantum integrable system is identiﬁed with the following limit of the
instanton partition function in the absence of any surface o perators [13]:
lim
ǫ1→0
ǫ1 logZ closed
BPS (ǫ1,ǫ 2) = 1
ǫ2
F (0) + F (1) + O(ǫ2) (4.42)
This expansion should not be confused with a similar-lookin g expansion in (4.40), which
describes the behavior of the open BPS partition function or, from the gauge theory viewpoint,
represents the contribution of a surface operator. In particular, the leading term F (0) in (4.42)
depends only on the closed string moduli, whereas a similar leading term~W in (4.40) depends
on both open and closed string moduli. Thus, the variableu in our discussion or, equivalently,
x =eu is an open string modulus.
Keeping these remarks in mind, we can express the reﬁned volu me conjecture (2.6b) as
a statement that the free energy log Z open
BPS (q1,q 2) has a ﬁrst-order pole in the limit (2.5):
logZ open
BPS (ǫ1,ǫ 2) = S0(u,t )
ℏ +... as q2 =eℏ → 1 and q1
q2
= −t = ﬁnite , (4.43)
where we used (4.7). This, at the same time, is both open and reﬁned generalization of (4.42).
In particular, in the special case t = −1 (or, equivalently,q1 = 1) we recover (4.40), with the
twisted superpotential
~W(u) = S0(u, −1). (4.44)
Therefore, we conclude that S0(u,t ) which appears in the reﬁned volume conjecture (2.6b)
is a “reﬁnement” of the twisted superpotential in the N = (2, 2) surface operator theory 15
15To be more precise, it is a three-dimensional N = 2 theory on a circle that is relevant to the K-theoretic
version of the vortex partition function [34].
– 64 –
with a twisted mass for the global symmetry U(1)F (= rotation in the plane orthogonal to
the surface operator), cf. (3.31):
˜mF = log( −t). (4.45)
As a simple example, let us consider a two-dimensional N = (2, 2) theory with a tower of
Kaluza-Klein states obtained by reducing a three-dimensio nal N = 2 chiral multiplet on a
circle. The twisted superpotential of this theory has the fa miliar form ~W = Li2(−tx), where
we assumed that the 3d chiral multiplet on R2 × S1 has charge +1 with respect to both
U(1)F as well as the globalU(1) symmetry with twisted mass logx. Therefore, in the twisted
superpotential (4.34) we can recognize a contribution of tw o chiral multiplets. Similarly, in
the expression (4.32) for the tetrahedron (or C3) we recognize contribution of a single chiral
multiplet. In general, the number of chiral multiplets is equal to the number of dilogarithms in
S0(u,t ), and the charges of chiral multiplets are simply the powersoft andx in the arguments
of these dilogarithms. It is easy to recognize such contribu tions e.g. in (3.166).
To summarize, each chiral multiplet in the D4-brane theory (4.37) (or, to be more precise,
in the ﬁve-brane theory on a circle, cf. (3.32)) contributes to the twisted chiral superpotential
a dilogarithm term:
tetrahedron ∆ ↔ chiralφ ↔ twisted superpotential
S0(∆;⃗ u,t) = Li2(e⃗ n·⃗ u+nF ˜mF )
where nF is the charge of the chiral multiplet under the global R-symm etry (4.38) and ⃗ n
denotes the charges of the chiral multiplet under all other ﬂ avor symmetries (with twisted
mass parameters ⃗ u). Here, we also identiﬁed the example of a single chiral mult iplet (or
C3) discussed in the present section with a single tetrahedron in examples coming from 3-
manifolds, cf. [34, 90, 19, 91, 92].
⏐
⏐
⏐ Model
values of ni
F
⏐
⏐
⏐
⏐
⏐
⏐ unknot
0, 3, 3
⏐
⏐
⏐
⏐
⏐
⏐ tetrahedron
1
⏐
⏐
⏐
⏐
⏐
⏐ conifold
1, − 1
2
⏐
⏐
⏐
T able 7: Values ofni
F in prominent examples.
More generally, one can consider a three-dimensional N = 2 theory T that contains Nf
chiral multiplets φi, i = 1,...,N f with charges ni
a under global ﬂavor symmetries U(1)a,
a = 1,...,N . This could be either a low-dimensional eﬀective ﬁeld theory in brane systems
(3.32) and (4.37), or a three-dimensional N = 2 theory TM associated to a triangulation of a
3-manifold M,
M =
⋃
i
∆i. (4.46)
– 65 –
In either case, the reﬁnement is achieved by assigning each c hiral multiplet φi (resp. each
tetrahedron ∆i) one extra chargeni
F that describes howφi transforms under the R-symmetry
U(1)F , which may already be a part of∏
aU(1)a. Then, using (4.45), we conclude that passing
from unreﬁned theory to reﬁned theory has the eﬀect of introdu cing the t-dependence in the
classical “volume functional” (= twisted superpotential) via a simple rule:
~W(xi) =
∑
i
Li2
(∏
a
xni
a
a
)
↝ S0(xi,t ) =
∑
i
Li2
(
(−t)ni
F
∏
a
xni
a
a
)
(4.47)
modulo logarithmic ambiguities that depend on choices of framing, polarization, etc. In other
words, at least in such models, the essential information ab out the reﬁnement is contained
in a set of charges {ni
F } that need to be assigned to chiral multiplets or, in the langu age of
3-manifolds, to tetrahedra ∆i. While many examples are considered in the present paper (se e
Table 7), a systematic rule for assigning {ni
F } will be presented in the follow-up work.
