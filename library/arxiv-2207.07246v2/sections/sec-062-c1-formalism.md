---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-062-c1-formalism
section_title: "C.1 Formalism"
section_number: null
pages: 144-145
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
Formalism
DMC with or without importance sampling mentioned previously, can be taken
as a special case of AFDMC (Schmidt and Fantoni (1999); Gandolﬁ(2007); Carlson
et al. (2015)). In general, in DMC simulations, the evolution of a state can be cast
into such a form,
|Ψ(t + δt)⟩=
Z
dXP(X)T(X)|Ψ(t)⟩,
(C.1)
where X are a series of variables called auxiliary ﬁelds. Note that X are not necessarily
coordinates. P(X) is the normalized probability density. T(X) is an operator acting
on |Ψ(t)⟩, it basically tells us how to move the walkers which form the state |Ψ(t)⟩.
As δt →0, we expect that the propagator is given by
e−(H−ET )δt =
Z
dXP(X)T(X).
(C.2)
We can think of |Ψ(t)⟩as a linear combination of NW walker states |RiSi⟩with
corresponding weight wi such that
|Ψ(t)⟩=
NW
X
i=1
wi|RiSi⟩,
(C.3)
where R and S denote the spatial and spinor (spin-isospin) part in a walker. Here the
amplitude of diﬀerent walkers are related by Kronecker delta ⟨RjSj|RiSi⟩= δij.
The key is that, we sample X from P(X), then use T(X) to move each walker
|RiSi⟩into the new walker |R′
iS′
i⟩with its weight W(X, Ri, Si),
T(X)|RiSi⟩= W(X, Ri, Si)|R′
iS′
i⟩.
(C.4)
With importance sampling, we denote |ΨTΨ(t)⟩as a state such that we deﬁne
⟨RiSi|ΨTΨ(t)⟩≡⟨ΨT|RiSi⟩⟨RiSi|Ψ(t)⟩,
(C.5)
and that
|ΨTΨ(t)⟩=
NW
X
i=1
wi|RiSi⟩.
(C.6)
In other words, it is
|Ψ(t)⟩=
NW
X
i=1
wi|RiSi⟩
⟨ΨT|RiSi⟩.
(C.7)
Consider that actually wi = 1, Om the mixed average of operator O can be written as
Om = ⟨ΨT|O|Ψ(t)⟩
⟨ΨT|Ψ(t)⟩
=
1
NW
NW
X
i=1
⟨ΨT|O|RiSi⟩
⟨ΨT|RiSi⟩
=
1
NW
NW
X
i=1
ˆO†⟨ΨT|RiSi⟩
⟨ΨT|RiSi⟩.
(C.8)
134
Putting Eq.(C.7) into Eq.(C.1) we have
|ΨTΨ(t + δt)⟩=
NW
X
i=1
wi
Z
dXP(X)⟨ΨT|T(X)|RiSi⟩
⟨ΨT|RiSi⟩
T(X)|RiSi⟩
W(X, Ri, Si).
(C.9)
Note that
|R′
iS′
i⟩= T(X)|RiSi⟩
W(X, Ri, Si).
(C.10)
Now we need a normalized distribution
˜P(X) = P(X)
N
⟨ΨT|T(X)|RiSi⟩
⟨ΨT|RiSi⟩
,
(C.11)
in which the normalization factor
N =
Z
dXP(X)⟨ΨT|T(X)|RiSi⟩
⟨ΨT|RiSi⟩
,
(C.12)
so that we can collect all the new walkers |R′
iS′
i⟩with less ﬂuctuation. Neglecting
O(δt2), we have
N = e−[EL(RiSi)−ET ]δt,
(C.13)
where the local energy is given by
EL(Ri, Si) = ⟨ΨT|H|RiSi⟩
⟨ΨT|RiSi⟩
=
ˆH⟨ΨT|RiSi⟩
⟨ΨT|RiSi⟩.
(C.14)
Now Eq.(C.9) can be written as
|ΨTΨ(t + δt)⟩=
NW
X
i=1
wi
Z
dX ˜P(X)e−[EL(RiSi)−ET ]δt T(X)|RiSi⟩
W(X, Ri, Si).
(C.15)
