---
doc_id: thurston
doc_title: "The Geometry and Topology of Three-Manifolds"
section_id: page-028
section_title: "Page 28"
section_number: null
pages: 28-28
source_pdf: Thurston.pdf
source_sha256: 6010919ed83edd81
toc_source: undetermined
doc_brief: "The Geometry and Topology of Three-Manifolds — 33 sections: Page 1; Page 2; Page 3"
---
2.6. TRIGONOMETRY.
We will use the notation Y ? to denote this hyperplane, with the normal orientation
determined by Y . (We have seen this correspondence before, in 2.4.)
2.6.2.
If X and Y 2 Hn, then c(X, Y ) = cosh d (X, Y ),
where d (X, Y ) denotes the hyperbolic distance between X and Y .
To prove this formula, join X to Y by a geodesic Xt of unit speed. From 2.6.1 we
2.14
have
¨Xt = Xt,
Xt · ˙X0 = 0,
so we get c( ¨Xt, Xt) = c(Xt, Xt), c( ˙X0, X0) = 0, c(X, X0) = 1; thus c(X, Xt) = cosh t.
When t = d (X, Y ), then Xt = Y , giving 2.6.2.
If X? and Y ? are distinct hyperplanes, then
2.6.3.
X? and Y ? intersect
() Q is positive deﬁnite on the subspace hX, Y i spanned by X and Y
() c(X, Y )2 < 1
=) c(X, Y ) = cos \(X, Y ) = −cos \(X?, Y ?).
To see this, note that X and Y intersect in Hn () Q restricted to X? \ Y ? is
indeﬁnite of type (n −2, 1) () Q restricted to hX, Y i is positive deﬁnite. (hX, Y i
is the normal subspace to the (n −2) plane X? \ Y ?).
2.15
There is a general elementary formula for the area of a parallelogram of sides X
and Y with respect to an inner product:
area =
p
X · X Y · Y −(X · Y )2 = kXk · kY k ·
p
1 −c(X, Y )2.
This area is positive real if X and Y span a positive deﬁnite subspace, and pos-
itive imaginary if the subspace has type (1, 1). This shows, ﬁnally, that X? and
Y ? intersect
()
c (X, Y )2 < 1. The formula for c(X, Y ) comes from ordinary
trigonometry.
Thurston — The Geometry and Topology of 3-Manifolds
19
