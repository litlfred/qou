---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-003-2-the-tensor-category-repst
section_title: "The tensor category Rep(St)"
section_number: 2
pages: 2-11
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
---
2.1. Motivation. Let d be a nonnegative integer, and let F be a ﬁeld of charac-
teristic zero. Let us consider the tensor category Rep( Sd;F ) of ﬁnite dimensional
representations overF of the symmetric group Sd. Note that we take S0 to be the
trivial group whose one element is the identity permutation of the empty set. Let
Vd denote the natural d-dimensional representation of Sd with basis {v1,...,v d},
so that Sd acts by permuting the basis elements ( V0 is taken to be 0). Setting
V⊗0
d =F for all d≥ 0, we have the following well-known result:
∗Notice that we do not require our tensor categories to be abelian, or even additive.
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 3
Proposition 2.1. Any irreducible representation ofSd is a direct summand ofV⊗n
d
for some nonnegative integer n.
As a consequence of Proposition 2.1, one way to understand Rep( Sd;F ) is to
study objects of the form V⊗n
d and morphisms between those objects. We will now
use set partitions to construct some such morphisms. Our notation will be similar
to that of [HR05].
By a partitionπ of a ﬁnite setS we mean a collectionπ1,...,π n of disjoint subsets
of S with S =⋃
iπi. The sets πi will be called parts of π. Given a partition π of
{1,...,n, 1′,...,m ′}, a partition diagram of π is any graph with vertices labelled
{1,...,n, 1′,...,m ′} whose connected components partition the vertices into the
parts of π. We will always draw partition diagrams using the following convention:
• Vertices 1,...,n (resp. 1′,...,m ′) are aligned horizontally and increasing
from left to right with i directly above i′.
• Edges lie entirely below the vertices labelled 1,...,n and above the vertices
labelled 1′,...,m ′.
We will abuse notation by writing π for both the partition and the partition dia-
gram.
Example 2.2. The graph
is a partition diagram for the partition {{1, 3, 2′, 3′},{2, 4},{1′}}. Note a partition
diagram representing this partition is not unique, but its connected components
are. 2
To each partition of the set {1,...,n, 1′,...,m ′} we will associate a linear map
V⊗n
d →V⊗m
d . Before doing so, we introduce some notation.
• Let Pn,m denote the set of all partitions of {1,...,n, 1′,...,m ′}, let Pn,0
denote the set of all partitions of {1,...,n }, let P0,m denote the set of
all partitions of {1′,...,m ′}, and let P0,0 denote the set consisting of the
empty partition. Finally, let FPn,m denote the F -vector space with basis
Pn,m.
• For nonnegative integers n and d, let [n,d ] denote the set of all functions
from{j| 1≤j≤n} to{j| 1≤j≤d}. In particular, [0 ,d ] ={∅} for all
d, and [n, 0] = ∅ for all n⁄= 0. Given i∈ [n,d ] and j∈{ j| 1≤ j≤ n},
write ij for the image of j under i.
• For i∈ [n,d ] and i′∈ [m,d ], the ( i, i′)-coloring of a partition π∈Pn,m is
obtained by coloring the vertices of π labelled j (resp. j′) by the integer ij
(resp. i′
j). Saying an ( i, i′)-coloring of π is good means vertices are colored
the same whenever they are in the same connected component of π. Saying
an (i, i′)-coloring of π is perfect means vertices are colored the same if and
only if they are in the same connected component of π.
• Forn⁄= 0 and i∈ [n,d ], setvi :=vi1⊗···⊗ vin∈V⊗n
d . Set v∅ := 1∈V⊗0
d
where∅ is the unique element of [0,d ].
We are now ready to associate partitions inPn,m with linear mapsV⊗n
d →V⊗m
d .
4 JONATHAN COMES AND VICTOR OSTRIK
Deﬁnition 2.3. For nonnegative integers n,m , and d, deﬁne the F -linear map
f :FPn,m→ HomSd(V⊗n
d ,V⊗m
d ) by setting
f(x)(vi) =
∑
i
′
∈[m,d]
f(x)i
i
′vi
′ (x∈FPn,m, i∈ [n,d ])
where
f(π)i
i
′ :=
{
1, if the ( i, i′)-coloring of π is good,
0, otherwise. (π∈Pn,m)
Indeed,f(x) commutes with the action of Sd which merely permutes the colors.
Example 2.4. (1) If ∅∈P0,0 denotes the empty partition, then f(∅) :F→F is
the identity map.
(2) Assume d> 0 and let π be the partition with partition diagram
Then f(π) :V⊗6
d →V⊗7
d is given by
f(π)(vi) =
{ ∑
1≤k,j≤d
vk⊗vj⊗vi4⊗vj⊗vi6⊗vi6⊗vi6, if i1 =i2 and i4 =i5,
0, otherwise.
for i∈ [6,d ].
(3) Assume d> 0 and let π be the partition with partition diagram
Then f(π) :F→V⊗5
d is given by
f(π)(1) =
∑
1≤i,j,k≤d
vi⊗vj⊗vi⊗vk⊗vj.
2
Next we wish to show that f is surjective. A proof of this fact when n =m can
be found in [HR05, Theorem 3.6]. Their proof extends to the case n⁄=m without
diﬃculty. For completeness we will give a modiﬁed version of their proof. Before
doing so, we must introduce a bit more notation.
• Let≤ be the partial order onPn,m deﬁned byπ≤µ whenever the partition
µ is coarser than the partitionπ (i.e. r ands are in the same part ofµ when-
ever they are in the same part ofπ for each pairr,s∈{ 1,...,n, 1′,...,m ′}).
• Deﬁne the basis{xπ| π∈Pn,m} of FPn,m inductively by setting
(2.1) xπ :=π−
∑
µ	π
xµ.
Example 2.5. (1) xπ =π when π is any partition consisting of one part.
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 5
(2) Let π∈ P4,3 be the partition with the partition diagram given in Example
2.2. Then xπ =π−µ1−µ2−µ3 + 2µ4 where
2
We are now ready to prove the following:
Theorem 2.6. For integersn,m,d ≥ 0, the map f :FPn,m→ HomSd(V⊗n
d ,V⊗m
d )
(see Deﬁnition 2.3) has the following properties:
(1) f is surjective.
(2) ker(f) = SpanF{xπ| π has more than d parts}.
In particular, f is an isomorphism of F -vector spaces whenever d≥n +m.
Proof. (compare with [HR05, proof of Theorem 3.6(a)]) If d = 0 then the theorem
is certainly true. Now assume d> 0. For g∈ HomSd(V⊗n
d ,V⊗m
d ) write
g(vi) :=
∑
i
′
∈[m,d]
gi
i
′vi
′ (i∈ [n,d ])
Since g commutes with the action of Sd, the matrix entries, gi
i
′, are constant on
the Sd-orbits of the matrix coordinates {(i, i′)}i∈[n,d],i
′
∈[m,d]. Each Sd-orbit of
{(i, i′)}i∈[n,d],i
′
∈[m,d] corresponds to a partition π∈ Pn,m as follows: ( i, i′) is in
the orbit corresponding to π if and only if the ( i, i′)-coloring of π is perfect. A
straightforward induction argument shows
(2.2)
f(xπ)i
i
′ =
{
1, if the ( i, i′)-coloring of π is perfect,
0, otherwise. (i∈ [n,d ], i′∈ [m,d ])
Thusg is an F -linear combination of the f(xπ)’s. This proves part (1).
To prove part (2) notice that for π∈Pn,m, there exist i∈ [n,d ] and i′∈ [m,d ]
such that the ( i, i′)-coloring of π is perfect if and only if π has at most d parts.
Hence, by (2.2), f(xπ) is the zero map if and only if π has more than d parts. Part
(2) now follows since{xπ| π∈Pn,m} is a basis for FPn,m. □
We conclude our investigation of morphisms of the form f(π) :V⊗n
d →V⊗m
d by
studying the composition of such morphisms. First we require the following:
Deﬁnition 2.7. Given partition diagramsπ∈Pn,m andµ∈Pm,l, construct a new
diagram µ⋆π by identifying the vertices 1′,...,m ′ of π with the vertices 1,...,m
6 JONATHAN COMES AND VICTOR OSTRIK
of µ and renaming them 1′′,...,m ′′ as illustrated below.
Now let𝓁(µ,π ) denote the number of connected components of µ⋆π whose vertices
are not among 1,...,n, 1′,...,l ′. Finally, let µ·π∈Pn,l be the partition obtained
by restrictingµ⋆π to{1,...,n, 1′,...,l ′} (i.e. r ands are in the same part of µ·π
if and only if r and s are in the same part of µ⋆π ).
We are now ready to state
Proposition 2.8. f(µ)f(π) =d𝓁(µ,π)f(µ·π) for any π∈Pn,m, µ∈Pm,l.
Before we give a proof of Proposition 2.8 let us consider an example.
Example 2.9. In this example we will verify Proposition 2.8 when
On the one hand,
Thus𝓁(µ,π ) = 2 and
Therefore we haved𝓁(µ,π)f(µ·π)(vi1⊗vi2⊗vi3⊗vi4) =d2δi1,i3vi2⊗vi2⊗vi2⊗vi4⊗vi4
where δi,j is the Kronecker delta function.
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 7
On the other hand,
f(µ)f(π)(vi) = f(µ)
(
δi1,i3
∑
1≤j,k,l≤d
vj⊗vi4⊗vj⊗vk⊗vl⊗vi2⊗vi2
)
=δi1,i3
∑
1≤j,k,l≤d
f(µ) (vj⊗vi4⊗vj⊗vk⊗vl⊗vi2⊗vi2)
=δi1,i3
∑
1≤j,k,l≤d
δj,k vi2⊗vi2⊗vi2⊗vi4⊗vi4
=δi1,i3
∑
1≤j,l≤d
vi2⊗vi2⊗vi2⊗vi4⊗vi4
=d2δi1,i3 vi2⊗vi2⊗vi2⊗vi4⊗vi4.
for any i∈ [4,d ], as desired. 2
Now to show Proposition 2.8 holds in general.
Proof of Proposition 2.8. Suppose π∈ Pn,m and µ∈ Pm,l for some integers
n,m,l ≥ 0. By Deﬁnition 2.3 the matrix coordinates of f(µ)f(π) :V⊗n
d →V⊗l
d are
given by
(2.3) ( f(µ)f(π))i
i
′ =
∑
i
′′
∈[m,d]
f(µ)i
′′
i
′f(π)i
i
′′.
Hence (f(µ)f(π))i
i
′ is the number of i′′∈ [m,d ] such that the ( i, i′′)-coloring of
π and the ( i′′, i′)-coloring of µ are simultaneously good. These are exactly the
i′′∈ [m,d ] such that coloring the vertices j,j′,j′′ of µ⋆π with integers ij,i′
j,i′′
j
respectively, gives a good coloring ofµ⋆π . Any good coloring of µ⋆π gives rise to a
good coloring ofµ·π. Clearly any good coloring of µ·π arises in this way. Moreover,
two good colorings ofµ⋆π give the same good coloring of µ·π if and only if the two
colorings ofµ⋆π diﬀer only at connected components whose vertices are not among
1,...,n, 1′,...,l ′. Since there are d choices of color for each component, we see the
number of i′′∈ [m,d ] such that the ( i, i′′)-coloring of π and the ( i′′, i′)-coloring of
µ are simultaneously good is d𝓁(µ,π)f(µ·π)i
i
′. The result follows. 2
Remark 2.10. From Proposition 2.8 the structure constants of the composition
f(µ)f(π) are polynomial in the integer d. We will exploit this fact in section
2.2 when we deﬁne the category Re p(St;F ) which “interpolates” the category
Rep(St;F ) for nonnegative integer t, but is deﬁned for arbitrary t∈F .
2.2. Deﬁnition of Rep(St;F ). In this section we deﬁne Deligne’s tensor category
Rep(St;F ) for arbitrary t∈ F following [Del07, §8] (so our deﬁnition is diﬀerent
from the one given in [Del07, §2]). To construct Re p(St;F ) we will ﬁrst use par-
titions to construct the smaller category Re p0(St;F ). We then obtain Re p(St;F )
from Rep0(St;F ) using the process of Karoubiﬁcation.
As in the previous section, assumed is a nonnegative integer and thatF is a ﬁeld
of characteristic zero. Let Rep 0(Sd;F ) denote the full subcategory of Rep( Sd;F )
whose objects are of the formV⊗n
d forn≥ 0. Clearly the objects in Rep 0(Sd;F ) are
indexed by nonnegative integers, and by Theorem 2.6 the morphisms in Rep0(Sd;F )
are given (albeit not uniquely) by F -linear combinations of maps f(π) indexed by
set partitions. Moreover, the structure constants of compositions of the f(π)’s are
polynomials in d (see Proposition 2.8). Using this data, we now deﬁne a tensor
8 JONATHAN COMES AND VICTOR OSTRIK
category similar to Rep 0(Sd;F ) replacing the integer d with an arbitrary element
of F .
Let t∈F .
Deﬁnition 2.11. The category Rep0(St;F ) has
Objects: [n] for each n∈Z≥0.
Morphisms: Hom Rep0(St;F )([n], [m]) :=FPn,m.
Composition: FPm,l×FPn,m→FPn,l is deﬁned to be the bilinear map satisfying
µ◦π =t𝓁(µ,π)µ·π for each π∈Pn,m, µ∈Pm,l.
To see that composition is associative, it is enough to showν◦(µ◦π) = (ν◦µ)◦π
for all π∈Pn,m, µ∈Pm,l, ν∈Pl,k. To do so, consider the partition
Notice thatν·(µ·π), (ν·µ)·π∈Pn,k are both obtained by restricting the partition
ν ⋆ µ ⋆ πto the set {1,...,n, 1′,...,k ′}. Furthermore, 𝓁(µ,π ) + 𝓁(ν,µ·π) and
𝓁(ν,µ ) +𝓁(ν·µ,π ) are both the number of connected components of ν⋆µ⋆π whose
vertices are not among{1,...,n, 1′,...,k ′}. Hence composition is associative.
One can easily check that the partition in Pn,n whose parts are all of the form
{j,j′} is the identity morphism idn : [n]→ [n].
Example 2.12. The identity morphism id 7 : [7]→ [7] is given by
2
Before giving Re p0(St;F ) the structure of a tensor category, we pause to give
the following deﬁnition which will play an important role in later sections.
Deﬁnition 2.13. (compare with [Mar91], [Mar94]) The partition algebra FPn(t)
is deﬁned to be the endomorphism algebra End Rep0(St;F )([n]).
Remark 2.14. We identify each element of the symmetric group Sn with a par-
tition in Pn,n as follows: σ↔{{ i,σ (i)′}| 1≤ i≤ n}. This identiﬁcation extends
linearly to an inclusion of algebras FSn ↪→FPn(t) for each t∈F .
Now to deﬁne tensor products. While reading the following deﬁnitions, the reader
may ﬁnd it helpful to keep in mind the analogy studied in section 2.1 between
the objects [ n] (resp. morphisms π) in Re p0(St;F ) and the objects V⊗n
d (resp.
morphisms f(π)) in Rep(Sd;F ).
Deﬁnition 2.15. For objects [n], [m] in Rep0(St;F ) set [n]⊗ [m] := [n +m]. For
morphisms we let ⊗ :FPn1,m1×FPn2,m2→FPn1+n2,m1+m2 be the bilinear map
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 9
such that
for all π∈Pn1,m1, µ∈Pn2,m2.
Example 2.16. Suppose
Then
2
Next we wish to show that Re p0(St;F ) is a tensor category with the following
choices.
• (associativity) αn,m,l : ([n]⊗ [m])⊗ [l]→ [n]⊗ ([m]⊗ [l]) is the identity
morphism idn+m+l.
• (commutativity)βn,m : [n]⊗ [m]→ [m]⊗ [n] is the partition in Pn+m,n+m
whose parts are of the form{j, (m +j)′} or{n +j,j′} as illustrated below.
• (unit) Set 1 := [0]. Both unit morphisms [0]⊗ [n]→ [n] and [n]⊗ [0]→ [n]
are the identity morphism idn.
• (duals) Set [ n]∨ := [n] with the morphism evn : [n]∨⊗ [n] → 1 (resp.
coevn : 1→ [n]⊗ [n]∨) given by the partition in P2n,0 (resp. P0,2n) whose
parts are of the form {j,n +j} (resp.{j′, (n +j)′}) as illustrated below.
10 JONATHAN COMES AND VICTOR OSTRIK
The triangle and pentagon axioms are easily satisﬁed, as all morphisms in both
diagrams are identity morphisms. The following diagrams illustrate the hexagon
axiom.
The diagrams below illustrate that the choice of dual objects as well as the evalu-
ation and coevaluation morphisms make Re p0(St;F ) into a rigid category.
Finally, End Rep0(St;F )(1) = F as P0,0 contains only the empty partition. Thus
Rep0(St;F ) is a tensor category.
Remark 2.17. Ford∈Z≥0, the connection between Rep0(Sd;F ) and Rep0(Sd;F )
can be made more precise as follows. The functor F0 : Rep0(Sd;F )→ Rep0(Sd;F )
given on objects by [n]↦→V⊗n
d , and on morphisms as the F -linear map π↦→f(π)
is a tensor functor. F0 is certainly surjective on objects. Moreover, by Theorem
2.6(1),F0 is surjective on morphisms. However, by Theorem 2.6(2), F0 does not
give an equivalence of categories.
Now we are ready to use the process of Karoubiﬁcation to deﬁne Deligne’s cat-
egory. For more on this process see [Del07, 1.7-8]. Informally, Re p(St;F ) is the
category obtained from Re p0(St;F ) by adding formal direct sums and images of
idempotents. Let us be more precise:
Deﬁnition 2.18. Let Rep1(St;F ) denote the additive envelope of Rep0(St;F ) so
that Rep1(St;F ) has
Objects: ﬁnite tuples of objects in Re p0(St;F ) written as A1⊕···⊕ Ak for
objects A1,...,A k in Rep0(St;F ). We also include the empty tuple which is the
zero object in Re p1(St;F ).
Morphisms: Hom Rep1(St;F )
(⨁k
i=1Ai,⨁l
i=1Bi
)
is the set of all l×k-matrices
whose (i,j )-entry is a morphism Aj→Bi in Rep0(St;F ).
Composition: given by matrix multiplication along with the induced composition
from Rep0(St;F ).
Deﬁnition 2.19. Let Rep(St;F ) denote the Karoubian envelope† of Rep1(St;F )
which has
†Some authors, including Deligne, refer to Karoubian envelopes as pseudo-abelian completions.
ON BLOCKS OF DELIGNE’S CATEGORY Re p(St). 11
Objects: pairs (A,e ) whereA is an object in Rep1(St;F ) ande∈ EndRep1(St;F )(A)
is an idempotent.
Morphisms: Hom Rep(St;F ) ((A,e ), (B,f )) :=f HomRep1(St;F )(A,B )e.
Composition: induced from composition in Re p1(St;F ).
The following properties of Rep(St;F ) follow from general theory of additive and
Karoubian envelopes.
Proposition 2.20. (1) The obvious tensor product on objects and morphisms, as
well as the obvious associativity, commutativity, unit, and dual constraints make
Rep(St;F ) a tensor category.
(2) Given a nonnegative integer n and a nonzero idempotent e∈ FPn(t), the
object ([n],e ) in Rep(St;F ) is indecomposable if and only if e is primitive‡. More-
over, every indecomposable object in Rep(St;F ) is isomorphic to one of the form
([n],e ). Finally, given two primitive idempotents e,e′∈FPn(t), the objects ([n],e )
and ([n],e′) are isomorphic if and only if e and e′ are conjugate§ in FPn(t).
(3) (Krull-Schmidt property) Every object in Rep(St;F ) can be decomposed as
a ﬁnite direct sum of indecomposable objects. Moreover, if A =L1⊕···⊕ Lr and
A =L′
1⊕···⊕ L′
s are two decomposition ofA into indecomposables, thenr =s and
there is a permutation σ∈Sr with Li∼=L′
σ(i) for all 1≤i≤r.
Remark 2.21. Informally, studying the category Re p0(St;F ) is a way to simul-
taneously study the partition algebras FPn(t) for all n≥ 0 (see Deﬁnition 2.13).
In this line of thinking, studying Re p(St;F ) is a way to simultaneously study all
ﬁnitely generated projective right FPn(t)-modules for all n≥ 0.
