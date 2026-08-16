---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-030-322-t-refoil
section_title: "T refoil"
section_number: 3.2.2
pages: 34-36
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
Our next task is to derive reﬁned recursion relations for the trefoil. Similarly as in the unknot
case, we will be able to determine these relations from the structure of thesl(2) specialization
Pn(T 2,3;q,t ) of the colored superpolynomial. For general (2, 2p + 1) torus knots, we found an
explicit expression for this homological invariant in (3.9 7), which for the present purpose of
deriving recursion relations we write in the form 7
Pn(T 2,3;q,t ) =
n−1∑
k=0
P (n,k ), (3.113)
where each P (n,k ) has a product structure
P (n,k ) =qn−1+nkt2k
k∏
i=1
(1 −qn−i)(1 +qit)
1 −qi . (3.114)
In particular
P (n, 0) =qn−1, P (n,n ) = 0. (3.115)
Note that for t = −1 simpliﬁcations occur and only one set of products remains i n (3.114).
To derive recursion relations let us write down the followin g ratios, which is immediate
due to the product structure of P (n,k ):
P (n + 1,k )
P (n,k ) = qk+1 1 −qn
1 −qn−k, (3.116)
P (n,k + 1)
P (n,k ) = qnt2 (1 −qn−k−1)(1 +qk+1t)
1 −qk+1 , (3.117)
P (n + 1,k + 1)
P (n,k ) = qn+k+2t2 (1 −qn)(1 +qk+1t)
1 −qk+1 . (3.118)
7The equivalence between this expression and (3.97) can be ea sily veriﬁed to suﬃciently large n. Plus, both
expressions enjoy the structural properties discussed in 3 .1.3.
– 33 –
These equations are equivalent to the following ones (obtained by clearing the denominators):
qkP (n + 1,k ) −qnP (n + 1,k ) = (1 −qn)q2k+1P (n,k ), (3.119)
qkP (n,k + 1) −qn+kt2(1 −qnt)P (n,k )
= −q2n−1t2P (n,k ) + q2k+1
(
P (n,k + 1) +t3qnP (n,k )
)
,(3.120)
P (n + 1,k + 1) −t3qn+2k+3(1 −qn)P (n,k )
=qk+1
(
P (n + 1,k + 1) + t2qn+1(1 −qn)P (n,k )
)
. (3.121)
These are linear equations in P (n,k ) (possibly with shifted arguments n or k). Therefore,
ideally, we would like to perform the sum over k as in (3.113) to transform them into equa-
tions for various Pn (possibly with shifted n’s). However such summation cannot be directly
performed because of k-dependent factors qk andq2k. Nonetheless, we can take these factors
into account at the expense of introducing auxiliary quanti ties:
Rn =
n−1∑
k=0
qkP (n,k ), S n =
n−1∑
k=0
q2kP (n,k ). (3.122)
Now resummation of (3.119)-(3.121) can be performed and the answer written in terms ofPn,
Rn, and Sn. Note that because of shifts in n we need to take care of some boundary terms
arising in various cases for k = 0 or k = n. However all such boundary terms ultimately
cancel and we get the following system of equations:
Rn+1 +aPn+1 = bSn, (3.123)
cRn +dPn = eSn, (3.124)
Pn+1 −Rn+1 +fR n = gSn, (3.125)
where
a = −qn, b =q(1 −qn), c =q−1 −t2qn(1 −qnt), d =t2q2n−1, (3.126)
e =q−1 +t3qn+1, f = −t2qn+2(1 −qn), g =t3qn+3(1 −qn).
Now we can determine Sn from the ﬁrst equation and substitute to the remaining two eq ua-
tions. This gives a system of two equations, which allows to d etermineRn andRn+1 in terms
of Pn and Pn+1:
Rn = −d(b +g)Pn + (1 +a)ePn+1
bc −ef +cg , (3.127)
Rn+1 = −bdfPn + (bc +aef −acg)Pn+1
bc −ef +cg . (3.128)
Finally we notice that Rn is related to Rn+1 simply by a shift of n by one unit. Therefore,
shifting the second equation above and comparing with the ﬁr st one we get a homogeneous,
– 34 –
3-term recursion relation
αPn−1 +βPn +γPn+1 = 0 , (3.129)
where
α = q3n−1(qn −q)t4
(q +q2nt3)(1 +qn+1t3), (3.130)
β = − t2
q−2n +qt3 − q −qn+1t2 +q4nt6 +q2nt2(1 +t +qt)
(q +q2nt3)(1 +qn+1t3) , (3.131)
γ = 1
q +q2n+2t3. (3.132)
We can also rewrite the above relation in the operator form (2 .1a):
ˆAref(ˆx,ˆy;q,t )Pn(T 2,3;q,t ) = 0 . (3.133)
Here, as in (2.4), ˆy acts as a shift operator Pn → Pn+1 and ˆx acts by multiplication by qn,
so that ˆx andˆy obey the commutation relation ˆyˆx =qˆxˆy. Then, the relation (3.129) can be
expressed in terms of the reﬁned quantum A-polynomial
ˆAref(ˆx,ˆy;q,t ) = αˆy−1 +β +γˆy, (3.134)
with
α = x3(x −q)t4
q(q +x2t3)(1 +xqt3), (3.135)
β = − t2x2
1 +x2qt3 − q −xqt2 +x4t6 +x2t2(1 +t +qt)
(q +x2t3)(1 +xqt3) , (3.136)
γ = 1
q +x2q2t3. (3.137)
In what follows we analyse various limits of this relation. I n particular, we study the classical
limit q = 1 and the associated asymptotic structure of the sl2 colored polynomial, and
generalize these results to other (2 , 2p + 1) torus knots. The classical reﬁned A-polynomials
which we ﬁnd for other values of p provide an important guidance in generalizing the full
quantum relations (3.134) to other torus knots.
