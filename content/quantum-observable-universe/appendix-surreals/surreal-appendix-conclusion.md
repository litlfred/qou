The surreal-number lift of QOU raises more questions than it answers:

1. **Mathlib gap.** There is no mature surreal-analysis library in mathlib. Formalising the birthday-grading definition and the Hoefsmit-as-$\{L\mid R\}$ proposition requires filling in the surreal-numbers development up to a real-closed-field witness.
2. **Surreal measure?** $\mathbf{No}$ carries no canonical Lebesgue measure. Loeb-type constructions on hyperfinite subsets of $\mathbf{No}$ yield finitely additive measures that pull back to $\mathbb{R}$ under standard-part. Whether such a construction recovers the Frobenius integral $\int_A$ up to an infinitesimal is open.
3. **Surreal Hilbert-like object.** The scattering pipeline's Hilbert space $\mathcal{H}_{\mathrm{phys}}$ has no surreal analogue with a canonical inner product. We should investigate whether a *birthday-bounded completion* gives a surrogate that can run the mass formula.
4. **Categorical size.** $\mathbf{No}$ is a proper class. Defining $\mathbf{Mod}_{\mathbf{No}}$ requires universe-polymorphic foundations. We sidestep this by stating axioms over a fixed real-closed field $K$ extending $\mathbb{R}$.
5. **Are the infinitesimal relaxations genuine generalisations?** The strict QOU axioms might force the $\varepsilon$-relaxed versions to coincide with the strict ones in any rigid monoidal category. If so, the $\varepsilon$-flexibility is illusory. We conjecture the flexibility is *real* when the ground ring is not a field ([infinitesimal Frobenius](#conj:infinitesimal-frobenius)).
6. **Kashaev as a surreal statement.** The reformulation $\mathrm{st}\bigl(2 \pi \log |J_K(q_\omega, \omega)|/\omega\bigr) = \mathrm{Vol}(S^3 \setminus K)$ ([Kashaev surreal](#conj:kashaev-surreal)) is equivalent to the classical conjecture. It separates the algebraic (Hecke/Markov) content from the transcendental (dilogarithm, hyperbolic volume) content.

## Accomplishments of this appendix

* We provide an explicit ambient for the $q \to 1$ limit and renormalisation blow-ups, avoiding informal $\infty$ notation.
* We exhibit an isomorphism between the Hoefsmit seminormal form and Conway's $\{L \mid R\}$ construction.
* We give a disciplined framework for $\varepsilon$-relaxed axioms.
* We catalogue which QOU constructions are purely algebraic versus which are genuinely analytic.

We offer the appendix as raw material for future work rather than as a completed extension of the theory.
