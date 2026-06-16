# Option-E PROBE 4 — KL-positivity prune: crystal multiplicities cannot supply the Δ_λ chirality sign

**Date:** 2026-06-16
**Branch:** `claude/option-e-probe4-kl-positivity-prune-2026-06-16`
**Status:** formalize-first prune of the remaining in-Option-E path (PROBE 4); no fit.
**Discipline:** formalize-first (narrow the search before running it) + critical-distance.

## Context

The Δ_λ closure ledger ([`docs/coordination/option-e.md`](../coordination/option-e.md)) records the deuteron
**closed** by the structural form
$$\Delta_\lambda = \mathrm{sgn}(w_0^{S_{\lambda'}})\cdot\dim(V_\lambda)$$
(a chirality sign times the regular-rep dimension $f^\lambda$). The single remaining in-Option-E direction is
**PROBE 4**: derive $\Delta_\lambda$ from a Kazhdan–Lusztig / crystal **multiplicity sum**
$\sum_w n^w_\lambda\,X_w$ (extending `kazhdan_lusztig.py` past its $n\le4$ cap to $S_6$). Single-vertex /
trivial-multiplicity candidates were already refuted (they return $\chi^\lambda$); PROBE 4 hopes the
**non-trivial** KL multiplicities close it.

## The prune (verified — `scripts/option_e_probe4_kl_positivity_prune.py`, exit 0; no KL engine needed)

1. **The target is mixed-sign.** $\Delta_\lambda = \mathrm{sgn}(w_0^{S_{\lambda'}})\cdot\dim$ has both positive
   and negative blocks: $n=3 \to 1{+}/2{-}$; $n=6 \to 6{+}/5{-}$ (computed).
2. **KL multiplicities are non-negative.** $n^w_\lambda\in\mathbb{Z}_{\ge0}$ — Kazhdan–Lusztig positivity
   (classical for $S_n$ via intersection cohomology of Schubert varieties; Elias–Williamson in general).
3. **Therefore** a sum $\sum_w n^w_\lambda\,X_w$ with $n^w_\lambda\ge0$ can produce the negative $\Delta_\lambda$
   blocks **only** if the sign comes from the $X_w$ (the braid-image traces), never from the multiplicities.

**Consequence.** The crystal/KL multiplicity structure can supply at most the **magnitude**
$|\Delta_\lambda| = \dim(V_\lambda)$ — which is *already* the deuteron closure's $f^\lambda$. The chirality
**sign** $\mathrm{sgn}(w_0^{S_{\lambda'}})$ must be supplied exogenously, exactly as the closed deuteron formula
already does. So PROBE 4 is **not a new closure mechanism**: at best it re-derives $|\Delta_\lambda|=\dim$ by a
longer (KL) route, and it cannot supply the sign that is the actual structural content of the closure.

## Recommendation

**De-prioritise the $S_6$ KL extension** (the "remaining in-Option-E path"). Spending a session extending
`kazhdan_lusztig.py` to $S_6$ to run the full $n^w_\lambda$ sum would hit this positivity wall: the output is
sign-positive by construction, but the target is mixed-sign. The honest Option-E frontier is therefore **not**
PROBE 4 but **PROBE 2** (the A=4 multi-nucleon interface operator — where the deuteron's $\mathrm{sgn}\cdot\dim$
may not even extend, and a genuinely new categorical operation is needed), which is the live scope of the sibling
A≥3 compute cluster (#2369/#2371/#2372).

This does **not** refute Option-E or the deuteron closure; it prunes one specific remaining sub-path on a
structural (KL-positivity) ground, consistent with the standing "no 7th fit-based ansatz" discipline.

## Sandbox note

The KL engine (`kazhdan_lusztig.py`) and the Option-E witnesses live in `folio-assistant/computations/`, which is
unpopulated in this sandbox (0 `.py`), so PROBE 4 could not be *run* here regardless — this prune is the
formalize-first reason it need not be, computed from pure combinatorics + the KL-positivity theorem.

## Cross-references

- [`docs/coordination/option-e.md`](../coordination/option-e.md) — Δ_λ closure ledger (PROBE 4 §"Open probes")
- `docs/audits/2026-05-26-delta-lambda-binding-formula-closure.md` — the deuteron sgn·dim closure
- `scripts/option_e_probe4_kl_positivity_prune.py` — sign pattern + positivity prune (exit 0)
