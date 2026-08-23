---
doc_id: s0025-5718-07-02027-3
doc_title: "Li(p)-service? An algorithm for computing p-adic polylogarithms"
section_id: sec-002-acknowledgments
section_title: "Acknowledgments"
section_number: null
pages: 2-6
source_pdf: S0025-5718-07-02027-3.pdf
source_sha256: 080b5ac8542ff19c
doc_brief: "Li(p)-service? An algorithm for computing p-adic polylogarithms — We describe an algorithm for computing Coleman’s p-adic poly- logarithms up to a given precision."
---
tute for a productive stay during the autumn of 2002, during which this paper
germinated and a ﬁrst version of an implementation of the algorithm was written.
He would also like to thank the University of Alberta and the Tata Institute of
Fundamental Research for very productive visits, and the EC network Arithmetic
Algebraic Geometry for travel support. He is grateful to Nils Bruin for sharing his
magic in order to overcome some aspects of programming in MAGMA and to Karim
Belabas for his comments on the last section of the paper and the implementation
of the algorithm. Finally, both authors would like to thank the referee for making
various suggestions for improving the paper.
2. The p-adic polylogarithm
A precise deﬁnition of Coleman integration is beyond the scope of the present
paper. Fortunately, in the case of p-adic polylogarithms there is a certain simpliﬁ-
cation that is suﬃcient for the computations that we give here.
Let p be a prime. Recall that the ﬁeld of p-adic complex numbers, C
p,i st h e
completion of the algebraic closure of the ﬁeld of p-adic numbers Qp.W e l e t|·|
be the absolute value on Cp, normalized such that |p| = p−1. It corresponds to
the valuation vp normalized by vp(p) = 1. The residue ﬁeld of Cp is the algebraic
closure of the ﬁeld with p elements,
 Fp.
We consider the projective line X = P1(Cp). A standard open disc in X with
centre a in Cp and radius r is the subsetD(a, r)= {z ∈ X || z −a| <r }. A standard
annulus with centre a in Cp is a subset of the form A(a, s, r)= {z ∈ X | s<
1There is a technical condition, satisﬁed for almost all primes, that we ignore here for the sake
of exposition. See the introduction of [5], in particular Theorem 1.10.
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1107
|z − a| <r }. Rigid analytic functions on D(a, r)a r ep o w e rs e r i e s∑ ∞
i=0 bi(z − a)i
that converge on D(a, r), and rigid analytic functions on A(a, s, r)a r eL a u r e n t
series ∑ ∞
i=−∞ bi(z − a)i that converge on A(a, s, r). For a = ∞ we take D(∞,r )=
{z ∈ Cp || z| > 1/r}∪{ ∞ }, and rigid analytic functions on it are power series in 1/z
that converge on D(∞,r ). Similarly, A(∞,s ,r)= {z ∈ Cp | 1/s > |z| > 1/r},a n d
rigid analytic functions on it are Laurent series in 1/z that converge on A(∞,s ,r).
Deﬁnition 2.1. A branch of the p-adic logarithm is a group homomorphism
log : C∗
p → Cp
given by the usual power series log(1 +z)= z − z2/2+ z3/3 −··· when |z| < 1.
Remark 2.2. A branch of the p-adic logarithm is determined by specifying log( p)
in Cp, as follows. If vp(z)=0 ,t h e nz reduces to an element of
 F
