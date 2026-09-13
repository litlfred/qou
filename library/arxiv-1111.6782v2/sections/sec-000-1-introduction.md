---
doc_id: arxiv-1111.6782v2
doc_title: "Stationary Points of O’Hara’s Knot Energies"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-13
source_pdf: 1111.6782v2.pdf
source_sha256: 5acfde49432e59e3
doc_brief: "Stationary Points of O’Hara’s Knot Energies — In this article we study the regularity of stationary points of the knot ener- gies E(α) introduced by O’Hara in [ 14, 15, 16] in the range α∈ (2, 3)."
---
2 Continuous di ﬀerentiability 4
3 Regularity of stationary points 13
A Results on fractional Sobolev spaces 17
1 Introduction
The motion of a knotted charged ﬁber within a viscous liquid s erved as model for the
deﬁnition of so-called knot energies introduced by Fukuhara [ 11]. One hopes that it
will reach a stationary point minimizing its electrostatic energy and that the resulting
shape will help to determine its knot type. The general idea is that this procedure leads
to a “nicer shape” for a given knot in the same knot class, i. e. a representative that is
as little entangled as possible with preferably large distances between diﬀerent strands.
∗Mathematics Institute, Zeeman Building, University of Warwick, Coventry CV4 7AL, United Kingdom,
S.Blatt@warwick.ac.uk
∗∗Abteilung f¨ ur Angewandte Mathematik, Universit¨ at Freib urg, Hermann-Herder-Straße 10, 79104
Freiburg i. Br., Germany,reiter@mathematik.uni-freiburg.de
MSC (2000) 42A45, 53A04, 57M25
The ﬁnal publication is available at www.springerlink.com.
1
For a general deﬁnition and an outline of di ﬀerent knot energies we refer the reader to
O’Hara [17]. Recent developements include the investigation of geome tric curvature
energies such as the integral Menger curvature, see Strzele cki, Szuma´ nska, and von
der Mosel [21, 22], which also extends to surfaces [23], or tangent-point energies [24]
whose domains can be characterized via Sobolev-Slobodecki j spaces [4]. Attraction
phenomena may also be modeled by a corresponding “inverse kn ot energy”, see Alt
et al. [ 2] for an example from mathematical biology discussing inter action between
pairs of ﬁlaments via cross-linkers.
In this paper, we investigate stationary points of the most p rominent family of knot
energies E(α) : C0,1(R/Z, Rn)→ [0,∞],
γ↦−→
∫
R/Z
∫1/2
−1/2
( 1
|γ(u +w)−γ(u)|α− 1
dγ(u +w, u)α
)⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐γ′(u)
⏐⏐⏐dw du,
where α ∈ [2, 3), which goes back to O’Hara [ 14, 15, 16]. Here dγ(u + w, u) de-
notes the intrinsic distance between γ(u + w) and γ(u) on the curve γ. More pre-
cisely, dγ(u +w, u) := min(L (γ|[u,u+w]), L (γ)− L (γ|[u,u+w]))provided|w|≤ 1
2 where
L (γ) :=
∫1
0 |γ′(θ)| dθ is the length ofγ.
The energy E(2) was thoroughly studied by Freedman, He, and Wang [10] who coined
the name “M¨ obius energy” due to the M¨ obius invariance of this energy. While the
existence of mimizers of the M¨ obuis energy is ensured in prime knot classes only,
O’Hara [15, 16] proved the existence of minimizers within any knot class ifα∈ (2, 3).
Abrams et al. [ 1] proved that circles are the global minimizers of all these e nergies
among all curves.
As to the regularity of stationary points , the ﬁrst result was obtained by He [ 13] for
α = 2 who initially assuming H2,3-regularity obtained C∞ by a bootstrapping argu-
ment. Together with a purely geometric result by Freedman, He, and Wang [10] heavily
relying on the M¨ obius invariance, this givesC∞-regularity for all local E(2)-minimizers
(which exist at least in prime knot classes). An outline is gi ven in [18]. Moreover, He
was able to show that under suitable conditions any planar (i. e. n = 2) stationary point
of E(2) is a circle [13, Thm. 6.3]. The argument highly relies on the M¨ obius invariance
of E(2).”
In [19], parts of these results were carried over to the energiesE(α) forα∈ [2, 3). It was
shown that stationary points in Hα,2∩ H2,3 of the energy E(α) +λL , where L denotes
the length functional andλ >0 is a constant, are smooth. Here Hs,p denote the Bessel
potential spaces. Unfortunately, one does not know whether local minimizers of E(α)
belong to Hα,2∩ H2,3 since the techniques used by Freedman, He, and Wang [ 10] to
show the regularity of local minimizers completely break down in these cases.
In this article we will close this gap by proving a much stronger result. We will extend
the results in [19] and [16] and prove smoothness of stationary points of the functionals
E(α) +λL under very natural conditions: We will only assume that the curveγ we are
looking at is parametrized by arc-length (which means no los s of generality as E(α) is
invariant of parametrization) and satisﬁes E(α)(γ)<∞.
The ﬁrst step to show this result is to extract as much informa tion regarding the reg-
ularity of γ out of the ﬁniteness of the energy E(α) as possible. After some partial
result [7] in this direction, in [ 3] a classiﬁcation of all curves with ﬁnite energy was
given: An embedded curve parametrized by arc-length has ﬁni te energy E(α) if and
only if it belongs to the fractional Sobolev space H(α+1)/2,2.
2
Since formulas for the ﬁrst variation of E(α) are only known under the assumption
thatγ∈ H2, we then have to extend these to injective curves in H(1+α)/2 parametrized
by arc-length. In fact our method even allows us to show that E(α) is continuously
diﬀerentiable on this space. To state the result, let
Uε := R/Z×
(
[− 1
2,−ε]∪ [ε, 1
2]
)
.
Theorem 1.1. Letα∈ (2, 3). The energies E(α) are C1-diﬀerentiable on the space of all
injective regular curvesγ∈ H(1+α)/2. Furthermore, if γ is parametrized by arc-length,
the derivative atγ in direction h is given by1
δE(α)(γ; h) = lim
εց0
/iintegdisplay
Uε
(
(α− 2)⟨γ′(u), h′(u)⟩
|w|α + 2 ⟨γ′(u), h′(u)⟩
|γ(u +w)−γ(u)|α
−α⟨γ(u +w)−γ(u), h(u +w)− h(u)⟩
|γ(u +w)−γ(u)|α+2
)
dw du.
Note that this is a principle value integral, i. e. we may not replace Uε by U0.
Now we are in the position to state the main result of this article.
Theorem 1.2. Let α∈ (2, 3) andγ∈ C0,1(R/Z, Rn) be a curve parametrized by arc-
length with E (α)(γ) <∞. If γ is furthermore a stationary point of E (α) +λL , i. e.
if
δE(α)(γ; h) +λ
∫
R/Z
⟨γ′, h′⟩= 0 ∀h∈ H(1+α)/2(R/Z, Rn),
thenγ∈ C∞(R/Z, Rn).
The gradient ﬂow of the M¨ obius energyE(2) was ﬁrst discussed by He [ 13] where he
states short time existence results for smooth initial data. In [6], the short time existence
was proven for all intial data inC2,β,β> 0, and ﬁrst long time existence results for this
gradient ﬂow near local minimizers were derived. For a discussion of gradient ﬂow for
E(α) +λL for positiveλ andα∈ (2, 3) or the gradient ﬂow of E(α) with respect to ﬁxed
length we refer the reader to [5].
The energies E(α) represent only the one-parameter range p = 1 of the larger family of
knot energies
Eα,p(γ) :=
∫
R/Z
∫1/2
−1/2
( 1
|γ(u +w)−γ(u)|α− 1
dγ(u +w, u)α
)p ⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐γ′(u)
⏐⏐⏐dw du,
whereαp≥ 2 and (α− 2)p< 1, see O’Hara [15, 16] and [3, 7]. We do not expect that
our results or the results for the gradient ﬂow of the energies carry over to p> 1 as we
expect the ﬁrst variation to be a degenerate elliptic operator in this case.
Let us close this introduction by brieﬂy introducing some no tation and the Sobolev
spaces of fractional order which are also referred to as Bessel potential spaces . For
s∈ R and p∈ [1,∞] let Hs,p := (id−∆)−s/2Lp where ∆denotes the Laplacian. There are
several equivalent deﬁnitions, e. g. by interpolation. In c ase p = 2, which mainly ap-
plies to our situation, the Bessel potential spaces coincide with the Slobodeckij spaces.
This gives rise to the following fundamental characterization of Hs,2, s∈ (0,∞)\ N.
1Ifγ belongs to Hα+1 one can use partial integration to obtain a formula for the L2 gradient like in [19,
Thm. 2.24].
3
Let f∈ L2(R/Z, Rn). For s∈ (0, 1) we deﬁne the seminorm
[ f]
Hs,2 :=
(∫
R/Z
∫ 1/2
−1/2
| f (u +w)− f (u)|2
|w|1+2s dw du
)1/2
.
Then the Sobolev space Hk+s,2(R/Z, Rn), k ∈ N∪{ 0}, is the set of all functions
Hk,2(R/Z, Rn) for which the norm
‖f‖Hs+k,2 :=‖f‖Hk,2 +
[
f (k)]
Hs,2
is ﬁnite. We will frequently use the embedding
Hk+s,2(R/Z, Rn)֒→Ck+s−1/2(R/Z, Rn), s∈ ( 1
2, 1), (1.1)
see, e. g., Taylor [ 25, Chap. 4, Prop. 1.5]. For further information on Sobolev spa ces
we refer to the books by Grafakos [ 12, Chap. 6], Runst and Sickel [ 20, Chap. 2], and
Taylor [25, Chap. 4 and 13].
For some space X⊂ C1(R/Z, Rn) we will denote by Xir the (open) subspace consisting
of all injective (embedded) and regular curves in X.
The standard scalar product in Rn is denoted by⟨·,·⟩, for complex vectors a, b∈ Cn we
deﬁne⟨a, b⟩Cn := ∑d
k=1 akbk. The L2-scalar product is, as usual, given by ⟨f,g⟩L2 :=∫1
0 ⟨f (u),g (u)⟩du.
Unless stated otherwise, we will assume
α∈ (2, 3)
throughout this paper.
Acknowledgements. The ﬁrst author was supported by the Swiss National Science
Foundation Grant Nr. 200020 125127 and the Leverhulm trust. The second author was
supported by DFG Transregional Collaborative Research Centre SFB TR 71.
2 Continuous di ﬀerentiability
In this section, we want to prove the following proposition f rom which Theorem 1.1
will follow quite easily. Recall that Uε = (R/Z)× ([−1/2,−ε]∪ [ε, 1/2]).
Proposition 2.1. Forα∈ (2, 3) the energies E (α) are continuously di ﬀerentiable on
H(α+1)/2,2
ir . The derivative of E (α) atγ∈ H(α+1)/2,2
ir in direction h∈ H(α+1)/2,2 is given by
δE(α)(γ; h) =
lim
εց0
/iintegdisplay
Uε
{
2
( 1
|γ(u +w)−γ(u)|α− 1
dγ(u +w, u)α
)⟨γ′(u)
|γ′(u)|2, h′(u)
⟩
−α

⟨γ(u +w)−γ(u), h(u +w)− h(u)⟩
|γ(u +w)−γ(u)|α+2 −
d
dτ
⏐⏐⏐τ=0 dγ+τh(u +w, u)
dγ(u +w, u)α+1

}
|γ′(u +w)||γ′(u)| dw du.
(2.1)
4
Note that since γ∈ C1 the derivative d
dτ
⏐⏐⏐τ=0 dγ+τh(u +w, u) is well deﬁned for almost
all (u,w )∈ R/Z× [−1/2, 1/2]. More precisely, we can deduce from
dγ(u +w, u) = min{L (γ|[u,u+w]), L (γ)− L (γ|[u,u+w])}
that
d
dτ
⏐⏐⏐τ=0 dγ+τh(u +w, u)
=

