---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-002-1-some-physics-background-electromagnetism
section_title: "§1. Some Physics Background Electromagnetism"
section_number: null
pages: 3-4
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
Electromagnetism
The electric ﬁeld E and the magnetic ﬁeld B in R3 are governed by Maxwell’s
equations, of T-shirt fame. Think of E and B, respectively, as a 1-form and a 2-form
on R3. Both are time-dependent, so we combine them into the electromagnetic ﬁeld
F := E∧dt + B, a 2-form on R4. Maxwell’s equations in vacuo are:
dF = 0
d ∗F = 0.
Here ∗is the Hodge star operator on forms on R4, determined by the Minkowski
metric g = dx2 + dy2 + dz2 −c2dt2. (The speed of light c is usually set to 1 by
adjusting units.)
The same equations make sense for an unknown 2-form F on any (pseudo)
Riemannian manifold (X, g). They are clearly invariant under the group of global
4
RON Y. DONAGI
isometries of (X, g).
When dim X = 4, the equations are also invariant under
the duality F 7→∗F.
When X = R4 with the Minkowski metric, this duality
interchanges the electric and magnetic ﬁelds. The group of isometries in this case
is the Poincare group, an extension of the Lorentz group SO(3, 1) of rotations by
the group (R4, +) of translations.
Geometrically, we ﬁx a U(1)-bundle L on X and consider a connection A on L
as a new variable. The ﬁrst equation dF = 0 is interpreted as saying that (locally)
F = dA is the curvature. The remaining equation then is d ∗dA = 0. The group of
isometries of the triple (X, g, L) acts on the connections and preserves the equation.
This is an extension of the group of those isometries of (X, g) which preserve L by
the gauge group of C∞maps from X to U(1). The duality is still there, but is now
hidden.
Now impose an external ﬁeld j. (In R4, j is a 3-form whose dx∧dy∧dz com-
ponent is the charge density, while the other 3 components give the current.) The
equations become
dF = 0,
d ∗F = j,
and duality is lost. Geometrically, once we think of F as curvature, the ﬁrst equation
becomes a tautology (the Bianchi identity), while the second is an extra condition
which may or may not hold. Physically, we explain this asymmetry as due to the
absence of magnetic charges (“monopoles”).
Dirac proposed that some magnetic charges can be introduced by changing the
topology, or allowing singularities. For example, a monopole at the origin of R3 is
represented by a U(1)-bundle on (R3
x,y,z ∖0) × Rt. Such bundles are characterized
topologically by their Chern class c1 ∈Z, and this c1 is interpreted as the magnetic
charge at the origin. Indeed, the “magnetic charge” at the origin is just the total
magnetic ﬂux across a small sphere S2 around the origin in R3; this is the integral
over S2 of B, which equals the integral of F, which is c1. We can extend F to R4 as
a distribution, but now dF is the δ-function c1.δx,y,z instead of dF = 0. This is not
yet suﬃcient to restore the symmetry to Maxwell’s equations: the electric charge
is arbitrary, but the magnetic charge is allowed only in discrete “quanta”. This
does raise the possibility, though, that complete symmetry could be restored in a
quantum theory, where, as in the real world, electric charge also comes in discrete
units. Indeed, Dirac discovered that in quantum mechanics, where an electrically
charged particle is represented by a wave function satisfying Schrodinger’s equation,
the electric charge e of one particle and the magnetic charge g of another (in
appropriate units) satisfy eg ∈Z . This has the curious interpretation that all
electric charges are automatically quantized as soon as one magnetic monopole
exists somewhere in the universe.
In [MO], Montonen and Olive conjectured that in certain supersymmetric
Yang-Mills quantum ﬁeld theories the electric-magnetic duality is indeed restored.
This involves an extension of the basic picture in three separate directions: replac-
ing the “abelian” Maxwell equations by the non-abelian Yang-Mills; quantizing the
classical theory; and adding supersymmetry to the Poincar´e invariance.
