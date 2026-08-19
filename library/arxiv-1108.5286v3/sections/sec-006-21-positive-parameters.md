---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of aﬃne Hecke algebras Maarten Solleveld Radboud Universiteit Nijmegen"
section_id: sec-006-21-positive-parameters
section_title: "Positive parameters"
section_number: 2.1
pages: 16-21
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
doc_brief: "Hochschild homology of affine Hecke algebras Maarten Solleveld Radboud Universiteit Nijmegen — Let H = H(R,q ) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not"
---
In this subsection we assume that q is positive. We will deﬁne analytic families
of representations and show that they can be used to construc t the dual space of
H(R,q ).
Theorem 2.1. Letξ,ξ′ ∈ Ξ .
(a) The H ⋊ Γ -representationsπΓ (ξ) and πΓ (ξ′) have the same trace if and only if
there exists a g ∈ G such that gξ =ξ′.
(b) Suppose that ξ,ξ′ ∈ Ξ un. Then πΓ (ξ) and πΓ (ξ′) are completely reducible, and
they have a common irreducible subquotient if only if there e xists a g ∈ G such
that gξ =ξ′. Moreover πΓ (ξ) ∼
=πΓ (ξ′) in this situation.
Proof. (a) [Sol3, Lemma 3.1.7] provides the ”if”-part. By [Sol3, pa ge 44] the
”only if”-part can be reduced to certain positive induction data, to which [Sol3,
Theorem 3.3.1] applies.
(b) See Corollary 3.1.3 and Theorem 3.3.1 of [Sol3]. We note t hat this is essentially
a consequence of Theorem 1.5. ✷
Since γ(P ) ⊂ ∆ for all γ ∈ Γ and P ⊂ ∆, (27) describes an action of Γ on Ξ.
Given an induction datum ξ = (P,δ,t ) ∈ Ξ we put
Γ ξ = {γ ∈ Γ P |δ ◦φt ∼
=δ ◦φt ◦ψ−1
γ as HP -representations }.
Now we ﬁx ( P,δ,u ) ∈ Ξ un and we let σ be an irreducible direct summand of
Ind
HP ⋊Γ (P,δ,u)
HP (δ ◦φu). In this case we abbreviate Γ (P,δ,u) = Γ σ. By Cliﬀord theory
the representations IndHP ⋊Γ σ
HP (δ ◦φu) and IndHP ⋊Γ P
HP ⋊Γ σ
(σ) are completely reducible.
Let T σ be the connected component of T W (RP )⋊Γ σ that contains 1 ∈T . Notice
that T σ ⊂T P because T W (RP )
P is ﬁnite. We call
{
πσ(t) = IndH⋊Γ
HP ⋊Γ σ
(σ ◦φt) |t ∈T σ}
(32)
an analytic d-dimensional family of H ⋊ Γ-representations, where d is the dimension
of the complex algebraic variety T σ. By Proposition 1.4 the representations πσ(t)
are tempered if and only if t ∈T σ
un :=T σ ∩Tun. We refer to {πσ(t) |t ∈T σ
un} as a
tempered analytic family or an analytic family of S-representations.
Correction (2021): To guarantee that the union of analytic families of rep-
resentations spans GQ(H × Γ), we need to allow more general σ. Namely, we need
all irreducible tempered elliptic representations of a par abolic subalgebra HP ⋊ Γ′
P ,
where Γ′
P is an arbitrary subgroup of Γ P . Here elliptic means that the image in
GQ(HP ⋊ Γ′
P ) does not belong to the span of the representations induced f rom
proper parabolic subalgebras of HP ⋊ Γ′
P . Such a σ is a direct summand of the
HP ⋊ Γ′
P -representation associated to a triple ( P,δ,u ) ∈ Ξ un. With that, the below
16
arguments hold in the necessary generality.
Since there are only ﬁnitely many pairs ( P,δ ) and since two u’s in the same T σ-
coset give rise to the same analytic family, there exist only ﬁnitely many analytic
families of H ⋊ Γ-representations. Recall from [OpSo1, Theorem 2.58] that the
absolute value of any AP -weight of δ is a monomial in the variables q(sα)±1/2. That
is, it lies in
W (RP )uδYP ⊗ZqZ/2 (33)
where uδ ∈TP,un is the unitary part of such a weight. Hence all A-weights of πσ(t)
lie in
W′tuuδY ⊗ZqZ/2. (34)
We note that the HP ⋊ Γ σ-representation πσ(t) is only deﬁned for t ∈T W (RP )⋊Γ σ ,
so it is impossible to extend (32) to a larger connected subse t of T P . As discussed
in [Sol3] after (3.30), the representations πσ(t) are irreducible for t in a Zariski-open
dense subset of T σ. Like in (28) the group
Gσ :=
{
g ∈ G | g(P ) = P,δ ◦ψ−1
g ∼
=δ,g stabilizes {πσ(t) |t ∈T σ
un}
}
(35)
acts on T σ. (Here the advantage of considering only T σ
un is that Theorem 2.1.b
applies.) By Theorem 2.1.a πσ(t) and πσ(gt) have the same trace for all t ∈ T σ
and g ∈ G σ. We will see later that every representation πσ(t′) with t′ in a diﬀerent
Gσ-orbit has a diﬀerent trace.
LetG(A) denote the Grothendieck group of ﬁnite dimensional A-representations,
for suitable algebras or groups A. As explained in [Sol3, Section 3.4],
GQ(H ⋊ Γ) := Q ⊗ZG(H ⋊ Γ)
can be built from analytic families of representations (cal led smooth families in
that paper). By this we mean that we can choose a collection of analytic families
{πσi(t) |t ∈T σi} such that the set
⋃
i
{πσi(t) |t ∈T σi/Gσi} (36)
spans GQ(H ⋊ Γ). In [Sol3, Section 3.4] this is actually done with ”Langla nds
constituents” of πσi(t). But by [Sol3, Lemma 2.2.6] the Langlands formalism is such
that the other constituents of πσi(t) are smaller in a certain sense. Hence the non-
Langlands constituents are already accounted for by famili es of smaller dimension.
All this can be made much more concrete for the algebra
H(R, 1) ⋊ Γ = C[X ⋊ (W ⋊ Γ)] = O(T ) ⋊W′.
By classical results which go back to Frobenius and Cliﬀord, i ts irreducible repre-
sentations with O(T )W ′
-character W′t are in bijection with the irreducible repre-
sentationsσ of the isotropy group W′
t , via
σ ↦→IndX⋊W ′
X⋊W ′
t
(Ct ⊗σ). (37)
17
With this one can easily determine the dual space of X ⋊W′. Let
˜T = {(w,t ) ∈T ×W′ |w(t) = t}.
ThenW′ acts on ˜T byw · (w′,t ) = (ww′w−1,w (t)) and ˜T/W′ is called the extended
quotient of T byW′. Let ⟨W′⟩ be a set of representatives for the conjugacy classes
in W′. Then
˜T/W′ ∼
=
⨆
w∈⟨W ′⟩
T w/ZW ′(w), (38)
where ZW ′(w) denotes the centralizer of w in W′. Let T w
i /ZW ′(w),i = 1,...,c (w)
be the connected components of T w/ZW ′(w), so that
˜T/W′ ∼
=
⨆
w∈⟨W ′⟩
⨆
1≤i≤c(w)
T w
i /ZW ′(w). (39)
By the above there exists a continuous bijection from ˜T/W′ to the space of irre-
ducible complex representations ofX⋊W′. We vary a little and take the Grothendieck
group of X ⋊W′ instead. Let Cw ⊂W′ be the cyclic group generated by w and let
ρw be a Cw-representation. This yields an analytic family of X ⋊W′-representations
{
πw,i(t) := Ind X⋊W ′
X⋊Cw (Ct ⊗ρw) |t ∈T w
i
}
.
For generic t, πw,i(t) is irreducible if W′
t =Cw. Moreover πw,i(t) arise by induction
from an elliptic representation of X ⋊ (W (RP ) ⋊ Γ′
P ), where W (RP ) ⋊ Γ′
P is a
parabolic subgroup of W ⋊ Γ minimally containing w.
By Artin’s Theorem [Ser, Theorem 17] it is possible to choose the ρw such that
GQ(W′
t ) is spanned by {IndW ′
t
Cw (ρw) |w ∈W′
t },
Correction (2021): The next claim is false, it can fail for
instance if W′ = Z/4Z.
and a basis is obtained by taking only one w from every conjugacy class in W′
t .
It follows that the representations
{
πw,i(t) |w ∈ ⟨W′⟩, 1 ≤i ≤c(w),t ∈T w
i /ZW ′(w)
}
(40)
form a basis of GQ(X ⋊W′). Notice that the space underlying (40) is exactly the
extended quotient ˜T/W′, since all the involved representations are diﬀerent. Havin g
described this Grothendieck group conveniently, we recall how it can be compared
with the Grothendieck groups of associated aﬃne Hecke algeb ras.
Theorem 2.2. [Sol3, Section 2.3]
Letq be positive. There exists a natural Q-linear bijection
ζ∨ :GQ(H ⋊ Γ) →GQ(X ⋊W′)
such that:
18
(1 ) ζ∨ restricts to a bijection between the corresponding Grothen dieck groups of
tempered representations;
(2 ) ζ∨ commutes with parabolic induction, in the sense that for a su bgroup Γ′
P ⊂ Γ P ,
a tempered HP ⋊ Γ′
P -representationπ and t ∈T W (RP )⋊Γ ′
P we have
ζ∨(
IndH⋊Γ
HP ⋊Γ ′
P
(π ◦φt)
)
= IndX⋊(W ⋊Γ)
X⋊(W (RP )⋊Γ ′
P )(ζ∨(π) ◦φt);
(3 ) if u ∈ Tun and π is a virtual representation with central character in W′uTrs,
then so is ζ∨(π).
Let d ∈ N. By property (2) ζ∨ sends analytic d-dimensional families of H ⋊ Γ-
representations to analytic d-dimensional families of X ⋊W′-representations - except
that the latter need not be generically irreducible. The ima ge can not be part of a
higher dimensional analytic family, for that would violate the bijectivity of ζ∨. Since
no d-dimensional variety is a ﬁnite union of varieties of dimens ion strictly smaller
than d, and since there are only ﬁnitely many analytic families, ζ∨ restricts to a
bijection between the subspaces (of the Grothendieck group s) spanned by analytic
families of dimension at least d. Let us call these subspaces Gd
Q(H ⋊ Γ) and Gd
Q(X ⋊
W′). Then ζ∨ induces a bijection
Gd
Q(H ⋊ Γ)/Gd+1
Q (H ⋊ Γ) →Gd
Q(X ⋊W′)/Gd+1
Q (X ⋊W′). (41)
By (40) the right-hand side has a basis which is parametrized by the d-dimensional
part of ~T/W′.
Correction (2022): Unfortunately the below construction of families of repre-
sentations does not work in general, because of the problems with (40) and because
an application of Theorem 2.2 could result in virtual H ⋊ Γ-representations. Never-
theless a collection of families of representations satisf ying Lemma 2.3 below can be
found in most cases:
• When the parameters q are of “geometric type”, one can use families of stan-
dard representations from [AMS, Paragraph 3.3].
• For most positive-valued q one can use the technique with parameter defor-
mations from [Sol4, proof of Lemma 6.4], to reduce to the prev ious case.
• We are not aware of any examples of graded Hecke algebras for w hich it is clear
that they do not possess families of representations satisf ying Lemma 2.3.
In all these cases, the remainder of the paper is valid withou t further changes.
We can use this to pick a suitable collection of analytic fami lies of H ⋊ Γ-
representations. Fix a d-dimensional component of ~T/W′ and let C be its im-
age in T/W′. In the notation of (39) let ˜C be the collection of ( w,i ) such that
19
w ∈ ⟨W′⟩, 1 ≤ i ≤ c(w) and T w
i /W′ = C. By Theorem 2.2 and (41) there exist
analytic families of H ⋊ Γ-representations {πσw,i (t) | (w,i ) ∈ ˜C,t ∈T σw,i } such that
ζ∨(
Gd+1
Q (H ⋊ Γ)
)
+ζ∨(
{πσw,i (t) | (w,i ) ∈ ˜C,t ∈T σw,i }
)
contains a basis of
span{π ∈ Irr(X ⋊W′) |c is the central character of π} ⊂ GQ(X ⋊W′),
for all generic points c ∈ C. This procedure yields analytic d-dimensional families
whose span in GQ(H ⋊ Γ) is mapped bijectively to Gd
Q(X ⋊W′)
/
Gd+1
Q (X ⋊W′) by
ζ∨. By (35) we may take the parameters for πσw,i in T σw,i/Gσw,i , when we consider
these representations in G(H ⋊ Γ). Let us list some properties of
{πσw,i (t) |w ∈ ⟨W′⟩, 1 ≤i ≤c(w),t ∈T σw,i/Gσw,i }. (42)
Lemma 2.3. (a) The parameter space T σw,i/Gσw,i is isomorphic to T w
i /ZW ′(w), as
orbifolds.
(b) πσw,i (t) and πσw,i (t′) have the same trace if and only if t and t′ lie in the same
Gσw,i -orbit.
(c) The family of representations (42) contains no repetitions and forms a basis of
GQ(H ⋊ Γ) .
Proof. By the above construction and since diﬀerent w ∈W′ act diﬀerently on T ,
ζ∨(
Gd+1
Q (H ⋊ Γ)
)
+ζ∨(
span{πσw,i (t) |t ∈T σw,i }
)
=
ζ∨(
Gd+1
Q (X ⋊W′)
)
+ζ∨(
span{πw(t) |t ∈T w
i /ZW ′(w)}
)
.
Hence the parameter space T w
i /ZW ′(w) is diﬀeomorphic to T σw,i modulo the equiv-
alence relation
t ∼t′ ⇐ ⇒πσw,i (t) = πσw,i (t′) in GQ(H ⋊ Γ).
By Theorem 2.1.bt ∼t′ if and only if there exists a g ∈ G withg(P,δ,ut ) = (P,δ,ut′),
where πσw,i is a direct summand of π(P,δ,u ). By deﬁnition any g ∈ G σw,i yields
such equivalences for all t ∈T σw,i , so T σw,i/ ∼ is a quotient of T σw,i/Gσw,i . On the
other hand, elements h ∈ G (P,δ) \ Gσw,i can only produce such equivalences on lower
dimensional subsets of T σw,i . But any such relation which does not already come
from Gσw,i would destroy the orbifold structure of T σw,i/Gσw,i , so
T w
i /ZW ′(w) ∼
=T σw,i/ ∼ ∼
=T σw,i/Gσw,i.
This proves (a) and since we work in GQ(H ⋊ Γ), it also implies (b).
We noted that (40) contains no repetitions and is a basis of GQ(X ⋊W′). Since
the collection of analytic families
{ζ∨(πσw,i (t)) |t ∈w ∈ ⟨W′⟩, 1 ≤i ≤c(w),t ∈T σw,i/Gσw,i }
is parametrized by the same space ˜T/W′, it also enjoys these properties. As ζ∨ is
bijective, these two properties already hold for (42) in GQ(H ⋊ Γ). ✷
20
