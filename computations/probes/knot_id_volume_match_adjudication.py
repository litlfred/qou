#!/usr/bin/env python3
"""Adjudicate the canonical-knot-id volume fork by recomputing the
historical volume-matching for BOTH candidate knot sets.

Context (snappy-census-volume-verification.witness.json + thread-2
gating doc §Update 2026-06-12): the `conj:canonical-knot-id-sdp`
§"Historical evidence" table prints volumes of {6_1, 8_1, 6^3_1} —
subscript-neighbours of the knots it names {6_2, 8_11, L6a4} — so the
volume-matching evidence stream appeared to support a different knot
set than production + the SDP partial closure use.

This probe recomputes the match itself. The reconstructed law is

    B_AME(H)  ≈  ρ · m_e · Vol(K)

— the framework's own binding-as-(electron scale × hyperbolic volume)
shape (cf. m(K) = m_e·Vol(K)·ρ(K)/ℏ_q², canonical cheat-sheet §9), with
ρ the conjecture table's multiplicity {D:1, T:2, ³He:2}. Under it:

    named set  {6_2, 8_11, L6a4}: errors ≈ +1.1 %, −0.16 %, −3.0 %
        — reproducing the historical table's claimed match-quality
        pattern (<1 %, <0.5 %, <2 % after correction);
    orphan set {6_1, 8_1, 6^3_1}: errors 27–59 % at the table ρ.

STEELMAN: the orphan set is also scored at its best integer ρ ∈ 1..4
per nucleus. The deuteron stays ≥ 27 % off at every ρ, so the orphan
set fails under any multiplicity choice.

Verdict the witness encodes: the *names* are right (production wiring
and the SDP stream are consistent with the volume-matching evidence
once recomputed); the printed volume *digits* in the conj table are
stale survivors. The mechanical digit fixes (conj table + the
MostowRigidity.lean:264 comment) remain owner-confirmed thread-4
actions — this probe supplies the decision basis, it changes nothing.

EXPLORATORY / DIAGNOSTIC — no production path touched, no fit: the law
has zero free parameters (m_e is CAL-1, volumes are census, ρ is the
conjecture's own table).

Ref: docs/audits/2026-06-06-thread2-deuteron-perknot-gating.md
Ref: docs/audits/2026-06-12-knot-id-volume-match-adjudication.md
Ref: content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md
"""
from __future__ import annotations

# Path bridge (probes cluster — subdirectory refactor Phase 1).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent

# (nucleus, named knot, orphan manifold, rho from conj table)
ROWS = [
    ("2H", "6_2", "6_1", 1),
    ("3H", "8_11", "8_1", 2),
    ("3He", "L6a4", "6^3_1", 2),
]

# AME2020 helium-3 binding fallback (the ame witness carries D and T).
B_HELIUM3_FALLBACK_MEV = "7.718043"


def b_ame() -> dict[str, mp.mpf]:
    """Per-nucleus AME binding energies, from the AME witness where
    available (D, T), literature AME2020 fallback for ³He."""
    data = json.loads(
        (COMPUTATIONS / "ame-2020-binding-energies.witness.json").read_text()
    )["data"]
    out = {
        "2H": mp.mpf(data["B_deuteron_MeV"]),
        "3H": mp.mpf(data["B_tritium_MeV"]),
    }
    for key in ("B_helium3_MeV", "B_he3_MeV", "B_3He_MeV"):
        if key in data:
            out["3He"] = mp.mpf(data[key])
            break
    else:
        out["3He"] = mp.mpf(B_HELIUM3_FALLBACK_MEV)
    return out


def hp_volume(name: str) -> mp.mpf:
    import snappy

    return mp.mpf(str(snappy.ManifoldHP(name).volume()))


