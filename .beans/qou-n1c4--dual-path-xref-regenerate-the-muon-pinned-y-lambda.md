---
# qou-n1c4
title: 'dual-path xref: the chi family straddles the ideal/experimental q0 layers (owner decision needed)'
status: completed
type: task
created_at: 2026-08-08T16:59:17Z
updated_at: 2026-08-08T18:05:00Z
---

## RESOLVED 2026-08-08 — owner ruled: all new compute to the proton pin

Owner decision: *"all new compute to the proton pin ... migrate what needed"* —
option 1, with option 3 as its mechanism. The ideal layer keeps its own cache
(AGENTS.md is explicit the directive does not redefine CAL-2); the experimental
layer got the counterpart it was missing.

Acceptance test passes — every atom, every leg on one pin:

    proton    3.450e-17   neutron    6.783e-17   deuteron  1.024e-16
    tritium   1.702e-16   helium-3   1.369e-16   helium-4  2.047e-16

all AGREES, from 8.1e-08 … 3.3e-07 before. `chi_convention_from_values_audit`
also now reads AGREES for deuteron/tritium/helium-3 (was MISLABELLED) with a
0.00e+00 weighted residual.

**Follow-up, not resolved here:** the muon layer used to agree at 9.111e-20 and
proton now sits at ~1e-16 — about four orders coarser, with a floor that looks
like an f64 leak. `_avg_color_delta` is documented to cap at ~5e-16 because it
reads the float64 `q_parameter.Q` rather than the 50-dps string, and AGENTS.md
says deep-1ppQ callers should use `flavor_split_leading(local_q0_50dps)`. The
A=1 atoms sit at ~1e-17 with no colour crossing at all, so that is probably not
the whole story. Worth its own bean.

---

**The original title and premise of this bean were WRONG and are corrected
here.** It was opened as "regenerate the muon-pinned y_lambda + markov-peel
upstreams onto the proton anchor", on the theory that those witnesses were
stale against producers that had already moved to the proton pin. Running them
disproved it. Nothing needs regenerating; a layer boundary needs a ruling.

## What is actually true

`computations/chi_dual_path_xref_audit.py` cross-checks each χ cache (Σ_λ y_λ χ_λ)
against the markov-peel scalar:

    proton     2.221e-50  ANCHOR_SPLIT    neutron    1.237e-51  AGREES
    tritium    9.111e-20  AGREES          helium-3   9.111e-20  AGREES
    deuteron   1.704e-07  ANCHOR_SPLIT    helium-4   3.261e-07  ANCHOR_SPLIT

Same pin agrees to ~1e-19; cross-pin lands at ~1e-7. ⁴He is the controlled
experiment — the identical 77-partition table scored 9.111e-20 before its
proton rebuild (4fb4ac54) and 3.261e-07 after.

This is **the defect AGENTS.md §"q₀ anchor convention" (STRICT) already names**,
rediscovered independently:

> Never straddle the two layers inside one quantity. … the μ₃ Fréchet probe
> took `y_λ` from the muon-built cache while evaluating `χ_λ` at the proton
> `q₀` — an 11.54 ppb layer separation … ~1e-7 relative on the result.

11.54 ppb is the μ–p substrate tension itself, and ~1e-7 is what this audit
measures. Diagnosis settled.

## Why "regenerate it" is the wrong instinct

`q0_anchor_manifest.json` classifies producers, and the muon legs are muon **by
design**:

    q_pinning_50_digit           ideal_muon (257 entries)
    atomic_tr_m_mpfr_50dps       ideal_muon
    markov_peel_atomic_witness   not listed  (inherits muon via the bridge)
    regenerate_y_lambda_mpfr     not listed  (so defaults to proton)

Measured: a wave over `q_pinning_50_digit -> atomic_tr_m_mpfr_50dps ->
markov_peel_atomic_witness` produced NOCHANGE + VALUES + VALUES, kept nothing.
They already emit what their class says they should.

