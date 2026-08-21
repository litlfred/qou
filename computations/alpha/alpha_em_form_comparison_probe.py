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

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402

sys.path.insert(0, str(_ROOT / "computations"))
# The private name is what exists on main today. PR #5302 exports a public
# `alpha_em_inv_derived` alias for exactly this reuse; switch to it once that
# lands, rather than keeping a second copy of the derivation here.
from meson_em_sinh_closed_form import (  # noqa: E402
    _alpha_em_inv_derived,
)

mp.mp.dps = 50

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

    pins = [("proton", mp.mpf(Q_50_DIGIT_STR)), ("muon", _muon_q())]

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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
