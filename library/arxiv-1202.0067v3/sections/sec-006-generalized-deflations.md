---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN\u2013NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON"
section_id: sec-006-generalized-deflations
section_title: "Generalized deflations"
section_number: 6
pages: 22-30
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON — 8 sections: Introduction; Deflation by averaging; Skew characters"
---
In this section we discuss deflation with respect to an arbitrary irreducible
character ϑ of Sm . In the case where ϑ is labelled by a hook partition,
b
ϑ = χ(a,1 ) where a+b = m, we give a combinatorial description, generalizing
Theorem 1.5. We also prove some other general results, and show how these,
together with the results of §4, may be used to calculate the values of an
irreducible character of Smn deflated with respect to an arbitrary character
of Sm .
Firstly we deduce from Theorem 1.5 an analogous result for deflations
with respect to the sign character. As is usual, if λ is a partition then we
denote by λ0 the conjugate partition to λ.
Proposition 6.1. Let m, n ∈ N and let λ/µ be a skew-partition of mn.
If γ is a composition of n and g ∈ Sn has cycle type γ then

a 0 0
if m is even
sgnSm
λ /µ ,γ
(DefresSn )(g) =
sgn (g) a 0 0
if m is odd.
Sn

λ /µ ,γ

Proof. It is easily seen that
ResSm oSn sgnSmn =


×n

^
sgn
Sm

if m is even


×n
^
sgn
Sm sgnSn

if m is odd.

Hence if χ is any character of Smn then
sgn

DefresSn Sm χ = η DefresSn (χ sgnSmn )
where η = 1Sn if m is even and η = sgnSn if m is odd. It follows from
Theorems 7.15.6 and 7.17.5 of [19] that if λ/µ is a skew-partition of mn
0
0
then χλ/µ sgnSmn = χλ /µ . Therefore, by Theorem 1.5, we have
sgn

0

0

DefresSn Sm (χλ /µ ) = η(g)aλ0 /µ0 ,γ ,
as required.



It would also have been possible to prove Proposition 6.1 directly from
Proposition 4.1, by reasoning along the same lines as the proof of Theorem 1.5 in §5.
b
We now turn our attention to the case where ϑ = χ(a,1 ) for a hook
partition (a, 1b ). For convenience, we use the language of skew shapes (see,
for example, [22]). A skew shape is a finite subset κ of N × N that is convex
with respect to the partial order ≤p defined by (i, j) ≤p (i0 , j 0 ) if and only
if i ≤ i0 and j ≤ j 0 . We identify the skew-partition λ/µ in which λ has t
parts with the skew shape {(i, j) : 1 ≤ j ≤ t, µi + 1 ≤ j ≤ λi }. We define
χκ = χλ/µ and εn (κ) = εn (λ/µ).


CHARACTER DEFLATIONS

23

