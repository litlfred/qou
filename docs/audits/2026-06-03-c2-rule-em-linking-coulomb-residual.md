# c=2 selection-rule × T-³He Coulomb-residual probe — a 0.1 %-level lead

**Date:** 2026-06-03
**Probe:** [`folio-assistant/computations/probes/c2_rule_em_linking_residual.py`](../../folio-assistant/computations/probes/c2_rule_em_linking_residual.py)
**Witness:** `c2-rule-em-linking-residual.witness.json`
**Branch:** `claude/habiro-per-knot-lambda-derivation-2026-06-03` (PR #1765 follow-up)
**Status:** EXPLORATORY. Suggestive lead at 0.1 % — **NOT** a derivation. No production wiring, no fit.

## What this tests

PR #1775 / [`docs/audits/2026-06-03-charge-coulomb-tn3he-derived.md`](2026-06-03-charge-coulomb-tn3he-derived.md) derives the categorical pp-Coulomb piece of the T-vs-³He AME binding split:

```
derived_Coulomb_dHe · [open EM-linking invariant] = AME split
   0.2377 MeV      ·    REMAINING_FACTOR 3.2137× = 0.7638 MeV
```

The 3.2137× is the open derivation target on **PR #1777** ("Derive the two-like-charge EM-linking invariant"). PR #1765 ships a zero-parameter per-component selection rule

```
lw(L; c=2) = (1/3) · Σ_{λ⊢3} dim_q V_λ = (q+1)² / (3q)
```

— the natural per-link scalar for the two-proton 2-component-link case. Question: does it fit the slot?

## Result

| object | value at q₀ | notes |
|---|---|---|
| `lw_c2(q₀) = (q+1)²/(3q)` | **1.336966** | zero-parameter selection rule |
| target factor | **3.213697** | exact from charge-coulomb witness |
| measured residual = target / lw_c2 | **2.403725** | what the EM-linking slot still needs |
| **candidate (a):** `12/5 = dim H_4 / I(4)` at q=1 | 2.400000 | −0.155 % off residual |
| candidate (b): `Σ dim_q² / Σ dim_q` at H_4, q₀ | 2.438529 | +1.448 % off residual |

Best factorization:

```
predicted_split = derived_Coulomb · lw_c2(q₀) · (12/5)
                = 0.2377  ·  1.336966  ·  2.4
                = 0.762616 MeV   vs AME 0.7638 MeV   →  −0.155 % off
```

## Honest framing — suggestive lead, not a derivation

**Why it's interesting:**

- The c=2 selection rule lands the residual within **0.155 %** of the *classical-limit* Wedderburn ratio `dim H_4 / I(4) = 24/10 = 12/5`.
- `12/5` carries a clean structural reading: regular-rep dimension over Gelfand-rep dimension at the proton's Wedderburn rank H_4 — exactly **one rank above** c=2's H_3, the same `n → n+1` jump my selection rule's open mechanism (lepton-fibre adjunction) hypothesizes.
- The full prediction reproduces the AME T-³He split to 0.155 %.
- **Zero free parameters.** The selection rule is fixed (anchored exact at muon c=1, proton c=3) and 12/5 is a categorical integer ratio.

**Why it's NOT a derivation:**

- 0.155 % is **NOT** derivation-tight. Δ_λ-gate / 1ppQ-level work requires ppm or better; this is ppt.
- The factorization mixes a **q-deformed** lw_c2(q₀) with the **classical-limit** 12/5. The natural fully-q-deformed analogue (candidate b: `Σ dim_q² / Σ dim_q` at H_4, q₀) lands **worse** (1.45 % off). There is no a-priori categorical reason for the un-q-deformation in the 12/5 piece.
- Could easily be coincidence at this precision — Wedderburn integer ratios at low n are not numerous enough to rule out chance.

**What would close it:**

1. A categorical reason for why `dim H_4 / I(4) = 12/5` enters un-q-deformed alongside the q-deformed lw_c2(q₀). E.g., maybe 12/5 lives in the **classical-limit projector** that selects the lepton-adjunction direction at the H_3 → H_4 boundary, while lw_c2(q₀) is the q-active Wedderburn weight inside that boundary.
2. OR: a different residual identification that lands at ≤ ppm. (Plausible candidates not yet tried: `(q+1)²/q + integer`, `[2]_q · ratio_classical_(H_5)`, etc.)
3. OR: the open derivation of PR #1777 lands by a different route entirely, and this 0.155 % near-match is recorded as a curious coincidence.

## Q-usage discipline

All symbolic work at fibre level (formal q). q₀ enters only at the final archimedean evaluation (Im(q₀) = 0). 12/5 is the **classical** limit at q = 1 — also a legitimate archimedean point. No |q| = 1 step. CLAUDE.md §7c compliant.

## Coordination

- **PR #1765** (selection rule home): this probe sits as a downstream consumer artefact, not a wiring change to the selection-rule probe itself.
- **PR #1777** (EM-linking invariant open derivation): concrete numerical candidate posted as a comment alongside this audit. The slot now has a falsifiable target shape: any derivation of the EM-linking invariant should either reproduce `lw_c2 · (12/5)` (or its q-deformed analogue) to ≤ ppm, or it gives a structurally different answer.
- **PR #1775** (parent Coulomb work): inputs sourced from its witness (provenance inlined in the probe).

## Next on the queue

Either:

- **(A) Categorical derivation attempt:** justify why 12/5 appears un-q-deformed in this factorisation — natural candidate is the H_3 → H_4 boundary projector. If it lands, the EM-linking invariant is derived; if it refutes, the 0.155 % is coincidence.
- **(B) Scan alternative residuals** before committing to (A) — `(q+1)/q`-family, `[n]_q · classical_integers`, etc.
- **(C) Hand off:** leave as exploratory candidate on PR #1777, let that PR's author pursue or refute via their own framework-knowledge.
