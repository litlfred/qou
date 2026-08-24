---
doc_id: resur-and-mld-calc-d-sauzin-hal
doc_title: "Resurgence and Mould Calculus"
section_id: sec-003-examples-from-mathematical-physics
section_title: "Examples from mathematical physics."
section_number: null
pages: 9-11
source_pdf: Resur_and_Mld_Calc_D_SAUZIN_HAL.pdf
source_sha256: b33f24cc76102f33
doc_brief: "Resurgence and Mould Calculus — 9 sections: Introduction; Alien operators. Alien derivations; Borel-Laplace summation"
---
In [GK21], the logarithm of Faddeev’s quantum dilog-
arithm Φ b(x) (a special function that plays a key
role in quantum Teichm¨ uller theory and Chern-Simons
theory) is shown to arise from the Borel-Laplace sum-
mation of a simple resurgent series: for ﬁxed x∈ C
with argx∈ (−π,π ),
log Φb( x
2πb) = z
2πi Li2(−ex) + (S{0}~G)(z,x ) (40)
for z = b−2, where ~G(z,x )∈ z−1C[[z−2]] has mero-
morphic Borel transform with simple poles that lie on
a countable union of lines passing through 0. More
precisely, ˆG(ζ,x ) has a simple pole with residue (−1)n
2πin
at
ωm,n(x) :=n
(
x+(2m+1)iπ
)
, m ∈ Z, n∈ Z∗. (41)
Since resurgent series are stable under nonlinear op-
erations like exponentiation [ ´Eca85] (details can be
found in [KS20]), it follows that
Φb( x
2πb) = exp
( z
2πi Li2(−ex)
)
(S{0}~H)(z,x ) (42)
with ~H := exp ~G∈ ~Rs. The Borel transform ˆH(ζ,x )
is not meromorphic, but its branches may be singular
only for ζ ∈ xZ + iπZ (because convolution and a
fortiori the Borel counterpart of exponentiation tend
to add singular points) and alien chain rule gives
∆ωm,n(x)~H(z,x ) = (−1)n
n
~H(z,x ), (43)
which indicates superpositions of simple poles and
logarithmic singularities. Notice that ∆ ω~H = 0 if
ω∈ xZ + iπZ is not among the ωm,n(x)’s, but some
branch of ˆH (though not the principal one) may be
singular at such a point ω.
Borel transforms displaying singularities arranged
on a countable union of lines through 0, like a peacock
pattern, have been observed
• in [CSMS17], in the context of topological string
theory (studying a resurgent transseries for the
free energy of topological strings on the local P2
toric Calabi-Yau threefold),
• in [GGM23], in the context of Chern-Simons the-
ory (studying the partition function of the com-
plement of a hyperbolic knot in S3).
4.3 Relaxing the constraint on the nature of
singularities.
Our earlier computation of a diﬀerence of Laplace
transforms illustrated by Figure 4 relied on the fact
8
that, given a direction θ∈ R, one has
a0 =
∫
Hθ
e−zζ a0
2πiζ dζ, (Lθˆχ)(z) =
∫
Hθ
e−zζ ∨
χ(ζ) dζ,
(44)
where
∨
χ(ζ) :=ˆχ(ζ) logζ
2πi +F (ζ), F (ζ)∈ C{ζ}, (45)
andHθ is a rotated Hankel contour as on Figure 5.
Figure 5: θ-rotated Hankel contour.
Let us thus introduce the Hankel-type Laplace
transform
(
∨
Lθ∨
ψ)(z) :=
∫
Hθ
e−zζ ∨
ψ(ζ) dζ. (46)
A simple singularity at 0 of the form
∨
ψ(ζ) := a0
2πiζ +
∨
χ(ζ), (47)
encoded by a0δ +ˆχ(ζ)∈ Cδ⊕ C{ζ}, is mapped to
a function that is asymptotic to a formal series a0 +
B−1ˆχ∈ C[[z−1]]. This gives a clue as to how we can
deal with much more general singularities, provided
they are still isolated.
Let ~C denote the Riemann surface of the logarithm
with its points denoted by ζ =r eiθ,r> 0,θ∈ R, i.e.
we view it as a covering space overC∗ withζ↦→ζ e−2πi
as a deck transformation. We now deﬁne ANA to be
the space of all functions
∨
ψ(ζ) analytic in a domain of
the form{r<h (θ)} for some continuous positive func-
tion h, i.e. the totality of all possibly singular germs
that are regular in a spiralling neighbourhood ofζ = 0.
Examples are singular germs with a simple singularity,
like (47), or higher order poles, or essential singular-
ities, or convergent expansions involving non-integer
powers of ζ and powers of log ζ as in (51), to name
but a few.
Deﬁnition 9. A singularity is any member of
SING := ANA/C{ζ}. We denote the canonical pro-
jection by
∨
ψ∈ ANA↦→ sing0
(∨
ψ(ζ)
)
∈ SING. (48)
The minor of a singularity
▽
ψ = sing0
(∨
ψ(ζ)
)
is
ˆψ(ζ) :=
∨
ψ(ζ)−
∨
ψ(ζ e−2πi)∈ ANA. (49)
We call resurgent singularity any
▽
ψ whose minor ˆψ(ζ)
is endlessly continuable in the sense of Deﬁnition 8.
The space of all resurgent singularities is denoted
by
▽
R.
The subspace
▽
Rs
Ω of
▽
R alluded to at the beginning of
this article is precisely Cδ⊕♭(ˆRs
Ω), with the notation
δ := sing0
( 1
2πiζ
)
, ♭ˆχ := sing0
(
ˆχ(ζ) logζ
2πi
)
(50)
(from now on, we no longer view δ as a symbol but
rather as a singularity).
It turns out that one can deﬁne a commutative con-
volution on
▽
R that extends the one inherited from ˆRs
Ω
and makes it an algebra, for which δ is the unit.
Observe that the Hankel-type Laplace transform
passes to the quotient: given a singularity whose mi-
nor has at most exponential growth at inﬁnity in the
direction θ, we can set
▽
Lθ
▽
ψ :=
∨
Lθ
∨
ψ for any repre-
sentative
∨
ψ of
▽
ψ.
However, the asymptotic expansions as |z| → ∞
of the resulting functions can be much more general
than mere power series. The direct generalization of
~Rs
Ω and ~Rs, the so-called formal model of Resurgence,
~R, is thus more delicate to deﬁne [ ´Eca85]. Suﬃce it
to say that ~R is an algebra containing monomials like
~Iσ :=z−σ or ~Jσ :=−z−σ logz, to be viewed as inverse
Borel transforms of the singularities represented by
∨
Iσ :=g(σ)ζσ−1,
∨
Jσ :=g(σ)ζσ−1 logζ +g′(σ)ζσ−1,
(51)
where g(σ) := 1
2πieiπσΓ(1−σ) for σ∈ C− Z>0 (the
case σ∈ Z>0 must be treated separately), as well as
z−σ(logz)m for any m∈ Z>0.
Accordingly, in practice, one often encounters resur-
gent transseries of the form
∑
k≥0
e−ωkz~ψk(z), ~ψk(z)∈z−σk C[[z−1]]∩ ~R (52)
9
with a certain sequence of exponents ( σk). This hap-
pens e.g. with one-parameter transseries solutions to
Painlev´ e equations, in which case there are also two-
parameter transseries containing logarithms [Bal+23;
SV22].
The general alien operators
∆+
ω∈ EndC(
▽
R), ∆ω∈ DerC(
▽
R), for ω∈~C (53)
are deﬁned by the natural generalization of what was
done in ~Rs, e.g. ∆ω
▽
ψ :=
∑
ε∈{+,−}r−1
p(ε)!q(ε)!
r! sing0
(
(contγ(ε)ˆψ)(ω+ζ)
)
, (54)
where ω1≺···≺ ωr−1 are the points of ]0 ,ω [ (now
in ~C) to be circumvented when following the analytic
continuation of the minor.
