---
doc_id: arxiv-hep-th-9310070v1
doc_title: "Quantum dilogarithm"
section_id: page-007
section_title: "Page 7"
section_number: null
pages: 7-7
source_pdf: 9310070v1.pdf
source_sha256: b979ebf2f47a4653
toc_source: undetermined
doc_brief: "Quantum dilogarithm — A quantum generalization of Rogers’ ﬁve term, or “pentagon” dilogarithm identity is suggested. It is shown that the classical limit gives usual Rogers’ identity."
---
To deﬁne the “symbol” of a ﬁnite dimensional operator, in analogy with Section 2, con-
sider two basis sets {|n⟩} and {|m⟩}, n, m ∈ZN, which diagonalize operators ˆU and ˆV ,
respectively:
⟨n| ˆU|n′⟩= ωn−1/2δn,n′,
⟨n| ˆV |n′⟩= ω−1/2δn,n′+1,
(3.15a)
⟨m| ˆV |m′⟩= ωm−1/2δm,m′,
⟨m| ˆU|m′⟩= ω−1/2δm,m′−1.
(3.15b)
The scalar products are given by
⟨n|n′⟩= δn,n′,
⟨n|m⟩= ω−nm,
⟨m|m′⟩= Nδm,m′,
(3.16)
while the decompositions of the unit operator are
1 =
X
n∈ZN
|n⟩⟨n| = 1
N
X
m∈ZN
|m⟩⟨m|.
(3.17)
The “U-V” symbol of an operator, ˆA, is deﬁned as a mixed matrix element
( ˆA)n,m = ⟨n| ˆA|m⟩
⟨n|m⟩,
(3.18)
the symbol of a product of ˆA and ˆB being
( ˆA ˆB)n,m = 1
N
X
n′,m′∈ZN
ω−(n−n′)(m′−m)( ˆA)n,m′( ˆB)n′,m.
(3.19)
Calculating the symbol of (3.9), we will have a direct analog for (2.16) with a double
sum instead of integrals. To apply the stationary phase method, we have to convert these
summations into integrals. For this purpose, ﬁrst let us write the following equality:
N−1
X
m=0
1
z −ωm =
N
z(1 −z−N)
(3.20)
for any complex z. Then, using Cauchy’s formula and (3.20), we have with exponential
accuracy
N−1
X
m=0
f(ωm) ∼N
2πi
I
S1 f(z)dz
z ,
N →∞
(3.21)
for any function f(z). Repeating calculations from Section 2, using (3.21), one can show
that (3.9) in the limit N →∞is reduced to (1.3b) as well.
6
