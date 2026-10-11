---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-044-krylov-space-methods
section_title: "Krylov space methods"
section_number: null
pages: 63-63
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
As we have already pointed out, very often what is really required, rather than the exponential of the matrix C itself,
is the computation of exp(C) applied to a vector. In this situation, evaluating eC is somehow analogous to computing C−1
to get the solution of the linear system of equations Cx = b for many different b’s: other procedures are clearly far more
desirable. The computation of eCv can be efficiently done with Krylov subspace methods, in which approximations to the
solution are obtained from the Krylov spaces spanned by the vectors {v, Cv, C2v, . . . , Cjv} for some j that is typically small
compared to the dimension of C [148,149]. The Lanczos method for solving iteratively symmetric eigenvalue problems is of
this form [150]. If, as before, we let C = −iτH, the symmetric Lanczos process recursively generates an orthonormal basis
Vm = [v1 · · · vm] of the mth Krylov subspace Km(H, u) = span(u, Hu, . . . , Hm−1u) such that
HVm = VmLm + [0 · · · 0 βm vm+1],
where the symmetric tridiagonal m × m matrix Lm = V T
mHVm is the orthogonal projection of H onto Km(H, u). Finally,
exp(−iτH)u ≈Vm exp(−iτLm)V T
mu
and the matrix exponential exp(−iτLm) can be computed by diagonalizing Lm, Lm = QmDmQ T
m, as
exp(−iτLm) = Qm exp(−iτDm)Q T
m,
with Dm a diagonal matrix. This iterative process is stopped when
βm

(exp(−iτLm))m,m

 < tol
for a fixed tolerance. Very good approximations are often obtained with relatively small values of m, and computable
error bounds exist for the approximation. This class of schemes generally require O(N2) floating point operations in the
computation of eCv. More details are contained in the references [151–153].
