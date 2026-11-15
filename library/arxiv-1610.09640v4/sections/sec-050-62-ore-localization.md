---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-050-62-ore-localization
section_title: "Ore Localization"
section_number: 6.2
pages: 114-124
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
here are [62], [49], [158], [75], [148] and [130]. The ﬁrst four references talk about
localization of categories; and the last two talk about noncommutative rings. It
seems that historically, this noncommutative calculus of fractions was discovered by
Ore and Asano in ring theory, around 1930. There was progress in the categorical
side, notably by Gabriel around 1960.
In this subsection we mostly follow the treatment of [148]; but we sometimes use
diagrams instead of formulas.
Deﬁnition 6.2.1. Let S be a multiplicatively closed set of morphisms in a category
A. A right Ore localization of A with respect to S is a pair (AS, Q), consisting of a
category AS and a functor Q : A →AS, having the following properties:
114
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(RO1) There is equality Ob(AS) = Ob(A), and Q is the identity on objects.
(RO2) For every s ∈S, the morphism Q(s) ∈AS is an isomorphism.
(RO3) Every morphism q ∈AS can be written as q = Q(a) ◦Q(s)−1 for some a ∈A
and s ∈S.
(RO4) Suppose a, b ∈A satisfy Q(a) = Q(b). Then a ◦s = b ◦s for some s ∈S.
The letters “RO” stand for “right Ore”. We refer to the expression q = Q(a) ◦
Q(s)−1 as a right fraction representation of q. Here is the left sided version of this
deﬁnition:
Deﬁnition 6.2.2. Let S be a multiplicatively closed set of morphisms in a category
A. A left Ore localization of A with respect to S is a pair (AS, Q), consisting of a
category AS and a functor Q : A →AS, having the following properties:
(LO1) There is equality Ob(AS) = Ob(A), and Q is the identity on objects.
(LO2) For every s ∈S, the morphism Q(s) ∈AS is an isomorphism.
(LO3) Every morphism q ∈AS can be written as q = Q(s)−1 ◦Q(a) for some a ∈A
and s ∈S.
(LO4) Suppose a, b ∈A satisfy Q(a) = Q(b). Then s ◦a = s ◦b for some s ∈S.
As in the right case, the letters “LO” stand for “left Ore”; and we refer to the
expression q = Q(s)−1 ◦Q(a) as a left fraction representation of q.
Remark 6.2.3. The results to follow in this subsection will be stated for right Ore
localizations only. They all have “left” versions, with identical proofs (just a matter
of reversing some arrows or compositions), and therefore they will be omitted.
To reinforce the last remark, we give:
Proposition 6.2.4. Let S be a multiplicatively closed set in a category A, let B be
a category, and let Q : A →B be a functor. Consider the multiplicatively closed
set Sop ⊆Aop and the functor Qop : Aop →Bop. The two conditions below are
equivalent:
(i) The pair (B, Q) is a left Ore localization of A with respect to S.
(ii) The pair (Bop, Qop) is a right Ore localization of Aop with respect to Sop.
Exercise 6.2.5. Prove Proposition 6.2.4.
Lemma 6.2.6. Let (AS, Q) be a right Ore localization, let a1, a2 ∈A and s1, s2 ∈S.
The following conditions are equivalent:
(i) Q(a1) ◦Q(s1)−1 = Q(a2) ◦Q(s2)−1 in AS.
(ii) There are b1, b2 ∈A s.t. a1 ◦b1 = a2 ◦b2, and s1 ◦b1 = s2 ◦b2 ∈S.
Proof.
(ii) ⇒(i): Since Q(si) and Q(si◦bi) are invertible, it follows that Q(bi) are invertible.
So
Q(a1) ◦Q(s1)−1 = Q(a1) ◦Q(b1) ◦Q(b1)−1 ◦Q(s1)−1
= Q(a2) ◦Q(b2) ◦Q(b2)−1 ◦Q(s2)−1 = Q(a2) ◦Q(s2)−1.
(i) ⇒(ii): By property (RO3) there are c ∈A and u ∈S s.t.
(6.2.7)
Q(s2)−1 ◦Q(s1) = Q(c) ◦Q(u)−1.
Rewriting this equation we get
(6.2.8)
Q(s1 ◦u) = Q(s2 ◦c).
It is given that Q(a1) = Q(a2) ◦Q(s2)−1 ◦Q(s1). Plugging (6.2.7) into it we obtain
Q(a1) = Q(a2) ◦Q(c) ◦Q(u)−1. Rearranging this equation we get Q(a1 ◦u) =
Q(a2 ◦c). By property (RO4) there is v ∈S s.t. a1 ◦u ◦v = a2 ◦c ◦v. Likewise,
from equation (6.2.8) and property (RO4), there is v′ ∈S s.t. s1 ◦u◦v′ = s2 ◦c◦v′.
115
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Again using property (RO3), there are d ∈A and w ∈S s.t. Q(v)−1 ◦Q(v′) =
Q(d) ◦Q(w)−1. Rearranging we get Q(v′ ◦w) = Q(v ◦d). By property (RO4) there
is w′ ∈S s.t. v′ ◦w ◦w′ = v ◦d◦w′. Deﬁne b1 := u◦v ◦d◦w′ and b2 := c◦v ◦d◦w′.
Then
s1 ◦b1 = s1 ◦u ◦v ◦d ◦w′ = s1 ◦u ◦v′ ◦w ◦w′
= s2 ◦c ◦v′ ◦w ◦w′ = s2 ◦b2,
and it is in S. Also
a1 ◦b1 = a1 ◦u ◦v ◦d ◦w′ = a2 ◦c ◦v ◦d ◦w′ = a2 ◦b2.
□
Proposition 6.2.9. A right Ore localization (AS, Q) is a localization in the sense
of Deﬁnition 6.1.2.
Proof. Say B is a category, and F : A →B is a functor such that F(s) is an
isomorphism for every s ∈S.
The uniqueness of a functor FS : AS →B satisfying FS ◦Q = F is clear from
property (RO3). We have to prove existence.
Deﬁne FS to be F on objects. For a morphism q in AS, property (RO3) says that
there is a right fraction presentation q = Q(a1) ◦Q(s1)−1, with a1 ∈A and s1 ∈S.
Let FS(q) := F(a1)◦F(s1)−1 in B. We have to prove that this is well-deﬁned, i.e. it
does not depend on the presentation. So suppose that q = Q(a2)◦Q(s2)−1 is another
right fraction presentation of q. Let b1, b2 ∈A be as in Lemma 6.2.6. Since F(si)
and F(si◦bi) are invertible, then so is F(bi). We get F(a2) = F(a1)◦F(b1)◦F(b2)−1
and F(s2) = F(s1) ◦F(b1) ◦F(b2)−1. Hence F(a2) ◦F(s2)−1 = F(a1) ◦F(s1)−1,
as required.
It remains to prove that FS is a functor. Since the identity idM of the object M
in AS can be presented as idM = Q(idM)◦Q(idM)−1, we see that FS(idM) = idF (M).
Next let q1 and q2 be morphisms in AS, such that the composition q2 ◦q1 exists
(i.e. the target of q1 is the source of q2). We have to show that FS(q2 ◦q1) equals
FS(q2) ◦FS(q1). Choose presentations qi = Q(ai) ◦Q(si)−1, so that
(6.2.10)
FS(q2) ◦FS(q1) = F(a2) ◦F(s2)−1 ◦F(a1) ◦F(s1)−1.
By property (RO3) there is a right fraction presentation
(6.2.11)
Q(s2)−1 ◦Q(a1) = Q(b) ◦Q(t)−1
for some b ∈A and t ∈S. Because Q(a1 ◦t) = Q(s2 ◦b), by (RO4) there is some
r ∈S such that a1 ◦t ◦r = s2 ◦b ◦r. Therefore F(a1 ◦t ◦r) = F(s2 ◦b ◦r), which
implies, by canceling the invertible morphism F(r) and rearranging, that
(6.2.12)
F(s2)−1 ◦F(a1) = F(b) ◦F(t)−1
in B.
Let us continue. Using equation (6.2.11) we have
q2 ◦q1 = Q(a2) ◦Q(s2)−1 ◦Q(a1) ◦Q(s1)−1
= Q(a2) ◦Q(b) ◦Q(t)−1 ◦Q(s1)−1 = Q(a2 ◦b) ◦Q(s1 ◦t)−1.
Using this presentation of q2 ◦q1, and the equality (6.2.12), we obtain
FS(q2 ◦q1) = F(a2 ◦b) ◦F(s1 ◦t)−1 = F(a2) ◦F(b) ◦F(t)−1 ◦F(s1)−1
= F(a2) ◦F(s2)−1 ◦F(a1) ◦F(s1)−1.
This is the same as (6.2.10).
□
Corollary 6.2.13. Let S be a multiplicatively closed set of morphisms in a category
A. Assume that these two assertions hold:
• The pair (B, Q) is either a right or a left Ore localization of A with respect
to S.
116
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
• The pair (B′, Q′) is either a right or a left Ore localization of A with respect
to S.
Then there is a unique isomorphism of localizations (B, Q) ∼= (B′, Q′).
Proof. By Proposition 6.2.9 (in its right or left versions, as the case may be), both
(B, Q) and (B′, Q′) are localizations in the sense of Deﬁnition 6.1.2.
Hence, by
Theorem 6.1.4, there is a unique isomorphism (B, Q) ∼= (B, Q′).
□
Deﬁnition 6.2.14. Let S be multiplicatively closed set of morphisms in a category
A. We say that S is a right denominator set if it satisﬁes these two conditions:
(RD1) (Right Ore condition) Given a ∈A and s ∈S, there exist b ∈A and t ∈S
such that a ◦t = s ◦b.
(RD2) (Right cancellation condition) Given a, b ∈A and s ∈S such that s◦a = s◦b,
there exists t ∈S such that a ◦t = b ◦t.
In the deﬁnition above the implicit assumption is that the sources and targets of
the morphisms match; e.g., in (RD1) the morphisms a and s have the same target.
Here are the diagrams illustrating the deﬁnition:
(6.2.15)
K
t
|
b
"
M
a
"
N
s
|
L
K
t
/ M
a
 
