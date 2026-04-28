**Remark.**
*The Strutinsky shell-correction method
(Strutinsky, Nucl. Phys. A 95, 1967) decomposes nuclear binding
energies as*

$$
  E \;=\; \tilde E \;+\; \delta E_{\mathrm{shell}},
$$

*with $\tilde E$ a smoothed (liquid-drop) macroscopic piece and
$\delta E_{\mathrm{shell}}$ an oscillating microscopic correction
obtained by comparing the actual single-particle level density
$\rho(E) = \sum_i \delta(E - e_i)$ to a Gaussian-smoothed version
$\tilde\rho(E)$.  This decomposition is the physics shadow of the
filtered-algebra identity*

$$
  \mathrm{tr}_M(T_w, q_0)
  \;=\;
  \mathrm{tr}_{\mathrm{gr}}(\sigma(T_w), q_0)
  \;+\;
  \mathrm{Res}_{\mathrm{GB}}(T_w, q_0)
$$

*from ([graded-trace residue split](#prop:graded-trace-residue-split)).*

**Identification.**

| Strutinsky (physics) | Categorical (algebra) |
|---|---|
| Smoothed level density $\tilde\rho(E)$ | Symbol map $\sigma: J^\ell \to J^\ell/J^{\ell+1}$ |
| Liquid-drop energy $\tilde E$ | Graded trace $\mathrm{tr}_{\mathrm{gr}}(\sigma(T_w), q_0)$ |
| Oscillating correction $\delta E_{\mathrm{shell}}$ | Residue sum $\mathrm{Res}_{\mathrm{GB}}(T_w, q_0)$ |
| Gaussian smoothing width | Filtration step $J^\ell / J^{\ell+1}$ granularity |
| Magic-number enhancement | Rectangular-partition spike in $w_\lambda(q_0)$ |

**Why the analogy is exact, not just suggestive.**
*The Strutinsky smoothing procedure averages $\rho(E)$ over an
energy window chosen to span several major shells; this is
equivalent to projecting onto the filtration quotient
$\mathrm{gr}\,H_n(q)$, which identifies all basis elements
differing only by rewriting within a stratum.  The oscillations
of $\rho - \tilde\rho$ encode exactly the Gröbner–Shirshov
rewriting defects that the symbol map loses — hence
$\delta E_{\mathrm{shell}} = \mathrm{Res}_{\mathrm{GB}}$.  The
Strutinsky prescription is therefore not a calculational trick:
it is the unique decomposition of the trace dictated by the
filtered-algebra structure.*

**What this buys.**
*Two practical consequences:*

1. *Strutinsky's method — smooth plus shell — is **forced by the
   filtered-algebra structure**, not an ansatz.  Any competing
   macroscopic-microscopic split of nuclear binding that uses a
   different smoothing is implicitly choosing a different
   filtration on $H_n(q)$.  The confinement filtration
   ([confinement level](#def:confinement-level)) is canonical
   once the knot-operator energy ordering is fixed, so the
   Strutinsky-like decomposition is canonical.*
2. *The shell correction
   $\delta E_{\mathrm{shell}}$ becomes computable **without**
   a phenomenological single-particle potential: it is the
   residue sum
   ([GB residue spectral sum](#prop:gb-residue-spectral-sum))
   applied to the atomic braid.  Magic-number enhancements arise
   algebraically when $\lambda$ reaches a rectangular shape and
   $H_q(\lambda)$ factorises
   ([shell–Schur–Weyl self-duality](#prop:shell-schur-weyl-self-duality)).*

**Scope.**
*The identification is paper-side interpretation and does not
replace a quantitative Strutinsky calculation.  A direct
numerical comparison — Strutinsky $\delta E_{\mathrm{shell}}$ at
a deformation parameter $\beta_2$ versus $\mathrm{Res}_{\mathrm{GB}}$
for the corresponding atomic braid — is the natural next
observational test.*
