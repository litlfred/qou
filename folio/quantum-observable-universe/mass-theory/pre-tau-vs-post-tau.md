> **Superseded.** The scalar aether density $\rho_q = 1/\hbar_q^2$ used below is the structurally-wrong leading-order ansatz; the operator-valued form supersedes it ([mass-endomorphism tower](mass-endomorphism-tower.md)).

**The Archimedean wall.**
Every derivation step belongs to exactly one of two registers:

| Register | Coefficient ring | Operative invariants | Examples |
|---|---|---|---|
| **Pre-$\tau$** | $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ (or $z$-Habiro) | Hecke spectra, Markov traces | SDP feasibility, Gröbner--Shirshov reductions |
| **Post-$\tau$** | $\mathbb{R}$ via $\tau_{\mathrm{arch}}$ | Hyperbolic volumes | PL thimble flow, Bloch--Wigner $D(z)$ |

The functor $\tau_{\mathrm{arch}}$ is the only legal bridge between these columns.

* Pre-$\tau$ derivation steps cannot use post-$\tau$ values (e.g., hyperbolic volume) as inputs.
* Post-$\tau$ derivation steps cannot claim algebraic-side identities (e.g., Hecke relations) that only hold prior to realization.
* Bridging equalities that cross the wall must use $\approx$ unless stating an explicit error term. They describe the functor rather than algebraic derivation steps.

**Motivic shorthand.**
The $z$-Habiro completion houses algebraic encounter data, treating quantum dilogarithm poles as quotients of cyclotomic ideals. Under $\tau_{\mathrm{arch}}$, these algebraic poles realize as hyperbolic-triangulation cusps. Any violation of the wall boundary breaks the formal derivation.