b
~
N
s
/ L
Now the left version of Deﬁnition 6.2.14:
Deﬁnition 6.2.16. Let S be multiplicatively closed set of morphisms in a category
A. We say that S is a left denominator set if it satisﬁes these two conditions:
(LD1) (Left Ore condition) Given a ∈A and s ∈S, there exist b ∈A and t ∈S
such that t ◦a = b ◦s.
(LD2) (Left cancellation condition) Given a, b ∈A and s ∈S such that a◦s = b◦s,
there exists t ∈S such that t ◦a = t ◦b.
Proposition 6.2.17. Let S be multiplicatively closed set of morphisms in a category
A. The two conditions below are equivalent:
(i) S is a left denominator set in A.
(ii) Sop is a right denominator set in Aop.
Exercise 6.2.18. Prove Proposition 6.2.17.
Here is the main theorem regarding Ore localization.
Theorem 6.2.19. The following conditions are equivalent for a category A and a
multiplicatively closed set of morphisms S ⊆A.
(i) The right Ore localization (AS, Q) exists.
(ii) S is a right denominator set.
The proof of Theorem 6.2.19 is after some preparation. The hard part is proving
that (ii) ⇒(i). The general idea is the same as in commutative localization: we
consider the set of pairs of morphisms A × S, and deﬁne a relation ∼on it, with
the hope that this is an equivalence relation, and that the quotient set AS will be
a category, and it will have the desired properties.
Let’s assume that S is a right denominator set. For any M, N ∈Ob(A) consider
the set
(A × S)(M, N) :=
a
L∈Ob(A)
A(L, N) × S(L, M).
117
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Remark 6.2.20. The set (A × S)(M, N) could be big, namely not an element of
the initial universe U. This would require the introduction of a larger universe, say
V, in which U is an element. And the resulting category AS will be a V-category.
This is the same issue we had in the proof of Theorem 6.1.4.
We will ignore this issue. Moreover, in many cases of interest (derived categories
where there are DG enhancements, such as the K-injective enhancement), there
will be an alternative presentation of AS as a U-category. We will refer to this when
we get to it.
An element (a, s) ∈(A × S)(M, N) can be pictured as a diagram
(6.2.21)
L
s
|
a
!
M
N
in A. This diagram will eventually represent the right fraction Q(a)◦Q(s)−1 : M →
N.
Deﬁnition 6.2.22. We deﬁne a relation ∼on the set A × S like this: (a1, s1) ∼
(a2, s2) if there exist b1, b2 ∈A s.t. a1 ◦b1 = a2 ◦b2 and s1 ◦b1 = s2 ◦b2 ∈S.
Note that the relation ∼imposes condition (ii) of Lemma 6.2.6. Here it is in a
commutative diagram, in which we have made the objects explicit:
(6.2.23)
K
b1
~
b2
 