`q_parameter` is **anchor-adaptive** — `q_at` returns proton from a plain shell
and muon when the running producer's stem is in `ideal_muon` (or
`QOU_Q0_ANCHOR=ideal`). The same call answering two ways is what made the
"stale" reading look plausible.

## An attempted fix, tried and reverted

b302d948 re-anchored `y-lambda-mpfr-witness.json` to proton (clean
ANCHOR_MIGRATION: 295 fields, 12 flips, worst move 8.461e-07). **Reverted.**
That cache is the ideal-layer artifact and 257 ideal_muon producers read it, so
re-pinning it straddles the ideal layer in the other direction — measured
immediately, `atomic_tr_m_mpfr_50dps` (ideal_muon) then moved 49 fields.

AGENTS.md gives the intended route instead: experimental-anchor compute should
call the live closed form `schur_principal_mpmath.y_lambda_at_q0_mpmath(n, q)`
rather than read the muon-built cache. It also flags the trap —
`wedderburn_jones_markov.y_lambda_at(n, q)` serves the cache whenever
`|q − q_parameter.Q| < 1e-12`, which a caller passing `q_parameter.Q` satisfies
trivially, with no signal that a boundary was crossed.

## The decision (owner-gated — do not resolve unilaterally)

The χ family is split: deuteron/⁴He/proton on the experimental pin,
tritium/helium-3/neutron on the ideal one. One of:

1. **χ stays experimental** — then its y_λ leg must come from the live closed
   form, not the cache, and the peel cross-check needs an experimental-layer
   counterpart. The cache stays muon for the ideal layer.
2. **χ returns to ideal** — re-anchor deuteron/⁴He/proton back to muon; the
   existing cross-check works unchanged.
3. **Two cached y_λ witnesses**, one per layer, with accessors that refuse to
   serve across the boundary.

The 2026-08-07 owner directive defaults *new compute* to proton, which points
at (1), but it explicitly does not redefine the ideal CAL-2 layer, and the
muon/proton split is owner-gated (AGENTS.md; bean `tnjb`). Not mine to pick.

## Acceptance test either way

`chi_dual_path_xref_audit.py` — every atom should read AGREES at ~1e-19. It
orders ANCHOR_SPLIT ahead of the numeric verdict deliberately: a cross-pin
comparison landing under the bound is not a passing check.

## Do not widen the collateral bound for the peel

`markov_peel_atomic_witness` is rejected on
`data.results[atom=deuteron].abs_diff_vs_bridge` moving 6.73e-04. That field is
a **residual** — true value near zero — and `ANCHOR_COLLATERAL_MAX` is
relative, so even a correct re-anchor collapsing it toward zero is a ~100%
relative move and reads as VALUES. Review that diff by hand if the moment
comes; a bound relaxed to admit one known-good diff stops constraining every
unknown one.

## Two open observations — not settled

- Both A=1 atoms agree to ~1e-50 *despite* being cross-pinned, so the
  single-nucleon comparison is not testing the anchor at all. Cancellation at
  n=3, or the peel row for A=1 sharing inputs (which would make it circular)?
  Unestablished.
- The same-pin floor moves with n: ~1e-50 at n=3, 9.111e-20 at both n=9 and
  n=12. Tritium and helium-3 hitting the *identical* 9.111e-20 points at a
  shared input (likely the y_λ table's precision). Nothing above n=12 measured.

## Related correction, already landed

`_b0vf_complete_he4_witness.py` GATE B claimed a "~4.8e-8 intrinsic
two-implementation gap". Not intrinsic — the deuteron's own cross-pin gap. Its
tolerance is `10·B_D` with B_D measured off that same deuteron, so the bound
inflated to 1.7e-06 and now admits ⁴He's 3.261e-07: re-run today the gate
PASSES. It did not go red, it stopped discriminating. Corrected in place.
