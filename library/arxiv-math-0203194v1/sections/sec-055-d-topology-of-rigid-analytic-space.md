---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry"
section_id: sec-055-d-topology-of-rigid-analytic-space
section_title: "Topology of Rigid Analytic Space."
section_number: D
pages: 220-225
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
---
In this section, we assume, for simplicity, that K is algebraically closed.
Deﬁnition 4.1.
(1) A rigid analytic space X is said to be quasi-compact
if every admissible covering of X has a ﬁnite admissible reﬁnement.
(2) A rigid analytic space X is said to be connected if there is no admis-
sible covering {Ui}i∈I of X such that
[
i∈I1
Ui ∩
[
i∈I2
Ui = ∅and
[
i∈I1
Ui̸ = ∅̸ =
[
i∈I2
Ui
for some non-empty subsets I1, I2 ⊆I with I = I1 ⊔I2.
Since admissible coverings of aﬃnoids are ﬁxed as ﬁnite, every aﬃnoid
is quasi-compact. So, we see that a rigid analytic space is quasi-compact
if and only if it is a ﬁnite union of aﬃnoids. It is easy to see that a rigid
analytic space X is connected if and only if the ring Γ(X, OX) has no other
idempotent than 0 and 1.
Deﬁnition 4.2. A morphism π: Y →X of rigid analytic spaces over K
is said to be an analytic covering if there exists an admissible covering(3)
{Xi}i∈I of X such that for each i ∈I π−1(Xi) is isomorphic to the disjoint
union of copies of Xi. A connect rigid analytic space X is said to be simply
connected if there is no other connected analytic covering over X than the
trivial one id: X →X (cf. [vdP87]).
(3)or else a topological covering, referring to the Grothendieck topology; cf. Chapter I,
§§1.4
4. TOPOLOGY OF RIGID ANALYTIC SPACE.
217
Lemma 4.3. Let X be a connect rigid analytic space X.
(1) The space X is simply connected if and only if every locally constant
sheaf of sets, with respect to the Grothendieck topology, is constant.
(2) If there exists an admissible covering {Xi}i∈N of X such that (a)
every Xi is simply connected, and (b) Xi ⊆Xi+1 for all i, then X is simply
connected.
Proof. Both are straightforward.
Example 4.4 (Topology of the closed disk). Let D = D(0, 1+) be the 1-
dimensional closed disk of radius 1. A rational subdomain in D of form
{x ∈D | |x −a| ≤ρ and |x −ai| ≥ρi for i = 1, . . . , s},
where ρ, ρi ∈|K∗| and a, ai ∈D, is called a standard domain. This is the
complement of ﬁnite union of open disks. The following properties are easy
to verify:
• If S1 and S2 are standard domains such that S1 ∩S2̸ = ∅, then so are
S1 ∪S2 and S1 ∩S2.
• Every ﬁnite union of standard domains is uniquely decomposed as a
disjoint union of standard domains.
What is more interesting is the following proposition:
Proposition 4.5. Every rational subdomain in D is a ﬁnite union of standard
domains. (Hence standard domains generate the Grothendieck topology of
D.)
Sketch of Proof. (cf. [GvdP80, III.1.18]). Let R be the rational subdo-
main given by |fi(x)| ≤|f0(x)| for i = 1, . . . , n. Deforming those functions
slightly, if necessary, we may assume fi and fj have no common zero for any
i̸ = j, and thus, we may concentrate to the single inequality |f1(x)| ≤|f0(x)|.
By Weierstrass Preparation Theorem we may assume f0 and f1 are polyno-
mials having all their roots in D. Then the proposition follows from an easy
calculation.
Corollary 4.6. The Grothendieck topology of the projective line P1,an
K
is gen-
erated by standard domains.
Proposition 4.7. Standard domains are connected.
Moreover, every con-
nected rational subdomain in P1,an
K
is simply connected.
Proof. The ﬁrst assertion is obvious since the corresponding aﬃnoid alge-
bra
K{t, t0, . . . , ts}/((t −a) −t0π, πi −ti(t −ai) for i = 1, . . . , s),
where a, ai ∈K and π, πi ∈K, is integral. (Note that K{t, t0, . . . , ts} is
Noetherian and factorial.) The second one is proved by using 4.3 (1). Let
S be a standard domain and F a constant sheaf of sets on S. We can take
an admissible covering {Si} of S which trivializes F. The point is that any
218
A. RAPID COURSE IN p-ADIC ANALYSIS.
non-disjoint union of standard domains is standard, and hence, connected.
So the restriction maps F(Si) →F(Si ∩Sj) must be bijective as far as
Si ∩Sj̸ = ∅. It follows that F(Si ∪Sj) →F(Si) are bijective, and repeating
this argument, we concludes F is constant.
The following corollary may seen at ﬁrst:
Corollary 4.8. Every connected open subanalytic space(4) in P1,an
K
is simply
connected.
Proof. A connected open subanalytic space U has an admissible covering
consisting of standard domains. By [GvdP80, III,2.6] and the easy fact that
a non-disjoint union of connected sets is again connected, we see that a ﬁnite
non-disjoint union of standard domain is a connected rational subdomain.
Hence the corollary follows from Lemma 4.3 (2) and Proposition 4.7.
Finally we quote, without proof, a theorem by van der Put which in-
dicates a close relation between the topology of a rigid analytic space and
that of its analytic reduction:
Theorem 4.9. Let X be a quasi-compact rigid analytic space over K which
has the irreducible and smooth analytic reduction. Then X is simply con-
nected.
For the proof, see [vdP87].
Remark 4.10. By the corollary, we know, for example, that the space Gan
K =
K× is simply connected. But, on the other hand, it is easy to see that the
map K× →K× by x 7→xn is an analytic morphism. As far as the charac-
teristic of K does not divide n, we are tempted to think of this morphisms
also as an analytic covering. But it is not. Certainly, this morphism induces
isomorphisms between stalks of the structure sheaf, but there is no admis-
sible covering which trivializes this morphism! This kind of morphisms is
said to be ´etale; analytic coverings are ´etale, but not vice versa. Simply
connected analytic spaces may have many ´etale coverings.
5. Berkovich’ approach to non-archimedean analysis
Berkovich’ viewpoint provides an innovative approach to topological
problems of p-adic geometry and analysis, which is much closer to the famil-
iar intuition derived from the complex context [Ber90](5). His analysis, in
fact, generalizes, or properly speaking, “completes” the rigid analysis. This
situation is, according to what he says in the introduction of his book, some-
how analogous to that of R completing Q. The standard archimedean metric
space Q is totally disconnected. The rigid analytic viewpoint corresponds,
to some extent, to regarding every rational interval {r ∈Q | a ≤r ≤b} as
(4)We refer [BGR84, 9.3.1] for the deﬁnition of open subanalytic spaces.
(5)Already in [vdP82] the esquisse of Berkovich’ idea can be seen.
5. BERKOVICH’ APPROACH TO NON-ARCHIMEDEAN ANALYSIS
219
“connected”, and considering only those functions which come from analytic
functions on the corresponding real interval. Berkovich’ non-archimedean
analysis can be compared, in this context, to analysis on R itself. Namely,
his presentation of analytic spaces complements those of rigid analysis by
putting some “generic points”, and consequently, simpliﬁes their topology.
Let us be a little more precise about his theory. Let A be a Banach ring,
i.e., a ring together with a norm ∥· ∥with respect to which A is complete.
Deﬁnition 5.1. (1) A semi-norm | · | on A is said to be bounded if there
exists C > 0 such that |f| ≤C∥f∥for any f ∈A.
(2) A semi-norm | · | on A is said to be multiplicative if |fg| = |f||g| for
all f, g ∈A.
Replacing the maximal spectra Spm(A) of rigid geometry, we have:
Deﬁnition 5.2. The Berkovich’ spectrum M(A) for a Banach ring A is the
set of all bounded multiplicative semi-norms on A, endowed with the weakest
topology so that the real valued functions of form | · | 7→|f| for f ∈A are
continuous.
In case A is an aﬃnoid algebra (a strict aﬃnoid algebra, in Berkovich’
term) over K, the aﬃnoid space Spm(A) is naturally viewed as a subspace,
with the relative topology, of the Berkovich’ spectrum M(A). This is done
by identifying an element m in Spm(A) with the unique semi-norm | · | on
A such that m = Ker | · |. The space Spm(A) is identiﬁed, in terms of this
correspondence, with the subspace of M(A) consisting of semi-norms | · |
such that dimK A/ Ker | · | is ﬁnite (the “classical points”).
Example 5.3. Let us consider the usual absolute-value norm | · |∞on Z.
The spectrum M(Z) consists of the following points:
(i) | · |∞,ǫ: = | · |ǫ
∞(0 < ǫ ≤1).
(ii) The p-adic norm | · |p,ǫ: with |p|p,ǫ = ǫ (0 < ǫ ≤1).
(iii) The semi-norm | · |p induced from the trivial norm on Z/pZ.
(iv) The trivial norm | · |0.
As a topological space, M(Z) is a tree with end points | · |p and | · |∞. Each
of these points is connected by a single edge with | · |0.
On the Berkovich’ spectrum, the aﬃnoid subdomains (incl. rational sub-
domains) are deﬁned in the similar way to rigid analysis.
Thus one can
deﬁne the structure sheaves on spectra, which one calls aﬃnoid spaces. The
local data consisting of Berkovich’ aﬃnoids and the structure sheaves can
glue to locally ringed spaces; thus we obtain analytic spaces in Berkovich’
sense.
Example 5.4. (Cf. [Ber90, 1.5].) Let K be a non archimedean complete
ﬁeld. An aﬃne space over K is deﬁned by
An
K = {multiplicative seminorm | · | on K[t1, . . . , tn] | | · ||K is bounded}
220
A. RAPID COURSE IN p-ADIC ANALYSIS.
together with the weakest topology so that | · | 7→|f| (f ∈K[t1, . . . , tn])
is continuous. This has a structure of analytic space so that the analytic
functions over it is characterized by limits of rational functions. When K =
C the space An
K is nothing but the usual aﬃne space in the complex analytic
sense. If K is a non-archimedean ﬁeld, then An
K is a union of balls; i.e., the
spectrum of Tate algebra.
Here are some general properties of Berkovich’ analytic spaces:
(i) Every connected K-analytic space is arcwise connected.
(ii) If X = M(A) with A an aﬃnoid algebra over K, then Krull-dimA =
dim|X|, where |X| is the underlying topological space of X.
(iii) If a K-analytic space X is smooth, then it is locally contractible.
Relation between Berkovich’ analytic spaces and rigid analytic spaces is
as follows. If a Berkovich’ K-analytic space X is formed only by spectra
of (strict) aﬃnoid algebras, we say X is strict. There exists a functor from
the category of separated strict K-analytic spaces to that of separated rigid
analytic spaces over K by
X 7→X0 = {x ∈X | [K(x): K] < ∞},
where K(x) is the residue ﬁeld at x.
Theorem 5.5. This functor is fully-faithful, and preserves ﬁber products.
APPENDIX B
Overview of theory of p-adic uniformization.
By F. Kato
In this appendix we always denote by K, R, and π a complete discrete
valuation ﬁeld, its valuation ring, and a prime element of R, respectively.
We assume that the residue ﬁeld k = R/πR is ﬁnite and consists of q ele-
ments. The Mumford-Kurihara-Mustaﬁn uniformization is a procedure to
construct nice analytic (and in many cases algebraic) varieties by taking
discrete Schottky-type quotients of a certain p-adic analogue of symmetric
space, so-called Drinfeld symmetric space Ω, or its variants.
