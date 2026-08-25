---
doc_id: arxiv-2301.02038v1
doc_title: "Vinogradov's Cohomological Geometry of Partial Differential Equations"
section_id: sec-009-31-homotopy-algebras
section_title: "homotopy algebras"
section_number: 3.1
pages: 18-25
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
doc_brief: "Vinogradov's Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a system of possibly non-li"
---
homotopy algebras that we will need in the rest of the paper. R oughly, a homotopy
algebra of a certain type (associative, Lie, etc.) is a grade d vector space equipped
with operations satisfying the algebra axioms only up to a co herent system of
higher homotopies . Homotopy algebras appear when cohomology and homotopy
interact with algebraic structures [ 14, 22 ]. We adopt the degree 1 convention on
the operations of a homotopy algebra, and we only work with (g raded) vector spaces
over a ﬁeld of zero characteristic.
Definition 3.1. AnL∞-algebra [13, 12 ] is a graded vector space V equipped
with a sequence l ={lk}k∈N of degree 1 symmetric multilinear brackets:
lk :
(
SkV
) •→V •+1, (v1,...,v k)↦→lk(v1,...,v k)
satisfying the following higher Jacobi identities :
(3.1)
∑
r+s=k
∑
σ∈Sr,s
ǫ(σ,v )ls+1
(
lr(vσ(1),...,v σ(r)),vσ(r+1),...,v σ(r+s)
)
= 0,
for all k∈ N, where Sr,s denotes (r,s )-unshuﬄes, and ǫ(σ,v ) is the Koszul sign
associated to the permutation σ of the homogeneous elements v1,...,v k∈V .
For k = 1 the identity (3.1) says that l1 : V • → V •+1 is a diﬀerential. In
particular there is a cohomology H •(V, l1) for every L∞-algebra (V, l). For k = 2
the identity (3.1) says that l1 is a derivation with respect to the binary bracket
VINOGRADOV’S COHOMOLOGICAL GEOMETRY OF PDES 19
l2 : (S2V )• → V •+1. For k = 3 the identity (3.1) says that l2 is a graded Lie
bracket only up to a homotopy encoded by l3. In particular l2 induces a honest
graded Lie bracket in cohomology H •(V, l1) (up to a décalage isomorphism that
we will ignore, for simplicity). So, whenever the cohomolog y of a cochain complex
supports a graded Lie bracket, it is natural to wonder whethe r or not it comes from
an L∞-algebra structure on cochains.
There is also a notion of L∞-module over an L∞-algebra.
Definition 3.2. An L∞-module [12] over an L∞-algebra (V, l) is a graded
vector space W equipped with a sequence m ={mk}k∈N of degree 1 multilinear
brackets:
mk :
(
Sk−1V⊗W
) •→W •+1, (v1,...,v k−1,w )↦→mk(v1,...,v k−1|w)
satisfying:
∑
r+s=k−1
∑
σ∈Sr,s
ǫ(σ,v )
[
ms+1
(
lr(vσ(1),...,v σ(r)),vσ(r+1),...,v σ(r+s)|w
)
+ (−)|vσ (1)|+···+|vσ (r)|mr+1
(
vσ(1),...,v σ(r)|ms(vσ(r+1),...,v σ(r+s)|w)
) ]
= 0
for all k∈ N, v1,...,v k−1∈V , w∈W .
In particular m1 :W •→W •+1 is a diﬀerential and m2 induces a honest graded
H •(V, l1)-module structure on H •(W, m1).
The next deﬁnition is a homotopy version of the notion of Lie- Rinehart algebra
(see [ 8, 9, 5, 7, 29, 31 ]).
Definition 3.3. An LR∞-algebra [29] ( LR for Lie-Rinehart) is a pair (A,L )
consisting of two graded vector spaces equipped with the fol lowing additional struc-
tures:
(1) L is an L∞-algebra with structure maps l;
(2) A is a commutative DG algebra with diﬀerential denoted m1;
(3) (L, l1) is a DG (A•, m1)-module;
(4) A is an L∞-module over (L•, l) with structure maps m (this means that
the 1-ary bracket is precisely m1).
Additionally, the maps
mk :
(
Sk−1L⊗A
) •→A•+1
are graded A-multilinear in the ﬁrst (k− 1)-arguments and they are a derivation in
the last argument. Finally the L∞-algebra brackets l satisfy the following Leibniz
rule:
lk(v1,...,v k−1,avk)
= mk(v1,...,v k−1|a)vk + (−)|a|(|v1|+···+|vk−1|+1)alk(v1,...,v k−1,vk),
for all v1,...,v k∈L, and a∈A.
Remark 3.4. Let (A,L ) be an LR∞-algebra with structure maps (m, l). Sim-
ilarly as for L∞-algebras and L∞-modules, the cohomology (H •(A, m1),H •(L, l1))
is then a graded Lie-Rinehart algebra.
20 F ABRIZIO PUGLIESE, GIOV ANNI SPARANO, AND LUCA VITAGLIAN O
As for Lie algebroids, there is a Chevalley-Eilenberg construction for LR∞-
algebras. Namely, let (A,L ) be an LR∞-algebra. Consider the graded commutative
algebra Sym•(A,L ) consisting of graded symmetric A-multilinear maps
S•L→A.
The structure maps (l, m) of (A,L ) induce on Sym•(A,L ) a sequence d ={dk} of
degree 1 derivations:
(3.2) dk : Symh(A,L )→ Symk+h−1(A,L )
given by
dkω(v1,...,v h)
=
∑
σ∈Sk−1,h
ǫ(σ,v )(−)|ω| ∑ k−1
i=1 |vσ (i)|mk
(
vσ(1),...,v σ(k−1)|ω(vσ(k),...,v σ(k+h−1))
)
+
∑
σ∈Sk,h −1
ǫ(σ,v )ω
(
lk(vσ(1),...,v σ(k)),vσ(k+1),...,v σ(k+h−1)
)
.
Proposition 3.5. The maps dk are well-deﬁned degree 1 derivations of the
graded algebra Sym•(A,L ). Additionally they satisfy
(3.3)
∑
r+s=k
[
dr, ds
]
= 0
for all k∈ N. In particular the total derivation
D := d1 + d2 +···
squares to zero, whenever deﬁned.
The pair (Sym•(A,L ), d) is called the Chevalley-Eilenberg algebra of (A,L ).
Remark 3.6. The derivation d2 does not square to 0 in general (it does only
up to a homotopy encoded by d3), however it induces a derivation which squares
to zero in the cohomology of d1. Hence H • (Sym(A,L ), d1), with the derivation
induced by d2, is a commutative DG algebra.
Remark 3.7. Let (A,L ) be an LR∞-algebra. If L is projective and ﬁnitely
generated as an A-module, then the Chevalley-Eilenberg algebra knows every thing
about (A,L ). More precisely, let A be a commutative graded algebra and let
L be a projective and ﬁnitely generated graded A-module. Then the Chevalley-
Eilenberg construction establishes a bijection between LR∞-algebra structures on
(A,L ) extending the preexisting structures on one side, and seque nces d ={dk} of
degree 1 derivations of Sym•(A,L ) satisfying both (3.2) and (3.3) on the other side.
3.2. the LR∞-algebra of secondary vector ﬁelds. Let (E, C ) be a diﬃ-
ety. According to Theorem 2.6 the pair (C ∞, X) is a graded Lie-Rinehart algebra.
Recall that C∞ = H •(E ) = H •(Ω( E ),d) and X = H •(E, V ) = H •(Ω( E, V ),d).
Moreover, the cochains Ω •(E, V ) are naturally a graded module over the cochains
Ω •(E ). It is then natural to look for an LR∞-algebra structure on cochains
(Ω •(E ), Ω •(E, V )) responsible for the Lie-Rinehart algebra structure on (C ∞, X).
SuchLR∞-algebra structure exists indeed as we now show.
Choose again a splitting (2.5) and use it to see transverse ve ctor ﬁelds and
horizontal forms as honest vector ﬁelds and diﬀerential for ms on E , as we did in
VINOGRADOV’S COHOMOLOGICAL GEOMETRY OF PDES 21
Subsection 2.3. We will also interpret horizontal forms wit h values in transverse
forms as ordinary vector valued forms.
The normal bundle V is now a (non-necessarily involutive) distribution on E .
Its curvature is
R :∧2V → C, (Y,Z )↦→R(Y,Z ) := [Y,Z ]− pr[Y,Z ],
where we denote by pr : T E→ V the projection, and can be seen as a vector valued
2-form on E :
R∈ V Ω 2(E )⊗ Γ( C )⊆ Ω 2(E,T E ).
In the following we will need to shift by 1 the degree in the graded module Ω •(E, V ).
Accordingly, we will denote by Ω •(E, V )[1] the new graded module whose degree
k component is Ωk+1(E, V ). We will also need the Nijenhuis-Richardson bracket
of vector valued forms [ 16, Section 16] that we denote [−,−]nr. We recall that
[−,−]nr maps an r-form and an s-form into an (r +s− 1)-form.
Theorem 3.8. A splitting (2.5) induces an LR∞-algebra structure on
(
Ω •(E ), Ω •(E, V )[1]
)
whose structure maps are given by
l1W =dW
l2
(
W,U
)
=−(−)|W |[W,U ]fn + [[R,W ]nr,U ]nr
l3
(
W,U,Z
)
=−[[[R,W ]nr,U ]nr,Z]nr
and
m1ω =dω
m2
(
W|ω
)
=−(−)|W |LWω +ι[R,W ]nrω
m3
(
W,U|ω
)
=−ι[[R,W ]nr,U]nrω
for all W,U,Z∈ Ω •(E, V )[1], and all ω∈ Ω •(E ), while lk = mk = 0 fork >3. The
graded Lie-Rinehart algebra structure induced in cohomology (Remark 3.4) agrees
with that of Theorem 2.6.
Remark 3.9. The degree 1 shift in the statement of Theorem 3.8 is due to
our convention on LR∞-algebra structure and can be removed choosing a diﬀerent
convention (see [ 29] for more details).
The graded Ω •(E )-module Ω •(E, V )[1] is projective and ﬁnitely generated. Ac-
cordingly, the LR∞-algebra structure of Theorem 3.8 can be also encoded into
the associated Chevalley-Eilenberg algebra. The Chevalle y-Eilenberg algebra of(
Ω •(E ), Ω •(E, V )[1]
)
is described in the next theorem.
Theorem 3.10. The Chevalley-Eilenberg algebra of the LR∞-algebra of Theo-
rem 3.8 is
Ω •(E,∧•V ∗)
with structure derivations given by
d1 =d
d2 =d−d +ιR
d3 =−ιR
22 F ABRIZIO PUGLIESE, GIOV ANNI SPARANO, AND LUCA VITAGLIAN O
while dk = 0 fork >3. In particular the total derivation D = d1 + d2 + d3 is just the
De Rham diﬀerential d. The DG algebra structure induced in cohomology (Remark
3.6) agrees with that of Theorem 2.7.
Remark 3.11. The LR∞-algebra of Theorem 3.8 is independent of the choice
of the splitting 2.5 up to LR∞-isomorphisms. We will not provide here a notion
of LR∞-morphism. We just mention that the independence of the LR∞-algebra(
Ω •(E ), Ω •(E, V )[1]
)
of the splitting is rigorously expressed by the fact that the
total derivation D = d1 + d2 +··· in the Chevalley-Eilenberg algebra of Theorem
3.10 is always the same, i.e. the De Rham diﬀerential, regard less of the splitting
we have chosen. See [ 29] for more details.
Theorems 3.8 and 3.10 provide indications towards Vinogradov’s conjecture
that the correct category where diﬀerential calculus on the space of solutions of a
PDE E0 should be developed is the homotopy category of DG-modules over the
horizontal De Rham algebra (Ω •(E ),d). They also suggest to add one further step
to the recipe presented at the end of Section 2. Namely
Secondarization Recipe (Addendum).
(5) Show that the cochains Ω •(E )⊗ V Φ support a homotopy algebra structure
responsible for the algebraic structure on Φ .
3.3. the A∞-algebra of secondary diﬀerential operators. In this ﬁnal
subsection we discuss secondary scalar diﬀerential operators . In order to deﬁne
them we follow the recipe presented at the end of Section 2. Le t (E, C ) be a
diﬃety. The construction Φ for which we want to ﬁnd a replacement on the space
of solutions of E0 is “ scalar diﬀerential operators ”, i.e. linear diﬀerential operators
from functions to functions (just DOs, for simplicity, in wh at follows).
For Step (1) in our recipe, we have to deﬁne transverse DOs . Intuitively, they
should be DOs taking derivatives just in the direction trans verse to C . Begin with
the (non-commutative) R-algebra DO(E ) of DOs
∆ : C∞(E )→C∞(E )
on E . As vector ﬁelds are DOs (of order 1), sections of C span a right ideal
Γ( C )·DO(E ) in DO(E ). Denote
VDO := DO(E )
Γ( C )·DO(E )
the quotient left DO(E )-module. By deﬁnition, VDO is the space of transverse
DOs.
For Step (2) in the recipe, we have to notice that VDO is equipped with an
action of the Lie algebroid C . This is indeed the case: left composition with a
section of C is indeed such action. Accordingly, the Ω •(E )-module
Ω •(E, VDO) := Ω •(E )⊗ VDO
is a DG (Ω •(E ),d)-module, whose diﬀerential we denote again by d.
In Step (3) we deﬁne secondary diﬀerential operators as the cohomology of
(Ω •(E, VDO),d):
DO :=H •(
Ω( E, VDO),d
)
.
For Step (4) we have to show that DO is equipped with the appropriate alge-
braic structure for DOs. Actually, we can show that DO is a graded associative
VINOGRADOV’S COHOMOLOGICAL GEOMETRY OF PDES 23
algebra (notice that, on the contrary, Ω •(E, VDO) is not a DG algebra in gen-
eral, as it does not possess a natural associative product). To do this, it is a good
idea to perform simultaneously Step (5) of the recipe (see th e end of the previous
subsection). The relevant homotopy algebras here are A∞-algebras.
Definition 3.12. AnA∞-algebra [13, 12 ] is a graded vector space U equipped
with a sequence a ={ak}k∈N of degree 1 multilinear maps:
ak :
( ⨂ kU
) •→U •+1, (u1,...,u k)↦→ak(u1,...,u k)
satisfying the following higher associativity conditions :
∑
r+s=k
r+s∑
j=1
(−)|u1|+···+|uj |as+1
(
u1,...,u j, as(uj+1,...,u j+r),uj+r+1,...,u r+s
)
= 0
for all k∈ N, and all u1,...,u k∈U .
It follows from the above deﬁnition that a1 is a diﬀerential, and it is a derivation
with respect to a2. Moreover a2 is associative up to a homotopy encoded by a3. In
particular a2 induces a honest associative product in cohomology H •(U, a1) (up to
décalage).
Theorem 3.13. The graded vector space Ω •(E, VDO)[1] can be equipped with
an A∞-algebra structure a such that a1 = d. Moreover, the induced associative
product in the cohomology DO is canonical.
The above theorem supports the interpretation of DO as secondary DOs, i.e.
(an appropriate replacement for) DOs on the space of solutio ns of E0.
We conclude the paper by sketching the proof of Theorem 3.13. As we will see,
the proof will also suggest an alternative Secondarization Recipe. From now on we
assume some familiarity with graded geometry (see, e.g., [ 15]). We begin recalling
a standard technique in homotopical algebra, namely the Homotopy Transfer (see
[14, 22 ]). The idea is that homotopy algebras can be transferred alo ng contraction
data. A set of contraction data is a diagram
(3.4) (A,δA)h
/d37/d37 p /d47/d47 (B,δB)
j
/d111/d111
where
(1) (A,δA) and (B,δB) are cochain complexes,
(2) p,j are cochain maps,
(3) h :A•→A•−1 is a homotopy,
such that
pj = idB and jp = [δA,h ]
and, moreover, the following side conditions are satisﬁed:
ph =hj =h2 = 0.
In particular p,j are mutually homotopy inverse homotopy equivalences and
H •(A,δA)∼
=H •(B,δB).
Theorem 3.14 (Homotopy Transfer) . Let (A,δA) be an associative DG alge-
bra and let (3.4) be a set of contraction data over a cochain co mplex (B,δB). Then
B[1] can be equipped with an A∞-algebra structure a, uniquely determined by the
24 F ABRIZIO PUGLIESE, GIOV ANNI SPARANO, AND LUCA VITAGLIAN O
associative product in A and the contraction data, such that a1 = δB. Moreover
(A,δA) and (B, a) induce the same graded associative algebra structure in coho mol-
ogyH •(A,δA)∼
=H •(B,δB).
There is a version of the Homotopy Transfer Theorem for L∞-algebras [ 6, 22 ]
and one, slightly more involved, for LR∞-algebras (see [ 30] for details). Actually
theLR∞-algebra of Theorem 2.6 can be obtained via Homotopy Transfe r. Namely,
let (E, C ) be a diﬃety. Consider the DG manifold C [1] obtained by the Lie algebroid
C → E by shifting by one the ﬁber degree. Clearly C∞(C [1]) =
Ω •(E ) and the
cohomological vector ﬁeld on C [1] is the horizontal De Rham diﬀerential d. The
pair
(
C∞(C [1]), X(C [1])
)
is a DG Lie-Rinehart algebra. The diﬀerential in X(C [1])
is the graded commutator of graded vector ﬁelds with the hori zontal De Rham
diﬀerential. Moreover, a splitting (2.5) uniquely determi nes contraction data
(3.5) X(C [1])h
/d37/d37 p /d47/d47 Ω •(E, V )
j
/d111/d111
that we can use to construct an LR∞-algebra structure on Ω •(E, V )[1] from the DG
Lie-Rinehart algebra structure on (C∞(C [1]), X(C [1])) (see [ 30] for details). This
means that the Lie-Rinehart algebra structure on secondary vector ﬁelds (C ∞, X)
is, equivalently, the one induced in cohomology by the DG Lie -Rinehart algebra
(C∞(C [1]), X(C [1])). A similar result holds for secondary DOs. Namely, consider
the space DO(C [1]) of graded DOs over the DG manifold C [1]. It is an associa-
tive DG algebra whose diﬀerential is the graded commutator o f graded DOs with
the horizontal De Rham diﬀerential. Now, a splitting (2.5), together with certain
additional data that we will not describe, uniquely determi ne contraction data
(3.6) DO
(
C [1]
)
h
/d39/d39 p /d47/d47 Ω •(E, VDO)
j
/d111/d111
that we can use to construct an A∞-algebra structure on Ω •(E, VDO)[1] from the
associative DG algebra structure on DO(C [1]). In particular there is a graded
associative algebra structure on secondary diﬀerential op erators
DO =H •(
Ω( E, VDO),d
) ∼
=H •(
DO(C [1])
)
induced by either the associative DG algebra structure on DO(C [1]) or the A∞-
algebra structure on
Ω •(E, VDO).
This discussion suggests the following alternative recipe to ﬁnd the secondary
analogue of a given construction Φ in diﬀerential geometry.
Secondarization Recipe.
(1) Apply the construction Φ to the DG manifold C [1] (when Φ is “vector
ﬁelds”, resp. “DO” we get X(C [1]), resp. DO(C [1])).
(2) Notice that Φ( C [1]) is canonically equipped with a diﬀerential induced by
the cohomological vector ﬁeld d on C [1] (when Φ is “vector ﬁelds”, resp.
“DOs”, such diﬀerential is the graded commutator of vector ﬁ elds, resp.
DOs, with d).
(3) Deﬁne Φ as the cohomology of Φ( C [1]) (when Φ is “vector ﬁelds”, resp.
“DOs”, then Φ is X, resp. DO).
(4) Notice that, being compatible with the diﬀerential, the alg ebraic structure
on Φ( C [1]) induces the same algebraic structure on Φ (when Φ is “vector
VINOGRADOV’S COHOMOLOGICAL GEOMETRY OF PDES 25
ﬁelds”, resp. “DOs”, then Φ = X, resp. Φ = DO, is a graded Lie-
Rinehart algebra, resp. a graded associative algebra).
Remark 3.15. Notice that, in the alternative Secondarization Recipe jus t
above there is no analogue of the Addendum (5) at p. 22. The rea son is that
the cochain complex Φ( C [1]) does possess the same (honest) algebraic structure as
Φ by deﬁnition, and there is no need to work with algebraic stru ctures up to homo-
topy at the level of cochains in this case. Nonetheless, by th e Homotopy Transfer
Theorem, cohomologies possess algebraic structures of the same type but only up to
homotopy. Moreover, cohomologies with their algebraic str uctures up to homotopy
are quasi-isomorphic to cochains with their algebraic stru ctures. In other words,
one can either choose to work with a larger space (cochains) a nd a simpler algebraic
structure, or with a smaller space (cohomologies) and a more complicated algebraic
structure (algebraic structure up to homotopy).
