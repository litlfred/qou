---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-004-5-the-microscopic-weakly-non-chiral-large-n-limi
section_title: "The microscopic weakly non-chiral large-N limit"
section_number: 5
pages: 15-18
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
toc_source: outline
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
The microscopic weakly non-chiral large-N limit
The microscopic large-N limit is deﬁned by the following rescaling of variables
ˆx ≡
√
2n x ,
ˆa ≡1
2
√
2n a .
(5.1)
These variables are then to be identiﬁed with the variables in WchPT as given in eq. (2.9). Here
we send the eigenvalues to zero and n →∞such that ˆx remains ﬁnite, hence we are in the vicinity
of the origin. The masses m and z are rescaled likewise. Also the parameter a corresponding to the
eﬀect of ﬁnite-lattice spacing in WchPT is sent to zero and n →∞such that ˆa remains ﬁnite. Thus
we are in the vicinity of the chGUE ensemble which has chiral symmetry. For this reason we call this
microscopic origin limit weakly non-chiral.
We begin with the asymptotic formulas of the partition function. Because we know the (Nf = 1)-
ﬂavour partition function for ﬁnite-N and general ν ≥0 we compute its asymptotic ﬁrst. It reduces
to the asymptotic for the even polynomials R2j at ν = 0. Based on the standard limit [35]
lim
n→∞n−νL(ν)
n
x
n

= x−ν/2Jν(2√x) ,
(5.2)
we obtain the following expression:
lim
n,j→∞
(−)j
2jj! ⟨det[x + /D5]⟩
=
lim
n→∞(1 −a2)j
Z ∞
−∞
ds
√π e−s2(x + 2ias −m)νL(ν)
j
(x + 2ias)2 −m2
2(1 −a2)

=
e−2tˆa2 Z ∞
−∞
ds
√π e−s2t
ν
2
 ˆm −(ˆx + 4isˆa)
ˆm + ˆx + 4isˆa
 ν
2
Iν
p
t( ˆm2 −(ˆx + 4isˆa)2)

.
(5.3)
First we have divided out part of the normalisation that cancels with the norms rj in the sums inside
the kernels. Second we have given the result for j = tn with t ∈[0, 1] as we will need these later when
replacing the sum inside the kernel by an integral. Last we have used that due to the rescaling the
prefactor turns into an exponential,
(1 −ja2/j)j →exp[−ja2] = exp[−2tˆa2] .
(5.4)
The result eq. (5.3) matches that of the partition function eq. (A.7) as it should.
The limiting even polynomial R2j(x) for ν = 0 is obtained by simply setting ν = 0 everywhere in
eq. (5.3) (due to parity there is no need to switch x →−x under the determinant):
lim
n,j→∞
(−)j
2jj! R2j(x)
=
e−2tˆa2 Z ∞
−∞
ds
√πe−s2I0
p
t( ˆm2 −(ˆx + 4isˆa)2)

.
(5.5)
The computation of the limiting odd polynomials R2j+1(x) for ν = 0 is now a simple consequence.
Starting from the explicit form eq. (4.6) we obtain
lim
n,j→∞
√
2n(−)j
2jj! R2j+1(x)
=
e−2tˆa2 Z ∞
−∞
ds
√π e−s2(ˆx + 4isˆa)I0
p
t( ˆm2 −(ˆx + 4isˆa)2)

, (5.6)
after an integration by parts. As a check the asymptotic of the odd polynomial is an odd function in
ˆx. Note that both prefactors from eq. (5.4) will cancel with the limiting norms rj.
Figure 3:
The microscopic density eq. (5.8) for ˆm = 1 (top left plots) and ˆm = 3 (top right plots)
at various values of ˆa = 0.1 (middle blue curves) and ˆa = 0.25 (lower red curves). For comparison
we also show the corresponding chGUE density (ˆa = 0) eq. (5.11) shifted as in eq. (4.30) (top black
curves). For the chGUE-GUE transition at ˆm = 0 (bottom plots) the diﬀerence to ˆa = 0.1 or ˆa = 0.25
is almost indistinguishable, apart from the origin.
For the limiting weight F(x) from eq. (3.16) we get a Gaussian times the error-functions:
lim
n→∞F(x) = exp
h ˆx2
32ˆa2
i 
erf

ˆx
4
√
2ˆa2 +
ˆm
2
√
2ˆa2

+ erf

ˆx
4
√
2ˆa2 −
ˆm
2
√
2ˆa2

.
(5.7)
Collecting all results we obtain the quenched ν = 0 microscopic density ρS(ˆx) ≡limn→∞
1
√
2nρ1(x):
ρS(ˆx)
=
Z ∞
−∞
dˆy e−(ˆx+ˆy)2
32ˆa2
32
√
2ˆa2π

erf
 ˆy −ˆx + 2 ˆm
4
√
2ˆa2

+ erf
 ˆy −ˆx −2 ˆm
4
√
2ˆa2
 Z ∞
