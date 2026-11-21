# Exact linked-word lepton traces against the window (2026-11-21)

Owner: "keep pushing on lepton". Question stated in the thread before the computation: for each of
the 59 distinct linked-word values x̂ (1560 γγ words, forced lepton normalisation of #8836), is x̂
outside the window (ε_n, ε_p) for **every** q in (1, 23/20], not only at q₀?

Method, fixed before the run: exact Laurent-polynomial arithmetic in q (integer coefficients, no
floats) for Tr(K⁹ (P_p ⊗ 1) ρ(W)); x̂ = that / [2]⁷ (writhe 0, 7 components). For e⁻ν̄ test
ε_n − x̂ > 0, for the mirror test x̂ − ε_p > 0, by exact real-root isolation (sympy `real_roots`)
of the numerator in t = q − 1 on (0, 3/20], plus the sign at one interior point. Report every
class, including any that enter the window. Nothing is selected or adopted.

Note on order: a first exploratory run in scratch preceded this file by minutes; the question and
method above are those stated in chat before it, and the run here reproduces it from the repo.
