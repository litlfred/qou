---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-032-two-level-quantum-system-rectangular-step
section_title: "Two-level quantum system: Rectangular step"
section_number: null
pages: 45-46
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
For the Hamiltonian (194), the first-order Fer and Wilcox operators in the Interaction Picture verify
F1 = W1 = Ω1 =
Z t
0
dt1 ˜HI(t1),
(215)
where ˜HI(t) is given by (198). The explicit expression is collected in (200) (first equation). Analogously, the second equation
there also corresponds to the second-order Wilcox operator W2 = Ω2.
To proceed further with Fer’s method, we must calculate the modified Hamiltonian ˜H(1) in (96). After straightforward
algebra, one eventually obtains
˜H(1) =
1
2θ

sin2 θ
θ
−sin 2θ +
1
θ

sin 2θ
2θ
−cos 2θ

F1

[F1, ˜HI],
(216)
where θ = (2γ /ξ) sin(ξ/2) (notice that ˜H(1) and therefore F2 depend on σ1 and σ2, while W2 is proportional to σ3). Since
it does not seem possible to derive an analytical expression for F2, the corresponding matrix elements have been computed
by replacing the integral by a conveniently chosen quadrature.
The transition probability P(t) from an initial state with spin up to a state with spin down (or vice versa) is given by
(193). This expression has been computed assuming UI ≃eF1 = eW1, UI ≃eF1eF2, UI ≃eW1eW2, UI ≃eF1eF2eF3 and
UI ≃eW1eW2eW3, and the results have been compared with the exact analytical solution (196).
In Figs. 9 and 10 we show the transition probability P as a function of ξ for two different values of γ (γ = 1.5 and γ = 2,
respectively), while in Fig. 11 we have plotted P versus γ for ξ fixed. Notice that the second order in the Wilcox expansion
does not contribute to the transition probability (this is similar to what happens in perturbation theory). On the other hand,
Fer’s second-order approximation is already in remarkable agreement with the exact result, whereas the third order cannot
even be distinguished from the exact result in Fig. 10 at the cost of a much larger computational effort. Wilcox approximants
preserve unitarity but do not give acceptable approximations.
196
S. Blanes et al. / Physics Reports 470 (2009) 151–238
Fig. 9. Rectangular step: Transition probability as a function of ξ, with γ = 1.5. The solid line corresponds to the exact result (196). Broken lines stand for
Fer and Wilcox approximations up to third order. Computations up to third order, in the Interaction Picture.
Fig. 10. Rectangular step: Transition probability as a function of ξ, with γ = 2. Lines are coded as in Fig. 9. Computations up to third order, in the Interaction
Picture.
