# Mirror-pair Coulomb sign-correction — general wiring + open-invariant attempt

**Date:** 2026-06-19
**Branch:** `claude/he3-mirror-coulomb-sign-correction-2026-06-19`
**Builds on:** #2467 (physical-z pin), #2478 (³He charge-asymmetry + pair-knot
synthesis), the A=3 diagnosis
[`docs/audits/2026-06-18-he3-brane-tower-structural-gap.md`](../audits/2026-06-18-he3-brane-tower-structural-gap.md).

## Problem (recap of the landed diagnosis)

The per-generator brane-tower sum `Σ_i −Li₂^q(−|V̂_i^full|)` is **monotone
increasing in proton near-pole count**, so it predicts the proton-richer mirror
member *more* bound — the **inverted Z-ordering** bug. At A=3 it gives
tower(³He)=5.350 > tower(³H)=5.072, but B_AME(³He)=7.718 < B_AME(³H)=8.482.

The diagnosis's "open question for the branch" (audit §"Where the fix must
live", lines 77–82) is precisely this tranche's task:

> Does replacing the duplicated proton per-generator pair with the
> pair-knot composite, plus an explicit Z(Z−1)/2 Coulomb term, restore the
> correct mirror ordering without per-atom retuning?

## What this tranche delivers

### 1. General sign-correction (the user's "do this in general")

Two structurally-motivated, **fit-free** changes to the tower's operator
content, wired across *all* mirror pairs (not just A=3):

- **(a) Composite pair-knot replacement.** The doubled proton near-pole pair is
  treated as one composite `σ_pp` knot rather than two additive per-generator
  terms. This removes the spurious additive over-count
  `E₀·Δtower ≈ 1.165 MeV` (wrong sign — it favored ³He;
  `he3-tower-charge-asymmetry.witness.json`) and restores the exact Z↔N
  Markov-trace isospin symmetry `tr_M(σ_pp) = tr_M(σ_nn)`.

- **(b) Explicit Z(Z−1)/2 Coulomb term.** The `C(Z,2) = Z(Z−1)/2` proton pairs
  each contribute the **derived** per-pair Coulomb reduction `ratio·B_pp`
  (`def:coulomb-charge`, `Q_pp=+1`, `ratio = tanh(ln q₀) = (q₀²−1)/(q₀²+1)`,
  Lean-proved; the 31%-covered value of `charge_coulomb_tn3he_derived.py`). The
  `Z(Z−1)/2` count is **pure combinatorics — no fit**; only the per-pair
  *magnitude* carries the known-open residual.

The Coulomb term reduces the proton-richer member's binding, so the corrected
ordering is right for **every** mirror pair with no per-atom retuning. The A=3
pair is computed fully from the H_6 trace; the right-sign prediction is reported
for A=7 (⁷Li/⁷Be), A=11 (¹¹B/¹¹C), A=13 (¹³C/¹³N) using the A=3-derived per-pair
unit as a uniform estimate (clearly labelled — the per-pair bond is A=3-specific
for A>3).

### 2. Open EM-linking invariant — derivation attempt (formalize-first)

The residual magnitude (A=3: 31%; the 3.2× gap) is the **un-derived categorical
"two-like-charge brane-pairing invariant"**. Closing it by tuning a coefficient
to hit 0.764 MeV is a **CAL-4 fit — forbidden**
([`production-vs-exploratory-discipline.md`](../../.claude/skills/local/production-vs-exploratory-discipline.md)
§Rule 14). This tranche makes a *formalize-first* attempt to derive it from the
13-driver menu (the `C_λ·S_λ` factorisation at H_6 /
`prop:mass-coefficient-shadow-price` path), and records an honest verdict —
expected to be a scoping / partial / negative result, **not** a fit.

## Discipline contract (STRICT)

- All compute is **EXPLORATORY** (`probe_*` under `computations/probes/`),
  banner per discipline §Step 7.
- The Coulomb magnitude is **cited** from the canonical
  `charge-coulomb-tn3he-derived.witness.json`, not re-derived to close the gap.
- Witnesses assert the **structural facts** (sign correct, ratio exact,
  magnitude partial-not-closed) so `allPassed=true` is an honest positive.
- **No production script, dashboard, or named constant is touched.** This does
  not enter `mass_table_ppb.py` until the magnitude invariant is derived.
- Any attempt to close the residual magnitude that cannot cite a 13-driver
  derivation triggers **Rule 14 escalation**, not a commit.

## Deliverables checklist

- [x] `computations/probes/mirror_pair_coulomb_sign_correction.py` + witness —
  sign correct for all 4 mirror pairs (A=3,7,11,13); magnitude 31–47% (open)
- [ ] EM-linking invariant derivation-attempt probe + witness (formalize-first)
- [ ] Audit doc recording the general sign result + the invariant verdict
- [x] PR #2487 opened (Gemini review addressed)
