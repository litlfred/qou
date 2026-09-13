---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "Quantum Monte Carlo Calculations of Light Nuclei"
section_id: sec-010-4-greens-function-monte-carlo
section_title: "GREEN’S FUNCTION MONTE CARLO"
section_number: 4
pages: 15-16
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
doc_brief: "Quantum Monte Carlo Calculations of Light Nuclei — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear"
---
The GFMC method (3, 42) projects out the exact lowest-energy state, Ψ 0, for a
given set of quantum numbers, using Ψ 0 = lim τ →∞ exp[−(H −E0)τ ]Ψ T , where
Ψ T is an initial trial function. If the maximum τ actually used is large enough,
the eigenvalueE0 is calculated exactly while other expectation values are ge nerally
calculated neglecting terms of order |Ψ 0 − Ψ T |2 and higher (18). In contrast, the
error in the variational energy, EV , is of order |Ψ 0 − Ψ T |2, and other expectation
values calculated with Ψ T have errors of order |Ψ 0 − Ψ T |. In the following we
present a brief overview of modern nuclear GFMC methods; muc h more detail
may be found in Refs. (18, 19).
We start with the Ψ T of Eq.(30) and deﬁne the propagated wave function Ψ( τ )
Ψ(τ ) = e−(H−E0)τ Ψ T =
[
e−(H−E0)△τ
] n
Ψ T , (39)
where we have introduced a small time step, τ =n△τ ; obviously Ψ( τ = 0) = Ψ T
and Ψ( τ → ∞ ) = Ψ 0. The Ψ( τ ) is represented by a vector function of R using
Eq.(37), and the Green’s function, Gαβ(R, R′) is a matrix function of R and R′
