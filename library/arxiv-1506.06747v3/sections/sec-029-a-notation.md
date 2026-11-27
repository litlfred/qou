---
doc_id: arxiv-1506.06747v3
doc_title: "Cottingham formula and nucleon polarizabilities"
section_id: sec-029-a-notation
section_title: "A Notation"
section_number: null
pages: 20-21
source_pdf: 1506.06747v3.pdf
source_sha256: c44709743db78865
toc_source: outline
doc_brief: "Cottingham formula and nucleon polarizabilities — The diﬀerence between the electromagnetic self-energies of proton and neutron can be calculated with the Cottingham formula, which expresses the"
---
The structure functions are related to the Fourier trans-
form of the spin-averaged matrix element of the current
commutator,
V µν(p, q) = 1
4π
Z
d4xeiq·x⟨p|[jµ(x), jν(0)]|p⟩.
(A.1)
The states are normalized with
⟨p′, s′|p, s⟩= 2p0(2π)3δ3(p ′ −p)δs′s
(A.2)
and ⟨p|O|p⟩
stands for
1
2
P
s⟨p, s|O|p, s⟩.
For
the
Fourier transform of the time-ordered matrix element,
⟨p|T jµ(x)jν(y)|p⟩, we use the normalization
T µν(p, q) = i
2
Z
d4xeiq·x⟨p|T jµ(x)jν(0)|p⟩.
(A.3)
Since Lorentz invariance, current conservation, and par-
ity only allow two independent tensors of this type,
Kµν
1
= qµqν −gµνq2 ,
Kµν
2
=
1
m2
n
(pµqν + pνqµ)p · q
−gµν(p · q)2 −pµpνq2o
,
(A.4)
these matrix elements contain two invariants each,
which only depend on the two variables ν ≡p · q/m
and q2 (m is the mass of the nucleon). We denote the
invariants by V1(ν, q2), V2(ν, q2) and T1(ν, q2), T2(ν, q2),
respectively:
V µν(p, q) = V1(ν, q2)Kµν
1
+ V2(ν, q2)Kµν
2
,
T µν(p, q) = T1(ν, q2)Kµν
1
+ T2(ν, q2)Kµν
2
.
(A.5)
In contrast to the standard structure functions F1, F2
the invariants V1, V2 are free of kinematic singularities
or zeros. The two sets are related by
V1 ≡−2xF1 + F2
4mx2ν
,
V2 ≡
F2
2xν2 ,
(A.6)
with x ≡Q2/2mν.
The notation for the longitudinal structure function
FL is not universal. The convention used in the mini-
review on the structure functions in The Review of Par-
ticle Physics [95] reads
FL = F2 −2xF1 .
(A.7)
The structure functions V1(ν, q2) and V2(ν, q2) rep-
resent linear combinations of the transverse and longi-
tudinal cross sections σT and σL:
V1 = N1(−Q2σT + ν2σL)/Q2 ,
V2 = N1(σT + σL) ,
N1 ≡
1
8π2αem
2mν −Q2
ν2 + Q2 .
(A.8)
The value of the structure function V2(ν, 0) also de-
termines the total cross section for photoproduction,
σtot = limQ2→0 σT :
σtot(ν) = 4π2αem
ν
mV2(ν, 0) .
(A.9)
For the one-particle matrix elements of the current,
we use the notation
⟨p1, s1|jµ|p2, s2⟩= ¯u(p1, s1)Γ µ(q)u(p2, s2) ,
Γ µ(q) = FD(q2)γµ + FP (q2)iσµν qν
2m ,
(A.10)
where q = p1 −p2. The nucleon spinors are normalized
with ¯u(p, s′)u(p, s) = 2mδs′s. The functions FD(t) and
FP (t) are referred to as Dirac and Pauli form factors,
21
respectively. Whenever convenient, we replace these by
the Sachs form factors, which are deﬁned by
GE(t) = FD(t)+
t
4m2 FP (t) ,
GM(t) = FD(t)+FP (t) .
(A.11)
In dipole approximation, the form factors are parame-
terized with
Gp
E(t) = Gd(t) ,
Gp
M(t) = (1 + κp)Gd(t) ,
Gn
E(t) =
t
4m2 κnGd(t) ,
Gn
M(t) = κnGd(t) ,
Gd(t) =
1
(1 −t/M 2
d)2 ,
M 2
d ≃0.71 GeV2 ,
(A.12)
where κ = FP (0) stands for the anomalous magnetic
moment.
