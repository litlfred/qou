---
doc_id: arxiv-hep-th-0610241v1
doc_title: "Gravity and the standard model with neutrino mixing"
section_id: sec-017-4-the-lagrangian
section_title: "The Lagrangian"
section_number: 4
pages: 34-36
source_pdf: hep-th-0610241.pdf
source_sha256: 6a71ab6f6459c070
toc_source: inferred
doc_brief: "Gravity and the standard model with neutrino mixing — We present an eﬀective uniﬁed theory based on noncommutative geometry for the standard model with neutrino mixing, minimally coupled to gravity."
---
The KO-dimension of the ﬁnite space F is 6 ∈Z/8, hence the KO-dimension of the product
geometry M × F (for M a spin 4-manifold) is now 2 ∈Z/8. In other words, according to
Deﬁnition 2.7, the commutation rules are
J2 = −1,
JD = DJ,
and Jγ = −γJ .
(4.1)
Let us now explain how these rules deﬁne a natural antisymmetric bilinear form on the even
part
H+ = {ξ ∈H , γ ξ = ξ}
(4.2)
of H.
Proposition 4.1. On a real spectral triple of KO-dimension 2 ∈Z/8, the expression
AD(ξ′, ξ) = ⟨J ξ′, D ξ⟩,
∀ξ, ξ′ ∈H+
(4.3)
deﬁnes an antisymmetric bilinear form on H+ = {ξ ∈H , γ ξ = ξ}. The trilinear pairing
(4.3) between D, ξ and ξ′ is gauge invariant under the adjoint action of the unitary group of
A, namely
AD(ξ′, ξ) = ADu(Ad(u)ξ′, Ad(u)ξ) ,
Du = Ad(u) D Ad(u∗).
(4.4)
Proof. 1) We use an inner product which is antilinear in the ﬁrst variable. Thus, since J is
antilinear, A is a bilinear form. Let us check that A is antisymmetric. One has
AD(ξ, ξ′) = ⟨J ξ, D ξ′⟩= −⟨J ξ, J2 D ξ′⟩= −⟨J D ξ′, ξ⟩= −⟨D J ξ′, ξ⟩= −⟨J ξ′, D ξ⟩
where we used the unitarity of J, i.e. the equality
⟨J ξ, J η⟩= ⟨η, ξ⟩,
∀ξ , η ∈H.
(4.5)
Finally, one can restrict the antisymmetric form AD to H+ without automatically getting
zero since one has
γ JD = JD γ .
2) Let us check that Ad(u) commutes with J. By deﬁnition Ad(u) = u (u∗)0 = u JuJ−1.
Thus
J Ad(u) = J u JuJ−1 = u J u JJ−1 = u J u = Ad(u) J ,
where we used the commutation of u with J u J. Since Ad(u) is unitary, one gets (4.4).
Now the Pfaﬃan of an antisymmetric bilinear form is best expressed in terms of the functional
integral involving anticommuting “classical fermions” (cf. [42], §5.1) At the formal level, this
means that we write
Pf(A) =
Z
e−1
2A(˜ξ) D[˜ξ]
(4.6)
Notice that A(ξ, ξ) = 0 when applied to a vector ξ, while A(˜ξ, ˜ξ)̸ = 0 when applied to
anticommuting variables ˜ξ. We deﬁne
H+
cl = {˜ξ : ξ ∈H+}
(4.7)
to be the space of classical fermions (Grassman variables) corresponding to H+ of (4.2).
GRAVITY AND THE STANDARD MODEL WITH NEUTRINO MIXING
35
As the simplest example let us consider a two dimensional vector space E with basis ej and
the antisymmetric bilinear form
A(ξ′, ξ) = a(ξ′
1ξ2 −ξ′
2ξ1)
For ˜ξ1 anticommuting with ˜ξ2, using the basic rule (cf. [42], §5.1)
Z
˜ξj d˜ξj = 1
one gets
Z
e−1
2 A(˜ξ) D[˜ξ] =
Z
e−a ˜ξ1 ˜ξ2 d˜ξ1d˜ξ2 = a.
Remark 4.2. It is the use of the Pfaﬃan as a square root of the determinant that makes it
possible to solve the Fermion doubling puzzle which was pointed out in [36]. We discuss this
in §4.4.1 below. The solution obtained by a better choice of the KO-dimension of the space
F and hence of M × F is not unrelated to the point made in [27].
We now state our main result as follows.
Theorem 4.3. Let M be a Riemannian spin 4-manifold and F the ﬁnite noncommutative
geometry of KO-dimension 6 described above. Let M ×F be endowed with the product metric.
1. The unimodular subgroup of the unitary group acting by the adjoint representation Ad(u)
in H is the group of gauge transformations of SM.
2. The unimodular inner ﬂuctuations of the metric give the gauge bosons of SM.
3. The full standard model (with neutrino mixing and seesaw mechanism) minimally cou-
pled to Einstein gravity is given in Euclidean form by the action functional
S = Tr(f(DA/Λ)) + 1
2 ⟨J ˜ξ, DA ˜ξ⟩,
˜ξ ∈H+
cl,
(4.8)
where DA is the Dirac operator with the unimodular inner ﬂuctuations.
Remark 4.4. Notice that the action functional (4.8) involves all the data of the spectral
triple, including the grading γ and the real structure J.
Proof. We split the proof of the theorem in several subsections.
To perform the comparison, we look separately at the terms in the SM Lagrangian. After
dropping the ghost terms, one has ﬁve diﬀerent groups of terms.
1. Yukawa coupling LHf
2. Gauge fermion couplings Lgf
3. Higgs self-coupling LH
4. Self-coupling of gauge ﬁelds Lg
5. Minimal coupling of Higgs ﬁelds LHg
36
CHAMSEDDINE, CONNES, AND MARCOLLI
