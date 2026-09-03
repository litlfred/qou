---
doc_id: arxiv-math-0203003v2
doc_title: "On the quantum Kazhdan-Lusztig functor Pavel I. Etingof Adriano A. Moura etingof@math.mit.edu adrianoam@ime.unicamp.br Introduction One of the most exciting developments in represe"
section_id: sec-003-3-gauge-transformations
section_title: "Gauge Transformations"
section_number: 3
pages: 8-10
source_pdf: 0203003v2.pdf
source_sha256: 7579ae76959396b8
doc_brief: "On the quantum Kazhdan-Lusztig functor Pavel I. Etingof Adriano A. Moura etingof@math.mit.edu adrianoam@ime.unicamp.br Introduction One of the most exciting developments in representation the ory in t"
---
To prove the theorem stated in the introduction, it remains t o identify the category Repf(RV ) for
V being the vector representation of Uq(ˆsln) with the category of representations of Felder’s elliptic
quantum group. To construct such an identiﬁcation is the goa l of this section. It is achieved by
using the fact that the corresponding dynamical R-matrices are gauge equivalent [M01].
The concept of gauge transformations of quantum dynamical R -matrices of gln type, that we
brieﬂy recall now, was introduced in [EV98].
Let h be an abelian n-dimensional Lie algebra. A multiplicative m-form on h∗ is a collection of
meromorphic functions ϕ = {ϕ a1,...,a m(λ)} where {a1,...,a m} runs through all (ordered) subsets
of {1,...,n } such that
ϕ a1,...,a i+1,a i,...,a m(λ)ϕ a1,...,a m(λ) = 1
Let Ω m be the set of all multiplicative m-forms. With the obvious deﬁnitions one turns Ω m into
an abelian group where the neutral element is the constant fo rm 1a1,...,a m(λ) = 1.
For a given γ ∈ C∗ and s ∈ { 1,...,n } deﬁne the operator δs on the space of meromorphic
functions on h∗ given by
δsf (λ 1,...,λ n) = f (λ 1,...,λ n)
f (λ 1,...,λ s −γ,...,λ n)
and then the diﬀerential homomorphism dγ : Ω m → Ω m+1, ϕ ↦→dγϕ , where
(dγϕ )a1,...,a m+1(λ) =
m+1∏
s=1
(
δasϕ a1,...,a s− 1,a s+1,...,a m+1(λ)
) (−1)s+1
We have d2
γϕ = 1 ∀ϕ . A form ϕ is said to be γ-closed if dγϕ = 1 and γ-exact if ϕ =dγψ for some
form ψ . When γ = 1 we just say that ϕ is closed or exact and denote d1 simply by d.
We list now the gauge transformations that will be important for us. Let R be an R-matrix of
gln type and step γ and deﬁne the following transformations
R(u,λ ) ↦→c(u)R(u,λ ) (3.1)
where c(u) is a meromorphic scalar function;
R(u,λ ) ↦→R(au,bλ +µ ) (3.2)
where a,b ∈ C∗ and µ ∈ h∗;
R(u,λ ) ↦→
n∑
m=0
α m,m (u,λ )Em,m ⊗Em,m +
∑
m⁄=l
ϕ m,l (λ)α m,l (u,λ )Em,m ⊗El,l +βm,l (u,λ )El,m ⊗Em,l (3.3)
8
where ϕ = {ϕ m,l (λ)} is a γ-closed 2-form.
It was proved in [EV98] that if ˜R is obtained from R by these gauge transformations, then it is
a quantum dynamical R-matrix of gln type and step γ (for (3.1) and (3.3)) or γ/b (for (3.2)). It is
clear that if ˜R is obtained from R by (3.1) and (3.2), then Repf( ˜R) is equivalent to Repf(R). The
following theorem, concerning gauge transformation (3.3) , was proved in [EV99] in the language of
bialgebroids. We repeat the proof here with the appropriate adaptations for this context.
Theorem 3.1. LetR be a quantum dynamical R-matrix of gln type and step γ andϕ be a γ-exact
2-form. If ˜R is obtained from R by (3.3) with this ϕ then Repf( ˜R) ∼= Repf(R)
Proof. Let ϕ =dγζ and set ξ = ∑
aζaEa,a . Note ﬁrst that we can write
˜R(u,λ ) = (ξ(1)(λ −γh(2)))−1(ξ(2)(λ))−1R(u,λ )ξ(1)(λ)ξ(2)(λ −γh(1))
Then let (W,L ) be a representation of R and set
˜L(u,λ ) = (ξ(1)(λ −γh(2)))−1L(u,λ )ξ(1)(λ)
Now it is easy to check that the functor ( W,L ) ↦→(W, ˜L) (identity on morphisms) is an equivalence
of tensor categories.
One can regard the exchange matrix RCn of example 2.1 as deﬁned on the whole Cartan sub-
algebra of gln. Then, if one looks at the coordinate k as a parameter, it is a quantum dynamical
R-matrix of gln type.
Theorem 3.2. [M01] Let Rell
τ,γ be the elliptic quantum dynamical R-matrix of example 1.2. T hen
RCn is gauge equivalent to Rell
τ,γ for γ = log q
πi and τ = −κγ = −κ log q
πi , where κ =k +n.
The three gauge transformations we have listed are used in th eorem 3.2. In particular, the
gauge transformation of type (3.3) used is given by the follo wing multiplicative 2-form
ϕ i,j (λ) = σj,i (λ/γ −ρ) (3.4)
where, for m<l ,
σl,m (λ) = q Γ p(1 + 1
κ (λ +ρ)l,m + 1
κ )
Γ p(1 + 1
κ (λ +ρ)l,m )
Γ p(− 1
κ (λ +ρ)l,m )
Γ p(− 1
κ (λ +ρ)l,m + 1
κ ) ,σ m,l (λ) = 1
σl,m (λ),
and Γ q is the q-Gamma function.
Lemma 3.3. The multiplicative 2-form (3.4) is γ-exact.
Proof. It is enough to show that ˜ ϕ i,j (λ) = ϕ i,j (γλ ) is exact. Let ξ = {ξj} be the 1-form given
by ξj(λ) = ∏
i<jqλ i. Then δsξj(λ) = 1 if s > jand δsξj(λ) = q if s < j. Therefore, for m < l,
(dξ)m,l (λ) = q and (dξ)l,m (λ) = q−1. In a similar way one proves that ˜ ϕ =d(ξηζ) where
ηj(λ) =
∏
i<j
Γ p
( λ i,j + 1
κ
) −1
and ζj(λ) =
∏
i<j
Γ p
(
1 + λ j,i
κ
) −1
Thus, we have constructed the equivalence of categories G : Repf(RV ) → Repf(Rell
τ,γ ), where
V = Cn, and hence, proved the following theorem, which is our main r esult.
Theorem 3.4. The functor F = GF V : Repf(Uq(ˆsln)) ⊗CMV → Repf(Rell
τ,γ ) is an exact, fully
faithful tensor functor, which deﬁnes an equivalence of Repf(Uq(ˆsln))⊗CMV with a full subcategory
of Repf(Rell
τ,γ ).
9