−∞
ds dr
π
e−s2−r2
×
Z 1
0
dt(ˆx −ˆy + 4iˆa(r −s))I0
p
t( ˆm2 −(ˆy + 4isˆa)2)

I0
p
t( ˆm2 −(ˆx + 4irˆa)2)

=
Z ∞
−∞
dˆy e−(ˆx+ˆy)2
32ˆa2
√
2ˆa2π

erf
 ˆy −ˆx + 2 ˆm
4
√
2ˆa2

+ erf
 ˆy −ˆx −2 ˆm
4
√
2ˆa2
 Z ∞
−∞
ds dr
π
e−s2−r2
×
p
ˆm2 −(ˆx + 4irˆa)2I0
p
ˆm2 −(ˆy + 4isˆa)2

I1
p
ˆm2 −(ˆx + 4irˆa)2

−(ˆx ↔ˆy)
ˆx + ˆy + 4iˆa(s + r)
.
(5.8)
It is shown in ﬁgure 3.
Here we give both forms, before and after using the Christoﬀel-Darboux
identity which has its large-N correspondence in
Z 1
0
dtI0(X
√
t)I0(Y
√
t) = 2XI0(Y )I1(X) −2Y I0(X)I1(Y )
X2 −Y 2
.
(5.9)
16
Unfortunately we have been unable to check analytically that eq. (5.8) is equivalent to the corre-
sponding density given in [20]. There it is given as the discontinuity of the imaginary part of its
resolvent.
As a check we can again take the limit ˆa →0, and we obtain from the ﬁrst form in eq. (5.8)
lim
ˆa→0 ρS(ˆx)
=
|ˆx|
2 Θ(|ˆx| −ˆm)
Z 1
0
dtJ0
p
t(ˆx2 −ˆm2)
2
=
|ˆx|
2 Θ(|ˆx| −ˆm)
h
J0
p
ˆx2 −ˆm2
2
+ J1
p
ˆx2 −ˆm2
2 i
.
(5.10)
It equals the shifted microscopic density of the chGUE at ν = 0 after the shift in eq. (4.30)
ρchGUE
S
(ˆx) = |ˆx|
2

J0(ˆx)2 + J1(ˆx)2
.
(5.11)
We now turn to the limiting density for ν = 1. Starting from eqs. (4.32) and (4.34) it is useful to
write it as the limiting density at ν = 0 which we have already determined, plus a correction term.
Collecting all terms and using the asymptotic expressions from above we arrive at
ρν=1
S
(ˆx)
=
ρS(ˆx) +
Z ∞
−∞
dˆz e−(ˆx+ˆz)2
32ˆa2
16ˆaπ
√
2π

erf
 ˆx −ˆz + 2 ˆm
4
√
2ˆa2

+ erf
 ˆx −ˆz −2 ˆm
4
√
2ˆa2

×
(Z ∞
−∞
ds e−s2I0
p
ˆm2 −(ˆx + 4isˆa)2
 Z ∞
−∞
dr e−r2
ˆm + ˆz + 4iˆar
p
ˆm2 −(ˆz + 4iˆar)2
× I1
p
ˆm2 −(ˆz + 4irˆa)2

−(ˆx ↔ˆz)
o
+
1
4πˆae−(ˆx+ ˆ
m)2
16ˆa2
Z ∞
−∞
ds e−s2I0
p
ˆm2 −(ˆx + 4isˆa)2

,
(5.12)
which we illustrate in ﬁgure 4.
Figure 4: The microscopic density eq. (5.12) for ˆm = 0 (left plots) and ˆm = 3 (right plots) at various
values of ˆa = 0.3 (red curves), ˆa = 0.1 (blue curves), and ˆa = 0 (black curves) for comparison. For
the chGUE-GUE transition at ˆm = 0 the density is still symmetric and we only display ˆx > 0. For
ˆm > 0 the delta-function is shifted to the left, and we can nicely see its increasing broadening from
ˆa = 0.1 to ˆa = 0.25.
Once more we can perform as a check the limit ˆa →0, and we obtain
lim
ˆa→0 ρν=1
S
(ˆx)
=
lim
ˆa→0 ρS(ˆx) −
|ˆx|
√
ˆx2 −ˆm2 J0
p
ˆx2 −ˆm2

J1
p
ˆx2 −ˆm2

Θ(|ˆx| −ˆm) + δ(ˆx + ˆm) .
(5.13)
The matching with the density of the chGUE at ν = 1,
ρchGUE
S, ν=1 (ˆx) = |ˆx|
2

J1(ˆx)2 −J0(ˆx)J2(ˆx)

,
(5.14)
shifted as in eq. (4.30) can be seen as follows:
ρchGUE
S, ν=1 (X) −ρchGUE
S
(X)
=
−X
2 J0(X)(J2(X) + J0(X))
=
−J0(X)J1(X) .
(5.15)
Here we used a Bessel identity and the abbreviation X =
√
ˆx2 −ˆm2. The delta-function in eq. (5.13)
is just the exact zero-eigenvalue at ˆx = −ˆm, originating from the last term in eq. (5.12) which is
non-Gaussian.
