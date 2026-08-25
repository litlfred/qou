---
doc_id: arxiv-2410.20973v1
doc_title: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS"
section_id: sec-003-13-proving-borellaplace-summability
section_title: "Proving Borel–Laplace summability"
section_number: 1.3
pages: 5-8
source_pdf: 2410.20973v1.pdf
source_sha256: 852b7bbc81a62883
doc_brief: "SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS — We prove conjectures of Garoufalidis-Gu-Mari˜ no [ 9] that perturbative series associated with the hyperbolic knots 4 1 and 5 2 are resurgent and"
---
the process of resurgence requires convergence and then analy tic continuation of the series’s
Borel transform [ 5, 20]. Recall that the Borel transform B is deﬁned as the formal inverse
of the Laplace transform
Lϑ(φ) :=
∫ eiϑ∞
0
e−ζ/ℏφ(ζ) dζ , (17)
6 VERONICA F ANTINI AND CAMPBELL WHEELER
where ϑ ∈ [0, 2π). More precisely, the Borel transform maps Gevrey-1 formal se ries to
convergent power series in a neighbourhood of the origin
B :
∑
n≥1
anℏn∈ C[ [ℏ] ] ↦→
∑
n≥1
an
n! ζ n−1∈ C{ζ} , (18)
where|an|≤ CA nn! for some constants A, C > 0.
When the analytic continuation of the Borel transform has good gr owth conditions at
inﬁnity, its Laplace transform in the direction ϑ is well deﬁned and gives an analytic function,
which is called the Borel–Laplace sum of the series sϑ :=Lϑ◦B . As the argument ϑ varies,
the resummation sϑ can jump at Stokes rays deﬁned by rays from the origin with arguments
agreeing with that of singularities in Borel plane. Following ´Ecalle’s formalism [ 5, 20], the
Stokes automorphism Sϑ associated to each Stokes ray is deﬁned by comparing two later
Borel–Laplace sums
sϑ+ = sϑ−Sϑ (19)
where ϑ± = ϑ± ǫ for some small ǫ. When the diﬀerence of the two lateral Borel–Laplace
sum of ϕ is given by a transseries like
sϑ+ϕ− sϑ−ϕ =
∑
arg(ω)=ϑ
Sωe−ωτ sϑ−(ϕω) (20)
where Sω∈ C, and ϕω∈ C[ [τ −1] ] are the secondary resurgent series arising at the singularity ω
(see for example [ 9, Sec. 5]). Then the Stokes automorphism allows the computation of the
Stokes constants Sω. Indeed, by factorising Sϑ into automorphisms associated to each
singularity ω in various orders, we can compute the so called alien derivatives [ 20, Def. 6.63].
Hence we can compute the Stokes constants Sω from Sϑ. Moreover, it is enough to compute
the Stokes automorphisms between two distinct direction; given tw o such directions ϑ1, ϑ2,
we can write
Sϑ1,ϑ2 =
∏
ϑ∈(ϑ1,ϑ2)
Sϑ . (21)
Therefore, factorising Sϑ1,ϑ2 into Sϑ and the previous remarks allow us to compute the
individual Stokes constants. This formalism is closely related to the a nalytic wall-crossing
structure of Kontsevich–Soibelman [ 19].
When the Borel–Laplace sum exists, it has uniform asymptotics as |τ|→∞ for arg( τ )
contained in an interval of length greater than or equal to π. Conversely, an analytic function
with such asymptotic properties is the resummation of its asymptot ics [ 21]. Indeed, the
analytic continuation of the Borel transform can be explicitly compu ted using Mordell’s
formula for the inverse Laplace transform [ 23]. Using this method and Theorem 1.2 we can
deduce that Faddeev’s quantum dilogarithm is the resummation of its asymptotics.
Corollary 1.3. The Borel–Laplace sum of Ψ( z;−2πi/τ ) in the direction ϑ is given by
µ8~q−1/24q1/24Φ( zτ ; τ )
• for arg( z + 1) + π
2 < ϑ < arg(z) + π
2 with Im( z)≥ 0,
• and for arg( z)− π
2 < ϑ < arg(z + 1)− π
2 with Im( z)≤ 0.
Proof. By deﬁnition, if z∈ C\(R≤−1∪ R≥0) then z∈ Cπ. Then the ﬁrst time the branch
cuts of Dθ intersect the point z are located at θ = arg(±(z + 1)) and θ = arg(±z). From
SUMMABILITY FOR STATE INTEGRALS OF HYPERBOLIC KNOTS 7
Theorem 1.2, the function Φ( zτ ; τ ) therefore has uniform asymptotics for arg( z + 1) < θ <
arg(z) + π or arg( z)− π < θ < arg(z + 1) depending on the sign of Im( z). □
The same method can also be used to prove that exponential integr als along their steepest
descent contours are the Borel–Laplace sum of their asymptotics (a diﬀerent proof is given
in [ 7]). Thus, given that Φ Ξ is deﬁned by formal Gaussian integration, one might expect
that a similar argument would work for the state integrals in Equation (13). However, the
state integrals’ contours are not deﬁned on Σ or on the Riemann su rface of the dilogarithm.
Moreover asymptotically, Faddeev’s quantum dilogarithm chooses b ranch cuts of the dilog-
arithm. Therefore, trying to deform state integrals into thimble int egrals cannot always be
done. To remedy this, we make the crucial observation that the int egrands of diﬀerent Im,ℓ
can have the same leading asymptotics depending on the branching o f Dθ. This allows us
to patch together a variety of integrals that follow the contour of steepest descent up to a
ﬁnite collection of extra integrals (we will call tails). The asymptotics of these ﬁnitely many
integrals can again be represented as a collection of state integrals up to a ﬁnite collection
of new tails. This process can be repeated and proved to eventually terminate, which hap-
pens when the tails have a (relatively) exponentially small contributio n. This leads to our
following main result.
Theorem 1.4. The asymptotic series Φ Ξ (−2πi/τ ) are Borel–Laplace summable with Stokes
rays on the countable set of rays τ∈S (V0) with two accumulation points at arg(τ ) = ± π
2 .
Moreover, there is an algorithm to compute the Borel–Laplac e resummation away from Stokes
rays, which gives rise to a Z[q±]-linear combination of state integrals Im,ℓ(τ ) for Re(τ ) > 0
andI −
m,ℓ(τ ) for Re(τ ) < 0.2
Remark 1.5. All of the proofs and statements work perfectly well for Re( τ ) < 0. To
avoid cluttering the notation we only give the details for Re( τ ) > 0. To deal with the case
Re(τ ) < 0 one would need to use the additional function
Φ −(z; τ ) = Φ( −z + 1 + τ ;−τ )−1 = (qe(−z); q)∞
(e(z/τ );~q)∞
. (22)
The function µ8~q−1/24q1/24Φ −(zτ ; τ ) gives the resummation of Ψ( z;−2πi/τ ) for some ϑ∈
(−π/2, π/2). The function Φ − comes with its own state integrals
I −
m,ℓ(τ ) := µB
8~q−B/24qB/24
∫
J −
ℓ,τ
Φ −((z− ℓ)τ ; τ )Be
( A
2 z(zτ + τ + 1) + mzτ
)
dz , (23)
whereJ −
ℓ,τ := ( i√−τ eiAǫR≥0 + 1
2 + ℓ)∪ ( i√−τ e+i(A−B)ǫR≤0 + 1
2 + ℓ) for some small ǫ > 0.
We can use Theorem 1.4 to describe the full resurgent structure for our examples. First ,
notice that there are max {A, B} critical points. One can also see that there are exactly
max{A, B}2 independent state integrals and asymptotic series. Indeed, cons ider the family
of asymptotic series
Φ Ξ ,j(ℏ) =
∫
Cp0
Ψ( z, ℏ)B exp
(
− A
2ℏ (2πi)2z
(
z + 1− ℏ
2πi
)
+ (2πi)2 m0z
ℏ + 2πizj
)
dz , (24)
2See Remark 1.5 or Equation ( 23) for a deﬁnition.
8 VERONICA F ANTINI AND CAMPBELL WHEELER
and collect all these asymptotic series into one matrix
(ˆΦ j(ℏ))ℓ,p0 = Φ (A,B,p0),j+ℓ(ℏ) . (25)
Then from Theorem
1.4, we know that this whole matrix of asymptotic series is resummable
for ϑ∈ arg(C\(∪p0S(V0))) to a matrix we denote ˆIj,ϑ(τ ). We show that this matrix is
invertible in Corollary A.2. Moreover, the theorem implies that the entries of this matrix
consist of ﬁnite Z[q]-integral combinations of state integrals. Therefore, for ϑ1, ϑ2∈ ( π
2 , 3π
2 )∩
arg(C\(∪p0S(V0))) we ﬁnd that
ˆIj,ϑ2(τ ) = ˆIj,ϑ1(τ )Sϑ1,ϑ2(q) where Sϑ1,ϑ2(q)∈ GLmax{A,B}(Z[q±]) . (26)
Moreover, for ϑ1 < ϑ 2 < ϑ 3 we have
Sϑ1,ϑ2(q)Sϑ2,ϑ3(q) = Sϑ1,ϑ3(q) . (27)
In Section 4, we will compute a couple of Stokes constants explicitly using the algo rithm
of Section 3.1. However, as will be clear to the reader this is not an eﬃcient method of
computation for ϑ near± π
2 . The method is extremely eﬀective when ϑ is near 0 , π as the
algorithm terminates almost immediately. Therefore, armed with The orem 1.4 and an easy
computation when ϑ is near 0 , π, we can compute the other Stokes constants using the
methods of [ 9]. This involves computing the Stokes automorphism for a small ǫ > 0
S+(q) = Sπ+ǫ,ǫ(q)∈ GLmax{A,B}(Z[q−1][ [q] ]),
S−(q) = Sǫ,−π+ǫ(q)∈ GLmax{A,B}(Z[q][ [q−1] ]). (28)
These series then store all the information of the Stokes constan ts. This allows for a complete
computation of the Stokes constants with proofs.
This paper is organised as follows. In Section 2 we deﬁne the geometric setting, namely a
relative homology to which both the class of thimbles and of state inte grals contours belong.
Section 3 is dedicated to the proof of our main results. More precisely, in Sect ion 3.1 we
illustrated the algorithm that leads to the proof of Theorem 1.4 in Section 3.2. Finally in
Section 4, we illustrate the algorithm in two examples: the case ( A, B) = (1 , 2) corresponding
to the 4 1 knot in Section 4.1, and the case ( A, B) = (4 , 1) in Section 4.2. As a result of the
decomposition into state integrals, we verify the numerical comput ations of the ﬁrst Stokes
constants [ 9, 24] in both examples. There are two appendices.
