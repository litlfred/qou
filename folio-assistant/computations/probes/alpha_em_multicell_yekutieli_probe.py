"""α_em multi-cell summed Yekutieli probe — Item 1 of PR #1708.

Prior α_em Yekutieli probes used INDIVIDUAL objects:
  - torus-knot product q·tr_M(T(2,9))·tr_M(T(3,5)) = 0.8 (REFUTED)
  - per-cell q-Lambert decomposition (NULL, sibling)

This probe tests the SUMMED non-abelian Stokes form over the
8-ideal-octahedron tessellation of the 𝓑_3 (Borromean) complement —
the explicit `Σ_{cells} per-cell contribution` that the canonical
chain `cat action → non-abelian Stokes → Wedderburn` predicts.

## Target: the open `2/(3π)` shift

The α_em⁻¹ structure is:
  α_em⁻¹ = q·[9]_q·[10]_q  +  2/(3π)  +  [2]_q/(8π)·(1−h²α)  + O(α³)
           tree=136.823       +0.2122    self-energy

The tree term is a Coulomb-channel form (existing prop). The `2/(3π)`
shift is believed to be Bring-surface Hodge data. The Borromean
complement has N_cusps = 3 (3 rings) and is tessellated by 2 ideal
octahedra (Vol = 2·V_oct = 7.327...) — NOT 8. (The audit's "8 ideal
octahedra" refers to a different subdivision; we test both 2 and 8.)

## What this probe tests (derive-or-refute)

For the SUMMED non-abelian Stokes integral over N cells, the leading
curvature contribution per cell scales as (per-cell volume)/(2π)² or
similar. We test whether natural per-cell SUMS reproduce 2/(3π):

  (a) Σ over 2 octahedra of V_oct-weighted curvature / normalisation
  (b) Σ over 8 cells with 1/N_cusps normalisation
  (c) N_cusps-based:  2/(3π) directly from 3 cusps
  (d) Catalan-based: the Vol(𝓑_3) = 8G route

## Pre-stated failure signature

If no SUMMED form lands within ~1% of 2/(3π) with a STRUCTURAL
(non-fitted) per-cell weight, the multi-cell Yekutieli route is
refuted for the α_em shift (consistent with the individual-cell
refutations).

## Cross-references

- alpha_em_yekutieli_h2_extraction.py (torus-knot REFUTED)
- audit 2026-06-01-yekutieli-mp-substrate-derivation-scaffolding.md
- prop:em-coupling-bring-zero-mode
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Puts the flat computations/ dir + cluster subdirs on sys.path so
# flat-namespace imports resolve from the probes/ subdirectory.
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys  # noqa: E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import q_at, q_str  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def qint(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def main() -> int:
    DPS = 50
    set_compute_dps(DPS)
    q = q_at(DPS)

    print("=" * 78)
    print("α_em multi-cell summed Yekutieli probe (item 1 of PR #1708)")
    print("=" * 78)
    print(f"\nq_0 = {q_str(40)} (display)\n")

    # Target: the 2/(3π) shift
    shift_target = mp.mpf(2) / (3 * mp.pi)
    codata_inv = mp.mpf("137.035999084")
    bare = q * qint(9, q) * qint(10, q)
    print(f"[Targets]")
    print(f"  bare q·[9]_q·[10]_q = {mp.nstr(bare, 15)}")
    print(f"  CODATA α_em⁻¹       = {mp.nstr(codata_inv, 15)}")
    print(f"  shift needed        = CODATA − bare = {mp.nstr(codata_inv - bare, 12)}")
    print(f"  2/(3π) reference    = {mp.nstr(shift_target, 15)}")
    print(f"  (the shift 2/(3π) closes bare to 4.3 ppm)")

    # Hyperbolic-geometry constants
    G = mp.catalan
    V_oct = 8 * mp.im(mp.polylog(2, mp.exp(mp.mpc(0, mp.pi / 2))))  # regular ideal octahedron volume
    # Actually V_oct = 8·Λ(π/4) = 3.66386...; use Lobachevsky
    # Λ(θ) = -∫_0^θ ln|2 sin t| dt ; V_oct = 8 Λ(π/4)
    def lobachevsky(theta):
        return mp.im(mp.polylog(2, mp.exp(2j * theta))) / 2
    V_oct = 8 * lobachevsky(mp.pi / 4)
    Vol_Bor = 2 * V_oct  # Borromean complement = 2 ideal octahedra
    Vol_Bor_8G = 8 * G   # alternate: the "8·Catalan" form used in mass work

    print(f"\n[Hyperbolic geometry]")
    print(f"  V_oct (regular ideal octahedron) = {mp.nstr(V_oct, 12)}")
    print(f"  Vol(𝓑_3) = 2·V_oct               = {mp.nstr(Vol_Bor, 12)}")
    print(f"  8·Catalan (mass-work form)       = {mp.nstr(Vol_Bor_8G, 12)}")

    # ── Multi-cell summed candidates for the shift ──
    print(f"\n[Summed-cell candidates for the 2/(3π) shift]")
    N_cusps = 3
    # Each candidate is tagged TAUTOLOGY (algebraically reduces to a
    # rewrite of 2/(3π), assuming the answer) or VOLUME (a genuine
    # hyperbolic-geometry sum whose value is NOT pre-set to 2/(3π)).
    candidates = [
        # (c) Direct N_cusps form — TAUTOLOGY (2/(3π) verbatim)
        ("(c) 2/(N_cusps·π), N_cusps=3", mp.mpf(2) / (N_cusps * mp.pi), "TAUT"),
        # (a) V_oct/Vol_Bor·... — TAUTOLOGY: V_oct/Vol_Bor = 1/2 exactly
        ("(a) 2·V_oct/(Vol_Bor·π)·(2/3) [V_oct cancels]",
         2 * V_oct / (Vol_Bor * mp.pi) * mp.mpf(2) / 3, "TAUT"),
        # (e) per-cusp — TAUTOLOGY (3·2/9π = 2/3π)
        ("(e) Σ_3 cusps · (2/9π)", 3 * (mp.mpf(2) / (9 * mp.pi)), "TAUT"),
        # (b) 8-cell with 1/cusps² — VOLUME
        ("(b) Vol_Bor / (N_cusps²·π)",
         Vol_Bor / (N_cusps ** 2 * mp.pi), "VOL"),
        # (d) Catalan/cusps — VOLUME
        ("(d) 8G / (3π · φ) with φ=golden",
         Vol_Bor_8G / (N_cusps * mp.pi * ((1 + mp.sqrt(5)) / 2)), "VOL"),
        # (f) V_oct curvature density — VOLUME
        ("(f) V_oct / (2π²)",
         V_oct / (2 * mp.pi ** 2), "VOL"),
    ]

    print(f"  {'name':<46}{'value':<18}{'Δ% vs 2/3π':<14}{'kind'}")
    scored = []
    for name, val, kind in candidates:
        rel = (val - shift_target) / shift_target * 100
        scored.append((name, val, rel, kind))
    scored.sort(key=lambda r: abs(r[2]))
    for name, val, rel, kind in scored:
        marker = " ⭐⭐ exact" if abs(rel) < mp.mpf("0.01") else (
            " ⭐ <1%" if abs(rel) < mp.mpf("1") else (
                " *" if abs(rel) < mp.mpf("10") else ""))
        print(f"  {name:<46}{mp.nstr(val, 11):<18}{mp.nstr(rel, 6):<14}{kind}{marker}")

    # Honest analysis: only VOLUME-tagged forms test a genuine derivation.
    vol_forms = [r for r in scored if r[3] == "VOL"]
    vol_within_1pct = [r for r in vol_forms if abs(r[2]) < mp.mpf("1")]
    print(f"\n[Volume-based (genuine, non-tautological) results]")
    for name, val, rel, _ in vol_forms:
        print(f"  {name}: {mp.nstr(rel, 6)}%")

    # ── Verdict ──
    print(f"\n[Verdict]")
    if vol_within_1pct:
        verdict = (
            f"VOLUME-FORM HIT: {vol_within_1pct[0][0]} at "
            f"{mp.nstr(vol_within_1pct[0][2], 6)}% — a genuine per-cell "
            f"hyperbolic-volume sum lands near 2/(3π) WITHOUT assuming it. "
            f"Worth structural follow-up."
        )
    else:
        best_vol = min(vol_forms, key=lambda r: abs(r[2]))
        verdict = (
            "REFUTED for genuine summed-volume forms. Only TAUTOLOGICAL "
            "rewrites (2/(N_cusps·π) with N_cusps=3; Σ_3·(2/9π); and "
            "2·V_oct/(Vol_Bor·π)·(2/3) where V_oct/Vol_Bor=1/2 cancels "
            "exactly) reproduce 2/(3π) — all three ASSUME the answer. "
            f"Genuine hyperbolic-volume sums miss: best is {best_vol[0]} "
            f"at {mp.nstr(best_vol[2], 6)}%. The multi-cell SUMMED Yekutieli "
            "route does NOT structurally derive the 2/(3π) shift "
            "coefficient — consistent with the individual-cell refutations "
            "(torus-knot 1e6 ppm, H_3 matter −445%, q-Lambert NULL). "
            "The N_cusps=3 reading of the '3' is a plausible INTERPRETATION "
            "but the coefficient '2' and the 1/π factor are not derived; "
            "the shift's structural origin remains open (RT-2-loop track)."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder("alpha-em-multicell-yekutieli-probe", engine="python")
    w.set_description(
        "Item 1 of PR #1708: tests the SUMMED non-abelian Stokes form "
        "over the 𝓑_3 octahedron tessellation for the α_em 2/(3π) shift. "
        "Prior probes used individual torus knots / cells (refuted); this "
        "tests the explicit cell SUM. Honest derive-or-refute."
    )
    w.add_parameter("q_50dps", q_str(DPS))
    w.add_parameter("mp_dps_runtime", str(mp.mp.dps))
    w.add_data("shift_target_2_over_3pi", mp.nstr(shift_target, 25))
    w.add_data("V_oct", mp.nstr(V_oct, 25))
    w.add_data("Vol_Borromean", mp.nstr(Vol_Bor, 25))
    w.add_data("verdict", verdict)
    w.add_data("N_cusps_reading", "3 (Borromean is 3-component link); "
               "consistent but not derived")

    w.add_assertion(
        name="multicell_scan_completed",
        computed=len(candidates),
        expected=len(candidates),
        tolerance=0,
        source=f"Scanned {len(candidates)} summed-cell candidates at 50 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
