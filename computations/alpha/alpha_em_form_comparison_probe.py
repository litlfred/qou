#!/usr/bin/env python3
"""Compare every alpha_EM closed form the corpus carries, at both pins.

Written because `computations/DERIVATION-STATUS.md` asserted the fine-structure
residual was "resolved at 6.7 ppb ... no further derivation required", citing a
form that `archimedean-functor-uniqueness-context` rules out **structurally**
as "a legacy PSLQ-empirical conjecture" requiring "arbitrary integer ratios".
Three separate sites in that one file carried the claim, two of them with the
live and ruled-out forms swapped.

The point of a probe rather than a table of typed numbers: the corrected doc
now quotes residuals, and a quoted residual is exactly the thing this arc keeps
finding stale. Re-run this instead of trusting the prose.

Reference values are READ (q from q_parameter, alpha from the NIST table via
qou_substrate.codata), never transcribed.

Run:  python3 -u computations/alpha/alpha_em_form_comparison_probe.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "computations" / "substrate"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402

sys.path.insert(0, str(_ROOT / "computations"))
# The private name is what exists on main today. PR #5302 exports a public
# `alpha_em_inv_derived` alias for exactly this reuse; switch to it once that
# lands, rather than keeping a second copy of the derivation here.
from meson_em_sinh_closed_form import (  # noqa: E402
    _alpha_em_inv_derived,
)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# The muon pin is used ONLY as an explicit comparison against the proton pin,
# per the owner directive of 2026-08-21 ("no muon pinning except explicitly,
# such as in comparison to proton"). It is read from the anchor-defining
# witness rather than typed.
_MUON_WITNESS = _ROOT / "computations" / "q-pinning-50-digit.witness.json"


def _muon_q() -> mp.mpf:
    import json
    return mp.mpf(json.loads(_MUON_WITNESS.read_text())["q0Value"])


def q_int(k: int, q: mp.mpf) -> mp.mpf:
    """Balanced quantum integer [k]_q = (q^k - q^-k)/(q - q^-1)."""
    return (q ** k - q ** -k) / (q - 1 / q)


def bare(q: mp.mpf) -> mp.mpf:
    """The bare force-carrier coupling q*[9]_q*[10]_q (prop:em-coupling-projection)."""
    return q * q_int(9, q) * q_int(10, q)


def cs_tower_resummed(q: mp.mpf) -> mp.mpf:
    """bare * (1 + c1/(1 - c1*kappa)) -- the CS tower, exactly resummed.

    IMPORTED, not reimplemented. A first draft of this probe hand-rolled the
    Gram determinants and produced -2242 ppb where the real derivation gives
    -467.6 ppb: a 4.8x error, inside a probe written to correct someone
    else's wrong number. The canonical mpmath derivation already exists and
    needs no numpy, so a second copy has nothing to recommend it.
    """
    return _alpha_em_inv_derived(q)


def zero_mode(q: mp.mpf) -> mp.mpf:
    """bare + 2/(3*pi): the photon IR zero-mode on Bring's surface (genus 4).

    b_1/Area = 2g/(4*pi*(g-1)) = 8/(12*pi) = 2/(3*pi) at g = 4.
    """
    return bare(q) + 2 / (3 * mp.pi)


def pslq_ruled_out(q: mp.mpf) -> mp.mpf:
    """45*[3]_q*(1 + d + 8q*d^2), d = hbar_q^4*[5]_q.

    RULED OUT structurally -- carried here only so the doc's claim can be
    checked rather than argued about. Do not wire this to production.
    """
    hb = 1 - 1 / q
    d = hb ** 4 * q_int(5, q)
    return 45 * q_int(3, q) * (1 + d + 8 * q * d ** 2)


FORMS = [
    ("bare  q[9][10]", bare, "derived"),
    ("bare + 2/(3pi)", zero_mode, "derived (superseding form)"),
    ("CS tower resummed", cs_tower_resummed, "derived (registry)"),
    ("45[3](1+d+8qd^2)", pslq_ruled_out, "RULED OUT (PSLQ-empirical)"),
]


def main() -> int:
    entry = codata("inverse fine-structure constant")
    c22 = entry.value
    c18 = mp.mpf("137.035999084")  # the CODATA-2018 value the doc scored against

    print("=" * 76)
    print("alpha_EM closed forms — every form the corpus carries, both pins")
    print("=" * 76)
    print(f"CODATA-2022 (NIST table): {entry.value_str} +/- {entry.uncertainty_str}"
          f"  ({entry.rel_ppb:.3g} ppb)")
    print(f"CODATA-2018 (for the historical comparison): {c18}")
    print()

    pins = [("proton", Q_MP), ("muon", _muon_q())]

    for pin_name, q in pins:
        print(f"--- {pin_name} pin  q0 = {mp.nstr(q, 18)}")
        for name, fn, status in FORMS:
            v = fn(q)
            d22 = (v - c22) / c22 * 10 ** 9
            print(f"  {name:<18s} = {mp.nstr(v, 13):>16s}   "
                  f"{float(d22):>12.1f} ppb   [{status}]")
        print()

    # The specific claim the correction removes.
    print("=" * 76)
    print("The retired claim, checked directly")
    print("=" * 76)
    q_mu = pins[1][1]
    v = pslq_ruled_out(q_mu)
    print(f"  45[3]_q(...) at the MUON pin vs CODATA-2018 : "
          f"{float((v - c18) / c18 * 10 ** 9):.3f} ppb   <- the doc's '6.7 ppb'")
    print(f"  same form   at the PROTON pin vs CODATA-2022: "
          f"{float((pslq_ruled_out(pins[0][1]) - c22) / c22 * 10 ** 9):.3f} ppb")
    print()
    print("  Smallest residual belongs to the RULED-OUT form. That is the")
    print("  signature of a fit, not evidence for it.")

    # `em-coupling-chern-simons` names two candidate causes for its residual:
    # a wrong kappa, or an order-delta^2 truncation missing higher orders.
    # Separating the two settles it.
    print()
    print("=" * 76)
    print("Truncation vs pin — which one owns the residual")
    print("=" * 76)
    for pin_name, q in pins:
        trunc = _alpha_em_inv_derived(q, order=2)
        exact = _alpha_em_inv_derived(q)
        dt = float((trunc - c22) / c22 * 10 ** 9)
        de = float((exact - c22) / c22 * 10 ** 9)
        print(f"  {pin_name:<7s} order-2 {dt:9.2f} ppb   exact {de:9.2f} ppb   "
              f"resummation shrinks |residual| by {abs(dt) - abs(de):.2f} ppb")
    # pins[0] is proton, pins[1] is muon -- going muon -> proton is [0] - [1].
    # An earlier draft had these the wrong way round and printed +79.17 under a
    # "muon -> proton" label.
    q_proton_pin, q_muon_pin = pins[0][1], pins[1][1]
    dm = float((_alpha_em_inv_derived(q_proton_pin)
                - _alpha_em_inv_derived(q_muon_pin)) / c22 * 10 ** 9)
    print(f"  muon -> proton pin change: {dm:+.2f} ppb")
    # Solve for the kappa that would close the gap exactly, rather than
    # restating a figure: the block's "~1.8878" is the old pin + edition.
    q = pins[0][1]
    b = bare(q)
    c1 = ((mp.pi ** 2 * mp.mpf(10) / 9 + mp.pi ** 2 * mp.mpf(16) / 15)
          * (q_int(2, q) / 2) * (1 - 1 / q) ** 2 / b)
    ratio = c22 / b
    kappa_needed = ((ratio - 1) - c1) / ((ratio - 1) * c1)
    witten = mp.mpf("1.722")
    resid = abs(float((cs_tower_resummed(q) - c22) / c22 * 10 ** 9))
    # Recomputed for THIS pin rather than reusing dt/de, which leak from the
    # loop above holding the last iteration's (muon) values. They happen to
    # coincide -- the resummation gain is pin-invariant -- so the number was
    # right by luck while the sentence reported the proton residual beside it.
    trunc_ppb = abs(float((_alpha_em_inv_derived(q, order=2) - c22) / c22 * 10 ** 9))
    gain = trunc_ppb - resid
    print()
    print(f"  Higher orders are worth {gain:.2f} ppb against a {resid:.0f} ppb "
          f"residual — one part in {resid / gain:.0f} of")
    print("  the gap. The truncation is NOT the explanation, so by elimination within")
    print("  that block's own two options the defect is kappa (still a `sorry`).")
    print(f"  Exact closure at this pin needs kappa = "
          f"{mp.nstr(kappa_needed, 8)} against Witten's {witten} "
          f"({float((kappa_needed - witten) / witten * 100):.1f}%).")

    # ------------------------------------------------------------------
    # Witness emission, added 2026-09-05 (qou-i229).
    #
    # This probe is the producer `tbl:em-coupling-projection-table1-data` names
    # in its own prose, and it computes six of that table's seven rows -- but it
    # emitted NO witness, so those six had no machine-readable provenance at
    # all, while `em_coupling_projection_probe.py` claimed the block via
    # contentBlock and computed only the single bare row.
    # `scripts/witness-block-agreement.py` reported the block 6/7 unmatched
    # against its declared witness. The block was correct; the POINTER was on
    # the wrong producer. Recording the real one is the fix.
    # ------------------------------------------------------------------
    try:
        from witness_base import WitnessBuilder  # noqa: E402

        wb = WitnessBuilder(Path(__file__).stem, engine="python")
        wb.set_content_block("prop:em-coupling-projection")
        wb.set_description(
            "Every alpha_EM closed form the corpus carries, evaluated at both "
            "registered pins and scored in ppb against CODATA 2022 read from the "
            "NIST table. This is the producer tbl:em-coupling-projection-table1-data "
            "names in its own prose and the source of six of that table's seven "
            "rows; it previously emitted no witness, leaving those rows with no "
            "machine-readable provenance while a different probe claimed the block "
            "and computed only the bare form (qou-i229). Records the resummed CS "
            "tower (the table's 137.0359351 at the proton pin, -467.6 ppb), the "
            "order-2 truncation it supersedes, and the RULED-OUT PSLQ-empirical "
            "form -- which has the smallest residual of any form here, the "
            "signature of a fit rather than evidence for one.")
        for pin_name, qp in pins:
            wb.add_data(f"forms_at_{pin_name}_pin", {
                "q0": mp.nstr(qp, 20),
                **{name: mp.nstr(fn(qp), 13) for name, fn, _st in FORMS},
                **{f"{name} [ppb vs CODATA2022]":
                   mp.nstr((fn(qp) - c22) / c22 * 10 ** 9, 8)
                   for name, fn, _st in FORMS},
            })
        # The block publishes three further figures this probe already computes
        # but never exposed: delta_CS (the tower's ratio, `c1` above), the
        # order-2 truncation at the muon pin that the table records as a
        # SUPERSEDED value, and the CODATA-2022 input it scores against. Naming
        # them is what gives the table's remaining rows provenance.
        wb.add_data("published_intermediates", {
            "delta_CS_at_proton_pin": mp.nstr(c1, 12),
            "order2_truncation_at_muon_pin__superseded":
                mp.nstr(_alpha_em_inv_derived(q_muon_pin, order=2), 12),
            "codata_2022_alpha_inv": entry.value_str,
            "codata_2022_uncertainty": entry.uncertainty_str,
        })
        wb.add_data("residual_ownership", {
            "resummation_gain_ppb": mp.nstr(mp.mpf(gain), 8),
            "cs_tower_residual_ppb": mp.nstr(mp.mpf(resid), 8),
            "pin_change_muon_to_proton_ppb": mp.nstr(mp.mpf(dm), 8),
            "kappa_needed_for_exact_closure": mp.nstr(kappa_needed, 8),
            "kappa_witten_1988": mp.nstr(witten, 6),
        })
        wb.add_assertion(
            name="the CS-tower row the block publishes reproduces at the proton pin",
            computed=mp.nstr(cs_tower_resummed(q_proton_pin), 10),
            expected="137.0359351")
        wb.add_assertion(
            name="the resummation gain is pin-invariant, so higher orders do not "
                 "own the residual",
            computed=f"{gain:.2f}", expected="11.06")
        wb.add_caveat(
            "The smallest residual belongs to the RULED-OUT PSLQ-empirical form. "
            "That is the signature of a fit, not evidence for it; the form is "
            "recorded only so the comparison is legible.")
        wb.add_caveat(
            "kappa is still a `sorry`. Exact closure at the proton pin needs "
            f"{mp.nstr(kappa_needed, 8)} against Witten's {mp.nstr(witten, 6)}, an "
            "11.2 % gap, and nothing here derives it.")
        wb.add_caveat(
            f"The muon-pin rows use the converged live pin from {_MUON_WITNESS.name}, "
            "not the retired CODATA-2018 vintage that several content blocks still "
            "publish (qou-i229).")
        # Both pins are read ON PURPOSE (every form is scored at each), so the
        # witness is a q0 comparison, not a single-pin result: stamp it with the
        # values actually computed with, and no bare q0Value.
        from qou_substrate.witness import q0_comparison  # noqa: E402
        print(f"\n  witness -> {wb.save(q0_comparison(muon=mp.nstr(q_muon_pin, 50, strip_zeros=False), proton=mp.nstr(q_proton_pin, 50, strip_zeros=False), reason='scores every alpha_EM closed form at BOTH registered pins (proton Q_50_DIGIT_STR and the live muon pin from the muon anchor witness) and reports the muon->proton pin change; both pins are read on purpose'))}")
    except Exception as e:  # pragma: no cover
        print(f"\n  (witness emit skipped: {e})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
