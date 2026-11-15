---
doc_id: resur-and-mld-calc-d-sauzin-hal
doc_title: "Resurgence and Mould Calculus"
section_id: sec-007-borel-laplace-summation
section_title: "Borel-Laplace summation"
section_number: null
pages: 6-8
source_pdf: Resur_and_Mld_Calc_D_SAUZIN_HAL.pdf
source_sha256: b33f24cc76102f33
toc_source: outline
doc_brief: "Resurgence and Mould Calculus — 18 sections: Front matter; Introduction; ``Simple'' version of Resurgence T"
---
3.1
Borel-Laplace summation
Many resurgent series encountered in practice are use-
ful because they are also ‘summable’ (or ‘accelero-
summable’,
but
we
won’t
touch
on
accelero-
summability in this article).
Borel-Laplace summation is the application of
Laplace transform (or some variant) to (B eϕ)(ζ), giv-
ing rise to a function ϕ(z) for which the formal se-
ries eϕ(z) appears as asymptotic expansion at inﬁnity;
but the function ϕ is usually not analytic in a full
neighbourhood of inﬁnity, only in a sectorial neigh-
bourhood, because eϕ is usually a divergent series.
A condition is needed for this to be possible. Let J
denote a real interval. We say that eϕ(z) is 1-summable
in the directions of J if the function bϕ(ζ) extends ana-
lytically to the sector {arg ζ ∈J} and satisﬁes there an
exponential bound, |bϕ(ζ)| ≤C ec|ζ| for some c, C > 0.
Each of the Laplace transforms
(L θB eϕ)(z) := c0 +
Z eiθ∞
0
e−zζ bϕ(ζ) dζ,
θ ∈J
(23)
is then analytic in the half-plane {ℜe(zeiθ) > c}. By
the Cauchy theorem, these functions match and can
be glued so as to deﬁne one function (L JB eϕ)(z) an-
alytic in the union DJ of these half-planes—see Fig-
ure 3. The domain DJ can be viewed as a sectorial
neighbourhood of inﬁnity of opening |J| + π (to be
considered as a part of the Riemann surface of the
logarithm if |J| > π).
Figure 3: Above: Directions for Laplace integration
with J = (θ1, θ2). Below: the union of half-planes DJ.
In that situation, the function S J eϕ := L JB eϕ
satisﬁes the asymptotic property (S J eϕ)(z) ∼eϕ(z)
as |z| →∞with 1-Gevrey qualiﬁcation—a classical
fact that sometimes goes under the name of Watson’s
lemma, see e.g. [Cos09; MS16]. The operator
S J = L J ◦B
(24)
is thus called the Borel-Laplace summation operator
in the directions of J. One can easily check that
S J deϕ
dz = d
dz(S J eϕ) and S J
eϕ(z+α)

= (S J eϕ)(z+α)
(25)
5
for any α ∈C. The summation operator is also an
algebra homomorphism. Indeed, B maps the Cauchy
product of formal series to convolution in C δ ⊕C{ζ},
which L J maps to the pointwise product of functions:
S J(eϕ eψ) = (S J eϕ)(S J eψ).
(26)
Equations (25)–(26) show that, if we start with eϕ(z)
formal solution to an ordinary diﬀerential equation
or a diﬀerence equation, even a nonlinear one, and
if we can subject it to Borel-Laplace summation, then
S J eϕ(z) is an analytic solution to the same equation.
Notice however that there may exist other solutions
with the same asymptotic series eϕ, maybe obtained
by means of S J′ with a diﬀerent interval J′, or by
some other means...
The Borel-Laplace picture becomes particularly in-
teresting when we start with a resurgent series eϕ(z),
in which case ϕJ(z) := S J eϕ(z) deserves to be called
a resurgent function.
Resurgent
series eϕ(z)
c0δ + bϕ(ζ) with
good analytic
continuation
Resurgent
function ϕJ(z)


