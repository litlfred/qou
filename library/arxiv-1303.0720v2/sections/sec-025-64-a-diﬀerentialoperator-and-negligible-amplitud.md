---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-025-64-a-diﬀerentialoperator-and-negligible-amplitud
section_title: "A diﬀerentialoperator and negligible amplitudes. The corrective algorithm involves the"
section_number: 6.4
pages: 16-16
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
diﬀerential operator
(6.4.1)
∇:=
1
¯∂wθ
¯∂w + 2mMz−w
and a (formal) diﬀusion operator S which will be described in detail later on. In (6.4.1) and
more generally in the sequel, M with a subscript stands for the operator of multiplication by
the function in the subscript. The diﬀerential operator ∇has the property that for smooth
functions A on D(z0, r) × D(z0, r),
(6.4.2)
1
¯∂wθ
¯∂w
n
A(z, w) e2m(z−w)θ(z,w)o
= e2m(z−w)θ(z,w)∇A(z, w),
which we may express in the more abstract (intertwining) form
(6.4.3)
M ¯∂wθ∇= Me−2m(z−w)θ ¯∂wMe2m(z−w)θ.
It follows from (6.4.2) that if u is a holomorphic function on D(z0, r), then
(6.4.4)
Z
Ω
u(w)χ0(w)[ ¯∂wθ(z, w)][∇A(z, w)] e2m(z−w)θ(z,w)dA(w)
=
Z
Ω
u(w)χ0(w) ¯∂w
n
A(z, w) e2m(z−w)θ(z,w)o
dA(w) =
Z
Ω
u(w)A(z, w) e2m(z−w)θ(z,w) ¯∂χ0(w)dA(w)
which we may estimate using (6.2.1):
(6.4.5)

Z
Ω
u(w)χ0(w)[ ¯∂wθ(z, w)][∇A(z, w)] e2m(z−w)θ(z,w)dA(w)

≤emQ(z)−δ0m
Z
Ω
|u(w)A(z, w)| e−mQ(w)| ¯∂χ0(w)|dA(w)
≤emQ(z)−δ0m∥A∥L∞(D(z0, 3
4 r)2)∥u∥m∥¯∂χ0∥L2(Ω) = O

emQ(z)−δ0m∥A∥L∞(D(z0, 3
4 r)2)∥u∥m

,
z ∈D(z0, 1
3r),
where the implied constant is absolute. Here, δ0 =
1
18r2ǫ0 as before, and the norm of A is the
supremum norm on the bidisk D(z0, 3
4r)2 = D(z0, 3
4r) × D(z0, 3
4r). Compared with the typical
size O(emQ(z)), this means that we have exponential decay in m. For this reason functions of the
form M ¯∂wθ∇A are called negligible amplitudes.
