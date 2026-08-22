---
doc_id: resur-and-mld-calc-d-sauzin-hal
doc_title: "Resurgence and Mould Calculus"
section_id: sec-002-borel-laplace-summation
section_title: "Borel-Laplace summation"
section_number: null
pages: 6-9
source_pdf: Resur_and_Mld_Calc_D_SAUZIN_HAL.pdf
source_sha256: b33f24cc76102f33
doc_brief: "Resurgence and Mould Calculus — 9 sections: Introduction; Alien operators. Alien derivations; Borel-Laplace summation"
---
3.1 Borel-Laplace summation
Many resurgent series encountered in practice are use-
ful because they are also ‘summable’ (or ‘accelero-
summable’, but we won’t touch on accelero-
summability in this article).
Borel-Laplace summation is the application of
Laplace transform (or some variant) to ( B~ϕ)(ζ), giv-
ing rise to a function ϕ(z) for which the formal se-
ries ~ϕ(z) appears as asymptotic expansion at inﬁnity;
but the function ϕ is usually not analytic in a full
neighbourhood of inﬁnity, only in a sectorial neigh-
bourhood, because ~ϕ is usually a divergent series.
A condition is needed for this to be possible. Let J
denote a real interval. We say that~ϕ(z) is 1-summable
in the directions ofJ if the function ˆϕ(ζ) extends ana-
lytically to the sector{argζ∈J} and satisﬁes there an
exponential bound,|ˆϕ(ζ)|≤ C ec|ζ| for some c,C > 0.
Each of the Laplace transforms
(LθB~ϕ)(z) :=c0 +
∫ eiθ∞
0
e−zζ ˆϕ(ζ) dζ, θ ∈J
(23)
is then analytic in the half-plane {ℜe(zeiθ) > c}. By
the Cauchy theorem, these functions match and can
be glued so as to deﬁne one function ( LJB~ϕ)(z) an-
alytic in the union DJ of these half-planes—see Fig-
ure 3. The domain DJ can be viewed as a sectorial
neighbourhood of inﬁnity of opening |J| +π (to be
considered as a part of the Riemann surface of the
logarithm if|J|>π ).
Figure 3: Above: Directions for Laplace integration
withJ = (θ1,θ 2). Below: the union of half-planes DJ.
In that situation, the function SJ~ϕ := LJB~ϕ
satisﬁes the asymptotic property ( SJ~ϕ)(z) ∼ ~ϕ(z)
as|z|→∞ with 1-Gevrey qualiﬁcation—a classical
fact that sometimes goes under the name of Watson’s
lemma, see e.g. [Cos09; MS16]. The operator
SJ = LJ◦ B (24)
is thus called the Borel-Laplace summation operator
in the directions of J. One can easily check that
SJ d ~ϕ
dz = d
dz (SJ~ϕ) and SJ[
~ϕ(z+α)
]
= (SJ~ϕ)(z+α)
(25)
5
for any α∈ C. The summation operator is also an
algebra homomorphism. Indeed, B maps the Cauchy
product of formal series to convolution in Cδ⊕ C{ζ},
which LJ maps to the pointwise product of functions:
SJ(~ϕ~ψ) = (SJ~ϕ)(SJ~ψ). (26)
Equations (25)–(26) show that, if we start with~ϕ(z)
formal solution to an ordinary diﬀerential equation
or a diﬀerence equation, even a nonlinear one, and
if we can subject it to Borel-Laplace summation, then
SJ~ϕ(z) is an analytic solution to the same equation.
Notice however that there may exist other solutions
with the same asymptotic series ~ϕ, maybe obtained
by means of SJ′
with a diﬀerent interval J′, or by
some other means...
The Borel-Laplace picture becomes particularly in-
teresting when we start with a resurgent series ~ϕ(z),
in which case ϕJ(z) := SJ~ϕ(z) deserves to be called
a resurgent function.
Resurgent
series ~ϕ(z)
c0δ +ˆϕ(ζ) with
good analytic
continuation
Resurgent
function ϕJ(z)
 1
