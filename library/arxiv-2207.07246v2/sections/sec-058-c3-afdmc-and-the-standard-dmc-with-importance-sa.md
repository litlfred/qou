---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-058-c3-afdmc-and-the-standard-dmc-with-importance-sa
section_title: "C.3 AFDMC and the Standard DMC with Importance Sampling"
section_number: null
pages: 147-149
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 64 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
AFDMC and the Standard DMC with Importance Sampling
Let us consider the Hamiltonian
H =
A
X
j=1
3
X
α=1
p2
jα
2m + V (R),
(C.27)
the approximated propagator e−(H−ET )δt after Hubbard-Stratonovich transformation is
e−P
j
P
α
p2
jα
2m δte−[V (R)−ET ]δt =
Z Y
jα
dxjα
1
√
2πe−
x2
jα
2
|
{z
}
dXP(X)
e−i
ℏpjαxjα
q
ℏ2δt
m
weight
z
}|
{
e−[V (R)−ET ]δt
|
{z
}
T(X)
. (C.28)
For the importance sampling case,
i
p
λjδt⟨Oj⟩= i
r
δt
m
⟨ΨT|pjα|RS⟩
⟨ΨT|RS⟩
= i
r
δt
m
p†
jα⟨ΨT|RS⟩
⟨ΨT|RS⟩
= −
r
ℏ2δt
m
∂jα⟨ΨT|RS⟩
⟨ΨT|RS⟩,
(C.29)
and therefore the sampled auxiliary ﬁeld xjα are
xjα = χjα +
r
ℏ2δt
m
∂jα⟨ΨT|RS⟩
⟨ΨT|RS⟩,
(C.30)
the new walker |R′S′⟩with weight e−[EL(RiSi)−ET ]δt is moved by the translation operator,
|R′S′⟩= e−i
ℏ
P
jα xjα
q
ℏ2δt
m pjα|RS⟩,
(C.31)
which means that S′ = S and
R′
jα = Rjα + xjα
r
ℏ2δt
m
= Rjα + χjα
r
ℏ2δt
m + ℏ2δt
m
∂jα⟨ΨT|RS⟩
⟨ΨT|RS⟩.
(C.32)
This is exactly the standard DMC with importance sampling introduced in Sec.B.3.
137
C.4
Quadratic Form of the AV6’ Interaction
The Hamiltonian with the AV6’ interaction for A-particle system can be written as
H =
X
iα
p2
iα
2m +
X
i<j
vc(rij) + 1
2
X
iα,jβ
Cσ
iα,jβσiασjβ
+ 1
2
X
iα,jβ,γ
Cστ
iα,jβ(σiατiγ)(σjβτjγ) + 1
2
X
iγ,jγ
Cτ
i,jτiγτjγ
(C.33)
where the matrices are deﬁned as
Cσ
iα,jβ = vσ(rij)δαβ + vt(rij)(3ˆα · ˆrij ˆβ · ˆrij −δαβ),
Cστ
iα,jβ = vστ(rij)δαβ + vtτ(rij)(3ˆα · ˆrij ˆβ · ˆrij −δαβ),
Cτ
i,j = vτ(rij).
(C.34)
Here α, β, γ refer to x, y and z components and ˆα, ˆβ refer to the corresponding unit
vector, and their nth eigenvectors and eigenvalues can be written as
X
jβ
Cσ
iα,jβψσ(n)
jβ
= λσ
nψσ(n)
iα ,
X
jβ
Cστ
iα,jβψσ(n)
jβ
= λστ
n ψστ(n)
iα
,
X
j
Cτ
i,jψτ(n)
j
= λτ
nψτ(n)
i
.
(C.35)
We deﬁne the following operators,
Oσ
n =
X
iα
ψσ(n)
iα σiα,
Oστ
nβ =
X
iα
ψστ(n)
iα
σiατiβ,
Oτ
nα =
X
i
ψτ(n)
i
τiα,
(C.36)
such that the Hamiltonian can now be written in a quadratic form
H =
A
X
i=1
3
X
α=1
p2
iα
2m +
X
i<j
vc(rij) + 1
2
3A
X
n=1
λσ
n(Oσ
n)2
+ 1
2
A
X
n=1
3
X
α=1
λτ
n(Oτ
nα)2 + 1
2
3A
X
n=1
3
X
α=1
λστ
n (Oστ
nα)2
(C.37)
which can be conveniently used in AFDMC.
138
