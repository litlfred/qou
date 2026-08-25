---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-050-331-homological-blocks-and-wrt-invariant
section_title: "Homological blocks and WRT invariant"
section_number: 3.3.1
pages: 47-48
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
Consider the partition function ofT [M3] onD2×S1 with the following 2dN = (0, 2) boundary
conditions (which generalize the boundary conditions for T [L(p, 1)] that produce ˆZa(q,t )):
• Neumann forN = 2 vector multiplet,
• Neumann for adjoint chiral Σ,
• Dirichlet for g adjoint chirals Φi,
• Neumann for g adjoint chirals ~Φi,
• 3d vector multiplet is coupled to modules ofZ2-orbifolded√2pZ lattice VOA by gauging
its ﬂavor symmetry. Note that when p = 0 the boundary conditions preserve 2d N =
(2, 2) supersymmetry. This cancels gauge anomaly inﬂow due to the level- p CS term.
The D2×qS1 partition then reads [30]
ˆZa(q,t,u )≡ZT [M3](D2
a×qS1) = 1
|Wa|
∫
γ
dz
2πiz
(z±2;q)∞(q;q)∞
(z±2tq;q)∞(tq;q)∞
×
g∏
i=1
(z±2tuiq;q)∞(tuiq;q)∞
(z±2ui;q)∞(ui;q)∞
×
∑
n∈pZ+aqn2/pz2n
(q;q)∞
. (3.122)
The choice of the contour γ, which corresponds to a precise choice of the boundary condition
for the vector multiplet (or, equivalently, Lagrangian submanifold in the complexiﬁed maximal
torus of SU (2)), will be discussed below.
The WRT invariant ofM3 can be computed as follows in terms of S and T matrices40:
ZCS
SU (2)k[M3] =
k−1∑
n=1
(S1n)2−2g(Tnn)−p =
∑′
n∈Z2k
(qn/2−q−n/2)2−2gq−pn2
4 (3.123)
where we use notation such that matrix indices are “colors” (= dimensions of representations),
q = e
2πi
k and a prime over the sum means that we skip singular terms. After applying the
Gauss reciprocity formula
∑
m∈Z2k
q−pm2
4 ·q
n𝓁
2 = e−πi
4 (2k)1/2
|p|1/2
∑
a∈Zp
e2πika2
p ·e2πia𝓁
p ·q
𝓁2
4p, (3.124)
40We omit simple overall factors below.
– 46 –
we arrive at
ZCS
SU (2)k[M3] =
∑
a,b∈Zp/Z2
e2πikCS(a)·Sab· 1
|Wb|
ˆZb(q)
⏐⏐⏐
q→e
2πi
k
(3.125)
where the S-matrix is given in ( 3.115) and, formally,
ˆZa(q) = L(p)
a
[
(z−z−1)2−2g]
(3.126)
with Laplace transform given in ( 3.116). To be precise, it can be computed using
ˆZa(q) = 1
|Wa|· v.p.
∫
|z|=1
(z−z−1)2−2g ∑
n∈pZ+a
qn2/pz2n (3.127)
as a series in q, convergent in the unit disk |q|< 1. One can see that ( 3.127) coincides with
the unreﬁned partition function of T [M3] on D2×S1, cf. (3.122), with removed contribution
of Cartan components of the adjoint chiral:
ˆZa(q) = ˆZa(q,t,u ) (qt;q)∞
g∏
i=1
(ui;q)∞
(tuiq;q)∞
⏐⏐⏐⏐⏐
t=1,ui=1
. (3.128)
The principal value contour prescription in ( 3.127) suggests that the contour γ in ( 3.122)
should be chosen as shown in Figure 4. Note, that the labels a of homological blocks now
correspond to the connected components of the space of abelian ﬂat connections.