Suppose κ is a skew shape. Then we define the initial box of κ to be
(iκ , jκ ) where (iκ , jκ ) ∈ κ and, for any i ≤ iκ and j ≥ jκ , if (i, j) ∈ κ then
i = iκ and j = jκ . Similarly, we define the terminal box of κ to be (kκ , `κ )
where (kκ , `κ ) ∈ κ and, for any k ≥ kκ and ` ≤ `κ , if (k, `) ∈ κ then k = kκ
and ` = `κ . The initial and terminal boxes exist due to the convexity of κ.
For all (i, j) ∈ κ, iκ ≤ i ≤ kκ and `κ ≤ j ≤ jκ .
We use the term border strip in this context to mean a connected skew
shape which contains no 2 × 2 square. We say that D is a border-strip ndiagram if D is a finite set of disjoint border strips, each of length n, such
S
that D is a skew shape. We say that D is a horizontal border-strip ndiagram if whenever (iρ , jρ ) is the initial box of some border strip ρ ∈ D,
S
we have (i, jρ ) ∈
/ D for all i < iρ . Similarly, D is a vertical border-strip ndiagram if whenever (kρ , `ρ ) is the terminal box of some border strip ρ ∈ D,
S
we have (kρ , `) ∈
/ D for all ` < `ρ .
We define a relation R on the set of border strips of length n by (ρ1 , ρ2 ) ∈
R if ρ1 and ρ2 are disjoint border strips of length n and there exist z ∈ ρ1
and w ∈ ρ2 such that z <p w. Observe that when n ≥ 3 the relation R
is not transitive. We can now state the following combinatorial definition,
which is illustrated in Figure 5 overleaf.
Definition 6.2. Let κ be a skew shape of size mn, a, b be positive integers
such that a + b = m, and D and E be two border-strip n-diagrams such that
S
κ = (D ∪ E). We say that (D, E) is an (a, 1b )-like border-strip n-diagram
of shape κ if the following conditions are satisfied:
(1) |D| = a and |E| = b + 1;
(2) D ∩ E = {σ} where σ is border strip of length n which contains the
initial box of κ;
(3) D is a horizontal border-strip n-diagram, and E is a vertical borderstrip n-diagram;
(4) there do not exist ρD ∈ D and ρE ∈ E such that (ρE , ρD ) ∈ R.
κ .
We denote the set of (a, 1b )-like border-strip n-diagrams of shape κ by Ba,b
κ ,
We note that, by a simple counting argument, whenever (D, E) ∈ Ba,b
the elements of D are pairwise disjoint, as well as those of E, and we have
S
S
( D) ∩ ( E) = σ. Definition 6.2 is inspired by the Littlewood–Richardson
Rule (see [8, 2.8.13] or [19, A1.3.3]) in the case of a hook partition (a, 1b ). In
b
this case the rule states that the multiplicity of χ(a,1 ) in χκ is the number
of ways to represent κ as a union of two skew shapes α and β satisfying the
following: (1) the size of α is a and the size of β is b + 1; (2) α ∩ β = {x}
where x is the initial box of κ; (3) α is a horizontal strip and β is a vertical


24

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

I
I

T

I

T

T
I

T

T
Figure
5. A
(4, 14 )-like
border-strip
3-diagram
of
shape
(9, 8, 7, 7, 6, 2, 1)/(5, 5, 3, 3).
Ribbons in the horizontal border-strip
3-diagram are shown in light grey and white, with their initial boxes
labelled I; ribbons in the vertical border-strip 3-diagram are shown in
light grey and dark grey with their terminal boxes labelled T .

strip; (4) there do not exist y ∈ α and z ∈ β such that z <p y. Thus
(a,1b )

(Def Sχ1

κ
χκ )(1S1 ) = |Ba,b
|.

This is the case n = 1 of the following theorem.
Theorem 6.3. Let κ be a skew shape of size mn. Let a, b be positive integers
such that a + b = m. Let g ∈ Sn be an n-cycle. Then
(a,1b )

(DefresSχn

κ
χκ )(g) = εn (κ)|Ba,b
|.

We observe that an (m)-like border-strip n-diagram of shape κ may be
viewed as an m-border-strip tableau of shape κ and type (n) by labelling
the border strips in the unique way so that the condition on row numbers in
Definition 1.4 holds. Thus Theorem 6.3 is a generalization of Theorem 1.5
in the case of an n-cycle.
(3,1)

Example 6.4. We compute (DefresχS3 χ(4,4,4) )(g) where g is a 3-cycle.
There are two (3, 1)-like border-strip 3-diagrams of shape (4, 4, 4, 4), namely
({ρ1 , ρ2 , ρ3 }, {ρ3 , ρ4 }) and ({ρ5 , ρ6 , ρ7 }, {ρ7 , ρ8 }), where ρi denotes the border strip consisting of those boxes labelled by i in the tableaux below.
1 2 2 3
1 2 3 3 ,
1 4 4 4

5 6 7 7
5 6 7 8 .
5 6 8 8
(3,1)

Since ε3 (4, 4, 4) = 1, Theorem 6.3 implies that (DefresχS3

χ(4,4,4) )(g) = 2.

The proof of Theorem 6.3 requires the following definition, in which we
assume that a + b = m.


CHARACTER DEFLATIONS

25

κ to be the
Definition 6.5. Let κ be a skew shape of size mn. Define Da,b
set of pairs (D, E) where D and E are border-strip n-diagrams such that
S
κ = (D ∪ E) and the following conditions are satisfied:

(10 ) |D| = a and |E| = b;
(3) D is a horizontal border-strip n-diagram, and E is a vertical borderstrip n-diagram;
(4) there do not exist ρD ∈ D and ρE ∈ E such that (ρE , ρD ) ∈ R.
Note that since |κ| = mn, the border-strips in D and E are necessarily
κ ; their proofs are given
disjoint. We need the following two lemmas on Da,b
after the proof of Theorem 6.3.
Lemma 6.6. Let κ be a skew shape of size mn, and let a, b be positive
integers such that a + b = m. Then
b

κ
|,
hω(ResSm oSn χκ ), IndSSm
(χ(a) × χ(1 ) )i = εn (κ)|Da,b
a ×Sb

Lemma 6.7. Let κ be a skew shape of size mn. Let 0 ≤ a < m and
b = m − a. Then
κ
κ
κ
|.
| + |Ba+1,b−1
|Da,b
| = |Ba,b
Proof of Theorem 6.3. The proof is by induction on b. Recall that g denotes
an n-cycle. In the case b = 0 we have
(m)

κ
κ
(DefresχSn χκ )(g) = aκ,(n) = εn (κ)|Dm,0
| = εn (κ)|Bm,0
|,

where the first equality follows from Theorem 1.5 and the second by Lemma 4.2.
For b > 0, we combine Proposition 2.6 with Lemmas 6.6 and 6.7, Young’s
Rule and the inductive hypothesis to get
(a,1b )

(DefresSχn

b

χκ )(g) = hω(ResSm oSn χκ ), χ(a,1 ) i
b

b−1 )

