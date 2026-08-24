---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-013-the-scalar-singlet-quark-condensate
section_title: "The scalar singlet quark condensate"
section_number: null
pages: 19-21
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
In the following, we will show that a non-vanishing scalar si nglet quark condensate in the chiral limit
is a suﬃcient (but not a necessary) condition for a spontaneo us symmetry breaking in QCD. In this
section all physical quantities such as the ground state, th e quark operators etc. are considered in the
chiral limit.
Let us ﬁrst recall the deﬁnition of the nine scalar and pseudo scalar quark densities:
Sa(y) = ¯ q(y)λaq(y), a = 0, · · ·, 8, (70)
Pa(y) = i¯q(y)γ5λaq(y), a = 0, · · ·, 8, (71)
where λ0 =
√
2/3 /BD . We need the equal-time commutation relation of two quark op erators of the form
Ai(x) = q†(x) ˆAiq(x), where ˆAi symbolically denotes Dirac and ﬂavor matrices and a summati on over
color indices is implied:
[A1(t,⃗ x),A 2(t,⃗ y)] = δ3(⃗ x−⃗ y)q†(x)[ ˆA1, ˆA2]q(x). (72)
With the deﬁnition
QaV (t) =
∫
d3xq†(t,⃗ x)λa
2 q(t,⃗ x),
and using
[λa
2 ,γ 0λ0] = 0, [λa
2 ,γ 0λb] = γ0ifabcλc,
we see, after integration of Eq. (72) over ⃗ x, that the scalar quark densities of Eq. (70) transform under
SU(3)V as a singlet and as an octet, respectively,
[QaV (t),S 0(y)] = 0 , a = 1, · · ·, 8, (73)
19
[QaV (t),S b(y)] = i
8∑
c=1
fabcSc(y), a,b = 1, · · ·, 8, (74)
with analogous results for the pseudoscalar quark densitie s. Using the relation
8∑
a,b=1
fabcfabd = 3δcd (75)
for the structure constants of SU(3), we re-express the octe t components of the scalar quark densities
as
Sa(y) = −i
3
8∑
b,c=1
fabc[QbV (t),S c(y)]. (76)
In the chiral limit the ground state is necessarily invarian t under SU(3) V [Vafa and Witten, 1984],
i.e., QaV |0⟩= 0, and we obtain from Eq. (76)
⟨0|Sa(y)|0⟩= ⟨0|Sa(0)|0⟩ ≡ ⟨Sa⟩= 0, a = 1, · · ·, 8, (77)
where we made use of translational invariance of the ground s tate. As an intermediate result we see
that the octet components of the scalar quark condensate must vanish in the chiral limit. From Eq.
(77), we obtain for a = 3
⟨¯uu⟩ − ⟨¯dd⟩= 0,
i.e. ⟨¯uu⟩= ⟨¯dd⟩and for a = 8
⟨¯uu⟩+ ⟨¯dd⟩ −2⟨¯ss⟩= 0,
i.e. ⟨¯uu⟩= ⟨¯dd⟩= ⟨¯ss⟩.
Because of Eq. (73) a similar argument cannot be used for the s inglet condensate, and if we assume
a non-vanishing singlet scalar quark condensate in the chir al limit, we ﬁnd using ⟨¯uu⟩= ⟨¯dd⟩= ⟨¯ss⟩:
0 ⁄= ⟨¯qq⟩= ⟨¯uu + ¯dd + ¯ss⟩= 3⟨¯uu⟩= 3⟨¯dd⟩= 3⟨¯ss⟩. (78)
Finally, we make use of (no summation implied!)
(i)2[γ5
λa
2 ,γ 0γ5λa] = λ2
aγ0
in combination with
λ2
1 =λ2
2 =λ2
3 =



1 0 0
0 1 0
0 0 0


, λ2
4 =λ2
5 =



1 0 0
0 0 0
0 0 1


, λ2
6 =λ2
7 =



0 0 0
0 1 0
0 0 1


, λ2
8 = 1
3



1 0 0
0 1 0
0 0 4



to obtain
i[QaA(t),P a(y)] =









¯uu + ¯dd, a = 1, 2, 3
¯uu + ¯ss, a = 4, 5
¯dd + ¯ss, a = 6, 7
1
3 (¯uu + ¯dd + 4¯ss), a = 8
(79)
where we have suppressed the y dependence on the right-hand side. We evaluate Eq. (79) for a ground
state which is invariant under SU(3) V , assuming a non-vanishing singlet scalar quark condensate ,
⟨0|i[QaA(t),P a(y)]|0⟩= 2
3 ⟨¯qq⟩, a = 1, · · ·, 8, (80)
20
where, because of translational invariance, the right-han d side is independent of y. Inserting a complete
set of states into the commutator of Eq. (80) yields that both the pseudoscalar density Pa(y) as well
as the axial charge operators QaA must have a non-vanishing matrix element between the vacuum and
massless one-particle states |φb⟩. In particular, because of Lorentz covariance, the matrix e lement of the
axial-vector current operator between the vacuum and these massless states, appropriately normalized,
can be written as
⟨0|Aµ
a(0)|φb(p)⟩=ipµF0δab, (81)
where F0 ≈ 93 MeV denotes the “decay” constant of the Goldstone bosons i n the chiral limit. From
Eq. (81) we see that a non-zero value of F0 is a necessary and suﬃcient criterion for spontaneous chira l
symmetry breaking. On the other hand, because of Eq. (80) a no n-vanishing scalar quark condensate
⟨¯qq⟩is a suﬃcient (but not a necessary) condition for a spontaneo us symmetry breakdown in QCD.
