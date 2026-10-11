---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-022-23-vertex-operator-algebras-and-weak-quasi-hopf-al
section_title: "Vertex operator algebras and weak quasi-Hopf algebras, unitarizing Rep(V_g^k)"
section_number: 23
pages: 138-146
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
23. Vertex operator algebras and weak quasi-Hopf algebras, unitarizing
Rep(Vgk)
In this section we describe some general Tannakian constructions of weak quasi-Hopf
algebras from the theory of vertex operator algebras (VOAs). This leads to some interesting applications to unitarizability of important examples of module categories of vertex
operator algebras including the affine examples and to new questions.
We will restrict to VOAs and conformal nets whose representation category are known
to be modular tensor categories. These are the rational VOAs satisfying the assumptions
in [93] and the completely rational conformal nets defined and studied in [107].
The main result of this section are Theorems 23.9 (a general result) and its most important application, Theorem 23.10 which give the construction of unitary structures on
ribbon braided tensor categories of modules of some vertex operator algebras, including

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 139
the affine vertex operator algebras Rep(Vgk
) at positive integer levels k of classical Lie
types and G2.
Our result is based on Wenzl work about the construction of unitary structures on fusion
categories of quantum groups at certain roots of unity [185] and on our proof of an analogue
of Kazhdan-Lusztig-Finkelberg equivalence theorem in the setting of vertex operator algebras, with Huang-Lepowsky ribbon braided tensor category structure, Theorem 2.11. To
obtain these unitary structures, weak quasi-Hopf algebras will play a role in transporting
the unitary structure from the setting of quantum groups to the setting of vertex operator
algebras following the general construction of Sect. 15. In this section we shall adopt
general Tannakian constructions described in the previous sections. Therefore at the end
of this section, we shall conclude with a positive result on unitarization of those Rep(Vgk
)
for the Lie types stated in Theorem 2.11 (the classical types and G2), but we shall not
give a full account on the unitary structure that we obtain. To this aim, we shall need
more work on canonical Tannakian constructions of weak Hopf algebras associated to the
quantum group fusion categories C(g, q, ℓ), and the complete proof of Theorem 2.11. This
will be done in Sect. 28–38. Therefore the unitary structure of Rep(Vgk
) will be clarified
in a more complete way by the end of the paper.
In the setting of rational conformal field theory, Moore and Seiberg observing an analogy
between certain polynomial equations that they had obtained and the structure of a braided
tensor category, discovered these structures in conformal field theory [129], [130]. It took
a long time and the work of many authors to construct braided tensor category structures
on the WZW models, and show that they they satisfy all the axioms of modular tensor
categories. The reader may find some history in the introduction of [149].
The first constructions were accomplished by the monumental work by Kazhdan and
Lusztig, Finkelberg. In a series of papers, inspired by the work by Kazhdan and Lusztig,
Huang and Lepowsky introduced a new notion of braided vertex tensor category and constructed this structure on Rep(V ) under certain general assumptions, one of the most
important being associativity of intertwining operators. This notion is stronger than the
notion of braided tensor category, and their methods for the tensor product module are
quite different from the work by Kazhdan and Lusztig and verification of the coherence
properties for the associativity morphisms and the braiding (pentagon and hexagon equations) is mostly included in their construction.
Let V be a VOA satisfying the rationality assumptions in [93], namely:
(a) V is simple and of CFT type (i.e. V(n) = 0 for n < 0, V(0) = C1) and the
contragredient module V
′
is isomorphic to V as a V -module;
(b) every Z≥0-graded weak module is a direct sum of irreducible V -modules;
(c) V is C2-cofinite, that is V/C2(V ) is finite dimensional, with C2(V ) the subspace of
V spanned by a(−2)b, for a, b ∈ V .
These rationality assumptions are motivated by the affine vertex operator algebras at
positive integer levels, and Virasoro vertex operator algebra. We refer the reader to [95]
for a review on the construction of vertex braided tensor category structure of Rep(V )

