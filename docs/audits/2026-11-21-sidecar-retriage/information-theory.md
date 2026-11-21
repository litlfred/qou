# Sidecar re-triage: information-theory chapter (2026-11-21)

Umbrella issue #8766. There were 11 stale items. After the writes the census shows every Lean-backed statement (10) and every proof (13) in this chapter fresh.

## Re-stamped (wording only, earlier verdict kept)

- hopf-link-symmetric-decomposition (pass): no change.
- reeb-operations-per-planck proof (warn).
- p-bandwidth-bound proof (fail).
- parallel-fibre-noninteraction proof (warn).
- phase-transition-boundary (fail).
- q-exponential-taylor proof (fail): the false growth claim for |q|<1 is still at lines 15 and 22.
- q-gaussian-solves-q-heat proof (warn).
- toffoli-lp-stability, statement and proof (fail): probe, Lean and witness names were stripped, and the convention-C numerical record is now labelled as such.

## Full reviews

**q-heat-kernel-peter-weyl proof: fail → warn, major.** The 2026-11-16 correction (symmetric integers, no ħ_q²) is right. I checked the per-cell factorisation and the classical limit by hand. Three things are still open:

1. Item 1, the spectral decomposition of a solution, is not argued.
2. The SU_q(2) Peter–Weyl wording does not match the λ ⊢ n indexing.
3. Bridge A, the Reeb holonomy identification, is unproved. The block says so itself.

**q-heat-kernel-peter-weyl statement: fail, major.** The lean.ref is still an unasserted `def … : Prop` (a `Summable`). The real eigenvalue theorem, `QOU.SchurWeyl.ContentCasimir.contentCasimir_smul_of_weight`, exists in the library but is not referenced.

## Ruling check

- No block in this chapter uses the photon form or the electron strand.
- The q-heat-kernel scope note gives the deuteron sign problem as −17.69 MeV, which matches the binding thread's current statement.
