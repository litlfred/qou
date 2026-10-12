---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-013-14-unitarizability-of-representations-and-rigidity
section_title: "Unitarizability of representations and rigidity"
section_number: 14
pages: 100-109
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
14. Unitarizability of representations and rigidity
Let A be a complex ∗-algebra either unital or discrete. In this section we are motivated
by studies of direct constructions of unitary structures on some objects of Rep(A) where
A is a suitable algebra arising in an application. In categorical terms we want to construct
objects of Rep+(A) and obtain a nontrivial linear C
∗
-category.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 101
In order to construct objects of Rep+(A), we need to know which representations of A
are equivalent to C
∗–representations. In this section we abstract to A procedures used in
the setting of group theory, quantum groups at generic parameters or at roots of unity.
This last case is of main interest in our paper, because we see a similar procedure in the
setting of vertex operator algebras, and wish to look for a unified description between the
two settings.
In the case of representations of quantum groups at roots of unity Uq(g) and rational
vertex operator algebras V , the question splits into a first step which reduces the problem
to the search of invariant Hermitian forms on the representation space. We discuss this
first step in abstract terms here looking for objects of Reph(A). Both cases are covered by
the assumption that A is discrete, but this can not be our starting assumption as Uq(g)
is not semi-simple. Later on we shall discuss Wenzl functor defined on the semi-simple
fusion category associated to Uq(g) which gives rise to a discrete quotient A of Uq(g) that
keeps all the information of the linear structure of the category. This discrete algebra
plays in fact an important role in showing that all its irreducible representations become
C
∗
-representations compatibly with a natural ∗-involution of Uq(g) in [185]. We shortly
comment some more on this, for details on the construction of this algebra, see Sect. 31.
The question of making representations of the discrete algebra A into C
∗
-representations
is equivalent to making A into a C
∗
-algebra. Until discussing more in detail the construction of the discrete algebra, we may think of A to be the non-semisimple unital ∗
-algebra
A = Uq(g).
Regarding the case of vertex operator algebras, representations are infinite dimensional.
To unify with the case of quantum groups, the main important point is to look at the Zhu
algebra
A = A(V )
associated to a vertex operator algebra V , which is associative, finite dimensional and
discrete under some rationality assumptions on V recalled in Sect. 23. We develop a
general correspondence between invariant Hermitian forms of modules of a vertex operator
algebra under suitable conditions and invariant Hermitian forms on modules of the Zhu
algebra, see Prop.23.6.
The second step regards verification of positivity of Hermitian forms, and is studied in
a direct way in applications. We do not develop an abstract theory for this, although it is
apparent that methods are of a similar nature. We discuss in detail in this paper the case
of affine vertex operator algebras at a positive integer level and quantum groups at certain
roots of unity via the mentioned unified algebraic method. The complete result is of course
not new, and may be regarded as going back to the work of Kac on the vertex operator
algebra or affine Lie algebra side (where one has unitary representations of the compact
real form of g) and of Wenzl on the quantum group side. However, the unified viewpoint
via discrete algebras A may have been overlooked in the literature. This viewpoint is
perhaps of help to discuss how positivity of the Hermitian form in the quantum group
side may be seen as derived from positivity on the vertex operator algebra side following
Wenzl continuous path argument that connects the two setting on each relevant irreducible