140 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
by Huang and Lepowsky, and references to the original articles, to the introduction of
[91] and Remark 3.8, and Theorem 3.9 therein for an explanation on the implication from
the rationality conditions (a), (b), (c) to the verification of the conditions needed for
the construction of Huang and Lepowsky vertex tensor category structure and to [93] for
more complete historical information and references, where the properties of rigidity and
modularity under these rationality conditions were proved by Huang.
It is important to note that this general braided tensor category construction was preceded by a direct application of Huang and Lepowsky tensor product theory to affine
vertex operator algebras at positive integer level (WZW model) in [89], where the authors
proved the conditions to apply their theory, including associativity of intertwining operators, building on previous work of several authors, including Knizhnik-Zamolodchikov
[114], Tsuchiya-Kanie [170], Frenkel-Huang-Lepowsky [59], Frenkel-Zhu [61], Dong, Li and
Mason [32]. In their work, validity of Knizhnik-Zamolodchikov differential equations for
products of intertwining operators is established at the level of formal variables, and it is
used to show the needed convergence of products of intertwining operators as functions of
complex variables, by Theorem 3.2 in [89].
Theorem 23.1. Let V be a VOA satisying the rationality assumptions (a), (b), (c). Assume moreover that M 7→ D(M) := dim(FV (M)), M irreducible, gives a weak dimension
function on the modular tensor category Rep(V ). Then, the Zhu’s algebra A(V ) admits the
structure of a weak quasi-Hopf algebra with a tensor equivalence EV : Rep(V ) → Rep(A(V ))
which, after composition with the forgetful functor : Rep(A(V )) → Vec is tensor isomorphic
to FV .
Proof. By Theorem 7.9 FV admits a weak quasi-tensor structure and the conclusion follows
from Theorem 7.6. □
Remark 23.2. The functor EV : Rep(V ) → Rep(A(V )) already appeared in the literature
without mention to the tensor structure, see [34, 96, 197].
Remark 23.3. The condition on M 7→ D(M), which we will call the weak dimension
condition, is not satisfied in general. For example if V is a rational unitary Virasoro VOA
then D(M) = 1 for all irreducible V-modules M. Moreover, from the known fusion rules
of these models, see e.g. [108, Sec. 2.2], it follows that one can always find an irreducible
M with D(M ⊗M) = 2 > D(M)
2 and hence the weak dimension condition is not satisfied.
On the other hand the class of rational VOAs satisfying the weak dimension condition
include many remarkable examples such as the unitary simple affine VOAs and the lattice
VOAs.
We now discuss the case of unitary affine VOAs. Let g be a complex simple Lie algebra
and let k be a positive integer. Moreover let gR ⊂ g be a real form of g and let G be
the corresponding simply connected compact simple Lie group. We denote by Vgkthe
level k affine simple unitary VOA associated to the pair (g, k). It is known to satisfy
the assumptions (a), (b), (c) so that Rep(Vgk) is a modular tensor category with HuangLepowsky ribbon braided tensor category structure. Accordingly we can consider the

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 141
functor FVgkwhich satisfies the weak-dimension condition so that the Zhu’s algebra A(Vgk
)
admits a weak quasi-Hopf algebra structure.
Now, let us consider the quantum group Uq(g) with
q = e
iπ
d(k+h∨)
, ℓ = d(k + h
∨
),
see Sect. 19 for a brief review, where h
∨
is the dual Coxeter number of g. Thus q is
a minimal root by Def. 20.2. Consider the fusion category C(g, q, ℓ) obtained from the
category of tilting modules recalled in Sect. 20. It is a modular braided category admitting
a compatible C
∗
-structure by [185, 194]. Let F(g,q): C(g, q, ℓ) → Vec be Wenzl functor.
Then F(g,q) satisfies the weak-dimension condition and hence it defines a weak quasi-Hopf
algebra A(g, q, ℓ) following the general procedure applied in Subsect. 20.4.
We next have the following remark that plays an important role in this paper.
Remark 23.4. By Theorem 2.11, the category C(g, q, ℓ) is tensor equivalent to Rep(Vgk
)
for the classical Lie types and G2. The weak dimension functions for the functors FVgkand
F(g,q) regarded as defined on the same family of irreducible objects, have the same range in
Z≥0. it follows that A(Vgk
) and A(g, q, ℓ) are, up to a twist, isomorphic weak quasi-Hopf
algebras, cf. the discussion after Theorem 7.9. (By the main result of [25], A(slN , q, ℓ)
admits a natural structure of weak Hopf algebra. We shall extend this result to the other
Lie types later on, and it will be useful) Here we have followed the original ideas of [125],
[82].
Note that the quantum group fusion category C(g, q, ℓ) is unitary and admits a weak
tensor functor to Hilb. Therefore A(g, q, ℓ) admits the structure of an Ω-involutive ribbon
weak quasi-Hopf algebra. Next we are going to use this fact to transport this unitary
structure to A(Vgk) following our general unitarizability results.
We now discuss the unitary aspects of the above constructions. To this aim, we shall not
need the detailed construction of weak Hopf algebras alluded to in the previous remark,
and general weak quasi-Hopf algebra constructions will suffice. We first need to recall some
properties of the Zhu’s algebra and fix some notation. From now on we shall mostly pass
to the following convenient notation, which is well known and very convenient.
Definition 23.5. (New grading notation for modes of module maps) Let a ∈ V be a
homogeneous element of conformal weight (or degree) d ∈ Z, i.e. such that L0a = da. For
every V -module M then a
M
n
is defined by
a
M
n
:= a
M
(n−1), n ∈ Z. (23.1)
For a general a ∈ V aM
n
is defined by linearity. With respect to the new notation (23.1)
and to the new gradation for the homogeneous subspaces of a module defined in (22.13),
the grading relation (22.11) becomes
a
M
n
: M(r) → M(r+d−n)for r ∈ R, n ∈ Z. (23.2)
Thus after a first increase by d = deg(a), energy further decreases by −n for n > 0 and
increases by −n for n < 0.

