---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-007-c-model-comparison-for-nonlinear-channel-equalis
section_title: "Model Comparison for Nonlinear Channel Equalisation"
section_number: C
pages: 13-13
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
In Section VI-C we compared the proposed Gaussian kernel
(real- and quaternion-valued) algorithms against strictly-linear
and widely-linear models. The underlying idea is that a novel
nonlinear estimation algorithm is only justiﬁed if it outper-
forms existing (strictly and w idely) linear approaches. A com-
pact description of the models implemented in Section VI-C,
together with their optimal leas t-squares parameters, is given
as follows
• Strictly linear:
ˆxL = As
A = (SH S + ρ1I)−1SH X
S =[ s1,..., sN ],
• Widely linear:
ˆxWL = Wsa
W =
⎥
SaH Sa + ρ2I
⎦−1SaH X
Sa =[ sa
1,..., sa
N ],
• Real Gaussian kernel (Eq. (13)):
ˆxRG =
N∑
i=1
ai KRG (si, s)
[a1,..., aN ]T = (KH K + ρ3I)−1KH X
Ki, j = KRG (si, sj ),
• Quaternion Gaussian kernel (Eq. (14)):
ˆxQG =
N∑
i=1
bi KQG (si, s)
[b1,..., bN ]T = (KH K + ρ4I)−1KH X
Ki, j = KQG (si, sj ).
Recall that ρ1,ρ 2,ρ 3,ρ 4 > 0 are regularisation factors, and
X =[ xT
1 ,..., xT
N ]T is the desired output data.
