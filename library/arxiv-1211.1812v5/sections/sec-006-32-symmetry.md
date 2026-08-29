---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com"
section_id: sec-006-32-symmetry
section_title: "Symmetry."
section_number: 3.2
pages: 16-17
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
doc_brief: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com — We show that superselection structures on curved spacetime s, that are expected to describe"
---
As a ﬁnal step we consider the symmetry structure. This is an esse ntial ingredient at the level of
duality theory ([16, §1]) and, at the same time, encodes the Fermi-Bose statistics (see [1 3] for a
friendly introduction). We introduce the family of unitary operator s
ǫ(zρ,wσ)e :=wσ(poe)∗σo(zρ(po′e))∗ ·zρ(po′e)ρe(wσ(poe)) , ∀e<a , (3.9)
where poe :e →o, po′e :e →o′ are paths in ∆ a such that o ⊥o′ . The fact the for any a ∈ ∆ there
are causally disjoint o,o ′ < a is an immediate consequence of [9, Lemma B.5], so any ǫ(zρ,wσ)e ,
e < a, is well-deﬁned as an element of UH ∩Ra . By Lemma A.2 we have that ǫ(zρ,wσ)e is
independent of the choice of poe , po′e , o and o′ .
The family ǫ(zρ,wσ) fulﬁls the symmetry relations of [16, §1], which, in our setting, take the
form 


ǫ(zρ,wσ)∂0b · (z ⊗w)ρ◦σ(b) = ( w ⊗z)σ◦ρ(b) ·ǫ(zρ,wσ)∂1b ,
(s ⊗t)e ·ǫ(zρ,wσ)e = ǫ(z′
ρ′,w ′
σ′ )e · (t ⊗s)e ,
ǫ(zρ,wσ)e ·ǫ(wσ,zρ)e = 1 , ǫ (ιa,zρ)e = ǫ(zρ,ιa)e = 1 ,
ǫ((z ⊗w)ρ◦σ,vτ )e = ǫ(zρ,vτ )e ·ρe(ǫ(wσ,vτ )e) ,
(3.10)
∀e<a , zρ,z ′
ρ′,wσ,w ′
σ′,vτ ∈ obj Z 1
c (R)<a , t ∈ (zρ,z ′
ρ′ ), s ∈ (wσ,w ′
σ′ ), b ∈ Σ 1(∆ a).
The explicit computations, that are on the line of [31, 35, 9], are pos tponed in §A. It is at this
point that we make use of the fact that we must have s ≥ 2 spatial dimensions, as otherwise we may
get a braiding instead of a symmetry. Since, as mentioned in the Intr oduction, where are interested
in ordinary Bose-Fermi statistics, in the rest of the section we sha ll assume that M has spacetime
dimension ≥ 3 .
Now, even if (3.10) are fulﬁlled, in general ǫ(zρ,wσ) does not deﬁne a symmetry, because we
should have
ǫ(zρ,wσ)e ∈Re , ∀e<a .
The standard way to prove the above property would be the followin g. In general, if t ∈ (ρe,σe)
then
tt′ =tρe(t′) = σe(t′)t =t′t , ∀o ⊥e,t ′ ∈Ro ⇒ t ∈R′
o , ∀o ⊥e ,
and this, by (punctured) Haag duality, suﬃces to conclude that t ∈Re . In particular, in our case
we can verify that ǫ(zρ,wσ)e ∈ (σeρe,ρeσe), nevertheless we are working with families of operators
in the restricted net
R|∆ a = ( {Re}e<a , )∆ a ,
that could violate punctured Haag duality because, given x ∈M , we expect that the inclusion
Re = ∩o⊥e,o⊥{x}R′
o ⊆ Ra
e := ∩o⊥e,o<aR′
o
is proper for any e < a. Thus we can conclude only that ǫ(zρ,wσ)e ∈ Ra
e , e < a. In the next
subsection we show how to avoid this diﬃculty using Rem.2.1.
16
