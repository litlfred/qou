---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-7
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
doc_brief: "On q-summation and confluence — 18 sections: Introduction; Part 1. Convergent q-Borel and q-L; Convergent q-Euler series"
---
Let C[[x]] be the ring of formal power series with complex coeﬃcients and
C{x} the ring of germs of analytic functions at zero. A divergent formal
power series ˆf =∑
n/greaterorequalslant0fnxn+1 ∈ xC[[x]] /integerdividexC{x} is said to be a generic
Gevrey series if it is solution of a diﬀerential equation of the form
(0.1) an(x)
(
x2∂
)n
y(x) +an−1(x)
(
x2∂
)n−1
y(x) +· · ·+a0(x)y(x) = g(x),
where ∂ = d
dx and a0(x),...,a n(x),g (x) ∈ C{x}, with a0(0)an(0) ⁄= 0 .
This implies that its formal Borel transform B( ˆf ) =∑
n/greaterorequalslant0
fn
n!ξn ∈ C{ξ} is
Keywords: Summation, conﬂuence, q-diﬀerence equations, Euler series.
Math. classiﬁcation: 34M30, 39A13, 33D05.
(*) The ﬁrst author is partially supported by the ANR contract ANR-06-JCJC-0028.
348 Lucia DI VIZIO & Changgui ZHANG
a germ of an analytic non entire function. The most important example is
the Euler series
ˆE(x) =
∑
n/greaterorequalslant0
(−1)nn!xn+1,
which is solution of the diﬀerential equation x2∂y +y =x. A generic Gevrey
series has the following properties: B( ˆf ) can be analytically continued along
almost all direction d ∈ (−π,π ] and the Laplace integral along the half line
eidR+:
S d( ˆf ) =
∫ eid∞
0
B( ˆf )(ξ)e−ξ/xdξ,
called sum of ˆf in the direction d, represents a convergent solution of ( 0.1),
analytic on a convenient sector and asymptotic to ˆf at zero: this is the ﬁrst
result of the well-known theory of summation of divergent series ( cf. [14,
11, 9, 10]).
In the last ﬁfteen years analogous summation theories for q-diﬀerence
equations have been developed ( cf. [20, 12, 23, 15, 5]). This last sentence
already shows one issue in the topic: there are many q-summation theories
in the literature and the relations among them are not clear.
Let us consider a q-deformation of the Euler series, namely:
ˆEq(x) =
∑
n/greaterorequalslant0
(−1)n[n]!
qxn+1,
where [n]q = 1 + q + · · · +qn−1 and [n]!
q = [n]q[n − 1]q · · ·[1]q. This series
converges coeﬃcientwise to ˆE(x) when q → 1 and is solution of the q-
diﬀerence equation
x2dqy +y =x, with q ∈ C∗ and dqy(x) = y(qx) −y(x)
(q − 1)x ,
which is a discretization, in an obvious sense, of the so-called Euler dif-
ferential equation x2∂y +y = x. A ﬁrst dichotomy immediately appears:
when |q| < 1 the series ˆEq is a germ of analytic function, converging for
|x|< |1 −q|, while for |q|> 1 the series ˆEq diverges. This is itself quite a
curious fact, that we have investigated in the present paper.
As far as the divergent case |q|> 1 is concerned, another dichotomy im-
mediately shows up: authors have been using two formal Borel transforms,
namely
Bq( ˆf ) =
∑
n/greaterorequalslant0
fn
[n]!q
ξn and Bq( ˆf ) =
∑
n/greaterorequalslant0
fn
qn(n−1)/2ξn.
Notice that we have Bq( ˆEq) = 1
1+ξ andBq( ˆEq) = ˆEp(ξ), withp =q−1. Each
one of these formal Borel transforms will be seen to naturally determine
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 349
two summation procedures, so that we end up with at least four summation
procedures: understanding the relations among them is a natural question.
Notice that from an arithmetic point of view, Bq andBq are deeply diﬀerent
(cf. [2]).
The present paper is divided in two parts: in the ﬁrst one we consider the
case q ∈ (0, 1) ⊂ R, while in the second one we study diﬀerent summation
procedures under the assumption q ∈ (1, ∞). Let us make a few comments
on these assumptions:
• We assume that the parameter q is real: this simpliﬁes the exposition,
although it is not always completely necessary.
• Authors writing on q-diﬀerence equations say sometimes that choosing q
smaller or greater than one is only a matter of convention: as we explain
below, this is not true in the present situation, and the two cases need to
be investigated separately.
Let q ∈ (0, 1) ⊂ R. In this case ˆEq is the Taylor expansion at 0 of a
meromorphic function Eq on C, whose poles are a discrete subset of the
negative real axis R−. In § 1 we prove the uniform convergence of Eq on the
compacts of C /integerdivide R− to the analytic continuation E of the Borel sum of ˆE
in the direction R+. The proof of this result is based on the development of
Eq at ∞, which is a q-deformation of the classical expansion of E at ∞(1) :
E(x) = (log x −γ)e
1
x +
∑
n/greaterorequalslant1
∑
1⩽k⩽n
1
k
n!
( 1
x
)n
,
where γ = lim n→∞
(∑n
k=1
1
k − ln(n)
)
is the Euler constant. In the same
spirit, using Sauloy’s canonical solutions at ∞ of a fuchsian q-diﬀerence
operators [ 16] and his result on their conﬂuence when q → 1, we can prove
the main theorem of the ﬁrst part. Namely, let y(q,x ) =∑
n/greaterorequalslant0yn(q)xn+1 ∈
xC[[x]] be a family of formal power series, with q ∈ (η, 1], for some η ∈
(0, 1). We suppose that the yn(q)’s are continuous functions of q and that
the family φ(q,ξ ) = Bqy(q,x ) ∈ C{ξ} is solution of a family of equations
over P1
C, fuchsian and non resonant at ∞(2) . Then ( cf. Theorem 2.6 below):
Theorem 0.1. — Letd ∈ [0, 2π) be such that φ(1,x ) is holomorphic on
a domain containing the half line eidR+. Then for any x ∈V := {| argx −
(1) cf. [7, page 261], where we have set a = c = 1 and made the variable change x ↦→ 1/x.
(2) For a precise deﬁnition of a family of equations over P1
C, fuchsian and non resonant
at ∞, cf. Assumption 2.7 below.
TOME 59 (2009), F ASCICULE 1
350 Lucia DI VIZIO & Changgui ZHANG
d|< π
2 } we have
lim
q→1−
y(q,x ) = S d(y(1,x )) =
∫ eid∞
0
φ(1,ξ )e−ξ/xdξ,
the convergence being uniform on the compacts of V .
This result immediately implies two corollaries ( cf. §2.3 below). First of
all, lety(x) =∑
n/greaterorequalslant0ynxn+1 ∈xC[[x]] be a series such that φ(ξ) =∑
n/greaterorequalslant0
yn
n!ξn
is solution of a fuchsian diﬀerential equation ∑µ
i=0Ai(ξ)(ξ∂ )iφ = 0 on P1
C,
non resonant at ∞. One can construct a family of power series yq(x), with
q ∈ (0, 1), such that Bqyq(x) is solution of ∑µ
i=0Ai(ξ)(ξdq)iφ = 0 and
yq(x) converges coeﬃcientwise to y(x) when q → 1−. Then:
Corollary 0.2. — The family yq(x) converges uniformly to the Borel
sum S d(y(ξ)) ofy(x), when q → 1−, on the compacts of a convenient sector
V = {| argx −d|<π/ 2}.
A second corollary is about the sum of conﬂuent hypergeometric series.
Let us consider a,b ∈ C, with a −b ⁄∈ Z, and the basic hypergeometric
function:
Φ(a,b ;q,x ) =
∑
n/greaterorequalslant0
(qa;q)n(qb;q)n
(q;q)n
( x
1 −q
)n
,
where (a;q)0 = 1 and (a;q)n = (1 −a)(1−qa) · · ·(1−qn−1a) for any integer
n /greaterorequalslant1.
Corollary 0.3. — The analytic function Φ(a,b ;q,x ) converges uni-
formly to the Borel sum of the hypergeometric conﬂuent series
2F0(a,b ; −;x) =
∑
n/greaterorequalslant0
(a)n(b)n
n! xn,
with (a)0 = 1 and (a)n =a(a + 1) · · ·(a +n) for any integer n /greaterorequalslant1, on the
compacts of a convenient sector centered at 0, when q → 1−.
Finally, notice that the result on the conﬂuence of Eq can be deduced
from theorem 0.1.
The second part of the paper deals with the summation of divergent
q-series when q ∈ (1, ∞) ⊂ R. Following the scheme of the ﬁrst part, we
start our investigation studying four summations of the series ˆEq(x). We
consider the q-exponential and the classical Theta function (here p =q−1):
eq(x) =
∑
n/greaterorequalslant0
xn
[n]!q
, θ p(x) =
∑
n∈Z
pn(n−1)/2xn.
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 351
We replace, in the classical Laplace integral, the exponential function by
eq or θp. By using an usual integral or a discrete q-analogue(3) , denoted∫
λpZfd pξ, we get four diﬀerent q-Borel sums of ˆEq(x):
E d
q (x) = q − 1
lnq
∫ eid∞
0
1
(1 +ξ)eq(q ξ
x )
dξ,
Ed
q (x) = q
lnq
∫ eid∞
0
ˆEp(ξ)
θp(q ξ
x )
dξ;
E [λ]
q (x) = q
1 −p
∫
λpZ
1
(1 + ξ
1−p )eq(q ξ
(1−p)x )
dpξ,
E[λ]
q (x) = q
1 −p
∫
λpZ
ˆEp(ξ)
θq(q ξ
x )
dpξ,
where d ∈ (−π,π ) and λ /∈ −pZ. We prove that Ed
q (x) = E d
q (x) on the
sector arg(x) ∈ (−2π, 2π) of the Riemann surface of the logarithm and that
E [λ]
q (x) = E[λ]
q (x) for any x ∈ C /integerdivide(p − 1)λqZ. Moreover we can explicitly
determine the functions E d
q (x)−E [λ]
q (x) and E [λ]
q (x)−E [µ]
q (x) forx ∈ C/integerdivideR−,
in terms of the Theta function. Finally, we establish the following relation
between E d
q (x) and E [λ]
q (x) (cf. Corollary 3.10 below):
E d
q (x) = 1
lnq
∫ q
1
E [λ]
q (x)dλ
λ .
In an analogous way, for a formal power series ˆf ∈ C[[x]] such that Bq ˆf is
an analytic function with a q-exponential growth of order one at ∞ we can
deﬁne its sums S d
q ˆf , S [λ]
q ˆf , Sd
q ˆf and S[λ]
q ˆf . Using some explicit results for
the Tschakaloﬀ series and a q-convolution product adapted to the situation
we can prove the following ( cf. Theorem 4.14):
Theorem 0.4. — Let ˆf ∈ C[[x]] be a generic q-Gevrey series. Then for
any λ ∈ C∗ /integerdivide∪n
i=1µiqZ, for convenient µ1,...,µ n ∈ C∗, and almost all
direction d ∈ (−π,π ), we have S d
q ˆf =Sd
q ˆf and S [λ]
q ˆf =S[λ]
q ˆf . Moreover:
S d
q ˆf = 1
lnq
∫ qeid
eid
S [λ]
q ˆfdλ
λ .
The theory of irregular singular q-diﬀerence equations is nowadays rela-
tively well understood. This paper deals with two of the questions that are
still without answer, namely:
(3) It’s the so-called Jackson’s integral, which is an inﬁnite sum that approximates the
associated usual integral. The precise deﬁnition is in Appendix A below.
TOME 59 (2009), F ASCICULE 1
352 Lucia DI VIZIO & Changgui ZHANG
1. Thanks to the work of J. Sauloy [ 16] we know how to “uniformly approx-
imate” the global monodromy of a fuchsian diﬀerential equation on P1
C, in
terms of the Birkhoﬀ matrices of a family of q-diﬀerence equations deform-
ing the given diﬀerential one. Of course an analogous result is expected
be true for the Stokes phenomenon: actually the conﬂuence of the Stokes
matrices is studied for some functional equations linked to classical special
functions ( cf. for instance [ 23]). The main theorem of the ﬁrst part of this
article goes in the direction of a discrete deformation of the Stokes phenom-
enon: diﬀerently from previous authors, we consider a discrete convergent
deformation of the divergent diﬀerential datum. This approach is not re-
ally explored and the present result surely does not exhaust its possible
applications.
2. In the second part of the paper we study the relations between the diﬀer-
ent kind ofq-Borel sums considered in the literature. We prove the relations
among them for a generic Gevrey series. This is a ﬁrst step towards the
proof of a general result for a divergent solution of a q-diﬀerence equations,
having a Newton polygon with more than one slope.
Acknowledgement. We would like to thank the organizers of the Sémi-
naire sur les équations aux q-diﬀérences, at the University of Toulouse 3,
and of the Special Session in Diﬀerential Algebra, at the 2007 AMS Spring
Eastern Sectional Meeting, for giving us the possibility to expose the re-
sults contained in this paper and their interest in our work. In particular we
thank Yves André, Jean-Pierre Ramis and Jacques Sauloy for their interest
and encouragement.
The ﬁrst author would like to thanks the University of Lille 1, and partic-
ularly the participants of the Séminaire de théorie de Galois diﬀérentielle,
for their hospitality.
The authors thanks the anonymous referee for his remarks and sugges-
tions.
