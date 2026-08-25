---
doc_id: arxiv-2505.00799v2
doc_title: "QUANTUM MODULAR FORMS AND RESURGENCE"
section_id: sec-009-32-median-resummation
section_title: "Median Resummation"
section_number: 3.2
pages: 19-24
source_pdf: 2505.00799v2.pdf
source_sha256: cc9d2ab4c6c79b50
doc_brief: "QUANTUM MODULAR FORMS AND RESURGENCE — In 2010, Zagier described a new phenomenon which he called quantum mod- ularity."
---
g(z)∼φ−d/c(z) as z approaches−d/c∈ Q. For appropriate −d/c, we will prove decompo-
sitions of the form
(3.1) g(z) =Sπ/2
med(φ−d/c)(z) +
Z
Γ
e−u/(z+d/c)bgodd
−d/c(u)du√u,
where bgodd
−d/c(u) is a function related to g and the contour Γ is displayed in Figure 1. In
the first cases we will consider, we will show that the second term in the sum vanishes,
giving a median resummation result for these functions. In the latter cases, the situation is
more interesting, as the second term in the sum will contribute. The general approach for
the results in this section was inspired by similar work in [2, 20] for false theta functions of
weight 1/2.
Proposition 3.4. Suppose g is of Type 4 with respect to Γ0(N) or of Type 5, and suppose
γ = (a b
c d)∈ Γ0(N). Then g =Sπ/2
med(φ−d/c).
Proof. Let g(z) =P∞
n=0bnqn and suppose that g(z)∼φ−d/c(z) as z approaches−d/c∈ Q.
Now define bg−d/c(u) := 1√π
P∞
n=0bnζ−dn
c e−
√
8πinu. We will relate g andbg−d/c through Borel
resummation.
We will prove our result for z +d/c along the half-line iR+ and deduce the equalities
in Propositions 3.4 on H by holomorphicity. Using Gaussian integration, we have that for
ε> 0,
e2πin(z+d/c) = 1√π
p
8πi(z +d/c)
Z
iR+ε
e−√nηe−η2/8πi(z+d/c) dη.
20 ELEANOR MCSPIRIT AND LARRY ROLEN
Figure 1. The contour Γ.
Then we may write
∞X
n=1
bnqn =
∞X
n=1
bnζ−dn
c e2πi(z+d/c)
= 1√π
p
8πi(z +d/c)
Z
iR+ε
X
n≥1
bnζ−dn
c e−√nηe−η2/8πi(z+d/c) dη.
Under the change of variables η2/8πi =u, this becomes
∞X
n=1
bnqn = 1
2
p
z +d/c
Z
Γ
e−u/(z+d/c)
∞X
n=1
bnζ−dn
c e−
√
8πinu du√πu,
for the contour Γ displayed in Figure 1. Expanding bg−d/c(u) as a Puiseux series supported
on half-integer powers, we have
(3.2) bg−d/c(u) = 1√π
X
n≥1
bnζ−dn
c e−
√
8πinu∼ 1√π
∞X
r=0
(−1)rL(g,ζ−d
c ;−r/2)
Γ(r + 1) (8πiu)r/2.
We split this series based on whether r is even or odd. We write
bgeven
−d/c(u) := 1√π
∞X
n=0
L(g,ζ−d
c ;−n)
Γ(2n + 1) (8πiu)n;
1√ubgodd
−d/c(u) :=− 1√π
∞X
n=0
L(g,ζ−d
c ;−n− 1/2)
Γ(2n + 2) (8πi)n+1/2un.
Since in both cases, we assume a functional equation of degree 2 for some L-function re-
lated to L(g,ζ−d
c ;ρ) by a shift, both of the above power series converge absolutely in some
neighborhood of u = 0. Moreover, since Γ(n + 1)Γ(n + 1/2) =
√π
4n Γ(2n + 1), we see that
B1/2(φ−d/c(z)) = 1√π
∞X
n=0
L(g,ζ−d
c ;−n)
Γ(2n + 1) (8πiu)n =bgeven
−d/c(u).
QUANTUM MODULAR FORMS AND RESURGENCE 21
Then the above allows us to write
∞X
n=1
bnqn = 1
2
p
z +d/c
Z
Γ
e−u/(z+d/c)B1/2(φ−d/c(z)) du√πu +
Z
Γ
e−u/(z+d/c)bgodd
−d/c(u)du√u