142 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
As a vector space the Zhu’s algebra is a quotient V/O(V ) for a certain subspace O(V ) ⊂
V and we denote by a 7→ [a] the quotient map : V → A(V ). When V satisfies the
assumption (a), (b), (c) then
O(V ) = {a ∈ V : a
M
d
↾M(0)= 0 for all V -modules M} , (23.3)
where d = deg(a). Moreover, for every V -module M the map [a] 7→ a
M
d
↾M(0) is a representation of the associative algebra A(V ) on M(0) which is the one corresponding to EV (M)
in Theorem 23.1.
Let V be a unitary VOA [22, 36] satisfying the rationality assumptions (a), (b), (c).
Note that if V is simple and unitary then a is necessarily of CFT type and isomorphic to
the contragredient module V
′ as a V-module so that (a) is a priori satisfied. Let θ be the
PCT operator giving the unitary structure on V . By [59, Eq. 5.3.1] and [34, Prop. 2.3.]
the map
[a] 7→ [e
L1
(−1)L0 a]
is an involutive anti-automorphism of A(V ). On the other hand, being θ an anti-linear
involutive automorphism of V , we have that θ(O(V )) = O(V ) and the map [a] 7→ [θa] is
an anti-linear involutive automorphism of the associative algebra A(V ). It follows that
[a] 7→ [a]
∗
:= [e
L1
(−1)L0 θa]
is an anti-linear involutive automorphism of A(V ) i.e. it gives a *-algebra structure on
A(V ) canonically associated to the unitary structure of A(V ).
Proposition 23.6. Let M be a unitary V -module then the restriction to M(0) of the invariant scalar product of M makes EV (M) into a *-representation of A(V ). Moreover, the
above restriction gives a one-to-one correspondence between the invariant scalar product
on M and the scalar products making EV (M) into a *-representation of A(V ).
Proof. The first claim follows in a straightforward way from the definition of invariant
scalar product and the *-operation on A(V ). Now, let U(M, V ) be the associative algebra
generated by the vertex operator coefficients a
M
(n)
, a ∈ V , n ∈ Z as before. U(M, V ) carries
a Z-grading
U(M, V ) = M
n∈Z
U(M, V )n
where
U(M, V )n := {X ∈ U(M, V ) : e
itLM
0 Xe−itLM0 = e
itnX} .
Accordingly, we have a
M
n ∈ U(M, V )n. Moreover, for every X ∈ M there is an X∗ ∈
U(M, V ) such that (m1, Xm2) = (X∗m1, m2) for all m1, m2 ∈ M(0), where (·, ·) is the
invariant scalar product on M. Note that (a
M
n
)
∗ = (eL1 (−1)L0 θa)M
−n
for all a ∈ V and all
n ∈ Z so that (U(M, V )n)
∗ = U(M, V )−n for all n ∈ Z. In particular U(M, V )0 is a *-
subalgebra of U(M, V ). For every X ∈ U(M, V )0 we have XM0 ⊂ M0 and hence X restricts
to an endomorphism X˜ of M0. Now, given m1, m2 ∈ M0 we have (Xkm1, Ynm2) = 0 if

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 143
k ̸= n. Accordingly we have
(Xm1, Y m2) = (m1,
X
n∈Z
(Xn)
∗Ynm2)
which shows that the invariant scalar product on M is determined by its restriction to M(0)
Now, let (·, ·) be a fixed invariant scalar product on M and let {·, ·} any scalar product
on M(0) making EV (M) into a *-representation of A(V ). Then there is an A(V )-module
isomorphism T0 : M(0) → M(0) such that {m1, m2} = (m1, T0m2) for all m1, m2 ∈ M(0).
Since EV is an equivalence of categories there is a unique V -module map T : M → M
such that EV (T) = T0 and we can define a sesquilinear form {·, ·}M on M by {m1, m2}M =
(m1, Tm2), m1, m2 ∈ M. It is now straightforward to check that {·, ·}M is an invariant
scalar product on M whose restriction to M(0) is {·, ·}. □
Remark 23.7. Let V a unitary vertex operator algebra satisfying the assumptions (a),
(b), (c) so that Rep(V ) is a modular tensor category. Let Rep+(V ) be the C
∗
-category of
unitary representations of V . Then the forgetful functor : Rep+(V ) → Rep(V ) is linear
equivalence if and only if every V -module is unitarizable. In this case Rep+(V ) is equivalent as a C
∗
-category to the representation category Rep+(A(V )) of finite dimensional
*-representations of the C
∗
-algebra A(V ). It is not clear in general if the linear equivalence Rep+
(V ) ≃ Rep(V ) can be used to make Rep+(V ) into a tensor C
∗
-category tensor
equivalent to Rep(V ). This is an important problem which has been recently solved in
some special cases by B. Gui [73, 74]. We also recall a work by Kirillov on the construction
of a tensor ∗-category closely related to Rep(V ) which preceded the work by Huang and
Lepowsky [113].
Proposition 23.8. Let V a unitary vertex operator algebra satisfying the assumptions (a),
(b), (c). Then the equivalence EV : Rep(V ) → Rep(A(V )) gives in a canonical way a faithful *-functor E
+
V
: Rep+(V ) → Rep+(A(V )). If the forgetful functor Rep+(V ) → Rep(V )
is an equivalence of linear categories then A(V ) is a C
∗
-algebra and E
+
V
: Rep+(V ) →
Rep+(A(V )) is an equivalence of C
∗
-categories. Moreover, in the latter case, any equivalence of linear categories SV : Rep(A(V )) → Rep(V ) together with an isomorphism
η : EV ◦ SV → 1Rep(A(V )) gives a canonical *-equivalence S
+
V
: Rep+(A(V )) → Rep+(V )
with E
+
V
◦ S
+
V
unitarily equivalent to the identity.
Proof. Let M be a unitary V -module. Then E
+
V
(M) is defined to be the A(V )-module
EV (M) together with the scalar product obtained by restricting the given invariant scalar
product on M. Then, thanks to Prop. 23.6 E
+
V
is a faithful *-functor which become an
equivalence if the forgetful functor : Rep+(V ) → Rep(V ) is a linear equivalence.. In the
latter case we have the linear eqivalence Rep(A(V )) ≃ Rep+(A(V )) and hence A(V ) is a C
∗
-
algebra. Assume now the linear equivalence Rep+(V ) ≃ Rep(V ) and let SV : Rep(A(V )) →
Rep(V ) be an equivalence with a natural isomorphism η : EV ◦SV → 1Rep(A(V )). Let W be a
C
∗
-module for A(V ) and let (·, ·)W be the corresponding scalar product. Then (ηW · ηW ·)W
is a scalar product on EV ◦SV (W) making it into a *-representation of A(V ). Then it follows
from Prop. 23.6 and the assumption Rep+(V ) ≃ Rep(V ) that there is a unique invariant
scalar product on SV (W) which restricts to (ηW · ηW ·)W . This scalar product defines a

