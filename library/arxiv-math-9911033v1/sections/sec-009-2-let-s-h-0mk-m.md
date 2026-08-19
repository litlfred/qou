---
doc_id: arxiv-math-9911033v1
doc_title: "ON THE LOWER BOUND ESTIMA TES OF SECTIONS OF THE CANONICAL BUNDLES OVER A RIEMANN SURF ACE ZHIQIN LU Contents 1. Introductions 1 2. A lower bound estimate 4 3. A counterexample 11 "
section_id: sec-009-2-let-s-h-0mk-m
section_title: "Let S ∈H 0(M,K m"
section_number: 2
pages: 14-17
source_pdf: 9911033v1.pdf
source_sha256: 196c05d2e3419565
doc_brief: "ON THE LOWER BOUND ESTIMATES OF SECTIONS OF THE CANONICAL BUNDLES OVER A RIEMANN SURFACE ZHIQIN LU Contents 1. Introductions 1 2. A lower bound estimate 4 3. A counterexample 11 4. Partial uniform est"
---
M ). We choose an x0 ∈M as follows: let ρ0< 0 be the
number such that
δ(coshρ0)2 =ε1.
14
Then ρ0 → −∞, ρ0 +R → +∞ as δ → 0.
By (3.3), we see that ( dz)m ∈H 0(C,K m
M ). Furthermore (dz)m ⁄= 0 on C.
Thus for any S ∈H 0(M,K m
M ), there is a holomorphic function f onC such
that
S|C =f (dz)m.
Let
f =g1 +g2 +g3,
where g1,g 2,g 3 are deﬁned in Lemma 3.1. Let
Si =gi(dz)m, i = 1, 2, 3.(3.7)
Lemma 3.4. With the notations as above, let x0 = (ρ0, 0). Then
lim
δ→0
||Si||2(x0)
||Si||2
L2(C)
= 0
for i = 1, 2, 3.
Proof. By (3.2), we have
w(x0) = e− 4π
δ (arctan eρ 0 − π
4 ).
Thus
||S1||2(x0) = 1
(coshρ0)2m |
∞∑
k=1
Ake− 4π
δ k(arctan eρ 0 −arctan e− R)+ 2πi
δ kθ|2
≤ 1
(coshρ0)2m
∞∑
k=1
|Ak|2e− 8π
δ k(arctan eρ 0− 1−arctan e− R)
·
∞∑
k=1
e− 8π
δ k(arctan eρ 0 −arctan eρ 0− 1)
≤
∞∑
k=1
|Ak|2e− 8π
δ k(arctan eρ 0− 1−arctan e− R) ·
∞∑
k=1
e− 4πk
δ cosh(ρ 0− 1).
(3.8)
We assume that δ is so small that
4π
δ cosh(ρ0 − 1) ≥ µ√
δ
> 0,
where µ is an absolute constant. In addition, assume that e− µ√
δ < 1
2 . Then
∞∑
k=1
e− 4πk
δ cosh(ρ 0− 1) ≤
∞∑
k=1
e− µk√
δ ≤ 2e− µ√
δ.(3.9)
15
On the other hand
||S1||2
L2(C) =δ
∫ R
−R
1
(coshρ)2m−1
∞∑
k=1
|Ak|2e− 8πk
δ (arctan eρ −arctan e− R)dρ.
Assuming ρ0 − 1 +R> 1 and cosh R< 2 sinhR, we have
||S1||2
L2(C)
≥δ
∫ ρ0−1
−R
1
(coshR)2m−1
∞∑
k=1
|Ak|2e− 8πk
δ (arctan eρ 0− 1−arctan e− R)dρ
≥ δ
( ε1
2δ )2m−1
∞∑
k=1
|Ak|2e− 8πk
δ (arctan eρ 0− 1−arctan e− R).
(3.10)
By (3.8), (3.9) and (3.10), we have
||S1||2(x0)
||S1||2
L2(C)
≤ 22m−1ε2m−1
1
δ2me− µ√
δ
→ 0(3.11)
for δ → 0.
The idea for estimating S2 andS3 are almost the same. By (3.7), we have
||S2||2(x0) = 1
(coshρ0)2m |B0|2,
||S2||2
L2(C) =δ
∫ R
−R
1
(coshρ)2m−1 |B0|2dρ.
(3.12)
If δ → 0, then R → +∞. Thus if R is large enough, we have
∫ R
−R
1
(coshρ)2m−1dρ ≥µ 1 > 0,
where µ 1 is a constant only depending on m. Thus
||S2||2(x0)
||S2||2
L2(C)
= 1
µ 1
1
δ(coshρ0)2m = 1
µ 1εm
1
δm−1 → 0(3.13)
for δ → 0.
ForS3, we have
||S3||2(x0) = 1
(coshρ0)2m |
−1∑
k=−∞
Bke− 4π
δ k(arctan eρ 0 −arctan eR)|2
≤
−1∑
k=−∞
|Bk|2e− 8π
δ k( π
4 −arctan eR)
−1∑
k=−∞
e− 8π
δ k(arctan eρ 0 − π
4 ).
(3.14)
Since ρ0 → −∞, we can assume
arctaneρ0 < π
8.
16
Thus
−1∑
k=−∞
e− 8π
δ k(arctan eρ 0 − π
4 ) ≤
−1∑
k=−∞
e
π 2
δ k ≤ 2e− π 2
δ(3.15)
for e− π
δ 2 < 1
2 . On the other hand,
||S3||2
L2(C) =δ
∫ R
−R
1
(coshρ)2m−1
−1∑
k=−∞
|Bk|2e− 8πk
δ (arctan eρ −arctan eR)dρ
≥δ
∫ R
0
1
(coshρ)2m−1
−1∑
k=−∞
|Bk|2e− 8πk
δ ( π
4 −arctan eR)dρ
≥ δR
(coshR)2m−1
−1∑
k=−∞
|Bk|2e− 8πk
δ ( π
4 −arctan eR).
(3.16)
By (3.14), (3.15) and (3.16), we have
||S3||2(x0)
||S3||2
L2(C)
≤ 2e− π 2
δ
δR (coshR)2m−1 ≤ 22m
δ2m 2e− π 2
δ → 0.(3.17)
Thus for any ε> 0 and m ≥ 2, from (3.11), (3.13) and (3.17), we can ﬁnd
M such that there is a closed geodesic with the length suﬃcient ly small and
an x0 ∈M such that
||Si||2(x0)
||Si||2
L2(C)
≤ε
for i = 1, 2, 3.
One can check that
(Si,S j)L2(C) = 0.
Thus for any S ∈H 0(M,K m
M ) with ||S||L2(M ) and x0 ∈M ,
||S||2(x0) ≤ ||S||2(x0)
||S||2
L2(C)
≤ 3
∑ 3
i=1 ||Si||2(x0)
∑ 3
i=1 ||Si||2
L2(C)
≤ 3ε.
Theorem 3.2 is proved.
