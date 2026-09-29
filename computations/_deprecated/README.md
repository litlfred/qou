# Deprecated witnesses and producing scripts

> **Note (2026-06-01):** `hecke_core_legacy.py` was moved out of this
> directory because 9 live importers still depend on its symbols
> (5 in `computations/` + 4 in `tools/pyhecke/python/
> pyhecke/`). It now sits at `../hecke_core_legacy.py` with a
> `DEPRECATION-CANDIDATE` banner, matching the convention used by the
> 23 other still-live deprecated scripts mentioned below.

This directory holds `*.witness.json` files that are **dead exploratory
probes** from earlier research passes:

- no content block consumes them (`computation.witness` / `:val[…]`
  registry / `witness:` array)
- no audit report under `docs/audits/*.md` cites them
- the witness body itself contains no assertions
  (`falsifiability == "no-assertions"`)

It also holds the **producing `.py` scripts** for those witnesses, when
the script is not imported by any live (non-`_deprecated/`) code.  In a
follow-on pass, 262 of the 285 candidate scripts were moved here
alongside their witnesses; the remaining 23 candidate scripts are
**kept in place** under `computations/` with a
`# DEPRECATION-CANDIDATE: ...` header comment, because they are still
imported by live code and moving them would break the importer.  Those
23 should be revisited when the live importer is itself retired or
rewired off the deprecated dependency.

A subsequent **"unwrap chains"** pass (this PR) moved the 30 remaining
orphan witnesses from the live area, plus their producer scripts, plus
the transitive closure of producer scripts that became unimported as a
result.  This brought the orphan-witness count to **0** and the live
script count from 522 down to ~225.  Restoration safety net: any wired
or audit-only witness whose `scriptFile` claim was about to be moved
was detected and the producer (and its transitive imports) were kept
in the live area.  Canonical scripts named in
[`../README.md`](../README.md) (`gb_residue_tower.py`,
`habiro_residue_symbolic.py`, `frobenius_partition_sum.py`,
`y_lambda_symbolic_validate.py`, `atom_mass_partition.py`) were also
explicitly preserved.

Reviving an exploration only requires running the producer to re-emit
the witness next to its script.

## Audit-wiring behavior

`scripts/audit-wiring.ts` scans `computations/*.witness.json`
(glob without `**`), so witnesses in this `_deprecated/` subdirectory
are excluded from every bucket (wired / audit-only / orphan).  This is
intentional — the directory is the storage location for "intentionally
not part of the live wiring graph".

## Reviving a witness

To bring a deprecated witness back into the audit:

1. `git mv computations/_deprecated/<name>.witness.json
   computations/<name>.witness.json`
2. Either:
   - add `"auditOnly": "docs/audits/<report>.md"` and `WitnessBuilder.set_audit_only(...)` in the producer, or
   - point a content block's `computation.witness` (or a `folio/values/registry.ts` `witnessFile:`) at it.

Bulk deletion of this directory is owner-only.

## 2026-05-28 pass — orphan re-sweep

Added `computations/cleanup_legacy_witnesses.py` which
codifies the same four heuristics from the original sweep plus two
guards added after the first dry-run produced false positives:

1. No top-level `contentBlock` self-claim on the witness JSON.
2. Not marked `auditOnly`.
3. Not imported by any live (non-`_deprecated/`) python file.
4. Not cited by name in any markdown under `_audits/` or `docs/audits/`.
5. Not referenced by **full filename** (with extension) from any CI
   workflow, shell script, content-pipeline TS file, or other live
   python file under `computations/`.
6. Script name does not end in `_audit`, `_scan`, `_compliance`,
   `_dashboard`, or `_validator` (I14 infra convention — these are
   always live regardless of contentBlock).

This pass moved **9 orphan scripts** + their `*.witness.json` sidecars
into `_deprecated/`. Re-run the helper any time the orphan list
appears to grow:

    python3 computations/cleanup_legacy_witnesses.py            # dry run
    python3 computations/cleanup_legacy_witnesses.py --apply --git


## Orphan witnesses kept in place (2026-08-08)

`witness_provenance_audit.py` names witnesses whose `scriptFile` provably
cannot produce them. Four were triaged; only one met the criteria at the top of
this file, and the reasons the other three did not are worth recording, because
"orphan" and "movable" turn out to be different questions.

| witness | moved? | why |
|---|---|---|
| `kite_tail_reconciliation.witness.json` | **yes** | rename residue — the producer writes the hyphenated `kite-tail-reconciliation`; 0 assertions, no `docs/audits/*.md` citation, no live reader |
| `psl27-irrep-verification.witness.json` | no | carries **4 assertions**; moving it would bury four falsifiable claims |
| `sigma-all-evaluator.witness.json` | no | cited by `docs/audits/2026-05-03-frob-filter-evaluator-wired.md` |
| `chi-helium-4-h12-numeric.witness.json` | no | **three live readers** — `delta_lambda_empirical_tabulation.py`, `y_lambda_at_q0_cache.py`, and `delta_lambda_2row_stratum_analysis.py:177` (a real `read_text()`) |

The last one is the serious case and is mis-filed as an orphan: it is a **live
input with no producer**. Nothing in the corpus can regenerate it, yet three
producers depend on it. Its live counterpart `chi-helium-4-h12.witness.json`
*does* have a producer (`per_irrep_pole_atom.py`, 8/8 payload-key match), so
the resolution is to repoint those three readers and then retire the `-numeric`
variant — a content decision, not a file move.

This mirrors the "kept in place with a `DEPRECATION-CANDIDATE` header"
convention already used above for the 23 scripts that live importers still
need. Witnesses have no comment syntax, so the marker lives here instead.

## `chi-{proton,neutron}-h3-at-q0-50dps-matrix-m.witness.json` (2026-08-16)

Deprecated rather than migrated, per the owner ruling that historical
convention-C material leaves the live corpus and is referenced only by audits.
All four conditions hold, checked rather than assumed:

1. **Producerless by design.** `chi_at_q0_via_matrix_m_mpfr.py` REFUSES to build
   them — `"A=1 single nucleon, use hoefsmit producer"`, exit 1. The matrix-M
   path covers A ≥ 2 only, so nothing in the tree can regenerate these.
2. **Unconsumed.** No `.py`, `.ts` or `.md` reads either file.
3. **Superseded.** The live siblings `chi-{proton,neutron}-h3-at-q0-50dps.witness.json`
   are convention D (`y = 0.50540422, 0.24729788, 0`), owned by the hoefsmit
   producer.
4. **Stale convention C.** They still carry `y = 0.41539579, 0.28092963,
   0.02274494` — the n=3 C fingerprints.

They were the last two convention-C files in the whole `-matrix-m` family; the
A ≥ 2 members regenerate to D from their own producer.
