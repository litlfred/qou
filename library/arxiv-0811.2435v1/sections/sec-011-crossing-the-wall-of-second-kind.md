---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic"
section_id: sec-011-crossing-the-wall-of-second-kind
section_title: "Crossing the wall of second kind"
section_number: null
pages: 30-33
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
Here we will interpret the parallel transport in a diﬀerent w ay, introducing
a wall of another kind. We use the notation from the previous s ection. In
particular, we ﬁx the quadratic form Q0 and the connected component U of
the set{Z∈ Hom(Γ, C)| (Q0)| KerZ < 0}.
For a given primitive γ ∈ Γ \{ 0} we introduce the set WQ0
γ ={Z ∈
U|Z(γ)∈ R>0}. It is a hypersurface in U. We call it a wall of second kind
associated with γ. We call the union ∪γWQ0
γ the wall of second kind and
denote it by W2.
Deﬁnition 4 We say that a path σ = (Zt)0≤t≤1⊂ U is short if the convex
coneCσ which is the convex hull of
(
∪0≤t≤1Z−1
t (R>0)
)
∩{Q0 /greaterorequalslant0} is strict.
With a short path we associate a pro-nilpotent group GCσ with the Lie
algebra gCσ =∏
γ∈Cσ∩Γ gγ.
The following result is obvious.
Proposition 3 For a generic short path σ = (Zt)0≤t≤1 there exists no more
than countable set ti∈ [0, 1] and corresponding primitive γi∈ Γ \{ 0} such
that Zti∈W Q0
γi . For each i we have: rkZ−1
ti (R)∩ Γ = 1 .
30
Let us recall the continuous lifting mapφ :U→Stab(g) from the previous
section. In the notation of the previous Proposition we deﬁn e for any ti a
group element
Ati = exp
(
εi
∑
n/greaterorequalslant1
ati(nγi)
)
∈GCσ ,
where εi =±1 depending on the direction in which the path Zt(γi) crosses
R>0 for t suﬃciently close to ti.
Theorem 4 For any short loop the monodromy∏ −→
ti Ati is equal to the iden-
tity (here the product is taken in the increasing order of the elements ti).
Proof. Here we also present a sketch of the proof. Similarly to the pr oof
of the Theorem 3 we consider the case of inﬁnitesimally small loop σ around
a point Z such that rk Γ 2 = 2 where Γ 2 := Z−1(R)∩ Γ (i.e. Z is a point
where two, and hence inﬁnitely many, walls of second kind int ersect). Since
σ is inﬁnitesimally small we can replace Γ by Γ 2. Then we have the space
Hom(Γ 2, C)≃ R4 which contains a countable collection of walls consisting o f
thoseZ : Γ 2→ C for which there exists γ∈ Γ 2\{0} such thatQ0(γ) /greaterorequalslant0 and
Z(γ)∈ R. All the hypersurfaces contain R2 = Hom(Γ 2, R)⊂ Hom(Γ 2, C).
Factorizing by this subspace R2 we obtain a collection of lines with ratio-
nal slopes in the union of two opposite strict sectors S∪ (−S) ⊂ R2 =
Hom(Γ 2,i R).
We have to prove that the product over a loop surrounding (0 , 0) is the
identity element. But it is easy to see that the product over t he rays belonging
to each of the sectors is equal to the left (resp. right) hand s ide of the wall-
crossing formula. ■
Let us now introduce a set X1⊂ Γ ×U which consists of pairs ( γ,Z )
such that γ∈ Γ \{ 0} is a non-zero element, Q0(γ) /greaterorequalslant0,Z (γ)∈ R>0 and
Z−1(R>0)∩ Γ = ( Q>0·γ)∩ Γ.
Proposition 4 The set of continuous sections ψ : U→ Stab(g) such that
ψ(Z) is compatible with Q0 for any Z∈ U is in one-to-one correspondence
with functions ˜a :X1→ g such that ˜a(γ,Z )∈ gγ satisfying the property that
for any small loop σ the monodromy deﬁned in the previous theorem is equal
to the identity.
Proof. The bijection is given by the formula ˜ a(γ,Z ) = aψ(Z)(γ). By the
previous theorem the corresponding monodromy is trivial. C onversely, the
31
triviality of the monodromy is equivalent to the wall-cross ing formula in the
special case when a 2-dimensional sublattice of Γ is mapped b y Z into the
line R⊂ C. The general case of an arbitrary line can be reduced to this o ne
by a rotation Z↦→Ze 2πit (it does not change the values a(γ) because we do
not cross the wall of ﬁrst kind). ■
Let us also introduce a set X2⊂ Γ×U which consists of such pairs ( γ,Z )
thatQ0(γ) /greaterorequalslant0,Z (γ)> 0 and there are no non-zero Q-independent elements
γ1,γ 2∈ Γ with the property γ = γ1 +γ2,Q 0(γi) /greaterorequalslant0,Z (γi) > 0,i = 1, 2.
SinceX2 is a locally-closed hypersurface in U× Hom(Γ, C) it has ﬁnitely
many connected components. Obviously, we have X1⊂X 2.
It follows from the wall-crossing formula that for a continu ous section
ψ : U→ Stab(g) the restriction of the function a toX2 is locally-constant
and uniquely determines the section ψ. Therefore, the values of the restric-
tion a|π0(X2) provides a countable coordinate system (satisfying a count able
system of equations) on the set of continuous sections {ψ :U→Stab(g)} as
above. It can be compared with another countable coordinate system (with
no constraints) given the value ψ(Z0) for Z0 ∈ U. The latter coordinate
system is not very convenient since one has to choose a generi c Z0.
2.5 Invariants Ω( γ) and the dilogarithm
Let Γ be a free abelian group of ﬁnite rank n as before, endowed with a
skew-symmetric integer-valued bilinear form ⟨•,•⟩: Γ × Γ → Z. Recall the
Lie algebra gΓ = gΓ,⟨•,•⟩=⊕γ∈Γ Q·eγ with the Lie bracket
[eγ1,eγ2] = (−1)⟨γ1,γ2⟩⟨γ1,γ 2⟩eγ1+γ2 .
Let us introduce a commutative associative product on gΓ by the formula
eγ1eγ2 = (−1)⟨γ1,γ2⟩eγ1+γ2 .
We denote by TΓ := TΓ,⟨•,•⟩the spectrum of this commutative algebra. It is
easy to see that TΓ is a torsor over the algebraic torus Hom(Γ , Gm). Moreover
TΓ is an algebraic Poisson manifold with the Poisson bracket
{a,b} := [a,b ].
The Poisson structure on TΓ is invariant with respect to the action of Hom(Γ , Gm).
32
We can specify the results of the previous sections to the Lie algebra
gΓ . For stability data ( Z,a ) we can write uniquely (by the M¨ obius inversion
formula)
a(γ) =−
∑
n/greaterorequalslant1, 1
nγ∈Γ\{0}
Ω( γ/n)
n2 eγ ,
where Ω : Γ \{ 0}→ Q is a function. Then we have
exp
(∑
n/greaterorequalslant1
a(nγ)
)
= exp
(
−
∑
n/greaterorequalslant1
Ω( nγ)
∑
k/greaterorequalslant1
eknγ
k2
)
:= exp
(
−
∑
n/greaterorequalslant1
Ω( nγ) Li2(enγ)
)
,
where Li 2(t) =∑
k/greaterorequalslant1
tk
k2 is the dilogarithm function.
The Lie algebra gΓ acts on TΓ by Hamiltonian vector ﬁelds. Let us denote
byTγ the formal Poisson automorphism
Tγ = exp({− Li2(eγ),•}) , Tγ(eµ) = (1−eγ)⟨γ,µ⟩eµ
considered as an automorphism of algebra of functions.
More precisely for any strict convex coneC⊂ Γ R containingγ the element
Tγ acts on the formal scheme Spf (∏
µ∈Γ∩C Qeµ). Moreover Tγ is the Taylor
expansion of a birational automorphism of TΓ .
Finally, in the case when Γ comes from a 3 d Calabi-Yau category the
numbers Ω( γ) are (conjecturally) integers for ( γ,Z ) ∈ X2 in notation of
Section 2.4. They provide generalization of DT-invariants (BPS degeneracies
in physics language).
