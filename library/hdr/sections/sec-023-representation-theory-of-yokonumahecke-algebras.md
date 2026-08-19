---
doc_id: hdr
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-023-representation-theory-of-yokonumahecke-algebras
section_title: "Representation theory of Yokonuma–Hecke algebras"
section_number: null
pages: 49-54
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
doc_brief: "HAL Id: tel-01411063 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 27 sections: Algebras of"
---
The representation theory of Yokonuma–Hecke algebras has been ﬁrst studied by Thiem [Th1, Th2, Th3]
in the general context of unipotent Hecke algebras. The generality of his results and the new presentation
for Yd,n(q) has led us to develop a combinatorial approach to the representation theory of the Yokonuma–
Hecke algebra of typeA in [ChPdA1]. In this section, we will give an explicit description of the irreducible
representations of Yd,n(q) in terms of d-partitions and standard d-tableaux.
Recall that we denote byP(d,n ) the set of d-partitions of n. Let λ = (λ(0),...,λ (d−1))∈P (d,n ). A
node θ of λ is a triple (x,y,i ), where 0⩽i⩽d− 1 and (x,y ) is a node of the partition λ(i). We deﬁne
p(θ) :=i to be the position of θ and c(θ) :=qy−x to be the quantum content of θ.
A d-tableau of shape λ is a bijection between the set {1,...,n } and the set of nodes of λ. In other
words, ad-tableau of shape λ is obtained by placing the numbers 1,...,n in the nodes of λ. The size of
ad-tableau of shape λ isn, that is, the size of λ. A d-tableau is standard if its entries increase along any
row and down any column of every diagram in λ. For d = 1, a standard 1-tableau is a usual standard
tableau.
For ad-tableauT , we denote respectively by p(T|i) and c(T|i) the position and the quantum content
of the node with the number i in it. For example, for the standard 3-tableau T =
(
1 3 , ∅, 2
)
of size
3, we have
p(T| 1) = 0, p(T| 2) = 2, p(T| 3) = 0 and c( T| 1) = 1, c(T| 2) = 1, c(T| 3) =q.
For anyd-tableauT of size n and any permutation σ∈ Sn, we denote byTσ thed-tableau obtained
fromT by applying the permutation σ on the numbers contained in the nodes of T . We have
p(Tσ|i) = p
(
T|σ−1(i)
)
and c( Tσ|i) = c
(
T|σ−1(i)
)
for all i = 1,...,n .
Note that if the d-tableauT is standard, the d-tableauTσ is not necessarily standard.
Now, let λ∈P (d,n ), and let Vλ be a C(q)-vector space with a basis {vT} indexed by the standard
d-tableaux of shape λ. We set vT := 0 for any non-standard d-tableauT of shape λ. By [ChPdA1,
Proposition 5 & Theorem 1] and [ChPo2, Theorem 3.7], we have the following description of the irre-
ducible representations of C(q)Yd,n(q):
46
Theorem 6.2 Let{ξ0,ξ 1,...,ξ d−1} be the set of all d-th roots of unity (ordered arbitrarily). Let T be
a standard d-tableau of shape λ∈P (d,n ). For brevity, we set pi := p(T|i) and ci := c(T|i) for all
i = 1,...,n . The vector space Vλ is a representation of C(q)Yd,n(q) with the action of the generators on
the basis element vT deﬁned as follows: for j = 1,...,n ,
tj(vT ) =ξpjvT ; (6.8)
for i = 1,...,n − 1, if pi > pi+1 then
gi(vT ) = vTsi , (6.9)
if pi < pi+1 then
gi(vT ) =q vTsi , (6.10)
and if pi = pi+1 then
gi(vT ) = qci+1− ci+1
ci+1− ci
vT + qci+1− ci
ci+1− ci
vTsi , (6.11)
where si is the transposition (i,i + 1). Further, the set {Vλ| λ∈P (d,n )} is a complete set of pairwise
non-isomorphic irreducible representations of C(q)Yd,n(q).
The above theorem implies that the algebra C(q)Yd,n(q) is split. As we have already mentioned,
when q↦→ 1, the algebra C(q)Yd,n(q) specialises to the group algebra C[G(d, 1,n )], which is semisimple.
By Tits’s deformation theorem, we obtain that the algebra C(q)Yd,n(q) is also semisimple.
Let now θ : C[q,q−1]→ C be a ring homomorphism such that θ(q) = η ∈ C\{ 0}. Using the
representation theory of C(q)Yd,n(q), we have proved the following semisimplicity criterion for CYd,n(η)
[ChPdA1, Proposition 9]:
Proposition 6.3 The specialised Yokonuma–Hecke algebra CYd,n(η) is (split) semisimple if and only if
θ(P (q))⁄= 0, where
P (q) =
∏
1⩽i⩽n
(1 +q +··· +qi−1).
Note that following Ariki’s semisimplicity criterion (4.2), the algebra CYd,n(η) is semisimple if and
only if the specialised Iwahori–Hecke algebra CHn(η) is semisimple.
Another way to obtain the above result is through our deﬁnition of a canonical symmetrising form τ
on Yd,n(q) [ChPdA1, Proposition 10]. Having calculated the Schur elements of Y d,n(q) with respect to
τ [ChPdA1, Proposition 11], we can deduce the above semisimplicity criterion with the use of Theorem
1.7. More precisely, we have the following:
Theorem 6.4 We deﬁne the linear map τ : Yd,n(q)→ C[q,q−1] by
τ(tr1
1 ...t rn
n gw) =
{
1 if w = 1 and rj = 0 for all j = 1, 2,...,n,
0 otherwise, (6.12)
where w∈ Sn and 0⩽ rj⩽ d− 1 for all j = 1, 2,...,n . Then τ is a symmetrising form on Yd,n(q),
called the canonical symmetrising form. If λ = (λ(0),...,λ (d−1))∈P (d,n ), then the Schur element of
Vλ with respect to τ is
sλ =dnsλ(0)sλ(1)...s λ(d−1), (6.13)
where sλ(i) is the Schur element of the Iwahori–Hecke algebra H|λ(i)|(q) corresponding to λ(i) for all
i = 0, 1,...,d − 1 (we take s∅ := 1).
A simple formula for the calculation of the Schur elements of Iwahori–Hecke algebras of type A is
given by Theorem 4.3.
The connection between the representation theory of the Yokonuma–Hecke algebra and that of
Iwahori–Hecke algebras of type A implied by (6.13) is explained by a result of Lusztig [Lu7, §34],
who has proved that Yokonuma–Hecke algebras, in general, are isomorphic to direct sums of matrix
algebras over certain subalgebras of classical Iwahori–Hecke algebras. Using the new presentation for
Yd,n(q), Jacon and Poulain d’Andecy [JaPdA] have explicitly described this isomorphism between the
47
Yokonuma–Hecke algebra of typeA and a direct sum of matrix algebras over tensor products of Iwahori–
Hecke algebras of typeA. Another proof of this result has been given recently in [EsRy], where Espinoza
and Ryom-Hansen have constructed a concrete isomorphism between Yd,n(q) and Shoji’s modiﬁed Ariki–
Koike algebra. Note that in all cases the result has been obtained over the ring C[q1/2,q−1/2] (using the
generators ~gi deﬁned in Remark 6.1). We have managed to show that it is still valid over the smaller
ring C[q,q−1]. We have [ChPo2, Theorem 4.3]:
Yd,n(q)∼=
⨁
µ∈Compd(n)
Matmµ(Hµ0(q)⊗Hµ1(q)⊗···⊗H µd−1(q)), (6.14)
where
Compd(n) ={µ = (µ0,µ 1,...,µ d−1)∈ Nd|µ0 +µ1 +··· +µd−1 =n} (6.15)
and
mµ = n!
µ0!µ1!...µ d−1! (6.16)
6.2 Aﬃne and Cyclotomic Yokonuma–Hecke algebras
We have now seen two families of algebras that are deformations of the groups algebra of the complex
reﬂection group G(d, 1,n ): the Ariki–Koike algebras and the Yokonuma–Hecke algebras of type A. Both
families include the Iwahori–Hecke algebras of typeA. The former preserve the “good” quadratic relations
of the Iwahori–Hecke algebras, while the latter preserve the wreath product structure of G(d, 1,n )∼=
(Z/dZ)≀ Sn.
In [ChPdA2], we introduced the aﬃne and cyclotomic Yokonuma–Hecke algebras, which give rise
to both Ariki–Koike algebras and Yokonuma–Hecke algebras of type A as quotients and as special
cases. Let n∈ N, d∈ N∗ and l∈ N∗∪{∞} . Let q and (Qi)i∈N be indeterminates, and set Rl :=
C[q±1,Q±1
0 ,Q±1
1 ,...,Q ±1
l−1] if l <∞, and R∞ := C[q±1]. We deﬁne the algebra Y( d,l,n ) to be the
associativeRl-algebra generated by the elements
g1,...,g n−1,t 1,...,t n,X 1,X−1
1
subject to the relations (6.1)–(6.2), together with the following relations concerning the generator X1:
X1X−1
1 = X−1
1 X1 = 1
X1g1X1g1 = g1X1g1X1
X1gi = giX1 for all i = 2,...,n − 1,
X1tj = tjX1 for all j = 1,...,n ,
(6.17)
and if l< ∞,
(X1−Q0)(X1−Q1)··· (X1−Ql−1) = 0. (6.18)
The algebra Y(d,∞,n ) is called the aﬃne Yokonuma–Hecke algebra. For l <∞, the algebra Y(d,l,n )
is called the cyclotomic Yokonuma–Hecke algebra. These algebras are isomorphic to the modular frami-
sations of, respectively, the aﬃne Hecke algebra ( l =∞) and the Ariki–Koike algebra ( l <∞); see
deﬁnitions in [JuLa5, Section 6] and [ChPdA1, Remark 1].
The cyclotomic Yokonuma–Hecke algebra is a quotient of the aﬃne Yokonuma–Hecke algebra by the
relation (6.18). If we map X1↦→Q0 for l< ∞ or X1↦→ 1 for l =∞, we obtain a surjection of Y( d,l,n )
onto Yd,n(q). If we map tj↦→ 1 for all j = 1,...,n , then we obtain a surjection of Y(d,l,n ) ontoH(l,n ),
whereH(l,n ) denotes the Ariki–Koike algebra associated to G(l, 1,n ) for l <∞ andH(∞,n ) denotes
the aﬃne Hecke algebra of type A. Moreover, we have Y( d, 1,n )∼= Yd,n(q) and Y(1,l,n )∼=H(l,n ). In
particular, we have Y(1, 1,n )∼=Hn(q). All these relations are depicted in the following commutative
diagram (where l is taken to be a positive integer):
48
H(∞,n )∼= Y(1,∞,n )
(6.18) ** **TTTTTTTTTTTTTTTT
X1↦→1
-- --ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
Y(d,∞,n )
tj↦→1
55 55llllllllllllll
(6.18)
// //
X1↦→1 )) ))RRRRRRRRRRRRRR Y(d,l,n ) tj↦→1
// //
X1↦→Q0

