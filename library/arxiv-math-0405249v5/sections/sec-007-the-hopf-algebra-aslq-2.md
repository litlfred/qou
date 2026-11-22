---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL (2)"
section_id: sec-007-the-hopf-algebra-aslq-2
section_title: "the hopf algebra A(SLq (2))"
section_number: null
pages: 8-9
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
toc_source: outline
doc_brief: "Twisted homology of quantum SL (2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra of the quan- tum SL(2) group"
---
Let k be a ﬁeld of characteristic zero, and q ∈k some nonzero parameter,
which we assume is not a root of unity.
The coordinate algebra A =
A(SLq(2)) of the quantum group SLq(2) over k is the k-algebra generated
by symbols a, b, c, d with relations
ab = qba,
ac = qca,
bd = qdb,
cd = qdc,
bc = cb
ad −qbc = 1,
da −q−1bc = 1
(21)
There is a unique Hopf algebra structure on A such that
∆(a) = a ⊗a + b ⊗c,
∆(b) = a ⊗b + b ⊗d,
∆(c) = c ⊗a + d ⊗c,
∆(d) = c ⊗b + d ⊗d,
ε(a) = ε(d) = 1,
ε(b) = ε(c) = 0,
S(a) = d,
S(b) = −q−1b,
S(c) = −qc,
S(d) = a.
(22)
A vector space basis of A is given by the monomials
ei,j,k := aibjck,
i ∈Z, j, k ∈N,
ai := d−i
for
i < 0,
(23)
(we use the convention that x0 = 1, for x ∈A, x̸ = 0). We have
ei,j,kel,m,n = q−l(j+k)ei+l,j+m,k+n +
X
r>0
λi,j,k,l,m,n(r)ei+l,j+m+r,k+n+r
for some constants λi,j,k,l,m,n(r). It follows that A admits a Z-grading
and three separating decreasing N-ﬁltrations
A =
M
i∈Z
Aa
i ,
A = Ax
0 ⊃Ax
1 ⊃. . . ,
x = b, c, bc,
(24)
8
where Aa
i = span{ei,j,k}j,k and Ax
n is the span of ei,j,k with j, k, j +k ≥n
for x = b, c, bc, respectively. For x ∈A, let xi be its component in Aa
i . Set
Ax
i,n := Ax
n ∩Aa
i . Then Ax
i,nAx
j,m = Ax
i+j,n+m. Deﬁne a Hermitian inner
product on A by requiring that ei,j,k are orthonormal and let πx, πi,j,k,
denote the orthogonal projections onto (Ax
1)⊥, ei,j,k. We freely consider
πi,j,k as a map A →k. Note that πx(y)i = πx(yi) for all y ∈A.
Finally, A has a Z2-grading given by
deg(ei,j,k) = (i, j −k)
(25)
This grading extends to A⊗(n+1) and is preserved by the Hochschild
boundary and the maps Bn (14). Hence HHσ
∗(A) and HCσ
∗(A) are nat-
urally Z2-graded.
