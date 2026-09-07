---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-046-81-quantum-coordinate-ring-let-uqg-be-hom-qquqg
section_title: "Quantum coordinate ring. Let Uq(g)∗ be Hom Q(q)(Uq(g), Q(q)). Then the co-"
section_number: 8.1
pages: 54-58
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
multiplication ∆ + (see (
1.1)) induces the multiplication µ on Uq(g)∗ as follows:
µ : Uq(g)∗ ⊗Uq(g)∗ → (Uq(g) ⊗Uq(g))∗ (∆ +)∗
− − − − →Uq(g)∗.
Later on, it will be convenient to use Sweedler’s notation ∆ +(x) = x(1) ⊗x(2). With
this notation,
(
fg
)
(x) = f (x(1))g(x(2)) for f,g ∈Uq(g)∗ and x ∈Uq(g).
TheUq(g)-bimodule structure onUq(g) induces aUq(g)-bimodule structure onUq(g)∗.
Namely,
(x ·f )(v) = f (vx) and ( f ·x)(v) = f (xv) for f ∈Uq(g)∗ and x,v ∈Uq(g).
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 55
Then the multiplication µ is a morphism of a Uq(g)-bimodule, where Uq(g)∗ ⊗Uq(g)∗
has the structure of a Uq(g)-bimodule via ∆ +. That is, for f,g ∈ Uq(g)∗ and x,y ∈
Uq(g), we have
x(fg )y = (x(1)fy (1))(x(2)gy(2)),
where ∆ +(x) = x(1) ⊗x(2) and ∆ +(y) = y(1) ⊗y(2).
Deﬁnition 8.1.1. We deﬁne the quantum coordinate ring Aq(g) as follows:
Aq(g) = {u ∈Uq(g)∗ | Uq(g)u belongs to Oint(g) and uUq(g) belongs to O r
int(g)}.
Then, Aq(g) is a subring of Uq(g)∗ because (i) µ is Uq(g)-bilinear, (ii) Oint(g) and
O r
int(g) are closed under the tensor product.
We have the weight decomposition: Aq(g) = ⨁
η,ζ ∈P
Aq(g)η,ζ , where
Aq(g)η,ζ := {ψ ∈Aq(g) | qhl ·ψ ·qhr =q⟨hl,η⟩+⟨hr,ζ⟩ψ for hl,h r ∈ P∨},
Forψ ∈Aq(g)η,ζ , we write
wtl(ψ) = η and wt r(ψ) = ζ.
For any V ∈ O int(g), we have the Uq(g)-bilinear homomorphism
ΦV : V ⊗(DϕV )r →Aq(g)
given by
ΦV (v ⊗ψr)(a) = ⟨ψr,av ⟩ = ⟨ψra,v ⟩ for v ∈V , ψ ∈ DϕV and a ∈Uq(g).
Proposition 8.1.2 ([17, Proposition 7.2.2]) . We have an isomorphism Φ of Uq(g)-
bimodules
(8.1) Φ : ⨁
λ∈P+
V (λ) ⊗
Q(q)
V (λ)r ∼
− →Aq(g)
given by Φ |V (λ) ⊗Q(q)V (λ)r = Φ λ := ΦV (λ). Namely,
Φ(u ⊗v r)(x) = ⟨v r,xu ⟩ = ⟨v rx,u ⟩ = (v,xu ) for any v,u ∈V (λ) and x ∈Uq(g).
We introduce the crystal basis
(
Lup(Aq(g)),B (Aq(g))
)
of Aq(g) as the images by Φ
of ⨁
λ∈P+
Lup(λ) ⊗Lup(λ)r and
⨆
λ∈P+
B(λ) ⊗B(λ)r.
Hence it is a crystal base with respect to the left action of Uq(g) and also the right
action of Uq(g). We sometimes write by e∗
i and f ∗
i the operators of Aq(g) obtained by
the right actions of ei and fi.
We deﬁne the Z[q±1]-form of Aq(g) by
Aq(g)Z[q±1] :=
{
ψ ∈Aq(g) | ⟨ψ, Uq(g)Z[q±1]⟩ ⊂ Z[q±1]
}
.
56 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
We deﬁne the bar-involution − of Aq(g) by
ψ(x) = ψ(x) for ψ ∈Aq(g), x ∈Uq(g).
Note that the bar-involution is not a ring homomorphism but it satisﬁe s
ψ θ =q(wtl(ψ),wtl(θ))−(wt r(ψ),wtr(θ)) θψ for any ψ, θ ∈Aq(g).
Since we do not use this formula and it is proved similarly to Proposition 8.1.4 below,
we omit its proof.
The triple
(
Q ⊗Aq(g)Z[q±1], Lup(Aq(g)), Lup(Aq(g))
)
is balanced ([ 17, Theorem 1]),
and hence there exists an upper global basis of Aq(g)
Bup(Aq(g)) := {Gup(b) | b ∈Bup(Aq(g))}.
Forλ ∈ P+ and µ ∈ Wλ , we denote by uµ the unique member of the upper global
basis of V (λ) with weight µ. It is also a member of the lower global basis.
Proposition 8.1.3. Let λ ∈ P+, w ∈ W and b ∈ B(λ). Then, Φ(Gup(b) ⊗ur
wλ) is a
member of the upper global basis of Aq(g).
Proof. The elementψ :=Φ(Gup(b) ⊗ur
wλ) is bar-invariant and a member of crystal basis
modulo qLup(Aq(g)). For any P ∈Uq(g)Z[q±1],
⟨ψ,P ⟩ =
(
uwλ,PG up(b)
)
belongs to Z[q±1] because PG up(b) ∈ V up(λ)Z[q±1] and uwλ ∈ V low(λ)Z[q±1]. Hence ψ
belongs to Aq(g)Z[q±1]. □
The Q(q)-algebra anti-automorphismϕ ofUq(g) induces a Q(q)-linear automorphism
ϕ∗ of Aq(g) by (
ϕ∗ψ
)
(x) = ψ
(
ϕ(x)
)
for any x ∈Uq(g).
We have
ϕ∗(
Φ(u ⊗v r)
)
= Φ(v ⊗ur),
and
wtl(ϕ∗ψ) = wt r(ψ) and wt r(ϕ∗ψ) = wt l(ψ).
It is obvious that ϕ∗ preservesAq(g)Z[q±1], Lup(Aq(g)) and Bup(Aq(g)).
Proposition 8.1.4.
ϕ∗(ψθ) = q(wtr(ψ),wtr(θ))−(wtl(ψ),wtl(θ))(ϕ∗ψ)(ϕ∗θ).
In order to prove this proposition, we prepare a sublemma.
Let ξ be the Q(q)-algebra automorphism of Uq(g) given by
ξ(ei) = q−1
i tiei, ξ (fi) = qifit−1
i , ξ (qh) = qh.
We can easily see
(ξ ⊗ξ) ◦ ∆ + = ∆ − ◦ξ.
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 57
Let ξ∗ be the automorphism of Aq(g) given by
(ξ∗ψ)(x) = ψ(ξ(x)) for ψ ∈Aq(g) and x ∈Uq(g).
Sublemma 8.1.5. We have
ξ∗(ψ) = qA(wtl(ψ),wtr(ψ))ψ,
whereA(λ,µ ) = 1
2
(
(µ,µ ) − (λ,λ )
)
.
Proof. Let us show that, for each x, the following equality
ψ(ξ(x)) = qA(wtl(ψ),wtr(ψ))ψ(x)(8.2)
holds for any ψ.
The equality (
8.2) is obviously true for x =qh. If ( 8.2) is true for x, then
ξ∗(ψ)(xei) = ψ
(
ξ(xei)
)
=ψ
(
ξ(x)eiti)qi
=q(αi,wtl(ψ))+(αi,αi)/2ψ(ξ(x)ei)
=q(αi,wtl(ψ))+(αi,αi)/2(
ξ∗(eiψ)
)
(x)
=q(αi,wtl(ψ))+(αi,αi)/2+A(wtl(ψ)+αi,wtr(ψ))(eiψ)(x).
Since ‖λ +αi‖2 = ‖λ‖2 + 2(αi,λ ) + ‖αi‖2, ( 8.2) holds for xei. Similarly if ( 8.2) holds
for x, then it holds for xfi. □
Proof of Proposition 8.1.4. We have
(ϕ ◦ϕ) ◦ ∆ − = ∆ + ◦ϕ.
Hence, we have
⟨ϕ∗(ψθ),x ⟩ = ⟨ψθ,ϕ (x)⟩
= ⟨ψ ⊗θ, ∆ +(ϕ(x))⟩
= ⟨ψ ⊗θ, (ϕ ⊗ϕ) ◦ ∆ −(x)⟩
= ⟨ϕ∗(ψ) ⊗ϕ∗(θ), ∆ −(x)⟩.
It follows that
⟨ξ∗(ϕ∗(ψθ)),x ⟩ = ⟨ϕ∗(ψθ),ξ (x)⟩ = ⟨ϕ∗(ψ) ⊗ϕ∗(θ), ∆ −(ξ(x))⟩
= ⟨ϕ∗(ψ) ⊗ϕ∗(θ), (ξ ⊗ξ) ◦ ∆ +x⟩
= ⟨ξ∗ϕ∗(ψ) ⊗ξ∗ϕ∗(θ), ∆ +x⟩
= ⟨
(
ξ∗ϕ∗(ψ)
)(
ξ∗ϕ∗(θ)
)
,x ⟩
=qA(wtr(ψ),wtl(ψ))+A(wt r(θ),wtl(θ))⟨(ϕ∗ψ) (ϕ∗θ), x⟩.
Therefore we obtain
ϕ∗(ψθ) = qc(ϕ∗ψ) (ϕ∗θ)
58 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
with
c =A(wtr(ψ), wtl(ψ)) +A(wtr(θ), wtl(θ)) −A(wtr(ψ) + wt r(θ), wtl(ψ) + wtl(θ))
= (wt r(ψ), wtr(θ)) − (wtl(ψ), wtl(θ)).
□
