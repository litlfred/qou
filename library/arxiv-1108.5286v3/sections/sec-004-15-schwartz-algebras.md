---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of aﬃne Hecke algebras Maarten Solleveld Radboud Universiteit Nijmegen"
section_id: sec-004-15-schwartz-algebras
section_title: "Schwartz algebras"
section_number: 1.5
pages: 12-16
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
doc_brief: "Hochschild homology of affine Hecke algebras Maarten Solleveld Radboud Universiteit Nijmegen — Let H = H(R,q ) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not"
---
An important tool to study H-representations is restriction to the commutative
subalgebra A ∼
= O(T ). We say that t ∈T is a weight of ( π,V ) if there exists a v ∈
V \ {0} such that π(a)v =a(t)v for all a ∈ A . Temperedness of H-representations,
which is deﬁned via A-weights, is analogous to temperedness of representations of
reductive groups. Via the Langlands classiﬁcation for aﬃne Hecke algebras [Sol3,
Section 2.2] these representations are essential in the cla ssiﬁcation of irreducible
representations.
The antidual of a∗+ := {x ∈ a∗ | ⟨x, α∨⟩ ≥ 0 ∀α ∈ ∆ } is
a− = {λ ∈ a | ⟨x, λ⟩ ≤ 0 ∀x ∈ a∗+} =
{ ∑
α∈∆
λαα∨ |λα ≤ 0
}
. (25)
The interior a−− of a− equals
{∑
α∈∆ λαα∨ | λα < 0
}
if ∆ spans a∗, and is empty
otherwise. We write T− = exp(a−) and T−− = exp(a−−).
12
Lett = |t|·t|t|−1 ∈Trs ×Tun be the polar decomposition of t. A ﬁnite dimensional
H-representation is called tempered if |t| ∈ T− for all its A-weights t, and anti-
tempered if |t|−1 ∈T− for all such t.
We say that an irreducible H-representation belongs to the discrete series (or
simply: is discrete series) if all its A-weights lie in T−−Tun. In particular the
discrete series is empty if ∆ does not span a∗. The discrete series is a starting point
for the construction of irreducible representations: they can all be realized as a
subrepresentation of the induction of a discrete series rep resentation of a parabolic
subalgebra of H. The notions tempered and discrete series apply equally wel l to
H ⋊ Γ, since that algebra contains A and the action of Γ on T preservesT−.
This terminology also extends naturally to graded Hecke alg ebras, via the S(t∗)-
weights of a representation. Thus we say that a ﬁnite dimensi onal H⋊Γ-representation
is tempered if all its S(t∗)-weights lie in a− +ia and we say that it is discrete series
if it is irreducible and all its S(t∗)-weights lie in a−− +ia. By construction Lusztig’s
two reduction theorems from Section 1.4 preserve the proper ties temperedness and
discrete series.
Proposition 1.4. LetP ⊂ ∆ .
(a) Let σ be a ﬁnite dimensional HP ⋊ Γ P -representation. For t ∈T P the H ⋊ Γ -
representation IndH⋊Γ
HP ⋊Γ P
(σ ◦φt) is tempered if and only if t ∈ T P
un and σ is
tempered.
(b) Let ρ be a ﬁnite dimensional HP ⋊ Γ P -representation. For λ ∈ tP the H ⋊ Γ -
representation IndH⋊Γ
HP ⋊Γ P (ρ ◦φλ) is tempered if and only if λ ∈ iaP and ρ is
tempered.
Proof. For (a) see [Sol3, Lemma 3.1.1.b] and for (b) see [Sol2, Lemma 2.2]. ✷
Now we will recall the construction of the Schwartz algebra S of an aﬃne Hecke
algebra [DeOp], which we will use in Section 3.3. For this we a ssume that the
parameter function q is positive, because otherwise there would not be a good link
with C∗-algebras. As a topological vector space S will consist of rapidly decreasing
functions on W e, with respect to a suitable length function N . For example we can
take a W -invariant norm on X ⊗Z R and put N (wtx) = ‖x‖ forw ∈W and x ∈X.
Then we can deﬁne, for n ∈ N, the following norm on H:
pn
( ∑
w∈W e
hwNw
)
= sup
w∈W e
|hw|(N (w) + 1)n.
The completion of H with respect to these norms is the Schwartz algebra S =
S(R,q ). It is known from [Opd, Section 6.2] that it is a Fr´ echet alg ebra. Diagram
automorphisms of R induce automorphisms of S, so the crossed product algebra
S⋊Γ is well-deﬁned. By [Opd, Lemma 2.20] a ﬁnite dimensional H⋊Γ-representation
is tempered if and only if it extends continuously to an S ⋊ Γ-representation.
Next we describe the Fourier transform for H and S. An induction datum for H
is a triple ( P,δ,t ), with P ⊂ ∆ ,t ∈T P andδ a discrete series representation of HP .
13
A large part of the representation theory of H is built on the parabolically induced
representations
π(P,δ,t ) = IndH
HP (δ ◦φt) and πΓ (P,δ,t ) = IndH⋊Γ
HP (δ ◦φt).
Let Ξ be the space of all such induction data ( P,δ,t ), with δ up to equivalence of
HP -representations. It carries a natural structure of a compl ex aﬃne variety with
ﬁnitely many components of diﬀerent dimensions. Furthermor e Ξ has a compact
submanifold
Ξ un :=
{
(P,δ,t ) ∈ Ξ |t ∈T P
un
}
,
which is a disjoint union of ﬁnitely many compact tori.
Given a discrete series representation ( δ,V δ) of a parabolic subalgebra HP of
H, the H ⋊ Γ-representation πΓ (P,δ,t ) can be realized on the vector space V Γ
δ :=
C[ΓW P ] ⊗Vδ, which does not depend on t ∈ T P . Here W P is a speciﬁed set of
representatives for W/W (RP ). Let V Γ
Ξ be the vector bundle over Ξ whose ﬁber at
ξ = (P,δ,t ) is V Γ
δ , and let
O(Ξ; End( V Γ
Ξ )) :=
⨁
P,δ
O(T P ) ⊗ EndC(V Γ
δ )
be the algebra of polynomials sections of the endomorphism b undle End( V Γ
Ξ ). The
Fourier transform for H ⋊ Γ is
F : H ⋊ Γ → O (Ξ; End( V Γ
Ξ )),
F(h)(ξ) = πΓ (ξ)(h).
It extends to an algebra homomorphism
F : S ⋊ Γ →C∞(Ξ un; End(V Γ
Ξ )) :=
⨁
P,δ
C∞(T P
un) ⊗ EndC(V Γ
δ ), (26)
deﬁned by the same formula.
We will need a groupoid G over the power set of ∆, deﬁned as follows. For
P,Q ⊂ ∆ the collection of arrows from P to Q is
GP Q = {(g,u ) ∈ Γ ⋉W ×KP |g(P ) = Q}.
Whenever it is deﬁned, the multiplication in G is
(g′,u′) · (g,u ) = (g′g,g−1(u)u′).
This groupoid acts from the left on Ξ by
(g,u )(P,δ,t ) =
(
g(P ),δ ◦ψ−1
u ◦ψ−1
g ,g (ut)
)
. (27)
This is the projection of an action of G on parabolically induced representations via
intertwining operators. These operators provide an action of G onC∞(Ξ un; End(V Γ
Ξ )),
see [Opd, Theorem 4.33] and [Sol3, (3.16)]. The Plancherel i somorphism for (ex-
tended) aﬃne Hecke algebras with positive parameters reads :
14
Theorem 1.5. The Fourier transform F induces an isomorphism of Fr´ echet alge-
bras
S ⋊ Γ →C∞(Ξ un; End(V Γ
Ξ ))G.
Proof. See [DeOp, Theorem 5.3] and [Sol3, Theorem 3.2.2]. ✷
From this isomorphism we see in particular that there are uni que central idem-
potents eP,δ ∈ S ⋊ Γ such that
eP,δ S ⋊ Γ ∼
=
(
C∞(T P
un) ⊗ EndC(V Γ
δ )
) GP,δ,
GP,δ :=
{
g ∈ G | g(P,δ,T P
un) = (P,δ,T P
un)
}
.
(28)
For a suitable collection P of pairs (P,δ ) we obtain decompositions
S ⋊ Γ =
⨁
(P,δ)∈P
eP,δ S ⋊ Γ,
Z(S ⋊ Γ) =
⨁
(P,δ)∈P
C∞(T P
un)GP,δ.
(29)
Via (28) the subalgebra eP,δH⋊Γ of S ⋊Γ is isomorphic to a subalgebra of
(
O(T P )⊗
EndC(V Γ
δ )
) GP,δ . We note that eP,δZ(H ⋊ Γ) is isomorphic to the restriction of Z(H ⋊
Γ) ∼
= O(T )W ′
to the image of ( P,δ,T P
un) in T/W′. We will see from Lemma 2.3 that
it is just O(T P )GP,δ .
Clearly eP,δ H ⋊ Γ is dense in eP,δS ⋊ Γ, so for any closed ideal I ⊂eP,δS ⋊ Γ of
ﬁnite codimension the canonical maps
eP,δ H ⋊ Γ/
(
I ∩eP,δH ⋊ Γ
)
→
(
eP,δ H ⋊ Γ + I
)
/I →eP,δ S ⋊ Γ/I (30)
are isomorphisms of eP,δH ⋊ Γ-modules.
Lemma 1.6. The multiplication map
µP,δ :eP,δZ(S ⋊ Γ) ⊗eP,δ Z(H⋊Γ) eP,δ H ⋊ Γ →eP,δS ⋊ Γ
is an isomorphism of eP,δZ(S ⋊ Γ) -modules.
Proof. ClearlyµP,δ iseP,δZ(S ⋊ Γ)-linear. By Theorem 1.5 eP,δ S ⋊ Γ is of ﬁnite
rank over eP,δZ(S ⋊ Γ) and we know that eP,δH ⋊ Γ is dense in eP,δS ⋊ Γ. Thus the
image of µP,δ is closed and dense in eP,δ S ⋊ Γ, which means that µP,δ is surjective.
Let Iξ be the maximal ideal of eP,δZ(S ⋊ Γ) ∼
= C∞(T P
un)GP,δ corresponding to
ξ = (P,δ,t ). Applying (30) to I n
ξeP,δ S ⋊ Γ we see that µP,δ induces isomorphisms
eP,δZ(S ⋊ Γ)/In
ξ ⊗eP,δZ(H⋊Γ) eP,δ H ⋊ Γ →eP,δS ⋊ Γ/In
ξ (eP,δ S ⋊ Γ), (31)
for all n ∈ Z>0. Consider any x ∈ kerµP,δ. Its annihilator Ann( x) is a closed ideal of
eP,δZ(S ⋊ Γ) and eP,δZ(S ⋊ Γ)x ∼
=eP,δZ(S ⋊ Γ)/Ann(x). By (31) I n
ξ/In
ξ Ann(x) = 0
for allξ ∈ (P,δ,T P
un). Therefore Ann(x) is not contained in any of the closed maximal
ideals Iξ. Consequently Ann( x) = eP,δZ(S ⋊ Γ) and x = 0. ✷
15
