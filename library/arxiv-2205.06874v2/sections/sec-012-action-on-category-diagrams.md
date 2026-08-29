---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-012-action-on-category-diagrams
section_title: "Action on category diagrams"
section_number: null
pages: 17-18
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
We also use the diagrammatic calculus to describe evaluation functorsev : Fun(M,N )×M→N that send
a pair (F,m ) of a functorF :M→N and an objectm∈ ObM to the objectF (m) and a pair(ν,α ) of a
natural transformationν :F⇒G and a morphismα :m→m′ to the morphismνm′◦F (α) =G(α)◦νm :
F (m)→G(m′).
For this, we describe objects inM by a thick vertical line and morphisms between them by vertices on this
line. Composition of morphisms is from the top to the bottom, and identity morphisms are omitted from the
diagrams. Thus, a line whose top end is labeled by an objectm inM and whose bottom end by an object
m′ inM describes a morphismα :m→m′ inM.
The diagram for the evaluationev(ν,α ) :F (m)→G(m′) of a natural transformationν :F⇒G in Fun(M,N )
on a morphismα : m→ m′ inM is obtained by placing the diagram forα to the right of a 2-category
diagram forν, such that no vertex of the diagram forν is on the same height as a vertex on the line forα.
The morphismev(ν,α ) is obtained by horizontally projecting the diagram forν on the line forα. All functors
labeling dashed lines to the left of a line segment or vertex on the latter are applied to the associated objects
and morphisms inM. Natural transformations labeling the vertices in the diagram forν are composed with
all functors labeling lines to their left and right and then evaluated on the object ofM to their right. The
resulting morphisms inN are then composed in order of their height.
17
Example 2.7. The diagram
F
G H
K
L
ρ
σ
MP
Q
N
m
m′′
m′
ϕ
ψ
(44)
describes the evaluationev(ν,α ) :FK (m)→GHL(m′′) of ν = (ρL)◦ (Fσ ) :FK⇒GHL from diagram(30)
on the morphismα =ψ◦ϕ :m→m′→m′′ inM. It is the composite
ev(ν,α ) :FK (m)
FK (ϕ)
−−−−→FK (m′)
F(σm′)
−−−−−→FL (m′)
ρL(m′)
−−−−→GHL(m′)
GHL(ψ)
−−−−−→GHL(m′′).
Note that the evaluation depends only on the natural transformation represented by the diagram on the left
and on the morphism represented by the line on the right, but not on the relative position of vertices in the
two diagrams. This follows from naturality and corresponds to the identity
K
L
m
m′
σ
ϕMP =
K
L
m
m′
σ
ϕ
MP
L(ϕ)◦σm =σm′◦K(ϕ) (45)
which allows one to move vertices in the diagram forFun(M,N ) above or below vertices on the line forM.
One can thus drop the requirement that the former are at different heights from the latter. Any diagram that
violates this condition can be deformed into one that satisfies it by slightly displacing the vertices on the line
on the right. As all ways of doing so yield the same morphism, its evaluation is defined by these deformations.
We also use diagrammatic calculus to describe the composites of morphisms of the formev(ν,α ) with general
morphisms inN. The resulting diagrams consist of a multicoloured thick line on the right and a diagram for
Fun(M,N ) to the left whose lines may end either at the top or bottom of the diagram forFun(M,N ) or on
vertices on the thick line on the right. For instance, the following diagrams describe morphismsτ :J(m)→n
and ω :n→J(m) inN for a functorJ :M→N
J m
n
τ
M
N
J m
n
ω
M
N
(46)
In this diagram, the dashed line may also stand for a composite functor and may be replaced by several
dashed lines that end in a common vertex of the line on the right. ForC-module orD-right module categories
M andN, any dashed line may be replaced by a thin black or grey line labeled with an object ofC orD
that stands for an endofunctorc▷− or−◁d.
