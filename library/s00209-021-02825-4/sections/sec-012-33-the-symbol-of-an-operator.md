---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-012-33-the-symbol-of-an-operator
section_title: "The symbol of an operator"
section_number: 3.3
pages: 10-12
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
Given representations V (λ) and V (α) (for λ ∈Nm
0 and α ∈Nl
0) of (SL2(C))m and
(SL2(C))l respectively, the space of linear maps between V (λ) and V (α) can be viewed
as a representation of (SL2(C))m+l in a standard way. This space of linear maps is denoted
Hom(V (λ), V (α)). As discussed previously, we will now use the apolarity form deﬁned
A representation theoretic explanation...
1369
above to construct a representation isomorphism between Hom(V (λ), V (α)) and V (λ ⊔α)
(which is a space of polynomials in m + l variables). This will lead us to a natural deﬁnition
for the symbol of an operator.
The signiﬁcance of this isomorphism will come from the fact that stability results about
V (λ ⊔α) will transfer to Hom(V (λ), V (α)) via the symbol lemma (Lemma 3.7) stated
below. We will see in Sect. 6.2 that this lemma and Grace’s theorem almost immediately
imply a characterization of stability-preserving operators which is similar to that of Borcea
and Brändén.
To this end, consider the standard representation isomorphism Hom(V (λ), V (α)) ∼=
V (λ)∗⊠V (α), given by T →
μ≤λ(xμyλ−μ)∗⊠T (xμyλ−μ), where V (λ)∗is the dual
representation of V (λ). We omit here the details regarding explicit deﬁnitions of the action
of (products of) SL2(C) on Hom and dual representations. Instead, we utilize the fact that
the apolarity form provides an (SL2(C))m-invariant isomorphism between V (λ) and the dual
representation V (λ)∗, as stated in the following result.
Proposition 3.5 For any λ ∈Nm
0 , there is an (SL2(C))m-invariant isomorphism V (λ)∗→
V (λ) given by (xμyλ−μ)∗→
λ
μ
	
(−1)μxλ−μyμ.
Proof We use the apolarity form to determine the isomorphism. In particular, up to scalar
(xμyλ−μ)∗maps to an element p ∈V (λ) such that (xμyλ−μ)∗= Dλ(p ⊗·). We compute:
Dλ(p ⊗xαyλ−α) = α!(λ −α)!
λ
α

(−1)α∂λ−α
x
∂α
y p = λ!(−1)α∂λ−α
x
∂α
y p
Picking p(x, y) := (λ!)−2λ
μ
	
(−1)μxλ−μyμ achieves the desired equality exactly, and there-
fore (xμyλ−μ)∗→
λ
μ
	
(−1)μxλ−μyμ is an (SL2(C))m-invariant isomorphism.
⊓⊔
With this, we consider the following string of (SL2(C))m+l-invariant isomorphisms:
Hom(V (λ), V (α)) →V (λ)∗⊠V (α) →V (λ) ⊠V (α) →V (λ ⊔α)
The ﬁrst map is the standard isomorphism discussed above, the second map is induced by the
previous proposition, and the third map is given by the discussion of outer tensor products
in Sect. 3.1. This string of maps is explicitly deﬁned on a given linear operator via:
T →

μ≤λ
(zμwλ−μ)∗⊠T (xμyλ−μ)
→

μ≤λ
λ
μ

(−1)μzλ−μwμ ⊠T (xμyλ−μ)
→

μ≤λ
λ
μ

zλ−μ(−w)μ · T (xμyλ−μ)
Here, T acts only on the x and y variables, and z and w are the λ variables in V (λ ⊔α). This
gives the desired isomorphism between Hom(V (λ), V (α)) and V (λ⊔α), and hence we refer
to this map as the Symb map.
Deﬁnition 3.6 For λ ∈Nm
0 and α ∈Nl
0, we deﬁne the following (SL2(C))m+l-invariant
isomorphism:
Symb : Hom(V (λ), V (α)) →V (λ ⊔α)
T →T

(zy −xw)λ

= Hmg(λ,α)

T [(z −x)λ]
	
=

μ≤λ
λ
μ

zλ−μ(−w)μ · T (xμyλ−μ)
1370
J. Leake
We call Symb(T ) the (universal) symbol of T .
This expression bears striking resemblance to the symbol used by Borcea and Brändén
in [1], which motivates the use of the name “symbol” here. (In fact, Symb is almost the
homogenization of the Borcea–Brändén symbol.) In Sect. 6, Symb will allow us to reduce
the study of Hom(V (λ), V (α)) to the study of V (λ ⊔α) via the next lemma. We refer to this
next result as the symbol lemma, and it demonstrates the fundamental connection between
an operator T , its symbol, and the apolarity form. Note that the computation done here in
the proof of this lemma is in a sense redundant. The operator Symb was essentially deﬁned
such that Symb(T ) acts as T via Dλ.
Lemma 3.7 (Symbol Lemma) Fix λ ∈Nm
0 , α
∈Nl
0, and a linear operator T
∈
Hom(V (λ), V (α)). For q ∈V (λ) and r ∈V (α), we have:
Dλ(Symb(T ) ⊗q · r) = (λ!)2T (q) ⊗r
Proof Letting qμ be the coefﬁcient of the xμyλ−μ term of q, we compute:
Dλ(Symb(T ) ⊗q · r) = Dλ
⎛
⎝
μ≤λ
λ
μ

xλ−μ(−y)μ · T (xμyλ−μ) ⊗q · r
⎞
⎠
=

μ≤λ
λ
μ
2
(λ −μ)!μ! · T (xμyλ−μ) ⊗(∂μ
x ∂λ−μ
y
q)r
= (λ!)2 
μ≤λ
T (xμyλ−μ) ⊗qμ · r
= (λ!)2T (q) ⊗r
⊓⊔
