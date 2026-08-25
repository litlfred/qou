---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-075-acknowledgments
section_title: "Acknowledgments"
section_number: null
pages: 67-69
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
We would like to thank J. E. Andersen, M. Aganagic, F. Benini, C. Cordova, A. Gadde,
E. Gorsky, K. Hori, H. Kim, S. Nawata, M. Romo, S. Shakirov, L. Rozansky and K. Ye for
useful comments and discussions. The work of S.G. and D.P. is supported in part by the
U.S. Department of Energy, Oﬃce of Science, Oﬃce of High Energy Physics, under Award
Number DE-SC0011632. In addition, the work of D.P. is supported by the center of excellence
grant “Center for Quantum Geometry of Moduli Space” from the Danish National Research
Foundation (DNRF95). P.P. gratefully acknowledges the support from Marvin L. Goldberger
Fellowship and the DOE Grant DE-SC0009988. The research of C.V. is supported in part
by NSF grant PHY-1067976. This work was performed in part (by P.P.) at Aspen Center
for Physics which is supported by National Science Foundation grant PHY-1066293. The
authors would like to thank Simons Center for Geometry and Physics and the organisers of
the Simons Summer Workshop 2016, where the work on the project has begun, for generous
hospitality.
– 66 –
A. Z[[q]]-valued invariant for negative deﬁnite plumbed 3-manifolds
We are interested in obtaining a certain analytic continuation ofsu(2)k WRT invariant [86,87]
of a plumbed 3-manidfoldM3(Γ),54 where Γ is a tree. Let us ﬁrst consider the case of positive
integer level, with k∈ Z+. The colored Jones polynomial of link L(Γ) is explicitly known
(see e.g. [87])55:
J[L(Γ)]n1,...,nL = 2i
q 1/2− q −1/2
∏
v∈ Vertices∼={1,...,L}
q
av(n2v−1)
4
( 2i
q nv/2− q −nv/2
)deg(v)−1
×
∏
(v1,v2)∈ Edges
q nv1nv2/2− q −nv1nv2/2
2i (A.2)
where q =e2πi/k.56 For the purposes of computing the WRT invariant of 3-manifold obtained
by Dehn surgery on a link L(Γ), it is useful to consider the following quantity:
F [L(Γ)]≡
∑
n∈{1,...,k−1}L
J[L(Γ)]n1,...,nL
L∏
v=1
q nv/2− q −nv/2
q 1/2− q −1/2 . (A.3)
Then the WRT invariant of M3(Γ) is given by [86] 57
τ[M3(Γ)] = F [L(Γ)]
F [L(+1•)]b+F [L(−1•)]b−
(A.5)
whereb± are the number of positive/negative eigenvalues of the linking matrix M while±1•
denotes a plumbing graph with one vertex corresponding to an unknot with±1 framing. The
SU (2)k CS partition function, in the usual physical normalization, with
ZSU (2)k[S2×S1] = 1, (A.6)
diﬀers from (A.5) by a simple factor:
ZSU (2)k[M3(Γ)] =
√
2
k sinπ
k · τ[M3(Γ)]. (A.7)
54Everything below in principle can be generalized to su(N) and u(N).
55We use the normalization in which the colored Jones polynomial of unlink with L components with
canonical framing is given by
J[Unlink]n1,...,nL =
L∏
v=1
q nv/2− q −nv/2
q 1/2− q −1/2 . (A.1)
56In this appendix, we use q to denote a k-th (k∈ Z+) root of unity e
2πi
k and reserve q to denote the
corresponding continuous variable which will appear in analytic continuation.
57Normalized such that
τ[S3] = 1. (A.4)
– 67 –
The following Gauss sum reciprocity formula will be very useful for us (see e.g. [88,89]):
∑
n∈ ZL/2kZL
exp
(πi
2k (n,Mn ) +πi
k (𝓁,n )
)
=
e
πiσ