PPPPPPPP i
Borel B
Laplace LJ
6
3.2 Transseries, symbolic Stokes automor-
phism
Indeed, let us pick a generator ω1 of Ω and θ∗∈ R
so that Ω + ⊂ d := e iθ∗ R>0 (making use of nota-
tions (2) and (10)). Suppose that ~ϕ ∈ ~Rs
Ω is 1-
summable in the directions of J+ := (θ∗−δ,θ∗) as
well as those of J− := ( θ∗,θ∗ + δ) for some δ ∈
(0,π ). We then have two Borel sums at our disposal,
SJ+~ϕ(z) and SJ−~ϕ(z). Comparing them in the do-
main DJ+∩ DJ−∩{ℜe(zeiθ∗)> 0}, we ﬁnd
SJ+~ϕ(z)− SJ−~ϕ(z) =
∫
Γdiff
e−zζ ˆϕ(ζ) dζ (27)
with a contour Γdiﬀ that can be decomposed in a sum
of contours Γ1, Γ2,... as illustrated on Figure (4).
Figure 4: Decomposition of the contour for the diﬀer-
ence of two Laplace transforms as a sum of contours.
By the Cauchy theorem we thus get
SJ+~ϕ(z) = SJ−~ϕ(z) +
∑
k≥1
∫
Γk
e−zζ ˆϕ(ζ) dζ, (28)
at least if the growth of the relevant branches of ˆϕ(ζ)
along the Γk’s stays at most exponential and the series
overk is convergent (if not, (28) still has asymptotic
meaning upon appropriate truncations). The point is
that, for each k ≥ 1, in view of (4), (9) and (11),
the branch of ˆϕ(ζ) that we are using along Γ k has a
pole and a monodromy variation precisely described
by B∆+
ωk~ϕ, hence
∫
Γk
e−zζ ˆϕ(ζ) dζ = e−ωkzSJ−∆+
ωk~ϕ(z) (29)
(use the change of variable ζ =ωk +ξ and (44)–(45)
below) and, ﬁnally,
SJ+~ϕ = SJ−~ϕ +
∑
k≥1
e−ωkzSJ−∆+
ωk~ϕ. (30)
The right-hand side of (30) can be interpreted as
the Borel-Laplace summation of a transseries, i.e. we
are naturally led to work with expressions of the form
~Ψ = ~ψ0 +
∑
k≥1
e−ωkz~ψk, ~ψ0,~ψ1,~ψ2... ∈ ~Rs
Ω, (31)
which live in the space
~Rs
Ω[[e−ω1z]] = ˆ⊕
k≥0
e−kω1z~Rs
Ω. (32)
6
We view that space as a completed graded algebra, in
which acts the operator
∆/+
d := Id +
∑
ω∈Ω∩d
e−ωz∆+
ω, (33)
and to which we extend SJ± by declaring that
SJ[e−ωz~Ψ] := e−ωz SJ~Ψ, the upshot being
SJ+ = SJ−◦ ∆/+
d, (34)
at least in restriction to those transseries of
~Rs
Ω[[e−ω1z]] all of whose components satisfy the
growth and convergence requirements needed for (28).
We can now reach a more conceptual understanding
of Theorem 3 and the identities (12):
• The identities (12) express that ∆/+
d is an algebra
endomorphism, which is no surprise since (34) in-
volves two algebra homomorphisms SJ±.
• The formulas expressing ∆ ωr in terms of
∆+
ω1,..., ∆+
ωr alluded to right after the statement
of Theorem 3 are just the homogeneous compo-
nents of the relation
log ∆/+
d =
∑
ω∈Ω∩d
e−ω∆ω, (35)
which is the true origin of formula (11).
• In the context of a completed graded algebra like
ours, the logarithm of an algebra automorphism is
always a derivation, and the homogeneous com-
ponents of a derivation are all derivations, this
explains why each ∆ω is a derivation of ~Rs
Ω.
Deﬁnition 7. The operator ∆/+
d is called the symbolic
Stokes automorphism in the direction d = e iθ∗ R>0.
The operator ∆/d := log ∆/+
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
The point is that ∆/+
d is an algebra automorphism
that commutes with d
dz and composition with z ↦→
z+α, and thus preserves the property of being a formal
solution to a diﬀerential or diﬀerence equation. One
can construct other such automorphisms; the simplest
example is (∆/+
d )w, with arbitrary w∈ C, which can
be written as a mould expansion:
(∆/+
d )w =
∑
ω∈Ω′
wr(ω)
r(ω)! e−‖ω‖z∆ω (36)
with the notation‖ω1··· ωr‖ :=ω1+··· +ωr. The case
w =± 1
2 gives rise to the median summation operator,
Sθ∗
med := SJ+◦ (∆/+
d )− 1
2 = SJ−◦ (∆/+
d )
1
2 , especially
useful when θ∗ = 0 and real symmetry is at play.
All this can be particularly relevant in physics,
where one often starts by developing a so-called per-
turbative theory, where various formal expansions nat-
urally appear; but then, if they can be subjected to
the resurgent apparatus, one may hope to incarnate
them as functions with meaningful exponentially small
contributions related to non-perturbative physics...
4 The algebra
▽
R of general resurgent
singularities
We now relax one by one the two requirements im-
posed by Deﬁnition 1, namely that the only obstacles
to analytic continuation may occur at points of a given
lattice Ω and that the singularities are no worse than
simple.
4.1 Relaxing the constraint on the location of
singularities.
Deﬁnition 8. We call endlessly continuable anyˆϕ(ζ)
analytic near 0 for which, for every real L >0, there
exists a ﬁnite subset FL of C such that ˆϕ(ζ) can be
analytically continued along every Lipschitz path of
length<L starting in the initial domain of deﬁnition
of ˆϕ and avoiding FL.
Variants are possible—see [CNP93; KS20], or
[´Eca85] for the most general deﬁnition (‘continuable
with no cut’). The point is that singular points are
possibly very numerous but, in a sense, still isolated.
This leaves room for a behaviour such as the one en-
visioned by Voros [Vor83b]: there may exist a dense
subset Ω of C such that, at every point of Ω, at least
one of the branches of the analytic continuation ofˆϕ is
7
singular (but, in any given region of C, one ‘sees’ only
ﬁnitely many singularities at a time: you need longer
and longer paths of analytic continuation to see more
and more singularities in that region).
Denoting by ~Rs the space of all ~ϕ(z)∈ B−1(Cδ⊕
C{ζ}) for which ˆϕ(ζ) is endlessly continuable with at
worst simple singularities for all the branches of its
analytic continuation, we can now deﬁne the alien op-
erators
∆+
ω∈ EndC(~Rs), ∆ω∈ DerC(~Rs), for ω∈ C∗
(37)
as follows: given ~ϕ = B−1(Cδ +ˆϕ)∈ ~Rs, Deﬁnition 8
allows us to ﬁnd a ﬁnite subset of ]0 ,ω [, the points of
which we denote by ω1≺···≺ ωr−1 (with reference
to the natural total order on the line-segment), so that
Deﬁnition 2 can be copied verbatim, except that the
ωk’s do not necessarily lie on any lattice (take anyL>
|ω| and{ω1,...,ω r−1} :=FL∩ ]0,ω [ in Deﬁnition 8).
Much of what has been said in the case of a lattice
can be generalized to the case of ~Rs; in particular, this
is a diﬀerential subalgebra of (C[[z−1]], d
dz ) and, in the
summable case, we have a passage formula generaliz-
ing (33)–(35):
S{θ} = S{θ′}◦
( ∑
ω∈Ω′
Pω
θ,θ′ e−‖ω‖z∆ω
)
, θ<θ ′,
(38)
(at least in restriction to the simple resurgent series for
which the action of the right-hand side is well-deﬁned),
with a scalar mould Pθ,θ′ deﬁned by
Pω
θ,θ′ :=



1 if r(ω) = 0
1
r1!···rs! if θ< argω1≤···≤ argωr <θ′
0 otherwise,
(39)
where, in the second case, ω =ω1··· ωr⁄= ∅,s counts
the number of pairwise distinct argωj’s, andr1,...,r s
count their multiplicities (r1 +··· +rs =r).
