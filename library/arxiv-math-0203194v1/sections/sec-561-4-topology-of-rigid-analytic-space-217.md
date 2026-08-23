---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-561-4-topology-of-rigid-analytic-space-217
section_title: "TOPOLOGY OF RIGID ANALYTIC SPACE. 217"
section_number: 4
pages: 221-222
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp — 580 sections: INTRODUCTION; INTRODUCTION; INTRODUCTION"
---
Lemma 4.3. Let X be a connect rigid analytic space X.
(1) The space X is simply connected if and only if every locally constant
sheaf of sets, with respect to the Grothendieck topology, is constant.
(2) If there exists an admissible covering {Xi}i∈N of X such that ( a)
everyXi is simply connected, and ( b) Xi⊆Xi+1 for all i, then X is simply
connected.
Proof. Both are straightforward.
Example 4.4 (Topology of the closed disk) . Let D = D(0, 1+) be the 1-
dimensional closed disk of radius 1. A rational subdomain in D of form
{x∈ D|| x−a|≤ ρ and|x−ai|≥ ρi for i = 1,... ,s},
where ρ,ρ i∈| K∗| and a,a i∈ D, is called a standard domain . This is the
complement of ﬁnite union of open disks. The following prope rties are easy
to verify:
• IfS1 andS2 are standard domains such that S1∩S2⁄=∅, then so are
S1∪S2 and S1∩S2.
• Every ﬁnite union of standard domains is uniquely decompose d as a
disjoint union of standard domains.
What is more interesting is the following proposition:
Proposition 4.5. Every rational subdomain in D is a ﬁnite union of standard
domains. (Hence standard domains generate the Grothendiec k topology of
D.)
Sketch of Proof. (cf. [GvdP80, III.1.18]). Let R be the rational subdo-
main given by |fi(x)|≤| f0(x)| for i = 1,... ,n . Deforming those functions
slightly, if necessary, we may assume fi andfj have no common zero for any
i⁄=j, and thus, we may concentrate to the single inequality|f1(x)|≤| f0(x)|.
By Weierstrass Preparation Theorem we may assume f0 andf1 are polyno-
mials having all their roots in D. Then the proposition follows from an easy
calculation.
Corollary 4.6. The Grothendieck topology of the projective line P1,an
K is gen-
erated by standard domains.
Proposition 4.7. Standard domains are connected. Moreover, every con-
nected rational subdomain in P1,an
K is simply connected.
Proof. The ﬁrst assertion is obvious since the corresponding aﬃnoi d alge-
bra
K{t,t 0,... ,t s}/((t−a)−t0π,π i−ti(t−ai) for i = 1,... ,s ),
where a,a i∈ K and π,π i∈ K, is integral. (Note that K{t,t 0,... ,t s} is
Noetherian and factorial.) The second one is proved by using 4.3 (1). Let
S be a standard domain and F a constant sheaf of sets on S. We can take
an admissible covering {Si} of S which trivializes F. The point is that any
218 A. RAPID COURSE IN p-ADIC ANALYSIS.
non-disjoint union of standard domains is standard, and hen ce, connected.
So the restriction maps F(Si) → F(Si∩Sj) must be bijective as far as
Si∩Sj⁄=∅. It follows that F(Si∪Sj)→ F(Si) are bijective, and repeating
this argument, we concludes F is constant.
The following corollary may seen at ﬁrst:
Corollary 4.8. Every connected open subanalytic space (4) in P1,an
K is simply
connected.
Proof. A connected open subanalytic space U has an admissible covering
consisting of standard domains. By [ GvdP80, III,2.6] and the easy fact that
a non-disjoint union of connected sets is again connected, w e see that a ﬁnite
non-disjoint union of standard domain is a connected ration al subdomain.
Hence the corollary follows from Lemma 4.3 (2) and Propositi on 4.7.
Finally we quote, without proof, a theorem by van der Put whic h in-
dicates a close relation between the topology of a rigid anal ytic space and
that of its analytic reduction:
Theorem 4.9. LetX be a quasi-compact rigid analytic space over K which
has the irreducible and smooth analytic reduction. Then X is simply con-
nected.
For the proof, see [ vdP87].
Remark 4.10. By the corollary, we know, for example, that the space Gan
K =
K× is simply connected. But, on the other hand, it is easy to see t hat the
map K×→K× byx↦→xn is an analytic morphism. As far as the charac-
teristic of K does not divide n, we are tempted to think of this morphisms
also as an analytic covering. But it is not. Certainly, this m orphism induces
isomorphisms between stalks of the structure sheaf, but the re is no admis-
sible covering which trivializes this morphism! This kind of morp hisms is
said to be ´ etale; analytic coverings are ´ etale, but not vice versa. Simply
connected analytic spaces may have many ´ etale coverings.