102 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
representation, of the Zhu algebra and of the discrete algebra associated to the quantum
group. The unitary structure gives a connection from the module category of the VOA to
the module category of a semisimple quotient of the quantum group. Then after getting
to the setting of quantum groups, over the discrete algebra we construct a unitary weak
Hopf algebra structure compatible with the fusion category structure, and extend Wenzl
connection to the module categories.
This suggests to study more connections between unitarizable quantum group fusion
categories and vertex operator algebra fusion categories.
After these motivating remarks, we start with A, and pose a question more precisely.
Given a (nondegenerate f.d.) representation ρ of A, is there and how do we construct a
∗
-representation σ of A on a nondegenerate Hermitian space equivalent to ρ? Do Hermitian
representations naturally arise or are they just a more general convenient setting to study
unitary representations?
This first step is related to the study of the contragredient representation of a representation ρ of A and its relation with the conjugate representation. This is related to the
study of rigidity of Rep(A) if A has the structure of a weak quasi-Hopf algebra.
Recall that the contragredient representation ρ
c
(or cρ) has been defined in Def. 7.3 on
the dual vector space V
∗
ρ by means of an invertible antimultiplicative map S : A → A. The
conjugate representation acts on the conjugate vector space Vρ, and is defined here below
in (14.1) and depends on S as well and the ∗-operation.
In order to have a nondegenerate Hermitian form on the space Vρ, by Riesz representation
theorem we at least need to find a canonical linear invertible map
Φ : ξ ∈ Vρ → Φξ ∈ V
∗
ρ
.
Our first result, Prop. 14.2, shows that the existence of such a Φ which in addition is an
intertwiner between the conjugate representation ρc on Vρ and the contragredient representation ρ
c on V∗
ρ
is a necessary condition for the existence of a nondegenerate Hermitian
form on Vρ making ρ into a ∗-representation. This intertwining condition corresponds to
invariance in the setting of vertex operator algebras. Moreover, this condition is also sufficient if ρ is irreducible, and the Hermitian form is unique up to scalar multiples. From
this point one can further study the case where ρ is a C
∗
-representation in applications.
For example, this is the case if A is a discrete C
∗
-algebra, by Cor. 14.3. This Corollary
is well known in some applications, for example in the theory of compact groups.
Recall the definition of contragredient representations ρ
c and cρ given in 7.3. Fur possible future applications, it is important to note that by Prop. 7.4 the contragredient
representations have a natural description in the setting of weak quasi-Hopf algebras, and
therefore of tensor categories, because they solve the duality equations of the tensor category Rep(A) making it into a rigid tensor category. On the other hand, one may work with
the contragredient representations without any tensor structure. Indeed the contragredient representations may be defined more generally in the case where A is only a complex
algebra, always assumed either unital or discrete to avoid degeneracies, endowed with a
linear invertible antimultiplicative map S : A → A. Thus we only need a pair (A, S). It

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 103
follows that the contragredient representations ρ
c and cρ are nondegenerate by invertibility
of S and clearly with the same dimension as ρ.
This more general starting point is important for applications to a vertex operator
algebra V , where one may start with the Zhu algebra A(V ) associated to V , which is known
to be associative, unital and endowed an invertible map S, known as Zhu’s antipode.
Let now (A,∗, S) be a triple with (A,∗) a complex ∗-algebra as at the beginning of
the section, and S : A → A an invertible linear antimultiplicative map. Then to any
nondegenerate finite dimensional representation ρ on a vector space we may associate two
more representations, ρc and cρ both acting on the conjugate vector space Vρ via
ρc(a)ξ = ρ(S(a)
∗
)ξ, cρ(a)ξ = ρ(S−1(a)
∗
)ξ. (14.1)
Remark 14.1. Alternatively, we may consider the representations acting on Vρ via ξ →
ρ(S(a
∗
))ξ and ξ → ρ(S−1(a
∗
))ξ. However, if (A, S,∗) can be completed to the structure
of an Ω-involutive a weak quasi-Hopf algebra (A, ∆, Φ, S, α, β,∗, Ω), then the two further
representations defined above are equivalent to cρ and ρc respectively. Moreover, there are
equivalences ρcc ≃ ρ ≃ ccρ. These properties easily follow from Prop. 11.16.
The following proposition is an abstraction of the construction of Kashiwara inner product, and of Lemma. 2.2 and Prop. 2.3 of [185].
Proposition 14.2. Let (A,∗, S) be be given as above, and let ρ be a finite dimensional
nondegenerate vector space representation of A.
a) If ρ is equivalent to a ∗-representation on a nondegenerate Hermitian space then
there is a linear invertible map
ξ ∈ Vρ → Φξ ∈ V
∗
ρ
, (resp. Φ
′
: ξ ∈ Vρ → Φ
′
ξ
∈ V
∗
ρ
)
which is an equivalence between the representations
Φ : ρc → ρ
c
, (resp. Φ
′
: cρ → cρ)
such that the Hermitian form of Vρ is given by
(ξ, η) = Φξ(η), (resp. (ξ, η) = Φ′
ξ
(η))
b) if ρ is irreducible and if ρ
c ≃ ρc (or cρ ≃ cρ) then ρ is equivalent to a ∗
-representation
on a nondegenerate Hermitian space and the associated Hermitian form is unique
up to a nonzero real scalar.
Proof. a) If ρ is equivalent to the ∗-representation σ via the invertible T ∈ (ρ, σ) we may
endow the space of ρ with the nondegenerate Hermitian form making T unitary, and in
this way ρ becomes a ∗
-representation. It follows that we may canonically identify the
conjugate space Vρ with V
∗
ρ
, via the invertible map
ξ ∈ Vρ → Φξ ∈ V
∗
ρ
,
where Φξis the functional η → (ξ, η). A computation shows that Φ is an equivalence
between ρ
c acting on V∗
ρ
and the representation acting on Vρ as ξ ∈ Vρ → ρ(S(a))∗ξ =

