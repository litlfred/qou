---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-004-the-serre-functor-on-dx
section_title: "The Serre functor on D(X)."
section_number: null
pages: 10-12
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
If X is a space then we consider the functor
S : D(X)→ D(X); E ↦→ ωX[dim X] ⊗ E ,
where ωX is the canonical line bundle of X. Serre duality then gives natural,
bifunctorial isomorphisms
ηE ,F : HomD(X)(E , F ) ∼−→ HomD(X)(F , SE )∨
for any objects E , F ∈ D(X), where − ∨ denotes the dual vector space.
10
A functor such as S, together with isomorphisms as above, was called a
Serre functor by Bondal and Kapranov [2] (see also [17]). From this data,
for any object E ∈ D(X), deﬁne the Serre trace as follows:
Tr: Hom(E , SE )→ k; Tr(α) := ηE ,E (IdE )(α).
Note that from this trace we can recover ηE ,F because
ηE ,F (α)(β) = Tr(β ◦ α).
We also have the commutativity identity
Tr(β ◦ α) = Tr(Sα ◦ β).
Yet another way to encode this data is as a perfect pairing, th e Serre pairing:
⟨− , − ⟩S : Hom(E , F ) ⊗ Hom(F , SE )→ k; ⟨α, β ⟩S := Tr(β ◦ α).
2.2 Serre kernels and the Serre functor for D(X × Y).
We are interested in kernels and the 2-category V ar, so are interested in
Serre functors for product spaces X × Y, and these have a lovely description
in the 2-categorical language. We can now deﬁne one of the key objects in
this paper.
Deﬁnition. For a space X, the Serre kernel ΣX ∈ 1-HomV ar(X, X) is deﬁned
to be ∆∗ωX[dim X] ∈ D(X × X), the kernel inducing the Serre functor on
X. Similarly the anti-Serre kernel Σ− 1
X ∈ 1-HomV ar(X, X) is deﬁned to be
∆∗ω− 1
X [− dim X] ∈ D(X × X).
Notation. In string diagrams the Serre kernel will be denoted by a dashe d-
dotted line, while the anti-Serre kernel will be denoted by a dashed-dotted
line with a horizontal bar through it (see the pictures in Sec tion 3.2).
The Serre kernel can now be used to give a natural description , in the 2-
category language, of the Serre functor on the product X × Y.
Proposition 1. For spaces X and Y the Serre functor SX×Y : D(X × Y)→
D(X × Y) can be taken to be ΣY ◦ − ◦ ΣX.
Proof. The Serre functor on D(X × Y) is given by
SX×Y(Φ) = Φ ⊗ π∗
XωX ⊗ π∗
YωY[dim X + dim Y].
However, observe that if Φ ∈ D(X × Y) and E ∈ D(X) then
Φ ◦ ∆∗E ∼= Φ ⊗ π∗
XE ,
where πX: X × Y→ X is the projection. This is just a standard application
of the base-change and projection formulas. Similarly if F ∈ D(Y) then
∆∗F ◦ Φ ∼= π∗
YF ⊗ Φ. From this the Serre functor can be written as
SX×Y(Φ) = ΣY ◦ Φ ◦ ΣX.
11
This means that the Serre trace map on X × Y is a map
Tr: 2-HomV ar(Φ, ΣY ◦ Φ ◦ ΣX)→ k
which can be pictured as
Tr


Φ 
Φ 

 ∈ k,
where the Serre kernel is denoted by the dashed-dotted line.
We will see below that we have ‘partial trace’ operations whi ch the Serre
trace factors through.
