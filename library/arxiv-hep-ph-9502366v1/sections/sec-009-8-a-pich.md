---
doc_id: arxiv-hep-ph-9502366v1
doc_title: ""
section_id: sec-009-8-a-pich
section_title: "A Pich"
section_number: 8
pages: 8-9
source_pdf: 9502366v1.pdf
source_sha256: 56df064956ca03f8
doc_brief: "An introduction to the basic ideas and methods of Chiral Perturbation Theory is presented."
---
We can use this symmetry to build a generalized eﬀective Lagr angian for the Goldstone
bosons, in the presence of external sources. Note that to res pect the local invariance,
the gauge ﬁelds vµ, aµ can only appear through the covariant derivatives
DµU = ∂µU − irµU + iU ℓµ , D µU † = ∂µU † + iU †rµ − iℓµU † , (3.15)
and through the ﬁeld strength tensors
F µν
L = ∂µℓν − ∂νℓµ − i[ℓµ, ℓν] , F µν
R = ∂µrν − ∂νrµ − i[rµ, rν] . (3.16)
At lowest order in momenta, the more general eﬀective Lagran gian consistent with
Lorentz invariance and (local) chiral symmetry is of the for m (Gasser and Leutwyler
1985)
L2 = f 2
4 ⟨DµU †DµU + U †χ + χ†U ⟩, (3.17)
where
χ = 2 B0 (s + ip), (3.18)
and B0 is a constant, which, like f , is not ﬁxed by symmetry requirements alone.
Once special directions in ﬂavour space, like the ones in equ ation (3.11), are
selected for the external ﬁelds, chiral symmetry is of cours e explicitly broken. The
important point is that (3.17) then breaks the symmetry in ex actly the same way as
the fundamental short-distance Lagrangian (3.10) does.
The power of the external ﬁeld technique becomes obvious whe n computing the
chiral Noether currents. The Green functions are obtained a s functional derivatives
of the generating functional Z[v, a, s, p], deﬁned via the path-integral formula
exp {iZ} =
∫
Dq D ¯q DGµ exp
{
i
∫
d4x LQCD
}
=
∫
DU exp
{
i
∫
d4x Leﬀ
}
. (3.19)
At lowest order in momenta, the generating functional reduc es to the classical action
S2 =
∫
d4x L2; therefore, the currents can be trivially computed by takin g the
appropriate derivatives with respect to the external ﬁelds :
J µ
L
.= δS2
δℓµ
= i
2 f 2DµU †U = f√
2DµΦ − i
2
(
Φ
↔
Dµ Φ
)
+ O(Φ 3/f ),
J µ
R
.= δS2
δrµ
= i
2 f 2DµU U† = − f√
2
DµΦ − i
2
(
Φ
↔
Dµ Φ
)
+ O(Φ 3/f ).
(3.20)
The physical meaning of the chiral coupling f is now obvious; at O(p2), f equals
the pion decay constant, f = fπ = 92.4 MeV, deﬁned as
⟨0|(J µ
A)12|π+⟩ ≡i
√
2fπpµ. (3.21)
Chiral Perturbation Theory 9
Similarly, by taking derivatives with respect to the extern al scalar and pseudoscalar
sources,
¯qj
Lqi
R
.= − δS2
δ(s − ip)ji = − f 2
