---
doc_id: arxiv-math-9301212v1
doc_title: "arXiv:math/9301212v1 [math.GT] 1 Jan 1993"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: 9301212v1.pdf
source_sha256: 029787800ddf73e5
toc_source: undetermined
doc_brief: "arXiv:math/9301212v1 [math.GT] 1 Jan 1993 — A physically natural potential energy for simple closed curves in R3 is shown to be invariant under M¨obius transformations."
---
4
STEVE BRYSON, M. H. FREEDMAN, Z.-X. HE, AND ZHENGHAN WANG
where L = Length(I(γ)) and
ε+ = ε+(u) = D((I ◦γ)(u), (I ◦γ)(u + ε)) = s(u + ε) −s(u)
=
Z u+ε
u
f(w) dw = f(u)ε + ε2
Z 1
0
(1 −t)f ′(u + εt) dt
and
ε−= ε−(u) = D((I ◦γ)(u −ε), (I ◦γ)(u)) = f(u)ε −ε2
Z 1
0
(1 −t)f ′(u −εt) dt.
Since |f ′(w)| is uniformly bounded, we have
1
ε+
=
1
f(u)ε
"
1
1 + (ε/f(u))
R 1
0 (1 −t)f ′(u + εt) dt
#
=
1
f(u)ε

1 −
ε
f(u)
Z 1
0
(1 −t)f ′(u + εt) dt + O(ε2)

=
1
f(u)ε −
1
f(u)2
Z 1
0
(1 −t)f ′(u + εt) dt + O(ε).
Similarly,
1
ε−
=
1
f(u)ε +
1
f(u)2
Z 1
0
(1 −t)f ′(u −εt) dt + O(ε).
Then by (4)
(5)
regularization (2) = 4 −
Z
R/lZ
2
ε du
+
ZZ
R/lZ×[0,1]
(1 −t)
f(u) [f ′(u + εt) −f ′(u −εt)] du dt + O(ε)
= 4 −2l
ε + O(ε) + O(ε).
Comparing (3) and (5), we get
Eε(γ) −Eε(I ◦γ) = O(ε);
hence, E(γ) = E(I ◦γ).
For the second assertion, let I send a point of γ to inﬁnity. In this case L = ∞
and, thus, the constant term 4 in (5) disappears.
□
Acknowledgment
The authors wish to thank Adriano Garsia and Fred Hickling for useful discus-
sions.
