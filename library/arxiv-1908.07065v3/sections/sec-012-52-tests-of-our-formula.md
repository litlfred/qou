---
doc_id: arxiv-1908.07065v3
doc_title: "Prepared for submission to JHEP Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-012-52-tests-of-our-formula
section_title: "Tests of our formula"
section_number: 5.2
pages: 31-37
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve ofN = 2, SU (2) super Yang–Mills"
---
We will now test the expression (5.6) in several ways.
A ﬁrst simple test is that the zeros of Ξ(E) give the correct spectrum of the modiﬁed Mathieu
operator. This should be expected from the general results of [18], but it is instructive to check
it explicitly. The zeros correspond to the vanishing of the cosh in (5.6), and by using (4.18) we
ﬁnd,
∂aFNS(a, ℏ) = ℏπ
(
n + 1
2
)
, (5.16)
which is the exact quantization condition obtained from the conjecture in [1], subsequently proved
in [56].
– 30 –
Another check can be obtained by comparing our expression to the asymptotics of Fredholm
determinants obtained in [20, 21, 66] by using the all-orders WKB method. This asymptotic
expansion is valid when E <0, where the Fredholm determinant is not oscillatory. In order to
write down the asymptotics, we need some ingredients. Let
G(E) =
∞∑
n=0
1
E−En
(5.17)
be the trace of the resolvent, and
T (E) = 1
2
∫
R
dx√
2Λ2 cosh(x)−E
(5.18)
the transit time. We also need the formal power series in ℏ
b(E) = exp


i
∑
n≥1
ℏ2n−1
∫
R
p2n(x,E )dx


