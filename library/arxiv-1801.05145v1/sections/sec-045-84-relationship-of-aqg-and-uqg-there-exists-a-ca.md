---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-045-84-relationship-of-aqg-and-uqg-there-exists-a-ca
section_title: "Relationship of Aq(g) and ~Uq(g). There exists a canonical pairing Aq(g) ×"
section_number: 8.4
pages: 63-65
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
~Uq(g) → Q(q) by
⟨ψ,xaµ⟩ =δµ,wtl(ψ)ψ(x) for any ψ ∈Aq(g), x ∈Uq(g) and µ ∈ P.
Theorem 8.4.1 ([19]). There exists a bi-crystal embedding
ιg : B(Aq(g)) − − →B( ~Uq(g))
which satisﬁes:
⟨Gup(b),ϕ (Glow(b′))⟩ =διg(b),b′
for any b ∈B(Aq(g)) and b′ ∈B( ~Uq(g)).
8.5. Relationship of Aq(g) and Aq(n).
Deﬁnition 8.5.1. Letpn : Aq(g) →Aq(n) be the homomorphism induced by U +
q (g) →
Uq(g):
⟨pn(ψ),x ⟩ =ψ(x) for any x ∈U +
q (g).
64 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
Then we have
wt(pn(ψ)) = wt l(ψ) − wtr(ψ).
It is obvious that pn sends all Φ( uwλ ⊗ur
wλ) (λ ∈ P+ and w ∈ W ) to 1. Note that
ιg(uwλ ⊗ur
wλ) = b∞ ⊗twλ ⊗b−∞ ∈B( ~Uq(g)).
Proposition 8.5.2. Forb ∈B(Aq(g)), set ιg(b) = b1 ⊗tζ ⊗b2 ∈B(∞) ⊗Tζ ⊗B(−∞) ⊂
B( ~Uq(g)) (ζ ∈ P). Then we have
pn(Gup(b)) = δb2,b −∞Gup(b1).
Proof. Set η := wt(b1) +ζ + wt(b2) = wt l(b). Then for any ˜b ∈B(∞), we have
⟨
pn(Gup(b)),ϕ (Glow(˜b))
⟩
=
⟨
Gup(b),G low(ϕ(˜b))aη
⟩
=
⟨
Gup(b),G low(b∞ ⊗tη ⊗ϕ(˜b))
⟩
=
⟨
Gup(b),ϕ (Glow(˜b ⊗tη−wt(˜b) ⊗b−∞))
⟩
=δ(ιg(b) = ˜b ⊗tη−wt(˜b) ⊗b−∞) = δ(b2 =b−∞,b 1 = ˜b). □
Hence the map pn sends the upper global basis of Aq(g) to the upper global basis of
Aq(n) or zero. Thus we have a map
pn : B(Aq(g)) →B(Aq(n))
⨆
{0}.
Although the map pn is not an algebra homomorphism, it preserves the multiplica-
tions up to a power of q, as we will see below.
Lemma 8.5.3. Forx ∈U +
q (g), if ∆ n(x) = x(1) ⊗x(2), then
∆ +(x) = qwt(x(1))x(2) ⊗x(1).(8.5)
Proof. Assume that ( 8.5) holds for x ∈U +
q (g). Note that
∆ n(eix) = (ei ⊗ 1 + 1 ⊗ei)(x(1) ⊗x(2)) = eix(1) ⊗x(2) +q−(αi,wt(x(1)))x(1) ⊗(eix(2)).
On the other hand, we have
∆ +(eix) = (ei ⊗ 1 +qαi ⊗ei)(qwt(x(1))x(2) ⊗x(1))
= (eiqwt(x1))x(2) ⊗x(1) + (qαi+wt(x(1))x(2)) ⊗(eix(1))
=q−(αi,wt(x(1)))(qwt(x(1))eix(2)) ⊗x(1) + (qwt(eix(1))x(2)) ⊗(eix(1)).
Hence ( 8.5) holds for eix. □
Proposition 8.5.4. Forψ,θ ∈Aq(g), we have
pn(ψθ) = q(wtr(ψ),wtr(θ)−wtl(θ))pn(ψ)pn(θ).
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 65
Proof. Forx ∈U +
q (g), set ∆ n(x) = x(1) ⊗x(2). Then, we have
⟨pn(ψθ),x ⟩ = ⟨ψθ,x ⟩ = ⟨ψ ⊗θ,q wt(x(1))x(2) ⊗x(1)⟩ = ⟨ψ,q wt(x(1))x(2)⟩⟨θ,x (1)⟩
=q(wtr(ψ),wt(x(1)))⟨ψ,x (2)⟩⟨θ,x (1)⟩ =q(wtr(ψ),wt(x(1)))⟨pn(ψ),x (2)⟩⟨pn(θ),x (1)⟩
=
(a)
q(wtr(ψ),wtr(θ)−wtl(θ))⟨pn(ψ) ⊗pn(θ), ∆ n(x)⟩
=q(wtr(ψ),wtr(θ)−wtl(θ))⟨pn(ψ)pn(θ),x ⟩.
Here, we used wt( x(1)) = − wt
(
pn(θ)
)
in (a). □