.
By deforming contours, we have
Z
Γ
e−u/(z+d/c)B1/2(φ−d/c) du√πu =
 Z ei(π
2−ε)∞
0
+
Z ei(π
2 +ε)∞
0
!
e−u/(z+d/c)B1/2(φ−d/c) du√πu,
noting that the integrand changes sign whenu circles the origin. This shows that this integral
is the median resummation with φ−d/c of angle π/2.
To prove Proposition 3.4, it then suffices to show that in the given cases,
(3.3) 1
2
p
z +d/c
Z
Γ
e−u/(z+d/c)bgodd
−d/c(u)du√u = 0.
We will treat both cases separately.
First, suppose that g is the Eichler integral of a cusp form f of weightk∈ 1
2 + Z on Γ0(N)
where 4 | N. Then bn = ann1−k for f(z) = P∞
n=1anqn. Considering equation (3.2), note
that for r/2≥k− 1 and r odd, L(f,ζ−d
c ;k− 1−r/2) vanishes due to the poles of Γ(ρ) and
the fact that Λ(f,ζ−d
c ;ρ) is entire. This means that
1√ubgodd
−d/c(u) =− 1√π
k−5/2X
n=0
L(g,ζ−d
c ;−n− 1/2)
Γ(2n + 2) (8πi)n+1/2un,
which is just a polynomial in u. Then, we claim that
Z
Γ
e−u/(z+d/c)


k−5/2X
n=0
L(g,ζ−d
c ;−n− 1/2)
Γ(2n + 2) (8πi)n+1/2un

 du = 0.
To see this, one considers an arc of radius R> 0 which connects two points of Γ to form an
oriented closed curve. The integral along this entire curve must be 0 by the residue theorem,
and as R tends to infinity, the integral along the arc approach zero since the expression in
brackets is a polynomial and e−u/(z+d/c) decays exponentially as ℑ(u)→∞ (recalling that
z +d/c∈iR+).
Now suppose that g is of Type 5. We consider only z→ 0. Showing Equation 3.3 will
require more work in this case. In order to show that the integral vanishes, we realize
1
2√ubgodd
−d/c as a Borel transform of another asymptotic series. Taking the Borel transform with
a different shift results in a much simpler function which is easily shown to be holomorphic
on H. This, coupled with Lemma 2.6, is enough to prove our claim.
22 ELEANOR MCSPIRIT AND LARRY ROLEN
Recalling the definitions of L0 and L1 from Section 2.3, we have
L0(−n− 1/2) = 1
π2n+3· 22n+2 Γ(n + 3/2)2L0(n + 3/2);
L1(−n− 1/2) =− 1
π2n+3· 22n+2 Γ(n + 3/2)2L1(n + 3/2).
Returning tobgodd
0 in this new case, we have
1
2√ubgodd
0 (u) =− 1
2√π
∞X
n=0
(8πi)n+1/2
π2n+3· 22n+2
Γ(n + 3/2)2
Γ(2n + 2) (L0(n + 3/2)−L1(n + 3/2))un.
Noting that Γ(2n + 2) = 22n+1
√π Γ(n + 1)Γ(n + 3/2), we can write this as
−
∞X
n=0
1
π2n+3· 22n+3
Γ(n + 3/2)
Γ(n + 1) (L0(n + 3/2)−L1(n + 3/2)) (2πi)n+1/2un.
Now we define the function
Φ(z) :=−
∞X
n=0
1
π2n+3· 22n+3 Γ(n + 3/2) (L0(n + 3/2)−L1(n + 3/2)) (2πi)n+1/2zn.
ThenB1(Φ(z)) = 1
2√ubgodd
0 (u). Let us instead consider B3/2(Φ(z)). This is equal to
−
∞X
n=0
1
π2n+3· 22n+3 (L0(n + 3/2)−L1(n + 3/2)) (2πi)n+1/2un.
From here, we compute
B3/2(Φ(z)) =−
∞X
n=0
(2πi)n+1/2
π2n+322n+3
" ∞X
m=1
A−m
mn+3/2
#
un
=− 1
2πi
∞X
n=0
" ∞X
m=1
A−m
(−2πim)n+3/2
#
un
=− 1
2πi
∞X
m=1
A−m
(−2πim)3/2
" ∞X
n=0
un
(−2πim)n
#
= 1
2πi
∞X
m=1
A−m
(−2πim)1/2
 1
