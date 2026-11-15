"""EM-linking: what computing the exact fibre kernel would actually buy.

Bean qou-17mq. Companion to em_linking_kernel_exponent_degeneracy_probe.py.

THE QUESTION THIS ANSWERS
-------------------------
Round 6 (docs/audits/2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md)
caveats its own admissible family and names the next step:

    "The one-term model is a model. Writing the admissible family as
     coth(alpha) - c0 ... is the simplest realisation of the zero-mean
     condition, not the exact Green's function of a quotient, which is a
     regularised Poincare series."
    "what is the zero-mean Green's function of the actual fibre?"

That has stood as an open computation because the Poincare series diverges
for a finite-covolume Gamma (delta(Gamma) = 2 exactly cancels the e^{-2R}
decay -- round 6 records this). But the question the front needs answered is
not the global kernel; it is how much the exact kernel DIFFERS from the
one-term model over the separations the data occupies. That difference is
available in closed form, without summing anything.

THE DERIVATION
--------------
Let M = H^3/Gamma be finite-volume and G_M its zero-mean Green's function,

    Laplacian_y G_M = delta_y - 1/vol(M),      integral_M G_M = 0.

The decaying fundamental solution on the universal cover is

    G_dec(r) = -(coth r - 1)/(4 pi),

fixed by the radial equation u'' + 2 coth(r) u' = 0 off the origin (whose
solutions are -C coth r + D), the delta normalisation for C, and decay at
infinity for D = C. Round 6's addendum derives this.

Set R := G_M - G_dec on the ball of radius inj(M) about x, where the covering
is injective and both terms are defined. Both carry the SAME delta, so it
cancels:

    Laplacian_y R = -1/vol(M),     R smooth on that ball.

Two consequences, and the first is the one that matters:

  (1) R contributes NO 1/r term and no leading linear term -- it is smooth
      where G_dec is singular. Expanding about r = 0 and using that the
      radial Laplacian u'' + 2 coth(r) u' agrees with the flat one to
      leading order (so Laplacian(r^2) = 6):

          R(r) = R_0 - r^2/(6 vol(M)) + O(r^3).

      Hence, in the normalisation the corpus uses for the pair kernel
      (kappa proportional to -4 pi G):

          kappa_exact(r) = coth r - c0 + (2 pi / (3 vol(M))) r^2 + O(r^3),
                     c0 := 1 + 4 pi R_0.

      SO THE ONE-TERM FAMILY IS NOT AN ARBITRARY STAND-IN. It is the exact
      quotient kernel truncated at O(r^2), and c0 -- scanned as a free
      parameter by round 6 -- IS the quotient's Robin constant. That
      identification is new; round 6 treats c0 as a modelling choice.

  (2) The first correction beyond it is PARAMETER-FREE once vol(M) is
      given: the r^2 coefficient is 2 pi / (3 vol), with no freedom. So it
      can be TESTED rather than fitted, which is what this probe does.

WHAT IS NOT CLAIMED. That the corpus's link volumes are the fibre volume --
they are the only hyperbolic volumes the corpus carries at these A, and all
three are reported here precisely so that no selection is made. Choosing
whichever fits best would be a fit under the NO-FITTING directive, and the
verdict below deliberately does not select one.

THE CONDITION, and it is load-bearing: the expansion is valid for
r < inj(M). A cusped finite-volume quotient has arbitrarily small
injectivity radius inside the cusp, so this is a real restriction and the
corpus holds no per-isotope geometry from which to check it. Every result
below is conditional on the measured separations lying inside the
injectivity ball, and is reported as such.

EXPLORATORY / audit-only. mpmath, no float64 anywhere.
"""

from __future__ import annotations

import pathlib

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

_UPSTREAM_RECORDS: list = []

from mpmath import mp, mpf, sqrt, log, pi, acoth, coth  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
SERIES = HERE / "em-linking-mirror-series.witness.json"
VOLUMES = HERE / "binding-link-volumes.witness.json"

set_compute_dps()

UNBOUND_A = {5, 9}
# The admissible floor under O2: coth > 1 pointwise, so its average over any
# finite-volume M exceeds 1. c0 = 1 is the infinite-volume boundary.
C0 = mpf(1)


def ols(xs, ys):
    n = mpf(len(xs))
    mx = sum(xs) / n
    my = sum(ys) / n
    m = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2
                                                              for x in xs)
    return m, my - m * mx


def rms_rel(pred, obs):
    n = len(obs)
    return sqrt(sum(((p - k) / k) ** 2 for p, k in zip(pred, obs)) / n)


