---
doc_id: arxiv-q-alg-9712055v2
doc_title: "The q-Fourier transform of q-distributions. M.A.Olshanetsky"
section_id: sec-013-5-from-47-and-48-66-and-67-we-obtain
section_title: "From (4.7) and (4.8), (6.6) and (6.7) we obtain"
section_number: 5
pages: 15-18
source_pdf: 9712055v2.pdf
source_sha256: eccb15d2c3dc7346
---
F ′
q2θ+
q2 = 1
2F ′
q2(θ+
q2−θ−
q2 + 1) = is−1
2Θ 0
+δq2,
F ′
q2θ−
q2 = 1
2F ′
q2(−θ+
q2 +θ−
q2 + 1) =−is−1
2Θ 0
+δq2.
Proposition 6.2 For an arbitrary integer n≥ 0
F ′
q2zn = 2inq−n(n+1) (q2,q 2)n
(1−q2)ns−nδq2(s).
Proof. The relation 1 = (1−q2)n
(q2,q 2)n
∂n
zzn follows from (3.2). Next, from (6.6) and Proposition
6.1 we obtain
δq2(s) = 1
2F ′
q21 = (1−q2)n
2(q2,q 2)n
F ′
q2∂n
zzn = (−i)n (1−q2)n
2(q2,q 2)n
(Λ −1s)nF ′
q2zn.
Thus,
F ′
q2zn = 2in (q2,q 2)n
(1−q2)n (s−1Λ) nδq2(s). (6.8)
Since (s−1Λ) n =q−n(n−1)s−nΛ n and δq2(q2ns) = q−2nδq2(s),
(s−1Λ) nδq2(s) = q−n(n+1)s−nδq2(s).
Then, the statement of Proposition follows from (6.8).
Proposition 6.3 For an arbitrary integer n≥ 0
F ′
q2z−n−1 =in+1 (q2,q 2)n
(1−q2)nsn signs.
15
Proof. For an arbitrary n≥ 0 we have from (3.3)
∂n
zz−1 = (−1)nq−n(n+1) (q2,q 2)n
(1−q2)nz−n−1.
Using Proposition 6.1 we obtain
F ′
q2z−n−1 = (−1)nqn(n+1) (1−q2)n
(1−q2)nF ′
q2∂n
zz−1 =inqn(n+1) (1−q2)n
(1−q2)n (Λ −1s)nF ′
q2z−1.
It can be derived from (4.5) that (Λ −1s)n =q−n(n+1)snΛ −n. Using this equality and (6.5),
we come to the statement of Proposition.
Proposition 6.4
F ′
q2zν−1
+ = eq2(q2)Eq2(−q2(1−ν))
2Θ 0
(¯cνs−ν
− +cνs−ν
+ ), (6.9)
F ′
q2zν−1
− =−eq2(q2)Eq2(−q2(1−ν))
2Θ 0
(cνs−ν
− + ¯cνs−ν
+ ), (6.10)
where
cν =
∞∑
m=−∞
q2νm (q−2m +i(1−q2))
(1−q2)−1q−2m + (1−q2)q2m.
Proof. If 0 < Reν <1, (4.10) and (6.2) give
Fq2zν−1
+ = 1−q2
2Θ 0
∞∑
m=−∞
q2νmeq2(i(1−q2)q2ms). (6.11)
It can be directly checked that zν−1
+ satisﬁes the equation
z∂zf (z) = 1−q2(ν−1)
1−q2 f (z).
From the Proposition 6.1 we obtain that the q2-Fourier transformed equation takes the
form
−q−2∂s(sg(q−2s)) = 1−q2(ν−1)
1−q2 g(s).
Since s−ν
− and s−ν
+ satisfy this equation we can write
F ′
q2zν−1
+ =c1s−ν
− +c2s−ν
+ . (6.12)
Substituting s = 1 in (6.12) we obtain from (2.6),(6.11) and (6.12)
c2 = 1−q2
2Θ 0
∞∑
m=−∞
q2νmeq2(i(1−q2)q2m) =
= 1−q2
2Θ 0
eq2(q2)
∞∑
m=−∞
q2νm
∞∑
n=0
(−1)nqn(n+1)
(q2,q 2)n[1−i(1−q2)q2(m+n)].
16
If 0 < Reν <1, we can change the order of summations. Then
c2 = 1−q2
2Θ 0
eq2(q2)
∞∑
n=0
(−1)nqn(n+1)
(q2,q 2)n
∞∑
m=−∞
q2νm
1−i(1−q2)q2(m+n) =
= eq2(q2)
2Θ 0
∞∑
n=0
(−1)nqn(n−1)q2(1−ν)n
(q2,q 2)n
∞∑
m=−∞
q2νm (q−2m +i(1−q2))
(1−q2)−1q−2m + (1−q2)q2m.
We denote the sum of the inner series by cν. Then
c2 = cν
2Θ 0
eq2(q2)Eq2(−q2(1−ν))
Assume now that s =−1 in (6.12). Then in the same way we obtain
c1 = ¯cν
2Θ 0
eq2(q2)Eq2(−q2(1−ν))
and thereby come to (6.9). It determines F ′
q2zν−1
+ as (6.9) for non-integer ν by the ana-
lytical continuation.
The q2-Fourier transform of zν−1
− , ν ⁄= 0,±1,....
F ′
q2zν−1
− =−1−q2
2Θ 0
∞∑
m=−∞
q2νmeq2
(−i(1−q2)q2ms).
diﬀers from (6.11) by the sign and the complex conjugation, i.e., in this way we have
(6.10).
We summarize all results in the table:
f (z) g(s) = 1
2Θ 0
∫
dq2zf (z)Eq2(i(1−q2)zs)
δq2(z) 1
2Θ 0
θ+
q2(z) i
2Θ 0
s−1 +δq2(s)
θ−
q2(z) − i
2Θ 0
s−1 +δq2(s)
zn 2inq−n(n+1) (q2,q 2)n
(1−q2)ns−nδq2(s)
(n = 0, 1,... )
z−n−1 in+1 (1−q2)n
(q2,q 2)n
sn signs
(n = 0, 1,... )
zν−1
+
eq2 (q2)Eq 2(−q2(1− ν ))
2Θ 0
(¯cνs−ν
− +cνs−ν
+ )
(ν⁄= 0,±1,... )
(zν−1
− −
eq2 (q2)Eq 2(−q2(1− ν ))
2Θ 0
(cνs−ν
− + ¯cνs−ν
+ ]
(ν⁄= 0,±1,... )
Acknowledgments.
The work is supported in part by grants 96-15-96455 for support of scientiﬁc schools,
INTAS-93-0166 extension and by Award No. RM2-150 of the Civilian R esearch & De-
velopment Foundation (CRDF) for the Independent States of the Former Soviet Union
(M.O.); by RFBR 97-01-00747 and NIOKR MPS RF (V.R.) The work is prepared partly
during visit of M.O. in IHES (Bur-sur-Yvette). He is grateful to Pro f. K.Gawedzky for
hospitality.
17
