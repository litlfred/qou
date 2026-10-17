---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-015-appendix-b-complements-on-the-pentagon-identity
section_title: "Appendix B. Complements on the pentagon identity"
section_number: null
pages: 43-46
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
toc_source: outline
doc_brief: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangulated cusped hyperbolic 3-manifold (together with some further choices)"
---
In this appendix, we give the omitted details in the last step of the proof of Theorem 3.6.
They are an aﬃne change of coordinates, followed by the corresponding computation of the
formal Gaussian integration.
Equations (49) and Equation (34) give
ψℏ(x, z1)ψℏ(y, z2) = e−ℏ
24 Cℏ(x, z1)Cℏ(y, ˆz1)

ψℏ(−w, ˆz1ˆz−1
0 )ψℏ(w, ˆz0)ψℏ(−w, ˆz2ˆz−1
0 )

w,ˆδ , (174)
where
ˆz1 = z1exℏ1/2
ˆz2 = z2eyℏ1/2
ˆz0 = ˆz1 + ˆz1 −ˆz1ˆz2,
ˆδ =
(ˆz2 + ˆz2 −ˆz1ˆz2)2
ˆz1ˆz2(1 −ˆz1)(1 −ˆz2) .
(175)
44
STAVROS GAROUFALIDIS, MATTHIAS STORZER, AND CAMPBELL WHEELER
Note that ˆz1, ˆz2, ˆz0 and ˆδ are power series in ℏ1/2 which, when evaluated at ℏ= 0, coincide
with z1, z2, z0 and δ given in Equations (46) and (47).
We apply Lemma 3.2 to obtain that
ψℏ(x, z1)ψℏ(y, z2) = e−ℏ
24Cℏ(x, z1)Cℏ(y, ˆz1) exp
1
2(log ˆδ −log δ)

×
D
exp
w2
2 (δ −ˆδ)

ψℏ(−w, ˆz1ˆz−1
0 )ψℏ(w, ˆz0)ψℏ(−w, ˆz2ˆz−1
0 )
E
w,δ .
(176)
where a = aℏ(x, z) ∈
Q(z)[x]Jℏ1/2K is given by
a :=
1
ℏ1/2 log(z0ˆz−1
0 ).
(177)
We write similarly to Equation (34)
ψℏ(−w, ˆz1ˆz−1
0 )ψℏ(w, ˆz0)ψℏ(−w, ˆz2ˆz−1
0 )
= exp(A0 + w((x + y) + 2a + Li0(z1z−1
0 )(a + x) + Li0(z0)a + Li0(z2z−1
0 )(a + y)) + w2
2 (ˆδ −δ))
× ψℏ(−w + a + x, ˆz1ˆz−1
0 )ψℏ(w −a, ˆz0)ψℏ(−w + a + y, ˆz2ˆz−1
0 )
(178)
where A0 = A0,ℏ(x, z) ∈1
ℏ
Q(z)[x]Jℏ1/2K is given by
A0 := 1
ℏ(Li2(ˆz1ˆz−1
0 ) + Li2(ˆz0) + Li2(ˆz2ˆz−1
0 ) −Li2(z1z−1
0 ) + Li2(z0) −Li2(z2z−1
0 ))
+ 1
2(log(1 −ˆz1ˆz−1
0 ) + log(1 −ˆz0) + log(1 −ˆz2ˆz−1
0 )
−log(1 −z1ˆz−1
0 ) + log(1 −z0) + log(1 −z2z−1
0 ))
+
1
ℏ1/2(log(1 −z1z−1
0 )(a + x) −log(1 −z0)a + log(1 −z2z−1
0 )(a + y))
−1
2(Li0(z1z−1
0 )(a + x)2 + Li0(z0)a2 + Li0(z2z−1
0 )(a + y)2)
(179)
Hence, ψℏ(x, z1)ψℏ(y, z2) can be written as
e−ℏ
24Cℏ(x, z1)Cℏ(y, ˆz1) exp
1
2(log(ˆδ) −log(δ)) + A0

×
D
exp

w((u + v) + 2a + Li0(z1z−1
0 )(a + u) + Li0(z0)a + Li0(z2z−1
0 )(a + v))

× ψℏ(−w + a + x, ˆz1ˆz−1
0 )ψℏ(w −a, ˆz0)ψℏ(−w, ˆz2ˆz−1
0 )
E
w+a+y,δ .
(180)
With the change of variables
w 7→w + a + x + y −xz1 + yz2
z0
(181)
PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS
45
combined with Equation (23) of Lemma 3.1, we obtain that
e−ℏ
24 Cℏ(x, z1)Cℏ(y, ˆz1) exp
1
2 (log(ˆδ) −log(δ)) + A0

exp
 δ
2

a + x + y −xz2 + yz1
z0
2
+

a + x + y −xz2 + yz1
z0

(x + y + δa + Li0(z1z−1
0
)x + Li0(z2z−1
0
)y)

×
D
ψℏ

−w −y + xz2 + yz1
z0
, ˆz1ˆz−1
0

ψℏ

w + x + y + xz2 + yz1
z0
, ˆz0

ψℏ

−w −x + xz2 + yz1
z0
, ˆz2ˆz−1
0
E
w,δ .
(182)
Hence, in order to prove Equation (48) it remains to prove that the term in front of the
bracket simpliﬁes to e−ℏ
24. For this, we use the deﬁnitions of Cℏ(35) and A0 (179) to obtain
log(Cℏ(x, z1)) + log(Cℏ(y, ˆz1)) + 1
2(log(ˆδ) −log(δ)) + A0 + δ
2

