---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-007-4-version-ii-classifying-maps
section_title: "Version II: Classifying Maps"
section_number: 4
pages: 18-21
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
It is well known that for a Lie group G the smooth ˇCech-cohomology ˇH1(M,G ) and the continuous
ˇCech-cohomology ˇH1
c(M,G ) agree if M is a smooth manifold (in particular paracompact). This
can e.g. be shown by locally approximating continuous cocycles by smo oth ones without changing
the cohomology class – see [MW09] (even for G inﬁnite-dimensional). Below we generalize this
fact to non-abelian cohomology for certain Lie 2-groups Γ. Here th e continuous ˇCech-cohomology
ˇH1
c (M, Γ) is deﬁned in the same way as the smooth one (Deﬁnition 3.4) but with all maps continuous
instead of smooth. A Lie groupoid Γ is called smoothly separable , if the set π0Γ of isomorphism
classes of objects is a smooth manifold for which the projection Γ 0 /d47/d47 π0Γ is a submersion.
Proposition 4.1. Let M be a smooth manifold and let Γ be a smoothly separable Lie 2-group.
Then, the inclusion
ˇH1(M, Γ) /d47/d47 ˇH1
c (M, Γ)
of smooth into continuous ˇCech cohomology is a bijection.
– 18 –
Remark 4.2. It is possible that the assumption of being smoothly separable is not n ecessary, but
a proof not assuming this would certainly be more involved than ours. Anyway, all Lie 2-groups
we are interested in are smoothly separable.
Proof of Proposition 4.1. We denote by π1Γ the Lie subgroup of Γ 1 consisting of automorphisms
of 1 ∈ Γ 0. Since it has two commuting group structures – composition and mult iplication – it is
abelian. The idea of the proof is to reduce the statement via long exa ct sequences to statements
proved in [MW09]. The exact sequence we need can be found in [Bre90 ]:
ˇH0(M, (π0Γ)dis) /d47/d47 ˇH1(M, Bπ1Γ) /d47/d47 ˇH1(M, Γ) /d47/d47 ˇH1(M, (π0Γ)dis) /d47/d47 ˇH2(M, Bπ1Γ).
Note that ˇH1(M, Γ) and ˇH1(M, (π0Γ)dis) do not have group structures: hence, exactness is only
meant as exactness of pointed sets. But we actually have more str ucture, namely an action of
ˇH1(M,Bπ 1Γ) on ˇH1(M, Γ). This action factors to an action of
C := coker
(
ˇH0(M, (π0Γ)dis) /d47/d47 ˇH1(M, Bπ1Γ)
)
.
In fact on the non-empty ﬁbres of the morphism ˇH1(M, Γ) /d47/d47 ˇH1(M, (π0Γ)dis) this action is simply
transitive. In other words: ˇH1(M, Γ) is a C-Torsor over
K := ker
(
ˇH1(M, (π0Γ)dis) /d47/d47 ˇH2(M, Bπ1Γ)
)
.
The same type of sequence also exists in continuous cohomology, na mely
ˇH0
c(M, (π0Γ)dis) /d47/d47 ˇH1
c (M, Bπ1Γ) /d47/d47 ˇH1
c(M, Γ) /d47/d47 ˇH1
c (M, (π0Γ)dis) /d47/d47 ˇH2
c(M, Bπ1Γ).
With
C′ := coker
(
ˇH0
c (M, (π0Γ)dis) /d47/d47 ˇH1
c(M, Bπ1Γ)
)
K ′ := ker
(
ˇH1
c(M, (π0Γ)dis) /d47/d47 ˇH2
c(M, Bπ1Γ)
)
,
we exhibit ˇH1
c (M, Γ) as a C′-Torsor over K ′.
The natural inclusions of smooth into continuous cohomology form a chain map between the
two sequences. From [MW09] we know that they are isomorphisms on the second, fourth and ﬁfth
factor. In particular we have an induced isomorphism K ∼ /d47/d47 K ′. Lemma 4.3 below additionally
shows that the induced morphism C /d47/d47 C′ is an isomorphism. Using these isomorphisms we see
that ˇH1(M, Γ) and ˇH1
c(M, Γ) are both C-torsors over K and that the natural map
ˇH1(M, Γ) /d47/d47 ˇH1
c (M, Γ)
is a morphism of torsors. But each morphism of group torsors is bije ctive, which concludes the
proof. □
– 19 –
Lemma 4.3. The images of
f : ˇH0(M, (π0Γ)dis) /d47/d47 ˇH1(M, Bπ1Γ) and f ′ : ˇH0
c (M, (π0Γ)dis) /d47/d47 ˇH1
c (M, Bπ1Γ)
are isomorphic.
Proof. ˇH0(M, (π0Γ)dis) is the group of smooth maps s : M /d47/d47 π0Γ and ˇH0
c(M, (π0Γ)dis) is
the group of continuous maps t : M /d47/d47 π0Γ. The groups ˇH1(M, Bπ1Γ) = ˇH2(M,π 1Γ) and
ˇH1
c (M, Bπ1Γ) = ˇH2
c (M,π 1Γ) are isomorphic by the result of [MW09]. Under the connecting homo -
morphism
ˇH0(π0Γ, (π0Γ)dis) /d47/d47 ˇH1(π0Γ, Bπ1Γ)
the identity idπ 0Γ is sent to a class ξΓ with the property that f (s) = s∗ξΓ andf ′(t) = t∗ξΓ . Hence it
suﬃces to show that for each continuous map t :M /d47/d47 π0Γ there is a smooth map s :M /d47/d47 π0Γ
withs∗ξΓ =t∗ξΓ . It is well known that for each continuous map t between smooth manifolds a homo-
topic smooth map s exists. It remains to show that the pullback ˇH1(π0Γ, Bπ1Γ) /d47/d47 ˇH1(M, Bπ1Γ)
along smooth maps is homotopy invariant. This can e.g. be seen by cho osing smooth (abelian)
Bπ1Γ-bundle gerbes as representatives, in which case the homotopy in variance can be deduced from
the existence of connections. □
It is a standard result in topology that the continuous G-valued ˇCech cohomology of paracompact
spaces is in bijection with homotopy classes of maps to the classifying space BG of the group G.
A model for the classifying space BG is for example the geometric realization of the nerve of the
groupoid BG, or Milnor’s join construction [Mil56].
Now let Γ be a Lie 2-group, and let |Γ | denote the geometric realization of the nerve of Γ. Since
the nerve is a simplicial topological group, |Γ | is a topological group. Version II for smooth Γ-gerbes
is:
Deﬁnition 4.4 ([BS09]). A classifying map for a smooth Γ -gerbe is a continuous map
f :M /d47/d47 B|Γ |.
We denote by
[
M, B|Γ |
]
the set of homotopy classes of classifying maps.
Proposition 4.5 ([BS09, Theorem 1]) . Let Γ be a Lie 2-group. Then there is a bijection
ˇH1
c (M, Γ) ∼=
[
M, B|Γ |
]
where the topological group |Γ | is the geometric realization of the nerve of Γ .
Note that the assumption of [BS09, Theorem 1] that Γ is well-pointed is automatically satisﬁed
because Lie groups are well-pointed. Propositions 4.1 and 4.5 imply the following equivalence
theorem between Version I and Version II.
– 20 –
Theorem 4.6. For M a smooth manifold and Γ a smoothly separable Lie 2-group, there is a
bijection
ˇH1(M, Γ) ∼=
[
M, B|Γ |
]
.
Remark 4.7. Baez and Stevenson argue in [BS09, Section 5.2.] that the space B|Γ | is homotopy
equivalent to a certain geometric realization of the Lie 2-groupoid |BΓ | from Section 3. Baas, B¨ ostedt
and Kro have shown [BBK12] that |BΓ | classiﬁes concordance classes of charted Γ-2-bundles. In
particular, charted Γ-2-bundles are a further equivalent version of smooth Γ-gerbes.
