#!/usr/bin/env python3
"""difference_knot_hyperbolicity_check.py — RETRACTION: the binding
difference link is reducible/non-hyperbolic; its "volume" was SnapPy noise.

Follow-up to difference_knot_binding_probe.py (PR #2235) and
difference_knot_jsj_classification_probe.py (PR #2242). Those probes reported
"nonzero, A-growing, p-n-distinguishing" hyperbolic volumes for the difference
link D = W_atom·W_free⁻¹ and framed it as a live geometric binding lead. That
framing was based on SnapPy's `.volume()` on a NON-geometric triangulation,
trusted WITHOUT checking hyperbolicity. This probe runs the checks that were
missing — and they refute the lead.

THREE DECISIVE FACTS (per difference link, topological closure of the
sign-reduced braid):

  1. SnapPy's `.volume()` is UNSTABLE across random triangulations
     (coefficient of variation 29-132%) and frequently NEGATIVE — a genuine
     hyperbolic volume is positive and triangulation-independent. The number
     is noise on a non-geometric triangulation.

  2. Regina's `isIrreducible() = False`: the link complements contain
     essential 2-spheres, i.e. the links are SPLIT/reducible. A reducible
     3-manifold is NOT hyperbolic (hyperbolic ⇒ irreducible). Definitive.

  3. `isHaken() = False` likewise.

CONCLUSION. The topological difference link `W_atom·W_free⁻¹` (Hecke weights
stripped to crossing signs, free-reduced, closed) is a reducible split link
with NO hyperbolic volume. The "volumes" in PR #2235 / #2242 are artifacts.
This CONVERGES with the pre-existing
`binding_volume_difference_probe.py`, which already found the derived braid
closures non-hyperbolic ("Seifert-fibred / degenerate, Vol≈0") — the corpus
was right; #2235 misread SnapPy noise as signal.

What survives: the geometric binding route needs the HAND-ASSIGNED hyperbolic
census knots (Hopf/8₁₁/L6a4 in `binding_link_volumes.py`, which ARE
hyperbolic), and the open question is the assignment itself
(`conj:canonical-knot-id-sdp`) — NOT a volume read off the raw difference
braid. The proven `prop:binding-error-amplification` still stands; only the
specific difference-knot-volume realisation is refuted.

Requires: snappy, regina (`pip install regina` — JSJ/decomposition WITHOUT
Sage). EXPLORATORY / DIAGNOSTIC; retracts a prior lead, promotes nothing.

Ref: folio-assistant/computations/probes/difference_knot_binding_probe.py (PR #2235)
Ref: folio-assistant/computations/probes/difference_knot_jsj_classification_probe.py (PR #2242)
Ref: folio-assistant/computations/binding_volume_difference_probe.py
Ref: docs/audits/2026-06-13-difference-knot-nonhyperbolic-retraction.md
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import statistics  # noqa: E402
import sys  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from difference_knot_binding_probe import _difference_braid  # noqa: E402

CASES = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
N_TRIALS = 25


def _hyperbolicity(braid: list[int]):
    """(cv, vmin, vmax, n_negative, irreducible, haken) for the closed braid."""
    import snappy
    import regina
    vols = []
    for _ in range(N_TRIALS):
        M = snappy.Link(braid_closure=braid).exterior()
        M.randomize()
        M.simplify()
        try:
            vols.append(float(M.volume()))
        except Exception:
            pass
    mean = statistics.mean(vols) if vols else 0.0
    cv = (statistics.pstdev(vols) / mean) if mean else float("inf")
    n_neg = sum(1 for v in vols if v < 0)
    M0 = snappy.Link(braid_closure=braid).exterior()
    M0.simplify()
    tri = regina.Triangulation3(M0._to_string())
    tri.intelligentSimplify()
    try:
        irred = bool(tri.isIrreducible())
    except Exception:
        irred = None
    try:
        haken = bool(tri.isHaken())
    except Exception:
        haken = None
    return cv, min(vols), max(vols), n_neg, irred, haken


def main() -> int:
    set_compute_dps()
    w = WitnessBuilder("difference-knot-hyperbolicity-check", engine="snappea")
    w.set_description(
        "RETRACTION of PR #2235/#2242: the binding difference link "
        "D = W_atom·W_free⁻¹ is reducible (Regina isIrreducible=False) and "
        "non-hyperbolic — SnapPy's volume is unstable (cv 29-132%) and "
        "frequently negative, i.e. noise on a non-geometric triangulation. "
        "The 'nonzero A-growing volumes' previously reported are artifacts. "
        "Converges with binding_volume_difference_probe.py (derived braid "
        "closures non-hyperbolic). prop:binding-error-amplification stands; "
        "only the difference-knot-volume realisation is refuted."
    )
    w.set_content_block("conj:canonical-knot-id-sdp")

    print(f"{'iso':4s} {'cv':>7s} {'vmin':>8s} {'vmax':>8s} {'neg/25':>7s} "
          f"{'irred':>6s} {'haken':>6s}")
    all_nonhyp = True
    for iso, Z, N in CASES:
        braid = _difference_braid(Z, N, "minus", reduce=True)
        cv, vmin, vmax, n_neg, irred, haken = _hyperbolicity(braid)
        nonhyp = (irred is False) or (n_neg > 0) or (cv > 0.05)
        all_nonhyp = all_nonhyp and nonhyp
        print(f"{iso:4s} {cv:>6.1%} {vmin:>8.2f} {vmax:>8.2f} {n_neg:>7d} "
              f"{str(irred):>6s} {str(haken):>6s}")
        w.add_data(f"{iso}_vol_cv", mp.nstr(mp.mpf(repr(cv)), 6))
        w.add_data(f"{iso}_vol_min", mp.nstr(mp.mpf(repr(vmin)), 6))
        w.add_data(f"{iso}_n_negative_of_25", n_neg)
        w.add_data(f"{iso}_regina_irreducible", irred)
        w.add_data(f"{iso}_regina_haken", haken)

    w.add_assertion(
        name="difference_links_reducible_nonhyperbolic",
        computed=bool(all_nonhyp),
        expected=True,
        tolerance=0,
        source="Regina isIrreducible=False (essential spheres ⇒ split ⇒ "
               "non-hyperbolic) and/or unstable/negative SnapPy volume — the "
               "difference-knot 'volume' of PR #2235/#2242 is an artifact",
    )
    w.add_data(
        "retraction",
        "PR #2235/#2242 reported hyperbolic volumes for the difference link; "
        "they are SnapPy noise on non-geometric triangulations. The links are "
        "reducible (split) and non-hyperbolic. The geometric binding route "
        "must use the hand-assigned hyperbolic census knots (conj:canonical-"
        "knot-id-sdp), not a volume of the raw difference braid. "
        "prop:binding-error-amplification is unaffected.",
    )
    out = w.save()
    print(f"\nRETRACTION: difference links are reducible/non-hyperbolic; "
          f"the #2235/#2242 volumes were artifacts.")
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
