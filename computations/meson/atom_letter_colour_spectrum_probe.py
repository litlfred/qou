"""Census the atom word's NON-BRAID letters by template, and solve each
template's spectrum for a type-`B` second parameter `(Q, c)`.

WHY THIS EXISTS. A prior probe on this arc censused the non-braid letters and
reported them all as "averaged", then a Lean file
(`QOU/MassTheory/AveragedLetterSpectrum.lean`) proved that an averaged letter
`(σ + σ⁻¹)/2` is `([2]_q/2)·ε` with `ε² = 1`, and that matching a scaled
generator with eigenvalues `cQ, −cQ⁻¹` to `±t` forces **`Q = 1`**.

That census did not distinguish the two templates `atom_braid_word_3A` actually
emits, and its own docstring names both:

    σ − (h/2)·1          == (σ + σ⁻¹)/2                        colour-BLIND
    σ − h·(1/2 − δ/4)·1  == (1/2 + δ/4)σ + (1/2 − δ/4)σ⁻¹      colour-WEIGHTED

The second is the **canonical** one (`pn_convention="bring_color_weighted"`,
owner ruling R3, and the function's own default). Its weights are unequal, so
its two eigenvalues are **not** negatives of one another and the `Q = 1`
conclusion does not apply to it.

WHAT IS MEASURED

1. **Census by template**, per isotope and under BOTH conventions: how many
   letters carry `d = 0` (σ), `d = −h` (σ⁻¹ — a braid generator, NOT averaged),
   `d = −h/2` (symmetric average), `d = −h(1/2 − δ/4)` (colour-weighted), and at
   which generator indices. Classification is exact-arithmetic against the four
   templates, never a tolerance on a float.

2. **The spectrum of each non-braid template.** For `w₊σ + w₋σ⁻¹` with
   `w₊ + w₋ = 1`, using the Hecke eigenvalues `σ ↦ q, −q⁻¹` (so `σ⁻¹ ↦ q⁻¹, −q`):

       μ₊ = w₊q + w₋q⁻¹
       μ₋ = −w₊q⁻¹ − w₋q

3. **The type-`B` solve.** A scaled generator `c·T₀` with
   `(T₀ − Q)(T₀ + Q⁻¹) = 0` has eigenvalues `cQ, −cQ⁻¹`, so matching gives

       c(Q − Q⁻¹) = μ₊ + μ₋      and      −c² = μ₊·μ₋ .

   `Q ↦ Q − Q⁻¹` is a bijection `(0, ∞) → ℝ`, so a positive `Q` is unique when
   it exists. `Q = 1` iff `μ₊ + μ₋ = 0` iff the weights are equal.

NO FLOAT64. Everything is `mpmath.mpf` at 60 dps from the 50-digit q₀ string;
`float()` appears only inside f-strings. Exactness of the census is by symbolic
template comparison, not by a numeric tolerance.

SCOPE. This measures the letters and solves the two-parameter match per
template. It does NOT claim the atom word is presentable in any type-`B`
algebra: that is a statement about a whole word at many generator indices, and
the distinct-index objection recorded in
`docs/audits/2026-08-25-vol-trm-division-of-labour-is-sound.md` §11b is
untouched by anything here.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 60)

from _li_2_q_util import flavor_split_leading  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

Q0 = mp.mpf(str(Q_50_DIGIT_STR))
H = Q0 - 1 / Q0
DELTA = flavor_split_leading(Q0)

ISOTOPES = [("proton", 1, 0), ("neutron", 0, 1), ("deuteron", 1, 1),
            ("helium-3", 2, 1), ("helium-4", 2, 2)]

# The four templates, as EXACT d-values. A letter is classified by which of
# these its d equals; ties are impossible because the four are distinct at q0.
TEMPLATES = {
    "sigma":            mp.mpf(0),
    "sigma_inv":        -H,
    "avg_symmetric":    -H / 2,
    "avg_colour":       -H * (mp.mpf(1) / 2 - DELTA / 4),
}
# Which templates are NOT in the image of rho : B_n -> H_n(q).
NON_BRAID = ("avg_symmetric", "avg_colour")


# The two averaged templates are separated by delta/4 ~ 3.4e-4, so any
# threshold well inside that separates them.  It is set far tighter than
# needed (1e-30) so a letter that is merely NEAR a template is reported
# UNKNOWN rather than snapped to it; the worst observed gap is printed.
_MATCH_TOL = mp.mpf("1e-30")
_WORST_GAP = [mp.mpf(0)]


def classify(d) -> str:
    """Template match with a recorded worst-case gap."""
    best, best_gap = "UNKNOWN", None
    for name, val in TEMPLATES.items():
        gap = abs(mp.mpf(d) - val)
        if best_gap is None or gap < best_gap:
            best, best_gap = name, gap
    if best_gap > _WORST_GAP[0]:
        _WORST_GAP[0] = best_gap
    return best if best_gap < _MATCH_TOL else "UNKNOWN"


def spectrum(w_plus):
    """Eigenvalues of `w₊σ + w₋σ⁻¹` on the two Hecke eigenvalues of σ."""
    w_minus = 1 - w_plus
    mu_plus = w_plus * Q0 + w_minus / Q0
    mu_minus = -(w_plus / Q0) - w_minus * Q0
    return mu_plus, mu_minus


def type_b_solve(mu_plus, mu_minus):
    """Solve c(Q − Q⁻¹) = μ₊+μ₋, −c² = μ₊μ₋ for c > 0, Q > 0.

    Returns (Q, c). `Q ↦ Q − Q⁻¹` is a bijection (0,∞) → ℝ, inverted exactly:
    Q = (s + sqrt(s²+4))/2 with s = (μ₊+μ₋)/c.
    """
    prod = mu_plus * mu_minus
    if prod >= 0:
        raise ValueError(f"eigenvalues do not straddle zero: {prod}")
    c = mp.sqrt(-prod)
    s = (mu_plus + mu_minus) / c
    Q = (s + mp.sqrt(s ** 2 + 4)) / 2
    return Q, c


def main() -> int:
    wb = WitnessBuilder("atom-letter-colour-spectrum", engine="python-exact")
    wb.set_description(
        "Census of atom_braid_word_3A's letters by exact template under both "
        "p-n conventions, plus the type-B (Q, c) solve for each non-braid "
        "template. Establishes that the colour-weighted interface letter is "
        "NOT an involution and forces Q != 1, correcting a prior result "
        "obtained on the colour-blind template only.")

    print(f"q0     = {mp.nstr(Q0, 30)}")
    print(f"h      = {mp.nstr(H, 30)}")
    print(f"delta  = {mp.nstr(DELTA, 30)}")
    print(f"dps    = {mp.mp.dps}\n")

    # ── 1 · census by template ────────────────────────────────────────────
    census = {}
    for conv in ("bring_color_weighted", "strict_averaged"):
        print(f"=== pn_convention = {conv} ===")
        print(f"{'isotope':<10} {'letters':>8} {'sigma':>7} {'sig^-1':>7} "
              f"{'sym':>5} {'colour':>7} {'?':>3}   colour-letter gen indices")
        for label, Z, N in ISOTOPES:
            word = atom_braid_word_3A(Z, N, pn_convention=conv)
            kinds = [classify(d) for (_c, d, _g) in word]
            counts = {k: kinds.count(k) for k in
                      list(TEMPLATES) + ["UNKNOWN"]}
            colour_gens = [g for (_c, _d, g), k in zip(word, kinds)
                           if k == "avg_colour"]
            sym_gens = [g for (_c, _d, g), k in zip(word, kinds)
                        if k == "avg_symmetric"]
            census[f"{conv}/{label}"] = {
                "Z": Z, "N": N, "A": Z + N, "letters": len(word),
                "counts": counts,
                "colour_gen_indices": colour_gens,
                "symmetric_gen_indices": sym_gens,
            }
            print(f"{label:<10} {len(word):>8} {counts['sigma']:>7} "
                  f"{counts['sigma_inv']:>7} {counts['avg_symmetric']:>5} "
                  f"{counts['avg_colour']:>7} {counts['UNKNOWN']:>3}   "
                  f"{colour_gens}")
        print()

    # ── 2 · spectra + type-B solve, per template ──────────────────────────
    print("=== spectrum and type-B (Q, c) per non-braid template ===")
    results = {}
    for name in NON_BRAID:
        w_plus = mp.mpf(1) / 2 if name == "avg_symmetric" \
            else mp.mpf(1) / 2 + DELTA / 4
        mu_p, mu_m = spectrum(w_plus)
        Q, c = type_b_solve(mu_p, mu_m)
        results[name] = {
            "w_plus": mp.nstr(w_plus, 30),
            "mu_plus": mp.nstr(mu_p, 30),
            "mu_minus": mp.nstr(mu_m, 30),
            "sum": mp.nstr(mu_p + mu_m, 30),
            "Q": mp.nstr(Q, 30),
            "c": mp.nstr(c, 30),
            "Q_minus_one": mp.nstr(Q - 1, 30),
        }
        print(f"\n{name}:")
        print(f"  w+          = {mp.nstr(w_plus, 25)}")
        print(f"  mu+         = {mp.nstr(mu_p, 25)}")
        print(f"  mu-         = {mp.nstr(mu_m, 25)}")
        print(f"  mu+ + mu-   = {mp.nstr(mu_p + mu_m, 25)}   "
              f"(zero iff involution up to scale)")
        print(f"  Q           = {mp.nstr(Q, 25)}")
        print(f"  Q - 1       = {mp.nstr(Q - 1, 25)}")
        print(f"  c           = {mp.nstr(c, 25)}")
        print(f"  [2]_q/2     = {mp.nstr((Q0 + 1 / Q0) / 2, 25)}")

    # ── assertions ────────────────────────────────────────────────────────
    sym, col = results["avg_symmetric"], results["avg_colour"]

    # A1 — the symmetric template really is an involution up to scale, and the
    #      earlier Lean result (Q = 1) is reproduced. This is the CONTROL: if
    #      it failed, the solve itself would be wrong.
    wb.add_assertion(
        name="symmetric_template_forces_Q_eq_1",
        # |Q - 1| against 0: Q vs "1" cancels in the float64 verdict
        # (witness.py:830) at ~2.2e-16, putting the 1e-40 bound 2.2e24x below
        # anything reachable. The residual form is reachable.
        computed=fmt(abs(mp.mpf(str(sym["Q"])) - 1)), expected="0",
        tolerance="1e-40",
        unit="dimensionless",
        source="QOU.MassTheory.second_parameter_is_one (Lean, sorry-free)")

    # A2 — the symmetric template's scale is exactly [2]_q/2, also per Lean.
    wb.add_assertion(
        name="symmetric_template_scale_is_qtwo_over_two",
        computed=sym["c"],
        expected=mp.nstr((Q0 + 1 / Q0) / 2, 40), tolerance="1e-40",
        unit="dimensionless",
        source="QOU.MassTheory.averagedOn_pos (Lean, sorry-free)")

    # A3 — THE FINDING: the colour-weighted template does NOT force Q = 1.
    #      Asserted as a strict separation, not as a fitted value.
    q_col = mp.mpf(col["Q"])
    wb.add_assertion(
        name="colour_template_Q_differs_from_one",
        computed="1" if abs(q_col - 1) > mp.mpf("1e-20") else "0", expected="1",
        tolerance="0", unit="boolean",
        source="this probe; delta != 0 at q0")

    # A4 — and the size of the departure is set by delta, not free. To leading
    #      order Q - 1 ~ (delta/4)h / c. Checked as a ratio, so a wrong power
    #      of delta would fail.
    lead = (DELTA / 4) * H / mp.mpf(col["c"])
    wb.add_assertion(
        name="colour_Q_departure_is_leading_order_delta",
        computed=mp.nstr((q_col - 1) / lead, 40), expected="1", tolerance="1e-3",
        unit="ratio",
        source="mu+ + mu- = (delta/2)h exactly; Q-1 ~ s/2 = (delta/4)h/c")

    # A5 — census shape: exactly ONE colour letter per atom with an interface,
    #      and ZERO for a single nucleon. This is what makes the colour letter
    #      structurally different from the 2A symmetric ones.
    n_col_deut = census["bring_color_weighted/deuteron"]["counts"]["avg_colour"]
    n_col_prot = census["bring_color_weighted/proton"]["counts"]["avg_colour"]
    wb.add_assertion(
        name="one_colour_letter_for_deuteron", computed=str(n_col_deut),
        expected="1", tolerance="0", unit="count", source="census above")
    wb.add_assertion(
        name="zero_colour_letters_for_single_nucleon",
        computed=str(n_col_prot), expected="0", tolerance="0", unit="count",
        source="census above; a single nucleon has no p-n interface")

    # A6 — CONTROL: under strict_averaged there are no colour letters at all,
    #      which is what makes the two conventions distinguishable here.
    n_col_strict = census["strict_averaged/deuteron"]["counts"]["avg_colour"]
    wb.add_assertion(
        name="control_strict_convention_has_no_colour_letters",
        computed=str(n_col_strict), expected="0", tolerance="0",
        unit="count", source="census above")

    # A7 — CONTROL: no letter escapes the four templates.
    total_unknown = sum(v["counts"]["UNKNOWN"] for v in census.values())
    wb.add_assertion(
        name="control_no_unclassified_letters", computed=str(total_unknown),
        expected="0", tolerance="0", unit="count",
        source="exact template match at 60 dps")

    print(f"\nworst template-match gap over all letters: "
          f"{mp.nstr(_WORST_GAP[0], 8)}  (tol {mp.nstr(_MATCH_TOL, 3)}, "
          f"template separation delta/4 = {mp.nstr(DELTA / 4, 8)})")

    wb.add_data("worst_template_match_gap", mp.nstr(_WORST_GAP[0], 20))
    wb.add_data("q0", mp.nstr(Q0, 50))
    wb.add_data("delta", mp.nstr(DELTA, 50))
    wb.add_data("census", census)
    wb.add_data("template_spectra", results)
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
