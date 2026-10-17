---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-006-31-smooth-descent-data
section_title: "Smooth Descent Data"
section_number: 3.1
pages: 11-12
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
---
(d) A descent object (triv, g) is called smooth, if the functor
triv : P1(X)
/ Gr
is smooth, i.e. internal to diﬀeological spaces, and if the components map
g : Y [2]
/ Mor(T )
of the natural equivalence g is the composition of a smooth map ˜g : Y [2]
/ Mor(Gr) with
i : Gr
/ T .
In view of the analogy between (a) - (c) and Sections 2.1 and 2.2, (d) is the analogue of the forthcoming
Section 3.1. Summarizing, we have:
Deﬁnition 2.4.1 ([SW09, Deﬁnition 3.6]).
A transport functor on X with values in T and with
Gr-structure is a locally i-trivializable functor
F : P1(X)
/ T
with smooth descent data.
Transport functors form a category which we denote by Trans1
Gr(X, T ). The main result of our
paper [SW09] is that transport functors are an axiomatic formulation of connection on ﬁbre bundles.
In order to illustrate that, and since we need this result later several times, we provide the following
example. let G be a Lie group, and let Bun∇
G(X) be the category of principal G-bundles with connection
over X. Further, we denote by BG the Lie groupoid with one object and morphisms G, by G-Tor the
category of G-torsors, and by i : BG
/ G-Tor the functor that sends the single object of BG to G,
regarded as a G-torsor over itself. Then, we have:
Theorem 2.4.2 ([SW09, Theorem 5.8]).
Let X be a smooth manifold. The assignment
Bun∇
G(X)
/ Trans1
BG(X, G-Tor) : (P, ω) ✤
/ FP,ω
deﬁned by
FP,ω(x) := Px
and
FP,ω(γ) := τγ,
where x ∈X, γ ∈PX, and τγ is the parallel transport of ω along γ, establishes a surjective equivalence
of categories.
– 11 –
