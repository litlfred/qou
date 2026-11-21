---
doc_id: arxiv-hep-ph-9511320v1
doc_title: "Chiral Lagrangians for Baryons Coupled to Massive Spin-1 Fields"
section_id: sec-012-b-on-the-equivalence-from-dual-transformations
section_title: "On the Equivalence from Dual Transformations"
section_number: B
pages: 22-26
source_pdf: 9511320v1.pdf
source_sha256: 4336112cecabdfdf
toc_source: inferred
doc_brief: "Chiral Lagrangians for Baryons Coupled to Massive Spin-1 Fields — We analyze the eﬀective low–energy ﬁeld theory of Goldstone bosons and baryons chirally coupled to massive spin–1 ﬁelds."
---
On the Equivalence from Dual Transformations
Here, we wish to critically examine the approach of Ref.[13], were it was ar-
gued that the equivalence between the tensor and vector ﬁeld formulations
can be shown formally by using path integral methods and a set of dual trans-
formations as motivated by e.g. Refs.[26],[27]. The starting point of Ref.[13]
is the generating functional in the presence of Goldstone bosons and external
vector and axial–vector sources,
Z[uµ, f +
µν] =
Z
[DVµ] δ(∂µV µ)eiR
d4x LV ,
(B.1)
where LV denotes the meson Lagrangian of Goldstone bosons chirally coupled
to massive spin–1 ﬁelds in the vector formulation. First, we wish to examine the
role of the δ–function which ensures transversality of the vector ﬁeld. From
the free part of the Lagrangian, Eq.(24), we derive the equation of motion
(eom), the well–known Proca equation,
✷V a
ν −∂ν (∂· V a) + M2
V V a
ν = 0 ,
(B.2)
which for MV̸ = 0 clearly leads to the transversality condition, ∂· V a = 0.
Let us now examine the generating functional more closely. Denote by V 0
µ the
ﬁeld which fulﬁlls the equation of motion (we drop the ﬂavor index ′a′). One
ﬁnds for the eﬀective action expanded aroung the classical solution
S[Vµ] =
Z
d4x LV = S[V 0
µ ] +
Z
d4x (Vµ −V 0
µ ) δS
δVµ

V 0
µ
+ 1
2
Z
d4x d4y (Vµ −V 0
µ )(x) (Vν −V 0
ν )(y)
δ2S
δVµδVν
(x, y)

V 0
µ
,
(B.3)
which using the eom leads to the generating functional
Z[uµ, f +
µν] = exp(iS[V 0
µ ]) det(M)−1/2 ,
(B.4)
with M = (−i/2)[(✷+M2
V )gµν −∂µ∂ν]. Neglecting loops with spin–1 mesons,
we have det M = 1 and arrive at
Z[uµ, f +
µν] = exp(iS[V 0
µ ]) =
Z
[DVµ] δ(Vµ −V 0
µ ) eiR
d4x LV ,
(B.5)
which diﬀers from Eq.(B.1) by the argument of the δ–function. To further
sharpen this constrast, let us perform the following substitution
V µ →V µ′ = V µ +
fV
√
2M2
V
∂νf νµ
+ +
igV
√
2M2
V
∂ν[uν, uµ] ,
(B.6)
which also deﬁnes a transverse ﬁeld and diﬀers in the eom from the original
one by terms of order O(q5) (and higher). To the order we are working and
for the processes we are considering, one has
L(Vµ) = L(Vµ
′)
(B.7)
so that the generating functional can also be cast in the form
Z[uµ, f +
µν] =
Z
[DVµ] δ((✷+ M2
V ) Vµ −∂µ∂· V ) eiR
d4x LV .
(B.8)
The two representations, Eq.(B.5) and Eq.(B.8), are obviously equivalent as
long as Vµ and V ′
µ fulﬁll the respective eom. This also ensures tranversality.
However, the argument can not be reversed, not any ﬁeld which obeys ∂·V = 0
is a solution of the eom. This is in contrast to the starting point of Ref.[13],
Eq.(B.1).
We can also make contact to the tensor ﬁeld formulation. We observe that
δ((✷+ M2
V ) Vµ −∂µ∂· V ) = δ(∂νVνµ + M2
V Vµ)
∼δ

Vµ +
1
M2
V
∂λ Vλµ

.
(B.9)
Consider now Vµν as the fundamental degree of freedom (instead of Vµ). This
leads to the following generating functional 7
exp (−i S[V 0
µν] ) =
Z
[DVµ] δ

Vµ +
1
M2
V
∂λ Vλµ

e−iR
d4x LV ,
(B.10)
with (it is straightforward to generalize this argument and include the covari-
ant instead of the partial derivative, ∂µ →Dµ)
L[Vµν] = −1
4Tr

VµνV µν

+
1
2M2
V
Tr

DλV λµDρVρµ

−Tr

Vµν Jµν

.
(B.11)
7 The sign in the exponential is derived from Z[uµ, f +
µν]∗= Z[uµ, f +
µν] which can
always be achieved by an appropriate choice of the phase of the in–state |0 , in >.
We make the ﬁeld redeﬁnition
˜Wµν ≡
1
MV
Vµν
(B.12)
where ˜Wµν fulﬁlls the following eom,
∂µ

∂µ∂ρ ˜Wρν −∂ν∂ρ ˜Wρµ + M2
V ˜Wµν

