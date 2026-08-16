---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-012-51-generic-q
section_title: "Generic q"
section_number: 5.1
pages: 22-22
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
any V ∈ C q, E|V is nilpotent, since E maps eigenvectors of g with
eigenvalue λ to those with eigenvalue λq. Thus, the indecomposable
objects of Cq are Vm1,m2, where m1 ≥m2 are integers, namely, Jordan
blocks for E of size m1 −m2 + 1 containing a nonzero vector v with
gv =qm1v,Ev = 0. Then dim Vm1,m2 =qm2 +... +qm1, which is never
zero, so there is no nonzero negligible objects. It is easy to see tha t the
tensor product of Vm1,m2 obeys the same fusion rules as representations
of GLq(2) with highest weights ( m1,m 2), where q2 =q. From this we
obtain
Proposition 5.1. One has
Cq ∼= RepGLq(2).
Proof. Let us construct a tensor functor T : RepGLq(2) → Cq such that
S ◦T is an equivalence Rep GLq(2) → Cq. For this purpose, consider
the Hopf algebra Uq(gl2) with generators g1,g 2,e,f such that g1,g 2 are
commuting grouplike elements and
g1eg−1
1 = qe, g1fg −1
1 = q−1f, g2eg−1
2 = q−1e, g2fg −1
2 = qf,
[e,f ] = g1g−1
2 −g2g−1
1
q − q−1 ,
∆(e) = e ⊗g1g−1
2 + 1 ⊗e, ∆(f ) = f ⊗ 1 +g2g−1
1 ⊗f.
Let us realize Rep GLq(2) as the category of ﬁnite dimensional repre-
sentations of Uq(gl2) on which g1,g 2 act semisimply with eigenvalues
being powers of q. Let J be the twist for Uq(gl2) which acts on v ⊗w by
q−rs when g1v = qrv and g2w = qsw. Then the conjugated coproduct
∆ J (a) := J −1∆(a)J of the element e has the form
∆ J (e) = e ⊗g1 +g−1
1 ⊗e.
Thus, setting ¯e :=g1e, we have
∆ J (¯e) = ¯e ⊗g2
1 + 1 ⊗ ¯e.
We therefore have an inclusion of Hopf algebras ψ : Hq֒→Uq(gl2)J
given by ψ(g) = g2
1,ψ(E) = ¯e, which deﬁnes the desired tensor functor
T . □
