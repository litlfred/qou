---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-Body Systems in Lattice Effective Field Theory"
section_id: sec-020-exact-methods
section_title: "Exact methods"
section_number: null
pages: 36-37
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
toc_source: outline
doc_brief: "Few-Body Systems in Lattice Effective Field Theory — 62 sections: Front matter; Introduction and Motivation; The standard model of particle phy"
---
As long as we consider only systems with a few particles, we can use the Lanczos/ Arnoldi algorithm [95,
96] for sparse matrices to solve the eigenvalue problem. Afterward, we have the energy and the wave
function of the system and use this information for the calculation of binding energies and phase shifts.
The Lanczos algorithm works as the following.
A general eigenvalue problem reads
A · v = λ · v,
(3.38)
where A is a n × n matrix, λ is the eigenvalue and v is the eigenvector which can be rewritten in the basis
of the power-iterated subspace,
n
q, Aq, A2q, A3q, . . .
o
,
(3.39)
where q is an arbitrary starting vector. Hence, we could use a ﬁnite number of m vectors based
on Eq. (3.39) to orthogonally transform the matrix A into a Hessenberg matrix Hm, from which the
eigenvalues and -vectors are calculated faster than for a general matrix. Admittedly, the aforementioned
arguments of Eq. (3.39) do not have to be orthogonal. After orthogonalization, the basis is given by
p1, . . . , pm and applied to the general matrix A, we get the m × m Hessenberg matrix, where all entries
below the ﬁrst subdiagonal are equal to zero. It is of the form
Hm =

h1,1
h1,2
. . .
h1,m
h2,1
h22
. . .
h2,m
0
h3,2
. . .
h3,m
0
0
. . .
h4,m
. . .
. . .
hm,m

,
(3.40)
and it is an similarity transformation of the original matrix A in the ﬁrst m arguments. In the case of a
real symmetric matrix A, Eq. (3.40) reduces to a tridiagonal matrix which can be evaluated even faster.
As we work with ﬁnite m, the eigenvectors and -values are only an approximation of the exact solution,
making it necessary to iterate the procedure until the desired precision is reached. Generally, we only
have to perform a matrix-vector multiplication and we have to store the vectors p1, . . . , pm as well as
the matrix Hm. This is particularly eﬃcient for very sparse matrices, where most of the entries are zero
and as such do not contribute to the calculation. Using a large enough basis and enough iterations it is
also possible to calculate more than one eigenvalue which is particularly important for the calculation of
phase shifts where one needs eigenvalues corresponding to a large range of energy.
30