|w|
∫1
0
⟨γ′(u+σw)
|γ′(u+σw)|, h′(u +σw)
⟩
dσ, if L (γ|[u,u+w])< 1
2 L (γ),
−|w|
∫1
0
⟨γ′(u+σw)
|γ′(u+σw)|, h′(u +σw)
⟩
dσ, if L (γ|[u,u+w])> 1
2 L (γ).
(2.2)
To prove Proposition 2.1, we will ﬁrst show that the following approximations of the
energy E(α), in which we cut o ﬀthe singular part, are continuously di ﬀerentiable and
give a formula for the derivative. Forε> 0 we set
E(α)
ε (γ) :=
/iintegdisplay
Uε
( 1
|γ(u +w)−γ(u)|α− 1
dγ(u +w, u)α
)⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐γ′(u)
⏐⏐⏐dw du.
To be more precise, we will show that E(α)
ε is C1 on the space of all embedded regular
curves of class C1, which due to the embedding (1.1) especially implies the continuous
diﬀerentiability on H(α+1)/2,2
ir .
The general strategy of the proof will be fairly standard. We ﬁrst derive a formula
for the pointwise variation of the integrand in the deﬁnitio n of E(α)
ε and E(α) which
holds almost everywhere. After that we will carefully analy se this formula in order to
prove that the integrand deﬁnes a continuously diﬀerentiable map from C1
ir(R/Z, Rn) to
L1(Uε). This allows us to deduce that E(α)
ε is continuously diﬀerentiable.
Lemma 2.2. The functional E (α)
ε is continuously diﬀerentiable on the space of all in-
jective regular curves in C 1(R/Z, Rn). The directional derivative at γ in direction
h∈ C1(R/Z, Rn) is given by
δE(α)
ε (γ; h) =
/iintegdisplay
Uε
{
2
( 1
|γ(u +w)−γ(u)|α− 1
dγ(u +w, u)α
)⟨γ′(u)
|γ′(u)|2, h′(u)
⟩
−α

⟨γ(u +w)−γ(u), h(u +w)− h(u)⟩
|γ(u +w)−γ(u)|α+2 −
d
dτ
⏐⏐⏐τ=0 dγ+τh(u +w, u)
dγ(u +w, u)α+1

}
|γ′(u +w)||γ′(u)| dw du.
(2.3)
Proof. Letγ0∈ C1(R/Z, Rn) be injective and regular and U⊂ C1(R/Z, Rn) be an open
neighbourhood ofγ0 such that there is a constant c> 0 with
min{|γ(u +w)−γ(u)|, dγ(u +w, u)}≥ c|w|, |γ′(u)|≥ c (2.4)
for allγ∈ U and (u,w )∈ R/Z× [−1/2, 1/2].
We will show that the integrand used to deﬁne the energies E(α) and E(α)
ε , i. e.
(Iγ)(u,w ) :=
( 1
|γ(u +w)−γ(u)|α− 1
dγ(u +w, u)α
)
|γ′(u +w)||γ′(u)|,
5
deﬁnes a continuously di ﬀerentiable operator from U into L1(Uε) for any ε >0 with
directional derivative
d
dτ (I(γ +τh)) (u,w )
⏐⏐⏐⏐⏐τ=0
=
( 1
|γ(u +w)−γ(u)|α− 1
dγ(u +w, u)α
)
·
(⟨γ′(u)
|γ′(u)|, h′(u)
⟩⏐⏐⏐γ′(u +w)
⏐⏐⏐+
⟨γ′(u +w)
|γ′(u +w)|, h′(u +w)
⟩⏐⏐⏐γ′(u)
⏐⏐⏐
)
−α

