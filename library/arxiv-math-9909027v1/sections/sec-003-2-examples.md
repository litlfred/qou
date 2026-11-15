---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I"
section_id: sec-003-2-examples
section_title: "Examples"
section_number: 2
pages: 27-54
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
toc_source: inferred
doc_brief: "Planar Algebras, I — We introduce a notion of planar algebra, the simplest example of which is a vector space of tensors, closed under planar contractions."
---
Example 2.1: Temperley-Lieb algebra. If δ1 and δ2 are two non-zero
scalars, one deﬁnes TL(n, δ1, δ2) as being the subspace of Pn(∅) spanned by
27
the tangles with no closed loops. Deﬁning multiplication on TL(n, δ1, δ2)
by multiplication as in Pn(∅) except that one multiplies by a factor δ1 for
each loop
and δ2 for each loop
, then discarding the loop. Clearly the
map from Pn(∅) to TL(n, δ1, δ2) given by multiplying by δ1’s or δ2’s then
discarding loops, gives a Φ exhibiting TL(n, δ1, δ2) as a planar algebra. For
general values of δ1 and δ2, TL(n) is not non-degenerate. An extreme case
is δ1 = δ2 = 1 where Z(c(T1 −T2)) = 0 for all relevant tangles c, T1, T2. In
fact the structure of the algebras TL(n, δ1, δ2) (forgetting Φ), depends only
on δ1δ2. To see this, show as in [GHJ] that TL(n, δ1, δ2) is presented as an
algebra by Ei, i ≤1, . . . , n−1 with E2
i = δ1Ei for i odd, E2
i = δ2Ei for i even,
and EiEi±1Ei = Ei and EiEj = EjEi for |i −j| ≥2. Then setting ei = 1
δ1Ei
(i odd), ei =
1
δ2Ei (i even), the relations become e2
i = ei, eiei±1ei =
1
δ1δ2ei,
eiej = ejei for |i −j| ≥2. If δ1 = δ2 = δ, we write TL(δ1, δ2) = TL(δ).
One may also obtain TL via invariants, as a planar algebra on one box,
in several ways.
(i) The chromatic polynomial. A planar network N on L = L2 with
#(L2)=1 determines a planar graph G(N ) by choosing as vertices the pos-
itively oriented regions of R2\N and replacing the 2-boxes by edges joining
the corresponding vertices (thus
⇝•—•). Fix Q ∈C −{0} and let
Z(N ) = (chromatic polynomial of G(N ) as evaluated at Q) ×f, where f =1
if the outside region is negatively oriented and f = Q−1 if the outside re-
gion is positively oriented.
To see that PZ is Temperley-Lieb, deﬁne the
map α : P(L) →TL(1, Q) by α(
) =
−
(extended by multilinearity
to P(L)). It is easy to check that α makes TL(1, Q) a planar algebra on
L and the corresponding partition function is Z as above. Thus PZ is the
non-degenerate quotient of TL(1, Q).
(ii) The knot polynomial of [J2]. Given a planar network N on one 2-
box, replace the 2-box
by
to get an unoriented link diagram. Deﬁne
Z(N ) to be the Kauﬀman bracket ([Ka1]) of this diagram. Sending
to
A
+ A−1
we see that this deﬁnes a map from P(L) to TL(−A2 −A2)
28
with the Temperley-Lieb partition function.
Both (i) and (ii) are generalized by the dichromatic polynomial (see [Tut]).
Example 2.2: Planar algebras on 1-boxes. If A is an associative
algebra with identity and a trace functional tr: A →K, tr(ab) = tr(ba),
tr(1) = δ, we may form a kind of “wreath product” of A with TL(n, δ). In
terms of generators and relations, we put L = L1 = A and
a, b ∈A
−
λa + b
λ ∈K
a + b
λ
b
a
−ba
R =
∪
a, b ∈A
a
1
−
∪
∪
−tr(a)
One may give a direct construction of this planar algebra using a basis as
follows. Choose a basis {ai | i ∈I} of A with aiaj = P ck
ijak for scalars
ck
ij. (Assume 1 ∈{ai} for convenience.) Let P A
n be the vector space whose
basis is the set of all Temperley-Lieb basis n-tangles together with a function
from the strings of the tangle to {ai}. Multiply these basis elements as for
Temperley-Lieb except that, when a string labelled ai is joined with one
labelled aj, the result gives a sum over j of ck
ij times the same underlying
Temperley-Lieb tangle with the joined string labelled ak. In the resulting
sum of at most #(I)n terms, if a closed loop is labelled ak, remove it and
multiply by a factor of tr(ak). This gives an associative algebra structure
on each P A
n . It becomes a planar algebra on A in the obvious way with Φ
mapping
a
to a linear combination of strings labelled aj, the coeﬃcients
being those of a in the basis {ai}.
If a string in P(A) has no 1-box on it, it is sent to the same string labelled
with 1. One may check that the kernel of Φ is precisely the ideal generated
by our relations R, so P A = P(A)/J (R).
Observe how P A
n is a sum, over Temperley-Lieb basis tangles, of tensor
powers of A.
When n = 2 this gives an associative algebra structure on
A ⊗A ⊕A ⊗A. Explicitly, write (a ⊗b) ⊕0 as a ⊗b and 0 ⊕(x ⊗y) as x ⊗y.
Multiplication is then determined by the rules:
(a1 ⊗b1)(a2 ⊗b2)
= a1a2 ⊗b2b1
(x1 ⊗y1)(x2 ⊗y2)
= tr(y1x2)x1 ⊗y2
29
(a ⊗b)(x ⊗y)
= 0 ⊕axb ⊗y
(x ⊗y)(a ⊗b)
= 0 ⊕x ⊗bya
The planar algebra P A may be degenerate, even when tr on A is non-
degenerate and δ is such that TL(δ) is non-degenerate. We will give more
details on the structure of P A in §3.1.
Example 2.3: The Fuss-Catalan algebras (see [BJ2]). If a1, a2, . . . , ak ∈
K −{0}, FC(n, a1, . . . , ak) is the algebra having as basis the Temperley-Lieb
diagrams in TL(nk) for which, for each p = 1, 2, . . ., k, the set of all boundary
points (counting from the left) indexed by {jk+(−1)jp+(sin2 jπ
2 )(k+j) | j =
01, 2, . . .(n −1)} are connected among themselves. Assign a colour to each
p = 1, 2, . . ., k so we think of the Temperley-Lieb strings as being coloured.
Then multiplication preserves colours so that closed loops will have colours.
Removing a closed loop coloured m contributes a multiplicative factor am.
To see that FC(n, a1, . . . , ak) is a planar algebra, begin with the case k = 2.
We claim FC(n, a, b) is planar on one 2-box. We draw the box symbolically
as
This shows in fact how to deﬁne the corresponding Φ : Pn →FC(n, a, b):
double all the strings and replace all the 2-boxes according to the diagram.
Thus for instance the tangle N below (with boxes shrunk to points, there
being only one 2-box),
30
is sent to ®(N) below
ab ba _ab ab bbab

