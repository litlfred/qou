---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-009-6-conclusion
section_title: "Conclusion"
section_number: 6
pages: 19-31
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
---
In this paper, we discuss about q-deformed Plancherel growth of Young diagrams. We
construct a unitary matrix model that captures the growth of Young diagrams with the
19
coupling constant playing the role of time [9]. The matrix model is a q analog of GWW
model and the growth of Young diagrams equipped with aq-deformed Plancherel measure is
captured by the no-gap phase of this model. The q-deformed limit shape is the q-deformed
GWW transition point. We use the connection between unitary matrix model and 2D
droplet picture of [6, 8] to construct the unitary matrix model. Construction of this matrix
model allows us to map the automodel diagrams to diﬀerent shapes of the 2D droplets. Upon
quantising the droplets, one can construct a Hilbert space and the automodel diagrams can
be mapped to coherent states in that Hilbert space. We study two diﬀerentq-deformations of
the Plancherel measure. One follows from the Iwahori-Hecke algebras, considered in [9, 18].
In this case, the measure is proportional to a product of q-deformed dimension and ordinary
dimension of the representation. The other kind of q-deformed measure is proportional to
the square of q dimension. Such measure appears in diﬀerent contexts in topological string
theories and gauge theories. We see that in the large N limit, the later can be solved
exactly in the deformation parameter, while we do a perturbative analysis of the former.
However, the automodel diagrams in either case have the same qualitative behaviour for
small deformation.
We compute the moments of diﬀerent automodel diagrams explicitly and show that these
moments are related to the inﬁnite number of commuting conserved charges associated with
the one matrix model. The moments of Young diagrams can be obtained from the large h
expansion of resolvent. Since the saddle point technique allows us to compute the resolvent
exactly in λ, in the large N limit, we have been able to compute the moments of automodel
diagrams explicitly.
Acknowledgments: The work of SD is supported by the MATRICS grant no.
MTR/2019/000390 from the Department of Science and Technology, Government of India.
DM, N and SP acknowledge many illuminating discussions with Arghya Chattopadhyay.
Neetu would like to thank Arindam Bhattacharya for many fruitful discussions over the
course of this work. We also thank all the medical and non-medical workers who are working
tirelessly in these troubled times. Finally, we are grateful to the people of India for their
unconditional support towards researches in basic sciences.
Appendix A. q analog of GWW phase transition
The no-gap phase of theq-deformed Plancherel growth process captured by the partition
function (3.3) has been discussed in section 3.1. There exist another class of solution for the
saddle point equation (3.13), namely the one-gap solution for which
0≤u(h)< 1 for h∈ [a,b ] . (A.1)
To solve the saddle point equation for this case, we deﬁne new variables
z = 1−e−λh
λ (A.2)
20
in terms of which the equation becomes
−
∫ zq
zp
dz′ u(z′)
z−z′ = 1
(1−λz) log
(z
ξ
)
(A.3)
where za and zb correspond to points a and b in the h plane. The resolvent for the above
integral equation is given by
H(z) =−
√
(z−za)(z−zb)
∮
C
ds
2πi
log(s/ξ)
(1−λs)(s−z)
√
(s−za)(s−zb)
(A.4)
where similar to the previous cases, the contour C encloses the branch cut between za and
zb. We deform the contour as shown in ﬁg 3. Taking contributions from all the poles and
the logarithmic branch cut, the resolvent is ﬁnally given by
H(z) =− 2
(1−λz) log


(√
za(zb−z)−i
√
zb(z−za)
)√ξ
z(√zb−z−i√z−za)


