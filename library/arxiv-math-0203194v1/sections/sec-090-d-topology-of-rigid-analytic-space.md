---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-090-d-topology-of-rigid-analytic-space
section_title: "Topology of Rigid Analytic Space."
section_number: D
pages: 220-222
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
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
