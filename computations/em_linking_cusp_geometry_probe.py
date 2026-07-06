#!/usr/bin/env python3
"""
em_linking_cusp_geometry_probe.py — is the pp-Coulomb 3.213× length-scale a
CUSP-GEOMETRY ratio of the mirror links? NO (owner-authorised Subgoal-2 probe).

Context: the T−³He pp-Coulomb magnitude gap (the remaining 3.2× beyond the
derived 31%) decodes as a dimensionful length ratio
`r_strong/r_charge = 6.06 fm / 1.885 fm ≈ 3.213`
([`docs/audits/2026-06-03-em-linking-invariant.md`]). That audit named a
productive direction it could not test (SnapPy was unavailable):
"derive r_pp from the JSJ decomposition of the ³He binding link (L6a4 =
Borromean) as a cusp/horoball separation." SnapPy 3.3.2 is now available, and
the owner explicitly reversed the Subgoal-2 decline for THIS probe only
(2026-07-04). Formalize-first: pin the ONE physical ratio, do NOT scan.

RESULT — the length-scale is NOT a cusp-geometry ratio, for two reasons:

(b) STRUCTURAL EXCLUSION (invariant: S₃ symmetry). The ³He binding link
    L6a4 = Borromean rings has a fully S₃-symmetric complement — all three
    cusps are geometrically IDENTICAL (shape = 2i, meridian √2, longitude
    2√2). So every within-link cusp-separation (pp, pn, nn) is EQUAL; the
    geometry carries no proton-vs-neutron distinction. A within-³He cusp
    ratio is 1, never 3.213. The charge asymmetry that sources the Coulomb
    split cannot be a geometric feature of a link whose components are
    interchangeable.

(a) SCOPE-LIMITED NEGATIVE. The pp/nn distinction DOES live in the mirror
    pair (³He=Borromean vs ³H=8_11 are different links). But no natural
    cross-link geometric ratio matches 3.213 to the <1% discipline gate:
    longitude 3.354 (4.3% off), |shape| 3.716 (15.6% off), vol 1.131. The
    closest (longitude, 4.3%) is not a match; selecting it would be the
    PSLQ-coincidence antipattern (a CAL-4 fit).

So the audit's "cusp/horoball separation" lever is closed. The magnitude gap
stays OPEN and owner-gated (a categorical length scale the framework does not
supply). NO fit. Baked SnapPy 3.3.2 constants; `--live` re-verifies.
EXPLORATORY — asserts the honest negative, no production wiring.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402  (mandatory — witness-emitting probe)

set_compute_dps()

# Target length ratio (docs/audits/2026-06-03-em-linking-invariant.md):
#   r_strong = 6.06 fm (dHe=0.2377 MeV), r_charge = 1.885 fm (AME split 0.7638)
R_STRONG_FM = 6.06
R_CHARGE_FM = 1.885
TARGET = R_STRONG_FM / R_CHARGE_FM        # ≈ 3.2149 (audit cites 3.213)
GATE = 0.01                                # <1% = a real match; else no-fit negative

# ── Baked SnapPy 3.3.2 cusp geometry (2026-07-04; --live reproduces) ──
#   L6a4 = Borromean (³He binding link), 8_11 (³H binding link).
CUSP = {
    "L6a4": {  # 3He — fully S3-symmetric: 3 identical cusps
        "vol": 7.32772, "n_cusps": 3,
        "cusp_shapes": [complex(0, 2.0)] * 3,   # all identical => symmetry
        "meridian": 1.41421, "longitude": 2.82843,   # √2, 2√2
        "shape_mod": 2.0,
    },
    "8_11": {  # 3H — 1 cusp
        "vol": 8.28632, "n_cusps": 1,
        "cusp_shapes": [complex(4.1756, 6.1488)],
        "longitude": 9.485, "shape_mod": 7.4326,
    },
}


def run_live():
    """Recompute the cusp geometry with SnapPy (raises ImportError if absent)."""
    import snappy
    out = {}
    for nm in ("L6a4", "8_11"):
        M = snappy.Manifold(nm)
        ci = M.cusp_info()
        shapes = [complex(c["shape"]) for c in ci]
        d = {"vol": float(M.volume()), "n_cusps": M.num_cusps(),
             "cusp_shapes": shapes, "shape_mod": abs(shapes[0])}
        tr = M.cusp_translations()[0]
        d["meridian"], d["longitude"] = abs(complex(tr[0])), abs(complex(tr[1]))
        out[nm] = d
    return out


def _all_cusps_identical(shapes, tol=1e-6):
    return all(abs(s - shapes[0]) < tol for s in shapes)


def main() -> int:
    live = "--live" in sys.argv
    cusp = CUSP
    if live:
        try:
            cusp = run_live()
            print("  [--live] recomputed with SnapPy\n")
        except ImportError as e:
            print(f"  [--live] SnapPy not installed ({e}); using baked values\n")

    bor = cusp["L6a4"]
    print(f"TARGET length ratio r_strong/r_charge = {R_STRONG_FM}/{R_CHARGE_FM} = {TARGET:.4f}\n")

    # (b) within-3He structural exclusion — S3 symmetry
    sym = _all_cusps_identical(bor["cusp_shapes"])
    print("(b) within-³He (L6a4 = Borromean) — STRUCTURAL:")
    print(f"    {bor['n_cusps']} cusps, shapes {[f'{s:.3f}' for s in bor['cusp_shapes']]}")
    print(f"    all cusps identical = {sym}  =>  S₃-symmetric complement")
    print("    => every within-link cusp-separation (pp,pn,nn) is EQUAL (ratio 1.000),")
    print("       so the geometry carries NO charge asymmetry. Structurally cannot give 3.213.\n")

    # (a) cross-link ratios — scope-limited negative
    h11 = cusp["8_11"]
    ratios = {
        "longitude(8_11)/longitude(L6a4)": h11["longitude"] / bor["longitude"],
        "|shape|(8_11)/|shape|(L6a4)": h11["shape_mod"] / bor["shape_mod"],
        "vol(8_11)/vol(L6a4)": h11["vol"] / bor["vol"],
    }
    print("(a) cross-link (8_11 vs L6a4) natural ratios vs target 3.2149:")
    best = None
    for k, v in ratios.items():
        miss = abs(v - TARGET) / TARGET
        print(f"    {k:38s} = {v:.4f}   miss {miss*100:5.1f}%")
        if best is None or miss < best[1]:
            best = (k, miss, v)
    print(f"    best: {best[0]} misses by {best[1]*100:.1f}%  (gate <{GATE*100:.0f}% = match)\n")

    none_match = best[1] > GATE
    print("### Verdict")
    print("  • within-³He cusp geometry: structurally excluded (S₃ symmetry, ratio≡1).")
    print(f"  • cross-link ratios: no match (best {best[1]*100:.1f}% > {GATE*100:.0f}% gate);")
    print("    selecting the closest would be a PSLQ-coincidence fit (CAL-4).")
    print("  • The 2026-06-03 audit's 'cusp/horoball separation' lever is CLOSED.")
    print("    The pp-Coulomb magnitude length-scale stays OPEN and owner-gated.")

    wb = WitnessBuilder("em-linking-cusp-geometry-probe", engine="snappy")
    wb.set_description(
        "Owner-authorised Subgoal-2 probe: is the pp-Coulomb 3.213× length ratio "
        "a cusp-geometry ratio of the mirror links? NO. (b) ³He=L6a4=Borromean is "
        "S₃-symmetric (3 identical cusps, shape 2i) so within-link cusp separations "
        "are all equal — no charge asymmetry; structurally cannot give 3.213. "
        f"(a) cross-link 8_11-vs-Borromean ratios miss (best {best[0]} "
        f"{best[2]:.3f}, {best[1]*100:.1f}%; >{GATE*100:.0f}% gate). The audit's "
        "cusp/horoball lever is closed; magnitude stays open/owner-gated. No fit.")
    wb.add_data("target_ratio", TARGET)
    wb.add_data("borromean_symmetric", bool(sym))
    wb.add_data("cross_link_ratios", {k: float(v) for k, v in ratios.items()})
    wb.add_assertion(
        name="borromean_cusps_identical_S3_symmetric",
        computed=float(1 if sym else 0), expected=1.0, tolerance=0,
        source=("³He L6a4=Borromean has 3 geometrically identical cusps (shape 2i) — "
                "S₃-symmetric complement, so within-link cusp separations carry no "
                "pp-vs-pn distinction (structural exclusion of the within-link route)."))
    wb.add_assertion(
        name="none_match",  # honest-negative: no cusp ratio hits the <1% gate (=1 means "confirmed no match")
        computed=float(1 if none_match else 0), expected=1.0, tolerance=0,
        source=(f"no natural cross-link cusp-geometry ratio matches 3.2149 to <1% "
                f"(best {best[0]} = {best[2]:.4f}, {best[1]*100:.1f}% off); the "
                "cusp/horoball length-scale lever is closed, gap stays owner-gated."))
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
