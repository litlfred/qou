# Binding magic-A wireup — the existing-but-unwired ⁴He formula

**Authored:** 2026-05-31
**Branch:** `claude/binding-magic-A-wireup-2026-05-31`
**Trigger:** Explaining why
[`binding-alpha-shift-extension`](../../content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean)
misses ⁴He binding by 5× (per the
[2026-05-31 status audit](2026-05-31-binding-alpha-shift-a4-status.md))
revealed the framework already carries a different formula that hits
⁴He to within 6% — but it isn't reachable from the §3b-cond class.

## Headline

For doubly-magic ⁴He (Z=N=2):

| Formula | Predicted B(⁴He) | Experimental | Miss |
|---|---:|---:|---:|
| `binding-alpha-shift-extension` (α_shift via T(3,4)) | 5.93 MeV | 28.30 MeV | **−79%** (5× too small) |
| [`magic_A_formula::magic_A_binding`](../../folio-assistant/computations/magic_A_formula.py) (ρ_F·m_e·A·8G, ρ_F=2) | 29.96 MeV | 28.30 MeV | **+5.9%** |

Wiring the existing magic_A path through for the doubly-magic case
closes the ⁴He gap by **13.5×** (|rel_err| from 0.7904 → 0.0587),
with zero new math required.

## What the framework already has (per existing code)

1. **`magic_A_formula.py`** — explicit:
   > *The reason ⁴He uses the magic-A rule rather than tr_M(T_w) is
   > that ⁴He has no single hyperbolic knot — it is doubly magic
   > (Z = N = 2, both magic) and the shell-closure structure replaces
   > the per-knot Markov-trace evaluation.*

2. **`prop:diagrammatic-double-magic-lr-fusion`** — algebraic content:
   - LR-fusion at double-magic is **rigid**: `V_λ ⊗ V_μ → V_ν` with
     multiplicity 1 and content sum zero.
   - *"no Wedderburn block at the double-magic level capable of
     absorbing further binding energy through Hecke channels"*
   - *"exceptional double-magic stability is the algebraic absence of
     decomposition channels, not a fitted shell-correction term"*

3. **`rem:strutinsky-from-graded-trace`** — the categorical
   decomposition is **forced**:
   $$
     \mathrm{tr}_M(T_w, q_0)
       = \mathrm{tr}_{\mathrm{gr}}(\sigma(T_w), q_0)
       + \mathrm{Res}_{\mathrm{GB}}(T_w, q_0)
   $$
   with the residue sum identified as the Strutinsky shell correction
   $\delta E_{\mathrm{shell}}$.  *"Magic-number enhancement arises
   algebraically when λ reaches a rectangular shape and H_q(λ)
   factorises"* (per `prop:shell-schur-weyl-self-duality`).

4. **`prop:shell-closure-normal-form`** (Lean ref:
   `qou:QOU.OptimalNF.optimal_nf_is_standard_basis`) — Poincaré
   distribution of the Hecke normal form at shell closure.

5. **`prop:gravity-spectral-prefactor`** — supplies the
   `8G = Vol(L6a4) = Vol(Borromean)` factor.

6. **`binding_ladder_catalog.py:63`** — supplies `ρ_F = 2` for ⁴He
   as `2·m_e·4·Vol(L6a4)`.

7. **`binding_shell_enhancement_derivation.py`** — the prior probe
   that confirmed the deuteron is exact and the A≥3 enhancement is
   "multiplicative per closure with f ≈ 2.45–2.88 (17% spread)",
   and refuted a single-q-power scalar closing it (p/n asymmetry kills
   any scalar derived factor).

## The wire-up gap