⟨γ(u +w)−γ(u), h(u +w)− h(u)⟩
|γ(u +w)−γ(u)|α+2 −
d
dτ
⏐⏐⏐τ=0 dγ+τh(u +w, u)
dγ(u +w, u)α+1

⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐γ′(u)
⏐⏐⏐.
(2.5)
The statement then follows from the chain rule and the fact that the operator
L1(Uε)→ R,
g↦→
/iintegdisplay
Uε
g(u,w ) du dw,
is continuously diﬀerentiable as it is a bounded linear operator.
The only non-trivial thing here is to deal with the intrinsic distance dγ in the integrand
that deﬁnes E(α)
ε . Obviously dγ(u,w ) deﬁnes a continuous operator from C1(R/Z, Rn)
to L∞(R/Z× [−1/2, 1/2]).
Using the fact that one has
dγ(u +w, u) = min{L (γ|[u,u+w]), L (γ)− L (γ|[u,u+w])}
and thatγ is regular, one can see that
d
dτ
⏐⏐⏐τ=0 dγ+τh(u +w, u) = D(γ, h)(u,w ) (2.6)
for all u,w with L (γ|[u,u+w]) /nequal1
2 L (γ) where
D(γ; h)(u,w ) :=

|w|
∫1
0
⟨γ′(u+σw)
|γ′(u+σw)|, h′(u +σw)
⟩
dσ, if L (γ|[u,u+w])< 1
2 L (γ),
−|w|
∫1
0
⟨γ′(u+σw)
|γ′(u+σw)|, h′(u +σw)
⟩
dσ, if L (γ|[u,u+w])≥ 1
2 L (γ).
(2.7)
Sinceγ is regular, the set L (γ|[u,u+w]) = 1
2 L (γ) is a compact C1 submanifold of R/Z×
[−1/2, 1/2] and hence a null set. Thus (2.6) and (2.5) hold almost everywhere.
Obviously, D deﬁnes a continuous operator from the space C1
ir(R/Z, Rn)× C1(R/Z, Rn)
to L1(Uε).
From Equation (2.5) we can read oﬀthat
(DI(γ)(h)) := d
dτ I(γ +τh)(u,w )
⏐⏐⏐⏐⏐τ=0
deﬁnes an operator C1(R/Z, Rn)→ L1(Uε) that continuously depends onγ. Hence I is
a continuously diﬀerentiable operator from U to L1(Uε).
Integrating and using a suitable reparametrization we then derive (2.3) from (2.5). □
6
Unfortunately, the energies E(α)
ε do not form a Cauchy sequence in C1(H(α+1)/2,2
ir ) –
actually not even in C0(H(α+1)/2,2
ir ) basically due to the fact that bounded sequences
in L1 are not uniformly integrable. We will deduce Proposition 2.1 from Lemma 2.2
which roughly speaking shows that E(α)
ε is nearly a Cauchy sequence in C1(Xδ) for
certain subsets Xδ⊂ H(α+1)/2,2, δ≥ 0. We will allow subsets Xδ⊂ H(α+1)/2,2 which
satisfy the following substitute of the uniform integrability property
lim sup
ε→0
sup
γ∈Xδ
(/iintegdisplay
R/Z×[−ε,ε]
|γ′(u +w)−γ′(u)|2
|w|α dwdu
)1/2
≤δ. (2.8)
Recall that lipY E = sup
f, ˜f∈Y
f /nequal˜f
⏐⏐⏐E( f )− E( ˜f )
⏐⏐⏐
‖‖‖f− ˜f
‖‖‖ for some functional E with Y⊂ domain E.
Lemma 2.3. Letγ0∈ H(α+1)/2,2
ir . Then there is an open neighborhood U ⊂ H(α+1)/2,2
ir
ofγ0 and a constant C<∞, such that E(α)
ε satisﬁes
lim sup
ε1,ε2→0
lipU∩Xδ(E(α)
ε1 − E(α)
ε2 )≤ Cδ (2.9)
for all subsets Xδ⊂ H(α+1)/2,2 satisfying (2.8) withδ∈ [0, 1].
For ﬁxedγ0∈ H(α+1)/2,2
ir and h∈ H(α+1)/2,2 we will apply this lemma later to the sets
X0 :={γ0 +τh :τ∈ (−a, a)}, 0< a<∞,
and
Xδ :={γ∈ H(α+1)/2,2 :‖γ−γ0‖H(α+1)/2,2≤δ}, δ> 0.
Of course we have forγτ :=γ +τh,|τ|≤ a,
(/iintegdisplay
R/Z×[−ε,ε]
|γ′
τ(u +w)−γ′
τ(u)|2
|w|α dwdu
)1/2
≤
(/iintegdisplay
R/Z×[−ε,ε]
|γ′(u +w)−γ′(u)|2
|w|α dwdu
)1/2
+ a
(/iintegdisplay
R/Z×[−ε,ε]
|h′(u +w)− h′(u)|2
|w|α dwdu
)1/2
→ 0 (2.10)
asε→ 0 and forγ∈ Xδ we have
(/iintegdisplay
R/Z×[−ε,ε]
|γ′(u +w)−γ′(u)|2
|w|α dwdu
)1/2
≤

