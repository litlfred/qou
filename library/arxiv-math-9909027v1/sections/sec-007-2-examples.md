---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California"
section_id: sec-007-2-examples
section_title: "Examples"
section_number: 2
pages: 27-35
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
doc_brief: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California — We introduce a notion of planar algebra, the simplest exampl e of which is a vector space of tensors, closed"
---
Example 2.1: Temperley-Lieb algebra. If δ1 and δ2 are two non-zero
scalars, one deﬁnes T L(n, δ1, δ2) as being the subspace of Pn(∅) spanned by
27
the tangles with no closed loops. Deﬁning multiplication on T L(n, δ1, δ2)
by multiplication as in Pn(∅) except that one multiplies by a factor δ1 for
each loop and δ2 for each loop , then discarding the loop. Clearly the
map from Pn(∅) to T L(n, δ1, δ2) given by multiplying by δ1’s or δ2’s then
discarding loops, gives a Φ exhibiting T L(n, δ1, δ2) as a planar algebra. For
general values of δ1 and δ2, T L(n) is not non-degenerate. An extreme case
is δ1 = δ2 = 1 where Z(c(T1 − T2)) = 0 for all relevant tangles c, T1, T2. In
fact the structure of the algebras T L(n, δ1, δ2) (forgetting Φ), depends only
on δ1δ2. To see this, show as in [GHJ] that T L(n, δ1, δ2) is presented as an
algebra by Ei, i ≤ 1, . . . , n−1 with E2
i = δ1Ei for i odd, E2
i = δ2Ei for i even,
and EiEi±1Ei = Ei and EiEj = EjEi for |i − j| ≥ 2. Then setting ei = 1
δ1
Ei
(i odd), ei = 1
δ2
Ei (i even), the relations become e2
i = ei, eiei±1ei = 1
δ1δ2
ei,
eiej = ejei for |i − j| ≥ 2. If δ1 = δ2 = δ, we write T L(δ1, δ2) = T L(δ).
One may also obtain T L via invariants, as a planar algebra on one box,
in several ways.
(i) The chromatic polynomial. A planar network N on L = L2 with
#(L2) = 1 determines a planar graph G(N ) by choosing as vertices the pos-
itively oriented regions of R2\N and replacing the 2-boxes by edges joining
the corresponding vertices (thus ↝ •— •). Fix Q ∈ C − {0} and let
Z(N ) = (chromatic polynomial of G(N ) as evaluated at Q) × f , where f = 1
if the outside region is negatively oriented and f = Q−1 if the outside re-
gion is positively oriented. To see that PZ is Temperley-Lieb, deﬁne the
map α : P(L) → T L(1, Q) by α( ) = − (extended by multilinearity
to P(L)). It is easy to check that α makes T L(1, Q) a planar algebra on
L and the corresponding partition function is Z as above. Thus PZ is the
non-degenerate quotient of T L(1, Q).
(ii) The knot polynomial of [J2]. Given a planar network N on one 2-
box, replace the 2-box by to get an unoriented link diagram. Deﬁne
Z(N ) to be the Kauﬀman bracket ([Ka1]) of this diagram. Sending to
A + A−1 we see that this deﬁnes a map from P(L) to T L(−A2 − A2)
28
with the Temperley-Lieb partition function.
Both (i) and (ii) are generalized by the dichromatic polynom ial (see [Tut]).
Example 2.2: Planar algebras on 1-boxes. If A is an associative
algebra with identity and a trace functional tr: A → K, tr( ab) = tr( ba),
tr(1) = δ, we may form a kind of “wreath product” of A with T L(n, δ). In
terms of generators and relations, we put L = L1 = A and
a, b ∈ A
− λa + b
λ ∈ K
a + b λ
b
a
− baR = ∪ a, b ∈ A a 1− ∪ ∪ −tr(a)
One may give a direct construction of this planar algebra usi ng a basis as
follows. Choose a basis {ai | i ∈ I} of A with aiaj = ∑ ck
ijak for scalars
ck
ij. (Assume 1 ∈ { ai} for convenience.) Let P A
n be the vector space whose
basis is the set of all Temperley-Lieb basis n-tangles together with a function
from the strings of the tangle to {ai}. Multiply these basis elements as for
Temperley-Lieb except that, when a string labelled ai is joined with one
labelled aj, the result gives a sum over j of ck
ij times the same underlying
Temperley-Lieb tangle with the joined string labelled ak. In the resulting
sum of at most #( I)n terms, if a closed loop is labelled ak, remove it and
multiply by a factor of tr( ak). This gives an associative algebra structure
on each P A
n . It becomes a planar algebra on A in the obvious way with Φ
mapping a to a linear combination of strings labelled aj, the coeﬃcients
being those of a in the basis {ai}.
If a string in P(A) has no 1-box on it, it is sent to the same string labelled
with 1. One may check that the kernel of Φ is precisely the idea l generated
by our relations R, so P A = P(A)/J (R).
Observe how P A
n is a sum, over Temperley-Lieb basis tangles, of tensor
powers of A. When n = 2 this gives an associative algebra structure on
A ⊗ A ⊕ A ⊗ A. Explicitly, write ( a ⊗ b) ⊕ 0 as a ⊗ b and 0 ⊕ (x ⊗ y) as x ⊗ y.
Multiplication is then determined by the rules:
(a1 ⊗ b1)(a2 ⊗ b2) = a1a2 ⊗ b2b1
(x1 ⊗ y1)(x2 ⊗ y2) = tr( y1x2)x1 ⊗ y2
29
(a ⊗ b)(x ⊗ y) = 0 ⊕ axb ⊗ y
(x ⊗ y)(a ⊗ b) = 0 ⊕ x ⊗ bya
The planar algebra P A may be degenerate, even when tr on A is non-
degenerate and δ is such that T L(δ) is non-degenerate. We will give more
details on the structure of P A in §3.1.
Example 2.3: The Fuss-Catalan algebras (see [BJ2]). If a1, a2, . . . , ak ∈
K − {0}, F C(n, a1, . . . , ak) is the algebra having as basis the Temperley-Lieb
diagrams in T L(nk) for which, for each p = 1, 2, . . . , k, the set of all boundary
points (counting from the left) indexed by {jk +(−1)jp+(sin2 jπ
2 )(k +j) | j =
01, 2, . . .(n − 1)} are connected among themselves. Assign a colour to each
p = 1 , 2, . . . , k so we think of the Temperley-Lieb strings as being coloured.
Then multiplication preserves colours so that closed loops will have colours.
Removing a closed loop coloured m contributes a multiplicative factor am.
To see that F C(n, a1, . . . , ak) is a planar algebra, begin with the case k = 2.
We claim F C(n, a, b) is planar on one 2-box. We draw the box symbolically
as
This shows in fact how to deﬁne the corresponding Φ : Pn → F C(n, a, b):
double all the strings and replace all the 2-boxes according to the diagram.
Thus for instance the tangle N below (with boxes shrunk to points, there
being only one 2-box),
30
is sent to Φ( N ) below
b b b a a a b b b a a a
a b b b a b
= a2b2
b a a b a b
It is clear that Φ deﬁnes an algebra homomorphism and surject ivity follows
from [BJ2]. That ker Φ is annular invariant is straightforwa rd. The general
case of F C(n, a1, . . . , ak) is similar. One considers the k − 1 2-boxes drawn
symbolically as
One proceeds as above, replacing the single strings in an N by k coloured
strings. Surjectivity follows from [La].
Note that these planar algebras give invariants of systems o f immersed
curves with generic singularities, and/or planar graphs. T he most general
such invariant may be obtained by introducing a single 2-box which is a linear
combination of the k − 1 2-boxes described above. This will generalize the
dichromatic polynomial.
Example 2.4: The BMW algebra. Let L = L2 = {R, Q} and deﬁne
the planar algebra BMW on L by the relations
= = (i) , , = =
RR Q Q R
Q
Q
R
31
(ii) = =R Q Q R
(iii) =,Q Q R=a−1= a =R , (a ∈ C − {0})
(iv) =
Q
Q
Q R
R
R
+ +(v) R Q = x
Note that we could use relation (v) to express BMW using only the
one label R, but the relations would then be more complicated. At this
stage BMW could be zero or inﬁnite dimensional, but we may deﬁne a
homomorphism from BMW to the algebra BM W of [BiW],[Mu] by sending
R to and Q to . This homomorphism is obviously surjective and
one may use the dimension count of [BiW] to show also that dim BMW (n) ≤
1.3.5. . . .(2n−1) so that BMW ∼= BM W as algebras. Thus BM W is planar.
It is also connected and the invariant of planar networks is t he Kauﬀman
regular-isotopy two-variable polynomial of [Ka2].
Remark. Had we presented BM W on the single 2-box R, the Reide-
32
meister type III move (number (iv) above) would have been
R
=
R
R
R
R
R
+ pictures with
at most two R ’s
This leads us to consider the general planar algebra Bn with the following
three conditions:
(1) Bn is planar on one 2-box.
(2) dim B2 = 3.
(3) dim B3 ≤ 15.
If one lists 16 tangles in B3 then generically any one of them will have to be
a linear combination of the other 15. Looking at the 15th and 1 6th tangles
in a listing according to the number of 2-boxes occuring in th e tangle, we will
generically obtain a type III Reidemeister move, or Yang-Ba xter equation,
modulo terms with less 2-boxes,as above. It is not hard to sho w that these
conditions force dim Bn ≤ 1.3.5 · . . . · (2n − 1) since there are necessarily
Reidemeister-like moves of types I and II. Note that F C(n, a, b) satisﬁes these
conditions as well as BM W! For C ∗-planar algebras, we have shown with
Bisch ([BJ1]) that the only B’s with (1) and (2) as above, and dim B3 ≤ 12
are the Fuss-Catalan algebras (with one exception, when dim B3 = 9).
Example 2.5: a Hecke-algebra related example. The homfly poly-
nomial of [F+] is highly sensitive to the orientation of a lin k and we may not
proceed to use it to deﬁne a planar algebra as in Example 2.4. I n particular,
a crossing in the homfly theory is necessarily oriented as . Thus it does
not yield a 2-box in our planar algebra context. Nevertheless it is possible to
use the homfly skein theory to deﬁne a planar algebra. We let P H
k be the
33
usual homfly skein algebra of linear combinations of (3-dimensional) is o-
topy classes of oriented tangles in the product of the k-box with an interval,
with orientations alternating out-in, modulo the homfly skein relation
t − t−1 = x where t ⁄= 0 and x are scalars. Projected onto the k-box,
such a tangle could look as in Figure 2.5.1,
Figure 2.5.1
If we take the labeling set Lk = P H
k , then P H is a general planar al-
gebra since planar isotopy of projections implies 3-dimens ional isotopy (in-
variance under the annular category is easy). Standard homfly arguments
show dim ( P H
k ) ≤ k! and a specialization could be used to obtain equality.
Thus the algebra is planar and the invariant is clearly the homfly polyno-
mial of the oriented link diagram given by a labeled network i n P H
0 . If we
used this invariant to deﬁne the algebra as in §1, we would only obtain the
same algebra for generic values of t and x. Note that P H
k is not isomorphic
to the Hecke algebra for k ≥ 4, e.g. P H
4 has an irreducible 4-dimensional
representation. In fact P H
k is, for generic ( t, x) and large n, isomorphic to
EndSU (n) (V ⊗ ¯V ⊗ V ⊗ ¯V . . . )/bracehtipupleft /bracehtipdownright/bracehtipdownleft/bracehtipupright
k vector spaces
, where V = Cn, the obvious SU (n)-module.
This isomorphism is only an algebra isomorphism, not a plana r algebra iso-
morphism.
It is clear that the labeling set for P H could be reduced to a set of k!
isotopy classes of tangles for P H
k . But in fact a single 3-label suﬃces as we
now show
Theorem 2.5.2 Any tangle in the knot-theoretic sense with alternating in
and out boundary orientations is isotopic to a tangle with a d iagram where
34
all crossings occur in disjoint discs which contain the patt ern
with some non-alternating choice of crossings.
Proof. We begin with a tangle without boundary, i.e. an oriented lin k
