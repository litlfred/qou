---
doc_id: arxiv-2509.02354v2
doc_title: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms"
section_id: sec-024-a2-fusion-identities
section_title: "A.2. Fusion identities"
section_number: null
pages: 36-37
source_pdf: 2509.02354v2.pdf
source_sha256: 14680221e597fe61
toc_source: outline
doc_brief: "The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilogarithms — We derive an explicit formula for the holonomy R-matrix of quantum sl2 at a root of unity."
---
(A.21)
1 −ωNα
1 −ωNβ = ωNγ
and consider the sum
(A.22)
f

α
β

γ

:=
X
k
w(α|k)
w(β|k)ωkγ
It clearly depends only on the parameters α, β, γ ∈C modulo NZ. By [18, eq. A.14] we have
(A.23)
f

α + k
β + l

γ + m

= f

α
β

γ

w(α −β −1|k −l) w(β|l) w(−γ|−m)
ωl(γ+m)ωm(β+1)w(α|k) w(α −β −γ −1|k −l −m)
THE HOLONOMY BRAIDING FOR Uξ(sl2)
37
when γ̸ ∈Z. In the special case where γ is an integer, so α ≡β (mod Z) this becomes
(A.24)
f

α + k
α + l −1

m

= N 1 −ωα+l
1 −ωNα
ω{−m}N(α+l)
w(α + l|{k −l}N)
(ω; ω){k−l}N+{−m}N
(ω; ω){k−l}N (ω; ω){−m}N
as in [11, eq. 40]. Here {k}N is the unique integer with
0 ≤{k}N < N and {k}N ≡k
(mod N)
and (ω; ω)k is the q-Pochhammer symbol defined in equation (A.6). Another useful identity
comes from taking the limit of (A.22) as α →−∞and using [18, eq. C.7] to obtain
(A.25)
"N−1
X
k=0
ωkγ
w(β|k)
#N
=

ω(N−1)β
D(0)
D(−γ + 1) D(β + 1)
N
.
