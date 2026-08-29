---
doc_id: arxiv-1901.08945v2
doc_title: "DECOMPOSITIONS OF DERIVED CATEGORIES OF GERBES"
section_id: sec-005-6-semi-orthogonal-decompositions-for-brauersever
section_title: "Semi-orthogonal decompositions for Brauer–Severi schemes"
section_number: 6
pages: 24-27
source_pdf: 1901.08945v2.pdf
source_sha256: df222d76e597057f
doc_brief: "DECOMPOSITIONS OF DERIVED CATEGORIES OF GERBES — It is well known that the category of quasi-coherent sheaves on a gerbe banded by a diagonalizable group decomposes accordi ng to the char- acters of"
---
In this section, we demonstrate how to use the theory of gerbes d eveloped by
Giraud to obtain a simple and conceptually appealing proof for the exis tence of the
semi-orthogonal decomposition of the derived category of a Brau er–Severi scheme
given by Bernardara [ Ber09, Theorem 4.1]. We start by recalling some basic facts
on Brauer–Severi schemes and their trivializing gerbes from [ Gir71, Example V.4.8].
Let S be an arbitrary algebraic stack. An algebraic stack P overS is called a
Brauer–Severi scheme overS if it is fppf -locally (onS) isomorphic to a projectivized
vector bundle. Of course P need not be a scheme in general; the terminology is
motivated by the fact that the structure morphism to S is representable by schemes.
DECOMPOSITIONS 25
Given a Brauer–Severi scheme π : P →S, we consider its gerbe of trivializations
and denote it by β :B →S. Let t : T →S be a morphism. The t-points of B are
pairs (V,v ), where V is a ﬁnite locally free sheaf of OT -modules andv : PT
∼
− →P(V ∨)
is an isomorphism over T . The gerbe B is endowed with a tautological ﬁnite locally
free sheaf E of OB-modules. This is obtained on t-points ( V,v ) as above by simply
forgetting the isomorphism v. The gerbe B also has an obvious banding by Gm
given on t-points as above by the usual action by O×
T (T ) on V. In particular, the
tautological sheaf E is a β-twisted sheaf over S in the sense of Deﬁnition 4.4.
Note that by construction, the gerbe of trivializations ﬁts into a 2- cartesian
diagram
(6.1) P(E ∨)
γ /d47/d47
ρ
/d15/d15
P
π
/d15/d15
B β
/d47/d47S,
which we call the tautological trivialization diagram .
The class [ β] of β : B → S (see Theorem 3.11) in H 2(Sfppf, Gm) is called the
Brauer class of the Brauer–Severi scheme π : P → S. This class vanishes if and
only if P is a projectivized vector bundle over S.
Remark 6.1. Consider the Brauer–Severi scheme π : [ Pn−1/ PGLn] → B PGLn. Its
gerbe of trivializations can be identiﬁed with the Gm-gerbe α : B GL n → B PGLn
in Example 3.7.(a). Note that the stack B PGL n classiﬁes Brauer–Severi schemes.
Given a Brauer–Severi scheme P over an arbitrary algebraic stack S, its gerbe
of trivializations can be identiﬁed with the pull-back of α along the morphism
S → B PGLn corresponding to P .
Theorem 6.2. LetS be an algebraic stack and π : P →S a Brauer–Severi scheme
of relative dimension n ≥ 0 over S. Using the notation from above, we consider
the tautological trivialization diagram (6.1). Then the functors
(6.2) Φ i : D qc,i (B) → Dqc(P ), F ↦→γ∗(O(i) ⊗ρ∗F ),
are fully faithful for each i. Moreover, for each a ∈ Z, we have a semi-orthogonal
decomposition
(6.3) D qc(P ) = ⟨Im Φa,..., Im Φa+n⟩
into right admissible categories.
Remark 6.3. In particular (see Corollary 5.8), the essential image Im Φ i is equivalent
to the category D qc,β i(S) ofβi-twisted complexes onS in the sense of Deﬁnition 5.1.
Recall that, as explained above, [ β] ∈ H2(Sfppf, Gm) is the Brauer class of P .
Proof. Since ρ is the projectivization of a vector bundle of rank n + 1, it follows
from [ BS17, Theorem 6.7] that the functors
Ψ i : D qc(B) → Dqc(P(E ∨)), F ↦→ O(i) ⊗ρ∗F,
are fully faithful and that
Dqc(P(E ∨)) = ⟨Im Ψa,..., Im Ψa+n⟩
is a semi-orthogonal decomposition for any a ∈ Z. Since both β and γ are Gm-
gerbes, Theorem 5.4 provides equivalences
∏
d∈Z
Dqc,d (B)
∼
− →Dqc(B),
∏
d∈Z
Dqc,d (P(E ∨))
∼
− →Dqc(P(E ∨)).
26 DANIEL BERGH AND OLAF M. SCHN ¨URER
By Proposition 5.6, the pull-back ρ∗ preserves d-homogeneous objects for each
d ∈ Z. Since E ∨ is homogeneous of degree -1 we see from the canonical surjection
ρ∗(E ∨) → O(1) and Theorem 5.4 that O(1) is homogeneous of degree -1. This shows
that Ψ i shifts the degree by −i. Hence we get a semi-orthogonal decomposition
Dqc, 0(P(E ∨)) = ⟨Im Ψ ′
a,..., Im Ψ ′
a+n⟩,
where Ψ ′
i denotes the restriction of Ψ i to D qc,i (B). Since γ is a gerbe, the pull-back
γ∗ is fully faithful with essential image D qc, 0(P(E ∨)) by Proposition 5.7. Therefore
the theorem follows from the identities Φ i =γ∗ ◦ Ψ ′
i. □
Remark 6.4. Note that Theorem 6.2 diﬀers from the corresponding decomposition
in [ Ber09, Theorem 4.1] with respect to the sign of the Brauer class β. This is
simply due to diﬀerent sign conventions. We follow the convention use d by Giraud
in [ Gir71, Example V.4.8].
Similarly, as in the corresponding theorem for projectivized vector bundles (see
[BS17, Theorem 6.7, Corollary 6.8]), we also get semi-orthogonal decompo sitions
for the categories of perfect complexes, of locally bounded pseud o-coherent com-
plexes, and for the singularity categories, respectively. Following t he notation from
[BS17, Section 2.3], we denote these categories by D pf (P ), D lb
pc(P ) and D sg
pc(P ),
respectively.
Corollary 6.5. Keep the assumptions from Theorem 6.2. The functors Φi induce
functors
Φ pf
i : D pf,i (B) → Dpf (P ), Φ pc
i : D lb
pc,i (B) → Dlb
pc(P ),
Φ sg
i : D sg,i (B) → Dsg(P ),
where the source categories are the full subcategories of i-homogeneous objects in the
categories Dpf (B), Dlb
pc(B) and Dsg(B) introduced above, respectively. Furthermore,
for each a ∈ Z, this yields a semi-orthogonal decomposition
Dpf (P ) = ⟨Im Φ pf
a ,..., Φ pf
a+n⟩,(6.4)
into admissible subcategories and semi-orthogonal decomp ositions
Dlb
pc(P ) = ⟨Im Φ pc
a ,..., Φ pc
a+n⟩,(6.5)
Dsg(P ) = ⟨Im Φ sg
a ,..., Φ sg
a+n⟩(6.6)
into right admissible subcategories. In particular, if S is Noetherian, we get the
corresponding decomposition of Db
coh(P ) = D lb
pc(P ).
Proof. The functors Φ i and their right adjoints restrict to the subcategories of
perfect complexes and the subcategories of locally bounded pseud o-coherent com-
plexes, respectively. Indeed, this follows from the corresponding properties for Ψ i
(cf. [BS17, Corollary 6.8]) using the notation in the proof of Theorem 6.2. Hence the
decompositions in the corollary into right admissible categories follow f ormally from
Theorem 6.2 (see [ BS17, Corollary 5.19]). Moreover, the restriction of each Ψ i to
the category of perfect complexes has a left adjoint (cf. [ BS17, Corollary 6.8]). □
Remark 6.6. Let us explain why Bernardara’s Theorem 4.1 from [ Ber09] is a spe-
cial case of the semi-orthogonal decomposition ( 6.4). In Bernardara’s setting, the
baseS is a Noetherian, separated scheme with the additional property th at any two
points is contained in an open aﬃne. In fact, he only states that S should be locally
noetherian with the extra condition on points, but the other prope rties are used
implicitly since he uses results from C˘ ald˘ araru’s thesis, where the stronger assump-
tions are in eﬀect [ C˘ al00, Section 2.1]. Bernardara’s category D( S,α ) is the derived
category of perfect complexes of α-twisted coherent sheaves. By the comparison by
DECOMPOSITIONS 27
Lieblich mentioned in Remark 4.6, this is equivalent to D pf (Cohα (S)), which is eas-
ily seen to be equivalent to D pf (Qcohα (S)) by using that every quasi-coherent sheaf
on the gerbe corresponding to α is a direct limit of its coherent subsheaves [ LMB00,
Theorem 15.4]. Now this category is equivalent to D pf,α (S) since the functor ( 5.1)
is an equivalence under the assumptions on S (see Remark 5.10).
