---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-014-14-the-coend-of-the-center
section_title: "The coend of the center"
section_number: 14
pages: 59-64
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
The aim of this section is to compute the coend of the center of a fus ion category.
This computation will be instrumental in the proof of Lemma 11.3 given in the next
section. It is based on the theory of Hopf monads, which was introd uced precisely
to this end in [BV1, BV2]. We brieﬂy recall this theory and state the r elevant
results of [BV1, BV2].
14.1. Coends. LetC andD be categories. A dinatural transformation from a
functor F :Cop×C→D to an object D ofD is a family
d ={dX : F (X,X )→D}X∈Ob(C)
60 V. TURAEV AND A. VIRELIZIER
of morphisms in D such that dXF (f, idX ) = dYF (idY,f ) for every morphism
f : X → Y inC. The composition of such a d with a morphism ϕ : D→ D′ in
D is the dinatural transformation ϕ◦d ={ϕ◦dX : F (X,X )→ D′}X∈Ob(C) from
F to D′. A coend of F is a pair ( C,ρ ) consisting in an object C ofD and a dinat-
ural transformation ρ from F to C satisfying the following universality condition:
every dinatural transformation d from F to an object of D is the composition of
ρ with a morphism in D and the latter morphism is uniquely determined by d. If
F has a coend ( C,ρ ), then it is unique (up to unique isomorphism). One writes
C =
∫ X∈C
F (X,X ). For more on coends, see [Mac].
For a left rigid category C (that is, a monoidal category such that every object
X ofC has a left dual ∨X), the formula ( X,Y ) ↦→∨X⊗ Y deﬁnes a functor
Cop×C→C . The coend of this functor (if it exists) is called the coend ofC.
Consider in more detail the case where C is a fusion category over a commutative
ring k. Let I be a (ﬁnite) representative set of simple objects of C. If D is a
k-category which admits ﬁnite direct sums, then any k-linear functor F :Cop×C→
D has a coend ( C,ρ ). Here C =⊕i∈IF (i,i ) and ρ ={ρX : F (X,X )→C}X∈Ob(C)
is computed by ρX =∑
αF (qα
X,p α
X ), where (pα
X,q α
X )α is any I-partition of X. An
arbitrary dinatural transformation d fromF to an object D ofD is the composition
of ρ with∑
i∈Idi : C→D. In particular, C has a coend ⨁
i∈Ii∗⊗i.
14.2. Centralizable functors. LetC be a left rigid category. A functor T :C→C
is centralizable if for every object X ofC, the functor Cop×C→C carrying any
pair (Y1,Y 2) to ∨T (Y1)⊗X⊗Y2 has a coend
ZT (X) =
∫ Y ∈C
∨T (Y )⊗X⊗Y.
The correspondence X ↦→ZT (X) extends to a functor ZT :C → C, called the
centralizer of T , so that the associated universal dinatural transformation
(19) ρX,Y : ∨T (Y )⊗X⊗Y →ZT (X)
is natural in X and dinatural in Y .
For example, ifC is a fusion category over k, then any k-linear functor T :C→C
is centralizable, and its centralizer ZT :C→C is given by
(20) ZT (X) =
⨁
i∈I
T (i)∗⊗X⊗i
for all X ∈ Ob(C), where I is a representative set of simple objects of C. The
associated universal dinatural transformation is
ρX,Y =
∑
β
T (qβ
Y )∗⊗ idX⊗pβ
Y :T (Y )∗⊗X⊗Y →ZT (X),
where (pβ
Y,q β
Y )β is any I-partition of Y .
14.3. Hopf monads. The Hopf monads generalize Hopf algebras to an abstract
categorical setting. We recall the basic deﬁnitions of the theory o f Hopf monads
referring to [BV1] for a detailed treatment.
Any categoryC gives rise to a category End (C) whose objects are functors C→C
and whose morphisms are natural transformations of such funct ors. The category
End (C) is a (strict) monoidal category with tensor product being compos ition of
functors and unit object being the identity functor 1 C :C→C . A monad onC is
an algebra in the category End ( C), that is, a triple ( T,µ,η ) consisting of a functor
T :C→C and two natural transformations
µ ={µX : T 2(X)→T (X)}X∈Ob(C) and η ={ηX : X→T (X)}X∈Ob(C)
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 61
called the product and the unit of T , such that for all X∈ Ob(C),
µXT (µX ) = µXµT (X) and µXηT (X) = id T (X) =µXT (ηX ).
For example, the identity functor 1 C :C →C is a monad on C (with identity as
product and unit), called the trivial monad .
Given a monad T onC, a T - module inC is a pair ( M,r ) where M∈ Ob(C) and
r : T (M )→ M is a morphism in C such that rT (r) = rµM and rηM = id M . A
morphism from a T - module (M,r ) to a T - module (N,s ) is a morphism f : M→N
inC such that fr =sT (f ). This deﬁnes the categoryT -C of T -modules inC, with
composition induced by that in C. We denote by UT the forgetful functor T -C→C ,
deﬁned by UT (M,r ) = M and UT (f ) = f . Note that 1 C-C =C.
To deﬁne Hopf monads, we recall the notion of a comonoidal functo r. A functor
F : C → D between monoidal categories is comonoidal if it is endowed with a
morphism F0 : F (1)→ 1 and a natural transformation
F2 ={F2(X,Y ) :F (X⊗Y )→F (X)⊗F (Y )}X,Y ∈Ob(C)
which are coassociative and counitary, i.e., for all X,Y,Z ∈ Ob(C),
(idF (X)⊗F2(Y,Z ))F2(X,Y ⊗Z) = (F2(X,Y )⊗ idF (Z))F2(X⊗Y,Z )
and
(idF (X)⊗F0)F2(X, 1) = id F (X) = (F0⊗ idF (X))F2(1,X ).
A natural transformation ϕ ={ϕX : F (X)→ G(X)}X∈Ob(C) between comonoidal
functors is comonoidal if G0ϕ1 =F0 and, for all X,Y ∈ Ob(C),
G2(X,Y )ϕX⊗Y = (ϕX⊗ϕY )F2(X,Y ).
LetC be a monoidal category. A bimonad onC is a monad ( T,µ,η ) on C such
that the underlying functor T :C→C and the natural transformations µ andη are
comonoidal. For a bimonad T onC, the category of T - modulesT -C has a monoidal
structure with unit object ( 1,T 0) and monoidal product
(M,r )⊗ (N,s ) =
(
M⊗N, (r⊗s)T2(M,N )
)
.
Note that the forgetful functor UT : T -C→C is strict monoidal.
By a rigid category we mean a monoidal category C such that every object X
ofC has a left dual ∨X and a right dual X ∨. Every morphism f : X→Y in a rigid
category gives rise to two dual morphisms ∨f : ∨Y → ∨X and f ∨ : Y ∨→ X ∨. A
bimonad T on a rigid category C is a Hopf monad if its category of modules T -C
is rigid. This condition can be reformulated in terms of morphisms
sl ={sl
X : T (∨T (X))→ ∨X}X∈Ob(C) and sr ={sr
X :T (T (X)∨)→X ∨}X∈Ob(C)
encoding the left and right duals of any T - module (M,r ) via the formulas
∨(M,r ) = ( ∨M,s l
MT (∨r)) and ( M,r )∨ = (M ∨,s r
MT (r∨)).
The morphisms sl and sr are called the left and right antipodes , respectively. For
example, the trivial monad on C is a Hopf monad (with identity morphisms for
comonoidal structure and antipodes), called the trivial Hopf monad .
14.4. Distributive laws. Let (P,m,u ) and (T,µ,η ) be monads on a category C.
Following Beck [Be], a distributive law of T over P is a natural transformation
Ω = {Ω X : TP (X)→PT (X)}X∈Ob(C) satisfying appropriate axioms which ensure
that the functor PT :C→C is a monad on C with product p and unit e given by
pX =mT (X)P 2(µX )P (Ω T (X)) and eX =uT (X)ηX for any X∈ Ob(C).
The monad (PT,p,e ) is denoted by P◦Ω T . A distributive law Ω of T overP also
deﬁnes a lift of P to a monad ( ˜P, ˜m, ˜u) on the category T -C by
˜P (M,r ) =
(
P (M ),P (r)Ω M
)
, ˜m(M,r) =mM, ˜u(M,r) =uM,
62 V. TURAEV AND A. VIRELIZIER
and the categories ˜P - (T -C) and (P◦Ω T )-C are isomorphic.
IfC is rigid, P and T are Hopf monads, and Ω is comonoidal, then P◦Ω T is
a Hopf monad on C, ˜P is a Hopf monad on T -C, and ˜P - (T -C)≃ (P◦Ω T )-C as
monoidal categories (see [BV2, Corollary 4.11]).
14.5. Centralizer and double of a Hopf monad. LetC be a rigid category.
We state here some results of [BV2] concerning the centralizer an d the double of a
Hopf monad on C. As an application, we shall compute (under certain additional
assumptions onC) the coend of the center Z(C) ofC.
LetT :C→C be a centralizable Hopf monad on C. Then its centralizer ZT :C→
C has a natural structure of a Hopf monad on C, see [BV2, Theorems 5.6]. Consider
the universal dinatural transformation ρ associated with ZT , see (19). Since T is a
Hopf monad on C, for any X∈ Ob(C), the dinatural transformation
{T (ρX,Y ) :T
( ∨T (Y )⊗X⊗Y
)
→TZ T (X)}Y ∈Ob(C)
is universal. Therefore there exists a unique morphism Ω T
X : TZ T (X)→ ZTT (X)
such that, for any Y ∈ Ob(C),
(21) Ω T
XT (ρX,Y ) = ρT (X),T (Y )
( ∨µYsl
T (Y )T (∨µY )⊗T2(X,Y )
)
T2(∨T (Y ),X⊗Y ),
whereµ andsl are the product and the left antipode of T . By [BV2, Theorem 6.1],
Ω T ={Ω T
X : TZ T (X)→ZTT (X)}X∈Ob(C) is an invertible comonoidal distributive
law, called the canonical distributive law of T over ZT . By Section 14.4, this has
two consequences.
Firstly,DT = ZT◦Ω T T is a Hopf monad on C and the rigid categories DT -C
andZ(T -C) are isomorphic, see [BV2, Theorem 6.5]. An explicit isomorphism
Φ T : DT -C→Z (T -C) carries any morphism in DT -C to itself viewed as a morphism
inZ(T -C) and carries any ( M,r )∈ Ob(DT -C) to
(
(M,ru T (M)),σ
)
∈ Ob(Z(T -C))
with
σ(N,s) = (s⊗rρT (M),N )(coevT (N )⊗ηM⊗ idN ) :M⊗N→N⊗M,
where η and u are the units of T and ZT respectively. The Hopf monad DT is
called the double of T . Though we shall not use it, it is important to note that
DT is quasitriangular in an appropriate sense and Φ T : DT -C → Z(T -C) is an
isomorphism of braided categories.
Secondly, Ω T determines a lift of ZT to a Hopf monad ˜ZT on T -C, which turns
out to be the centralizer of the identity functor of T -C, see [BV2, Theorem 6.9]. By
the deﬁnition of a centralizer, ˜ZT (1,T 0) =
(
ZT (1),Z T (T0)Ω T
1
)
is the coend of T -C.
Now letC be a rigid category such that the trivial Hopf monad 1 C is centralizable.
Clearly, the centralizer Z = Z1C of 1 C coincides with the double of 1 C. Applying
the results above to T = 1 C, we obtain that Z is a quasitriangular Hopf monad
and Φ = Φ 1C : Z-C → Z(C) is an isomorphism of braided categories. Assume
furthermore that Z is centralizable. Applying the results above to T = Z, we
obtain a morphism Ω = Ω Z
1 : ZZ Z(1)→ ZZZ(1). Then
(
ZZ (1),Z Z(Z0)Ω
)
is the
coend of Z-C. So,
(C,σ ) = Φ
(
ZZ (1),Z Z(Z0)Ω
)
∈ Ob(Z(C))
is the coend of Z(C). We have C =ZZ(1) and, for any X∈ Ob(C),
(22) σX = (id X⊗ZZ(Z0)Ω̺C,X )(coevX⊗ idC⊗X ) :C⊗X→X⊗C,
where ̺X,Y : ∨Y ⊗X⊗Y → Z(X) is the universal dinatural transformation for
Z(X) =
∫ Y ∈C ∨Y⊗X⊗Y .
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 63
14.6. The case of fusion categories. We apply the computations of the previous
subsections to a fusion categoryC over k. Fix a representative set I of simple objects
ofC. For X∈ Ob(C), denote by ( pα
X : X→ iα,q α
X : iα→ X)α∈Λ X an I-partition
of X. For i∈ I, let Λ i
X be the subset of Λ X consisting of all α∈ Λ X such that
iα =i.
By the results above, the trivial Hopf monad 1 C, being k-linear, is centralizable
and its centralizer Z :C→C is the Hopf monad given by Formula (20) for T = 1 C,
that is, Z(X) =⨁
i∈Ii∗⊗X⊗i. The structural morphisms of Z can be computed
as follows, see [BV2]. Let ψ be the pivotal structure of C (see Remark 1.5). Then
for any X,Y ∈ Ob(C),
Z2(X,Y ) =
∑
i∈I
PSfrag replacements
i i
i
X Y
: Z(X⊗Y )→Z(X)⊗Z(Y ),
Z0 =
∑
i∈I
PSfrag replacements
i
X
Y i :Z(1)→ 1,
µX =
∑
i,j,k∈I
α∈Λ k
i⊗j
PSfrag replacements
i
X
Y
i
i ij j
kk X
(qα
i⊗j )∗ pα
i⊗j : Z 2(X)→Z(X),
ηX = id X :X→X = 1∗⊗X⊗ 1֒→Z(X),
sl
X =sr
X =
∑
i,j∈I
α∈Λ i
j∗
PSfrag replacements
i
X
Y
i
i
j
k
X
(qα
i⊗j )∗
pα
i⊗j
i i∗∗ jj
X qα
j∗ψ−1
ipα
j∗
: Z(Z(X)∗)→X ∗.
Being k-linear, the Hopf monad Z is centralizable and its centralizer ZZ :C→C
is given by Formula (20) for T =Z, that is,
ZZ (X) =
⨁
j∈I
Z(j)∗⊗X⊗j≃
⨁
i,j∈I
i∗⊗j∗⊗i⊗X⊗j,
with universal dinatural transformation
ρX,Y =
∑
i,j∈I, α∈Λ j
Y
idi∗⊗ (qα
Y )∗⊗ψ−1
i ⊗ idX⊗pα
Y : (Z(Y ))∗⊗X⊗Y →ZZ(X).
By Section 14.5, Z(C) admits a coend ( C,σ ), where
(23) C =ZZ(1) =
⨁
i,j∈I
i∗⊗j∗⊗i⊗j,
andσ ={σX : C⊗X→X⊗C}X∈Ob(C) is given by (22). Using (21) and the above
description of the structural morphisms of Z, we obtain that, for any X∈ Ob(C),
σX =
∑
i,j,k,l,z∈I
α∈Λ i
z⊗k⊗z∗
β∈Λ l
z∗⊗j⊗z
γ∈Λ z
X
PSfrag replacements
ii jj
k kl l
z z
z z
z
X
X
pβ
z∗⊗j⊗z
qβ
z∗⊗j⊗z
qα
z⊗k⊗z∗
pα
z⊗k⊗z∗
pγ
X
qγ
X
.
Using the fact that for any X,Y ∈ Ob(C), the family of pairs
64 V. TURAEV AND A. VIRELIZIER


PSfrag replacements
k l
YX
qα
X ∗⊗l⊗Y ∗
pα
X ∗⊗l⊗Y ∗
, dim(l)
PSfrag replacements
k
l
YX
qα
X ∗⊗l⊗Y ∗
pα
X ∗⊗l⊗Y ∗


l∈I,α∈Λ 1
X∗ ⊗l⊗Y ∗
is an I-partition of X⊗Y , the half braiding σ can be rewritten as
σX =
∑
i,j,k,l,z∈I
α∈Λ 1
z⊗k∗⊗z∗⊗i
β∈Λ 1
z∗⊗j∗ ⊗z⊗l
γ∈Λ z
X
dim(i) dim(l)
PSfrag replacements
i i jj
k k l l
z
z z
z
z
X
X
qβ
z∗⊗j∗⊗z⊗lpβ
z∗⊗j∗⊗z⊗l
pα
z⊗k∗⊗z∗⊗iqα
z⊗k∗⊗z∗⊗i
pγ
X
qγ
X
.
The latter formula simpliﬁes for X∈ I. In this case (id X, idX ) is an I-partition
of X, so the top-left and bottom-right boxes may be deleted from the p icture and
the summation over z is unnecessary: only z =X may contribute a non-zero term.
