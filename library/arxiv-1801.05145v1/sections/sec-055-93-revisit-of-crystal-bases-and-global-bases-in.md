---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-055-93-revisit-of-crystal-bases-and-global-bases-in
section_title: "Revisit of crystal bases and global bases. In order to prove Theorem 9.3.3"
section_number: 9.3
pages: 70-74
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
below, we ﬁrst investigate the upper crystal lattice of DϕV induced by an upper crystal
lattice of V ∈ O int(g).
LetV be a Uq(g)-module in Oint(g). Let Lup be an upper crystal lattice of V . Then
we have (see Lemma 1.3.1)
⨁
ξ∈P
q(ξ,ξ)/2(Lup)ξ is a lower crystal lattice of V .
Recall that, for λ ∈ P+, the upper crystal lattice Lup(λ) and the lower crystal lattice
Llow(λ) of V (λ) are related by
Lup(λ) = ⨁
ξ∈P
q((λ,λ)−(ξ,ξ))/2Llow(λ)ξ ⊂Llow(λ).(9.3)
Write
V ≃ ⨁
λ∈P+
Eλ ⊗V (λ)
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 71
with ﬁnite-dimensional Q(q)-vector spaces Eλ . Accordingly, we have a canonical de-
composition
Lup ≃ ⨁
λ∈P+
Cλ ⊗A0Lup(λ),
where Cλ ⊂Eλ is an A0-lattice of Eλ.
On the other hand, we have
DϕV ≃ ⨁
λ∈P+
E∗
λ ⊗V (λ).
Note that we have
ΦV ((a ⊗u) ⊗ (b ⊗v)r) = ⟨a,b ⟩Φλ(u ⊗v r) for u,v ∈V (λ) and a ∈Eλ, b ∈E∗
λ.
We deﬁne the induced upper crystal lattice DϕLup of DϕV by
DϕLup := ⨁
λ∈P+
C ∨
λ ⊗A0Lup(λ) ⊂ DϕV,
where C ∨
λ := {u ∈E∗
λ | ⟨u,Cλ⟩ ⊂ A0}. Then we have
ΦV (Lup ⊗ (DϕLup)r) ⊂Lup(Aq(g)).
Indeed, we have
DϕLup = {u ∈ DϕV | ΦV (Lup ⊗ur) ⊂Lup(Aq(g))}.
Since (Lup(λ))∨ =Llow(λ), we have
(Lup)∨ = ⨁
λ∈P+
C ∨
λ ⊗A0Llow(λ).
The properties Lup(λ) ⊂Llow(λ) and Lup(λ)λ =Llow(λ)λ imply the following lemma.
Lemma 9.3.1. D ϕLup is the largest upper crystal lattice of DϕV contained in the
lower crystal lattice (Lup)∨.
Let λ,µ ∈ P+. Then
(
Lup(λ) ⊗+Lup(µ)
) ∨
= Llow(λ) ⊗−Llow(µ) is a lower crystal
lattice of Dϕ
(
V (λ) ⊗+V (µ)
)
≃ V (λ) ⊗−V (µ). Let Ξ λ,µ : V (λ) ⊗+V (µ) ∼− →V (λ) ⊗−
V (µ) ≃ Dϕ
(
V (λ) ⊗+V (µ)
)
be the Uq(g)-module isomorphism deﬁned by
Ξλ,µ(u ⊗+v) = q(λ,µ)−(ξ,η)(
u ⊗−v
)
for u ∈V (λ)ξ and v ∈V (µ)η.
Then
~L := Ξ λ,µ
(
Lup(λ) ⊗+Lup(µ)
)
= ⨁
ξ,η∈P
q(λ,µ)−(ξ,η)Lup(λ)ξ ⊗−Lup(µ)η
is an upper crystal lattice of V (λ) ⊗−V (µ). Since we have ( λ,µ ) − (ξ,η ) ≥ 0 for any
ξ ∈ wt
(
V (λ)
)
and η ∈ wt
(
V (µ)
)
, Lemma 9.3.1 implies that
~L ⊂ Dϕ
(
Lup(λ) ⊗+Lup(µ)
)
.(9.4)
72 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
Lemma 9.3.2. Let λ,µ ∈ P+ and x1,x 2,y 1,y 2 ∈ W such that xk ≥ yk (k = 1, 2).
Then we have
(9.5)
q(λ,µ)−(x2λ,y2µ)∆(x1λ,x 2λ)∆(y1µ,y 2µ)
≡Gup(
ι−1
λ,µ(ux1λ ⊗uy1µ) ⊗ι−1
λ,µ(ux2λ ⊗uy2µ)r) mod qLup(Aq(g)).
Proof. By the deﬁnition, we have
∆(x1λ,x 2λ)∆(y1µ,y 2µ) = Φ V (λ)⊗+V (µ)
(
(ux1λ ⊗+uy1µ) ⊗(ux2λ ⊗−uy2µ)r)
.
Hence we have
q(λ,µ)−(x2λ,y2µ)∆(x1λ,x 2λ)∆(y1µ,y 2µ)
= Φ V (λ)⊗+V (µ)
(
(ux1λ ⊗+uy1µ) ⊗q(λ,µ)−(x2λ,y2µ)(ux2λ ⊗−uy2µ)r)
= Φ V (λ)⊗+V (µ)
(
(ux1λ ⊗+uy1µ) ⊗
(
Ξλ,µ(ux2λ ⊗+uy2µ)
) r)
.
The right-hand side of ( 9.5) can be calculated as follows. Let us take vk ∈Lup(λ +µ)
such thatιλ,µ(vk)−uxkλ⊗+uykµ ∈qLup(λ)⊗+Lup(µ) fork = 1, 2. Here ιλ,µ : V (λ+µ) →
V (λ) ⊗+V (µ) denotes the canonical Uq(g)-module homomorphism and such a vk exists
by Lemma 9.1.8.
Then we have
Gup
(
ι −1
λ,µ (ux1λ ⊗uy1µ) ⊗
(
ι −1
λ,µ (ux2λ ⊗uy2µ)
) r)
≡ Φλ+µ(v1 ⊗v r
2) mod qLup(Aq(g))
= Φ V (λ)⊗+V (µ)
(
ιλ,µ(v1) ⊗
(
Ξλ,µιλ,µ(v2))r)
.
The last equality follows from ( v2,u ) = (Ξ λ,µιλ,µ(v2),ιλ,µ(u)) for all u ∈V (λ +µ).
On the other hand, we have
ιλ,µ(v1) ≡ux1λ ⊗+uy1µ mod qLup(λ) ⊗+Lup(µ)
and
Ξλ,µ
(
ιλ,µ(v2)
)
≡ Ξλ,µ(ux2λ ⊗+uy2µ) mod q ~L.
Hence
ΦV (λ)⊗+V (µ)
(
(ux1λ ⊗+uy1µ) ⊗ Ξλ,µ(ux2λ ⊗+uy2µ)r)
≡ ΦV (λ)⊗+V (µ)
(
(ιλ,µ(v1) ⊗(Ξλ,µιλ,µ(v2))r)
mod qLup(Aq(g))
by ( 9.4), as desired. □
Theorem 9.3.3. Letλ ∈ P+ and x,y ∈W such that x ≥y. Then we have
D(xλ,yλ )D(yλ,λ ) ≡ D(xλ,λ ) mod qLup(Aq(n)).
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 73
Proof. Applying pn to ( 9.5), we have
D(xλ,yλ )D(yλ,λ )
≡pn
(
Gup(ι−1
λ,λ(uxλ ⊗uyλ) ⊗ι−1
λ,λ(uyλ ⊗uλ)r)
)
mod qLup(Aq(n)).
Hence the desired result follows from Proposition 8.5.2, Proposition 8.5.4 and Lemma
9.3.4 below. □
Lemma 9.3.4. Letλ ∈ P+ and x,y ∈W such that x ≥y. Then we have
ιg
(
ι −1
λ,λ (uxλ ⊗uyλ) ⊗
(
ι −1
λ,λ (uyλ ⊗uλ)
) r)
=ιλ(uxλ) ⊗tyλ+λ ⊗b−∞.
Proof. We shall argue by induction on ℓ(x). We set bxλ =ιλ(uxλ). Since the case x = 1
is obvious, assume that x ⁄= 1. Take i ∈I such that x′ :=six<x
(a) First assume thatsiy >y. Then we have y ≤x′. Hence by the induction hypothesis,
ιg
(
ι −1
λ,λ (ux′λ ⊗uyλ) ⊗
(
ι −1
λ,λ (uyλ ⊗uλ)
) r)
=bx′λ ⊗tyλ+λ ⊗b−∞.(9.6)
We haveϕi(ux′λ) = ⟨hi,x ′λ⟩ andϕi(bx′λ ⊗tyλ+λ ⊗b−∞) = ϕi(bx′λ ⊗tyλ+λ) = ⟨hi,x ′λ⟩+
⟨hi,yλ ⟩ ≥ ⟨hi,x ′λ⟩. Hence, applying ˜f ⟨hi,x′λ⟩
i to (
9.6), we obtain
ιg
(
ι −1
λ,λ (uxλ ⊗uyλ) ⊗
(
ι −1
λ,λ (uyλ ⊗uλ)
) r)
=bxλ ⊗tyλ+λ ⊗b−∞.
(b) Assume that y′ :=siy < y. Then we have y′ ≤ x′, and the induction hypothesis
implies that
ιg
(
ι −1
λ,λ (ux′λ ⊗uy′λ) ⊗
(
ι −1
λ,λ (uy′λ ⊗uλ)
) r)
=bx′λ ⊗ty′λ+λ ⊗b−∞.
Apply ˜e∗ ⟨hiy′λ⟩
i ˜f ⟨hi,x′λ+y′λ⟩
i to the both sides. Then the left-hand side yields
ιg
(
ι −1
λ,λ (uxλ ⊗uyλ) ⊗
(
ι −1
λ,λ (uyλ ⊗uλ)
) r)
.
Since ϕi(bx′λ ⊗ty′λ+λ) = ⟨hi,x ′λ⟩ + ⟨hi,y ′λ +λ⟩ ≥ ⟨hi,x ′λ +y′λ⟩, the right-hand side
yields
˜e∗ ⟨hi,y′λ⟩
i ˜f ⟨hi,x′λ+y′λ⟩
i
(
bx′λ ⊗ty′λ+λ ⊗b−∞
)
= ˜e∗ ⟨hi,y′λ⟩
i
(
( ˜f ⟨hi,x′λ+y′λ⟩
i bx′λ) ⊗ty′λ+λ ⊗b−∞
)
= ˜e∗ ⟨hi,y′λ⟩
i
(
( ˜f ⟨hi,y′λ⟩
i bxλ) ⊗ty′λ+λ ⊗b−∞
)
.
Since ε∗
i (bxλ) = −ϕi(bxλ) = ⟨hi,λ ⟩ and ˜f ⟨hi,y′λ⟩
i bxλ = ˜f ∗ ⟨hi,y′λ⟩
i bxλ, we have
˜e∗ ⟨hi,y′λ⟩
i
(
( ˜f ⟨hi,y′λ⟩
i bxλ) ⊗ty′λ+λ ⊗b−∞
)
=bxλ ⊗tyλ+λ ⊗b−∞. □
74 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
