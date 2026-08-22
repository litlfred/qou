---
doc_id: arxiv-1002.0126v1
doc_title: "An introduction to the volume conjecture"
section_id: sec-008-41-approximation-of-the-colored-jones-polynomial
section_title: "Approximation of the colored Jones polynomial"
section_number: 4.1
pages: 22-26
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
doc_brief: "An introduction to the volume conjecture — This is an introduction to the Volume Conjecture and its gene r- alizations for nonexperts."
---
−1/N)
and I will give an interpretation of the R-matrix used to deﬁne the colored Jones
polynomial. From (2.2) and (2.4) we have
Rij
kl
⏐
⏐
q:=ξN
=
∑
m
(a power of ξN )× δl,i+mδk,j−m
{l}!{N− 1− k}!
{i}!{m}!{N− 1− j}! ,
(R−1)ij
kl
⏐
⏐
q:=ξq
=
∑
m
(a power of ξN )× δl,i−mδk,j+m
±{k}!{N− 1− l}!
{j}!{m}!{N− 1− i}! .
(4.1)
Since
{k}!
⏐
⏐
q:=ξN
=
(
2
√
−1
) k
sin(π/N) sin(2π/N)··· sin(kπ/N ),
AN INTRODUCTION TO THE VOLUME CONJECTURE 23
we have
{k}!{N− k− 1}!
⏐
⏐
q:=ξN
=
(
2
√
−1
) N −1
sin(π/N) sin(2π/N)··· sin(kπ/N )
× sin
(
(N− (k + 1))π/N
)
sin
(
(N− (k + 2))π/N
)
sin
(
(N− (N− 1))π/N
)
=(−1)N −k−1(√
−1
) N −1
2N −1 sin(π/N) sin(2π/N)··· sin((N− 1)π/N)
=εN
for ε∈{ 1,−1,√−1,−√−1}. For the last equality, see for example [28]. So if we
put
(ξN )k+ := (1− ξN )··· (1− ξk
N ),
(ξN )k− := (1− ξN )··· (1− ξN −1−k
N ),
we have
{k}!
⏐
⏐
q:=ξN
= (a power of ξN )× (ξN )k+ ,
{N− 1− k}!
⏐
⏐
q:=ξN
= (a power of ξN )× (ξN )k−
and
(ξN )k+ (ξN )k− = (a power of ξN )× N.
Therefore from (4.1) the R-matrix and its inverse can be written as
Rij
kl
⏐
⏐
q:=ξN
=
∑
m
δl,i+mδk,j−m
(a power of ξN )× N 2
(ξN )m+ (ξN )i+ (ξN )k+ (ξN )j− (ξN )l−
,
(R−1)ij
kl
⏐
⏐
q:=ξN
=
∑
m
δl,i−mδk,j+m
(a power of ξN )× N 2
(ξN )m+ (ξN )i− (ξN )k− (ξN )j+ (ξN )l+
.
If we are given a knot K, we express it as a closed braid and calculate the colored
Jones polynomial as described in §2.5. Then we have
JN (K; ξN ) =
∑
labelings

 ∏
crossings
(R±1)ij
kl


=
∑
labelings

 ∏
crossings
(a power of ξN )× N 2
(ξN )m+ (ξN )i± (ξN )k± (ξN )j∓ (ξN )l∓

 ,
(4.2)
where the summation is over all the labelings with {0, 1, . . . , N− 1} corresponding
to the basis {e0, e1, . . . , eN −1} and for a ﬁxed labeling the product is over all the
crossings, each of which corresponds to an entry Rij
kl (or ( R−1)i,j
kl , respectively),
determined by the four labeled arcs around the vertex, of the R-matrix (or its
inverse, respectively).
24 HITOSHI MURAKAMI
We will approximate ( ξN )k+ for large N . By taking the logarithm, we have
log(ξN )k+ =
k∑
j=1
log(1− ξj
N )
=
k∑
j=1
log
(
1− exp(2π
√
−1j/N )
)
.
Putting x := j/N , we may replace the summation with the following integral for
large N (this is not rigorous!).
log(ξN )k+ ≈
N →∞
N
∫ k/N
0
log
(
1− exp(2π
√
−1x)
)
dx
= N
2π√−1
∫ exp(2π√−1k/N)
1
log(1− y)
y dy,
where we put y := exp(2π√−1x) in the last equality and ≈
N →∞
means a very rough
approximation (which may be not true at all) for large N .
This integral is known as the dilogarithm function. We put
Li2(z) :=−
∫ z
0
log(1− y)
y dy
for z∈ C\ [1,∞). This is called dilogarithm since it has the Taylor expansion for
|z| < 1 as
∞∑
n=1
zn
n2 .
For more details about this function, see for example [42].
So by using the dilogarithm function, we have the following approximat ion:
log(ξN )k+ ≈
N →∞
N
2π√−1
[
Li2(1)− Li2(ξk
N )
]
.
Since Li 2(1), which equals ζ(2) = π2/6 ( ζ(z) is the Riemann zeta function), can be
ignored for large N , we have
(ξN )k+ ≈
N →∞
exp
[
− N
2π√−1 Li2(ξk
N )
]
.
Similarly we have
(ξN )k− ≈
N →∞
exp
[
− N
2π√−1 Li2(ξ−k
N )
]
.
Therefore from (4.2) the colored Jones polynomial can be (roughly ) approxi-
mated as follows.
(4.3) JN (K; ξN ) ≈
N →∞
∑
labelings
exp

 N
