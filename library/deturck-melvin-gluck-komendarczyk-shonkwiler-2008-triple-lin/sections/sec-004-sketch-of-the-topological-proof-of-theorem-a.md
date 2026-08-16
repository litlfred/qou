---
doc_id: deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin
doc_title: "© 2008, Sociedade Brasileira de Matem´ atica TRIPLE LINKING NUMBERS, AMBIGUOUS HOPF INV ARIANTS"
section_id: sec-004-sketch-of-the-topological-proof-of-theorem-a
section_title: "Sketch of the topological proof of Theorem A"
section_number: null
pages: 10-17
source_pdf: deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-linking-numbers.pdf
source_sha256: db149864ce367da2
doc_brief: "Matemática Contemporânea, Vol. 34, 251–283 © 2008, Sociedade Brasileira de Matemática TRIPLE LINKING NUMBERS, AMBIGUOUS HOPF INVARIANTS — Three-component links in the 3-dimensional sphere were"
---
Starting with a link in the 3-sphere, consider the delta move shown in
Figure 3, which may be thought of as a higher order variant of a crossing
change. It takes place within a 3-ball, outside of which the link is left
fixed. This move was introduced by Matveev [1987].
Figure 3: The delta move L→L′
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS 261
It was shown by Murakami and Nakanishi [1989] that an appropriate
sequence of such moves can transform any link into any other link with
the same number of components, provided the two links have the same
pairwise linking numbers.
The key organizational idea for this proof of Theorem A is to show that
the delta move, when applied to the three components X,Y andZ of the
link L, as shown in Figure 3, increases its Milnor µ-invariant by 1, while
increasing the Pontryagin ν-invariant of its characteristic map gL by 2.
The fact that the delta move increases µ by 1 is well known to ex-
perts; our proof relies on the geometric formula for µ due to Mellor and
Melvin [2003] in terms of how each link component pierces the Seifert
surfaces of the other two components, plus a count of the triple point in-
tersections of these surfaces. In particular, one can use a family of Seifert
surfaces that differ only near the delta move, as shown in Figure 4.
Figure 4: Seifert surfaces for L and L′
To see how the delta move affects the ν-invariant, we will view ν as
a relative Euler class, following Gompf [1998] and Cencelj, Repovˇ s and
Skopenkov [2007].
To that end let L and L′ be two three-component links in S3 with the
same pairwise linking numbers p,q andr, and let L and L′ be the framed
links in the 3-torus 1 that are the preimages of a common regular value
1For the reader’s convenience, all subsets of T 3 in this section are written in black-
board bold to distinguish them from subsets of S3.
262 DETURC, GLUCK, KOMENDARCZYK, MEL VIN et al
of their characteristic maps gL and gL′. Orient L and L′ so that, when
combined with the pullback of the orientation on S2 to a tangent 2-plane
transverse to these links, we get the given orientation on T 3. Since L
andL′ have the same pairwise linking numbers, their characteristic maps
gL and gL′ have the same degrees on the coordinate 2-tori in T 3 (by the
first part of Theorem A, proved in Section 3), and so the framed links L
and L′ have the same intersection numbers with these 2-tori. By Poincar´ e
duality, it follows that L and L′ are homologous in T 3, and then by a
standard argument that L× 0 and L′× 1 together bound an embedded
surface F in T 3× [0, 1].
The relative normal Euler class e(F) is the intersection number of F
with a generic perturbation of itself that is directed by the given framings
along L× 0 and L′× 1, but is otherwise arbitrary. Then, according to
Gompf and Cencelj–Repovˇ s–Skopenkov,
ν(gL′,gL) ≡ e(F) mod 2 gcd( p,q,r ).
The key step in seeing how the delta move affects the ν-invariant is to
adjust L and L′ by link homotopies so that up to isotopy
L′ = L∪ L∗
where L∗ is a two-component link bounding an annulus A⊂T 3− L with
relative normal Euler class 2. Then the surfaceF=( L×[0, 1])∪(A×1), with
∂F = L′×1−L×0, hase(F) = 2, sincee(L×[0, 1]) = 0. Thus ν(gL′,gL)≡
e(F) = 2, showing that the delta move increases the ν-invariant of L by
2. Explaining how this step is carried out will complete our sketch of the
topological proof of Theorem A.
We begin with the delta move as shown above and change it by an
isotopy so that it now appears as pictured in Figure 5.
From this picture, we see that the delta move can be regarded as a pair of
crossing changes of opposite sign which introduce a pair of small “clasps”
.
We may assume that the move takes place inside the large ball B inS3
of radius π/2 centered at −1. If we think of 1 and −1 as the north and
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS 263
Figure 5: A different view of the delta move
south poles of S3, thenB is just the southern hemisphere. Figure 5 shows
that inside B, the portions of X andX′ lie along the great circle through
1 and i (so in fact X andX′ coincide) while the portions of Y ,Z,Y′ and
Z′ lie close to the great circle C through j and k, shown in orange.
Outside B, the links L and L′ coincide and, maintaining this coinci-
dence, we move them into a more favorable position as follows. First
unknot X =X′ by a link homotopy, and move it to the rest of the great
circle through 1 and i. Then by an isotopy move Y and Z into a small
neighborhood of the great circle C, and position them so that their or-
thogonal projections to C are Morse functions with just one critical point
per critical value. As intended, Y′ and Z′ move likewise outside B. Note
that each of the aforementioned clasps contributes two critical values to
these projections, and we may assume that no other critical values fall
between these two.
Now we use the asymmetric versions egL and egL′ of the characteristic
maps T 3→ S2, identifying the target S2 with the unit 2-sphere in the
purely imaginary ijk-subspace of the quaternions. We interpret Figure 5
as showing the image of S3−{ 1} under the stereographic projection ℘1,
and view i as the north pole of S2.
It is straightforward to check that, under the genericity conditions im-
posed above, the point i∈S2 is a common regular value for egL andegL′,
and that the framed links L and L′ in T 3 that are the inverse images of
264 DETURC, GLUCK, KOMENDARCZYK, MEL VIN et al
i under these maps are for the most part the same. In fact we will show
that, up to isotopy L′ = L∪ L∗ where L∗ consists of a pair of oppositely
oriented spiral perturbations of S1× pt× pt, coming from the two clasps
shown in Figure 5, and that these two spirals bound an annulus A in
T 3− L whose relative normal Euler class e(A) is 2. The argument will be
given as we explain Figures 6–8.
The discussion is independent of what the links L and L′ look like
outside the ball B shown in Figure 5. The simplest case occurs when L
is the three-component unlink, and L′ = X′∪Y′∪Z′ is the Borromean
rings, whose stereographic image is shown in Figure 6.
Figure 6: Borromean Rings
We have, as before, thatX′ is the great circle through 1 andi, with image
the blue vertical axis, while Y′ and Z′ lie in a small tubular neigborhood
of the great circleC throughj andk, with images shown in red and green.
In this circumstance, the general formula L′ = L∪ L∗ has L empty, and
hence L′ = L∗.
Figure 7 shows enlargements of the two clasps between redY′ and green
Z′, with points on their segments labeled by numbers onY′ and by letters
on Z′, ordered consistently with their orientations.
Our job is to find the preimage L′ in S1×S1×S1 of the regular value
i of the map egL′, which means we must find the points where the vector
from the green ℘1(zx−1) to the red ℘1(yx−1) points straight up.
We pause to see the effect of right multiplication by x−1. Let x travel
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS 265
Figure 7: The two clasps
along X = X′ from 1 to −i to−1 to i and back to 1, which is the
direction in which this component is oriented. Then right multiplication
byx−1 gradually rotates this component in the opposite direction. In the
image 3-space, it looks like the vertical axis is moving downwards. At the
same time, the great circle C through j and k is gradually rotated in the
direction from j towards−k. A small tubular neighborhood of C follows
this rotation and twists as it goes, dragged by the downward motion of
the vertical axis.
Now focusing on the left clasp, and starting with x = 1, we see that the
arrow ⃗f2 from green f to red 2 points up. As x moves around X′ from 1
towards−i (up on the blue vertical axis) a loop of upward pointing vectors
is traced out, passing successively through ⃗e1, ⃗d2, ⃗e3, and finally back to
⃗f2. In Figure 8, the 3-torus is depicted as a cube, in which this loop is
shown near the front left corner of the bottom red-green square, traced
in a counterclockwise direction. When the progression of x(s) values is
taken into account, we get the orange spiral curve shown above this loop.
This is one component of L′, and is oriented according to the convention
for framed links.
Focusing on the right clasp and repeating the above procedure, we
get the orange spiral curve shown at the right rear, lying over the loop
⃗a5⃗b6⃗c5⃗b4. This is the other component of L′, and is also oriented accord-
ing to convention.2
2In fact, one need not go through the careful analysis to determine the orientations
of the spirals. All that is important is that they are oppositely oriented, which follows
from the fact that the pairwise linking numbers for the Borromean rings are zero.
266 DETURC, GLUCK, KOMENDARCZYK, MEL VIN et al
Figure 8: Computing e(A) = 2
Together, the components of L′ bound the orange annulus A shown in
the cube. This annulus is constructed as follows. Each point on the left
spiral loop is joined to the point on the right spiral loop at the same height
s by a straight line segment in the 2-torus s×S1×S1. The t-coordinate
moves steadily so that y(t) travels along the arc of Y′ which lies in the
ballB and the u-coordinate moves steadily so that z(u) travels along the
arc ofZ′ which lies inB. It is easy to see that this annulus A is embedded
in the 3-torus and that, even in the general case where L is not empty, it
would still be disjoint from L.
Now since A lies inT 3, its relative normal Euler classe(A) (when viewed
as a surface in T 3× [0, 1]) can be computed as the intersection number of
A with the inverse image of any other regular value of egL′. In particular,
the point−i is also a regular value, and its inverse image bL′ is calculated
from an analysis of the clasps, just as we did for the inverse image of i.
It consists of two spirals, which can be obtained from the spirals in L′ by
moving them half-way along in the vertical (blue) direction. We show bL′
in Figure 8 as a pair of purple spirals, which are oriented the same way as
the orange spirals.
It is seen in this figure that the purple spirals pierce the orange annulus
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS 267
twice in the positive direction, confirming that
e(A) = A  bL′ = 2 ,
and completing the sketch of the topological proof of Theorem A.