= 0 .
(B.13)
The term in the curly brackets is nothing but the eom for the antisymmetric
tensor ﬁeld, cf. the appendix of Ref.[9]. This can be used to show the formal
(symbolic) equivalence
Z[uµ, f +
µν] = exp ( i S[V 0
µ ] ) = exp ( i S′[ ˜W 0
µν] ) ,
(B.14)
provided one substitutes the vector ﬁeld and its respective ﬁeld strength tensor
in the Lagrangian as follows
LV [Vµ, Vµν] →−LV

−1
MV
Dλ ˜Wλµ, MV ˜Wµν

.
(B.15)
Therefore, the rather conventional treatment of the path integral presented
here leads to
Z[uµ, f +
µν] =
Z
[DVµ] δ

Vµ +
1
M2
V
DλVλµ

e iR
d4x LV .
(B.16)
In Ref.[13], an extra integration over the ﬁeld Hµν,
R [DHµν], is performed.
This additional integration allows to produce additional constant terms in the
Goldstone boson–spin–1 Lagrangian and is at the heart of the formal equiv-
alence. However, the coeﬃcients of the local contact terms can only be ﬁxed
since it is known that the tensor formulation indeed gives the correct result
(for e.g. the pion radius). We remark here that in the papers on dual transfor-
mations, the components of the ﬁeld strength tensor are in general not treated
as a degrees of freedom independent of the vector ﬁeld components. Let us
summarize our observations. Starting from Eq.(B.16) and considering Vµν as
the fundamental object, we could introduce (by rescaling) the ﬁeld ˜Wµν which
obeys the eom of the antisymmetric tensor ﬁeld. Furthermore, the Lagrangian
can be shown to be identical to the one in tensor ﬁeld formulation. This allows
to identify ˜Wµν with the fundamental antisymmetric tensor ﬁeld Wµν up to an
overall constant which can be absorbed in the coupling constants appearing
in the current Jµν. This equivalence is, however, formal. The complete equiva-
lence as discussed in Ref.[13] can only be achieved if one treats the vector ﬁeld
Vµ and the vector DρHρµ appearing in the dual transfomation as independent
degrees of freedom. Again, this does not ﬁx the coeﬃcients of the local contact
terms, for doing that, arguments like in Ref.[10] have to be invoked.
References
[1] J. Gasser, M.E. Sainio and A. ˇSvarc, Nucl. Phys. B307 (1988) 779
[2] E. Jenkins and A.V. Manohar, Phys. Lett. B255 (1991) 558
[3] E. Jenkins and A.V. Manohar, in “Eﬀective Field Theories of the Standard
Model”, ed. Ulf-G. Meißner, World Scientiﬁc, Singapore, 1992
[4] V. Bernard, N. Kaiser, J. Kambor and Ulf-G. Meißner, Nucl. Phys. B388 (1992)
315
[5] V. Bernard, N. Kaiser and Ulf-G. Meißner, Int. J. Mod. Phys. E4 (1995) 193
[6] S. Weinberg, Physica 96A (1979) 327
[7] J. Gasser and H. Leutwyler, Ann. Phys. (N.Y.) 158 (1984) 142
[8] J. Gasser and H. Leutwyler, Nucl. Phys. B250 (1985) 465
[9] G. Ecker, J. Gasser, A. Pich and E. de Rafael, Nucl. Phys. B321 (1989) 311
[10] G. Ecker, J. Gasser, H. Leutwyler, A. Pich and E. de Rafael, Phys. Lett. B223
(1989) 425
[11] J.F. Donoghue, C. Ramirez and G. Valencia, Phys. Rev. D39 (1989) 1947
[12] Ulf-G. Meißner, Phys. Rep. 161 (1988) 213
[13] J. Bijnens and E. Pallante, preprint NORDITA-95/63 [hep-ph/9510338]
[14] G. Ecker, Phys. Lett. B336 (1994) 508
[15] G. Ecker and M. Mojzis, Wien preprint UWThPh-1995-22 [hep-ph/9508204]
[16] A. Krause, Helv. Physica Acta 63 (1990) 3
[17] S. Weinberg, Phys. Rev. 166 (1968) 1568
[18] V. Bernard, N. Kaiser and Ulf-G. Meißner, Phys. Lett. B309 (1993) 421
[19] V. Bernard, N. Kaiser and Ulf-G. Meißner, Nucl. Phys. B457 (1995) 147
[20] Ulf-G. Meißner, in “Chiral Dynamics: Theory and Experiment”, A.M. Bernstein
and B.R. Holstein (eds.), Springer, Berlin, 1995
[21] Ulf-G. Meißner, Int. J. Mod. Phys. E1 (1992) 561
[22] K. Kawarabayashi and M. Suzuki, Phys. Rev. Lett. 16 (1966) 255;
Fayyazuddin and Riazuddin, Phys. Rev. 147 (1966) 1071
[23] V. Bernard, N. Kaiser and Ulf-G. Meißner, Z. Phys. C60 (1993) 111
[24] M. Bando, T. Kugo and K. Yamawaki, Phys. Rep. 164 (1988) 217
[25] P. Mergell, Ulf-G. Meißner and D. Drechsel, preprint MKPH-T-95-07 and TK
95-15, 1995, Nucl. Phys. A (in print) [hep-ph/9506375]
[26] P.K. Townsend, K. Pilch and P. van Nieuwenhuizen, Phys.Lett. B136 (1984)
38
[27] S. Deser and R. Jackiw, Phys.Lett. B139 (1984) 371
