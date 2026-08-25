---
doc_id: arxiv-1003.4485v2
doc_title: "email: baez@math.ucr.edu huerta@math.ucr.edu"
section_id: sec-013-52-curvature
section_title: "Curvature"
section_number: 5.2
pages: 46-47
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describ e parallel trans- port for particles and strings in terms of 2-connections on 2 -bundles."
---
2-connection:
F ′ = dA′ + A′ ∧ A′
= d(gAg −1 + g dg−1 + t(a)) +
(gAg −1 + g dg−1 + t(a)) ∧ (gAg −1 + g dg−1 + t(a))
This looks like a mess—but except for the terms containing t(a), this is just the
usual mess we get in ordinary gauge theory when we compute the cu rvature of
a gauge transformed connection. So, we have:
F ′ = gF g−1 + d(t(a)) + t(a) ∧ A′ + A′ ∧ t(a) − t(a) ∧ t(a)
= gF g−1 + t(da) + [ t(a), A′] − t(a) ∧ t(a)
where we use the fact that d(t(a)) = t(da) and rewrite A′ ∧ t(a) + t(a) ∧ A′ as
a graded commutator.
On the other hand, we have
t(B′) = t(α(g)(B)) + t(α(A′) ∧ a) + t(da − a ∧ a)
The G-equivariance of t implies that t(α(g)(B)) = gt(B)g−1, and the g-equivariance
of t implies that t(α(A′) ∧ a) = [ A′, t (a)]. So, we see that
t(B′) = gt(B)g−1 + [ A′, t (a)] + t(da − a ∧ a)
and thus t(B′) = F ′, as desired.
5.2 Curvature
Suppose G is a Lie 2-group whose crossed module is ( G, H, t, α), and let ( g, h, t
, α)
be the corresponding diﬀerential crossed module. Suppose we hav e a connec-
tion on the trivial G-2-bundle over M : that is, a g-valued 1-form A and an
h-valued 2-form B.
As in ordinary gauge theory, we may deﬁne the curvature of this connection
to be the g-valued 2-form given by:
F = dA + A ∧ A.
We also have another g-valued 2-form, the fake curvature F − t(B). Recall
from Section 3 that only a connection with vanishing fake curvature counts as a
2-connection. In other words, we need t(B) = F to obtain well-deﬁned parallel
transport over surfaces.
46
We may also deﬁne the 2-curvature of a connection in higher gauge theory.
This is the h-valued 3-form given by:
Z = dB + α(A) ∧ B.
In the second term here, we compose α: g → aut(H) with the g-valued 1-form A
and obtain an aut(H)-valued function α(g). Then we wedge this with B, letting
aut(H) act on h as part of this process, and obtain an h-valued 2-form.
The intuitive idea of 2-curvature is this: just as the curvature des cribes the
holonomy of a connection around an inﬁnitesimal loop, the 2-curvat ure describes
the holonomy of a 2-connection over an inﬁnitesimal 2-sphere. This can be made
precise using formulas for holonomies over surfaces [69, 88]
If the 2-curvature of a 2-connection vanishes, the holonomy ove r a surface
will not change if we apply a smooth homotopy to that surface while ke eping
its edges ﬁxed. A 2-connection whose curvature and 2-curvatur e both vanish
truly deserves to be called ﬂat . We have seen ﬂat 2-connections already in
our discussion of 4-dimensional BF theory in Section 4.3: the solutions of this
theory are ﬂat 2-connections.
