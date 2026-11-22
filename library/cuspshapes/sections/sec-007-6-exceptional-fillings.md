---
doc_id: cuspshapes
doc_title: "CUSP SHAPE AND TUNNEL NUMBER"
section_id: sec-007-6-exceptional-fillings
section_title: "Exceptional fillings"
section_number: 6
pages: 12-14
source_pdf: CuspShapes.pdf
source_sha256: 01db19e63193e6ae
toc_source: outline
doc_brief: "CUSP SHAPE AND TUNNEL NUMBER — We show that the set of cusp shapes of hyperbolic tunnel number one manifolds is dense in the Teichm¨uller space of the torus."
---
Recall that Berge knots have tunnel number one. Corollary 5.1 contrasts with the
following proposition concerning Berge knots, which follows from work of Baker [3].
Proposition 6.1. Let [T0] denote the Euclidean similarity structure on the torus that
includes the 1 × 2 rectangle. Let U denote a neighborhood of [T0]. Then there exists
a sequence of hyperbolic Berge knots, all with cusp shape lying in the neighborhood U
of [T0]. Moreover, maximal cusps for these Berge knots limit to a 2 × 4 rectangle.
Proof. Baker showed that large volume Berge knots are obtained by Dehn ﬁlling the
complement of a minimally twisted (2n + 1)-chain link L2n+1 [3]. For V large, any
Berge knot with volume at least V is obtained by such a Dehn ﬁlling. Thus for ﬁxed
n > 0, there is a sequence of such knots converging geometrically to S3∖L2n+1, and
so the cusp shapes of this sequence of knots converge to a cusp shape of S3∖L2n+1.
We show that as n →∞, cusp shapes of S3∖L2n+1 approach [T0]. By symmetry,
cusp shapes of all cusps of S3∖L2n+1 are identical, so we need only show that one
cusp shape approaches this similarity structure.
The minimally twisted (2n + 1)-chain link is obtained by Dehn ﬁlling a link
obtained by the following procedure. First, augment the minimally twisted 3-chain
link; the complement is a hyperbolic manifold with four cusps, three of which have
shape [T0]. Denote the link by La
3. See Figure 4, obtained from SnapPy [12]. Next,
take the augmented minimally twisted 2-chain link, denoted La
2, shown in Figure 5.
This is a hyperbolic manifold with three cusps, two of which have shape [T0].
We will take belted sums, as in Adams [1]. Recall that belted sum cuts two
manifolds along embedded 3-punctured spheres and reglues by isometry of the 3-
punctured spheres. Take the belted sum of S3∖La
3 and S3∖La
2, summing along
the augmentation component of each. The result will be the augmented minimally
twisted 5-chain link La
5. For both La
3 and La
2, the 3-punctured sphere we cut along
meets the cusp under consideration exactly twice in a curve perpendicular to the
cusp, with the two curves spaced equidistantly along the cusp. In Figure 4, the
3-punctured sphere corresponds to the two curves running vertically across the cusp
over the horoball colored cyan. Note they are equidistantly spaced and perpendicular
to the boundary. In Figure 5, the 3-punctured sphere runs over the green horoball.
CUSP SHAPE AND TUNNEL NUMBER
13
Figure 5. The augmented minimally twisted 2-chain link La
2 on the
left. It is hyperbolic. Its two cusps coming from the chain, not the
augmentation component, have cusp shape [T0].
Figure 6. The cusp of a chain component of the minimally twisted
5-chain link is obtained by taking half of that of La
3 and half of that
of La
2.
When we perform the belted sum, we cut along these curves and reassemble, gluing
half of a cusp of La
3 to half of a cusp of La
2 to obtain a cusp of La
5, shown in Figure 6.
Because the cut happened halfway along each, along 3-punctured spheres meeting
full-sized horospheres, the cusp shape is still [T0].
The cusp of the augmentation component under the belted sum is similarly
changed, now by stacking the cusps corresponding to the augmentation components
of La
3 and La
2 along 3-punctured spheres. We do not need to know the geometry of
this cusp precisely, except that the length of the meridian of the cusp has increased.
Now to obtain the augmented minimally twisted (2n + 1)-chain link La
2n+1, induc-
tively take the belt sum of La
2n−1 with La
2. As in the case of La
5, the cusp shape of
the chain link component is obtained by cutting cusps of La
2n−1 and La
2 in half and
assembling half of each into the new cusp. Hence its shape is still [T0]. The cusp
of the augmentation component is obtained by stacking the cusp corresponding to
the augmentation components of La
2n−1 and La
2; this is equivalent to stacking one
copy of the cusp of La
3 and n −1 copies of the cusp of La
2. Thus the meridian length
grows linearly with n.
Note that Dehn ﬁlling the meridian of the augmentation component of La
2n+1
gives the minimally twisted chain link L2n+1. Since the length of the meridian grows
linearly with n, by the hyperbolic Dehn ﬁlling theorem for n large enough, the cusp
shape of L2n+1 will lie in the neighborhood U of [T0]. Take a sequence of ﬁlling
slopes on the other cusps of L2n+1 that have high length and yield a Berge knot.
Again the hyperbolic Dehn ﬁlling theorem implies that the cusp shape of the Berge
knot lies in U.
14
VINH DANG AND JESSICA S. PURCELL
Finally, because Berge knots are obtained by Dehn ﬁlling, which gives a geometri-
cally convergent sequence, not only will their cusp shapes converge, but in addition,
their maximal cusps will converge to the maximal cusp of the unﬁlled component
of the augmented minimally twisted (2n + 1)-chain link. The maximal cusp of a
chain link component of La
3 and La
2 is a 2 × 4 rectangle. (This can be shown via
SnapPy [12] as in Figures 4 and 5, or by hand.) The cutting and regluing in both
cusps is along 3-punctured spheres meeting that maximal cusp in identical horocycle
patterns. Thus the belted sums of these links have cusps that are 2 × 4 rectangles,
and the result follows.
□
Remark 6.2. As noted by the referee, in the proof of Proposition 6.1, the hyperbolic
structure on the augmented, minimally twisted (2n −1)-chain link complement can
also be obtained by taking the (2n−1)-fold cover of the Whitehead link, then cutting
along the 3-punctured sphere bounded by the augmented component, untwisting,
and then regluing. Following this procedure using the geometry of the Whitehead
link complement, for example as in [19], leads to the same results on cusp shapes
without appealing to belted sums.
