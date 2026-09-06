---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-025-31-realizations-of-coxeter-systems-for-both-soer
section_title: "Realizations of Coxeter systems. For both Soergel’s construction of Soergel bi-"
section_number: 3.1
pages: 18-20
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
modules, and for our construction of a diagrammatic categor y by generators and
relations, the starting point will be the data of a realizati on of a Coxeter system.
Deﬁnition 3.1. Let k be a commutative ring. A realization of (W,S ) over k is a free,
ﬁnite rank k-module h, together with subsets {α∨
s | s ∈ S} ⊂ h and {αs | s ∈ S} ⊂
h∗ = Hom k(h, k), satisfying:
(1) ⟨α∨
s,α s⟩ = 2 for alls ∈S;
(2) the assignment s(v) def= v − ⟨v,α s⟩α∨
s for allv ∈ h yields a representation ofW ;
(3) the technical condition in (3.3) is satisﬁed. (Its descr iption requires some back-
ground.)
We will often refer to h as a realization, however the choice of {α∨
s } and {αs} is
always implicit.
Given a realization over k and a homomorphism k → k′ we obtain a realization
k′ ⊗k h over k′ by base change. We call a realization faithful if the action of W on h
(and hence the contragredient action on h∗) is faithful. Base change does not preserve
faithfulness in general. For us, the ability to perform base change is the more impor-
tant property , so we must allow realizations which are not faithful. For instance, any
realization of the dihedral group with mst = m < ∞ is also a realization of the di-
hedral group with mst = 2m, 3m,... , and is also a realization of the inﬁnite dihedral
group.
We call a realization symmetric if ⟨α∨
s,α t⟩ = ⟨α∨
t,α s⟩ for alls,t ∈S.
Example 3.2. Some examples of realizations that we have in mind are the fol lowing:
(1) Let (W,S ) be any Coxeter system of ﬁnite rank. Let k = R and h = ⨁
s∈S Rα∨
s .
Deﬁne elements {αs} ⊂ h∗ by
(3.1) ⟨α∨
t,α s⟩ = −2 cos(π/mst)
(by convention mss = 1 andπ/∞ = 0 ). Then h is a symmetric realization of
(W,S ), called the geometric representation (see [Hum90, §5.3]). Note that the
subset {αs} ⊂ h∗ is linearly independent if and only if W is ﬁnite.
SOERGEL CALCULUS 19
(2) More generally , given a real vector space h with subsets {α∨
s } ⊂ h and {αs} ⊂
h∗ satisfying (3.1) then h is a realization of (W,S ). In [Soe07, §2] Soergel builds
his theory of Soergel bimodules for arbitrary Coxeter syste ms on a realization
for which both {α∨
s } ⊂ h and {αs} ⊂ h∗ are linearly independent, and such
that h has minimal dimension with this property . To construct such a rep-
resentation, Soergel mimics the construction of the action of an afﬁne Weyl
group on the Cartan subalgebra of an afﬁne Kac-Moody group.
(3) Let (X,R,X ∨,R ∨) be a (reduced) root datum (see [Spr98, §7.4] for notation)
and let ∆ ⊂R be a set of simple roots. Let (W,S ) be the corresponding Weyl
group and simple reﬂections. Then the triple h = X, {α | α ∈ ∆ } ⊂ h
and {α∨ | α ∈ ∆ } ⊂ h∗ = X ∨ gives a faithful realization of (W,S ) over
Z. We obtain a (potentially non-faithful) realization of (W,S ) over any k by
extension of scalars.
(4) More generally , if A is a generalized Cartan matrix and t denotes the Cartan
subalgebra of the corresponding Kac-Moody Lie algebra g(A) (see [Kac90,
Chapters 1 and 3]) then any choice of Z-lattices h ⊂ t such that h contains
the root lattice and its dual lattice h∗ ⊂ t∗ contains the coroot lattice yields
a realization of the Weyl group (W,S ) of g(A). In this way one obtains re-
alizations over Z (and hence over any k) of any Coxeter system for which
mst ∈ {2, 3, 4, 6, ∞} for alls ⁄=t ∈S. (Such Coxeter systems are called crystal-
lographic.)
(5) Let (W,S ) be a Coxeter system for which mst ∈ { 2, 3, 5, ∞} and let k = Z[φ]
whereφ = (1 +
√
5)/2 denotes the golden ratio. Let h = ⨁
s∈S kα∨
s and deﬁne
αs ∈ h∗ via
⟨α∨
s,α t⟩ =



2 ifs =t,
0 ifmst = 2,
−1 ifmst = 3,
−φ ifmst = 5,
−2 ifmst = ∞.
Using that −2 cos(π/5) = −φ it follows from the example of the geometric
realization that (h, {α∨
s }, {αs}) is a (symmetric) realization of (W,S ) over k.
In particular, the ﬁnite reﬂection groups of types H3 andH4 have symmetric
realizations over (any extension of) k.
(6) Let (W,S ) be the afﬁne Weyl group of type ~An for n ≥ 2. Let k = Z[q,q −1]
and h = ⨁
s∈S Z[q,q −1]α∨
s , and let the values of ⟨α∨
s,α t⟩ be encoded (as will be
