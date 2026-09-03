---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-007-33-the-symbol-of-an-operator
section_title: "The Symbol of an Operator"
section_number: 3.3
pages: 9-11
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨ and´ en characterized all linear oper ators on multivariate polynomials which preserve the"
---
Given representations V (λ) and V (α) (for λ ∈ Nm
0 and α ∈ Nl
0) of (SL 2(C))m and (SL 2(C))l respectively,
the space of linear maps between V (λ) and V (α) can be viewed as a representation of (SL 2(C))m+l in a
standard way. This space of linear maps is denoted Hom( V (λ),V (α)). As discussed previously, we will now
use the apolarity form deﬁned above to construct a representat ion isomorphism between Hom( V (λ),V (α))
and V (λ ⊔α) (which is a space of polynomials in m +l variables). This will lead us to a natural deﬁnition
for the symbol of an operator.
The signiﬁcance of this isomorphism will come from the fact that stab ility results about V (λ ⊔α) will
transfer to Hom(V (λ),V (α)) via the symbol lemma (Lemma 3.7) stated below. We will see in §6.2 that this
lemma and Grace’s theorem almost immediately imply a characterization of stability-preserving operators
which is similar to that of Borcea and Br¨ and´ en.
To this end, consider the standard representation isomorphism Ho m(V (λ),V (α)) ∼=V (λ)∗ ⊠V (α), given
by T ↦→∑
µ≤λ(xµyλ−µ)∗ ⊠T (xµyλ−µ), where V (λ)∗ is the dual representation of V (λ). We omit here the
details regarding explicit deﬁnitions of the action of (products of) S L2(C) on Hom and dual representations.
Instead, we utilize the fact that the apolarity form provides an (SL 2(C))m-invariant isomorphism between
V (λ) and the dual representation V (λ)∗, as stated in the following result.
Proposition 3.5. For any λ ∈ Nm
0 , there is an (SL2(C))m-invariant isomorphism V (λ)∗ →V (λ) given by
(xµyλ−µ)∗ ↦→
( λ
µ
)
(−1)µxλ−µyµ.
Proof. We use the apolarity form to determine the isomorphism. In particula r, up to scalar ( xµyλ−µ)∗ maps
to an element p ∈V (λ) such that ( xµyλ−µ)∗ =Dλ(p ⊗ ·). We compute:
Dλ(p ⊗xαyλ−α) = α!(λ −α)!
( λ
α
)
(−1)α∂λ−α
x ∂α
yp =λ!(−1)α∂λ−α
x ∂α
yp
Picking p(x,y ) := (λ!)−2( λ
µ
)
(−1)µxλ−µyµ achieves the desired equality exactly, and therefore ( xµyλ−µ)∗ ↦→( λ
µ
)
(−1)µxλ−µyµ is an (SL 2(C))m-invariant isomorphism.
9
With this, we consider the following string of (SL 2(C))m+l-invariant isomorphisms:
Hom(V (λ),V (α)) →V (λ)∗ ⊠V (α) →V (λ) ⊠V (α) →V (λ ⊔α)
The ﬁrst map is the standard isomorphism discussed above, the sec ond map is induced by the previous
proposition, and the third map is given by the discussion of outer ten sor products in §3.1. This string of
maps is explicitly deﬁned on a given linear operator via:
T ↦→
∑
µ≤λ
(zµwλ−µ)∗ ⊠T (xµyλ−µ)
↦→
∑
µ≤λ
( λ
µ
)
(−1)µzλ−µwµ ⊠T (xµyλ−µ)
↦→
∑
µ≤λ
( λ
µ
)
zλ−µ(−w)µ ·T (xµyλ−µ)
Here, T acts only on the x and y variables, and z and w are the λ variables in V (λ ⊔α). This gives the
desired isomorphism between Hom( V (λ),V (α)) and V (λ ⊔α), and hence we refer to this map as the Symb
map.
Deﬁnition 3.6. Forλ ∈ Nm
0 and α ∈ Nl
0, we deﬁne the following (SL 2(C))m+l-invariant isomorphism:
Symb : Hom(V (λ),V (α)) →V (λ ⊔α)
T ↦→T
[
(zy −xw)λ]
= Hmg (λ,α)
(
T [(z −x)λ]
)
=
∑
µ≤λ
( λ
µ
)
zλ−µ(−w)µ ·T (xµyλ−µ)
We call Symb(T ) the (universal) symbol of T .
This expression bears striking resemblance to the symbol used by B orcea and Br¨ and´ en in [BB09a], which
motivates the use of the name “symbol” here. (In fact, Symb is almo st the homogenization of the Borcea-
Br¨ and´ en symbol.) In§6, Symb will allow us to reduce the study of Hom( V (λ),V (α)) to the study of V (λ⊔α)
via the next lemma. We refer to this next result as the symbol lemma, and it demonstrates the fundamental
connection between an operator T , its symbol, and the apolarity form. Note that the computation don e here
in the proof of this lemma is in a sense redundant. The operator Symb was essentially deﬁned such that
Symb(T ) acts as T via Dλ.
Lemma 3.7 (Symbol Lemma) . Fix λ ∈ Nm
0 , α ∈ Nl
0, and a linear operator T ∈ Hom(V (λ),V (α)). For
q ∈V (λ) and r ∈V (α), we have:
Dλ(Symb(T ) ⊗q ·r) = (λ!)2T (q) ⊗r
Proof. Letting qµ be the coeﬃcient of the xµyλ−µ term of q, we compute:
Dλ(Symb(T ) ⊗q ·r) = Dλ

∑
µ≤λ
( λ
µ
)
xλ−µ(−y)µ ·T (xµyλ−µ) ⊗q ·r


=
∑
µ≤λ
( λ
µ
) 2
(λ −µ)!µ! ·T (xµyλ−µ) ⊗ (∂µ
x∂λ−µ
y q)r
= (λ!)2 ∑
µ≤λ
T (xµyλ−µ) ⊗qµ ·r
= (λ!)2T (q) ⊗r
10
