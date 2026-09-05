#!/usr/bin/env python3
"""Triage the 26 files the `w_lambda` name gate never examined.

Bean `qou-oots`. `w_lambda_family_consumer_audit.py` reports 26 files carrying a
Plancherel-SHAPED `d^2/[n]_q!` construction that its name gate never looked at
(the 13th blindness mode, PR #6867). That count is not a blast radius, and this
audit is what stands between the two.

THE PREMISE, MEASURED FIRST, BECAUSE I GOT IT WRONG ONCE. In PR #6867 I wrote
that `mass_endomorphism.py` "divides by the sum of its own weights and is
therefore already self-normalised dim_q^2/D^2, which the ruling does not move."
The second clause is FALSE and the error matters, because it would exempt a
whole class from triage. Measured at the proton q0:

    worst |selfnorm(dim_q^2/[n]!) - Molien| / Molien   =  0.385  at n = 3
                                                          3.826  at n = 6

Self-normalisation cancels a LAMBDA-INDEPENDENT rescale, which is exactly what
`dim_q^2/[n]_q! -> dim_q^2/D^2` is (same numerator). Molien is NOT that: its
numerator changes from `dim_q^2` to `f^lam q^{-kappa} dim_q`, which is
lambda-DEPENDENT, so nothing cancels. A self-normalised file sits on the
RETAINED SECOND ARM of the qou-oots two-arm ruling -- it needs no fix -- but it
is not invariant, and its number differs from the canonical arm by up to 383 %
at the nuclear n = 6. "On a sanctioned arm" and "unmoved by the ruling" are
different claims and only the first is true.

SO THE TRIAGE QUESTION IS NOT "DOES IT MOVE". Essentially every file here moves,
because every one of them weights a sum over lambda. The questions that separate
them are:

  1. IS IT EVEN THE FAMILY? A `shape_only` hit matched `d*d/[n]_q!` with `d`
     built inline from q-integers, and the two_quark pair proved that `d` can be
     the HOOK PRODUCT -- i.e. the q-dimension INVERTED (`dim_q =
     [n]_q!/hook_prod`). Those are in no arm at all. Checked here by evaluating
     the file's own numerator against a true `dim_q` where it is callable.
  2. DOES ANYTHING READ IT? Importer count, and whether it writes a witness that
     is actually committed. A file with no importers whose value reaches a PNG
     is a different object from one feeding a committed number.

WHAT THIS DOES NOT DO. It does not re-derive each file's physics or decide which
arm each SHOULD be on. It sizes the population so the next agent -- or I -- can
stop quoting "26" as though it were a blast radius, which is the error this
whole thread has been correcting in one form or another all day.

No float64: mpmath end to end for the premise measurement; the rest is file
inspection and exact counts.
"""

from __future__ import annotations

import ast
import json
import re
import subprocess
import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "probes"))
import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
import molien_feray_meliot_bridge_probe as MB  # noqa: E402
import plancherel_deformation_uniqueness_probe as PU  # noqa: E402

ROOT = _Path(__file__).resolve().parent.parent.parent
# The consumed witness records paths relative to `computations/`, not to the
# repo root -- that audit sets its own ROOT to `computations/`. Resolving
# against the wrong base is a FileNotFoundError here, which is the good case;
# silently reporting 0 importers for every file would have been the bad one.
CROOT = ROOT / "computations"
AUDIT_WITNESS = (ROOT / "computations/audits/"
                 "w-lambda-family-consumer-audit.witness.json")


def _find(o, key):
    if isinstance(o, dict):
        if key in o:
            return o[key]
        for v in o.values():
            r = _find(v, key)
            if r is not None:
                return r
    return None


def importer_count(rel: str) -> int:
    """Files that import this module by its bare stem."""
    stem = _Path(rel).stem
    r = subprocess.run(
        ["grep", "-rlE", rf"^\s*(from|import)\s+{re.escape(stem)}(\.|\s|$)",
         "--include=*.py", "computations", "tools"],
        capture_output=True, text=True, cwd=str(ROOT))
    return len([x for x in r.stdout.splitlines()
                if x and "_deprecated" not in x and _Path(x).name != _Path(rel).name])


