---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-005-43-irreducible-constituents-and-dimension-formul
section_title: "Irreducible constituents and dimension formulas: the non-Archimedean case"
section_number: 4.3
pages: 14-16
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
case. In this subsection we ﬁx a non-Archimedean local ﬁeld F. Let O denote the ring
of integers and p the maximal ideal. The Grassmann representation C
(
G(n,d ; F)
)
was
studied in [11] and later in [1, 2]. Therein it is shown that the irreducible MF-spherical
KF-representations are also parameterized by Λ n. We now proceed to recall the explicit
construction of the irreducibles. The path to the construction of these representations is
completely diﬀerent compared to the Archimedean case. First of all, there is no (highest)
weight theory, in particular there is no concrete description of the full unitary dual ˆKF as
in the Archimedean case. We thus have to resort to a direct constr uction of the spherical
unitary dual (KF/MF)ˆ and the concrete construction of the corresponding represe ntations,
which has a combinatorial ﬂavor due to the proﬁnite nature of KF,
KF ≃ lim
←−
GLd(O/pk).
The latter identiﬁcation is realized by the canonical epimorphisms πk : KF → GLd(O/pk)
deﬁned by reduction modulo pk (k ∈ Z>0). Denoting Ik for the kernel of πk, one has (cf.
[2])
C
(
G(n,d ; F)
)
≃ lim
−→
C
(
G(n,d ; F)
) Ik
as KF-representations, where C
(
G(n,d ; F)
) Ik
stands for the KF-module consisting of the
Ik-ﬁxed vectors in the Grassmann representation. The structure of the Grassmann repre-
sentation is completely determined by its so-called level k − 1 components C
(
G(n,d ; F)
) Ik
for k ∈ Z>0. We proceed now to recall the precise structure of these level co mponents.
The set of partitions Λ n parametrizes the isomorphism classes of the ﬁnite dimensional
O-modules of rank ≤n. Concretely, the partition λ ∈ Λ n corresponds to the isomorphism
class of the ﬁnite O-module ⊕n
i=1O/pλi. The ﬁnite O-modules in the isomorphism class
labeled by λ ∈ Λ n are called O-modules of type λ. Denote ⊆ for the partial order on
partitions deﬁned by inclusion of Young diagrams. Fix a module of type kd = (k,...,k ) (d
entries). For any type λ ⊆kd let G(λ,k d; O) be the Grassmannian of its submodules of type
λ. Let C
(
G(λ,k d; O)
)
be the vector space of complex valued functions on G(λ,k d; O). The
canonical action of KF on G(λ,k d; O) gives rise to a representation of KF on C
(
G(λ,k d; O)
)
.
The ﬁnite Grassmann representations relate to the Grassmann re presentation C
(
G(n,d ; F)
)
by the identiﬁcation
(4.11) C
(
G(n,d ; F)
) Ik
≃ C
(
G(kn,k d; O)
)
as KF-modules, see [2, Lemma 2.1].
The irreducible constituents of the ﬁnite Grassmann representat ion C
(
G(kn,k d; O)
)
have
been explicitly described in [2] in terms of the so-called cellular basis of t he associated
ﬁnite Hecke algebra End KF
(
C
(
G(kn,k d; O)
))
. It leads to a natural parametrization of the
irreducible MF-spherical KF-representations by partitions Λ n, as described in the following
theorem, which is a direct consequence of [2, Theorem 1].
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 15
Denote Λ k
n for partitions λ ∈ Λ n satisfying λ ⊆ kn. Furthermore, for an irreducible
KF-module V we denote ⟨V : C
(
G(µ,k d; O)
)
⟩ for the multiplicity of V in the KF-module
C
(
G(µ,k d; O)
)
.
Theorem 4.4 ([2]). Forλ ∈ Λ n there exists a unique irreducible MF-spherical KF-repre-
sentation V F
λ satisfying, for all k ∈ Z>0 such that λ ∈ Λ k
n,
(1) ⟨V F
λ : C
(
G(µ,k d; O)
)
⟩ ≥ 1 for µ ∈ Λ k
n satisfying λ ⊆µ,
(2) ⟨V F
λ : C
(
G(µ,k d; O)
)
⟩ = 0 for µ ∈ Λ k
n satisfying λ ⁄⊆µ.
The KF-representations V F
λ (λ ∈ Λ n) form a complete set of representatives of the irre-
ducible MF-spherical KF-representations.
Theorem 4.4 gives the multiplicity free irreducible decomposition
C
(
G(n,d ; F)
)
≃
⨁
λ∈Λ n
V F
λ
as KF-modules, as well as the identiﬁcations
(KF/MF)ˆ ≃ Λ n ≃ {isomorphism types of O-modules of rank ≤n}.
Furthermore, (4.11) and Theorem 4.4 imply
(4.12) C
(
G(kn,k d; O)
)
≃
⨁
λ∈Λ k
n
V F
λ
for k ∈ Z>0 as KF-modules, cf. [2, Prop. 2.2]. The following is one of the main results in
this paper.
Theorem 4.5. Lett = |O/p|−1. We have
(4.13) Dim C(V F
λ ) = t−(d−2n+1)|λ|−2(ρ,λ)
[ n
∂λ′
]
t
(td−λ′
1−λ′
2+2;t)λ′
1+λ′
2
(tn−λ′
1+1;t)λ′
1
(1 −td−2λ′
1+1)
(1 −td+1)
for λ ∈ Λ n.
Theorem 4.5 is a direct consequence of the formula
(4.14) Dim C
(
V F
λ
)
=D0
(
λ;td−2n+1,t ;t), t = |O/p|−1
from [23], and the explicit evaluation of D0(λ;a,b ;t) derived in Theorem 7.6. Formula
(4.14) is obtained in [23] as a consequence of (4.2) and the identiﬁcat ion of the zonal
spherical function ϕF
λ with a suitable p-adic (q = 0) degeneration of the multivariable little
q-Jacobi polynomial P L
λ .
Corollary 4.6. Fork ∈ Z>0 we have
∑
λ⊆kn
t−(d−2n+1)|λ|−2(ρ,λ)
[ n
∂λ′
]
t
(td−λ′
1−λ′
2+2;t)λ′
1+λ′
2
(tn−λ′
1+1;t)λ′
1
(1 −td−2λ′
1+1)
(1 −td+1) =t−n(d−n)(k−1)
(d
n
)
t−1
.
16 URI ONN AND JASPER V. STOKMAN
Proof. Since the desired expression is rational in t, it suﬃces to prove the identity with the
formal parametert−1 specialized to the cardinality of the residue ﬁeld of a non-Archimedea n
local ﬁeld F. In this case, the identity immediately follows from (4.12), (4.11), (4 .13) and
the easily veriﬁed identity (alternatively see e.g. [2, Claim 4.1(1)])
(4.15) |G(kn,k d; O)| =t−n(d−n)(k−1)
(d
n
)
t−1
, t = |O/p|−1.
□
Forn = 1, Corollary 4.6 reduces to the trivial geometric sum identity
1 +t1−d (1 −td−1)
(1 −t) + (1 −td−1)(1 −td)
(1 −t)
k∑
m=2
t(1−d)m =t(1−d)k (1 −td)
(1 −t).
We end this subsection by discussing the dimension formula (4.13) in tw o cases that
the dimensions have been computed before by representation the oretic methods. The
dimension formula (4.13) yields for r = 1,...,n ,
(4.16) Dim C
(
V F
ωr
)
=tr(r−d)
(
td−r+2;t
)
r(1 −td−2r+1)(
t;t
)
r(1 −td+1) =
(d
r
)
t−1
−
( d
r − 1
)
t−1
where t = |O/p|−1. Alternatively, by (4.12)
C
(
G(ωr, 1d; O)
)
≃ C
(
G(ωr−1, 1d; O)
)
⊕V F
ωr,
which implies (4.16) in view of (4.15). The latter representation theor etic derivation es-
sentially is the argument from [6].
A similar analysis applies for the irreducible representations V F
k (k ∈ Z≥2 ⊂ Λ 1) arising
in the representation C
(
G(1,d ; F)
)
associated to the projective space Pd(F) = G(1,d ; F),
see [9] and [23, §4]. In this case, (4.13) yields
DimC
(
V F
k
)
=t−(d−1)k (1 −td−1)(1 −td)
(1 −t) =t−(d−1)k (1 −td)
(1 −t) −t−(d−1)(k−1) (1 −td)
(1 −t)
where t = |O/p|−1. This dimension formula can be reconﬁrmed using (4.15) and the
decomposition
C
(
G(k1,k d; O)
)
≃ C
(
G((k − 1)1, (k − 1)d; O)
)
⊕V F
k
as KF-modules, which is a direct consequence of (4.12).
