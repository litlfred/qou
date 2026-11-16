---
# qou-8jq2
title: Reconcile the mu3 arc onto the canonical signed cyclic Markov trace (non-cyclic perblock vs tr_M)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T09:09:03Z
updated_at: 2026-11-16T19:15:00Z
parent: qou-rtxm
---


## The finding

The μ₃ arc (#4404 → #4657 → #4662) computes `Δ²g` from the **non-cyclic perblock**
`g = Σ_λ y_λ |χ_λ|`. The corpus canonical object is the **signed cyclic Jones–Markov
trace** `tr_M = Σ_λ y_λ χ_λ`. That reconciliation has never been done for this context.

This is **not** a fresh question — an earlier chat framing of mine ("nobody derived
why `|χ|`") was wrong and is corrected in
`docs/audits/2026-08-07-mu3-door-status-consolidated.md` §4quater. The prior art:

- **`Σ y_λ|χ_λ|` is a named object** — the *non-cyclic perblock*, explicitly
  contrasted with the cyclic `tr_M` in
  `docs/audits/2026-08-01-deltalambda-milnor-exact-coefficient.md` (#4364 / #4378).
  The modulus is what breaks cyclicity.
- **The signed convention is corpus-canonical for binding**, and the modulus form is
  deprecated on exactly that ground:
  `docs/audits/2026-06-13-binding-method-reconciliation-and-defit-program.md` §1 —
  *"the double-modulus form was a non-archimedean misuse"*;
  `hecke_core.atom_markov_trace` / `binding_from_frobenius_pairing` are DEPRECATED.
- **The canonical trace is pinned**:
  `computations/markov/markov_trace_canonical.py::tr_M_element`, `z = 1/(√q + 1/√q)`,
  **forced** by the four Jones/Wenzl axioms (`prop:categorical-mass-markov`).
- **Reconciliation is a known blocker**:
  `docs/audits/2026-06-09-binding-trace-convention-split.md` found binding split
  across ≥3 incompatible `(tr_M, χ^λ)` conventions disagreeing by **factors of ~7 in
  χ**, and called reconciliation — not compute — the real blocker.

## What is already measured (so this does not need re-deriving)

`computations/deltalambda/mu3_abs_choice_robustness_probe.py` computes both readings
from identical braid words and identical `y_λ`:

| reading | Δ²g (T) | Δ²g (³He) | c₃ (T) | c₃ (³He) | door |
|---|---|---|---|---|---|
| non-cyclic perblock (as published, #4404) | +0.422547 | +0.335746 | −1.7688 | −1.4054 | closed |
| signed cyclic (corpus-canonical) | +0.389988 | +0.317449 | −1.6325 | −1.3288 | closed |

**The door is closed under both**, ~5–8 % apart. So this does **not** threaten the
§2 exclusions or the §4.2 sign rule.

## What it does affect

1. **Which `c₃` is the canonical published number.** Re-designating it has downstream
   reach and is an **owner call** — not something to change as a side effect of a
   robustness probe. That silent-convention-drift failure mode is exactly what the
   2026-06-09 audit exists to prevent.
2. **The per-block classification of #4657.** The split of submodular pushes into
   *Fréchet-violating* vs *negative-weight* (7 T / 9 ³He) is computed on `|χ|` and is
   conditional on it, since `abs()` flips sign on a substantial fraction of blocks.

## Mitigation already known

On the **Brunnian** family the cyclic and non-cyclic forms **coincide to machine
precision** (`milnor-exact-coefficient`). So the divergence is not universal — it is
specific to the non-Brunnian A=3 words used in the μ₃ arc. Worth checking whether the
A=3 words can be re-expressed Brunnian-ly, which would collapse the question entirely.

## Definition of done

1. Owner decides which reading is canonical for the μ₃ context (or rules that the
   Brunnian coincidence makes it moot).
2. If signed: re-publish `c₃`, and re-run the per-block Fréchet classification on the
   signed object — the violator sets will change.
3. Either way, the μ₃ producers state which trace object they use, in the docstring
   and the witness, so the next reader does not have to infer it from a call site.

## 2026-11-16 — Signed Cyclic Markov Trace vs Non-Cyclic Per-Block Modulus Readout in Lean (PR #8162)
- Formalized `signed_trace_abs_le_perblock_modulus` (`|y₁ · c₁ + y₂ · c₂| ≤ y₁ · |c₁| + y₂ · |c₂|` for `y₁, y₂ ≥ 0`) and `perblock_modulus_overshoot_and_nonadditivity_witness` (strict inequality on opposite-sign block characters and explicit refutation of additivity for `T_abs`) in `folio/quantum-observable-universe/lean/QOU/Foundations/WenzlTemperleyLiebH4Keystone.lean` (wired into `QOU.lean`, 0 `sorry`).
- PR: https://github.com/litlfred/qou/pull/8162 (commit `f3dcbfe5fb51a67f3233319674c13a3791ba91d2`). Status kept `in-progress`.
