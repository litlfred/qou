---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-003-32-path-2-groupoids
section_title: "Path 2-Groupoids"
section_number: 3.2
pages: 14-15
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
Path groupoids play a big though often neglected role in physics: the path
groupoid of a spacetime manifold describes all the possible motions of a point
particle in that spacetime. The path 2-groupoid does the same thing for particles
and strings .
First of all, a 2-groupoid is a 2-category where:
• Every morphism f : x → y has an inverse, f −1: y → x, such that:
f −1f = 1 x and f f−1 = 1 y.
• Every 2-morphism α: f ⇒ g has a vertical inverse , α−1
vert: g ⇒ f , such
that:
α−1
vert · α = 1 f and α · α−1
vert = 1 f .
It actually follows from this deﬁnition that every 2-morphism α: f ⇒ g also has
a horizontal inverse, α−1
hor: f −1 ⇒ g−1, such that:
α−1
hor ◦ α = 1 1x and α ◦ α−1
hor = 1 1x.
So, a 2-groupoid has every kind of inverse your heart could desire.
An example of a 2-group is the ‘path 2-groupoid’ of a smooth manifold M .
To deﬁne this, we can start with the path groupoid P1(M ) as deﬁned in the
previous section, and then throw in 2-morphisms. Just as the morp hisms in
P1(M ) were thin homotopy classes of lazy paths, these 2-morphisms will b e
thin homotopy classes of lazy surfaces.
What is a ‘lazy surface’ ? First, recall that a homotopy between lazy paths
γ, δ: x → y is a smooth map Σ: [0 , 1]2 → M with
Σ(0 , t) = γ(t)
Σ(1 , t) = δ(t)
We say this homotopy is a lazy surface if
• Σ( s, t) is independent of s near s = 0 and near s = 1,
• Σ( s, t) is constant near t = 0 and constant near t = 1.
Any homotopy Σ yields a one-parameter family of paths γs given by
γs(t) = Σ( s, t).
If Σ is a lazy surface, each of these paths is lazy. Furthermore, th e path γs equals
γ0 when s is suﬃciently close to 0, and it equals γ1 when s is suﬃciently close to
1. This allows us to compose lazy homotopies either vertically or horizo ntally
and obtain new lazy homotopies!
However, vertical and horizontal composition will only obey the 2-g roupoid
axioms if we take 2-morphisms in the path 2-groupoid to be equivalence classes
14
of lazy surfaces. We saw this kind of issue already when discussing th e path
groupoid, so we we will allow ourselves to be a bit sketchy this time. The
key idea is to deﬁne a concept of ‘thin homotopy’ between lazy surfa ces Σ
and Ξ. For starters, this should be a smooth map H: [0, 1]3 → M such that
H(0, s, t) = Σ( s, t) and H(1, s, t) = Ξ( s, t). But we also want H to be ‘thin’.
In other words, it should sweep out no volume: the rank of the diﬀer ential dH
should be less than 3 at every point.
To make thin homotopies well-deﬁned between thin homotopy classes of
paths, some more technical conditions are also useful. For these, the reader can
turn to Section 2.1 of Schreiber and Waldorf [87]. The upshot is that w e obtain
for any smooth manifold M a path 2-groupoid P2(M ), in which:
• An object is a point of M .
• A morphism from x to y is a thin homotopy class of lazy paths from x to
y.
• A 2-morphism between equivalence classes of lazy paths γ0, γ1: x → y is a
thin homotopy class of lazy surfaces Σ: γ0 ⇒ γ1.
As we already did with the concept of ‘lazy path’, we will often use ‘lazy s urface’
to mean a thin homotopy class of lazy surfaces. But now let us haste n on to
