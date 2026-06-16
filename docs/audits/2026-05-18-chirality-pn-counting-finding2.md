# Finding 2 closure: `term5_aK_audit.aK_closed_form` ↔ canonical sign-pattern reconciliation

> **Status (2026-05-18, this branch):** closes Finding 2 of
> [`2026-05-18-item-b-chirality-v234-audit.md`](2026-05-18-item-b-chirality-v234-audit.md):
> the pn-counting discrepancy at T/³He between
> `term5_aK_audit.aK_closed_form` and
> `prop:chirality-dual-space-derivation`'s verification table.
>
> Also includes a **Lean-side audit** of
> `chirality-dual-space-derivation.lean` (no sorries; two cosmetic
> gaps noted).

## The discrepancy

`term5_aK_audit.aK_closed_form(Z, N)` previously returned `1.209`
for tritium and ³He (Z=1,N=2 and Z=2,N=1 respectively), but
`prop:chirality-dual-space-derivation`'s verification table gives
`0.956 = 1 − h²` (amphichiral 1+, 1− pattern).

The discrepancy was at the **adjacency-counting step**, not the
per-crossing rule:

| convention | how pn-crossings are counted | T value at $q_0$ |
|---|---|---|
| **Audit script (old)** | adjacencies in `['p']*Z + ['n']*N` flat list | `(1+h)^1 = 1.2091` |
| **`paper_six_term_isotope_sweep.chirality_signs_for_isotope_inferred`** | (Z, N)-keyed hand-coded sign pattern per the prop | `(1+h)(1-h) = 1 - h² = 0.9563` |
| **`prop:chirality-dual-space-derivation` §"Verification"** | "1+, 1− (amphichiral)" | `1 - h² = 0.9563` |

The latter two are the canonical convention; the audit script was
the outlier.

## The fix

`term5_aK_audit.aK_closed_form` now imports
`chirality_signs_for_isotope_inferred` from
`paper_six_term_isotope_sweep` and iterates the product:

```python
def aK_closed_form(Z: int, N: int) -> float:
    from paper_six_term_isotope_sweep import (
        chirality_signs_for_isotope_inferred,
    )
    signs = chirality_signs_for_isotope_inferred(Z, N)
    h_val = float(_h_num)
    a_K = 1.0
    for s in signs:
        a_K *= 1.0 + s * h_val
    return float(a_K)
```

Verified output at $q_0$ (independent Python invocation):

| atom | (Z, N) | sign pattern | a_K | matches prop? |
|---|---|---|---|---|
| p | (1, 0) | `[]` | 1.0000 | OK (1) |
| n | (0, 1) | `[]` | 1.0000 | OK (1) |
| D | (1, 1) | `[+1]` | 1.2091 | OK (1+h) |
| T | (1, 2) | `[+1, -1]` | **0.9563** | OK (1−h²) |
| ³He | (2, 1) | `[+1, -1]` | **0.9563** | OK (1−h²) |
| ⁴He | (2, 2) | `[+1, -1, +1, -1]` | 0.9145 | OK ((1−h²)²) |

## Witness regeneration

After the fix, `term5-aK-audit.witness.json` was re-run for T and
³He (V1, ~few seconds each at A=3) to update the cached
`closed_form_aK` values. Existing p/n/D rows were carried over via
`--merge-prior`. V2/V3/V4 entries at p/n were preserved.

