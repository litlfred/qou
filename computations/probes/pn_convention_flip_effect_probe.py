#!/usr/bin/env python3
"""What the strict_averaged -> bring_color_weighted flip actually moves.

# Why this probe exists

A green test suite is not evidence about this flip. The Rust crate's 212
tests pass identically before and after it, because its only atom tests
(`vacuum`, `hydrogen`) have NO p-n bond at all. The check that means
something is a quantity computed for an atom with Z >= 1 AND N >= 1,
measured against a prediction derived independently of the code under test.

# The headline, and the correction it forced

**The two canonical paths disagree about how many p-n bonds an atom has,
so the flip moves them by different amounts.** An earlier revision of this
probe measured only the closed form, found a single A-independent factor,
and stated it as a property of THE FLIP. That was an over-generalisation
from one path, and it is the sort that invites skipping a regeneration.

    closed_form_ratio   adjacent pairs of the ordering ["p"]*Z + ["n"]*N.
                        That ordering is all protons then all neutrons, so
                        it has EXACTLY ONE p-n boundary -- for the deuteron
                        and for carbon-12 alike. The flip is a single
                        A-independent factor 1 + 1.4149466e-04, verified
                        here to 56-57 decimal places.

    build_atom_nf       ALL pairs (`for prev in range(k)`), so Z*N mixed
                        bonds. The shift GROWS with A: measured +8.5e-05
                        (2H), +2.1e-04 (4He), +8.1e-04 (7Li).

Nor is the normal-form shift proportional to Z*N -- measured rel/pred is
0.60, 1.06, 1.16, 1.47, 5.41, 5.69 against Z*N of 1, 2, 2, 4, 9, 12 --
because `nf_tr` is a trace of a product in the Hecke algebra and not a
product of scalars, so its sensitivity to one coefficient is not additive
in the bonds.

# What is safe to conclude

1. Z = 0 OR N = 0 IS UNTOUCHED, on both paths. The proton and the neutron
   have no mixed bond and are bit-identical across the flip. Any witness
   whose atoms are all pure-flavour needs no regeneration. This is the only
   "no work needed" rule this probe supports.

2. On the closed-form path a RATIO of two mixed atoms sees the single
   factor cancel exactly. That does NOT extend to the normal-form path.

3. Anything on the normal-form path must be re-run to learn its new value.
   There is no shortcut and this probe deliberately does not offer one.

Bean qou-cblw. Owner authorisation 2026-08-26.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for _p in (_HERE.parent, _HERE.parent / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from mpmath import mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from closed_form_tau_M import closed_form_ratio, markov_z, hecke_h  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

DPS = 60

ATOMS = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1),
         ("4He", 2, 2), ("7Li", 3, 4), ("12C", 6, 6)]
PURE = [("proton", 1, 0), ("neutron", 0, 1), ("2p", 2, 0), ("2n", 0, 2)]


def main() -> int:
    _started = time.monotonic()
    mp.dps = DPS
    # `q_parameter.Q` is a float64. Carrying it here would cap every
    # printed value at 17 significant digits while the corpus computes
    # these factors at 50 dps -- the committed witnesses record
    # 0.508157887748645593880406757381..., which is the 50-dps value and
    # diverges from the f64-q one at digit 18.
    q = mp.mpf(Q_50_DIGIT_STR)
    z, h = markov_z(q), hecke_h(q)
    delta = flavor_split_leading(q)

    f_blind = z - h / 2
    h_f64 = float(h)
    f_canon = z - h * (mp.mpf(1) / 2 - delta / 4)
    predicted = f_canon / f_blind - 1

    w = WitnessBuilder("pn-convention-flip-effect", engine="mpmath",
                       output_dir=_HERE, start_time=_started)
    w.set_description(
        "What the strict_averaged -> bring_color_weighted p-n flip moves. "
        "The canonical ordering p..p n..n carries exactly ONE p-n boundary "
        "for every atom, so the flip is a single A-independent factor "
        "1 + 1.4149466e-04 on the closed-form trace ratio, not an "
        "accumulating per-bond error; pure-flavour systems are untouched."
    )
    w.set_content_block("prop:pn-averaging-uniqueness")
    # Emitted BY THE PRODUCER. A hand-built witness that gets these keys
    # backfilled downstream loses them on every re-run -- the bare-producer
    # hazard AGENTS.md records under the witness staleness triage.
    w.add_parameter("q0Anchor", "proton")
    w.add_parameter("q0", mp.nstr(q, 50))
    w.add_assertion("f_pn_blind", mp.nstr(f_blind, 30),
                    "0.508157887748645593880406757381")
    w.add_assertion("f_pn_canonical", mp.nstr(f_canon, 30),
                    "0.508229789376738962577995797656")
    # Exact identity, so the residual is pure arithmetic noise at 60 dps.
    # A tolerance is required: asserting == 0.0 against 8.6e-63 fails, which
    # is a defect in the assertion and not in the mathematics.
    w.add_assertion("per_bond_gap_is_h_delta_over_4",
                    mp.nstr(abs((f_canon - f_blind) - h * delta / 4), 5), "0.0",
                    tolerance="1e-55",
                    source="the whole difference is exactly h*delta/4")

    print(f"f_pn  blind      {mp.nstr(f_blind, 30)}")
    print(f"f_pn  canonical  {mp.nstr(f_canon, 30)}")
    print(f"predicted shift  {mp.nstr(predicted, 30)}\n")

    print(f"{'atom':>8} {'p-n bonds':>10} {'measured rel shift':>34} {'agrees to':>10}")
    for name, Z, N in ATOMS:
        order = ["p"] * Z + ["n"] * N
        bonds = sum(1 for k in range(len(order) - 1) if order[k] != order[k + 1])
        rb = closed_form_ratio(Z, N, q, pn_convention="strict_averaged")
        rc = closed_form_ratio(Z, N, q, pn_convention="bring_color_weighted")
        rel = (rc - rb) / rb
        discrepancy = abs(rel / predicted - 1)
        agree = int(-mp.log10(discrepancy)) if discrepancy > 0 else DPS
        print(f"{name:>8} {bonds:>10} {mp.nstr(rel, 25):>34} {agree:>7} dp")
        w.add_assertion(f"{name}_mixed_bond_count", str(bonds), "1",
                        source="canonical ordering p..p n..n has ONE p-n boundary")
        # Numeric, not a rendered string: a string assertion cannot express
        # "at least this good", so `agrees_to_57_dp` vs `agrees_to_>=50_dp`
        # compares unequal and reports a failure on a correct result.
        w.add_assertion(f"{name}_shift_matches_single_factor_prediction",
                        mp.nstr(discrepancy, 5), "0.0", tolerance="1e-50",
                        source="relative discrepancy vs f_canon/f_blind - 1")

    print()
    for name, Z, N in PURE:
        rb = closed_form_ratio(Z, N, q, pn_convention="strict_averaged")
        rc = closed_form_ratio(Z, N, q, pn_convention="bring_color_weighted")
        same = rb == rc
        print(f"{name:>8}  Z={Z} N={N}  unchanged by the flip: {same}")
        w.add_assertion(f"{name}_unchanged_by_flip", str(same), "True",
                        source="no mixed bond, so no factor to move")

    # ── the normal-form path, which does NOT obey the single-factor law ──
    #
    # Measured separately and deliberately: `build_atom_nf` bonds ALL pairs
    # (`for prev in range(k)`), so it has Z*N mixed bonds where the closed
    # form has one. Reporting only the closed form here is what produced the
    # over-generalised claim this probe now opens by retracting.
    print()
    print("normal-form path (pyhecke.atom.build_atom_nf, ALL pairs):")
    print(f"{'atom':>8} {'Z*N':>5} {'blind':>20} {'canonical':>20} {'rel':>13} {'rel/pred':>9}")
    try:
        import pyhecke.atom as _A
        from pyhecke.gram import nf_tr as _nf_tr
        _canon_d, _blind_d = _A.D_PN, -h_f64 / 2
        for name, Z, N in [("proton", 1, 0), ("neutron", 0, 1)] + ATOMS[:5]:
            _A.D_PN = _blind_d
            tb = float(_nf_tr(_A.build_atom_nf(Z, N)))
            _A.D_PN = _canon_d
            tc = float(_nf_tr(_A.build_atom_nf(Z, N)))
            rel = (tc - tb) / tb if tb else 0.0
            print(f"{name:>8} {Z*N:>5} {tb:>20.15f} {tc:>20.15f} "
                  f"{rel:>13.4e} {rel/float(predicted) if predicted else 0:>9.4f}")
            w.add_assertion(f"nf_{name}_shift", f"{rel:.6e}",
                            "0.0" if Z * N == 0 else f"{rel:.6e}",
                            tolerance="1e-30" if Z * N == 0 else None,
                            source="build_atom_nf bonds ALL pairs, so Z*N mixed "
                                   "bonds; the shift is NOT the single closed-form "
                                   "factor and is not proportional to Z*N either")
        _A.D_PN = _canon_d
        nf_measured = True
    except Exception as exc:              # pragma: no cover - env dependent
        print(f"  (skipped: {exc})")
        nf_measured = False
    w.add_assertion("normal_form_path_measured", str(nf_measured), "True",
                    source="reporting only the closed form is what produced the "
                           "retracted single-factor claim")

    path = w.save(extra={"data": {
        "q0": mp.nstr(q, 25),
        "delta": mp.nstr(delta, 25),
        "f_pn_strict_averaged": mp.nstr(f_blind, 30),
        "f_pn_bring_color_weighted": mp.nstr(f_canon, 30),
        "relative_shift": mp.nstr(predicted, 30),
        "mixed_bonds_in_canonical_ordering": 1,
        "a_independence_holds_for_closed_form_ratio_ONLY": True,
        "normal_form_path_bonds_all_pairs_and_shift_grows_with_A": True,
        "retracted_claim": "an earlier revision called the single A-independent factor a property of the flip; it is a property of closed_form_ratio's adjacent-pair walk over the ordering p..p n..n",
    }})
    print(f"\nwitness -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
