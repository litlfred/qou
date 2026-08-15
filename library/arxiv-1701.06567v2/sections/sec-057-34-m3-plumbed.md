---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-057-34-m3-plumbed
section_title: "M3 = plumbed"
section_number: 3.4
pages: 51-52
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
Now we move to consider another very large class of 3-manifolds M3(Γ) associated to a
plumbing graph Γ. There are various ways to deﬁne M3 for a given Γ. One of them is
to say that M3 is obtained by a Dehn surgery on the corresponding link L(Γ) of unknots
(see Figure 5). For simplicity, we also assume that Γ is connected. Such class of 3-manifolds
contains Seifert ﬁbrations overS2, which correspond to star-shaped plumbing graphs. Denote
byL the number of vertices of Γ. It is equal to the number of components of the link L(Γ).
We will also need L×L linking matrix ofL(Γ) which will be denoted by M:
Mv1,v2 =



1, v 1,v 2 connected,
av, v1 =v2 =v,
0, otherwise.
vi∈ Vertices of Γ ∼= {1,...,L }. (3.142)
a1
a2
a5 a6
a3
a4
a7
a8
a9
a1
a2
a3
a4
a5 a6
a8
a7
a9
Figure 5: An example of a plumbing graph Γ (left) and the corresponding linkL(Γ) of framed unknots
in S3 (right). The associated 3-manifold M3(Γ) can be constructed by performing a Dehn surgery on
L(Γ).
The ﬁrst homology group ofM3(Γ) is given by the cokernel (overZ) of the linking matrix:
H1(M3, Z)∼= CokerM = ZL/MZL. (3.143)
– 50 –
In what follows we assume for simplicity thatM3(Γ) is a rational homology sphere (b1(M3) =
0), which implies that Γ has no loops ( i.e. it is a tree). The linking form on H1(M3, Z) is
then given by
𝓁k(a,b ) = (a,M−1b) mod Z, a,b ∈ ZL/MZL. (3.144)
Diﬀerent plumbing graphs can give homeomorphic 3-manifolds — M3(Γ)∼=M3(Γ′) iﬀ Γ and
Γ′ can be connected by a sequence of 3d Kirby moves, as shown in Figure 642.
a1+a2
a2a1 0
'
a2§1a1§1 §1
'
a1 a2
a1§1 §1
'
a1
Figure 6: 3d Kirby moves that relate plumbing graphs which result in homeomorphic 3-manifolds.
The theoryT [M3,SU (2)] can in principle be obtained by combining together the following
3d theories (see e.g. [66]):
• edge: S-duality wall inN = 4 SU (2) super-Yang-Mills (i.e. theory T [SU (2)]),
• 2-valent vertex: Ta-duality wall = “supesymmetric Chern-Simons term at level a,”
• n-valent vertex: T [(sphere with n holes)×S1] = n copies of T [SU (2)] gauged together.
