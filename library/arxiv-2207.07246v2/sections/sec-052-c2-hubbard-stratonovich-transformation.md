---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-052-c2-hubbard-stratonovich-transformation
section_title: "C.2 Hubbard-Stratonovich Transformation"
section_number: null
pages: 145-147
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
The key of AFDMC is to reduce the quadratic dependence of operators to linear,
with the Hubbard-Stratonovich transformation,
e
O2
2 = 1√
2π
∫
dxe−x2
2 exO, (C.16)
such that the interaction between nucleons can be conveniently cast into the form of
DMC.
If possible, we can ﬁnd ways to write a Hamiltonian intoN operators with quadratic
dependence, that is
H = 1
2
N∑
j=1
λjO2
j, (C.17)
135
and then the DMC propagator(neglecting O(δt2)) can be written as
e−(H−ET )δt =
∫
dx1...dxN| {z }
dX
1
(2π)N/2e− 1
2
∑N
j=1x2
j
| {z }
P (X)
e−i ∑N
j=1xj
√
λjδtOjeETδt
| {z }
T (X)
, (C.18)
neglectingO(δt3/2), the normalized distribution ˜P (X) can be written as
˜P (X) = 1
(2π)N/2 exp



−1
2
N∑
j=1
[
xj +i
√
λδt⟨ΨT|Oj|RiSi⟩
⟨ΨT|RiSi⟩| {z }
⟨Oj⟩
]2



, (C.19)
which means thatχj≡xj +i
√
λδt⟨Oj⟩ is a gaussian random number with unit variance.
In other words, we choose each auxiliary ﬁeld xj by
xj =χj−i
√
λjδt⟨Oj⟩. (C.20)
We move each walker by such an operation
|R′
iS′
i⟩ =e−i ∑N
j=1xj
√
λjδtOj|RiSi⟩, (C.21)
and the weight of the new walker |R′
iS′
i⟩ is given by e−[EL(RiSi)−ET ]δt.
Hubbard-Stratonovich transformation can be mathematically understood as a
Fourier transform. Consider that if we deﬁne
O≡−i ˜O, (C.22)
F ( ˜O)≡e− ˜O2/2, (C.23)
the Fourier transform pair is
F ( ˜O) =
∫ dx
2πe−ix ˜O ˜F (x), (C.24)
˜F (x) =
∫
d ˜Oeix ˜OF ( ˜O) =
∫
d ˜Oeix ˜Oe− ˜O2/2 =
√
2πe−x2/2. (C.25)
Substituting Eq.(C.26) back to Eq.(C.24) we have
e− ˜O2/2 =
∫ dx√
2πe−x2/2e−ix ˜O, (C.26)
which is essentially the same as Eq.(C.16).
136
