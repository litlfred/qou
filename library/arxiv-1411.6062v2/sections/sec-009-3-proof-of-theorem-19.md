---
doc_id: arxiv-1411.6062v2
doc_title: "EV ALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-009-3-proof-of-theorem-19
section_title: "Proof of Theorem 1.9"
section_number: 3
pages: 13-16
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quant um diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨ uller t"
---
We start by taking the logarithmic derivative of Faddeev’s quantum d ilogarithm
∂
∂x log Φ b(x) =
∫
R+iǫ
−2ie−2ixz
4 sinh(zb) sinh(zb−1) dz(60)
=
∫
R+iǫ
e−2ixz
2i sinh(zb) sinh(zb−1) dz
=
∫
R+iǫ
πse−2πisxz
2i sinh(πz bs) sinh(πz b−1s) dz
=
∫
R+iǫ
πse−2πisxz
2i sinh(πzM ) sinh(πzN ) dz .
After rescaling x↦→ x
2πs we obtain
(61) 4 i ∂
∂x log Φ b
( x
2πs
)
=
∫
R+iǫ
e−ixz
sinh(πzM ) sinh(πzN ) dz .
The integrand in ( 61), given by the function
(62) f( z) = e−ixz
sinh(πzM ) sinh(πzN )
satisﬁes Equation ( 26) with a = i as a direct consequence of the equalities
(63) f(z± i)
f(z) = (−1)M +N e±x .
Equation ( 27) and an application of Cauchy’s residue theorem implies that
2
π
(
1− (−1)M +N ex) ∂
∂x log Φ b
( x
2πs
)
= 1
2πi
(∫
R+iǫ
−
∫
R+i(1+ǫ)
)
f(z) dz
= S1(z) + S2(z) + S3(z) ,(64)
where
S1 =
M −1∑
m=1
Resz=i m
M
f(z), S 2 =
N −1∑
n=1
Resz=i n
N
f(z), S 3 = Res z=i f(z) .
So, we have reduced the integrals to the sum of residues. Our next task is to calculate each
residue. Let us introduce Ci for i = 1, 2, 3 by:
C1 =
(
1− ex+πi(M +N )) M −1
2M
DM (e(x+πi(M +N ))/M; e2πiN/M)
C2 =
(
1− ex+πi(M +N )) N−1
2N
DN (e(x+πi(M +N ))/N; e2πiM/N )
C3 =
(
1− (−1)M +N ex) ix
2π s2
e
i
2π s2 Li2((−1)M +N ex) .
14 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
Lemma 3.1. For i = 1, 2, 3 we have:
(65) Si = 2
π
(
1− (−1)M +N ex) ∂
∂x log Ci .
Proof. First we compute S1. Expanding in powers of z around z = 0, we have
(66) f
(
z + i m
M
)
= (−1)memx/M
πzM i sin(πmN/M ) (1 + O(z)) = (−1)memx/M
πzM i sin(πmN/M ) + O(1)
so that
Resz=i m
M
f(z) =
(
−ex/M) m
πiM sin(πmN/M ) = 2
(
−ex/M) m
πM (eπimN/M− e−πimN/M)
=−2
(
−e(x+πiN )/M) m
πM (1− e2πimN/M) =−2em(x+πi(M +N ))/M
πM (1− e2πimN/M) .
Now, by using Lemma 3.2 (see below), we calculate
− π
2
M −1∑
m=1
Resz=i m
M
f(z) = M −1
M −1∑
m=1
em(x+πi(M +N ))/M
1− e2πimN/M
= M− 1
2M ex+πi(M +N ) +
(
1− ex+πi(M +N )) ∂
∂x log DM
(
e(x+πi(M +N ))/M; e2πiN/M)
.
Finally observe that
−
∫ x
−∞
ey+πi(M +N )
(1− ey+πi(M +N )) dy = log
(
1− ex+πi(M +N ))
This proves Equation ( 65) for i = 1. Interchanging M with N proves Equation ( 65) for
i = 2. Finally we compute S3. Expanding in powers of z around z = 0, we have
(−1)M +N e−x f(z + i) = f( z) = 1− ixz + O(z2)
πzM (1 + O(z2))πzN (1 + O(z2))
= 1− ixz + O(z2)
π 2M N z2 = 1
π 2s2z2− ix
π 2s2z + O(1)
so that
Resz=i f(z) = (−1)1+M +N ixex
π 2s2 .
Now we calculate
2πis2 log C3 =
∫ x
−∞
(−1)M +N yey dy
1− (−1)M +N ey =−
∫ x
−∞
y d log
(
1− (−1)M +N ey)
=−
[
y log
(
1− (−1)M +N ey)] x
−∞ +
∫ x
−∞
log
(
1− (−1)M +N ey)
dy
=−x log
(
1− (−1)M +N ex)
+
∫ (−1)M +N ex
0
log(1− z)
z dz
=−x log
(
1− (−1)M +N ex)
− Li2
(
(−1)M +N ex)
.
Equation ( 65) follows for i = 3. □
EV ALUATION OF STATE INTEGRALS AT RATIONAL POINTS 15
We now ﬁnish the proof of Theorem 1.9. Using
(67) lim
x→−∞
Φ b(x) = 1
it follows that
(68) log Φ b
( x
2πs
)
=
∫ x
−∞
∂
∂y log Φ b
( y
2πs
)
dy
Combining the above with Equation ( 64) and Lemma 3.1, we obtain that
(69) Φ b
( x
2πs
)
= C1C2C3
Introduce a new variable z related to x by
(70) x
2πs = z
2πs− cb .
In other words, we have
(71) x = z− πi(M + N) .
Equation (
68) implies that
(72) Φ b
( z
2πs− cb
)
DN (ez/N; q+) DM (ez/M ; q−)e− i
2π s2 Li2(ez)
= (1− ez)
M −1
2M + N−1
2N + i(z−π i(M +N))
2πM N = (1− ez)1+ iz
2πM N .
This concludes the proof of Theorem 1.9. □
Lemma 3.2. For any complex root of unity q of order M, we have
(73)
M −1∑
m=1
xm
1− qm = M− 1
2 xM + (1− xM )x ∂
∂x log DM (x; q).
Proof. We calculate
(1− xM )x ∂
∂x log DM (x; q) = (1− xM )x ∂
∂x
M −1∑
m=1
m
M log(1− xqm)
=−(1− xM )x
M
M −1∑
m=1
mqm
1− xqm =− x
M
M −1∑
m=1
mqm(
1− (xqm)M)
1− xqm
=− x
M
M −1∑
m=1
mqm
M −1∑
n=0
(xqm)n =− 1
M
M −1∑
n=0
xn+1
M −1∑
m=1
mqm(n+1)
=− 1
M
M∑
n=1
xn
M −1∑
m=1
mqmn =−M− 1
2 xM− 1
M
M −1∑
n=1
xn
M −1∑
m=1
mqmn .
To ﬁnish the proof, we do the ﬁnal calculation
(74)
M −1∑
m=1
mqmn = t ∂
∂t
M −1∑
m=1
tm
⏐
⏐
⏐
⏐
⏐
t=qn
= t ∂
∂t
(1− tM
1− t − 1
) ⏐
⏐
⏐
⏐
t=qn
=−M tM
1− t
⏐
⏐
⏐
⏐
t=qn
= −M
1− qn .
16 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
□
