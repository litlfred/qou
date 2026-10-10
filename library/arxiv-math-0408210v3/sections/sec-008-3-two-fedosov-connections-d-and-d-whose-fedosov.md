---
doc_id: arxiv-math-0408210v3
doc_title: "A SIMPLE ALGEBRAIC PROOF OF THE ALGEBRAIC INDEX THEOREM"
section_id: sec-008-3-two-fedosov-connections-d-and-d-whose-fedosov
section_title: "Two Fedosov connections D and ~D whose Fedosov-Weyl curvatures represent the same"
section_number: 3
pages: 9-12
source_pdf: 0408210v3.pdf
source_sha256: 16d5ccb83a86954f
doc_brief: "A SIMPLE ALGEBRAIC PROOF OF THE ALGEBRAIC INDEX THEOREM — In math.QA/0311303 B. Feigin, G. Felder, and B."
---
De Rham cohomology class in H 2
DR(M)[[ℏ]] are equivalent in the sense of deﬁnition 4.
If the equivalence betweenD and ~D is established by an element U ∈IN ⊕Γ(W 1(EndV ))
then the map
a ↦→U ◦a ◦U −1
gives an isomorphism from the algebra Γ ~D(W (EndV )) of ﬂat sections of ~D to the
algebra Γ D(W (EndV )) of ﬂat sections of D .
9
Remark 1. The construction of the Fedosov connection is functorial in the se nse that if u
is an isomorphism from V to ~V then
~D =D + [uD(u−1), · ]
is a Fedosov connection in Ω •(W (End ~V )) . Moreover, the corresponding isomorphisms
λ : EndV ((ℏ)) ~→ Γ D(W (EndV )), ~λ : End ~V ((ℏ)) ~→ Γ ~D(W (End ~V ))
are related by the formula
~λ(a) = uλ(u−1au)u−1, a ∈End ~V .
Remark 2. If V is a trivial vector bundle L1 of rank N = 1 then the isomorphism λ (28)
gives a star-product ∗ in the algebra of functions C(M)((ℏ)) . Due to the result of P. Xu [19],
any star-product in C(M)((ℏ)) is equivalent to the one obtained via Fedosov’s procedure 2.
In particular, the cohomology class of the Fedosov-Weyl curvatu re (18) is a well-deﬁned
characteristic class of a star-product in C(M)((ℏ)). This characteristic class is referred to
as the Deligne-Fedosov class .
Let us prove here an important technical lemma which might as well ha ve an independent
interest
Lemma 1 Let V be a vector bundle over the symplectic manifold M and D be a Fedosov
connection (17) with the form r = A +dxiω ij(x)yj satisfying the normalization condition
(27). If q ∈EndV is an endomorphism of V then
∂Vq = 0 ⇒ Dq = 0.
In other words, if q is ∂V -ﬂat then the isomorphism λ (28) sends the q to itself.
Proof. Since q does not depend on y′s and ∂Vq = 0 we have that ∇q = δq = 0 . Hence,
Dq = ℏ−1[r,q ] and it suﬃces to show that the commutator [ r,q ] is vanishing. Since D is
nilpotent D[r,q ] = 0.
The operator δ−1 (24) is not a derivation of algebra Ω •(W (EndV )). However, since q
does not depend on y′s and δ−1r = 0,
δ−1[r,q ] = 0 .
Thus if η = [r,q ] ∈ Ω 1(W (EndV )) we have
δη = ∇η + 1
ℏ [r,η ], δ −1η = 0.
Therefore, applying (25) to η we get
η =δ−1(∇η + 1
ℏ [r,η ]).
The latter equation has the unique vanishing solution since δ−1 raises the degree in y . Thus
the lemma is proven. ✷
2See paper [8], in which this result was extended to any smooth aﬃne alg ebraic symplectic variety.
10
2.4 The Feigin-Felder-Shoikhet trace density map.
Let as above V be a vector bundle of rank N over the symplectic manifold M and ∗ be a
star-product (12) in the algebra EndV ((ℏ)) . Then,
Deﬁnition 5 A trace density map trd is a C((ℏ))-linear map
trd : EndV ((ℏ)) ↦→H 2n(M)((ℏ))
vanishing on commutators
trd(a ∗b −b ∗a) = 0 , a,b ∈EndV ((ℏ)).
We will show that if the star-product ∗ inEndV ((ℏ)) is obtained via the Fedosov procedure
[9] then the Feigin-Felder-Shoikhet cocycle (6) provides us with a na tural trace density map.
Let as above D be the Fedosov connection (17) and λ be the isomorphism (28). Since Θ N
2n
(6) is a cocycle of g = glN (W) relative to h = glN ⊕ sp2n , we have the following well-deﬁned
map
Ψ D : EndV ((ℏ)) ↦→Ω 2n(M)((ℏ)), Ψ D(a) = 1
ℏn Θ N
2n(A,...,A,λ (a)), (29)
where A ∈ Ω 1(W (EndV )) is the one-form entering the deﬁnition of the Fedosov connectio n
D (17) .
We assemble the required properties of the map Ψ D in the following
Theorem 3 (Feigin-Felder-Shoikhet, [10]) With the above notations the following state-
ments hold:
i) If V1 and V2 are two vector bundles over M and D1, D 2 are Fedosov connections on
W (EndV1) and W (EndV2), respectively, then for any a ∈EndV1
Ψ D1⊕D2(a ⊕ 0) = Ψ D1(a),
where 0 stands for the trivial endomorphism of V2 .
ii) For any pair of endomorphisms a,b ∈EndV ((ℏ))
Ψ D(a ∗b −b ∗a) ∈dΩ 2n−1(M)((ℏ)),
whered is the De Rham diﬀerential.
iii) LetD and ~D be two equivalent Fedosov connections and U ∈IN ⊕ Γ(W 1(EndV )) be the
element establishing their equivalence in the sense of (21) . Then for any a ∈EndV ((ℏ))
Ψ ~D(σ(U −1 ◦λ(a) ◦U)) − Ψ D(a) ∈dΩ 2n−1(M)((ℏ)),
whereσ is the projection (26) and λ is the isomorphism (28).
iv) For the identity endomorphism IN ∈EndV
Ψ D(IN ) − 1
ℏnQn(C(A,A ),...,C (A,A )) ∈dΩ 2n−1(M)((ℏ)),
where Qn ∈ ((Snh)∗)h is the n-th component of the adjoint invariant form (11), A ∈
Ω 1(W (EndV )) is the one-form entering the deﬁnition of the Fedosov connec tion D (17)
and C is the ﬁberwise “curvature” (7) of the projection (9) .
11
Proof. Statement i) is obvious from the construction of the cocycle Θ N
2n (1), (5), (6).
Statements ii), iii), and iv) are proven in [10] for the case when the bundle V is trivial.
Statements ii) and iii) follow from the fact Θ N
2n is a cocycle relative to h = glN ⊕ sp2n and
statementiv) is a consequence of (10) . These results of [10] are generalized to the non-trivial
bundle V in a straightforward manner since we always deal with the Lie algebra cochains
relative to h = glN ⊕ sp2n . ✷
As an immediate consequence of this theorem we get that
Corollary 1 If ∗ is the star-product in EndV ((ℏ)) obtained via the isomorphism λ (28) then
trd(a) = [Ψ D(a)] : EndV ((ℏ)) ↦→H 2n(M)((ℏ)) (30)
is a trace density map.
In what follows we refer to (30) as the Feigin-Felder-Shoikhet (FFS ) trace density map.
