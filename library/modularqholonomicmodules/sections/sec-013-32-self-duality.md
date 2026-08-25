---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-013-32-self-duality
section_title: "Self duality"
section_number: 3.2
pages: 25-28
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
ﬁnite sum of products of solutions of the module M associated to Equations (111) and its
dualM∧ (see Section 2.5 for the deﬁnitions of the two duals). To prove modularity we must
factorise the state integral as a ﬁnite sum of products of solutions of M and M∨. To do
so, we need to give an explicit isomorphism between M∨ and M∧. This is the content of
the following proposition, which after some change of variables, is equivalent to Beukers–
Jouhet [8, Thm.1.3]. For completeness, we will give an independent proof using the methods
of our paper.
Proposition 3.1. [8, Thm.1.3] If M is the module associated to Equations (111) then
M∨∼=M∧. (117)
Explicitly, there exists Q(t,a,b,q )∈GLr(Q (t,a,b,q )) such that
Q(qt,a,b,q )A(qt,a,b,q −1)−1 =A(t,a,b,q )−TQ(t,a,b,q ). (118)
In addition, Q satisﬁes
U(t,a,b,q )−T =Q(t,a,b,q )U(t,a,b,q −1)diag(1,−1,−1,..., −1). (119)
Proof. To prove Equation (118) let
(1−q−1b1)... (1−q−1br−1)P (t,a,b,q )
=


1−t 0 0 ... 0
0 −(e2(b/q)−q−1te2(a)) e3(b/q)−q−2te3(a) ... (−1)r−1(er(b/q)−q−r+1ter(a))
0 ( e3(b/q)−q−1te3(a)) −(e4(b/q)−q−2te4(a)) ... 0
: : : ... :
0 ( −1)r−1(er(b/q)−q−1ter(a)) 0 ... 0


.
(120)
26 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
Using the fact that ek(λx) =λkek(x), one can then see that
(1−q−1b1)... (1−q−1br−1)P (qt,a,b,q )A(qt,q−1a,q−2b,q−1)−1
= (1−q−1b1)... (1−q−1br−1)A(t,a,b,q )−TP (t,a,b,q )
=


e1(b/q)−te1(a) −(e2(b/q)−q−1te2(a)) ... (−1)r−1(er(b/q)−q−r+1ter(a))
−(e2(b/q)−te2(a)) e3(b/q)−q−1te3(a) ... 0
: : ... :
(−1)r−1(er(b/q)−ter(a)) 0 ... 0

 .
(121)
Now notice that the second and third Equations (111) give gauge equivalences between the
modules in t thinking of a,b as constants when we shift aj↦→qaj and bi↦→qbi. Therefore,
multiplyingP by these gauge equivalences gives the desiredQ. Now to prove Equation (119)
we note that, from Equation (118)
E(t,a,b,q ) :=U(t,q−1a,q−2b,q−1)−1P (t,a,b,q )−1U(t,a,b,q )−T (122)
is an elliptic function. However,
H(t,a,b,q ) := diag
(θ(q−2bit;q)
θ(q−1t;q)
)−1
E(t,a,b,q ) diag
(θ(q−1bit;q)
θ(t;q)
)
(123)
is holomorphic at t = 0. Therefore, we see that
Hi,j(t,a,b,q ) =−tθ(q−1bj−1t;q)
θ(q−2tbi−1;q)Ei,j(t,a,b,q ) (124)
is holomorphic. This implies that if i⁄=j that Ei,j(t,a,b,q ) has at most has simple poles at
q∈b−1
j−1qZ and must have zeros at t∈b−1
i−1qZ and there is no such non-zero elliptic function
and therefore Ei,j(t,a,b,q ) = 0. Then notice that
Hii(t,a,b,q ) =−tθ(q−1bi−1t;q)
θ(q−2tbi−1;q)Ei,i(t,a,b,q ) =qb−1
i−1Ei,i(t,a,b,q ) (125)
is holomorphic at t = 0 and so as Ei,i(t,a,b,q ) is also elliptic in t it is constant in t. Now
notice that
lim
t→0
U (t,q−1a,q−2b,q−1)diag
(θ(q−2bit;q)
θ(q−1t;q)
)
=


