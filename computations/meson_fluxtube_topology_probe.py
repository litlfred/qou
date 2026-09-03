#!/usr/bin/env python3
"""Meson flux-tube topology probe (bean qou-qpj9 / PR #4614).

Verifies the two structural facts behind the honest negative in
docs/audits/2026-08-02-meson-fluxtube-junction-reduction.md:

  (A) The 3-strand Borromean baryon knot (σ₁σ₂⁻¹)³ is hyperbolic
      (Vol = 2·V_oct ≈ 7.32772), while EVERY 2-strand closure σ₁^k =
      T(2,k) has hyperbolic volume 0 — so the naive Y-junction →
      single-tube (3→2 strand) reduction cannot produce a hyperbolic
      meson mass-knot.

This is a VERIFICATION probe (SnapPy volumes), not a fit. No braid is
selected to match any observed meson mass. The charm-winding
degeneracy (Route 2) is combinatorial and lives in the Lean file
MesonFluxTubeReduction.lean, not here.

Engine: SnapPy (Culler–Dunfield–Goerner–Weeks).
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import _path_bridge  # noqa: F401
from _precision import fmt, set_compute_dps  # noqa: E402

import snappy  # noqa: E402
from mpmath import mpf  # noqa: E402

# SnapPy computes volume at a requested bit precision; 230 bits ~ 69 dps,
# covering the repo's compute default with margin. `float(M.volume())`
# discards everything past the 16th digit of a number SnapPy already has.
BITS_PREC = 230


def braid_volume(word, nstrands, name):
    L = snappy.Link(braid_closure=word)
    M = L.exterior()
    try:
        vol = mpf(str(M.volume(bits_prec=BITS_PREC)))
    except Exception:
        vol = None
    sol = M.solution_type()
    hyperbolic = (sol == "all tetrahedra positively oriented"
                  and vol is not None and vol > mpf("1e-3"))
    return {
        "name": name,
        "n_strands": nstrands,
        "braid_word": word,
        "volume": vol,
        "solution_type": sol,
        "hyperbolic": hyperbolic,
    }


def main():
    set_compute_dps()
    results = []
    # 3-strand Borromean baryon knot and its family
    results.append(braid_volume([1, -2, 1, -2, 1, -2], 3,
                                 "Borromean baryon (sigma1 sigma2^-1)^3"))
    results.append(braid_volume([1, -2] * 6, 3, "(sigma1 sigma2^-1)^6"))
    results.append(braid_volume([1, -2] * 7, 3, "(sigma1 sigma2^-1)^7"))
    # 2-strand reductions: T(2,k) torus links, all Vol 0
    for k in (2, 3, 4, 5, 6, 9, 10):
        results.append(braid_volume([1] * k, 2, f"2-strand T(2,{k}) = sigma1^{k}"))

    borromean = next(r for r in results if r["n_strands"] == 3
                     and "Borromean" in r["name"])
    two_strand = [r for r in results if r["n_strands"] == 2]

    checks = {
        "borromean_hyperbolic": borromean["hyperbolic"],
        "borromean_vol_matches_2_voct":
            borromean["volume"] is not None
            and abs(borromean["volume"] - mpf("7.32772475342")) < mpf("1e-6"),
        "all_two_strand_non_hyperbolic":
            all(not r["hyperbolic"] for r in two_strand),
        "gluon_T29_vol_zero":
            next(r for r in two_strand if "T(2,9)" in r["name"])["volume"]
            in (0, None) or abs(next(r for r in two_strand
                                     if "T(2,9)" in r["name"])["volume"]) < mpf("1e-3"),
    }

    script_path = Path(__file__).resolve()
    script_bytes = script_path.read_bytes()
    try:
        commit = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(script_path)],
            cwd=script_path.parent, text=True).strip()
    except Exception:
        commit = None

    witness = {
        "schema": "witness/v1",
        "name": "meson-fluxtube-topology",
        "description": ("Borromean baryon knot is hyperbolic (Vol=2 V_oct); "
                        "every 2-strand T(2,k) closure has Vol=0. The naive "
                        "Y-junction -> single-tube (3->2 strand) reduction "
                        "cannot yield a hyperbolic meson mass-knot. "
                        "Verification, not fit."),
        "witness": {
            "engine": f"snappy-{snappy.__version__}",
            "scriptHash": hashlib.sha256(script_bytes).hexdigest()[:12],
            "scriptCommitSha": commit,
            "producer": "computations/meson_fluxtube_topology_probe.py",
        },
        "results": results,
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "refs": [
            "docs/audits/2026-08-02-meson-fluxtube-junction-reduction.md",
            "content/quantum-observable-universe/lean/QOU/ParticleInteractions/MesonFluxTubeReduction.lean",
            "bean qou-qpj9",
        ],
    }

    # Volumes are carried as mpf through the checks above and serialized only
    # here, via _precision.fmt -- a raw float64 in a witness is a NO-FLOAT64
    # violation, and json.dumps would emit one for any mpf left in the tree.
    def _ser(o):
        if isinstance(o, dict):
            return {k: _ser(v) for k, v in o.items()}
        if isinstance(o, list):
            return [_ser(v) for v in o]
        if isinstance(o, bool) or isinstance(o, int) or o is None:
            return o
        if isinstance(o, str):
            return o
        return fmt(o)

    out = script_path.parent / "meson-fluxtube-topology.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(_ser(witness), indent=2) + "\n")
    print(json.dumps(checks, indent=2))
    print(f"all_checks_pass={witness['all_checks_pass']}  -> {out.name}")
    return 0 if witness["all_checks_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
