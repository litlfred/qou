---
doc_id: arxiv-math-0606222v2
doc_title: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS"
section_id: sec-017-8-the-one-parameter-family-of-quantum-complex-gr
section_title: "The one-parameter family of quantum complex Grassmannians"
section_number: 8
pages: 35-40
source_pdf: 0606222v2.pdf
source_sha256: 5c2a45596d04dd07
doc_brief: "QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIONS — We derive explicit dimension formulas for irreducible MF-spherical KF-re- presentations where KF is the maximal compact subgroup of the"
---
In this section we consider the one-parameter family of quantum co mplex Grassmannians
from [20], [5] and [22] (see also [17] for the general theory of harmo nic analysis on quantum
compact symmetric spaces). This more general set-up does no lon ger ﬁt into the framework
of quantum Gelfand pairs associated to CQG algebras as discussed in Section 3, since the
role of the quantum subgroup is replaced by a suitable inﬁnitesimal co unterpart, depending
on an additional continuous parameter.
In [20] and [5] harmonic analysis on the one-parameter family of quan tum complex Grass-
mannians was studied in detail, leading to the interpretation of Macdo nald-Koornwinder
polynomials and multivariable big and little q-Jacobi polynomials as the associated quan-
tum zonal spherical functions. From these results we now derive r epresentation theoretic
interpretations of the evaluation formulas and norm formulas for M acdonald-Koornwinder
polynomials and multivariable big and little q-Jacobi polynomials. The arguments fol-
low closely [19, Section 6], now applied to the one-parameter family of q uantum complex
Grassmannians. In this more general context we discuss the quan tum dimension formu-
las for irreducible spherical representations in terms of quantum z onal spherical functions.
The analysis leads to the quantum dimension formulas (5.5) and (5.6) f or the irreducible
Uq-representationsV q
λ (λ ∈ Λ n).
We now ﬁrst recall the construction of the quantum zonal spheric al functions on a one-
parameter family of quantum analogues of the complex Grassmannia n K/M. We will
freely use the notations from Section 5. The role of the subgroup M is taken over by a
two-sided co-ideal kσ ⊆ U q depending (in a suitable sense continuously) on an additional
parameter σ ∈ R ∪ {∞}, see e.g. [20], [5] for the explicit deﬁnition of kσ. The case σ = ∞
corresponds to the standard quantum complex Grassmannian fro m Section 5.
The space of kσ-invariants in Cq(K),
Cσ
q (K/M) := {f ∈ Cq(K) | f (YX ) = 0, ∀X ∈ kσ, ∀Y ∈ U q}
36 URI ONN AND JASPER V. STOKMAN
is a Uq-submodule of Cq(K) with respect to the regular Uq-action
(
Xf
)
(X′) = f (S(X)X′), f ∈ Cσ
q (K/M), X,X ′ ∈ U q.
The Uq-module Cσ
q (K/M) serves as a one-parameter family of quantum analogues of the
Grassmann representation C(K/M). Furthermore, C∞
q (K/M) is the Grassmann represen-
tation Cq(K/M) associated to the standard quantum complex Grassmannian from Section
5. The space (
Lq
µ
) kσ
= {v ∈Lq
µ | Xv = 0, ∀X ∈ kσ}
for µ ∈ P +
d serves as the one-parameter quantum analogue of the space of M-ﬁxed vec-
tors in LC
µ. The subspace
(
Lq
µ
) kσ
is one-dimensional or zero dimensional, and it is one-
dimensional if and only if µ ∈ Λ ♮
n. Consequently, the irreducible spherical representations
V q
λ =Lq
λ♮ (λ ∈ Λ n) associated to the standard quantum complex Grassmannian also s erve
as complete set of representatives of ﬁnite dimensional, irreducible Uq-representations with
nonzero (in fact, one-dimensional) space of kσ-invariants. From the Peter-Weyl decompo-
sition for Cq(K) we obtain the irreducible decomposition
Cσ
q (K/M) ≃
⨁
λ∈Λ n
V q
λ
as Uq-modules. Furthermore, for µ ∈P +
d we recall from [5] that
(
Lq
µ
) k∞
=
(
Lq
µ
) Uq(mC)
,
cf. Subsection 5.2.
We ﬁx generic σ,τ ∈ R unless speciﬁed diﬀerently (the case σ = ∞ and/or τ = ∞ will
subsequently be analyzed as degeneration of the theory for σ,τ ∈ R). For λ ∈ Λ n we
choose a nonzero kσ-ﬁxed vector vσ(λ) ∈
(
V q
λ
) kσ
which we normalize by requiring
vσ(λ) =
∑
ν∈Zd
vσ(λ;ν), v σ(λ;λ♮) = uλ♮,
where vσ(λ;ν) ∈ V q
λ is the weight ν component of vσ(λ) in V q
λ and uλ♮ is the highest
weight vector of V q
λ =Lq
λ♮ (it is known that vσ(λ) has a weight λ♮ component, hence such
a normalization is possible). From the analysis in [5, Section 6] it furthe rmore follows that(
V q
λ
) k∗
σ
is spanned by K−δvσ+d−2n(λ) for λ ∈ Λ n (see also [22] for the special case d = 2n).
The normalized quantum zonal spherical functions ϕσ,τ
λ (σ,τ ∈ R) associated to the
one-parameter family of quantum Grassmannians are now deﬁned b y
(8.1) ϕσ,τ
λ ( · ) = q⟨δ,λ♮⟩⟨·vσ(λ),K−δvτ +d−2n(λ)⟩λ
⟨uλ♮,u λ♮⟩λ
, λ ∈ Λ n.
The ϕσ,τ
λ (λ ∈ Λ n) form a basis of
Hσ,τ := {f ∈ Cq(K) | f (YZ ) = 0 = f (ZX ), Z ∈ U q, X ∈ kσ, Y ∈ kτ }.
The analogue of the quantum dimension formula (5.4) in terms of the q uantum zonal
spherical functions ϕσ,τ
λ (λ ∈ Λ n) reads as follows.
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 37
Lemma 8.1. Forλ ∈ Λ n and generic σ,τ ∈ R we have
(8.2) Dim q
(
V q
λ
)
= ϕσ,σ+2n−d
λ (K δ)ϕτ +d−2n,τ
λ (K δ)
‖ϕσ,τ
λ ‖2
h
.
Proof. By the quantum Schur orthogonality relations (see Proposition 3.3 b) we have
(8.3) ‖ϕσ,τ
λ ‖2
h = q2⟨δ,λ♮⟩
Dimq(V q
λ )
‖vσ(λ)‖2
λ‖vτ +d−2n(λ)‖2
λ
‖uλ♮‖4
λ
,
where ‖v‖2
λ := ⟨v,v ⟩λ. On the other hand, from the deﬁnition (8.1) of the quantum zonal
spherical function ϕσ,τ
λ we have
(8.4) ϕσ,σ+2n−d
λ (K δ) = ‖vσ(λ)‖2
λ
‖uλ♮‖2
λ
q⟨δ,λ♮⟩.
The desired quantum dimension formula follows directly from (8.3) and (8.4). □
To arrive at an explicit evaluation of the quantum dimensions, we now t ranslate (8.2) into
an expression involving the evaluations and the quadratic norms of M acdonald-Koornwinder
polynomials.
The radial part P σ,τ
λ := Res T
(
ϕσ,τ
λ
)
∈ C[u±1] is deﬁned to be the unique Laurent poly-
nomial in d independent variables u1,...,u d such that
P σ,τ
λ (qν) = ϕσ,τ
λ (K ν) ∀ν ∈ Zd.
We have the following key facts from [20], see also [5] and [22]. Set zj = uju−1
d+1−j (j =
1,...,n ), then
P σ,τ
λ ∈ C[z±1]W, ∀λ ∈ Λ n,
whereW =Sn ⋉ {±1}n as before. From now on we will view P σ,τ
λ asW -invariant Laurent
polynomial in the independent variables z1,...,z n. The key result is the identiﬁcation of
P σ,τ
λ with Macdonald-Koornwinder polynomials,
P σ,τ
λ (z) = Pλ(z; −qσ+τ +1, −q−σ−τ +1,q σ−τ +1,q−σ+τ +2(d−2n)+1;q2,q 2), λ ∈ Λ n
(the particular normalization of ϕσ,τ
λ ensures that it precisely coincides with the monic
Macdonald-Koornwinder polynomial). We denote ⟨·, ·⟩σ,τ for the corresponding orthogo-
nality pairing (6.3), with the six parameters ( a,b,c,d,q,t ) specialized to
(−qσ+τ +1, −q−σ−τ +1,q σ−τ +1,q−σ+τ +2(d−2n)+1,q 2,q 2).
We set ‖p‖2
σ,τ = ⟨p,p ⟩2
σ,τ for the corresponding quadratic norm of p ∈ C[z±1]W .
Lemma 8.2. Forλ ∈ Λ n and generic σ,τ ∈ R we have
ϕσ,τ
λ (K δ) = P σ,τ
λ (qd−2n+1q2ρ),
‖ϕσ,τ
λ ‖2
h = ‖P σ,τ
λ ‖2
σ,τ.
In particular,
(8.5) Dimq
(
V q
λ
)
= P σ,σ+2n−d
λ (qd−2n+1q2ρ)P τ +d−2n,τ
λ (qd−2n+1q2ρ)
‖P σ,τ
λ ‖2
σ,τ
.
38 URI ONN AND JASPER V. STOKMAN
Proof. Observe thatu =qδ ∈
(
R×) d
maps toz =qd−2n+1q2ρ ∈
(
R×) n
under the assignment
zj =uju−1
d+1−j (j = 1,...,n ). By the deﬁnition of P σ,τ
λ as the radial part of ϕσ,τ
λ , we obtain
the desired expression of ϕσ,τ
λ (K δ) in terms of Macdonald-Koornwinder polynomials. The
quadratic norm formula follows from [5, Corollary 8.1]. The quantum d imension formula
(8.2) then yields (8.5). □
We are now in a position to derive the explicit quantum dimension formula s for the
spherical Uq-representationsV q
λ (λ ∈ Λ n).
Corollary 8.3. Proposition 5.3 holds.
Proof. Observe that the value of the Macdonald-Koornwinder polynomial
P σ,σ+2n−d
λ (z) = Pλ(z; −q2σ+2n−d+1, −q−2σ−2n+d+1,q d−2n+1,q d−2n+1;q2,q 2),
at z = qd−2n+1q2ρ can be evaluated in closed form by the evaluation formula (6.2) for
Macdonald-Koornwinder polynomials. The resulting expression is
P σ,σ+2n−d
λ (qd−2n+1q2ρ) = q(2n−d−1)|λ|−2⟨ρ,λ⟩
×
∏
1≤j<k≤n
(1 −q2(d−2n+1+λj +λk+ρj+ρk))(1 −q2(λj−λk+ρj−ρk))
(1 −q2(d−2n+1+ρj +ρk))(1 −q2(ρj−ρk))
×
n∏
i=1
(
q2(d−2n+1+ρi),q 2(d−2n+1+ρi), −q2(σ+1+ρi), −q2(−σ+d−2n+1+ρi);q2)
λi(
q2(d−2n+1+2ρi);q2)
2λi
.
On the other hand, by the closed expression (6.4) for the quadrat ic norms of the Macdonald-
Koornwinder polynomials we have
‖P σ,τ
λ ‖2
σ,τ =
n∏
j=1