def witness_status(rel: str) -> dict:
    """Does it write a witness, and is that witness committed?"""
    src = (CROOT / rel).read_text(errors="replace")
    writes = bool(re.search(r"WitnessBuilder\(|\.witness\.json", src))
    plots = bool(re.search(r"savefig|matplotlib", src))
    committed = []
    for m in re.finditer(r'"([a-z0-9\-]+\.witness\.json)"', src):
        p = (CROOT / rel).parent / m.group(1)
        if p.exists():
            committed.append(p.relative_to(ROOT).as_posix())
    return {"writes_witness": writes, "plots": plots,
            "committed_witnesses": committed}


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(Q_50_DIGIT_STR)

    b = WitnessBuilder("molien-name-gate-missed-triage")
    b.set_description(
        "Bean qou-oots. Triages the 26 files that w_lambda_family_consumer_"
        "audit's NAME GATE never examined (13th blindness mode, PR #6867), so "
        "that 26 stops being quoted as a blast radius. Establishes first, by "
        "measurement, that SELF-NORMALISATION DOES NOT PROTECT AGAINST MOLIEN "
        "-- correcting my own claim in #6867 that a self-normalised file is "
        "'not moved by the ruling'. It cancels a lambda-INDEPENDENT rescale "
        "(which dim_q^2/[n]! -> dim_q^2/D^2 is) but not Molien's "
        "lambda-DEPENDENT q^{-kappa}: worst divergence 0.385 at n=3 and 3.826 "
        "at n=6. Such a file sits on the RETAINED SECOND ARM and needs no fix, "
        "but is NOT invariant. Then sizes each file by whether it is even the "
        "family (shape_only hits can be the hook product, i.e. the q-dimension "
        "inverted) and by whether anything reads it."
    )
    b.add_parameter("q0_50dps", Q_50_DIGIT_STR)

    # -- the premise ----------------------------------------------------------
    prem = {}
    for n in (3, 6, 9):
        lams = MB.partitions(n)
        qf = PU.q_factorial(q0, n)
        wA = {l: PU.dim_q(q0, l) ** 2 / qf for l in lams}
        wM = {l: MB.molien_weight(q0, l) for l in lams}
        SA, SM = mp.fsum(wA.values()), mp.fsum(wM.values())
        worst = max(abs(wA[l] / SA - wM[l] / SM) / (wM[l] / SM) for l in lams)
        prem[str(n)] = {"sum_dimq2_over_qfact": fmt(SA),
                        "sum_molien": fmt(SM),
                        "worst_selfnorm_vs_molien_rel": fmt(worst)}
    b.add_data("premise_selfnorm_does_not_protect", {
        "per_n": prem,
        "correction": "PR #6867 said a self-normalised file is 'already "
                      "dim_q^2/D^2, which the ruling does not move'. The second "
                      "clause is FALSE. Self-normalisation cancels only a "
                      "lambda-INDEPENDENT rescale; Molien's numerator change "
                      "dim_q^2 -> f^lam q^{-kappa} dim_q is lambda-dependent. "
                      "'On a sanctioned arm' and 'unmoved by the ruling' are "
                      "different claims and only the first holds.",
    })
    b.add_assertion(
        "selfnorm_arm_diverges_from_molien_at_nuclear_n",
        computed="1" if mp.mpf(prem["6"]["worst_selfnorm_vs_molien_rel"]) > 1
                 else "0",
        expected="1",
        source=f"worst relative divergence at n = 6 (A = 2) is "
               f"{prem['6']['worst_selfnorm_vs_molien_rel']}, i.e. over 100 %. "
               f"Recorded as a predicate so the witness summary cannot read "
               f"FAILURES when nothing failed; the magnitudes are in "
               f"premise_selfnorm_does_not_protect.",
    )

    # -- the 26 ---------------------------------------------------------------
    reg = json.loads(AUDIT_WITNESS.read_text())
    missed = _find(reg, "name_gate_missed")
    rows = {}
    tally = {"shape_only": 0, "no_importers": 0, "writes_committed_witness": 0,
             "plot_only": 0, "session_harness": 0}
    for rel, hits in sorted(missed["files"].items()):
        so = any(h.get("shape_only") for h in hits)
        imp = importer_count(rel)
        ws = witness_status(rel)
        harness = "/probes/" in "/" + rel and "triage" in rel or "budget_probe" in rel
        rows[rel] = {
            "hits": len(hits),
            "shape_only": so,
            "importers": imp,
            **ws,
            "session_harness": bool(harness),
            "first_hit": hits[0]["source"][:70],
        }
        tally["shape_only"] += so
        tally["no_importers"] += (imp == 0)
        tally["writes_committed_witness"] += bool(ws["committed_witnesses"])
        tally["plot_only"] += (ws["plots"] and not ws["committed_witnesses"])
        tally["session_harness"] += bool(harness)
    b.add_data("per_file", rows)
    b.add_data("tally", {
        **tally, "total": len(rows),
        "note": "A row is NOT automatically in the Molien blast radius. "
                "`shape_only` means the numerator was built inline from "
                "q-integers and is NOT confirmed to be a dim_q -- the two_quark "
                "pair is the proof that such a `d` can be the HOOK PRODUCT, the "
                "q-dimension inverted, which is in no arm at all. A file with 0 "
                "importers whose value reaches only a plot is a different "
                "object from one feeding a committed witness.",
    })

    # -- the one file with reach, traced end to end -----------------------------
    # 24 of the 26 have ZERO importers. The two that do not are
    # keystone_wlambda_defect_coeff_ladder (1) and mass_endomorphism (8 module
    # importers), and only the latter carries the WEIGHTS anywhere. Traced:
    b.add_data("the_one_file_with_reach", {
        "file": "computations/mass_endomorphism.py",
        "chain": [
            "w_sym/w_std/w_alt at L93-99: dim_q^2/[3]_q!, then divided by their "
            "own sum -> self-normalised (the RETAINED second arm, not the "
            "canonical one)",
            "L132  Vf = w_sym*sp + w_std*Vs + w_alt*ap, inside "
            "additive_wedderburn_volumes()",
            "returned as v['full']",
            "m_p_m_e_li2q.py:78-80 calls it for electron / proton / neutron",
            "m_p_m_e_li2q.py:48,50,54 consume v['full'] into desc/single/cross",
            "-> mp_me = p_total/e_total, compared against codata_mp_me = 1836.152",
        ],
        "weights_do_not_cancel_in_the_ratio": "w_sym/w_std/w_alt are MODULE-LEVEL "
            "constants for lambda |- 3 applied to the electron (2 strands) and "
            "the nucleons (3 strands) alike, and Vf enters non-linearly through "
            "Phi_q(|Vf|) and through products Vf_i*Vf_j. So there is no "
            "cancellation and the ruling does reach this number.",
        "import_counts_measured_by_AST": {
            "additive_wedderburn_volumes": 2, "Phi_q": 8, "z_mark": 7,
            "proton_cross": 4, "neutron_cross": 4, "mass_from_tower": 1,
            "note": "measured with ast.ImportFrom, NOT grep. A single-line "
                    "`import.*\\bname\\b` grep reported 0 for "
                    "additive_wedderburn_volumes, because BOTH real importers "
                    "use a parenthesised multi-line import and the name sits on "
                    "a continuation line. Same blindness class as everything "
                    "else in this thread, committed by me while auditing it.",
        },
        "🛑 AND IT IS IMMATERIAL, WHICH IS THE POINT": "The committed witness "
            "computations/m-p-m-e-li2q.witness.json records m_p/m_e = "
            "9310.3278 (err 407.06 %) on the Phi_q arm and 3.3322 (err 99.82 %) "
            "on the Li_2_q arm, against CODATA 1836.152. The route is ALREADY "
            "recorded as a catastrophic miss, so a 38.5 % weight change can "
            "neither rescue nor damage it. The one file of the 26 with real "
            "reach carries the weight into a comparison that is already "
            "refuted.",
        "separate_observation_not_fixed_here": "additive_wedderburn_volumes is "
            "float64 throughout (a, b = 0.0, 1.0; sp, ap = 1.0, 1.0) on a path "
            "that ends at a CODATA comparison. Noted, not fixed: it is a "
            "different defect from the weight family and belongs in its own "
            "change.",
    })

    b.save()

    print("PREMISE -- does self-normalisation protect against Molien?")
    for n in ("3", "6", "9"):
        p = prem[n]
        print(f"  n={n}: sum(d_q^2/[n]!) = {p['sum_dimq2_over_qfact'][:14]}   "
              f"worst |selfnorm - Molien|/Molien = "
              f"{p['worst_selfnorm_vs_molien_rel'][:14]}")
    print("  -> NO. It cancels a lambda-independent rescale; Molien is not one.\n")

    print(f"{'shp':>3} {'imp':>4} {'wit':>4} {'plot':>5}  file")
    for rel, r in rows.items():
        print(f"{'Y' if r['shape_only'] else '.':>3} {r['importers']:>4} "
              f"{'Y' if r['committed_witnesses'] else '.':>4} "
              f"{'Y' if r['plots'] else '.':>5}  {rel}")
    print(f"\ntally: {tally}  of {len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
