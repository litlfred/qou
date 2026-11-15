---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I"
section_id: sec-006-31-algebra-structure-markov-trace
section_title: "Algebra structure, Markov trace"
section_number: 3.1
pages: 67-74
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
toc_source: inferred
doc_brief: "Planar Algebras, I — We introduce a notion of planar algebra, the simplest example of which is a vector space of tensors, closed under planar contractions."
---
The proof of Theorem 3.1.3 below is routine for those conversant with [J1]
or [GHJ]. We include it since, as stated, it can be useful in determining prin-
cipal graphs. Recall that in a planar algebra P, ek denotes the idempotent
in Pk equal to 1
δ(|| . . .
).
Lemma 3.1.1 Let P be a ﬁnite-dimensional spherical nondegenerate pla-
nar algebra over an algebraically closed ﬁeld. Then for each k, Pk−1ek−1Pk−1
67
is a 2-sided ideal, denoted Ik, in Pk and if Mk is a set of minimal idempotents
in Pk generating all the distinct minimal ideals in Pk/Ik, we have
(i) pPkek−1 = 0 for p in Mk
(ii) pPkq = 0 for p̸ = q in Mk
(iii) For each x in Pk\Ik there is a p ∈M∥with xPkp̸ = 0.
(iv) tr(p)̸ = 0 for all p ∈Mk.
(v) Ik+2 = L
p∈Mk Pk+2pek+1Pk+2, pek+1 being a minimal idem-
potent in Pk+2.
Moreover, if, for each k, N∥is a set of minimal idempotents of Pk satisfying
(i) . . . (iv) (with Mk replaced by Nk), then there is an invertible uk in Pk
with ukN∥⊓−∞
∥
= M∥(so in particular (v) is true for Nk).
Proof. To see that Pk−1ek−1Pk−1 is an ideal, consider the maps α, β :
Pk →Pk−1 given by the annular tangles
and
respectively. A diagram shows that xek−1y = α(x)ek−1β(y) for x, y ∈Pk.
By Corollary 1.30, Pk is semisimple and multimatrix since K is alge-
braically closed. Thus properties (i), (ii), (iii) and (v) are obvious for Mk. If
p̸ = 0 satisﬁed tr(p) = 0, then tr would vanish on the whole matrix algebra
containing p which would then be orthogonal to Pk.
Finally, suppose we are given Nk satisfying (i)–(iv). Then since Pk is
multimatrix, each p in Nk belongs to a unique matrix algebra summand in
which there is an invertible up with uppu−1
p
∈Mk. Putting together the
up’s, and the identity of Ik, we get uk. Property (v) for Nk then follows from
(iii).
□
Deﬁnition 3.1.2. With P and Nk as in 3.11, we deﬁne the principal
graph ΓP of P to be the (bipartite) graph whose vertices are S
k≥0 N∥with
68
distinguished vertex ∗so that N0 = {∗}, and dim (pPk+1q) edges between
p ∈Nk and q ∈Nk+1. Let dp denote the distance from p to ∗on ΓP.
Theorem 3.1.3 As an algebra, Pk is isomorphic to the algebra whose basis
is random walks of length 2k on ΓP beginning and ending at ∗with multipli-
cation rule w1w2 = w3 if the ﬁrst half of the walk w2 is equal to the second
half of w1, and w3 is the ﬁrst half of w1 followed by the second half of w2;
0 otherwise. Moreover, if⃗t is the function from the vertices of ΓP to K,⃗
tp = δdptr(p),⃗t is an eigenvector for the adjacency matrix of Γ, eigenvalue δ.
Proof. The ﬁrst assertion is easily equivalent to showing that the Brat-
teli diagram (see [GHJ]) of the multimatrix algebra Pk in Pk+1 is the bipartite
graph consisting of those vertices p with dp ≡k (mod 2) and dp ≤k, con-
nected to those with dp ≡(k + 1) (mod 2) and dp ≤k + 1 with appropriate
multiplicities. Observe ﬁrst that P0 = C and M1 is a set of minimal projec-
tions, one for each matrix algebra summand of P1, so the Bratelli diagram
is correct for P0 ⊂P1. Now proceed by induction on k. The trace on Pk
is nondegenerate, as is its restriction to Pk−1 so one may perform the ab-
stract “basic construction” of [J1] to obtain the algebra ⟨Pk, ePk−1⟩which is
multimatrix and isomorphic to Pk ⊗Pk−1 Pk as a Pk −Pk bimodule via the
map x ⊗y 7→xePk−1y. Moreover the matrix algebra summands of ⟨Pk, ePk−1⟩
are indexed by those of Pk−1, which by induction are the vertices of ΓP with
dp ≤k −1, dP ≡(k + 1) mod 2. If one deﬁnes the trace tr on ⟨Pk, ePk−1⟩by
etr(xePk−1y) =
1
δ2tr(xy) then the traces of minimal projections in ⟨Pk, ePk−1⟩
are
1
δ2 times those in Pk−1. Moreover, setting γ(xePk−1y) = xeky deﬁnes an
algebra homomorphism from ⟨Pk, ePk−1⟩which is injective by property (iv)
and onto Ik+1. And Tr(xeky) = 1
δ Tr(xy) so tr = etr ◦γ−1 on Ik+1. Properties
(i), (ii) and (iii) ensure that the other vertices of the Bratteli diagram for
Pk ⊂Pk+1 are labelled by vertices p of ΓP with dP = k + 1. And the number
of edges on ΓP connecting a p in Mk to a q in Mk+1 is by deﬁnition the
number of edges in the Bratteli diagram. That there are no edges between
Mk+1 and Mj, j < k, follows from
(xek−1y)p = 1
δ2 x(ek−1ekek−1)yp = 1
δ2 x(ek−1ekpek−1)y = 0
by (i) for x, y ∈Pk−1 and p ∈Mk+1.
69
Finally, the (normalized) trace of a minimal projection p in Ik is δdP −k⃗tp
so the assertion about the trace follows as usual (see [J1]).
□
Remarks. (1) Similarly, the algebras P1,k have a principal graph Γ′
P with
the trace vector⃗s. We call Γ′
P the dual principal graph. Ocneanu has shown,
in the C∗case, how to associate numerical data encoding the ensuing em-
bedding of the random walk algebra of Γ′
P into that of ΓP. This completely
captures the planar algebra structure and is analogous to choosing local co-
ordinates on a manifold. The same could be done under the hypotheses of
Lemma 3.1.1. The principal graphs alone do not determine the planar alge-
bra — for instance the algebras (P σ)Z/4Z and (P σ)Z/2Z⊕Z/2Z of 2.8 have the
same principal graph but are readily distinguished by counting ﬁxed points
under the rotation.
(2) In fact, the assumption of nondegeneracy on P in 3.1.1 and 3.1.3
could be replaced by the hypothesis Pk/Ik semisimple. Then conditions (i)–
(iv) could be used to inductively guarantee nondegeneracy.
(3) If P had been a C∗-planar algebra, we would have a theorem (3.1.3)∗
with all tr(p) positive, all p’s projections, and the obvious adjoint
∗
on
random walks.
Theorem 3.1.3 can be used to compute the principal graphs for Temperley
Lieb and the Fuss Catalan algebra (it is the “middle pattern” method of
[BJ2]). We now illustrate its use by calculating the principal graph of the
nondegenerate planar algebras coming from Example 2.2. We work over C
for convenience, and in the C∗case to simplify life.
Let (A, TR) be a ﬁnite-dimensional unital C∗-algebra with normalized
faithful (positive) trace TR. The labelling set L is L1 = A.
We choose
a number δ > 0 and let τp be TR(p) for projections p ∈A.
A labelled
network is then a disjoint union of smoothly embedded circles, each one
containing a (possibly empty) sequence of 1-boxes labelled by elements in
A.
We deﬁne the partition function Z of such a collection of circles to
be δ# (circles) Q
(circles) TR(a1a2 . . . an), where a1a2 . . . an are the labels on the
given circle, numbered in order around the circle. The partition function Z is
obviously multiplicative so we deﬁne P (A,TR) to be the nondegenerate planar
algebra, with obvious ∗-structure, deﬁned by 1.23. It is linearly spanned
70
by Temperley-Lieb diagrams with a single labelled box on each string. The
relations of Example 2.2 hold, noting that Z( p
) = δτp. For certain values
of δ and traces TR we will compute the principal (and dual principal) graphs
of P A,TR) and the Markov trace, and show it to be a planar C∗-algebra. Let
us ﬁrst describe the graphs. Let M = {p} be a set of minimal projections in
A, one for each matrix algebra direct summand and let np = dim(pA). Let
S(M) be the free semigroup with identity on M. Let λ : Proj →N∪{∞} be
a function, and Wλ be the set of words in S(M) which contain no consecutive
string of p’s longer than λ(p), for each p.
Deﬁnition 3.1.4. The graph ΓA,λ is the rooted tree having vertices Wλ,
with np edges between w and wp for every p ∈M with {w ∪wp} ⊂Wf. The
root ∗is the identity of S(M).
Thus if λ(p) = 1 for all p and A is abelian, ΓA,λ is the regular tree of
valence |M|.
If λ(p) = ∞for all p and A is abelian, the root ∗of the
tree ΓA,λ has valence |M| and all other vertices have valence |M| + 1. If
A = Cp + Cq and λ(p) = 1, λ(q) = 2, the tree ΓA,λ is as in Figure ??.
∗
Figure 3.1.5
Recall the polynomials Tn(x) of [J1], T1 = 1, T2 = 1, Tn+1 = Tn −xTn−1 and
the “Jones-Wenzl” projections fk ∈TL(k) with f ∗
k = f 2
k = fk, fkei = 0 for
i = 1, 2, . . ., k −1 so that fk are elements of any (spherical) planar algebra,
and tr(fk) = Tk−2( 1
δ2) if Tj( 1
δ2)̸ = 0 for j < k + 2.
Theorem 3.1.6 With notation as above, suppose τpδ = 2 cos π/(λ(p)+2)
(τpδ ≥2 if λ(p) = ∞).
Then P (A,TR) is a (spherical) C∗-planar algebra
71
with principal and dual principal graphs equal to ['4,.. The (normalized)
trace of the minimal projection in PAT) corresponding to the word w=

