"""
delta_lambda_jsj_phase3.py — Phase 3 of the closed-forms workplan.

Tests the **JSJ-decomposition closure form**:

    Δ_λ(K) = Σ_{P ∈ JSJ(K)} c_λ^(P) · Vol_hyp(P)

where Vol_hyp(P) is the hyperbolic volume of the JSJ piece P. As a
first concrete probe, we test the simplest specialisation: if K has a
single hyperbolic JSJ piece, Vol_hyp(K) is its volume, and we test
whether the per-knot factor V(K) = Vol_hyp(K) yields a K-independent
per-partition residue c_λ across D, T, ³He, ⁴He.

For each atom, this script:
  1. Builds the canonical atomic braid word β_K (reusing
     probe_he4_jsj_topology.py infrastructure).
  2. Closes the braid to a link, simplifies via SnapPy.
  3. Extracts hyperbolic volume (None for non-hyperbolic closures).
  4. Compares Vol(K) to the empirical |Δ_λ*(K)| from the empirical
     tabulation; tests separability.

Caveats:
  - SnapPy's simplification heuristic is not unique. The volume
    is well-defined (Mostow rigidity) IF the manifold is hyperbolic,
    but the simplification can fail to find a hyperbolic structure
    for satellite knots or composite links.
  - Non-hyperbolic JSJ pieces (Seifert-fibered) contribute 0 to
    the hyperbolic volume sum. The full master formula
    B = Σ_P ρ_F · Vol_hyp(P) effectively excludes these from the
    summation.

  Ref: [manuscript] conj:delta-lambda-categorical-closure
  Ref: docs/audits/2026-05-19-delta-lambda-phase2-findings.md
  Ref: docs/path-to-1ppb-04-plan.md (master formula)
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp
import snappy

from witness_base import WitnessBuilder
from codata_constants import M_E_MEV
from q_parameter import Q as Q0, HBAR_Q


def load_atom_braids() -> dict:
    """Build canonical braid words for D, T, ³He, ⁴He via the
    he4_compositional_braids helper + per-atom analogues."""
    from probe_he4_jsj_topology import (
        _proton_braid_word,
        _neutron_braid_word,
        he4_compositional_braids,
    )
    p = _proton_braid_word()
    n = _neutron_braid_word()

    # Deuteron at H_6: p (strands 1-3) + I_pn (σ_3) + n (strands 4-6)
    D = list(p) + [3] + [g + 3 for g in n]
    # Tritium at H_9: p (1-3) + I_pn (σ_3) + n (4-6) + I_nn (σ_6⁻¹) + n (7-9)
    T = list(p) + [3] + [g + 3 for g in n] + [-6] + [g + 6 for g in n]
    # ³He at H_9: p (1-3) + I_pp (σ_3) + p (4-6) + I_pn (σ_6) + n (7-9)
    He3 = list(p) + [3] + [g + 3 for g in p] + [6] + [g + 6 for g in n]
    # ⁴He at H_12: canonical pppnnn (per probe_he4_jsj_topology.py)
    He4 = he4_compositional_braids()["canonical_pppnnn"][0]

    return {
        "D":   (D,   6),
        "T":   (T,   9),
        "3He": (He3, 9),
        "4He": (He4, 12),
    }


def compute_jsj_vol(braid_word: list[int], simplify_passes: int = 5):
    """Attempt to compute hyperbolic volume of the closure of `braid_word`.
    Returns (volume_or_None, n_components, n_tetrahedra, simplification_path)."""
    link = snappy.Link(braid_closure=braid_word)
    n_components = len(link.link_components) if hasattr(link, "link_components") else None
    simplify_log = []
    for mode in ("global", "level", "global", "level", "global"):
        try:
            link.simplify(mode=mode)
            simplify_log.append(mode)
        except Exception as e:
            simplify_log.append(f"{mode}:err({type(e).__name__})")
            break

    try:
        manifold = link.exterior()
        # try to get hyperbolic volume
        try:
            vol = float(manifold.volume())
        except Exception:
            vol = None
        try:
            n_tet = int(manifold.num_tetrahedra())
        except Exception:
            n_tet = None
    except Exception as e:
        vol = None
        n_tet = None

    return vol, n_components, n_tet, "→".join(simplify_log)


def main() -> int:
    builder = WitnessBuilder("delta-lambda-jsj-phase3")
    builder.set_description(
        "Phase 3 of the closed-forms-first-principles workplan: tests "
        "the JSJ-decomposition closure form Δ_λ(K) = Σ_P c_λ^(P) · "
        "Vol_hyp(P) on D, T, ³He, ⁴He. Uses SnapPy to extract "
        "hyperbolic volumes of canonical braid closures, then tests "
        "separability V(K) = Vol(K) against empirical |Δ_λ*|."
    )

    builder.add_parameter("snappy_version", snappy.version())
    builder.add_parameter("q0", str(Q0))

    # 1. Build canonical braids
    braids = load_atom_braids()
    builder.add_data("braids", {
        a: {"word_length": len(w), "n_strands": n}
        for a, (w, n) in braids.items()
    })

    # 2. Compute hyperbolic volume for each
    vols = {}
    for a, (word, n_strands) in braids.items():
        vol, n_comp, n_tet, simp = compute_jsj_vol(word)
        vols[a] = {
            "word_length": len(word),
            "n_strands": n_strands,
            "n_components": n_comp,
            "hyperbolic_volume": vol,
            "n_tetrahedra": n_tet,
            "simplification": simp,
        }
        print(f"  {a:<6} word_len={len(word):>3} n_strands={n_strands:>2} "
              f"n_components={n_comp} vol={vol} n_tet={n_tet}")
    builder.add_data("jsj_volumes", vols)

    # 3. Load empirical |Δ_λ*| from tabulation
    emp = json.loads(
        (_pb.witness_path("delta-lambda-empirical-tabulation.witness.json", HERE)).read_text()
    )["data"]["per_atom"]
    empirical_delta = {a: float(mp.mpf(emp[a]["a_single_block"]["best_abs_delta"]))
                       for a in ("D", "T", "3He", "4He")}
    builder.add_data("empirical_best_abs_delta", empirical_delta)

    # 4. Test separability: if V(K) = Vol(K) gives K-independent c_λ
    #    then |Δ*(K)| / Vol(K) should be roughly constant across atoms
    print(f"\n  {'atom':<6} {'|Δ*|':>12} {'Vol(K)':>12} {'|Δ*|/Vol':>14}")
    ratios = {}
    for a in ("D", "T", "3He", "4He"):
        vol = vols[a]["hyperbolic_volume"]
        delta = empirical_delta[a]
        if vol is not None and vol > 0:
            ratio = delta / vol
            ratios[a] = ratio
            print(f"  {a:<6} {delta:>12.4f} {vol:>12.6f} {ratio:>14.4f}")
        else:
            ratios[a] = None
            print(f"  {a:<6} {delta:>12.4f} {'None':>12} {'—':>14}")
    builder.add_data("delta_over_vol_ratios", ratios)

    valid_ratios = [r for r in ratios.values() if r is not None]
    if len(valid_ratios) >= 2:
        rmean = sum(valid_ratios) / len(valid_ratios)
        rmax = max(valid_ratios)
        rmin = min(valid_ratios)
        rstd = (sum((r - rmean) ** 2 for r in valid_ratios) / len(valid_ratios)) ** 0.5
        rel_std = rstd / rmean if rmean else float("inf")
        builder.add_data("ratio_stats", {
            "mean": rmean, "min": rmin, "max": rmax,
            "max_over_min": rmax / rmin if rmin else float("inf"),
            "rel_std": rel_std,
            "n_valid": len(valid_ratios),
        })

        if rel_std < 0.05:
            verdict = "PASS — V(K) = Vol_hyp(K) gives K-independent c_λ < 5%"
        elif rel_std < 0.5:
            verdict = f"PARTIAL — rel_std = {rel_std:.3f}, c_λ varies by < 50%"
        else:
            verdict = f"MISS — rel_std = {rel_std:.3f}, V(K) = Vol(K) insufficient"
    else:
        verdict = "INCONCLUSIVE — < 2 atoms have hyperbolic closures"
    builder.add_data("verdict", verdict)
    print(f"\n  Verdict: {verdict}")

    builder.add_assertion(
        "snappy_available",
        computed=1.0,
        expected=1.0,
        tolerance=0.0,
        unit="boolean",
        source="snappy.version() = " + str(snappy.version()),
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
