---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com"
section_id: sec-005-31-charge-structure
section_title: "Charge structure."
section_number: 3.1
pages: 14-16
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
doc_brief: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com — We show that superselection structures on curved spacetime s, that are expected to describe"
---
To introduce the charge structure we follow the standard way and , given a ∈ ∆, deﬁne the set
locRa ⊆ endRa whose elements are *-endomorphims
ρ ∈ endRa | ∃ e<a fulﬁlling
{
ρ(Ro) ⊆Ro , ∀o ⊇e,o<a,
ρ =idRo , ∀o ⊥e,o<a . (3.3)
In the sequel we shall keep in evidence the localization region e ∈ ∆ a by writing ρe ≡ρ. Note that
τe :=ρe ◦σe ∈ locRa , ∀ρe,σe ∈ locRa .
We now consider the category Z 1
c (R)<a with objects pairs ( z,ρ ) ≡zρ , where
z = {z(b) ∈UR |b|}b∈Σ 1(∆ a) , ρ = {ρe ∈ locRa}e∈∆ a ,
14
fulﬁll { dz(c) = 1 , ∀c ∈ Σ 2(∆ a) ,
z(b) ·ρ∂1b(t) = ρ∂0b(t) ·z(b) , ∀b ∈ Σ 1(∆ a) , t ∈Ra . (3.4)
The ﬁrst equation says that z is a cocycle deﬁned on the ”local” poset ∆ a . The second one yields
an interpretation of z as the ﬂat connection transporting from ∂1b to ∂0b the quantum charge
represented by ρ (see [31, §25-28] or the friendly [13]) and implies that z uniquely determines ρe
on Re for any e<a : for, if o ∈ ∆ a with o ⊥e and p :e →o is a path in ∆ a then
ρe(T ′)
(3.4 )
= z(p)∗ρo(T ′)z(p) , ∀T ′ ∈Ra ⇒ ρe(T )
(3.3 )
= z(p)∗Tz (p) , ∀T ∈Re . (3.5)
The arrows of Z 1
c (R)<a are given by
(zρ,wσ) := { t = {te ∈Re}e∈∆ a : t∂0bz(b) = w(b)t∂1b , ∀b ∈ Σ 1(∆ a) } . (3.6)
Note that ρ,σ play no role in the deﬁnition of ( zρ,wσ). Applying repeatedly (3.4) to a path
p :e →o, p =bn ∗... ∗b1 , with e ⊥o<a , we have that if t ∈ (zρ,wσ) then
tozρ(p) = wσ(p)te ⇒ Twσ(p)te =Ttozρ(p)
Einstein causality
= toTzρ(p) , ∀T ∈Re ,
so, applying (3.5),
σe(T )te = teρe(T ) , ∀t ∈ (zρ,wσ) , e<a , T ∈Re . (3.7)
We deﬁne the tensor product on Z 1
c (R)<a . To this end, given zρ,wσ , z′
ρ′,w ′
σ′ ∈ objZ 1
c (R)<a ,
t ∈ (zρ,z ′
ρ′ ), s ∈ (wσ,w ′
σ′ ), we set
{ {z ⊗w}ρ◦σ(b) := zρ(b)ρ∂1b(wσ(b)) , ∀e<a , b ∈ Σ 1(∆ a) ,
(t ⊗s)e :=teρe(se) , ∀e<a . (3.8)
The fact that the above-deﬁned relations yield a tensor product o n Z 1
c (R)<a follows by elemen-
tary *-algebraic computations (analogous to those in [31, §27], [35, §4.2.1]), anyway for conve-
nience of non-specialists we recall some of them. A ﬁrst point is that since any ρe , e < a, is
a unital *-endomorphism, we have that zρ(b)ρ∂1b(wσ(b)) is unitary. Moreover, (3.3) implies that
zρ(b)ρ∂1b(wσ(b)) ∈ R|b| for any b ∈ Σ 1(∆ a). The cocycle relations follow by computing, for any
c ∈ Σ 2(∆ a),
zρ(∂0c)ρ∂10c(wσ(∂0c)) ·zρ(∂2c)ρ∂12c(wσ(∂2c)) = zρ(∂0c)zρ(∂2c)ρ∂12c(wσ(∂0c))ρ∂12c(wσ(∂2c)) =
=zρ(∂1c)ρ∂12c(wσ(∂1c)) =
=zρ(∂1c)ρ∂11c(wσ(∂1c)) ,
having used repeatedly (3.4), the composition rule of face maps ∂12 =∂11 (see (2.1) or [32, Eq.1]),
and the cocycle relations of z,w . Passing to the ”charges”, for any t ∈Ra we have
zρ(b)ρ∂1b(wσ(b)) · {ρ∂1b ◦σ∂1b}(t) = zρ(b) ·ρ∂1b(wσ(b)σ∂1b(t)) = ρ∂0b(σ∂0b(t)wσ(b)) ·zρ(b) =
= {ρ∂0b ◦σ∂0b}(t) ·zρ(b)ρ∂1b(wσ(b)) ,
so (3.4(2)) is fulﬁlled for z ⊗w and (z ⊗w)ρ◦σ ∈ obj Z 1
c (R)<a . To verify that t ⊗s is an arrow in
( (z ⊗w)ρ◦σ , (z′ ⊗w′)ρ′◦σ′ ) we compute
t∂0bρ∂0b(s∂0b) ·zρ(b)ρ∂1b(wσ(b)) = t∂0bzρ(b) ·ρ∂1b(s∂0bwσ(b)) =
= z′
ρ′(b)t∂1bρ∂1b(w′
σ′ (b))ρ∂1b(s∂1b) =
(3.7)
= z′
ρ′(b)ρ′
∂1b(w′
σ′ (b)) ·t∂1bρ∂1b(s∂1b) ,
obtaining the desired relations.
15
Remark 3.1. Let ιa ∈ obj Z 1
c (R)<a be the pair deﬁned by the identity cocycle of Z 1(R)<a and
the constant family with element the identity idRa ∈ autRa . Clearly ιa is the identity object of the
tensor product of Z 1(R)<a , and, given x ∈a, we have
C1 ⊆ (ιa,ιa) = ∩e<aRe ⊆ ∩ e<a:x∈eRe
(∗)
= ∩a∋xRa
(3.1 )
= C1 ,
where for the equality (*) we used the fact that {a ∈ ∆ : x ∈a} is downward directed. So (ιa,ιa) =
C1 and Z 1
c (R)<a has a simple unit.
