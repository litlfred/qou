---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-046-75-the-relative-case
section_title: "The relative case"
section_number: 7.5
pages: 57-62
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
from Pn
A to projective bundles PV∨ on an arbitrary base scheme X, as in Example 7.5. We
assume that bothX andV are acted on by a torusT , and that we have a decomposition:
(7.13) OX∼=
[⨁
x∈XT
Px, a certain differential
]
∈Db(CohT (X))
58 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
where the indexing set goes over the ﬁxed points of X. We assume that the above is semi-
orthogonal, in the sense that Hom(Px,Py) = 0 wheneverx > ywith respect to some total
order. We wish to upgrade the decomposition (7.13) to the projective bundle PV∨.
Proposition 7.17. Letn+1 = rankV. There exist objectsPx
i for alli∈{ 0,...,n} andx∈XT ,
such that we have a semi-orthogonal decomposition:
(7.14) OPV∨∼=
[0≤i≤n⨁
x∈XT
Pi
x, a certain differential
]
∈Db(CohT (PV∨))
whenever the homological subtorus C∗⊂ T acts with distinct weights in the ﬁbersV|x for all
x∈XT . We have Hom(Pi
x,Pj
y) = 0 ifx>y or ifx =y andi<j .
The objectPi
x is precisely of the form (7.9) if one replaces O withPx, and λ0,...,λ n are
precisely the weights of the torusT in the ﬁberV|x.
8. L OCAL CHARTS AND FIXED POINTS OF FHilbn
8.1. Afﬁne charts for Hilbert schemes. Recall the action of C∗× C∗ on Hilbert schemes
given by rescaling theX andY matrices. The ﬁxed points of this action on the Hilbert scheme
are well-known. They are given by monomial ideals, which are indexed by partitions ofn:
HilbC∗×C∗
n ={Iλ}λ⊣n, I λ = (xλ1,xλ2y,... )⊂ C[x,y ]
Haiman described a set of afﬁne charts on the Hilbert scheme, each of which isC∗×C∗ invariant
and contains a single ﬁxed point:
(8.1) Hilbn =
⋃
λ⊣n
˚Hilbλ
where:
(8.2) ˚Hilbλ =
{
I such that{xayb}(a,b)∈λ is a basis of C[x,y ]/I
}
Here and throughout this paper, we identify a partition with its Young diagram, which is the set
of 1× 1 boxes in the ﬁrst quadrant of the plane with coordinates (a,b )∈ N0× N0,b<λ a:
For example, the above Young diagram corresponds to the partition λ = (4, 3, 1). It would be
very nice to have a clear description of the algebra of functions on each afﬁne chart (8.1), but
this is not at all easy. Instead, Haiman’s construction gives us a set of generators:
{f1,...,f 2n}∈ mλ/m2
λ
where mλ∈ C[ ˚Hilbλ] denotes the maximal ideal of the ﬁxed pointIλ.
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 59
8.2. Afﬁne charts for ﬂag Hilbert schemes. The situation is somewhat better in the case of
ﬂag Hilbert schemes FHilbn(∗) for any∗∈{ C2, C, point}, where one has afﬁne coverings:
(8.3) FHilbn(∗) =
⋃
T⊣n
˚FHilbT (∗)
indexed by standard Young tableaux T of size n. Recall that a standard Young tableau is a
numbering of the boxes of a Young diagram of size n with the numbers 1,...,n such that the
numbers increase as we go up and right in the diagram. A covering (8.3) is called good if all
the charts are C∗× C∗ equivariant and it respects passage fromn + 1 ton:
where the chart corresponding to any T′ maps to the chart corresponding to T = T′\□n+1.
Here,□n+1 denotes the box labeled n + 1 inT , which must necessarily be an outer corner of
T and an inner corner ofT′. Restricting the sheaf of dg algebras FHilbdg
n (∗) to the afﬁne charts
(8.3) gives rise to dg algebras:
(8.4) ˚Adg
T (∗) = C
[
˚FHilb
dg
T (∗)
]
Conjecture 8.1. There exists a good covering whose coordinate rings (8.4) satisfy:
(8.5) ˚AT∪□(∗) =
˚AT (∗)[∗,f□1,f□2,... ]
(r■1,r■2,... )
where□1,□2,... denote the inner corners ofT different from□, and■1,■2,... denote the outer
corners of T (except for the outer corner labeled n in the case∗ = point ). The generators
denoted by∗ stand for the afﬁne coordinates{xn+1,yn+1},{xn+1},∅ when∗ = C2, C, point.
We do not know how to deﬁne the generators fk and the relations rk, but we know how to
predict their characters with respect to the C∗× C∗ action. Speciﬁcally, for a box□ = (a,b ) in
a Young diagram, we deﬁne its weight as:
(8.6) z□ =qatb
When■ is the box labeled by i in a Young tableauT , we will write z■ =zi for brevity. Then
we expect that the generators and relations of (8.5) have equivariant weights
(8.7) weight f■ = z■
z□
, weightr■ = z■
z□
where□ is the corner that is being added in (8.5). In the remainder of this Section, we will
establish a weaker version of Conjecture 8.1, by constructing afﬁneC∗× C∗ invariant open sets
that contain the ﬁxed points of FHilbn(∗), but are not required to cover it.
8.3. Deﬁning the charts. In this Section, we will deﬁne afﬁne charts on the ﬂag Hilbert
scheme which only satisfy Conjecture 8.1 on the local rings around the ﬁxed points. FHilbn
will henceforth refer to either of FHilbn(∗) for∗∈{ C2, C, point}.
60 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
Deﬁnition 8.2. For any point (X,Y,v )∈ FHilbn and standard Young tableauT , consider the
following algorithm to construct a basise1 =v,e 2,...,e n of Cn. Supposee1,...,e k−1 have been
constructed and thek-th box looks as in the following picture:
i
i′
k
Deﬁne the vectorek∈ Ker(Cn↠ Ck−1) by the following formula ifi>i ′:
(8.8) Xei =ek +
k−1∑
j=i
xj
iej
wherexj
i are coefﬁcients, and by the following formula ifi<i ′:
(8.9) Yei′ =ek +
k−1∑
j=i′
yj
i′ej
whereyj
i′ are coefﬁcients. If the process terminates after having constructed en, in a way such
thate1,...,e k form a basis of the quotient Cn↠ Ck for allk, then we set:
(X,Y,v )∈ FHilbT
In either (8.8) or (8.9), it is clear that the vector ek is unique, since the coefﬁcients xj
i oryj
i
are uniquely determined by the fact that ek vanishes in the quotient Cn↠ Ck−1. The fact that
such an ek exists at each step, and that the resulting collection of vectors forms a basis, is an
open condition and therefore:
FHilbT⊂ FHilbn
thus deﬁned is an open subscheme. It is also an afﬁne subscheme, simply because the basis
e1,...,e n is unique. We could therefore deﬁne FHilbT alternatively as the afﬁne space of matri-
cesX,Y of the form prescribed by (8.8) and (8.9) in a ﬁxed basis. It is also clear that the locus
FHilbT is C∗× C∗ invariant and that the only ﬁxed point it contains is:
IT =
{
Cn =
n⨁
i=1
C·ei with X·ei =ei→, Y·ei =ei↑, v=e1
}
In the above formula, for any boxi∈T we writei→ andi↑ for the boxes immediately right
and above□, respectively. If there is no box to the right or up of□, we naturally setei→ orei↑
equal to 0. The fact that the open sets of Deﬁnition 8.2 cover the whole ofFHilbn follows from
the following principle:
(8.10) any open torus invariant property which holds
near the ﬁxed points of FHilbn holds everywhere
This is because the set of points which do not enjoy said property is closed, torus invariant and
contains no ﬁxed points: any such set must be empty. One must be careful here, because the
argument is a priori only true for projective varieties, such as FHilbn(point). However, it also
applies to FHilbn(C) and FHilbn(C2) because the torus C∗× C∗ contracts the afﬁne directions
C and C2 to the origin.
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 61
8.4. The special coefﬁcients. Note that the coefﬁcients xi
i and yi
i in (8.8) and (8.9) are pre-
cisely the eigenvalues of the matrices (X,Y,v )∈ FHilbn. If we are in the case ∗ = C or
∗ = point, then we must setyi
i = 0 orxi
i =yi
i = 0 in (8.8) and (8.9), respectively.
Deﬁnition 8.3. The coefﬁcientsxj
i andyj
i which appear in (8.8) and (8.9) will be calledspecial
coefﬁcients. We also apply this terminology to the case whenk is an outer corner of the Young
diagram ofT , but in that case (8.8) and (8.9) hold withek = 0.
Note that the number of special coefﬁcients corresponding to a standard Young tableauT is:
(8.11)
n∑
i=1
# (of inner corners of the Young diagram consisting of the boxes labeled1,...,i )
Conjecture 8.1 would suggest that the special coefﬁcients generate the dg ring of functions ˚AT
subject to a number of:
(8.12)
n∑
i=1
# (of outer corners of the Young diagram consisting of the boxes labeled1,...,i )
However, this is not true, because this would entail that all coefﬁcientsxj
i andyj
i could be writ-
ten as polynomials in the special coefﬁcients. We partially salvage this in the next Subsection,
when we will show that the previous sentence holds if we replace the word “polynomials” by
“rational functions”. In other words, some open subset of FHilbT can be described by (8.11)
generators and (8.12) relations.
Example 8.4. WhenT = (n) and∗ = C, only relations (8.8) come into play:
Xei =ei+1 +xiei
unlessi = 1, in which case we have:
Ye 1 =
n∑
j=2
yj
1ej
Therefore, the special coefﬁcients are{xi,yj
1}1≤i≤n
2≤j≤n. The number of these coefﬁcients is2n−1,
and it matches (8.11) minus 1, where the minus one stems from the fact thaty1
1 = 0 for∗ = C.
The non-special coefﬁcients are the yj
i with i > 1, but they can be inferred from the special
ones via the commutation relation [X,Y ] = 0, which in the case at hand reads:
(8.13) yj
i (xi−xj) =yj
i+1−yj−1
i
for all i < j. Note that (8.13) is precisely (1.28). We make the convention that yj
i = 0 for
j≤i. After solving foryj
i in terms of{xi,yj
1}, we obtain the inductive formulas for anyδ >0:
yi+δ
i =yδ+1
1 +
i−1∑
s=1
yi−s+δ+1
i−s (xi−s−xi−s+δ+1)
The above relation also holds when i +δ = n + 1, in which case the left hand side is 0. We
therefore obtain a relation among the special coefﬁcients{xi,yj
1} for allδ >0. There aren− 1
such relations, and their number matches (8.12) minus 1, where the minus one stems from the
fact thaty1
1 = 0 for∗ = C.
62 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
Example 8.5. WhenT = (1,..., 1) and∗ = C, only relations (8.9) come into play:
Yei =ei+1
unlessi = 1, in which case we have:
Xe1 =
n∑
j=1
xj
1ej
Therefore, the special coefﬁcients arexj
1 for allj. Note that the commutation relation [X,Y ] =
0 implies that:
xj−1
i =xj
i+1 ∀i<j
and therefore we conclude thatxj
i =uj−i+1 for some variablesu1,...,u n. Compare with (1.27).
