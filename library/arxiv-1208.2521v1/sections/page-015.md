---
doc_id: arxiv-1208.2521v1
doc_title: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS"
section_id: page-015
section_title: "Page 15"
section_number: null
pages: 15-15
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
toc_source: undetermined
doc_brief: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS
15
Here we have used the notation (3.3).
(The functions introduced above should
not be confused with the functions cosq and sinq considered in [6, Exercise 1.14].)
Clearly we have the formal (termwise) limits
cos((1 −q)z; q2) −→cos z
and
sin((1 −q)z; q2) −→sin z
as q ↑1. By Proposition A.2 these limit transitions hold pointwise, uniformly on
compacta. When we substitute (5.2) or (5.4) in (3.4) and replace f(qk), g(qn) by
q−k/2f(qk), q−n/2g(qn), we obtain the transform pairs
(5.5)















g(qn) = (q; q2)∞
(q2; q2)∞
∞
X
k=−∞
qk



cos(qk+n; q2)
or
sin(qk+n; q2)


f(qk),
f(qk) = (q; q2)∞
(q2; q2)∞
∞
X
n=−∞
qn



cos(qk+n; q2)
or
sin(qk+n; q2)


g(qn).
The transformations f 7→g and g 7→f of (5.5) establish an isometry of Hilbert
spaces:
∞
X
k=−∞
qk |f(qk)|2 =
∞
X
n=−∞
qn |g(qn)|2.
Now let q ↑1 under the side condition that log(1−q)
log q
∈2Z. Replace qk, qn in (5.5)
by (1 −q)1/2qk, (1 −q)1/2qn, and then f((1 −q)1/2qk), g((1 −q)1/2qn) by f(qk),
g(qn). Then (5.5) takes the form















g(λ) = (1 + q)1/2
Γq2(1/2)
Z ∞
0
f(x)



cos((1 −q)λx; q2)
or
sin((1 −q)λx; q2)


dqx,
f(x) = (1 + q)1/2
Γq2(1/2)
Z ∞
0
g(λ)



cos((1 −q)λx; q2)
or
sin((1 −q)λx; q2)


dqλ.
Formally, as q ↑1, we obtain the classical Fourier pairs
g(λ) =
p
2/π
Z ∞
0
f(x) cos(λx) dx,
f(x) =
p
2/π
Z ∞
0
g(λ) cos(λx) dλ
and
g(λ) =
p
2/π
Z ∞
0
f(x) sin(λx) dx,
f(x) =
p
2/π
Z ∞
0
g(λ) sin(λx) dλ.
With the notation
(Dqf)(z) = Dq,z f(z) := f(z) −f(qz)
(1 −q)z
