"""SW-residue hyperbolicity gate (workplan Lemma L4).

Step-9 binding-closure workplan
([`docs/workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md`]):
each body-order term of the binding series is a Seiberg–Witten period =
a residue sum over the *hyperbolic* link-components. Non-hyperbolic
components (torus / Seifert-fibered knots and links) carry zero
hyperbolic volume — the Bloch–Wigner dilogarithm `D(z)=0` there — so they
contribute nothing to the volume channel. This module is the explicit
predicate the gate needs; it was previously absent (the framework cached
hyperbolic volumes but had no per-knot hyperbolicity flag).

Public API
----------
    is_hyperbolic(name) -> bool
        True for hyperbolic canonical knots/links, False for the
        torus/Seifert family. Raises ValueError on an unclassified name
        (we do NOT guess — mis-gating would corrupt the binding series).
    vol_component(name, dps) -> mpf
        The L4 gate: Vol(name) from the canonical `knot_volumes` source if
        hyperbolic, else mpf(0).

The hyperbolic set is exactly the canonical-volume registry of
`knot_volumes._VOL_DISPATCH`; the non-hyperbolic set lists the torus
knots/links the framework uses (unknot, trefoil 3_1 = T(2,3), 5_1 =
T(2,5), and the electroweak T(2,k) triplet W/Z/H), all Vol = 0.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_HERE = _Path(__file__).resolve().parent
_sys.path.insert(0, str(_HERE.parent))  # computations/ — home of _path_bridge
_sys.path.insert(0, str(_HERE))         # substrate/ — knot_volumes, _precision, witness_base
import _path_bridge as _bridge  # noqa: E402, F401  (bridges all cluster subdirs)

import mpmath as mp  # noqa: E402

import knot_volumes as kv  # noqa: E402
from _precision import COMPUTE_DPS  # noqa: E402

# Hyperbolic canonical knots/links — the volume registry is, by
# construction, the set of hyperbolic complements the pipeline uses.
HYPERBOLIC: frozenset[str] = frozenset(kv._VOL_DISPATCH.keys())

# Non-hyperbolic (torus / Seifert-fibered): Vol = 0, D(z) = 0.
# Trefoil 3_1 = T(2,3); 5_1 = T(2,5); EW triplet W± = T(2,4), Z = T(2,6),
# H = T(2,8) (Seifert-fibered, Vol = 0 — see cheat-sheet §5 item 5).
NON_HYPERBOLIC: frozenset[str] = frozenset({
    "unknot", "0_1",
    "3_1", "trefoil", "T(2,3)",
    "5_1", "T(2,5)",
    "T(2,4)", "T(2,6)", "T(2,8)",
})


def is_hyperbolic(name: str) -> bool:
    """True iff `name` is a hyperbolic knot/link. Raises ValueError for an
    unclassified name (we refuse to guess — a wrong gate corrupts the
    binding series)."""
    if name in HYPERBOLIC:
        return True
    if name in NON_HYPERBOLIC:
        return False
    raise ValueError(
        f"hyperbolicity of {name!r} is unclassified; add it to "
        f"HYPERBOLIC (with a knot_volumes entry) or NON_HYPERBOLIC."
    )


def vol_component(name: str, dps: int | None = None) -> mp.mpf:
    """The L4 gate: the hyperbolic volume of `name` if it is hyperbolic,
    else mpf(0). This is the per-component volume entering an SW-residue
    binding term. `dps` defaults to the active mpmath precision context."""
    if dps is None:
        dps = mp.mp.dps
    if is_hyperbolic(name):
        return kv.vol_at(name, dps)
    return mp.mpf(0)


def _emit_witness() -> None:
    from witness_base import WitnessBuilder

    mp.mp.dps = COMPUTE_DPS
    tol = mp.mpf(10) ** (-(COMPUTE_DPS - 5))
    eight_G = 8 * kv.CATALAN_G_MPF  # Vol(L6a4) = 8·Catalan

    w = WitnessBuilder("sw-hyperbolicity-gate", engine="mpmath")
    w.set_audit_only(
        "docs/workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md"
    )
    # Record the gate decision + volume for every canonical knot/link.
    table = {}
    for nm in sorted(HYPERBOLIC | NON_HYPERBOLIC):
        try:
            hyp = is_hyperbolic(nm)
            v = vol_component(nm)
            table[nm] = {"hyperbolic": hyp, "vol_component": mp.nstr(v, 16)}
        except Exception as e:  # noqa: BLE001
            table[nm] = {"error": repr(e)}
    w.add_data("hyperbolicity_gate", table)

    # Assertions encoding L4.
    asserts = [
        # Borromean L6a4 is hyperbolic and its gated volume is 8·G (the n=4
        # magic-shell binding term Vol).
        ("L6a4_hyperbolic_vol_eq_8G",
         1 if (is_hyperbolic("L6a4")
               and abs(vol_component("L6a4") - eight_G) < tol) else 0,
         "Vol_component(L6a4) = 8·Catalan = magic-A n=4 term volume"),
        # Trefoil (torus T(2,3)) is non-hyperbolic and gated to 0.
        ("trefoil_nonhyperbolic_vol_zero",
         1 if ((not is_hyperbolic("3_1"))
               and vol_component("3_1") == 0) else 0,
         "T(2,3) Seifert-fibered ⇒ D(z)=0 ⇒ Vol_component = 0"),
        # Figure-eight is hyperbolic with positive volume.
        ("fig8_hyperbolic_vol_positive",
         1 if (is_hyperbolic("4_1") and vol_component("4_1") > 0) else 0,
         "4_1 hyperbolic, Vol_component > 0"),
        # The EW torus triplet is gated to 0 (VolDensity chain N/A there).
        ("ew_torus_triplet_vol_zero",
         1 if all(vol_component(t) == 0 for t in ("T(2,4)", "T(2,6)", "T(2,8)"))
         else 0,
         "W=T(2,4), Z=T(2,6), H=T(2,8) Seifert ⇒ Vol_component = 0"),
    ]
    for nm, computed, src in asserts:
        w.add_assertion(nm, computed=computed, expected=1, source=src)

    out = w.save()
    print(f"  Witness: {out.name}")


if __name__ == "__main__":
    mp.mp.dps = COMPUTE_DPS
    print("SW-residue hyperbolicity gate (L4)")
    for nm in ("L6a4", "4_1", "6_2", "8_11", "3_1", "T(2,6)", "unknot"):
        try:
            print(f"  {nm:>8}: hyperbolic={is_hyperbolic(nm)!s:>5}  "
                  f"Vol_component={mp.nstr(vol_component(nm), 10)}")
        except ValueError as e:
            print(f"  {nm:>8}: {e}")
    _emit_witness()
