---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: page-001
section_title: "Page 1"
section_number: null
pages: 1-1
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: undetermined
doc_brief: "arXiv:hep-th/9304063v2 29 Jan 1999 — 18 sections: Page 1; Page 2; Page 3"
---
arXiv:hep-th/9304063v2  29 Jan 1999
Level Spacing Distributions and the Bessel Kernel
Craig A. Tracy∗
Department of Mathematics and Institute of Theoretical Dynamics,
University of California, Davis, CA 95616, USA
Harold Widom†
Department of Mathematics,
University of California, Santa Cruz, CA 95064, USA
Scaling models of random N × N hermitian matrices and passing to the limit N →∞leads to
integral operators whose Fredholm determinants describe the statistics of the spacing of the eigenval-
ues of hermitian matrices of large order. For the Gaussian Unitary Ensemble, and for many others
as well, the kernel one obtains by scaling in the “bulk” of the spectrum is the “sine kernel” sin π(x−y)
π(x−y) .
Rescaling the GUE at the “edge” of the spectrum leads to the kernel Ai(x) Ai′(y) −Ai′(x) Ai(y)
x−y
where Ai
is the Airy function. In previous work we found several analogies between properties of this “Airy
kernel” and known properties of the sine kernel: a system of partial diﬀerential equations associated
with the logarithmic diﬀerential of the Fredholm determinant when the underlying domain is a union
of intervals; a representation of the Fredholm determinant in terms of a Painlev´e transcendent in
the case of a single interval; and, also in this case, asymptotic expansions for these determinants
and related quantities, achieved with the help of a diﬀerential operator which commutes with the
integral operator. In this paper we show that there are completely analogous properties for a class of
kernels which arise when one rescales the Laguerre or Jacobi ensembles at the edge of the spectrum,
namely
Jα(√x) √yJ′
α(√y) −√xJ′
α(√x) Jα(√y)
2(x −y)
where Jα(z) is the Bessel function of order α. In the cases α = ∓1
2 these become, after a variable
change, the kernels which arise when taking scaling limits in the bulk of the spectrum for the
Gaussian orthogonal and symplectic ensembles. In particular, an asymptotic expansion we derive
will generalize ones found by Dyson for the Fredholm determinants of these kernels.
I. INTRODUCTION AND STATEMENT OF RESULTS
A. Introduction
Scaling models of random N × N hermitian matrices and passing to the limit N →∞leads to integral operators
whose Fredholm determinants describe the statistics of the spacing of the eigenvalues of hermitian matrices of large
order [18,25]. Which integral operators (or, more precisely, which kernels of integral operators) result depends on the
matrix model one starts with and at which location in the spectrum the scaling takes place.
For the simplest model, the Gaussian Unitary Ensemble (GUE), and for many others as well (see, e.g., [16,17,23,24]),
the kernel one obtains by scaling in the “bulk” of the spectrum is the “sine kernel”
sin π(x −y)
π(x −y)
.
Precisely, this comes about as follows. If {φk(x)}∞
k=0 is the sequence obtained by orthonormalizing the sequence
{xk e−x2/2} over (−∞, ∞) and if
KN(x, y) =
N−1
X
k=0
φk(x) φk(y) ,
(1.1)
∗e-mail address: tracy@itd.ucdavis.edu
†e-mail address: widom@cats.ucsc.edu
1