(
q2(1+ρj ),q 2(d−2n+1+ρj );q2) 2
λj
(
q2(d−2n+1+2ρj ),q 2(d−2n+2+2ρj );q2)
2λj
×
(
−q2(σ+1+ρj ), −q2(−σ+d−2n+1+ρj ), −q2(τ +d−2n+1+ρj ), −q2(−τ +1+ρj );q2)
λj
}
.
Combining these explicit formulas with (8.5) we obtain an explicit expres sion for Dim q(V q
λ ),
which results in Proposition 5.3. □
We end this section by considering the σ → ∞ and σ = τ → ∞ degenerations in the
above representation theoretic formulas. This in particular leads t o the interpretation of
Dq(λ;a,b ;t) for special values of the parameters as quantum dimensions of V q
λ (λ ∈ Λ n),
see (5.6).
In [5] the limit σ → ∞ (respectively σ,τ → ∞ ) is considered, leading to the interpre-
tation of the multivariable big q-Jacobi polynomials P B
λ (·; 1,q 2(d−2n), 1,q 2τ +2(d−2n);q2,q 2)
(respectively the multivariable little q-Jacobi polynomials P L
λ (·;q2(d−2n), 1;q2,q 2)) as radial
parts of quantum zonal spherical functions associated to the st andard quantum Grassmann
representation C∞
q (K/M) = Cq(K/M). In these degenerations, the quantum dimensions
Dimq(V q
λ ) are naturally expressed in terms of the multivariable big and little q-Jacobi
polynomials as follows.
QUANTUM DIMENSIONS AND THEIR NON-ARCHIMEDEAN DEGENERATIO NS 39
Proposition 8.4. We have
Dimq(V q
λ ) =
(
−q2τ +d−2n−1) |λ|P L
λ (0;q2(d−2n), 1;q2,q 2)P τ +d−2n,τ
λ (qd−2n+1q2ρ)
NB(λ; 1,q 2(d−2n), 1,q 2τ +2(d−2n);q2,q 2) , ∀λ ∈ Λ n.
Furthermore, in terms of the generalized quantum dimension Dq(λ;a,b ;t), see (2.4), we
have
Dimq(V q
λ ) =
(
P L
λ (0;q2(d−2n), 1;q2,q 2)
) 2
NL(λ;q2(d−2n), 1;q2,q 2) =Dq2(λ;q2(d−2n+1),q 2;q2), ∀λ ∈ Λ n.
Proof. We degenerate the expression (8.5) of the quantum dimension Dim q(V q
λ ) by taking
the limitσ → ∞ (respectivelyσ =τ → ∞). In order to parallel the particular degeneration
scheme from [5], we make use of the elementary symmetry
(8.6) Pλ(−z; −a, −b, −c, −d;q,t ) = ( −1)|λ|Pλ(z;a,b,c,d ;q,t )
for the monic Macdonald-Koornwinder polynomials, which implies the sy mmetry
(8.7) NK(λ; −a, −b, −c, −d;q,t ) = NK(λ;a,b,c,d ;q,t ), λ ∈ Λ n
for the corresponding quadratic norms (which also immediately follow s from its explicit
evaluation (6.2)). Combined with the limit formula (6.36) in base q2, with parameters
(a,b,c,d,t ) specialized to (1 ,q 2(d−2n), 1,q 2τ +2(d−2n),q 2) and with ǫ =qσ+τ−1, we obtain
lim
σ→∞
q2(σ+τ−1)|λ|‖P σ,τ
λ ‖2
σ,τ =NB(λ; 1,q 2(d−2n), 1,q 2τ +2(d−2n);q2,q 2), ∀λ ∈ Λ n.
On the other hand, from (6.11) and the explicit evaluation formula fr om the proof of
Corollary 8.3 we obtain
lim
σ→∞
(
−q2σ) |λ|
P σ,σ+2n−d
λ (qd−2n+1q2ρ) = q(d−2n+1)|λ|P L
λ (0;q2(d−2n), 1;q2;q2), ∀λ ∈ Λ n.
Taking the limit σ → ∞ in (8.5) now leads to the expression of the quantum dimension as
mixture of factors involving Macdonald-Koornwinder, multivariable b ig and multivariable
little q-Jacobi polynomials.
Takingτ =σ in (8.5) and using the fact that
lim
σ→∞
(
q−1+2σ) 2|λ|
‖P σ,σ
λ ‖2
σ,σ =NL(λ;q2(d−2n), 1;q2,q 2), ∀λ ∈ Λ n
in view of (6.21), we similarly obtain the desired expression of the quan tum dimension
Dimq(V q
λ ) in terms of Dq(λ;a,b ;t). □
Remark 8.5. By the arguments from [5] one can show that
lim
σ→∞
(
ϕσ,σ+2n−d
λ
‖ϕσ,σ+2n−d
λ ‖h
)
=ϕq
λ, λ ∈ Λ n
in the pre-Hilbert space Cq(K), where ϕq
λ (λ ∈ Λ n) are the (orthonormal) quantum zonal
spherical functions associated to the standard quantum complex Grassmanian. Degener-
ating (8.2) accordingly, we obtain the quantum dimension formula (5.4 ).
40 URI ONN AND JASPER V. STOKMAN
