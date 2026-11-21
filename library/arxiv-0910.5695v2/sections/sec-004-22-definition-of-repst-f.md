---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-004-22-definition-of-repst-f
section_title: "Definition of Rep(St; F)"
section_number: 2.2
pages: 7-11
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
Rep(St; F) for arbitrary t ∈F following [Del07, §8] (so our deﬁnition is diﬀerent
from the one given in [Del07, §2]). To construct Rep(St; F) we will ﬁrst use par-
titions to construct the smaller category Rep0(St; F). We then obtain Rep(St; F)
from Rep0(St; F) using the process of Karoubiﬁcation.
As in the previous section, assume d is a nonnegative integer and that F is a ﬁeld
of characteristic zero. Let Rep0(Sd; F) denote the full subcategory of Rep(Sd; F)
whose objects are of the form V ⊗n
d
for n ≥0. Clearly the objects in Rep0(Sd; F) are
indexed by nonnegative integers, and by Theorem 2.6 the morphisms in Rep0(Sd; F)
are given (albeit not uniquely) by F-linear combinations of maps f(π) indexed by
set partitions. Moreover, the structure constants of compositions of the f(π)’s are
polynomials in d (see Proposition 2.8). Using this data, we now deﬁne a tensor
8
JONATHAN COMES AND VICTOR OSTRIK
category similar to Rep0(Sd; F) replacing the integer d with an arbitrary element
of F.
Let t ∈F.
Deﬁnition 2.11. The category Rep0(St; F) has
Objects: [n] for each n ∈Z≥0.
Morphisms: HomRep0(St;F )([n], [m]) := FPn,m.
Composition: FPm,l×FPn,m →FPn,l is deﬁned to be the bilinear map satisfying
µ ◦π = tℓ(µ,π)µ · π for each π ∈Pn,m, µ ∈Pm,l.
To see that composition is associative, it is enough to show ν ◦(µ◦π) = (ν ◦µ)◦π
for all π ∈Pn,m, µ ∈Pm,l, ν ∈Pl,k. To do so, consider the partition
Notice that ν ·(µ·π), (ν ·µ)·π ∈Pn,k are both obtained by restricting the partition
ν ⋆µ ⋆π to the set {1, . . . , n, 1′, . . . , k′}.
Furthermore, ℓ(µ, π) + ℓ(ν, µ · π) and
ℓ(ν, µ) + ℓ(ν · µ, π) are both the number of connected components of ν ⋆µ ⋆π whose
vertices are not among {1, . . . , n, 1′, . . . , k′}. Hence composition is associative.
One can easily check that the partition in Pn,n whose parts are all of the form
{j, j′} is the identity morphism idn : [n] →[n].
Example 2.12. The identity morphism id7 : [7] →[7] is given by
2
Before giving Rep0(St; F) the structure of a tensor category, we pause to give
the following deﬁnition which will play an important role in later sections.
Deﬁnition 2.13. (compare with [Mar91], [Mar94]) The partition algebra FPn(t)
is deﬁned to be the endomorphism algebra EndRep0(St;F )([n]).
Remark 2.14. We identify each element of the symmetric group Sn with a par-
tition in Pn,n as follows: σ ↔{{i, σ(i)′} | 1 ≤i ≤n}. This identiﬁcation extends
linearly to an inclusion of algebras FSn ,→FPn(t) for each t ∈F.
Now to deﬁne tensor products. While reading the following deﬁnitions, the reader
may ﬁnd it helpful to keep in mind the analogy studied in section 2.1 between
the objects [n] (resp. morphisms π) in Rep0(St; F) and the objects V ⊗n
d
(resp.
morphisms f(π)) in Rep(Sd; F).
Deﬁnition 2.15. For objects [n], [m] in Rep0(St; F) set [n] ⊗[m] := [n + m]. For
morphisms we let ⊗: FPn1,m1 × FPn2,m2 →FPn1+n2,m1+m2 be the bilinear map
ON BLOCKS OF DELIGNE’S CATEGORY Rep(St).
9
such that
for all π ∈Pn1,m1, µ ∈Pn2,m2.
Example 2.16. Suppose
Then
2
Next we wish to show that Rep0(St; F) is a tensor category with the following
choices.
• (associativity) αn,m,l : ([n] ⊗[m]) ⊗[l] →[n] ⊗([m] ⊗[l]) is the identity
morphism idn+m+l.
• (commutativity) βn,m : [n] ⊗[m] →[m] ⊗[n] is the partition in Pn+m,n+m
whose parts are of the form {j, (m + j)′} or {n + j, j′} as illustrated below.
• (unit) Set 1 := [0]. Both unit morphisms [0] ⊗[n] →[n] and [n] ⊗[0] →[n]
are the identity morphism idn.
• (duals) Set [n]∨:= [n] with the morphism evn : [n]∨⊗[n] →1 (resp.
coevn : 1 →[n] ⊗[n]∨) given by the partition in P2n,0 (resp. P0,2n) whose
parts are of the form {j, n + j} (resp. {j′, (n + j)′}) as illustrated below.
10
JONATHAN COMES AND VICTOR OSTRIK
The triangle and pentagon axioms are easily satisﬁed, as all morphisms in both
diagrams are identity morphisms. The following diagrams illustrate the hexagon
axiom.
The diagrams below illustrate that the choice of dual objects as well as the evalu-
ation and coevaluation morphisms make Rep0(St; F) into a rigid category.
Finally, EndRep0(St;F )(1) = F as P0,0 contains only the empty partition.
Thus
Rep0(St; F) is a tensor category.
Remark 2.17. For d ∈Z≥0, the connection between Rep0(Sd; F) and Rep0(Sd; F)
can be made more precise as follows. The functor F0 : Rep0(Sd; F) →Rep0(Sd; F)
given on objects by [n] 7→V ⊗n
d
, and on morphisms as the F-linear map π 7→f(π)
is a tensor functor. F0 is certainly surjective on objects. Moreover, by Theorem
2.6(1), F0 is surjective on morphisms. However, by Theorem 2.6(2), F0 does not
give an equivalence of categories.
Now we are ready to use the process of Karoubiﬁcation to deﬁne Deligne’s cat-
egory. For more on this process see [Del07, 1.7-8]. Informally, Rep(St; F) is the
category obtained from Rep0(St; F) by adding formal direct sums and images of
idempotents. Let us be more precise:
Deﬁnition 2.18. Let Rep1(St; F) denote the additive envelope of Rep0(St; F) so
that Rep1(St; F) has
Objects: ﬁnite tuples of objects in Rep0(St; F) written as A1 ⊕· · · ⊕Ak for
objects A1, . . . , Ak in Rep0(St; F). We also include the empty tuple which is the
zero object in Rep1(St; F).
Morphisms: HomRep1(St;F )
Lk
i=1 Ai, Ll
i=1 Bi

