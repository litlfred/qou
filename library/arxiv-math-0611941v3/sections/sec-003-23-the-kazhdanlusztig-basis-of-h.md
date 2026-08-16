---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR MEINOLF GECK"
section_id: sec-003-23-the-kazhdanlusztig-basis-of-h
section_title: "The Kazhdan–Lusztig basis of H"
section_number: 2.3
pages: 4-5
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
doc_brief: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR MEINOLF GECK — Let H be the one-parameter Hecke algebra associated to a ﬁnite Weyl gr oup W , deﬁned over a ground ring in which “bad” primes for W are"
---
deﬁned in [25, Theorem 5.2]. We have cw = Tw + ∑
y py,w Ty where py,w ∈ v−1Z[v−1] and
py,w = 0 unless y < w in the Bruhat–Chevalley order. Given x, y ∈ W , we write
cxcy =
∑
z∈W
hx,y,zcz where hx,y,z ∈ A.
As in [25], we usually work with the elements c†
w obtained by applying the unique A-algebra
involution H → H, h ↦→h† such that T †
s = −T −1
s for any s ∈ S; see [25, 3.5]. We refer to [25,
Chap. 8] for the deﬁnition of the preorders ⩽ L, ⩽ R, ⩽ LR and the corresponding equivalence
relations ∼L, ∼R, ∼LR on W , induced by L. The equivalence classes with respect to these
relations are called left, right and two-sided cells of W , respectively. If L(s) = 1 for all s ∈ S,
then Cw = (−1)l(w)c†
w where {Cw} is the basis originally constructed in [22].
Let z ∈ W . Following Lusztig [25, 13.6], we deﬁne a(z) ∈ Z/greaterorequalslant0 by the condition that
va(z)hx,y,z ∈ Z[v] for all x, y ∈ W ,
va(z)−1hx,y,z ⁄∈Z[v] for some x, y ∈ W .
Furthermore, if p1,z ⁄= 0, we deﬁne ∆( z) ∈ Z/greaterorequalslant0 and 0 ⁄= nz ∈ Z by the condition that
p1,z = nzv−∆( z) + strictly smaller powers of v; see [25, 14.1] .
Otherwise, we set ∆( z) = ∞ and leave nz undeﬁned. (This case can only occur when
L(s) = 0 for some s ∈ S.) We set
D = {z ∈ W | a(z) = ∆( z)}.
(In what follows, the coeﬃcients nz will only play a role when z ∈ D .)
2.4. Lusztig’s conjectures and the asymptotic ring J. In the sequel, we assume that
the following hypotheses are satisﬁed.
Lusztig’s conjectures (P1)–(P15) in [25, 14.2] hold for H.
(Actually, for our purposes, instead of (P15) it is enough to require the somewhat weaker
statement [25, 18.9(b)], which we called (P15’) in [11, §5].) By [25, Chap. 15], these
conjectures are known to hold when L is a positive multiple of the length function (“equal
parameter case”), thanks to a deep geometric interpretation of the basis {cw}. They are also
known for a certain class of non-trivial weight functions in type Bn; see [12], [10].
Assuming the above hypotheses, we can perform the following cons tructions. Following
Lusztig [25, Chap. 18], let J be a free Z-module with basis {tw | w ∈ W }. We deﬁne a
multiplication on J by
txty =
∑
z∈W
γx,y,z −1 tz,
where γx,y,z −1 ∈ Z is the constant term of va(z)hx,y,z ∈ Z[v]. Then it turns out that this
multiplication is associative and we have an identity element given by 1 J = ∑
d∈D ndtd.
HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR 5
Furthermore, we have a homomorphism of A-algebras φ : H → JA = A ⊗Z J such that
φ(c†
w) =
∑
z∈W,d ∈D
a(z)=a(d)
hw,d,z ˆnz tz (w ∈ W ),
where ˆnz is deﬁned as follows. Given z ∈ W , let d be the unique element of D such that
d ∼L z−1; then ˆnz = nd = ±1. (See properties (P5), (P13) in Lusztig’s conjectures [25,
14.2].) Note that the function z ↦→ˆnz is constant on the right cells of W .
