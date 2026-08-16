---
doc_id: arxiv-2607.03827v1
doc_title: "AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS"
section_id: sec-003-4-the-asymptotic-algebra-of-an-affine-cellular-a
section_title: "The asymptotic algebra of an affine cellular algebra"
section_number: 4
pages: 13-17
source_pdf: 2607.03827v1.pdf
source_sha256: 965d69603381942a
doc_brief: "AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS — The theory of affine cellular algebrasAis extended to incorporate their asymptotic algebras ˆA, clarifying unexpected differences between classical"
---
In this section, the asymptotic algebra of an affine cellular algebra and the embedding of an affine
cellular algebra into its asymptotic algebra will be described in detail. Moreover, the asymptotic algebra
will be constructed as endomorphism ring in a double centraliser property. This proves Theorems A
and D.
LetAbe an affine cellular algebra with cell chain
(10)0 =J 0⊂J 1⊂···⊂J n =A,
with cell data(Bi,σi,∆i,ψ (i),αi). In particular,
(11)α i :J i/Ji−1→∆ i⊗Bi ∆′
i = (Mdi(Bi),ψ (i))
is an isomorphism ofA-bimodules.
Theasymptotic algebra bAof an affine cellularAhas been defined in [18] as the direct product of all
matrix algebrasMdi(Bi)obtained from the cell data of the cell chain. In [18, comment before Lemma
5.5 on page 177], it has been mentioned that the definition of the asymptotic algebra given in [18]
coincides with Lusztig’s asymptotic algebra in the case of the extended affine Hecke algebra of type
An−1. Further details will be given in the final section when discussing examples and methods.
Definition 9.The asymptotic algebra ofAis defined as bA=M dn(Bn)×···×M d1(B1). Set bAi =
Mdi(Bi), for anyi.
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 14
For each1≤k≤ndenote the left multiplication ofAonJ k/Jk−1 byλ k :A→End(J k/Jk−1), i.e.
λk(a) = [x+J k−17→ax+J k−1],
for alla∈Aandx∈J k. Note thatλk is rightA-linear. Consider the ring homomorphism
(12)λ:A→End(J n/Jn−1)×End(J n−1/Jn−2)×···×End(J 1), λ= (λ n,λn−1,···,λ 1)
Due to [5, Lemmas 4.2, 3.2], the mapλis injective if and only if no determinantdet(ψ (k))is a
zero-divisor inBk. By [5, Theorem 3.3], the ringEnd(Jk/Jk−1)is isomorphic toM dk(Bk)ifdet(ψ (k))
is not a zero-divisor inBk (or ifJ k/Jk−1 is idempotent). We will briefly recall the steps of the proof
of [5, Theorem 3.3]. LetJbe an affine cell ideal with cell datum(B,σ,∆,ψ,α)withn= rank B(∆).
Assume thatJis idempotent ordet(ψ)is not a zero-divisor inB. Then in a first step one shows that the
rightA-linear endomorphisms ofJcoincide with the rightJ-linear endomorphisms ofJ, i.e.End(J A) =
End(JJ). Moreover, the isomorphismα:J→(M n(B),ψ) =: ^Mn(B)induces an isomorphism between
End(JJ)andEnd( ^Mn(B) ^Mn(B))given byf7→αfα −1. Finally one checks that the ring homomorphism
l:M n(B)→End( ^Mn(B) ^Mn(B))given by left multiplication,l(X) = [Y7→XY], for any matrices
X,Y∈M n(B)is invertible, with inverse given byl −1(g) =g(I n), for anyg∈End( ^Mn(B) ^Mn(B)).
Hence the isomorphism betweenEnd(JA)andM n(B)is given byf7→α(f(α −1(In))).
We summarise the situation as follows: The isomorphism
α:J→(M n(B),ψ) = ^Mn(B)
induces an isomorphismEnd(JA)∼=Mn(B),f7→α(f(α −1(In))), which is the composition
End(JA) = End(JJ) α→End( ^Mn(B) ^Mn(B)) l−1
→M n(B)
f7→αfα −1
g7→g(I n)
For1≤k≤nlete k =α−1
k (Idk)∈J k/Jk−1. Combining the left multiplicationλk :A→End(J k/Jk−1)
with the isomorphism betweenEnd(Jk/Jk−1)andM dk(Bk)yields a ring homomorphismΘ k :A→
Mdk(Bk)given by
(13)Θ k(a) =α k(aek),
for alla∈A. Since the multiplication onJk/Jk−1 is encoded inψ(k), by (8) any elementa∈J′
k satisfies:
(14)Θ k(a) =α k(aek) =α k(a)ψ(k),
where a=a+J k−1.
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 15
Theorem 10(Theorem A).LetAbe an affine cellular algebra such that no determinantdet(ψ (k))is
a zero-divisor inB k. ThenΘ :A→ bAgiven byΘ = (Θ n,···,Θ 1), is an embedding ofAinto its
asymptotic algebra. More concretely,
(15)Θ(a) = (α n(aen),...,α 1(ae1)), a∈A.
Let1≤k≤n, then for anya∈J ′
k:
(16)Θ(a) = (α n(aen),···,α k(aek),αk(a)ψ(k),0,...,0),
sinceΘ l(a) = 0, for alll<k.
Remark 11.The same proof shows that there is the following embedding ofAinto a more economic
version of bA:
Letmbe the least non-negative integer such thatJ m/Jm−1 is a faithful leftA/Jm−1-module. Then
there is an embedding ofAintoM dm(Bm)×···×M d1(B1).
In particular, when the affine cell idealJ1 is a faithfulA-module, one may choosem= 1and get an
embedding into the matrix algebraMd1(B1).
We choose however not to take this abbreviation, for the following reason: By[18], simpleA-modules
are classified by subsets of the disjoint union of the maximal spectra of the matrix components ofbA.
The abbreviation usingm<nwould confuse this approach and Theorem C could not be formulated any
more.
In the second part of this section we will show that the asymptotic algebra can also be constructed
as the double centraliser of the direct sum of cell modules. LetJbe an affine cell ideal ofA, with cell
datum(B,σ,∆,ψ,α)andn= rank B(∆). Letα:J→∆⊗ B ∆′ be the givenA-bimodule isomorphism
with∆ =V⊗BanA-B-bimodule,Vfree of ranknoverkand∆ ′ =B⊗Vthe inducedB-A-bimodule.
ThenJ ∼= ∆n as leftA-module andJ ∼= (∆′)n as rightA-module. Moreover, B∆∼= BBn∼= ∆′
B as
B-modules.
By Lemma 3 or [5, Theorem 3.3],End(A∆)∼= B, ifJis idempotent ordet(ψ)is not a zero-divisor
inB. Similarly, the maplb : ∆′→∆′ given bylb(x) =bx, for anyb∈Bis rightA-linear and yields an
injective ring homomorphisml:B→End(∆ ′
A). In caseJis idempotent ordet(ψ)is not a zero-divisor
inB, it can be shown as in Lemma 3 that the maplis an isomorphism. Thus in this case we obtain
the following chain of isomorphisms, usingJ∼= (∆′)n as rightA-modules:
(17)End(J A)∼=Mn(End(∆′
A))∼=Mn(B)∼= End(Bn
B) = End(∆B).
The left multiplication ofAonJ, i.e.λ(a) =:λ a∈End(J A)∼= End(∆B)is defined byλ a(x) =ax,
for allx∈J. IdentifyingJ ∼= ∆⊗ B ∆′∼= ∆n, the leftA-actionλ a onJand its restriction, sayλ ′
a,
on∆coincide. The mapΘ :A→A/J×End(J A), withΘ(a) = (a+J,λ a), for alla∈A, is a ring
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 16
homomorphism. By Lemma 2,Θis injective if and only ifdet(ψ)is not a zero-divisor inB. Using
equation (17) we obtain an injective ring homomorphism
Θ :A→A/J×End(∆ B), a7→(a+J,λ ′
a),
withλ ′
a the left action ofAon∆. Repeating this process along a cell chain yields an embedding of
rings:
Θ :A→
nY
i=1
End((∆i)Bi), a7→(λ ′(n)
a ,···,λ ′(1)
a ),
whereλ′(i)
a denotes the left action ofa∈Aon∆ i. By Corollary 6,HomA(∆i,∆j) = 0fori̸=j, if for
allithe idealJ i/Ji−1 is idempotent anddet(ψ (i))is not a zero-divisor inB i. Therefore, the faithful
A-moduleM= Ln
i=1 ∆i satisfies:
EndA(M) =
nY
i=1
EndA(∆i)(18)
End(MEndA(M)) =
nY
i=1
End(∆iBi)(19)
Thus we have proven the following Theorem:
Theorem 12.LetAbe an affine cellular algebra with cell chain0 =J 0⊂J 1⊂···⊂J n =Aand cell
datum(B i,σi,∆i,ψ (i),αi)andn i = rankBi(∆i), for alli. If for alli, the idealJ i/Ji−1 is idempotent
anddet(ψ (i))is not a zero-divisor, then the following hold.
(1)M= Ln
i=1 ∆i is a faithful leftA-module.
(2)T= End A(M) =Qn
i=1 EndA(∆i).
(3) The leftA-module action ofAonMinduces an embedding of rings
λ:A→End(M T ) =
nY
i=1
End(∆iBi)∼=Mdn(Bn)×···×M d1(B1) = bA,
which coincides with the embedding ofA→bAas shown in[5].
Proof.Note thatMis a faithful leftA-module, because ifaM= 0, thena∆ i = 0, for alli. Hence,
a(Ji/Ji−1) = 0, for alli. Thusa+J i−1 ∈ann Ji−1/Ji−2(Ji−1/Ji−2). Asdet(ψ (i−1))are not zero-
divisors by assumption,a∈J i−1, for alli. Thusa∈J 0 = 0. In particular, the left action ofA
onMyields an embedding ofAintoEnd(M T ), whereT= End( AM). By the previous argument,
End(MT )∼=Qn
i=1 End(∆iBi)∼= bA.□
AFFINE CELLULAR ALGEBRAS AND ASYMPTOTIC ALGEBRAS 17
