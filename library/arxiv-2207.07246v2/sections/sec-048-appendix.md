---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-048-appendix
section_title: "APPENDIX"
section_number: null
pages: 130-134
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
---
VARIATIONAL MONTE CARLO BRIEF
120
The time-independent Schr¨odinger equation can be written as Hψ0 = E0ψ0 if the
system is at its lowest energy E0 with wave function ψ0. We are interested in the
ground state energy E0 because a system will naturally go to its lowest energy state
ψ0. The question is how to ﬁnd ψ0 and E0.
Variational Monte Carlo(VMC), based on a trial wave function ψT (usually not
normalized) with parameters, provides a way to ﬁnd the upper limit of E0. Its foundation
is
Evar ≡⟨ψT|H|ψT⟩
⟨ψT|ψT⟩
≡
Z HψT(R)
ψT(R) |ψT(R)|2dR
Z
|ψT(R)|2dR
≡
Z
EL(R)p(R)dR ≥E0,
(A.1)
where the local energy is deﬁned as
EL(R) = HψT(R)
ψT(R) ,
(A.2)
the probability density is given by
p(R) =
|ψT(R)|2
Z
|ψT(R)|2dR
.
(A.3)
The closer ψT is to ψ0, the closer Evar is to E0 from above. For bosons ψT has to
be symmetric while for fermions ψT has to be anti-symmetric. For example, a possible
trial wave function for the system of bosons might be written in the form of
ψT(R) =
Y
i<j
f2(rij)
Y
i<j<k
f3(i, j, k)
Y
i<j<k<l
f4(i, j, k, l)...
Y
k
g(rk −rc),
(A.4)
where fn denotes the correlation function between n particles, and g(rk −rc) denotes
the correlation between the position of one particle (rk) and the system’s center of
mass(rc). For fermions, the following form (Kalos and Whitlock (2008)) may be used
as a simple example,
ψT(R) = exp

−
X
i<j
f(rij)

×

eik1·r1
eik2·r1
...
eik1·r2
eik2·r2
...
eik1·r3
eik2·r3
...
...
...
...

,
(A.5)
where ki is momentum of the particle i in three dimensional space.
The VMC trial wave function ψT usually contains some parameters which can be
adjusted to minimize Evar, so that ψT can be optimized as close to the ground state as
its structure allows. Then DMC and PIMC can be performed based on this optimized
trial wave function.
121
APPENDIX B
DIFFUSION MONTE CARLO BRIEF
122
Diﬀusion quantum Monte Carlo (DMC) method (Negele and Orland (1998); Kalos
and Whitlock (2008); Hammond et al. (1994); Apaja (2009)) is based on the time-
dependent Green’s function. Beginning with a trial wave function which is non-
orthogonal to the true ground state, by treating the imaginary time as a real number,
it provides a way to project out the true ground state wave function through diﬀusion
and branching process. Unlike VMC which uses trail wave function with adjustable
parameters, DMC is able to numerically ﬁnd the true ground state wave function and
the corresponding ground state energy with time step error.
B.1
Time-Dependent Green’s Function
The solution of the time-dependent Schr¨odinger equation i ∂Ψ(x,t)
∂t
= HΨ(x, t) in
natural units can be written as the superposition of the eigenstates Φk(x) with time
evolution,
Ψ(x, t) =
∞
X
i=0
akΦk(x)e−iEkt.
(B.1)
In Monte Carlo method, we care more about the energy shifted Schr¨odinger
equation,
i∂φ(x, t)
∂t
= (H −ET)φ(x, t),
(B.2)
and the solution can be written as
φ(x, t) =
∞
X
k=0
ckΦk(x)e−i(Ek−ET )t,
(B.3)
where ck = ⟨Φk|φ(t = 0)⟩are the coeﬃcients which only depend on the initial condition.
In DMC, we want to ﬁnd connections between Eq.(B.2) and the diﬀusion equation.
In order to do this, we use imaginary time τ = it and rewrite Eq.(B.2) as
−∂φ(x, τ)
∂τ
= (H −ET)φ(x, τ),
(B.4)
with the solution
φ(x, τ) =
∞
X
k=0
ckΦk(x)e−(Ek−ET )τ.
(B.5)
If we merely look at Eq.(B.4) and Eq.(B.5) and take τ as a real number, as τ →∞,
there are three situations. First, if ET > E0, then limτ→∞φ(x, τ) = ∞. Second, if
ET < E0, then limτ→∞φ(x, τ) = 0. Third, if ET = E0, then limτ→∞φ(x, τ) = c0Φ0(x),
which means if c0̸ = 0, then only the ground state Φ0 contributes. However if c0 happen
to be zero, then with proper ET we should be left with the ﬁrst excited state Φ1.
123
Eq.(B.4) tells us that
|φ(τ2)⟩= e−(H−ET )(τ2−τ1)|φ(τ1)⟩,
(B.6)
acting ⟨y| on both side leads to
φ(y, τ2) =
Z
⟨y|e−(H−ET )(τ2−τ1)|x⟩φ(x, τ1)dx,
(B.7)
where
⟨y|e−(H−ET )(τ2−τ1)|x⟩≡G(y, τ2; x, τ1)
(B.8)
is the Green’s function. It only depends on the time diﬀerence τ2 −τ1, so, for the small
step δτ, Eq.(B.7) can be written as
φ(y, τ + δτ) =
Z
G(y, x; δτ)φ(x, τ)dx.
(B.9)
The Green’s function can be expanded as
G(y, x; δτ) =
∞
X
i=0
Φi(y)Φi(x)e−(Ei−ET )δτ.
(B.10)
Assuming φ(y, τ = 0) = P∞
k ckΦk and substitute Eq.(B.10) into Eq.(B.9) we have
φ(y, δτ) =
∞
X
k=0
ckΦk(y)e−(Ek−ET )δτ.
(B.11)
After n iterations we have
φ(y, nδτ) =
∞
X
k=0
ckΦk(y)e−(Ek−ET )nδτ.
(B.12)
As n →∞, and as long as c0̸ = 0, the ﬁnal state will be dominated by the ground
state Ψ0. Furthermore, if we set ET = E0, the exponential term will be just a constant.
It needs to pointed out that since we treat τ as a real number, for ﬁnite τ, φ(x, τ)
does not have the physical meaning as the time-dependent wave function anymore.
