---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-017-71-normal-states
section_title: "Normal states."
section_number: 7.1
pages: 43-46
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Normal states.
In quantum mechanics if ξ is a unit vector in a Hilbert space it deﬁnes a
"state" φ. In particular this means that if an observable is given by the
self-adjoint operator a then the average value of repeated observations of the
system in the state φ is ⟨aξ, ξ⟩. For this reason one calls a positive linear
functional φ a ”state" on a unital C∗-algebra provided φ(1) = 1.
Deﬁnition 7.1.1. If A is a C∗-algebra on H and φ is a state on A we say φ is
a vector state if there is a unit vector ξ ∈H with φ = ωξ, i.e. φ(a) = ⟨aξ, ξ⟩
for all a ∈A.
Not all states are vector states but our goal in this chapter is to show
that on von Neumann algebras there is a natural class of states which are
automatically vector states provided one ampliﬁes the Hilbert space.
Deﬁnition 7.1.2. (i) If M is a von Neumann algebra a positive linear func-
tional φ is called completely additive if
φ(
_
α
pα) =
X
α
φ(pα)
whenever pα is a family of mutally orthogonal projections.
(ii) A positive linear map Φ : A →B between von Neumann algebras is
called normal if
Φ(
_
α
aα) =
_
α
Φ(aα)
for any increasing net (aα) of self-adjoint operators in A.
Our goal in this chapter is to show the following:
43
Theorem 7.1.3. If φ is state on a von Neumann algebra M on H the fol-
lowing are equivalent:
(1) φ is normal.
(2) φ is completely additive
(3) φ is a vector state on H ⊗ℓ2(N)
(4) φ is ultraweakly continuous.
The only implication that is not obvious from what we have done is
(2) =⇒(3). To prove it we will put together some results. The ﬁrst couple
actually establish (4) =⇒(3) by 5.1.2.
Lemma 7.1.4. Let A be a C∗-algebra on H containing 1. If ψ is a positive
linear functional on A and ξ ∈H is a vector with ψ ≤ωξ (i.e. ωξ −ψ is
positive), then there is a s ∈A′ with ψ = ωsξ.
Proof. Deﬁne a sesquilinear form (, ) on Aξ by (aξ, bξ) = ψ(b∗a). Cauchy-
Schwarz and ψ ≤φξ give that |(aξ, bξ)| ≤||aξ||||bξ|| so (, ) is well-deﬁned
and there is a bounded positive operator t on Aξ with ⟨aξ, tbξ⟩= ψ(b∗a).
But ⟨aξ, tbcξ⟩= ψ(c∗b∗a) = ⟨b∗aξ, tcξ⟩= ⟨aξ, btcξ⟩so that t ∈A′ on Aξ. If
p = pAξ, tp is a positive operator in A′ and if s =
√
t, ψ(a) = ⟨aξ, tξ⟩=
⟨asξ, sξ⟩= ωξ(a).
.
Corollary 7.1.5. If ξ and η are vectors such that ω(a) = ⟨aξ, η⟩is positive
(on a C∗-algebra A on H) then there is a vector ν with ω = ων.
Proof. For a ≥0,
⟨aξ, η⟩= 1/4(⟨a(ξ + η), ξ + η⟩−⟨a(ξ −η), ξ −η⟩)
≤1/4ωξ+η(a).
Now we begin to show that complete additivity means that two states
cannot disagree too erratically.
Lemma 7.1.6. Let φ1 and φ2 be completely additive. Suppose p ∈M is a
projection and φ1(p) < φ2(p) . Then there is a projection q ≤p, for which
φ1(x) < φ2(x)
∀x ≥0 with qxq = x.
Proof. Choose a maximal family of mutually orthogonal “bad" projections
eα ≤p for which φ1(eα) ≥φ2(eα). By complete additivity W
α eα is bad so let
q = p −W
α eα. By maximality φ1(f) < φ2(f) for all projections f ≤q and
since α is norm continuous, by the spectral theorem φ1(x) < φ2(x)
∀x ≥0
with qxq = x.
44
Next we get vector state behaviour for φ on some small projection.
Lemma 7.1.7. There exists p > 0 and ξ ∈H for which
φ(x) = ⟨xξ, ξ⟩
∀x ∈pMp
Proof. Choose ξ ∈H with φ(1) = 1 < ⟨ξ, ξ⟩. Then by the previous lemma
there is a p > 0 for which φ(x) ≤⟨xξ, ξ⟩
∀x ∈pMp. By 7.1.4 we are
done.
Now we put together all the little parts and prove that (3) =⇒(4) in
7.1.3. So let φ be a completely additive state on a von Neumann algebra M
acting on H. Let pα be a maximal family of pairwise orthogonal projections
admitting a vector ξα ∈pαH with φ(x) = ⟨xξα, ξα⟩on pαMpα. Then by
the previous lemma W
α pα = 1. And obviously ||ξα||2 = φ(pα). Since φ(pα)
can only be non-zero for countably many α we can assume the set of α’s is
countable.
By Cauchy-Schwarz, for any x ∈M,
|φ(xpα)| ≤φ(pαx∗xpα)1/2φ(pα)1/2 = ||xξα||φ(pα)1/2.
So the linear functional xξα 7→φ(xpα) is well-deﬁned and bounded on
Mξα which means there is a vector ηα, ||ηα||2 = φ(pα), with
φ(xpα) = ⟨xξα, ηα⟩.
Moreover, also by Cauchy-Schwarz, |φ(x) −P
α∈F φ(xpα)| can be made
arbitrarily small by choosing the ﬁnite set F suﬃciently large since φ is
completely additive. We conclude that there exist ξα, ηα, each of norm ≤
φ(α)1/2 with
φ(x) =
X
α
⟨xξα, ηα⟩
which is the same as saying that φ(x) = ⟨(x⊗1)ξ, η⟩for some ξ, η ∈ℓ2(N, H).
By corollary 7.1.5 we have proved theorem 7.1.3.
Sadly this proof doesn’t work.
There’s a mistaken Cauchy Schwarz at
some point. The projections can not be made to add up in this way. One
needs to do a maximality argument with another Cauchy Schwarz.
Corollary 7.1.8. If φ is a normal state on the von Neumann algebra M then
the GNS representation πφ is ultraweakly continuous onto a von Neumann
algebra on Hφ.
45
Proof. We saw in the last theorem that φ(x) = ⟨x ⊗1(ν), ν⟩on H ⊗ℓ2(N).
The map x 7→x ⊗1 is ultraweakly continuous. By 6.2.8 we have that πφ
is ultraweakly continuous since the reduction to M ⊗1(ν) is ultraweakly
continuous. So the kernel of πφ is an ultraweakly closed 2-sided ideal, hence
of the form Me for some e in the centre of M. It follows that πφ is injective on
M(1−e) and since the norm of an operator x is determined by the spectrum
of x∗x, the unit ball of the image of M is the image of the unit ball which is
weakly compact so by 5.2.2 we are done.
We record a corollary that is used often without explicit mention:
Corollary 7.1.9. Let M be a von Neumann algebra and let A be a weakly
dense *-subalgebra of M generated by some self-adjoint set X. Suppose φ
is a faithful normal state on M and N is another von Neumann algebra
with faithful normal state ψ. If θ : X →N is a function, multiplicatively
extend θ to words w(x1, x2, · · · xn).
Then if ψ(w(θ(x1), θ(x2), · · · θ(xn)) =
φ(w(1, x2, · · · xn)), θ extends uniquely to a von Neumann algebra isomorphism
from M to θ(X)′′.
Proof. Faithfulness of the states φ and ψ means that the extension of θ to
linear combinations of words is a well-deﬁned *-isomorphism from A to the
*-subalgebra θ(A) of N which sends φ to ψ. This further extends to a unitary
between the GNS constructions for φ and ψ|θ(A) which intertwines the actions
of A and θ(A). We are done by 7.1.8.
