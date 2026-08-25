---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-003-4-grassmannians-over-local-fields
section_title: "Grassmannians over local fields"
section_number: 4
pages: 10-11
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
In this section we specialize the general theory of the previous sec tion to the classical
examples arising from Grassmannians over local ﬁelds.
4.1. The Grassmann representation over local ﬁelds. Consider the commutative
CQG algebra A = C(K) of representative functions on a compact topological group K.
The Hopf ∗-algebra structures are given by
∆(f )(g,g′) = f (gg′), ǫ (f ) = f (e), S (f )(g) = f (g−1), f ∗(g) =
f (g),
where g,g′ ∈ K , f ∈ C(K), e ∈ K is the unit element of K, and where we have used the
natural identiﬁcation C(K) ⊗ C(K) ≃ C(K × K) by the multiplication map. The positive
deﬁnite normalized Haar functional h is
h(f ) =
∫
K
f (g)dg, f ∈ C(K),
where dg is the normalized Haar measure on K. Observe that C(K)h = L2(K,dg ) and
Σ ≃ ˆK, the unitary dual of the compact group K, since there is a natural one-to-one
correspondence between ﬁnite-dimensional right C(K)-comodules and ﬁnite dimensional K-
representations preserving notions as irreducibility, equivalence a nd unitarity. Concretely,
for a given right C(K)-comodule π :V →V ⊗ C(K) we deﬁne a left K-action on V by
gv =
(
IdV ⊗ evg
)
π(v), g ∈ K, v ∈V,
where ev g : C(K) → C is the evaluation map ev g(f ) = f (g). Under this correspondence,
the dual representation of a ﬁnite dimensional K-representation (π,V ) becomes
(π∗(g)f )(v) = f (π(g−1)v) ( f ∈V∗,v ∈V,g ∈ K).
Clearly the isomorphism π∗∗ ≃π for a ﬁnite dimensional K-representation (π,V ) is realized
byF = Id, hence the quantum dimension Dim C(K)(V ) is the complex dimension Dim C(V )
of the representation space V . We now deﬁne one of our main object of study.
Deﬁnition 4.1. Let n,d ∈ N with n ≤ d/2. The Grassmannian G(n,d ; F) over the local
ﬁeld F is the set of n-dimensional F-subspaces in Fd.
Consider the maximal compact subgroup KF of GL d(F), see (1.1). Note that KF acts
transitively on G(n,d ; F), e.g. by the Iwasawa decomposition in GL d(F). The subgroup of
KF stabilizing {0}d−n × Fn ∈ G (n,d ; F) is denoted by MF, so that
G(n,d ; F) ≃ K F/MF
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 11
as transitive KF-space. The pair ( KF, MF) is a Gelfand pair in the usual sense of topo-
logical groups. This is well known for the Archimedean ﬁelds R and C, see [12] and [5]
and the references therein. For non-Archimedean ﬁelds we refer to [2]. Consequently,
(A,B ) =
(
C(KF), C(MF)
)
is a quantum Gelfand pair in the sense of CQG algebras, where
the surjective Hopf ∗-homomorphism p : C(KF) → C(MF) is the canonical restriction
map p(f ) = f |MF. The parametrizing set Σ C(MF) of the ﬁnite dimensional, irreducible
C(MF)-spherical right C(KF)-comodules is in bijection with ( KF/MF)ˆ, the unitary spher-
ical dual of KF with respect to the subgroup MF. The corresponding right C(KF)-comodule
C(KF)C(MF), viewed as KF-representation, now identiﬁes with the Grassmann representa-
tion
C
(
G(n,d ; F)
)
:= {f ∈ C(KF) | f (gh) = f (g), ∀g ∈ K F, ∀h ∈ M F},
considered as left KF-module by the regular action
(
gf
)
(g′) = f (g−1g′), f ∈ C
(
G(n,d ; F)
)
, g,g′ ∈ K F.
In this setting we take ( πF
α,V F
α ) (α ∈ (KF/MF)ˆ) to be a complete set of representatives
of the irreducible MF-spherical KF-representations. Then
(4.1) C
(
G(n,d ; F)
)
≃
⨁
α∈(KF/MF)ˆ
V F
α
is the multiplicity-free decomposition of C
(
G(n,d ; F)
)
in irreducible KF-representations,
cf. (3.2). For α ∈ (KF/MF)ˆ we choose a scalar product ⟨·, ·⟩α on V F
α turning πF
α into a
unitary KF-representation, and we choose a nonzero MF-ﬁxed vector vF
α ∈V F
α . Using again
the identiﬁcation of ﬁnite dimensional right C(KF)-comodules with ﬁnite dimensional KF-
representations, the quantum zonal spherical functions assoc iated to the quantum Gelfand
pair ( C(KF), C(MF)) are the usual zonal spherical functions
ϕF
α(g) = ⟨πF
α(g)vF
α,v F
α⟩α, g ∈ K F, α ∈ (KF/MF)ˆ
associated to the Gelfand pair ( KF, MF). The dimension formula (see Proposition 3.6) now
becomes
(4.2) Dim C
(
V F
α
)
=
(
ϕF
α(e)
) 2
∫
KF
|ϕF
α(g)|2dg, α ∈ (KF/MF)ˆ,
where e is the unit element of KF.
