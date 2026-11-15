---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-010-8-harmonic-polynomials
section_title: "Harmonic polynomials"
section_number: 8
pages: 16-21
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
toc_source: inferred
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 18 sections: Front matter; Contents; Introduction."
---
We study in some more detail the harmonic polynomials cΓ ∈He(h∗) associated to a 2n-cycle Γ ∈
H2n(S( ¯O)) over ¯O by the relation
θΓ (λ) = cΓ (λ)θO + o(|λ|e).
(1)
These polynomials, or variants thereof, have a history. When θΓ represents a coherent family of virtual
characters of Harish-Chandra modules, then cΓ is the character polynomial studied by King [1979] using
results of Joseph [1980], except that in King’s deﬁnition the polynomials are not canonically normalized:
there they are deﬁned up to a constant factor which depends on an arbitrary regular element in the
REPRESENTATIONS OF WEYL GROUPS
17
Cartan ho. King shows that these polynomials are essentially the same as the polynomials introduced by
Jantzen [1977], Joseph [1980], and Vogan [1978]. The approach taken here is logically independent of (but
strongly inspired by) these developments; it opens up some (from the previous point of view) surprising
perspectives, among them the relation of the cΓ to the homology of the ﬂag variety, and a formula for the
cΓ in terms of Euler numbers.
Write
Γ =

y∈W/Wo
myy · S1.
(2)
Then
θΓ (λ) = 1
π

y∈W
myey−1λ.
(3)
Expanding the exponential gives
θΓ (λ) =
∞

k=0
1
k!
1
π

y∈W
myy−1λk.
(4)
Comparing (1) and (4) one ﬁnds that

y∈W
myy−1λk = 0
for k < e
(5)
and

y∈W
myy−1λe = cΓ (λ)pO
(6)
where
pO = e!πθO.
(7)
From equation (7) it appears that pO is a Go-invariant distribution on go (the Wo-invariant polynomial
π on ho extends to a Go-invariant polynomial on go), but from (6) one sees that on ho
pO is a Wo-invariant polynomial on h, homogeneous of degree e = e(O).
(8)
(In this interpretation we used implicitly Harish-Chandra’s regularity theorem, which guarantees that θO
is a locally integrable function on go.)
The relation (6) is an amazingly powerful tool for analyzing the polynomials cΓ . First of all we get
from (6) a fromula for the cΓ for arbitrary Γ ∈H2n(S( ¯O)):
If Γ =

y∈W/Wo
myy · S1 , then cΓ =
1
pO(x)

y∈W
myy · xe
(9)
REPRESENTATIONS OF WEYL GROUPS
18
For any x ∈h with pO(x)̸ = 0. In particular, for Γ = Sw (any w ∈W/Wo) we take for O = O(w) the
unique nilpotent Go-orbit in igo∗which intersects s1⊥∩igo∗densely (which amounts to O intersecting
bo
⊥∩w−1bo
⊥densely if we think of O as a Go-orbit on go∗and represent w ∈W/Wo as (1, w)); then
Sw ∈H2n(S( ¯O(w))) and according to Corollary 5.2
Sw =

y∈W/Wo
(−1)l(w)−l(y)Euy(Sw)y · S1.
(10))
Γ = Sw ∈H2n(S( ¯O)) corresponds to the fundamental cycle [Bνw] ∈H2e(B) of the component Bν
w of Bν
under the map
H2n(S( ¯O)) →H2n(S(O)) ≈H2e(Bν)Ao(ν) →H2e(B).
From the deﬁnition of cΓ the corresponding cΓ = cw is explicitly given by the formula
cw(λ) =

Bν w
eωλ.
(11)
On the other hand, the formula (9) says that
cw =
1
pO(x)

y∈W
(−1)l(w)−l(y)Euy(Sw)y · xe
(12)
for any x ∈h with pO(x)̸ = 0. Comparing (11) and (12) leads to the curious integral formula

Bν w
eωλ =
1
pO(x)

y∈W
(−1)l(w)−l(y)Euy(Sw)⟨λ, y · x⟩e
(12)
for any x ∈h with pO(x)̸ = 0
The polynomials cΓ have some positiviy and integrality properties which should be mentioned.
When λ ∈h∗is the s1-heighest weight of a ﬁnite-dimensional representation Vλ of G, the integral on the
left of (13) can be thought of as follows.
Embed the ﬂag-manifold B of G into the projective space PVλ of Vλ by
iλ : B →PVλ, b →[b-highest weight vector].
(14)
Then
ωλ = iλ∗ωP Vλ
where ωP Vλ is the K¨ahler 2-form of the Fubini-Study metric on PVλ. Thus for a complex subvariety V of
B,

