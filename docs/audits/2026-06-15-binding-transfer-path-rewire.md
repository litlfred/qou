# Binding tr_M rewired onto the fine-Bratteli transfer path (2026-06-15)

**Status:** compute rewire — DONE (wiring change, not new research).
Branch `claude/epic-shannon-eo7vh0`, PR #2314.

## Summary

The atom-binding Markov trace `tr_M(β_atom) = Σ_{λ⊢3A} y_λ χ^λ(β_atom)`
is now computed by the **fine-Bratteli transfer matrix**
([`chi_monotone_transfer.chi_all_lambda`](../../folio-assistant/computations/chi_monotone_transfer.py)
via
[`tr_m_atom_via_transfer.tr_m_atom_zn`](../../folio-assistant/computations/tr_m_atom_via_transfer.py))
in the two production binding consumers:

| consumer | before | after |
|----------|--------|-------|
| [`binding_canonical`](../../folio-assistant/computations/binding_canonical.py) | symbolic `tr_M_element` (d_λ wall at A≥3) | transfer (default `use_transfer=True`) |
| [`canonical_tr_m_via_branching`](../../folio-assistant/computations/canonical_tr_m_via_branching.py) A≥3 | `pyhecke_native.chi_lambda_all_partitions_mpfr` (Rust wheel) | transfer (pure-Python mpmath) |

`atom_level_wedderburn_tower.py` (brute-force, materialises the full
`d_λ × d_λ` Hoefsmit rep per partition) is marked **superseded** and
retained only as a `d_λ`-explicit cross-check.

## Motivation — the transfer path was built, validated, and orphaned

Before this rewire **no production binding script imported the transfer
path**. `binding_canonical` defaulted to the symbolic `tr_M_element`
recursion (the d_λ wall — markov_peel territory, ~17 min for ⁶Li);
`canonical_tr_m_via_branching` A≥3 delegated to `pyhecke_native` (a hard
Rust-wheel dependency that also forms χ per-partition). The transfer
engine — lossless over all `p(3A)` partitions, d_λ-free, pure-Python —
sat unused.

## Precision compliance (no truncation)

The transfer path is **lossless**: it sums over **all** `p(3A)`
partitions, not the few-row active set. This honours the owner ruling in
[`2026-06-10-binding-active-set-compute-optimization.md`](2026-06-10-binding-active-set-compute-optimization.md):
the active-set truncation is a ~10⁻³ error and is **rejected** for
1-ppQ. The speedup is the transfer *sweep* (fine-Bratteli edges, not the
d_λ rep), **not** dropping partitions — exactly the "lossless scaling
win" that audit endorsed as the admissible optimization (its step 2).

## Validation (this branch, 50 dps)

| check | result |
|-------|--------|
| transfer ≡ `char_fast` (full Hoefsmit), color-weighted, n=6 | **4.7e-15** ✓ |
| transfer ≡ legacy symbolic `binding_canonical` (D, T) | ~1e-8 (legacy is float64 via `complex(sp.N)` + lossy `nsimplify` of the color-weighted δ; transfer is full 50-dps) |
| `canonical_tr_m_via_branching` A≥3 vs transfer ref (T/³He/⁴He/⁶Li) | exact |
| ⁶Li wall | 0.16 s (λ=385) — was ~17 min (markov_peel) |
| ⁷Li wall | 0.58 s (λ=792) |

`tr_M_atom(D) = 0.388357276…` matches the canonical-branching A=2 value
(the transfer module's own assertion) and the legacy path to 1e-8.

## Side finding — q0-repin staleness in cached oracles

The `chi_monotone_transfer` self-test's *cached-oracle* cross-check
(`chi-{deuteron,tritium,helium-*}-*-50dps.witness.json`) fails at ~1e-7.
Diagnosed as **q0-repin staleness**: the oracles were computed at
q0 = `1.10997859`**`27`**…, the current proton-anchored substrate is
`1.10997859`**`55`**… (Δq ≈ 1.3e-8 → ~1e-7 in χ). This is **not** a
transfer bug — the fresh full-Hoefsmit (`char_fast`) cross-check passes
at 4.7e-15. The committed `tr-m-atom-via-transfer.witness.json` is itself
at the old q0 (its D Δtr_M = 0.595168822… vs the current 0.595168923…).

Follow-ups (not blockers for the rewire):
- Refresh the stale q0-repin oracle witnesses (needs a native-enabled
  env), or retarget the self-test's gold check to `char_fast` (already
  the definitive check) and downgrade the stale-oracle compare to a
  warning.
- Regenerate `tr-m-atom-via-transfer.witness.json` in CI: this sandbox
  lacks `pyhecke_native`, so the script's `free_chi_matches_parabolic_lr`
  cross-check (`chi_free_via_lr`) degrades (env artifact). The
  `binding-canonical.witness.json` was regen'd here (native-free, full
  50-dps).

## Payoff

Un-gates the A≥5 reach of the per-isotope binding sweep (step 9b): the
χ^λ trace is no longer the bottleneck, so the Δ_λ tower flips from
"gated" to "one wiring change away" — making a q-Lommel / Δ_λ-closure
test decisive against ⁶Li/⁷Li data. Δ_λ itself remains the open Track-A
blocker; this rewire changes only the **trace compute**, not the Δ_λ
gate.
