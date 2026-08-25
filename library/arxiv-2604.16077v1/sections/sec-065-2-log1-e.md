---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-065-2-log1-e
section_title: "Log(1 −e"
section_number: 2
pages: 49-59
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
1
N Log(u0)+z) + 1
N Ψu0,N (z)
)
where Ψu0,N (z) = ΨN
(1
N Log(u0) +z
)
(see (119)). Using that
Li2
(
e
1
N Log(u0)+z
)
= Li 2 (ez) − Log(u0)
N
∫ 1
0
Log
(
1 −e
Log(u0)
N t+z
)
dt(127)
Log
(
1 −e
Log(u0)
N t+z
)
= Log(1 −ez) − Log(u0)
N ez
∫ t
0
e
Log(u0)
N s
1 −e
Log(u0)
N s+z
ds
we can write
ˆSN
( 1
N Log(u0) +z
)
= exp
(N
2iπ Li2 (ez)
)
exp
(
Tu0,N (z) + 1
N Ψu0,N (z)
)
= exp
(N
2iπ Li2 (ez)
)
exp
(
− 1
2
(
1 + Log(u0)
iπ
)
Log(1 −ez)
)
× exp
( 1
N (Ψu0,N (z) + Iu0,N (z))
)
,
50 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
where
Tu0,N (z) := − N
2iπ Li2 (ez) + N
2iπ Li2
(
e
1
N Log(u0)+z
)
− 1
2 Log(1 −e
1
N Log(u0)+z)
= − 1
2 Log
(
1 −e
1
N Log(u0)+z
)
− Log(u0)
2iπ
∫ 1
0
Log
(
1 −e
Log(u0)
N t+z
)
dt
= − 1
2
(
1 + Log(u0)
iπ
)
Log(1 −ez)
+ Log(u0)
N ez
(
Log(u0)
2iπ
∫ 1
0
(∫ t
0
e
Log(u0)
N s
1 −e
Log(u0)
N s+z
ds
)
dt + 1
2
∫ 1
0
e
Log(u0)
N s
1 −e
Log(u0)
N s+z
ds
)
= − 1
2
(
1 + Log(u0)
iπ
)
Log(1 −ez) + Iu0,N (z)
and
Iu0,N (z) := Log(u0)
N ez
(
Log(u0)
2iπ
∫ 1
0
(∫ t
0
e
Log(u0)
N s
1 −e
Log(u0)
N s+z
ds
)
dt + 1
2
∫ 1
0
e
Log(u0)
N s
1 −e
Log(u0)
N s+z
ds
)
is the last summand of Tu0,N (z) made of the integrals.
By its deﬁnition the function Tu0,N (z) is holomorphic on the domain (121). Then so is
Iu0,N (z). Applying several times the triangle inequality on |Iu0,N (z)|, and using Lemma 3.2
as at the end of Lemma 3.3, we ﬁnd
(128) |Iu0,N (z)| ≤ BM
δ
√
1 − π2
24
for every z ∈] − ∞,M ] + i(2πk + [δ + π
N, 2π − δ − π
N ]), δ ∈]0,π [, k ∈ Z (so that δ ≤
I
(1
N Log(u0)s +z
)
≤ 2π −δ for every s ∈ [0, 1]), where BM > 0 is a constant independent of
N , δ and k.
Step 3: Approximating ∏ N −a0/2
k=1
(
1 −el0,N +z+ 2iπ
N k
)
.
Next consider the product in (122). By factoring out a0/2 terms, and using that l0,N =
−2iπ +ON →∞( 1
N ), for every z ∈CN we get
N −a0/2∏
k=1
(1 −el0,N +z+ 2iπ
N k) =
N∏
k=1
(1 −el0,N +z+ 2iπ
N k)
N∏
k=N +1−a0/2
(1 −el0,N +z+ 2iπ
N k)−1
= (1 −eN (z+l0,N ))
N∏
k=N +1−a0/2
(
1 −ez+ 1
NON→∞(1)
) −1
= (1 −u0eNz )
(
1 −ez+ 1
NON→∞(1)
) −a0/2
= 1 −u0eNz
(1 −ez)a0/2 . 1
(1 − ez
ez−1 . 1
NON →∞(1))a0/2
= 1 −u0eNz
(1 −ez)a0/2
(
1 + 1
NON →∞ (1)
)
,(129)
where the last ON →∞(1) term is a sequence of holomorphic functions on C \ {2iπk,k ∈ Z},
where each singularity 2 iπk is removable, and with moduli bounded from above by some
constant independent of N on any ﬁxed compact subset of C.
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 51
Step 4: Approximating coth
(Nz
2
)
and e
N
2iπ (z2−l1,Nz).
Finally, for every z in CN \ {isN, 2iπ −isN − 2iπ
N } we have
coth
(Nz
2
)
= sign (R(z))
(
1 +oN →∞
( 1
N
))
,
where the oN →∞
(1
N
)
term is a sequence of holomorphic functions on C \ {2iπk,k ∈ Z},
where each singularity 2 iπk is a simple pole, and with moduli bounded from above by some
constant independent of N on any compact subset of this domain.
Moreover, since l1,N = 1
N l′
1 +πia1, with l′
1 = Log(u1) +πia1, and πia1 =ℓ mod(2iπ), with
ℓ ∈ {πi, 2πi}, by the comment after (85) for every z ∈CN we can replace e− N
2iπ l1,Nz with
e− N
2iπ ( 1
N (Log(u1)+πia1)+ℓ)z =e− 1
2iπ (Log(u1)+πia1)ze− N
2iπℓz =e−
l′
1
2iπze− N
2iπℓz.
Step 5: Putting all together towards the RHS.
Recalling the formula (120), the approximations we have obt ained in Steps 2 to 5 imply that
for all z ∈CN one has:
e
N
2iπ (z2−l1,Nz) ˆSN (l0,N +z) coth(Nz
2 )
= sign (R(z)) exp
(N
2iπ
(
Li2 (ez) +z2 −ℓz
) )
(1 −u0eNz )
×ρ(z) exp
( 1
N Ψu0,N (z)
)(
1 + 1
NRN (z)
)
= sign (R(z))
(
e
N
2iπ L−(z;−2iπ,ℓ) −u0e
N
2iπ L+(z;−2iπ,ℓ)
)
×ρ(z) exp
( 1
N Ψu0,N (z)
)(
1 + 1
NRN (z)
)
,
where
(130) 1 + 1
NRN (z) := exp
( 1
N Iu0,N (z)
)(
1 + 1
NON →∞ (1)
) coth
(Nz
2
)
sign (R(z))
satisﬁes the expected properties (the term 1
NON →∞(1) comes from (129), and recall that
coth( N z
2 )
sign(R(z)) =
(
1 +oN →∞
(1
N
))
from Step 5). More precisely, RN (z) is of the form
RN (z) = Iu0,N (z) +ON →∞ (1) +oN →∞ (1) +ON →∞
( 1
N
)
,
where the second, third and fourth terms in the right hand sid e are of course functions of z
as before. Denote by C +
N andC −
N the intersections of CN with the right and left half-spaces.
Because of the term sign ( R(z)) in the above expressions, we can write
∫
CN
e
N
2iπ (z2−l1,Nz) ˆSN (l0,N +z) coth(Nz
2 )dz =
∫
C+
N
(
e
N
2iπ L−(z;−2iπ,ℓ) −u0e
N
2iπ L+(z;−2iπ,ℓ)
)
ρ(z) exp
( 1
N Ψu0,N (z)
)(
1 + 1
NRN (z)
)
dz
−
∫
C−
N
(
e
N
2iπ L−(z;−2iπ,ℓ) −u0e
N
2iπ L+(z;−2iπ,ℓ)
)
ρ(z) exp
( 1
N Ψu0,N (z)
)(
1 + 1
NRN (z)
)
dz.
The integrand is holomorphic on the intersection U of the domains (63) shifted by − 1
N Log(u0)
and the domain (121). Since −π < I(Log(u0)) < π one can choose s−
N , s+
N in (125) so
52 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
that s±
N > 1
N I(Log(u0)), and therefore the contours C +
N and C −
N are homotopic within U
to [is−
N, 2iπ −is+
N ] relatively to their endpoints, with upwards and downwards orientations
respectively. So the opposite of the integral over C −
N coincides with the integral over C +
N , and
the last expression reduces to 2 times the integral over C +
N on the RHS. This concludes the
proof. ✷
Remark 5.2. We can give sharp uniform bounds on |Ψu0,N (z)| for points z ∈CN , as follows.
Deﬁne (with υ,υ ′,υ ′′ as in (124)–(125)):
δ−
N := (1 −υ)π
2N + π
N,
δ+
N := (υ′′ −υ′)π
N .
Then the inequalities (126) become
(131) δ−
N − π
N ≤ I
( 1
N Log(u0) +z
)
≤ 2π −δ+
N − π
N,
and thus deﬁne strips as in Lemma 3.3 and Remark 3.4 (iii) (wit h the variable 1
N Log(u0) +z
in place of z). In that lemma take now M equal to the constant ε used in the deﬁnition of
the contours CN . Then, by (57), for every z in the strip (131) satisfying R(z) ≤ε′ for some
ε′ >ε (so that R( 1
N Log(u0) +z) ≤ε for N large enough), we have
(132) |Ψu0,N (z)| ≤ B′
δ+
N
+ πeε/2
2δ+
N
√
1 − π2
24 +B′′,
for constants B′,B ′′ > 0 independent of N and of δ+
N (note that δ+
N = min(δ−
N,δ +
N )). Since
Nδ +
N =π(υ′′ −υ′)> 0, (132) shows that 1
N |Ψu0,N (z)| is bounded from above by a constant
independent of N , δ−
N , and δ+
N on any half-strip given by (131) and R(z) ≤ε′.
By Remark 3.4 (i), the bound (132) holds true also when δ−
N in (131) is replaced with any
δ ∈]0,π [, as long as 1
N Log(u0) + z is not contained in a cut of the domain (63) shifted by
− 1
N Log(u0). In particular we can take δ−
N of the form δ−
N = α′ π
N , with α′ > 0 arbitrary.
SinceNδ −
N =α′π >0, as in the proof of Lemma 3.5 (ii) we ﬁnd that 1
N |Ψu0,N (z)| is bounded
from above by a constant independent of N , δ+
N , and such a δ−
N on any half-strip given by
(131) and R(z) ≤ε′.
By Lemma 5.1 we have
(133)
∫
CN
e
N
2iπ (z2−l1,Nz) ˆSN (l0,N +z) coth(Nz
2 )dz = 2IN,−(ℓ) − 2u0IN,+(ℓ),
where
(134) IN,±(ℓ) :=
∫
C+
N
gN (z)e
N
2iπ L±(z;−2iπ,ℓ)dz,
and we put
gN (z) := ρ(z) exp
( 1
N Ψu0,N (z)
)(
1 + 1
NRN (z)
)
(135)
=ρ(z) exp
( 1
N Ψu0,N (z)
)
exp
( 1
N Iu0,N (z)
)(
1 + 1
NON →∞ (1)
) coth
(Nz
2
)
sign (R(z)).
Lemma 5.5 below extends to the integrals IN,±(ℓ) in (134) the asymptotics obtained for the
integrals in Section 4. The proof requires the following gen eralizations of Proposition 4.2; why
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 53
we need these generalizations is explained before Lemma 5.5 . First, we will need a special
case of Perron’s method for a contour starting at a maximum.
Proposition 5.3. (i) ([51, Theorem 1.2, case of µ = 1 and S = 1]) Assume that λ is a
compact piecewise C1 contour from z0 to z1 in C, and f and g are holomorphic functions on
a domain containing λ. Assume furthermore that f ′(z0) ⁄= 0, and I(f (z))< I(f (z0)) for all
z ∈λ, z ⁄=z0. Then we have
(136)
∫
λ
g(z)en(−i)f (z)dz =en(−i)f (z0)
( g(z0)
if ′(z0)
1
n +On→∞
(Kg
n2
))
,
whereKg := supz∈λ∪B |g(z)| and On→∞
(
Kg
n2
)
≤C · Kg
n2 for a constant C >0 independent of
g and n.
(ii) Suppose that the assumptions in (i) on λ and f hold, and a sequence of holomorphic
functions (gn) converges uniformly to a function g on a domain containing λ. Then
(137)
∫
λ
gn(z)en(−i)f (z)dz =en(−i)f (z0)
( g(z0)
if ′(z0)
1
n +on→∞
( 1
|f ′(z0)| · 1
n
))
,
whereon→∞
(
1
|f ′(z0)| · 1
n
)
≤εn 1
|f ′(z0)| · 1
n for a sequence of real positive numbers (εn) converging
to 0 and independent of f and n.
(iii) The On→∞ and on→∞ error terms in (136) and (137) do not depend on z0 when z0
varies in a ﬁxed compact set which does not contain critical p oints of f .
Note that (iii) says that the expansions (136) and (137) are uniform with respect to z0 in the
given range; see [61, Chapter VII] for the notion of uniform a symptotic expansions.
Proof of (ii) and (iii). The statement (ii) is a direct consequence of the proof of (i) given
in [51]. Indeed write gn = g + (gn −g), and apply (i) to the integrals with integrands g
and gn −g. The uniform convergence of ( gn −g) to the 0 function implies an asymptotic
expansion like (136) for the integral with integrand gn −g, with coeﬃcients (gn−g)(z0)
if ′(z0) and
Kgn−g arbitrarily close to 0 as n → +∞. As there is no assumption on the convergence speed
of the sequence ( gn), the error term is only known to be an on→∞
(
1
|f ′(z0)| · 1
n
)
.
For the statement (iii) one uses an estimate of the constant C in (i). Namely, by the equations
(3-10) to (3-15) of [51] in the case µ = 1 and S = 1, we have a lower bound for C of the
following form, described below:
(138) On→∞
(Kg
n2
)
≤ 16Kφ
|f ′(z0)|2 · Kg
n2 +On→∞
(
Kge−εn)
.
Here On→∞
(
Kge−εn)
≤C ′Kge−εn, with C ′> 0 a constant bounded by the length of λ, and
ε> 0 depends only on the contour λ and a constant Rf (z0)> 0; precisely, ε is chosen so that
I(f (z)−f (z0)) ≤ −ε for allz satisfying |z−z0| ≥ Rf (z0) and belonging to a small deformation
ofλ, where the deformation occurs in the disk D(z0,Rf (z0)] (see the proof of [51, Proposition
1.3]). The constant Rf (z0) is such that the following properties hold ([51, Propositi on 2.1]):
(*) the solutions ( r,θ ) of the equation I(f (z0 +reiθ) −f (z0))/r = 0 have the form ( r,θ ) =
(r,hk(r)) when r belongs to on an interval containing [0 ,Rf (z0)], where the functions hk(r),
k ∈ {0, 1}, are all deﬁned and diﬀerentiable, and hk(0) = − arg(if ′(z0)) +π(k + 1
2 ).
Now assume that z0 varies in a compact set E which does not contain critical points of f .
ThenRf (z0) as above is deﬁned and can be chosen continuously as a functi on of z0 ∈E. We
have Rf := minz0∈E(Rf (z0)) > 0, and the above properties (*) hold true uniformly for all
54 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
z0 ∈ E, replacing Rf (z0) with Rf . Using Rf to deﬁne the ε >0 above, it depends only on
the compact set E. Also, in (138) we have (see [51, equations (2-1) and (3-1)])
Kφ := max
z∈Dz0
⏐
⏐
⏐
⏐1 − f (z) −f (z0)
f ′(z0)(z −z0)
⏐
⏐
⏐
⏐,
whereDz0 is a small closed disk neighborhood of z0. Then 16Kφ
|f ′(z0)|2 is bounded from above by
a constant independent of z0 ∈E.
It follows that the error term en(−i)f (z0)On→∞
(
Kg/n2)
in (136) is a on→∞ of the leading
order term en(−i)f (z0)eiθ g(z0)
f ′(z0)
1
n , independent of z0 ∈E, as claimed. ✷
The second generalization of Proposition 4.2 that we will ne ed is for contours passing through
a maximum. It is a classical result that the general form of Pe rron’s method, which generalizes
Proposition 5.3 (i), implies Proposition 4.2 (see [51, Coro llary 1.4, case of µ = 2 and k2 =
k1 + 1]). In the situation of a sequence ( gn) converging uniformly to g as in Proposition 5.3
(ii), the proof of this classical result generalizes immedi ately to give the statement (ii) in
the next Proposition. In particular, the arguments show tha t if we are in the situation of a
sequence (gn) converging to g as in the statement (i), the error term on→∞ (1/√n) is in fact
a On→∞ (1/n), as stated. We point out this particular case, as it can be fo und verbatim in
the litterature.
Proposition 5.4. Keep the same assumptions on the path λ and the function f as in Propo-
sition 4.2.
(i) ([50, Remark 3.3], [61, page 145, note of §5]) If there is a neighborhood of the critical
point z0 of f where for all n large enough gn(z) = g(z) +gn,1(z) 1
n , with g holomorphic and
independent of n, and |gn,1| bounded from above by a constant independent of n, then we have
∫
λ
gn(z)en(−i)f (z)dz =en(−i)f (z0)
(
√
2πeiθ g(z0)√
|f ′′(z0)|
1√n +On→∞
(1
n
) )
for some explicit constant θ ∈ R.
(ii) Suppose (gn) is a sequence of holomorphic functions converging uniforml y to a function
g on a domain containing λ. Then we have, with θ as in (i):
∫
λ
gn(z)en(−i)f (z)dz =en(−i)f (z0)
(
√
2πeiθ g(z0)√
|f ′′(z0)|
1√n +on→∞
( 1√n
) )
.
We now describe in Lemma 5.5 some asymptotics of the integral s IN,±(ℓ) in (134). The
proof will follow the main lines of the analysis of Section 4. We will use Proposition 5.3
because ρ(z) (and hence gN (z), see (135)) has poles at z = 0 and z = 2iπ; indeed, some
subintegrals of IN,±(ℓ), which were negligible in the context of Section 4 (by the re sults of
Sections 4.3.1-4.3.2), will now dominate its asymptotics i n case (b) (ℓ = 2iπ). Proposition 5.4
(ii) will play the same role as Proposition 4.2 in Section 4, t o estimate the integrals (where
now gN depends on N ) on subcontours with endpoints away from 0 and 2 iπ. Recall that
l′
0 := Log(u0) +iπa0, and the endpoint s−
N of C ±
N is written as α− π
N .
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 55
Lemma 5.5. ForgN (z) as in (135) we have
lim
N →+∞
2π
N |IN,−(iπ)| = 1
2 Vol(M ),
|IN,+(iπ)| ∼N →+∞
N
l′
0
2iπ − 1
2 + α−
2
Log(N )
( 1
α−π
) l′
0
2iπ + 1
2 + α−
2
|vN |,
|IN,+(2iπ)| ∼N →+∞
N
l′
0
2iπ − 1
2 + α−
2
Log(N )
( 1
α−π
) l′
0
2iπ + 1
2 + α−
2
|vN |,
|IN,−(2iπ)| ∼N →+∞
N
l′
0
2iπ − 1
2 + α−
2
Log(N )
( 1
α−π
) l′
0
2iπ + 1
2 + α−
2
e−α−π|vN |,
where (vN ) (the same in the last three asymptotic formulas) is a bounded sequence, bounded
from below by a constant > 0, and we choose a0 ≥ 4 (even, as usual) so that R( l′
0
2iπ − 1
2 )> − 1
2 .
The choice of a0 ≥ 4 will be explained in Step 6 of the proof. When a0 = 2 the asymptotics
of the integrals IN,+(iπ), IN,+(2iπ) and IN,−(2iπ) depend on the sign of I(Log(u0)); for
instance, if it is negative, then IN,+(2iπ) and IN,−(2iπ) are of the form in (115). The choice
a0 = 2 would not aﬀect the conclusions of the subsequent results.
Remark 5.6. One could worry about the factor e−α−π in the asymptotic formula of IN,−(2iπ)
but not of IN,+(2iπ); indeed, by (133) these formulas combine to give the leadin g order term
asN → +∞ of the LHS integral for ℓ = l1,∞ = 2iπ, which does not depend on α−. However,
one should be careful that a full asymptotic expansion of thi s integral is needed to describe it
faitfully. In the present situation IN,−(ℓ) andIN,+(ℓ) emerged from the diﬀerent asymptotical
behaviours of the integrand on the half-spaces R(z)< 0 and R(z)> 0, with terms becoming
exponentially small in the former region and exponentially large in the latter (see (129), and
also (94)). Therefore R(z) = 0 is an anti-Stokes line of the asymptotics of the integran d, and
exponentially small terms coming from a full asymptotic exp ansion of IN,−(ℓ) and IN,+(ℓ)
are required to recover the LHS integral of (133) as N → +∞.
Proof. Step 1: Conditions on moving the contours.
We adapt the analysis of Sections 4.4 (case (a), ℓ = iπ) and 4.5 (case (b), ℓ = 2iπ) to the
integrals IN,±(ℓ). Recall that the integrals in Section 4.4-4.5 have gN ≡ 1 and C −
N or C +
N
replaced by [is−
N, 2iπ −is+
N ] (the two being homotopic relatively to their endpoints, wi th the
opposite or the same orientation respectively).
First we show that the function gn :z ↦→gN (z), n := N
2π , is holomorphic on a domain where
we can deform C −
N or C +
N to a contour very close to those in Figure 3, Figure 4, and Figu re
5. In each situation the diﬀerence between the two contours wi ll occur on short subcontours
close to 0 or 2 iπ, where the integrals will have polynomial growth at worst.
These deformations occur in the set Sη formed by the strip −η ≤ I(z) ≤ 2π with cuts
[0, +∞[ and 2 iπ + [0, +∞[, where η > 0 is deﬁned in the path C ′
3 below Figure 4. By
deﬁnition ρ(z) and the term ON →∞(1) in (130) are holomorphic on Sη. The function Ψ u0,N
is holomorphic on the domain (63) shifted by − 1
N Log(u0), and Iu0,N on (121), whence the
two on Sη minus the two half-lines (the poles − 1
N Log(u0) + 2iπ + 2piπ/N are not in Sη since
−π <I (Log(u0))<π ):
L1 := − 1
N Log(u0) + [0, +∞[ , L2 := − 1
N Log(u0) + 2iπ + [0, +∞[.
56 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
In Figure 7, these two shifted cuts are represented with teal half-lines, either dashed or dot-
ted. The dotted part around the y-axis covers the case when ℜLog(u0) > 0. For each of
L1,L 2, two copies are drawn, according to the sign of ℑLog(u0) = arg(u0).
Step 2: Deformed contour in case (b), integral IN,−(2iπ), or case (a), integral IN,−(iπ).
Figure 7 actually expands Figure 5, so let us justify the shif ted cuts are where they seem to
be in the corresponding case (case (b), integral IN,−(2iπ)). Recall that we assume that there
exists some υ ∈ (0, 1) such that −υπ ≤ I(Log(u0)) ≤υπ (which makes sense even in a more
general case when u0 depends on N ). In this situation, choosing α− = 1+υ
2 ands−
N =α− π
N as
in the proof of Lemma 5.1, we conclude that α−> 1
π |I(Log(u0)| and thuss−
N > 1
N |I(Log(u0)|.
Hence we can deform C ±
N to the contour shown in Figures 5 and 7 without crossing the cu ts
L1, L2.
By the same arguments gN (z) is also holomorphic on a domain where we can deform C ±
N to
[is−
N,is +
N ], which is the contour occuring in case (a) for the integral IN,−(iπ).
ℑf−< 0
ℑf−< 0
ℑf−> 0
ℑf−> 0
b +iπ
0
is−
N
iπ
2iπ −is+
N
2iπ
1 +is−
N
1 +i(π −ǫ)
i(π +ǫ)
Cut
Cut
Shifted cut L1 (if arg( u0) < 0)
Shifted cut L2 (if arg( u0) < 0)
Shifted cut L1 (if arg( u0) > 0)
Shifted cut L2 (if arg( u0) > 0)
Figure 7. The deformed contour of Figure 5 with the shifted cuts
Step 3: Deformed contour in case (b), integral IN,+(2iπ).
Consider the situation of Figure 4, expanded upon in Figure 8 with the shifted cuts L1,L 2.
Since η,η ′ > 0 are ﬁxed constants, and η′ ≥ s+
N with s+
N = α+ π
N , α+ ∈]1, 2[, we have
α+ > |I(Log(u0))| and then η′ > | 1
N I(Log(u0))|; we can also take N large enough so that
η > | 1
N I(Log(u0))|. Then we can deform C ±
N to the contour shown in Figure 4 without
crossing L1 and L2, except in the case R(Log(u0))> 0, where the contour must circumvent
L1 in a small subarc Ca close to 0, joining −iη to is−
N (drawn in dashed black in Figure 8).
To be more precise, recall that a is the critical point of f+, and let r,υ ′′ ∈]0,a [ be such that
η,υ ′′ >r> 1
N |ℜ(Log(u0))|. We deﬁne Ca as the concatenation of
• C −
a , going from −iη to −υ′′, while staying in the domain where If+< 0 and R(z)< 0,
at a distance ≥r from 0, and avoiding L1 if arg(u0)> 0;
• C +
a , going from −υ′′ to is−
N , while staying at a distance ≥ s−
N from 0, and avoiding
L1 if arg(u0)< 0.
See Figure 9 for an illustration of this. One should understa nd Figure 9 as a zoomed part of
Figure 8 around the origin.
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 57
ℑf+> 0
ℑf+< 0ℑf+> 0
ℑf+< 0
a
a + 2iπ −iη′
0
is−
N
iπ
2iπ −is+
N
2iπ −iη′
2iπ
−iη
Cut
Cut
Shifted cut L1 (if arg( u0) < 0)
Shifted cut L2 (if arg( u0) < 0)
Shifted cut L1 (if arg( u0) > 0)
Shifted cut L2 (if arg( u0) > 0)
Figure 8. The deformed contour of Figure 4 with the shifted cuts.
−υ′′
is−
N
−iη
Cut
Shifted cut L1 (if arg( u0) < 0)
Shifted cut L1 (if arg( u0) > 0)
C −
a
C +
a
Figure 9. The small contour Ca, which avoids the shifted cut L1
Let us compute asymptotics of the integral IN,+(2iπ) on the subcontours C −
a , C +
a .
On the subarc C −
a : we can use the fact that ℑ(f+(z))< ℑ(f+(υ′′)) = 0 for all z in the interior
of C −
a . Let us decompose C −
a into consecutive subarcs C −−
a , C −+
a with initial endpoint −iη
and ﬁnal endpoint −υ′′ respectively, such that along C −−
a we have ℑ(f+) < −c for some
c> 0. Then:⏐
⏐
⏐
⏐
∫
C−−
a
gN (z)e
N
2iπ L+(z,−2iπ,2iπ)dz
⏐
⏐
⏐
⏐ ≤ max
C−−
a
(|gN (z)|)
∫
C−−
a
e
N
2π ℑ(f+(z))|dz|
≤ max
C−−
a
(|gN (z)|)
∫
C−−
a
e− N
2πc|dz| =oN →∞
( 1
N
)
.(139)
Here we use that |gN (z)| is bounded from above by a constant independent of N onC −
a . In-
deedC −
a is compact and stays away from a ﬁxed small disc centered at 0, so (120) implies that
|ρ(z)| is bounded from above by a constant independent of N onC −
a . The formula of Iu0,N (z)
above (128) and Lemma 3.5 imply this as well for | exp
(1
N Iu0,N (z)
)
| and exp
(1
N Ψu0,N (z)
)
,
respectively, and clearly it holds for the term
(
1 + 1
NON →∞ (1)
)
coth
(Nz
2
)
in (130). Hence
58 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
gN (z) = ρ(z) exp
(1
N Ψu0,N (z)
)
(1 + 1
NRN (z)) has modulus bounded on C −
a by a constant
independent of N .
Along the subarc C −+
a we can apply Proposition 5.3 (ii) with n = N/2π, f = f+, and ( gn)
the sequence (gN ); indeed, C −+
a is a compact subset of U , so Lemma 3.5 (iii) and the bounds
discussed above for RN (z) imply that ( gN ) converges uniformly to ρ(z) on C −+
a . We have
ℑ(f+(υ′′)) = 0, f ′
+(υ′′) ⁄= 0, and ρ(υ′′) ⁄= 0, so from (137) we deduce
⏐
⏐
⏐
⏐
∫
C−+
a
gN (z)e
N
2iπ L+(z,−2iπ,2iπ)dz
⏐
⏐
⏐
⏐ ∼N →+∞D · 1
N
for a scalar D ⁄= 0 (we will not use its actual value).
Consider now the subarc C +
a . Unlike in the case of C −
a above, the function gN is not bounded
on C +
a since its factor ρ(z) satisﬁes |ρ(z)| → +∞ as z :=is−
N → 0. Let us see precisely what
happens.
Part of the above discussion about C −
a is still true. Namely, by Lemma 3.5 (ii) the function
| exp
(1
N Ψu0,N (z)
)
| is bounded from above by a constant independent of N and z ∈ Ca+.
Also, by the comment after (129) the same is true for obvious r easons for the modulus of the
factor
(
1 + 1
NON →∞ (1)
)
coth(Nz/ 2) in (135), since coth( Nis −
N/2) = coth(iα−π/2).
Considerρ(z). We claim that, because z =is−
N is the point of C +
a which is the closest to the
singularity z = 0 of ρ(z), it is enough to consider the behaviour of ρ(is−
N ). Indeed, we can
deform C +
a slightly upwards near is−
N , so that it reaches a point iη with s−
N < η < π, and
then goes vertically to is−
N . By the same arguments as for C −
a , |ρ(z)| is bounded from above
by a constant independent of N on the subarc from −υ′′ to iη. For z = it on the vertical
subarc from iη to is−
N , it is readily checked from the formula (120) that
|ρ(it)| = (Constant) · exp
(
−t
(Log|u1|
2π + Log|u0|
4π
)
− I(l′
0) +π
2π · ln(sin(t/2))
)
.
Our choice of a0 ≥ 2 makes I(l′
0 +π)/2π = R((l′
0 +iπ)/2iπ)> 0, and the derivative of |ρ(it)|
is (
−
(Log|u1|
2π + Log|u0|
4π
)
− I(l′
0) +π
2π cotan
(t
2
))
· |ρ(it)|,
which is negative for t >0 and small, as lim t→0+ cotan
(t
2
)
= + ∞. The maximum of |ρ(it)|
is therefore attained at |ρ(is−
N )| on the subarc from −υ′′ to iη. This concludes the proof of
our claim.
Now we have 1 −ez = 1
NO(1) ⁄= 0 for every z ∼N →+∞ u
N ,u ∈ C∗, so the formula (120) implies
thatN −(l′
0+iπ)/2iπ|ρ(is−
N )| has modulus bounded from above by a constant independent of N
(note again that our choice of a0 ≥ 2 makes R((l′
0 +iπ)/2iπ)> 0, whence N (l′
0+iπ)/2iπ → +∞
asN → +∞). A similar argument applied to the integral formula of Iu0,N (z) shows that the
same conclusion holds true for exp
(1
N Iu0,N (is−
N )
)
.
Summing up, we obtain that N −(l′
0+iπ)/2iπgN is bounded from above by a constant indepen-
dent of N on Ca+. Then let us write
(140)
∫
C+
a
gN (z)e
N
2iπ L+(z,−2iπ,2iπ)dz =N (l′
0+iπ)/2iπ
∫
C+
a
gN (z)
N (l′
0+iπ)/2iπe
N
2π ℑ(f+(z))dz.
Now, from Section 4.5.1 we have
∂
∂x ℑ(f+(x +it)) = 2t − arg
(
1 −ex+it)
.
Since arg
(
1 −ex+it)
< 0 when x <0 and t >0 is close to 0, it follows that, if one initially
choosesυ′′ small enough (which, by the deﬁnition of C +
a andC −
a is always possible by letting
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 59
N be large enough), then ∂
∂x ℑ(f+(z))> 0 for any z ∈C +
a , and thus for any such z =x +it
we have
(141) e
N
2π ℑ(f+(z)) ≤e
N
2π ℑ(f+(it)) =e
N
2π Cl2(t).
Then, a simple upper bound of the modulus of the RHS integral i n (140) is
max
C+
a
( |gN (z)|
N (l′
0+iπ)/2iπ
) ∫
C+
a
e
N
2π ℑ(f+(z))dz ≤ max
C+
a
( |gN (z)|
N (l′
0+iπ)/2iπ
)
·ON →∞(1) ·
∫ sN
0
e
N
2π Cl2(t)dt
=ON →∞
(
1
N 1− α−
2
)
=oN →∞
( 1√
N
)
,(142)
where we used (141) in the inequality, and the asymptotics of the last integral computed in
Section 4.3.2 in the equality. Note that the factor ON →∞(1) on the RHS of the inequality
comes from the change of measure from the (compact) contour C +
a to the vertical contour
[0,isN ].
This estimate is not enough for our purposes, because it only implies that the integral (140)
has order ≤N (l′
0+iπ)/2iπoN →∞
(
1
√
N
)
, whereas the integral over the subpath C ′
3 ∪C ′