104 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
ρ(S(a)
∗
)ξ = ρc(a)ξ. (Similarly, cρ turns into cρ.) b) Let Φ ∈ (ρc, ρc) be an invertible
morphism, and introduce a sesquilinear form on Vρ by (ξ, η) = Φξ(η), clearly nondegenerate. Let us define the right and left adjoint of a linear map T : Vρ → Vρ respectively by (T
∗
ξ, η) = (ξ, T η) and (ξ, ∗T η) = (T ξ, η). A computation using the intertwining property of Φ shows that for a ∈ A, ρ(a)
∗ = ρ(a∗
) = ∗ρ(a). Let us introduce
an inner product (ξ, η)pos in Vρ making some basis orthonormal, let T → T
† be the
corresponding adjoint map and B : Vρ → Vρ be the unique invertible map such that
(ξ, η) = (ξ, Bη)pos. Then T
∗ = B−1†
T
†B† and ∗T = B−1T†B. Equating ρ(a)∗ = ∗ρ(a)
gives B−1†Bρ(a) = ρ(a)B−1†B, hence B†is a scalar multiple of B by irreducibility of ρ.
But ∥B∥ = ∥B†∥ (norm associated to (ξ, η)pos) and it follows that this scalar lies in T.
Hence after rescaling B we get B† = B, and finally derive that (ξ, η) is Hermitian. Finally,
with a similar argument, if ρ is irreducible and unitary on a Hermitian space with Hermitian form (ξ, η) then any other nondegenerate Hermitian form on the same space making ρ
∗
-invariant, when written as (ξ, Aη) with A invertible and selfadjoint, implies that A is a
real scalar. □
Let us now discuss the tensorial aspects. If in particular (A, S) upgrades to a weak
quasi-Hopf algebra (A, ∆, Φ, S, α, β) then Rep(A) is a rigid tensor category. Indeed, the
contragredient ρ
c and cρ are a right and left dual of ρ in Rep(A) respectively, by Prop. 7.4.
If (A,∗) upgrades to the structure of an Ω-involutive weak quasi-bialgebra (A, ∆, Φ,
∗
, Ω),
then Reph(A) is a tensor ∗-category by Thoerem 12.5. When is Reph(A) rigid?
Given (A,∗, S), and a representation ρ of A equivalent to a ∗-representation, e.g. it
satisfies condition b) of Prop. 14.2, then ρ becomes a ∗-representation of A. On the other
hand, the contragredient representations ρ
c and cρ are not necessarily ∗
-representations if
S does not commute with ∗.
This is well known to occur in the setting of compact quantum groups, although it does
not occur in the setting of quantum groups at roots of unity, or in the setting of unitary
vertex operator algebras because S commutes with ∗. In the case where one is able to make
any nondegenerate f.d. representation of A equivalent to a ∗-representation, then one can
apply this procedure to the contragredient representations, and this second step provides
with equivalent ∗-representations on nondegenerate Hermitian spaces. This connects with
the work done in the setting of compact quantum groups. In this section we discuss this
second step as well in the setting of weak quasi-Hopf algebras.
Recall that the definition of conjugate object in a tensor ∗-category is usually given
as in Def. (5.11). But is equivalent to that of the underlying tensor category. A more
precise discussion is before formula (5.11). On the other hand, the underlying category of
Reph(A) is not Rep(A), but Rep(A) and Reph(A) are equivalent iff every object of Rep(A)
is equivalent to a ∗-representation.
A ∗–representation ρ ∈ Reph(A) has a conjugate in Reph(A) if and only if the canonical
right dual ρ
c
introduced in Def. 7.3 is equivalent to a ∗-representation, the latter is a
conjugate ρ of ρ. If this is the case the canonical left dual cρ will be automatically equivalent
to ρ
c and ρ as well, and the double dual ρcc to ρ.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 105
Summarizing, if (A,∗, S) has the structure of an Ω-involutive weak quasi-Hopf algebra
then Reph(A) a tensor ∗-category and is rigid as a tensor category. If every representation
is equivalent to a ∗-representation then Reph(A) is a rigid tensor ∗-category.
In the setting of this section, this amounts to verify that the contragredient representations, which solve the right and left duality equations in Rep(A) are equivalent to
∗
-representations.
Corollary 14.3. Let (A,∗, S) be a discrete C
∗
-algebra. Then every representation is equivalent to a C
∗
-representation. In particular if A has the structure of a Ω-involutive (unitary) weak quasi-Hopf algebra then Reph
(A) (Rep+(A)) is rigid and the forgetful functor
Reph(A) → Rep(A) (Rep+(A) → Rep(A)) is a tensor equivalence.
Proof. Let ρ be a representation of A that we may assume irreducible by complete reducibility. Note that the antipode S permutes the minimal central idempotents of A and
that these idempotents are selfadjoint since the involution of A is positive by assumption,
see Def. 11.5. This implies that ρc and ρ
c have the same central support, and therefore
they are related by an isomorphism T. We may then apply Prop. 14.2. Note also that a
nonzero scalar multiple of T induces a positive inner product on the space of ρ by the classification of Hermitian forms associated to involutive discrete weak quasi-Hopf algebras,
Prop. 12.10, hence the conclusion follows also in the case where Ω is positive.
□
By the end of the section we shall identify the conjugates in the tensor C
∗
-category
Rep+(A) in the discrete weak Hopf case. We next discuss some results guaranteeing rigidity
in possibly non-semisimple tensor categories motivated by the work of Kashiwara, Kirillov,
Wenzl for Uq(g) at roots of unity [104, 111, 185]. Recall that the element ω was defined in
Prop. 11.16.
Proposition 14.4. Let A be an Ω-involutive weak quasi-Hopf algebra and ρ a
∗
-representation
equivalent to ρ
cc. Then
a) ρc is equivalent to a ∗–representation if and only if there is an invertible Kρ ∈ (ρ, ρcc)
such that Fρ := Kρρ(ω
∗
) is selfadjoint with respect to the Hermitian form of ρ. In
this case, the forms making ρc into a ∗-representation are parametrised by Kρ via
(ξ, η) = (η, Fρξ),
b) if ρ is a C
∗
-representation then ρc is equivalent to a C
∗
-representation if and only
if Fρ can be chosen positive,
c) if ρ is irreducible then ρc is equivalent to a ∗-representation. The associated Kρ ∈
(ρ, ρcc) is unique up to a real scalar multiple.
Proof. a) If ρc is equivalent to a ∗–representation then ρcc and ρ
c
c
are equivalent by the
previous proposition, and let Ψ be this equivalence. We may write Ψ as the composite of
ρ(ω
∗
) : ρcc → ρ with an equivalence Kρ : ρ → ρ
cc in turned followed by Φt
: ρ
cc → (ρc)c
,
where Φ : ρc → ρ
c
is defined as in the proof of a) of Prop. 14.2, and Φtis the transposed
of Φ. The Hermitian form making ρc into a ∗-representation is given by (ξ, η) = Ψξ(η).

