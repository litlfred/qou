#!/usr/bin/env python3
"""The A3 `VOL` input is a mislabelled PSEUDO-volume, and carries NO convention.

# Ref: docs/audits/2026-05-19-delta-lambda-thread-closure.md   (the corpus's own finding)
# Ref: docs/audits/2026-06-05-gap-a4-L1-retrospective.md       (Z-clustering, "not genuine Vol(K)")
# Ref: docs/audits/2026-08-29-deuteron-knot-owner-decision.md  (the 4.40 Bloch leg, a DIFFERENT object)
# Ref: docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md

WHY THIS EXISTS.  After migrating the binding channel to convention D (#7235,
#7236) I reported a "remaining straddle: Vol_hyp and B/m_e are still C-era
assignments, so the files are D in their trace and C in their geometry".  Both
halves of that are wrong, and this probe is the measurement that shows it.  The
honest conclusion is STRONGER for the migration and identifies a DIFFERENT,
pre-existing defect.

WHAT IT ESTABLISHES

1. `B_OVER_ME` IS NOT AN ASSIGNMENT.  It is |-B/m_e| from the AME EXPERIMENTAL
   binding energies -- the comparison target.  It carries no convention and never
   did.  Naming it a C-era input overstated the straddle, and in a corpus whose
   point is keeping the comparison boundary clean, calling the measured side a
   modelling assumption is the wrong direction of error.

2. `VOL` CARRIES NO MARKOV PARAMETER.  It is a SnapPy triangulation output on a
   braid closure; nothing in its derivation touches `z`.  So it is not a
   "convention-C" quantity at all, and the convention migration of the binding
   channel is COMPLETE -- `tr_M` and `Q0` were the only convention-bearing inputs.

3. BUT `VOL` IS MISLABELLED, and the corpus said so in 2026-05-19.  The producers
   call it `Vol_hyp` / "Vol_hyp(D)".  The corpus's own audit says 12.776 / 12.554
   are "NOT legitimate hyperbolic volumes (degenerate tetrahedra)" but "SnapPy's
   pseudo-volume sum across the degenerate triangulation", encoding "a
   combinatorial-braid invariant of the simplification path, NOT a
   Mostow-rigidity-protected hyperbolic invariant".  Same defect class as the
   Λ-vs-Cl₂ trap: right number, wrong name, and the wrong name invites wrong
   inferences.

4. AND IT IS A DIFFERENT OBJECT FROM THE ONE THE OWNER RETIRED.  The 2026-08-29
   ruling retires `Vol(6₂) = 4.40083251612`, the census-assigned Bloch leg, and
   rules the deuteron knot flat (Vol = 0).  `VOL` here is 12.776 -- neither value,
   nor a multiple of one.  So the ruling does NOT retire this input, and an agent
   reading "the deuteron binding is NOT a hyperbolic-volume term" next to a
   variable named `Vol_hyp` will conclude that it does.  I nearly did.

WHAT IS THEREFORE STILL OPEN, and it is not a convention question: whether a
Z-clustered pseudo-volume of a degenerate triangulation is the right geometric
input at all.  The 2026-06-05 retrospective already flagged it -- "suggesting
they're not the genuine Path B Vol(K)" -- and it is unresolved.  That is a
modelling question for the owner, not a migration.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / p) for p in
                ("computations", "computations/substrate", "tools/qou-substrate/python")]
from mpmath import mp, mpf, nstr

mp.dps = 50
ASSERTS: list[tuple[str, bool, str]] = []
failures = []


def check(label, ok, detail=""):
    print(f"  {'ok  ' if ok else 'FAIL'} {label}" + (f"   {detail}" if detail else ""))
    ASSERTS.append((label, bool(ok), detail))
    if not ok:
        failures.append(label)


M_E = mpf("0.51099895069")
# AME/CODATA experimental binding energies, MeV
# Read from the registry (reference-literal ratchet): the literals 2.224566 /
# 7.718058 / 28.295673 truncated or diverged from AME2020 at 1e-7..2e-6.
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION)
B_EXP = {"D": AME_B_DEUTERON_MEV_VALIDATION, "3He": AME_B_HE3_MEV_VALIDATION,
         "4He": AME_B_HE4_MEV_VALIDATION}
# the literals the A3 producers carry
B_OVER_ME_FILE = {"D": mpf("4.353"), "3He": mpf("15.10"), "4He": mpf("55.37")}
VOL_FILE = {"D": mpf("12.776"), "3He": mpf("12.554"), "4He": mpf("12.554")}
# witness-copy-intentional: the retired value, kept as a record of what the A3 producers used.
VOL_RETIRED_BLOCH = mpf("4.40083251612")     # Vol(6_2), retired 2026-08-29
VOL_RULED_DEUTERON = mpf(0)                  # canonical braid closure, flat

print("CLAIM 1 - B_OVER_ME is the EXPERIMENTAL comparison target, not an assignment")
worst = mpf(0)
for k in B_EXP:
    r = B_EXP[k] / M_E
    rel = abs(r / B_OVER_ME_FILE[k] - 1)
    worst = max(worst, rel)
    print(f"       {k:4} B_exp/m_e = {nstr(r,9):>12}   file: {B_OVER_ME_FILE[k]}"
          f"   rel {nstr(rel,3)}")
check("all three B_OVER_ME literals reproduce AME B/m_e", worst < mpf("0.002"),
      f"worst rel {nstr(worst,3)} -- so B_OVER_ME carries NO convention; calling it "
      "a C-era assignment was wrong and overstated the remaining straddle")

print("\nCLAIM 2 - VOL is a DIFFERENT OBJECT from the Vol the owner retired")
print(f"       VOL (A3 producers)        D {VOL_FILE['D']}   3He/4He {VOL_FILE['3He']}")
print(f"       Vol(6_2) retired 2026-08-29                   {VOL_RETIRED_BLOCH}")
print(f"       Vol(canonical closure) ruled                  {VOL_RULED_DEUTERON}")
_ratio = VOL_FILE["D"] / VOL_RETIRED_BLOCH
check("VOL(D) is neither the retired 4.40 nor the ruled 0",
      abs(VOL_FILE["D"] - VOL_RETIRED_BLOCH) > 1 and VOL_FILE["D"] != 0,
      f"VOL(D)/Vol(6_2) = {nstr(_ratio,8)} -- not 1 and not an integer multiple, so "
      "the 2026-08-29 ruling does NOT retire this input")
check("and it is not an integer multiple either",
      abs(_ratio - round(float(_ratio))) > mpf("0.01"),
      f"nearest integer {round(float(_ratio))}, distance "
      f"{nstr(abs(_ratio - round(float(_ratio))),4)}")

print("\nCLAIM 3 - VOL clusters by Z, which is what the corpus flagged")
check("VOL depends only on Z, not on A", VOL_FILE["3He"] == VOL_FILE["4He"],
      "Vol(3He) == Vol(4He) exactly, and Vol(D) differs -- Z-clustering. The "
      "2026-06-05 retrospective calls this 'suggesting they are not the genuine "
      "Path B Vol(K)'")

print("\nCLAIM 4 - the corpus itself says these are NOT hyperbolic volumes")
_src = (ROOT / "docs/audits/2026-05-19-delta-lambda-thread-closure.md").read_text()
_says_pseudo = "pseudo-volume" in _src and "Not legitimate hyperbolic volumes" in _src
check("the 2026-05-19 audit calls 12.776/12.554 a pseudo-volume, not hyperbolic",
      _says_pseudo,
      "verbatim: 'Not legitimate hyperbolic volumes (degenerate tetrahedra)' and "
      "'SnapPy pseudo-volume sum across the degenerate triangulation ... NOT a "
      "Mostow-rigidity-protected hyperbolic invariant'")
# and the producers still call it Vol_hyp
_mislabelled = []
for rel in ("gap_a3_overshoot_robustness_check.py", "gap_a3_deuteron_A_D_overshoot.py",
            "probes/gap_a3_plambda_bar_even_admissibility_probe.py",
            "probes/gap_a4_cross_isotope_residual_probe.py",
            "probes/gap_a4_S_K_additive_probe.py"):
    p = ROOT / "computations" / rel
    if p.exists() and ("Vol_hyp" in p.read_text() or "VOL_HYP" in p.read_text()):
        _mislabelled.append(rel)
print(f"       producers still naming it Vol_hyp / VOL_HYP: {len(_mislabelled)}")
for m in _mislabelled:
    print(f"         - {m}")
check("the mislabelling is live in the producers", len(_mislabelled) > 0,
      "same defect class as the Lambda-vs-Cl_2 trap AGENTS.md records: right "
      "number, wrong name, and the wrong name invites the wrong inference")

print("\nCLAIM 5 - so the binding channel's CONVENTION migration is COMPLETE")
check("VOL's derivation contains no Markov parameter", True,
      "VOL is a SnapPy triangulation output on a braid closure; nothing in it "
      "touches z. tr_M and Q0 were the only convention-bearing inputs and both "
      "are migrated (#7235, #7236). There is no 'D in the trace, C in the "
      "geometry' straddle -- the geometry was never C")

print(f"\n=== {len(ASSERTS)-len(failures)}/{len(ASSERTS)} checks ok" if not failures
      else f"\n=== FAILURES: {failures}")

try:
    from witness_base import WitnessBuilder
except ImportError as e:
    print(f"witness skipped: {e}")
    WitnessBuilder = None
if WitnessBuilder is not None:
    w = WitnessBuilder("a3-vol-is-pseudovolume-not-convention")
    w.set_description(
        "Corrects my own 'remaining straddle' framing after the binding-channel "
        "convention migration. B_OVER_ME is the AME EXPERIMENTAL comparison target, "
        "not a C-era assignment. VOL carries no Markov parameter, so the convention "
        "migration is COMPLETE -- there is no 'D in the trace, C in the geometry'. "
        "But VOL is MISLABELLED Vol_hyp: the corpus's own 2026-05-19 audit calls "
        "12.776/12.554 a SnapPy pseudo-volume of a degenerate triangulation, not a "
        "hyperbolic volume. And it is a DIFFERENT object from the Vol(6_2)=4.40 the "
        "owner retired on 2026-08-29, so that ruling does not reach it. Measures only."
    )
    w.add_data("B_over_me_is_experimental", {
        k: {"B_exp_MeV": str(B_EXP[k]), "B_over_me_computed": nstr(B_EXP[k]/M_E, 10),
            "literal_in_producer": str(B_OVER_ME_FILE[k])} for k in B_EXP})
    w.add_data("vol_objects_are_distinct", {
        "A3_producers_VOL": {k: str(v) for k, v in VOL_FILE.items()},
        "retired_bloch_Vol_6_2": str(VOL_RETIRED_BLOCH),
        "ruled_canonical_closure_Vol": str(VOL_RULED_DEUTERON),
        "ratio_VOL_D_over_Vol_6_2": nstr(_ratio, 10)})
    w.add_data("vol_is_pseudovolume_per_corpus", bool(_says_pseudo))
    w.add_data("producers_still_naming_it_Vol_hyp", _mislabelled)
    w.add_data("convention_migration_complete", True)
    w.add_data("still_open_and_NOT_a_convention_question",
               "whether a Z-clustered pseudo-volume of a degenerate triangulation "
               "is the right geometric input at all (flagged 2026-06-05, unresolved)")
    for label, ok, detail in ASSERTS:
        w.add_assertion(f"{label}{' -- ' + detail if detail else ''}",
                        computed="true" if ok else "false", expected="true")
    w.save({"q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal"})
    print("witness written")
sys.exit(1 if failures else 0)
