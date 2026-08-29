#!/usr/bin/env python3
"""Route 10: the three level-7 numerators are a Bernoulli B₂, i.e. a distribution relation.

Context
-------
Bean ``qou-fivt`` (child of ``qou-0yqu``), following the merge of PR #4658.

Route 9 left the sum rule equivalent to three explicit rational values

    Re[2·L(wₖ) + L(−wₖ)] = mₖ·π²/42,   m = (17, 5, −1),   wₖ = 1 + 2cos(2πk/7)

verified to 100 dps but **not derived**.  Those three integers are the entire
remaining content of the 5₂ sum rule.

What this probe establishes
---------------------------
The numerators are not three unrelated constants.  They are a quadratic in ``k``:

    mₖ = 3k² − 21k + 35            (symmetric under k ↦ 7−k, as cos(2πk/7) demands)

and that quadratic is a **Bernoulli polynomial**:

    mₖ/7 = 21·B₂(k/7) + 3/2,       B₂(x) = x² − x + 1/6

``B₂`` is the Fourier signature of the dilogarithm at roots of unity — the
classical fact ``Σₙ cos(2πnx)/n² = π²·B₂(x)`` on ``[0,1]``, i.e.

    Re Li₂(ζ₇^k) = π²·B₂(k/7)

So the target collapses to a single **distribution relation** between the Rogers
dilogarithm at a real cyclotomic *unit* and ``Li₂`` at a *root of unity*:

    Re[2·L(wₖ) + L(−wₖ)] = (7/2)·Re Li₂(ζ₇^k) + π²/4,   wₖ = ζ₇^k + ζ₇^{−k} + 1

Why that is the useful form
---------------------------
* ``Re Li₂(ζ₇^k) = π²B₂(k/7)`` is **elementary and provable** — it is the cosine
  Fourier series of ``B₂``, needing only real analysis and ``Cl₂``, **not** the
  complex ``Li₂`` continuation that blocks `qou-clx8` / `qou-ph1k`.  The corpus
  already has ``Cl₂`` infrastructure from #4666
  (``QOU/Archimedean/BlochWignerLobachevsky.lean``: ``summable_clausen``,
  ``Cl_2_duplication``, ``Cl_2_neg``, ``Cl_2_add_two_pi``).
* It replaces "prove three mysterious integers" with "prove one distribution
  relation", which is a named classical object with standard proof technique
  (Kubert / multiplication relations), rather than a coincidence to be fitted.

⚠ Still not a proof
-------------------
The distribution relation itself is **verified, not derived**.  This is the same
epistemic status as everything upstream of it.  Sum rule: verified to 80 dps,
unproved.

Gates
-----
G1  mₖ = 3k² − 21k + 35 reproduces (17, 5, −1) and is k ↦ 7−k symmetric.
G2  Re Li₂(ζ₇^k) = π²·B₂(k/7)  (the classical Fourier fact).
G3  wₖ = ζ₇^k + ζ₇^{−k} + 1 exactly.
G4  THE RELATION: Re[2L(wₖ) + L(−wₖ)] = (7/2)·Re Li₂(ζ₇^k) + π²/4.
G5  Equivalent Bernoulli form: = (7π²/2)·B₂(k/7) + π²/4.
G6  Summing G4 over k = 1,2,3 returns π²/2, hence Route 8's −π²/2 and the sum rule.
"""
from __future__ import annotations

import json
import pathlib

from mpmath import cos, exp, fabs, log, mp, mpf, nstr, pi, polylog, re

mp.dps = 60
TOL = mpf(10) ** -50