106 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
An explicit computation shows that this is precisely the form in the statement. Conversely, for any Kρ ∈ (ρ, ρcc), the sesquilinear form defined by Fρ = Kρρ(ω
∗
) is Hermitian (positive) precisely when Fρ is selfadjoint (positive). A computation shows that
(ρc(a)ξ, η) = (ξ, ρc(a
∗
)η), in other words ρc is a ∗-representation. The proof of b) is now
clear. c) By irreducibility and b) of Prop. 14.2, it suffices to show that ρcc ≃ (ρc)
c
. Now
such an equivalence can be obtained as in the proof of a) starting from the choice of an
invertible Kρ ∈ (ρ, ρcc).
□
Corollary 14.5. Let A be an Ω-involutive weak quasi-Hopf algebra with an antipode
(S, α, β) such that S commutes with ∗. Then
a) every ∗-representation ρ has ρc as a conjugate in Reph(A) with respect to the form
conjugate to that of ρ: (ξ, η) = (η, ξ). Hence Reph
(A) is rigid.
b) If ρ is a C
∗
-representation, so is ρc. Hence if A is a unitary weak quasi-Hopf
algebra, Rep+(A) is rigid as well.
Proof. We may take Kρ = ρ(ω
∗−1
) by Prop. 11.17, hence Fρ = I for all ∗-representations
ρ. □
Remark 14.6. Let A = Nat0(F) be the discrete weak quasi-bialgebra associated to a
semisimple tensor category C endowed a weak quasi-tensor functor F : C → Vec as in
Theorem 7.6. When C is also a C
∗
-category and F factors through a ∗-functor F : C → Hilb
then A has a natural pre-C
∗
-algebra involution. If C is rigid and the dimension assumption
of Prop. 7.6 (d) hold (e.g. C is a fusion category) then A has an antipode (S, α, β). We
note that S may always be chosen commuting with ∗. Indeed, following the proof of
Theorem 7.6 (d), for each ρ, F(ρ)
∗
identifies naturally with the conjugate vector space
F(ρ), which we endow with the unique Hilbert space structure making the conjugation
map J : F(ρ) → F(ρ) antiunitary. It also follows that a transposed linear map L
t
identifies
with JL∗J
−1
. On the other hand, we may choose the natural transformation U unitary.
It follows from the antipode formula given in the proof that S(η
∗
) = S(η)
∗
. For example
if C = Rep(A) with A a discrete weak quasi-Hopf algebra which is also a pre-C
∗
-algebra
then the procedure reconstructs the original antipode of A when this commutes with ∗ by
Remark 7.7 c), but it gives a new one otherwise.
Example 14.7. We next describe the conjugate equations in Reph(A) (Rep+(A)) under
the assumption that S commutes with ∗. Given a ∗-representation ρ, we may use the
canonical identification of ρ
c with ρc and obtain from Prop. 7.4 the following solution for
the pair ρ, ρc ∈ Reph(A),
rρ = d
∗
ρ = Ω−1Xn
i=1
µiei ⊗ α
∗
ei, rρ = bρ =
Xn
i=1
βei ⊗ µiei (14.2)
with ei a basis of the space of ρ satisfying (ei, ej ) = δi,jµi and µi = ±1. Let us consider
the case of Rep+(A), so µi = 1. Then it follows by a straightforward computation that

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 107
rρ = Ω−1 P
i
ei ⊗ α
∗
ei =
P
i
ei ⊗ (αΩ)
∗
ei, r
∗
ρ
ξ ⊗ η = (βΩη, ξ) and this implies
r
∗
ρ
rρ = dρrρ = Tr(α(αΩ)
∗
), r
∗
ρ
rρ = r
∗
ρ
bρ = Tr((βΩ)
∗β), (14.3)
where αΩ and βΩ are defined in (6.11). When Ω = ∆(I) is trivial then a computation shows
that αΩ = α and βΩ = β. If α, β are in addition unitary then the intrinsic dimensions
coincide with the vector space dimensions. In Sect. 32 we shall discuss examples of Ωinvolutive weak quasi-Hopf algebras A = A(g, q, ℓ) arising from a certain semisimplified
quotient category associated to quantum groups at roots of unity Uq(g). In this case the
antipode is of Kac type but Ω is non-trivial, compatibly with non-integrality of intrinsic
dimensions.
We next construct a natural solution of the conjugate equations for objects of Rep+(A),
with A a unitary discrete weak Hopf algebra not necessarily of Kac type. Our methods
extend those of [190, 49, 176] for the case of discrete or compact quantum groups. We first
establish existence of a Haar element.
Proposition 14.8. Let A be a discrete Ω-involutive weak quasi-bialgebra. There is a
unique nonzero selfadjoint idempotent h ∈ A such that ah = ha = ε(a)h for all a ∈ A.
Proof. The proof is as in Prop. 3.1 in [176]. The counit is an irreducible ∗-representation
of A. As such, it coincides with the projection onto one of its one dimensional matrix
subalgebras. The idempotent defining this component is the desired element h. □
Definition 14.9. The element h is called the Haar element.
The following lemma extends a known idea in the framework of coassociative quantum
groups which, to our knowledge, dates back to [190]. Here we consider a modification due
to non-triviality of the associator, where the need of the special form that the associator
takes for weak Hopf algebras is apparent. We are not aware of validity of an analogous
lemma in a general quasi-coassociative framework.
Lemma 14.10. Let A be a discrete weak Hopf algebra. Then
∆(I)A ⊗ A = ∆(A)I ⊗ A, A ⊗ A∆(I) = A ⊗ I∆(A).
Proof. We write ∆(I) = a⊗b and for a generic x ∈ A, ∆(x) = x1 ⊗x2. Consider the linear
map T : A ⊗ A → A ⊗ A defined by T(x ⊗ y) = xy1 ⊗ y2. We show that T is surjective,
and this gives the second stated relation. It is straightforward to see that T coincides with
the map T˜ : A ⊗ A → A ⊗ A defined by T˜(x ⊗ y) = xS(a1)a2y1 ⊗ by2. Consider also the
map R given by R(x ⊗ y) = xS(y1) ⊗ y2. We have
T R(x ⊗ y) = T(xS(y1) ⊗ y2) = T˜(xS(y1) ⊗ y2) = xS(a1y1)a2y2,1 ⊗ by2,2.
We use the associativity relation a1y1 ⊗ a2y2,1 ⊗ by2,2 = y1,1a ⊗ y1,2b1 ⊗ y2b2 and get after
a brief computation T(xS(y1) ⊗ y2) = [x ⊗ y][S(a)b1 ⊗ b2]. A slight modification of this
idea gives T(xS(y1) ⊗ y2b
′
) = T˜(xS(y1) ⊗ y2b
′
) = [x ⊗ y][S(a)b1b
′
1 ⊗ yb2b
′
2
]. We replace x
by ˜x = xS(a
′
2
) and y by ˜y = yS(a
′
1
) and obtain T R(˜x ⊗ y˜) = [x ⊗ y]f, where the element
f was defined in Prop. 6.13 for general weak quasi-Hopf algebras and considered again
in Prop. 10.8 for weak Hopf algebras. Since f is partially invertible with domain ∆(I),

