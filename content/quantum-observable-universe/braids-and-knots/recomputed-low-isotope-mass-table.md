**Remark (recomputed low-isotope mass table after q-Hecke
character gap closure).** *After PR #572's q-Hecke character
closure ([`prop:q-hecke-seminormal-character-closure`](#prop:q-hecke-seminormal-character-closure))
and the cherry-picked* $\rho_K$ *refinement infrastructure from
PR #564, **three independent production paths** to* $\mathrm{tr}_M(\beta_K)$
*at* $q = q_0$ *now agree to machine epsilon across* $\{p, n, D, T, ^{3}\mathrm{He}\}$:

1. **Canonical Markov-axiom reducer** —
   [`markov_trace_recursive.markov_trace_of_word`](../../../folio-assistant/computations/markov_trace_recursive.py)
   at mpfr 50-dps; reference values stored in
   [`atomic-tr-m-mpfr-50dps.witness.json`](../../../folio-assistant/computations/atomic-tr-m-mpfr-50dps.witness.json).
2. **Hybrid partition-sum** (this PR) — 30-dps sympy `Float`
   for $y_\lambda$ via Wenzl's Schur principal specialization,
   float64 for $\chi^\lambda_q$ via Hoefsmit seminormal matrices,
   per-`n` cache.  Module:
   [`wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`](../../../folio-assistant/computations/wedderburn_jones_markov.py);
   driver: [`tr_m_q_hecke_seminormal.py`](../../../folio-assistant/computations/tr_m_q_hecke_seminormal.py).
3. **Symbolic partition-sum** (PR #564) — full 50-dps mpmath via
   [`rho_k_h3a_refinement.py`](../../../folio-assistant/computations/rho_k_h3a_refinement.py),
   the production path for binding-fraction $\Delta_\lambda$ analysis.

## Cross-check (machine epsilon for all 5 atoms)

| Atom | $Z$ | $N$ | $n = 3A$ | canonical $|\mathrm{tr}_M|$ | hybrid partition-sum | rel err |
|---|:-:|:-:|:-:|---:|---:|---:|
| $p$ | 1 | 0 | 3 | 1.0653062286 | 1.0653062286 | $3.96 \times 10^{-15}$ |
| $n$ | 0 | 1 | 3 | 0.9232332972 | 0.9232332972 | $4.21 \times 10^{-15}$ |
| $D$ | 1 | 1 | 6 | 0.3882864715 | 0.3882864715 | $7.01 \times 10^{-15}$ |
| $T$ | 1 | 2 | 9 | 0.1040521187 | 0.1040521187 | $1.07 \times 10^{-14}$ |
| $^{3}\mathrm{He}$ | 2 | 1 | 9 | 0.2065408586 | 0.2065408586 | $1.03 \times 10^{-14}$ |

## Mass-table predictions (ρ_K leading-order ansatz)

Per PR #564's
[`atomic_mass_via_rho_k.py`](../../../folio-assistant/computations/atomic_mass_via_rho_k.py)
with the resolved T6 unit-convention
([`prop:atomic-mass-gb-nf`](atomic-mass-gb-nf.md)):

$$
  \mathcal{M}(K) \;=\; \rho_K(Z, N) \cdot m_e \cdot |\mathrm{tr}_M(K)|, \qquad \rho_K^{\mathrm{LO}}(Z, N) \;=\; \frac{Z m_p + N m_n}{m_e \cdot |\mathrm{tr}_M(K)|}.
$$

Substitution shows $\mathcal{M}^{\mathrm{LO}}(K) = Z m_p + N m_n$ — the
$|\mathrm{tr}_M|$ factor cancels.  The leading-order ρ_K formula
predicts the **free-constituent sum** for every atom; nuclear
binding is recovered only at higher orders of $\rho_K$.

| Atom | $\mathcal{M}_{\text{pred}}^{\mathrm{LO}}$ (MeV) | $\mathcal{M}_{\text{CODATA}}$ (MeV) | $\Delta$ (MeV) | rel err | binding (CODATA) |
|---|---:|---:|---:|---:|---:|
| $p$ | 938.272088 | 938.272088 | 0.0000 | 0.000 % | (anchor) |
| $n$ | 939.565421 | 939.565421 | 0.0000 | 0.000 % | (anchor) |
| $D$ | 1877.837509 | 1875.612943 | $+2.2246$ | $+0.119$ % | 2.225 MeV |
| $T$ | 2817.402929 | 2808.921133 | $+8.4818$ | $+0.302$ % | 8.482 MeV |
| $^{3}\mathrm{He}$ | 2816.109597 | 2808.391607 | $+7.7180$ | $+0.275$ % | 7.718 MeV |

## Two structural notes

**1. The 0.000 % on $p$ and $n$ is a tautology, not a prediction.**
The ρ_K leading-order ansatz is built from $m_p$ and $m_n$
directly, so for $K = p$ ($Z = 1, N = 0$) and $K = n$ ($Z = 0, N = 1$)
the formula returns the input mass exactly.  This is by
construction; the framework's three CAL inputs are $m_e$, $m_p$,
$m_n$ (CODATA), with $Q_\beta = m_n - m_p - m_e$ derived.

**2. The $\Delta$ column is the prediction target, not an error.**
The $+2.225$ MeV / $+8.482$ MeV / $+7.718$ MeV differences are
the actual nuclear binding energies — the
[deuteron binding](https://en.wikipedia.org/wiki/Deuterium),
[tritium binding](https://en.wikipedia.org/wiki/Tritium),
[³He binding](https://en.wikipedia.org/wiki/Helium-3).  Predicting
these from the categorical structure (rather than reading them
from CODATA) is the territory of:

- $\rho_K^{\text{full}}(Z, N) = \rho_K^{\mathrm{LO}}(Z, N) + (1/|\mathrm{tr}_M|)
  \cdot \sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda(K)$
  ([`rho_k_h3a_refinement.py`](../../../folio-assistant/computations/rho_k_h3a_refinement.py)
  on PR #564 deuteron-only proof-of-concept; closure error
  $2.7 \times 10^{-48}$ MeV by construction).
- The per-block binding fractions $\Delta_\lambda(K)$ — currently
  determined by Occam's-razor minimal-perturbation selection
  (single dominant partition); the categorical derivation of
  $\Delta_\lambda$ from first principles is an open research
  question.

## Performance summary

| Path | Time (5 atoms) | Precision floor |
|---|---:|---:|
| Canonical reducer (`markov_trace_recursive`, 50 dps mpmath) | ~30 s | $10^{-50}$ |
| Hybrid partition-sum (30-dps $y_\lambda$ + float64 $\chi^\lambda_q$) | ~66 s | $10^{-14}$ (machine $\varepsilon$) |
| Full mpmath partition-sum (PR #564) | ~5–10 min | $10^{-50}$ |
| Pure float64 partition-sum (legacy) | ~1 s | $10^{-5}$ at $n = 9$ |
| Pure symbolic Wenzl + symbolic χ^λ | timeout (>4 min) | exact |

The hybrid technique (30-dps $y_\lambda$ + float64 $\chi^\lambda_q$,
with per-`n` cache) is the **recommended default** for
partition-sum consumers needing better than $10^{-5}$ agreement
without the overhead of full 50-dps mpmath.

## Cross-references

- [`prop:atomic-mass-gb-nf`](atomic-mass-gb-nf.md) — the master
  mass formula $\mathcal{M}(K) = \rho_K \cdot m_e \cdot |\mathrm{tr}_M|$.
- [`prop:q-hecke-seminormal-character-closure`](q-hecke-seminormal-character-closure.md)
  — the partition-sum / canonical-reducer agreement at machine $\varepsilon$.
- [`prop:hecke-branching-trace-decomposition`](hecke-branching-trace-decomposition.md)
  — the operator-valued LR-block formula behind the partition sum.
- [`docs/audits/2026-05-08-q-hecke-character-gap-closure.md`](../../../docs/audits/2026-05-08-q-hecke-character-gap-closure.md)
  — full audit of the closure with three-path comparison.
- [`docs/audits/2026-05-08-rho-k-mass-table-audit.md`](../../../docs/audits/2026-05-08-rho-k-mass-table-audit.md)
  — pre-q-Hecke audit of the ρ_K mass table at 0.23 % MAE.
