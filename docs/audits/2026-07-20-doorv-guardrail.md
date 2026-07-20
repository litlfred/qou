# Door-v bar-parity GUARDRAIL — decay (bar-odd) is not derivable from binding (bar-even) (2026-07-20)

**Bean:** `qou-fawf` · **Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**Status:** GUARDRAIL landed. **Structural confirmation only — NO new physical
number** (no AME data, no fit, no q₀-derived prediction).

## The rule this guardrail encodes

The framework's bar involution (`q ↦ q⁻¹`) splits every q-difference observable
into two sectors of **opposite `(−1)^m` parity**:

| Sector | Observable | Character | Module | Sign structure |
|---|---|---|---|---|
| **bar-even** | mass / binding | cosh | C1 kernel | **non-negative cone** (sum of real squares `f₊²`, `f₋²`, provably `≥ 0`) |
| **bar-odd** | Q_β / decay | sinh | GGM / eq-49 | **`(−1)^m` alternating** (growing GGM: `y_{m+1} ~ −q^m y_m`) |

Door-v ([`…qlift-doorV-stokes.md`](2026-07-20-qlift-doorV-stokes.md)) isolated the
**sole** residual between GGM and the C1 tensor-square `{+1,−1}` realization as
exactly this diagonal ℤ/2 `(−1)^m` character: slopes and theta magnitudes match,
the unipotent Stokes bridge is trivial (`U → I`), only the bar-parity **sign**
separates them.

This is a **parity WALL**, Lean-proved (sorry-free) in
[`QOU/Mass/DoorVParityNoIdentity.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/DoorVParityNoIdentity.lean):
`doorV_parity_no_identity` — no non-negative-cone combination of the bar-even
squares can equal a sign-alternating bar-odd target, because a real square is
`≥ 0` (`nonneg_not_signalternating`, `posCone_nonneg`). Same non-negativity
invariant as the [KL-positivity prune](2026-06-16-option-e-probe4-kl-positivity-prune.md).

**Guardrail assertion:** a bar-even (mass/binding) quantity and a bar-odd
(Q_β/decay) quantity have opposite `(−1)^m` parity and **cannot be
gauge/transform-related by any parity-preserving map**. Concretely:

> **Decay observables MUST NOT be derived from the binding kernel by any
> parity-crossing transform.** Any parity-preserving (non-negative-cone) map
> from a bar-even object stays non-negative and cannot produce the `(−1)^m`
> bar-odd alternation.

This is the producer-side realization of the impact-analysis recommendation
([`…sinhcosh-scale-impact-analysis.md §4.2`](2026-07-20-sinhcosh-scale-impact-analysis.md)):
"add a guard/annotation that Q_β is NOT to be routed through the binding kernel …
analogous to the canonical-mass guardrail."

## The producer + witness

[`computations/doorv_barparity_guardrail.py`](../../computations/doorv_barparity_guardrail.py)
(mpmath dps=50) → `doorv_barparity_guardrail.witness.json`
(`framing: "structural-confirmation"`, `adds_new_number: false`). It:

1. Models the two sectors — bar-even = squares `f₊²`, `f₋²` of the C1 carriers
   (real squares, `≥ 0`); bar-odd = the growing GGM solution's `(−1)^m` sign
   character. **Sign structure only — no magnitude, no fit, no data.**
2. Verifies both squares classify **bar-even** (no consecutive flip), GGM
   classifies **bar-odd** (genuine flip), at `q ∈ {0.9, 1.05, 1.10998}`
   (q-independent — the sampled q is a structural sample, **not** a prediction).
3. Exposes `check_parity_derivable(bar_even_seqs, bar_odd_seq)` — the FLAG a
   future producer calls: `violation=True` when a compute tries to derive a
   bar-odd observable from bar-even sources by a parity-preserving map.
4. Self-tests: the wall fires on the (even → odd) derivation and a negative
   control (even → even) does **not** flag.

Result: `structural_confirmation = True` at all three q.

## Discipline

Adds **no** production number; it is a guardrail + structural confirmation, per
the anti-fit rule. The scope-(b) exclusion it encodes cites a **proved
invariant** (`0 ≤ x²`), not a numerical near-match. Corpus-grep: the C1↔GGM
bar-parity trail is this branch's 2026-07-20 files; no closed item re-opened.
Lean backing: `QOU.Mass.DoorVParityNoIdentity.doorV_parity_no_identity`.
