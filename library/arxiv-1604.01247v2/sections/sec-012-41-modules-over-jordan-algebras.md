---
doc_id: arxiv-1604.01247v2
doc_title: "Exceptional quantum geometry and particle physics"
section_id: sec-012-41-modules-over-jordan-algebras
section_title: "Modules over Jordan algebras"
section_number: 4.1
pages: 18-20
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
toc_source: outline
doc_brief: "Exceptional quantum geometry and particle physics — Based on an interpretation of the quark-lepton symmetry in terms of the unimodularity of the color group SU(3) and on the existence of 3"
---
Modules over Jordan algebras
There are general deﬁnitions of bimodules for classes of algebras [38], [27]
or for categories of algebras [14]. For Jordan algebras this reduces to the
following (see also in [31]). Let J be a Jordan algebra and let M be a vector
space equipped with left and right actions of J
J ⊗M →M,
x ⊗Φ 7→xΦ ∈M
M ⊗J →M,
Φ ⊗x 7→Φx ∈M
for x ∈J, Φ ∈M. Deﬁne a bilinear product on J ⊕M by setting
(x + Φ)(x′ + Φ′) = xx′ + (xΦ′ + Φx′).
Then M is said to be a Jordan bimodule over J if J ⊕M endowed with
the above product is a Jordan algebra. This is equivalent to the following
conditions (i), (ii) and (iii) :



(i) xΦ = Φx
(ii) x(x2Φ) = x2(xΦ)
(iii) (x2y)Φ −x2(yΦ) = 2((xy)(xΦ) −x(y(xΦ)))
for x, y ∈J and Φ ∈M. When J is unital with unit denoted by 1l, the
Jordan bimodule M will be said to be unital whenever it satisﬁes the further
18
condition (iiii)
(iiii)
1lΦ = Φ
for any Φ ∈M, which implies that J ⊕M is again a unital Jordan algebra
with unit 1l.
It follows from Condition (i) that one can restrict attention to the left
action (for instance), this is why Jordan bimodules are usually refered to as
Jordan modules.
Let us deﬁne the linear mapping x 7→Lx of J into the algebra L(M) of
linear endomorphisms of the J-module M by setting
LxΦ = xΦ
(4.1)
for x ∈J and Φ ∈M. Then (ii) reads
[Lx, Lx2] = 0
(4.2)
for x ∈J, while (iii) reads
Lx2y −Lx2Ly −2LxyLx + 2LxLyLx = 0
for x, y ∈J which is equivalent to
Lx3 −3Lx2Lx + 2L3
x = 0
(4.3)
and
[[Lx, Ly], Lz] + L[x,z,y] = 0
(4.4)
for x, y, z ∈J where [x, z, y] = (xz)y −x(zy) is the associator.
Thus Conditions (ii) and (iii) can be replaced by Conditions (4.2), (4.3)
and (4.4) above while the unital condtion (iiii) reads
L1l = 1l
(4.5)
where on the right-hand side 1l denotes the unit of the algebra L(M).
Notice that if p ∈J is an idempotent, i.e. satisﬁes p2 = p, then (4.3)
reads
Lp −3L2
p + 2L3
p = 0
that is
Lp(Lp −1
2)(Lp −1) = 0
(4.6)
from which follows the associated Pierce decomposition of the module M.
19
4.2
J8
