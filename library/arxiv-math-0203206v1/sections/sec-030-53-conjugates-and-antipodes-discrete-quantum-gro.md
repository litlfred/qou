---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-030-53-conjugates-and-antipodes-discrete-quantum-gro
section_title: "Conjugates and Antipodes: Discrete Quantum Groups"
section_number: 5.3
pages: 32-36
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
We have already seen that the concrete semisimple tensor ∗-categories Repf (A, ∆) and Corep f ( ˆA, ˆ∆) come with
conjugates whenever (A, ∆) is a discrete aqg. In this section we prove the converse. We star t oﬀ with a couple
of preparatory results.
Lemma 5.22 Let C be a semisimple tensor ∗-category with conjugates and let E : C → H be an embedding
functor. Then the coproduct ∆ : A →M (A⊗A) for the discrete quantum semigroup (A, ∆) given by Proposition
5.20 has the following inclusion properties
(1 ⊗A)∆( A) ⊂A ⊗A, (A ⊗ 1)∆( A) ⊂A ⊗A.
Proof. We prove only the inclusion ( A ⊗ 1)∆( A) ⊂ A ⊗A, the proof of the inclusion (1 ⊗A)∆( A) ⊂ A ⊗A
being completely analogous. We need to show that ( a ⊗ 1)∆( b) ∈A ⊗A for all a,b ∈A. It is clearly suﬃcient
to show this for b = (bi) where all components except i =m vanish and for a =In. By the calculation done in
the proof of Lemma 5.18 we have
∆( b)ij =bXi⊗Xj =
∑
k∈IC
N k
ij∑
α=1
E(Vkα
ij ) ◦ bk ◦ E(Vkα∗
ij ) ∈ EndE(Xi ⊗Xj).
In view of a =In and bi = 0 for i ⁄=m we obtain
((a ⊗ 1)∆( b))ij =δi,n
N m
nj∑
α=1
E(Vmα
nj ) ◦ bm ◦ E(Vmα∗
nj ).
Now, since C has conjugates we have isomorphisms Mor(Xn ⊗Xj,Xm) ∼= Mor(Xj,Xn ⊗Xm). By semisimplicity,
for ﬁxed n,m the latter space is non-zero only for ﬁnitely many j ∈IC. Thus (( a ⊗ 1)∆( b))ij is non-zero only
for i =n and ﬁnitely many j and therefore (a ⊗ 1)∆( b) ∈A ⊗A. ■
32
Proposition 5.23 Let C be a semisimple tensor ∗-category with conjugates and let E : C → H be an embedding
functor. Let b = (bX,Y ) ∈ NatE⊗. Using the identiﬁcations B((E(X ⊗Y )) = B(E(X)) ⊗B(E(Y )), for
any objects X and Y in C, we may write bX,X = ∑
kak
X ⊗ bk
X ∈ B(E(X)) ⊗ B(E(X)), and then deﬁne
˜m(b)X ∈B(E(X)) by
˜m(b)X =
∑
k
ak
X ◦ bk
X,
for any object X ∈ C . This gives a unital linear map ˜m : NatE⊗ → NatE which sends b ∈NatE ⊗ to ˜m(b).
Furthermore, it restricts to the linearized multiplicatio n m :A ⊗A →A on A ⊂ NatE.
Proof. The bilinear multiplication map from B(E(X)) ⊗ B(E(X)) to B(E(X)) exists since E(X) is ﬁnite
dimensional. The rest is obvious. ■
Proposition 5.24 Let C be a semisimple tensor ∗-category with conjugates and let E : C → H be an embedding
functor. Then the discrete quantum semigroup (A, ∆) given by Proposition 5.20 is a discrete aqg. The coinverse
S :A →A is given by
S(a)X =E(idX ⊗r∗
X ) ◦ idE(X) ⊗aX ⊗ idE(X) ◦ E(rX ⊗ idX )
for all a ∈ A ⊂ NatE and objects X in C, and where (rX,rX,X) is any solution of the conjugate equations
associated to X.
Proof. In view of Proposition 2.4 it is suﬃcient to show that ( A ⊗ 1)∆( A) ⊂A ⊗A and (1 ⊗A)∆( A) ⊂A ⊗A
and to produce an invertible coinverse S. We thus get an aqg since Theorem 2.13 provides a (non-zero) left-
invariant positive functional for discrete multiplier Hopf ∗-algebras. Now the inclusions ( A ⊗ 1)∆( A) ⊂A ⊗A
and (1 ⊗A)∆( A) ⊂A ⊗A are the content of Lemma 5.22.
We show that the map S : A → A given by the formula in the theorem is well-deﬁned. We ﬁrst show
that for a ∈ A and X ∈ C , the formula for S(a)X ∈ EndE(X) does not depend on the choice of solution
(rX,rX,X) of the conjugate equations associated to X. Suppose therefore that ( r′
X,r′
X,X
′
) is another solution
of the conjugate equations associated to X. By [23] there exists a unique invertible t ∈ Hom(X,X
′
) such that
r′
X =t ⊗ idX ◦ rX and r′
X = idX ⊗t∗−1 ◦ rX . Thus
E(idX ⊗r′∗
X ) ◦ idE(X) ⊗aX
′ ⊗ idE(X) ◦ E(r′
X ⊗ idX )
=E(idX ⊗ (r∗
X ◦ t∗ ⊗ idX )) ◦ idE(X) ⊗aX
′ ⊗ idE(X) ◦ E((idX ⊗t∗−1 ◦ rX ) ⊗ idX )
=E(idX ⊗r∗
X ) ◦ idE(t) ⊗ (E(t∗) ◦ aX
′ ◦ E(t∗−1)) ⊗ idE(X) ◦ E(rX ⊗ idX )
=E(idX ⊗r∗
X ) ◦ idE(X) ⊗ (E(t∗ ◦ t∗−1 ◦ aX ) ⊗ idE(X)) ◦ E(rX ⊗ idX )
=E(idX ⊗r∗
X ) ◦ (idE(X) ⊗aX ⊗ idE(X)) ◦ E(rX ⊗ idX ),
and S(a)X ∈ EndE(X) does not depend on the choice of solution ( rX,rX,X) of the conjugate equations
associated with X.
Next we show that S(a) = (S(a)X ) ∈ NatE fora ∈A, i.e., we must show that E(t) ◦S(a)X =S(a)Y ◦E(t),
for all a ∈A and t ∈ Hom(X,Y ). By the existence of the transpose t•∗ ∈ Hom(Y,X ) given in [23], we get
E(t) ◦ S(a)X = E(idY ⊗r∗
X ) ◦ E(t) ⊗aX ⊗ idE(X) ◦ E(rX ⊗ idX )
= E(idY ⊗r∗
X ) ◦ idE(Y ) ⊗aX ⊗ idE(X) ◦ E((t ⊗ idX ◦ rX ) ⊗ idX )
= E(idY ⊗r∗
X ) ◦ idE(Y ) ⊗aX ⊗ idE(X) ◦ E((idY ⊗t•∗ ◦ rY ) ⊗ idX )
= E(idY ⊗r∗
X ) ◦ idE(Y ) ⊗ (aX ◦E(t•∗)) ⊗ idE(X) ◦ E(rY ⊗ idX )
= E(idY ⊗r∗
X ) ◦ idE(Y ) ⊗ (E(t•∗) ◦aY ) ⊗ idE(X) ◦ E(rY ⊗ idX )
= E(idY ⊗ (r∗
X ◦ t•∗ ⊗ idX )) ◦ idE(Y ) ⊗aY ⊗ idE(X) ◦ E(rY ⊗ idX )
= E(idY ⊗ (r∗
Y ◦ idY ⊗t)) ◦ idE(Y ) ⊗aY ⊗ idE(X) ◦ E(rY ⊗ idX )
= E(idY ⊗r∗
Y ) ◦ idE(Y ) ⊗aY ⊗E(t) ◦ E(rY ⊗ idY )
= S(a)Y ◦ E(t),
33
as desired.
Clearly, we have S(a) ∈A for all a ∈A and it is also clear that the map S is linear. We must prove the two
identities
m(ι ⊗S)((a ⊗ 1)∆( b)) = ε(b)a, m (S ⊗ι)((1 ⊗a)∆( b)) = ε(b)a,
for all a,b ∈ A. We prove only the ﬁrst one. Thus let a,b ∈ A and write ( a ⊗ 1)∆( b) = ∑
kak ⊗bk for some
ak,bk ∈A. This means that
(aX ⊗ 1Y ) ◦ bX⊗Y =
∑
k
ak
X ⊗bk
Y
for all objects X and Y of C. Thus we get
m(ι ⊗S)((a ⊗ 1)∆( b))X =
∑
k
m(ak ⊗S(bk))X =
∑
k
ak
X ◦ S(bk)X
=
∑
k
ak
X ◦ E(idX ⊗r∗
X ) ◦ idX ⊗bk
X ⊗ idE(X) ◦ E(rX ⊗ idX )
=E(idX ⊗r∗
X ) ◦ (
∑
k
ak
X ⊗bk
X ) ⊗ idE(X) ◦ E(rX ⊗ idX )
=E(idX ⊗r∗
X ) ◦ (aX ⊗ idE(X) ◦ bX⊗X ) ⊗ idE(X) ◦ E(rX ⊗ idX )
=aX ◦ E(idX ⊗r∗
X ) ◦ bX⊗X ⊗ idE(X) ◦ E(rX ⊗ idX )
=aX ◦ E(idX ⊗r∗
X ) ◦ E(rX ⊗ idX )b1 = aX ◦ E(idX ⊗r∗
X ◦ rX ⊗ idX )b1
=aX ◦ E(idX )b1 = aXb1 = aXε(b) = ( ε(b)a)X
for all objects X in C, so m(ι ⊗S)((a ⊗ 1)∆( b)) = ε(b)a as natural transformations.
It remains to show that S is invertible. We do that by showing S(S(a)∗) = a∗ for all a ∈ A. Now with
X ∈ C , we calculate
S(S(a)∗)X =E(idX ⊗r∗
X ) ◦ idE(X) ⊗S(a)∗
X ⊗ idE(X) ◦ E(rX ⊗ idX )
=E(idX ⊗r∗
X ) ◦ idE(X) ⊗ [E(idX ⊗r∗
X ) ◦ idE(X) ⊗aX ⊗ idE(X) ◦ E(rX ⊗ idX )]∗ ⊗ idE(X) ◦ E(rX ⊗ idX ),
where we used ( rX,rX,X ) as a solution of the conjugate equations for X ∈ C . Thus
S(S(a)∗)X
= E(idX ⊗r∗
X ) ◦ idE(X) ⊗ [E(r∗
X ⊗ idX ) ◦ idE(X) ⊗a∗
X ⊗ idE(X) ◦ E(idX ⊗rX )] ⊗ idE(X) ◦ E(rX ⊗ idX )
= E(idX ⊗r∗
X ◦ idX ⊗r∗
X ⊗ idX⊗X ) ◦ idE(X⊗X) ⊗a∗
X ⊗ idE(X⊗X) ◦ E(idX⊗X ⊗rX ⊗ idX ◦ rX ⊗ idX )
= E(idX ⊗r∗
X ⊗r∗
X ) ◦ idE(X⊗X) ⊗a∗
X ⊗ idE(X⊗X) ◦ E(rX ⊗rX ⊗ idX )
= E(idX ⊗r∗
X ⊗r∗
X ◦ rX ⊗ idX⊗X⊗X ) ◦ a∗
X ⊗ idE(X⊗X) ◦ E(rX ⊗ idX )
= E((idX ⊗r∗
X ) ◦ (rX ⊗ idX ) ⊗ idX⊗X ◦ idX ⊗r∗
X ) ◦ a∗
X ⊗ idE(X⊗X) ◦ E(rX ⊗ idX )
= E(idX ⊗r∗
X ) ◦ a∗
X ⊗ idE(X⊗X) ◦ E(rX ⊗ idX ) = a∗
X ◦ E(idX ⊗r∗
X ◦ rX ⊗ idX )
= a∗
X ◦ idE(X) = a∗
X = ( a∗)X.
■
After these preparatory computations, the following Main Result is essentially a restatement of Theorem
5.21 and Proposition 5.24.
Theorem 5.25 Let C be a semisimple tensor ∗-category with conjugates and E : C → H an embedding functor.
Let (A, ∆) be the corresponding discrete aqg. Then the functor F : C → Repf (A, ∆) deﬁned by
F (X) = (E(X),πX ), π X (a) = aX ∀a ∈A, F (s) = E(s)
provides an equivalence of tensor ∗-categories such that K ◦ F =E.
34
Remark 5.26 1. In combination with Theorem 3.14 this gives Woronowicz’ generalize d Tannaka-Krein result.
Woronowicz constructs Corep f ( ˆA, ˆ∆) for a compact aqg ( ˆA, ˆ∆) more directly and uses the universal corepre-
sentation U of (A, ∆) implicitly. In his proof Woronowicz constructs a compact matrix ps eudogroup from a
category with a generator. Our result is more general in that this a ssumption is redundant.
2. In view of Theorem 3.20, an alternative reconstruction theorem for a concrete semisimple tensor ∗-category
C with conjugates would be that
C
⊗
∼= Comodf ( ˆA, ˆ∆ op),
where ( ˆA, ˆ∆ op) is a Hopf ∗-algebra with a positive invariant functional. We refer to [34, 15] for similar construc-
tions, where concrete non-semisimple tensor categories are show n to be equivalent to tensor categories of ﬁnite
dimensional comodules over (inﬁnite dimensional) Hopf algebras (with no ∗-operation). ✷
We now discuss how the aqg ( A, ∆) depends on the choice of the embedding functor E. This discussion is
only preliminary and will be taken up again in part II of this series. We ne ed the following
Definition 5.27 Let C, D be strict tensor categories and E,E ′ : C → D be tensor functors (with structural
isomorphisms e,e ′,dX,Y,d ′
X,Y ). Then E,E ′ are said to be isomorphic as tensor functors, E
⊗
∼= E′, if the
diagram
E(X) ⊗E(Y ) uX ⊗uY✲ E′(X) ⊗E′(Y )
E(X ⊗Y )
dX,Y
❄
uX⊗Y
✲ E′(X ⊗Y )
d′
X,Y
❄
(5.1)
commutes for all X,Y ∈ C , where u : E → E′ is a natural transformation whose components uX : E(X) →
E′(X) are isomorphisms. A similar and obvious commutative diagra m involves the structural isomorphisms
e,e ′. If C, D are tensor ∗-categories and E,E ′ are ∗-preserving then all uX must be unitary.
Proposition 5.28 Let C be a semisimple tensor ∗-category C with conjugates. Let E,E ′ : C → H be embedding
functors, and let (A, ∆) , (A′, ∆ ′) be the corresponding discrete aqg. An isomorphism u :E
⊗
∼=E′ gives rise to an
isomorphism θ : (A, ∆) ∼= (A′, ∆ ′) with π′
Xθ =πX for all X ∈ C .
Proof. Let u : E → E′ be a unitary equivalence of tensor ∗-functors. Then θ : NatE → NatE′ given by
θ(a)X = uXaXu∗
X for a ∈ NatE and X ∈ C restricts to a unital ∗-homomorphism from A to A′. Suppressing
as usual the natural transformations d and d′, we clearly have ∆ ′(θ(a))(X,Y ) = uX⊗YaX⊗Yu∗
X⊗Y , whereas
(θ ⊗θ)∆( a)(X,Y ) = (uX ⊗uY )aX⊗Y (u∗
X ⊗u∗
Y ), for all a ∈ NatE andX,Y ∈ C . Since uX⊗Y =uX ⊗uY , for all
X,Y ∈ C , we get ( θ ⊗θ)∆ = ∆ ′θ, and (A, ∆) ∼= (A′, ∆ ′). ■
The following deﬁnition will be useful in our discussion of embedded sym metric tensor categories.
Definition 5.29 Let C, D be tensor categories and E : C → D a tensor functor. Then the automorphism group
Aut⊗E consists of the natural isomorphisms of E for which the diagram (5.1) commutes (with E′ =E), together
with the obvious componentwise group structure. If C is a tensor ∗-category and E is a ∗-preserving embedding
functor then the intrinsic group GE is the subgroup of Aut⊗E where all uX are unitaries.
35
