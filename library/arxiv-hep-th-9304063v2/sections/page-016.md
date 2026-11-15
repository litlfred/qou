---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: page-016
section_title: "Page 16"
section_number: null
pages: 16-16
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: undetermined
doc_brief: "arXiv:hep-th/9304063v2 29 Jan 1999 — 18 sections: Page 1; Page 2; Page 3"
---
6. The asymptotics of λi
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