/iintegdisplay
R/Z×[−ε,ε]
|γ′
0(u +w)−γ′
0(u)|2
|w|α dwdu

1/2
+δ→δ
(2.11)
so both satisfy (2.8).
7
Proof. Using that H(α+1)/2,2 continuously embeds into C1 andγ0 is a injective regular
curve, we can ﬁnd an open neighborhood U⊂ H(α+1)/2,2
ir of γ0 and a constant c > 0
such that (2.4) holds for all γ∈ U and (u,w )∈ R/Z× [−1/2, 1/2]. Making U smaller
if necessary, we can also achieve that there is anε0 > 0 such that
dγ(u +w, u) = L (γ|[u,u+w])
for allγ∈ U andw∈ [−ε0,ε 0]. Let nowε0 >ε 2 >ε 1 and let us set
F(α) := E(α)
ε2 − E(α)
ε1 .
We will now rewrite this diﬀerence in a more convenient form. For this let us introduce
the function
g(α)(ζ,η,ϑ,ι ) := ζ−α−η−α
η2−ζ2 ϑι
which is Lipschitz continuous and positive on [˜c,∞)4 for any ˜c > 0. We deﬁne for
u∈ R/Z,w∈ [−ε,ε ]
G(α)
γ : (u,w )↦→g(α)
(⏐⏐⏐⏐⏐⏐
∫1
0
γ′(u +θ1w) dθ1
⏐⏐⏐⏐⏐⏐,
∫1
0
⏐⏐⏐γ′(u +θ2w)
⏐⏐⏐dθ2,
⏐⏐⏐γ′(u +w)
⏐⏐⏐,
⏐⏐⏐γ′(u)
⏐⏐⏐
)
.
We have chosen U in such a way that the arguments in G(α) are uniformly bounded
away from zero.
We decompose the integrand in the deﬁnition of E(α) for|w|≤ ε0 into
( 1
|γ(u +w)−γ(u)|α− 1
dγ(u +w, u)α
)⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐γ′(u)
⏐⏐⏐
= 1
|w|α

