---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-011-c-skew-orthogonal-polynomials
section_title: "C Skew-orthogonal polynomials"
section_number: null
pages: 22-23
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
toc_source: outline
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
Skew-orthogonal polynomials
In this appendix we compute the skew-orthogonal polynomials given in eqs. (4.6) for ν = 0. We
ﬁrst recall that the expectation value of a single characteristic polynomial (or equivalently the Nf =
1 partition function) gives the even polynomials R2j where we follow the argument of [38].
This
expectation value is computed using the supersymmetric method in the next subsection C.1. Based
on that the odd polynomials R2j+1 then follow as shown in C.2.
Starting from the quenched partition function eq. (3.17) for ν = 0
Z(0)
0
=
Z ∞
−∞
2n
Y
j=1
dsjw(sj) ∆2n({s}) Pf1≤i,j≤2n[F(si −sj)] ,
(C.1)
we can write the expectation value of a single determinant as follows:
⟨det[z −/D5]⟩2n
=
1
Z(0)
0
Z ∞
−∞
2n
Y
j=1
dsjw(sj)(z −sj) ∆2n({s}) Pf1≤i,j≤2n[F(si −sj)]
=
1
Z(0)
0
(2n)!
2nn!
Z ∞
−∞
N
Y
j=1
dsjw(sj) ∆2n+1({s}, z)
n
Y
l=1
F(s2l −s2l−1).
(C.2)
Here we have used the fact that both the Vandermonde determinant and the Pfaﬃan are antisym-
metric in order to simplify their product (times the symmetric integral over all eigenvalues), cf. [29]
Appendix 25. Furthermore we have included the determinant into a larger Vandermonde. Writing the
Vandermonde determinant in terms of even and odd monic polynomials Φ2i and Ψ2i+1 respectively,
∆2n+1({s}, z) =
det
i=0,...,n−1;j=1,...,2n+1
h
{Φ2i(sj), Ψ2i+1(sj)} Φ2n(sj)
i
,
(C.3)
and relabeling z = s2n+1, we have from the generalised de Bruijn formula (cf. [38] eq. (4.9), or [34])
⟨det[z −/D5]⟩2n =
n!
Z(0)
0
Pf0≤i,j≤2n


⟨ϕi, ϕj⟩
. . .
ϕ0(s2n+1)
. . .
· · ·
ϕ2n(s2n+1)
−ϕ0(s2n+1) . . .
−ϕ2n(s2n+1)
0

,
(C.4)
for the set of all monic polynomials ϕi = {Φ0, Ψ1, Φ2, Ψ3, · · · , Φ2n}, with the scalar product deﬁned
in eq. (4.9). Choosing polynomials ϕj = Rj to satisfy the skew-orthogonality eq. (4.8) we obtained
the desired relation
R2n(z) = ⟨det[z −/D5]⟩2n = ⟨det[z + /D5]⟩2n ,
(C.5)
which obviously has parity.
