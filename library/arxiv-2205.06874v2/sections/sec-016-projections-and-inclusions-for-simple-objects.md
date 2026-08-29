---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-016-projections-and-inclusions-for-simple-objects
section_title: "Projections and inclusions for simple objects"
section_number: null
pages: 24-26
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
LetM a finite semisimpleC-linear category, equipped with a traceθ in the sense of Definition 1.13 and letI
be a set of representatives of the isomorphism classes of its simple objects. Then every objectx inM can
be expressed as a direct sumx∼=⊕m∈Im⊕nxm with multiplicitiesnxm = dimC HomM(m,x )∈ N0. One can
choose bases{pα
xm} of HomM(x,m ) and{jα
xm} of HomM(m,x ) with m∈I and α∈{ 1,...,n xm} such that
pβ
xm′◦jα
xm = δαβδmm′
dim(m) 1m 1x =
∑
m∈I
nxm∑
α=1
dim(m) jα
xm◦pα
xm (53)
for allm,m′∈I, where dim(m) =θm(1m). Their normalisation is fixed by (53) such that
θm(pβ
xm◦jα
xm) =δαβ, (54)
and this implies with the cyclicity of the trace
∑
m∈I
dim(m) dimC HomM(m,x ) = dim(x). (55)
The identities (53) imply for all morphismsϕ :m→x and ψ :x→m
ϕ =
nxm∑
α=1
θm(pα
xm◦ϕ)jα
xm ψ =
nym∑
α=1
θm(ψ◦jα
xm)pα
xm (56)
and for all morphismsχ :x→y
χ =
∑
m∈I
nxm∑
α=1
nym∑
β=1
dim(m)θm(pβ
ym◦χ◦jα
xm)jβ
ym◦pα
xm. (57)
These identities are represented by the diagrams
∑
α x
m
m
ϕ
α
m
x
α (56)
=
m
x
ϕ ∑
α x
m
m
α
ψ
x
m
α (56)
=
x
m
ψ
∑
m
∑
α,β dim(m)
x
y
m
m
α
χ
β
x
y
m
α
β
(57)
=
x
y
χ
(58)
IfM andN are bimodule categories with bimodule traces over spherical fusion categoriesC andD and
F :M→N is a C-linear functor, then one can characteriseF by decomposing the images of simple objects
m∈IM into simple objectsn∈IN. We writepα
Fmn =pα
F(m)n :F (m)→n and jα
Fmn =jα
F(m)n :n→F (m)
for the associated projection and inclusion morphisms satisfying (53) and denote them by
m
n
F
α
m
n
F
α
(59)
24
such that the identities (53) are given by
n
F m
n′
α
β
= δαβδnn′
dim(n)
n
∑
n,α dim(n)
F
F
m
m
n
α
α
=
F m
(60)
For functors that are 1-morphisms in the pivotal 2-categoriesBimodθ(C,D) and Modθ(C) from Theorem 1.17
and hence have left and right adjoints, the morphismspα
Fmn and jα
Fmn from (59) can also be modified by
composing them with the units and counits of the adjunctions. By composing them with the component
morphisms ofη′F : idM⇒FlF and ϵF :FlF⇒ idN, introduced before Corollary 1.20, one obtains
n
m
F
α
m
n
F
α
(61)
πα
Flnm :Fl(n)→m ι α
Flnm :m→Fl(n)
These morphisms satisfy identities analogous to (60). For allm,m′∈IM and n∈IN one has
m
m′
nF
α
β
= δαβδmm′
dim(m)
m
∑
m,α dim(m)
n
n
m
F
F
α
α
=
F n
(62)
The first identity follows directly from the fact thatm,m′∈IM are simple, by taking the trace and then
using its cyclicity, the second identity in(50) and the first identity in(53) and (60). For the second identity
note that the morphismsπα
Flnm and ια
Flnm can be expressed as linear combinations
πα
Flnm =
∑
β
Mαβpβ
Flmn ια
Flnm =
∑
β
Nαβjβ
Flmn (63)
with invertible complex matricesM = (Mαβ) and N = (Nαβ). The first identity in(62) implies MT =N−1.
Inserting (63) into the left-hand side of the second equation in(62), together with the identityMT =N−1
and the second identity in(53) and (60) then yields the second identity in(62). This implies for alln∈IN
∑
m,α dim(m)
n
n
m
F
F
G
H
ν
α
α
= ∑
m,α dim(m)
n
n
m
G
H
F
F
ν
α
α
(62)
=
nG
H
Fν
(64)
In particular, identities(60), (62) and (64) hold for endofunctorsF =c▷− :M→M orF =−◁d :M→M
for a (C,D)-bimodule categoryM. In this case, we use thin black or grey lines labeledc or d instead of
25
dashed lines, and the upward arrows denote the duals inC andD. Identities (60), together with(5), (22)
and (55), then imply for all simple objectsn∈IM
∑
i,m,α dim(i) dim(m)
n
n
mi
α
α
= dim(C)
n
n (65)
