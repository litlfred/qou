#!/usr/bin/env python3
"""Which letters of the atom word are braid generators, and which are not.

Bean qou-qpj9. Witnesses the correction made to
`mass_at_3A_proper.atom_braid_word_3A`'s docstring, so the numbers in it are
checkable and a future edit that breaks them fails here.

WHY THIS EXISTS
===============
That docstring (PR #5765) establishes the load-bearing fact that the atom
object lies in H_n(q) OUTSIDE the image of rho : B_n -> H_n(q), so there is no
single link behind it and no topological quantity -- volume, crossing number,
genus -- may be read off it. That is correct and this probe confirms its two
counts.

But it also said "Only the `d == 0` letters are braid generators", which is
measurably wrong and points the conclusion at the wrong objects. Under this
module's own convention `sigma^-1 = sigma - h`, a `d == -h` letter IS a braid
generator. The letters outside im(rho) are the AVERAGED ones, `d/h` in
{1/2, 1/2 - delta/4}, which are genuine weight-1 averages over crossing sign
and so are sums of two monomials rather than one.

The distinction is not pedantic. Under a `d == 0` rule the figure-eight
`(s1 s2^-1)^2` -- the muon carrier, a genuine hyperbolic LINK from which the
mass law reads Vol -- would classify as "not a braid word". The non-link
conclusion belongs to the atom object; it must not leak onto the knot-dictionary
carriers, which are links and for which Vol(K) is exactly what the mass law
reads.

EXPLORATORY / audit-only. Reads the canonical word; runs no producer and
rewrites no witness but its own.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from canonical_braid_crossings import classify_crossing  # noqa: E402
from pyhecke.gram import h as h_val  # noqa: E402
from q_parameter import HA_MP  # noqa: E402 — exact mpf, not the f64 twin

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# The classify() ratios below are mpmath constructions, so the module must not
# compute at mpmath's default dps=15 (never-raises-dps ratchet). The margins
# here are wide -- d/h lands at 0, -1, -1/2 or -(1/2 - delta/4), tested against
# 1e-9 -- so no verdict in this file moves. Raised anyway: the gate is about
# never computing at 15, not about whether this particular file got lucky.
set_compute_dps()

ISOTOPES = [("2H", 1, 1), ("3He", 2, 1), ("4He", 2, 2)]


def _is_averaged_family(ctype: str) -> bool:
    """Both members of the averaged family — colour-blind and colour-weighted.

    The census question is "does this letter lie in im(rho)?", and NEITHER
    averaged letter does, so both belong in `n_avg`. Matching the corpus
    convention (`per_nucleon_shift_derivation`, `ocneanu_cancellation_derivation`,
    `wenzl_a3_combiner_end_to_end`) rather than enumerating the two names, so a
    future third member is caught too.
    """
    return ctype.startswith("averaged")


def main() -> None:
    h = HA_MP
    rows = []
    for name, Z, N in ISOTOPES:
        w = atom_braid_word_3A(Z, N)
        kinds = [classify_crossing(_c, d, float(h),
                                   context=f"{name} gen {_g}")
                 for (_c, d, _g) in w]
        n_avg = sum(1 for k in kinds if _is_averaged_family(k))
        A = Z + N
        rows.append({
            "isotope": name, "Z": Z, "N": N, "A": A,
            "letters": len(w),
            "sigma": kinds.count("sigma"),
            "sigma_inv": kinds.count("sigma_inv"),
            "averaged_not_in_im_rho": n_avg,
            # Split reported so the p-n colour weighting is VISIBLE in the
            # witness. `atom_braid_word_3A` defaults to bring_color_weighted,
            # so a table showing averaged_weighted == 0 would mean the word
            # was built colour-blind — which the total alone cannot show.
            "averaged_colour_blind": kinds.count("averaged"),
            "averaged_colour_weighted": kinds.count("averaged_weighted"),
            "braid_generators": kinds.count("sigma") + kinds.count("sigma_inv"),
            "predicted_2A_plus_1": 2 * A + 1,
            "branch_closures_2_pow": 2 ** n_avg,
        })

    d2 = rows[0]

    # 1. the docstring's own count, confirmed at every A -- this is the claim
    #    that the object is outside im(rho), and by how much.
    assert all(r["averaged_not_in_im_rho"] == r["predicted_2A_plus_1"]
               for r in rows), \
        "the averaged-letter count is not 2A+1; the non-link argument's " \
        "arithmetic does not hold"
    # 2. the 32 branch closures the SnapPy sweep measured for 2H
    assert d2["branch_closures_2_pow"] == 32, \
        f"2H branch count {d2['branch_closures_2_pow']} != the measured 32"
    # 3. the correction: sigma^-1 letters exist and are braid generators, so a
    #    'd == 0' rule undercounts them
    assert d2["sigma_inv"] > 0, \
        "no sigma^-1 letters found -- then the 'd == 0' rule would have been " \
        "harmless and this correction is unfounded"
    assert d2["braid_generators"] > d2["sigma"], \
        "braid generators do not exceed the d == 0 letters"

    wb = WitnessBuilder("atom-word-braid-letter-census", engine="python-exact")
    wb.set_description(
        "Census of the atom word's letters by whether they lie in the image of "
        "rho : B_n -> H_n(q). Confirms the two counts the atom_braid_word_3A "
        "docstring rests its no-single-link argument on (averaged letters = "
        "2A+1; 2^(2A+1) = 32 branch closures for 2H), and corrects its "
        "'only d == 0 letters are braid generators' parenthetical: under the "
        "module's own sigma^-1 = sigma - h, the d == -h letters are braid "
        "generators too.")
    wb.add_data("census", rows)
    wb.add_data("correction", {
        "where": "computations/mass_at_3A_proper.py::atom_braid_word_3A docstring",
        "was": "Only the `d == 0` letters are braid generators.",
        "measured_on_2H": (f"{d2['letters']} letters: {d2['sigma']} sigma, "
                           f"{d2['sigma_inv']} sigma^-1, "
                           f"{d2['averaged_not_in_im_rho']} averaged. So "
                           f"{d2['braid_generators']} are braid generators, "
                           f"not {d2['sigma']}."),
        "why_it_matters": ("under a 'd == 0' rule the figure-eight "
                           "(s1 s2^-1)^2 -- the muon carrier, a genuine "
                           "hyperbolic LINK the mass law reads Vol from -- "
                           "would classify as 'not a braid word'. The "
                           "no-single-link conclusion belongs to the atom "
                           "object and must not leak onto the knot-dictionary "
                           "carriers."),
        "what_is_CONFIRMED_not_corrected": ("the substance. The atom object IS "
                                            "outside im(rho), the averaged "
                                            "count IS 2A+1, and 2^5 = 32 DOES "
                                            "match the SnapPy sweep. Only the "
                                            "parenthetical was wrong."),
    })
    wb.set_audit_only(
        "docs/audits/2026-08-25-ito-dehornoy-hyperbolicity-criterion.md")
    wb.add_assertion(
        name="averaged_letter_count_is_2A_plus_1",
        computed=sum(1 for r in rows
                     if r["averaged_not_in_im_rho"] == r["predicted_2A_plus_1"]),
        expected=len(rows), tolerance=0, unit="count",
        source="Holds at every A tested; this is the non-link argument's arithmetic.")
    wb.add_assertion(
        name="deuteron_branch_closures_match_the_snappy_sweep",
        computed=d2["branch_closures_2_pow"], expected=32, tolerance=0,
        unit="count",
        source="2^(2A+1) at A=2, against the 32/32 non-hyperbolic sweep.")
    wb.add_assertion(
        name="braid_generators_exceed_the_d_eq_0_letters",
        computed=d2["braid_generators"] - d2["sigma"], expected=7,
        tolerance=0, unit="letters",
        source=("The sigma^-1 letters the 'd == 0' rule dropped. Non-zero is "
                "the correction; the value is the size of it on 2H."))
    out = wb.save()

    print(f"{'iso':>5} {'letters':>8} {'sigma':>6} {'s^-1':>6} {'avg':>5} "
          f"{'2A+1':>6} {'braid':>6} {'closures':>9}")
    for r in rows:
        print(f"{r['isotope']:>5} {r['letters']:>8} {r['sigma']:>6} "
              f"{r['sigma_inv']:>6} {r['averaged_not_in_im_rho']:>5} "
              f"{r['predicted_2A_plus_1']:>6} {r['braid_generators']:>6} "
              f"{r['branch_closures_2_pow']:>9}")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
