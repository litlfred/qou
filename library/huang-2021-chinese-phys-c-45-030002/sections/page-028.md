---
doc_id: huang-2021-chinese-phys-c-45-030002
doc_title: "The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures"
section_id: page-028
section_title: "Page 28"
section_number: null
pages: 28-28
source_pdf: Huang_2021_Chinese_Phys._C_45_030002.pdf
source_sha256: 1dd3329ed87476c8
toc_source: undetermined
doc_brief: "The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures — 343 sections: Page 1; Page 2; Page 3"
---
Chinese Physics C
Vol. 45, No. 3 (2021) 030002
In the original paper [2004Ra33], this equation is given
as:
13C+H−14 N = 8105.86288(10) µu,
which diﬀers by 12(10) nu from our calculation. The dif-
ference is because we used the updated molecular bind-
ing energy from Ref. [36, 38]. In this case, the molecular
binding energy is 170 times larger than the uncertainty,
and even the updates of the molecular energies have sig-
niﬁcant impact on the deduced values.
Appendix B
Mixtures of isomers or of
isobars in mass spectrometry
In cases where two or more unresolved lines may com-
bine into a single one in an observed spectrum, while one
cannot decide which ones are present and in which pro-
portion, a special procedure has to be used.
The ﬁrst goal is to determine what is the most prob-
able value Mexp that will be observed in the measure-
ment, and what is the uncertainty σ of this prediction.
We assume that all the lines may contribute and that
all contributions have equal probabilities. The measured
mass reﬂects the mixing. We call M0 the mass of the
lowest line, and M1,M2,M3, . . . the masses of the other
lines. For a given composition of the mixture, the result-
ing mass m is given by
m = (1−
n
∑
i=1
xi)M0+
n
∑
i=1
xiMi ,
with
{
0 ≤xi ≤1
∑n
i=1 xi ≤1
(27)
in which the relative unknown contributions x1,x2,x3,
. . . have each a uniform distribution of probability within
the allowed range.
If P(m) is the normalized probability of measuring
the value m, then :
M
=
∫
P(m)mdm
(28)
and
σ2
=
∫
P(m)(m−M)2 dm.
(29)
It is thus assumed that the experimentally measured
mass will be Mexp = M, and that σ, which reﬂects the
uncertainty on the composition of the mixture, will have
to be quadratically added to the experimental uncertain-
ties.
B.1
Case of 2 spectral lines
In the case of two lines, one simply gets
m = (1−x1)M0 +x1M1 with
0 ≤x1 ≤1.
(30)
The relation between m and x1 is biunivocal so that
P(m) =
{
1/(M1 −M0)
if M0 ≤m ≤M1,
0
elsewhere
(31)
i.e. a rectangular distribution, and one obtains:
Mexp
=
1
2(M0 +M1),
(32)
σ
=
√
3
6 (M1 −M0) = 0.290 (M1 −M0).
Therefore, the ground state mass M0±σ0 can be de-
termined from the measured mass Mexp ± σexp and the
knowledge of the excitation energies E1±σ1 with follow-
ing equations:
M0
=
Mexp −1
2E1 ,
σ2
=
1
12E2
1
or
σ = 0.29E1 ,
σ2
0
=
σ2
exp +(1
2σ1)2 +σ2 .
B.2
Case of 3 spectral lines
In the case of three spectral lines, we derive from
Eq. 27:
m = (1−x1 −x2)M0 +x1M1 +x2M2 ,
(33)
with





0 ≤x1 ≤1
0 ≤x2 ≤1
0 ≤x1 +x2 ≤1.
(34)
After normalization, one gets:
P(m) =
2k
M2 −M0
,
(35)
with
{
k = (m−M0)/(M1 −M0) if M0 ≤m ≤M1
k = (M2 −m)/(M2 −M1) if M1 ≤m ≤M2
(36)
and ﬁnally:
Mexp = 1
3(M0 +M1 +M2)
(37)
σ =
√
2
6
√
M 2
0 +M 2
1 +M 2
2 −M0M1 −M1M2 −M2M0 .
The ground state mass M0 ± σ0 can be determined
from the measured mass Mexp ±σexp and the knowledge
of the excitation energies E1 ±σ1 and E2 ±σ2 :
M0
=
Mexp −1
3(E1 +E2),
σ2
=
1
18(E2
1 +E2
2 −E1E2)
or
σ = 0.236
√
E2
1 +E2
2 −E1E2 ,
σ2
0
=
σ2
exp +(1
3σ1)2 +(1
3σ2)2 +σ2 .
030002-27
