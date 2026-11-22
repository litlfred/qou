---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-052-b1-time-dependent-greens-function
section_title: "B.1 Time-Dependent Green's Function"
section_number: null
pages: 133-134
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
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
