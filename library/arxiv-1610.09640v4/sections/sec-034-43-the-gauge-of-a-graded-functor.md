---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-034-43-the-gauge-of-a-graded-functor
section_title: "The Gauge of a Graded Functor"
section_number: 4.3
pages: 83-84
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
M and a DG ringA. The next deﬁnition is new.
Deﬁnition 4.3.1.Let F : C(A, M)→C(B, N) be a graded functor. For every
object M∈C(A, M) let
γF,M := dF(M)−F (dM)∈HomB,N
(
F (M),F (M)
{1
.
The collection of morphisms
γF :={γF,M}M∈C(A,M)
is called thegauge ofF.
The next theorem is due to R. Vyas.
Theorem 4.3.2. The following two conditions are equivalent for a graded functor
F : C(A, M)→C(B, N).
(i) F is a DG functor.
(ii) The gaugeγF is a degree1 morphism of graded functorsγF :F→F.
Proof. Recall thatF is a DG functor (condition (i)) iﬀ
(4.3.3) (F◦dA,M)(φ) = (dB,N◦F )(φ)
for everyφ∈HomA,M(M0,M 1)i. AndγF is a degree1 morphism of graded functors
(condition (ii)) iﬀ
(4.3.4) γF,M1◦F (φ) = (−1)i·F (φ)◦γF,M0
for every suchφ.
Here is the calculation. BecauseF is a graded functor, we get
(4.3.5)
F
(
dA,M(φ)
{
=F
(
dM1◦φ−(−1)i·φ◦dM0
{
=F (dM1)◦F (φ)−(−1)i·F (φ)◦F (dM0)
and
(4.3.6) dB,N
(
F (φ)
{
= dF(M1)◦F (φ)−(−1)i·F (φ)◦dF(M0).
Using equations (4.3.5) and (4.3.6), and the deﬁnition ofγF, we obtain
(4.3.7)
(F◦dA,M−dB,N◦F )(φ) =F
(
dA,M(φ)
{
−dB,N
(
F (φ)
{
=
(
F (dM1)−dF(M1)
{
◦F (φ)−(−1)i·F (φ)◦
(
F (dM0)−dF(M0)
{
=−γF,M1◦F (φ) + (−1)i·F (φ)◦γF,M0.
Finally, the vanishing of the ﬁrst expression in (4.3.7) is the same as equality
in (4.3.3); whereas the vanishing of the last expression in (4.3.7) is the same as
equality in (4.3.4). □
83
Derived Categories | Amnon Yekutieli | 14 Apr 2019
