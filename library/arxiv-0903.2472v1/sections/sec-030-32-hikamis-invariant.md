---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-030-32-hikamis-invariant
section_title: "Hikami’s invariant"
section_number: 3.2
pages: 32-33
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
We can now describe Hikami’s geometric construction. Rough ly speaking, to compute the
invariant for a hyperbolic manifold M , one chooses an ideal triangulation of M , assigns an
inﬁnite-dimensional vector space V or V ∗ to each tetrahedron face, and assigns a matrix
element in V⊗V⊗V ∗⊗V ∗ to each tetrahedron. These matrix elements depend on a small
parameter ℏ, and in the classical ℏ→ 0 limit they capture the hyperbolic structure of the
tetrahedra. The invariant of M is obtained by taking inner products of matrix elements
on every pair of identiﬁed faces (gluing the tetrahedra back together), subject to the cusp
conditions described above in the classical limit.
To describe the process in greater detail, we begin with an or ientable hyperbolic man-
ifold that has an oriented ideal triangulation {∆ i}N
i=1, and initially forget about the hyper-
bolic structures of these tetrahedra. As discussed in Secti on 3.1 and indicated in Figure 4,
each tetrahedron comes with one of two possible orientation s of its edges, which induces
an ordering of its vertices v(i)
j (the subscript j here is not to be confused with the shape
parameter subscript in (3.2)), an ordering of its faces, and orientations on each face. The
latter can be indicated by inward or outward-pointing norma l vectors. The faces (or their
normal vectors) are labelled by p(i)
j , in correspondence with opposing vertices. The normal
face-vectors of adjacent tetrahedra match up head-to-tail (and actually deﬁne an oriented
dual decomposition) when tetrahedra are glued to form M .
/X76 /X31
/X76 /X33
/X76 /X32
/X76 /X34
/X70 /X33
/X70 /X34
/X70 /X32
/X70 /X31
/X76 /X31
/X76 /X32
/X76 /X33
/X76 /X34
/X70 /X32
/X70 /X34
/X70 /X33
/X70 /X31
/X7A/X20/X3D/X20/X65 /X70/X34/X2D/X70/X33 /X7A/X20/X3D/X20/X65 /X70/X34/X2D/X70/X33 
ε/X20/X3D/X20/X2B /X31 ε/X20/X3D/X20/X2D /X31
Figure 4: Oriented tetrahedra, to which matrix elements ⟨p1,p 3|S|p2,p 4⟩ (left) and
⟨p2,p 4|S−1|p1,p 3⟩ (right) are assigned.
Given such an oriented triangulation, one associates a vect or space V to each inward-
oriented face, and the dual space V ∗ to each outward-oriented face. (Physicists should think
14The branch of Li 2 in (3.11) is taken to be the standard one, with a cut from 1 to + ∞. Note, however,
that we could also take care of ambiguities arising from the c hoice of dilogarithm branch by rewriting (3.11)
in terms of the function ˜L(w) =
R w
−∞
t dt
1−e−t . This is a well-deﬁned holomorphic function : C → C/ 4π 2Z
because all the residues of t/ (1 − et) are integer multiplies of 2 πi , and it coincides with a branch of the
function Li 2(ew) + w log(1 − ew).
– 31 –
of these spaces as “Hilbert” spaces obtained by quantizing t he theory on a manifold with
boundary.) The elements of V are represented by complex-valued functions in one variabl e,
with adjoints given by conjugation and inner products given by integration. Abusing the
notation, but following the very natural set of conventions of [26, 27], we denote these
complex variables by p(i)
j , which we used earlier to label the corresponding faces of th e
tetrahedra. As a result, to the boundary of every tetrahedro n ∆ i one associates a vector
space V ⊗V ⊗V ∗⊗V ∗, represented by functions of its four face labels, p(i)
1 , p(i)
2 , p(i)
3 ,
and p(i)
4 .
To each tetrahedron one assigns a matrix element ⟨p1,p 3|S|p2,p 4⟩ or⟨p2,p 4|S−1|p1,p 3⟩,
depending on orientation as indicated in Figure 4. Here, the matrix S acts on functions
f (p1,p 2)∈V⊗V as
S = eˆq1 ˆp2/2ℏ Φ ℏ(ˆp1 + ˆq2− ˆp2), (3.12)
where ˆpif = pif and ˆqif = 2 ℏ ∂
∂pi