1⏐⏐⏐⏐
∫1
0 γ′(u +θ1w) dθ1
⏐⏐⏐⏐
α− 1(∫1
0|γ′(u +θ2w)| dθ2
)α

⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐γ′(u)
⏐⏐⏐
=G(α)
γ (u,w )
(∫1
0|γ′(u +θ2w)| dθ2
)2
−
⏐⏐⏐⏐
∫1
0 γ′(u +θ1w) dθ1
⏐⏐⏐⏐
2
|w|α
=G(α)
γ (u,w )
/iintegtext
[0,1]2 (|γ′(u +θ1w)||γ′(u +θ2w)|−⟨γ′(u +θ1w),γ′(u +θ2w)⟩) dθ1 dθ2
|w|α .
Using 2|a|| b|− 2⟨a, b⟩=|a− b|2−|| a|−| b||2 for a, b∈ Rn this can be written as
1
2G(α)
γ (u,w )
/iintegtext
[0,1]2|γ′(u +θ1w)−γ′(u +θ2w)|2 dθ1 dθ2
|w|α
− 1
2G(α)
γ (u,w )
/iintegtext
[0,1]2 (|γ′(u +θ1w)|−| γ′(u +θ2w)|)2 dθ1 dθ2
|w|α .
8
Hence,
F(α)(γ)
= 1
2
∫
R/Z
∫
ε1<|w|<ε2
G(α)
γ (u,w )
/iintegtext
[0,1]2|γ′(u +θ1w)−γ′(u +θ2w)|2 dθ1 dθ2
|w|α dw du
− 1
2
∫
R/Z
∫
ε1<|w|<ε2
G(α)
γ (u,w )
/iintegtext
[0,1]2 (|γ′(u +θ1w)|−| γ′(u +θ2w)|)2 dθ1 dθ2
|w|α dw du
=: 1
2 F(α)
1 (γ)− 1
2 F(α)
2 (γ).
To estimate the diﬀerence F(α)(˜γ)− F(α)(γ), we ﬁrst consider
⏐⏐⏐⏐G(α)
˜γ (u,w )−G (α)
γ (u,w )
⏐⏐⏐⏐
≤ C
⏐⏐⏐⏐⏐⏐
⏐⏐⏐⏐⏐⏐
∫1
0
˜γ′(u +θ1w) dθ1
⏐⏐⏐⏐⏐⏐−
⏐⏐⏐⏐⏐⏐
∫1
0
γ′(u +θ2w) dθ2
⏐⏐⏐⏐⏐⏐
⏐⏐⏐⏐⏐⏐
+ C
⏐⏐⏐⏐⏐⏐
∫1
0
(⏐⏐⏐˜γ′(u +θw)
⏐⏐⏐−
⏐⏐⏐γ′(u +θw)
⏐⏐⏐
)
dθ
⏐⏐⏐⏐⏐⏐
+ C
⏐⏐⏐
⏐⏐⏐˜γ′(u +w)
⏐⏐⏐−
⏐⏐⏐γ′(u +w)
⏐⏐⏐
⏐⏐⏐+ C
⏐⏐⏐
⏐⏐⏐˜γ′(u)
⏐⏐⏐−
⏐⏐⏐γ′(u)
⏐⏐⏐
⏐⏐⏐
≤ C
∫ 1
0
⏐⏐⏐˜γ′(u +θw)−γ′(u +θw)
⏐⏐⏐dθ + C
⏐⏐⏐˜γ′(u +w)−γ′(u +w)
⏐⏐⏐+ C
⏐⏐⏐˜γ′(u)−γ′(u)
⏐⏐⏐
≤ C
‖‖‖˜γ′−γ′‖‖‖L∞.
We arrive at
⏐⏐⏐F(α)
1 (˜γ)− F(α)
1 (γ)
⏐⏐⏐
≤
/iintegdisplay
R/Z×[−ε2,ε2]
⏐⏐⏐⏐G(α)
˜γ (u,w )−G (α)
γ (u,w )
⏐⏐⏐⏐
/iintegtext
[0,1]2|˜γ′(u +θ1w)− ˜γ′(u +θ2w)|2 dθ1 dθ2
|w|α dw du
+
/iintegdisplay
R/Z×[−ε2,ε2]
⏐⏐⏐G(α)
γ (u,w )
⏐⏐⏐
/iintegtext
[0,1]2
⏐⏐⏐|˜γ′(u +θ1w)− ˜γ′(u +θ2w)|2−|γ′(u +θ1w)−γ′(u +θ2w)|2⏐⏐⏐dθ1 dθ2
|w|α
dw du
≤ C
‖‖‖˜γ′−γ′‖‖‖L∞
/iintegdisplay
[0,1]2
/iintegdisplay
R/Z×[−ε2,ε2]
|˜γ′(u +θ1w)− ˜γ′(u +θ2w)|2
|w|α dw du dθ1 dθ2
+ C
/iintegdisplay
[0,1]2
/iintegdisplay
R/Z×[−ε2,ε2]
|(˜γ′ +γ′)(u +θ1w)− (˜γ′ +γ′)(u +θ2w)|| (˜γ′−γ′)(u +θ1w)− (˜γ′−γ′)(u +θ2w)|
|w|α
dw du dθ1 dθ2
≤ C [ ˜γ′] 2
H(α−1)/2(R/Z×[−2ε2,2ε2])
‖‖‖˜γ′−γ′‖‖‖L∞
+ C [ ˜γ′ +γ′]
H(α−1)/2(R/Z×[−2ε2,2ε2])
[ ˜γ′−γ′]
H(α−1)/2(R/Z×[−2ε2,2ε2])
9
where we set for a subset S⊂ R/Z× [− 1
2, 1
2]
[ f]
H(α−1)/2(S ) :=
(/iintegdisplay
S
| f (u +w)− f (u)|2
|w|α dw du
)1/2
.
For the second term we compute
⏐⏐⏐F(α)
2 (˜γ)− F(α)
2 (γ)
⏐⏐⏐
≤
/iintegdisplay
R/Z×[−ε2,ε2]
⏐⏐⏐⏐G(α)
˜γ (u,w )−G (α)
γ (u,w )
⏐⏐⏐⏐
/iintegtext
[0,1]2(|˜γ′(u +θ1w)|−| ˜γ′(u +θ2w)|)2 dθ1 dθ2
|w|α dw du
+
/iintegdisplay
R/Z×[−ε2,ε2]
⏐⏐⏐⏐G(α)
˜γ (u,w )
⏐⏐⏐⏐·
·
/iintegtext
[0,1]2
⏐⏐⏐(|˜γ′(u +θ1w)|−| ˜γ′(u +θ2w)|)2− (|γ′(u +θ1w)|−| γ′(u +θ2w)|)2⏐⏐⏐dθ1 dθ2
|w|α
dw du
≤ C
‖‖‖˜γ′−γ′‖‖‖L∞
/iintegdisplay
[0,1]2
/iintegdisplay
R/Z×[−ε2,ε2]
|˜γ′(u +θ1w)− ˜γ′(u +θ2w)|2
|w|α dw du dθ1 dθ2
+ C
/iintegdisplay
[0,1]2
/iintegdisplay
R/Z×[−ε2,ε2]
|(|˜γ′(u +θ1w)|−| ˜γ′(u +θ2w)|) + (|γ′(u +θ1w)|−| γ′(u +θ2w)|)|
|w|α/2 ·
·|(|˜γ′(u +θ1w)|−| ˜γ′(u +θ2w)|)− (|γ′(u +θ1w)|−| γ′(u +θ2w)|)|
|w|α/2 dw du dθ1 dθ2
≤ C
‖‖‖˜γ′−γ′‖‖‖L∞
[ ˜γ′] 2
H(α−1)/2(R/Z×[−2ε2,2ε2])
+ C
[ ⏐⏐⏐˜γ′⏐⏐⏐+
⏐⏐⏐γ′⏐⏐⏐
]
H(α−1)/2(R/Z×[−2ε2,2ε2])
[ ⏐⏐⏐˜γ′⏐⏐⏐−
⏐⏐⏐γ′⏐⏐⏐
]
H(α−1)/2(R/Z×[−2ε2,2ε2]).
Using the chain and product rule for Sobolev spaces and the formula
⏐⏐⏐˜γ′⏐⏐⏐−
⏐⏐⏐γ′⏐⏐⏐=⟨˜γ′ +γ′, ˜γ′−γ′⟩
|˜γ′| +|γ′| ,
we get
[ ⏐⏐⏐˜γ′⏐⏐⏐−
⏐⏐⏐γ′⏐⏐⏐
]
H(α−1)/2(R/Z×[−2ε2,2ε2])≤
[ ⏐⏐⏐˜γ′⏐⏐⏐−
⏐⏐⏐γ′⏐⏐⏐
]
H(α−1)/2,2(R/Z)
≤ C
‖‖‖˜γ′−γ′‖‖‖H(α−1)/2,2(R/Z,Rn)
and hence
⏐⏐⏐F(α)
2 (˜γ)− F(α)
2 (γ)
⏐⏐⏐≤ C
([ ˜γ′] 2
H(α−1)/2(R/Z×[−2ε2,2ε2]) +
[ ⏐⏐⏐˜γ′⏐⏐⏐+
⏐⏐⏐γ′⏐⏐⏐
]
H(α−1)/2(R/Z×[−2ε2,2ε2])
)
‖˜γ′−γ′‖H(α−1)/2,2(R/Z,Rn).
From this the claim follows. □
Proof of Proposition 2.1. From the classiﬁcation of all embedded regular curves of ﬁ-
nite energy in [ 3] we get E(α)(γ0) <∞ for all γ0∈ H(α+1)/2,2
ir . From this we deduce
immediately that E(α)
ε converges to E(α) pointwise asε tends to 0.
10
We begin by proving that directional derivatives exist for all directions h∈ H(α+1)/2,2.
Let us ﬁx γ0 ∈ H(α+1)/2,2
ir and let U ⊂ H(α+1)/2,2
ir and C < ∞ be as in Lemma 2.3.
Applying ﬁrst Lemma 2.3 with X0 ={γ0 +τh :τ∈ (−τ0,τ 0)} forτ0 small enough, we
deduce for
fε :τ↦→E(α)
ε (γ0 +τh)
that
⏐⏐⏐f′
ε1(τ)− f′
ε2(τ)
⏐⏐⏐=
⏐⏐⏐δE(α)
ε1 (γ0 +τh; h)−δE(α)
ε2 (γ0 +τh; h)
⏐⏐⏐
≤ lim sup
θ→0
⏐⏐⏐⏐⏐⏐⏐
E(α)
ε1 (γ0 + (τ +θ)h)− E(α)
ε1 (γ0 +τh)
θ − E(α)
ε2 (γ0 + (τ +θ)h)− E(α)
ε2 (γ0 +τh)
θ
⏐⏐⏐⏐⏐⏐⏐
≤ lipU∩X0
(
E(α)
ε1 − E(α)
ε2
)
‖h‖H(α+1)/2,2 (2.12)
ε1,ε2ց0
−−−−−−→0 by ( 2.10).
As E(α)
ε → E(α) pointwise this proves that( fε)ε>0 is a Cauchy sequence inC1((−τ0,τ 0))
converging to E(α)(γ0 +τh) = limεց0 E(α)
ε (γ0 +τh) as ε→ 0. Hence especially all
directional derivatives of E(α) exist and
δE(α)(γ0; h) = lim
εց0
δE(α)
ε (γ0; h)
for allγ0∈ H(α+1)/2,2
ir , h∈ H(α+1)/2,2.
The next step is to establish Gˆ ateaux diﬀerentiability. To this end we merely have to
showδE(α)(γ0,·)∈
(
H(α+1)/2,2
)∗
for γ0∈ H(α+1)/2,2
ir . Linearity carries over from E(α)
ε .
For boundedness we chooseδ∈ (0, 1] such that
Xδ :={γ∈ H(α+1)/2,2
ir :‖γ−γ0‖≤δ}⊂ U.
Now
δE(α)(γ0; h) =δE(α)
ε (γ0; h) +δE(α)(γ0; h)−δE(α)
ε (γ0; h)
=δE(α)
ε (γ0; h) + lim
ε1→0
(δE(α)
ε1 (γ0; h)−δE(α)
ε (γ0; h))
and thus, arguing as in (2.12) and recallingδE(α)
ε (γ0;·)∈
(
H(α+1)/2,2
)∗
,
|δE(α)(γ0; h)|≤| δE(α)
ε (γ0; h)| + lim sup
ε1ց0
lipU∩Xδ
(
E(α)
ε1 − E(α)
ε
)
/bracehtipupleft/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehtipdownright/bracehtipdownleft/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehext/bracehtipupright
<∞
‖h‖H(α+1)/2,2
≤ C‖h‖H(α+1)/2,2
for allγ0∈ H(α+1)/2,2
ir and h∈ H(α+1)/2,2. Hence, E(α) is Gˆ ateaux diﬀerentiable and the
diﬀerential
(
E(α)
)′
(γ0)∈ (H(α+1)/2,2)∗ is given by
(
E(α))′
(γ0) =δE(α)(γ0;·)
for allγ0∈ H(α+1)/2,2
ir , h∈ H(α+1)/2,2.
Finally, to see that the di ﬀerential is continuous, letσ >0 be given and let us choose
δ> 0 andε> 0 so small that
lipU∩Xδ
(
E(α)
ε1 − E(α)
ε2
)(2.9)
≤ Cδ≤ 1
3σ
11
for allε1,ε 2 <ε . Then we have forγ∈ Xδ∩ U and any h∈ H(α+1)/2,2
|δE(γ; h)−δE(γ0; h)|≤| δE(α)(γ; h)−δE(α)
ε (γ; h)| +|δE(α)
ε (γ; h)−δE(α)
ε (γ0; h)|
+|δE(α)
ε (γ0; h)−δE(α)(γ0; h)|
(2.12)
≤|δE(α)
ε (γ; h)−δE(α)
ε (γ0; h)| + 2
3σ‖h‖H(α+1)/2,2.
Since E(α)
ε is C1 we deduce that there is an open neighborhood V⊂ Xδ ofγ0 such that
|δE(α)
ε (γ; h)−δE(α)
ε (γ0; h)|≤ 1
3σ‖h‖H(α+1)/2,2
and hence
|δE(α)(γ; h)−δE(α)(γ0; h)|≤ σ‖h‖H(α+1)/2,2.
This proves that
(
E(α)
)′
is continuous from H(α+1)/2,2
ir into
(
H(α+1)/2,2
)∗
and hence E(α)
is C1(H(α+1)/2,2
ir ). □
Proof of Theorem 1.1. The only thing left to do is to show that for curvesγ∈ H(α+1)/2,2
ir
parametrized by arc-length and h∈ H(α+1)/2,2 the derivative can be given in the form
stated in the theorem. Using that γ is parametrized by arc-length, we get from Propo-
sition 2.1 and (2.2) that
δE(α)(γ; h)
εց0
←−−−
/iintegdisplay
Uε
2
( 1
|γ(u +w)−γ(u)|α− 1
|w|α
)⟨γ′(u), h′(u)⟩
−α
(⟨γ(u +w)−γ(u), h(u +w)− h(u)⟩
|γ(u +w)−γ(u)|α+2 − D(γ, h)(u,w )
|w|α+1
)
dwdu
where now
D(γ, h)(u,w ) =|w|
∫1
0
⟨γ′(u +θw), h′(u +θw)⟩dθ
for all (u,w )∈ R/Z× (−1/2, 1/2). Hence,
δE(α)(γ; h)
εց0
←−−−
/iintegdisplay
Uε
{
2
( 1
|γ(u +w)−γ(u)|α− 1
|w|α
)⟨γ′(u), h′(u)⟩
−α

⟨γ(u +w)−γ(u), h(u +w)− h(u)⟩
|γ(u +w)−γ(u)|α+2 −
∫1
0 ⟨γ′(u +θw), h′(u +θw)⟩dθ
|w|α

}
dwdu
=
/iintegdisplay
Uε
{
2
( 1
|γ(u +w)−γ(u)|α− 1
|w|α
)⟨γ′(u), h′(u)⟩
−α
(⟨γ(u +w)−γ(u), h(u +w)− h(u)⟩
|γ(u +w)−γ(u)|α+2 −⟨γ′(u), h′(u)⟩
|w|α
)}
dwdu
=
/iintegdisplay
Uε
(
(α− 2)⟨γ′(u), h′(u)⟩
|w|α + 2 ⟨γ′(u), h′(u)⟩
|γ(u +w)−γ(u)|α
−α⟨γ(u +w)−γ(u), h(u +w)− h(u)⟩
|γ(u +w)−γ(u)|α+2
)
dwdu. □
12