pips? ...pr (Somp=k and p; # pir) is TE, 7. Tmi (7,4).

PROOF. We shall give explicit projections satisfying conditions (i)—(iv)
of 3.1.1. The key observation is that tangles with a fixed p labelling each
string form a Temperley-Lieb subalgebra B, with parameter 67, (and identity

_ ). So if m < A(p) we consider the projection
| | | |

P P P P

Jin

where f,, is calculated in Temperley-Lieb with 7 strings and Z (QO) = 7,0.

Now set , ,

Pi P2 Pr
I I I

fina tina eee tim,
I I

Pi P2 Pr
I I I

where we have combined the m, strings at the top (and bottom) of fm, into
one. Orientations are completely forgotten and may be inserted, if required,
so as to satisfy Definition 1.7.

Condition (1) of 3.1.1 is easy: P, is linearly spanned by Temperley Lieb
diagrams with matrix units (with the p’s among the diagonal ones) from the
simple summands of A in a single box on each string. If x is such an element,

72
then if xek−1 is non-zero, the product pwxek−1 contains
e
PW
with e being a matrix unit. The string containing e enters the box for pw
either connecting two distinct f’s or two strings of the same one. In the ﬁrst
case the result is zero since e belongs to precisely one of the direct summands.
In the second case it is zero because of the properties of the f’s.
Condition (ii) follows similarly, noting that a picture like the above will
occur unless all the strings of x are through strings.
For condition (iii) we observe that the ideal Ik is linearly spanned by x’s
as above with less than k through-strings, so we may suppose x is composed
of through-strings, each with a matrix unit in its box. Note that any relation
true in Bp is true in Pk. Hence if j ≥λ(p), fj = 0 and the identity of Bp is a
linear combination of tangles with less than λ(p) through-strings. So we can
suppose that in x there is no sequence of λ(p) strings in a row whose matrix
unit labels are in the same simple summand as p. Thus by multiplying x
to the left and right by tangles with the appropriate matrix unit labels, we
get axb = pw for some word w in S(M) of length k. Thus (iii) will follow
provided (iv) holds.
We calculate the normalized trace of pw. It is
· · ·
) = δ−kΠiZ(
)
δ−kZ(
p1
p2
pr
fmr
fm2
fm1
pi
fmi
Now the partition function on Pm, restricted to Bp, gives a Markov trace
which will be normalized after division by Z( p
)m = (δτp)m. So Z( fm
) =
δmτ m
p Tm(τpδ). Hence tr(pw) = Qr
i=1 τpiTmi(τpiδ).
73
Finally we must calculate the multiplicities dim(pvPkpw) for v of length
k and w of length k −1. We must consider diagrams of the form
PW
x
PV
· · ·
· · ·
· · ·
· · ·
where x is a Temperley Lieb diagram decorated with matrix units as before.
Arguing on pv,
x has only through-strings, v = wp for some p ∈M, and
the ﬁrst k −1 strings of x are labelled by the elements of M in w. Thus the
diagram is in fact equal to
PV
· · ·
· · ·
e
where e is a matrix unit with one subscript ﬁxed.
These diagrams span
pvPkpw and the sesquilinear form given by (x, y) = tr(y∗x) is diagonal with
non-zero entries. Hence dim(pvPkpw) = np.
□