ab ba ab ab baab

It is clear that ® defines an algebra homomorphism and surjectivity follows
from [BJ2]. That ker ® is annular invariant is straightforward. The general
case of FC(n,a1,...,a,) is similar. One considers the k — 1 2-boxes drawn
symbolically as

WW AMA MAN

\ [\

FPIP\W\\ TIPE AMA TPTP AM

One proceeds as above, replacing the single strings in an N by k coloured
strings. Surjectivity follows from [La].

Note that these planar algebras give invariants of systems of immersed
curves with generic singularities, and/or planar graphs. The most general
such invariant may be obtained by introducing a single 2-box which is a linear
combination of the k —1  2-boxes described above. This will generalize the
dichromatic polynomial.

Example 2.4: The BMW algebra. Let L = Lz = {R,Q} and define
the planar algebra BMW on L by the relations

xy
Q

y &¥y¥ ey Ky IR
() |Fl=[4], [@]=[°], N= N- iy
YX 4X XX FX [Q} Tl [R
4 X

31
(ii)
=
=
R
Q
Q
R
(iii)
=
,
Q
Q
R
=
a−1
=
a
=
R
, (a ∈C −{0})
(iv)
=
Q
Q
Q
R
R
R
+
+
(v)
R
Q
=
x
Note that we could use relation (v) to express BMW using only the
one label R, but the relations would then be more complicated.
At this
stage BMW could be zero or inﬁnite dimensional, but we may deﬁne a
homomorphism from BMW to the algebra BMW of [BiW],[Mu] by sending
R
to
and Q
to
. This homomorphism is obviously surjective and
one may use the dimension count of [BiW] to show also that dim BMW(n) ≤
1.3.5. . . .(2n−1) so that BMW ∼= BMW as algebras. Thus BMW is planar.
It is also connected and the invariant of planar networks is the Kauﬀman
regular-isotopy two-variable polynomial of [Ka2].
Remark. Had we presented BMW on the single 2-box R, the Reide-
32
meister type III move (number (iv) above) would have been
R
=
R
R
R
R
R
+
pictures with
at most two
R ’s
This leads us to consider the general planar algebra Bn with the following
three conditions:
(1) Bn is planar on one 2-box.
(2) dim B2 = 3.
(3) dim B3 ≤15.
If one lists 16 tangles in B3 then generically any one of them will have to be
a linear combination of the other 15. Looking at the 15th and 16th tangles
in a listing according to the number of 2-boxes occuring in the tangle, we will
generically obtain a type III Reidemeister move, or Yang-Baxter equation,
modulo terms with less 2-boxes,as above. It is not hard to show that these
conditions force dim Bn ≤1.3.5 · . . . · (2n −1) since there are necessarily
Reidemeister-like moves of types I and II. Note that FC(n, a, b) satisﬁes these
conditions as well as BMW! For C∗-planar algebras, we have shown with
Bisch ([BJ1]) that the only B’s with (1) and (2) as above, and dim B3 ≤12
are the Fuss-Catalan algebras (with one exception, when dim B3 = 9).
Example 2.5: a Hecke-algebra related example. The homfly poly-
nomial of [F+] is highly sensitive to the orientation of a link and we may not
proceed to use it to deﬁne a planar algebra as in Example 2.4. In particular,
a crossing in the homfly theory is necessarily oriented as
. Thus it does
not yield a 2-box in our planar algebra context. Nevertheless it is possible to
use the homfly skein theory to deﬁne a planar algebra. We let P H
k be the
33
usual homfly skein algebra of linear combinations of (3-dimensional) iso-
topy classes of oriented tangles in the product of the k-box with an interval,
with orientations alternating out-in, modulo the homfly skein relation
t
−t−1
= x
where t̸ = 0 and x are scalars. Projected onto the k-box,
such a tangle could look as in Figure 2.5.1,
Figure 2.5.1
If we take the labeling set Lk = P H
k , then P H is a general planar al-
gebra since planar isotopy of projections implies 3-dimensional isotopy (in-
variance under the annular category is easy). Standard homfly arguments
show dim (P H
k ) ≤k! and a specialization could be used to obtain equality.
Thus the algebra is planar and the invariant is clearly the homfly polyno-
mial of the oriented link diagram given by a labeled network in P H
0 . If we
used this invariant to deﬁne the algebra as in §1, we would only obtain the
same algebra for generic values of t and x. Note that P H
k is not isomorphic
to the Hecke algebra for k ≥4, e.g. P H
4
has an irreducible 4-dimensional
representation. In fact P H
k
is, for generic (t, x) and large n, isomorphic to
EndSU(n) (V ⊗¯V ⊗V ⊗¯V . . .)
|
{z
}
k vector spaces
, where V = Cn, the obvious SU(n)-module.
This isomorphism is only an algebra isomorphism, not a planar algebra iso-
morphism.
It is clear that the labeling set for P H could be reduced to a set of k!
isotopy classes of tangles for P H
k . But in fact a single 3-label suﬃces as we
now show
Theorem 2.5.2 Any tangle in the knot-theoretic sense with alternating in
and out boundary orientations is isotopic to a tangle with a diagram where
34
all crossings occur in disjoint discs which contain the pattern
with some non-alternating choice of crossings.
Proof. We begin with a tangle without boundary, i.e. an oriented link
L. Choose a diagram for L and add a parallel double L′ of L to the left of L
and oppositely oriented, with crossings chosen so that
a) L′ is always under L
b) L′ itself is an unlink.
An example of the resulting diagram (for the Whitehead Link) is given in
Figure 2.5.3
Figure 2.5.3
Now join L to L′, component by component, by replacing
by
, at
some point well away from any crossings. Since L′ is an unlink below L, the
resulting link is isotopic to L. All the crossings in L ∪L′ occur in disjoint
35
discs containing the pattern
which can be isotoped to the pattern
containing two discs of the required form. Alternating patterns can
be avoided by keeping the top string on top in this isotopy.
For a tangle with boundary we make the doubling curve follow the bound-
ary, turning right just before it would hit it and right again as it nears the
point where the next string exits the tangle, as in Figure 2.5.4
boundary of tangle
Figure 2.5.4
Join the original tangle to L′ one string at a time and proceed as before.
□
Corollary 2.5.5 The planar algebra P H is generated by the single 3-box
.
Proof. The homfly relations can be used to go between the various
possible choices of crossings in the 3-box of Theorem 2.5.2.
□
This corollary was ﬁrst proved by W. B. R. Lickorish using an argument
adapted to the homfly skein. His argument is much more eﬃcient in pro-
ducing a skein element involving only the above 3-box. The tangles may be
chosen alternating in Theorem 2.5.2.
Remarks. 1) Another way of stating Theorem 2.5.2 is to say that any
tangle can be projected with only simple tiple point singularities. One may
36
ask if there are a set of “Reidemeister moves” for such non-generic projec-
tions.
2) A related question would be to ﬁnd a presentation of P H on the above
3-box.
Discussion 2.5.6 In the remark of Example 2.4 we introduced relations
on the planar algebra generated by a 2-box, which force ﬁnite dimensionality
of all the Pn’s. One should explore the possibilities for the planar algebra
generated by a single 3-box. The dimension restrictions analogous to the
1,3 ≤15 values of Example 2.4 are 1,2,6,≤24 and we conjecture, somewhat
weakly, the following
Conjecture 2.5.7 Let (P, Φ) be a planar algebra with labelling set L = L3,
#(L3) = 1. Suppose dim Pn ≤n! for n ≤4. Let V be the subspace of P4(L)
spanned by tangles with at most two labeled 3-boxes, and let R = V ∩ker Φ
be relations. Then
dim
Pn(L)
Jn(R)

