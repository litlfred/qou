---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-031-54-the-non--case
section_title: "The Non- ∗ Case"
section_number: 5.4
pages: 36-37
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
Our starting point in this paper is a tensor ∗-category with direct sums, subobjects, conjugates and irredu cible
unit. From it we (re)construct a multiplier Hopf ∗-algebra with positive left invariant functional. Such algebras
were called algebraic quantum groups (aqg) by Van Daele, who now pr efers to speak of ‘multiplier Hopf ∗-
algebras with integrals’. We stick to ‘algebraic quantum groups’ mainly for the sake of deﬁniteness and brevity.
When A is no longer a ∗-algebra and the invariant functional is required to be faithful rat her than positive
(ϕ(ab) = 0 for all a ∈ A implies b = 0) we arrive at the notion of a regular multiplier Hopf algebras with
left invariant functional. Essentially the entire theory works just a s well in this setting, provided one adopts
a modiﬁed notion of dual. We say a tensor category is rigid if every obj ect X comes with a chosen left dual
X and morphisms eX : X ⊗X → 1 and dX : 1 → X ⊗X satisfying the triangular equations instead of the
conjugate equations. In a semisimple category, left duals are auto matically two-sided duals since dual morphisms
e′
X : 1 → X ⊗X and d′
X : X ⊗X → 1 exist. Adopting the standard deﬁnition of semisimple categories as
abelian categories with all exact sequences splitting, one can prove the following:
Theorem 5.30 Let F be an algebraically closed ﬁeld (of arbitrary characterist ic). Let C be a F-linear semisimple
rigid tensor category with End 1 ∼= F and let E : C → VectF be a faithful tensor functor. Then there is
a discrete regular multiplier Hopf algebra (A, ∆) with faithful left invariant functional ϕ and an equivalence
F : C → Rep(A, ∆) such that K ◦F =E.
The proof proceeds exactly as for ∗-categories, ignoring all references to the ∗-preserving property of E and
the ∗-involution of A. Again, existence, uniqueness and faithfulness of the invariant fu nctional are proven using
results due to Van Daele. Only the construction of the coinverse re quires careful examination since the notion
of dual is diﬀerent.
We close with some remarks on the two diﬀerent notions of discreten ess applying to multiplier Hopf algebras.
In analogy to the ∗-case, a regular multiplier Hopf algebra ( A, ∆) with left invariant functional is called discrete
if A is a direct sum of ﬁnite dimensional matrix algebras over F. In the non- ∗ case Proposition 2.14 fails, and
(A, ∆) is said to be of discrete type iﬀ there exists 0 ⁄= h ∈ A such that ah = ε(a)h for all a ∈ A. As in the
∗-case, (A, ∆) is of compact type or, equivalently, compact if A has a unit. It is well known [37] that ( A, ∆) is
of discrete type iﬀ ( ˆA, ˆ∆) is of compact type.
Every discrete multiplier Hopf algebra has a copy of F as a direct summand, corresponding to the one-
dimensional representation ε. The unit I0 of this algebra has the property aI0 =I0a =ε(a)I0, thus a discrete
multiplier Hopf algebra is of discrete type. The following characterize s discrete multiplier Hopf algebras, gen-
eralizing a well known result for ﬁnite dimensional Hopf algebras (whic h automatically possess integrals).
Proposition 5.31 Let (A, ∆) and ( ˆA, ˆ∆) be mutually dual regular multiplier Hopf algebras with fait hful left
invariant functionals. Then the following are equivalent:
1. (A, ∆) is discrete.
2. (A, ∆) is of discrete type and h can be chosen to be idempotent.
3. ( ˆA, ˆ∆) is of compact type and ˆϕ(1) ⁄= 0.
Proof. The implication 1. ⇒2. has been discussed before. Assuming 2., we have h =hh =ε(h)h, thus ε(h) = 1.
Conversely, ifε(h) ⁄= 0 then h/ε(h) satisﬁes 2. Now, 2. implies that ( ˆA, ˆ∆) is compact, and compactness implies
the existence of 0 ⁄=h ∈A satisfying xh =ε(x)h for all x ∈A. By deﬁnition of the dual ( ˆA, ˆ∆) and assuming
the normalization ϕ(h) = 1, we have ˆϕ(1) = ε(h), yielding the equivalence 2. ⇔3. Now assume 3. holds. Then
( ˆA, ˆ∆) is a Hopf algebra with left invariant functional ˆ ϕ satisfying ˆϕ(1) ⁄= 0. By classical results, cf., e.g., [32,
14.0.3] or [1, Theorem 3.3.2], it follows that ( ˆA, ˆ∆) is cosemisimple. This means that the F-coalgebra ( ˆA, ˆ∆ , ˆε)
is a direct sum of ﬁnite dimensional coalgebras. Since F is algebraically closed, every ﬁnite dimensional F-
coalgebra is a matrix coalgebra, i.e. it has a basis {aij, 1 ≤ i,j ≤ n} such that ∆( aij) = ∑
lail ⊗alj . Since
36
A = { ˆϕ(·a), a ∈ ˆA} ⊂ ˆA∗ and ˆϕ is faithful, A has a basis {bα
ij = ˆϕ(·aα
ij), α ∈ I, 1 ≤ i,j ≤ nα ∈ N}. These
elements multiply according to bα
ijbα′
i′j′ =δαα′δji′bα
ij′ , thus
A =
⨁
α∈I
Mnα (F),
as desired. ■
Remark 5.32 1. In the ∗-case, ˆϕ is positive and 1 > 0, thus discrete type implies discreteness.
2. We indicate how Proposition 5.31 can be used to prove Theorem 5.30 . Given a semisimple tensor category
C with embedding functor E, by [34] there exists a Hopf algebra H such that C ≃ ComodH. By [32, 14.0.3],
semisimplicity of C implies the existence of a left invariant functional ˆϕ onH, satisfying ˆϕ(1) ⁄= 0. Thus ( H, ˆ∆)
is a compact multiplier Hopf algebra with left invariant functional. Its d ual (A, ∆) then is a discrete multiplier
Hopf algebra with left invariant functional, and by Theorem 3.14 we ha ve C ≃ Repf (A, ∆). However, the direct
proof of Theorem 5.30 analogous to the proof of Theorem 5.25 is mor e direct and instructive. ✷