V
eωλ = volλ(V ) =
1
(dimV )!degλ(V )
(15)
REPRESENTATIONS OF WEYL GROUPS
19
where volλ(V) is the volume of V with respect to the metric on B coming from the embedding (14) and
degλ(V ) is the degree of the projective variety iλ(V ) in PVλ. (See [Griﬃth-Harris 1978], p. 171, for
example.) The formula (11) says that for λ regular, s1-positive, integral
cw(λ) = volλ(Bνw) = 1
e!degλ(Bνw).
(16)
Thus
e!cw(λ) is positive integral for regular, s1-positive, integral λ.
(17)
We want a more explicit formula for the Wo-invariant polynomial pO. For that purpose we make a
particular choice for Γ ∈H2n(S( ¯O)) as follows.
We know that the W-quotient H2n(S(O)) of H2n(S( ¯O)) is ≈H2e(Bν)Ao(ν) and contains the
A(ν)-invariants He(Bν)A(ν) as an irreducible subrepresentation (isomorphic with the space He(h∗) of
W-harmonic polynomials on h∗). Let
χO = character of Wo on H2e(Boν)Ao(ν).
(Note that we passed from the irreducible representation H2eo(Bν)A(ν) of W = Wo × Wo to the cor-
responding irreducible representation H2e(Boν)Ao(ν) of Wo.) It follows from these remarks that we can
choose Γ = ΓO in H2n(S( ¯O)) so that
my = eo
|W|χO(y)
(18)
where
eo = degχO = dimBoν
and we identify W/Wo = Wo via (y1, y2) →y1y2−1 to think of χO as a function on W/Wo (or as a
Wo-bi-invariant function on W). Explicitly:
χO(y) = χO(y1y2−1)
when we write y ∈W = Wo × Wo as y = (y1, y2). With this choice of my the element

y∈W
myy−1 = eo
|W|

y∈W
χO(y)y−1
(19)
of the group ring of W operates as the projection on the Wo-invariants of type χO ⊗χO, which have
dimension = 1 in the irreducible W-module of this type.
Write out the equation (6) with my given by (18):
cO(λ)pO(x) = eo
|W|

y∈W
χO(y)⟨λ, y · x⟩e.
(20)
REPRESENTATIONS OF WEYL GROUPS
20
If one identiﬁes h and h∗by a W-invariant, C-bilinear, symmetric, inner product, then the right side of
(20) is symmetric in λ and x, since χO(y) = χO(y−1) as function of W. As a consequence,
cO = const.pO
(21)
for some constant depending only on O. In particular, pO belongs to He(h∗), and consequently:
pO =
eo
cO(λ)|W|

y∈W
χO(y)y−1 · λe
(22)
is the (up to a constant factor) unique Wo-invariant, harmonic polynomial on ho which transforms under
W by χO ⊗χO. In (22) we can take any λ for which cO(λ)̸ = 0. For the same values (18) of mw the
relations (5) and (6) imply:
The W-representation of type χO ⊗χO occurs with multiplicity one in degree e = e(O) in C[h∗]
and not at all in lower degree.
This follows from (5), (6), and (22), since the λk span the homogeneous polynomials of degree k on h∗
and each irreducible subspace of type C[h∗] contains exactly one Wo-invariant (up to scalar multiples).
On the other hand, C[h∗] ≈C[ho
∗] ⊗C[ho
∗] as W = Wo × Wo module, so we can pass from W to Wo to
get the following result of Borho-Macpherson [1981]:
8.1 Lemma. The Wo-representation of type χO occurs with multiplicity one in degree eo = eo(O)
in C[ho
∗] and not at all in lower degree.
To make use of the formula (22) for pO one needs to know when cO(λ)̸ = 0. This happens exactly when
the linear functional
Ce[h∗] →C, c →c(λ)
has a nonzero value on the Wo-invariant therein. That functional is the restriction of the natural pairing
of polynomials on h∗with the formal power series eλ on h. Hence :
cO(λ)̸ = 0 iﬀλe has a non-zero component along the Wo-invariant in Ce[h∗].
A simple suﬃcient condition is:
cO(λ)̸ = 0 whenever λ is regular in h∗.
To see this , recall that for regular λ the map
H(h∗) →C[W], c →

w
c(w · λ)w
is a W-isomorphism. Under this isomorphism the linear functional c →c(λ) corresponds to evaluation
at 1 in the regular representation of W, hence has the non-zero component deg χ along each irreducible
character χ of Wo (considered as a Wo-bi-invariant function on W). We summarize what has transpired
in a theorem.
REPRESENTATIONS OF WEYL GROUPS
21
8.2 Theorem. Let Γ ∈H2n(S( ¯O)) be a 2n −cycle Γ over ¯O on the conormal variety S of the
Go-orbits on B, cΓ ∈He(h∗) the associated harmonic polynomial on h∗:
θΓ (λ) = cΓ (λ)θO + o(|λ|e).
If Γ = 
y∈W/Wo myy·S1, then cΓ =
1
pO(x)

y∈W myy·xe. Here pO is the (up to a constant factor) unique
Wo-invariant, harmonic polynomial on h which transforms under W by χO ⊗χO; χO is the (irreducible)
character of Wo on H2e(Boν)Ao(ν); x ∈h is arbitary subject to pO(x)̸ = 0, which is the case whenever x
is regular. The Wo-representation of type χO occurs with multiplicity one in degree eo = eo(O) in C[ho
∗]
and not at all in lower degree. In particular, if Γ = Sw, the fundamental cycle to the conormal of the
Go-orbit Sw, then cΓ = cw is given by
cw =
1
pO(x)

y∈W
(−1)l(w)−l(y)Euy(Sw)y · xe.