H(l,n )∼= Y(1,l,n ) X1↦→Q0
// //Hn(q)∼= Y(1, 1,n )
Yd,n(q)∼= Y(d, 1,n )
tj↦→1
11 11ddddddddddddddddddddddddddddddddddd
Remark 6.5 Letp be a prime number. In a recent series of papers [Vi1, Vi2, Vi3], Vign´ eras introduced
and studied a large family of algebras, called pro-p-Iwahori–Hecke algebras. They generalise convolution
algebras of compactly supported functions on a p-adic connected reductive group that are bi-invariant
under the pro-p-radical of an Iwahori subgroup, which play an important role in the p-modular repre-
sentation theory of p-adic reductive groups. In [ChSe] we have shown that the aﬃne Yokonuma–Hecke
algebra Y(d,∞,n ) is a pro-p-Iwahori–Hecke algebra. Thus, the aﬃne Yokonuma–Hecke algebra gener-
alises the aﬃne Hecke algebra of type A in a similar way that the Yokonuma–Hecke algebra generalises
the Iwahori–Hecke algebra of type A. In particular, for q = pm and d = pm− 1, where m is a positive
integer, Y(d,∞,n ) is isomorphic to the convolution algebra of complex valued and compactly supported
functions on the group GL n(F ), with F a suitable p-adic ﬁeld, that are bi-invariant under the pro- p-
radical of an Iwahori subgroup.
Remark 6.6 Following Lusztig’s approach in [Lu7], Cui [Cui] has established an explicit algebra isomor-
phism between the aﬃne Yokonuma–Hecke algebra Y(d,∞,n ) and a direct sum of matrix algebras over
tensor products of aﬃne Hecke algebras of type A, similar to (6.14). More recently, Poulain d’Andecy
[PdA] obtained the same result, as well as an isomorphism between the cyclotomic Yokonuma–Hecke
algebra Y(d,l,n ), where l< ∞, and a direct sum of matrix algebras over tensor products of Ariki–Koike
algebras, using the same approach as in [JaPdA]. The isomorphism theorem for cyclotomic Yokonuma–
Hecke algebras has been subsequently re-obtained by Rostam [Ros] using his result that cyclotomic
Yokonuma–Hecke algebras are cyclotomic quiver Hecke algebras.
In [ChPdA2] we have constructed several bases for the algebra Y( d,l,n ). In order to describe them
here, we introduce the following notation: Let Zl :={0,...,l − 1} for l <∞ and Z∞ := Z. We deﬁne
inductively elements X2,...,X n of Y(d,l,n ) by setting
Xi+1 :=q−1giXigi for all i = 1,...,n − 1.
LetBd,n be a basis of the Yokonuma–Hecke algebra Y d,n(q)∼= Y(d, 1,n ) over Rl (we can take, for
example,BH
d,n deﬁned in (6.7)). We denote by BAK
d,l,n the following set of elements of Y(d,l,n ):
Xa1
1 ...X an
n ·ω, a k∈Zl and ω∈B d,n.
Now, for k = 1,...,n , we set
W (k)
J,a,b :=g−1
J ...g −1
2 g−1
1 Xa
1 tb
1g1g2...g k−1,
W (k)−
J,a,b :=gJ...g 2g1Xa
1 tb
1g−1
1 g−1
2 ...g −1
k−1,
~W (k)
J,a,b :=gJ...g 2g1Xa
1 tb
1g1g2...g k−1,
~W (k)−
J,a,b :=g−1
J ...g −1
2 g−1
1 Xa
1 tb
1g−1
1 g−1
2 ...g −1
k−1,
where J ∈ {0,...,k − 1} and a,b ∈ Z. We use the following standard conventions: for ϵ = ±1,
gϵ
J...g ϵ
2gϵ
1 := 1 and gϵ
k−J...g ϵ
k−2gϵ
k−1 := 1 if J = 0. Then we denote, respectively, by BInd
d,l,n,BInd−
d,l,n ,
~BInd
d,l,n and ~BInd−
d,l,n the following sets of elements of Y(d,l,n ):
W (n)
Jn,an,bn
...W (2)
J2,a2,b2
W (1)
J1,a1,b1
, J k∈{ 0,...,k − 1}, ak∈Zl and bk∈{ 0,...,d − 1}.
49
W (n)−
Jn,an,bn
...W (2)−
J2,a2,b2
W (1)−
J1,a1,b1
, J k∈{ 0,...,k − 1}, ak∈Zl and bk∈{ 0,...,d − 1}.
~W (n)
Jn,an,bn
... ~W (2)
J2,a2,b2
~W (1)
J1,a1,b1
, J k∈{ 0,...,k − 1}, ak∈Zl and bk∈{ 0,...,d − 1}.
~W (n)−
Jn,an,bn
... ~W (2)−
J2,a2,b2
~W (1)−
J1,a1,b1
, J k∈{ 0,...,k − 1}, ak∈Zl and bk∈{ 0,...,d − 1}.
We then have the following [ChPdA2, Theorem 4.4]:
Theorem 6.7 Each setBAK
d,l,n,BInd
d,l,n,BInd−
d,l,n , ~BInd
d,l,n and ~BInd−
d,l,n is anRl-basis of Y(d,l,n ). In particular,
Y(d,l,n ) is a freeRl-module and, if l< ∞, its rank is equal to (dl)nn!.
Remark 6.8 The set BAK
d,l,n is the analogue of the Ariki–Koike basis (4.1) of the Ariki–Koike algebra
H(l,n ) forl< ∞, and the standard Bernstein basis of the aﬃne Hecke algebra of type A forl =∞. The
four other sets are inductive sets with respect to n, which are analogous to the inductive bases ofH(l,n )
studied in [La2, OgPo].
Furthermore, in [ChPdA2] we have studied the representation theory of the cyclotomic Yokonuma–
Hecke algebra Y(d,l,n ), which is quite similar to the representation theory of the Yokonuma–Hecke
algebra Yd,n(q). From now on, we only consider the case l< ∞.
LetKl denote the ﬁeld of fractions of Rl. We will see that the irreducible representations of the
algebraKlY(d,l,n ) are parametrised by thedl-partitions ofn. Instead of looking though at dl-partitions
as dl-tuples of partitions, we look at them as d-tuples of l-partitions, and we call them ( d,l )-partitions
when seen as such. We denote by P(d,l,n ) the set of ( d,l )-partitions of n. If λ∈ P(d,l,n ), then
λ = (λ(0), λ(1),..., λ(d−1)), where λ(i) is an l-partition for all i = 0, 1,...,d − 1, and ∑d−1
i=0|λ(i)| = n.
We thus have λ(i) = (λ(i,0),λ (i,1),...,λ (i,l−1)), where λ(i,j) is a partition for all i = 0, 1,...,d − 1 and
j = 0, 1,...,l − 1, and∑d−1
i=0
∑l−1
j=0|λ(i,j)| =n.
A node θ of λ is a 4-tuple (x,y,i,j ), where 0⩽i⩽d− 1, 0⩽j⩽l− 1 and (x,y ) is a node of the
partition λ(i,j). We deﬁne p( θ) := i to be the d-position of θ and c(θ) := Qjqy−x to be the l-quantum
content of θ.
Following the deﬁnitions in §6.1, a (d,l )-tableau is simply a dl-tableau and a standard (d,l )-tableau
is simply a standard dl-tableau. For a ( d,l )-tableauT and for i = 1,...,n , we denote respectively by
p(T|i) and c(T|i) the d-position and the l-quantum content of the node with the number i in it.
Now, let λ∈P (d,l,n ), and let Vλ be a C(q)-vector space with a basis{vT} indexed by the standard
(d,l )-tableaux of shape λ. We set vT := 0 for any non-standard (d,l )-tableauT of shape λ. By [ChPdA2,
Propositions 3.2 & 3.4], the vector space Vλ is a representation of KlY(d,l,n ), with the action of the
generators g1,...,g n−1,t 1,...,t n on the basis element vT deﬁned exactly as in Theorem 6.2, and the
action of the generator X1 given by:
X1(vT ) = c(T| 1) vT. (6.19)
Further, the set{Vλ| λ∈P (d,l,n )} is a complete set of pairwise non-isomorphic irreducible representa-
tions ofKlY(d,l,n ).
Remark 6.9 We can easily show, by induction on i, that [ChPdA2, Lemma 3.3]:
Xi(vT ) = c(T|i) vT for all i = 1,...,n. (6.20)
We also have a semisimplicity criterion for cyclotomic Yokonuma–Hecke algebras, which is exactly
the same as Ariki’s semisimplicity criterion (4.2) for Ariki–Koike algebras [ChPdA2, Proposition 4.7]:
Proposition 6.10 Let θ : Rl → C be a ring homomorphism such that θ(q)∏l−1
j=0θ(Qj) ⁄= 0 . The
specialised cyclotomic Yokonuma–Hecke algebra CY(d,l,n )θ, deﬁned via θ, is (split) semisimple if and
only if θ(P )⁄= 0, where
P =
∏
1⩽i⩽n
(1 +q +··· +qi−1)
∏
0⩽s<t⩽l−1
∏
−n<k<n
(qkQs−Qt).
We deduce that the algebraCY(d,l,n )θ is semisimple if and only if the specialised Ariki–Koike algebra
CH(l,n )θ is semisimple.
Finally, we have proved the existence of a “canonical” symmetrising form on KlY(d,l,n ) and calcu-
lated the Schur elements with respect to it [ChPdA2, §7]:
50
Theorem 6.11 We deﬁne the linear map τ : Y(d,l,n )→R l by
τ(Xa1
1 ...X an
n tb1
1 ...t bn
n gw) =
{ 1 if w = 1 and aj =bj = 0 for all j = 1, 2,...,n,
0 otherwise, (6.21)
where w∈ Sn, aj ∈ Zl and 0⩽ bj ⩽ d− 1 for all j = 1, 2,...,n . Then τ (extended linearly) is a
symmetrising form on KlY(d,l,n ). If λ = (λ(0),..., λ(d−1))∈P (d,l,n ), then the Schur element of Vλ
with respect to τ is
sλ =dnsλ(0)sλ(1)...s λ(d−1), (6.22)
where sλ(i) is the Schur element of the Ariki–Koike algebra H(l,|λ(i)|) corresponding to λ(i) for all
i = 0, 1,...,d − 1 (we take s∅ := 1).
A simple formula for the calculation of the Schur elements of Ariki–Koike algebras is given by Theorem
4.3.
Remark 6.12 The map τ is known to be a symmetrising form on Y( d,l,n ) (deﬁned overRl) in cases
d = 1 [MalMat] and l = 1 [ChPdA1]. In these cases, τ is called the canonical symmetrising form on
Y(d,l,n ).
Remark 6.13 Equation (6.22) hints towards an isomorphism between the cyclotomic Yokonuma–Hecke
algebra Y(d,l,n ) and a direct sum of matrix algebras over tensor products of Ariki–Koike algebras; this
isomorphism was recently described by Poulain d’Andecy in [PdA] and by Rostam in [Ros].
