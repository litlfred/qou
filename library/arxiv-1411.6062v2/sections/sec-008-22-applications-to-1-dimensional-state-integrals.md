---
doc_id: arxiv-1411.6062v2
doc_title: "EV ALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-008-22-applications-to-1-dimensional-state-integrals
section_title: "Applications to 1-dimensional state-integrals: proof of Theorem 1.1"
section_number: 2.2
pages: 10-13
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quant um diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨ uller t"
---
section we prove Theorem 1.1. Fix integers A and B with B > A > 0. The values of
particular interest are ( A, B ) = (1 , 2) and (1 , 3) which correspond to the state-integrals of
the knots 4 1 and 5 2 respectively. For the 4 1 knot, see [ AK14, Eqn.38] and [ KL V12, Eqn.47]
and [GK]. For the 5 2 knot, see [KL V12, Eqn.53]. For the remaining values of ( A, B ), although
EV ALUATION OF STATE INTEGRALS AT RATIONAL POINTS 11
the 1-dimensional state integral makes sense, and it can be analyz ed using our methods, there
is no corresponding knot that we know of.
If
(51) f( z− cb) = Φ b(z)Be−Aπiz2
, c b = (b + b−1)i/ 2,
then
g(x) = (−x)A(1− x)−B(52a)
g±(x) = g( q±x)(52b)
g±
n(x; q±) = (−x)Anq
A
2 n(n+1)
± (q±x; q±)−B
n , ∀n∈ Z.(52c)
Observe that f( z) is non-vanishing and absolutely integrable along the line Cλ if
(53) − (M + N)/ 2 < λ < 0,
and f( z + si)⁄= f( z) if λ is in general position. By using (
25), we obtain that
f(z) = Φ b(z + cb)Be−Aπi(z+cb)2
(54)
= e
iB
2π s2 Li2(e2π sz ) (1− e2πsz)B+Bizs−1
/DN (e2πbz; q+)B /DM (e2πb−1z; q−)B e−Aπi(z+cb)2
.
By using the identity
e−Aπi(z+cb)2
= e−Aπi(cb+ i
2s)
2
eA(2πsz−πi)(1−4sicb−2siz)s−2/4
= eAπi (M +N+1)2
4M N eA(2πsz−πi)(1−4sicb−2siz)s−2/4
and ( 52a), we can rewrite ( 54) in the form
f(z) = e
iB
2π s2 R(e2π sz )(1−e2π sz )
(2N+1)(2M +1)
4M N B
/DN (e2πbz; q+)B /DM (e2πb−1z; q−)B eπi B+3A(M +N+1)2
12M N g
(
e2πsz) 1−4sicb−2siz
4s2 ,(55)
where R(x) is the Rogers dilogarithm (
8).
It is easy to see that the only singularities in Equation ( 42) are simple poles that come
from solutions to the equation 1 − g(e2πsz) = 1. Moreover, if z = α is a solution with
0 < s Imα− λ < 1, then
2πi Resz=α
f(z) S
(
e2πbz, e 2πb−1z
)
1− g(e2πsz) = i−1s−1
f(α ) S
(
e2πbα, e 2πb−1α
)
e2πsα g′ (e2πsα) .
Combining Lemma 2.3 with Equation ( 55) concludes the proof of Theorem 1.1. □
2.3. The case of the (−2, 3, 7) pretzel knot. The second author computed the state-
integral invariant of the ( −2, 3, 7) pretzel knot. The result of the long computation is the
following 1-dimensional state integral, which we take as input to our a nalysis:
(56) I(−2,3,7)(b) =
∫
/CA +iǫ
Φ b(x)2 Φ b(2x− cb)e−2πix2
dx
12 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
The integral is absolutely convergent, and the statement and pro of of Theorem
1.1 applies
using the following deﬁnition of the functions f( x), g ±
k(x, q ) and g( x):
f(x− cb) = Φ b(x)2 Φ b(2x− cb)e−2πix2
(57a)
g±
k(x, q ) = qk(k+1)x2k
(qx; q)2
k(qx2; q)2k
(57b)
g(x) = x2
(1− x)2(1− x2)2 .(57c)
Observe that f( z) is non-vanishing and absolutely integrable along the line Cλ if
(58) − (M + N)/ 4 < λ < 0,
and f( z + si)⁄= f( z) if λ is in general position.
We now discuss the solutions of the gluing equations g( x) = 1 and the matching with the
set of nonabelian parabolic PSL(2 ,
/BV ) representations, illustrating Remark 1.6.
The equation g( x) = 1 has 6 solutions that come from two cubic equations:
(59) z
(1− z2)(1− z) =±1 .
Each triple of solutions lies in number ﬁelds F+ and F− of discriminant−23 and 49 and type
[1, 1] and [3 , 0] respectively.
On the other hand, there are 6 nonabelian parabolic PSL(2 , /BV ) representations of the
(−2, 3, 7) pretzel knot. These may be found using the Ptolemy methods of [GGZ14] and
their snappy implementation [ CDW]. An alternative method is to use the A-polynomial of
the pretzel knot from [ Cul]
A(m, l ) = l6−l5m8+2l5m9−l5m10−2l4m18−l4m19+l2m36+2l2m37+lm45−2lm46+lm47−m55
Observe that A(1, l ) = ( l− 1)3(l + 1)3. Setting ( m, l ) = (1 + t,±1 + c±t + O(t2)) we obtain
that
−6119 + 2012c−− 220c2
− + 8c3
− = 0, −6193− 2020c+− 220c2
+− 8c3
+ = 0
Then, we have F± =
/C9 (c±). If z is a solution to ( 59), let ρz denote the corresponding
nonabelian parabolic PSL(2 , /BV ) representation. The Rogers dilogarithm of z agrees with the
complex volume of ρz, and g ′(x) agrees with the 1-loop invariant of ρz.
Incidentally, if z∈ F+, a totally real ﬁeld, then the corresponding triple of elements of th e
Bloch group is torsion and triple of complex volumes is given by
(
e
(
−19
42
)
, e
(
−13
42
)
, e
(11
42
))
= e
(
−19
42
)(
1, e
(1
7
)
, e
(
−2
7
))
,
where e(x) is given by Equation ( 20).
EV ALUATION OF STATE INTEGRALS AT RATIONAL POINTS 13
