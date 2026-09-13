---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-024-274-calculating-the-samples
section_title: "Calculating the Samples"
section_number: 2.7.4
pages: 57-59
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
The reason to recast Eq.(2.15) into the form of Eq.(2.87) is because once we have
the detailed form of Eq.(2.92), the normalized probability distribution Plr(R), we can
sample it by using suitable algorithms. And then after we take enough uncorrelated
47
samples of Alr(R) andBlr(R) in Eq.(2.87) from the probability distribution Plr(R) in
Eq.(2.92), we have the corresponding average values⟨A⟩ forAlr(R) and⟨B⟩ forBlr(R)
and their errors σA and σB, ﬁnally⟨ ˆO(∆τ)⟩ and its error bar σ can be estimated by,
⟨ ˆO(∆τ)⟩ =
∑
l
∑
r
∫
dRAlr(R)Plr(R)∑
l
∑
r
∫
dRBlr(R)Plr(R) =⟨Alr(R)⟩
⟨Blr(R)⟩
⏐⏐⏐⏐
{l,r,R}∈Plr(R)
=⟨A⟩
⟨B⟩ (2.114)
σ =
√[∂(⟨A⟩/⟨B⟩)
∂⟨A⟩ σA
]2
+
[∂(⟨A⟩/⟨B⟩)
∂⟨B⟩ σB
]2
=
√( σA
⟨B⟩
)2
+
(⟨A⟩σB
⟨B⟩2
)2
. (2.115)
Alternatively, we can also ﬁnd⟨ ˆO⟩ and its error bar σ from the block average of A
and B. For example we can arrange all the N samples of A and B into much smaller
blocks. Each block contain n samples of A and B. So there are nb =N/n blocks. We
can mark each of the block average as ¯An and ¯Bn. And the average of block average is
the average value, namely
⟨ ¯An⟩ =⟨A⟩, (2.116)
⟨ ¯Bn⟩ =⟨B⟩. (2.117)
The standard deviation of the nb samples of ¯An and ¯Bn are σAn and σBn. According
to central limit theorem (Negele and Orland (1998); Apaja (2009)), the independent
block averages of ¯An and ¯Bn each forms a gaussian distribution P ( ¯An) and P ( ¯Bn)
with average value⟨A⟩ and⟨B⟩ and their corresponding standard deviations are
σP ¯An
= σ ¯An
√nb
, (2.118)
σP ¯Bn
= σ ¯Bn
√nb
. (2.119)
Then we ﬁnd that,
⟨ ¯An
¯Bn
⟩
=
∫
d ¯And ¯Bn
¯An
¯Bn
P ( ¯An)P ( ¯Bn)
=
∫
d ¯An ¯AnP ( ¯An)
∫
d ¯Bn
1
¯Bn
P ( ¯Bn)
=⟨A⟩
∫
d ¯Bn
1
¯Bn
P ( ¯Bn). (2.120)
48
Note that when σPBn is small, the gaussian distribution P ( ¯Bn) becomes a δ function
δ( ¯Bn−⟨B⟩), so Eq.(2.120) in this case becomes,
⟨ ¯An
¯Bn
⟩
=⟨A⟩
∫
d ¯Bn
1
¯Bn
δ
( ¯Bn−⟨B⟩
)
=⟨A⟩
⟨B⟩ =⟨ ˆO⟩, (2.121)
and we can take the standard deviation of the mean of ¯An/ ¯Bn as the error bar σ. In
all cases we ensure that the number of samples is large enough that any bias from
dividing two stochastic quantities is smaller than the statistical error.
