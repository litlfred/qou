---
doc_id: zagier-the-dilogarithm-function
doc_title: "The dilogarithm function"
section_id: sec-038-2-x-and-the-corresponding-higherp-adic
section_title: "(x), and the corresponding higherp-adic"
section_number: 2
pages: 29-31
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
doc_brief: "The dilogarithm function — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
---
polylogarithms Li(p)
m (x), have good properties of analytic continuation and are
related top-adicL-functions [11]. Furthermore, thep-adic dilogarithm andp-
adic polylogarithms have modiﬁed versions analogous to the Bloch-Wigner
dilogarithm and Bloch-Wigner-Ramakrishnan polylogarithms which satisfy
the same “clean” functional equations as their complex counterparts [41].
Finally, instead of working over thep-adic numbers we can work over the
ﬁnite ﬁeld F
p and consider the ﬁnite sum
£2(x)=£ (p)
2 (x)=
∑
0<n<p
xn
n2 , (15)
32 Don Zagier
a polynomial with coeﬃcients in Fp. The corresponding analogue £1(x)=∑p−1
n=1xn/n of the 1-logarithm was ﬁrst proposed (under the name “The 1 1
2 -
logarithm”) by M. Kontsevich in a note in the informal Festschrift prepared
on the occasion of F. Hirzebruch’s retirement as director of the Max Planck
Institute for Mathematics in Bonn [23]. Kontsevich showed that this function,
as a function from Fp to Fp, satisﬁes the 4-term functional equation
£1(x +y)=£ 1(y)+( 1 −y)£1
( x
1−y
)
+ y £1
(
−x
y
)
(16)
(the mod p analogue of the “fundamental equation of information theory”
satisﬁed by the classical entropy function−xlogx− (1−x) log(1−x)), mid-
way between the 3-term functional equation of log(xy)− log(x)− log(y)=0
of the classical logarithm function and the 5-term functional equation of
the classical dilogarithm, and also that £1 is characterized uniquely by this
functional equation together with the two one-variable functional equations
£1(x)= £1(1−x)a n dx£1(1/x)= −£1(x). Kontsevich’s question whether
the higher polylogarithm analogues £m(x)= ∑p−1
n=1xn/nm satisﬁed similar
equations was taken up and answered positively by Ph. Elbaz-Vincent and
H. Gangl [14]. They called these functions “polyanalogs”, an amalgam of the
words “analogue,” “polylog,” and “pollyanna” (an American term suggesting
exaggerated or unwarranted optimism). Presumably the correct term for the
case m = 2 would then be “dianalog”, which has a pleasing British ﬂavo(u)r.
The main property of the dianalog and its higher-order generalizations,
generalizing the identities found by Kontsevich for m = 1, is that if we con-
sider them as functions from F
p to Fp (rather than as polynomials with co-
eﬃcients in Fp) they satisfy functional equations which are reminiscent of,
but of a somewhat diﬀerent type than, the functional equations of the clas-
sical polylogarithms. In particular, Elbaz-Vincent and Gangl proved that the
dianalog function satisﬁes several functional equations: the easy symmetry
property £
2(x)= x£2(1/x), the somewhat less obvious three-term relation
£2(1−x)− £2(x)+x£ 2(1− 1/x) = 0, and the “Kummer-Spence analogue”
£2(xy)+ y £2
(x
y
)
− (1 +y)£2(x)− (1 +x)£2(y)
−(1−y)
[
£2
( y(x− 1)
1−y
)
− £2
( 1−x
1−y
)]
−x(1−y)
[
£2
( y(1−x)
x(1−y)
)
− £2
( x− 1
x(1−y)
)]
=0 ,
each of which is the analogue of a classical functional equation of the trilog-
arithm. There is also a 22-term functional equation based on Cathelineau’s
diﬀerential version of the trilogarithm. Moreover, in each of the functional
equations for £
1 and £2, if one replaces the polynomial factors preceding the
polyanalogs (for instance, the factors 1−y andy preceding £1(x/(1−y)) and
£1(−x/y) in (16)) by theirpth powers, then the functional equation becomes
The Dilogarithm Function 33
true as an identity between polynomials inFp[x,y ] and not merely as an equal-
ity between functions from Fp× Fp to Fp. Finally, by passing via thep-adics
and using a recent result of Besser [4] expressing the polyanalogs (now again
considered as functions rather than polynomials) as the mod p reductions
of certain derivatives of modiﬁedp-adic polylogarithm functions, the authors
show how functional equations of the mth classical complex polylogarithm
induce by a process of diﬀerentiation corresponding functional equations of
the (m− 1)-st polyanalog. The whole story is intimately related to Cathelin-
eau’s theory of inﬁnitesimal polylogarithms (inﬁnitesimal or Lie version of the
Bloch group), which is yet another and even more subtle manifestation of the
world of polylogarithms.
We do not give any further details, referring the reader to the original
papers [8] and [14].