The V1-Gram values themselves are unchanged (the Gram-form
implementation didn't have the bug). What flips is the comparison
delta:

- T pre-fix: V1 = 1.079 vs (wrong) closed = 1.209 → Δ = 0.130 (V1 *below* closed)
- T post-fix: V1 = 1.079 vs (canonical) closed = 0.956 → Δ = 0.123 (V1 *above* closed)

The magnitudes are similar, but the sign-of-gap flips. Under the
new framing on main (`2026-05-18-m-p-item-b-t5-categorical-attribution.md
§7c`), this is unsurprising — V1-Gram is a different categorical
quantity from the closed form; nothing forces them close.

## Downstream impact survey

Searched for direct consumers of `aK_closed_form` /
`closed_form_aK` outside the audit script itself:

```bash
grep -rln "aK_closed_form\|closed_form_aK" \
  computations/ docs/audits/ 2>/dev/null
```

Result: the only direct consumer is `term5_aK_audit.py` itself
(the function and its callers within `main()`); the
`closed_form_aK` field appears in the audit witness JSON and is
read by downstream display / cross-check code (none currently
load-bearing for production mass predictions). The production
path uses `term5_chirality(Z, N, chirality_signs)` with
`chirality_signs_for_isotope` (or its `_inferred` variant) — both
of which carry the canonical pattern from the start; **the bug
was confined to the audit script's reference column.**

That means: no production mass prediction or 1ppb cross-check
output changed due to this fix. The fix is "audit-only correctness"
but important for anyone reading the witness to interpret the
V1/V2/V3 deltas in context.

## Lean-side audit: `chirality-dual-space-derivation.lean`

**Sorry count:** 0.

**What's proved:**

- `crossingChiralityFactor h c` = `1 + c.toReal * h`
- `chiralityFactor h crossings` = `List.prod` of per-crossing factors
- `chiralityFactor_nil`, `_cons`, `_replicate`, `_append` — list-shape
  lemmas (all proved)
- `tau_sym_pos_deviation` — proves `(q - (-q⁻¹)) = q + q⁻¹` (the
  "deviation" content)
- `amphichiral_factor` — proves `chiralityFactor h [+, −] = 1 − h²`
- `amphichiral_factor_k_pairs` — proves k pos-then-neg pairs give
  `(1+h)^k · (1-h)^k`
- `deuteron_factor` — proves `chiralityFactor h [+] = 1 + h`
- `pn_pair_factor` — proves T/³He value
- `he4_factor` — proves ⁴He value `(1-h²)²`
- `chirality_at_h_zero` — proves the classical limit `h=0 ⇒ a_K = 1`
- `chirality_dual_space_derivation` — the headline theorem

**Two cosmetic gaps (not blockers):**

1. **`chirality_dual_space_derivation` is tautological (`rfl`).**
   The proof reads:
   ```lean
   theorem chirality_dual_space_derivation (h : ℝ)
       (crossings : List CrossingSign) :
       chiralityFactor h crossings =
         (crossings.map (crossingChiralityFactor h)).prod := rfl
   ```
   This is literally the definition of `chiralityFactor`; it does
   not encode the prop's actual algebraic content (that the
   symmetric-channel deviation equals `h`). The algebraic content
   *is* proved separately in `tau_sym_pos_deviation`, but the
   headline theorem doesn't tie back to it. A more faithful
   formalization would prove a theorem like
   `∀ s : CrossingSign, τ_sym([σ^s]) − τ_sym([σ^{-s}]) = s · h`
   and have `chirality_dual_space_derivation` consume it.

2. **No `(Z, N) → crossing-list` mapping in Lean.** The atomic
   factor theorems (`deuteron_factor`, `pn_pair_factor`,
   `he4_factor`) take literal crossing lists as inputs
   (`[pos]`, `[pos, neg]`, `[pos, neg, pos, neg]`). They prove
   each specific list gives the expected factor, but don't tie
   "this list is the canonical one for atom (Z, N)" — the
   bridge between atomic structure and crossing-list (which is
   carried in `chirality_signs_for_isotope_inferred` on the
   Python side) is not in Lean.

   The clean way to close this would be a Lean
   `atomicCrossingPattern : Atom → List CrossingSign` definition
   matching the Python table, then per-atom theorems of shape
   `chiralityFactor h (atomicCrossingPattern Atom.T) = 1 − h²`.

Neither gap blocks production use — the Python `aK_closed_form`
fix above gives the canonical values; the Lean side proves the
formulas hold for the right patterns; nothing in the production
code reads from Lean directly.

## Files modified by this branch

- [`computations/audits/term5_aK_audit.py`](https://github.com/litlfred/qou/blob/claude/chirality-pn-counting-finding2/computations/audits/term5_aK_audit.py)
  — `aK_closed_form` uses canonical `chirality_signs_for_isotope_inferred`
- [`computations/audits/term5-aK-audit.witness.json`](https://github.com/litlfred/qou/blob/claude/chirality-pn-counting-finding2/computations/audits/term5-aK-audit.witness.json)
  — T and ³He `closed_form_aK` updated from `1.209` to `0.956`
- [`docs/audits/2026-05-18-chirality-pn-counting-finding2.md`](https://github.com/litlfred/qou/blob/claude/chirality-pn-counting-finding2/docs/audits/2026-05-18-chirality-pn-counting-finding2.md)
  (this file)

Also cherry-picked from open [PR #697](https://github.com/litlfred/qou/pull/697):

- V4 retirement in `term5_aK_audit.py` (commit `b4037324`,
  cherry-pick of `71234ce1`) — same file as the Finding 2 fix; clean
  diff stacking.

## Related blocks / audits

- [`prop:chirality-dual-space-derivation`](../../content/quantum-observable-universe/braids-and-knots/chirality-dual-space-derivation.md)
  + [`.lean`](../../content/quantum-observable-universe/braids-and-knots/chirality-dual-space-derivation.lean)
- `paper_six_term_isotope_sweep.chirality_signs_for_isotope_inferred`
- Parent audit:
  [`2026-05-18-item-b-chirality-v234-audit.md`](2026-05-18-item-b-chirality-v234-audit.md)
  Finding 2
- Upstream T5 attribution:
  [`2026-05-18-m-p-item-b-t5-categorical-attribution.md §7c`](2026-05-18-m-p-item-b-t5-categorical-attribution.md)
