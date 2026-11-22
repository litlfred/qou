---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-027-44-degenerations-of-abelian-varieties
section_title: "Degenerations of abelian varieties"
section_number: 4.4
pages: 87-93
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
79
where Yη and Ys denote the generic resp. special ﬁbres of ˜f. Note that Ys
can be naturally identiﬁed with the ﬁbre f −1(s) ⊂Y. In the case of the
perverse intersection cohomology sheaf the passage between the global and
the local picture is provided by the following observation, where we now
denote by i : Ys = f −1(s) ,→Y the global embedding.
COROLLARY 4.10. In the above situation,
sp(δYη) = i∗(δY[−1]).
Proof. Our smoothness assumption on f implies that the generic ﬁbreYη
is smooth so that the perverse intersection cohomology sheaf δ = δYη is
the constant sheaf up to a degree shift. From this one easily deduces that
the intermediate extension j!∗(δ[1]) which occurs in lemma 4.9 arises from
the perverse intersection cohomology sheaf δY on the total space Y via the
Henselization morphism ˜Y −→Y.
□
4.4. Degenerations of abelian varieties
To ﬁnd sufﬁciently large lower bounds on the general Tannaka group
in theorem 4.2 we consider certain families of ppav’s whose theta divisor
degenerates. To construct these we ﬁx an integer n ≥3 and work over the
moduli space Ag,n of ppav’s of dimension g with level n structure. It has
been shown in chapter 7.3 of [80] that this moduli space is representable by
a smooth quasi-projective variety over Q. Analytically it can be written as
the quotient
Ag,n(C) = Hg/Γg(n)
of the Siegel upper half space by the action of the principal congruence
subgroup Γg(n) = ker(Sp2g(Z) −→Sp2g(Z/nZ)). Recall that for n ≥3 this
action is free, which again explains why in this case the moduli space is
smooth. We denote by
p :
X = Hg ×Cg 
Γg(n)⋉Z2g
/ Ag,n
the universal abelian scheme and by Θ ⊂X the divisor which is deﬁned
on the universal covering Hg × Cg by the zero locus of the Riemann theta
function ϑ(τ,z). Thus for each point τ ∈Ag,n(C) the ﬁbre Xτ = p−1(τ)
is a complex ppav with Θτ = Θ ∩Xτ as a symmetric theta divisor. More
generally, for any complex algebraic variety S with a morphism S −→Ag,n
we denote by
XS = X ×Ag,n S
and
ΘS = Θ×Ag,n S
80
Chapter 4 – The Tannaka group of the theta divisor
the corresponding abelian scheme resp. its relative theta divisor. For the
construction of families of ppav’s with degenerating theta divisors we will
use the following general observation.
LEMMA 4.11. For every point s ∈Ag,n(C) there is a smooth complex
quasi-projective curve S ,→Ag,n, passing through the point s in a general
tangent direction, such that
(a) the generic ﬁbre of the family ΘS →S is smooth,
(b) the singular loci of the total space and of the special ﬁbre of this
family satisfy
Sing(ΘS) ⊆Sing(Θs).
If the theta divisor Θs contains a singular point of precise multiplicity two,
then the inclusion in part (b) is strict for a suitable choice of S.
Proof. Since the moduli space Ag,n is smooth and quasi-projective, for
any s ∈Ag,n(C) we can ﬁnd a smooth quasi-projective curve S ,→Ag,n
passing through the point s in a general tangent direction. We can assume
that our general curve S is not contained in the locus of ppav’s with singular
theta divisor, indeed by [4] this locus is itself a divisor in Ag,n. So after
shrinking S we can assume that for all t ∈S(C) \ {s} the theta divisor Θt
is smooth. Then property (a) is clearly satisﬁed, and property (b) easily
follows from the fact that the total space ΘS is given locally in the smooth
variety XS as the zero locus of a single analytic function.
Explicitly, let ∆⊂S be an analytic coordinate disk with coordinate w
centered at the given point s, and consider a local lift h : ∆→Hg of the
embedding ∆,→S ,→Ag,n. On the universal covering the divisor ΘS is
described as the locus

(w,z) ∈∆×Cg | F(w,z) = 0
	
⊂∆×Cg
where the analytic function F(w,z) = ϑ(h(w),z) vanishes. If a point (w,z)
on this locus deﬁnes a singular point of the relative theta divisor ΘS, then
the gradient of F must vanish at this point. For the gradient in the variable z
this implies
0 = (∇zF)(w,z) = (∇zϑ)(τ,z)
for
τ = h(w).
Hence (τ,z) deﬁnes a singular point of the ﬁbre Θt where t ∈S(C) denotes
the image of the point τ. By our choice of the curve S the only singular
ﬁbre Θt is the one over the point t = s, hence claim (b) follows.
This being said, if some point (τ,z) ∈Hg ×Cg deﬁnes a singular point
of the theta divisor Θs with precise multiplicity two, then by deﬁnition the
4.4. Degenerations of abelian varieties
81
Hesse matrix
 ∂2ϑ