144 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
unitary V -module S
+
V
(W) and it is not hard to see that the map W 7→ S
+
V
(W) defines a
functor with the desired properties. □
Theorem 23.9. Let V be a unitary vertex operator algebra satisfying assumptions (a),
(b), (c) and such that the forgetful functor : Rep+(V ) → Rep(V ) is a linear equivalence
and assume that the functor FV : Rep(V ) → Vec satisfies the weak dimension condition
in Remark 23.3. Then Rep+(V ) admits a structure of tensor C
∗
-category with unitary
braided symmetry such that the forgetful functor: Rep+(V ) → Rep(V ) is a braided tensor
equivalence if and only if the weak quasi-Hopf algebra on A(V ) obtained from a weak quasitensor structure on the functor FV : Rep(V ) → Vec admits the structure of a Ω-involutive
weak quasi-Hopf C
∗
-algebra compatible with the canonical *-structure on A(V ).
Proof. The functor F
+
V
: Rep+(V ) → Hilb obtained by composition of the equivalence
E
+
V
: Rep+(V ) → Rep+(A(V )) with the forgetful functor : Rep+(A(V )) → Hilb is a
*-functor as a consequence of Prop. 23.8. If Rep+(V ) admits a structure of tensor C
∗
-
category such that the forgetful functor : Rep+(V ) → Rep(V ) is a tensor equivalence then
F
+
V
admits a weak quasi-tensor *-structure so that Nat0(F
+
V
) admits the structure of a weak
quasi-Hopf C
∗
-algebra as a consequence of Theorem 13.5. By construction the C
∗
-algebra
A(V ) with its canonical *-operation is isomorphic to Nat0(F
+
V
) so that it inherits from the
latter the structure of a Ω-involutive weak quasi-Hopf C
∗
-algebra coinciding , up to a twist,
with the weak quasi-Hopf algebra structure on A(V ) obtained from a weak quasi-tensor
structure on the functor FV : Rep(V ) → Vec.
Conversely, if A(V ) admits the structure of a Ω-involutive weak quasi-Hopf C
∗
-algebra
with the canonical *-structure then, by Corollary 12.6 Rep+(A(V )) is a tensor C
∗
-category
tensor equivalent Rep(A(V )) and hence to Rep(V ) . Let SV : Rep(A(V )) → Rep(V ) be any
tensor equivalence together with an isomorphism of tensor functors η : EV ◦SV → 1Rep(A(V ))
and let S
+
V
: Rep+(A(V )) → Rep+(V ) be the corresponding canonical *-equivalence as in
Prop. 23.8 so that E
+
V
◦ S
+
V unitarily equivalent to the identity.
Given unitary V -modules Mα, Mβ ∈ Rep+(V ) we define a unitary module Mα ⊗Mβ by
Mα ⊗ Mβ:= S
+
V