1
P
P
P
P
P
P
P
P
i
Borel B
Laplace L J
6
3.2
Transseries,
symbolic
Stokes
automor-
phism
Indeed, let us pick a generator ω1 of Ωand θ∗∈R
so that Ω+ ⊂d := eiθ∗R>0 (making use of nota-
tions (2) and (10)).
Suppose that eϕ ∈
eRs
Ωis 1-
summable in the directions of J+ := (θ∗−δ, θ∗) as
well as those of J−:= (θ∗, θ∗+ δ) for some δ ∈
(0, π). We then have two Borel sums at our disposal,
S J+ eϕ(z) and S J−eϕ(z). Comparing them in the do-
main DJ+ ∩DJ−∩{ℜe(zeiθ∗) > 0}, we ﬁnd
S J+ eϕ(z) −S J−eϕ(z) =
Z
Γdiff
e−zζ bϕ(ζ) dζ
(27)
with a contour Γdiﬀthat can be decomposed in a sum
of contours Γ1, Γ2, . . . as illustrated on Figure (4).
Figure 4: Decomposition of the contour for the diﬀer-
ence of two Laplace transforms as a sum of contours.
By the Cauchy theorem we thus get
S J+ eϕ(z) = S J−eϕ(z) +
X
k≥1
Z
Γk
e−zζ bϕ(ζ) dζ,
(28)
at least if the growth of the relevant branches of bϕ(ζ)
along the Γk’s stays at most exponential and the series
over k is convergent (if not, (28) still has asymptotic
meaning upon appropriate truncations). The point is
that, for each k ≥1, in view of (4), (9) and (11),
the branch of bϕ(ζ) that we are using along Γk has a
pole and a monodromy variation precisely described
by B∆+
ωk eϕ, hence
Z
Γk
e−zζ bϕ(ζ) dζ = e−ωkzS J−∆+
ωk eϕ(z)
(29)
(use the change of variable ζ = ωk + ξ and (44)–(45)
below) and, ﬁnally,
S J+ eϕ = S J−eϕ +
X
k≥1
e−ωkzS J−∆+
ωk eϕ.
(30)
The right-hand side of (30) can be interpreted as
the Borel-Laplace summation of a transseries, i.e. we
are naturally led to work with expressions of the form
eΨ = eψ0 +
X
k≥1
e−ωkz eψk,
eψ0, eψ1, eψ2 . . . ∈eRs
Ω, (31)
which live in the space
eRs
Ω[[e−ω1z]] = b⊕
k≥0e−kω1z eRs
Ω.
(32)
6
We view that space as a completed graded algebra, in
which acts the operator
∆
/ +
d := Id +
X
ω∈Ω∩d
e−ωz∆+
ω ,
(33)
and to which we extend S J± by declaring that
S J[e−ωz eΨ] := e−ωzS J eΨ, the upshot being
S J+ = S J−◦∆
/ +
d ,
(34)
at
least
in
restriction
to
those
transseries
of
eRs
Ω[[e−ω1z]] all of whose components satisfy the
growth and convergence requirements needed for (28).
We can now reach a more conceptual understanding
of Theorem 3 and the identities (12):
• The identities (12) express that ∆
/ +
d is an algebra
endomorphism, which is no surprise since (34) in-
volves two algebra homomorphisms S J±.
• The
formulas
expressing
∆ωr
in
terms
of
∆+
ω1, . . . , ∆+
ωr alluded to right after the statement
of Theorem 3 are just the homogeneous compo-
nents of the relation
log ∆
/ +
d =
X
ω∈Ω∩d
e−ω∆ω,
(35)
which is the true origin of formula (11).
• In the context of a completed graded algebra like
ours, the logarithm of an algebra automorphism is
always a derivation, and the homogeneous com-
ponents of a derivation are all derivations, this
explains why each ∆ω is a derivation of eRs
Ω.
Deﬁnition 7. The operator ∆
/ +
d is called the symbolic
Stokes automorphism in the direction d = eiθ∗R>0.
The operator ∆
/ d := log ∆
/ +
d is called the directional
alien derivation in the direction d.
Here we see how we can go beyond the traditional
theory of asymptotic series, in which a function is de-
termined by its asymptotics only up to an inﬁnitely
ﬂat function. In the framework of 1-Gevrey asymp-
totics, ﬂat functions are in fact exponentially small,
and the previous computation oﬀers a glimpse of how
the resurgent tools gives us a handle on the exponen-
tially small ambiguities inherent to the situation.
The point is that ∆
/ +
d is an algebra automorphism
that commutes with
d
dz and composition with z 7→
z+α, and thus preserves the property of being a formal
solution to a diﬀerential or diﬀerence equation. One
can construct other such automorphisms; the simplest
example is (∆
/ +
d )w, with arbitrary w ∈C, which can
be written as a mould expansion:
(∆
/ +
d )w =
X
ω∈Ω′
wr(ω)
r(ω)! e−∥ω∥z∆ω
(36)
with the notation ∥ω1 · · · ωr∥:= ω1+· · ·+ωr. The case
w = ± 1
2 gives rise to the median summation operator,
S θ∗
med := S J+ ◦(∆
/ +
d )−1
2 = S J−◦(∆
/ +
d )
1
2 , especially
useful when θ∗= 0 and real symmetry is at play.
All this can be particularly relevant in physics,
where one often starts by developing a so-called per-
turbative theory, where various formal expansions nat-
urally appear; but then, if they can be subjected to
the resurgent apparatus, one may hope to incarnate
them as functions with meaningful exponentially small
contributions related to non-perturbative physics...
4
