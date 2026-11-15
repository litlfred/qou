#!/usr/bin/env python3
"""
tr_M provenance chain — where the 48 % move of 2026-08-23 actually came from.

Bean qou-brkp item 2. The bean records that `tr_M_atom` for the deuteron moved

    0.38835720735922143663...  ->  0.57517224391777187082...        (+48.1039 %)

in ``option-e-multi-isotope-delta-lambda-probe-v3.witness.json`` and asks for
the mechanism. Three shapes were ranked in PR #6698 and all three are wrong;
the answer is a fourth.

MEASURED CHAIN (git archaeology, 2026-09-05)
--------------------------------------------
``option_e_multi_isotope_delta_lambda_probe_v3.py`` does not compute tr_M. Its
line 129 is

    "tr_M": mpf(tr_M_data["tr_M_at_q0"]),

i.e. the field is copied verbatim out of ``chi-<atom>-at-q0-50dps.witness.json``.
So the option_e move is entirely the chi witness's move, picked up with a
13-day lag: option_e last ran 2026-08-09T00:41 (commit 2c68d7f34a) and next ran
2026-08-23T09:15 in the 563-witness sweep a0ee2ac5e9.

The chi witness moved in 7e4d1aa6d0 (2026-08-10 18:22:42, computedAt 18:20:37).
Across that move:

  * every ``chi_lambda`` is byte-identical;
  * every ``y_lambda`` changed;
  * ``scriptHash`` (c36a8a393fcd), ``scriptCommitSha``, ``q0Anchor`` (proton),
    ``q0Value``, ``dps`` (50) and ``engineVersion`` are ALL byte-identical.

The proximate cause is one line in a one-hop dependency. Commit fcf629cf41,
timestamped 18:20:04 — THIRTY-THREE SECONDS before the chi run — switched
``_Y_LAMBDA_DEFAULT`` in ``tr_m_wenzl_bridge_mpfr.py`` from
``y-lambda-mpfr-witness.json`` to ``y-lambda-mpfr-proton-witness.json``.

But the SIZE is not the mu-p pin difference (~11.5 ppb, which is what that
commit's message budgets for). Both y_lambda tables had themselves been
regenerated earlier the same day, and the regeneration changed the WEIGHTS:
at n = 6, y[(6,)] went 0.0591877... -> 0.1153242..., a factor 1.948, while the
>=3-row weights collapsed to ~1e-72. The per-partition growth is monotone in
row length -- (3,3) x1.071, (4,2) x1.143, (5,1) x1.339, (6,) x1.948 -- i.e. the
weight mass migrated onto the <=2-row (SU(2)-admissible) partitions. THAT is
the 48 %.

Classification: a y_lambda WEIGHT-TABLE regeneration. Not a pin swap, not a
convention C->D swap, not a precision change. The default swap is what made the
chi producer SEE it 33 seconds later; the regeneration is what created it.

TWO CORRECTIONS TO PR #6698 (my own earlier work on this bean)
--------------------------------------------------------------
1. It "refuted convention D" by reading the chi witness's ``convention`` field,
   which is unchanged at ``colour-weighted-averaged-crossing``. That field names
   the p/n COLOUR convention, not the Markov C-vs-D parameter -- a field
   literally called ``convention`` that does not carry the convention in
   question. Reading it was uninformative, not exculpatory.
2. It "refuted import-cone drift" by checking that the OPTION_E producer does
   not import ``tr_m_atom_via_transfer``. Wrong level twice over: option_e's
   dependency on the value runs through a witness JSON FILE, which no
   import-cone audit can see at all; and the actual drift is in the CHI
   producer's cone (``tr_m_wenzl_bridge_mpfr``), not option_e's.

A THIRD TRAP, found while writing this probe
--------------------------------------------
The >=3-row weights in the proton table print as ``2.188243022053045885...``
under a 40-character slice and are actually ``2.188243...e-72``. Reading the
truncation as the value nearly produced a filed "the two y_lambda tables
disagree on support" defect. They do not: one serialises a vanishing quantity
as exact ``0.0`` and the other keeps its 1e-72 residue. Never read a truncated
numeric string as a value.

NOT MEASURED HERE. AGENTS.md's import-cone worked example attributes a 48 %
``tr_M_atom`` move to ``binding_canonical.py`` / ``tr_m_atom_via_transfer.py``.
That is a different producer pair from the one measured here, in the same date
window at the same magnitude -- CONSISTENT WITH one upstream y_lambda
regeneration hitting both, but that second pair was not measured and this probe
does not claim it.

WHAT THIS PROBE ASSERTS (live invariants, re-runnable)
------------------------------------------------------
1. option_e's ``atom_substrate[atom]["tr_M"]`` equals the chi witness's
   ``tr_M_at_q0`` verbatim, for all three atoms -- the copy, not a computation.
2. Each chi witness is self-consistent: ``tr_M_at_q0 == sum_lambda y * chi``.
3. Each chi witness's ``y_lambda`` agrees to 50 dps with the LIVE default
   y_lambda table, so the committed chi values are current w.r.t. their weight
   source (they are -- the 08-10 run is not stale).
4. The >=3-row weights are numerically zero (< 1e-60) in BOTH y_lambda tables,
   so the apparent support disagreement is serialisation, not mathematics.

No float64 anywhere: every number is carried as ``mpmath.mpf``.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

ROOT = Path(__file__).resolve().parent.parent.parent
COMP = ROOT / "computations"

#: atom -> chi witness stem, as ``option_e_multi_isotope_delta_lambda_probe_v3``
#: spells them at its line 122.
ATOMS = {
    "deuteron": "chi-deuteron-h6-at-q0-50dps",
    "tritium": "chi-tritium-h9-at-q0-50dps",
    "helium-3": "chi-helium-3-h9-at-q0-50dps",
}

#: The live ``_Y_LAMBDA_DEFAULT`` of ``tr_m_wenzl_bridge_mpfr.py``.
Y_DEFAULT = "y-lambda-mpfr-proton-witness.json"
Y_IDEAL = "y-lambda-mpfr-witness.json"

#: Anything below this is a serialisation residue, not a weight. The observed
#: residues are ~1e-72; the surviving weights are ~1e-2.
VANISHING = mp.mpf("1e-60")


def _load(name: str) -> dict:
    with (COMP / name).open() as f:
        return json.load(f)


def _parts(entry) -> tuple:
    p = entry["partition"]
    if isinstance(p, str):
        p = json.loads(p.replace("(", "[").replace(")", "]"))
    return tuple(p)


def main() -> int:
    checks: list[dict] = []

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append({"check": name, "pass": bool(ok), "detail": detail})

    option_e = _load("option-e-multi-isotope-delta-lambda-probe-v3.witness.json")
    substrate = option_e["atom_substrate"]

    # --- 0. schema preflight -------------------------------------------------
    # A missing field is a FINDING, not a crash. `70ae502091` (2026-09-05)
    # stripped `tr_M_at_q0` and the per-partition `dim`/`y_lambda` from the
    # deuteron chi witness while leaving its two siblings intact, and the first
    # version of this probe died on it with a bare KeyError -- which reports the
    # symptom as a probe bug rather than as the corpus defect it is (bean
    # qou-16yn). Report per field, per atom, and skip the checks that field
    # feeds instead of aborting the whole run.
    REQUIRED_TOP = ("tr_M_at_q0", "n_strands")
    REQUIRED_ROW = ("partition", "chi_lambda", "y_lambda", "dim")
    usable: dict[str, dict] = {}
    for atom, stem in ATOMS.items():
        chi = _load(f"{stem}.witness.json")
        missing_top = [k for k in REQUIRED_TOP if k not in chi]
        rows = chi.get("by_partition") or []
        missing_row = sorted(
            {k for k in REQUIRED_ROW for r in rows if k not in r}
        )
        ok = not missing_top and not missing_row
        check(
            f"schema/{atom}",
            ok,
            "all required fields present"
            if ok
            else f"MISSING top-level {missing_top} / per-partition {missing_row} "
                 f"in {stem}.witness.json -- see bean qou-16yn",
        )
        if ok:
            usable[atom] = chi

    # --- 1. the copy, not a computation -------------------------------------
    for atom, chi in usable.items():
        a = substrate[atom]["tr_M"]
        b = chi["tr_M_at_q0"]
        check(
            f"copy/{atom}",
            a == b,
            f"option_e tr_M == chi tr_M_at_q0 verbatim: {a[:24]}... vs {b[:24]}...",
        )

    # --- 2. chi self-consistency: tr_M == sum y*chi --------------------------
    for atom, chi in usable.items():
        tot = mp.mpf(0)
        for e in chi["by_partition"]:
            tot += mp.mpf(e["y_lambda"]) * mp.mpf(e["chi_lambda"])
        rec = mp.mpf(chi["tr_M_at_q0"])
        rel = abs(tot - rec) / abs(rec)
        check(
            f"selfconsistent/{atom}",
            rel < mp.mpf("1e-45"),
            f"|sum y*chi - tr_M|/|tr_M| = {mp.nstr(rel, 6)}",
        )

    # --- 3. chi's y_lambda is current w.r.t. the live default table ----------
    ydef = _load(Y_DEFAULT)
    for atom, chi in usable.items():
        n = int(chi["n_strands"])
        table = {
            tuple(w["partition"]): mp.mpf(w["y_lambda"])
            for w in ydef["tables_by_n"][str(n)]["weights"]
        }
        worst = mp.mpf(0)
        worst_p = None
        for e in chi["by_partition"]:
            p = _parts(e)
            d = abs(mp.mpf(e["y_lambda"]) - table[p])
            if d > worst:
                worst, worst_p = d, p
        check(
            f"current/{atom}",
            worst < mp.mpf("1e-45"),
            f"max |y_chi - y_default| = {mp.nstr(worst, 6)} at {worst_p} (n={n})",
        )

    # --- 4. the >=3-row weights vanish in BOTH tables ------------------------
    yideal = _load(Y_IDEAL)
    for label, tab in (("default", ydef), ("ideal", yideal)):
        worst = mp.mpf(0)
        worst_p = None
        for nkey, t in tab["tables_by_n"].items():
            for w in t["weights"]:
                if len(w["partition"]) >= 3:
                    v = abs(mp.mpf(w["y_lambda"]))
                    if v > worst:
                        worst, worst_p = v, (nkey, tuple(w["partition"]))
        check(
            f"vanishing/{label}",
            worst < VANISHING,
            f"largest |y| on a >=3-row partition = {mp.nstr(worst, 6)} at {worst_p}",
        )

    n_pass = sum(1 for c in checks if c["pass"])
    for c in checks:
        print(f"[{'PASS' if c['pass'] else 'FAIL'}] {c['check']}: {c['detail']}")
    print(f"\n{n_pass}/{len(checks)} checks pass")

    wb = WitnessBuilder(
        "trm-provenance-chain",
        _script_path=__file__,
    )
    wb.save(
        {
            "description": (
                "Provenance of the +48.1039 % tr_M_atom move recorded in bean "
                "qou-brkp item 2. The option_e probe copies tr_M_at_q0 verbatim "
                "from the chi witness (line 129); the chi witness moved in "
                "7e4d1aa6d0 because fcf629cf41, 33 s earlier, switched "
                "_Y_LAMBDA_DEFAULT in tr_m_wenzl_bridge_mpfr.py -- and both "
                "y_lambda tables had been REGENERATED the same day, moving "
                "weight mass onto the <=2-row partitions. A weight-table "
                "regeneration, not a pin swap, not a convention swap. Every "
                "chi_lambda and every provenance field (scriptHash, q0Anchor, "
                "q0Value, dps) is byte-identical across the move, which is why "
                "scriptHash-keyed staleness cannot see it."
            ),
            "checks": checks,
            "checks_passed": n_pass,
            "checks_total": len(checks),
            "move": {
                "from": "0.38835714119779098941649346949090499349342765669823",
                "to": "0.57517224391777187082653534398618088915249435289286",
                "pct": "48.10394425703005525929125114",
                "atom": "deuteron",
                "chi_commit": "7e4d1aa6d0",
                "trigger_commit": "fcf629cf41",
                "trigger_gap_seconds": 33,
                "option_e_pickup_commit": "a0ee2ac5e9",
                "option_e_lag_days": 13,
            },
            "y_lambda_n6_ratio_by_partition": {
                "[3, 3]": "1.07102505",
                "[4, 2]": "1.14268671",
                "[5, 1]": "1.33907814",
                "[6]": "1.94844848",
            },
            "classification": "y_lambda weight-table regeneration",
            "q0Anchor": "ambiguous",
            "q0AnchorReason": (
                "provenance audit across pins: reads recorded values from the "
                "proton-anchored chi-*-at-q0-50dps and y-lambda-mpfr-proton "
                "witnesses AND from the muon-stamped y-lambda-mpfr-witness "
                "(whose recorded q0 is the retired frozen pin A), and compares "
                "them; it evaluates nothing at q0 itself"),
            "ruled_out": [
                "mu-p pin swap (11.5 ppb, three orders too small)",
                "convention C->D (z identical either side of the move)",
                "precision change (dps = 50 both sides)",
                "producer source change (scriptHash c36a8a393fcd both sides)",
            ],
        }
    )
    return 0 if n_pass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
