---
doc_id: arxiv-math-0505170v2
doc_title: "AN AVERAGING PROCESS FOR UNIPOTENT GROUP ACTIONS"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-2
source_pdf: math0505170.pdf
source_sha256: 0846b74f9c7c55cb
toc_source: outline
doc_brief: "AN AVERAGING PROCESS FOR UNIPOTENT GROUP ACTIONS — We present an averaging process for sections of a torsor under a unipotent group."
---
Let K be a ﬁeld of characteristic 0. For any natural number q let K[t0, . . . , tq]
be the polynomial algebra, and let ∆q
K be the geometric q-dimensional simplex
∆q
K := Spec K[t0, . . . , tq]/(t0 + · · · + tq −1).
Our main result is the following theorem.
Theorem 0.1. Let G be a unipotent algebraic group over K, let X be a K-scheme,
let Z be a G-torsor over X, and let Y be any X-scheme. Suppose f = (f0, . . . , fq)
is a sequence of X-morphisms fi : Y →Z. Then there is an X-morphism
wavG(f) : ∆q
K × Y →Z
called the weighted average, such that the operation wavG is symmetric, simplicial,
functorial in the data (G, X, Y, Z), and is the identity for q = 0.
“Symmetric” means that wavG is equivariant for the action of the permutation
group of {0, . . ., q} on the sequence f and the scheme ∆q
K. “Simplicial” says that
as q varies
wavG : HomX(Y, Z)q+1 →HomX(∆q
K × Y, Z)
is a map of simplicial sets. “Functorial in the data (G, X, Y, Z)” means that e.g.
given a morphism h : Z →Z′ of G-torsors over X, one has
h ◦wavG(f) = wavG(h ◦f),
where h ◦f is the sequence (h ◦f0, . . . , h ◦fq). Theorem 0.1 is repeated, in full
detail, as Theorem 1.11.
Observe that when we restrict the morphism wavG(f) to each of the vertices
of ∆q
K we recover the original morphisms f0, . . . , fq. This is due to the simplicial
property of wavG. Thus wavG(f) interpolates between f0, . . . , fq. This is illustrated
in Figure 1.
Date: 12 January 2006.
Key words and phrases. Unipotent group, torsor, simplicial set.
Mathematics Subject Classiﬁcation 2000. Primary: 14L30; Secondary: 18G30, 20G15.
This work was partially supported by the US - Israel Binational Science Foundation.
1
2
AMNON YEKUTIELI
