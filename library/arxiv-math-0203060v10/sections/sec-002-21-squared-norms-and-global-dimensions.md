---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-002-21-squared-norms-and-global-dimensions
section_title: "Squared norms and global dimensions"
section_number: 2.1
pages: 4-5
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
the global dimension of a fusion category. First of all, we have the fo llowing known
result (see e.g., [O]).
Proposition 2.1. In a fusion category, any simple object V is isomorphic to its
double dual V ∗∗.
To prove this, it suﬃces to note that for any simple object V , the right dual V ∗
is the unique simple object X for which V ⊗X contains the neutral object, while
the left dual ∗V is the unique simple object X for which V ⊗X projects to the
neutral object; so ∗V =V ∗ by semisimplicity of the category, and hence V =V ∗∗
for any simple V .
Next, recall ([BaKi], p.39) that if V ∈ C , and g :V →V ∗∗ is a morphism, then
one can deﬁne its “quantum trace” Tr V (g) ∈k by the formula
TrV (g) = evV ∗ ◦ (g ⊗ 1V ∗ ) ◦ coevV,
where 1 is the unit object of C, coevV : 1 →V ⊗V ∗ and evV :V ∗ ⊗V → 1 are the
coevaluation and evaluation maps (see [BaKi]). It is easy to show (an d well known,
see e.g. [BaKi]) that for any simple object V and a nonzero morphism a :V →V ∗∗
one has Tr V (a) ⁄= 0. Indeed, otherwise there is a sequence of nonzero maps 1 →
V ⊗V ∗ → 1 with zero composition, which would imply that the multiplicity of 1
inV ⊗V ∗ is at least 2 – a contradiction.
Now, following [Mu1], for every simple object V of a fusion category C, deﬁne
the squared norm |V |2 ∈ k× of V as follows. Fix an isomorphism a : V → V ∗∗
(which exists by Proposition 2.1), and let |V |2 = TrV (a)TrV ∗ ((a−1)∗). It is clearly
independent on the choice of a (since a is uniquely determined up to a scaling),
and nonzero by the explanation in the previous paragraph. For exa mple, for the
neutral object 1 we have |1|2 = 1.
Deﬁnition 2.2. [Mu1] The global dimension of a fusion category C is the sum of
squared norms of its simple objects. It is denoted by dim( C).
One of our main results is
Theorem 2.3. If k = C then |V |2 > 0 for all simple objects V ∈ C ; therefore
dim(C) ≥ 1, and is > 1 for any nontrivial C. In particular, for any fusion category
C one has dim(C) ⁄= 0.
Remark 2.4. Note that the second statement immediately follows from the ﬁrst
one, since C is always deﬁned over a ﬁnitely generated subﬁeld k′ of k, which can
be embedded into C.
The proof of Theorem 2.3, which relies on Theorem 2.6 below, is given in S ec-
tion 3. Theorem 2.6 is proved in Section 4.
Remark 2.5. In the course of proof of Theorem 2.3 we show that for any simple
object V , the number |V |2 is an eigenvalue of an integer matrix. In particular, if
k = C then |V |2 is an algebraic integer. Thus, for k = C Theorem 2.3 actually
ON FUSION CATEGORIES 5
implies that |V |2 is a “totally positive” algebraic integer, i.e. all its conjugates are
real and positive (since one can twist a fusion category by an autom orphism of
C and get a new fusion category). Similarly, dim( C) is “totally” ≥ 1, i.e. all its
conjugates are ≥ 1.
One of the main tools in the proof of Theorem 2.3 is
Theorem 2.6. In any fusion category, the identity functor is isomorphic t o the
functor **** as a tensor functor.
For the category of representations of a Hopf algebra, this resu lt follows from
Radford’s formula for S4 [R1]. In general, it follows from the analog of Radford’s
formula for weak Hopf algebras, which was proved by the second au thor in [N] (see
Section 4).
Deﬁnition 2.7. A pivotal structure on a fusion category C is an isomorphism of
tensor functors i : Id → ∗∗ . A fusion category equipped with a pivotal structure is
said to be a pivotal fusion category.
We conjecture a stronger form of Theorem 2.6:
Conjecture 2.8. Any fusion category admits a pivotal structure.
For example, this is true for the representation category of a sem isimple Hopf
algebra overk, since in this case by the Larson-Radford theorem [LR2], the squa red
antipode is 1 and hence Id = ∗∗. Furthermore, in Section 8 we will show that
the conjecture is true for the representation category of a sem isimple quasi-Hopf
algebra.
