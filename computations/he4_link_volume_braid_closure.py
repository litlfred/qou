#!/usr/bin/env python3
"""
he4_link_volume_braid_closure.py — does closing the canonical atomic braid word
give the SDP binding link (and hence the ⁴He 4-body link volume)?  NO.

Motivation: the linear-chain bond-count binding B = m_e·Σ(n−1)·Vol_n (PR #3282,
merged) reproduces ³H to −0.16% and backs out the ⁴He 4-body link volume as
Vol₄ ≈ 8.046 (`theta_mn_bondcount_linearchain.py`), flagged "falsifiable — needs
SnapPy."  All four θ_λ sibling branches left it there.  SnapPy 3.3.2 installs and
runs here (fig-8 = 2.0298832 ✓), so the block is lifted — but the test comes back
NEGATIVE for the obvious route:

  **The naive Markov closure of the canonical operator-valued atomic word does
  NOT reproduce the framework's SDP binding links at ANY A.**  The known 3-body
  links are the SDP/canonical-knot-ID outputs (8_11 for ³H, L6a4 = Borromean for
  ³He), NOT braid closures.  Closing the words instead gives non-hyperbolic links
  with the WRONG component count (a knot vs a 4-component link) — so closure
  cannot supply the ⁴He 4-body link either.

This is a scope-(a) negative (this construction, alone, fails), not a structural
exclusion: the bond-count model is not refuted — its Vol₄ ≈ 8.046 stays an
UNVERIFIED back-out, because the canonical 4-body link needs the SDP /
canonical-knot-ID (conj #604, GAP-A-1) at A=4, which needs B_5 Hoefsmit + the
Clarabel SDP backend (recipe: "not SDP-optimum-verified at A=4; solver scope
A≤3").  The provisional doubly-magic 2·Vol(Borromean) = 14.655 DISAGREES with the
8.046 back-out (~1.8×) — a real, unresolved A=4 tension recorded, not resolved.

Baked SnapPy results (no runtime SnapPy needed, per binding_link_volumes.py
convention); re-verify with `--live` if snappy/spherogram are installed.
EXPLORATORY — no production wiring, no fitted constant.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402  (mandatory — witness-emitting probe)
from knot_volumes import VOL_8_11_MPF, VOL_BORROMEAN_MPF  # noqa: E402

set_compute_dps()

# ── The framework's SDP binding links (binding-link-volumes.witness.json) ──
#   isotope → (link, hyperbolic components, hyperbolic volume)
BINDING_LINK = {
    "3H":  {"link": "8_11",           "components": 1, "vol": float(VOL_8_11_MPF)},      # a KNOT
    "3He": {"link": "L6a4=Borromean", "components": 3, "vol": float(VOL_BORROMEAN_MPF)}, # 3-comp link
}
# per-nucleon braid 𝓑₃ = Borromean rings (3 components, 8G)
NUCLEON_BORROMEAN = {"components": 3, "vol": float(VOL_BORROMEAN_MPF)}
BONDCOUNT_VOL4_BACKOUT = 8.046        # theta_mn_bondcount_linearchain.py (m_e·3·Vol₄ = residual)
DOUBLY_MAGIC_VOL4 = 2 * float(VOL_BORROMEAN_MPF)   # 14.655 provisional (binding_a3plus_*)

# ── Baked SnapPy 3.3.2 closure results (2026-07-04; avg-interface → +σ) ──
#   Markov closure of atom_canonical_crossings(Z,N); simplify('global') + 12
#   randomizations.  geometric=False ⇒ SnapPy finds no positively-oriented
#   (hyperbolic) triangulation ⇒ non-hyperbolic (Vol → 0).  Provenance: run via
#   `--live` to reproduce.  Every mode (avg → +σ / −σ / drop) gives the same
#   non-geometric outcome; +σ tabulated.
CLOSURE = {
    "proton": {"components": 2, "geometric": False, "geometric_volume": 0.0, "crossings": 9},
    "neutron": {"components": 2, "geometric": False, "geometric_volume": 0.0, "crossings": 11},
    "3H":  {"components": 4, "geometric": False, "geometric_volume": 0.0, "crossings": 31},
    "3He": {"components": 4, "geometric": False, "geometric_volume": 0.0, "crossings": 29},
    "4He": {"components": 5, "geometric": False, "geometric_volume": 0.0, "crossings": 40},
}


def run_live():
    """Recompute the closure results with SnapPy (if installed). Returns the
    same dict shape as CLOSURE, or raises with a clear message."""
    from canonical_braid_crossings import atom_canonical_crossings
    import spherogram  # noqa: F401
    import snappy

    m = snappy.Manifold("4_1")
    assert abs(m.volume() - 2.0298832128) < 1e-6, "SnapPy fig-8 sanity failed"

    def close(Z, N, inter):
        cross = atom_canonical_crossings(Z, N, include_inter=inter)
        w = []
        for g, ct in cross:
            gg = g + 1
            w.append(gg if ct in ("sigma", "averaged") else -gg)  # avg → +σ
        L = spherogram.Link(braid_closure=w)
        L.simplify("global")
        M = L.exterior()
        best, geo = 0.0, False
        for i in range(12):
            try:
                if i:
                    M.randomize()
                if "positively" in M.solution_type():
                    geo = True
                    best = max(best, float(M.volume()))
            except Exception:
                pass
        return {"components": len(L.link_components), "geometric": geo,
                "geometric_volume": round(best, 6), "crossings": len(L.crossings)}

    spec = {"proton": (1, 0, False), "neutron": (0, 1, False),
            "3H": (1, 2, True), "3He": (2, 1, True), "4He": (2, 2, True)}
    return {k: close(*v) for k, v in spec.items()}


def main() -> int:
    live = "--live" in sys.argv
    closure = CLOSURE
    if live:
        # Probe ONLY the optional third-party deps here; if they're missing we
        # fall back to baked values. run_live() then does the repo imports +
        # SnapPy work, and any error there (repo bug, assertion, runtime) is a
        # real failure that must surface — not be masked as "SnapPy unavailable".
        try:
            import snappy  # noqa: F401
            import spherogram  # noqa: F401
        except ImportError as e:
            print(f"  [--live] SnapPy/spherogram not installed ({e}); using baked values\n")
        else:
            closure = run_live()
            print("  [--live] recomputed with SnapPy\n")

    print("Canonical atomic-braid closures vs the SDP binding links")
    print("=" * 64)
    for iso in ("proton", "neutron", "3H", "3He", "4He"):
        c = closure[iso]
        bl = BINDING_LINK.get(iso) or (NUCLEON_BORROMEAN if iso in ("proton", "neutron") else None)
        tgt = f"  vs {bl['link'] if 'link' in (bl or {}) else '𝓑₃'} " \
              f"({bl['components']}-comp, Vol={bl['vol']:.3f})" if bl else "  vs 4-body link (unknown)"
        print(f"  {iso:8s} closure: {c['components']}-comp, "
              f"{'geometric' if c['geometric'] else 'NON-hyperbolic (Vol→0)'}, "
              f"{c['crossings']} crossings{tgt}")
    print()
    print("Finding — braid closure is NOT the binding-link assignment rule:")
    print(f"  • ³H closure is {closure['3H']['components']}-component, but 8_11 is a "
          "1-component KNOT ⇒ wrong link type (not a triangulation artifact).")
    print(f"  • ³He closure is {closure['3He']['components']}-component, but "
          "L6a4=Borromean is 3-component ⇒ wrong link type.")
    print("  • single proton/neutron closures are non-hyperbolic 2-comp links, "
          "not 𝓑₃=Borromean (3-comp, 7.328).")
    print("  ⇒ the SDP binding links come from the canonical-knot-ID (conj #604), "
          "NOT Markov closure of the operator-valued word.")
    print()
    print("⁴He 4-body link — the A=4 gate (scope-a, no fit):")
    print(f"  • closure route DEAD (5-comp non-hyperbolic, ≠ any binding link).")
    print(f"  • bond-count back-out Vol₄ ≈ {BONDCOUNT_VOL4_BACKOUT} stays UNVERIFIED — needs the")
    print(f"    SDP/canonical-knot-ID at A=4 (B_5 Hoefsmit + Clarabel; solver scope A≤3).")
    print(f"  • provisional doubly-magic 2·Vol(𝓑₃) = {DOUBLY_MAGIC_VOL4:.3f} disagrees with "
          f"{BONDCOUNT_VOL4_BACKOUT} (~{DOUBLY_MAGIC_VOL4/BONDCOUNT_VOL4_BACKOUT:.2f}×) — unresolved.")

    wb = WitnessBuilder("he4-link-volume-braid-closure", engine="snappy+mpmath")
    wb.set_description(
        "Naive Markov closure of the canonical operator-valued atomic braid word "
        "does NOT reproduce the SDP binding links at any A (³H closure is "
        "4-component vs 8_11's 1; ³He closure 4-comp vs Borromean's 3; all "
        "non-hyperbolic). So closure cannot supply the ⁴He 4-body link volume; "
        "Vol₄ ≈ 8.046 stays an unverified bond-count back-out gated on the "
        "SDP/canonical-knot-ID (conj #604) at A=4. SnapPy 3.3.2 verified "
        "(fig-8 = 2.0298832). Scope-(a) negative, no fit.")
    wb.add_data("closure_results", closure)
    wb.add_data("binding_links", BINDING_LINK)
    wb.add_data("he4_vol4", {"bondcount_backout": BONDCOUNT_VOL4_BACKOUT,
                             "doubly_magic_provisional": DOUBLY_MAGIC_VOL4,
                             "disagreement_ratio": DOUBLY_MAGIC_VOL4 / BONDCOUNT_VOL4_BACKOUT})
    # Real invariants (regression guards), not tautologies:
    wb.add_assertion(
        name="3H_closure_component_count_ne_8_11",
        computed=float(closure["3H"]["components"]), expected=4.0, tolerance=0,
        source=("³H canonical braid closure has 4 components; 8_11 is a 1-component "
                "knot — wrong link type, so closure ≠ the SDP binding link."))
    wb.add_assertion(
        name="3He_closure_component_count_ne_borromean",
        computed=float(closure["3He"]["components"]), expected=4.0, tolerance=0,
        source=("³He canonical braid closure has 4 components; L6a4=Borromean is "
                "3-component — wrong link type."))
    wb.add_assertion(
        name="3H_closure_non_hyperbolic",
        computed=float(closure["3H"]["geometric_volume"]), expected=0.0, tolerance=1e-2,
        source=("³H closure admits no geometric (positively-oriented) triangulation "
                "⇒ non-hyperbolic (Vol→0), vs the hyperbolic 8_11 (Vol=8.286)."))
    out = wb.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
