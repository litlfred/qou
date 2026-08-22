---
doc_id: arxiv-alg-geom-9408004v1
doc_title: "Cubics, Integrable Systems, and Calabi-Yau Threefolds"
section_id: sec-000-x-this-number-is-conjectured-but-not-known-to-be
section_title: "This number is conjectured, but not known, to be ﬁnite. The m ulti-"
section_number: X
pages: 20-26
source_pdf: 9408004v1.pdf
source_sha256: d3bc00265294aa02
doc_brief: "Cubics, Integrable Systems, and Calabi-Yau Threefolds — 2 sections: This number is conjectured, but no; References"
---
parameterq is deﬁned by q :=e2πit , where t is a set of linear coordinates on
H 2(X, C). Intrinsically, we deﬁne qdk as the function given at t ∈H 2(X, C)
by:
(10) qdk :=e2πid<t,k> .
The sum is expected to converge for t inK, the complexiﬁed K¨ ahler cone of
X, i.e. when Im(t) ∈H 2(X, R) is in the K¨ ahler cone.
In the B-model, V isH 2, 1(X), and the partition function is a normalized
version of the Yukawa cubic, so its coeﬃcients are functions on M. The
Yukawa cubic is deﬁned only up to a scalar factor which is dete rmined by
a choice of holomorphic gauge s ∈H 3, 0(X). In order to get the coeﬃcients
in the partition function to be functions on M (rather than ~M), we need a
section of ~M → M . According to [Mo], one chooses a maximally unipotent
degeneration of X; this determines a vanishing cycle
γ0 ∈H3(X, Z),
20
and s is normalized by the condition
∫
γ 0
s0 = 1.
Physicists believe [Gep] that either the A-model or B-model construc-
tions set up bijections between CFTs and CY families. This, t ogether with
the existence of an internal symmetry of CFT which interchan ges A and B
variables, led [Di,L VW] to the mirror conjecture, which says that each CY
family X → M , perhaps with some extra data, determines another family
X ′ → M ′ such that the A-model CFT of the former is isomorphic to the
B-model CFT of the latter, and vice versa.
It is not clear (to us) what the precise mathematical formula tion of this
conjecture should be. What is clear, though, is that the conj ecture involves
the existence of an isomorphism, called the mirror map .
(11) t : M → K ′
where M is (an open subset of ?) the moduli space of Calabi-Yaus (with
extra structure ?) in the ﬁrst family, and K ′ is the complexiﬁed K¨ ahler cone
of an X ′ in the second family. This should satisfy:
(a) dt :H 1(TX) ∼→H 1, 1(X ′) is an isomorphism. (In particular, the dimen-
sions agree, so that the Hodge diamonds of X,X ′ are obtained from
each other by a 90 ◦ turn).
(b) The partition functions correspond through t, i.e.:
Yukawa (X,s 0) = (Topo X′ +
∑
k∈H2(X′,Z)
d∈Z+
nk(X ′)k3qdk) ◦dt,
where both sides are interpreted as sections of Sym 3T ∗
M.
In [CdOGP], this conjectural equality of partition functio ns was used
to obtain some spectacular predictions for numbers of ratio nal curves of
arbitrary degrees in quintic hypersurfaces in P4. These predictions have
since been extended to many other CY families. We refer to [Mo ] for more
details of the conjecture and the evidence for it.
In the remainder of this section we wish to speculate on the ro le which
the ACIHS on relative Deligne cohomology ~D might play in the mirror story.
A couple of relationships are evident:
(i) Both of the relevant dimensions, h1, 1 and h2, 1, occur in ~D, as the rank
of the discrete part and (one less than) the dimension of the c ontinuous
21
part (of either base or ﬁbers), respectively. This suggests that the rela-
tion between the two ACIHS attached to mirror-symmetric CY f amilies
might be expressible directly as some sort of Fourier transf orm.
(ii) The mirror map, t of (11), as constructed in [CdOGP], [Mo], etc., is
given by
ti = ˜ti/˜t0, i = 1, · · ·,h 2, 1,
where ˜ti are the action coordinates for the ACIHS, for an appropriate
choice of Lagrangian basis γ0, · · ·,γ h2,1 in terms of a maximally unipo-
tent degeneration. (This follows immediately from the cons truction in
[Mo] and our Lemma 3.)
(iii) We also recall from [Mo] that mirror symmetry is expect ed to hold
for “most” Calabi-Yaus, but probably not all; a notorious co llection
of probable exceptions is provided by Calabi-Yaus which are rigid, i.e.
h2, 1 = 0. Now a somewhat analogous situation occurs for the Torell i
and Schottky problems, of recovering a variety or family of v arieties
from its Hodge structure: this is known to be true, at least ge nerically,
for many classes of varieties, but various counterexamples exist. It is
conceivable that all failures of mirror symmetry could be ex plained by
failures of Schottky or Torelli results, i.e. that there is s till some mirror
data, but it does not come from a geometric object, namely a CY family.
The above observations, and some others which will be discus sed below,
suggest that we might try to split the mirror conjecture roug hly into three
parts:
(1) Axiomatize the integrable system associated to a CY fami ly, by listing a
collection of cohomological and symplectic data which can b e attached
to each family, and which satisﬁes certain axioms.
(2) Describe a formal mirror transform on abstract systems, which inter-
changes the continuous and discrete parts.
(3) Study the validity of Torelli- and Schottky-type result s, which say that
a CY-family can be uniquely recovered from its system, and de scribe
which abstract systems actually arise from geometry.
A weaker version of this last step, likely to hold in greater g enerality,
would be:
(3’) Extract from an abstract system enough data to reconstr uct either
theA- or B-model partition functions. (Ideally, we should be able to e xtract
both partition functions from the system, and the formal tra nsform of step
(2) should interchange them.)
An abstract system should consist at least of the following d ata:
22
(i) An analytically completely integrable Hamiltonian sys tem ~D → ~M,
which is an extension of another ACIHS ~J → ~M by a lattice H 1, 1(Z).
(ii) An indeﬁnite (“Lorentzian”) polarization on the torus ﬁbers of ~J → ~M
and a (symmetric, cubic, Z-valued) intersection product on H 1, 1(Z).
(iii) A C∗-action on ~D lifting an action of C∗ on ~M.
(iv) A 1-form τ on ~D, homogeneous of weight 1 with respect to the C∗-
action, satisfying dτ =σ (= the symplectic form on ~D).
Some further pieces of data may also need to be speciﬁed, such as the
choice of a maximally unipotent degeneration. The above dat a lets us recover
the variation of weight-3 Hodge structures over ~M, and the family of all
normal functions: these are the integral manifolds for τ . A key question
which we cannot answer is whether the collection of normal fu nctions coming
from 1-cycles is determined by the above data, or needs to be s peciﬁed
explicitly.
These data certainly seem rich enough that one expects to rec over from
them much of the underlying CY geometry. The hope, which of co urse we
are nowhere near realizing, is that when these data satisfy s ome appropriate
axioms they can be used to generate a mirror system of the same type. If
this is so, one must be able to extract both the A- and B-model data (i.e.
the two partition functions) from a given system. Let us disc uss the various
ingredients.
For the B-model, we need two essential pieces: the Yukawa cubic c and
the aﬃne structure on ~M. Now the Yukawa cubic is determined by the
symplectic form on ~J and the polarization on the ﬁbers, by Theorem 1. The
aﬃne structure used to convert c to a cubic on the ﬁxed vector space V is
determined by the coordinates ˜ti, which by Lemma 3 are the action variables,
so they too are determined by ~J . This of course depends on the discrete
choice of a Lagrangian basis for H3(X, Z); we do not see how to avoid this
choice, so it must either be built into the axioms, or be deduc ible somehow
from knowing the collection of all normal functions (and in p articular, their
monodromy).
For theA-model it seems plausible that the relevant data can be obtai ned,
but this leads us to Hodge-theoretic questions which we cann ot (yet?) re-
solve. We need the topological intersection form Topo, whic h is built into
the axioms. The essential problem is to recover the coeﬃcien ts nk. Each
rational curve on the generic CY in the family gives a (ﬁnitel y multivalued)
normal function in ~D, and each homologous pair gives one in ~J . The prob-
lem is that not all normal functions arise in this way. We are l ed to a series
of problems.
23
(i) Which normal functions in ~D arise from eﬀective curves?
(ii) Which of these arise from irreducible curves?
(iii) Which of these arise from rational curves?
We note that a given normal function ν might arise from many diﬀerent
curves. The simplest example is that of complete intersecti on curves: a given
family of such curves is parametrized by a (usually positive dimensional)
projective space on each CY in the family, and all such curves have the same
Abel-Jacobi image since they are rationally equivalent. In fact, the Corollary
to Theorem 5 says that all curves in any connected family on th e generic
CY give rise to the same ν.
The above remark suggests that we need not only decide which n ormal
functions ν come from rational curves, but to determine a multiplicity o r
weight ofν accounting for all its realizations in terms of rational cur ves. Now
this seems rather special; one can just as well hope for a weig ht function wν
counting all curves, of all genera, corresponding to ν, through an expansion
such as wν = ∑ Nν,g λg−1, where λ is a dummy variable and the coeﬃcients
Nν,g account for the curves.
A master partition function F , accounting for curves of all genera on a
CY, has recently been proposed in [BCOV]. It can be written:
F = ∑ Fgλg−1
= ∑ Nk,gqkλg−1
= ∑ wkqk,
where the qk are as in (10), the Fg are the genus-g partition functions (they
depend on the qk), and the coeﬃcients Nk,g are certain combinations of
the “numbers” nk,g of curves of genus g and fundamental class k. [A rigid
non-singular curve of class k and genus g contributes a term of 1 ·λg−1,
but also makes contributions to higher-genus terms, becaus e of multiple
(branched) coverings. The situation is more complicated fo r continuous fam-
ilies of curves, where the basic contribution involves the E uler characteristic
of the base, but there are other terms corresponding, e.g., t o singular curves
in the family.] This F is a function of the variables q andλ. Via the mirror
correspondence (11), it is carried to a function on ~M, whose leading term
is the Yukawa coupling. The genus-0 partition function F0 is recovered as a
residue of F in the λ direction.
In order to recover the partition function F0, or F for that matter, we
need a reﬁnement of the BCOV coeﬃcients: to each Lagrangian n ormal
function ν we want to associate a weight function
wν =
∑
Nν,g λg−1
24
such that for each nef class k we have
wk =
∑
{ν |ϕ (ν )=k}
wν,
or
Nk,g =
∑
{ν |ϕ (ν )=k}
Nν,g ,
or equivalently:
F =
∑
Nν,g qϕ (ν )λg−1.
The point is that we want a formula for the wν in terms of ν alone, without
knowledge of the actual curves on X whose Abel-Jacobi image is ν.
We do not know whether such a formula exists. But if it does, it is
likely to involve only the inﬁnitesimal invariant δν, associated to a normal
function by Griﬃths [G2] and improved by Green [Gr1]. This in variant lives
in a certain Koszul cohomology group. It vanishes if and only if ν is locally
constant, i.e. can be lifted locally to a constant section ν of the Gauss-Manin
local system R3 ~χ∗C of the family ~χ : ~X → ~M.
The reason is that the sum, over all ν inϕ−1(k), is too big. For example,
when k = 0, any torsion element in J(X) (or in H 3(X, Q/Z)) extends to a
ﬁnitely valued Lagrangian multisection of ~J , but there is no reason to expect
any contribution of these torsion sections to the curve coun t. By continuity,
one expects no contribution from any locally constant norma l function, so
wν should depend only on δν.
In our case, of normal functions on CY threefolds, we can desc ribe the
Koszul cohomology group in which δν lives explicitly in terms of the Yukawa
cubic. In general, δν is obtained by choosing a lift ν, diﬀerentiating it with
respect to the Gauss-Manin connection ∇, and taking the part independent
of choices. In our case, ∇ν lives in
Hom(TX,s ~M,H 3/F 2H 3)
which is canonically identiﬁed with ⊗2(F 2)∗. The diﬀerential equation (7)
satisﬁed by any normal function asserts that ν lands in
Hom(TX,s ~M,F 1H 3/F 2H 3)
which is (F 2)∗ ⊗ (H 2, 1)∗. By Remark (2) to Theorem 4, any normal function
is Lagrangian. This means that ∇ν is symmetric, so we are down to
Sym 2(H 2, 1)∗,
or the space of quadrics on V =H 2, 1. The ambiguity arising from a change
of the lift ν amounts to those quadrics which are partial derivatives, in some
25
direction, of the Yukawa cubic c ∈ Sym 3(H 2, 1)∗. Summarizing, the Koszul
complex in our case can be identiﬁed with the complex
(H 2, 1) Y ukawa→ ⊗ 2(H 2, 1)∗ →
2
∧ (H 2, 1)∗.
We conclude that δν is in R2, where Rd is the dth graded piece of the Ja-
cobian ring of c : R• := S•/J •, where S• = Sym •(V ∗) and J • ⊂ S• is
the Jacobian ideal, generated by the partials of c. The problem of recon-
structing the curves on X with given normal function ν from the invariant
δν may therefore have some resemblance to the variational Tore lli problem,
where certain parts of R are given and one needs to recover the underlying
variety, as in [D]. It is known how to extract quite a bit of inf ormation from
the invariants δν in some situations, e.g. [G2], [Gr1], [CP]. The question is
whether, on a generic Calabi-Yau threefold X, one can recover the collection
of all curves from their δν invariants.
