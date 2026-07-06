# Placeholder-bean re-sweep — honest actionable counts (2026-06-23)

**Session / PR:** `claude/idle-backlog-drain-2026-06-23` (#2637)
**Tool:** `scripts/count-actionable-placeholders.ts` (strips comments/strings,
excludes `.qa.json`/`.witness.json` sidecar prose, cited `sorry`s, and §3b
conjecture-class `sorry`s).

## Finding

The 2026-06-22 "Resolve N placeholders/TODOs" bean sweep used a **naive marker
grep**; its counts are inflated **~10–30×** for the Lean beans. Honest
repo-wide actionable total: **47 in the QOU paper + 4 UGB + 22 schema = 73**,
vs the *many hundreds* the sweep beans claim in aggregate. Most "placeholders"
are intentional `-- TODO upstream:` markers, cited `sorry`s, sidecar prose, or
genuine compile breakages — **not** mechanical drains.

## Per-bean honest counts

| Bean | Area | Claimed | Honest actionable | Nature |
|---|---|--:|--:|---|
| `8ehe` | lean/MathlibExt (dir) | 5 | 0 (**done**) | the 1 real item was a compile breakage — fixed in #2637 |
| `ixx4` | lean/MathlibExt.lean | 6 | ~0 drainable | all six are intentional `-- TODO upstream:` Mathlib-port markers |
| `1osq` | lean/Substrate | 5 | 1 | `ProtonMassSubstrateIdentity` (1 sorry) |
| `ekb8` | lean/Interactions | 17 | 1 | `QIntegerMassFormula` (1 sorry) |
| `b3pe` | lean/Archimedean | 87 | 4 | SnapPyAxioms 2, EmCouplingBringZeroMode 1, BorromeanVolumeCatalan 1 |
| `95jh` | lean/BraidKnot | 213 | 7 | JucysMurphy 2, Helium3 2, Tritium 1, QBetaPerBlockChi 1, Deuteron 1 |
| `zslh` | mass-theory | 103 | 8 | q-beta-radius gate 5, frobenius-self-duality 2, jucys-murphy 1 |
| `mlt7` | mass-endomorphism | 15 | 2 | qbeta-per-block 1, explicit-central-idempotent 1 |
| `xj99` | quantum-observable-universes | 7 | 1 | `q-resolvent` (1 sorry) |
| `ldup` | unital-groebner-bases | 29 | 4 | 2 files, all TODO/FIXME |
| `doth` | schema | 25 | 22 | **≈accurate** — 22 real TODO/FIXME in one schema file |

(`i6p9` "qou/lean" overlaps the per-module beans above; the only non-overlap
hot-spots in the lean tree are `HyperellipticQuintic/zeta5_residue_monodromy`
(7 sorry — deep math) and `lean/AUDIT-REPORT.md` (3 — a generated report, not
source).)

## Reading

- **Do not** drain on the claimed counts — they are noise. Use the honest
  column (or re-run the counter with `--list` on the bean's path).
- `doth` (schema, 22) is the one genuinely large, accurate backlog item.
- `ixx4`'s "TODO upstream" markers are *intentional* (they record lemmas that
  should migrate to Mathlib) — not cosmetic cruft; leave them unless actually
  upstreaming.
- The Lean beans' real items are mostly single `sorry`s needing a proof or a
  `-- Ref:` citation, plus the occasional genuine breakage (like `8ehe`).