The §3b-cond class
[`BindingForceCarrierKnot`](../../content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean#L106)
takes a single `αShiftAt : ℕ → ℕ` per nucleus, embedding the
**implicit assumption** that every light nucleus has a single
hyperbolic force-carrier knot whose `k·(p−1)` pole order suffices.
For doubly-magic A's that assumption is false by construction — the
shell-closure rigidity means there is no single hyperbolic knot.

The current `lightNucleiForceCarrierKnot` instance dutifully maps
A=4 to `T(3,4)` per the agent-survey table, and gets the wrong
number (-79%). The categorical answer is "A=4 is in a different
regime; dispatch to magic_A".

## The minimal fix

Three options, in order of scope:

### Option 1 — Witness-side dispatch (this PR's deliverable)

Extend [`binding_alpha_shift_witness.py`](../../folio-assistant/computations/binding_alpha_shift_witness.py)
to compute and report **both** formulas for each candidate, with the
doubly-magic predicate dispatching to `magic_A_formula`. The witness
JSON now carries `B_predicted_magic_A_MeV` + `ratio_magic_A_over_exp`
for the ⁴He row alongside the original alpha_shift columns. Honest
audit; no Lean / canonical changes; closes the "what's the wire-up
look like" question.

**Status:** done in this PR. Output:

```
   A nucleus T(p,k)   α_shift     B_pred      B_exp  pred/exp
   2 D     T(2,3)         3     2.2246     2.2246    1.0000
   3 T     T(2,5)         5     3.7076     8.4818    0.4371
   3 ³He   T(2,5)         5     3.7076     7.7181    0.4804
   4 ⁴He   T(3,4)         8     5.9322    28.2957    0.2096
```

with the new gap report: *"For doubly-magic ⁴He the magic_A formula
B = ρ_F·m_e·A·8G predicts 29.956 MeV (+5.9% miss), closing the
alpha_shift gap by **13.5×** (|rel_err| 0.7904 → 0.0587)."*

The script dispatches to the canonical
[`magic_A_formula.magic_A_binding`](../../folio-assistant/computations/magic_A_formula.py)
rather than mirroring the formula locally; `VOL_BORROMEAN` is sourced
from `knot_volumes` (mpmath 50dps) via that import chain.

### Option 2 — Lean dispatcher class (DONE in this PR)

**Status:** completed via the new content block
[`prop:magic-A-binding-formula`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula.md).
The block triple ships:

- [`magic-A-binding-formula.ts`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula.ts) —
  manifest, `proposition` kind, `uses` cites
  `prop:binding-alpha-shift-extension`,
  `prop:diagrammatic-double-magic-lr-fusion`,
  `rem:strutinsky-from-graded-trace`.
- [`magic-A-binding-formula.md`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula.md) —
  narrative theorem statement (conditional on
  `conj:magic-numbers-bring` + `prop:gravity-spectral-prefactor`)
  with the two-regime dispatch table.
- [`magic-A-binding-formula.lean`](../../content/quantum-observable-universe/mass-theory/magic-A-binding-formula.lean) —
  Lean §3b-cond formalisation:
  - `isMagic : ℕ → Prop` (magic-number predicate)
  - `isDoublyMagic Z N : Prop` (conjunction)
  - `class CatalanPrefactor R` (abstracts `8G` as a field-level
    parameter so the formula statement doesn't depend on
    Catalan-constant Mathlib import depth)
  - `class MagicABindingFormula B m_e` (the §3b-cond hypothesis
    bundling `ρ_F` per (Z, N) and the formula
    `B Z N = ρ_F · m_e · A · 8G`)
  - `theorem magic_A_binding_formula` — sorry-free conditional
    theorem discharging the formula from the class hypothesis
  - `theorem he4_is_doubly_magic` — `isDoublyMagic 2 2` proven by
    `Or.inl rfl`
  - `theorem two_regime_dispatch_exists` — non-trivial existence

Per CLAUDE.md §3b-cond: the formula is a rigorous-conditional
theorem — fully verified by Lean modulo the single class hypothesis
`MagicABindingFormula`. The class field `formula` discharges
definitionally for any concrete (Z, N) instance; the categorical
derivation of `ρ_F = 2` for ⁴He (Open Math A below) is the
remaining open content.

Chapter manifest
[`mass-theory.ts`](../../content/quantum-observable-universe/mass-theory/mass-theory.ts)
updated to include the new block after
`binding-alpha-shift-extension`.

### Option 3 — Canonical-side full-trace replacement (research)

Per the user's question: *"replace α_shift(T(p_A, k_A)) with the
full Markov-trace sum over ALL partitions."* This means folding the
two regimes into one: the binding becomes
`B = m_e · F[tr_M(β_atom)]` for the full Markov trace, where the
graded-trace + residue split (`rem:strutinsky-from-graded-trace`)
naturally produces the magic-A enhancement at doubly-magic Z, N via
the rectangular-partition spike. The `canonical_tr_m_via_branching.py`
infrastructure already computes the full trace; the binding wiring
would consume its output rather than the single-knot α_shift.

This is the right long-term path — it makes Option 2 a special case
(magic A's pick up the residue spike automatically) — but the
functional `F[·]` derivation and the `tr_M → B` calibration are
research-grade.

## ρ_F = 2 — what derives it?

The current ⁴He magic_A formula uses `ρ_F = 2` from
`binding_ladder_catalog.py:63`. The canonical chain
([`prop:gravity-spectral-prefactor`](../../content/quantum-observable-universe/mass-theory/gravity-spectral-prefactor.md))
should fix it from first principles; the chain is plausible but the
exact derivation of the integer 2 (vs `[2]_q` vs `2 cos(π/3)` etc.)
is not in the file. This is **Open Math A**:

> Derive `ρ_F = 2` for ⁴He from the categorical structure (likely
> via the Borromean-rings residue prefactor `8G` and the doubly-magic
> LR-fusion rigidity).

## A=3 (T, ³He) — what closes them?

Neither formula closes A=3:
- α_shift miss: T −56%, ³He −52%
- magic_A_formula is N/A (T, ³He are *single*-magic, not doubly)

The `binding_shell_enhancement_derivation.py` finding is the relevant
constraint: **T (f≈2.82) ≠ ³He (f≈2.45)** — a 15% p/n asymmetry that
no scalar q-factor can produce. **Open Math B**:

> The single-magic enhancement is p/n-asymmetric; identify the
> categorical object that carries the proton/neutron distinction
> for the H_9(q) Wedderburn block at A=3.

## Action items

1. ✓ **This PR**: witness emitter shows the 13.5× ⁴He gap closure
   (|rel_err| 0.7904 → 0.0587) via the wired-in formula.
2. ✓ **This PR (now)**: Lean content-block triple
   `magic-A-binding-formula.{ts,md,lean}` ships the §3b-cond
   formalisation + chapter-manifest entry. The Lean theorem
   `magic_A_binding_formula` is sorry-free conditional on the
   `MagicABindingFormula` class hypothesis.
3. **Research (Option 3 + Open Math A, B)**: full-trace functional
   derivation; ρ_F = 2 derivation from
   `prop:gravity-spectral-prefactor`; p/n asymmetric A=3 closure.

## References

- [`binding-alpha-shift-extension.lean`](../../content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean) — the §3b-cond class that needs the dispatcher.
- [`magic_A_formula.py`](../../folio-assistant/computations/magic_A_formula.py) — the doubly-magic formula `B = ρ_F·m_e·A·8G`.
- [`binding_shell_enhancement_derivation.py`](../../folio-assistant/computations/binding_shell_enhancement_derivation.py) — prior shell-enhancement probe.
- [`prop:diagrammatic-double-magic-lr-fusion`](../../content/quantum-observable-universe/observations/diagrammatic-double-magic-lr-fusion.md) — LR-rigidity at double-magic.
- [`rem:strutinsky-from-graded-trace`](../../content/quantum-observable-universe/observations/strutinsky-from-graded-trace.md) — Strutinsky decomposition is forced by graded-trace residue split.
- [`magic-ladder-pattern-investigation.md`](../../folio-assistant/computations/magic-ladder-pattern-investigation.md) — confirms pure partition combinatorics doesn't pick out the magic ladder; the categorical input is required.
- [Binding A=4 already-closed audit (2026-05-31)](2026-05-31-binding-alpha-shift-a4-status.md) — the precursor finding.
- [Universal-branching multinucleon gap audit (2026-05-30)](2026-05-30-universal-branching-multinucleon-gap.md) — analogous "already-implemented" pattern (Track B Gap #2).
