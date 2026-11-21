---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-054-krylov-space-methods
section_title: "Krylov space methods"
section_number: null
pages: 63-63
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
As we have already pointed out, very often what is really required, rather than the exponential of the matrix C itself,
is the computation of exp(C) applied to a vector. In this situation, evaluating e° is somehow analogous to computing C~!
to get the solution of the linear system of equations Cx = b for many different b’s: other procedures are clearly far more
desirable. The computation of e“v can be efficiently done with Krylov subspace methods, in which approximations to the
solution are obtained from the Krylov spaces spanned by the vectors {v, Cv, C?v, ..., Civ} for some j that is typically small
compared to the dimension of C [148,149]. The Lanczos method for solving iteratively symmetric eigenvalue problems is of
this form [150]. If, as before, we let C = —itH, the symmetric Lanczos process recursively generates an orthonormal basis

‘im = [V1 +++ Um] of the mth Krylov subspace K,,(H, u) = span(u, Hu, ..., H™~'u) such that

HVm = Vinkm + [0-+-0 Bm Um41],

where the symmetric tridiagonal m x m matrix Ly» = VIAVin is the orthogonal projection of H onto K,,(H, u). Finally,
exp(—itH)u © Vin exp(—itLm)VnU

and the matrix exponential exp(—itL) can be computed by diagonalizing Ly, Lm = QnDnQ, as

exp(—itLm) = Qn exp(—itDm)Qn.
with D,, a diagonal matrix. This iterative process is stopped when

Bm ||(eXP(-itLm))mml]_ < tol

for a fixed tolerance. Very good approximations are often obtained with relatively small values of m, and computable
error bounds exist for the approximation. This class of schemes generally require @(N) floating point operations in the
computation of e“v. More details are contained in the references [151-153].
