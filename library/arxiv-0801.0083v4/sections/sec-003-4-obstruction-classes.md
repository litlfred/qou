---
doc_id: arxiv-0801.0083v4
doc_title: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI"
section_id: sec-003-4-obstruction-classes
section_title: "Obstruction Classes"
section_number: 4
pages: 19-25
source_pdf: 0801.0083v4.pdf
source_sha256: 8e38b9e56d246709
doc_brief: "CENTRAL EXTENSIONS OF GERBES AMNON YEKUTIELI — W e introduce the notion of central extension of gerbes on a to po- logical space X."
---
We ﬁx a topological space X. Given a sheaf N of abelian groups on X, and an
open covering U = {Uk}k∈K ofX, there are the Čech cohomology groups ˇHp(U, N )
for p ≥ 0. Passing to the limit over all such open coverings we obtain the Čech
cohomology groups ˇHp(X, N ).
From here until the end of this section we consider a central e xtension of gerbes
(4.1) 1 → N → G
F
− →H → 1
on X (see Deﬁnition 3.21 and Proposition 3.19).
20 AMNON YEKUTIELI
Construction 4.2. Let i,j ∈ Ob G(X), and let h ∈ H(X)
(
F (i),F (j)
)
. Since F
is a weak epimorphism, there exists an open covering U = {Uk}k∈K of X, such
that for every k ∈K there is an isomorphism gk ∈ G(Uk)(i,j ) with F (gk) = h. For
everyk0,k 1 ∈K we deﬁne
gk0,k 1 :=g−1
k1 ◦gk0 ∈ G(Uk0,k 1 )(i,i ).
Since F (gk0,k 1 ) = 1 we see that in fact gk0,k 1 ∈ N (Uk0,k 1). An easy calculation
shows that the collection
(4.3) c := {gk0,k 1}k0,k 1∈K
is a Čech 1-cocycle for the covering U with values in the sheaf of groups N .
Lemma 4.4. Let i,j ∈ Ob G(X) and let h ∈ H(X)
(
F (i),F (j)
)
. Suppose that c
and c′ are 1-cocycles with values in N , for open coverings U and U′, obtained as
in Construction 4.2, for the same isomorphism h. Then their Čech cohomology
classes [c], [c′] ∈ ˇH1(X, N ) are equal.
Proof. Say U′ = {U′
k}k∈K ′. Suppose that in the course of constructing the cocycle
c′ we chose, for every k ∈K′, an isomorphism g′
k ∈ G(U′
k)(i,j ) with F (g′
k) = h. So
g′
k0,k 1 =g′−1
k1 ◦g′
k0 and c′ = {g′
k0,k 1}k0,k 1∈K ′.
Take some open covering V = {Vl}l∈L ofX which reﬁnes both U and U′. Thus
there are functions φ :L →K andφ′ :L →K′, such that Vl ⊂Uφ (l) andVl ⊂U′
φ ′(l)
for all l ∈L. We get cocycles
φ∗(c) := {gφ (l0),φ (l1)}l0,l 1∈L
and
φ′∗(c′) := {g′
φ ′(l0),φ ′(l1)}l0,l 1∈L.
For any l ∈L let
fl :=g−1
φ (l) ◦g′
φ ′(l) ∈ G(Vl)(i,i ).
Now
F (fl) = F (gφ (l))−1 ◦F (g′
φ ′(l)) = h−1 ◦h = 1.
So b := {fl}l∈L is a 0-cochain with values in N .
Take any l0,l 1 ∈L. Then
(f−1
l1 ◦fl0) ◦gφ (l0),φ (l1)
= (g−1
φ (l1) ◦g′
φ ′(l1))−1 ◦ (g−1
φ (l0) ◦g′
φ ′(l0)) ◦ (g−1
φ (l1) ◦gφ (l0))
=g′−1
φ ′(l1) ◦g′
φ ′(l0) =g′
φ ′(l0),φ ′(l1).
Denoting the Čech coboundary operator by d, we see that
d(b) ·φ∗(c) = φ′∗(c′).
□
In view of this lemma, the following deﬁnition makes sense.
Deﬁnition 4.5. Let i,j ∈ Ob G(X), and let h ∈ H(X)
(
F (i),F (j)
)
. Take any
1-cocycle c as in Construction 4.2. We deﬁne the obstruction class
cl1
F (h) := [c] ∈ ˇH1(X, N ).
CENTRAL EXTENSIONS OF GERBES 21
Theorem 4.6 (Obstruction to lifting isomorphisms) . Consider a central extension
of gerbes
1 → N → G
F
− →H → 1.
Let i,j ∈ Ob G(X), and let h ∈ H(X)
(
F (i),F (j)
)
. Then there exists an isomor-
phism g ∈ G(X)(i,j ) satisfying F (g) = h if and only if
cl1
F (h) = 1.
In other words, the class cl 1
F (h) is the obstruction to lifting the isomorphism
h :F (i) →F (j) to an isomorphism g :i →j.
Proof. First assume there exists a lifting g. We construct a cocycle c as follows:
for the open covering U = {Uk}k∈K we take K := {0} andU0 :=X. We then take
g0 :=g. The resulting cocycle is c is trivial, and hence cl 1
F (h) = 1.
Conversely, assume that cl 1
F (h) = 1. Let c′ = {g′
k0,k 1}k0,k 1∈K be a 1-cocycle
that represents cl 1
F (h) on some open covering U . Say g′
k ∈ G(Uk)(i,j ) are the
isomorphisms chosen in the construction of c′, so that g′
k0,k 1 =g′−1
k1 ◦g′
k0 .
By replacing U with a suitable reﬁnement, we can assume that c′ is a cobound-
ary; i.e. there is a 0-cochain b := {fk}k∈K with values in N such that c′ = d(b).
Deﬁne
gk :=g′
k ◦f−1
k ∈ G(Uk)(i,j ).
A calculation shows that {gk}k∈K is a 0-cocycle with values in the sheaf of sets
G(i,j ). Hence it glues to a global isomorphism g ∈ G(X)(i,j ). And by construction
we have F (g) = h. □
Corollary 4.7. Given a central extension of gerbes as above, let i,j ∈ Ob G(X).
Then G(X)(i,j ) ⁄= ∅ if and only if there exists some h ∈ H(X)
(
F (i),F (j)
)
such
that cl1
F (h) = 1 .
Proof. This is an immediate consequence of the theorem. □
Remark 4.8. In an earlier version of this paper we claimed that cl 1
F (h) = cl 1
F (h′)
for any h,h ′ ∈ H(X)
(
F (i),F (j)
)
. However the referee discovered a mistake in our
proof.
Construction 4.9. Letj ∈ Ob H(X). Choose some open covering U = {Uk}k∈K
of X. For every k ∈ K choose, if possible, an object ik ∈ Ob G(Uk) and an
isomorphism
hk ∈ H(Uk)
(
F (ik),j
)
.
For every (k0,k 1) ∈K ×K deﬁne
hk0,k 1 :=h−1
k1 ◦hk0 ∈ H(Uk0,k 1 )
(
F (ik0 ),F (ik1 )
)
.
Choose, if possible, an isomorphism
gk0,k 1 ∈ G(Uk0,k 1 )(ik0,i k1)
that lifts hk0,k 1 , i.e. F (gk0,k 1) = hk0,k 1. Deﬁne
gk0,k 1,k 2 :=g−1
k0,k 2
◦gk1,k 2 ◦gk0,k 1 ∈ G(Uk0,k 1,k 2 )(ik0,i k0).
Thus we get a collection of elements
(4.10) c := {gk0,k 1,k 2 }k0,k 1,k 2∈K.
22 AMNON YEKUTIELI
Lemma 4.11. The collection c from this construction is a Čech 2-cocycle with
values in N .
Proof. Since F (gk0,k 1,k 2 ) = 1 it follows that gk0,k 1,k 2 ∈ N (Uk0,k 1,k 2).
Let us now calculate the value of the coboundary of c in N (Uk0,k 1,k 2,k 3), using
the fact that N is central in G:
gk1,k 2,k 3 ◦g−1
k0,k 2,k 3 ◦gk0,k 1,k 3 ◦g−1
k0,k 1,k 2
=gk1,k 2,k 3 ◦ (g−1
k0,k 3 ◦gk2,k 3 ◦gk0,k 2 )−1
◦ (g−1
k0,k 3 ◦gk1,k 3 ◦gk0,k 1 ) ◦ (g−1
k0,k 2 ◦gk1,k 2 ◦gk0,k 1 )−1
=gk1,k 2,k 3 ◦g−1
k0,k 2 ◦g−1
k2,k 3 ◦gk0,k 3
◦g−1
k0,k 3 ◦gk1,k 3 ◦gk0,k 1 ◦g−1
k0,k 1 ◦g−1
k1,k 2 ◦gk0,k 2
=g−1
k0,k 2 ◦g−1
k2,k 3 ◦gk1,k 3 ◦gk1,k 2,k 3 ◦g−1
k1,k 2 ◦gk0,k 2
=g−1
k0,k 2 ◦g−1
k2,k 3 ◦gk1,k 3
◦ (g−1
k1,k 3 ◦gk2,k 3 ◦gk1,k 2 ) ◦g−1
k1,k 2 ◦gk0,k 2
= 1.
□
Lemma 4.12. Letj ∈ Ob H(X). Suppose that c and c′ are 2-cocycles with values
in N , for open coverings U and U′, obtained as in Construction 4.9. Then their
Čech cohomology classes [c], [c′] ∈ ˇH2(X, N ) are equal.
Proof. The cocycle c′ is constructed using some open covering U′ = {U′
k}k∈K ′,
objectsi′
k ∈ Ob G(U′
k) that lift j, isomorphisms h′
k ∈ H(U′
k)
(
F (i′
k),j
)
, and isomor-
phismsg′
k0,k 1 ∈ G(U′
k0,k 1 )(i′
k0,i ′
k1) that lift h′
k0,k 1 :=h′−1
k1 ◦h′
k0 .
The proof proceeds in four steps, labeled (a)-(d).
(a) Suppose U′ = U , i′
k =ik and h′
k =hk, but we choose some other lifting g′
k0,k 1
of hk0,k 1. The 2-cocycle c′ = {g′
k0,k 1,k 2 } is
(4.13) g′
k0,k 1,k 2 :=g′−1
k0,k 2 ◦g′
k1,k 2 ◦g′
k0,k 1 ∈ G(Uk0,k 1,k 2 )(ik0,i k0).
Now there are unique elements
nk0,k 1 ∈ N (Uk0,k 1)(ik0,i k0 )
such that
g′
k0,k 1 =nk0,k 1 ◦gk0,k 1.
Consider the Čech 1-cochain b := {nk0,k 1} with values in N . A little calculation
shows that
g′
k0,k 1,k 2 =gk0,k 1,k 2 ◦ (n−1
k0,k 2 ◦nk0,k 1 ◦nk1,k 2);
so that c′ =c · d(b). We see that c and c′ have the same cohomology class.
(b) Next suppose U′ = U and i′
k = ik, but we choose other isomorphisms h′
k ∈
H(Uk)(F (ik),j ). Deﬁne
h′
k0,k 1 :=h′−1
k1 ◦h′
k0 ∈ H(Uk0,k 1 )(F (ik0 ),F (ik1 )).
Consider the elements
fk :=h−1
k ◦h′
k ∈ H(Uk)(F (ik),F (ik)).
CENTRAL EXTENSIONS OF GERBES 23
Take some open covering V = {Vl}l∈L that reﬁnes U , with comparison function
φ : L → K, such that for every l ∈ L the isomorphism fφ (l) lifts to some gl ∈
G(Vl)(iφ (l),i φ (l)). This is possible since F is locally surjective on isomorphism
sheaves. By replacing U with V , we can now assume that each fk lifts to some
gk ∈ G(Uk)(ik,i k).
Now let us deﬁne
g′′
k0,k 1 :=g−1
k1 ◦gk0,k 1 ◦gk0 ∈ G(Uk0,k 1)(ik0,i k1 ).
Theng′′
k0,k 1 is a lifting of h′
k0,k 1 . Proceeding as in equation (4.13), we obtain a Čech
2-cocycle c′′ = {g′′
k0,k 1,k 2 }. However, it is easy to see that
g′′
k0,k 1,k 2 =g−1
k0 ◦gk0,k 1,k 2 ◦gk0.
Since gk0,k 1,k 2 is central in G it follows that in fact g′′
k0,k 1,k 2 = gk0,k 1,k 2 , so that
c′′ =c. On the other hand, from step (a) we see that [ c′′] = [c′] in ˇH2(X, N ).
(c) Now suppose U′ = U , but we choose another object i′
k ∈ Ob G(Uk) for each k.
Take some open covering V = {Vl}l∈L that reﬁnes U , with comparison function
φ :L →K, such that for every l ∈L one has
G(Vl)(iφ (l),i ′
φ (l)) ⁄= ∅.
This can be done because G is locally connected. After replacing U with V , we
can assume that there is some fk ∈ G(Uk)(ik,i ′
k) for every k ∈K.
In view of steps (a-b) we might as well take
h′
k :=hk ◦F (fk)−1 ∈ H(Uk)
(
F (i′
k),j
)
,
and then lift
(4.14) h′
k0,k 1 :=h′−1
k1 ◦h′
k0 ∈ H(Uk0,k 1 )
(
F (i′
k0 ),F (i′
k1 )
)
to
g′
k0,k 1 :=fk1 ◦gk0,k 1 ◦f−1
k0 ∈ G(Uk0,k 1)(i′
k0,i ′
k1 ).
The resulting 2-cocycle c′ = {g′
k0,k 1,k 2} deﬁned as in (4.13) will satisfy
g′
k0,k 1,k 2 =f−1
k0
◦gk0,k 1,k 2 ◦fk0.
Because N is central we get c′ =c.
(d) Finally let’s see what happens when we take a new open cove ring U′ = {Uk}k∈K ′
of X, for which we can construct a cocycle c′. Let V = {Vl}l∈L be a common
reﬁnement, namely there are functions φ : L → K and φ′ : L → K′, such that
Vl ⊂ Uφ (l) and Vl ⊂ U′
φ ′(l) for all l ∈ L. Let φ∗(c) and φ′∗(c′) be the pullback 2-
cocycles on the open covering V . These are both cocycles that are constructed like
in Construction 4.9, for the obvious choices of objects etc. By steps (a-c) we know
that [φ∗(c)] = [φ′∗(c′)]. But on the other hand [ φ∗(c)] = [c] and [φ′∗(c′)] = [c′]. □
The lemma justiﬁes the next deﬁnition.
Deﬁnition 4.15. Letj ∈ Ob H(X). If there exists a 2-cocycle c as in Construction
4.9, for some open covering U , then we deﬁne the obstruction class to lifting objects
to be
cl2
F (j) := [c] ∈ ˇH2(X, N ).
Otherwise we say that this obstruction class is undeﬁned.
24 AMNON YEKUTIELI
In Section 5 we shall see suﬃcient conditions for the obstruc tion class cl 2
F (j) to
be deﬁned.
Proposition 4.16. Let j ∈ Ob H(X) be such that the obstruction class cl2
F (j) is
deﬁned. Suppose j′ ∈ Ob H(X) is such that H(X)(j,j ′) ⁄= ∅. Then the obstruction
class cl2
F (j′) is also deﬁned, and moreover
cl2
F (j′) = cl 2
F (j).
What the proposition says is that two isomorphic objects hav e the same obstruc-
tion class.
Proof. We want to construct a Čech 2-cocycle c′, starting with j′ instead of j. Take
anyf ∈ H(X)(j,j ′). Using this isomorphism we may deﬁne
h′
k :=f ◦hk ∈ H(Uk)(F (ik),j ′),
where ik is the lifting of j that was used in the construction of c, and hk ∈
H(Uk)(F (ik),j ) is the isomorphism that was chosen.
Let
h′
k0,k 1 :=h′−1
k1 ◦h′
k0 ∈ H(Uk0,k 1 )(F (ik0 ),F (ik1 )).
Then h′
k0,k 1 =hk0,k 1 ; so continuing with Construction 4.9 we get a cocycle c′ that
equalsc. □
Theorem 4.17 (Obstruction to lifting objects) . Consider a central extension of
gerbes
1 → N → G
F
− →H → 1.
Let j ∈ Ob H(X) be such that the obstruction class cl2
F (j) is deﬁned. Then there
exists an object i ∈ Ob G(X) with
H(X)
(
F (i),j
)
⁄= ∅
if and only if
cl2
F (j) = 1.
What the theorem says is that cl 2
F (j) is the obstruction to lifting j to an object
of G(X).
Proof. Assumej lifts to an object i ∈ Ob G(X). So there exists some isomorphism
h ∈ H(X)(F (i),j ). In Construction 4.9 we may choose ik := i|Uk ∈ Ob G(Uk).
Having done so, we take
hk :=h|Uk ∈ H(Uk)(F (ik),j ).
Proceeding with the construction, we get
hk0,k 1 = 1 ∈ G(Uk0,k 1 )(F (i),F (i)),
which can then be lifted to
gk0,k 1 = 1 ∈ G(Uk0,k 1 )(i,i ).
The resulting 2-cocycle c = {gk0,k 1,k 2 } is trivial.
Conversely, suppose cl 2
F (j) = 1. From construction 4.9 and the choices made
there we get a a 2-cocycle c = {gk0,k 1,k 2} with values in N , on some open covering
U . By replacing U with a suitable reﬁnement, we may assume it is a coboundary.
Namely there is a 1-cochain b = {fk0,k 1 } with values in N , such that c = d(b).
CENTRAL EXTENSIONS OF GERBES 25
Consider the isomorphisms
g′
k0,k 1 :=gk0,k 1 ◦f−1
k0,k 1 ∈ G(Uk0,k 1 )(ik0,i k1),
where gk0,k 1 are the isomorphisms chosen when constructing the cocycle c. Then
{g′
k0,k 1 } is a 1-cocycle. Since G is a stack, the collection of objects {ik}k∈K can
be glued. I.e. there is an object i ∈ Ob G(X), and isomorphisms g′
k ∈ G(Uk)(ik,i ),
such that
g′−1
k1 ◦g′
k0 =g′
k0,k 1.
Deﬁne
ek :=F (g′
k) ◦h−1
k ∈ H(Uk)
(
j,F (i)
)
.
Then one checks that
ek0 =ek1 ∈ H(Uk0,k 1)
(
j,F (i)
)
.
The sheaf property says that these glue to an isomorphism e ∈ H(X)
(
j,F (i)
)
. □
Remark 4.18. If we were to use open hypercoverings in Construction 4.9, th en
the obstruction class cl 2
F (j) would always be deﬁned, as an element of H 2(X, N ).
However the technicalities involved in proving the corresponding version of Theorem
4.17 would be enormous. Since Construction 4.9 works in the c ases that interest
us, we chose to limit ourselves to this weaker approach.
Remark 4.19. L. Breen [private communication] proposed looking at the th e cen-
tral extension of gerbes (4.1) in the following way: G is a gerbe over H, with band
N . Perhaps this point of view can yield a stronger version of Th eorem 4.17.