def rogers(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def B2(x):
    return x * x - x + mpf(1) / 6


def main():
    gates = []
    z7 = exp(2j * pi / 7)
    ks = (1, 2, 3)
    W = [1 + 2 * cos(2 * pi * k / 7) for k in ks]
    ms = [17, 5, -1]

    # G1 -- the quadratic
    fit = [3 * k * k - 21 * k + 35 for k in ks]
    mirror = [3 * k * k - 21 * k + 35 for k in (6, 5, 4)]
    gates.append({"gate": "G1", "claim": "m_k = 3k^2 - 21k + 35 = (17, 5, -1), symmetric under k -> 7-k",
                  "fitted": fit, "target": ms, "mirror_k_6_5_4": mirror,
                  "pass": bool(fit == ms and mirror == ms)})

    # G2 -- the classical Fourier fact
    w2 = mpf(0)
    per2 = []
    for k in ks:
        lhs = re(polylog(2, z7 ** k))
        rhs = pi ** 2 * B2(mpf(k) / 7)
        w2 = max(w2, fabs(lhs - rhs))
        per2.append({"k": k, "Re_Li2_zeta": nstr(lhs, 24), "pi2_B2": nstr(rhs, 24)})
    gates.append({"gate": "G2", "claim": "Re Li2(zeta_7^k) = pi^2 B_2(k/7)  (cosine Fourier series of B_2)",
                  "per_k": per2, "worst": nstr(w2, 8), "pass": bool(w2 < TOL)})

    # G3 -- w is the real cyclotomic unit
    w3 = max(fabs(w - (z7 ** k + z7 ** (-k) + 1)) for k, w in zip(ks, W))
    gates.append({"gate": "G3", "claim": "w_k = zeta_7^k + zeta_7^-k + 1",
                  "worst": nstr(w3, 8), "pass": bool(w3 < TOL)})

    # G4 -- THE DISTRIBUTION RELATION
    w4 = mpf(0)
    per4 = []
    for k, w in zip(ks, W):
        lhs = re(2 * rogers(w) + rogers(-w))
        rhs = mpf(7) / 2 * re(polylog(2, z7 ** k)) + pi ** 2 / 4
        w4 = max(w4, fabs(lhs - rhs))
        per4.append({"k": k, "lhs": nstr(lhs, 24), "rhs": nstr(rhs, 24),
                     "abs_err": nstr(fabs(lhs - rhs), 6)})
    gates.append({"gate": "G4",
                  "claim": "Re[2L(w_k)+L(-w_k)] = (7/2) Re Li2(zeta_7^k) + pi^2/4  -- a DISTRIBUTION RELATION",
                  "per_k": per4, "worst": nstr(w4, 8),
                  "note": "verified, NOT derived; this is the whole remaining content of the sum rule",
                  "pass": bool(w4 < TOL)})

    # G5 -- Bernoulli form
    w5 = max(fabs(re(2 * rogers(w) + rogers(-w))
                  - ((7 * pi ** 2 / 2) * B2(mpf(k) / 7) + pi ** 2 / 4))
             for k, w in zip(ks, W))
    gates.append({"gate": "G5", "claim": "equivalently = (7 pi^2/2) B_2(k/7) + pi^2/4",
                  "worst": nstr(w5, 8), "pass": bool(w5 < TOL)})

    # G6 -- the sum returns the sum rule
    tot = sum(re(2 * rogers(w) + rogers(-w)) for w in W)
    viaB2 = (7 * pi ** 2 / 2) * sum(B2(mpf(k) / 7) for k in ks) + 3 * pi ** 2 / 4
    e6 = max(fabs(tot - pi ** 2 / 2), fabs(viaB2 - pi ** 2 / 2))
    gates.append({"gate": "G6", "claim": "summing over k = 1,2,3 gives pi^2/2, hence Route 8's -pi^2/2",
                  "direct_sum": nstr(tot, 24), "via_B2": nstr(viaB2, 24),
                  "target_pi2_over_2": nstr(pi ** 2 / 2, 24),
                  "worst": nstr(e6, 8), "pass": bool(e6 < TOL)})

    # G7 -- the cyclotomic dictionary a derivation has to work in
    w7 = mpf(0)
    for k, w in zip(ks, W):
        zk = z7 ** k
        w7 = max(w7,
                 fabs(w - (1 + zk + zk ** -1)),
                 fabs(w - zk ** -1 * (1 - zk ** 3) / (1 - zk)),
                 fabs(w ** 2 - (1 + zk + zk ** 2) * (1 + zk ** -1 + zk ** -2)),
                 fabs((1 - w) + (zk + zk ** -1)),
                 fabs((1 + w) - 4 * cos(pi * k / 7) ** 2))
    gates.append({"gate": "G7",
                  "claim": "cyclotomic dictionary: w = 1+z^k+z^-k = z^-k (1-z^3k)/(1-z^k); "
                           "w^2 = (1+z^k+z^2k)(1+z^-k+z^-2k); 1-w = -(z^k+z^-k); 1+w = 4cos^2(pi k/7)",
                  "worst": nstr(w7, 8), "pass": bool(w7 < TOL)})

    # G8 -- the Galois orbit IS the orbit of the order-3 Mobius map T(x) = 1 - 1/x
    def T(x):
        return (x - 1) / x

    cyc = max(fabs(1 / W[i] - (1 - W[(i + 1) % 3])) for i in range(3))
    per = max(fabs(T(T(T(w))) - w) for w in W)
    orbit_sums = [re(rogers(w) + rogers(T(w)) + rogers(T(T(w)))) for w in W]
    spread = max(fabs(orbit_sums[i] - orbit_sums[0]) for i in range(3))
    gates.append({"gate": "G8",
                  "claim": "1/w_k = 1 - w_{k+1}: the three embeddings are ONE orbit of T(x) = 1 - 1/x, "
                           "so the Galois action coincides with the order-3 Mobius map",
                  "cyclic_relation_worst": nstr(cyc, 8),
                  "T_has_order_3_worst": nstr(per, 8),
                  "orbit_sum": nstr(orbit_sums[0], 22),
                  "orbit_sum_over_pi_sq": nstr(orbit_sums[0] / pi ** 2, 18),
                  "orbit_sums_agree_worst": nstr(spread, 8),
                  "note": "STRUCTURE, NOT A PROOF: the T-orbit sum is IRRATIONAL (0.27318.../pi^2), so the "
                          "3-cycle alone does not produce the rational value. The rational combination is "
                          "2[w] + [-w], which is not the orbit sum. Recorded so nobody mistakes the "
                          "Galois/Mobius coincidence for a derivation.",
                  "pass": bool(cyc < TOL and per < TOL and spread < TOL)})

    out = {
        "probe": "qbeta_5two_route10_kubert_distribution",
        "bean": "qou-fivt",
        "parent_bean": "qou-0yqu",
        "builds_on": "qou-b7cy (Route 9), qou-8v3k (Route 8) -- merged in PR #4658",
        "dps": mp.dps,
        "gates": gates,
        "verdict": {
            "route10": "MECHANISM IDENTIFIED -- reduction to one distribution relation. NOT a proof.",
            "finding": "the three numerators 17, 5, -1 are m_k = 3k^2 - 21k + 35 = 7(21 B_2(k/7) + 3/2)/7, "
                       "and B_2 is the Fourier signature of Li_2 at roots of unity "
                       "(Re Li2(zeta_7^k) = pi^2 B_2(k/7)). So the target is the single relation "
                       "Re[2L(w_k)+L(-w_k)] = (7/2) Re Li2(zeta_7^k) + pi^2/4 with "
                       "w_k = zeta_7^k + zeta_7^-k + 1.",
            "why_it_helps": "Re Li2(zeta_7^k) = pi^2 B_2(k/7) is elementary -- the cosine Fourier series "
                            "of B_2 -- needing only real analysis and Cl_2, NOT the complex Li_2 "
                            "continuation that blocks qou-clx8/qou-ph1k. The corpus already has Cl_2 "
                            "from #4666. And it replaces three fitted-looking integers with a named "
                            "classical object (Kubert / multiplication relations).",
            "still_open": "the distribution relation itself is verified, not derived.",
            "sum_rule_status": "verified to 80 dps, unproved -- UNCHANGED",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route10-kubert-distribution.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=False)
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:84]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: mechanism identified (Bernoulli B_2 / distribution relation). NOT a proof.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
