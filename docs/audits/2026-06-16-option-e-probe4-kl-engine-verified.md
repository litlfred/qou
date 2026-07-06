# Option-E PROBE 4 prune — now engine-verified on real Kazhdan–Lusztig data

**Date:** 2026-06-16
**Branch:** `claude/option-e-probe4-kl-engine-validation-2026-06-16`
**Status:** strengthens the merged PROBE-4 KL-positivity prune from theorem-cited to engine-verified.
**Discipline:** formalize-first; no fit.

## Why this follow-up

The merged prune ([`2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md))
argued from the **KL-positivity theorem** that a Kazhdan–Lusztig multiplicity sum
$\sum_w n^w_\lambda X_w$ cannot supply the mixed-sign target $\Delta_\lambda=\mathrm{sgn}(w_0^{S_{\lambda'}})\dim$.
With the in-repo compute located (the KL engine lives at **`computations/kazhdan_lusztig.py`** — the live path,
not the stale `folio-assistant/computations/`), the prune's two premises are now checked on **real KL data**.

## Engine verification (`scripts/option_e_probe4_kl_engine_validation.py`, exit 0)

Using the real engine `computations/kazhdan_lusztig.py`:

- **(P1) KL positivity at $S_4$** — the smallest symmetric group with non-trivial KL polynomials: all
  $24^2=576$ polynomials $P_{x,w}(q)$ have **non-negative integer coefficients**. The 6 non-trivial ones are
  **all $q+1$** (the classical $S_4$ result). ⇒ any cell-module multiplicity $n^w_\lambda$ (built from the
  $C$-basis, whose change-of-basis coefficients are these non-negative $P_{x,w}$) is a **non-negative integer**.
- **(P2) mixed-sign target at $n=4$** — $\Delta_\lambda=\mathrm{sgn}(w_0^{S_{\lambda'}})\dim$ gives
  $(4)\!:\!+1,\ (3,1)\!:\!-3,\ (2,2)\!:\!+2,\ (2,1,1)\!:\!-3,\ (1^4)\!:\!+1$ → **3 positive, 2 negative**.

(P1) + (P2) ⇒ a non-negative-weighted sum $\sum_w n^w_\lambda X_w$ cannot reproduce the chirality **sign** of
the target; it can supply at most the magnitude $|\Delta_\lambda|=\dim$ (already the deuteron $f^\lambda$). **PROBE 4 is
not a closure mechanism** — now confirmed on real KL polynomials, not only the theorem.

## Net

No change to the verdict (PROBE 4 de-prioritised; honest frontier = PROBE 2, the A=4 interface operator, the
sibling A≥3 cluster's scope #2369/#2371/#2372). This follow-up simply removes the "theorem-cited, not run" caveat:
the positivity premise is now demonstrated on the actual $S_4$ KL polynomials produced by the repo's engine.

## Note on infra

The compute referenced throughout the corpus as `folio-assistant/computations/*.py` is in fact tracked in **qou
at top-level `computations/`** (5770 files, incl. `kazhdan_lusztig.py`); `folio-assistant/computations/` is a
stale path from before the platform/content split. Audit checkers that need the real engine import from
`computations/`.

## Cross-references

- [`2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md) — the merged prune (theorem argument)
- [`docs/coordination/option-e.md`](../coordination/option-e.md) — Δ_λ closure ledger
- `computations/kazhdan_lusztig.py` — the KL engine used here
- `scripts/option_e_probe4_kl_engine_validation.py` — this engine verification (exit 0)
