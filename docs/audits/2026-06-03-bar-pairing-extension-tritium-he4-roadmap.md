# Bar-pairing extension to T / ³He / ⁴He — roadmap from PR #1748's branch

**Date:** 2026-06-03
**Branch:** `claude/hecke-mpfr-intra-partition-rayon-2026-06-03` (PR #1748)
**Consumer:** PR #1742 (`derive_binding_bar_pairing.py`)

## Goal

Extend PR #1742's bar-pairing binding observable from D (only) to the
full light-isotope series {D, T, ³He, ⁴He} using the patched
`pyhecke-native` Rust kernel from PR #1748.

PR #1742's audit
([`docs/audits/2026-06-03-bar-pairing-does-not-improve-binding.md`](2026-06-03-bar-pairing-does-not-improve-binding.md))
established the deuteron finding:

> The per-block bar-LENGTH does NOT improve the binding — it
> underbinds badly: D: B_arch = 2.304 MeV (+3.6 %) vs B_bar =
> 0.660 MeV (−70.3 %) … T (n=9, behind `QOU_BAR_INCLUDE_T=1`) did
> not finish in the compute budget … A Rust per-partition χ kernel
> would make T/³He/⁴He cheap.

PR #1748 ships exactly that kernel. This roadmap commissions
the cross-isotope extension.

## q-usage discipline (per CLAUDE.md §7c, §q-usage)

The bar-pairing `χ(q_0) · χ(q_0^{-1})` evaluates the Wedderburn
character at TWO points:

| q-value           | type           | role                            |
|-------------------|----------------|---------------------------------|
| q_0 ≈ 1.110       | real, > 1       | substrate anchor (archimedean)  |
| q_0^{-1} ≈ 0.901  | real, ∈ (0, 1)  | mirror image (also archimedean!) |

Both are **real-positive archimedean evaluations** (Im = 0 at
both). The bar-pairing is a **two-archimedean-point construction**
— the fibre-level Hecke / KL involution `q ↦ q^{-1}` restricted to
ℝ — NOT a unit-circle / root-of-unity construction. The
`lusztig_q_0_imaginary_part_zero` assertion (in
`four_unwired_theorems_regression.py`) applies at each anchor
independently.

This satisfies the discipline:

- `def:reeb-derivation` evaluates at q_0 (archimedean) — OK
- the bar evaluates `χ` at q_0^{-1} (also archimedean, *different*
  point on ℝ_{>0}) — OK
- no `|q| = 1` evaluation surfaces — the script verifies real(χ)
  upstream of any `sqrt`

## Compute layer (Rust kernel from PR #1748)

`pyhecke_native.chi_lambda_all_partitions_mpfr(n, word_signed, q_str, dps)`
evaluates χ^λ over ALL partitions of `n` at any decimal-string q,
at MPFR precision `dps` (default 50). Uses the patched
inner-rayon kernel from this branch — ⁴He chi-cache regen drops
from infeasible (sequential, > 30 min estimated) to **~10 min** wall
on a 4-core box.

| atom | n | p(n) | max dim_λ | wall @ each q-value |
|---|---|---|---|---|
| D | 6 | 11 | 16 | **0.003 s** |
| T | 9 | 30 | 216 | **0.38 s** |
| ³He | 9 | 30 | 216 | **0.37 s** |
| ⁴He | 12 | 77 | 7700 | **~10 min** (4-core saturated) |

Two q-evaluations per atom (q_0 + q_0^{-1}) × two braid words
(free + atomic) = **4 native calls per atom**.

## Implementation (this branch)

Three scripts on PR #1748's branch:

1. [`chi_at_q_inv_via_native_mpfr.py`](../../computations/chi_at_q_inv_via_native_mpfr.py)
   — driver that runs the Rust kernel at q_0^{-1} and persists to
   `chi-{atom}-h{n}-at-qinv-50dps.witness.json` (parallel naming
   to the existing `at-q0` witnesses).
   - q-usage: decodes the q_0-encoded word using h(q_0) but
     evaluates at q_0^{-1} via the Rust kernel's internal h
     substitution.
   - **Status:** D + T + ³He generated; ⁴He in flight (~10 min).

2. [`bar_pairing_binding_observable.py`](../../computations/bar_pairing_binding_observable.py)
   — consumer that computes both `B_arch` and `B_bar` per atom
   using:
   - Rust kernel χ_λ at q_0 and q_0^{-1} (free + atomic)
   - `y_lambda_wenzl_bridge_numeric(λ, q)` for the bar-symmetrized
     weight `(y(q_0) + y(q_0^{-1})) / 2`
   - The SAME formulas as #1742:
     - `B_arch = E_0 · Σ_λ y_λ (|χ^λ_free| − |χ^λ_atom|)` at q_0
     - `B_bar  = E_0 · Σ_λ y_λ_sym (‖χ^λ_free‖_bar − ‖χ^λ_atom‖_bar)`
     - `E_0 = m_e / (q_0(q_0 − 1))` (#1742 calibration; CAL-1)
   - **D sanity check (bit-identical to #1742):**
     `B_arch = 2.3043, B_bar = 0.6597`
     vs PR #1742 `B_arch = 2.304, B_bar = 0.660` ✓

3. Witness:
   `bar-pairing-binding-observable-extension.witness.json` —
   records the full per-atom table.

## Preliminary results — D, T, ³He (instant via Rust kernel)

| atom | B_arch (MeV) | B_bar (MeV) | AME (MeV) | err_arch | err_bar | growth_free / atom |
|---|---|---|---|---|---|---|
| D   | 2.3043 | 0.6597 | 2.2246  | **+3.6 %**   | **−70.3 %** | 4 / 5 |
| T   | 3.2525 | 0.8827 | 8.4818  | **−61.7 %**  | **−89.6 %** | 16 / 16 |
| ³He | 3.4667 | 0.8991 | 7.7180  | **−55.1 %**  | **−88.4 %** | 16 / 12 |
| ⁴He | _pending_ | _pending_ | 28.296 | _pending_ | _pending_ | _pending_ |

### Honest observations

1. **#1742's bar-pairing finding extends.** Bar consistently
   underbinds 70-90 % across D / T / ³He. The +1742 conclusion
   ("archimedean observation must stay `|χ(q_0)|`") is reinforced.

2. **Archimedean per-block ALSO fails at A ≥ 3.** B_arch err is
   +3.6 % at D but jumps to −55 to −62 % at T / ³He. This is NOT
   a bar-vs-arch issue — both realizations fail at the same
   absolute scale for T / ³He.

3. **Interpretation (hypothesis, not proof):** the
   `Σ_λ y_λ (|χ_free| − |χ_atom|)` formula at A ≥ 3 is missing
   the **per-isotope binding contribution** — the magic-A residual
   (cf. PR #1731 magic-A residual investigation, PR #1733's α_r
   refutations). The Borromean tower probably needs the
   operator-valued LR branching combiner gated on PR #1443 (per
   the canonical-derivation-cheat-sheet § "Δ_λ gate") to recover
   T / ³He binding. The bar-vs-arch distinction is orthogonal to
   the missing per-isotope correction.

4. **Growth channel tally** rises with A: D = 4/5; T = 16/16;
   ³He = 16/12. The "growth" channels (where
   χ^λ(q_0) · χ^λ(q_0^{-1}) < 0, imaginary bar-length) are the
   q-Reeb arccosh / hyperbolic regime channels per
   `binding_reeb_phase_decomposition.py`. At T / ³He the bar-length
   contribution is genuinely imaginary for ALL channels — confirms
   #1742's "growth channels are the obstruction" framing.

## ⁴He plan (in flight)

⁴He @ q_0^{-1} is currently running in background (PID 10462 at
383 % CPU, 4-core saturated) — expected wall ~10 min via the PR
#1748 kernel.

When it completes:
1. Add the ⁴He row to the table (via the same wrapper script)
2. Verify the trend extends to A = 4
3. Comment on PR #1742 with the full table + observations

## Future extensions (out of scope this roadmap)

| atom | n=3A | max dim_λ | feasibility w/ PR #1748 |
|---|---|---|---|
| ⁵He   | 15 | ~30 000 (est.) | ~hours, marginal |
| ⁶Li   | 18 | ~250 000 (est.) | infeasible at 50 dps |
| ⁸Be   | 24 | ~9 M (est.) | infeasible |

The chi-cache wall scales as `O(p(n) × max(dim_λ)² × |word|)` at
fixed precision. At n=15 (⁵He) the dominant partition has
dim_λ ≈ 30 000 ≈ 4 × dim_⁴He — a 16× wall increase (~2.5-3 hours
on 4 cores). At n=18 (⁶Li) we hit 60-80× ⁴He cost — many hours,
not worth without further kernel speedups.

The "5th nuclide" requested by the user, if it means ⁵He or ⁶Li,
would need either:
- A precision drop to 30 dps (2× speedup, conflicts L1 1-ppQ)
- An algorithmic change (per-partition diagonalization of σ_g
  before matmul; out of scope this PR)
- The operator-valued combiner from PR #1443 (resolves the
  per-isotope binding formula upstream — the right fix)

## Coordination

- **Origin kernel:** PR #1748 (this branch)
- **Consumer audit:** PR #1742 (`derive_binding_bar_pairing.py`)
- **Δ_λ-gate context:** PR #1731 (magic-A residual), PR #1733
  (α_r refutations), the cheat-sheet § "Δ_λ gate"
- **Upstream fix for T/³He binding miss:** PR #1443 (operator-
  valued LR branching combiner) — would resolve the per-isotope
  formula; until then, both B_arch and B_bar underbind at A ≥ 3

This roadmap and the two driver scripts ride on PR #1748's branch
since they exercise PR #1748's kernel; the bar-pairing extension
itself is informational input for PR #1742 (a comment + table,
not a code change there).
