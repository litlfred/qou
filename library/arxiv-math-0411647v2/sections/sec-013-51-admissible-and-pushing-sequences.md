---
doc_id: arxiv-math-0411647v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS"
section_id: sec-013-51-admissible-and-pushing-sequences
section_title: "Admissible and pushing sequences"
section_number: 5.1
pages: 42-46
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear combination of indicators of many"
---
with moments of the Jucys–Murphy element J (or with products of such
moments) and we need an efﬁcient way to enumerate the summand s in
sums similar to (2.5). Conceptually the simplest way is to en umerate the
summands by sequences a1, . . . , a n ∈ A and which will be called admissi-
ble. However, it turns out that manipulating admissible seq uences is quite
complicated. It turns out that the suitable objects to enumerate summands in
(2.5) are pushing sequences. We will describe pushing seque nces in terms
of admissible sequences.
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 43
5.1.1. Admissible sequences. Map Φ as
~SA
. We recall that ∗ /∈ A. We say that
a sequence a1, . . . , a n is admissible if it contributes in the sum (2.5) or
equivalently if a1, . . . , a n ∈ A and
(5.1) [(a1∗) · · ·(an∗)](∗) = ∗.
The set of admissible sequences is a semigroup if for multiplication we take
the concatenation of sequences:
ab = (a1, . . . , a n, b 1, . . . , b o )
for admissible sequences a = (a1, . . . , a n) and b = (b1, . . . , b o ). The unit
is the empty sequence.
We consider a mapΦ as
SA from the set of admissible sequences to the sym-
metric group SA by setting
Φ as
SA : (a1, . . . , a n) ↦→ (a1∗) · · ·(an∗).
We can treat the right–hand side as a partial permutation of A with the
support {a1, . . . , a n}; in this way we obtain a map Φ as
~SA
from the set of
admissible sequences to the semigroup ~SA of partial permutations. It is
easy to check that both maps are homomorphisms of semigroups.
5.1.2. Pushing sequences. We say that no neighbor elements of a sequence
(p1, . . . , p n) are equal if pl ⁄= pl+1 holds for any 1 ≤ l ≤ n. We should
think that the elements of the sequence are arranged in a circ le and the
successor of pn is p1, therefore in the above deﬁnition the case l = n
means that we require pn ⁄= p1. In particular, it cannot happen that n = 1.
We will say that a sequence (p1, . . . , p n) is a pushing sequence if
p1, . . . , p n ∈ A ∪ {∗} and if p1 = ∗ and if no neighbor elements of
(p1, . . . , p n) are equal.
5.1.3. Commutative diagram. In the following we will construct functions
such that the following diagram commutes. Later on we shall equip pushing
sequences with a multiplicative structure in such a way that all maps will
become homomorphisms of semigroups.
(5.2)
44 PIOTR ´SNIADY
5.1.4. Map Φ as
ps. Let a = ( a1, . . . , a n), a1, . . . , a n ∈ A be an admissible
sequence. We assign to it a sequence of permutationsσ 1, . . . , σ n+1 ∈ SA ∪{∗}
deﬁned by
(5.3) σ l = (al∗)(al+1∗) · · ·(an∗)
and a sequence p = Φ as
ps(a) = ( p1, . . . , p n), p1, . . . , p n ∈ A ∪ {∗}deﬁned
by
(5.4) pl = σ − 1
l (∗).
Notice that since a is admissible hence p1 = ∗ and p1 = ∗ ⁄= an = pn.
Furthermore since σ l− 1 = (al− 1∗)σ l hence pl− 1 = σ − 1
l (al− 1) ⁄= σ − 1
l (∗) =
pl and p is a pushing sequence.
Equation (5.4) should explain the name of pushing sequences : imagine
that A ∪ {∗} is a set of some items and initially every item x is located
within a box which carries a label ‘ x’. In the process of computing the
product (a1∗) · · ·(an∗) (from the right to the left) we obtain a sequence of
partial products σ n, σ n− 1, . . . , σ 1: permutation σ l− 1 is obtained from σ l by
transposition of the item which is in the box labeled by ‘ ∗’ and the item
(which turns out to be the item pl− 1) from the box labeled by ‘ al− 1’. We
can think therefore that the item pl− 1 is pushing out the contents of the box
labeled by ‘∗’.
5.1.5. Map Φ ps
as. Let a pushing sequence p = ( p1, . . . , p n) be given.
By backward induction we will assign to it a unique pair of seq uences
(σ 1, . . . , σ n+1), Φ ps
as(p) = ( a1, . . . , a n), where σ 1, . . . , σ n+1 ∈ SA ∪{∗} and
(a1, . . . , a n) is an admissible sequence such that (5.3) and (5.4) are ful-
ﬁlled.
We start the construction by setting σ n+1 = e since it is the only choice
if we want (5.3) to be fulﬁlled for l = n + 1. If σ l is already deﬁned we set
al− 1 = σ l(pl− 1) and σ l− 1 = (al− 1∗)σ l. Again, it is the only choice that we
have since equations (5.3) and (5.4) imply
(5.5) al− 1 = (al− 1∗)(∗) = σ lσ − 1
l− 1(∗) = σ l(pl− 1).
Since p is pushing hence σ − 1
l (al− 1) = pl− 1 ⁄= pl = σ − 1
l (∗) therefore
a1, . . . , a n ⁄= ∗; furthermore [(a1∗) · · ·(an∗)]− 1(∗) = σ − 1
1 (∗) = p1 = ∗
hence a is admissible.
Equations (5.3) and (5.4) are indeed fulﬁlled by constructi on, therefore
Φ as
ps(Φ ps
as(p)) = p for every pushing sequence p. Furthermore the unique-
ness of the pair (a1, . . . , a n), (σ 1, . . . , σ n+1) implies that there exists at
most one preimage of p with respect to Φ as
ps. Therefore we proved the fol-
lowing result:
Proposition 5.1. Maps Φ ps
as and Φ as
ps are inverses of each other.
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 45
5.1.6. Map Φ ps
~SA
. The bijections between pushing and admissible se-
quences allow us to deﬁne the map Φ ps
~SA
in a unique way which makes
the diagram (5.2) commute.
Let p be a pushing sequence and a be the corresponding admissible se-
quence. Observe that if σ 1, . . . , σ n+1 is the sequence of permutations which
was constructed in Sections 5.1.4 and 5.1.5 then
(5.6) Φ ps
SA (p) = Φ as
SA (a) = σ 1.
In order to compute Φ ps
~SA
(p) we need to specify the support of this permuta-
tion. It is the support of Φ as
~SA
(a), namely {a1, . . . , a n} = {p1, . . . , p n} \ { ∗};
the inclusions which imply the latter equality follow directly from the con-
struction of the maps Φ as
ps and Φ ps
as. In Section 5.2.1 we shall compute Φ ps
~SA
and Φ ps
as more explicitly.
5.1.7. Multiplication of pushing sequences. The bijections between push-
ing and admissible sequences allow us to deﬁne multiplicati on of pushing
sequences in the unique way which makes arrows of (5.2) to be h omomor-
phisms of semigroups in such a way that the diagram commutes.
The exact form of this multiplication is given by the followi ng proposi-
tion
Proposition 5.2. Let p = ( p1, . . . , p k) and q = ( q1, . . . , q l) be pushing
sequences and let π = Φ ps
SA (q1, . . . , q l). Then
pq =
(
π − 1(p1), . . . , π − 1(pk), q 1, . . . , q l
)
.
Proof. Let p = Φ as
ps(a) and let σ a
1, . . . , σ a
k be the sequence of permuta-
tions constructed in Section 5.1.4 for a, i.e. σ a
m = ( am ∗) · · ·(ak∗) for
1 ≤ m ≤ k. Let b = Φ as
ps(q) and let σ b
1, . . . , σ b
l be the analogous sequence
of permutations obtained for b.
Let σ 1, . . . , σ k+l be the sequence of permutations obtained for the con-
catenated sequence ab. Observe that
σ m =
{
(bm − k∗) · · ·(bl∗) for m ≥ k + 1
(am ∗) · · ·(ak∗)(b1∗) · · ·(bl∗) for m ≤ k
=
{
σ b
m − k for m ≥ k + 1
σ a
m π for m ≤ k,
where π = (b1∗) · · ·(bl∗) = Φ as
SA (b) = Φ ps
SA (q).
46 PIOTR ´SNIADY
It follows that r = (r1, . . . , r n+l) = pq = Φ as
ps(ab) is given by
rm = σ − 1
m (∗) =
{
qm − n for m ≥ n + 1
π − 1(pm ) for m ≤ n
which ﬁnishes the proof. □
5.1.8. Invariance of the conjugacy class assigned to a pushing sequ ence.
For the purpose of this section let us forget about the set A and the distin-
guished element ∗. Let a sequence p = ( p1, . . . , p n) be given such that
no neighbor elements are equal: pl ⁄= pl+1 for all 1 ≤ l ≤ n. Now we
can deﬁne the distinguished element ∗ by setting ∗ = p1 and set A by
A = {p1, . . . , p n} \ { ∗}.
Let f be a one to one function deﬁned on the set {p1, . . . , p n}. We set
p ′ =
(
f(p1), . . . , f (pn)
)
, ∗ ′ = f(∗), A ′ = f(A).
Pushing sequence p deﬁnes a partial permutation Φ ps
~SA
(p) ∈ ~SA and the
pushing sequence p ′ deﬁnes a partial permutation Φ ps
~SA ′
(p ′) ∈~
SA ′.
Proposition 5.3. We use the above notations. Then
Φ ps
SA (p ′) = f ◦ Φ ps
SA (p) ◦ f− 1
and the support of Φ ps
~SA ′
(p ′) is equal to the image of the support of Φ ps
~SA
(p)
under the map f.
Proof. Let a1, . . . , a n and σ 1, . . . , σ n+1 be the sequences we considered
in Sections 5.1.4 and 5.1.5 and let a ′
1, . . . , a ′
n and σ ′
1, . . . , σ ′
n+1 be their
analogues obtained for the pushing sequence p ′.
We leave to the reader to show by backward induction that a ′
l = f(al)
and σ ′
l = f ◦ σ l ◦ f− 1 for every 1 ≤ l ≤ n. From (5.6) (and its analogue for
p ′) it follows that
Φ ps
SA (p ′) = f ◦ Φ ps
SA (p) ◦ f− 1.
Now it is enough to observe that the support of Φ ps
~SA ′
(p ′) is equal to A ′
and the support of Φ ps
~SA
(p) is equal to A. □
