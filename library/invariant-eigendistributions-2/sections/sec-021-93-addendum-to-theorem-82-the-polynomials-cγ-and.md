---
doc_id: invariant-eigendistributions-2
doc_title: "REPRESENTATIONS OF WEYL GROUPS 1 Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups W. ROSSMAN"
section_id: sec-021-93-addendum-to-theorem-82-the-polynomials-cγ-and
section_title: "Addendum to theorem 8.2. The polynomials cΓ and pO are given by"
section_number: 9.3
pages: 23-26
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
doc_brief: "REPRESENTATIONSOFWEYL GROUPS 1 Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups W. ROSSMANN1 — 25 sections: Intr"
---
cΓ(λ)= kO
∑
y∈Wo
my⟨λ1,y ·λ2⟩eo (8)
pO(x)= 1
e!kO
∑
y∈Wo
χσ(y)⟨x1,y ·x2⟩eo (9)
REPRESENTATIONS OF WEYL GROUPS 24
for some constant kO depending only on O.
(Note that in these equationsmy = m(y,1) in accordance with the identiﬁcationW/Wo = Wo.)
Proof. This follows bycomparing the relation (8.6):
∑
y∈W
my⟨λ,y ·x⟩e =cΓ(λ)pO(x)
with the relation
1
e!
∑
y∈W
my⟨λ,y ·x⟩e =fa(λ1,λ 2)fσ(x1,x 2)
from Lemma 9.2 when we takeχσ = χO and a = the component ofm which transforms byχO ⊗χO on
the left. In the formula
fa(λ1,λ 2)=
∑
y∈Wo
a(y)⟨λ1,y ·λ2⟩eo
we maythen again replacea(y)b ymy, because the component ofm of typeχO is the onlyone which
contributes in degreeeo in this sum, as follows from
Γ∈H2n(S( ¯O))≈H2n(S(O)) +
∑
O′<O
H2n(S(O′)).
10. Nilpotent orbital integrals
For eachGo-orbit O in igo∗ let µO be the distribution ongo∗ deﬁned by
⟨µO,f⟩= 1
(2πi)d
∫
O
fe −σO (1)
with d =d i mCO. µO is a tempered distribution onigo∗. (Of course, we useigo∗ rather thango∗ or go
onlyto conform with the deﬁnition of the distributionsθΓ, which will simplifythe notation.) We denote
by ˆµO the Fourier transform ofµO, a tempered distribution ongo, given bya locallyintegrable function.
In this sense :
ˆµO(ξ)= 1
(2πi)d
∫
Oλ
exO −σO.
For regularλ ∈ ih∗ we setOλ = Go ·λ and µλ = µOλ.S i n c eGo ·λ = K ·(λ+ibo
⊥)= pλS1 for suchλ
we ﬁnd that its Fourier transform is
ˆµλ = 1
(2πi)n
∫
Oλ
eλ−σλ = 1
π
∑
y∈Wo
ey−1λ (2)
as tempered distributions ongo.
REPRESENTATIONS OF WEYL GROUPS 25
Nowtakefor O anilpotent Go-orbitin igo∗.From(8.7)weknowthat itsFouriertransform ˆµO =θO
is
ˆµO = 1
e!
pO
π (3)
wherepO isthedistributionon go whichon ho isgiv enb ytheuptoscalarsunique Wo-invariantpolynomial
of degreee =e(O)o nh transforming accordingto the irreducible characterχO⊗χO underW =Wo×Wo.
Using (8.20) we have for anyregularλ∈h∗ af o r m u l a
ˆµO =c o n s t .1
π
∑
y∈W
cO(y)y−1 ·λe (4)
for a constant depending onO and λ, namely
const. = eo
e!cO(λ)|W|
in the notation of section 8. Alternatively, using (9.9):
ˆµO(x)=c o n s t .
∑
y∈Wo
χσ(y)⟨x1,y ·x2⟩eo (5)
where this time the constant depends onlyon O , namely
const. = 1
kOe!.
(4) is a rather explicit formula for the invariant eigendistributionsˆµO on go, which have inﬁnitesimal
character 0. Compare this with Harish-Chandra’sformula for eigendistributions with regular inﬁnitesimal
character λ :
θ = 1
π
∑
y∈W
myey−1λ. (6)
(Of course, (6) is part of the genesis of (4).)
Formula (3) quicklyleads to a formula forµO itself as follows. Let∂O be the constant coeﬃcient
operator onh∗ corresponding to the polynomialpO on h. It satisﬁes
∂O,λe⟨λ,x⟩|λ=0 = pO(x).
where the subscriptλ on ∂O,λ means “diﬀerentiation with respect toλ”.
Diﬀerentiating equation (2) with respect toλ and evaluating atλ =0o n eg e t s
lim
λ→ 0
∂O,λ ˆµλ(x) = lim
λ→ 0
∂O,λ
{1
π
∑
y∈Wo
e⟨λ,y·x⟩
}
= |Wo|
π pO(x)= e!|Wo|ˆµO(x).
Inverting the Fourier transforms we arrive at
REPRESENTATIONS OF WEYL GROUPS 26
