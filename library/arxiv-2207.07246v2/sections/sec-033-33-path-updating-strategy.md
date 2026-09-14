---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-033-33-path-updating-strategy
section_title: "Path Updating Strategy"
section_number: 3.3
pages: 87-88
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
In each type of sampling, after we judge whether to accept the new l and r order
in the trial wave function or not, we mark the order after judgement as l and r. In
order to make the computation fast, as illustrated in Fig. 3.4 by the blue and yellow
bands with texture, we store all the states from |ψr
0(R)⟩ to|ψr
N(R)⟩ and|ψl
0(R)⟩ to
|ψl
N(R)⟩, by storing all the coeﬃcients from φr
0(R,S ) to φr
N(R,S ) and from φl
0(R,S )
to φl
N(R,S )|S⟩ in the arrays. We also store fV
lr (R) which is calculated by Eq.(2.109).
I I+2 I+1 I+3 I+7 I+6 I+5 I+4 I+8 0 N
I I+2 I+1 I+3 I+7 I+6 I+5 I+4 I+8 0 N
Figure 3.4: Illustration of the path updating.
Then, we propose new moves asR′. In order to judge if the new spatial conﬁguration
R′ is accepted or not, we need to calculate fV
lr (R′)/fV
lr (R). For theR′, it is usually
the same as R except for several contiguous beads. For example in the multi-level
sampling with level n, for a chosen integer I, we only propose new conﬁgurations from
bead I + 1 to bead I + 2n− 1 inR′, and the rest of the beads remain the same as
those inR. When we propose new moves from bead I + 1 to bead I + 2n− 1, we only
need to calculate from right to left, from φr
I+2n−1(R′,S ) untilφr
I+1(R′,S ), by using the
recursion relations Eq.(2.112) starting from φr
I+2n(R,S ) which is already stored. Then
we calculate fV
lr (R′) =
⟨
ψl′
I (R)|G|ψr′
I+1(R′)
⟩
, and since fV
lr (R) is also already stored,
77
we can readily calculate fV
l′r′(R′)/fV
lr (R). If the proposed new moves are accepted, we
update all the rest beads. From right to left we update from φr
I(R′,S ) untilφr
0(R′,S ),
and from left to right we update from φr
I+1(R′,S ) untilφr
N(R′,S ). In Fig. 3.4, the
corresponding updated parts of the path from left to right are marked as green band,
and those updated from right to left are marked as the red band.
The path updating process is the most time-consuming part, especially if the
number of beadsN is large. So we ﬁnd a proper n in multi-level sampling to make sure
n is big enough to ensure the acceptance rate is relatively low, in order to optimize
the decorrelation of the path within the computer time.