is the set of all l × k-matrices
whose (i, j)-entry is a morphism Aj →Bi in Rep0(St; F).
Composition: given by matrix multiplication along with the induced composition
from Rep0(St; F).
Deﬁnition 2.19. Let Rep(St; F) denote the Karoubian envelope† of Rep1(St; F)
which has
†Some authors, including Deligne, refer to Karoubian envelopes as pseudo-abelian completions.
ON BLOCKS OF DELIGNE’S CATEGORY Rep(St).
11
Objects: pairs (A, e) where A is an object in Rep1(St; F) and e ∈EndRep1(St;F )(A)
is an idempotent.
Morphisms: HomRep(St;F ) ((A, e), (B, f)) := f HomRep1(St;F )(A, B)e.
Composition: induced from composition in Rep1(St; F).
The following properties of Rep(St; F) follow from general theory of additive and
Karoubian envelopes.
Proposition 2.20. (1) The obvious tensor product on objects and morphisms, as
well as the obvious associativity, commutativity, unit, and dual constraints make
Rep(St; F) a tensor category.
(2) Given a nonnegative integer n and a nonzero idempotent e ∈FPn(t), the
object ([n], e) in Rep(St; F) is indecomposable if and only if e is primitive‡. More-
over, every indecomposable object in Rep(St; F) is isomorphic to one of the form
([n], e). Finally, given two primitive idempotents e, e′ ∈FPn(t), the objects ([n], e)
and ([n], e′) are isomorphic if and only if e and e′ are conjugate§ in FPn(t).
(3) (Krull-Schmidt property) Every object in Rep(St; F) can be decomposed as
a ﬁnite direct sum of indecomposable objects. Moreover, if A = L1 ⊕· · · ⊕Lr and
A = L′
1 ⊕· · ·⊕L′
s are two decomposition of A into indecomposables, then r = s and
there is a permutation σ ∈Sr with Li ∼= L′
σ(i) for all 1 ≤i ≤r.
Remark 2.21. Informally, studying the category Rep0(St; F) is a way to simul-
taneously study the partition algebras FPn(t) for all n ≥0 (see Deﬁnition 2.13).
In this line of thinking, studying Rep(St; F) is a way to simultaneously study all
ﬁnitely generated projective right FPn(t)-modules for all n ≥0.