L1
s1

a1
(
L2
s2
w
a2

M
N
The paths (i.e. morphisms) ending at M are in S.
Lemma 6.2.24. If S is a right denominator set, then the relation ∼is an equiva-
lence.
Proof. Reﬂexivity: take K := L and bi := idL : L →L. Symmetry is trivial.
Now to prove transitivity. Suppose we are given (a1, s1) ∼(a2, s2) and (a2, s2) ∼
(a3, s3). So we have the solid part of the ﬁrst diagram in (6.2.25), and it is com-
mutative. The morphisms ending at M are in S.
(6.2.25)
H
u
/ I
t
{
d
#
K
b1

b2
#
J
c2
|
c3

L1
s1

a1
(
L2
s2
}
a2
!
L3
s3
v
a3

M
N
H
b1◦t◦u

c3◦d◦u

L1
s1

a1
&
L3
s3
y
a3

M
N
By condition (RD1) applied to the morphisms K →M ←J there are t ∈S and
d ∈A s.t. (s3 ◦c3) ◦d = (s1 ◦b1) ◦t. Comparing the morphisms I →M in this
118
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
diagram, we see that
s2 ◦(b2 ◦t) = s1 ◦b1 ◦t = s3 ◦c3 ◦d = s2 ◦(c2 ◦d).
By (RD2) there is u ∈S s.t. (b2 ◦t) ◦u = (c2 ◦d) ◦u. So all morphisms H →M
are equal and belong to S, and all morphisms H →N are equal. Now delete the
object L2 and the arrows going through it. Then delete the objects I, J, K, but
keep the paths going through them. We get the second diagram in (6.2.25). It
is commutative, and all morphisms ending at M are in S. This is evidence for
(a1, s1) ∼(a3, s3).
□
Proof of Theorem 6.2.19.
Step 1. In this step we prove (i) ⇒(ii). Take a ∈A and s ∈S with the same
target.
Consider q := Q(s)−1 ◦Q(a).
By (RO3) there are b ∈A and t ∈S
s.t. q = Q(b) ◦Q(t)−1.
So Q(s ◦b) = Q(a ◦t).
By (RO4) there is u ∈S s.t.
(s◦b)◦u = (a◦t)◦u. We read this as s◦(b◦u) = a◦(t◦u), and note that t◦u ∈S.
So (RD1) holds.
Next a, b ∈A and s ∈S s.t. s ◦a = s ◦b. Then Q(s ◦a) = Q(s ◦b). But Q(s)
is invertible, so Q(a) = Q(b). By (RO4) there is t ∈S s.t. a ◦t = b ◦t. We have
proved (RD2).
Step 2. Now we assume that condition (ii) holds, and we deﬁne the morphism sets
AS(M, N), composition between them, and the identity morphisms.
For any M, N ∈Ob(A) let
AS(M, N) := (A × S)(M, N) / ∼,
the quotient set modulo the relation ∼from Deﬁnition 6.2.22, which is an equiva-
lence relation by Lemma 6.2.24.
We deﬁne composition like this. Given q1 ∈AS(M0, M1) and q2 ∈AS(M1, M2),
choose representatives (ai, si) ∈(A × S)(Mi−1, Mi).
We use the notation qi =
(ai, si) to indicate this. By (RD1) there are c ∈A and u ∈S s.t. s2 ◦c = a1 ◦u.
The composition q2 ◦q1 ∈AS(M0, M2) is deﬁned to be
q2 ◦q1 := (a2 ◦c, s1 ◦u) ∈(A × S)(M0, M2)).
The idea behind the formula can be seen in diagram (6.2.26).
(6.2.26)
K
u
}
c
!
L1
s1
}
a1
!
L2
s2
}
a2
!
M0
M1
M2
We have to verify that this deﬁnition is independent of the representatives. So
suppose we take other representatives qi = (a′
i, s′
i), and we choose morphisms u′, c′
to construct the composition. This is the solid part of the diagram (6.2.27), and it
is a commutative diagram. We must prove that
(a2 ◦c, s1 ◦u) = (a′
2 ◦c′, s′
1 ◦u′).
119
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(6.2.27)
J1
b1