108 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
the proof is complete. The first relation can be proved in a similar way with the maps
T
′
(x ⊗ y) = x1 ⊗ x2y as R′(x ⊗ y) = x1 ⊗ S(x2)y.
□
The following relations extend Prop. 4.1 of [176] to our setting.
Proposition 14.11. Let A be a discrete weak Hopf algebra. For all x, y ∈ A we have
∆(h)x ⊗ y = ∆(h)I ⊗ S(x)y, x ⊗ y∆(h) = xS(y) ⊗ I∆(h).
Proof. We only show the first relation. We write ∆(I)x ⊗ y as a finite sum of elements of
the form ∆(p)I ⊗ q, thanks to the first relation of Lemma 14.10. Evaluating m ◦ S ⊗ 1 on
this element gives S(x)y = ε(p)q. On the other hand
∆(h)x ⊗ y = ∆(hp)I ⊗ q = ∆(hε(p))I ⊗ q = ∆(h)I ⊗ ε(p)q = ∆(h)I ⊗ S(x)y,
and the relation follows. □
The following result gives a canonical implementing element for the squared antipode.
We omit the proof as it equals that of Prop. 4.3 in [176]. For every full matrix subalgebra
Mr(C) we let er denote its identity, regarded as a central projection of A, Trr the trace
map which takes value 1 on the minimal idempotents, and r
′
the unique index such that
S(Mr(C)) = Mr
′(C), which is the same as S(Mr′(C)) = Mr(C).
Proposition 14.12. Let A be a discrete weak Hopf algebra. Then
S
2
(x) = KxK−1
for all x ∈ A, where K = (Kr) ∈ M(A) is given by Kr = [Trr
′ ⊗ 1(∆(h))]−1 ∈ Mr(C).
Theorem 14.13. Let A be an unitary discrete weak Hopf algebra. Then for every C
∗
-
representation ρ, the invertible operator Fρ := ρ(Kω∗) is positive. Therefore ρc becomes a
conjugate of ρ in Rep+(A) with inner product (ξ, η) = (η, Fρξ).
Proof. It suffices to show positivity of Fρ for the C
∗
-representations ρr which project onto
the matrix algebras Mr(C), since any other ρ is unitarily equivalent to a direct sum of
them. We note that ∆(h)Ω−1is positive in M(A ⊗ A), as
∆(h)Ω−1 = ∆(h)
2Ω−1 = ∆(h)Ω−1∆(h)∗
.
Hence ∆(h)Ω−1er
′ ⊗er is positive as well. Using the notation Ω−1 = x⊗y, we have, thanks
to Prop. 14.11,
∆(h)Ω−1er
′ ⊗ er = ∆(h)I ⊗ S(xer′)yer = ∆(h)I ⊗ S(x)yer = ∆(h)I ⊗ ωr,
with ωr the component of ω along Mr(C). Evaluating the positive map Trr
′ ⊗ 1 on this
element we see that K−1
r ωr = ρr(K−1ω) is positive. Hence ρr(Kω∗
) = ωrρr(K−1ω)
−1ω∗
r
is
positive as well. □

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 109