E
+
V
(Mα) ⊗ E
+
V
(Mβ)

.
Moreover, if α denotes the unitarty associator in Rep+(A(V )) we define the unitaries
α
′
Mα,Mβ,Mγ : (Mα ⊗ Mβ
) ⊗ Mγ → Mα ⊗ (Mβ ⊗ Mγ)
by
α
′
Mα,Mβ,Mγ :=
S
+
V
(1E
+
V
(Mα) ⊗ η
−1
E
+
V
(Mβ)⊗E
+
V
(Mγ)
◦ αE
+
V
(Mα),E
+
V
(Mβ),E
+
V
(Mγ)
◦ ηE
+
V
(Mα)⊗E
+
V
(Mβ) ⊗ 1E
+
V
(Mγ)
)
where η : EV ◦ SV → 1Rep(A(V )) is the isomorphism used to define the functor S
+
V
.
Then, thanks to Prop. 23.8, one can check that this gives the desired C
∗
- tensor structure
on Rep+(V ). From the tensor equivalence Rep+(V ) ≃ Rep(V ) we see that Rep+(V ) admits
a braiding making the equivalence a braided tensor equivalence and this braided symmetry
on Rep+(V ) is necessarily unitary by [66]. □

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 145
Theorem 23.10. Let g be a complex simple Lie algebra of classical Lie type or G2, and
let k be a positive integer and let Vgkbe the corresponding level k affine unitary vertex
operator algebra. Then Rep+(Vgk
) admits the structure of tensor C
∗
-category with unitary
braided symmetry such that the forgetful functor : Rep+(Vgk
) → Rep(Vgk
) is a braided
tensor equivalence.
Proof. It is known that every Vgk
-module is unitarizable and hence Rep+(Vgk
) ≃ Rep(Vgk
).
Let q = e
iπ
d(k+h∨)
. Then the quantum group category C(g, q, ℓ) is a tensor C
∗
-category by
[185, 193]. It follows from Theorem 2.11 that C(g, q, ℓ) ≃ Rep(Vgk
) that A(Vgk
) admits the
structure of a Ω-involutive weak quasi-Hopf C
∗
-algebra and the conclusion follows from
Theorem 23.9. □
Remark 23.11. Theorem 23.10 has been recently proved by B. Gui by directly working
on modules [73], [74].
Theorem 23.10 can be seen as a special case of the following more abstract result which
we will use to give other examples of unitary VOAs such that Rep+(V ) admits a tensor
C
∗
-structure.
Theorem 23.12. Let V be a unitary vertex operator algebra satisfying assumptions (a),
(b), (c) and such that the forgetful functor : Rep+(V ) → Rep(V ) is a linear equivalence
and assume that the functor FV : Rep(V ) → Vec satisfies the weak dimension condition
in Remark 23.3. Assume that Rep(V ) is tensor equivalent to a tensor C
∗
-category. Then
Rep+(V ) admits a structure of tensor C
∗
-category with unitary braided symmetry such that
the forgetful functor: Rep+(V ) → Rep(V ) is a braided tensor equivalence.
Proof. □
We now give some examples of applications of Theorem 23.12.
Example 23.13. Let L be an even positive definite lattice and let VL be the corresponding
unitary VOA. It satisfies assumptions (a), (b), (c). It follows from [36, Th. 4.12] the
forgetful functor Rep+(V ) → Rep(V ) is a linear equivalence. The fusion ring of Rep(VL)
is isomorphic to the finite abelian group L
∗/L, where L∗
is the dual lattice of L. For an
irreducible VL-module M[x], with equivalence class corresponding to [x] ∈ L
∗/L we have
D(M[x]) = N[x], where N[x]is the number of elements of L
∗
in the equivalence class [x]
having minimal norm, see e.g. [65]. In some cases, e.g. square lattices, one can easily
check that D is a weak dimension function. The irreducible objects of Rep(VL) are all
invertible their equivalence classes form a finite abelian group G ≃ L
∗/L. It follows
that Rep(VL) is tensor equivalent to Vecω
G for some 3-cocycle ω ∈ Z
3
(G, T), where Vecω
G
is the category of G-graded finite dimensional vector spaces with associators twisted by
ω, see [50]. Vecω
G is tensor equivalent to the tensor C
∗
-category Hilbω
G of G-graded finite
dimensional Hilbert spaces with associators twisted by ω and hence, if VL satisfies the weak
dimension property, Rep+
(VL) admits a structure of a tensor C
∗
-category with unitary
braided symmetry making the forgetful functor : Rep+(VL) → Rep(VL) into a braided
tensor equivalence.