= hω(ResSm oSn χκ ), IndSSm
(χ(a) × χ(1 ) ) − χ(a+1,1
a ×Sb
(a+1,1b−1 )

κ
= εn (κ)|Da,b
| − (DefresχSn

i

χϑ )(g)

κ
κ
= εn (κ)|Da,b
| − εn (κ)|Ba+1,b−1
|
κ
= εn (κ)|Ba,b
|.

as required.



It remains to demonstrate the truth of the two lemmas.
Proof of Lemma 6.6. Let g denote an n-cycle. In the case b = 0,
κ
hω(ResSm oSn χκ ), χ(m) i = (DefresSn χκ )(g) = aκ,(n) = εn (κ)|Dm,0
|

by Proposition 2.6, Theorem 1.5 and Lemma 4.2. Similarly, the case a = 0
follows using Proposition 6.1:
m

sgn

κ
hω(ResSm oSn χκ ), χ(1 ) i = (DefresSn Sm χκ )(g) = εn (κ)|D0,m
|.


26

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

In the general case, let κ = λ/µ. By Frobenius reciprocity and Lemma 4.4,
b

(χ(a) × χ(1 ) )i =
hω(ResSm oSn χκ ), IndSSm
a ×Sb
X
b
h
ω(ResSa oSn χτ /µ ) × ω(ResSb oSn χλ/τ ), χ(a) × χ(1 ) i,
τ

where the sum is over all partitions τ such that µ ⊆ τ ⊆ λ and |τ /µ| = an.
Using the two extreme cases, it follows that
X
τ /µ
λ/τ
(a)
(1b )
(χ
×
χ
)i
=
εn (τ /µ)|Da,0 |εn (λ/τ )|D0,b |
hω(ResSm oSn χκ ), IndSSm
a ×Sb
τ

= εn (λ/µ)

X

τ /µ

λ/τ

|Da,0 | |D0,b |

τ
λ/µ

= εn (λ/µ)|Da,b |
as required.



The proof of Lemma 6.7 relies upon the following simple result.
Lemma 6.8. Let ρ1 and ρ2 be disjoint border strips, each of length n, such
that (ρ1 , ρ2 ) ∈ R. For t ∈ {1, 2}, let (it , jt ) and (kt , `t ) be the initial and
terminal boxes respectively of ρt . Then
(1) There exists (r, s) ∈ ρ2 such that either r ≥ i1 and s > j1 , or r > k1
and s ≥ `1 .
(2) There exists (t, q) ∈ ρ1 such that either t < i2 and q ≤ j2 , or t ≤ k2
and q < `2 .
Proof. We prove the first statement only; the second is entirely analogous.
Suppose that (ρ1 , ρ2 ) ∈ R but there exists no (r, s) ∈ ρ2 satisfying the stated
conditions. Since (ρ1 , ρ2 ) ∈ R, there exist (a, b) ∈ ρ1 and (e, f ) ∈ ρ2 such
that (a, b) <p (e, f ). In particular, i1 ≤ e and `1 ≤ f , and our assumption
implies that f ≤ j1 and e ≤ k1 . Thus (e, f ) belongs to the rectangle [i1 , k1 ]×
[`1 , j1 ]. The ribbon ρ1 divides its complement in [i1 , k1 ] × [`1 , j1 ] into two
connected components, with (e, f ) lying to the south east of ρ1 (as (a, b) ∈ ρ1
satisfies (a, b) <p (e, f )).
Let τ = {(c, j1 + 1) : i1 ≤ c ≤ k1 + 1} ∪ {(k1 + 1, d) : `1 ≤ d ≤ j1 + 1}, and
observe that our assumption ensures that τ ∩ ρ2 = ∅. The set ρ1 ∪ τ is the
boundary of a certain region ∆. Since (e, f ) ∈ ∆ and ρ2 does not intersect
the boundary, the whole border strip ρ2 must be contained in ∆ and, in
particular, ρ2 ⊂ [i1 , k1 ]×[`1 , j1 ]. However, as ρ1 is a border strip of the same
length with initial and terminal boxes (i1 , k1 ) and (`1 , j1 ) respectively, ρ2
must contain the corners (i1 , k1 ) and (`1 , j1 ) and hence intersect ρ1 , contrary
to our hypotheses.

This lemma can be used to verify that if D is a horizontal border-strip
n-diagram with initial box (iσ , jσ ) ∈ σ ∈ D then (σ, ρ) ∈
/ R for all ρ ∈ D.


CHARACTER DEFLATIONS

27

Indeed, if (σ, ρ) ∈ R then by Lemma 6.8(1) there exists (r, s) ∈ ρ such
that either r ≥ iσ and s > jσ , or r > kσ and s ≥ `σ . The ‘either’ case is
impossible because (iρ , jρ ) is the initial box of D. Hence (iρ , jρ ) must lie
in [iσ , r] × [s, jσ ], to the south of σ, and so a box of σ lies above (iρ , jρ ),
contradicting the horizontality of D. Similarly, if E is a vertical border-strip
n-diagram with initial box (iσ , jσ ) ∈ σ ∈ E then (ρ, σ) ∈
/ R for all ρ ∈ E:
indeed if (ρ, σ) ∈ R then by Lemma 6.8(2) there exists (t, q) ∈ ρ such that
either t < iσ and q ≤ jσ , or t ≤ kσ and q < `σ . The ‘either’ case is again
ruled out because (iσ , jσ ) is the initial box of E. Hence
(t, q) <p (kσ , q) ≤p (kσ , `σ ),
S
and so (kσ , q) is a box of E because E is convex. But this box lies to the
left of the terminal box of σ, a contradiction. We shall use these observations
in the proof of Lemma 6.7.
Proof of Lemma 6.7. We construct a bijection
κ
κ
κ
.
→ Da,b
t Ba+1,b−1
f : Ba,b
κ t Bκ
Given (D, E) ∈ Ba,b
a+1,b−1 , let σ denote the unique element of D ∩ E.
κ
κ
For (D, E) ∈ Ba,b , we set f (D, E) = (D, E \ {σ}), and for (D, E) ∈ Ba+1,b−1
we set f (D, E) = (D \ {σ}, E).
κ . Suppose that (D, E) ∈ B κ (as
Firstly, we verify that f (D, E) ∈ Da,b
a,b
the second case is exactly analogous). The conditions (10 ), (3), (4) on
S
(D, E \ {σ}) follow immediately provided that (E \ {σ}) is a skew shape.
S
Take x <p y <p z with x, z ∈ (E \ {σ}). We know y lies in the skew shape
S
E, so suppose that y ∈ σ. Then if z ∈ ρE ∈ E \ {σ} we have (σ, ρE ) ∈ R,
contrary to condition (4) of Definition 6.2.
To see that f is the bijection we require, we define its inverse map
κ
κ
κ
.
t Ba+1,b−1
h : Da,b
→ Ba,b
κ , let σ denote the border strip of D ∪ E containing the
For (D, E) ∈ Da,b
initial box of κ. Then if σ ∈ D we set h(D, E) = (D, E ∪ {σ}) and if σ ∈ E
we set h(D, E) = (D ∪ {σ}, E).
κ t Bκ
We verify that h(D, E) ∈ Ba,b
a+1,b−1 . Suppose σ ∈ D. To see that
S
S
(E ∪{σ}) is a skew shape, take x <p y <p z with x, z ∈ (E ∪{σ}). If x, z
S
lie in the skew shape E then so does y, and similarly if x, z ∈ σ then y ∈ σ.
Two cases remain. Firstly, if x ∈ ρ ∈ E and z ∈ σ ∈ D then (ρ, σ) ∈ R,
κ . Secondly, suppose that x ∈ σ ∈ D and
contrary to the definition of Da,b
S
z ∈ E, and, for a contradiction, that y ∈ ρ ∈ D \ {σ}. Then (σ, ρ) ∈ R,
which is impossible by the first observation following Lemma 6.8. (The proof
that D ∪ {σ} is a skew shape in the case σ ∈ E is entirely analogous.)


28

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

Next we verify that if σ ∈ D then E ∪ {σ} is a vertical n-border strip
diagram. Let (iσ , jσ ) be the initial box of σ and let (kσ , `σ ) ∈ σ be the
terminal box of σ. Since E is a vertical n-border strip diagram, it suffices
to check firstly that there is no box (kσ , `) ∈ ρE ∈ E for ` < `σ , and
secondly that, if ρ ∈ E has terminal box (kρ , `ρ ), then (kρ , j) ∈
/ σ for any
κ since
j < `ρ . The first statement is a consequence of the definition of Da,b
the existence of such a box implies (ρE , σ) ∈ R. If the second statement
fails with (kρ , j) ∈ σ, then (σ, ρ) ∈ R and Lemma 6.8(1) implies that there
is a box (r, s) ∈ ρ with either r ≥ iσ and s > jσ , or r > kσ and s ≥ `σ .
The ‘either’ case is ruled out because (iσ , jσ ) is the initial box of σ. In the
‘or’ case, since (kρ , j) ∈ σ, we have kσ ≥ kρ , and therefore r > kσ ≥ kρ ,
contradicting that (r, s) ∈ ρ. (The proof that if σ ∈ E then D ∪ {σ} is a
κ and
horizontal n-border strip diagram is simpler, using the definition of Da,b
the fact that (iσ , jσ ) is the initial box of ϑ.)
Finally, we must check that if σ ∈ D then there do not exist ρ ∈ D and
0
κ , and, by
ρ ∈ E ∪ {σ} with (ρ0 , ρ) ∈ R. This is true because (D, E) ∈ Da,b
the observation following Lemma 6.8, for all ρ ∈ D, (σ, ρ) ∈
/ R. (Again, the
case σ ∈ E is similar).
We have demonstrated that f and h are well-defined, and by their construction the maps are mutually inverse.

This completes the proof of Theorem 6.3 on deflation with respect to
hook characters. We now give some results on DefresϑSn χλ for an arbitrary
irreducible character ϑ.
Proposition 4.1 combined with the Littlewood–Richardson rule yields the
following corollary, which gives a useful sufficient condition for the deflation
of an irreducible character of Smn to vanish on an n-cycle.
Corollary 6.9. Let m, n ∈ N, let λ be a partition of mn. Let β be a partition of m and let ϑ = χβ . Let g ∈ Sn be an n-cycle. If (DefresϑSn χλ )(g) 6= 0
then λ has empty n-core and moreover, λ(i) ⊆ β for each i ∈ {0, . . . , n − 1},
where (λ(0) , . . . , λ(n−1) ) is the n-quotient of λ. In this case
(DefresϑSn χλ )(g) = εn (λ/∅)cβλ(0) ...λ(n−1)
where cβλ(0) ...λ(n−1) denotes a generalized Littlewood–Richardson coefficient.
A related result is Proposition 6.10 below, which gives the degrees of the
deflations of the irreducible characters of Smn to Sn . It may be proved in
the same way as Equation (2) in §1. Note that the right-hand side equals
the generalized Littlewood–Richardson coefficient cλβ...β .


CHARACTER DEFLATIONS

29

Proposition 6.10. Let m, n ∈ N. Let β be a partition of m and let ϑ = χβ .
Then
D
E
β
β
λ
DefresϑSn (χλ )(1Sn ) = IndSSmn
χ
×
·
·
·
×
χ
,
χ
m ×···×Sm
for any partition λ of mn.



We end with an example showing how Propositions 4.1, 4.5, and 6.10 and
Corollary 6.9 may be used to calculate the values of an irreducible character
of Smn deflated with respect to an arbitrary character of Sm .
Example 6.11. Let ϑ = χ(2,2) . We shall find (DefresϑS4 χ(6,4,4,2) )(g) in the
cases where g ∈ S4 is a transposition or a double transposition.
Firstly take g to be a transposition. By Proposition 4.5 we have
X
(DefresϑS2 χτ )(1S2 )(DefresϑS2 χ(6,4,4,2)/τ )(k)
(DefresϑS4 χ(6,4,4,2) )(g) =
τ

where k = (12) ∈ S2 and the sum is over all partitions τ of 8. Using
Proposition 6.10 on the first term we obtain
X
(DefresϑS4 χ(6,4,4,2) )(g) =
cτ(2,2)(2,2) (DefresϑS2 χ(6,4,4,2)/τ )(k)
τ

with the same conditions on the sum. By Proposition 4.1, we need only
consider those partitions τ such that (6, 4, 4, 2)/τ is 2-decomposable. The

2-quotient of (6, 4, 4, 2) is (2, 1), (3, 2) , so the τ we must consider are the
partitions (6, 12 ), (4, 3, 1), (6, 2), (4, 22 ), (42 ), (32 , 2), (4, 2, 12 ), (24 ), (32 , 12 ).
Calculation shows that cτ(2,2)(2,2) = 1 when τ ∈ P where
P = {(4, 3, 1), (4, 22 ), (42 ), (24 ), (32 , 12 )}
and that cτ(2,2)(2,2) is zero in the other four cases. Hence by Proposition 4.1
we have
(DefresϑS4 χ(6,4,4,2) )(g) =
E
X
D
(0)
(1)
ε2 (6, 4, 4, 2)/τ IndSH4 χ(2,1)/τ × χ(3,2)/τ , χ(2,2)
τ ∈P

where H = S|(2,1)/τ (0) | × S|(3,2)/τ (1) | . The contributions to the sum from
the elements of P , in the order given above, are −1, +2, +1, +1 and +1
respectively. For example, the 2-quotient of (6, 4, 4, 2)/(4, 2, 2) is

(2, 1)/(1), (3, 2)/(2, 1)
and ε2 (6, 4, 4, 2)/(4, 2, 2)) = 1, so the contribution from (4, 2, 2) is
D
E D
E
IndSS42 ×S2 χ(2,1)/(1) × χ(3,2)/(2,1) , χ(2,2) = IndS1 4 1, χ(2,2) = 2.
Therefore (DefresϑS4 χ(6,4,4,2) )(g) = 4.


30

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

Similar arguments can be used in the case where g is a double transposition. By Proposition 4.5 we have
X
(DefresϑS2 χτ )(k)(DefresϑS2 χ(6,4,4,2)/τ )(h)
(DefresϑS4 χ(6,4,4,2) )(g) =
τ

where k and h are transpositions, and the sum is over all partitions τ of 8.
Proposition 4.1 and Corollary 6.9 restrict the possible partitions τ to be
considered and show that (DefresϑS4 χ(6,4,4,2) )(g) equals
E
X
 (2,2)
D
(0)
(1)
ε2 τ /∅ cτ (0) τ (1) ε2 (6, 4, 4, 2)/τ IndSH4 χ(2,1)/τ × χ(3,2)/τ , χ(2,2)
τ ∈P

where
P = {(4, 3, 1), (4, 22 ), (42 ), (24 ), (32 , 12 )}
and H = S|(2,1)/τ (0) | × S|(3,2)/τ (1) | . The contributions to the sum from the
elements of P , in the order given above, are +1, +2, +1, +1 and +1 respectively. Hence (DefresϑS4 χ(6,4,4,2) )(g) = 6.
