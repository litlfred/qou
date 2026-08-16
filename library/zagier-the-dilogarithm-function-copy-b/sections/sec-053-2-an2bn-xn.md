---
doc_id: zagier-the-dilogarithm-function-copy-b
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-053-2-an2bn-xn
section_title: "An2+Bn x−n ="
section_number: 2
pages: 52-56
source_pdf: zagier-the-dilogarithm-function-copy-b.pdf
source_sha256: c584944a501ef0c5
doc_brief: "The Dilogarithm Function Don Zagier — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
duplicate_of: "zagier-the-dilogarithm-function"
---
√
i
Az
∞∑
n=−∞
e
(
− (u − Bz + n)2
2Az
)
,
The Dilogarithm Function 55
where q = e(z): = e2πiz , x = e(u). Hence we ﬁnd, for any u0 ∈ C,
FA,B(q)=
∫ u0+1
u0
θA,B(z, u)
(
e(u); q
) −1
∞ du
=
√
i
Az
∫
ℑ(u)=ℑ(u0)
e
(
− (u − Bz)2
2Az
) (
e(u); q
) −1
∞ du
= 1√
2πAε
∫
ℑ(t)=const
exp
(
− t2
2Aε +L i 2(qBeit; q)
)
dt .
where in the last line we have substituted u = Bz + t/2π. The derivative with
respect to t of the argument of exp equals [ A log(1 − eit) − it]/iAε + O(1),
which vanishes at it = log(1 − Q)+O ( ε), where Q is the solution between 0
and 1 (or, of course, any other solution) of Nahm’s equation 1 − Q = QA.N o w
moving the path of integration to a neighbourhood of this point and applyi ng
the method of stationary phase (saddle point method), we obtain the des ired
asymptotic expansion for FA,B
(
e−ε)
. This method has the further advantage,
as explained in Nahm’s paper, that the contributions from the further s addle
points could in principle be used to describe all the terms of the q-expansion
of fA,B,C (−1/z) in the cases when fA,B,C is a modular function.
As already mentioned, one can also do an almost exactly similar calculation
using the power series expansion (7) rather than (8), at least if A> 1: we now
write
FA,B(q)= Cx0
[( ∞∑
n=−∞
(−1)n q
A−1
2 n2+(B+ 1
2 )n x−n
)( ∞∑
n=0
(−1)n q
n2−n
2
(q)n
xn
)]
=
∫ u0+1
u0
√
i
(A − 1)z
∑
n∈Z
e
( (u − (B + 1
2 )z + n + 1
2 )2
2(A − 1)z
) (
e(u); q
)
∞ du
= 1√
2π(A − 1)ε
∫
ℑ(t)=const
exp
(
− t2
2(A − 1)ε − Li2(−qB+ 1
2 eit; q)
)
dt ,
and again an asymptotic expansion could now be obtained by the saddle point
method. I have not carried out the details.
This completes our discussion and proof of Proposition 5. We remark that
each of the methods described applies also to r> 1, and we again ﬁnd an
expansion of log FA,B(q) of the form (35), with leading coeﬃcient given by
c−1(A, B)=
r∑
i=1
(
L(1) − L(Qi)
)
= rL(1) − L(ξA)= c(A)L(1) .
In particular, the modularity of fA,B,C (z) for any B ∈ Qr and C ∈ Q requires
that L(ξA) be a rational multiple of π2 and hence suggests very strongly that
ξA has to be a torsion element of B(Q(ξA)), as required by Nahm’s conjecture.
56 Don Zagier
The higher coeﬃcients are given by a formula essentially the same as i n the
case r = 1, except that the previous expression of the form I
[
H(u)
]( 1−Q
∆ε
)
with I
[]
deﬁned by equation (30) or (31) must now be replaced by its multi -
dimensional generalization
√
det~A
(2π)r/2
∫
Rr
exp
(
− ε
2 u~Aut)
H(u) du ∼
∞∑
n=0
(2ε)−n
n! ∆n
~AH(0),
where ~A is given by (30) and ∆~A denotes the Laplacian with respect to the
quadratic form u~Aut.
We now use the proposition to classify the modular fA,B,C when r =1 .
Theorem. The only (A, B, C) ∈ Q+ ×Q×Q for which fA,B,C (z) is a modular
form are those given in Table 1.
The basic idea of the proof is that, if f (z)= F (q) is a modular form
of weight k on some group Γ , then the function g(z)= z−kf (−1/z) is also
a modular form (on the group SΓS , where S =
( 0 −1
10
)
) and hence has an
expansion as z → 0o ft h ef o r ma0qn0 +a1qn1 +··· for some rational exponents
n0 <n 1 < ··· and non-zero algebraic coeﬃcients a0,a 1, ... . In particular
we have F
(
e−ε)
= f (iε/2π)=( 2 πi/ε)k a0 e−4π2n0/ε +O
(
ε−ke−4π2n1/ε)
and
hence log F
(
e−ε)
= −4π2n0ε−1 − k log ε + c +O ( εN ) for all N> 0a s ε
tends to 0, where c = log((2 πi)ka0). Comparing this with the expansion of
log FA,B,C
(
e−ε)
= log FA,B
(
e−ε)
− Cε as given in equation (35), we see that
if fA,B,C (z) is a modular form of weight k then
(i) the weight k must be 0 (i.e. fA,B,C (z) must be a modular function);
(ii) the number c−1(A, B)m u s tb e π2 times a rational number;
(iii) the number c0(A, B) must be the logarithm of an algebraic number;
(iv) the number c1(A, B) must be a rational number (namely, C); and
(v) the numbers cj(A, B) must vanish for all j ≥ 2.
The conditions (ii)–(iv) are useless for numerical work, since the r ationals lie
dense in R, but condition (v) gives inﬁnitely many constraints on the two real
numbers A and B and can be used to determine their possible values. This
approach was already used by Terhoeven in 1994 to prove a weaker version
of the theorem, namely, that the only values of A ∈ Q+ for which fA,0,C is
modular for some C ∈ Q are 1/2, 1 and 2. (See [36], where, however, the details
of the calculation are not given.) To do this, Terhoeven computed cj(A, B)u p
to j = 2 using the method (c) above, as developed in his earlier joint pape r [31].
If fA,0,C is to be modular for some C, then the number c2(A, 0) must vanish.
We have c2(A, 0) = P (A, Q)/(A + Q − AQ)6 for a certain polynomial P (A, Q)
with rational coeﬃcients (given after Proposition 5), where Q is the root
of Q + QA = 1 in (0,1). By looking at the graph of the function Φ(Q)=
P
( log(1−Q)
log Q) ,Q ) on the interval (0,1), we ﬁnd numerically that it has a simple
zero at Q1 =( 3 −
√
5)/2, a double zero at Q2 =1 /2, a simple zero at Q3 =
The Dilogarithm Function 57
(
√
5 − 1)/2, and no other zeros. Since P (Q1, 1
2 )= P (Q2, 1) = P (Q3, 2) = 0
and since Φ(Q)= Φ(1−Q), we know that there really are zeros of the speciﬁed
multiplicities at Q1, Q2 and Q3. It follows that they are the only zeros in this
interval and hence that fA,0,C can only be modular for the three values given
in Table 1.
To prove the full theorem we proceed in the same way, but since we now
have two variables A and B to determine we must use at least two coeﬃcients
cj(A, B). The functions c2(A, B)a n dc3(A, B) are polynomials in B of degree 3
and 4, respectively, whose coeﬃcients are known elements of Q(A, Q). For ﬁxed
A ∈ R+ the condition that the two polynomials c2(A, · )a n d c3(A, · )h a v ea
common zero is that their resultant vanishes. From the explicit form ulas for c2
and c3 we ﬁnd that this resultant has the form R(A, Q)/(A+Q−AQ)39 where
R(A, Q) is a (very complicated) polynomial in A and Q with rational coeﬃ-
cients. Now a graphical representation of the function Ψ (Q)= R
( log(1−Q)
log Q) ,Q )
on the interval (0,1) (which we can unfortunately not show here since t his
function varies by many orders of magnitude in this range and hence has to
be looked at at several diﬀerent scales on appropriate subintervals) sh ows that
it has nine zeros (counting multiplicities), namely:
a simple zero at Q0 =0 .196003534545184447085746160093577 ···
a double zero at Q1 =0 .3819660 ··· =( 3 −
√
5)/2
a triple zero at Q2 =0 .5000000 ··· =1 /2
a double zero at Q3 =0 .6180339 ··· =(
√
5 − 1)/2
a simple zero at Q4 =0 .803996465454815552914253 ··· =1 − Q0
and no other zeros. Since Ψ (1 − Q)= −Ψ (Q) and since we know from Table 1
that Ψ (Q) has to have at least a double zero at Q = Q1 and at Q = Q3
and a triple one at Q = Q2, we deduce that the numerically found zeros at
these places are really there and correspond to the known cases of modu larity.
As to the new value Q0 and Q4 =1 − Q0 and the corresponding A-values
A0 =0 .133871736816761609695060406707385 ··· and A4 = A−1
0 , we ﬁnd that
indeed c2(A0,B )a n d c3(A0,B ) have a (simple) common root at B = B0 =
−0.397053221675466369 ... , as they must since their resultant vanishes. But
for the pair ( A0,B 0) we ﬁnd numerically
c−1(A0,B 0)/π2 =0 .1277279468293881629887898 ···
which is (apparently) not a rational number,
exp(c0(A0,B 0)) = 3 .4660299497719132664077586 ···
which is (apparently) not algebraic,
c1(A0,B 0)=0 .4917635587907976876492549 ···
which is (apparently) not rational, and ﬁnally
c4(A0,B 0)=0 .0175273497972616555765902 ···
which is (deﬁnitely) not zero. It follows that the function fA0,B0,c1(A0,B0)(z)
is not modular and thus that the list given in Table 1 is complete. □
This analysis was quite tedious and would become prohibitively so for
r ≥ 2 (although the method applies in principle) because we would need
58 Don Zagier
explicit formulas for many more of the coeﬃcients cj(A, B). An alternative
approach might be to reﬁne Proposition 5 by showing that
log FA,B
(
ζe −ε)
∼
∞∑
j=−1
cj,ζ(A, B) εj (
ε ց 0
)
for every root of unity ζ.I f fA,B,C (z) is modular for some C ∈ Q, then the
logarithm of FA,B,C
(
ζe −ε)
= ζ Ce−CεFA,B
(
ζe −ε)
has vanishing coeﬃcient
of εj in its expansion at ε =0f o re v e r y j ≥ 1. In particular we must have
c1,ζ(A, B)= C for all roots of unity ζ with the same constant C,s ow eg e t
inﬁnitely many constraints on A and B without having to calculate any of the
Taylor expansions further than their O( ε) term. I have not yet tried to carry
this out, but it seems to hold out good prospects for an easier proof of the
r = 1 case and perhaps a reasonable attack on the higher rank cases of the
conjecture as well.
Finally, we remark that Proposition 5 (or its generalization to r> 1) can
be used to search eﬃciently for values of B for a given A for which fA,B,C may
be modular for some C. Indeed, since the function φ(ε) = log( FA,B(e−ε) must
have a terminating asymptotic expansion of the form c−1ε−1 +c0 +c1ε with an
error term that is exponentially small in 1 /ε, we can simply check whether four
successive values of nφ(α/n) (say, those with α =1a n d n =2 0, 21, 22, 23) are
approximated to high precision by a quadratic polynomial in n (i.e., whether
the third diﬀerence of this 4-tuple is extremely small). In fact, since we know
c−1 by (30), we can look instead at three sucessive values of nφ(α/n)−c−1n2/α
and check whether they lie on a line (i.e., whether their second d iﬀerence
vanishes) to high precision. This can be done very rapidly and theref ore we
can search through a large collection of candidate vectors B ∈ Qr for those
which can correspond to some modular fA,B,C . This is the method which was
used to ﬁnd the modular solutions for r = 2 amd 3 given in (d) and (e) of
subsection B.
