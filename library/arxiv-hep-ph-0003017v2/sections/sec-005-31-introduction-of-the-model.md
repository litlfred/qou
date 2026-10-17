---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-005-31-introduction-of-the-model
section_title: "Introduction of the Model"
section_number: 3.1
pages: 15-16
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.703
latex_coverage_ratio: 0.98
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
In this section we introduce a chiral random matrix theory (chRMT) with the global symmetries of the QCD Dirac operator. In the spirit of the invariant random matrix ensembles, we construct a model with eigenfunctions distributed uniformly over the unitary unit sphere. This is achieved by choosing Gaussian-distributed random matrix elements. We thus arrive at the following chRMT [@Shur93; @Verb94a]: $$Z_{N_f,\nu}^\beta(m_1,\ldots, m_{N_f}) = 
  \int DW \prod_{f= 1}^{N_f} \det({\cal D} +m_f)
  e^{-\frac{N \beta}4 \Tr v(W^\dagger W)}\:,
\label{zrandom1}$$ where $\beta$ is the Dyson index, $${\cal D} = \left (\begin{array}{cc} 0 & iW\\
      iW^\dagger & 0 \end{array} \right )\:,$$ and $W$ is an $n\times m$ matrix with $\nu = m-n$ and $N= n+m$. The interpretation of this model is that $N$ low-lying modes interact via a random interaction. A natural representation of this model is in the form of gauge field configurations given by a liquid of instantons. Then the low-lying modes are the zero modes of each instanton. We assume that $\nu$ does not exceed $\sqrt N$ so that, to a good approximation, $n = N/2$ for large $N$. The parameter $N$ is identified as the dimensionless volume of spacetime. For the formulation of this model with explicit factors of $N/V$ included, see Ref. [@smilran]. The potential $v$ is defined by $$v(\phi) = \sum_{k\ge 1} a_k \phi^k\:.$$ The simplest case is the Gaussian case, where $v(\phi) = \Sigma^2\phi$. It can be shown (see Sec. [\[UniversalityProofs\]](#UniversalityProofs){reference-type="ref" reference="UniversalityProofs"}) that the microscopic spectral density does not depend on the higher-order terms in this potential provided that the average spectral density near zero remains nonzero. The matrix elements of $W$ are either real \[$\beta =
1$, chiral Gaussian Orthogonal Ensemble (chGOE)\], complex \[$\beta =
2$, chiral Gaussian Unitary Ensemble (chGUE)\], or quaternion real \[$\beta = 4$, chiral Gaussian Symplectic Ensemble (chGSE)\]. In the latter case, the eigenvalues of ${\cal D}$ are doubly degenerate, and the use of Majorana fermions is implemented by replacing the determinant by its square root. For a non-Gaussian potential $v(\phi)$, we will omit the G in the abbreviations and use chOE, chUE, and chSE, respectively. Two earlier attempts to describe QCD Dirac eigenvalues used the Wigner-Dyson ensembles instead of the above chiral ensembles [@early].

This model reproduces the following symmetries of the QCD partition function:

-   The $\rm U_A(1)$ symmetry. All eigenvalues of the random matrix Dirac operator occur in pairs $\pm i\lambda_n$ or are zero.

-   The topological structure of the QCD partition function. The Dirac matrix has exactly $|\nu|=|n-m|$ zero eigenvalues. This identifies $\nu$ as the topological sector of the model.

-   The flavor symmetry, which is the same as in QCD. For $\beta = 2$ it is ${\rm SU}(N_f) \times {\rm SU}(N_f)$, for $\beta = 1$ it is ${\rm
        SU}(2N_f)$, and for $\beta = 4$ it is ${\rm SU}(N_f)$ (each Majorana flavor counts as 1/2 Dirac flavor).

-   The chiral symmetry, which is broken spontaneously with a chiral condensate given by $$\Sigma = \lim_{N\rightarrow \infty} {\pi \rho(0)}/N\:.$$ ($N$ is interpreted as the dimensionless volume of spacetime.) The symmetry-breaking pattern is [@SmV] ${\rm SU}(N_f) \times {\rm
        SU}(N_f)\to{\rm SU}(N_f)$, ${\rm SU}(2N_f)\to{\rm Sp}(2N_f)$, and ${\rm SU}(N_f)\to{\rm O}(N_f)$ for $\beta = 2$, 1, and 4, respectively --- the same as in QCD [@peskin].

-   The anti-unitary symmetries. These are implemented by choosing the matrix elements of $W$ to be real, complex, or quaternion real for $\beta =1$, $\beta =2$, and $\beta =4$, respectively.

Along with the invariant random matrix ensembles, the chiral ensembles are part of a larger classification scheme that also includes ensembles for the description of disordered superconductors [@Altland]. In total, 10 different families of random matrix ensembles have been identified. They correspond one-to-one with the Cartan classification of symmetric spaces [@class].

The uniform distribution of the eigenfunctions over the unitary unit sphere is expressed as the invariance $$W \rightarrow U^\dagger W V\:,
\label{inv}$$ where the $n\times n$ matrix $U$ and the $m\times m$ matrix $V$ are orthogonal matrices for $\beta=1$, unitary matrices for $\beta = 2$, and symplectic matrices for $\beta = 4$. This invariance makes it possible to express the partition function in terms of eigenvalues of $W$ defined by $$W = U^\dagger \Lambda V\:.$$ Here, $\Lambda$ is a diagonal matrix with real diagonal matrix elements $\lambda_k \ge 0$. In terms of the eigenvalues, the partition function ([\[zrandom1\]](#zrandom1){reference-type="ref" reference="zrandom1"}) is given by $$Z_{N_f, \nu}^{\beta}(m_1, \ldots, m_{N_f}) = 
  \int d\lambda |\Delta(\lambda^2)|^\beta
  \prod_k \lambda_k^{\beta|\nu|+\beta-1} 
  e^{-\frac{N\beta}4 v(\lambda_k^2)}
  \prod_f m_f^{|\nu|}(\lambda_k^2 + m^2_f)\:,
  \label{zeig}$$ where the Vandermonde determinant is defined by $$\Delta(\lambda^2) = \prod_{k<l} (\lambda_k^2-\lambda_l^2)\:.
  \label{vandermonde}$$ In Eq. ([\[zeig\]](#zeig){reference-type="ref" reference="zeig"}) and elsewhere in this review, we have omitted the normalization constant of the partition function. From the joint eigenvalue distribution (which is the integrand of Eq. ([\[zeig\]](#zeig){reference-type="ref" reference="zeig"})), we see that a nonzero topological charge $\nu$ can be introduced by adding $\beta|\nu|/2$ massless flavors to the theory with $\nu=0$. Therefore, this duality between flavor and topology is a general feature of all correlation functions. For a discussion of this duality in terms of finite volume partition functions, see Refs. [@cam97; @wadati].
