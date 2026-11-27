---
doc_id: arxiv-2406.18369v2
doc_title: "112 years of listening to Riemannian manifolds"
section_id: sec-006-41-geometric-preliminaries
section_title: "Geometric preliminaries"
section_number: 4.1
pages: 16-17
source_pdf: 2406.18369v2.pdf
source_sha256: 20b3f8dbc40eacc3
toc_source: outline
doc_brief: "112 years of listening to Riemannian manifolds — In1910, HendrikAntoonLorentzdelvedintotheenigmaticLaplace eigenvalue equation, also known as the Helmholtz equation, pondering to what extent the"
---
the plane converging to another domain. To define this, we need a way of measuring
the distance between two sets. We will use Hausdorff distance. Recall that an
isometry in R2 is an affine linear mapping fromR2 to itself which corresponds to a
composition of rotations, translations, and reflections. IfΘ and Ω are two sets in
R2, then the Hausdorff distance betweenΘ and Ω is defined as
D(Θ, Ω) = inf
T,S isometries
dH(T (Θ),S (Ω)),
where
dH(Θ, Ω) = max

sup
x∈Θ
inf
y∈Ω
||x−y||, sup
x∈Ω
inf
y∈Θ
||x−y||

.
Given a sequence of sets{Ωk}∞
k=1 in R2, we say thatΩk converges in Hausdorffto
some set Ω⊂ R2, written Ωk→ Ω as k→∞ , ifD(Ωk, Ω)→ 0 as k→∞ .
For anyx∈ R2, infy∈Ω||x−y|| is often called thedistance betweenx and Ω. The
following proposition gives some justification for the above definition. The proof is
a straightforward application of the definition and can be found in [85, p. 6-7].
Proposition 4.1. Given two non-empty setsΘ, Ω⊂ R2, we havedH(Θ, Ω) = 0 if
and only if Θ = Ω. If we further assume thatΘ and Ω are closed, andϵ >0, we
have dH(Θ, Ω)<ϵ if and only if
Ω⊂
[
x∈Θ
Bϵ(x),
Θ⊂
[
x∈Ω
Bϵ(x),
(15)
where
Bϵ(x) ={y∈ R2 :||x−y||<ϵ}.
112 YEARS OF LISTENING TO RIEMANNIAN MANIFOLDS 17
In§4.2.4wewillusethe Euler characteristic(sometimescalledthe Euler number)
of a bounded domain in the plane. IfΩ⊂ R2 is bounded and consists of finitely
many polygons, then its Euler characteristic is given by
(16) χ(Ω) =V−E +F,
where V is the number of vertices inΩ, E is the number of edges inΩ, andF is
the number of polygons inΩ.
Ifinstead Ωisasmoothlyboundeddomain, onecomputestheEulercharacteristic
using triangulations. Intuitively, a triangulation ofΩ is a collection of “triangles”
which need not have straight edges. Their union should beΩ and the intersection
of two triangles is either empty, a common edge, or a common vertex. For the
precise definition of a triangulation, we refer to [99, Definition 13.4.1]. The Euler
characterstic ofΩ is then given by the Euler characterstic of the given triangulation.
By [99, Corollary 13.4.6],χ(Ω) is independent of the choice of triangulation. Ahole
of Ω is a bounded connected component ofR2\Ω. The number of holes in a domain
is related to the Euler characteristic by the following result.
Theorem 4.2([59], Thm. 2.44). If Ω has r holes, thenχ(Ω) = 1−r.