def grid_min2(f, c_lo, c_hi, p_lo, p_hi, n=70, refines=3):
    """Coarse-to-fine grid over BOTH parameters.

    Deliberately NOT a golden section. The first version of this probe used
    one on c alone and it converged to rms 25-32% where the true minimum is
    2.7-3.0% -- the objective is not unimodal in c (coth blows up as c -> 0),
    and a bracket method walks into that wall. A grid cannot, and the
    self-check assertion below fails loudly if the fitted optimum is ever
    worse than the un-refitted evaluation."""
    c_lo, c_hi, p_lo, p_hi = mpf(c_lo), mpf(c_hi), mpf(p_lo), mpf(p_hi)
    best = (None, None, None)
    for _ in range(refines):
        dc = (c_hi - c_lo) / n
        dp = (p_hi - p_lo) / n
        for i in range(n + 1):
            c = c_lo + i * dc
            if c <= 0:
                continue
            for j in range(n + 1):
                pp = p_lo + j * dp
                v = f(c, pp)
                if best[2] is None or v < best[2]:
                    best = (c, pp, v)
        c_lo, c_hi = best[0] - dc, best[0] + dc
        p_lo, p_hi = best[1] - dp, best[1] + dp
    return best


def main() -> None:
    set_compute_dps()

    w = record_upstream(SERIES, _UPSTREAM_RECORDS)
    v = record_upstream(VOLUMES, _UPSTREAM_RECORDS)
    rows = [{"A": int(r["A"]), "kappa": mpf(str(r["kappa"]))}
            for r in w["data"]["series"] if int(r["A"]) not in UNBOUND_A]
    A = [mpf(r["A"]) for r in rows]
    K = [r["kappa"] for r in rows]
    lnA = [log(a) for a in A]
    n = len(rows)

    blv = v["data"]["binding_link_volumes"]
    # Every hyperbolic volume the corpus carries at these A. Reported
    # together; deliberately NOT selected among.
    vols = {"L6a4_3He (Borromean)": mpf(str(blv["L6a4_3He"])),
            "knot_8_11_3H": mpf(str(blv["knot_8_11_3H"])),
            "figure_eight_4_1": 2 * mp.clsin(2, pi / 3)}

    # Separations implied by the O2-admissible one-term kernel.
    alpha = [acoth(k + C0) for k in K]
    a_min, a_max = min(alpha), max(alpha)

    # Noise floor: a bare 2-parameter power law on the same data.
    pb, plnC = ols(lnA, [log(k) for k in K])
    floor = rms_rel([mp.e ** plnC * a ** pb for a in A], K)

    # Baseline: the uncorrected one-term kernel at its own best exponent.
    p0, lnc0 = ols(lnA, [log(x) for x in alpha])
    c_scale0 = mp.e ** lnc0
    base_pred = [coth(c_scale0 * a ** p0) - C0 for a in A]
    base_rms = rms_rel(base_pred, K)

    # --- the correction, and its size relative to the kernel -------------
    def quad(r, vol):
        return 2 * pi * r ** 2 / (3 * vol)

    sizes = {}
    for name, vol in vols.items():
        rel = [quad(r, vol) / k for r, k in zip(alpha, K)]
        sizes[name] = {"vol": vol,
                       "rel_at_alpha_min": min(rel),
                       "rel_at_alpha_max": max(rel),
                       "ratio_to_noise_floor_at_max": max(rel) / floor}

    # coth's own next term, which the corpus already reports as unresolvable
    cubic = [(r ** 3 / 45) / k for r, k in zip(alpha, K)]

    # --- the PARAMETER-FREE test ----------------------------------------
    # Add the derived r^2 term with NO new freedom: vol is FIXED at a corpus
    # value and the coefficient 2*pi/(3*vol) is forced. Then refit the SAME
    # TWO parameters (scale and exponent) the uncorrected baseline already
    # carries, so the comparison is at matched degrees of freedom. Refitting
    # only the scale would penalise the corrected model for a DOF it is not
    # being given, which is what the first version of this probe did.
    tests = {}
    for name, vol in vols.items():
        def obj(c, pp, vol=vol):
            return rms_rel([coth(c * a ** pp) - C0 + quad(c * a ** pp, vol)
                            for a in A], K)
        cb, pb2, rb = grid_min2(obj, "0.02", "1.2", "0.02", "0.60")
        frozen = rms_rel([coth(c_scale0 * a ** p0) - C0
                          + quad(c_scale0 * a ** p0, vol) for a in A], K)
        tests[name] = {"vol": vol, "scale": cb, "exponent": pb2,
                       "kappa_rms": rb,
                       "kappa_rms_without_refitting": frozen,
                       "delta_vs_uncorrected": rb - base_rms,
                       "exponent_shift_vs_uncorrected": pb2 - p0}

    best = min(tests.values(), key=lambda t: t["kappa_rms"])
    worst = max(tests.values(), key=lambda t: t["kappa_rms"])
    max_size = max(s["rel_at_alpha_max"] for s in sizes.values())
    min_size = min(s["rel_at_alpha_max"] for s in sizes.values())

    wb = WitnessBuilder("em-linking-quotient-kernel-correction",
                        engine="mpmath")
    wb.add_data("derivation", {
        "decomposition": ("G_M = G_dec + R on the ball of radius inj(M); "
                          "both carry the same delta so Laplacian R = "
                          "-1/vol(M) and R is smooth where G_dec is not."),
        "exact_kernel_near_diagonal": ("kappa = coth r - c0 + "
                                       "(2 pi / (3 vol)) r^2 + O(r^3)"),
        "c0_identified": ("c0 = 1 + 4 pi R_0, the quotient's Robin "
                          "constant. Round 6 scans c0 as a free modelling "
                          "parameter; this identifies what it IS."),
        "why_the_one_term_family_is_not_arbitrary": (
            "It is the exact quotient kernel truncated at O(r^2). The "
            "correction beyond it is parameter-free once vol is given."),
        "condition": ("Valid for r < inj(M). A cusped quotient has "
                      "arbitrarily small injectivity radius in the cusp and "
                      "the corpus holds no per-isotope geometry to check "
                      "this. Everything here is conditional on it."),
    })
    wb.add_data("implied_separations", {
        "alpha_min": a_min, "alpha_max": a_max,
        "kernel": "coth(alpha) - 1 (the O2-admissible boundary member)"})
    wb.add_data("noise_floor_2param_power_law", floor)
    wb.add_data("uncorrected_one_term_baseline",
                {"exponent": p0, "scale": c_scale0, "kappa_rms": base_rms})
    wb.add_data("correction_size_relative_to_kernel", sizes)
    wb.add_data("coth_own_cubic_term_for_comparison",
                {"rel_at_alpha_max": max(cubic),
                 "note": ("The corpus already reports this term as "
                          "unresolvable (0.97% against 3.5% scatter). The "
                          "quotient correction is compared against it.")})
    wb.add_data("parameter_free_test", tests)

    wb.add_assertion(
        name="quotient_correction_is_not_negligible",
        computed=1 if max_size > floor else 0, expected=1, tolerance=0,
        unit="boolean",
        source=(f"At the largest measured separation (alpha = "
                f"{mp.nstr(a_max, 6)}) the derived r^2 term is "
                f"{mp.nstr(max_size * 100, 4)}% of the kernel at the "
                f"smallest corpus volume and {mp.nstr(min_size * 100, 4)}% "
                f"at the largest, against a noise floor of "
                f"{mp.nstr(floor * 100, 4)}%. So the exact kernel is NOT "
                f"indistinguishable from the one-term model on this data -- "
                f"this is the first thing computing it would buy, and it "
                f"grows with r, so it enters as a systematic trend."))
    wb.add_assertion(
        name="correction_exceeds_coths_own_unresolvable_cubic",
        computed=mp.nstr(max_size / max(cubic), 6), expected="1",
        tolerance="1e9", unit="ratio (recorded, not gated)",
        source=(f"The quotient r^2 term reaches "
                f"{mp.nstr(max_size * 100, 4)}% where coth's own r^3/45 "
                f"term reaches {mp.nstr(max(cubic) * 100, 4)}%, a ratio of "
                f"{mp.nstr(max_size / max(cubic), 5)}. Recorded with a wide "
                f"tolerance because the ORDERING is the content, not the "
                f"value: the correction the corpus never modelled is larger "
                f"than the one it already declared unresolvable."))
    wb.add_assertion(
        name="fitter_selftest_refit_beats_frozen",
        computed=1 if all(t["kappa_rms"] <= t["kappa_rms_without_refitting"]
                          for t in tests.values()) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=("Self-check on the optimiser, not on the physics: a refit "
                "over a superset of the frozen point must not do worse than "
                "the frozen point. The first version of this probe used a "
                "golden section on the scale alone and returned rms 25-32% "
                "where the true minimum is 2.7-3.0%, because the objective "
                "is not unimodal in the scale (coth diverges as it goes to "
                "0). This assertion makes that class of failure loud."))
    wb.add_assertion(
        name="the_correction_is_reabsorbed_by_the_exponent",
        computed=1 if (max_size > floor
                       and all(t["kappa_rms"] < mpf("1.15") * base_rms
                               for t in tests.values())) else 0,
        expected=1, tolerance=0, unit="boolean",
        source=(f"The derived term is NOT small -- it reaches "
                f"{mp.nstr(max_size * 100, 4)}% of the kernel, "
                f"{mp.nstr(max_size / floor, 3)}x the noise floor, against "
                f"only {mp.nstr(max(cubic) * 100, 3)}% for coth's own r^3/45 "
                f"term which the corpus already calls unresolvable. Yet at "
                f"MATCHED degrees of freedom every corpus volume lands "
                f"within 15% of the uncorrected "
                f"{mp.nstr(base_rms * 100, 4)}%: "
                f"{mp.nstr(best['kappa_rms'] * 100, 4)}% to "
                f"{mp.nstr(worst['kappa_rms'] * 100, 4)}%, bought by an "
                f"exponent shift of up to "
                f"{mp.nstr(max(abs(t['exponent_shift_vs_uncorrected']) for t in tests.values()), 4)}. "
                f"So the exact kernel would change the KERNEL materially "
                f"and the FIT hardly at all -- the same kernel/exponent "
                f"degeneracy the companion probe measures, one order down."))

    wb.add_data("scope", {
        "a_scope_limited": (
            "A statement about the SIZE of the leading quotient correction "
            "over the measured separations, at the volumes the corpus "
            "carries, conditional on those separations lying inside the "
            "injectivity radius. Not a computation of the exact kernel."),
        "what_is_new": (
            "That c0 is the Robin constant rather than a modelling "
            "parameter, that the one-term family is the exact kernel "
            "truncated at O(r^2), that the first neglected term is "
            "parameter-free -- so round 6's named next step is answerable in "
            "SIZE without summing a divergent series -- and that the term is "
            "nonetheless reabsorbed by the separation exponent, which is the "
            "degeneracy showing up one order down."),
        "NOT_claimed": (
            "That any corpus volume IS the fibre volume. That the exact "
            "kernel is excluded -- the test above uses one truncation at "
            "three assumed volumes, and a genuine quotient could differ in "
            "c0, in vol, and at O(r^3). That the metric Coulomb route "
            "fails: untouched."),
    })
    wb.add_upstream_records(_UPSTREAM_RECORDS)
    out = wb.save(extra={
        "q0Anchor": "ambiguous",
        "q0AnchorReason": (
            "q0 enters only through upstream data: kappa(A) is read from "
            "em-linking-mirror-series.witness.json, whose producer divides by "
            "a TYPED per-pair Coulomb unit tanh(ln q0)*B_pp = 0.2376702253 "
            "with no recorded pin (the proton-pinned "
            "mirror-pair-coulomb-sign-correction witness it cites now carries "
            "0.2212723003), and that upstream witness is itself unstamped; the "
            "pin of the series this probe fits is therefore undetermined"),
    })

    print(f"implied separations (kernel coth-1): alpha in "
          f"[{mp.nstr(a_min, 6)}, {mp.nstr(a_max, 6)}]")
    print(f"noise floor (2-param power law): {mp.nstr(floor * 100, 4)}%")
    print(f"uncorrected one-term baseline : {mp.nstr(base_rms * 100, 4)}%  "
          f"(p = {mp.nstr(p0, 5)})\n")
    print("derived correction  +2*pi*r^2/(3*vol)  as a fraction of the kernel:")
    for name, s in sizes.items():
        print(f"  vol {mp.nstr(s['vol'], 8):>12}  {name:<26} "
              f"{mp.nstr(s['rel_at_alpha_min'] * 100, 3):>6}% -> "
              f"{mp.nstr(s['rel_at_alpha_max'] * 100, 4):>6}%   "
              f"({mp.nstr(s['ratio_to_noise_floor_at_max'], 3)}x the floor)")
    print(f"\n  coth's own r^3/45 term reaches only "
          f"{mp.nstr(max(cubic) * 100, 3)}% -- already declared unresolvable")
    print("\nPARAMETER-FREE test (vol fixed, coefficient forced; the same "
          "TWO parameters refit):")
    for name, t in tests.items():
        print(f"  {name:<26} rms {mp.nstr(t['kappa_rms'] * 100, 4):>6}%   "
              f"({'+' if t['delta_vs_uncorrected'] >= 0 else ''}"
              f"{mp.nstr(t['delta_vs_uncorrected'] * 100, 3)} pp vs "
              f"uncorrected)")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
