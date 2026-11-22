---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: page-017
section_title: "Page 17"
section_number: null
pages: 17-17
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: undetermined
doc_brief: "arXiv:hep-th/9304063v2 29 Jan 1999 — 18 sections: Page 1; Page 2; Page 3"
---
contradicting ν̸ = 0.
Now that we know the eigenvalues λi of K are simple we can order them so that λ0 > λ1 > . . . . There is a
permutation σ of N such that the eigenvalue corresponding to fi is λσ(i). This permutation is independent of s since
the eigenvalues µi and λi both vary continuously with s. The next lemma allows us to compute dλi/ds for each i.
Lemma 2. Let λ be a simple eigenvalue of an integral operator on (0, 1) with symmetric kernel of the form s K(sx, sy)
where K(x, y) is smooth and symmetric. Let f be a corresponding eigenfunction. Then
dλ
ds = λ
s
f(1)2
R 1
0 f(x)2 dx
.
Proof. We may assume f normalized so that
R 1
0 f(x)2dx = 1. Then according to Lemma 3 of [28] we have
dλ
ds =
Z 1
0
Z 1
0
∂
∂s(s K(sx, sy)) f(y) f(x) dy dx.
(This holds no matter what the form of the kernel.) In the case at hand the ﬁrst factor in the integrand equals
K(sx, sy) + (x ∂
∂x + y ∂
∂y)K(sx, sy)
and we easily deduce from this that the integral itself equals
λ
s
Z 1
0
f(x)2dx +
Z 1
0
x f ′(x) f(x) dx +
Z 1
0
y f ′(y) f(y) dy

and integration by parts shows that the expression in parentheses equals f(1)2.
Remark. It is easily seen that the conclusion of the lemma holds when the kernel has a mild singularity at 0 such as
our Besssel kernel has when α < 0.
Lemma 3. For each i we have λi →1 as s →∞.
Proof. The Hankel transform, when rescaled by the variable change x 7→√x, is the integral operator H on (0, ∞) with
kernel 1
2Jα(√xy) and so our operator K on (0, s) may be thought of as Ps H Ps H Ps where Ps denotes the projection
from L2(0, ∞) to L2(0, s). Since, as is well-known, H2 = I, the minimax characterization of the eigenvalues shows
that for each i the eigenvalue of Ps H Ps with i’th largest absolute value tends to ± 1 as s →∞. Since our operator
is the square of this one, the statement of the lemma follows.
We can now deduce the asymptotic formula (15) for the eigenvalues λi. We apply Lemma 2 to the eigenvalue λσ(i)
associated with the eigenfunction fi(x) of (3.3) and use (3.14) to deduce
d log λσ(i)
ds
∼
2π
Γ(α + i + 1) i! si+ α
2 e−2√s 24i+2α+2.
Recalling Lemma 3 we see that we can integrate from s to ∞and we obtain
1 −λσ(i) ∼
2π
Γ(α + i + 1) i! si+ α+1
2
e−2√s 24i+2α+2.
It remains to show that σ(i) = i for all i. But it is clear from the above formula that i < j implies that λσ(i) > λσ(j)
for large s (and so for all s) and therefore σ(i) < σ(j). Since σ : N →N is onto, we must have σ(i) = i for all i.
ACKNOWLEDGMENTS
We wish to thank Professor F. J. Dyson for bringing to our attention the notion of “hard edge” random matrix
ensembles. This work was supported in part by the National Science Foundation, DMS–9001794 and DMS–9216203,
and this support is gratefully acknowledged.
17