∗
p and therefore zn
reduces to 1 for some positiven.T h e nl o g (zn) is independent of the branch as it is
determined by the power series given above, and log(z)=l o g (zn)/n, independent of
n. In general, if bvp(z)= a for integers a and b with b positive, then vp(zb/pa)=0
and log(z)= a log(p)/b +l o g (zb/pa)/b, independent of the choice of a and b.
We now once and for all ﬁx a branch of the p-adic logarithm. All constructions
that follow do depend on this choice in principle. (For the precise dependence of
the functions Lin(z) that we are about to describe on the choice of the branch of
the logarithm, we refer to Remark 7.4 or [5, Proposition 2.6].)
We deﬁne log-type functions on A(a, s, r) to be polynomials ∑ fi · (log(z − a))i
with respect to log(z − a)i f a ⁄= ∞ and polynomials ∑ fi · (log z)i with respect to
log z if a = ∞,w i t ht h efi rigid analytic functions on A(a, s, r). We let Olog(U)
denote the space of rigid analytic functions on U if U = D(a, r), and the space of
log-type functions on U if U = A(a, s, r). We diﬀerentiate functions formally, with
the rule that the derivative of log(z − a)i s1 /(z − a). It is a basic fact, and rather
easy to prove, that diﬀerentiation gives a surjective map from Olog(U)t oi t s e l f ,
with kernel consisting of the constants.
Consider now the system of diﬀerential equations
(2.3)
dLi1(z)= dz
1 − z,
dLin+1(z)=L i n(z)dz
z (n ≥ 1)
or, equivalently,
(2.4)
Li0(z)= z
1 − z,
dLin+1(z)=L i n(z)dz
z (n ≥ 0) .
The complex polylogarithms are deﬁned by the same system. It has singularities
at 0, 1 and ∞. It follows from the properties of the rings Olog(U) discussed before
that on each disc or annulusU not containing 0, 1 or∞, (2.3) or (2.4) can be solved
with Lin(z)i n Olog(U). In fact, such solutions on U are unique up to adding
cn−1 + cn−2
1! log z + ··· + c0
(n − 1)! logn−1 z
with cj in Cp corresponding to the constant of integration in (2.4) for n = j.
1108 AMNON BESSER AND ROB DE JEU
In particular, all such solutions are rigid analytic for all but three “residue discs”
Ua, consisting of those points in P1(Cp) reducing to the same point asa.T h et h r e e
residue discs for which this does not hold a priori are U0, U1 and U∞.O n U0 it is
well known (and immediate) that the series in (1.1) for z in Cp with |z| < 1a n d
n ≥ 0 satisfy the systems (2.3) and (2.4), and we shall in fact assume that the
Lin(z)o n U0 are given by those series. But on Ua with a =1o r ∞ the Lin(z)o n l y
belong to Olog(U)f o rU = Ua \{ a}.
Clearly, what has been said so far does not suﬃce to determine Lin(z) uniquely.
The real magic of Coleman’s theory is that there is a canonical way of choosing
solutions to diﬀerential equations such as in (2.3) (in general, unipotent diﬀerential
equations) using a principle known as Frobenius equivariance. As we mentioned
before, a general discussion of Coleman’s theory is beyond the scope of the present
work, but we explain what it means in the present context.
For this we also need the functions
(2.5) Li
(p)
n (z)=L i n(z) − 1
pn Lin(zp) ,
a priori deﬁned for z in Cp with zp ⁄= 1. They satisfy conditions similar to (2.4),
namely
(2.6)
Li(p)
0 (z)= z
1 − z − zp
1 − zp ,
dLi(p)
n+1(z)=L i (p)
n (z)dz
z (n ≥ 0) .
Theorem 2.7 (Coleman). For any branch of the p-adic logarithm there exists a
unique sequence of functions
Lin : P1(Cp) \{ 1, ∞} → Cp (n ≥ 0)
with the properties:
(1) the restrictions of the Lin to every residue disc U = Ua other than U1 and
U∞, and to the annuli U = U1 \{1} and U = U∞ \{ ∞ },b e l o n gt oOlog(U)
and satisfy (2.4);
(2) the restrictions of the Lin to U0 are given by the series (1.1);
(3) for each n ≥ 0 the function Li(p)
n (z) with Li(p)
n (∞)=0 extends to a function
on P1(Cp) \{ z in Cp with zp =1 } that on the set
(2.8) P1(Cp) \{ z in Cp with |z − 1|≤ p−1/(p−1)}
is given by a convergent power series in 1/(1 − z).
Moreover, Li(p)
n (z) on the set in (2.8) is independent of the branch of the logarithm.
Proof. We use [7]. The Li n(z) are deﬁned there in section VI (page 195) ex-
actly to satisfy (2.4) (the deﬁnition of Li 0(z) in loc. cit. is incorrect) as well as
limz→0 Lin(z) = 0. The fact that the polylogarithms belong to Olog(U) for all
residue discs but U0 is part of the properties of Coleman integration. Using induc-
tion on n it follows directly from the deﬁnition that Lin(z)o n U0 is given by (1.1),
hence lies in Olog(U0). The power series expansion of Li (p)
n (z) in (3) is Proposi-
tion 6.2 of loc. cit.
As for uniqueness, we ﬁrst notice that the power series expansion of Li(p)
n (z)w i t h
respect to 1/(1 −z) on the set in (2.8) is uniquely determined by (2.6) and its value
at ∞ (cf. Proposition 4.3 below). In particular, Li (p)
n (z) on this set is independent
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1109
of the branch of the logarithm. Assuming that, on each residue discU,L in−1(z)i n
Olog(U) has already been determined, the diﬀerential equation in (2.4) determines
Lin(z) up to a constant. Therefore Li n(z) is determined up to adding a function
C(z) that is constant on each U. Since the set in (2.8) intersects every U we have
that C(z) − C(zp)/pn = 0. Because z and zpf
lie in the same residue disc for some
f> 0 this implies that C is the zero function. □
Remark 2.9. (1) The characterisation of Li n(z) in Coleman’s theory is diﬀerent,
and requires the full force of this theory to explain.
(2) The part of P1(Cp) that has to be removed in part (3) of Theorem 2.7 is the
disc around 1 that contains all the singularities of the diﬀerential equation satisﬁed
by Li(p)
n (z) except for 0 and ∞, i.e., the p-th roots of unity. The convergence of
the power series in 1/(1 − z) on the indicated domain implies a growth condition
on its coeﬃcients. We will in fact deduce, by explicit computation, a more precise
growth condition on these coeﬃcients (see Proposition 6.1).
(3) In Remark 7.4 below we shall show that Lin(z)o n Ua depends on the branch
of the logarithm only when a =1 , ∞, and make explicit this dependence (cf. [5,
Proposition 2.6]).
We will need some further results about Lin(z).
Proposition 2.10. (1) For m ≥ 1 and z in Cp with zm ⁄=1 ,
Lin(zm)= mn−1 ∑
ζm =1
Lin(ζz);
(2) Li n(z)+( −1)nLin(z−1)= − 1
n! logn(z).
Proof. Those are (the correct version of) Proposition 6.1 and Proposition 6.4(i)
of [7]. □
3. Method of computation on U0 and U∞
On U0 we can use the standard expansion in (1.1),
(3.1) Li n(t)=
∞∑
k=1
tk
kn ,
which we shall denote by Fn,0(t).
Remark 3.2. As an immediate consequence of the power series expansion of Lin(z)
on U0 and the deﬁnition of Li(p)
n (z) in (2.5) we see that on U0
(3.3) Li (p)
n (z)=
∑
k≥1
′zk
kn ,
where the prime indicates that we only sum over those k for which p⁄| k.W e c a n
collect terms zk/kn in Lin(z)= ∑
k≥1
zk
kn for which vp(k)= m and ﬁnd that
(3.4) Li n(z)=
∑
m≥0
Li(p)
n (zpm
)
pmn
as well.
1110 AMNON BESSER AND ROB DE JEU
For the disc U∞ we use that
Lin(z)+( −1)nLin(1/z)= − 1
n! logn(z)
as in part (2) of Proposition 2.10. This reduces the calculation of Lin(z)t ot h a to f
Lin(1/z), with 1/z in U0, and that of log(z).