b′
1
#
K
u
{
c
)
K′
u′
u
c′
#
J2
b2
{
b′
2

L1
s1

a1
)
L′
1
s′
1
|
a′
1
"
L2
s2
{
a2
"
L′
2
s′
2
u
a′
2

M0
M1
M2
There are morphisms bi, b′
i that are evidence for (ai, si) ∼(a′
i, s′
i). They are
depicted as the dashed arrows in (6.2.27). That whole diagram is commutative.
The morphisms J1 →M0, K →M0, K′ →M0 and J2 →M1 are all in S.
Choose v1 ∈S and d1 ∈A s.t. the ﬁrst diagram in (6.2.28) is commutative. This
can be done by (RD1).
(6.2.28)
I1
v1
~
d1
 
J1
b1
 
K
u
~
L1
I2
˜v
 ˜I2
˜v2
~
˜d2
 
K′
c′
 
J2
b′
2
}
L′
2
s′
2
!
M1
I2
v2
~
d2
 
K′
c′
 
J2
b′
2
~
L′
2
Consider the solid part of the middle diagram in (6.2.28). Since J2 →M1 is in
S, by (RD1) there are ˜v2 ∈S and ˜d2 ∈A s.t. the two paths ˜I2 →M1 are equal. By
(RD2) there is ˜v ∈S s.t. the two paths I2 →L′
2 are equal. We get the commutative
diagram in the middle of (6.2.28). Next, deﬁning d2 := ˜d2 ◦˜v and v2 := ˜v2 ◦˜v ∈S,
we obtain the third commutative diagram in (6.2.28).
We now embed the ﬁrst and third diagrams from (6.2.28) into the diagram
(6.2.27). This gives us the solid diagram in (6.2.29), and it is commutative. The
morphisms I1 →M0 belong to S.
(6.2.29)
H′′
w′′
/ H′
w′
/ H
w
z
e
$
I1
v1
{
d1

I2
v2

d2
#
J1
b1

b′
1
#
K
u
{
c
)
K′
u′
u
c′
#
J2
b2
{
b′
2

L1
s1

a1
)
L′
1
s′
1
|
a′
1
#
L2
s2
{
a2
"
L′
2
s′
2
u
a′
2

M0
M1
M2
120
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Choose w ∈S and e ∈A, starting at an object H, to ﬁll the diagram I1 →
M0 ←I2, using (RD1). The path H →I1 →M0 is in S, and all the paths H →M0
are equal. But we could have failure of commutativity in the paths H →L′
1 and
H →L2.
The two paths H →L′
1 in (6.2.29) satisfy
s′
1 ◦(b′
1 ◦v1 ◦w) = s′
1 ◦(u′ ◦v2 ◦e).
Therefore, by (RD2), there is w′ ∈S s.t.
(b′
1 ◦v1 ◦w) ◦w′ = (u′ ◦v2 ◦e) ◦w′.
Next, the two paths H′ →L2 satisfy
s2 ◦(c ◦d1 ◦w ◦w′) = s2 ◦(b2 ◦d2 ◦e ◦w′);
this is because we can take a detour through L′
1. Therefore, again by (RD2), there
is w′′ ∈S s.t.
(c ◦d1 ◦w ◦w′) ◦w′′ = (b2 ◦d2 ◦e ◦w′) ◦w′′.
Now all paths H′′ →M2 in (6.2.29) are equal. All paths H′′ →M0 are equal and
are in S.
Erase the objects M1, J1, J2 and all arrows touching them from (6.2.29). Then
erase H, H′, but keep the paths through them. We obtain the commutative diagram
(6.2.30).
(6.2.30)
I1
d1

H′′
w◦w′◦w′′
o
e◦w′◦w′′ / I2
v2

K
u
{
c
)
K′
u′
u
c′
#
L1
s1

L′
1
s′
1
{
L2
a2
#
L′
2
a′
2

M0
M2
This is evidence for
(a2 ◦c, s1 ◦u) ∼(a′
2 ◦c′, s′
1 ◦u′).
The proof that composition is well-deﬁned is done.
The identity morphism idM in AS of an object M is (idM, idM).
Step 3. We have to verify the associativity and the identity properties of compo-
sition in AS. Namely that AS is a category. This seems to be not too hard, given
Step 2, and we leave it as an exercise.
Step 4. The functor Q : A →AS is deﬁned to be Q(M) := M on objects, and
Q(a) := (a, idM) for a : M →N in A. We have to verify this is a functor... Again,
an exercise.
Step 5. Finally we verify properties (RO1)-(RO4). (RO1) is clear. The inverse of
Q(s) is (id, s), so (RO2) holds.
It is not hard to see that (a, s) = (a, id) ◦(id, s); this is (RO3).
If Q(a1) = Q(a2), then (a1, idM) ∼(a2, idM); so there are b1, b2 ∈A s.t. a1 ◦b1 =
a2 ◦b2 and id ◦b1 = id ◦b2 ∈S. Writing s := b1 ∈S, we get a1 ◦s = a2 ◦s. This
proves (RO4).
□
Exercise 6.2.31. Finish the details in the proof of Theorem 6.2.19.
121
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proposition 6.2.32 (Common Denominator). Let A be a category, let S be a right
denominator set in A, and let (AS, Q) be the right Ore localization. For every two
morphisms q1, q2 : M →N in AS there is a common right denominator. Namely
we can write qi = Q(ai) ◦Q(s)−1 for suitable ai ∈A and s ∈S.
Proof. Choose representatives qi = Q(a′
i) ◦Q(s′
i)−1. By (RD1) applied to L1 →
M ←L2, there are b ∈A and t ∈S such that the part of diagram (6.2.33) that lies
above M is commutative:
(6.2.33)
L1
s′
1

a′
1
)
L
t
o
b
/ L2
s′
2
u
a′
2

M
N
Write s := s′
1 ◦t = s′
2 ◦b, a1 := a′
1 ◦t and a2 := a′
2 ◦b. By Lemma 6.2.6 we get
qi = Q(ai) ◦Q(s)−1.
□
Proposition 6.2.34. Let A be a category, let S ⊆A be a right denominator set, and
let A′ ⊆A be a full subcategory. Deﬁne S′ := A′ ∩S. Assume these two conditions
hold:
(i) S′ is a right denominator set in A′.
(ii) Let M ∈Ob(A). If there exists a morphism s : M →L′ in S with L′ ∈
Ob(A′), there exists a morphism t : K′ →M in S with K′ ∈Ob(A′).
Then the canonical functor A′
S′ →AS is fully faithful.
Proof. Let’s denote the inclusion functor by F : A′ →A. We want to prove that its
localization FS′ : A′
S′ →AS is fully faithful.
Step 1. Let L′
1, L′
2 ∈Ob(A′), and let q : L′
1 →L′
2 be a morphism in AS. Choose a
presentation q = Q(a) ◦Q(s)−1 with s : M →L′
1 a morphism in S and a : M →L′
2
a morphism in A. This is possible because S is a right denominator set in A. By
condition (ii) we can ﬁnd a morphism t : K′ →M in S with K′ ∈Ob(A′). See next
diagram.
K′
t
/ M
s
~
a
 
L′
1
q
/ L′
2
Then q = Q(a ◦t) ◦Q(s ◦t)−1. But s ◦t ∈S′ and a ◦t ∈A′, so q is in the image of
the functor FS′. We see that FS′ is full.
Step 2. Let p′, q′ : L′
1 →L′
2 be morphisms in A′
S′ such that FS′(p′) = FS′(q′). Let
us denote the localization functor of A′ by Q′ : A′ →A′
S′. Because S′ is a right
denominator set in A′, and using Proposition 6.2.32, we can ﬁnd presentations
p′ = Q′(a′) ◦Q′(s′)−1 and q′ = Q′(b′) ◦Q′(s′)−1 with morphisms s′ : N ′ →L′
1 in S′
and a′, b′ : N ′ →L′
2 in A′. Next, since FS′(p′) = FS′(q′), Lemma 6.2.6 tells us that
there are morphisms u, v : M →N ′ in A s.t. a′ ◦u = b′ ◦v, and s′ ◦u = s′ ◦v ∈S.
Condition (ii), applied to the morphism s′ ◦u : M →L′
1, says that there is a
morphism t : K′ →M in S with source K′ ∈Ob(A′). See diagram below.
K′
t
/ M
u,v / N ′
s′
~
a′,b′
 
L′
1
p′,q′
/ L′
2
122
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Then we have
p′ = Q′(a′ ◦u ◦t) ◦Q′(s′ ◦u ◦t)−1
= Q′(b′ ◦u ◦t) ◦Q′(s′ ◦u ◦t)−1 = q′.
This proves that FS′ is faithful.
□
In the next subsection we study Ore localization of linear categories, and give
rings as examples (see Examples 6.3.6 and 6.3.5).
And in Section 7 we study
localization of triangulated categories. Here is a nonlinear example.
Example 6.2.35. Fix a base commutative ring K and a topological space (or,
more generally, a site) X. Let KX be the constant sheaf of rings K on X. Consider
the category DGRng≤0
sc /KX of sheaves of commutative DG KX-rings on X (see
Deﬁnition 3.3.4 and Remark 12.8.22).
For the sake of brevity let us just write
DGRngX := DGRng≤0
sc /KX.
The localization of DGRngX with respect to the quasi-isomorphisms in it is called
the derived category of commutative DG KX-rings, and the notation is D(DGRngX).
The categorical localization functor is Q : DGRngX →D(DGRngX), and it is the
identity on objects. (The unfortunate tradition in homotopy theory is to call such
a localization the “homotopy category”, and to denote it by “Ho(DGRngX)”.)
As explained in the lecture notes [179], every DG KX-ring A admits a semi-
pseudo-free resolution ˜
A →A in DGRngX. The semi-pseudo-free DG KX-rings have
good lifting properties. Indeed, they behave like coﬁbrant objects in a Quillen model
structure (even though there does not seems to be such a structure on DGRngX,
except when X is a discrete space).
There is a congruence on the category DGRngX, called the quasi-homotopy re-
lation. (It turns out that this idea was already known to some homotopy theorists,
see Remark 6.2.37 below.) Let us denote by K(DGRngX) the homotopy category,
which is the quotient of DGRngX modulo this congruence. So there is a functor
P : DGRngX →K(DGRngX), which is the identity on objects, and it sends a DG
ring homomorphism to its quasi-homotopy class.
The functors Q and P ﬁt into this commutative diagram:
(6.2.36)
DGRngX
P
/
Q

K(DGRngX)
¯Q
/ D(DGRngX)
The functor ¯Q is a faithful right Ore localization. The proof relies on the lifting
properties of semi-pseudo-free DG KX-rings. See Remark 12.8.22 for related mate-
rial.
Remark 6.2.37. Suppose C is a category, with a given multiplicatively closed set
of morphisms S ⊆C. If C admits a Quillen model structure for which S is the
set of weak equivalences, then there is automatically a calculus of fractions for the
localization functor Q : C →CS.
For instance, suppose that all objects of C are ﬁbrant. In this case C is called
a category of ﬁbrant objects. Then there is a congruence relation H on C, and a
commutative diagram
C
P
/
Q

C / H
¯Q
/ CS
in which, like in (6.2.36), the functor P is full, and the functor ¯Q is a right Ore
localization. These facts are explained in [115] (search for the emphasized text in
this remark).
123
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Remark 6.2.38. This is a continuation of Remark 3.8.22 on strictly unital A∞
categories, and it is related to Example 6.2.35 and Remark 6.2.37 above, and to
Remark 12.8.21 below. The references are [83] and [37]. Recall that the base ring
K is a ﬁeld.
Let A and B be A∞categories, i.e. objects of the category A∞Cat.
An A∞
functor F : A →B is called a quasi-equivalence if H(F) : H(A) →H(B) is an
equivalence of graded categories. The derived category of A∞Cat is the localization
D(A∞Cat) of A∞Cat with respect to the quasi-equivalences. (As mentioned above,
the tradition is to call D(A∞Cat) the “homotopy category” of A∞Cat, and to denote
it by “Ho(A∞Cat)”.) There is a localization functor Q : A∞Cat →D(A∞Cat), which
is the identity on objects.
Suppose F, F ′ : A →B are A∞functors.
So F and F ′ are objects of the
A∞category A∞Fun(A, B). We say that F and F ′ are A∞homotopic if they are
isomorphic in the category H0 A∞Fun(A, B)

, in which case we write F ≈F ′.
Deﬁne K(A∞Cat) to be the quotient of A∞Cat modulo the relation ≈. There is
a full functor P : A∞Cat →K(A∞Cat), which is the identity on objects. An A∞
functor F : A →B is called an A∞equivalence if it is an isomorphism in K(A∞Cat).
This means that there is an A∞functor G : B →A, such that G ◦F ≈IdA and
F ◦G ≈IdB. There is a commutative diagram
(6.2.39)
A∞Cat
P
/
Q

K(A∞Cat)
¯Q
/ D(A∞Cat)
An important theorem (see [94, Theorem 9.2.0.4 ]) says that an A∞functor F
is a quasi-equivalence iﬀit is an A∞equivalence. This implies that the functor ¯Q
in diagram (6.2.39) is an isomorphism of categories.
It is worthwhile to mention that the category A∞Cat does not have a Quillen
model structure (for which the weak equivalences are the quasi-equivalences).
Let DGCat be the category of K-linear DG categories, where the morphisms
are the DG functors (see Deﬁnition 3.5.1).
There is a fully faithful embedding
DGRng /c K →DGCat, since the DG rings (see Deﬁnition 3.3.2) are the single-
object DG categories. Because an A∞category whose higher operations vanish is
a DG category, there is a faithful (but not full) embedding DGCat →A∞Cat. The
derived category of DGCat is the localization D(DGCat) of DGCat with respect to
the quasi-equivalences in it. (Once more, the traditional notation for D(DGCat) is
“Ho(DGCat)”.) The embedding of DGCat into A∞Cat induces a functor D(DGCat)
→D(A∞Cat), and this is an equivalence. Together with the equivalence ¯Q from
(6.2.39), this implies that every morphism F : A →B in D(DGCat) can be repre-
sented by an A∞functor ˜F : A →B, which is unique up to a unique isomorphism
in K(A∞Cat).
Moreover, the category D(DGCat) is symmetric monoidal, with tensor operation
A ⊗B. It turns out that the DG category A∞Fun(A, B) is the internal Hom object,
making D(DGCat) into a closed monoidal category.
