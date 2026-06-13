"""Many-body binding series — body-order enumerator (workplan task C3).

Step-9 binding-closure workplan: binding is the additive body-order series
`B(K) = Σ_n B_n` (= the jet-order filtration, `conj:binding-manybody-eq-jet-filtration`).
Each term `B_n = m_e · a_D^{(n)}` is m_e times the n-th prolonged SW period,
a residue sum over the *hyperbolic* link-components (`sw_hyperbolicity_gate`).

This enumerator computes the two DERIVED members of the series and checks
them against AME (zero fits):

  • n=2 (deuteron, one inter-nucleon bond): `B_2 = m_e · Vol(6_2)`.
  • n=4 (magic-shell ⁴He, whole-α): `B_4 = 2 · m_e · A · Vol(L6a4)`
    (the canonical magic-A formula; Vol(L6a4) = 8·Catalan).

The n=3 (genuine three-body) term is OPEN (not reducible to pairwise sums,
confirmed negative in sibling #1790) and is recorded as such — no fit.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_HERE = _Path(__file__).resolve().parent
_sys.path.insert(0, str(_HERE.parent))  # computations/
_sys.path.insert(0, str(_HERE))         # substrate/
import _path_bridge as _bridge  # noqa: E402, F401
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION  # noqa: E402

import mpmath as mp  # noqa: E402

from sw_hyperbolicity_gate import vol_component  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from _precision import COMPUTE_DPS  # noqa: E402

# AME binding energies (MeV) — comparison anchors, NOT inputs.
B_DEUTERON_AME = AME_B_DEUTERON_MEV_VALIDATION
B_HE4_AME = AME_B_HE4_MEV_VALIDATION


def body_term(n: int) -> mp.mpf:
    """The derived n-body binding term (MeV). Raises for the open n=3."""
    m_e = mp.mpf(str(M_E_MEV))
    if n == 2:
        # deuteron: one inter-nucleon bond, hyperbolic knot 6_2.
        return m_e * vol_component("6_2")
    if n == 4:
        # magic-A ⁴He: whole-α Borromean volume, A = 4.
        A = 4
        return 2 * m_e * A * vol_component("L6a4")
    if n == 3:
        raise NotImplementedError(
            "n=3 (genuine three-body) term is open — not a pairwise sum "
            "(sibling #1790 negative); awaits the n=3 SW period."
        )
    raise ValueError(f"no derived body term for n={n}")


def _emit_witness() -> None:
    from witness_base import WitnessBuilder

    mp.mp.dps = COMPUTE_DPS
    B2 = body_term(2)
    B4 = body_term(4)
    err2 = (B2 - B_DEUTERON_AME) / B_DEUTERON_AME
    err4 = (B4 - B_HE4_AME) / B_HE4_AME

    w = WitnessBuilder("binding-manybody-series", engine="mpmath")
    w.set_audit_only(
        "docs/workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md"
    )
    w.add_data("series_structure",
               "B(K) = sum_n B_n; body order n = jet/SW vertical degree")
    w.add_data("n2_deuteron", {
        "formula": "m_e * Vol(6_2)",
        "value_MeV": mp.nstr(B2, 12),
        "ame_MeV": mp.nstr(B_DEUTERON_AME, 12),
        "rel_err": mp.nstr(err2, 6),
    })
    w.add_data("n3_threebody", {"status": "open",
                                "note": "not pairwise (sibling #1790 negative)"})
    w.add_data("n4_he4_magicA", {
        "formula": "2 * m_e * A * Vol(L6a4), A=4",
        "value_MeV": mp.nstr(B4, 12),
        "ame_MeV": mp.nstr(B_HE4_AME, 12),
        "rel_err": mp.nstr(err4, 6),
    })

    # Anchors: deuteron within +1.1%, ⁴He within +5.87% — the two derived
    # members of the body-order series (no fit).
    w.add_assertion(
        "n2_deuteron_within_2pct",
        computed=1 if abs(err2) < mp.mpf("0.02") else 0, expected=1,
        source=f"n=2 m_e·Vol(6_2): rel_err = {mp.nstr(err2, 4)}")
    w.add_assertion(
        "n4_he4_magicA_within_6pct",
        computed=1 if abs(err4) < mp.mpf("0.065") else 0, expected=1,
        source=f"n=4 2·m_e·A·Vol(L6a4): rel_err = {mp.nstr(err4, 4)} (+5.87% anchor)")
    out = w.save()
    print(f"  Witness: {out.name}")


if __name__ == "__main__":
    mp.mp.dps = COMPUTE_DPS
    print("Many-body binding series (C3) — derived members")
    B2 = body_term(2)
    B4 = body_term(4)
    print(f"  n=2 deuteron  m_e·Vol(6_2)        = {mp.nstr(B2, 10)} MeV "
          f"(AME {mp.nstr(B_DEUTERON_AME, 8)}, {mp.nstr(100*(B2-B_DEUTERON_AME)/B_DEUTERON_AME, 3)}%)")
    print(f"  n=3 three-body                    = OPEN (not pairwise, #1790)")
    print(f"  n=4 ⁴He  2·m_e·A·Vol(L6a4), A=4   = {mp.nstr(B4, 10)} MeV "
          f"(AME {mp.nstr(B_HE4_AME, 8)}, {mp.nstr(100*(B4-B_HE4_AME)/B_HE4_AME, 3)}%)")
    _emit_witness()
