#!/usr/bin/env python3
"""Every derived weighting overshoots AME by ~2x, and no natural one rescues it.

Bean qou-6tcn. Follow-on from `binding_cut_entropy_sign_is_forced_probe.py`,
which built the proton|neutron cut entropy but chose no weighting over the
Wedderburn blocks -- because choosing one to hit AME would be a fit. This probe
enumerates the weightings that have INDEPENDENT provenance, computes all of
them once, and reports what comes out. None is selected and none is tuned.

THE QUESTION
============
`S_cut` is defined per block. A state is a distribution `p_lambda` over blocks,
and only then does `E_0 * S_cut` have a value. Is there a DERIVED `p_lambda` --
one the framework already fixes for its own reasons -- under which
`E_0 * S_cut = B_AME`?

Under convention D only the four two-row blocks exist (the rest span the
Temperley-Lieb ideal, addendum 19). Conveniently the cut is closed on them:
`c^lambda_{mu,nu} != 0` requires `mu, nu` contained in `lambda`, so a two-row
`lambda` restricts entirely inside `TL_3 (x) TL_3`. No truncation is needed and
none is imposed.

The reduced state on the proton side is block-diagonal in the `mu`-isotypic
decomposition, with eigenvalue `A_mu = sum_lambda p_lambda a^lambda_mu` of
multiplicity `f^mu`, where `a^lambda_mu = sum_nu c^lambda_{mu,nu} f^nu /
f^lambda`. So `S_vN = -sum_mu f^mu A_mu ln A_mu`. (The earlier probe reported
the SECTOR entropy `-sum_{mu,nu} P ln P`, a different and larger quantity. Both
are non-negative and both vanish on a product, so the sign theorem there is
unaffected; this one is the von Neumann entropy of the reduced density matrix
and is the right thing to compare against an energy.)

THE FOUR WEIGHTINGS -- two derived, two controls
================================================
W1  Markov / Plancherel, `p = y_lambda f^lambda`. The framework's own trace
    weights, taken from the EXACT closed form of
    `prop:markov-trace-frobenius-selection`,
    `y_{(n-k,k)} = [n-2k+1]_q / [2]_q^n`. State-independent. Sums to 1 by M1.
W2  Born, state-dependent, `p = t_lambda / tr_M(beta_D)` with
    `t_lambda = y_lambda chi^lambda(beta_D)`. The deuteron braid's OWN block
    distribution -- a genuine probability vector because all four support
    characters are positive (addendum 17).
W3  classical Plancherel `p ~ (f^lambda)^2`  -- CONTROL, q-independent.
W4  uniform on the support                   -- CONTROL, structure-free.

MEASURED at the proton pin, `E_0 = m_e / (q_0 (q_0 - 1)) = 4.185981 MeV`,
`B_AME(2H) = 2.224566`, so AME needs `S_vN = 0.531432`:

    weighting                          S_vN      E_0*S_vN     vs B_AME
    W1 Markov/Plancherel  (EXACT)    1.035920     4.33633      1.949x
    W2 Born, deuteron                0.896974     3.75471      1.688x
    W3 classical Plancherel  CTRL    1.096580     4.59024      2.063x
    W4 uniform               CTRL    1.014390     4.24623      1.909x

**All four overshoot, by 1.69x to 2.06x.** No derived weighting reaches AME.

WHY THE OVERSHOOT IS ROBUST, NOT A KNOB
=======================================
Entropy is concave, so its minimum over weightings sits at a vertex. The four
vertices are

    delta_(6)     S_vN = 0.000000     0.000x B     <- the trivial block
    delta_(5,1)   S_vN = 0.950271     1.788x B
    delta_(4,2)   S_vN = 1.098612     2.067x B
    delta_(3,3)   S_vN = 1.054920     1.985x B

Every NON-trivial block lands in 1.79x - 2.07x. The only low value in the whole
simplex is the trivial block, which carries no cut structure at all -- it
restricts to a single `(mu,nu)` and is by definition a product. Reaching AME
from W1 requires moving **69.3 % of the total weight onto `(6)`**, taking
`p_(6)` from 0.1153 to 0.7282 -- a **6.31x** concentration on the one block that
says nothing.

This SHARPENS the caveat the previous probe attached to itself. That one warned
that a weighting over blocks spanning `[0, 1.4708]` could hit almost anything in
the interval, so being in range was genericity rather than evidence. True in
principle; **false for the derived candidates.** They do not span the interval.
They cluster in a band a factor of ~2 above the target, and the escape route is
the one block with no content. So this is a robust negative, not a free
parameter -- which is a more useful result than either a hit or a fit.

THE NEAR-2 IS NOT A RESULT
==========================
W1 gives 1.9493x, which is 2.6 % from exactly 2. In a framework whose accuracy
targets are quoted in ppb, 2.6 % is not agreement, and "close to 2" is exactly
the kind of observation the anti-numerology discipline exists to stop. It is
recorded as a number, asserted as NOT equal to 2, and not pursued.

SCOPE -- (a) throughout
=======================
MEASURED: the four weightings and their entropies; the vertex entropies; the
concentration AME would require; that the exact closed-form `y_lambda`
reproduces the committed Frobenius Gram.

NOT claimed: that `E_0 * S_cut` should equal B, or that this refutes an
entanglement-cost contribution to binding -- an overshoot by 2x with the right
sign and the right order of magnitude is not an exclusion, and a term that
enters with a coefficient, or alongside others, is untouched by this. Nor is
any statement made beyond 2H: the LR branching data exists only for the
deuteron, so this is ONE isotope. A single point could not have distinguished a
derivation from a coincidence even had it hit.
"""