146 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Example 23.14. Let V be a unitary VOA satisfying assumptions (a), (b), (c) and assume
that V is holomorphic i.e. that Rep(V ) is equivalent to Vec. Let G be a finite subgroup of
the unitary automorphism group of V and let V
G be the corresponding orbifold unitary sub
VOA. It is conjectured that always V
G satisfies (a), (b), (c) and that Rep(VG) is braided
tensor equivalent to Rep(Dω(G)) ≃ Z(Vecω
G), for some 3-cocycle ω ∈ Z
3
(G, T). Here,
Dω(G) the twisted quantum double quasi-Hopf algebra introduced in [31] and Z(Vecω
G) is
the center of Vecω
G, [50]. This conjecture is known to be true in various cases, see e.g.
[21, 37, 112, 136]. Assume now that the above conjecture is true for a given V and G and
also assume that every irreducible V
G-module is unitarizable. Since Rep(Dω
(G)) is tensor
equivalent to a tensor C
∗
-category then, if V
G satisfies the weak dimension property,
Rep+(V
G) admits a structure of a tensor C∗
-category with unitary braided symmetry
making the forgetful functor : Rep+(V
G) → Rep(VG) into a braided tensor equivalence.
Let us know consider an explict example. Let Λ be the Leech lattice, the even unimodular
lattice of rank 24 with trivial root system, and let let VΛ be the corresponding lattice VOA.
Since Λ = Λ∗, VΛ is holomorphic. VΛ as special automorphism of order two which can easily
seen to be unitary, see [36, Sec. 4.4] where this automorphim is denoted by θ. As usual we
denote by V
+
Λ
the corresponding unitary fixed point subalgebra. V
+
Λ
satisfies (a), (b) and
(c). Moreover, up to equivalence it has exactly four irreducible modules V
+
Λ
, V
−
Λ
, (V
T
Λ
)
+
and (V
T
Λ
)
− which are all invertible and unitarizable [36, 37]. Hence the equivalence classes
of irreducibles form an abelian group of order 4 which in fact is isomorphic to Z2 × Z2,
see e.g. [37, Prop.5.6]. Arguing as before can conclude that Rep(V
+
Λ
) is tensor equivalent
to a tensor C
∗
-category. The characters (graded dimensions) of the irreducible modules
of V
+
Λ
are known, see [60, Sec. 10.5] and [164, Prop. 2.5] and from them one can easily
compute the function M 7→ D(M) = dimFV
+
Λ
(M) and we find D(V
+
Λ
) = 1, D(V
−
Λ
) = 24,
D

(V
T
Λ
)
+

= 212 and D

(V
T
Λ
)
−

= 24 · 2
12. It follows that V
+
Λ has the weak dimension
property and hence , by Theorem 23.12, Rep+(V
+
Λ
) admits a structure of tensor C
∗
-category
with unitary braided symmetry such that the forgetful functor: Rep+(V
+
Λ
) → Rep(V
+
Λ
)
is a braided tensor equivalence. With this structure Rep+(V ) is a modular tensor C
∗
-
category because Rep(V
+
Λ
) is modular. The modular T matrix of Rep+(V ) can also be
computed from the characters and it is given by the diagonal matrix with diagonal entries
1, 1, 1, −1. By [160] there is, up to equivalence, a unique unitary fusion category with
fusion rules Z2 × Z2, the above T matrix and topological central charge 24 mod 8 and
it is realized by the representation category of the quantum double D(Z2), with trivial
twist ω ∈ H3(Z2, T) ≃ Z2. Note that, A(V
+
Λ
) and D(Z2) have equivalent representation
categories but are inequivalent associative algebras. D(Z2) is commutative while A(V
+
Λ
)
is not. Note also that D(Z2) is a Hopf algebra while A(V
+
Λ
) is a weak quasi-Hopf algebra.
