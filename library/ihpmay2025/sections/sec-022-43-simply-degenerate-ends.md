---
doc_id: ihpmay2025
doc_title: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS"
section_id: sec-022-43-simply-degenerate-ends
section_title: "Simply degenerate ends"
section_number: 4.3
pages: 28-29
source_pdf: IHPMay2025.pdf
source_sha256: 0440a39721552a9e
toc_source: outline
doc_brief: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS — These notes are designed to accompany my mini-course on hyperbolic 3-manifolds at IHP in May 2025."
---
Peter Scott [69] proved that every irreducible 3-manifold N with finitely generated fundamen-
tal group contains a compact submanifold C so that the inclusion of C into M is a homotopy
equivalence. We call such a submanifold a compact core for N. If N is homeomorphic to the
interior of a handlebody, it is easy to construct compact cores which are not isotopic, since one
may form a compact core by thickening any bouquet of circles in N whose inclusion into N is
a homotopy equivalence. McCullough, Miller and Swarup [56] proved that this core is unique
in the sense that if C1 and C2 are two compact cores for N, then there is a homeomorphism
from C1 to C2 which is homotopic, within N, to the inclusion of C1 into N. I believe it is the
case that the compact core is unique up to isotopy when the compact core has incompressible
boundary (i.e. when π1(N) is freely indecomposable).2
2This will definitely be the case when N is topologically tame, i.e homeomorphic to the interior of a compact
3-manifold, and its compact core has incompressible boundary
IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS
29
If NΓ is a hyperbolic 3-manifold, let CΓ denote a compact core for NΓ. We will call each
component of NΓ −CΓ an end of NΓ. If E is an end of NΓ, then any open subset of U so that
E −U is bounded, will be called a nieghborhood of the end E. (See Section 1.2 in Bonahon
[13] for a discussion of why this is equivalent to the more abstract definition of ends.)
Inspired by the examples above, we say that an end of a hyperbolic 3-manifold is simply
degenerate if it has a neighborhood U which is homeomorphic to S × (0, ∞) (where S is
homeomorphic to the boundary of E) and there exists a sequence {fn : S →U} of simplicial
hyperbolic surfaces so that {fn(S)} exits the end E (i.e. for any compact subset K of the closure
of E, there exists N so that if n ≥N, then fn(S) ∩K = ∅) and, for all n, fn is homotopic,
within U to the inclusion map ι : S →S × {1} given by ι(x) = (x, 1).
Furthermore, we say that an end of NΓ is convex cocompact if it has a neighborhood disjoint
from C(NΓ). Notice, that NΓ is convex cocompact if and only if every end of NΓ is convex
cocompact.
We say that NΓ is geometrically tame if every end of NΓ is either simply degenerate or convex
cocompact. Notice that if NΓ is geometrically tame, then every end has a neighborhood of the
form S × (0, ∞). It follows, that if NΓ is geometrically tame, then it is also topologically tame,
i.e. homeomorphic to the interior of a compact 3-manifold.
We note that these definitions can be exended to the setting of hyperbolic 3-manifolds with
cusps, but we will forego the technicalities involved.
Historical Remarks: (1) Thurston’s original definition of a simply degenerate end was only given
in the setting where the compact core has incompressible boundary. In this case, the assumption
that each simplicial hyperbolic surface fn is homotopic to the inclusion map ι within U is un-
necessary (in fact, follows from results in 3-manifolds). His simpler definition was that there
exist a sequence of simple closed curves αn on ∂E whose geodesic representatives {α∗
n} exit
E. Given such a sequence of curves one may construct simplicial hyperbolic surfaces fn which
realize αn with one vertex, and one may easily check that the resulting hyperbolic surfaces must
also exit E. However, in the compressible case this additional assumption is necessary to ensure
that the regions homologically bounded by fn(S) and ∂E exhaust E. This new definition first
appears in [25].
(2) One need not use simplicial hyperbolic surfaces in the definition of simply degenerate
ends. Most of Thurston’s work uses pleated surfaces instead of simplicia hyperbolic surfaces.
Minsky [57] showed that one can use harmonic maps in place of simplicial hyperbolic surfaces.
In recent work, authors often simply use 1-Lipschitz maps of hyperbolic surfaces (which include
all of these examples). However, one cannot use minimal surfaces, since they are much more
sparse than these other examples.