≤n!
forall n.
There is some evidence for the conjecture. It would imply in particular
the n = 0 case which implies the following result, proved by D. Thurston
about hexagons:
“Consider all graphs with hexagonal faces that may be drawn on S2 with
non-intersecting edges. Let M be the move of Figure 2.5.8 on the set of all
such graphs (where the 8 external vertices are connected in an arbitrary way
to the rest of the graph).
Figure 2.5.8: The move M
37
Then one may ﬁnd a ﬁnite number of applications of the move M leading to
a graph with two adjacent 2-valent vertices.”
Example 2.6: Tensors. Let V be a ﬁnite dimensional vector space with
dual ˆV . We will deﬁne a planar algebra P ⊗= ∪kP ⊗
k with dim P ⊗
0 = 0 and
P ⊗
k = End(V ⊗ˆV ⊗V ⊗ˆV ⊗. . .) where there are k vector spaces in the tensor
product. The planar structure on P ⊗can be deﬁned invariantly using the
canonical maps V ⊗ˆV →K and ˆV ⊗V →K, which are applied to any pair of
vector spaces connected by an internal edge in a planar tangle, where V and
ˆV are associated with the marked points of a k-box in an alternating fashion
with V associated to ∗. One could also think of C ⊂End(V ) as a ﬁnite factor
and use the method of Theorem 4.2.1. It is perhaps easiest to understand this
structure using a basis (v1, v2, . . . , vn) of V , with corresponding dual basis.
An element of P ⊗
k is then the same as a tensor Xj1j2...jk
i1i2...ik . The labelling set Lk
is P ⊗
k itself and the presenting map Φ : Pk(L) →P ⊗
k is deﬁned by summing
(“contracting”) over all the internal indices in a labelled planar tangle. The
ﬁrst marked point in a box corresponds to the “j1” above. To be more precise,
one deﬁnes a state σ of a planar tangle T to be a function from the connected
components of the set S(T) of strings in T, σ : S(T) →{1, 2, . . ., n}, to the
basis elements of V . A state deﬁnes a set of indices around every box B in T,
and since the label associated to B is a tensor, with the appropriate number
of indices, to each labelled box, the state σ associates a number, σ(B). A
state also induces a function ∂σ from the marked points on the boundary of
T to {1, 2, . . ., n}. Now we associate a tensor Φ(T) with T as follows: let
f : {marked points (T)} →{1, 2, . . ., n} denote the indices
j1 . . . jk
i1 . . . ik