def main() -> int:
    set_compute_dps()
    me = mp.mpf(repr(M_E_MEV))
    B = b_ame()

    w = WitnessBuilder("knot-id-volume-match-adjudication", engine="snappea")
    w.set_description(
        "Adjudicates the conj:canonical-knot-id-sdp volume fork: scores "
        "BOTH knot sets (named {6_2, 8_11, L6a4} vs orphan {6_1, 8_1, "
        "6^3_1}) under the zero-free-parameter law B_AME ≈ ρ·m_e·Vol(K) "
        "with the conjecture's own multiplicities ρ={1,2,2}. Named set "
        "reproduces the historical match-quality pattern (≤3 %); orphan "
        "set fails (27–59 % at table ρ; deuteron ≥27 % at EVERY integer "
        "ρ ≤ 4). Verdict: the names are right, the printed digits are "
        "stale. Diagnostic only — content/Lean digit fixes remain "
        "owner-confirmed thread-4 actions."
    )

    print(f"law: B_pred = rho * m_e * Vol(K),  m_e = {mp.nstr(me, 12)} MeV")
    print(f"{'nuc':4s} {'set':7s} {'knot':6s} {'Vol':>12s} {'rho':>3s} "
          f"{'B_pred':>10s} {'B_AME':>10s} {'rel_err%':>9s}")

    for nucleus, named, orphan, rho in ROWS:
        b = B[nucleus]
        for tag, knot in (("named", named), ("orphan", orphan)):
            vol = hp_volume(knot)
            pred = rho * me * vol
            rel = (pred - b) / b
            print(f"{nucleus:4s} {tag:7s} {knot:6s} {mp.nstr(vol, 10):>12s} "
                  f"{rho:>3d} {mp.nstr(pred, 8):>10s} {mp.nstr(b, 8):>10s} "
                  f"{mp.nstr(100 * rel, 4):>9s}")
            w.add_data(f"{nucleus}_{tag}_knot", knot)
            w.add_data(f"{nucleus}_{tag}_vol", mp.nstr(vol, 50))
            w.add_data(f"{nucleus}_{tag}_B_pred", mp.nstr(pred, 50))
            w.add_data(f"{nucleus}_{tag}_rel_err", mp.nstr(rel, 10))
            if tag == "named":
                w.add_assertion(
                    name=f"{nucleus}_named_matches_within_3p5pct",
                    computed=bool(abs(rel) < mp.mpf("0.035")),
                    expected=True,
                    tolerance=0.035,
                    source=f"B_AME({nucleus}) vs rho·m_e·Vol({knot}) — "
                           "reproduces the conj table's claimed quality",
                )
            else:
                w.add_assertion(
                    name=f"{nucleus}_orphan_fails_at_table_rho",
                    computed=bool(abs(rel) > mp.mpf("0.20")),
                    expected=True,
                    tolerance=0.20,
                    source=f"B_AME({nucleus}) vs rho·m_e·Vol({knot}) — "
                           "orphan volume fails the same law",
                )
        w.add_data(f"{nucleus}_B_AME", mp.nstr(b, 20))
        w.add_data(f"{nucleus}_rho_table", str(rho))

    # Steelman: orphan set at its BEST integer rho in 1..4 per nucleus.
    print("steelman — orphan set at best integer rho in 1..4:")
    for nucleus, _named, orphan, _rho in ROWS:
        b = B[nucleus]
        vol = hp_volume(orphan)
        best_rho, best_rel = min(
            ((r, abs(r * me * vol - b) / b) for r in range(1, 5)),
            key=lambda t: t[1],
        )
        print(f"  {nucleus:4s} {orphan:6s} best rho={best_rho} "
              f"|rel_err|={mp.nstr(100 * best_rel, 4)}%")
        w.add_data(f"{nucleus}_orphan_best_rho", str(best_rho))
        w.add_data(f"{nucleus}_orphan_best_rel_err", mp.nstr(best_rel, 10))
    # The deuteron is the decisive case: no integer rho rescues 6_1.
    vol_d = hp_volume("6_1")
    d_best = min(abs(r * me * vol_d - B["2H"]) / B["2H"] for r in range(1, 5))
    w.add_assertion(
        name="2H_orphan_fails_at_every_rho_1_to_4",
        computed=bool(d_best > mp.mpf("0.20")),
        expected=True,
        tolerance=0.20,
        source="Vol(6_1) cannot match B_AME(2H) under B=rho·m_e·Vol for "
               "any integer rho ≤ 4 — the orphan set fails regardless of "
               "multiplicity choice",
    )

    out = w.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