− 2λ
(1−λz)
√
(z−za)(z−zb)√
(1−λza)(1−λzb)
log
[√
za(1−λzb)−
√
zb(1−λza)(√1−λzb−√1−λza
)√ξ
] (A.5)
The discontinuity of the resolvent gives
u(z) = 1
π(1−λz) cos−1
[4√zazb(z−za)(zb−z) + (za +zb− 2z)(2zazb−zza−zzb)
(zb−za)2z
]
(A.6)
The support of u(z) is given by
√za =e−λ/2√
ξ− e−λ/2
√
−e−λ/2 +eλ +λξ−e−λ/2λξ√
λ
√zb =e−λ/2√
ξ + e−λ/2
√
−e−λ/2 +eλ +λξ−e−λ/2λξ√
λ
(A.7)
In terms of our original variable h, we have
u(h) = 1
π cos−1
[1 +eλe−2λh− 2eλ/2e−λh(1 +λξ) +λξ(2e−λh +λξ)
2λ(1−e−λh)ξ
]
. (A.8)
Inverting this relation with the help of the identiﬁcation (3.40), we ﬁnd
h+(θ) =
log
(
−λξ cos(θ)+
√
λξ(cos(θ)+1)(λξ(cos(θ)+1)−2eλ/2(λξ+1)+2eλ)−λξ+eλ/2(λξ+1)
−2λξ cos(θ)+λ2ξ2+1
)
λ
h−(θ) =
log
(
λξ cos(θ)+
√
λξ(cos(θ)+1)(λξ(cos(θ)+1)−2eλ/2(λξ+1)+2eλ)+λξ−eλ/2(λξ+1)
2λξ cos(θ)−λ2ξ2−1
)
λ .
(A.9)
Now using the mapping (3.38), we ﬁnd S(θ) which matches with (3.42).
21
Appendix B. Explicit computation of the partition function
Here, we provide some details of the computation for the partition function (4.1) that
follows if one takes the q-deformed Plancherel measure following Strahov [9]. The partition
function can be written as
Zq =
∞∑
k=1
∑
{hi}
exp [k lnt +k ln(1−q) +b(λk) lnq + lnk!]
exp
[
ln
∏
1≤i<j≤N
(hi−hj)− ln
N∏
i=1
hi! + ln
∏
1≤i<j≤N
[hi−hj]− ln
N∏
i=1
[hi]!
]
.
(B.1)
The total number of boxes in a Young diagram can be expressed as
k =
N∑
i=1
λi =
N∑
i=1
(hi−N +i) =
N∑
i=1
hi− N(N− 1)
2 . (B.2)
We will now write down the above in the large N limit. Large N naturally implies large k
which is an O(N 2) number. We can also write
b(λk) =
N∑
i=1
(i− 1)(hi−N +i) =
N∑
i=1
(i− 1)hi− N(N− 1)(N− 2)
6 . (B.3)
Using Stirling’s approximation, the partition function in the large N limit becomes
Zq≈
∞∑
k=1
∑
λk
exp
[
k lnt(1−q) +
N∑
i=1
(i− 1)hi lnq +k lnk−k + 1
2
∑
1≤i⁄=j≤N
ln|hi−hj|
−
N∑
i=1
(hi lnhi−hi) +
∑
1≤i<j≤N
ln[hi−hj]−
N∑
i=1
ln[hi]!
]
exp
[
−lnq
6 N(N− 1)(N− 2)
]
.
(B.4)
We can simplify the last two terms appearing in the exponent of above expression as follows:
∑
1≤i<j≤N
ln[hi−hj] =
∑
1≤i<j≤N
ln(1−qhi−hj) =
∑
1≤i<j≤N
(
ln(qhj−qhi)−hj lnq
)
= 1
2
∑
1≤i⁄=j≤N
ln|qhj−qhi|−
N∑
i=1
(i− 1)hi lnq
(B.5)
and
N∑
i=1
ln[hi]! =
N∑
i=1
hi∑
j=1
ln[j] =
N∑
i=1
hi∑
j=1
ln(1−qj) . (B.6)
22
Using (B.5) and (B.6) in the expression of the partition function, we end up with
Zq≈
∞∑
k=1
∑
λk
exp
[
k lnt(1−q) +k lnk−k +
∑
1≤i⁄=j≤N
1
2 ln|hi−hj|−
N∑
i=1
(hi lnhi−hi)
+
∑
1≤i⁄=j≤N
1
2 ln|qhj−qhi|−
N∑
i=1
hi∑
j=1
ln(1−qj)
]
exp
[
−lnq
6 N(N− 1)(N− 2)
]
.
(B.7)
Appendix C. Calculation of automodel density for the second class ` a la Strahov
Here, we give details of derivation for the solution of (4.6). The ﬁrst term in the kernel,
namely coth λ(h−h′)
2 has a series representation of the form
cothλ(h−h′)
2 = 2
λ(h−h′) + 2
∞∑
k=1
B2kλ2k−1
(2k)! (h−h′)2k−1, (C.1)
clearly demonstrating that there is a singularity in the ﬁrst term above as h′→h. However,
the second term is well behaved for any real h′. Motivated by this observation, we deﬁne
the function
G(h)≡
∫ b
a
dh′ ˜u(h′)
[
cothλ(h−h′)
2 − 2
λ(h−h′)
]
. (C.2)
Note that in the above deﬁnition, the integral kernal has been precisely deﬁned so as to
remove any singularities. Further, since we are looking for ˜ u(h) that are analytic within
its region of support, it is expected that the function G(h) as deﬁned above will be “well-
behaved”. This motivates us to make the assumption that under complexiﬁcation, the
function will be analytic in the annulus where a< |h|<b . One can easily see that asymp-
totically,
G(h)
h→∞
−−−→1− 2
λh− 2
λh2
(
k′ + 1
2
)
+O
( 1
h3
)
. (C.3)
Note that without knowing the function ˜u(h) we cannot write an expression forG(h). How-
ever, plugging in (C.1) in (4.6), we get,
−
∫ b
a
dh′ ˜u(h′)
[
1
h−h′ + 1
2
∞∑
k=1
B2kλ2k
(2k)! (h−h′)2k−1
]
= λ
4 (1−a) + 1
2 ln 1−e−λ(h−a)
λ(h−a) + lnh−a
ξ .
(C.4)
The second term appearing on the LHS of the above equation can be represented as follows:
1
2
∞∑
k=1
B2kλ2k
(2k)! −
∫ b
a
dh′ ˜u(h′)(h−h′)2k−1 = 1
2
∞∑
k=1
B2kλ2k
(2k)!
∫ b
a
dh′ ˜u(h′)(h−h′)2k−1
= 1
2
∞∑
k=1
B2kλ2k
(2k)!
2k−1∑
n=0
(2k− 1
n
)
h2k−n−1(h−a)n
(C.5)
23
where
hn≡
∫ b−a
0
˜u(h′ +a)h′n dh′. (C.6)
In writing the ﬁnal line in (C.5), we ﬁrst made the substitution h′→ h′−a followed by a
binomial expansion which brings in a second sum running from 0 to 2 k− 1. We perform
these operations simply for computational convenience later. Note that the quantity hn
appearing in (C.6) are something that we will henceforth refer to as translated moments, are
actually diﬀerent from the moments of the solution ˜u(h).
Finally, the integral equation we require to solve takes the form
−
∫ b
a
dh′ ˜u(h′)
h−h′ = lnh−a
ξ + λ
4 (1−a) + 1
2 ln 1−e−λ(h−a)
λ(h−a)
− 1
2
∞∑
k=1
B2kλ2k
(2k)!
2k−1∑
n=0
(2k− 1
n
)
h2k−n−1(h−a)n.
(C.7)
The resolvent corresponding to the above integral equation is given by
H(h) = ln h
h−a−
√
(h−a)(h−b)
∮
C
ds
2πi
ln s−a
ξ
(s−h)
√
(s−a)(s−b)
−
√
(h−a)(h−b)
∮
C
ds
2πi
λ
4(1−a)
(s−h)
√
(s−a)(s−b)
−
√
(h−a)(h−b)
∮
C
ds
2πi
1
2 ln 1−e−λ(s−a)
λ(s−a)
(s−h)
√
(s−a)(s−b)
−
√
(h−a)(h−b)
∮
C
ds
2πi
− 1
2
∑∞
k=1
B2kλ2k
(2k)!
∑2k−1
n=0
(2k−1
n
)
h2k−n−1(s−a)n
(s−h)
√
(s−a)(s−b)
(C.8)
where the contourC encloses the branch cut in the interval [a,b ] on the real axis (as depicted
below).
Figure C.6: The contour C over which the resolvent (C.8) is deﬁned encloses the branch cut over the real
interval [a,b ]. ContourC is composed of four smaller compenents, namely γ+,γ−,Ca andCb.
24
The integral apearing in the ﬁrst line above in (C.8), is in fact identical to the GWW
solution and was evaluated in [6]. Thus, using the result from [6], the resolvent simpliﬁes to
H(h) = lnh
ξ + ln
√
b−√a√
b +√a
+ lnh +
√
ab−
√
(h−a)(h−b)
h−
√
ab +
√
(h−a)(h−b)
+Hconst(h) +Hλ(h) +Hseries(h)
(C.9)
where the terms Hconst(h),Hλ(h) and Hseries(h) each correspond to the second, third and
fourth line appearing in (C.8).
Unlike the method employed in [6], we will not be blowing up the countour and extending
to inﬁnity in order to evaluateHconst(h),Hλ(h) andHseries(h) but rather compute it directly
through an appropriate choice of parametrization of the integration variables. See Appendix
C.1 for details of the computation. After evaluating all the contour integrals, the ﬁnal
expression of resolvent is given by
H(h) = lnh
ξ + ln
√
b−√a√
b +√a
+ lnh +
√
ab−
√
(h−a)(h−b)
h−
√
ab +
√
(h−a)(h−b)
+ λ
4 (1−a) +
∞∑
k=1
A(1)
k
√
(h−a)
(h−b)
+
∞∑
k=1
A(2)
k
2F1(1, 1
2 +k, 2 +k, a−b
a−h)√
(h−a)(h−b)
+
∞∑
k=1
2k−1∑
n=1
A(1)
k,n
√
(h−a)
(h−b)
+
∞∑
k=1
2k−1∑
n=1
A(2)
k,n
2F1(1, 1
2 +n, 2 +n, a−b
a−h)√
(h−a)(h−b)
,
(C.10)
where
A(1)
k = 1
4√π
λkBk
k.k! (b−a)kΓ(k + 1
2) 2
Γ(k + 1) ,
A(2)
k = − 1
4√π
λkBk
k.k! (b−a)k+1Γ(k + 1
2) ,
A(1)
k,n = − 1
4√π
λ2kB2k
2k!
(2k− 1
n
)
h2k−n−1(b−a)nΓ(n + 1
2) 2
Γ(n + 1)
A(2)
k,n = 1
4√π
λ2kB2k
2k!
(2k− 1
n
)
h2k−n−1(b−a)n+1Γ(n + 1
2). (C.11)
Appendix C.1. Computing Hconst(h),Hλ(h) and Hseries(h)
In order to perform the contour integrals in (C.8), one needs to reparametrize the inte-
gration variables ass =a +xeiϵ alongγ+ ands =a +xei(2π−ϵ) alongγ−. It can be further
demonstrated that the contribution to this integral coming from the parts Ca andCb i.e.
two inﬁnitesimal circles centered around a and b vanishes in the limit when the radii of the
circles are taken to zero.
Carrying out the above procedure, we get
Hconst(h) =−
√
(h−a)(h−b)
∮
C
ds
2πi
λ
4(1−a)
(s−h)
√
(s−a)(s−b)
= λ
4 (1−a). (C.12)
25
For the next term, we get,
Hλ(h) =−
√
(h−a)(h−b)
∮
C
ds
2πi
1
2 ln 1−e−λ(s−a)
λ(s−a)
(s−h)
√
(s−a)(s−b)
=−
√
(h−a)(h−b)
2
∞∑
k=1
λkBk
(k).(k)!
∮
C
ds
2πi
(s−a)k
(s−h)
√
(s−a)(s−b)
.
(C.13)
In writing the above line, we have used the expansion
ln 1−e−λ(s−a)
λ(s−a) =
∞∑
n=1
λnBn
(n).(n)!(s−a)n . (C.14)
Simplifying the above integrals, we get eventually
Hλ(h) =−
√
(h−a)(h−b)
2π
∞∑
k=1
λkBk
(k).(k)!
∫ b−a
0
dx xk
(x +a−h)
√
x(b−a−x)
=−
√
(h−a)(h−b)
4√π
∞∑
k=1
λk(b−a)kBk
(b−h)(k).(k)!Γ(k + 1
2)
[ 2
Γ(k + 1) +
(b−a
a−h
)
.2F1(1, 1
2 +k, 2 +k, a−b
a−h)
]
.
(C.15)
A similar exercise on Hseries(h) yields:
Hseries(h) =−
√
(h−a)(h−b)
∮
C
ds
2πi
− 1
2
∑∞
k=1
B2kλ2k
(2k)!
∑2k−1
n=0
(2k−1
n
)
h2k−n−1(s−a)n
(s−h)
√
(s−a)(s−b)
=
√
(h−a)(h−b)
2 ·
∞∑
k=1
B2kλ2k
(2k)!
2k−1∑
n=0
(2k− 1
n
)
h2k−n−1×
∮ ds
2πi
(s−a)n
(s−h)
√
(s−a)(s−b)
=
√
(h−a)(h−b)
4√π
1
(b−h)·
∞∑
k=1
B2kλ2k
(2k)!
2k−1∑
n=0
(2k− 1
n
)
h2k−n−1(b−a)n×
Γ
(
n + 1
2
)[ 2
Γ(n + 1)− a−b
a−h· 2F1
[
1,n + 1
2;n + 2;a−b
a−h
]]
.
(C.16)
Appendix D. Droplet quantisation
The droplet picture, discussed in section 3.3, has no dynamics. Diﬀerent large N phases,
obtained by solving the saddle point equation, are possible minimum free energy conﬁgura-
tions of the model. Hence the corresponding droplets are static - the shapes are not changing
26
with time. To incorporate dynamics into the picture, we follow an ad-hoc way : identify the
largeN droplets with Thomas-Fermi distribution at zero temperature and obtain the single
particle Hamiltonian by comparing the two. In this way it is possible to incorporate time in
our system.
Comparing the phase space distribution function (3.35) with Thomas-Fermi distribution
function, we get
h(h,θ ) = h2
2 −S(θ)h + g(θ)
2 +µ, where g(θ) =h+(θ)h−(θ). (D.1)
The above Hamiltonian is not in diagonal form. Deﬁning a new variable
¯h =h−S(θ). (D.2)
the single particle Hamiltonian density is given by
h(¯h,θ ) =
¯h2
2 − π2
2 ρ(θ)2 (D.3)
and the droplet boundary is given by
¯h±(θ) =±πρ(θ). (D.4)
The phase space Hamiltonian can be calculated by integrating (D.3) over ¯h from ¯h−(θ) to
¯h+(θ) and is given by
Hh = 1
3πℏ
∫
dθ π3ρ(θ)3 (D.5)
where ℏ = 1/N is the minimum accessible area in phase space. The phase space boundary
is doubly degenerate, i.e. for a given θ there are two boundaries, ¯h± corresponding to two
signs on the right hand side of (D.4). Hence, we write the Hamiltonian (D.5) over the two
segments of droplets [25]
Hh = 1
6πℏ
[∫
+
dθ ¯h3
+(t,θ )−
∫
−
dθ ¯h3
−(t,θ )
]
. (D.6)
From the single particle Hamiltonian (D.3), we ﬁnd that the equations of motion satisﬁed
by the droplet boundaries are given by 3
˙¯h±(t,θ ) = ¯h±(t,θ )¯h′
±(t,θ ) (D.8)
3Equations of motion from (D.3) are given by
˙¯h(t) =−∂h
∂θ =π2ρ(θ)ρ′(θ), ˙θ(t) = ∂h
∂¯h = ¯h(t) (D.7)
Substituting the boundary relations (D.4) in these equations, one ﬁnds (D.8).
27
where the dot and prime denote derivative with respect to t and θ respectively.
In order to quantise the droplets, we ﬁnd a simplectic form such that the Hamilton’s
equation
˙¯h±(t,θ ) ={¯h±(t,θ ),Hh} (D.9)
would coincide with (D.8) [25, 26]. To achieve this, we introduce Poisson brackets between
¯h±(t,θ ) and ¯h±(t,θ′)
{¯h±(t,θ ), ¯h±(t,θ′)} =±πℏδ′(θ−θ′) and {¯h+(t,θ ), ¯h−(t,θ′)} = 0. (D.10)
It is easy to check that using these Poisson brackets, equation (D.9) boils down to (D.8).
The circular droplet (ρ(θ) = 1
2π) corresponds to ¯h±(t,θ ) =± 1
2 and satisfy the classical
equations of motion (D.8). We consider quantum ﬂuctuations about this classical circular
droplet
¯h±(t,θ ) =±1
2 + ℏ ˜h±(t,θ ). (D.11)
We also assume that the ﬂuctuations preserve the total area of the droplet. This implies
∫ π
−π
dθ(˜h+(t,θ )− ˜h−(t,θ )) = 0. (D.12)
To quantise the above classical system, we promote the Poisson brackets (D.10) to com-
mutation relations
[
˜h±(t,θ ), ˜h±(t,θ′)
]
=±πiδ′(θ−θ′) and [ ˜h+(t,θ ), ˜h−(t,θ′)] = 0. (D.13)
We decompose ˜h±(t,θ ) into Fourier modes
˜h+(t,θ ) =
∞∑
n=−∞
a−n(t)einθ, and ˜h−(t,θ ) =−
∞∑
n=−∞
bn(t)einθ. (D.14)
From the constraint equation (D.12), we see that the zero-modes a0 and b0 are equal up to
a sign
a0 =−b0 =π0. (D.15)
It follows from equation (D.13) that the Fourier modes an andbn satisfy a U(1) Kac-Moody
algebra
[am(t),an(t)] = 1
2mδm+n, [bm(t),bn(t)] = 1
2mδm+n, and [ am(t),bn(t)] = 0. (D.16)
Since ˜h±(t,θ ) are real, we have a−n =a†
n and b−n =b†
n. The Hamiltonian (D.6) in terms of
these modes is given by (up to over all constant factors)
˜H =H+ +H− (D.17)
28
where
H+ = ℏ
2a2
0 + ℏ2
3 a3
0− ℏ2
24a0 + ℏ(1 + 2ℏa0)
∑
n>0
a†
nan
+ ℏ2
∑
m,n>0
(
a†
m+naman +h.c.
) (D.18)
and H− has a similar expression in terms of modes bn’s.
Since π0 commutes with all the an,bn and hence with ˜H, application of ans and bns can-
not change the eigenvalue of π0. Therefore, the Hilbert space is constructed upon a one
parameter family of vacua|s,s
⟩
≡|s
⟩
, where
an|s
⟩
= 0, b n|s
⟩
= 0 for n> 0
and a0|s
⟩
=−b0|s
⟩
=π0|s
⟩
=s|s
⟩
. (D.19)
Starting with the primary|s
⟩
we can now construct a Hilbert spaceH which is ans charged
module. Let us denote by H+ andH− as Hilbert spaces associated with a and b sectors
respectively. The commutativity of a and b operators implies that the full Hilbert space is
factorizable intoH+ andH− i.e.H =H+⊗H−.
A generic excited state in H is given by
|⃗k,⃗l
⟩
=
∞∏
n,m=1
(
a†
n
)kn(
b†
m
)lm
|s
⟩
. (D.20)
The vectors⃗k and⃗l correspond to excitations in the upper and lower Fermi surfaces. Since
an and bn commute, a generic excitation |⃗k,⃗l
⟩
∈H can be written as a direct product of
states belonging to the two sectors i.e. |⃗k,⃗l
⟩
=|⃗k
⟩
⊗|⃗l
⟩
.
The excited states inH+ are orthogonal with the normalization
⟨⃗k′|⃗k⟩ =z⃗kδ⃗k⃗k′ where z⃗k =
∏
j
kj!
(j
2
)kj
(D.21)
and has π0 eigenvalues. They also satisfy the completeness relation
∑
⃗k
1
z⃗k
|⃗k
⟩⟨⃗k| = IH+ (D.22)
and hence form a basis in H+. The particle like excited states |⃗k
⟩
in either sectors are
eigenstates of the free Hamiltonian of the corresponding sectors
H±
free|⃗k
⟩
= ℏ(1± 2sℏ)
( ∞∑
n=1
nkn
)
|⃗k
⟩
, (D.23)
29
but not an eigenstate of the full Hamiltonian. The interaction Hamiltonian is such that its
action on an excited state doesn’t change the level of the state. Explicitly stated, the inter-
action Hamiltonian takes a state|⃗k
⟩
to|⃗k′⟩
satisfying∑
nnkn =∑
nnk′n. The expectation
value of ¯h+(t,θ ) operator in |⃗k
⟩
state is (1/2 + ℏs). The quantum dispersion, ∆ ¯h+ in|⃗k
⟩
state is O(ℏ) and hence a generic|⃗k
⟩
state can be interpreted as quantum ﬂuctuations over
the ground state.
A generic coherent state in H+ can be deﬁned as
|τ+
⟩
= exp
( ∞∑
n=1
2τ +
na†
n
nℏ
)
|s
⟩
. (D.24)
The state|τ+
⟩
is not normalised. The normalization is given by
⟨
τa
+|τb
+
⟩
= exp
(∑
n
4τa
n+τb
n+
nℏ2
)
. (D.25)
The coherent state|τ+
⟩
is an eigenstate of an (∀n >0) with eigenvalue τ +
n/ℏ. A coherent
state|τ+
⟩
can be expanded in |⃗k
⟩
basis in the following way
|τ+
⟩
=
∑
⃗k
τ +
⃗k
z⃗k
|⃗k
⟩
, where τ +
⃗k =
∏
m
(τ +
m
ℏ
)km
. (D.26)
The expectation value of ¯h+ in a coherent state|τ+
⟩
is given by
ωτ+(z) =
⟨
τ+|
¯h+(z)
π |τ+
⟩
⟨
τ+|τ+
⟩ = 1
2π + sℏ
π + 1
π
∑
n>0
τ +
n
(
zn + 1
zn
)
. (D.27)
Value ofωτ+(z) on a unit circle (|z| = 1) in the complex z plane is given by
ωτ+(θ)≡ωτ+(z =eiθ) = 1
2π + sℏ
π + ˜ωτ+(θ)
where ˜ωτ+(θ) = 2
π
∑
n>0
τ +
n cosnθ.
(D.28)
Since the quantum dispersion of ¯h+ in a coherent state is zero, we call such states classical.
References
[1] A. Chattopadhyay, S. Dutta, D. Mukherjee, and Neetu, “Quantum Mechanics of Plancherel Growth,”
2019, 1909.06797.
[2] B. Eynard, “All orders asymptotic expansion of large partitions,” J. Stat. Mech. , vol. 0807, p. P07023,
2008, 0804.0381.
30
[3] A. Vershik and S. Kerov, “Asymptotics of the Plancherel measure of the symmetric group and the
limiting form of Young tableaux,” Dokl. Akad. Nauk , vol. 233, pp. 1024–1027, 1977.
[4] B. Logan and L. Shepp, “A variational problem for random Young tableaux,” Advances in Mathematics,
vol. 26, pp. 206–222, 1977.
[5] S. V. Kerov, “A Diﬀerential Model Of Growth Of Young Diagrams,” Proceedings of St.Petersburg
Mathematical Society, 1996.
[6] S. Dutta and R. Gopakumar, “Free fermions and thermal AdS/CFT ,” JHEP, vol. 03, p. 011, 2008,
0711.0133.
[7] P. Dutta and S. Dutta, “Phase Space Distribution of Riemann Zeros,” J. Math. Phys. , vol. 58, no. 5,
p. 053504, 2017, 1610.07743.
[8] A. Chattopadhyay, P. Dutta, and S. Dutta, “Emergent Phase Space Description of Unitary Matrix
Model,” JHEP, vol. 11, p. 186, 2017, 1708.03298.
[9] E. Strahov, “A diﬀerential Model for the Deformation of the Plancherel Growth Process,” arXiv e-
prints, p. arXiv:0706.3292, Jun 2007, 0706.3292.
[10] N. Caporaso, L. Griguolo, M. Marino, S. Pasquetti, and D. Seminara, “Phase transitions, double-scaling
limit, and topological strings,” Phys. Rev. D , vol. 75, p. 046004, 2007, hep-th/0606120.
[11] N. Nekrasov and A. Okounkov, “Seiberg-Witten theory and random partitions,” Prog. Math., vol. 244,
pp. 525–596, 2006, hep-th/0306238.
[12] N. A. Nekrasov, “Seiberg-Witten prepotential from instanton counting,” Adv. Theor. Math. Phys. ,
vol. 7, no. 5, pp. 831–864, 2003, hep-th/0206161.
[13] M. Marino, “Open string amplitudes and large order behavior in topological string theory,” JHEP,
vol. 03, p. 060, 2008, hep-th/0612127.
[14] A. Okounkov, “The uses of random partitions,” in XIVth International Congress on Mathematical
Physics, pp. 379–403, World Scientiﬁc, 2006.
[15] A. Chattopadhyay, S. Dutta, D. Mukherjee, and Neetu, “From 2d Droplets to 2d Yang-Mills,” 10 2020,
2010.11923.
[16] W. Fulton and J. Harris, Representation Theory: A First Course . Graduate texts in mathematics,
Springer, 1991.
[17] S. Kerov, “A q-analog of the hook walk algorithm for random young tableaux,” Journal of Algebraic
Combinatorics, vol. 2, pp. 383–396, 1993.
[18] V. Feray and P.-L. M´ eliot, “Asymptotics of q-Plancherel measures,”arXiv e-prints, p. arXiv:1001.2180,
Jan. 2010.
[19] A. A. Migdal, “Loop Equations and 1/N Expansion,” Phys. Rept., vol. 102, pp. 199–290, 1983.
[20] J. Baik, P. Deift, and K. Johansson, “On the Distribution of the Length of the Longest Increasing
Subsequence of Random Permutations,” arXiv Mathematics e-prints , Oct 1998, math/9810105.
[21] P. Dutta and S. Dutta, “Phase Space Distribution for Two-Gap Solution in Unitary Matrix Model,”
JHEP, vol. 04, p. 104, 2016, 1510.03444.
[22] E. Brezin, C. Itzykson, G. Parisi, and J. B. Zuber, “Planar Diagrams,” Commun. Math. Phys. , vol. 59,
p. 35, 1978.
[23] M. R. Douglas, “Conformal ﬁeld theory techniques in large N Yang-Mills theory,” in NATO Advanced
Research Workshop on New Developments in String Theory, Conformal Models and Topological Field
Theory Cargese, France, May 12-21, 1993 , 1993, hep-th/9311130.
[24] A. Jevicki, “Development in 2-d string theory,” in Workshop on String Theory, Gauge Theory and
Quantum Gravity, 9 1993, hep-th/9309115.
[25] L. Maoz and V. S. Rychkov, “Geometry quantization from supergravity: The Case of ‘Bubbling AdS’,”
JHEP, vol. 08, p. 096, 2005, hep-th/0508059.
[26] L. Grant, L. Maoz, J. Marsano, K. Papadodimas, and V. S. Rychkov, “Minisuperspace quantization of
‘Bubbling AdS’ and free fermion droplets,” JHEP, vol. 08, p. 025, 2005, hep-th/0505079.
31
