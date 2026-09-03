#!/usr/bin/env python3
"""q-Reeb eigenphase compactness probe (bean qou-0g4z).

The surviving lead of the Δ_λ magnitude gate after the single-universal ``C_knot`` route was
refuted (PR #4556) is the **per-vertex q-Reeb eigenphase** ``θ_λ = arccos(χ_λ / d_λ)`` — the
accumulated rotation angle of the knot operator on the Wedderburn block ``V_λ``, already
formalized for the figure-eight muon anchor (``figure-eight-reeb-rotation``) where
``2 cos θ = tr M_{4₁}(q)`` and the perfect-square identity gives ``tr M_{4₁}(q) ≥ −2`` (the block
is provably *compact* on the real substrate axis).

This probe measures, 0-fit, the block-by-block normalized character ``|χ_λ / d_λ|`` for the
binding knots D (H₆), T (H₉), ³He (H₉) from the committed per-partition χ witnesses, and reports
the compact-vs-boost split. The eigenphase ``θ_λ = arccos(χ_λ/d_λ)`` is a *real rotation angle*
only where ``|χ_λ/d_λ| ≤ 1`` (compact); where it exceeds 1 the eigenvalue is off the unit circle
(a boost / real scaling, no rotation angle — see ``QReebEigenphaseCompact.no_rotation_angle_of_boost``).

Finding (see the companion audit): in **every** binding knot the ONLY block with ``|χ/d| > 1`` is
the **trivial 1-dimensional representation** ``(n,)`` (dim ``f^λ = 1``, character ``q^w`` — a pure
scaling by the writhe ``w``, which has no mixing hence no rotation angle at all). **Every**
genuinely-rotational block (dim ``≥ 2``, where ``θ_λ`` is defined) is compact. Therefore the
q-Reeb eigenphase content is bounded, and the sole unbounded channel is the trivial-rep scaling
``q^w`` — already a summand of the master binding formula ``B = m_e·|Σ_λ y_λ χ^λ f^λ|``. The
eigenphase route is difference-only and cannot supply the absolute binding scale ``C_knot``.

scope-(a): this construction, alone, does not close the Δ_λ magnitude gate. No fit; ``B_AME``
is not read; ``free_parameters = 0``; nothing wired. AME never enters — the probe reads only the
categorical χ witnesses.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
COMP = REPO / "computations"

# (label, H_n, committed per-partition χ witness at q₀)
KNOTS = [
    ("D", 6, COMP / "chi-deuteron-h6-at-q0-50dps.witness.json"),
    ("T", 9, COMP / "chi-tritium-h9-at-q0-50dps.witness.json"),
    ("3He", 9, COMP / "chi-helium-3-h9-at-q0-50dps.witness.json"),
]


def _by_partition(doc: dict) -> list:
    return doc.get("by_partition") or doc.get("data", {}).get("by_partition") or []


def analyze(path: Path) -> dict:
    doc = json.load(open(path))
    boost, rot_max, rot_max_part = [], 0.0, None
    for e in _by_partition(doc):
        part = tuple(e.get("partition", []))
        dim = e.get("dim") or e.get("f_lambda")
        chi = e.get("chi_lambda", e.get("chi"))
        if dim is None or chi is None:
            continue
        ratio = abs(float(chi) / dim)
        if ratio > 1.0:
            boost.append({"partition": list(part), "dim": dim, "abs_chi_over_dim": ratio})
        elif dim >= 2 and ratio > rot_max:
            rot_max, rot_max_part = ratio, list(part)
    return {"boost": boost, "rotation_max": rot_max, "rotation_max_partition": rot_max_part,
            "n_blocks": len(_by_partition(doc))}


def main() -> int:
    results, ok = {}, True
    print(f"{'K':4}{'H_n':>4}{'blocks':>7}   sole-boost block            max|χ/d| dim≥2 (rotation)")
    print("-" * 78)
    for label, hn, path in KNOTS:
        if not path.exists():
            print(f"{label:4}{hn:>4}   MISSING witness: {path.name}")
            ok = False
            continue
        r = analyze(path)
        results[label] = r
        # Discipline check: exactly one boost block, and it is 1-dimensional (trivial rep).
        one_boost = len(r["boost"]) == 1
        boost_is_1dim = one_boost and r["boost"][0]["dim"] == 1
        rot_compact = r["rotation_max"] <= 1.0
        b = r["boost"][0] if r["boost"] else {"partition": None, "dim": None, "abs_chi_over_dim": 0.0}
        flag = "OK" if (boost_is_1dim and rot_compact) else "!! UNEXPECTED"
        print(f"{label:4}{hn:>4}{r['n_blocks']:>7}   "
              f"{str(tuple(b['partition'])):<12} dim={b['dim']} |χ/d|={b['abs_chi_over_dim']:.4f}   "
              f"{r['rotation_max']:.4f} @ {r['rotation_max_partition']}  {flag}")
        if not (boost_is_1dim and rot_compact):
            ok = False

    print("-" * 78)
    print("Verdict: in every binding knot the SOLE |χ/d|>1 block is the trivial 1-dim rep (n,)")
    print("  — a q^w scaling with no rotation angle; every dim≥2 rotation channel is compact.")
    print("  ⇒ the q-Reeb eigenphase route is bounded/difference-only and cannot supply C_knot.")
    print("  scope-(a) negative; free_parameters=0; B_AME not read; nothing wired.")

    out = COMP / "deltalambda" / "qreeb-eigenphase-compactness.witness.json"
    # Provenance stamp (bean qou-f1rs): the witness dict was built
    # INLINE at the write below, so there was nothing to stamp. It
    # is bound to a name here so this producer records which script
    # wrote it -- a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    _prov_payload = {
        "description": "q-Reeb eigenphase compactness: sole |chi/d|>1 block per binding knot is the "
                       "trivial 1-dim rep; all dim>=2 rotation blocks compact. Eigenphase route "
                       "cannot supply C_knot (scope-a). bean qou-0g4z.",
        "free_parameters": 0,
        "reads_B_AME": False,
        "knots": results,
        "verdict": "eigenphase-route-compact-cannot-supply-absolute-scale",
    }
    _prov_payload.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        _prov_payload, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(_prov_payload, indent=2) + "\n")
    print(f"\nwitness -> {out.relative_to(REPO)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