u− (−2πim)

This function has only simple poles at points −2πim for m∈ N. Importantly, the poles are
not in the upper half-plane. In particular, we have that
Lπ/2−ε
3/2 (B3/2(Φ(z)) =Lπ/2+ε
3/2 (B3/2(Φ(z))
QUANTUM MODULAR FORMS AND RESURGENCE 23
for 0 <ε<π/ 2. Then by Lemma 2.6, we have that
Lπ/2−ε
1 (B1(Φ(z)) =Lπ/2−ε
3/2 (B3/2(Φ(z)) =Lπ/2+ε
3/2 (B3/2(Φ(z)) =Lπ/2+ε
1 (B1(Φ(z)).
This is exactly what we want. To see this, consider again
1
2
Z
Γ
e−u/zbgodd
0 (u)du√u.
Forε sufficiently small, the contour Γ in Figure 1 is equivalent to a median resummation
contour forθ =π/2 since our function is analytic in a disc around the origin. From here, we
have that
1
2
Z
Γ
e−u/zbgodd
0 (u) du√u =
Z
Γ
e−u/zB1(Φ(z))du
=
 Z ei(π
2−ε)∞
0
−
Z ei(π
2 +ε)∞
0
!
e−u/zB1(Φ(z))du
=z

Lπ/2−ε
3/2 B3/2(Φ(z))−Lπ/2+ε
3/2 B3/2(Φ(z))

= 0.
Now we have shown that the second integral in Equation 3.1 vanishes, proving that g(z) =
Sπ/2
med(φ−d/c)(z) as desired. □
In the case where g is of Type 6, we modify the argument slightly and end up with a
similar result.
Proposition 3.5. If g is of Type 6, then
g =Sπ/2
med(φ0) + 1
2√z
Z
Γ
e−u/z
−4 + 2 log(8πiu)
2πiu
 du√πu.
Proof. We write
1− 4
∞X
n=1
d(n)qn = 1
2√z
Z
Γ
e−u/z
 
1− 4
∞X
n=1
d(n)e−
√
8πinu
!
du√πu,
and using the Mellin transform again we rewrite the inner sum as
−4− 2 log(8πiu)
2πiu − 4√π
∞X
r=1
(−1)rζ2(−r/2)
Γ(r + 1) (8πiu)r/2,
Noting that the calculation for the pole at s = 2 differs slightly. Leaving the leading term,
we again split the sum into the cases where r is even or odd to get
bgeven
0 (u) :=−4√π
∞X
n=0
ζ2(−n)
Γ(2n + 1)(8πiu)n;
24 ELEANOR MCSPIRIT AND LARRY ROLEN
1√ubgodd
0 (u) := 4√π
∞X
n=0
ζ2(−n− 1/2)
Γ(2n + 2) (8πi)n+1/2un.
As before, we have that bgeven
0 (u) = B1/2(φ0), where φ0 was defined for g in the proof of
Proposition 3.3. The proof that the integral of bgodd
0 (u) vanishes is the same as in Proposition
3.4 when g is of Type 5. After appropriately rescaling to get from P∞
n=1d(n)qn to g, we get
the desired result. □
Note that in the cases where g is of Type 1 , 2, or 3, one can argue the same way as in
Proposition 3.4 to get the same decomposition as in Equation 3.1. However, in these cases,
the second integral no longer vanishes. Moreover, we know that when g is of Type 1 or 2,
B1/2(φ−d/c(z)) is zero, while for g of Type 3, it is a polynomial. So we have that the first
integral satisfies
1
2
p
z +d/c
Z
Γ
e−u/(z+d/c)B1/2(φ−d/c(z)) du√πu
= 1p
z +d/c
Z ∞
0
e−u/(z+d/c)B1/2(φ−d/c(z)) du√πu,
which up to prefactors is the Borel-Laplace sum of φ−d/c in direction 0.
