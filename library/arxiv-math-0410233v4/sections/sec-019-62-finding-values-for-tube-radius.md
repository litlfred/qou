---
doc_id: arxiv-math-0410233v4
doc_title: "Cusp shapes under cone deformation"
section_id: sec-019-62-finding-values-for-tube-radius
section_title: "Finding values for tube radius"
section_number: 6.2
pages: 39-41
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "Cusp shapes under cone deformation — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
radius remains larger than R1 = 0.56 throughout the cone deformation. We
can do so by again applying work of Hodgson and Kerckhoﬀ [14]. They
show that in the neighborhood of the j-th component of the singular locus,
we can increase the cone angle from 0 to 2 π, maintaining the tube radius
R ≥ R1, provided equation (24) of the proof of Lemma 4.3 holds.
That is, consider a particular component of the singular loc us Σ j. The
singular locus consists of crossing circles of the link L. At the j-th crossing
circle, the hyperbolic cone deformation performs Dehn ﬁlli ng along a slope of
the form 1 /nj. Let L0 denote the normalized length of this slope in S3 − L.
We can then increase the cone angle from 0 to 2 π, maintaining the tube
radius bound R ≥ R1, provided the normalized length L2
0 is larger than the
increasing function I(R1) deﬁned in equation (24).
So to ensure R ≥ R1 ≥ 0.56, we compute that L2
0 must be at least
113.044. By Proposition 6.5, we know L2
0 is at least ci, where ci is the
number of crossings in the i-th twist region. Thus by ensuring there are at
least 114 crossings in the i-th twist region, we will guarantee that our tube
radius is at least 0 .56. For general R1, we have the following result.
Lemma 6.6. Let K, L be as above, such that we have a cone deformation
from S3 − L to S3 − K. Fix R1 ≥ 0.531. Then R ≥ R1 throughout the
deformation provided the number of crossings in each twist r egion is at least
I(R1), where I(R1) is deﬁned in equation (24).
6.3. Proof of Theorem 1.8.
Theorem 1.8 Let K be a knot in S3 which admits a prime, twist reduced
diagram with a total of n ≥ 2 twist regions, with each twist region containing
at least c ≥ 116 crossings. In a hyperbolic structure on S3 − K, take a
horoball neighborhood U about K. Normalize so that the meridian on ∂U
has length 1. Then the height H of the cusp of S3 − K satisﬁes:
H ≥ n (1 − f (c))2.
Here f (c) is a positive function of c which approaches 0 as c increases to
inﬁnity. Additionally, H ≤ n(√
n − 1 + f (c))2.
Proof. If K admits a prime, twist reduced diagram with at least 2 twist
regions, then we may form the augmented link L from the diagram of K.
We have seen in §6.1.3 that, provided there are at least 113 crossings in each
twist region of the diagram of K, then S3 − L and S3 − K are connected by
a hyperbolic cone deformation Xt, with X0 = S3 − L, Xτ = S3 − K. The
singular locus will consist of the crossing circle componen ts of L. There will
be n of these.
By results of Section 6.2, if there are at least 114 crossings per twist
region then the tube radius of the deformation is at least R1 = 0.56. Then
40 JESSICA S. PURCELL
1.81.6
1
0.8
1.4
0.6
0.4
1.2
0.2
0
10.8
y = ¯f (R)
1.81.61.4
600
1.2
500
400
1
300
200
0.8
y = I(R)
Figure 13. Graphs of ¯f (R) and I(R). Here ¯f (R) gives the
bounds in Theorem 1.8 for given tube radius R. I(R) gives
the number of crossings required to guarantee tube radius R.
by Theorem 1.4,
−(2π)2
√
n C(R1)
(1 − e−2R1 )
√
2 ≤ hτ − h0 ≤ (2π)2
√
n C(R1)
(1 − e−2R1)
√
2 ,
where ht denotes the normalized height of the cusp at time t.
And so:
(27) h0 − (2π)2
√
n C(R1)
(1 − e−2R1 )
√
2 ≤ hτ ≤ h0 + (2π)2
√
n C(R1)
(1 − e−2R1)
√
2 .
We may now apply part (2) of Proposition 6.5. This implies tha t the initial
normalized height h0, i.e. the normalized height on S3 − L, is between √n
and
√
n(n − 1).
Plug this into the left hand side of the above equation and we ﬁ nd:
(28) hτ ≥ √n
(
1 − (2π)2
√
C(R1)
(1 − e−2R1)
√
2
)
.
For the right hand side, we ﬁnd:
(29) hτ ≤ √n
(
√
n − 1 + (2π)2
√
C(R1)
(1 − e−2R1)
√
2
)
.
The term C(R1) can be computed explicitly using the formulas in the
proof of Lemma 4.3. Recall C(R1) is strictly decreasing, approaching 0 as
R1 approaches inﬁnity. Thus the function
¯f (R1) = (2 π)2
√
C(R1)
(1 − e−2R1)
√
2
,
which appears in both (28) and (29), is decreasing with R1, approaching 0.
The graph of ¯f , as well as that of I(R), is shown in Figure 13.
CUSP SHAPES UNDER CONE DEFORMATION 41
When R1 = 0.56, 1 − ¯f (R1) is negative. Since hτ is known to be positive,
this doesn’t give a very good estimate in (28). To get a better estimate,
we increase R1. The value 1 − ¯f (R1) becomes positive when R1 is about
0.6624. However, as R1 increases, so does I(R1), so by Lemma 6.6, we need
to increase the number of crossings in each twist region to gu arantee that
the tube radius remains larger than R1 throughout the deformation. In
particular, c must be at least 116 to ensure R1 ≥ 0.6624.
In general, let f (c) = ¯f (I −1(c)). Since I(R) is strictly increasing for
R ≥ 0.56, this is well deﬁned. Then for c ≥ 116, 1 − f (c) is positive.
To ﬁnish the proof, note that we can scale so that the meridian of the
cusp of S3 − K has length 1. Then the actual height H of the cusp of S3 − K
will be at least ( hτ )2. □
Notice in Figure 13 that ¯f is close to 0 for values of R near 2. However
for R this size, I(R), or the number of crossings required per twist region, is
nearly 700. We ﬁnd a nice compromise by choosing R = 1.0. Then I(R) is
not much larger than 116, and yet 1 − ¯f is already over 0 .8. We use this fact
in the following corollary, which gives more explicit numbe rs to the results
of Theorem 1.8.
Corollary 6.7. Let K be as in the previous theorem, with at least c ≥ 145
crossings in each twist region. Then when the meridian of the c usp of S3 −K
is normalized to have length 1, the height of the cusp satisﬁes:
H ≥ n (0.81544)2.
Proof. Letting c ≥ 145 in the above theorem ensures that R > R 1 = 1 .0.
Then 1 − f (c) = 1 − ¯f (1.0) ≥ 0.81544. □
