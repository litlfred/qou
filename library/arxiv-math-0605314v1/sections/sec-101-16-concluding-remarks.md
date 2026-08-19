---
doc_id: arxiv-math-0605314v1
doc_title: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO"
section_id: sec-101-16-concluding-remarks
section_title: "Concluding remarks"
section_number: 16
pages: 61-62
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A UNIFIED WITTEN-RESHETIKHIN-TURAEV INVARIANT FOR INTEGRAL HOMOLOGY SPHERES KAZUO HABIRO — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the"
---
In this section, we give some remarks and discussions.
16.1. The WRT invariants as limiting values of holomorphic functi ons.
As explained in the introduction, the invariant JM for an integral homology sphere
M uniﬁes the WRT invariants τζ(M ) for all the roots of unity in an algebraic way.
It should be remarked that there is another analytic approach to “unify” the WRT
invariants by realizing the radial limiting values of a holo morphic function deﬁned
on the unit disk {z∈ C;|z|< 1}, studied in [44, 45, 46, 47, 24, 25, 26, 27].
Unfortunately, the invariant JM∈ ˆZ[q] does not immediately determine such a
holomorphic function, i.e., there is no natural homomorphi sm from the ring ˆZ[q]
to the ring of holomorphic function on |q|< 1. However, some expressions for JM
may deﬁne well-deﬁned holomorphic functions for on |q| < 1 as we explain below
for the Poincar´ e homology sphere Σ(2 , 3, 5).
We have
JΣ(2 ,3,5) =
∑
n≥0
qn (1−qn+1)(1−qn+2)··· (1−q2n+1)
1−q ∈ ˆZ[q].(16.1)
The modiﬁed WRT invariant W (ζ) = ζ(ζ− 1)τζ (Σ(2 , 3, 5)), ζ ∈ Z, deﬁned by
Lawrence and Zagier [47], is uniﬁed into
W (q) = q(q− 1)JΣ(2 ,3,5)∈ ˆZ[q].
For our purpose, it is useful to modify it further as
B(q) = 1−W (q) = 1 + q(1−q)JΣ(2 ,3,5)
=
∑
n≥0
qn(qn;q)n,(16.2)
62 KAZUO HABIRO
where (qn;q)n = (1 −qn)(1−qn+1)··· (1−q2n−1). A beautiful observation by
Lawrence and Zagier [47] is that the series
A(q) =
∑
n≥1
χ+(n)q
n2−1
120 = 1 +q +q3 +q7−q8−···∈ Z[[q]],
which converges on |q| < 1, converges radially at each root of unity ζ to 2(1 −
W (ζ)) = 2B(ζ). They also showed that the radial asymptotic expansion of A(q) at
q = 1 gives 2 times the Ohtsuki series τ O(M ).
Note that the formula (16.2) for B(q) can also deﬁne a power series in q.
(Actually, (16.2) deﬁnes an element of lim←−nZ[q]/(qn(q)n) ∼
= ˆZ[q]× Z[[q]].) Let
B(q)Z[[q]]∈ Z[[q]] denote this element. Hikami [26] proved
A(q) = B(q)Z[[q]]∈ Z[[q]].
Thus, there are two ways to obtain the value of the (modiﬁed) W RT invariants
from B(q). One is just to evaluate at roots of unity, and the other is to expand it
in q, take the radial limit at roots of unity and then multiply by 1
2 . The meaning
of the factor 1
2 is not clear to the author. It would be natural to expect that t he
radial asymptotic expansion at each root of unity ζ is 2 times the power series
ιζ(B(q))∈ Z[ζ][[q−ζ]].
It would be natural to expect that certain formulas (16.1) fo r JM of integral
homology spheres M may give a power series in q whose radial asymptotic behavior
at a root of unity ζ is closely related to the “algebraic behavior near ζ” obtained
by the map ιζ : ˆZ[q]→ Z[ζ][[q−ζ]]. For example, for an integral homology sphere
Mi,j,k with i,j,k > 0 deﬁned in Section 14.3, the formula 14.8 of JMi,j,k deﬁnes
an element of Z[[q]] which converges on |q|< 1. Note that the Poincar´ e homology
sphere Σ(2 , 3, 5) is the special case M1,1,1.
