#!/usr/bin/env python3
"""The automated C->D migration is 0-for-2 on the decay channel (bean qou-cds1).

The owner ruling is unambiguous: convention D is canonical, convention C is
excised.  This probe does not question that.  It measures HOW the excision must
be carried out for the two decay-channel sites that
`scripts/convention-c-producer-migrate.py` was willing to rewrite automatically
-- and finds that rewriting BOTH is wrong, in two different ways.

Run BEFORE trusting `--apply` on any qbeta file.  The guards it justifies (G1,
G2) are now in the migrate script; this probe is the evidence for them and the
regression test that they still fire.

## Site 1 -- FAILS LOUDLY (the safe kind)

`qbeta_zcd_classical_coincidence_probe.py:213` binds `markovZ_prime` to z_C.
The name is not C-shaped, so the migrate script's per-site `DELIBERATE` name
check did not protect it.  But the binding exists ONLY to be asserted equal to
a C reference:

    check("7. the ladder's markovZ' equals z_C exactly (so alpha is C-frame)",
          sp.simplify(markovZ_prime - z_C(q)) == 0, ...)

Measured: rewriting it takes that probe from `8/8, exit 0` to
`FAILED 1/8, exit 1`, printing the self-refuting line

    1/(sqrt q + 1/sqrt q) = q**3/(q**2 + 1) = z_C

A migration that makes a probe assert a falsehood is not a migration.  This is
the class AGENTS.md calls "deliberate comparison -> LEAVE IT": sweeping it does
not clean the corpus, it destroys the instrument that measures the excision.

## Site 2 -- PASSES SILENTLY (the dangerous kind)

`qbeta_h_frame_rungs_probe.py:73` binds the z that feeds the ladder phase
`alpha = (z - 1) * h / 2`.  Substituting z_D there is exactly the move the
corpus PROVES is not a migration -- `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`
(sorry-free) makes "keep the C-frame ladder" and "the two-row forcing applies"
mutually exclusive, so the ladder must be RE-DERIVED, not re-evaluated.

Measured: after the rewrite the probe still exits 0 with all 3 assertions
passing, and silently moves 14 mathematical fields of its COMMITTED witness:

    h^3 rung   -sqrt(3)/64            ->  1/16 - sqrt(3)/64      (SIGN CHANGE)
               -0.02706329386826...   ->  +0.03543670613173...
    h^6 rung   -6781/2949120          ->  -25381/2949120 - 25*sqrt(3)/12288

The h^6 change is not merely numeric: the committed value is purely RATIONAL
and the rewritten one is irrational.  The probe's own headline finding is that
"h^3 = -sqrt(3)/64 is nonzero and purely irrational" -- a statement about which
rungs are rational -- so the rewrite contradicts the result the file exists to
report, while reporting success.

## What this probe asserts

  S1  G2 fires on the ladder-phase site (the `(z-1)*h/2` detector works).
  S2  G1 fires on the deliberate-comparison site.
  S3  After both guards, the auto-migratable set for the decay channel is EMPTY
      -- i.e. no qbeta site may be migrated by machine.
  S4  The two guards are independent: neither alone catches both sites.

NO FLOAT64: this probe does static AST analysis and string comparison only; it
computes no mathematical quantity.  The numeric figures quoted above were
measured by running the two probes before and after `--apply` and diffing the
witness, and are recorded here as documentation, not recomputed.

Scope-(a): this says the AUTOMATED path is unsafe for these two sites and why.
It does NOT say convention C should be kept anywhere -- the ruling stands, and
the remaining ~30 actionable sites outside the decay channel are untouched by
this finding and still need their own per-site triage.
"""

from __future__ import annotations

import ast
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts"))

LADDER_SITE = REPO / "computations/qbeta/qbeta_h_frame_rungs_probe.py"
COMPARE_SITE = REPO / "computations/qbeta/qbeta_zcd_classical_coincidence_probe.py"

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"{'PASS' if ok else 'FAIL'}  {name}")
    if detail:
        print(f"        {detail}")
    if not ok:
        FAILURES.append(name)


def _load_migrate():
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "ccpm", REPO / "scripts" / "convention-c-producer-migrate.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    print(__doc__.split("\n")[0])
    print("=" * 72)
    m = _load_migrate()

    ladder_tree = ast.parse(LADDER_SITE.read_text())
    compare_tree = ast.parse(COMPARE_SITE.read_text())

    # S1 — G2 detects the ladder phase
    phase = m._ladder_phase_targets(ladder_tree)
    check(
        "S1 G2 detects the ladder-phase target (z-1)*h/2",
        "z" in phase,
        f"ladder-phase targets in {LADDER_SITE.name}: {sorted(phase)}",
    )

    # S2 — G1 detects the deliberate C reference
    has_c = m._file_has_c_reference(compare_tree)
    check(
        "S2 G1 detects the file's deliberate C reference",
        has_c,
        f"{COMPARE_SITE.name} references a C-named symbol (z_C) -> comparison file",
    )

    # S3 — nothing in the decay channel is auto-migratable any more
    leftovers = []
    for p in sorted((REPO / "computations" / "qbeta").rglob("*.py")):
        edits, _ = m.migrate_file(p, apply=False)
        for e in edits:
            leftovers.append(f"{p.relative_to(REPO)}:{e[0]} {e[1]}")
    check(
        "S3 no decay-channel site is auto-migratable after the guards",
        not leftovers,
        "auto-migratable: none" if not leftovers else f"STILL MIGRATABLE: {leftovers}",
    )

    # S4 — the guards are independent
    ladder_has_c = m._file_has_c_reference(ladder_tree)
    compare_phase = m._ladder_phase_targets(compare_tree)
    independent = (not ladder_has_c) and ("markovZ_prime" not in compare_phase)
    check(
        "S4 the two guards are independent — neither alone catches both",
        independent,
        f"G1 on the ladder file: {ladder_has_c} (needs G2); "
        f"G2 on the comparison file: {'markovZ_prime' in compare_phase} (needs G1)",
    )

    print("=" * 72)
    if FAILURES:
        print(f"{len(FAILURES)} FAILED: {', '.join(FAILURES)}")
        return 1
    print("4/4 pass — the automated C->D path is 0-for-2 on the decay channel,")
    print("and both failure modes are now refused rather than applied.")
    print()
    print("The ruling is unchanged: D is canonical, C is excised. What this")
    print("measures is that the decay channel's excision is a RE-DERIVATION")
    print("(qou-cds1), not a substitution -- and that ~30 sites OUTSIDE this")
    print("channel remain to be triaged individually.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
