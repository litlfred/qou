# Hecke-natural closed form for sym(Δtr_M)(q) — algebraic identity

**Date:** 2026-06-01
**PR:** TBD (claude/qbeta-bar-sym-categorical-id-2026-06-01)
**Status:** EXACT ALGEBRAIC IDENTITY (verified sympy-clean to 0).
Follow-up to PR #1615 bar-decomposition.

## TL;DR

The symmetric part `sym(Δtr_M)(q)` from PR #1615's bar-decomposition
under `t ↔ 1/t` (`t = q^(1/2)`) is algebraically equivalent to a clean
Hecke-natural product:

```
sym(Δtr_M)(q) = -h · (q-1) / (2·q^(1/2))
              = -[2]_{q^(1/2)} · h̃² / 2
              = -(q^(1/2) + q^(-1/2)) · (q^(1/2) - q^(-1/2))² / 2
```

Where:
| Symbol | Definition | Bar-symmetry under t ↔ 1/t (t = q^(1/2)) |
|---|---|---|
| `h` | `q - q⁻¹` | antisymmetric (h(1/q) = -h(q)) |
| `h̃` | `q^(1/2) - q^(-1/2)` | antisymmetric (h̃(1/t) = -h̃(t)) |
| `[2]_{q^(1/2)}` | `q^(1/2) + q^(-1/2)` | symmetric |

## Why this matters (anti-pattern guard restated)

The sym part factors as a PRODUCT of two bar-antisymmetric Hecke
quantities (h at full q, h̃ at half q). Under bar-involution
`t ↔ 1/t`, each factor flips sign, so the product is preserved —
consistent with the sym-projection definition by construction.

The form `h · h̃` is suggestive of a Lie bracket `[h, h̃]` or
wedge-product structure in the Hecke bar-derivative algebra.
**Open research direction (NOT yet derived):** identify the
categorical object whose contribution to Q_β projects onto exactly
this product structure.

## What's NOT done — explicit anti-pattern guard

This audit identifies the ALGEBRAIC FORM of sym, not a c_k closure
candidate. Per CLAUDE.md "Don't propose a seventh fit-based ansatz"
discipline:

- The numerical relation `Q_β/m_e ≈ 140 · |sym|` at q_proton would
  require a substrate constant ~140. Nearby candidates:
  - `1/h² ≈ 102` (15% off, wrong direction)
  - `[2]_q/h² ≈ 195` (39% off, opposite direction)
  - `[2]_{q^(1/2)}²/h² ≈ ?` — DO NOT compute and report; that's the trap
- **DO NOT WIRE.** Wiring any substrate-constant near 140 without
  structural justification = 8th-ansatz fit-trap.

To use this identity for Q_β requires identifying the CATEGORICAL
OBJECT (operator, characteristic class, etc.) producing the sym
projection in the chain. The cross-anchor test (q_proton vs q_muon)
plus a structural derivation are both required before any wiring.

## Verification

Run `computations/qbeta/qbeta_sym_part_hecke_natural_form.py`.

All three forms verified algebraically equal to the upstream
sym closed form `(-q³+q²+q-1)/(2q^(3/2))` from PR #1615. SymPy
diff after `q → t²` substitution: 0 for all three.

Assertion `three_hecke_natural_forms_all_match_upstream_sym`: PASSED.

## Categorical-reading research direction

The identity `sym = -h · (q-1) / (2·q^(1/2))` and the factored form
`-(q-1)²(q+1)/(2q^(3/2))` together suggest the categorical object
producing the sym projection might be:

1. **A 2-form / curvature** of the Hecke bar-involution acting on
   the (2,1) standard rep (since Δtr_M is the n vs p braid difference
   — the (2,1) block dominates per `qbeta-per-block-paper-closed-forms`)
2. **A wedge product** `h ∧ h̃` interpreted in the Hecke bar-derivative
   algebra (the two h's are at different q-resolutions; their wedge
   is naturally bar-symmetric)
3. **A boundary operator** in some Hochschild / cyclic-homology
   spectral sequence — h̃² resembles a coboundary squared, which
   vanishes for genuine cocycles but appears in cup products

Each is a research direction, not a candidate to wire. Failure-mode
signature: any of (1)–(3) must reproduce the c_3 at BOTH q_proton
AND q_muon (the fibre-vs-observable distinction) — and must derive
from substrate axioms, not match-by-fitting.

## Cross-refs

- PR #1615 — bar-decomposition structural finding (this PR's upstream)
- `docs/audits/2026-06-01-delta-tr-m-bar-decomposition-structural-finding.md`
- `computations/probes/qbeta-delta-tr-bar-decomposition-probe.witness.json`
- `computations/qbeta/qbeta-sym-part-hecke-natural-form.witness.json` (this PR)
- `todos/research-queue.json` — `research-qbeta-bar-decomposition-followup`
- CLAUDE.md §Canonical derivation chain: Im(q) fibre vs observable (PR #1616 framing)
