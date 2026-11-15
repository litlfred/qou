---
doc_id: arxiv-hep-th-0306165v1
doc_title: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial"
section_id: sec-023-62-path-integral-interpretation
section_title: "Path Integral Interpretation"
section_number: 6.2
pages: 47-49
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
toc_source: inferred
doc_brief: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial — We study three-dimensional Chern-Simons theory with complex gauge group SL(2,C), which has many interesting connections"
---
6.2. Path Integral Interpretation
As we already pointed out earlier, the colored Jones polynomial can be viewed as the
expectation value of the Wilson loop observable (1.3) in the SU(2) Chern-Simons theory
[3],
JN(K, e
2πi
k0+2 ) = ⟨WRj(K)⟩=
1
ZSU(2)(S3)
Z
DA WRj(K) e
ik0
4π SCS(A)
(6.11)
46
where k0 is the tree-level value of the coupling constant, Rj is an irreducible N = (2j + 1)
dimensional representation of SU(2), and SCS(A) is the Chern-Simons functional of the
su(2)-values gauge connection A,
SCS = Tr
Z
S3(A ∧dA + 2
3A ∧A ∧A)
(6.12)
The Wilson loop expectation value (6.11) is normalized by the Chern-Simons path
integral on S3,
ZSU(2)(S3) =
r
2
k sin
π
k

(6.13)
where k = k0 + 2 is the renormalized value of the level.
In the semi-classical limit, k →∞, the path integral (6.11) can be represented as a
sum over ﬂat connections,
ZSU(2)(WRj, k) =
X
α
Z(α)
SU(2)(WRj, k)
(6.14)
where each term has the form of a perturbation series,
Z(α)
SU(2)(WRj, k) = exp ik
4π
 
S(α)
CS +
∞
X
n=1
(2π/k)nS(α)
n
!
(6.15)
Therefore, the leading contribution to the path integral (6.11) comes from the classical
value of the Chern-Simons functional (6.12) evaluated on the ﬂat connection A(α). Then,
the next, “1-loop” term, S(α)
1
, has the form, see e.g. [3,92,93],
exp
 i
2S(α)
1

=
p
T(A(α))
Vol(Hα)
4π2
k
(h0(A(α))−h1(A(α)))/2
exp

−iπ
4 Nph

(6.16)
where hk(A(α)) is the dimension of the k-th cohomology of M = S3 \ K with coeﬃcients
twisted by A(α), and T(A(α)) is the SU(2) Ray-Singer torsion of M twisted by A(α). The
isotropy group, Hα, is a subgroup of SU(2) that commutes with the holonomies of the
connection Aα. Its tangent space, THα, can be identiﬁed with the 0-th cohomology space
of M twisted by A(α). Therefore, we have
h0(A(α)) = dim(Hα)
(6.17)
On the other hand, the elements of the 1-st twisted cohomology can be identiﬁed with
inﬁnitesimal deformations of the ﬂat connection Aα. However, since these deformations
47
may be obstructed there is no simple formula for h1(A(α)), analogous to (6.17). Finally,
Nph is given by
Nph = 2SF (α) + h0(A(α)) + h1(A(α)) + (1 + b1) dim G
(6.18)
where SF (α) is a spectral ﬂow of the self-adjoint operator L = ∗D + D∗restricted to the
space of odd forms.
Now, following Rozansky [29], let us evaluate (6.16) in the case of a trivial connection.