a + x + y −xz2 + yz1
z0
2
+

a + x + y −xz2 + yz1
z0

(x + y + δa + Li0(z1z−1
0 )x + Li0(z2z−1
0 )y))
= 1
ℏ(−Li2(ˆz1) + Li2(z1) −Li2(ˆz2) + Li2(z2) + Li2(ˆz1ˆz−1
0 ) −Li2(z1z−1
0 )
+ Li2(ˆz−1
0 ) −Li2(z0) + Li2(ˆz2ˆz−1
0 ) −Li2(z2z−1
0 ))
+ 1
2(−log(1 −ˆz1) + log(1 −z1) −log(1 −ˆz2) + log(1 −z2) + log ˆδ −log δ
+ log(1 −ˆz1ˆz−1
0 ) −log(1 −z1z−1
0 ) + log(1 −ˆz0) −log(1 −z0)
+ log(1 −ˆz2ˆz−1
0 ) −log(1 −z2z−1
0 ))
+
1
ℏ1/2(−log(1 −z1)x −log(1 −z2)y + (x + y)(log(z0) −log(ˆzo))
+ log(1 −z1z−1
0 )(a + x) −log(1 −z0)a + log(1 −z2z−1
0 )(a + y))
+ a2
2 (δ −Li0(z1z−1
0 ) −Li0(z0) −Li0(z2z−1
0 ))
+

x + y −xz2 + yz2
z0

x + y + Li0(z1z−1
0 )x + Li0(z2z−1
0 )y −δ
2

x + y −xz2 + yz2
z0

−Li0(z1z−1
0 )x2
2 −Li0(z2z−1
0 )y2
2 .
(183)
Inserting the deﬁnitions of δ (47) and ˆδ (175) and using the relations
1 −z1z−1
0
= z2(1 −z1)z−1
0 ,
1 −z2z−1
0
= z1(1 −z2)z−1
0 ,
1 −z0 = (1 −z1)(1 −z2),
(184)
and similar ones for ˆz1, ˆz2 and ˆz0 we obtain that the terms
1
2(−log(1 −ˆz1) + log(1 −z1) −log(1 −ˆz2) + log(1 −z2) + log ˆδ −log δ
+ log(1 −ˆz1ˆz−1
0 ) −log(1 −z1z−1
0 ) + log(1 −ˆz0) −log(1 −z0)
+ log(1 −ˆz2ˆz−1
0 ) −log(1 −z2z−1
0 ))
(185)
46
STAVROS GAROUFALIDIS, MATTHIAS STORZER, AND CAMPBELL WHEELER
vanish. Furthermore, we have
δ −Li0(z1z−1
0 ) −Li0(z0) −Li0(z2z−1
0 ) = 2
(186)
as well as

x + y −xz2 + yz2
z0

x + y + Li0(z1z−1
0 )x + Li0(z2z−1
0 )y −δ
2

x + y −xz2 + yz2
z0

−Li0(z1z−1
0 )x2
2 −Li0(z2z−1
0 )y2
2
= xy.
(187)
Therefore, Equation (183) simpliﬁes to
1
ℏ(−Li2(ˆz1) + Li2(z1) −Li2(ˆz2) + Li2(z2) + Li2(ˆz1ˆz−1
0 ) −Li2(z1z−1
0 )
+ Li2(ˆz−1
0 ) −Li2(z0) + Li2(ˆz2ˆz−1
0 ) −Li2(z2z−1
0 ))
+
1
ℏ1/2(−log(1 −z1)x −log(1 −z2)y + (x + y)(log(z0) −log(ˆzo))
+ log(1 −z1z−1
0 )(a + x) −log(1 −z0)a + log(1 −z2z−1
0 )(a + y))
+ a2 + xy.
(188)
Using the deﬁnition of a and the relations from Equation (184) we compute
1
ℏ1/2(−log(1 −z1)x −log(1 −z2)y + (x + y)(log(z0) −log(ˆzo))
+ log(1 −z1z−1
0 )(a + x) −log(1 −z0)a + log(1 −z2z−1
0 )(a + y))
+ a2 + xy
=
1
ℏ1/2(x(log(z2) −log(ˆz0)) + y(log(z1) −log(ˆz0))
+ 1
ℏ(log(z0)(log(z1) + log(z2)) + log2(z0) −log(ˆz0)(log(z1) + log(z2)))
= 1
ℏ(log(z2) log(z0) + log(z1) log(z0) −log(z1) log(z2)
−log(ˆz2) log(ˆz0) + log(ˆz1) log(ˆz2) −log(ˆz1) log(ˆz0)).
(189)
Using the 5–term relation of the dilogarithm we obtain that the expression in Equation (188)
Li2(z1) + Li2(z2) −Li2(z1z−1
0
) −Li2(z0) −Li2(z2z−1
0
) + log(z2) log(z0) + log(z1) log(z0) −log(z1) log(z2)
−Li2(ˆz1) −Li2(ˆz2) + Li2(ˆz1ˆz−1
0
) + Li2(ˆz−1
0
) + Li2(ˆz2ˆz−1
0
) −log(ˆz2) log(ˆz0) −log(ˆz1) log(ˆz0) + log(ˆz1) log(ˆz2).
(190)
vanishes. In particular, the terms in front of the bracket in Equation (182) simplify to e−ℏ
24
which concludes the proof of the last step of Theorem 3.6.
