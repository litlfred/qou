---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-021-power-counting-scheme
section_title: "Power-counting scheme"
section_number: null
pages: 35-37
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
The Lagrangian Leﬀ of mesonic chiral perturbation theory is organized as a stri ng of terms with an
increasing number of derivatives and quark-mass terms,
Leﬀ = L2 + L4 + L6 + · · ·, (136)
where the subscripts refer to the order in the momentum and qu ark-mass expansion. The index 2, for
example, denotes either two derivatives or one quark-mass t erm. In terms of Feynman rules, derivatives
generate four-momenta. A quark-mass term counts as two deri vatives because of Eqs. (105) - (107)
(M 2 ∼ mq) in combination with the on-shell condition p2 = M 2. We will generically count a small
four-momentum—or the corresponding derivative—and a Gold stone-boson mass as of O(q). The chiral
orders in Eq. (136) are all even [ O(q2k), k ≥ 1], because Lorentz indices of derivatives always have to
be contracted and quark-mass terms count as O(q2).
Besides the knowledge of the most general Lagrangian, we nee d a method which allows one to assess
the importance of diﬀerent renormalized diagrams contribu ting to a given process. For that purpose
we analyze a given diagram under a simultaneous re-scaling o f all external momenta, pi ↦→tpi, and
the light-quark masses, mq ↦→t2mq (corresponds to M 2 ↦→t2M 2). The chiral dimension D of a given
diagram is deﬁned as
M(tpi,t 2mq,tµ ) = tDM(pi,m q,µ ) = O(qD). (137)
35
2 2
D = 4 · 2 − 2 · 3 + 2· 2 = 6.
42
D = 4·2−2·3+2·1+4·1 = 8.
22
D = 4 ·4−2·5+2 ·2 = 10.
Figure 6: Application of the power-counting formula of Eq. ( 138) in n = 4 dimensions.
For small enough momenta (and masses) contributions with in creasing D become less important. The
chiral dimension is given by
D = nNL − 2NI +
∞∑
k=1
2kN2k (138)
= 2 + ( n − 2)NL +
∞∑
k=1
2(k − 1)N2k (139)
≥ 2 in 4 dimensions ,
where n is the number of space-time dimensions, NL the number of independent loops, NI the number
of internal Goldstone boson lines, and N2k the number of vertices from L2k. Equation (139) establishes
a relation between the momentum and loop expansion, because at each chiral order, the maximum
number of loops is bounded from above. In other words, we have a perturbative scheme in terms of
external momenta and masses which are small compared to some scale [here: Λ χ = 4πF0 = O (1 GeV)].
Examples of the application of the power-counting formula a re shown in Fig. 6.
In order to prove the power-counting formula we start from th e Feynman rules for evaluating the
S-matrix element and investigate the behavior of the indivi dual building blocks. Internal lines are
described by a propagator in n dimensions which under re-scaling behaves as
∫ dnk
(2π)n
i
k2 −M 2 +i0+ →
∫ dnk
(2π)n
i
t2(k2/t2 −M 2 +i0+)
k =tk′
= tn−2
∫ dnk′
(2π)n
i
k′2 −M 2 +i0+.
Vertices with 2k derivatives or k quark-mass terms re-scale as
δn(q)q2k →t2k−nδn(q)q2k,
sincep →tp ifq is an external momentum, and k =tk′ ifq is an internal momentum (see above). These
are the rules to calculate S ∼ δn(P )M. We need to add n to compensate for the overall momentum-
conserving delta function. Applying these rules, the scali ng behavior of the contribution to M of a
given diagram reads
D =n + (n − 2)NI +
∞∑
k=1
N2k(2k −n).
The relation between the number of independent loops, the nu mber of internal lines, and the total
number of vertices NV =∑ ∞
k=1N2k is given by NL =NI − (NV − 1). The product of NV momentum-
conservingδ functions contains overall momentum conservation. Theref ore, one has NV − 1 rather than
NV restrictions on the internal momenta. Applying
−n
∞∑
k=1
N2k = −nNV =n(NL −NI − 1)
36
/BE /CZ
D = 0 − 0 + 2k = 2k =
{
0 for k = 0,
2 for k = 1.
/BE /CZ /BE /CZ
D = 4−2·2+2·(2k) = 4k =
{
0 for k = 0,
4 for k = 1.
Figure 7: The loop diagram is only suppressed if kmin> 0.
results in Eq. (138):
D =nNL − 2NI +
∞∑
k=1
2kN2k.
On the other hand, applying
−n
∞∑
k=1
N2k = −2
∞∑
k=1
N2k + (n − 2)(NL −NI − 1),
results in Eq. (139):
D = 2 +
∞∑
k=1
2(k − 1)N2k + (n − 2)NL.
In particular, diagrams containing loops are suppressed du e to the term 2 NL in four dimensions.
Note that a minimal k > 0 is important. Otherwise, an inﬁnite number of diagrams con taining
vertices from L0 would have to be summed (see Fig. 7). This is for example the ca se when dealing with
the nucleon-nucleon interaction.
