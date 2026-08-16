---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of aﬃne Hecke algebras Maarten Solleveld Radboud Universiteit Nijmegen"
section_id: sec-010-33-schwartz-algebras
section_title: "Schwartz algebras"
section_number: 3.3
pages: 32-38
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
doc_brief: "Hochschild homology of affine Hecke algebras Maarten Solleveld Radboud Universiteit Nijmegen — Let H = H(R,q ) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not"
---
In this section we will compute the Hochschild homology of th e Schwartz completion
S ⋊ Γ of an (extended) aﬃne Hecke algebra H ⋊ Γ with positive parameters q. It
turns out that there is a clear relation between HH∗(S ⋊Γ) and HH∗(H⋊Γ), similar
to the relation between C∞(S1) and O(C×) ∼
= C[z,z−1].
To get the correct answer we must take the topology of S ⋊ Γ into account. The
best way to do so is with complete bornological algebras [Mey ] and bornological
tensor products, which we will denote by ˆ⊗. Thus HH∗(S ⋊ Γ) is the homology of
the diﬀerential complex
(
(S ⋊ Γ) ˆ⊗n+1,b n
)
. It is isomorphic to
TorS⋊Γ ˆ⊗(S⋊Γ) op
∗ (S ⋊ Γ, S ⋊ Γ),
computed in the category of complete bornological S ⋊ Γ-bimodules.
We will use the notation from (42). By Theorem 1.5 the evaluat ion map
H ⋊ Γ → O (T σw,i ) ⊗ EndC(Vσw,i )
extends to a homomorphism of Fr´ echet algebras
S ⋊ Γ →C∞(T σw,i
un ) ⊗ EndC(Vσw,i ).
Applying this to all w and i yields a homomorphism
˜σun : S ⋊ Γ →
⨁
w∈⟨W ′⟩
c(w)⨁
i=1
C∞(T σw,i
un ) ⊗ EndC(Vσw,i ) (66)
which extends (63). Recall that by the topological version o f the Hochschild–
Kostant–Rosenberg Theorem
HH∗(C∞(Tun)) ∼
= Ω∗
sm(Tun),
the algebra of smooth complex valued diﬀerential forms on the real manifold Tun.
Hence (66), like ˜σ, induces a C-linear map
HH∗(˜σun) : HH∗(S ⋊ Γ) →
⨁
w∈⟨W ′⟩
c(w)⨁
i=1
Ω∗
sm(T σw,i
un )Gσw,i. (67)
It becomes Z(S ⋊ Γ)-linear if we write cc(σw,i)T σw,i
un instead of T σw,i
un and interpret
the Z(S ⋊ Γ)-action accordingly.
Theorem 3.6. Let q be positive. The map (67) is an isomorphism of Z(S ⋊ Γ) -
modules and it extends Theorem 3.4.
32
Proof. Since eP,δ ∈ S ⋊ Γ is a central idempotent,
HH n(eP,δ S ⋊ Γ) = Hn
(
(eP,δS ⋊ Γ) ˆ⊗(∗+1),b∗
) ∼
=Hn
(
eP,δS ⋊ Γ ˆ⊗S ⋊ Γ) ˆ⊗∗,b∗
)
. (68)
Forξ = (P,δ,t ) ∈ Ξ un let Fξ be the ring of formal power series on ( P,δ,T P
un) centred
at ξ. By [OpSo2, Theorem 3.5] the functor
FGP,δ
ξ ˆ⊗Z(S⋊Γ) = FGP,δ
ξ ˆ⊗eP,δ Z(S⋊Γ)
is exact on a large class of Z(S ⋊ Γ)-modules, which contains all modules that we
use here. Applying this to the right-hand side of (68) we obta in
FGP,δ
ξ ˆ⊗Z(S⋊Γ)HH n(eP,δ S ⋊ Γ) ∼
=Hn
(
FGP,δ
ξ ˆ⊗Z(S⋊Γ)eP,δ S ⋊ Γ ˆ⊗S ⋊ Γ) ˆ⊗∗,b∗
)
. (69)
It follows from a result of Borel [Tou, Remarque IV.3.5] that the Taylor series map
eP,δZ(S ⋊ Γ) ∼
=C∞(T P
un)GP,δ → FGP,δ
ξ
is surjective, and (by deﬁnition) its kernel I∞
ξ consists of all functions that are ﬂat
at ξ. Clearly the Z(S ⋊ Γ)-action on (69) factors through FGP,δ
ξ , so I∞
ξ annihilates
(69). Together with Lemma 1.6 this shows that (69) is isomorp hic to
Hn
(
(FGP,δ
ξ ˆ⊗Z(S⋊Γ)eP,δ S⋊Γ) ˆ⊗(∗+1),b∗
) ∼
=Hn
(
(FGP,δ
ξ ⊗eP,δ Z(H⋊Γ)eP,δH⋊Γ) ˆ⊗(∗+1),b∗
)
=HH n
(
FGP,δ
ξ ⊗eP,δ Z(H⋊Γ) eP,δH ⋊ Γ
)
. (70)
Let pr : Ξ → T/W′ be the projection that sends ξ to the Z(H ⋊ Γ)-character of
the representation πΓ (ξ). With (29) and Lemma 2.3.c we can associate to every
tempered analytic family of H ⋊ Γ-representations a unique ( P,δ ) ∈ P . In the
notation of (42) we write σw,i ≺ (P,δ ) if πσw,i (t)(eP,δ ) ⁄= 0 for any t ∈T P
un.
If we want to apply the algebra homomorphism ˜ σ (or ˜σun, that comes down to
the same thing) to FGP,δ
ξ ⊗eP,δ Z(H⋊Γ) eP,δ H ⋊ Γ, we must replace the target by
FGP,δ
ξ ⊗eP,δ Z(H⋊Γ)
⨁
w∈⟨W ′⟩
c(w)⨁
i=1
O(T σw,i ) ⊗ EndC(Vσw,i )
=
⨁
σw,i≺(P,δ)
ˆO(T σw,i )pr(ξ) ⊗ EndC(Vσw,i ).
Let us denote the resulting algebra homomorphism by ˜ σξ. It induces a morphism
C∗(˜σξ) on Hochschild complexes, whose composition with the gener alized trace map
gtr lands in a sum of Gσw,i -invariant subcomplexes:
gtr ◦C∗(˜σξ) : C∗
(
FGP,δ
ξ ⊗eP,δ Z(H⋊Γ) eP,δ H ⋊ Γ
)
→
⨁
σw,i≺(P,δ)
C∗
( ˆO(T σw,i )pr(ξ)
) Gσw,i.
(71)
33
More precisely, the image of gtr ◦C∗(˜σξ) is the same as the formal completion of
⨁
σw,i≺(P,δ)
gtr ◦C∗(˜σ)w,i
(
C∗(H ⋊ Γ)
)
at ξ. Since gtr ◦C∗(˜σ) is a quasi-isomorphism (by Theorem 3.4), and since
H ⋊ Γ ↦→ FGP,δ
ξ ⊗eP,δ Z(H⋊Γ) eP,δH ⋊ Γ
just has the eﬀect of formally completing at pr( ξ) and forgetting all analytic families
with σw,i ⁄≺(P,δ ), (71) is also a quasi-isomorphism. Thus ˜ σξ induces
HH n
(
FGP,δ
ξ ⊗eP,δ Z(H⋊Γ) eP,δ H ⋊ Γ
) ∼
=
⨁
σw,i≺(P,δ)
ˆΩ∗(T σw,i )
Gσw,i
pr(ξ).
By (70), (69) and (68) this means that, for all ξ = (P,δ,t ) ∈ Ξ un, ˜σ induces an
isomorphism
FGP,δ
ξ ⊗eP,δ Z(S⋊Γ) HH n
(
eP,δS ⋊ Γ
) ∼
=
⨁
σw,i≺(P,δ)
ˆΩ∗(T σw,i )
Gσw,i
pr(ξ).
In other words, the homomorphism of Z(S ⋊ Γ)-modules (67) becomes an iso-
morphism upon formally completing with respect to any close d maximal ideal of
Z(S ⋊ Γ). Now the same argument as in the proof of Lemma 1.6 shows tha t (67) is
itself an isomorphism. ✷
The following consequence of Theorem 3.6 can be proved in the same way as
Corollaries 3.2 and 3.5.
Corollary 3.7. The algebra homomorphism ˜σun induces isomorphisms
HC∗(˜σun) : HC∗(S ⋊ Γ) → ⨁
w∈⟨W ′⟩
c(w)⨁
i=1
HC∗(C∞(T σw,i
un ))Gσw,i,
HP ev/odd(˜σ) : HP ev/odd(S ⋊ Γ) → ⨁
w∈⟨W ′⟩
c(w)⨁
i=1
H ev/odd
DR (T σw,i
un )Gσw,i ∼
=H ev/odd
DR ( ~Tun)W ′
.
3.4 Comparison of diﬀerent parameters
Let k be real valued and let q be positive. We will investigate what happens to the
homology of the algebras H( ˜R,k ) ⋊ Γ, H(R,q ) ⋊ Γ and S(R,q ) ⋊ Γ when we replace
k by ǫk (ǫ ∈ C×) and q by qǫ (ǫ ∈ C \iR). For the Schwartz algebras we must of
course take ǫ real.
Recall the analytic families of representations πσw,i from Lemma 2.3 and πρw
from Corollary 2.5. As discussed in the proof Theorem 2.6, ad justing the parameter
function by ǫ corresponds to applying m∗
ǫ to σw,i and ρw. Let
H( ˜R,ǫk ) ⋊ Γ → O (tρw ) ⊗ EndC(V Γ
ρw ),
H(R,q ǫ) ⋊ Γ → O (T σw,i ) ⊗ EndC(V Γ
σw,i ),
S(R,q ) ⋊ Γ → C∞(T σw,i
un ) ⊗ EndC(V Γ
σw,i )
34
be the corresponding algebra homomorphisms. By Theorems 3. 1, 3.4 and 3.6 these
induce isomorphisms
HH∗(H( ˜R,ǫk ) ⋊ Γ) →
⨁
w∈⟨W ′⟩
Ω∗(tρw )Gρw ∼
=
⨁
w∈⟨W ′⟩
Ω( tw)ZW ′ (w),
HH∗(H(R,q ǫ) ⋊ Γ) →
⨁
w∈⟨W ′⟩
c(w)⨁
i=1
Ω∗(T σw,i )Gσw,i ∼
=
⨁
w∈⟨W ′⟩
Ω∗(T w)ZW ′ (w),
HH∗(S(R,q ǫ) ⋊ Γ) →
⨁
w∈⟨W ′⟩
c(w)⨁
i=1
Ω∗
sm(T σw,i
un )Gσw,i ∼
=
⨁
w∈⟨W ′⟩
Ω∗
sm(T w
un)ZW ′ (w).
The action of Z(H( ˜R,ǫk ) ⋊ Γ) ∼
= O(t)W ′
on Ω∗(tρw ) is via the embedding
tρw → t :λ ↦→cc(m∗
ǫ (ρw)) +λ =ǫcc (ρw) +λ.
The translation factor cc(m∗
ǫ (ρw)) ∈ t is a representative for the central character
of m∗
ǫ (ρw). Similarly, the actions of Z(H(R,q ǫ) ⋊ Γ) ∼
= O(T )W ′
on Ω∗(T w) and on
Ω∗
sm(T w
un) go via the embedding
T σw,i →T :t ↦→cc(m∗
ǫ (σw,i))t.
Herecc(m∗
ǫ (σw,i)) ∈Tun is a representative for the central character of σw,i, and by
(46) it lies in Y ⊗S1qǫZ/2.
Now we will generalize these results to the case ǫ = 0. Recall the maps
ζ∨ :G
(
H( ˜R,ǫk
)
⋊ Γ
)
→G
(
S(t∗) ⋊ Γ
)
from Theorem 2.4 and
ζ∨ :G
(
H(R,q ǫ) ⋊ Γ
)
→G
(
C[X] ⋊W′)
from Theorem 2.6. These maps send analytic families to other analytic families,
because they commute with parabolic induction.
Theorem 3.8. (a) Let k be real valued and let ǫ ∈ C×. There exists a unique
isomorphism
HH∗(ζ∨) : HH∗(S(t∗) ⋊W′) →HH∗(H( ˜R,ǫk ) ⋊ Γ)
such that
HH∗(πρ) ◦HH∗(ζ∨) = HH∗(ζ∨(πρ))
for all analytic families of H( ˜R,ǫk ) ⋊ Γ -representations {πρ(λ) |λ ∈ tρ}.
(b) Letq be positive and let ǫ ∈ C \iR. There exists a unique isomorphism
HH∗(ζ∨) : HH∗(C[X] ⋊W′) →HH∗(H(R,q ǫ) ⋊ Γ)
such that
HH∗(πσ) ◦HH∗(ζ∨) = HH∗(ζ∨(πσ))
for all analytic families of H(R,q ǫ) ⋊ Γ -representations {πσ(t) |t ∈T σ}.
35
(c) Letq be positive. There exists a unique isomorphism
HH∗(ζ∨) : HH∗(S(X) ⋊W′) →HH∗(S(R,q ) ⋊ Γ)
such that
HH∗(πσ) ◦HH∗(ζ∨) = HH∗(ζ∨(πσ))
for all analytic families of S(R,q ) ⋊ Γ -representations {πσ(t) |t ∈T σ
un}.
In all three settings the analogous statements for cyclic and periodic cyclic homology
are also valid.
Proof. We will only prove (a), the other parts follow in the same way. The
construction of the πρw and the proof of Lemma 2.3 show that the analytic families
{ζ∨(πρw (λ)) |w ∈ ⟨W′⟩,λ ∈ tρw } (72)
fulﬁll Corollary 2.5 for H( ˜R, 0)⋊Γ = S(t∗)⋊W′. We remark that the representations
(72) can be reducible, even for generic λ. But since this does not aﬀect the arguments
in Section 3.1, we may ignore it. In particular Theorem 3.1 ho lds for S(t∗) ⋊W′
with (72). Now the condition of the theorem enforces that HH∗(ζ∨) is the composite
isomorphism
HH∗(S(t∗) ⋊W′) − →
⨁
w∈⟨W ′⟩
Ω∗(tρw )W ′
ρw
HH ∗(˜ρ)−1
− − − − − − − →HH∗(H( ˜R,ǫk ) ⋊ Γ).
For all w ∈ ⟨W′⟩ this map satisﬁes
HH∗(πρw ) ◦HH∗(ζ∨) = HH∗(ζ∨(πρw )).
Thus it remains to check compatibility with an arbitrary ana lytic family of H( ˜R,ǫk )⋊
Γ-representations {πρ(λ) |λ ∈ tρ}. Let λ be a generic point of tρ. By Corollary 2.5.c
we can ﬁnd nρ ∈ N,n w ∈ Z and µw,λ ∈ tρw such that
nρπρ(λ) =
∑
w∈⟨W ′⟩
nwπρw (µw,λ) in G
(
H( ˜R,ǫk ) ⋊ Γ
)
. (73)
The genericity of λ implies nw = 0 unless W′tρw ⊃ W′tρ. Comparing the central
characters also shows that there exist ˜w ∈W′ with
˜λ +cc(πρ(0)) = µw,λ +cc(πρw (0)),
for suitable representatives cc(π) of the central character of the representations π
under consideration. Hence we may take
µw,λ = ˜wλ +cc(πρ(0)) −cc(πρw (0)) =: ˜λ +µw.
Sinceλ was generic, with this choice of µw,λ (73) becomes valid for all generic λ ∈ tρ,
which then by continuity extends to the whole of tρ. Next we bring the terms nw < 0
to the other side and obtain
nρπρ(λ) +
∑
w∈⟨W ′⟩−
−nwπρw (˜λ +µw) =
∑
w∈⟨W ′⟩+
nwπρw (˜λ +µw).
36
This is an equality in G(H( ˜R,ǫk ) ⋊ Γ), but the representations on the both sides
need not be isomorphic. Since Hochschild homology does not d istinguish direct sums
from nontrivial extensions [Lod, Theorem 1.2.15], we may ne vertheless treat it as an
equivalence of H( ˜R,k ) ⋊ Γ-representations. Consequently
nρHH∗(πρ) +
∑
w∈⟨W ′⟩−
−nwHH∗(πρw )
⏐
⏐
µw+ ˜wtρ =
∑
w∈⟨W ′⟩+
nwHH∗(πρw )
⏐
⏐
µw+ ˜wtρ
as maps
HH∗
(
H( ˜R,ǫk ) ⋊ Γ
)
→HH∗(O(tρ)) ∼
= Ω∗(tρ).
Now he aforementioned compatibility of HH∗(ζ∨) with the πρw and the additivity
of ζ∨ show that
HH∗(πρ) ◦HH∗(ζ∨) = HH∗(ζ∨(πρ)),
as required. The analogous statements for (periodic) cycli c homology can be proved
in the same way, using Corollary 3.2. ✷
In [Sol3, Theorem 4.4.2] the author constructed a homomorph ism of Fr´ echet
algebras
ζ0 : S(X) ⋊W′ → S (R,q ) ⋊ Γ.
It is related to Theorem 2.2 by [Sol3, Corollary 4.4.3]: ζ∨(π) ∼
=π◦ζ0 for all irreducible
S(R,q ) ⋊ Γ-representations. Furthermore it was shown in [Sol3, Theo rems 5.1.4 and
5.2.1] that ζ0 induces isomorphisms on topological K-theory and on periodic cyclic
homology. With Theorem 3.8 we can improve on this:
Proposition 3.9. Letq be positive.
(a) HH∗(ζ0) = HH∗(ζ∨) : HH∗(S(X) ⋊W′) →HH∗(S(R,q ) ⋊ Γ) .
(b) There exists a natural commutative diagram
HH∗(C[X] ⋊W′) → HH∗(S(X) ⋊W′)
↓HH ∗(ζ ∨) ↓HH ∗(ζ0)
HH∗(H(R,q ) ⋊ Γ) → HH∗(S(R,q ) ⋊ Γ)
in which the horizontal maps are induced by inclusions of alg ebras and the ver-
tical maps are isomorphisms.
(c) The analogues of (a) and (b) for cyclic and periodic cyclic hom ology are also
valid.
Proof. By [Sol3, Lemma 4.2.3 and Theorem 4.4.2.e]
πσ(t) ◦ζ0 =ζ∨(πσ(t))
for every tempered analytic family of H(R,q ) ⋊ Γ-representations {πσ(t) |t ∈T σ
un}.
Thus (a) follows from the unicity part of Theorem 3.8.c. That and Theorem 3.8
directly imply (b) and (c). ✷
37
