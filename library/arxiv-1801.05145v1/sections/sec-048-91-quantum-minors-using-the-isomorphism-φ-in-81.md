---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-048-91-quantum-minors-using-the-isomorphism-φ-in-81
section_title: "Quantum minors. Using the isomorphism Φ in ( 8.1), for each λ ∈ P+ and"
section_number: 9.1
pages: 66-70
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
µ,ζ ∈Wλ , we deﬁne the elements
∆(µ,ζ ) := Φ(uµ ⊗ur
ζ) ∈Aq(g)
and
D(µ,ζ ) :=pn(∆(µ,ζ )) ∈Aq(n).
The element ∆( µ,ζ ) is called a ( generalized) quantum minor and D(µ,ζ ) is called a
unipotent quantum minor .
Lemma 9.1.1. ∆(µ,ζ ) is a member of the upper global basis of Aq(g). Moreover,
D(µ,ζ ) is either a member of the upper global basis of Aq(n) or zero.
Proof. Our assertions follow from Proposition 8.1.3 and Proposition 8.5.2. □
Lemma 9.1.2 ([3, (9.13)]) . Foru,v ∈W and λ,µ ∈ P+, we have
∆(uλ,vλ )∆(uµ,vµ ) = ∆
(
u(λ +µ),v (λ +µ)
)
.
By Proposition 8.5.4, we have the following corollary:
Corollary 9.1.3. Foru,v ∈W and λ,µ ∈ P+, we have
D(uλ,vλ )D(uµ,vµ ) =q−(vλ,vµ−uµ)D
(
u(λ +µ),v (λ +µ)
)
.
Note that
D(µ,µ ) = 1 for µ ∈Wλ .
Then D(µ,ζ ) ⁄= 0 if and only if µ ≼ ζ. Recall that for µ,ζ in the same W -orbit,
we say that µ ≼ ζ if there exists a sequence {βk}1≤k≤l of positive real roots such that,
deﬁning λ0 =ζ, λk =sβkλk−1 (1 ≤k ≤l), we have (βk,λk−1) ≥ 0 and λl =µ.
More precisely, we have
Lemma 9.1.4. Letλ ∈ P+ and µ,ζ ∈Wλ . Then the following conditions are equiva-
lent:
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 67
(i) D(µ,ζ ) is an element of upper global basis of Aq(n),
(ii) D(µ,ζ ) ⁄= 0,
(iii) uµ ∈U −
q (g)uζ,
(iv) uζ ∈U +
q (g)uµ,
(v) µ ≼ ζ,
(vi) for any w ∈W such that µ =wλ, there exists u ≤w (in the Bruhat order ) such
that ζ =uλ,
(vii) there exist u,v ∈W such that µ =wλ, ζ =uλ and u ≤w.
Proof. (i) and (ii) are equivalent by Lemma 9.1.1. The equivalence of (ii), (iii) and (iv)
is obvious. The equivalence of (v), (vi), (vii) is well-known. The equiva lence of (iv)
and (vi) is proved in [ 18]. □
For any u ∈Aq(n) \ {0} and i ∈I, we set
εi(u) := max {n ∈ Z≥0 |en
iu ⁄= 0},
ε∗
i (u) := max {n ∈ Z≥0 |e∗n
i u ⁄= 0}.
Then for any b ∈B(Aq(n)), we have
εi(Gup(b)) = εi(b) and ε∗
i (Gup(b)) = ε∗
i (b).
Lemma 9.1.5. Letλ ∈ P+, µ,ζ ∈Wλ such that µ ≼ ζ and i ∈I.
(i) If n := ⟨hi,µ ⟩ ≥ 0, then
εi(D(µ,ζ )) = 0 and e(n)
i D(siµ,ζ ) = D(µ,ζ ).
(ii) If ⟨hi,µ ⟩ ≤ 0 and siµ ≼ ζ, then εi(D(µ,ζ )) = −⟨hi,µ ⟩.
(iii) If m := −⟨hi,ζ ⟩ ≥ 0, then
ε∗
i (D(µ,ζ )) = 0 and e∗
i
(m)D(µ,siζ) = D(µ,ζ ).
(iv) If ⟨hi,ζ ⟩ ≥ 0 and µ ≼ siζ, then ε∗
i (D(µ,ζ )) = ⟨hi,ζ ⟩.
Proof. We have εi
(
∆(µ,ζ )
)
= max( −⟨hi,µ ⟩, 0) and ε∗
i
(
∆(µ,ζ )
)
= max( ⟨hi,ζ ⟩, 0).
Moreover,pn commutes with e(n)
i and e∗
i
(n).
Let us show (ii). Set ℓ = −⟨hi,µ ⟩. Then we have eℓ+1
i ∆(µ,ζ ) = 0, which implies
eℓ+1
i D(µ,ζ ) = 0. Hence εi(D(µ,ζ )) ≤ℓ. We have
e(ℓ)
i ∆(µ,ζ ) = ∆( siµ,ζ ).
Hence we have e(ℓ)
i D(µ,ζ ) = D(siµ,ζ ). By the assumption siµ ≼ ζ, D(siµ,ζ ) does not
vanish. Hence we have εi(D(µ,ζ )) ≥ℓ.
The other statements can be proved similarly. □
Proposition 9.1.6 ([3, (10.2)]) . Let λ,µ ∈ P+ and s,t,s ′,t ′ ∈ W such that ℓ(s′s) =
ℓ(s′) +ℓ(s) and ℓ(t′t) = ℓ(t′) +ℓ(t). Then we have
68 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
(i) ∆( s′sλ,t ′λ)∆(s′µ,t ′tµ) = q(sλ,µ)−(λ,tµ)∆(s′µ,t ′tµ)∆(s′sλ,t ′λ).
(ii) If we assume further that s′sλ ≼ t′λ and s′µ ≼ t′tµ, then we have
D(s′sλ,t ′λ)D(s′µ,t ′tµ) = q(s′sλ+t′λ,s ′µ−t′tµ)D(s′µ,t ′tµ)D(s′sλ,t ′λ),(9.1)
or equivalently
q(t′λ,t ′tµ−s′µ)D(s′sλ,t ′λ)D(s′µ,t ′tµ) = q(s′µ−t′tµ,s ′sλ)D(s′µ,t ′tµ)D(s′sλ,t ′λ)(9.2)
Note that (ii) follows from by Proposition 8.5.4 and (i). Note also that the both
sides of ( 9.2) are bar-invariant, and hence they are members of the upper glob al basis
as seen by Corollary 4.1.5.
Proposition 9.1.7. Forλ,µ ∈ P+ and s,t ∈ W , set ιg
(
usλ ⊗(uλ)r)
= b− ⊗tλ ⊗b−∞
and ιg
(
uµ ⊗(utµ)r)
=b∞ ⊗ttµ ⊗b+ with b∓ ∈B(±∞). Then we have
∆(sλ,λ )∆(µ,tµ ) = Gup(
ιg
−1(b− ⊗tλ+tµ ⊗b+)
)
.
Proof. Recall that there is a pairing ( •, • ) :
(
V (λ) ⊗−V (µ)
)
×
(
V (λ) ⊗+V (µ)
)
→ Q(q)
deﬁned by (u ⊗−v,u ′ ⊗+v′) = (u,u ′)(v,v ′). It satisﬁes
(
P (u ⊗−v),u ′ ⊗+v′)
=
(
u ⊗−v,ϕ (P )(u′ ⊗+v′)
)
for any P ∈Uq(g).
Foru,u ′ ∈V (λ) and v,v ′ ∈V (µ), we have
⟨Φ(u ⊗u′r)Φ(v ⊗v′r),P ⟩ =
(
u′ ⊗−v′,P (u ⊗+v)
)
=
(
ϕ(P )(u′ ⊗−v′),u ⊗+v
)
.
Hence for P ∈Uq(g), we have
⟨∆(sλ,λ )∆(µ,tµ ),Pa ζ⟩ =δ(ζ =sλ +µ)
(
ϕ(P )(uλ ⊗−utµ),usλ ⊗+uµ
)
.
If Paζ =Glow(ϕ(b)) for b ∈B( ~Uq(g)), then we have
⟨∆(sλ,λ )∆(µ,tµ ),ϕ (Glow(b))⟩ =δ(ζ =sλ +µ)
(
Glow(b)(uλ ⊗−utµ),usλ ⊗+uµ
)
.
The element Glow(b)(uλ ⊗−utµ) vanishes or is a global basis of V (λ) ⊗−V (µ) by Propo-
sition 8.6.2. Since usλ ⊗+uµ is a member of the upper global basis of V (λ) ⊗+V (µ),
we have
⟨∆(sλ,λ )∆(µ,tµ ),ϕ (Glow(b))⟩ =δ(ζ =sλ +µ)δ
(
πλ,tµ(b) = usλ ⊗uµ
)
.
Here πλ,tµ : B( ~Uq(g)aλ+tµ) →B(λ) ⊗B(µ) is the crystal morphism given in ( 8.6).
Hence we obtain
∆(sλ,λ )∆(µ,tµ ) = Gup(ιg
−1(b)),
whereb ∈B( ~Uq(g)) is a unique element such that
(
Glow(b)(uλ ⊗−usµ),usλ ⊗+uµ
)
= 1.
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 69
On the other hand, we have Glow(b+)utµ =uµ andGlow(b−)uλ =usλ. The last equal-
ity implies ϕ(Glow(b−))usλ = uλ because (ϕ(Glow(b−))usλ,uλ) = ( usλ,G low(b−)uλ) =
(usλ,usλ) = 1. As seen in ( 8.4), we have
Glow(b−)Glow(b+)aλ+tµ −Glow(b− ⊗tλ+tµ ⊗b+) ∈U −
q (g)>sλ−λU +
q (g)<µ−tµaλ+tµ.
Hence we obtain
(
Glow(b− ⊗tλ+tµ ⊗b+)(uλ ⊗−utµ), usλ ⊗+uµ
)
=
(
Glow(b−)Glow(b+)(uλ ⊗−utµ), usλ ⊗+uµ
)
=
(
Glow(b+)(uλ ⊗−utµ), ϕ(Glow(b−))(usλ ⊗+uµ)
)
= 1.
In the last equality, we used Glow(b+)(uλ ⊗−utµ) = uλ ⊗− (Glow(b+)utµ) = uλ ⊗−uµ and
ϕ(Glow(b−))(usλ ⊗+uµ) =
(
ϕ(Glow(b−))usλ) ⊗+uµ =uλ ⊗+uµ.
Hence we conclude that b =b− ⊗tλ+tµ ⊗b+. □
Let
ιλ,µ : V (λ +µ) ֌V (λ) ⊗V (µ)
be the canonical embedding and
ιλ,µ : B(λ +µ) ֌B(λ) ⊗B(µ)
the induced crystal embedding.
Lemma 9.1.8. Forλ,µ ∈ P+ and x,y ∈W such that x ≥y, we have
uxλ ⊗uyµ ∈ιλ,µ(B(λ +µ)) ⊂B(λ) ⊗B(µ).
Proof. Let us show by induction on ℓ(x), the length of x in W . We may assume that
x ⁄= 1. Then there exists i ∈ I such that six < x. If siy < y, then six ≥ siy and
˜emax
i (uxλ⊗uyµ) = usixλ⊗usiyµ. If siy >y, thensix ≥y and ˜emax
i (uxλ⊗uyµ) = usixλ⊗uyµ.
In both cases, uxλ ⊗uyµ is connected with an element of ιλ,µ(B(λ +µ)). □
Lemma 9.1.9. Forλ,µ ∈ P+ and w ∈W , we have
∆(wλ,λ )∆(µ,µ ) = Gup(
ι−1
λ,µ(uwλ ⊗uµ) ⊗uλ+µ
r)
.
Proof. We have
ιg(uwλ ⊗ur
λ
)
=bwλ ⊗tλ ⊗b−∞,
ιg(uµ ⊗ur
µ
)
=b∞ ⊗tµ ⊗b−∞,
where bwλ :=ιλ(uwλ). Hence Proposition 9.1.7 implies that
∆(wλ,λ )∆(µ,µ ) = Gup(
ιg
−1(bwλ ⊗tλ+µ ⊗b−∞)
)
.
Then, ιg
(
ι−1
λ,µ(uwλ ⊗uµ) ⊗uλ+µ r)
=bwλ ⊗tλ+µ ⊗b−∞ gives the desired result. □
70 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
