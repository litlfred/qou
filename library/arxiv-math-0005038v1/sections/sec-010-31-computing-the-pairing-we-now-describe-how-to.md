---
doc_id: arxiv-math-0005038v1
doc_title: "BRAID GROUPS ARE LINEAR STEPHEN J. BIGELOW"
section_id: sec-010-31-computing-the-pairing-we-now-describe-how-to
section_title: "Computing the pairing. We now describe how to compute the pairing be-"
section_number: 3.1
pages: 6-8
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
doc_brief: "BRAID GROUPS ARE LINEAR STEPHEN J. BIGELOW — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
tween a give noodle and fork. Let N be a noodle and let F be a fork. By applying a
preliminary isotopy, we can assume that T (F ) intersects N transversely at a ﬁnite
number of points, which we label z1, . . . , zl. Let F ′ be a parallel copy of F . Choose
F ′ so that T (F ′) intersects N transversely at z′
1, . . . , z′
l, where zi and z′
i are joined
by a short arc in N which meets no other zj or z′
j. Let z be the vertex which lies
in all three edges of F , and let z′ be the vertex which lies in all three edges of F ′.
For every pair {zi, z′
j} there exist unique integers ai,j and bi,j such that ˜Σ( F )
intersects qai,j tbi,j ˜Σ( N ) at a point in the ﬁber of {zi, z′
j}. Let ǫi,j denote the sign
of that intersection. Let mi,j = qai,j tbi,j . Then
⟨N, F ⟩ =
l∑
i=1
l∑
j=1
ǫi,j mi,j .(8)
We can compute mi,j as follows. Deﬁne the following embedded arcs in D \ P .
BRAID GROUPS ARE LINEAR 7
• α1 from d1 to z along the handle of F ,
• α2 from d2 to z′ along the handle of F ′,
• β1 from z to zi along T (F ),
• β2 from z′ to z′
j along T (F ′),
• γ1 from zi to dk along N , where k = 1, 2 is such that γ1 does not pass through
z′
j,
• γ2 from z′
j to dk′ along N , where k′ = 1 , 2 is such that γ2 does not pass
through zi.
Let
δi,j = {α1, α2}{β1, β2}{γ1, γ2}.
Then
mi,j = φ(δi,j ).
We can calculate the exponent ai,j even more explicitly. For k = 1 , . . . , l, let ζk
be the arc from d1 to zk along F , then back to d1 along N . Let ak be the sum of
the winding numbers of ζk around each of the puncture points. Let ζ be the arc
from d1 to d2 along N , and then back to d1 moving clockwise along ∂D. Let a be
the sum of the winding numbers of ζ around the puncture points.
Claim 3.2. ai,j = ai + aj + a.
Proof. Let ζ′
k be the arc from d2 to z′
k along F ′, then back to d2 along N . Let a′
k
be the sum of the winding numbers of ζ′
k around each of the puncture points. If zi
is closer to d1 than z′
j along N then ai,j = ai + a′
j. If not, then ai,j = a′
i + aj. But
a′
k = ak + a for all k = 1, . . . , l, so in either case ai,j = ai + aj + a.
In order to compute ǫi,j we need to choose orientations for Σ( F ), Σ( N ) and C.
We choose the orientation on C induced by the product orientation on D × D. We
orient Σ( F ) and Σ( N ) as follows.
Let f : T (F ) → I and f ′ : T (F ′) → I be diﬀeomorphisms which give T (F ) and
T (F ′) parallel orientations. Let f1 and f2 be the maps from Σ( F ) to I such that
if x ∈ T (F ) \ P and y ∈ T (F ′) \ P then f1({x, y}) = f (x) and f2({x, y}) = f ′(y).
Then the 2-form d f1 ∧ d f2 deﬁnes an orientation on Σ( F ).
Let g : N → I be a diﬀeomorphism such that g(d1) = 0 and g(d2) = 1. Let
g1 and g2 be the maps from Σ( N ) to I given by g1({x, y}) = min( g(x), g(y)) and
g2({x, y}) = max( g(x), g(y)). Then the 2-form dg1 ∧ dg2 deﬁnes an orientation on
Σ( N ).
Claim 3.3. With these orientations, ǫi,j = −mi,i mi,j mj,j |(q = 1, t = −1).
Proof. By deﬁnition, ǫi,j is the sign of the volume form dg1 ∧ dg2 ∧ d f1 ∧ d f2 at the
point {zi, z′
j} in C. This is determined by the following three things:
• the sign of the intersection of N with T (F ) at zi,
• the sign of the intersection of N with T (F ′) at z′
j,
• which of zi and z′
j is closer to d1 along N .
These in turn are determined by the following three values respectiv ely:
• mi,i |(q = 1, t = −1),
• mj,j |(q = 1, t = −1),
• mi,j |(q = 1, t = −1).