1 1 ... 1
1 qb−1
1 ... qb −1
r−1
: : ... :
1 ( qb−1
1 )r−1 ... (qb−1
r−1)r−1




1 0 ... 0
0 B1(q−1a,q−2b,q−1) ... 0
: : ... :
0 0 ... B r−1(q−1a,q−2b,q−1)


(126)
and
lim
t→0
diag
(θ(q−1bit;q)
θ(t;q)
)−1
U(t,a,b,q )T
=


1 0 ... 0
0 B1(a,b,q ) ... 0
: : ... :
0 0 ... B r−1(a,b,q )




1 1 ... 1
1 qb−1
1 ... (qb−1
1 )r−1
: : ... :
1 qb−1
r−1 ... (qb−1
r−1)r−1

 .
(127)
Then using the fact that
r∑
j=0
(−1)jej(b/q)ρj = (1−ρ)(1−q−1b1ρ)... (1−q−1br−1ρ) (128)
MODULAR q-HOLONOMIC MODULES 27
vanishes at ρ∈{qb−1
i } we can show the matrix
r∏
k=1
(1−q−1bk)


1 1 ... 1
1 qb−1
1 ... (qb−1
1 )r−1
: : ... :
1 qb−1
r−1 ... (qb−1
r−1)r−1

P (t,a,b,q )


1 1 ... 1
1 qb−1
1 ... qb −1
r−1
: : ... :
1 ( qb−1
1 )r−1 ... (qb−1
r−1)r−1


(129)
has (i + 1,j + 1)-th entry
r−1∑
k=0
(−1)jej(b/q)(qb−1
j )k
r−1−k∑
𝓁=0
(bib−1
j )𝓁
=δi,j(1−b0/bj)... (1−bj−1/bj)(1−bj+1/bj)... (1−br−1/bj)
(130)
where we have used the fact that
r−1∑
k=0
(−1)jej(b/q)xk
r−1−k∑
𝓁=0
(xy−1)𝓁 =
r−1∑
k=0
(−1)jej(b/q)xk 1− (xy−1)r−k
1−xy−1
= 1
1−xy−1
(
(1−x)(1−q−1b1x)... (1−q−1b2x)−xry−r(1−y)(1−q−1b1y)... (1−q−1b2y)
)
.
(131)
Therefore, with the convention that ( x;q−1)∞ = (qx;q)−1
∞ and (q−1;q−1)∞ = (q;q)−1
∞ when
|q|< 1, for j >0
Bj(a,b,q )Bj(q−1a,q−2b,q−1)
=−q−1bj
(1−q−1b1)... (1−q−1br−1)
(1−q/bj)(1−b1/bj)... (1−bj−1/bj)(1−bj+1/bj)... (1−br−1/bj)
(132)
and we see that

E1,1(t,a,b,q ) 0 0 ... 0
0 qb−1
1 E2,2(t,a,b,q ) 0 ... 0
: : : ... :
0 0 0 ... qb −1
r−1Er,r(t,a,b,q )


= lim
t→0
H(t,a,b,q ) =


1 0 0 ... 0
0 −qb−1
1 0 ... 0
: : : ... :
0 0 0 ... −qb−1
r−1


(133)
Therefore, again using the gauge equivalence in the second and third Equations (111) com-
plete the proof. □
Remark 3.2. When r = 2, Proposition 3.1 is equivalent to the identity [38, Eqn.(1.4.3)]
2φ1(a,b ;c;q,t ) = (abc−1t;q)∞
(t;q)∞
2φ1(ca−1,cb−1;c−1;q,abc−1t) (134)
where we note that the ratio of Pochhammers is related to the determinant of U. This is
the q-analogue of Euler’s transformation formula for 2F1 [38, Eqn.(1.4.2)]
2F1(a,b ;c;t) = (1−t)c−a−b
2F1(c−a,c−b;c;t) (135)
28 STA VROS GAROUF ALIDIS AND CAMPBELL WHEELER
where
rFr−1(a;b;t) =
∞∑
k=0
(a1)k... (ar)k
(b1)k... (br−1)k
tk
k!. (136)
Remark 3.3. The q → 1 limit of Proposition 3.1 is discussed in full generality in [8,
Thm.1.1], where it is shown that the dual of the module associated to rFr−1(a;b;t) is the
module associated to rFr−1(1−a; 2−b;t).
