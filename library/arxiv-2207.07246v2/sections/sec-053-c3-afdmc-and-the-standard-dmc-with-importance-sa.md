---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-053-c3-afdmc-and-the-standard-dmc-with-importance-sa
section_title: "C.3 AFDMC and the Standard DMC with Importance Sampling"
section_number: null
pages: 147-149
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
Let us consider the Hamiltonian
H =
A∑
j=1
3∑
α=1
p2
jα
2m +V (R), (C.27)
the approximated propagatore−(H−ET )δt after Hubbard-Stratonovich transformation is
e− ∑
j
∑
α
p2
jα
2mδte−[V (R)−ET ]δt =
∫ ∏
jα
dxjα
1√
2πe−
x2
jα
2
| {z }
dXP (X)
e−i
ℏpjαxjα
√
ℏ2δt
m
weight
z }| {
e−[V (R)−ET ]δt
| {z }
T (X)
. (C.28)
For the importance sampling case,
i
√
λjδt⟨Oj⟩ =i
√
δt
m
⟨ΨT|pjα|RS⟩
⟨ΨT|RS⟩
=i
√
δt
m
p†
jα⟨ΨT|RS⟩
⟨ΨT|RS⟩
=−
√
ℏ2δt
m
∂jα⟨ΨT|RS⟩
⟨ΨT|RS⟩ , (C.29)
and therefore the sampled auxiliary ﬁeld xjα are
xjα =χjα +
√
ℏ2δt
m
∂jα⟨ΨT|RS⟩
⟨ΨT|RS⟩ , (C.30)
the new walker|R′S′⟩ with weighte−[EL(RiSi)−ET ]δt is moved by the translation operator,
|R′S′⟩ =e−i
ℏ
∑
jαxjα
√
ℏ2δt
m pjα|RS⟩, (C.31)
which means that S′ =S and
R′
jα =Rjα +xjα
√
ℏ2δt
m
=Rjα +χjα
√
ℏ2δt
m + ℏ2δt
m
∂jα⟨ΨT|RS⟩
⟨ΨT|RS⟩ . (C.32)
This is exactly the standard DMC with importance sampling introduced in Sec.B.3.
137
C.4 Quadratic Form of the AV6’ Interaction
The Hamiltonian with the AV6’ interaction for A-particle system can be written as
H =
∑
iα
p2
iα
2m +
∑
i<j
vc(rij) + 1
2
∑
iα,jβ
Cσ
iα,jβσiασjβ
+ 1
2
∑
iα,jβ,γ
Cστ
iα,jβ(σiατiγ)(σjβτjγ) + 1
2
∑
iγ,jγ
Cτ
i,jτiγτjγ (C.33)
where the matrices are deﬁned as
Cσ
iα,jβ =vσ(rij)δαβ +vt(rij)(3ˆα· ˆrij ˆβ· ˆrij−δαβ),
Cστ
iα,jβ =vστ (rij)δαβ +vtτ(rij)(3ˆα· ˆrij ˆβ· ˆrij−δαβ),
Cτ
i,j =vτ(rij). (C.34)
Here α, β, γ refer to x, y and z components and ˆα, ˆβ refer to the corresponding unit
vector, and their nth eigenvectors and eigenvalues can be written as
∑
jβ
Cσ
iα,jβψσ(n)
jβ =λσ
nψσ(n)
iα ,
∑
jβ
Cστ
iα,jβψσ(n)
jβ =λστ
n ψστ (n)
iα ,
∑
j
Cτ
i,jψτ(n)
j =λτ
nψτ(n)
i . (C.35)
We deﬁne the following operators,
Oσ
n =
∑
iα
ψσ(n)
iα σiα,
Oστ
nβ =
∑
iα
ψστ (n)
iα σiατiβ,
Oτ
nα =
∑
i
ψτ(n)
i τiα, (C.36)
such that the Hamiltonian can now be written in a quadratic form
H =
A∑
i=1
3∑
α=1
p2
iα
2m +
∑
i<j
vc(rij) + 1
2
3A∑
n=1
λσ
n(Oσ
n)2
+ 1
2
A∑
n=1
3∑
α=1
λτ
n(Oτ
nα)2 + 1
2
3A∑
n=1
3∑
α=1
λστ
n (Oστ
nα)2 (C.37)
which can be conveniently used in AFDMC.
138