, (5.19)
where the functions p2n(x,E ) are the ones appearing in the solution to the all-orders WKB
method in (2.4). Let us now deﬁne κ =−E, which will be taken to be positive. It is convenient
to introduce the functions
~G(κ) =G(−κ), ~Ξ(κ) = Ξ(−κ), ~b(κ) =b(−κ), ~T (κ) =T (−κ). (5.20)
Then, one has the following small ℏ asymptotics,
~Ξ(κ)∼~b(κ) exp
{1
ℏ
∫ κ
0
~T (κ′)dκ′−
∫ ∞
0
(
~G(κ′) + 1
ℏ
~T (κ′)
)
dκ′
}
. (5.21)
The second term in the exponent is independent of κ but depends on ℏ. We note that all the
integrals involved in this expression are well deﬁned precisely because E is negative. The very
ﬁrst terms in the asymptotics can be easily worked out, and one ﬁnds 8
log Ξ(−κ)∼− i
2ℏΠ(0)
B (κ) + iℏ
2 Π(1)
B (κ) +··· , κ> 0, (5.22)
up to κ-independent terms. Note that the sign in the subleading correction is the opposite one
to what one ﬁnds in the WKB expansion of the quantum B period.
Let us now compare this result to the exact expression for the spectral determinant (5.6),
which can be written as
Ξ(E) =A(ℏ)
(
sinh
(πa
ℏ
))−1
cos
(1
ℏ
∂FNS
∂a
)
. (5.23)
From the explicit expression (4.28) it is easy to see that, whenE is negative,a is purely imaginary.
More precisely, one has
a(−κ, ℏ) = iα, α =a(κ, iℏ), (5.24)
8This agrees with an unpublished calculation of Y. Hatsuda, who obtained the same result by considering the
semiclassical expansion of the spectral traces.
– 31 –
and we take α> 0 for deﬁniteness. In addition,
∂aF inst
NS (a, ℏ) = i∂αF inst
NS (α, iℏ). (5.25)
By using the explicit expression (4.16) and standard identities for the Γ function, we ﬁnd
Ξ(−κ)
A(ℏ) = 1
2π Γ
(
1 +α
ℏ
)
Γ
(α
ℏ
)
exp
[α
ℏ log
( ℏ2
Λ2
)
+ 1
ℏ∂αF inst
NS (α, iℏ)
]
+ 1
2π Γ
(
1− α
ℏ
)
Γ
(
−α
ℏ
)
exp
[
−α
ℏ log
( ℏ2
Λ2
)
− 1
ℏ∂αF inst
NS (α, iℏ)
]
.
(5.26)
The term in the second line gives an exponentially small correction to the leading asymptotics.
The small ℏ asymptotics of the quantity in the ﬁrst line is given by
log
[ 1
2π Γ
(
1 +α
ℏ
)
Γ
(α
ℏ
)]
+ α
ℏ log
( ℏ2
Λ2
)
+ 1
ℏ∂αF inst
NS (α, iℏ)
∼− i
2ℏ
∑
n≥0
(−1)nΠ(n)
B (κ)ℏ2n.
(5.27)
We have used that, due to (5.24) and (5.25), the quantum period is evaluated at −E, where
E = −κ < 0, and we have to change ℏ → iℏ. The result is in agreement with the WKB
asymptotics obtained in (5.22).
A more precise test of (5.6) can be made by comparing the analytical formulae for the
spectral traces with numerical results. These are obtained by calculating the spectrum of H with
standard techniques. An example of such a comparison is shown in Table 11.
Nb Z2
2 0.004794786 11468342466
4 0.004794786073913 81196
6 0.00479478607391375025
Num 0.00479478607391375025
Table 11: The second spectral trace Z2 as computed from (5.9) for ℏ = 3π and Λ = 1. The
number Nb means that we truncate the series (4.13) at order Λ 4Nb. The last line gives the
numerical result obtained from the spectrum of H.
We ﬁnally note that Ξ(E) is an entire function ofE. In particular, the would-be singularities
due to the denominator of (5.23) or to the Gamma functions in (4.16) must cancel in the end.
This leads in turn to constraints on the form of the singularities of F inst
NS , which might be testable
against the results in [67] (see also [68]).
5.3 Comparison to Zamolodchikov’s TBA equation
An additional test of our formula (5.6) comes from a comparison with [19]. Inspired by the
ODE/IM correspondence [69, 70], Zamolodchikov found in [19] a TBA equation which computes
precisely the spectral determinant (5.6). Let us state the main result of [19], referring to Appendix
B for more details. Let ϵ(θ,P ) be a solution of the TBA equation (3.69) but with the boundary
condition at θ→−∞ given by
ϵ(θ,P )∼ 8Pθ− 2C(P ), θ →−∞, P > 0, (5.28)
– 32 –
where C(P ) is written down in (B.15). Let us now introduce the function
X(µ,P ) = exp [−ϵ(θ,P )/2], (5.29)
where µ is related to θ by
µ = e2θ
(
Γ
( 1
4
)2
16√π
)2
. (5.30)
Then, according to [19], the spectral determinant of the modiﬁed Mathieu operator (2.14) is
given by
Ξ(E) = X(µ,P )
X(µ, 0), (5.31)
where the parameters Λ, E and ℏ of the operator are related to the parameters appearing in
X(µ,P ) by
µ = Λ2ℏ−2, P 2 =−Eℏ−2. (5.32)
If we compare the result of [19] with ours we should have (by using the dictionary (5.32))
X(µ,P )
X(µ, 0) =A(ℏ)
(
sinh
(Πex
A (E, ℏ)
2ℏ
))−1
cosh
( 1
2ℏΠex
B (E, ℏ)
)
. (5.33)
In order to ﬁnd the relation between the two normalization constants X(µ, 0) and A(ℏ), it is
useful to ﬁrst derive the asymptotic behavior (5.28) from our expression (5.6). We need to
expand around small Λ ℏ−1 and take u < 0, which means that a is imaginary, as discussed in
(5.24). In this regime, and by using (4.18), we have
(
sinh
(πa
ℏ
))−1
cosh
( i
ℏ∂aFNS(a, ℏ)
)
≈ 2−1π−1
((Λ
ℏ
)−2s
Γ(1 +s)Γ(s) +
(Λ
ℏ
)2s
Γ(1−s)Γ(−s)
)
,
(5.34)
where
s =−ia
ℏ = α
ℏ > 0. (5.35)
By using (4.14) we have
E≈a2/4 (5.36)
and therefore
P =s/2> 0. (5.37)
Hence we can neglect the second term in the r.h.s. of (5.34). It follows from (5.32) that (5.34)
agrees precisely with (5.28). In particular this means that the two normalization constants are
identiﬁed and we have
X(µ,P ) =
(
sinh
(Πex
A (E, ℏ)
2ℏ
))−1
cosh
( 1
2ℏΠex
B (E, ℏ)
)
. (5.38)
We test this equality by solving numerically the TBA equation (3.69) with the boundary condition
(5.28). Some results are given in Table 12. We ﬁnd perfect agreement.
– 33 –
Nb log
((
sinh
(πa
ℏ
))−1 cosh
( i
ℏ∂aFNS(a, ℏ)
))
2 11.360025 317439438
4 11.36002529911 2863
6 11.360025299117259
TBA 11.360025299117
Table 12: The un-normalized spectral determinant as computed by using instanton counting
and by solving numerically the TBA (3.69) with (5.28). We use P 2 =−E = 5, µ = Λ 2 =(
Γ (1/4)2/(16√π)
)2
, and ℏ = 1. The number Nb means that we truncate the series (4.13) at
order Λ4Nb.
An important spinoﬀ of this comparison is that our result (5.6) provides an analytic, closed
form solution to the TBA equation of [19]. This also has the following consequence. When
we derived the Fredholm determinant from the topological string perspective, and due to our
regularization procedure, we generated an integration constant A(ℏ) whose explicit expression
is given in (5.7). Given the identity (5.38) between our Fredholm determinant and the solution
to the Zamolodchikov’s TBA, we expect A(ℏ) to be computed by the integral equation (3.69) at
P =u = 0. More precisely we expect
2 logA(ℏ) =ϵ(θ,P = 0), (5.39)
where we used the dictionary (5.32). For P = 0 the asymptotic condition (5.28) does not make
sense, strictly speaking. Nevertheless, we can derive the appropriate asymptotic condition for
the TBA at P = 0 by using our analytic expression (5.38). We ﬁnd that, as θ→−∞ ,
ϵ(θ,P = 0)∼− 2 log
(
−2(θ +γEuler)− logπ + 4 log Γ(5/4)
π
)
. (5.40)
This is precisely the boundary condition used in section 3.3, equation (3.74). One can now check
(5.39) numerically. For instance, by solving the TBA of section 3.3 we ﬁnd
ϵ(θ,P = 0)
⏐⏐⏐
θ=−1
= 0.51888··· (5.41)
Likewise, by using instanton counting, and in particular (4.18) and (5.7), we have (Λ = 1)
2 log
(
A
(
16e√π
Γ
( 1
4
)2
))
= 0.51887965286656··· (5.42)
We have 5 matching digits which is consistent with the precision achieved with the TBA equation.
This discussion provides an additional result along the lines of what we obtained in section
4.2. As we discussed in section 3.3, the functionϵ(θ) with the boundary condition (3.74) computes
the dyonic period Π D(0, ℏ). As pointed out in Sec 4.2, such period is Borel summable, and we
can indeed test that its Borel resummation agrees with (5.7), namely
exp
( 1
2ℏs (ΠD) (0, ℏ)
)
= sinh
(πa
ℏ
)
cosh
( i
ℏ∂aFNS(a, ℏ)
)
⏐⏐⏐⏐
a=a(0,ℏ)
= sinh
( 1
2ℏΠex
A (0, ℏ)
)
cosh
( 1
2ℏΠex
B (0, ℏ)
). (5.43)
– 34 –
We have veriﬁed this identity numerically. In addition we have tested that (5.43) also holds for
other values of u in the strong coupling region, and we conjecture that, for u∈ [−1, 1], one has
exp
( 1
2ℏs (ΠD) (u, ℏ)
)
= sinh
( 1
2ℏΠex
A (u, ℏ)
)
cosh
( 1
2ℏΠex
B (u, ℏ)
). (5.44)
6 On the modiﬁed Mathieu operator and Painlev´ e III3
It was observed by many authors [63, 71, 72] that the movable poles of Painlev´ e III3 are somehow
related to Mathieu functions. In particular in [73], based on [65], it was observed that the zeros
of the Painlev´ e III3 τ function compute the spectrum of modiﬁed Mathieu (with a suitable dic-
tionary). From the view point of the TS/ST correspondence [2] this connection comes naturally
since both systems arise as limiting cases of this duality. In particular, the modiﬁed Mathieu
operator arises in the standard geometric engineering limit [18, 55, 74], while Painlev´ e III3 arises
in the dual geometric engineering limit considered in [65].
In this section we prove the connection between the zeros of the Painlev´ e III3 τ function and
the spectrum of the modiﬁed Mathieu operator by using [75]. From the CFT perspective this
is a connection between Liouville conformal blocks at c = 1 and c =∞. We proceed as follows.
First we write the Painlev´ e III3 τ function as [76–78]
τ(Λ,a,η, ℏ) =
∑
n∈Z
e4πinη exp
(
F SD(a + 2iℏn, ℏ, Λ)
)
(6.1)
where
exp
(
F SD(a, ℏ, Λ)
)
=
(Λ
ℏ
)−a2
ℏ2 1
G(1− ia
ℏ)G(1 + ia
ℏ)
×
(
1− 2Λ4
a2ℏ2 + Λ8(
2a2− ℏ2)
a2ℏ2 (a2 + ℏ2)2 +O(Λ12)
) (6.2)
is the so-called four dimensional Nekrasov partition function in the selfdual Ω background [45]
(namely, the equivariant parameters are ϵ1 =−ϵ2 = ℏ). The parameters ( a,η ) in (6.1) play the
role of initial conditions while Λ is the time. We are interested in the case in which
η = 0. (6.3)
We now recall the result of [75], where it was demonstrated that, in the NS limit, the Nakajima–
Yoshioka blowup equations for SU (2) pure SYM [79–81] can be written as 9
∑
n∈Z
exp
(
inπ +F SD (a + 2iℏn + iℏ, ℏ, Λ)− 2inℏ−1 ∂
∂aFNS (a, ℏ)
)
= 0. (6.4)
Finally, we use the quantization condition for the modiﬁed Mathieu operator in the NS form
(5.16). It then follows from (6.4) that, if a value of a satisﬁes this exact quantization condition,
one ﬁnds a vanishing condition for the tau function of Painlev´ e III3, namely
τ (Λ,a + iℏ, 0, ℏ) =
∑
n∈Z
exp
(
F SD (a + 2iℏn + iℏ, ℏ, Λ)
)
= 0. (6.5)
9Strictly speaking this is the four-dimensional limit of [75]. This type of expressions ﬁrst appeared in [82] as
compatibility conditions between the exact quantization conditions of [2, 3] and those of [55, 83, 84]. A diﬀerent
connection between blowup and Painlev´ e equations was used in [85–87] to prove the so-called Kiev formula [76, 88]
or its q-deformed version [89, 90].
– 35 –
Notice that we think of (5.16) and (6.5) as quantization conditions for the variable a. In order
to obtain the spectrum of modiﬁed Mathieu one has to use the quantum Matone relation (4.14).
