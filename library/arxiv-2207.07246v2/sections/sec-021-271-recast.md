---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-021-271-recast
section_title: "Recast"
section_number: 2.7.1
pages: 47-50
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
We need to recast Eq.(2.11) into a form that is suitable for PIMC calculations. We
set the total time τ as τ =τ1 +τ2 =N∆τ, and we insert N short-time propagators
U(∆τ) in Eq.(2.11) as well as inserting corresponding identity operators in Eqs.(2.36)
at each of them, then Eq.(2.11) with short-time propagator becomes,
⟨ ˆO(∆τ)⟩=
Re∑
S′
∫
DR′⟨ΨT|R0S0⟩⟨R0S0|U(∆τ)|R1S1⟩...⟨RISI| ˆO|RI+ 1SI+ 1⟩...⟨RN+ 1SN+ 1|ΨT⟩
Re∑
S
∫
DR⟨ΨT|R0S0⟩⟨R0S0|U(∆τ)|R1S1⟩...⟨RN−1SN−1|U(∆τ)|RNSN⟩⟨RNSN|ΨT⟩,(2.84)
where∑
S′
and
∫
DR′ in the numerator means ∑
S0,...,SN+1
and
∫
dR0...dRN+1, and∑
S
and
∫
DR in the denominator means ∑
S0,...,SN
and
∫
dR0...dRN.
37
For any local operator ˆO in Eq.(2.84), we can write down,
⟨RISI| ˆO|RI+1SI+1⟩ =⟨SI|OI|SI+1⟩⟨RI|RI+1⟩ =⟨SI|OI|SI+1⟩δ(RI−RI+1), (2.85)
where OI means operator ˆO with spatial conﬁguration RI. Note that Eq.(2.85) allows
us to remove RI+1 from the integral in the numerator of Eq.(2.84). So the N +
2 conﬁgurations R0 to RN+1 in the numerator can ﬁnally be reduced to N + 1
conﬁgurations from R0 to RN after relabeling. So the actual number of beads in the
numerator is the same as in the denominator.
For the propagator in Eq.(2.84) we insert ∑
SI
|SI⟩⟨SI| = 1 in Eq.(2.35) and we
can write down,
∑
SI
⟨RI−1SI−1|US(∆τ)|RISI⟩⟨RISI|US(∆τ)|RI+1SI+1⟩
=
∑
SI
{
⟨SI−1|⊗⟨ RI−1|e−V†
2 ∆τGe−T ∆τe−V
2 ∆τ|RI⟩⊗| SI⟩
×⟨SI|⊗⟨ RI|e−V†
2 ∆τGe−T ∆τe−V
2 ∆τ|RI+1⟩⊗| SI+1⟩
}
=⟨SI−1|e−
V†
I−1∆τ
2 Ge−VI∆τ
2 e−
V†
I ∆τ
2 Ge−
VI+1∆τ
2 |SI+1⟩× Gf
RI−1RIGf
RIRI+1, (2.86)
whereVI means the potential operator V with spatial conﬁguration RI, and e−VI∆τ
2 is
calculated by Eq.(2.63). The free particle propagator Gf
RIRJ =⟨RI|e−T ∆τ|RJ⟩ can be
calculated by Eq.(2.69). By repeatedly using Eq.(2.86) in Eq.(2.84) we can remove
anySI sandwiched between two short-time propagators U(∆τ). Finally we are left
with 2 spin-isospin symbols in the trial wave functions to be summed over, we label
them S0 and SN, where S0 is for the trial wave function on the left ⟨ΨT|R0S0⟩, and
SN is for the trial wave function on the right ⟨RNSN|ΨT⟩.
Furthermore, consider the l and r order picked from the trial wave function Ψ T as
shown in Eqs.(2.51,2.52), the approximated expectation value ⟨ ˆO(∆τ)⟩ in Eq.(2.84)
38
for PIMC calculations can ﬁnally be written as a general form,
⟨ ˆO(∆τ)⟩ =
=∑
l
∑
r
∫
DRRe[g(R)lr]
z }| {
Re
∑
S0,SN
∫
DR⟨ΨT|R0S0⟩⟨R0S0|[U(∆τ)]N1 ˆO[U(∆τ)]N2|RNSN⟩⟨RNSN|ΨT⟩
Re
∑
S0,SN
∫
DR⟨ΨT|R0S0⟩⟨R0S0|[U(∆τ)]N|RNSN⟩⟨RNSN|ΨT⟩
| {z }
=∑
l
∑
r
∫
DRRe[f(R)lr]
=
∑
l
∑
r
∫
DR
{
Re[g(R)lr]
|Re[f(R)lr]|
}
|Re[f(R)lr]|
∑
l
∑
r
∫
DR
{
Re[f(R)lr]
|Re[f(R)lr]|
}
|Re[f(R)lr]|
=
∑
l
∑
r
∫
DRAlr(R)Plr(R)∑
l
∑
r
∫
DRBlr(R)Plr(R)
=⟨Alr(R)⟩
⟨Blr(R)⟩
⏐⏐⏐⏐
{l,r,R}∈Plr(R)
, (2.87)
where we use symbolR to denote all the spatial conﬁgurations {R0,R 1,...RN},
R≡{ R0,R 1,...RN}, (2.88)
and its integral is the spatial integral over all the conﬁgurations RI,
∫
DR≡
N∏
I=0
∫
dRI. (2.89)
In Eq.(2.87), Alr(R) and Blr(R) are real functions,
Alr(R) = Re[g(R)lr]
|Re[f(R)lr]|, (2.90)
Blr(R) = Re[f(R)lr]
|Re[f(R)lr]|, (2.91)
and we can see that Blr(R) is either 1 or -1.
In Eq.(2.87), Plr(R) is the probability distribution,
Plr(R) =|Re[f(R)lr]|
N , (2.92)
which is normalized to one in the following way,
∑
l
∑
r
∫
DRPlr(R) = 1, (2.93)
and its normalization factor is N =∑
l
∑
r
∫
DR|Re[f(R)lr]|.
39