2π√−1
×

 ∑
crossings
{
Li2(ξm
N ) + Li2(ξ±i
N ) + Li2(ξ∓j
N ) + Li2(ξ±k
N ) + Li2(ξ∓l
N ) + log terms
}



 ,
where the log terms come from powers of ξN and N .
AN INTRODUCTION TO THE VOLUME CONJECTURE 25
Since the term
(4.4)
∑
crossings
{
Li2(ξm
N ) + Li2(ξ±i
N ) + Li2(ξ∓j
N ) + Li2(ξ±k
N ) + Li2(ξ∓l
N ) + log terms
}
can be regarded as a function of ξi1
N , ξi2
N , . . . , ξic
N with i1, i2, . . . , ic labelings of arcs,
we can write it as V (ξi1
N , ξi1
N . . . , ξic
N ). Note that m can be expressed as a diﬀerence
of two such labelings. So we have
(4.5) JN (K; ξN ) ≈
N →∞
∑
i1,i2,...,ic
exp
[ N
2π√−1 V (ξi1
N , ξi2
N , . . . , ξic
N )
]
.
We want to apply a method used in the proof for the ﬁgure-eight kno t in §3.2.
Recall that the point of the proof is to ﬁnd the maximum term of the s ummand
because the maximum dominates the asymptotic behavior. We will see k for the
“maximum” term of the summation in (4.5).
To do that we ﬁrst approximate this with the following integral:
(4.6) JN (K; ξN ) ≈
N →∞
∫
J1
∫
J2
···
∫
Jc
exp
[ N
2π√−1 V (z1, z2 . . . , zc)
]
dz1dz2··· dzc,
where zd corresponds to ξid
N and J1, J2, . . . , Jc are certain contours. (The argument
here is not rigorous. In particular I do not know how to choose the c ontours.)
Then we will ﬁnd the maximum of the absolute value of the integrand. T o be
more precise we apply the steepest descent method. For a precise statement, see
for example [20, Theorem 7.2.9]).
Theorem 4.2 (steepest descent method) . Under certain conditions for the func-
tions f , g, and a contour C, we have
∫
C
g(z) exp(N h(z)) dz ∼
N →∞
exp(N h(z0))
√
2πg(z0)√
N
√
−h′′(z0)
≈
N →∞
exp(N h(z0)),
where h′(z0) = 0 and Re(h(z)) takes its positive maximum at z0.
Note that the symbol ∼
N →∞
means that the ratio of both sides converges to 1 when
N→∞ and that we ignore the constant term and
√
N in the rough approximation
≈
N →∞
because exp(N h(z0)) grows exponentially when N→∞ . (Recall that we want
to know the limit of log|JN (K, ξN )|/N and so polynomial terms will not matter. )
Remark 4.3. In general, to apply the steepest descent method, we need to cha nge
the contour C so that it passes through z0.
Now we apply (a multidimensional version of) this method to (4.6) and w e will
ﬁnd the the maximum of {Im V (z1, . . . , zc)| (z1, z2, . . . , zc)∈ J1× J2···× Jc}. Let
(x1, x2, . . . , xc) be such a point. Then we have
(4.7) JN (K; ξN ) ≈
N →∞
exp
[ N
2π√−1 V (x1, x2, . . . , xc)
]
and so we ﬁnally have
(4.8) 2 π
√
−1 lim
N →∞
log JN (K; ξN )
N = V (x1, x2, . . . , xc).
26 HITOSHI MURAKAMI
Note that the point ( x1, x2, . . . , xc) is a solution to the following equation:
(4.9) ∂ V
∂ zd
(z1, z2, . . . , zc) = 0
for d = 1, 2, . . . , c.
Remember that our argument here is far from rigor! Especially I am c heating
on the following points:
• Replacing a summation with an integral in (4.6). Here we do not know ho w
to choose the multidimensional contour.
• Applying the steepest descent method in (4.7). In general, we have many
solutions to the system of equations (4.9) but we do not know which s olution
gives the maximum. Moreover we may need to change the contour so that
it passes through the solution that gives the maximum but we do not k now
whether this is possible or not.
