---
doc_id: arxiv-hep-th-9811173v1
doc_title: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links"
section_id: sec-033-55-dedekind-zeta-values-from-12-crossing-feynman
section_title: "Dedekind zeta values from 12-crossing Feynman knots"
section_number: 5.5
pages: 21-23
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are ratio nally related to"
---
At 12 crossings, corresponding to 8 loops in QFT, Broadhurst and K reimer [14] found
that 7 of the 2,176 hyperbolic knots are positive. We found that 3 of these have rational
Dedekind-zeta invariants, with
Z23, 3 = 1
3 × vol(σ1σ 3
2σ1σ 7
2) (70)
Z848, 4 = 1 × vol(σ1σ 5
2σ1σ 5
2) (71)
Z2068, 4 = 2 × vol(σ 3
1σ 3
2σ 3
1σ 3
2) (72)
The ﬁrst two are those identiﬁed as Feynman knots in [13, 14]. Again, we ﬁnd it uncanny
that, with odds of at least 100 : 1 against, both Feynman knots pro ved to have single-
complex-place invariant trace ﬁelds. It is clear that the Dedekind sin gle-complex-place
20
criterion and the Feynman positivity criterion are strongly related. The origin of this
association is, however, quite unclear to us.
Most notable is the result (70) for the 12-crossing positive knot wit h braid word
σ1σ 3
2σ1σ 7
2, which is associated [13] with the irreducible MZV ζ(9, 3) in QFT. It has a
rather small, and very special, volume:
vol(σ1σ 3
2σ1σ 7
2) = vol(5 2) = 3
10 × vol(949) = 3
7 × vol(72
2) = 3Z23, 3 ≈ 2. 828122 (73)
which is precisely 3 times the volume of the closed Weeks manifold, m003 (−3, 1), conjec-
tured to be the smallest of all hyperbolic manifolds. The knot σ1σ 3
2σ1σ 7
2 is the ﬁrst in the
sequence of hyperbolic Feynman knots [14] F2n := σ1σ 3
2σ1σ 2n− 5
2 , with 2 n ≥ 12 crossings,
associated with ζ(2n − 3, 3) in Feynman diagrams with n + 2 ≥ 8 loops.
We found that the equality of the volumes of F12 and 5 2 generalizes to
vol(σ1σ 3
2σ1σ 2n− 5
2 ) = vol(σ1σ 3
2σ1σ 11− 2n
2 ) (74)
where the knot on the r.h.s. is formally obtained by n → 8 −n and has no more than
2n − 6 crossings. For 2 n ≥ 12 we also found that
vol(F12) ≤ vol(F2n) ≤ vol(92
60) = 1
2Z7 ≈ 5. 333489 (75)
where Z7 is the pivot of (26), which is the ﬁrst of the non-trivial Clausen relat ions from
1-loop box diagrams. At large n, the behaviour was measured to be
vol(F2n) = 1
2Z7 − C
( 1
4n − 1)2 +O(1/n 4) (76)
with C ≈ 0. 8160, found from 12-digit SnapPea results, with up to 500 crossing s.
The asymptote suggested that the manifolds complementary to th e series F2n of Feyn-
man knots might be isometric to a series of Dehn ﬁllings of a manifold with volume 1
2Z7.
The drill command of Snap suggested the manifold s785, which we found to be isomet-
ric to the complement of the link 9 2
60. Performing the surgeries ( −2, 1)... (−21, 1) on its
second cusp, we obtained 20 manifolds and asked SnapPea to compa re them with the
manifolds complementary to the Feynman knots F2n, with crossing numbers from 12 to
50. The result was isometry, in all 20 cases. It was then possible to c ompute 64 good
digits of
C = 0. 8160162119959694990691941006445603982758744790599736680521553757...
(77)
from 20 high-precision Snap triangulations of s785( , )(4 −n, 1), with n =O(103). It would
be interesting to obtain analytical results for asymptotic changes [45] in volume, such as
that given by (77).
Now one sees the origin of the invariance (74) of volumes, under the transformation
n → 8 −n. This merely ﬂips a sign of the Dehn surgery on the torus [46] curve ( 4 −n, 1).
The ﬁxed point, at n = 4, is the non-hyperbolic longitudinal surgery (0 , 1), correspond-
ing to the (4 , 3) torus knot, F8 := (σ1σ 3
2)2 ∼ (σ1σ2)4 = 8 19, which is the ﬁrst 3-braid
21
Feynman knot, found at 6 loops [11] in QFT, where it signals the appea rance of the
ﬁrst irreducible [40, 41] MZV, ζ(5, 3), in the counterterms of φ 4-theory. At 7 loops, with
n = 5, the surgery ( −1, 1) is likewise non-hyperbolic, corresponding to the (5 , 3) torus
knot F10 := σ1σ 3
2σ1σ 5
2 ∼ (σ1σ2)5 = 10 124, associated with ζ(7, 3). Only at 12 crossings,
and hence 8 loops, does this series of Feynman knots start to be hy perbolic. One thus
expects to ﬁnd a rather special volume at 12 crossings, as is indeed seen in (73).
