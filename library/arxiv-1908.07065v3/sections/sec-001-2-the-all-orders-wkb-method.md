---
doc_id: arxiv-1908.07065v3
doc_title: "Prepared for submission to JHEP Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-001-2-the-all-orders-wkb-method
section_title: "The all-orders WKB method"
section_number: 2
pages: 3-8
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve ofN = 2, SU (2) super Yang–Mills"
---
particular against high order results for the expansion of the quantum periods. We also comment
on how to use these TBA equations to compute Borel resummations of the quantum periods.
As pointed out in [11] and explored in many subsequent papers, the NS limit of instanton
calculus [1] provides a diﬀerent resummation of the WKB expansion, in terms of a convergent
expansion in the instanton counting parameter. However, this resummation has a very diﬀerent
ﬂavor from the Borel resummation appearing in the theory of resurgence, and it is important to
have a precise dictionary between the two types of resummation. We address this issue in section
4.
As we mentioned above, the TS/ST correspondence gives explicit expressions for spectral
determinants of operators obtained in the quantization of mirror curves. As pointed out in
[18], there is a four-dimensional limit of the correspondence in which the relevant operator is
the quantization of the SW curve for pure N = 2, SU (N) Yang–Mills theory. This leads to
a spectral problem which is diﬀerent from the one considered in [1] for N > 2. In the case
of the SU (2) theory considered in this paper, the spectral problems coincide, but the TS/ST
correspondence gives, in addition to the quantization condition of [1], an explicit expression for
the spectral determinant, which we derive in detail in section 5 of this paper. The resummed
quantum periods deﬁned by instanton calculus are key ingredients in this expression. We test
the resulting formula and in particular we compare our result to the TBA equation describing
this spectral determinant which was conjectured by Al. B. Zamolodchikov in [19].
In section 6, based on previous works, we use the vanishing Nakajima-Yoshioka blowup
equations to prove that the exact spectrum of the modiﬁed Mathieu operator is computed by
the zeros of the τ function of Painlev´ e III3. Finally, in section 7 we conclude and discuss some
open problems.
We have also included two Appendices: in the ﬁrst one we extend the derivation of section
– 2 –
5 to SU (N) quantum SW curves, while in the second one we review some of the results of
Zamolodchikov’s paper [19].
2 The all-orders WKB method
Our ﬁrst approach to the quantum SW curve will be based on the so-called exact WKB method,
see for example [20–23]. We will now summarize the basic ingredients of the theory.
The Schr¨ odinger equation for a non-relativistic particle in a potentialV (x) and with energy
E reads as follows:
− ℏ2ψ′′(x) + (V (x)−E)ψ(x) = 0. (2.1)
The standard WKB method produces asymptotic expansions in ℏ for the solutions to this equa-
tion. Let us consider the following ansatz for the wavefunction,
ψ(x) = exp
( i
ℏ
∫ x
Y (x′,E ; ℏ)dx′
)
. (2.2)
The function Y (x,E ; ℏ) satisﬁes the Riccati equation
Y 2− iℏdY
dx =E−V (x) . (2.3)
It has the formal power series expansion in powers of ℏ
Y (x,E ; ℏ) =
∞∑
n=0
pn(x,E )ℏn , (2.4)
where in particular p0(x,E ) is the classical momentum as a function of x and the conserved
energy. If one splits Y into the even component and the odd component,
Y =peven +podd, (2.5)
with
peven(x,E ; ℏ) =
∞∑
n=0
p2n(x,E )ℏ2n , p odd(x,E ; ℏ) =
∞∑
n=0
p2n+1(x,E )ℏ2n+1 , (2.6)
one ﬁnds that the odd component is in fact a total derivative
podd(x,E ; ℏ) = iℏ
2
d
dx logpeven(x,E ; ℏ). (2.7)
By substituting (2.2) into the Schr¨ odinger equation, one ﬁnds (see for instance [24])
p2n = (−1)nv2n , n ≥ 0 (2.8)
vn = 1
2p0
(
∂xvn−1−
n−1∑
k=1
vkvn−k
)
, (2.9)
from which the components p2n(x,E ) can be solved recursively, starting from the known expres-
sion of p0.
– 3 –
Geometrically, we can regard peven(x,E ; ℏ)dx as a meromorphic diﬀerential on the curve
deﬁned by
y2 = 2(E−V (x)). (2.10)
We will call it the WKB curve, and we will denote it as Σ WKB. This curve depends on a set of
moduli which include the energy E and the parameters of the potential V (x). The basic objects
in the exact WKB method are the periods of peven(x,E ; ℏ)dx along one-cycles of Σ WKB, which
we will call WKB periods or quantum periods. We will denote them as
Πγ(ℏ) =
∮
γ
peven(x,E ; ℏ)dx, γ ∈H1(ΣWKB), (2.11)
and they are formal power series in even powers of ℏ, just like peven(x),
Πγ(ℏ) =
∑
n≥0
Π(n)
γ ℏ2n, Π(n)
γ =
∮
γ
pn(x,E )dx. (2.12)
Note that the coeﬃcients Π (n)
γ depend on the moduli of the WKB curve. We will call Π (0)
γ the
classical periods. The calculation of these coeﬃcients at high order can be quite involved, even
for simple quantum systems.
In this paper we are interested in the modiﬁed Mathieu Hamiltonian, with the conventions
H(p,x ) =p2 +V (x), V (x) = 2Λ2 coshx. (2.13)
Upon quantization, we obtain the operator
H = p2 + 2Λ2 cosh(x), [x, p] = iℏ. (2.14)
We will refer to this as the modiﬁed Mathieu operator. It is well-known that the WKB curve
of the modiﬁed Mathieu Hamiltonian happens to coincide with the SW curve of N = 2, SU (2)
Yang–Mills theory, in the conventions appropriate for the relation to integrable systems (see e.g.
[25] for a review of SW theory and [26] for its connection to integrable systems). In order to do
this, we identify E with the Coulomb modulus u by
E = 2u . (2.15)
Let us ﬁrst consider the classical periods of the modiﬁed Mathieu equation. Since the WKB
curve is a torus, there will be two periods, corresponding to the two cycles of the torus. The B
period corresponds to the classical volume of phase space
Π(0)
B (E) = 4 i
∫ x+
0
dx
√
E− 2Λ2 coshx, (2.16)
where
x+ = cosh−1 E
2Λ2 (2.17)
is the turning point. This classical period can be evaluated explicitly as
Π(0)
B (E) = 8 i
√
E + 2Λ2
[
K
(E− 2Λ2
E + 2Λ2
)
− E
(E− 2Λ2
E + 2Λ2
)]
. (2.18)
– 4 –
(We denote the elliptic integrals with boldface letters K, E, and their argument is the squared
modulus m = k2). There is in addition an A period which corresponds to motion along the
imaginary axis. Classically, it is given by,
Π(0)
A (E) =−2 i
∫ πi
−πi
dx
(√
E− 2Λ2 coshx
)
= 8
√
E + 2Λ2E
( 4Λ2
2Λ2 +E
)
. (2.19)
In the simplest case when E = 0 and Λ = 1, we have
Π(0)
A (0) = (1 + i) 16π3/2
Γ(1/4)2, Π(0)
B (0) =−i 16π3/2
Γ(1/4)2. (2.20)
We note that these classical periods are, up to normalization, the famousa andaD =∂aF periods
of SW theory [27], namely
Π(0)
A (E) = 2πa(u), Π(0)
B (E) = 2iaD(u). (2.21)
We will denote the all-orders WKB quantum periods as
ΠA,B(E, ℏ) =
∞∑
n=0
ℏ2nΠ(n)
A,B(E). (2.22)
In the case of the modiﬁed Mathieu equation, the most eﬃcient way to calculate the quantum
corrections is the so-called quantum operator approach (see e.g. [13]). It turns out that, for each
functionp2n(x,E ) appearing in (2.6), one can ﬁnd a ﬁrst order diﬀerential operator On(E) such
that
On(E)◦p0(x,E ) =p2n(x,E ) (2.23)
up to a total derivative. Since On(E) commutes with integration, one immediately has
Π(n)
A,B(E) =On(E)◦ Π(0)
A,B(E) . (2.24)
In this way, we have computed quantum corrections up to order 193. As a simple example, with
Λ = 1 we have [13]
O1(E) = E
48(4−E2) + ∂
24∂E . (2.25)
Therefore,
Π(1)
A (E = 0) =−1− i
6
√
2 K(−1) , Π(1)
B (E = 0) =− i
6
√
2K(−1) . (2.26)
We recall that the quantum periods satisfy the so-called quantum Matone relation [14, 17, 28–31].
One of the consequences of this relation is that
Π(0)
A (E)Π(1)
B (E)− Π(0)
B (E)Π(1)
A (E) = const. , (2.27)
which we can then evaluate at E = 0 to be−2πi/3.
It is well-known that the formal power series appearing in the quantum periods diverge
generically as [24, 32]
Π(n)
γ ≈ (2n)!, n ≫ 1. (2.28)
– 5 –
Therefore the expressions (2.12) are just formal power series and need to be properly resummed.
A natural way of doing so is to perform the Borel resummation. In general, given an asymptotic
series of the form
F =
∞∑
n=0
fnℏ2n , ℏ∈ C , (2.29)
with
fn∼ (2n)! , n ≫ 1 (2.30)
we split ℏ = eiφ|ℏ|, and deﬁne the Borel resummation to be
s(F )(ℏ) = 1
|ℏ|
∫ ∞
0
ˆF (eiφζ)e−ζ/|ℏ|dζ , (2.31)
where ˆF (ζ) is the Borel transform
ˆF (ζ) =
∞∑
n=0
fn
(2n)!ζ2n . (2.32)
The analytic properties ofˆF (ζ) in theζ-plane, also called the Borel plane, are crucial. If the Borel
transform has singularities along the ray arg( ζ) = φ, the series F (ℏ) is not Borel summable, as
the integral in the Laplace transformation (2.31) is obstructed. We can however deform slightly
the integration contour below or above the positive real axis, obtaining in this way the so-called
lateral Borel resummations of the formal power series F (ℏ):
s±(F )(ℏ) = 1
|ℏ|
∫ ei0±
∞
0
ˆF (eiφζ)e−ζ/|ℏ|dζ. (2.33)
These lateral resummations are in general diﬀerent, and their diﬀerence is deﬁned as the Stokes
discontinuity of F :
disc(F )(ℏ) =s+(F )(ℏ)−s−(F )(ℏ). (2.34)
Stokes discontinuities play a crucial rˆ ole in the theory of resurgence, see e.g. [33].
Let us look at some examples of the Borel plane of the quantum periods for the modiﬁed
Mathieu equation. In practice, to calculate the Borel transform, we use standard Borel–Pad´ e
techniques, i.e. we use a ﬁnite number of terms in the formal power series (in this case we have used
193 terms), and in order to extend analytically the resulting function, we use a Pad´ e transform
of the Borel transform. In this method, branch cuts of the Borel transform are indicated by a
dense accumulation of poles of the Borel–Pad´ e transform along a segment. The ﬁrst example is
when u = E = 0. We plot the poles of the Borel–Pad´ e transforms of Π A(0, ℏ), ΠB(0, ℏ) in the
Borel plane in Figures 1. They indicate the existence of four branch cuts in the case of the A
period, and two branch cuts in the case of B period. Since in both cases there are branch cuts
along the positive real axis, neither of the two quantum periods are Borel summable.
Next, we consider u = E/2 = 4. Again we plot the poles of the Borel–Pad´ e transforms of
ΠA(4, ℏ), ΠB(4, ℏ) in the Borel plane in Figures 2. In both cases we observe six branch cuts, and
they are in diﬀerent locations as compared to what we found at u = 0. In this case, the quantum
A period is Borel summable, but the quantum B period is not.
As we can see, in general, the quantum periods are not Borel summable, and their Borel
transforms and resummations have a rich structure. Fortunately the connection with SW theory
gives very powerful information on this structure, which we will explore in detail in the next
section.
– 6 –
(0, 1)
(0,-1)
(1, 1)(-1,-1)
-20 -10 10 20
-20
-10
10
20
(a) ΠA
(1, 1)(-1,-1)
-20 -10 10 20
-20
-10
10
20 (b) ΠB
Figure 1: Poles of the Borel–Pad´ e transforms, which would accumulate to branch cuts for the
Borel transform of the quantum periods ΠA(E, ℏ) (a) and ΠB(E, ℏ) (b) atu = 0 and Λ = 1. The
red points are the central charges of the BPS states which contribute to the branch points, and
their electromagnetic charges are labelled nearby. See discussion in section 3.2.
(0, 1)
(0,-1)
(1, 1)
(1,-1)
(-1, 1)
(-1,-1)
-40 -20 20 40
-40
-20
20
40
(a) ΠA
(1, 0)(-1, 0)
(1, 1)
(1,-1)
(-1, 1)
(-1,-1)
-40 -20 20 40
-40
-20
20
40 (b) ΠB
Figure 2: Poles of the Borel–Pad´ e transforms, which would accumulate to branch cuts for the
Borel transforms of the quantum periods ΠA(u, ℏ) (a) and ΠB(u, ℏ) (b) at u = 4 and Λ = 1. The
red points are the central charges of the BPS states which contribute to the branch points, and
their electromagnetic charges are labelled nearby. See discussion in section 3.2.
