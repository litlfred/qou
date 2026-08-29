---
doc_id: arxiv-hep-th-9304063v2
doc_title: "Level Spacing Distributions and the Bessel Kernel Craig A. Tracy∗"
section_id: sec-024-6-the-asymptotics-of-λi
section_title: "The asymptotics of λi"
section_number: 6
pages: 16-17
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
doc_brief: "Level Spacing Distributions and the Bessel Kernel Craig A. Tracy∗ — 26 sections: INTRODUCTION AND STATEMENT OF RESU; KN(; (α2 −aj + 2v)q2"
---
Since L commutes with our integral operator K, rescaled to act on (0, 1), the set {fi} of eigenfunctions corresponding
to the eigenvalues µ0 < µ1 < . . . of L is the set of eigenfunctions of K corresponding to its eigenvalues, in some order.
Lemma 1. The eigenvalues of K are simple.
Proof. Since the eigenvalues of K are the squares of the eigenvalues of J what we have to show is that if f1(x) and
f2(x) are eigenfunctions of L (they need not correspond to any particular µ here) and if for some ν we have either
Z 1
0
Jα(√sxy)fi(y)dy = νfi(x)
(i = 1, 2)
or
Z 1
0
Jα(√sxy)f1(y)dy = νf1(x),
Z 1
0
Jα(√sxy)f2(y)dy = −νf2(x)
then f1 and f2 are linearly dependent. We shall assume them normalized so that they both have the value 1 at x = 1.
Notice ﬁrst that ν̸ = 0 for otherwise if we expand the f1 equation near x = 0 we would ﬁnd that
Z 1
0
x
α
2 +kf1(x)dx = 0,
k = 0, 1, . . .,
and f1 would be identically 0.
Next we deﬁne
H(x) = e−x/2Jα(
√
s e−x), gi(x) = e−x/2fi(e−x),
make the obvious variable changes, and ﬁnd that our relations become
Z ∞
0
H(x + y) gi(y) dy = ν gi(x),
(i = 1, 2),
(3.15)
Z ∞
0
H(x + y) g1(y) dy = ν g1(x),
Z ∞
0
H(x + y) g2(y) dy = −νg2(x).
(3.16)
What comes now is almost identical to the proof of Lemma 1 of [28]. Assuming ﬁrst that (3.15) holds, we diﬀerentiate
twice this relation with i = 1 and then integrate by parts twice to obtain
ν g1(x) = −H′(x) + H(x) g′
1(0) +
Z ∞
0
H(x + y) g1(y) dy.
If we multiply both sides by g2(x) and integrate, using (3.15) and its diﬀerentiated version, we obtain (recall that
gi(0) = 1)
ν
Z ∞
0
g′′
1(x) g2(x) dx = −νg′
2(0) + νg′
1(0) + ν
Z ∞
0
g2(y) g′′
1 (y) dy.
Thus, since ν̸ = 0, we have g′
1(0) = g′
2(0). Equivalently, f ′
1(1) = f ′
2(1). But since also f1(1) = f2(1), it follows from
equation (2) that the corresponding eigenvalues µ must be the same, and so the eigenfunctions are the same.
Next, assume (3.16) holds. Diﬀerentiating both sides of the ﬁrst relation once and integrating by parts give
ν g′
1(x) = −H(x) −
Z ∞
0
H(x + y) g′
1(y) dy.
Multiplying both sides of this by g2(x) and integrating, using the second part of (3.16), we obtain
ν
Z ∞
0
g′
1(x) g2(x) dx = −ν + ν
Z ∞
0
g2(y) g′
1(y) dy,
16
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
