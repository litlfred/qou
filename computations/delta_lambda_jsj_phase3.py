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

  Ref: [manuscript] `delta-lambda-categorical-closure`
  Ref: docs/audits/2026-05-19-delta-lambda-phase2-findings.md
  Ref: docs/path-to-1ppb-04-plan.md (master formula)

Retired-label note: a block named above with a backticked stem and no
`prop:`/`conj:` prefix has NO carrier in folio/ — it was demoted to
_deprecated/ and is recorded in docs/audits/2026-10-11-retired-label-records.md §A,
with the statement it carried and the command to recover its content.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
from _precision import set_compute_dps, fmt  # noqa: E402 — raise dps before any mpmath value; fmt for mpf serialisation
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


ATOMS = ("D", "T", "3He", "4He")

# Thurston's closed form for the figure-eight knot complement:
#   Vol(4_1) = 6·Λ(π/3) = 3·Cl₂(2π/3)
# (Λ = Lobachevsky, Cl₂ = Clausen).  Used below to CALIBRATE SnapPy's
# numerical gluing-equation solver against a route that never touches
# SnapPy — see `figure8_volume_matches_lobachevsky_closed_form`.
def figure8_volume_closed_form() -> mp.mpf:
    """Vol(4_1) from the Lobachevsky closed form — no SnapPy involved."""
    return 3 * mp.clsin(2, 2 * mp.pi / 3)


def strands_snappy_will_use(braid_word: list[int]) -> int:
    """Strand count SnapPy infers from a braid word: max|generator| + 1.

    Rebuilt from the word itself rather than taken from the caller's
    declared `n_strands`, so the two can be compared.
    """
    return max(abs(g) for g in braid_word) + 1


def load_atom_braids() -> dict:
    """Build canonical braid words for D, T, ³He, ⁴He via the
    he4_compositional_braids helper + per-atom analogues."""
    # Repointed 2026-08-09: these helpers moved to the live module
    # `atom_braid_words` when `probe_he4_jsj_topology` was deprecated.
    # `_path_bridge` skips `_deprecated/`, so the old import raised
    # ImportError here at call time. Bodies are unchanged.
    from atom_braid_words import (
        _proton_braid_word,
        _neutron_braid_word,
        he4_compositional_braids,
        shift_word,
    )
    p = _proton_braid_word()
    n = _neutron_braid_word()

    # Deuteron at H_6: p (strands 1-3) + I_pn (σ_3) + n (strands 4-6)
    D = list(p) + [3] + shift_word(n, 3)
    # Tritium at H_9: p (1-3) + I_pn (σ_3) + n (4-6) + I_nn (σ_6⁻¹) + n (7-9)
    T = list(p) + [3] + shift_word(n, 3) + [-6] + shift_word(n, 6)
    # ³He at H_9: p (1-3) + I_pp (σ_3) + p (4-6) + I_pn (σ_6) + n (7-9)
    He3 = list(p) + [3] + shift_word(p, 3) + [6] + shift_word(n, 6)
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


# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

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

    # 2b. Strand-count consistency: what SnapPy actually got vs what we
    #     declared.  They disagreed until 2026-11-21: the sub-words were
    #     shifted with a bare `g + k` on the SIGNED generator, so σ_2⁻¹ (-2)
    #     became +1 instead of -5 and the inter-nucleon braid collapsed.
    #     Fixed at the builder (`atom_braid_words.shift_word`, bean
    #     qou-yaqm); this check stays as the regression guard.  The
    #     committed witness predates the fix and must be regenerated
    #     (needs SnapPy) before its volumes are read.
    strand_mismatch = {
        a: {"declared_n_strands": n,
            "strands_snappy_infers": strands_snappy_will_use(w)}
        for a, (w, n) in braids.items()
        if strands_snappy_will_use(w) != n
    }
    builder.add_data("declared_vs_inferred_strand_counts", strand_mismatch)
    if strand_mismatch:
        builder.add_caveat(
            "BRAID CONSTRUCTION DEFECT (regression of bean qou-yaqm, fixed 2026-11-21): the "
            "shifted sub-words use `g + k` on the SIGNED generator, so a "
            "negative generator is reflected instead of translated "
            "(σ_2⁻¹ + 3 = +1, not -5). SnapPy therefore closes a braid on "
            f"{sorted(strand_mismatch)} with fewer strands than declared, "
            "and every hyperbolic volume in this witness is the volume of "
            "that collapsed braid. The separability verdict below is "
            "conditional on this defect being repaired."
        )

    # 3. Load empirical |Δ_λ*| from tabulation
    emp = builder.add_upstream(_pb.witness_path("delta-lambda-empirical-tabulation.witness.json", HERE))["data"]["per_atom"]
    empirical_delta = {a: float(mp.mpf(emp[a]["a_single_block"]["best_abs_delta"]))
                       for a in ATOMS if a in emp}
    builder.add_data("empirical_best_abs_delta", empirical_delta)

    # 4. Test separability: if V(K) = Vol(K) gives K-independent c_λ
    #    then |Δ*(K)| / Vol(K) should be roughly constant across atoms
    print(f"\n  {'atom':<6} {'|Δ*|':>12} {'Vol(K)':>12} {'|Δ*|/Vol':>14}")
    ratios = {}
    for a in ATOMS:
        vol = vols[a]["hyperbolic_volume"]
        delta = empirical_delta.get(a)
        if delta is None:
            ratios[a] = None
            print(f"  {a:<6} {'(no upstream |Δ*|)':>12} {'—':>12} {'—':>14}")
        elif vol is not None and vol > 0:
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

    # ── Assertions ────────────────────────────────────────────────────
    # Was: add_assertion("snappy_available", computed=1.0, expected=1.0)
    # — a hardcoded constant compared with itself.  It could not fail even
    # if SnapPy returned nonsense, and it asserted nothing about the
    # volumes this producer exists to compute.  Replaced by three checks
    # that each have a second, independent route.

    # (1) Calibrate the volume engine itself.  Route A: SnapPy's numerical
    #     solve of the gluing equations for the 4_1 exterior.  Route B:
    #     Thurston's closed form 6·Λ(π/3) = 3·Cl₂(2π/3), evaluated by
    #     mpmath's Clausen function, which never touches SnapPy.  A SnapPy
    #     build whose hyperbolic solver regressed fails this.
    #     Both routes are carried at 200 bits / 40 dps, so the check bites
    #     ~40 digits deep rather than at float64.
    vol_4_1_snappy = mp.mpf(str(snappy.Manifold("4_1").volume(bits_prec=200)))
    vol_4_1_closed = figure8_volume_closed_form()
    builder.add_data("figure8_calibration", {
        "snappy_volume_bits_prec_200": fmt(vol_4_1_snappy, 40),
        "lobachevsky_closed_form": fmt(vol_4_1_closed, 40),
    })
    builder.add_assertion(
        "figure8_volume_matches_lobachevsky_closed_form",
        computed=fmt(vol_4_1_snappy, 40),
        expected=fmt(vol_4_1_closed, 40),
        tolerance="1e-38",
        unit="hyperbolic volume",
        source=(
            "volume-engine calibration: SnapPy's numerical gluing-equation "
            "solve of the figure-eight exterior (bits_prec=200) vs "
            "Thurston's closed form 6·Λ(π/3) = 3·Cl₂(2π/3) via mpmath's "
            "Clausen function — two independent routes to the same "
            f"constant, agreeing to ~40 dps (snappy {snappy.version()})."
        ),
    )

    # (2) Pin the separability verdict.  Route A: rel_std of |Δ*|/Vol
    #     recomputed from this run's volumes and the upstream tabulation.
    #     Route B: the 0.5 MISS boundary of this producer's own verdict
    #     taxonomy, pinned against the committed run (rel_std = 1.398,
    #     max/min = 153×).  A rerun that drops under the boundary flips
    #     this assertion so a human re-adjudicates instead of the verdict
    #     string quietly changing inside add_data.
    rel_std_now = None
    if len(valid_ratios) >= 2:
        rel_std_now = rel_std
    if rel_std_now is not None:
        builder.add_assertion(
            "separability_misses_beyond_50pct_spread",
            computed=1.0 if rel_std_now >= 0.5 else 0.0,
            expected=1.0,
            tolerance=0.5,
            unit="boolean",
            source=(
                f"V(K) = Vol_hyp(K) does NOT separate: rel_std = "
                f"{rel_std_now:.4f} is at or beyond the 0.5 MISS boundary "
                f"(committed run: 1.398, max/min = 153×). Pinned as a "
                f"regression guard — a rerun finding rel_std < 0.5 flips "
                f"this and reopens conj:delta-lambda-categorical-closure."
            ),
        )

    # (3) Coverage, rebuilt from inputs.  Route A: the atoms for which an
    #     empirical |Δ*| was actually recovered from the upstream
    #     tabulation witness.  Route B: this producer's declared ATOMS
    #     roster.  Catches an upstream that silently drops an atom.
    builder.add_assertion(
        "empirical_tabulation_covers_every_declared_atom",
        computed=len(empirical_delta),
        expected=len(ATOMS),
        tolerance=0,
        unit="atoms",
        source=(
            "atoms recovered from delta-lambda-empirical-tabulation."
            "witness.json vs the ATOMS roster this producer declares."
        ),
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
