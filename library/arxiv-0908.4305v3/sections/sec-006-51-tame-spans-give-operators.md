---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidification"
section_id: sec-006-51-tame-spans-give-operators
section_title: "Tame Spans Give Operators"
section_number: 5.1
pages: 45-50
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
doc_brief: "Higher Dimensional Algebra VII: Groupoidification — Groupoidiﬁcation is a form of categoriﬁcation in which vect or spaces are replaced by groupoids and linear operators are replaced by spans of"
---
To prove that a tame span gives a well-deﬁned operator, we begin wit h three
lemmas that are of some interest in themselves. We postpone to App endix
A some well-known facts about groupoids that do not involve the con cept of
degroupoidiﬁcation. This Appendix also recalls the familiar concept of ‘equiva-
lence’ of groupoids, which serves as a basis for this:
Deﬁnition 29. Two groupoids over a ﬁxed groupoid X, say v : Ψ → X and
w : Φ → X, are equivalent as groupoids over X if there is an equivalence
F : Ψ → Φ such that this diagram
Ψ
F /d47/d47
p
/d32/d32/d64/d64/d64/d64/d64/d64/d64 Φ
q
/d126/d126/d126 /d126/d126 /d126/d126 /d126/d126
X
commutes up to natural isomorphism.
Lemma 30. Letv : Ψ →X and w : Φ →X be equivalent groupoids over X. If
either one is tame, then both are tame, and Ψ
~
= Φ
~
.
Proof. This follows directly from Lemmas 62 and 63 in Appendix A.
Lemma 31. Given tame groupoids Φ and Ψ over X,
Φ + Ψ
~
= Φ
~
+ Ψ
~
.
45
More generally, given any collection of tame groupoids Ψ i overX, the coproduct∑
i Ψ i is naturally a groupoid over X, and if it is tame, then
∑
i
Ψ i
~
=
∑
i
Ψ
~
i
where the sum on the right hand side converges pointwise as a f unction on X.
Proof. The full inverse image of any object x ∈ X in the coproduct ∑
i Ψ i is
the coproduct of its fulll inverse images in each groupoid Ψ i. Since groupoid
cardinality is additive under coproduct, the result follows.
Lemma 32. Given a span of groupoids
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
we have
1. S(∑
i Ψ i) ≃ ∑
iSΨ i
2. S(Λ × Ψ) ≃ Λ ×SΨ
whenever vi : Ψ i →X are groupoids over X, v : Ψ →X is a groupoid over X,
and Λ is a groupoid.
Proof. To prove 1, we need to describe a functor
F :
∑
i
SΨ i →S(
∑
i
Ψ i)
that will provide our equivalence. For this, we simply need to describe for each
i a functor Fi : SΨ i → S(∑
i Ψ i). An object in SΨ i is a triple ( s,z,α ) where
s ∈ S, z ∈ Ψ i and α : p(s) → vi(z). Fi simply sends this triple to the same
triple regarded as an object of S(∑
i Ψ i). One can check that F extends to a
functor and that this functor extends to an equivalence of group oids over S.
To prove 2, we need to describe a functor F : S(Λ × Φ) → Λ ×SΦ. This
functor simply re-orders the entries in the quadruples which deﬁne the objects
in each groupoid. One can check that this functor extends to an eq uivalence of
groupoids over X.
Finally we need the following lemma, which simpliﬁes the computation of gr oupoid
cardinality:
Lemma 33. IfX is a tame groupoid with ﬁnitely many objects in each isomor-
phism class, then
|X| =
∑
x∈X
1
|Mor(x, −)|
where Mor(x, −) = ⋃
y∈X hom(x,y ) is the set of morphisms whose source is the
objectx ∈X.
46
Proof. We check the following equalities:
∑
[x]∈X
1
|Aut(x)| =
∑
[x]∈X
|[x]|
|Mor(x, −)| =
∑
x∈X
1
|Mor(x, −)|.
Here [x] is the set of objects isomorphic to x, and |[x]| is the ordinary cardinality
of this set. To check the above equations, we ﬁrst choose an isomo rphism
γy : x → y for each object y isomorphic to x. This gives a bijection from
[x] × Aut(x) to Mor(x, −) that takes ( y,f : x →x) to γyf : x →y. Thus
|[x]| |Aut(x)| = |Mor(x, −)|,
and the ﬁrst equality follows. We also get a bijection between Mor( y, −) and
Mor(x, −) that takes f : y →z to fγ y : x →z. Thus, |Mor(y, −)| = |Mor(x, −)|
whenevery is isomorphic to x. The second equation follows from this.
Now we are ready to prove the main theorem of this section:
Theorem 34. Given a tame span of groupoids
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
there exists a unique linear operator S
~
: RX → RY such that S
~
Ψ
~
=SΨ
~
for any
vector Ψ
~
obtained from a tame groupoid Ψ over X.
Proof. It is easy to see that these conditions uniquely determine S
~
. Suppose
ψ : X → R is any nonnegative function. Then we can ﬁnd a groupoid Ψ over X
such that Ψ
~
=ψ. So, S
~
is determined on nonnegative functions by the condition
thatS
~
Ψ
~
=SΨ
~
. Since every function is a diﬀerence of two nonnegative functions
and S
~
is linear, this uniquely determines S
~
.
The real work is proving that S
~
is well-deﬁned. For this, assume we have a
collection {vi : Ψ i →X}i∈I of groupoids over X and real numbers {αi ∈ R}i∈I
such that ∑
i
αi Ψ i
~
= 0. (9)
We need to show that ∑
i
αiSΨ i
~
= 0. (10)
We can simplify our task as follows. First, recall that a skeletal groupoid
is one where isomorphic objects are equal. Every groupoid is equivale nt to a
skeletal one. Thanks to Lemmas 30 and 65, we may therefore assu me without
loss of generality that S,X,Y and all the groupoids Ψ i are skeletal.
Second, recall that a skeletal groupoid is a coproduct of groupoid s with one
object. By Lemma 31, degroupoidiﬁcation converts coproducts o f groupoids
47
overX into sums of vectors. Also, by Lemma 32, the operation of taking we ak
pullback distributes over coproduct. As a result, we may assume wit hout loss
of generality that each groupoid Ψ i has one object. Write ∗i for the one object
of Ψ i.
With these simplifying assumptions, Equation 9 says that for any x ∈X,
0 =
∑
i∈I
αi Ψ i
~
([x]) =
∑
i∈I
αi |v−1
i (x)| =
∑
i∈J
αi
|Aut(∗i)| (11)
where J is the collection of i ∈I such that vi(∗i) is isomorphic to x. Since all
groupoids in sight are now skeletal, this condition implies vi(∗i) = x.
Now, to prove Equation 10, we need to show that
∑
i∈I
αiSΨ i
~
([y]) = 0
for any y ∈Y . But since the set I is partitioned into sets J, one for each x ∈X,
it suﬃces to show ∑
i∈J
αiSΨ i
~
([y]) = 0. (12)
for any ﬁxed x ∈X and y ∈Y .
To compute SΨ i
~
, we need to take this weak pullback:
SΨ i
π S
/d126/d126/d124/d124/d124/d124/d124/d124/d124/d124 π Ψ i
/d33/d33/d67/d67/d67/d67/d67/d67/d67/d67
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d33/d33/d67/d67/d67/d67/d67/d67/d67/d67 Ψ i
vi
/d125/d125/d122/d122/d122 /d122/d122/d122/d122/d122
Y X
We then have
SΨ i
~
([y]) = |(qπS)−1(y)|, (13)
so to prove Equation 12 it suﬃces to show
∑
i∈J
αi |(qπS)−1(y)| = 0. (14)
Using the deﬁnition of ‘weak pullback’, and taking advantage of the fa ct
that Ψ i has just one object, which maps down to x, we can see that an object
of SΨ i consists of an object s ∈S withp(s) = x together with an isomorphism
α : x → x. This object of SΨ i lies in ( qπS)−1(y) precisely when we also have
q(s) = y.
So, we may brieﬂy say that an object of ( qπS)−1(y) is a pair ( s,α ), where
s ∈S hasp(s) = x,q(s) = y, and α is an element of Aut( x). Since S is skeletal,
there is a morphism between two such pairs only if they have the same ﬁrst entry.
48
A morphism from ( s,α ) to (s,α ′) then consists of a morphism f ∈ Aut(s) and
a morphism g ∈ Aut(∗i) such that
x α /d47/d47
p(f )
/d15/d15
x
vi(g)
/d15/d15x
α ′
/d47/d47x
commutes.
A morphism out of ( s,α ) thus consists of an arbitrary pair f ∈ Aut(s),
g ∈ Aut(∗i), since these determine the target ( s,α ′). This fact and Lemma 33
allow us to compute:
|(qπS)−1(y)| =
∑
(s,α )∈(qπ S )−1(y)
1
|Mor((s,α ), −)|
=
∑
s∈p−1(y)∩q−1(y)
|Aut(x)|
|Aut(s)||Aut(∗i)|.
So, to prove Equation 14, it suﬃces to show
∑
i∈J
∑
s∈p−1(x)∩q−1(y)
αi|Aut(x)|
|Aut(s)||Aut(∗i)| = 0. (15)
But this easily follows from Equation 11. So, the operator S
~
is well deﬁned.
In Deﬁnition 61 we recall the natural concept of ‘equivalence’ for s pans of
groupoids. The next theorem says that our process of turning sp ans of groupoids
into linear operators sends equivalent spans to the same operator :
Theorem 35. Given equivalent spans
S
qS
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pS
/d31/d31/d64/d64/d64/d64/d64/d64/d64 T
qT
/d127/d127/d126/d126/d126/d126/d126/d126/d126 pT
/d32/d32/d64/d64/d64/d64/d64/d64/d64
Y X Y X
the linear operators S
~
and T
~
are equal.
Proof. Since the spans are equivalent, there is a functor providing an equiv alence
of groupoids F :S →T along with a pair of natural isomorphisms α :pS ⇒pTF
and β :qS ⇒qTF . Thus, the diagrams
S
/d31/d31/d64/d64/d64/d64/d64/d64/d64 Φ
/d126/d126/d126 /d126/d126 /d126/d126/d126 /d126 T
/d32/d32/d64/d64/d64/d64/d64/d64/d64 Φ
/d126/d126/d126/d126 /d126/d126 /d126/d126 /d126
X X
49
are equivalent pointwise. It follows from Lemma 65 that the weak pullb acks
SΨ and T Ψ are equivalent groupoids with the equivalence given by a functor
˜F : SΨ → T Ψ. From the universal property of weak pullbacks, along with F ,
we obtain a natural transformation γ : Fπ S ⇒πT ˜F . We then have a triangle
SΨT Ψ
ST
Y
˜F/d111/d111
π S
/d7/d7/d15/d15/d15/d15/d15/d15/d15/d15/d15/d15/d15
π T
/d23/d23/d47/d47/d47/d47/d47/d47/d47/d47/d47/d47/d47
qS
/d7/d7/d15/d15/d15/d15/d15/d15/d15/d15/d15/d15/d15
qT
/d23/d23/d47/d47/d47/d47/d47/d47/d47/d47/d47/d47/d47
F/d111/d111
γ
/d115/d123 /d111/d111/d111/d111/d111/d111
β
/d115/d123 /d111/d111/d111/d111/d111/d111
where the composite of γ and β is (qT ·γ)−1β : qSπS ⇒qTπT ˜F . Here · stands
for whiskering: see Deﬁnition 55.
We can now apply Lemma 63. Thus, for every y ∈Y , the full inverse images
(qSπS)−1(y) and ( qTπT )−1(y) are equivalent. It follows from Lemma 62 that
for each y ∈Y , the groupoid cardinalities |(qSπS)−1(y)| and |(qTπT )−1(y)| are
equal. Thus, the linear operators S
~
and T
~
are the same.
