---
doc_id: pjm-v161-n1-p02-p
doc_title: "Studying links via closed braids. III. Classifying links which are closed 3-braids"
section_id: sec-001-it
section_title: "it"
section_number: null
pages: 22-32
source_pdf: pjm-v161-n1-p02-p.pdf
source_sha256: a93e922eab1ee67c
toc_source: inferred
doc_brief: "Studying links via closed braids. III. Classifying links which are closed 3-braids — 59 sections: Front matter; STUDYING LINKS VIA CLOSED BRAIDS I; it"
---
u
K
elementary 3-braids, viewed
as they appear "projected"
onto dT
(dotted edges to be identified) 
Diagram on dT of a'^a? a^
(opposite sides of rectangle to be identified)
FIGURE 3.8
In the pictures at the left in Figure 3.8 we have augmented the pic-
tures in Figure 1.5 by adding the digons and shading the two sides of
F. On the right in Figure 3.8 we show an example of a link diagram
on <9T. The reader is advised to return to Figure 3.8 later, as needed.
In future pictures we will omit the shading which we use here to high-
light F + and F~ . The rule is clear: parts of F which are to the right
(left) of the oriented link L, with orientations from the top of the
page toward the bottom, are in F + (F~).
One more illustration is in order. Figure 3.9 (next page) shows the
region which abuts on two digons, from two points of view: first, as
it would appear on 9T and second as it would appear on <9B;. The
undercrossing arc is missing from the former and visible in the latter.
We need to use one more feature of the geometry in order to de-
fine the complexity function. The union of all of the digon-attaching
curves (regarded now as curves on F and not on F + or F~) divide
F into a number of connected components. We call these subsets #1,
2 and 3 of F. They are defined uniquely by the following conditions:
(a) If a component is intersected by A it is in subset #3.
46
JOAN S. BIRMAN AND WILLIAM W. MENASCO
viewed on dT
viewer insideT
viewed on dBj
viewer inside
Region abutting on two digons. viewed on dT and dB;
FIGURE 3.9
(b) If a component meets L, it is in subset #1. Also:
If it meets the undercrossing arcs, it is in subset 1"
If not it is in subset V
(c) If a component has empty intersection with A and L, it is in
subset #2.
Figure 3.3 illustrates the subdivision of F into subsets V, 1" ,2 and
3. Using it, we are almost ready to define our complexity function.
Notice that we have already standardized the geometry in the following
ways:
1. F is a Bennequin surface with respect to H and H
7.
2. W and W are admissible words.
3. A is disjoint from the digons, by construction.
4. The standard foliation of the interior of Ω is singularity-free.
We now need to standardize the intersections of fibers of FT with the
digons:
LEMMA 3.3. Let Ω be the union of all the digons. We may assume
that
(i) The intersections of A! with F U Ω are finite in number and
transverse.
(ii) The non-standard foliation o / F u Ω is radial near each pierce
point
(iii) All but finitely many fibers H', ofH' 
meet FuΩ transversally.
Those which do not (the Ω-singular fibers) are each tangent to 
FuΩ
at exactly one point in the interior of Ω.
STUDYING LINKS VIA CLOSED BRAIDS III 
47
(iv) Each component of intersection of a non-singular fiber H^ with
F {respectively with Ω) is an arc. There are no simple closed curves in
the foliation of ¥ (respectively Ω).
Proof. The arguments are identical with those used to prove Lemma
2 of [B-M, I]. All of the new modifications which are needed can be
achieved by isotopy of Ω, so they won't upset earlier standardiza-
tions. 
D
Finally, we have the long-promised definition of complexity. If S is
a set, we write \S\ for the cardinality of S. If X and Y are families of
surfaces in general position, we write |X Y| to denote the cardinality
of the set of tangencies between X and Y. Our complexity function
is a 5-tuple C = (c\, ... , C5), defined as follows:
C\ — the number of syllables in the word W = W{a\, a2, #3),
c2 = the number of syllables in the word W = W'(b\, b2, b$),
C3 = |A
/Π(FUΩ)|,
c4 = |A' Π (subsets #1" and #2 and #3 of F)|,
c5 = |H
/.(Fu(int(Ω))|.
(Remark: The meaning of c 4, and of our subsets of F, will become
clear later.)
We assume that we have chosen W and W to minimize c\ and
c2 . Our next proposition deals with the minimization of C3.
PROPOSITION 3.4. We may assume that the non-standard axis A! is
disjoint from all of the dίgons.
Proof. The proof will be based upon a study of the foliation of
a single digon Δ by its arcs of intersection with the non-standard
fibration FT. Call this the non-standard foliation of Δ. Let H^ be a
non-singular fiber of H'. If H^ is not one of the exceptional fibers
which is tangent to F, the set F n H^ will be a union of three arcs, as
in Figure 2.1(b). Figure 2.1(c) depicts the fiber H^ split open along
those arcs. We have labeled the sides of the split-open fiber with the
numerals 0, 0', 0", 1, 2, ... , 6 so that sides 0 , 0 ' , 0" are subarcs
of A
7, sides 1, 3, and 5 are subarcs of F~ n H^ and sides 2, 4 and
6 are sub-arcs of F
+ n H^ . There is a natural projection π from the
split-open fiber to the closed fiber and a "lifting" π~
x. Thus we can
describe each leaf in Δ n H^ by the unordered numbers of the sides
towhich its endpoints in the split-open fiber belong. We call these
48
JOAN S. BIRMAN AND WILLIAM W. MENASCO
numbers the name of the leaf. Define two leaves to be equivalent if
they are equivalent under one of the six symmetries of the split-open
fiber generated by the rotation which changes 0, 0
7, 0" to 0
7, 0", 0
and the flip which changes 0, 0', 0" to 0, 0", 0
7. Let [pq] denote
the equivalence class of the leaf pq in H^.
We want to prove that A
7 does not intersect the digons. This is
equivalent to the assertion that no arc in H
7^ n Ω has an endpoint on
A', i.e. leaves with name pq, where p or q is 0, 0
7 or 0" do not
occur. Up to equivalence, it suffices to prove that leaves of name Oq
do not occur, for q = 0, 0
7, 0", 1 , 2 , 3 , 4 , 5 , 6 . As the first step in
this direction we prove:
LEMMA 3.5. We may assume that there are no leaves in the equiv-
alence classes [00] and [01]. Also, choosing any fixed fiber H
7^ we
may assume that there are no leaves of type [11] in this fiber.
Proof of Lemma 3.5. A leaf a (resp. α
7, β) in the class [00] (resp.
[01], [11]) cobounds with a subarc of A
7 (resp. subarcs of A
7 UF,
subarc μ of F n H
7^) a disc d (resp. d', dπ) on H
7^, as illustrated
in Figure 3.10. These leaves are in Ω Π H
7^, so they lie both in some
digon Δ and on H
7,, as illustrated. Figure 3.10 also depicts these
OUype [00]
1 type [01]
(3 type [11]
α, has type [00]
FIGURE 
3.10
STUDYING LINKS VIA CLOSED BRAIDS III
49
p has type [11)
Possible complications in removing arcs of type [11]
Picture in 3-space when digons intersect
FIGURE 
3.11
arcs and associated discs in 3-space, for types [00] and [01]. The
corresponding picture for type [11] is in Figure 3.11.
In the case of leaves of type [00], the only leaves which could
intersect the disc d are other leaves of type [00], so we may assume
that we have chosen a so that d is innermost. We may then push
A' across d to remove a from Δ n H^. This also removes leaves of
type [00] from nearby fibers of H'. Since our isotopy of A' reduces
C3, it reduces complexity. Thus we may assume there are no leaves of
type [00].
In the case of leaves of type [01], there could be leaves of type
[01] or [11] inside the disc d
f, so we begin by removing the latter.
Passing to Figure 3.11 we see that leaves of type [11] could intersect
a component of F Π H', on both the positive and negative sides of F,
50 
JOAN S. BIRMAN AND WILLIAM W. MENASCO
and in fact there are three ways this could happen. If the endpoints of
two such arcs β and β
1 of type [11] do not separate one another, as
in the two left sketches, we simply choose β to bound an innermost
disc dπ, so that no other leaf of type [11] intersects the arc μ in
Figure 3.10. Assume this to be the case. Then, since β is an arc with
its endpoints on F
± n Δ, it cobounds with a second arc μ! (also in
F) another disc dA C Δ, as illustrated. The two discs dπ and d& fit
together to give a disc dπ U d& with boundary μ U μ' a simple closed
curve on F, as depicted in Figure 3.11. Now, F is incompressible,
so d(dπ U dΔ) must also bound a second disc dp c F. The three
discs dπ^d^U 
dp form a 2-sphere S
2 in S
3 - L. Since S
3 - L is
irreducible, this 2-sphere must bound a 3-ball B in S
3 - L. We can
then remove the intersections by changing the fibration, pushing H^
across this 3-ball. After a finite number of repetitions of this argument
we will obtain a half-disc on H^ whose interior contains no leaves of
type [11].
We now examine the same move, when the endpoints of our arc
β of type [11] are separated by the endpoints of another arc β" of
type [11]. Notice that the only way this can happen is if β and β"
are on opposite sides of F, because digons are embedded, and by our
construction distinct digons have disjoint interiors. So the situation in
3-space must be as illustrated in the bottom sketch in Figure 3.11. It
is clear that our change in fibration will not increase the intersections
of fibers of H' with Δ', so in every case the complexity is reduced.
Returning to Figure 3.10, we may now proceed to remove leaves of
type [01]. We begin with an "innermost" leaf of type [01] that is, as
we proceed along a component of H^nF, starting at the A
7 endpoint,
we choose the arc a' of type [01] whose F-endpoint is encountered
first. The disc d
r in Figure 3.10 then meets no other leaf of type [01].
Pushing A' across d
1, we remove the leaf of type [01] from this fiber
and also from nearby fibers. Since complexity is reduced, we conclude
that leaves of type [01] do not occur. 
D
Proof of Proposition 3.4 [continued). In view of Lemma 3.5, we are
reduced to showing that q φ 0', 0", 2, 3, 4, 5. Now, since W' is
admissible, we know that W' contains the letter (b^)
±ι. 
So there is
an F-singularity of type (bs)
±ι 
at, say, Φo. The joining arcs for a
singularity of type (b^)~
ι run between the arcs we have labeled 2 and
6, whereas those for £3 run between sides 1 and 5. Thus q{φo) cannot
be 0', 0", 3 or 4 in either case,because such a leaf is an obstruction
STUDYING LINKS VIA CLOSED BRAIDS III
51
Effect of a type bt singularity on digon-crossing arcs
FIGURE 
3.12
to the joining arc, also if (b3)~
ι 
occurs it cannot be 5, whereas if £3
occurs it cannot be 2. Assume the former. Then g(Φo) must be 2. But
now Figure 3.12 shows how a singularity of type (/>/)"
ι can result in a
change in name of other arcs. If q(φ) = 2 before an F-singularity of
type bj
ι, 
then after the singularity there will be a leaf with name 06.
But this is impossible by Lemma 3.5 because [06] = [01]. Similarly,
if an F-singularity of type b3 occurs at φ0 then the only possibility
is that q(φo) = 5, but in that case there will be a leaf with name 01
after the singularity, and again we have a contradiction to Lemma 3.5.
Thus we conclude that for ^-values which are close to φo there are
no leaves of type Oq, because all values of q have been ruled out.
Now notice that the points where A' pierces Ω are independent of
φ. Thus if there is a leaf with name Oq in some fiber H'φ, there must
be a leaf with name 0... in every fiber of H'. However we have just
shown that no such leaf can occur when φ is close to φo. Thus it
cannot occur at any other ^-value either.
But then, by symmetry, there are no leaves of type 0'q and 0"q
either. Thus A
7 is disjoint from all of the digons. 
•
4. The non-standard foliation of the digons. We have shown that A'
is disjoint from all of the digons. Thus the entries C\, c2, c3 in our
complexity 5-tuple have now been minimized. In this section we will
52
JOAN S. BIRMAN AND WILLIAM W. MENASCO
(a) degenerately
foliated region
qq 11
(b) Singularity of
type (p-q)-»,p=1,q=4or 6
FIGURE 4.1
(c) Singularity
of type [12]
deal with consequences of the minimization of c$. We have not yet
dealt with the consequences of the minimization of C4 . This will not
matter. The actual value of C4 depends upon the location on F of
the three points in A7 n F. In this section we will regard A' as rigidly
fixed. The minimization of C5 can thus be carried out, independently,
for each of the possible values of C4. Later, when we need to move
A' in order to minimize C4 we will be sure that no matter where it is
located, subject to earlier restrictions, we will be able to achieve the
standardizations of this section.
The central result of this section will be to show that the assumption
that C5 is minimal implies that the possible singularities in the non-
standard foliation of the digons are quite limited. See Figure 4.1. The
precise restrictions, which can only be stated in terms of the notation
set up below, are given in Proposition 4.8. We will end this section
with a result (Corollary 4.9) which shows that these singularities are a
key to the geometry, because we can use them to deduce an important
property of W.
As in §3, a leaf in the non-standard foliation of a digon has name
pq, where (by Proposition 3.4) p and q belong to the set {1, 2, 3, 4,
5, 6} . Its equivalence class under symmetries of H^ is denoted [pq].
There are 5 equivalence classes of leaves, listed in Table 4.1. Some-
times it will be useful to refine this classification by distinguishing
equivalence classes with different signs, where the signs ++, — and
H— distinguish the cases when the endpoints of a leaf are both in
STUDYING LINKS VIA CLOSED BRAIDS III
TABLE 4.1
53
type
[22]
[24]
[14]
[12]
[23]
Sign
++
—
++
—
+-
+-
+-
Members of class
22,44,66
11,33, 55
24,46,62
13,35,51
14,25, 36
12,34, 56
23,45,61
c?Δ
+, both in dA 
or one in each. The 5 equivalence classes of leaves
divide into 7 subclasses when we consider signs, and these are also
listed in Table 4.1.
As the fibers of H' pass through Ω-singular or F-singular fibers the
names of the leaves will change. If two leaves have names mn and
pq before the singularity, and np and qm after it, we can describe
the singularity by the symbol " mn +pq —• np + qm ". We choose our
notation so that the labels m, n, p, q have that order on
\ . The
surgery is then uniquely specified. The equivalence class of a surgery
[mn + pq -> np + qm] means equivalence up to symmetries of H^
and (if the symbol " —•" is replaced by * —•") reversal of the sense of
the fibration.
LEMMA 4.1. Singularities in the class [mq + qq
occur.
qq + qm] do not
Proof. See Figures 4.2 and 4.3 (next page). The top picture in Figure
4.2 shows the leaves which would be involved in the surgery, as they
occur on three fibers in the nonstandard fibration, at φ = φo, φ\ and
φ2. 
The middle picture is the singular fiber and the other two are
fibers just before and just after the singularity at s. The point p' is
on A', and the point ί(φ) is on the link L. The heavy arc joining
p
f to L(φ) is on F Π H'±. The lighter arcs are on Δ Π H',. Two discs
d and δ have been labeled in the middle picture. The next picture
in Figure 4.2 shows the foliation of the digon Δ in the region under
investigation. Its boundary dA is on F, and we notice that the entire
region of interest is attached to either F
+ or F~, i.e. dA does not
cross L. We have labeled two regions of Δ as d
r and δ', noting that
dd = dd
f and d δ = dδ
f. The final picture in Figure 4.2 shows the
region ofinterest on Δ, embedded in 3-space.
54
JOAN S. BIRMAN AND WILLIAM W. MENASCO
PICTURE ON A SEQUENCE OF Fl BERS
PICTURE ON THE DIGON
PICTURE IN 3-SPACE
FIGURE 
4.2
SAME PICTURES, AFTER THE MODIFICATIONS
F I G U R E 4.3
Let D = d U d
f or δ U δ'. 
Then D is a disc, and its boundary
<9D is a curve in F. Since F is incompressible, the curve dΌ also
bounds a second disc, say D', in F. Now D u D ' is a 2-sphere in
M = S
3 - L, and since M is irreducible, this 2-sphere must bound a
STUDYING LINKS VIA CLOSED BRAIDS III 
55
3-ball B in M. Then we can use B to isotope d
r to d. Similarly,
we can isotope δ
r to δ. After the change we tip the discs d and
δ a little bit, to make the new digon transverse to the fibers of H'.
The effect of the isotopy is to eliminate the given singularity of the
foliation. See Figure 4.3. This reduces c$, keeping C\, ... , C4 fixed.
Since C is by hypothesis minimal, this cannot happen. Notice that
these changes can't increase |H' (F U IntΔ')|, even if there is another
digon Δ' in the picture, because distinct digons which intersect always
do so in a very controlled fashion (cf. the bottom picture in Figure
3.11), because near a point which is in Δ n Δ ' the digons Δ and Δ'
will always be attached to opposite sides of F. 
D
A region T on a digon Δ is said to be degenerately foliated if it
is foliated by parallel arcs of decreasing lengths, with a single degen-
erate leaf as in Figure 4.1a. Our first observation is that degenerately
foliated regions sometimes tell us that there is a fiber H^ which is
tangent to F at a 0-value near the value at the instant of degeneracy:
LEMMA 4.2. (I) Let T be a degenerately foliated region on Δ. Sup-
pose that each nondegenerate leaf in T has name 24 (respectively 46,
62, 13, 35, 51). Then within a small φ-neighborhood of the instant
of degeneracy a braiding of type b^
