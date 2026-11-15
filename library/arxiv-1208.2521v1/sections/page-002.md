---
doc_id: arxiv-1208.2521v1
doc_title: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS"
section_id: page-002
section_title: "Page 2"
section_number: null
pages: 2-2
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
toc_source: undetermined
doc_brief: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
2
TOM H. KOORNWINDER AND REN´E F. SWARTTOUW
where the q-shifted factorials are deﬁned by
(1.3)
(a; q)k :=
k−1
Y
j=0
(1 −aqj),
k = 1, 2, . . .;
(a; q)0 := 1;
(a; q)∞:= lim
k→∞(a; q)k,
|q| < 1.
Hahn [8] considered the case α = 0 of (1.2). They obtained these functions as
the solutions of a special basic Sturm-Liouville equation, by which they could also
derive the following q-analogue of the Fourier-Bessel orthogonality relations:
Z 1
0
xα Cα(q; µiqx) Cα(q; µjqx) dqx = 0,
i̸ = j,
α > −1,
where µ1, µ2, . . . are the roots of the equation Cα(q; µ) = 0, and where the q-integral
is deﬁned by
Z 1
0
f(x) dqx := (1 −q)
∞
X
k=0
f(qk) qk.
By specialization to α = ±1/2, Exton obtained similar orthogonalities for q-
analogues of the sines and cosines.
So some of the harmonic analysis involving
Bessel functions, sines and cosines has been extended to the q-case. However, q-
analogues of the Fourier-cosine, Fourier-sine and Hankel transforms were missing
until now (except for a q-Laplace transform with inversion formula, cf. Hahn [7, §9]
and Feinsilver [5]).
Exton [4, (5.3.3.1)] also generalized the generating function
(1.4)
ez(t−t−1)/2 =
∞
X
k=−∞
tk Jk(z)
(cf. Watson [15, §2.1 (1)]) to the case of his q-Bessel functions (1.2):
(1.5)
eq((1 −q)t) Eq(−(1 −q)t−1x) =
∞
X
n=−∞
tn Cn(q; x),
where
(1.6)
eq(z) :=
∞
X
k=0
zk
(q; q)k
=
1
(z; q)∞
,
|z| < 1,
and
(1.7)
Eq(z) :=
∞
X
k=0
qk(k−1)/2 zk
(q; q)k
= (−z; q)∞
