---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Bonn, November 2018"
section_id: sec-005-quantum-monte-carlo-methods---status-and-open-ch
section_title: "Quantum Monte Carlo methods - status and open challenges"
section_number: null
pages: 11-14
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-Body Systems in Lattice Effective Field Theory Dissertation Erlangung des Doktorgrades (Dr. rer. nat.) Mathematisch-Naturwissenschaftlichen Fakultät Rheinischen Friedrich-Wilhelms-Universität Bonn"
---
Generally, there are two approaches in Quantum Monte Carlo calculations, a continuum and a lattice
approach, which are used for the estimation of physical properties of nuclei.
In continuum Monte Carlo theory, the ﬁrst approach is a variational method called variational Monte
Carlo (VMC) for the calculation of ground states, E0. The basic idea is to minimize the energy EV of the
5
Chapter 1 Introduction and Motivation
trial wave function|ΨT⟩,
EV =
⟨ΨT
⏐⏐⏐ H
⏐⏐⏐ΨT
⟩
⟨ΨT
⏐⏐⏐ ΨT
⟩ ≥ E0. (1.8)
H is the Hamiltonian of the systems. It is crucial to ﬁnd a trial wave function as close as possible to the
exact ground state wave function. Therefore, it is suitable to make a separation ansatz,
⏐⏐⏐ΨT
⟩ =F|Φ⟩, (1.9)
whereF reﬂects the short-range physics while |Φ⟩ is optimized for the long-range part. The short-
range part consists of pair functions fulﬁlling a modiﬁed Schrödinger-equation that includes the exact
Schrödinger equation as well as variational modiﬁcations. The long-range part just reﬂects the antisym-
metry of the wave function. One of the severe problems is the exponential scaling of required computer
time with the number of particles making it hard to use in the many-body sector. Nowadays, VMC is
used to create good trial wave functions|ΨT⟩ for a time-evolution which leads to the ground state at
inﬁnite time. This method is called Green’s function Monte Carlo, where the ground state wave function
is deﬁned as ⏐⏐⏐Ψ0
⟩ = lim
τ→∞
exp[−(H− E0
)τ]⏐⏐⏐ΨT
⟩. (1.10)
E0 is introduced for normalization reasons of the wave function and it can be identiﬁed with the ground
state energy. It is not possible to calculate the equation for inﬁnite times, and one therefore evaluates the
equation for several time steps. After N time steps the wave function reads
⏐⏐⏐Ψ0 (R)N
⟩ =
∏
1...N
⟨⃗RN
⏐⏐⏐⏐ exp[−(H− E0
)τ]⏐⏐⏐⏐⃗RN−1
⟩
...
⟨⃗R1
⏐⏐⏐⏐ exp[−(H− E0
)τ]⏐⏐⏐⏐⃗R0
⟩⏐⏐⏐ΨT
⟩. (1.11)
⃗Ri are the possible paths and they can be calculated using Monte Carlo methods. Nevertheless, the
scaling is again very bad, and it is diﬃcult to scale this up to many-particle calculations. This scheme
can be modiﬁed by the introduction of auxiliary ﬁelds which change the two-particle interaction to a
one-particle interaction via Hubbard-Stratonovitch transformation. Green’s function Monte Carlo was
used to calculate light and medium-mass nuclei mainly up to oxygen-16 [29, 30] and for the calculation
of the Hoyle state, where the theoretical prediction is 10.4(5) MeV , which is far oﬀ from the experimental
value of 7.65 MeV [31].
Another approach is NLEFT, which discretizes space (and time) and uses the chiral Lagrangian as the
underlying theory making ab initio calculations possible. Generally, one conﬁnes the physical system in
a discrete box of size L3 with spatial lattice length L = NLa with NL nodes and lattice spacing a. Finally,
one solves the Schrödinger equation
H|Ψ⟩ = E|Ψ⟩, (1.12)
using the Lanczos algorithm for sparse matrices. This approach scales at least with L3(Np−1), where Np
is the number of particles and even stronger if the particles have inner spin-isospin structure. Hence it
is limited to very few particles. For more particles, the time direction is discretized as well and Monte
Carlo methods are used again to calculate the corresponding generating functional,
ZA(t) = ⟨ΨA
⏐⏐⏐ exp (−Ht)
⏐⏐⏐ΨA
⟩, (1.13)
where|ΨA⟩ is a prepared initial state. While any arbitrary initial state with non-zero overlap with the
ground state would be applicable, it might be advisable to use states reﬂecting the expected symmetry of
the ground state for improved convergence. A famous example is the Wigner SU(4) symmetry which is
6
1.5 Quantum Monte Carlo methods - status and open challenges
almost fulﬁlled in nucleons. Then the energy at a given time step t is deﬁned as
EA(t) =−∂ log ZA(t)
∂t , (1.14)
and the ground state energy is calculated by an inﬁnite time extrapolation
E0 = lim
t→∞
EA(t). (1.15)
Details on NLEFT and its practical implementation will be given in Chap. 3.
This method was ﬁrst used at leading order (LO) in the two-body sector [32] and rapidly extended to
next-to-leading order (NLO) and next-to-next-to-leading order (N2LO) and the three-body sector as well
as many-particle calculations. For details see [33] and references therein. The Hoyle state was calculated
ab initio with a very high accuracy. In addition, it was shown that the quark masses can vary by only
2 before the carbon production collapses and life as we know it becomes impossible [34, 35]. Another
process was the ﬁrst ab initio calculation of alpha-alpha scattering using the adiabatic projection method
[36].
In spite of the quite impressive results in NLEFT, one has to look for possible issues of the theory
with great detail to estimate the systematic errors and - if possible - ﬁnd a way to reduce them. One of
the main systematic errors is caused by the lattice discretization. Although such a discretization also
exists in lattice QCD, the situation in NLEFT is diﬀerent as the lattice spacing is linked to a cutoﬀ, which
should not exceed the physical breakdown scale of the theory. The standard lattice spacing for most
of the calculations so far is a = 1.97 fm, which is approximately Λ≈ 314 MeV . The proton radius is
≈ 0.85 fm [37] equivalent to≈ 730 MeV and the general cutoﬀ of the theory is Λ≈ 500 MeV equivalent
to 1.24 fm. This means that one should investigate physical observables, regularization schemes, etc.
at least in the range from 1 fm to 2 fm for systematic errors and see whether or not they depend on the
cutoﬀ/ lattice spacing in this area. From a lattice QCD and/ or continuum EFT point of view it would
be interesting as well to see whether one could decouple the lattice spacing from the cutoﬀ, i.e. a ﬁxed
cutoﬀ regulator for the eﬀective potentials can be used thereby the lattice spacing can be sent to zero,
such that its limit depends only on computational limits but not on physical ones [38].
Additionally, in the case of eﬀective many-body calculations it was always necessary to introduce
a four-body force to absorb lattice spacing errors. It has been argued that this artifact vanishes once
the lattice spacing is small enough but it was never really tested. As a result, the Tjon line cannot be
reproduced in the framework of NLEFT for coarse lattices while it is reproduced in continuum eﬀective
ﬁeld theory.
As the nuclear eﬀective theory includes a lot of additional operators in the sense of an eﬀective theory,
one could also include additional operators in the sense of Symanzik’s improvement program [3, 4].
From a lattice theory point of view it is quite interesting to see whether we can set up a clear counting
scheme that absorbs lattice spacing artifacts order-by-order and what is the applicability range of such a
scheme.
This thesis is organized as the following.
Chap. 2 reviews eﬀective ﬁeld theory for few- and many-nucleon systems and the theory of scattering.
The aforementioned theory is transferred on the lattice in Chap. 3. We will explain the discretization
procedure and give an introduction into solution methods – exact methods as well as Monte Carlo
methods.
In Chap. 4 we have a look at the leading-order NN system with focus on the deuteron bound state
and the S wave eﬀective range expansion. The evolution of low-energy coupling constants as well as
leading-order observables with respect to the lattice spacing are shown and arguments for a special
7
Chapter 1 Introduction and Motivation
regularization of the one-pion exchange potential are given.
In Chap. 5 we make the transition from a NN system to the light nuclei triton and helium-4 where we
focus on the correlation between both binding energies and show that we can reproduce the Tjon line
once the spacing is chosen small enough.
