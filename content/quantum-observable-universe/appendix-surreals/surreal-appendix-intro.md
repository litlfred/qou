This appendix explores a speculative lift of the Quantum Observable Universe from its native ground field $\mathbb{R}$ to Conway's surreal numbers $\mathbf{No}$. This is the unique proper-class real-closed field containing every ordered-field extension of $\mathbb{R}$ [@conway1976; @ehrlich2012].

**Nothing in this appendix alters the main paper.** The Quantum Observable Universe is developed and proved over $\mathbb{R}$. This appendix offers an *ambient* field into which we can embed the archimedean content, recovering it via a standard-part map. We present claims as remarks interpreting existing blocks, conjectures pending further development, or definitions of new auxiliary structures.

## Motivation for the surreal lift

Four distinct uses motivate the lift:

1. **An explicit ambient for $q \to 1$ limits.** Setting $q = 1 + \varepsilon$ for an infinitesimal $\varepsilon \in \mathbf{No}$ replaces the classically broken classical-limit functor ([classical limit functor](#def:classical-limit-functor)) with evaluation at a specific surreal, composed with Robinson's standard-part map [@robinson1966]. The classical regime becomes a quotient, not a limit.
2. **A grading source aligned with braid combinatorics.** Gonshor's sign-sequence presentation of $\mathbf{No}$ [@gonshor1986] assigns every surreal a function $\alpha \to \{+,-\}$ for some ordinal $\alpha$. The Hecke generator $\sigma$ has two eigenvalues. A braid word decorated with eigenspace choices produces a sign sequence and therefore a surreal number. The Hoefsmit seminormal form ([Hoefsmit seminormal form](#prop:hoefsmit-seminormal-form)) is the surreal $\{L \mid R\}$ construction in disguise ([Hoefsmit is surreal construction](#prop:hoefsmit-is-surreal-construction)).
3. **Named values for blow-ups and singularities.** The Möbius energy integral, renormalisation scales, and hyperbolic-volume divergences become honest elements of $\mathbf{No}$ rather than informal symbols $\infty$. Counterterms become named negative surreals.
4. **Infinitesimal axioms.** We can relax strict equalities in the QOU axioms (Frobenius pairing $= \mathrm{id}$; observability cohomology $= 0$; vacuum $= 0$) to hold *up to an infinitesimal*. The archimedean theory is recovered by taking standard-parts. The surreal theory is strictly stronger and tracks the infinitesimal deviation.

## Lossiness of the lift

Replacing $\mathbb{R}$ with $\mathbf{No}$ seemingly costs us Lebesgue measure, Hilbert-space completions, and hyperbolic geometry. However, an honest audit shows we *never actually use* most of these in a load-bearing way (see [analytic obstructions](#rem:analytic-obstructions)):

- **Lebesgue measure** enters only the Möbius energy integral. Everywhere else, "integrals" are categorical (Frobenius counit) or reduce to rational formulas.
- **Hilbert completion** appears in exactly one proof passage. The word "dense" can be replaced by "spans the algebraic direct limit" without loss.
- **Hausdorff dimension** is given by the rational formula $d_H(q) = (2q-1)^2/q^3$, so it transfers to $\mathbf{No}$ exactly.
- **Spectral theorems** are never used. Hoefsmit's seminormal form diagonalises Hecke generators algebraically over $\mathbb{Q}(q^{1/2})$.

The only obstructions that genuinely bite are the Möbius energy integral and the hyperbolic-volume side of the Kashaev comparison. The main paper's mass-formula pipeline transfers to $\mathbf{No}$ unchanged.

## Non-goals

This appendix does **not**:
- Claim a physical interpretation of non-archimedean values. We work purely mathematically.
- Replace any main-text proof. The main paper's results stand on their own over $\mathbb{R}$.
- Solve the Kashaev volume conjecture. We offer a reformulation that separates the algebraic from the transcendental parts ([Kashaev surreal reformulation](#conj:kashaev-surreal)).
- Construct a canonical Lebesgue-like measure on $\mathbf{No}$. We sidestep this rather than solving it.

## Structure of the appendix

Section 1 states the algebraic core that survives unchanged. Section 2 lists the analytic obstructions. Section 3 shows what survives of calculus up to infinitesimals. Sections 4–5 construct the birthday and sign-sequence gradings and the standard-part functor. Section 6 relaxes the strict QOU axioms. Section 7 gives two speculative reformulations: the substrate as a Hahn series, and Kashaev's conjecture as a standard-part identity.

All Lean files in this appendix axiomatise the ambient field $\mathbf{No}$ as a real-closed field. We make no attempt to construct $\mathbf{No}$ inside Lean (that would require mathlib's `SurrealNumber` development, which is not yet exhaustive).