∂zα∂zβ
(τ,z)

α,β=1,...,g
is non-zero. Then the heat equation
∂ϑ
∂ταβ
(τ,z) = 2πi·(1+δαβ)·
∂2ϑ
∂zα∂zβ
(τ,z)
implies for the gradient with respect to the variable τ that (∇τϑ)(τ,z)̸ = 0
as well. Hence, taking S to be a curve which passes through the point s in
a sufﬁciently general tangent direction u, we obtain with notations as in the
preceding paragraph that
(∂F/∂w)(0,z) = (u·∇τϑ)(τ,z)̸ = 0
where F(w,z) = ϑ(h(w),z) is deﬁned for w in some coordinate disk ∆⊂S
by a suitable local lift h : ∆→Hg with h(0) = τ. In particular, since the
gradient of F does not vanish at the considered point, it follows that (τ,z)
deﬁnes a smooth point of the total space ΘS of our family. This shows that
the inclusion in claim (b) is strict.
□
We will now use the above construction to obtain information about the
Tannaka groups G(δΘτ) by varying the base point τ ∈Ag,n(C). In order to
apply the algebraic formalism of nearby cycles developed in section 4.3 we
consider perverse sheaves with coefﬁcients in Λ = Ql throughout, but the
ﬁnal result may as well be read in the category of analytic perverse sheaves
with coefﬁcients in Λ = C. Anyway all the occuring perverse sheaves will
be of geometric origin in the sense of [10, sect. 6.2.4].
In general it is not clear how to put the perverse sheaves δΘτ for the
various points τ ∈Ag,n(C) into a global family because there is no good
relative notion of a perverse intersection cohomology sheaf. However, over
the Zariski-open dense locus U ⊂Ag,n of ppav’s with a smooth theta divisor
this is no issue — the shifted constant sheaf ΛΘ[g−1] restricts to δΘτ on the
ﬁbre Xτ for each geometric point τ in U. This being said, proposition 3.20
shows that there are ﬁnitely many reductive algebraic groups G1,...,Gm
over Λ and a constructible stratiﬁcation
U =
m
G
i=0
Ui with G(δΘτ) = Gi for all geometric points τ in Ui.
The hypotheses of the proposition are satisﬁed because for each geometric
point τ in U the divisor Θτ ⊂Xτ is irreducible and symmetric. Indeed
these two conditions precisely say that the perverse sheaf δΘτ is simple and
isomorphic to its adjoint dual.
82
Chapter 4 – The Tannaka group of the theta divisor
Let U0 ⊆U be the open dense stratum so that G0 ⊆G(g) is the Tannaka
group of the theta divisor on a generic ppav. By lemma 4.6 the perverse
intersection cohomology sheaf of such a theta divisor corresponds on the
Tannakian side to the restriction V|G0 of the standard representation V of
the special orthogonal or symplectic group G(g).
PROPOSITION 4.12. With notations as above, the following properties
hold for the Tannaka groups of smooth theta divisors.
(1) For g = g1 + g2 the generic Tannaka group G0 has a subquotient
which is isogenous to
G(g1)×G(g2),
provided that theorem 4.2 holds for the dimensions g1 and g2.
(2) There exists a connected subgroup H ,→G0 and an irreducible
representation W of H such that
V|H =
(
W ⊕1⊕1
if g is even,
W ⊕1
if g is odd,
where 1 denotes the one-dimensional trivial representation.
(3) For g ≥4 and any stratum Ui of codimension at most one in U
there exists a homomorphism
f : Sl2g−2(Λ) −→Gi
such that f ∗(V) contains the g−1st fundamental representation of
the special linear group as a direct summand.
Proof. Consider a morphism from a smooth irreducible quasi-projective
complex curve S to the moduli space Ag,n such that the generic point of S is
mapped into some stratum Ui in the above stratiﬁcation, and ﬁx a geometric
generic point η of S. Passing to the strict Henselization of S at s ∈S(C)
we can form the perverse sheaf Ψ(δΘη) ∈Perv(Xs,C) of nearby cycles. By
theorem 3.15 we have an embedding
G(Ψ(δΘη)) ,→G(δΘη) = Gi ,→G(g)
such that Ψ(δΘη) corresponds on the Tannakian side to the restriction of the
standard representation V to the subgroup G(Ψ(δΘη)). We will apply this
remark in the following situations.
For part (1) take S ,→Ag,n to be an embedding of a smooth curve which
meets the locus of decomposable ppav’s in a single point s ∈S(C) but which
is otherwise contained in the open dense stratum U0 and has the properties
4.4. Degenerations of abelian varieties
83
in lemma 4.11. We choose the point s such that the corresponding ppav and
its theta divisor have the form
Xs = X1 ×X2
resp.
Θs = (Θ1 ×X2)∪(X1 ×Θ2),
where for α ∈{1,2} the Xα are general complex ppav’s of dimension gα
with a symmetric theta divisor Θα. In particular, like for any divisor with
two components which intersect each other transversally along a smooth
subvariety, we have an exact sequence
0 −→δΘ1×Θ2 −→ΛΘs[g−1] −→δΘ1×X2 ⊕δX1×Θ2 −→0
of perverse sheaves. Restricting this short exact sequence to the open dense
subset
V = Xs \Sing(ΘS) ⊂Xs
we get a monomorphism
δΘ1×Θ2|V ,→ΛΘs[g−1]|V = sp(δΘη)|V
of perverse sheaves, where the last equality holds by the formula for the
specialization in corollary 4.10. Now by the last statement in lemma 4.11
we can assume that the singular locus Sing(ΘS) is a proper closed subset
of Sing(Θs) = Θ1 ×Θ2, and in this case the open dense subset V will have
non-empty intersection with Θ1 × Θ2. Then via intermediate extension it
follows from the above that the semisimpliﬁcation of sp(δΘη) contains a
direct summand δΘ1×Θ2. By the properties of the monodromy ﬁltration
in section 4.3 the same then a fortiori holds for the semisimpliﬁcation of
the perverse sheaf of nearby cycles Ψ(δΘη). This being said, our claim
follows from the elementary observation that the Tannaka group G(δΘ1×Θ2)
is isogenous to G(δΘ1)×G(δΘ2).
For part (2) let s ∈Ag,n(C) be a point which corresponds to a general
ppav Xs with a vanishing theta null, and let S ,→Ag,n be a general curve
which passes through s but is otherwise contained in the open stratum U0
and has the properties in lemma 4.11. For the special ﬁbre with a vanishing
theta null we know from [26] with the correction given in [53, rem. 4.5],
or alternatively also from theorem 4.2 of loc. cit., that the theta divisor Θs
has an isolated ordinary double point e as its only singularity. Hence the
Picard-Lefschetz formula [32, exp. XV, th. 3.4] says that
χ(Θs) = χ(Θη) + (−1)g = (−1)g−1 ·(g!−1)
because the generic theta divisor Θη is smooth of dimension g −1 with
Euler characteristic (−1)g−1 · g! by the Gauss-Bonnet theorem. Now the
perverse intersection cohomology sheaf near an ordinary double point can
84
Chapter 4 – The Tannaka group of the theta divisor
be controlled explicitly, indeed lemma 4.16 below gives an exact sequence
of perverse sheaves
0 −→κg −→ΛΘs[g−1] −→δΘs −→0
for the skyscraper sheaf
κg =
(
δe(−g−2
2 )
if g is even,
0
if g is odd.
Hence it follows that
χ(δΘs) = χ(ΛΘs[g−1])−χ(κg) =
(
g!−2
if g is even,
g!−1
if g is odd.
On the other hand, by remark 4.7 we can assume that the nearby cycles
for our degeneration coincide with the unipotent nearby cycles. Then from
the formula for the specialization in corollary 4.10 one deduces that the
semisimpliﬁcation of the nearby cycles must have the form
Ψ(δΘη)ss = δΘs ⊕γ
for some perverse skyscraper sheaf γ supported on the singular point e of
the special ﬁbre. Looking at the above Euler characteristics, one sees that
this skyscraper sheaf γ must have rank two if g is even, resp. rank one if g
is odd. Now take a Levi splitting
Gs = G(δΘs) ,→G(Ψ(δΘη)),
and let W be the irreducible representation of Gs which corresponds to the
simple perverse sheaf δΘs. In lemma 4.13 below we will see as a general
fact about irreducible theta divisors that the restriction ofW to the connected
component H = G0
s ⊆Gs remains irreducible, so our claim follows.
For part (3) consider the locus J ⊂Ag,n of Jacobian varieties of smooth
projective curves of genus g. If a stratum Ui ⊆U has codimension at most
one in the open subset U, then the closure Ui ⊆Ag,n has codimension at
most one in Ag,n. In this case it has been observed in [83, cor. (0.7)] that
the intersection J ∩Ui is nonempty and hence of codimension at most one
in J. We can then ﬁnd a point t ∈Ui(C) which corresponds to the Jacobian
variety of a non-hyperelliptic smooth curve (indeed the hyperelliptic locus
has codimension greater than one in J for g ≥4). Now consider in the
closure Ui a curve which meets the Jacobian locus J in the chosen point t
and is otherwise contained in the open dense subset Ui ⊂Ui. Deﬁne
ϕ : S −→Ag,n
to be the normalization of this curve, and choose s ∈S(C) to be any point
with ϕ(s) = t. Then XS →S is a family of ppav’s whose geometric generic
ﬁbre Xη is a ppav in the stratumUi and whose special ﬁbre Xs is the Jacobian
