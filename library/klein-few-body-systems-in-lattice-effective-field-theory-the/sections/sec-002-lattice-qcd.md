---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-002-lattice-qcd
section_title: "Lattice QCD"
section_number: null
pages: 8-9
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
theory approach. Both methods are explained in the subsequent sections.
While lattice QCD and eﬀective theory are highly successful in the two- and partly three- and four-body
sector, one has to use diﬀerent methods for the description of many-body physics. The reason is that
an extension of the corresponding Faddeev-Yakubovsky equations become impractical to solve. There
are various many-body methods whereas we just name a few in the following. Firstly we have coupled
cluster theory or shell/no-core shell models, which use phenomenological Lagrangians as input. Secondly,
there are Green’s function Monte Carlo methods which combine variational methods with Monte Carlo
methods for the evaluation of integrals. This method is rather successful and details will be given below.
In this thesis we will use a third approach, namely the nuclear lattice eﬀective ﬁeld theory (NLEFT),
where the interactions are determined from ab initio 2N and 3N interactions based on chiral eﬀective
theory. Moreover, the space is discretized, such that a natural cuto ﬀ Λ arises by the lattice spacing a,
Λ = π/a and exact methods as well as statistical methods known from Lattice QCD are used for the
evaluation of binding energies, phase shifts, etc. for two-, few- and many-body problems.
1.2 Lattice QCD
Lattice QCD is a non-perturbative method for solving QCD in the low-energy region. Generally, one
calculates correlation functions in a discretized space-time using Monte Carlo methods. In the following
2
1.3 E ﬀective Theory
we give a very short introduction with a focus on the questions which will arise throughout this thesis. A
thorough introduction can be found in [2].
Starting point is the partition function,
Z =
∫
DADΨD ¯Ψ exp
{
−S F
[
Ψ, ¯Ψ, A
]
− S G[A]
}
, (1.5)
where A is the gauge ﬁeld, and Ψ the fermion ﬁeld. S F and S G are the fermion and gauge actions. Any
correlation function of two operators ˆO1, ˆO2 can be calculated by taking its average,
⟨ ˆO2(t) ˆO1(0)
⟩
= 1
Z
∫
DAµDΨD ¯Ψ ˆO2
[
Ψ, ¯Ψ, A
] ˆO1
[
Ψ, ¯Ψ, A
]
exp
{
−S F
[
Ψ, ¯Ψ, A
]
− S G [A]
}
. (1.6)
where the imaginary time t = iτ has been introduced already for the Euclidean rotation. While the
Eqs. (1.5) and (1.6) are only formal expression, the respective discretized version is solvable numerically.
Therefore, we put the system in a box of size Na× Na× Na× NT aT , where a is the spatial lattice spacing
and aT the temporal lattice spacing. N, NT are the number of nodes in spatial and temporal directions.
For the discretization, one deﬁnes all ﬁelds and operators on the lattice points and substitutes continuous
derivatives by ﬁnite diﬀerences. Then one uses Monte Carlo methods to calculate any observables from
their respective correlation function. In such an approach, we have three main sources of artifacts. Firstly,
one has to do inﬁnite time extrapolations for observables, where one mostly expects an exponential
decay and which gives a certain uncertainty. Secondly, the volume L3 may cause an error if it is not
large enough. Thirdly, the lattice spacing a itself produces a lattice artifact which makes an extrapolation
to the continuum necessary or to improve the disctretization scheme. In a very simple lattice QCD
calculation the lattice spacing error is linear, but one can use a diﬀerent discretization scheme or include
more operators in order to push this error to higher order. Symanzik’s improvement program gives a
clear strategy to do this [3, 4]. Note that additionally, the quark mass plays an important role for the
eﬃciency of the algorithm, as one may be forced to do calculations at larger quark/ pion mass Mπ and to
ﬁnally extrapolate to the physical point. Nowadays, lattice calculations use parameters in the range of
a∼ 0.05− 0.15 fm, L∼ 2− 4 fm and Mπ∼ 134− 450 MeV . Lattice QCD is mainly successful in the
description of two-meson or two-baryon physics and in the near future, it may work in the three-body
sector as well [5–8].