of a
tensor in P ⊗
k
(f(p, 0) = ip, f(p, 1) = jp, for 1 ≤p ≤k). Then
Φ(T)j1...jk
i1...ik =
X
σ:∂σ=f




Y
B∈{labelled
boxesof T }
σ(B)



.
An empty sum is zero and an empty product is 1. One easily checks that
Φ deﬁnes an algebra homomorphism and that ker Φ is invariant under the
annular category.
38
This planar algebra has an obvious ∗-structure. The invariant Z is rec-
ognizable as the partition function for the “vertex model” deﬁned by the
labelled network, the labels supplying the Boltzmann weights (see [Ba]).
For further discussion we introduce the following notation — consider
the indices as a (ﬁnite) set ∆. Given a function
γ1 . . . γk
δ1 . . . δk

from the marked
points of a k-box to ∆, we deﬁne the corresponding basic tensor to be
T j1...jk
i1...ik =



1
if i1 = δ1, i2 = δ2 etc.
and j1 = γ1, j2 = γ2 etc.
0
otherwise.
If S(∆) is the free semigroup on ∆, ∂T is then the word
γ1γ2γ3 . . . γkδkδk−1 . . . δ1 in S(∆), and we will use the notation
γ1 γ2 . . . γk
δ1 δ2 . . . δk
for this basic tensor.
The planar algebra P ⊗is not terribly interesting by itself (and there
seems to be no reason to limit the contractions allowed to planar ones). But
one may look for planar subalgebras. One way is to take a set {Ai ∈P ⊗
ki}
and look at the planar subalgebra Pk(Ai) they generate. The calculation of
Pk(Ai) as a function of the Ai’s can be extremely diﬃcult. While it is easy
enough to decide if the Ai’s are in the TL subalgebra, we will see in the next
example that the question of whether Pk(Ai)̸ = P ⊗
k is undecidable, even for
k = 1.
Note that if the tensors Ai have only 0–1 entries, the partition function
will be simply the number of “edge colourings” of the network by n colours
with colourings allowed only if they correspond to a non-zero entry of the
tensor label at each box.
The next example gives a situation where we can say Pk(Ai)̸ = P ⊗
k .
Example 2.7: Finitely generated groups. As in 2.6, if ∆is a set,
S(∆) will denote the free semigroup on ∆, and F(∆) will denote the free
group on ∆.
We deﬁne the map alt:S(∆) →F(∆) by alt(γ1 . . . γm) =
γ1γ−1
2 γ3γ−1
4
. . . γ±1
m , (where the + sign occurs if m is odd, – if m is even).
Note that alt is only a homomorphism from the subsemigroup of words of
even length.
39
Now let Γ be a discrete group and ∆a ﬁnite set, together with a function
δ 7→˜δ from ∆to Γ. There is then a natural map φ : F(∆) →Γ deﬁned by
φ(δ) = ˜δ. Let V be the vector space with basis ∆. Use V and the basis ∆to
form the planar algebra P ⊗of §2.6. Recall that, for a basic tensor T ∈P ⊗
k ,
∂T is the element of S(∆) obtained by reading around the boundary of T.
Let ∗denote the involution on S(∆) given by writing words backwards.
Deﬁnition. P Γ,∆= ∪kP Γ,∆
k
is the linear span of all basic tensors T such
that φ(alt(∂T)) = 1 in Γ.
Proposition 2.7.1 P Γ,∆is a planar ∗-subalgebra of P ⊗.
Proof. By 1.18, it suﬃces to show P Γ,∆is a unital subalgebra invari-
ant under the annular category A(∅). If T is a basic tensor in P Γ,∆
k
, let
∂+T (resp. ∂−T) be the element of S(∆) obtained by reading along the
top of T (resp. the bottom), so ∂T = ∂+T(∂−T)∗. Then for the product
T1T2 to be non-zero, ∂−T1 = ∂+T2. In the product alt(T1)alt(T2), the last
letter of (∂−T1)∗is then the same as the ﬁrst letter of ∂T2, but with op-
posite sign. Thus the contribution of ∂−T1 cancels with that of ∂+T2 and
φ(alt(T1)alt(T2)) = 1. So P Γ,∆is a subalgebra, clearly unital and self-adjoint.
Now consider a typical A(∅) element C applied to a basic tensor T as in
Figure 2.7.2.
γ1
γ2
γ3
γ6
γ5
γ4
Figure 2.7.2
This tensor is a sum of basic tensors, the sum ranging over all functions
from the curves in the diagram to ∆. If R is a particular basic tensor in
the sum, notice that the non through-strings in C contribute to alt(∂R) in
40
two ways — either they occur in cancelling pairs or, if their beginning and
end are separated by the left-hand side of the diagram, they change alt(∂R)
by conjugation (eliminate all the cancelling pairs ﬁrst to see this). Thus the
conjugacy class in F(∆) of alt(R) (and alt(T)) is not changed by removing
all non through-strings. Once this is done, however, the word around the
outer boundary is just an even cyclic permutation of the word w′ around the
inner boundary, so φ(alt w) = 1 ⇐⇒φ(alt(w′)) = 1. Thus PΓ,∆is invariant
under A(∅).
□
Note that the basic tensors in P Γ,∆are unchanged if we change ∼: ∆→Γ
by right multiplication by an element of Γ. So we may suppose there is an
element e of ∆with ˜e = 1 ∈Γ. To denote this situation we will say simply
“e ∈∆”.
Let G⊆Γ (resp. G′) = {φ(alt(∂+T)) | T a basic tensor in P Γ,∆
2k
(resp. P Γ,∆
k
), k∈
N}.
Lemma 2.7.3 G is the subgroup ⟨˜∆˜∆−1⟩of Γ generated by ˜∆˜∆−1, and if
e ∈∆, G = G′.
Proof. The deﬁnition of alt implies immediately that G ⊆⟨˜∆˜∆−1⟩.
That G = G−1 follows from Figure 2.7.4
T
T
φ(alt(∂+T)) = w
φ(alt(∂+T)) = w−1
φ(alt(∂+T)) = w−1
φ(alt(∂+T)) = w
Figure 2.7.4
41
That G is a group follows from Figure 2.7.5
T
R
φ(alt(∂+T))
φ(alt(∂+R))
φ(alt(∂+T))φ(alt(∂+R))
Figure 2.7.5
Also G contains ˜∆˜∆−1 since
γ
δ
is in P Γ,∆
2
where for γ ∈∆,
γ
is the “diagonal” tensor
γ
γ . That G = G′ if e ∈∆is easily seen by
attaching
e
to the right of basic tensors in P Γ,∆
k
when k is even.
□
We see that, if e ∈∆, a basis for P Γ,∆is formed by all random walks on
G, starting and ending at 1 ∈Γ, where the odd transitions correspond to
multiplying by a ˜δ for each δ ∈∆, and the even ones by ˜δ−1 for δ ∈∆. If
˜∆= ˜∆−1 and˜is injective, these are just random walks on the Cayley graph
of G.
If e ∈∆, each basic tensor T ∈P Γ,∆gives the relation alt(∂T) in G,
thinking of G as being presented on ∆\{e}.
Suppose G = ⟨∆\{e} | r1, r2, . . .⟩is a presentation of G, i.e. the kernel
of the map induced by ∼from F(∆\{e}) to G is the normal closure of
the ri’s. Then each ri may be represented by a k-box, written
ri , with
µ(alt(∂( ri ))) = ri, for some k with 2k ≥ℓ(r). (We use ℓ(w) to denote
the length of a word w.) To do this one may have to use e ∈∆so that the
word ri conforms with the alternating condition. For instance to represent
γδ2γ−1δ one might use the basic tensor
γ e δ e
e δ γ δ
.
Let µ : F(∆) →F(∆\{e}) be the homomorphism deﬁned by µ(e) = 1 ∈
F(∆\{e}), µ|∆\{e} = id.
42
Deﬁnition. Let R = S∞
k=0 Rk be the planar subalgebra of P Γ,∆generated
by { δ
: δ ∈∆}∪{ r }∪{r−1
i
}. Let H = {µ(alt(∂T)) | T is a basic tensor
in R}.
Theorem 2.7.6 The set H is a subgroup of F(∆\{e}) equal to the normal
closure N of {ri} in F(∆\{e}). Moreover, P G,∆= R.
Proof. That H is multiplicatively closed follows from Figure 2.7.7.
S
T
Q =
alt(∂Q) =alt(∂S)alt(∂T)
Figure 2.7.7
To see that H = H−1, note that the transpose of a basic tensor gives the
inverse boundary word, and a planar algebra generated by a ∗-closed set of
boxes is ∗-closed (note that the box δ
is self-adjoint). Figure 2.7.8 exhibits
conjugation of α = alt(∂T) by γδγ−1 for γ, δ ∈∆, which shows how to prove
that H is normal
Q =
γ
e
δ
γ
T
= γδγ−1alt(∂Q)γδ−1γ−1
µ(alt(∂T)
Figure 2.7.8
Thus H contains the normal closure N.
Now the tangle picture of an arbitrary basic tensor in R can be isotoped
so that it is as in Figure 2.7.9.
43
Figure 2.7.9
This is a tangle T all of whose curves are vertical straight lines surrounded
by an element of the category A(∅). But it is easy to see that applying an
A(∅) element changes alt(∂T) at most by a conjugation.
The most diﬃcult part of Theorem 2.7.6 is to show that P Γ,∆= R. We
must show that if w is a word of even length on ∆with φ(alt(w)) = 1 then
there is a basic tensor T ∈R with ∂T = w.
As a ﬁrst step, observe that if µ is a homomorphism from F(∆) to F(∆−
{e}) sending e to the identity and with µ(δ) = δ for δ̸ = e, then if w1, w2 ∈
S(∆) are of even length and µ(alt(w1)) = µ(alt(w2)) then alt(w1) = alt(w2).
This is because w1w∗
2 (w∗is w written backwards) satisﬁes alt(w1w∗
2) =
alt(w1)alt(w2)−1, thus alt(w1w∗
2) ∈ker µ which is the normal closure of e.
The length of w1w∗
2 can be reduced (if necessary) by eliminating consecutive
letters two at a time to obtain another word w, of even length, with ℓ(w) =
ℓ(alt w) (ℓ= length). By the uniqueness of reduced words in a free group,
w must be a product of words of the form x e y, which map to conjugates of
e±1 in F(∆). But the last letter of x and the ﬁrst letter of y must then be
the same, and alt will send both these letters to the same free group element.
Thus in the process of reducing w1w∗
2, all occurrences of e must disappear
and alt(w1) = alt(w2).
A consequence of this observation is that, if T is a basic tensor with
φ(alt(∂T)) = 1 in Γ so that µ(alt(∂T)) is in the normal closure of {ri} in
F(∆\{e}), then alt(∂T) is the normal closure of {alt(∂( ri ))} in F(∆).
Thus it suﬃces to show that, if T1 and T2 are basic tensors with alt(∂T1) =
alt(∂T2) ∈F(∆), then T1 = cT2 for some c in A(∅) (since for any x ∈S(∆)
with φ|µ(alt(x)) = 1 we have shown there is a T in the planar algebra R with
alt(∂T) = alt(x)). But this is rather easy — we may suppose without loss
of generality that no cancellation happens going from ∂T1 to alt(∂T1) and
then use induction on ℓ(∂T2). If ℓ(∂T2) = ℓ(∂T1) then ∂T2 = ∂T1. Otherwise
there must be a sequence . . . δδ . . . in ∂T2 for some δ ∈∆. Connecting δ to
δ in the tangle reduces the length of ∂T2 by 2, and the remaining region is a
disc.
□
44
A.Casson has pointed out the connection between P Γ,∆and van Kampen
diagrams.
If e ∈∆, the dimension of P Γ,∆
n
is the number of ways of writing 1 ∈Γ
as a product of elements ˜δ, δ ∈∆, with alternating signs. In particular,
dim(P Γ,∆
1
) = |∆|2 iﬀΓ is trivial. Since the problem of the triviality of a
group with given presentation is undecidable, we conclude the following.
Corollary 2.7.10 The calculation of the dimension of a planar subalgebra
of P ⊗is undecidable.
Since there are groups which are ﬁnitely generated but not ﬁnitely pre-
sented we have
Corollary 2.7.11 There are ﬁnite dimensional planar ∗-algebras which are
not ﬁnitely generated as planar algebras.
Proof. If ﬁnitely many linear combinations of basic tensors generated a
planar algebra, then certainly the basic tensors involved would also. But by
2.7.6, the group would then be ﬁnitely presented.
□
Example 2.8
Spin models. We give a general planar algebra that
is not a planar algebra, although it is the planar algebras associated with it
that will be of most interest. In some sense it is a “square root” of the planar
algebra P ⊗of §2.6.
Let V be a vector space of dimension Q with a basis indexed by “spin
states” {1, 2, . . .Q}. For each odd n let P σ
n be the subalgebra of End(V ⊗n+1
2 )
given by End(V ⊗n−1
2 ) ⊗∆where ∆is the subalgebra of End(V ) consisting
of linear maps diagonal with respect to the basis. For n = 0, P0 is the ﬁeld
K and for n even, P σ
n = End(V ⊗n
2 ). Elements of P σ
n will be identiﬁed with
functions from {1, 2, . . ., Q}n to K, the value of the function on (i1, i2, . . . , in)
being the coeﬃcient of the basic tensor
i1
i2 . . . . . . im−1
im
in
in−1 . . . .im+2
im+1
for n = 2m, and the coeﬃcient of
i1
i2 . . . . . . im−1
im
in
in−1 . . . .im+2
im
45
for n = 2m −1. (See §2.6 for notation.) We shall make P σ into a general
planar algebra in two slightly diﬀerent ways. In both cases the labelling set
will be P σ itself.
First planar structure on P σ. Take a tangle T in Pk(L). We will
deﬁne Φ0(T) ∈Pσ
k as follows.
First, shade the connected components of Bk\T (called regions) black
and white so that the region containing a neighborhood of (0,0) is white,
and so that regions whose closures intersect (i.e. which share an edge) have
diﬀerent colours. In other words, regions whose boundary induces the pos-
itive orientation of R2 are coloured white and negatively oriented ones are
black. Observe that the top and bottom of Bk consists of segments of length
one forming parts of the boundaries of regions alternately coloured white
and black. If k is odd, the right-hand boundary of Bk can be joined with
the rightmost top and bottom segments to form part of the boundary of a
black region. This way the boundary of Bk always has k segments attached
to black regions whose closure meets the boundary. Number these segments
cyclically 1, 2, . . ., k starting form the top left and going clockwise. To deﬁne
an element of P σ
k from T we must give a function Φ0(T) : {1, 2, . . .Q}k →K.
It is
Φ0(T)(i1, i2, . . .ik) =
X
σ
Y
B∈
n labelled boxes
ofT
o σ(B)
where σ runs over all functions from the black regions of T to {1, 2, . . ., Q}
which take the value ij on the black region whose closure contains the jth
boundary segment, for all j = 1, 2, . . ., k. Given a labeled box B of T, and
such a σ, the boundary segments of B which meet closures of black regions
are numbered 1 to kB so σ deﬁnes an element of {1, 2, . . ., Q}kB, and thus
the label of B gives a scalar σ(B) in K. As usual empty sums are zero and
empty products are 1. This completes the deﬁnition of Φ0 and it is easily
checked that Φ0 presents P σ as a planar algebra. The induced representation
of P(φ) gives a representation of TL with δ1 = Q, δ2 = 1. It is precisely the
representation associated with the Potts model used by Temperley and Lieb
in [TL].
To be sure of relevance to subfactors, we now show how to adjust these
46
parameters so that δ1 = δ2 = √Q.
Second planar structure on P σ. If T is a labeled tangle in Pk(L), we
deﬁne a tangle ˜T in Pk(φ) by “smoothing” all the boxes of ˜T, i.e. replacing
R by ↑↓↑, and shrinking all non-through-strings to semicircles near the top
or bottom of Bk. Put f(T) = Q
1
2(n+−n−)+ 1
4 (n∂
+−n∂
−) where n+ and n−are the
numbers of positively and negatively oriented circles in ˜T respectively, and
n∂
± are similarly the numbers of positively and negatively oriented semicircles
near the top and bottom. Thus deﬁned, f(T) is clearly an isotopy invariant,
so we could redeﬁne it by assuming all the boxes are parallel to the x-axis.
Assuming all maxima and minima of the y-coordinate restricted to the strings
of T are nondegenerate, 2(n+ −n−) + (n∂
+ −n∂
−) is just p+ + q+ −p−−q−
where p+, p−are the numbers of local maxima of y oriented to the left and
right respectively and similarly q+ and q−count minima to the right and left
respectively. It follows that T →f(T) is multiplicative and indeed that if A
is in the annular category one may deﬁne f(A) so that f(AT) = f(A)f(T).
The normalisation constant n+ −n−+ 1
2(n∂
+ −n∂
−) may seem mysteious.
What is actually being calculated is the isotopy invariant
R
dθ where the
intgral is taken over the strings of the tangle and dθ is the change of angle
or curvature 1-form, normalised so that integrating over a positively oriented
circle counts one. The above factor is then this integral when all strings meet
all boxes at right angles. Thus, by following shaded regions at every internal
box, another formula for this normalisation factor for a k−tangle is
[k + 1
2
] −b −
X
i≥1
[ni
2 ].
If all boxes are 2- or 3-boxes we get
1
2(#(black regions) −#(boxes)) + 1
4(n∂
+ −n∂
−),
where now n∂
+ and n∂
−are calculated by eliminating the boxes by following
the black regions rather than going straight through the box.
Proposition 2.8.1 The map Φσ : P(L) →P σ, Φ(T) = f(T)Φ0(T) (linearly
extended) presents P σ as a general planar algebra, Φ|P(φ) presents TL with
δ1 = δ2 = √Q.
47
Proof. Annular invariance follows from the relation f(AT) = f(A)f(T)
and the annular invariance of Φ0. If
is a part of a tangle T then Φ(T) =
QQ−1
2Φ( ˜T) where
has been removed from T. If
is part of T, Φ(T) =
Q
1
2Φ( ˜T).
□
When we refer to P σ, we will mean P σ, together with Φ.
Although dim P σ
0 = 1, so that P σ gives an invariant of labeled planar
networks with unbounded region positively oriented, dim(P σ
1,1) = Q so P σ is
not planar. However, P σ does have the obvious ∗structure and trR is deﬁned
and positive deﬁnite, so that any self-adjoint planar subalgebra of P σ will be
a C∗-planar algebra.
Proposition 2.8.2 A planar subalgebra P of P σ is spherical.
Proof. Given a planar network N in P with positively oriented un-
bounded region, we need only show that
N
=
Z(N)
But since P is planar, the sum over all internal spins in
N
is indepen-
dent of the spin value in the unbounded region, and each term in the sum
for
N
is Q times the corresponding term for
N . Taking the sum
over all Q spin states in the shaded region we are done.
□
There are ways to obtain planar subalgebras of P σ. An obvious place
to look is association schemes where one is given a family of (0,1) Q × Q
matrices Ai, i = 1, . . . , d, whose linear span is closed under the operations
given by the tangles
(matrix multiplication) and
(Hadamard
48
product). The requirement that this linear span (the “Bose-Mesner algebra”)
be closed under all planar contractions is presumably much more stringent.
If the requirement is satisﬁed, and the row and column sums of each Ai
do not depend on the row or column, we will have a planar subalgebra of
P σ.
A particularly simple example of this comes from transitive actions
of a ﬁnite group G on a set S. Then the orbits of G on S × S deﬁne an
association scheme whose Bose-Mesner algebra is the ﬁxed points for the
action on M|S|(C) by conjugation. We get a planar subalgebra of P σ either
by taking the ﬁxed points for the G-action on P σ or the planar subalgebra
generated by the assocation scheme. They are diﬀerent in general. A case
where they are the same is for the dihedral group on a set with ﬁve elements
(see [J4]). They are diﬀerent for Jaeger’s Higman-Sims model ([Ja],[dlH]) —
although the dimensions of the two planar algebras agree for a while, they
have diﬀerent asymptotic growth rates, one being that of the commutant of
Sp(4) on (C4)⊗k and the other being 100k.
Here is an interesting example for a doubly transitive group. It connects
with Example 2.5 and gives a new kind of “spin model” for link invariants
from links projected with only triple point singularities.
The alternating group A4 is doubly transitive on the set {1, 2, 3, 4} but
there are two orbits on the set of ordered triples (a, b, c) of distinct elements
according to whether 1 7→a, 2 7→b, 3 7→c, 4 7→d (with {a, b, c, d} =
{1, 2, 3, 4}) is an even or odd permutation. Let
e
∈P3(L) be such that
Φσ( e ) is the characteristic function of the even orbit. Deﬁne a mapping
from P(
) (the universal planar algebra on a single 3-box) to P σ by
sending
to
e
−1
2
. It is possible to prove that this map passes to
the quotient P H (the planar algebra of 2.5) with parameters t = i = x. This
is equivalent to showing that twice the value of the homfly polynomial of
a link obtained by connecting 3-boxes
(at 1,–1 in ℓ−m variables) in an
oriented way is the partition function in P σ (with Q = 4) given by ﬁlling the
same three boxes with
e
−1
2
. We give a sample calculation below
which illustrates all the considerations. Note that, for t = i = x, the value
49
of a single circle in the homfly skein is 2.
b
c
c
a
c
d
Figure 2.8.3
Smoothing all the 3-boxes leads to a single negatively oriented circle so
we must divide the ﬁnal partition function by 2.
Replacing the 3-boxes
by
e
−1
2
we look for spin states, i.e. functions from the shaded
regions to {1, 2, 3, 4} for which each 3-box yields a non-zero contribution to
the partition function. Around each 3-box this means that either the three
spin values are in the even orbit under A4, or they are all the same. The ﬁrst
case contributes +1 to the product over boxes, the second case contributes
–1 (not −1
2 because of the maxima and minima in the box).
If the box
labeled (†) is surrounded by the same spin value, all the spin states must be
the same for a nonzero contribution to Z. This gives a factor 4 × (−1)5. On
the other hand, if the spins at (†) are as in Figure 2.8.3 with (a, b, c) in the
even orbit, the other spin choices are forced (where {a, b, c, d} = {1, 2, 3, 4}),
for a contribution of –1. The orbit is of size 12 so the partition function is
1
2(−12−4) = −8. For this link the value of the homfly polynomial PL(1, −1)
is –4. The factor of 2 is accounted for by the fact that our partition function
is 2 on the unknot. Thus our answer is correct. Note how few spin patterns
actually contributed to Z!
50
If we wanted to use non-alternating 3-boxes we could simply use the
homfly skein relation to modify the 3-box. For instance
=
=
−
−
−
e
+
1
2
In general by [LM], PL(1, −1) is (−1)c−1(−2)
1
2 d where c is the number of
components of L and d is the dimension of the ﬁrst homology group (with
Z/2Z coeﬃcients) of the triple branched cover of S3, branched over L. It
would be reassuring to be able to see directly why our formula gives this value.
This would also prove directly that the map
7→
e
−1
2
passes to
the homfly quotient. Our proof of this is a little indirect — one shows that
the planar subalgebras P H and (P σ)A4 are the same by showing they arise
as centralizer towers from the same subfactor (constructed in [GHJ]). Thus
there must be a 3-box corresponding to:
and we obtained the explicit
expression for it by solving an obvious set of equations.
As far as we know, this is the ﬁrst genuine “3-spin interaction” statistical
mechanical model for a link invariant. Of course one may produce 3-spin
interaction models by taking a 2-spin one and summing over the internal
spin σ in the picture
σ1
σ3
σ
σ2
but that is of little interest. One may check quite easily that the above model
does not factorize in this way.
Example 2.9. Finite groups
A special case of the subalgebra of P σ of Example 2.8 where a group acts
on a set S is where S = G itself, the action being left multiplication. The
algebra P2 is then the group algebra CG, linearly spanned by elements
g
51
for g in G, which are by deﬁnition the matrices ga
b = δag,b. They have the
properties
h
=
=
,
,
g
gh
h
g
g
g
g
δg,h
gh
h
which can be used to present P as a planar algebra (see [La]). In particular
P1,3 = ℓ∞(G) and P2 = M|G|(C). It is obvious that G can be recovered from
the abstract planar algebra P by using the minimal idempotents of P1,3.
A noncommutative, ﬁnite-dimensional Hopf algebra gives a planar algebra
but it cannot be a subalgebra of P σ.
Example 2.10
Invariant planar algebras. Given an invertible ele-
ment u ∈P1 in a general planar algebra P we deﬁne u⊗k to be the element
of Pk deﬁned by the following k-tangle
u
u
u
u
· · ·
u⊗k =
(k is odd in the picture). The u’s and upside down u−1’s alternate.
Proposition 2.10.1 If P is a general planar algebra and S is a set of
invertible elements of P1, set
P S
k = {x ∈Pk | u⊗kx = xu⊗k ∀u ∈S} .
Then P S is a general planar subalgebra of P (planar if P is) and a ∗-planar
algebra if P is, and S = S∗.
Proof. That P S is a unital ﬁltered subalgebra is obvious. In the ∗case
note that (u⊗k)∗= (u∗)⊗k. So by Lemma 1.18 we only have to check invari-
ance under A(φ). Given an A ∈Ak,n(φ) consider the tangle representing
(⊗nu)πA(x)(⊗nu)−1 in Figure 1
Each string of ⊗ku, at the top and bottom, either connects to another ex-
ternal boundary point, in which case the u cancels with u−1, or it connects
to an internal boundary point of the annulus. Isotoping each such u and u−1
52
u
u
u
u−1
u−1
u−1
u−1
u−1
u
u
u
u−1
Figure 1:
close to the internal boundary and inserting cancelling pairs of u and u−1 on
strings connecting internal boundary points, we see that the tangle of Figure
2.10.2 gives the same element of P as the one where the only instances of u
and u−1 surround the x
in an alternating fashion. Since x ∈P S, these u’s
may be eliminated and we are left with πA(x).
□
This gives a useful way of constructing planar subalgebras. In particular
P S
1 is the commutant of S in P1 which may be much smaller than P1. Of
special interest is the case where P = P ⊗and S is a subgroup G of the
unitary group. In this case P G
k = EndG(V ⊗V ∗⊗V ⊗V ∗⊗. . .) (k copies of
V or V ∗) where V ∗represents the contragredient representation of G. Other
cases of interest can be constructed by cabling as in §3 and then picking some
set of invertible elements in the original Pn.
To obtain a more general construction one may replace ⊗nu with tangles
of the form
u1
u2
u3
for u’s satisfying appropriate equations. We will use this approach with n = 1
to pick up some important cases of commuting squares in Example 2.11.
53
