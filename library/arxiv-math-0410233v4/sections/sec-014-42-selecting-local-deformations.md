---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMA TION JESSICA S. PURCELL"
section_id: sec-014-42-selecting-local-deformations
section_title: "Selecting local deformations"
section_number: 4.2
pages: 19-21
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION JESSICA S. PURCELL — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
responds to a local deformation with 1–form ( ω0)j expressed in Vj as in
equation (22). In terms of the deformation, varying ¯ s varies the rates at
which the cone angles are changing (instantaneously). When ¯s = (1, . . . ,1),
all cone angles are changing at the same rate. It might be conv enient to let
¯s = (1, . . . ,1), to simplify calculations. However, such a choice may not give
us the bounds on ∑ bj that we need.
In particular, we would like to select ¯ s such that we may use certain
inequalities from [14]. (These inequalities appear in the p roof of Lemma 4.3
in this paper.) In order to use these inequalities, we will ne ed to ﬁnd ¯s such
that each bj(¯s) ≥ 0.
The existence of such an ¯s has been discovered by Hodgson and Kerckhoﬀ,
but their result is unpublished, so we include it as Lemma 4.1 here.
Lemma 4.1 (Hodgson–Kerckhoﬀ) . There is an ¯s ⁄= 0 for which bj(¯s) ≥ 0
for all j = 1, 2, . . . , n.
Proof. It suﬃces, by rescaling, to restrict ¯ s to the simplex
T = {¯s = (s1, . . . , sn)|
∑
j
sj = n, sj ≥ 0}.
We ﬁrst set up some notation.
Let the j-th vertex of T be denoted tj. So tj = (0, . . . ,0, n, 0, . . . ,0) where
the single non-zero value is in the j-th location. Notice that at tj, bi(tj) ≤ 0
for all i ⁄= j. Because the sum of the bi is always strictly positive, we must
have bj(tj) > 0.
Let the face of T opposite tj be denoted fj. That is, on fj the j-th
coordinate is always 0. Notice that on fj, bj ≤ 0. We will assume that bj < 0
on fj. If not, consider instead level sets of bj for values ǫ > 0 arbitrarily
close to 0. Below, we will be ﬁnding points where all the bj are positive.
Taking a limit will at least give points where the bj are nonnegative.
We will also assume level sets bj = 0 intersect transversely. If not, take
an arbitrarily small perturbation of the quadratic functio ns (keeping them
quadratic).
First we note that the set where bj > 0 is an open neighborhood of tj
in T . This is because on any line from tj to fj, bj goes from positive to
negative. Because bj(s) is quadratic in s, bj = 0 on this line in exactly one
value. Thus the level set bj = 0 separates tj from fj. It has a well–deﬁned
positive and negative side.
Now, we prove the following sublemma by induction.
20 JESSICA S. PURCELL
t3
t2
e3
t1
B2
{b2 = 0}
ˆB2
{b1 = 0} = ˆE2
e2 ∈ E2
Figure 1. Proof of Lemma 4.1 when k = 3.
Lemma 4.2. Consider the k − 1 simplex Sk of T where si = 0 for all i > k .
There exists a nonempty open set Bk ⊆ Sk where bj > 0 for all j ≤ k.
Furthermore, the set Ek ⊆ Sk where bj = 0 for all j < k is an odd number
of points, each on the boundary of Bk.
Notice that in the above statement, when k = n, the simplex Sn is all of
T . Then if the statement is true, Bn is an open set on which all the bj are
positive, so this will prove Lemma 4.1.
An additional fact we will pick up from the proof is that the se t En where
bj = 0 for j = 1, 2, . . . , n− 1 is an odd number of points. (We will use this
additional fact in the proof of Lemma 4.4 below.)
Proof. We ﬁrst prove Lemma 4.2 when k = 2. In this case, S2 is the 1–
simplex from t1 to t2. At t1, b1 > 0. At t2, b1 < 0. Since b1 is quadratic,
somewhere on S2 is a single point e2 where b1 = 0. Notice that b2(e2)
must be positive. This is because each bj(e2) ≤ 0 for j > 2 (since the
corresponding coordinates sj are all zero). Since b1(e2) is zero, and the sum∑ bi > 0, this forces b2 > 0. Then in this case, E2 contains the single point
e2. B2 is nonempty, with e2 on its boundary.
We will now prove the lemma by induction for k + 1. For reference, an
example of the case when k + 1 = 3 is illustrated in Figure 1.
Sk+1 is the k subsimplex of T with vertices t1, t2, . . . , tk+1, on which
sk+2 = · · · = sn = 0. It has as one boundary face the k − 1 simplex
Sk, on which sk+1 = sk+2 = · · · = sn = 0. On any other face of Sk+1,
sk+2 = · · · = sn = 0, and also sj = 0 for some j < k + 1.
By induction, we are assuming that on the face Sk the set Bk, where
bj > 0 for all j ≤ k is a nonempty open set. By continuity, the set ˆBk in
Sk+1 where the same bj > 0 must also be nonempty. The set ˆEk ⊂ Sk+1
where bj = 0 for j < k is a 1–manifold with boundary. A neighborhood of
Ek in ˆEk lies in the boundary of ˆBk.
Consider ˆEk. As a 1–manifold, it consists of closed components and arcs.
The part of its boundary contained in Sk is the set Ek, so consists of an odd
number of points. Hence there must be an odd number of arc comp onents
of ˆEk with exactly one endpoint in Sk.
CUSP SHAPES UNDER CONE DEFORMATION 21
Consider the other boundary components of ˆEk. They must lie on faces
of Sk+1. Recall the set {bj = 0} does not intersect any face fj where sj = 0.
Thus the only possible additional face of intersection of ˆEk and Sk+1 is the
face on which sk = sk+2 = · · · = sn = 0, spanned by vertices t1, . . . , tk−1 and
tk+1 (note this face is in fk). By induction (using the induction hypothesis
with vertices renumbered), there are an odd number of inters ection points
of ˆEk on this face of Sk+1.
Thus there must be an odd number of arcs of ˆEk running from Sk to the
face fk. Along any of these arcs, bk goes from positive (at a point of Ek on
Sk) to negative (since bk < 0 on fk). Thus it must be zero at an odd number
of interior points. Each of these points is in Ek+1. We may also have points
of Ek+1 coming from the intersection of {bk = 0 } with closed components
of ˆEk, or with arc components of ˆEk with both endpoints of the arc on the
same face (either Sk or fk). In the former case, {bk = 0} must intersect any
closed component an even number of times, and in the latter ca se bk has the
same sign on both endpoints, so again {bk = 0 } intersects the arc an even
number of times. Thus the total number of points in Ek+1 is odd.
At each point in Ek+1, we have b1 = b2 = · · · = bk = 0, and we have
bk+2 through bn all less than or equal to zero. Since the sum of all the bj is
positive, bk+1 must be positive. This implies Bk+1 is a nonempty open set,
and the points of Ek+1 are on its boundary. □
This completes the proof of Lemma 4.1. □
Now, as mentioned above, the choice of ¯ s is tied to the rates at which the
cone angles are varying. Lemma 4.1 implies that a desired ¯ s exists, but gives
us no further information about ¯s. In particular, some cone angle may reach
2π before the others. When this happens, the hyperbolic struct ure in the
corresponding tube about the singular locus is nonsingular . We may thus
view the deformation from this point on as a deformation on a c one manifold
with one fewer component of the singular locus. We do this, ob taining
deformations with fewer and fewer singular components, unt il each cone
angle has reached 2 π.
