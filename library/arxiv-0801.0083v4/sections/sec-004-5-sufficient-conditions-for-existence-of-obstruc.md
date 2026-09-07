---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI"
section_id: sec-004-5-sufficient-conditions-for-existence-of-obstruc
section_title: "Sufficient Conditions for Existence of Obstruction Classes"
section_number: 5
pages: 25-29
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
doc_brief: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI — W e introduce the notion of central extension of gerbes on a to po- logical space X."
---
Let N be a sheaf of abelian groups on a topological space X. The operation in
N is multiplication. We denote by H i(X, N ) the derived functor sheaf cohomology.
An open set U ⊂ X will be called N -acyclic if the sheaf cohomology satisﬁes
Hi(U, N ) = 1 for all i> 0. Now suppose U = {Uk}k∈K is a collection of open sets
in X. We say that the collection U is N -acyclic if all the open sets Uk0,...,k m are
N -acyclic.
Deﬁnition 5.1. Let N be a sheaf of abelian groups on X. We say that there are
enough N -acyclic open coverings if for any open set U ⊂X, and any open covering
U of U , there exists an N -acyclic open covering U′ of U which reﬁnes U .
Example 5.2. Suppose X is a diﬀerentiable (i.e. C ∞) manifold, and let OX be
the sheaf of C ∞ R-valued functions on it. If N is an OX -module, then any open
covering of X is N -acyclic. If K is a constant sheaf of abelian groups on X, then
any open covering U = {Uk}k∈K such that the ﬁnite intersections Uk0,...,k m are
contractible, is K-acyclic. There are always enough coverings of this sort.
Example 5.3. Suppose X is a complex analytic manifold, and let OX be the
sheaf of holomorphic C-valued functions on it. If N is a coherent OX -module, then
any open covering of X by Stein manifolds is N -acyclic. There are always enough
coverings of this sort. Regarding constant sheaves see the p revious example. (Oddly,
we do not know if it is possible to ﬁnd an open covering U = {Uk}k∈K such that
the ﬁnite intersections Uk0,...,k m are both contractible and Stein.)
26 AMNON YEKUTIELI
Example 5.4. Suppose X is an algebraic variety over a ﬁeld K (i.e. a separated
integral ﬁnite type K-scheme), and let OX be the structure sheaf. If N is a coherent
OX -module, then any aﬃne open covering of X (i.e. a covering U = {Uk}k∈K such
that the open sets Uk are all aﬃne) is N -acyclic. There are always enough coverings
of this sort. If K is a constant sheaf of abelian groups on X, then any open covering
of X is K-acyclic (since K is a ﬂasque sheaf in the Zariski topology).
Recall that there are canonical group homomorphisms
ˇHi(X, N ) → Hi(X, N ),
which are bijective for i = 0, 1; see [Ha, Section III.4.].
Proposition 5.5. Let N be a sheaf of abelian groups on X.
(1) If U is an N -acyclic open covering of X, then the canonical group homo-
morphisms
ˇHi(U, N ) → Hi(X, N )
are bijective for all i.
(2) If there are enough N -acyclic open coverings, then for any N -acyclic open
covering U of X, the canonical group homomorphisms
ˇHi(U, N ) → ˇHi(X, N ) → Hi(X, N )
are bijective for all i.
Proof. Assertion (1) is [Ha, Exercise III.4.11]. Assertion (2) fol lows from (1). See
also the original [Gr2]. □
From now on in this section, the operation in the group N is multiplication, and
the identity element is 1.
Proposition 5.6. Suppose
(5.7) 1 → N → G → H → 1
is an exact sequence of sheaves of groups on X.
(1) There is an exact sequence in Čech cohomology
1 → N (X) → G (X) → H(X)
→ ˇH1(X, N ) → ˇH1(X, G) → ˇH1(X, H).
Here ˇH1(X, −) are pointed sets.
(2) Assume (5.7) is a central extension, and there are enough N -acyclic open
coverings. Then the exact sequence of part (1) extends to an exact sequence
· · · → ˇH1(X, G) → ˇH1(X, H)
∂
− →ˇH2(X, N ).
Proof. (1) This is pretty easy. A readable proof can be found in [Gr1, Chapter V].
(2) A more general result is [Gr2, Corollaire to Proposition 3.4.2], where there is
no topological assumption of the sheaf N . However, the precise statement and the
proof rely on Godement resolutions, and are hard to follow. H ence we provide a
relatively easy proof in the case we need.
Recall that the pointed set ˇH1(X, H) classiﬁes left H-torsors on X, up to iso-
morphism. And the function ˇH1(X, G) → ˇH1(X, H) sends a G-torsor to the induced
H-torsor.
CENTRAL EXTENSIONS OF GERBES 27
Let S be an H-torsor. Choose an N -acyclic open covering U = {Uk}k∈K of X
that trivializes S. For any index k choose some sk ∈ S (Uk). For any k0,k 1 we have
an element hk0,k 1 ∈ H(Uk0,k 1) such that sk1 =hk0,k 1 ·sk0 . Since ˇH1(Uk0,k 1, N ) = 1,
by part (1) we have a surjection of groups G(Uk0,k 1) → H(Uk0,k 1 ), and thus we can
lift hk0,k 1 to some gk0,k 1 ∈ G (Uk0,k 1). Deﬁne
nk0,k 1,k 2 :=g−1
k0,k 2 ◦gk1,k 2 ◦gk0,k 1 ∈ G (Uk0,k 1,k 2 ).
Then
c := {nk0,k 1,k 2}k0,k 1,k 2∈K
is a Čech 2-cocycle with values in N ; cf. Lemma 4.11. Let
∂ (S) := [c] ∈ ˇH2(X, N ).
As in the proof of Lemma 4.12 we see that the cohomology class ∂ (S) is independent
of choices, and thus we get a well deﬁned function
∂ : ˇH1(X, H) → ˇH2(X, N ).
And like in the proof of Theorem 4.17 we see that ∂ (S) = 1 if and only if S comes
from a G-torsor. □
Consider a central extension of gerbes
(5.8) 1 → N → G
F
− →H → 1
on X.
Lemma 5.9. SupposeU is an N -acyclic open set. Let i,j ∈ Ob G(U ) be such that
G(U )(i,j ) ⁄= ∅. Then the function
F : G(U )(i,j ) → H(U )
(
F (i),F (j)
)
is surjective.
Proof. Here both torsors G(i,j ) and H
(
F (i),F (j)
)
are trivial over the respec-
tive sheaves of groups G(i,i ) and H
(
F (i),F (i)
)
; so we may assume i = j. Since
ˇH1(U, N ) = 1 the assertion follows from the exact sequence in Proposi tion 5.6(1),
applied to the short exact sequence of sheaves of groups
1 → N |U → G(i,i )
F
− →H(i,i ) → 1.
□
Lemma 5.10. SupposeU is an N -acyclic open set. Then for any i,j ∈ Ob G(U )
the function
F (i,j ) : G(U )(i,j ) → H(U )
(
F (i),F (j)
)
is surjective.
Proof. If H(U )
(
F (i),F (j)
)
= ∅ then there is nothing to prove. So let us assume it
is nonempty. We will prove that G(U )
(
i,j
)
⁄= ∅; and then the assertion will follow
by Lemma 5.9.
Choose some h ∈ H(U )
(
F (i),F (j)
)
. Let U = {Uk}k∈K be an open covering of
U , such that for any k there exists an isomorphism gk ∈ G(Uk)(i,j ) lifting h. This
can be done. Now for k0,k 1 ∈K deﬁne
gk0,k 1 :=g−1
k1 ◦gk0 ∈ G(Uk0,k 1)(i,j ).
28 AMNON YEKUTIELI
SinceF (gk0,k 1) = 1 we see that in fact
gk0,k 1 ∈ N (Uk0,k 1 ).
An easy calculation shows that the Čech 1-cochain {gk0,k 1 }k0,k 1∈K is a cocycle.
Since ˇH1(U, N ) = 1, after possibly replacing U with a reﬁnement, we can ﬁnd a
0-cochain {fk}k∈K such that gk0,k 1 =f−1
k1
◦fk0 . Deﬁne
g′
k :=gk ◦f−1
k ∈ G(Uk)(i,j ).
Then the 0-cochain {g′
k}k∈K is a cocycle with values in the sheaf of sets G(i,j ).
From the sheaf property it follows that there is an element g′ ∈ G(U )(i,j ) such
thatg′|Uk =g′
k for all k. We see that G(U )
(
i,j
)
⁄= ∅. □
Theorem 5.11. Consider the central extension of gerbes (5.8). If there are enough
N -acyclic open coverings, then the obstruction class cl2
F (j) from Deﬁnition 4.15
exists, for any j ∈ Ob H(X).
Proof. Since the morphism of gerbes F is locally surjective on objects, we can ﬁnd
an open covering U = {Uk}k∈K of X, and objects ik ∈ Ob G(Uk) that lift j|Uk .
By reﬁning it we can assume that U is N -acyclic. According to Lemma 5.10 there
exist elements gk0,k 1 that lift the elements hk0,k 1, in the notation of Construction
4.9. □
Now suppose we are given a morphism of central extensions of g erbes
(5.12) 1 /d47/d47N /d47/d47
/d15/d15
G
F /d47/d47
D
/d15/d15
H /d47/d47
E
/d15/d15
1
1 /d47/d47N′ /d47/d47G′ F ′
/d47/d47H′ /d47/d471
There is a homomorphism of sheaves of abelian groups D : N → N ′, and an induced
homomorphism
D : ˇH2(X, N ) → ˇH2(X, N′).
Proposition 5.13. Consider the morphism of central extension of gerbes (5.12).
(1) Let j ∈ Ob H(X) be such that the obstruction class cl2
F (j) is deﬁned, and
let j′ := E(j) ∈ Ob H′(X). Then the obstruction class cl2
F ′ (j′) is also
deﬁned, and moreover
cl2
F ′ (j′) = D
(
cl2
F (j)
)
in ˇH2(X, N′).
(2) Leti,j ∈ Ob G(X) and let h ∈ H(X)
(
F (i),F (j)
)
. We write i′ :=D(i) and
j′ := D(j) for the corresponding objects of G′(X), and h′ := E(h) for the
corresponding isomorphism i′ →j′. Then
cl1
F ′(h′) = D
(
cl1
F (h)
)
in ˇH1(X, N′).
Proof. Take the choices made in constructing the class cl 2
F (j) or cl 1
F (h), as the
case may be, and use the same open covering, and the images und er D,F of the
elements, to construct the class cl 2
F ′(j′) or cl 1
F ′ (h′). □
CENTRAL EXTENSIONS OF GERBES 29
Corollary 5.14. Consider the morphism of central extension of gerbes (5.12). As-
sume that E is an equivalence, and that there are enough N -acyclic open coverings.
Then the obstruction class cl2
F ′ (j′) is deﬁned for any j′ ∈ Ob H′(X).
Proof. There is some j ∈ Ob H(X) such that H′(X)
(
j′,E (j)
)
⁄= ∅. Now use
Propositions 5.13(1) and 4.16. □
