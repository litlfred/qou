---
doc_id: resur-and-mld-calc-d-sauzin-hal
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-006-the-hyperlogarithmic-mould
section_title: "The hyperlogarithmic mould."
section_number: null
pages: 12-13
source_pdf: Resur_and_Mld_Calc_D_SAUZIN_HAL.pdf
source_sha256: b33f24cc76102f33
doc_brief: "HAL Id: hal-04253203 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 9 sections: Introduction"
---
Here is a reinforcement of Theorem 5:
Theorem 11 ([´Eca81]). Let A := ~R (resp. ~Rs,
resp. ~Rs
Ω) andN :=~C (resp. C∗, resp. Ω′). There ex-
ists a symmetral A-valued mould (Uω)ω∈N such that,
for every ω0∈N and ω =ω1··· ωr∈N ,
∆ω0 Uω1···ωr =
{
Uω2···ωr if r≥ 1 and ω0 =ω1
0 otherwise.
(63)
Sketch of proof with A = ~Rs andN = C∗. Pick an
entire function ˆaω such that ˆaω(ω) ⁄= 0 for each
ω∈N . The equations V ∅(z) := 1 and, for ω⁄= ∅,
( d
dz +‖ω‖
)
V ω(z) =−V ω1···ωr−1(z)(B−1ˆaωr)(z) (64)
inductively deﬁne V ω(z) ∈ z−1C[[z−1]], with Borel
transforms
ˆV ω1(ζ) = ˆaω1(ζ)
ζ−ω1
, ˆV ω(ζ) =
ˆV ω1···ωr−1∗ˆaωr
ζ−‖ω‖ .
(65)
The resulting mould V is A-valued and symmetral.
Elementary manipulations show that, for each η∈
N , there is an alternal scalar mould V (η) such that
∆ηV =−V (η)× V, V ω(η)⁄= 0 ⇒ ‖ω‖ =η.
(66)
By (65), Vω1(ω1) =−2πiˆaω1(ω1).
We deﬁne an alternal mould by V = ∑
η∈NV (η).
It has a composition inverse, that we denote by −U.
Elementary manipulations show that U := V◦U sat-
isﬁes the requirements of Theorem 11. Details can be
found in [ ´Eca81; Sau09].
The hyperlogarithmic mould is the scalar mould U
obtained whenN = Z∗ andˆaω(ζ) = 1 for all ζ andω.
In that case, there are scalar moulds L(η) (η∈ Z∗)
such that
∆+
η V =L(η)× V, L ω(η)⁄= 0 ⇒ ‖ω‖ =η,
(67)
giving rise to a ‘multiple logarithm’ mould
Lω =
∑
η
Lω(η) =
∫
Γ+
2πi dζ1··· dζr−1
(ζ1−
∨
ω1)··· (ζr−1−
∨
ωr−1)
,
(68)
11
where
∨
ω1 = ω1,
∨
ω2 = ω1 +ω2,... and Γ+ connects 0
and
∨
ωr = ω1 +··· +ωr by circumventing integers to
the right. The moulds L± := 1 +∑
±η>0Lω(η) are
symmetral. These moulds are related to the MZVs.
