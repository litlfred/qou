---
doc_id: arxiv-1002.0168v2
doc_title: "Non-cyclotomic fusion categories Scott Morrison Noah Snyder"
section_id: sec-006-4-rational-forms-and-twisted-moments
section_title: "Rational forms and twisted moments"
section_number: 4
pages: 14-20
source_pdf: 1002.0168v2.pdf
source_sha256: c95d5d193d57b097
doc_brief: "Non-cyclotomic fusion categories Scott Morrison Noah Snyder — Etingof, Nikshych and Ostrik ask in [ 7,§2] if every fusion category can be completely deﬁned over a cyclotomic ﬁeld."
---
The goal of this section is to prove the “only if” direction of Thereom 1.2 parts 2
and 3 and as an immediate corollary Theorem 1.1.
First we prove part 2. Suppose Hd
k is a complete rational from of Hd. The absolute
value squared of the dimension of any object in Hd must lie in k, by [7,§2.1] (we
take the absolute value squared because this does not depend on having a pivotal
structure over k). Hence |D𝓁|2∈k, but Q(D𝓁) = Q(|D2
𝓁|) in our cases.
Now we turn our attention to the main result, part 3. Again our approach is to ﬁnd
an invariant which does not depend on the rational form and see that it generates
Q(λ𝓁). A key observation in [ 22, 2] is that the whole structure of the Haagerup
and extended Haagerup planar algebras can be recovered from the “moments” and
“twisted moments” of a generator S. The moments are just the diagrammatic traces
of the powers of S, while the twisted moments are the diagrammatic traces of
the powers of ρ
1
2 (S) where ρ
1
2 is the ‘one-click’ rotation. Since ρ
1
2 changes the
shading, it only makes sense in the shaded planar algebra, rather than the even part.
Nonetheless we show in this section how to construct normalized twisted moments
of an element R in a shaded planar algebra which are invariants of the even part. In
particular, ifCK is the even part of a 3-supertransitive shaded planar algebra, R is
a Q-linear combination of projections in CK and ifCk is a complete rational form of
CK over k, then k must contain the normalized third twisted moment of R.
In order to deﬁne the twisted moments we need to deﬁne several morphisms.
Suppose that Ck is a split fusion category over k with an object Y such that
Hom (Y⊗Y⊗Y, 1) is 1-dimensional (this is assured if Kk is the even part of a
3-supertransitive planar algebra) and R is a Q-linear combination of simple projec-
tions in End (Y⊗m) for some m. Later, we will specialize to the category Ck =Hp
𝓁 ,
the object Y =f (2), and the morphism
R = 1
λ𝓁
S = 1
2(P−Q)∈ End
(
f (2)⊗n/2)
.
14
Choose nonzero elementsB,B′,T , andT′ in the 1-dimensional spaces Hom (Y⊗Y, 1),
Hom (1,Y ⊗Y ), Hom (Y⊗Y⊗Y, 1), and Hom (1,Y ⊗Y⊗Y ) respectively. We
can build morphisms BY ⊗2i : Y⊗2i → 1 and BY ⊗2i : 1 → Y⊗2i by composing
appropriately many copies of B or B′. For example, BY ⊗4 =B◦ (1⊗B⊗ 1).
Deﬁnition 4.1 Deﬁne the theta symbol Θ∈k by T◦T′, and the circle C∈k by
B◦B′. Using the usual string notation, with a string labeled by Y , we have:
Θ(T,T ′) =
T′
T
and C(B,B′) =
B′
B
Let a thick line denote m− 1 copies of a thin line (i.e. the object Y⊗m−1).
Deﬁnition 4.2 Deﬁne ˆM3(R;B,B′,T,T ′)∈ k, the unnormalized third twisted
moment of a morphism R∈ End (Y⊗m), by the value of the following composition
ˆM3(R;B,B′,T,T ′) =BY ⊗2m−2◦ (idY ⊗m−1⊗T⊗ idY ⊗m−1)◦
◦ (R⊗ idY ⊗m+1)◦ (idY⊗R⊗ idY ⊗m)◦
◦ (idY ⊗2⊗R⊗ idY ⊗m−1)◦ (T′⊗B′
Y ⊗2m−2)
=
R
R
R
B
B′
T
T′
Deﬁne the normalized third twisted moment by
M3(R) =
ˆM3(R;B,B′,T,T ′)
Θ(T,T ′)C(B,B′)m−1.
Lemma 4.3 M3(R) does not depend on the choice of B, B′, T , and T′.
Proof Each of B, B′, T , and T′ are well-deﬁned up to a choice of scalar. Each of
Θ, C , and ˆM3(R) are homogoenous with respect to these rescalings, and it is easy
to see that M3(R) is degree 0 with respect to each of these rescalings.
Theorem 4.4 IfCk is a split rational form for Hp
𝓁(C) over a ﬁeld k, then λ𝓁∈k.
15
Proof Let Y be the simple object of Ck corresponding to the object f (2) ofHp
𝓁(C).
Let R = 1
2(P−Q) = 1
λ𝓁
S∈ End
(
Y⊗2𝓁+2)
. The morphism R makes sense in Ck
because Ck is split. Consider the scalar M3(R)∈ k. Since this scalar does not
depend on any choices, we can compute it in Hp
𝓁(C) using the following obvious
choices:
B = f (2) f (2) B′ = f (2)f (2)
T = f (2) f (2) f (2) T′ = f (2)f (2)f (2) .
Since S is uncappable, any f (2) connected to an S can be replaced with the identity.
Thus with the above choices the unnormalized third twisted moment ˆM3(R) is given
by
ˆM3(R) =
R
R
R
⋆
⋆
⋆
= 1
[2]2λ3
𝓁
S
S
S
⋆
⋆
⋆
= 1
[2]2λ3
𝓁
tr
(
ρ
1
2 (S)3
)
hence the name “third twisted moment.” (In the equation above, we don’t literally
mean equality of these diagrams; they live in diﬀerent vector spaces. Instead, we
mean that each diagram is the same multiple of the appropriate empty diagram.)
The value of this moment can be easily computed using the formula for the square
of ρ
1
2 (S) in Equation (3.1):
1
[2]2λ3
𝓁
tr
(
ρ
1
2 (S)3
)
= 1
[2]2λ3
𝓁
tr
(
(ˇr− 1)ρ1/2(S)2 + ˇrρ1/2(S)
)
= 1
[2]2λ3
𝓁
ˇr(ˇr− 1)[n + 1]
=λ𝓁[2]2(1− ˇr−1)[n + 1]
16
=λ𝓁[2]2 [2n + 2]
[n + 2].
(In the last step we used the identity ([ n + 2]− [n])[n + 1] = [2n + 2].)
We have Θ = [5] + 1 and C = [3] and thus
M3(R) =λ𝓁
[2n + 2]
[n + 2]
[2]2
([5] + 1) [3]2𝓁+1.
Finally, since M3(R)∈k, and [2n+2]
[n+2]
[2]2
([5]+1)[3]2𝓁+1∈k since odd quantum numbers
lie in Q(D𝓁), [2] 2 = [3] + 1 can be written as a sum of odd quantum numbers, and
ratios of even quantum numbers (in particular [2n+2]
[n+2] ) lie in Q(D𝓁), we conclude
that λ𝓁∈k.
5 The Drinfel’d center
The goal of this section is to give a proof of part 4 of Theorem 1.2, completing the
proof of Theorem 1.2. Our proof is somewhat unsatisfying since it is indirect and
relies on extensive computations from [ 11]. Presumably one could use calculations
along the lines of [ 11] to give a more direct proof (speciﬁcally by explicitly writing
down formulas for the half-braidings which only use scalars in Q(ζ39)).
First notice that the entries of the T -matrix (see below) for Z(Hp
0(C)) generate
Q(ζ39) so if there is a complete rational form over a ﬁeld k as a ribbon category,
then k must contain ζ39.
Now we prove the other direction, namely that Z(Hp
0(C)) has a complete rational
form over Q(ζ39) as a ribbon category. Explicitly we will prove that Z(Hp
0(Q(ζ39)))
is a complete rational form. The argument will take place in two steps. First we
prove a general result that the Drinfel’d center of a rational form is a rational form
for the Drinfel’d center. Next, we check that Z(Hp
0(Q(ζ39))) is split. For both
steps of the argument the key element is the induction functor I :C→ Z(C) which
commutes with base extension.
We quickly recall some key deﬁnitions and results concerning the Drinfel’d center and
module categories (see [ 19, 20]). Let D be a fusion category and M a semisimple
ﬁnite left module category. If M1 and M2 are objects in M then the internal hom
HomD
⟲M(M1,M 2) is deﬁned to be the object in D which represents the functor
X↦→ Hom (X⊗M1,M 2). Deﬁne the dual category D∗ = FunD(M,M) of module
endofunctors of M. If M is a simple object in M, there is a natural algebra
structure on the object A = HomD
⟲M(M,M ) and the categories M,Mop, and
D∗ can be concretely identiﬁed with the categories of right A-modules inM, left
A-modules inM, and A–A bimodules inM, respectively. Fixing the simple object
M , there’s an induction functor I :M→D ∗, given by tensoring a right A-module
on the left with A.
The Drinfel’d center Z(C) has two equivalent deﬁnitions. First, the objects of
Z(C) are pairs ( X,{σX,Y}Y ) consisting of an object in C and a collection of half-
braidings σX,Y : X⊗Y → Y ⊗X satisfying certain naturality conditions. For
17
the second, recall that C is a module category over C ⊠Cop (with the action
(X ⊠Y )⊗M→X⊗M⊗Y ). Then, Z(C) is the dual of C ⊠Cop. Explicitly, we
can take M = 1, and let A = HomC⊠Cop
⟲C(1, 1) be the internal endomorphisms
of 1 ∈C . Thus A is an algebra object in C ⊠Cop, and Z(C) is the category of
A–A bimodule objects in C ⊠Cop. From this point of view the induction functor
I :C→ Z(C) is given by X↦→A⊗X .
Remark. It is natural to wonder what I(X) is in terms of the ﬁrst deﬁnition of the
center. According to [ 7, Prop. 5.4] for a split fusion category the underlying object
of I(X) is ⨁
V V⊗X⊗V∗ (where the sum is taken over all simples). This formula
certainly does not work in the non-split case. Notice, however, that an analogous
problem occurs when decomposing the adjoint representation of the group ring k[G].
Here, in the nonsplit case, the adjoint representation is not ⨁
V V⊗V∗ but instead
the coinvariants with respect to the the left action of the division ring EndG(V ) on
V and its right action on V∗. The same modiﬁcation works for the induction functor:
for each f∈ End (V ), we have two maps ⨁
V V⊗X⊗V∗ ⇒⨁
V V⊗X⊗V∗ given
by acting on either V or V∗, and the correct value of I(X) is the colimit of the
collection of these diagrams where f varies over a basis of End (V ). (This colimit
exists because all small colimits exist in an abelian category.) The half-braidings for
I(X) in the split case were written down in [ 17, Theorem 2.3]. Their formula can be
modiﬁed to work in the non-split case, by being careful about normalizations and
by quotienting out by the action of End (V ) as above. Indeed, since every object in
Z(C) is a summand of an induced object, it’s possible to prove that the center of a
rational form is a rational form of the center explicitly by writing down formulas
for the half-braiding on the induced objects following [ 17, Theorem 2.3]. Here, we
choose instead to work directly with the second description of the center.
Lemma 5.1 Suppose that Ck is a rational form of CK . The natural functor
Z(Ck)⊗kK→Z(CK) is full, faithful, commutes with the induction functors, and is
dominant. Hence, Z(Ck) is a rational form as a braided tensor category of Z(CK).
Lemma 5.1 follows immediately from the following more general result.
Lemma 5.2 Suppose thatDK is a fusion category overK , thatMK is a semisimple
module category over DK , that Dk is a rational form of DK over k (as a fusion
category), and that Mk is a rational form of MK over k (as a module category
overDk). Let F be the full, faithful and dominant functor F :Dk⊗kK→D K
guaranteed by the fact thatDk is a rational form, andG the corresponding functorG :
Mk⊗kK→M K . Let M be a simple object in Mk. Then, F(HomDk
⟲Mk
(M,M ))
and HomDK
⟲MK
(G(M),G(M)) are isomorphic as algebra objects, and there is a
functorF∗ : D∗
k⊗kK→ D∗
K induced by F which is full, faithful and dominant.
Hence, D∗
k is a rational form of D∗
K .
Proof Let Ak = HomDk
⟲Mk
(M,M ) inDk and AK = HomDK
⟲MK
(G(M),G(M))
inDK . First we show thatF(Ak)∼=AK as algebra objects. We need only check that
F(Ak) represents the functor DK→ Set given by X↦→ Hom (X⊗G (M),G(M)),
which follows immediately from the fact that Mk is a rational form for MK .
18
Since F(Ak) ∼= AK , the functor F : Dk⊗k K → DK induces a functor F∗ :
D∗
k⊗kK→D∗
K , which we now describe. Recall we can interpret D∗
k as the Ak–Ak
bimodules in Dk (and similarly for DK ). Given an Ak–Ak bimodule in Dk, we
can construct an AK –AK bimodule in DK simply by applying the functor F to
the underlying object, as well as to the morphisms making it a bimodule. We now
want to prove that F∗ is full and faithful. Suppose that X and Y are Ak–Ak
bimodules, then among all maps from X to Y the bimodule maps are picked out by
satisfying certain linear equations with coeﬃcients in k. Similarly among all maps
fromF(X) to F(Y ) the bimodule maps are picked out by satisfying the same linear
equations with coeﬃcients in k. Thus, since F :Dk⊗kK→DK is an isomorphism
on morphism spaces, it follows that F∗ :D∗
k⊗kK→D∗
K is as well.
Thus we need only check that F∗ :D∗
k⊗kK→D∗
K is dominant (i.e. every object in
the target is a summand of an object in the image of the functor). SinceF(Ak)∼=AK
we see that F◦ I and I◦F are naturally isomorphic functors. If X is an arbitrary
AK –AK bimodule, then certainly X is a summand of I(R(X)) (where R is the
restriction functor which forgets the left action of AK ). Since Mk is a rational form
ofMK , we see that R(X) is a summand of F(N) for some right Ak module N .
Hence, X is a summand of I(F(N))∼=F(I(N), and the functor is dominant.
The centerZ(Hp
0(C)) has previously been described in [11] (see [10] for further details).
The simple objects are 1,π 1,π 2,µ 1,...,µ 6,σ 0,σ 1,σ 2. Let I be the induction functor
I :Hp
0→ Z(Hp
0). Over C, it is described on the level of objects by the graph in
Figure 3. Note that over C we have
I(f (2))∼=π1⊕π2⊕µ1⊕... ⊕µ6⊕σ0⊕σ1⊕σ2,
and in particular there is exactly one copy of each simple except 1.
1 π1 π2 µ1 µ2 µ3 µ4 µ5 µ6 σ0 σ1 σ2
1 f (2) P Q P′′ Q′′
Figure 3: The induction functor for Hp
0(C), reproduced from Figure 5 of [ 11], with
ˆ0ρ,ˆ1ρ,ˆ2ρ,ˆα1 and ˆα2 renamed to f (2),P,Q,P ′′ and Q′′ respectively.
Theorem 5.3 Z(Hp
0(Q(ζ39))) is a split fusion category over Q(ζ39).
Proof Since f (2) is an object in Hp
0(Q(ζ39)), we have that I(f (2)) is an object in
Z(Hp
0(Q(ζ39))). We build explicit projections on to many of its summands. Let
θI(f (2)) be the ribbon element acting on I(f (2)). Over C, the ribbon element θI(f (2))
acts on each simple object by the corresponding entry in the T -matrix which is
diagonal with entries
(Tjj) = (1, 1, 1,ζ 6
39,ζ−6
39 ,ζ 15
39,ζ−15
39 ,ζ 18
39,ζ−18
39 , 1,ζ 13
39,ζ−13
39 ).
19
Consider 1
39
∑
iζmi
39θi
I(f (2)) for diﬀerent values of m. These give projections onto the
eigenspaces of the T -matrix Using the values of the T -matrix it follows that for
these give projections onto each of µi, σ1, and σ2. Hence all of those simples are
deﬁned over Q(ζ39).
The sum ∑
iθi
I(f (2)) gives a projection onto π1⊕π2⊕σ0. Let F be a single strand
labelled by π1⊕π2⊕σ0 with a ring around it labelled by σ1. Looking at the
corresponding entries in the S-matrix (described in [ 10]) we see that 5+
√
13
18 (1 +F )
gives a projection onto π1 while its complement gives a projection onto π2⊕σ0.
Consider I(1)∼= 1⊕π1⊕ 2π2. Notice that here π2 is a summand while σ0 is not.
In particular, there is a map over C from I(1) to π2⊕σ0, and hence over Q(ζ39)
there also must be such a map. Hence by semisimplicity, we must have σ0 and π2
are objects over Q(ζ39).