from __future__ import annotations

import json
import pathlib
import sys
from math import factorial

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    M_E_MEV  # noqa: E402,
)
from q_parameter import Q as Q0  # noqa: E402
from q_parameter import Q_MP  # noqa: E402 — exact mpf, not the f64 twin
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 50)

HERE = pathlib.Path(__file__).resolve().parent
BRANCH = HERE.parent / "sublemma-2-1-deuteron-branching.witness.json"
SDP = HERE.parent / "deuteron-real-sdp.witness.json"
SUPPORT = ["(6,)", "(5, 1)", "(4, 2)", "(3, 3)"]
N = 6


def hook_dim(lam):
    lam = tuple(lam)
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= (row - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def main() -> int:
    wb = WitnessBuilder("binding-cut-entropy-derived-weightings",
                        engine="python-exact")
    wb.set_description(
        "Enumerates every block weighting with independent provenance and "
        "computes E_0*S_vN of the proton|neutron cut entropy against "
        "B_AME(2H). All four overshoot by 1.69x-2.06x; none is selected or "
        "tuned. The overshoot is robust: every non-trivial vertex of the "
        "weight simplex lands in 1.79x-2.07x, and reaching AME needs 69.3% of "
        "the weight moved onto the trivial block (6,), a 6.31x concentration "
        "on the one block carrying no cut structure.")

    q0 = Q_MP
    me = mp.mpf(str(M_E_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    B = AME_B_DEUTERON_MEV_VALIDATION
    need = B / E0

    def qint(m):
        return (q0 ** m - q0 ** (-m)) / (q0 - 1 / q0)

    # W1 — EXACT closed form from prop:markov-trace-frobenius-selection
    y = {s: qint(N - 2 * k + 1) / qint(2) ** N for k, s in enumerate(SUPPORT)}
    w1 = {s: y[s] * hook_dim(eval(s)) for s in SUPPORT}  # noqa: S307

    sdp = json.loads(SDP.read_text())["data"]
    gram = {k: mp.mpf(str(v)) for k, v in
            zip(sdp["partitions"], sdp["frobenius_gram_diag"])}
    t = {k: mp.mpf(str(v)) for k, v in
         zip(sdp["partitions"], sdp["cost_t_lambda"])}
    n_target = mp.mpf(str(sdp["n_target"]))
    gram_agree = max(abs(w1[s] - gram[s]) / gram[s] for s in SUPPORT)

    w2 = {s: t[s] / n_target for s in SUPPORT}
    tot = sum(hook_dim(eval(s)) ** 2 for s in SUPPORT)          # noqa: S307
    w3 = {s: mp.mpf(hook_dim(eval(s)) ** 2) / tot for s in SUPPORT}  # noqa: S307
    w4 = {s: mp.mpf(1) / len(SUPPORT) for s in SUPPORT}
    WEIGHTS = [("W1_markov_plancherel_exact", w1, True),
               ("W2_born_deuteron", w2, True),
               ("W3_classical_plancherel_CONTROL", w3, False),
               ("W4_uniform_CONTROL", w4, False)]

    lr = json.loads(BRANCH.read_text())["lr_breakdown_per_lambda"]

    def a_vector(lam_s):
        fl = hook_dim(eval(lam_s))                               # noqa: S307
        a = {}
        for term in lr[lam_s]:
            mu = tuple(term["mu"])
            a[mu] = a.get(mu, mp.mpf(0)) + mp.mpf(
                term["c"] * hook_dim(term["nu"])) / fl
        return a

    def s_vn(p):
        A = {}
        for lam_s, pl in p.items():
            for mu, v in a_vector(lam_s).items():
                A[mu] = A.get(mu, mp.mpf(0)) + pl * v
        return -mp.fsum(hook_dim(mu) * A[mu] * mp.log(A[mu])
                        for mu in A if A[mu] > 0)

    rows, norm_ok = {}, 0
    for name, p, _derived in WEIGHTS:
        norm_ok += (abs(mp.fsum(p.values()) - 1) < mp.mpf("1e-14"))
        S = s_vn(p)
        rows[name] = {"S_vN": mp.nstr(S, 24),
                      "E0_S_vN_MeV": mp.nstr(E0 * S, 24),
                      "ratio_to_B_AME": mp.nstr(E0 * S / B, 24)}

    verts = {s: s_vn({s: mp.mpf(1)}) for s in SUPPORT}
    ratios = [mp.mpf(r["ratio_to_B_AME"]) for r in rows.values()]
    n_reach = sum(1 for r in ratios if r <= 1)
    nontrivial = [E0 * verts[s] / B for s in SUPPORT if verts[s] > 0]

    # concentration onto (6,) needed to drag W1 down to AME
    def mix(x):
        p = {s: (1 - x) * w1[s] for s in SUPPORT}
        p["(6,)"] += x
        return p

    lo, hi = mp.mpf(0), mp.mpf(1)
    for _ in range(200):
        m = (lo + hi) / 2
        if s_vn(mix(m)) > need:
            lo = m
        else:
            hi = m
    concentration = mix(lo)["(6,)"] / w1["(6,)"]

    print(f"E0 = {mp.nstr(E0, 12)} MeV (proton pin)   B_AME(2H) = {B}   "
          f"required S_vN = {mp.nstr(need, 8)}\n")
    print(f"{'weighting':<36}{'S_vN':>10}{'E0*S_vN':>11}{'vs B':>9}")
    for name, r in rows.items():
        print(f"{name:<36}{float(mp.mpf(r['S_vN'])):>10.6f}"
              f"{float(mp.mpf(r['E0_S_vN_MeV'])):>11.5f}"
              f"{float(mp.mpf(r['ratio_to_B_AME'])):>8.4f}x")
    print(f"\nvertices (entropy is concave -> the minimum is here):")
    for s in SUPPORT:
        print(f"  delta_{s:<10} S_vN = {float(verts[s]):.6f}   "
              f"{float(E0 * verts[s] / B):.4f}x B")
    print(f"\nto reach AME from W1: move {float(lo) * 100:.1f}% of the weight "
          f"onto (6,) -- a {float(concentration):.2f}x concentration")

    # ── assertions ────────────────────────────────────────────────────────
    # A1 — THE RESULT. Nothing derived reaches AME.
    wb.add_assertion(
        name="no_derived_weighting_reaches_ame",
        computed=str(n_reach), expected="0", tolerance="0", unit="count",
        source="weightings with E_0*S_vN <= B_AME(2H), out of 4")

    # A2 — CONTROL that W1 really is the framework's weighting: the exact
    #      closed form reproduces the committed Frobenius Gram diagonal.
    wb.add_assertion(
        name="control_exact_y_lambda_matches_committed_gram",
        computed=mp.nstr(gram_agree, 20), expected="0",
        tolerance="1e-7", unit="relative",
        source="y_{(n-k,k)} = [n-2k+1]_q/[2]_q^n vs "
               "deuteron-real-sdp frobenius_gram_diag (float64 in the witness)")

    # A3 — CONTROL that all four are genuine probability vectors.
    wb.add_assertion(
        name="control_all_weightings_normalise",
        computed=str(norm_ok), expected="4", tolerance="0", unit="count",
        source="sum_lambda p_lambda = 1 over the four support blocks")

    # A4 — the overshoot is TIGHT across wildly different weightings.
    wb.add_assertion(
        name="overshoot_band_lower_edge",
        computed=mp.nstr(min(ratios), 20), expected="1.6878",
        tolerance="1e-3", unit="ratio",
        source="min over the four weightings of E_0*S_vN / B_AME")
    wb.add_assertion(
        name="overshoot_band_upper_edge",
        computed=mp.nstr(max(ratios), 20), expected="2.0634",
        tolerance="1e-3", unit="ratio",
        source="max over the four weightings of E_0*S_vN / B_AME")

    # A5 — and it is robust: every NON-trivial vertex overshoots too, so the
    #      band is a property of the cut, not of the weightings chosen.
    wb.add_assertion(
        name="every_nontrivial_vertex_overshoots",
        computed=str(sum(1 for r in nontrivial if r > mp.mpf("1.7"))),
        expected="3", tolerance="0", unit="count",
        source="vertices delta_(5,1), delta_(4,2), delta_(3,3)")

    # A6 — CONTROL against the vacuous reading "the range is bounded below by
    #      1.7": the trivial block DOES give zero, so the simplex reaches low
    #      values -- just nowhere any derived weighting goes.
    wb.add_assertion(
        name="control_trivial_block_vertex_is_exactly_zero",
        computed=mp.nstr(verts["(6,)"], 20), expected="0",
        tolerance="1e-30", unit="nats",
        source="delta_(6,) restricts to a single (mu,nu): a product state")

    # A7 — so reaching AME demands an absurd concentration on that block.
    wb.add_assertion(
        name="ame_requires_concentration_on_trivial_block",
        computed=mp.nstr(concentration, 20), expected="6.314",
        tolerance="1e-2", unit="ratio",
        source="p_(6,) needed / p_(6,) under W1, bisected")

    # A8 — ANTI-NUMEROLOGY CONTROL. W1's 1.9493 is NOT 2, and 2.6% is not
    #      agreement in a framework quoting ppb. Asserted so the near-miss
    #      cannot later be read as a hit.
    wb.add_assertion(
        name="markov_ratio_is_not_two",
        computed=mp.nstr(abs(mp.mpf(rows["W1_markov_plancherel_exact"]
                                    ["ratio_to_B_AME"]) - 2) / 2, 20),
        expected="0.02535", tolerance="1e-4", unit="relative",
        source="|1.9493 - 2|/2 -- recorded as NOT agreement, not pursued")

    wb.add_data("E0_MeV", mp.nstr(E0, 30))
    wb.add_data("q0_pin", "proton")
    wb.add_data("B_AME_2H_MeV", str(B))
    wb.add_data("required_S_vN", mp.nstr(need, 30))
    wb.add_data("weightings", rows)
    wb.add_data("vertex_S_vN", {s: mp.nstr(verts[s], 24) for s in SUPPORT})
    wb.add_data("weight_fraction_onto_trivial_block_for_ame",
                mp.nstr(lo, 24))
    wb.add_data("concentration_factor", mp.nstr(concentration, 24))
    wb.add_caveat(
        "Scope (a). No weighting is selected, endorsed, or tuned; all four are "
        "computed once and reported. The two controls (classical Plancherel, "
        "uniform) are deliberately structure-poor so that agreement between "
        "them and the derived pair is informative about the CUT rather than "
        "about the weighting.")
    wb.add_caveat(
        "This does NOT refute an entanglement-cost contribution to binding. An "
        "overshoot of ~2x with the right sign and order of magnitude is not an "
        "exclusion, and a term entering with a coefficient or alongside others "
        "is untouched. What is established is that E_0*S_cut alone, under every "
        "weighting the framework already fixes, is about twice too large.")
    wb.add_caveat(
        "ONE isotope. LR branching data exists only for the deuteron, so "
        "nothing here speaks to 3H, 4He or beyond -- and a single point could "
        "not have distinguished a derivation from a coincidence even had it "
        "hit.")
    wb.add_caveat(
        "SHARPENS the genericity caveat of "
        "binding_cut_entropy_sign_is_forced_probe.py: a weighting CAN in "
        "principle reach anything in [0, max], but no DERIVED one does -- they "
        "cluster at ~2x and the only low region is the trivial block. The "
        "earlier caveat was right in principle and too weak in fact.")
    wb.save()
    print("\nwitness written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
