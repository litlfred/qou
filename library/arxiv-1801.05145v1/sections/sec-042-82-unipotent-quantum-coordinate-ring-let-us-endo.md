---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-042-82-unipotent-quantum-coordinate-ring-let-us-endo
section_title: "Unipotent quantum coordinate ring. Let us endow U +"
section_number: 8.2
pages: 58-60
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
q (g) ⊗U +
q (g) with the
algebra structure deﬁned by
(x1 ⊗x2) · (y1 ⊗y2) = q−(wt(x2),wt(y1))(x1y1 ⊗x2y2).
Let ∆ n be the algebra homomorphism U +
q (g) →U +
q (g) ⊗U +
q (g) given by
∆ n(ei) = ei ⊗ 1 + 1 ⊗ei.
Set
Aq(n) = ⨁
β∈Q−
Aq(n)β where Aq(n)β := (U +
q (g)−β)∗.
Deﬁning the bilinear form ⟨ · , · ⟩ : (Aq(n) ⊗Aq(n)) × (U +
q (g) ⊗U +
q (g)) → Q(q) by
⟨ψ ⊗θ,x ⊗y⟩ =θ(x)ψ(y),
we get an algebra structure on Aq(n) given by
(ψ ·θ)(x) = ⟨ψ ⊗θ, ∆ n(x)⟩ =θ(x(1))ψ(x(2))
where ∆ n(x) = x(1) ⊗x(2).
Since U +
q (g) has a U +
q (g)-bimodule structure, so does Aq(n).
We deﬁne the Z[q±1]-form of Aq(n) by
Aq(n)Z[q±1] =
{
ψ ∈Aq(n) |ψ
(
U +
q (g)Z[q±1]
)
⊂ Z[q±1]
}
,
and deﬁne the bar-involution − on Aq(n) by
ψ(x) = ψ(x) for ψ ∈Aq(n) and x ∈U +
q (g).
Note that the bar-involution is not a ring homomorphism but it satisﬁe s
ψ θ =q(wt(ψ),wt(θ)) θψ for any ψ, θ ∈Aq(n).
Fori ∈I, we denote by e∗
i the right action of ei on Aq(n).
Lemma 8.2.1. Foru,v ∈Aq(n), we have q-boson relations
ei(uv) = (eiu)v +q(αi,wt(u))u(eiv) and e∗
i (uv) = u(e∗
iv) +q(αi,wt(v))(e∗
iu)v.
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 59
Proof.
⟨ei(uv),x ⟩ = ⟨uv,xei⟩ = ⟨u ⊗v, ∆ n(xei)⟩.
If we set ∆ nx =x(1) ⊗x(2), then we have
∆ n(xei) = (x(1) ⊗x(2))(ei ⊗ 1 + 1 ⊗ei) = q−(αi,wt(x(2)))(x(1)ei) ⊗x(2) +x(1) ⊗(x(2)ei).
Hence, we have
⟨u ⊗v, ∆ n(xei)⟩ =q−(αi,wt(x(2)))u(x(2))v(x(1)ei) +u(x(2)ei)v(x(1))
=q(αi,wt(u))u(x(2)) · (eiv)(x(1)) + (eiu)(x(2)) ·v(x(1))
= ⟨q(αi,wt(u))u ⊗(eiv) + (eiu) ⊗v, ∆ nx⟩.
The second identity follows in a similar way. □
We deﬁne the map ι : U −
q (g) →Aq(n) by
⟨ι(u),x ⟩ = (u,ϕ (x)) for any u ∈U −
q (g) and x ∈U +
q (g).
Since ( , ) is a non-degenerate bilinear form on U −
q (g), ι is injective. The relation
⟨ι(e′
iu),x ⟩ = (e′
iu,ϕ (x)) = (u,fiϕ(x)) = (u,ϕ (xei)) = ⟨ι(u),xei⟩ = ⟨eiι(u),x ⟩,
implies that
ι(e′
iu) = eiι(u).
Lemma 8.2.2. ι is an algebra isomorphism.
Proof. The map ι is an algebra homomorphism because e′
i andei both satisfy the same
q-boson relation. □
Hence, the algebra Aq(n) has an upper crystal basis ( Lup(Aq(n)),B (Aq(n))) such
that B(Aq(n)) ≃B(∞). Furthermore, Aq(n) has an upper global basis
Bup(Aq(n)) = {Gup(b)} b∈B(Aq(n))
induced by the balanced triple
(
Q ⊗Aq(n)Z[q±1], Lup(Aq(n)), Lup(Aq(n))
)
(see ( 1.3)).
There exists an injective map
ιλ : B(λ) →B(∞)
induced by the U +
q (g)-linear homomorphism ιλ : V (λ) →Aq(n) given by
v ↦− →
(
U +
q (g) ∋a ↦→(av,uλ)
)
.
The map ιλ commutes with ˜ei. We have
Glow
λ (b) = Glow(ιλ(b))uλ and ιλGup
λ (b) = Gup(ιλ(b)) for any b ∈B(λ).
60 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
Remark 8.2.3. Note that the multiplication on Aq(n) given in [ 11] is diﬀerent from
ours. Indeed, by denoting the product of ψ andφ in [ 11, §4.2] by ψ ·φ, for x ∈U +
q (g),
we have
(ψ ·φ)(x) = ψ(x(1))φ(x(2)),
where ∆ +(x) = x(1)qh(1) ⊗x(2)qh(2) for x(1),x (2) ∈ U +
q (g), h(1),h (2) ∈ P∨. By Lemma
8.5.3 below, we have
(ψ ·φ)(x) = ψ
(
q(wt(x(1)),wt(x(2)))(x(2))
)
φ
(
x(1)
)
=q(wt(x(1),wt(x(2)))ψ(x(2))φ(x(1)) = q(wt(ψ),wt(φ))(ψφ)(x)
for x ∈ U +
q (g), where ∆ n(x) = x(1) ⊗x(2). In particular, we have a Q(q)-algebra
isomorphism from (Aq(n), ·) to Aq(n) given by
x ↦→q− 1
