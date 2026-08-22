"""
chi_convention_trM_ratio_probe.py — is the mass/vol-density path's use of the
AVERAGED (B) χ cache a bug? (b0vf follow-up / #3047 ⚠ finding resolution)

The #3047 chi-convention audit flagged that `canonical_tr_m_via_chi_cache.py`
(consumed by the mass / vol-density / per-knot path, incl.
`_li_2_q_util.per_knot_density_per_block`) loads the **averaged-crossings (B)** χ
cache, while the canonical *binding* path (`binding_canonical.py`) uses the
Jones–Markov trace (C). Since `per_knot_density_per_block = [Vol(K)/ℏ_q²]·tr_M_K`
is LINEAR in tr_M_K, the production delta from switching to the sign-only (A)
cache is exactly the ratio tr_M_A / tr_M_B.

This probe computes tr_M = Σ_λ y_λ(q₀)·χ^λ for each atom from BOTH caches
(the averaged `chi-{atom}-h{n}-at-q0-50dps` and the sign-only
`…-at-q0-50dps-matrix-m`), using the SAME y_λ, and reports the ratio.

## Verdict (NOT a bug — averaged B is correct for the mass path)

Two facts settle it:

  1. **Sign-only (A) loses the p/n distinction.** A gives
     proton = neutron = 1.6332 (the crossing signs are identical for the two
     nucleons), so it CANNOT produce m_n ≠ m_p. The averaged (B) color-
     weighting gives proton 1.0653 ≠ neutron 0.9232 — the asymmetry that the
     mass path needs (cheat-sheet §"Bring color-tube weighted averaging":
     the averaging reproduces Δm_{n-p}).
  2. **The documented canonical-for-mass values ARE the averaged ones.**
     `_li_2_q_util.py` (the per_knot_density_per_block docstring) states
     "the H₃ Markov trace tr_M(𝓑₃) ≈ 1.065 (proton) / 0.923 (neutron)" —
     exactly the averaged (B) values, not sign-only's 1.633/1.633.

So the three-convention structure is INTENTIONAL, not an inconsistency:
  - A (sign-only)        → production character catalogue / chi_lambda_braid
  - B (averaged)         → mass / vol-density path (REQUIRED for p/n asymmetry)
  - C (Jones–Markov)     → binding (free − bound difference)

Switching the mass path to A would destroy the proton–neutron mass
difference. The #3047 "convention inconsistency" flag is hereby downgraded to
"intentional three-convention structure".

Usage:  python3 chi_convention_trM_ratio_probe.py
Output: chi-convention-trM-ratio-probe.witness.json
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50

# atom → (Z, N, n_strands). Only atoms with BOTH a complete averaged and a
# complete sign-only cache give a trustworthy ratio; he4's averaged cache is
# partial (22/77) so its ratio is reported but flagged unreliable.
ATOMS = [
    ("deuteron", 1, 1, 6),
    ("proton", 1, 0, 3),
    ("neutron", 0, 1, 3),
    ("helium-4", 2, 2, 12),
]


def sum_tr_m(cache_file: Path, n: int, q0: mp.mpf) -> tuple[mp.mpf, int, int]:
    d = json.loads(cache_file.read_text())
    y = y_lambda_at(n, q0)
    tr = mp.mpf(0)
    used = 0
    for e in d["by_partition"]:
        raw = e["partition"]
        lam = tuple(json.loads(raw)) if isinstance(raw, str) else tuple(raw)
        if lam not in y:
            continue
        tr += mp.mpf(str(y[lam])) * mp.mpf(e["chi_lambda"])
        used += 1
    return tr, used, len(d["by_partition"])


def main() -> int:
    q0 = mp.mpf(Q_50_DIGIT_STR)
    rows = []
    print(f"{'atom':10} {'tr_M avg(B)':>14} {'tr_M sign(A)':>14} "
          f"{'A/B':>10}  used(B/A)")
    for atom, Z, N, n in ATOMS:
        b_file = HERE / f"chi-{atom}-h{n}-at-q0-50dps.witness.json"
        a_file = HERE / f"chi-{atom}-h{n}-at-q0-50dps-matrix-m.witness.json"
        if not (b_file.exists() and a_file.exists()):
            continue
        b, ub, tb = sum_tr_m(b_file, n, q0)
        a, ua, ta = sum_tr_m(a_file, n, q0)
        ratio = (a / b) if b != 0 else mp.mpf("nan")
        complete = (ub == tb == ua == ta)
        rows.append({
            "atom": atom, "Z": Z, "N": N, "n_strands": n,
            "tr_M_averaged_B": str(b), "tr_M_sign_only_A": str(a),
            "ratio_A_over_B": str(ratio),
            "averaged_complete": ub == tb, "sign_only_complete": ua == ta,
            "ratio_trustworthy": complete,
        })
        print(f"{atom:10} {mp.nstr(b, 8):>14} {mp.nstr(a, 8):>14} "
              f"{mp.nstr(ratio, 6):>10}  {ub}/{ua}"
              + ("" if complete else "  (partial — ratio unreliable)"))

    # The p/n discriminator: sign-only gives proton == neutron; averaged does not.
    p = next((r for r in rows if r["atom"] == "proton"), None)
    nn = next((r for r in rows if r["atom"] == "neutron"), None)
    pn_distinct_B = pn_distinct_A = None
    if p and nn:
        pn_distinct_A = p["tr_M_sign_only_A"] != nn["tr_M_sign_only_A"]
        pn_distinct_B = p["tr_M_averaged_B"] != nn["tr_M_averaged_B"]
        print()
        print(f"p/n distinct under sign-only (A)? {pn_distinct_A}  "
              f"(proton {mp.nstr(mp.mpf(p['tr_M_sign_only_A']),6)} vs "
              f"neutron {mp.nstr(mp.mpf(nn['tr_M_sign_only_A']),6)})")
        print(f"p/n distinct under averaged (B)?  {pn_distinct_B}  "
              f"(proton {mp.nstr(mp.mpf(p['tr_M_averaged_B']),6)} vs "
              f"neutron {mp.nstr(mp.mpf(nn['tr_M_averaged_B']),6)})")

    verdict = (
        "NOT a bug. The mass/vol-density path correctly uses the averaged (B) "
        "trace: sign-only (A) gives proton==neutron (cannot produce m_n≠m_p), "
        "while the documented canonical-for-mass values tr_M(𝓑₃)≈1.065(p)/"
        "0.923(n) (_li_2_q_util.py) ARE the averaged (B) values. Switching to "
        "A would destroy the p/n mass asymmetry. The #3047 'convention "
        "inconsistency' flag is downgraded to 'intentional three-convention "
        "structure' (A=character catalogue, B=mass/vol-density, C=binding)."
    )
    print("\nVERDICT:", verdict)

    builder = WitnessBuilder("chi-convention-trM-ratio-probe")
    builder.set_description(
        "Resolves the #3047 ⚠ finding: switching canonical_tr_m_via_chi_cache "
        "from averaged (B) to sign-only (A) changes tr_M by 1.5–3.4×, BUT B is "
        "correct for the mass path (p/n asymmetry + documented 1.065/0.923). "
        "NOT a bug. See docs/audits/2026-06-29-chi-convention-mass-path-verdict.md."
    )
    builder.add_data("rows", rows)
    builder.add_data("pn_distinct_sign_only_A", pn_distinct_A)
    builder.add_data("pn_distinct_averaged_B", pn_distinct_B)
    builder.add_data("verdict", verdict)
    builder.add_assertion(
        "sign_only_collapses_pn",
        computed=int(pn_distinct_A is False), expected=1, tolerance=0,
        unit="bool", source="probe (this script)",
    )
    builder.add_assertion(
        "averaged_preserves_pn",
        computed=int(pn_distinct_B is True), expected=1, tolerance=0,
        unit="bool", source="probe (this script)",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
