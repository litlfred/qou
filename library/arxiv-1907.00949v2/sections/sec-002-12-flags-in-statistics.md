---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-002-12-flags-in-statistics
section_title: "Flags in statistics"
section_number: 1.2
pages: 3-4
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
analysis techniques [26] may be cast as nested subspace-searching problems, i.e., constrained or
unconstrained optimization problems on the ﬂag manifold.
We let 1 denote a vector of all ones (of appropriate dimension). We assume that our data set is
given in the form of a sample-by-variables design matrix X∈ Rn×p, n≥ p, which we call a data
matrix for short. Let x = 1
nX T1 ∈ Rp be its sample mean and SX = (X− 1 xT)T(X− 1 xT)∈ Rp×p
be its sample covariance. For another data matrix Y ∈ Rn×q, SXY = (X− 1 xT)T(Y − 1 yT) =
S T
YX ∈ Rp×q denotes sample cross-covariance.
Example 1.5 (Principal Component Analysis (PCA)). Thekth principal subspace ofX is im(Zk),
where Zk is the p×k orthonormal matrix given by
Zk = argmax{tr(Z TSXZ) :Z∈ V(k,p )}, k = 1,...,p. (1)
So im(Zk) is a k-dimensional linear subspace of Rp spanned by the orthonormal columns of Zk.
In an appropriate sense, the kth principal subspace captures the greatest variability in the data
among allk-dimensional subspaces of Rp. In principal component analysis (PCA), the data points,
i.e., columns of X, are often projected onto im( Zk) with k = 2, 3 for visualization or with other
small values of k for dimension reduction. Clearly im( Zk) is contained in im(Zk+1) and the ﬂag
im(Z1)⊆ im(Z2)⊆···⊆ im(Zp)
explains an increasing amount of variance in the data.
In [32, Theorem 9], it is shown how one may directly deﬁne PCA as an optimization problem
on a ﬂag manifold, a powerful perspective that in turn allows one to generalize and extend PCA
in various manners. Nevertheless what is lacking in [32] is an algorithm for optimization on ﬂag
manifolds, a gap that our article will ﬁll.
Example 1.6 (Canonical Correlation Analysis (CCA)) . The kth pair of canonical correlation
loadings (ak,bk)∈ Rp× Rq is deﬁned recursively by
(ak,bk) = argmax{aTSXYb :aTSXa =bTSYb = 1,
aTSXaj =aTSXYbj =bTSYXaj =bTSYbj = 0, j= 1,...,k − 1}. (2)
Let Ak = [a1,...,a k] ∈ Rp×k and Bk = [b1,...,b k] ∈ Rq×k. Then the canonical correlation
subspaces of X and Y are given by
im(A1)⊆···⊆ im(Ap) and im( B1)⊆···⊆ im(Bq),
which are ﬂags in Rp and Rq respectively. Collectively they capture how the shared variance
between the two data sets increases with k.
Example 1.7 (Correspondence Analysis (CA)) . Let t = 1 TX1 ∈ R, r = 1
tX1 ∈ Rn, c = 1
tX T1 ∈
Rp denote the total, row, and column weights of X respectively and set Dr = 1
t diag(r)∈ Rn×n,
Dc = 1
t diag(c)∈ Rp×p. For k = 1,...,p , we seek matrices Uk∈ Rk×n and Vk∈ Rk×p such that
(Uk,Vk) = argmax{tr
(
U T( 1
tX−rcT)V
)
:U TDrU =I =V TDcV}. (3)
The solution
im(U1)⊆···⊆ im(Up) and im( V1)⊆···⊆ im(Vp)
are ﬂags in Rn and Rp respectively and collectively they explain the increasing deviation from the
independence of occurrence of two outcomes.
For reasons such as sensitivity of the higher-dimensional subspaces to noise in the data, in
practice one relies on the ﬁrst few subspaces in these ﬂags to make various inference about the
data. Nevertheless, we stress that the respective ﬂags that solve (1), (2), (3) over all k will paint
4 K. YE, K. S.-W. WONG, AND L.-H. LIM
a complete picture showing the full proﬁle of how variance, shared variance, or deviation from
independence vary across dimensions.
Apart from PCA, CCA, and CA, ﬂags arise in other multivariate data analytic techniques [26],
e.g., factor analysis (FA), linear discriminant analysis (LDA), multidimensional scaling (MDS), etc,
in much the same manner. One notable example is the independent subspace analysis proposed in
[29, 30], a generalization of independent component analysis.
