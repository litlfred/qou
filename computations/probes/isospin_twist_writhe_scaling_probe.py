#!/usr/bin/env python3
"""
isospin_twist_writhe_scaling_probe.py -- the A-scaling of the braid-channel T(T+1) term.

Accuracy epic qou-myts, ledger gap G2 (bean qou-tcl2); follow-up to PR #9685 (Lean)
and PR #9706 (wiring, held).

WHAT IS DERIVED (Lean, QOU/Nuclear/IsospinTwistWrithe.lean)
----------------------------------------------------------
Let chi be ANY multiplicative map from the Hecke algebra H_N(q) to a commutative
monoid (the case used here: chi = det o rho_lambda on a seminormal block of
dimension d_lambda).  Then

  * chi takes the SAME value a on every generator sigma_i (braid relation + sigma_i
    invertible)                                            (chi_σ_eq)
  * chi(L_k) = a^{2k}, so chi(Phi) = a^{N(N-1)} for the Murphy product, which is a
    word of N(N-1) letters                                 (chi_murphyProd_full)
  * for any braid word w of writhe (exponent sum) e,  chi(w) = a^e   (chi_word)
  * on a block, Phi is the scalar q^{2c}, so
        det rho(w)^{N(N-1)} = q^{2 c d e}                  (seminormal_det_word_pow)

So the block log-determinant per block dimension (the sum of ln|eigenvalue| over the
block, which is what the log law B = -alpha * sum ln|V| computes block by block) of a
word w is

    e(w) * 2 c(lambda) * ln q / (N (N - 1)),   c = T(T+1) + N(N-4)/4.

The T(T+1) coefficient is the WRITHE OVER N(N-1).  The full twist has writhe N(N-1),
which gives #9706's kappa * T(T+1) with no 1/A.  A word whose writhe grows linearly
in A gives a coefficient Theta(1/A) (Lean: chain_coeff_bounds).  The n-only part
e*(N-4)/(2(N-1)) is then extensive.

WHAT THIS PROBE DOES (diagnostic only; no producer number changes)
-----------------------------------------------------------------
Uses the energy map of #9706 unchanged (kappa = 2 alpha ln q, alpha = 8 G m_e,
lowest block T = |N-Z|/2, sign: larger T binds less) and replaces the full-twist
writhe N(N-1) by the writhe of the corpus's own nucleus words, N = 3A:

  full twist   e = N(N-1)        (reproduces #9706)
  chain        e = A - 1         (ruled law, binding_ruled_tz_even: A-1 bond letters)
  T3 valence   e = 3*floor(A/2)  (PR #9710 colour-valence cap, open card)

The writhe of each bond letter is taken as +1.  The nucleon's own core
V^3 = (sigma_0 sigma_1^{-1})^3 has writhe 0, so it carries no T(T+1) under this
reading.  Whether the bond letters are all positive is NOT derived here (word
axis, G5); a bond of writhe -1 flips its share.

It reports, against Table 3.4b of the scorecard (same row filter), the median
relative Q_beta error for each variant.  AME enters ONLY as a comparison.
Nothing is selected on these numbers: the per-letter coefficient is fixed by the
Lean result before they are read.

Also reported, as a separate observation: the dimension of the two-row block,
d_(m,k) = C(N,k) (m-k+1)/(m+1), with ln d_T - ln d_0 = ln(2T+1) - 2T^2/N + O(T^4/N^3).
Its -2T^2/N piece is the other place a 1/A comes out of the representation theory
(the multiplicity, i.e. the Pauli/Fermi-gas analogue); the ln(2T+1) piece pulls the
other way and still dominates at 208Pb (T = 22 < sqrt(N) ~ 25).  Its coefficient is printed, not wired, because no
corpus energy map for the block multiplicity exists yet.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
REPO = COMP.parent
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import q_at  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:  # pragma: no cover
    WitnessBuilder = None

set_compute_dps()

M_E = mp.mpf("0.51099895069")  # the literal the scorecard subtracts and the proxy scales by


def tt1(z: int, n: int) -> mp.mpf:
    """T(T+1) on the lowest block T = |N - Z|/2."""
    t = abs(n - z)
    return mp.mpf(t * (t + 2)) / 4


WRITHES = {
    "full_twist": lambda A: 3 * A * (3 * A - 1),
    "chain": lambda A: A - 1,
    "T3_valence": lambda A: 3 * (A // 2),
}


def coeff(kappa, A: int, e: int) -> mp.mpf:
    """T(T+1) coefficient in MeV: kappa * e / (N (N - 1)), N = 3A (Lean: per-letter exponent)."""
    N = 3 * A
    return kappa * mp.mpf(e) / (N * (N - 1))


def log_dim_two_row(N: int, t: int) -> mp.mpf:
    """ln d_(m,k) for the two-row block, m + k = N, m - k = t (hook length formula)."""
    k = (N - t) // 2
    m = N - k
    return mp.log(mp.binomial(N, k)) + mp.log(mp.mpf(t + 1) / (m + 1))


def median(xs):
    s = sorted(xs)
    L = len(s)
    return s[L // 2] if L % 2 else (s[L // 2 - 1] + s[L // 2]) / 2


def main() -> int:
    q = q_at(60)
    alpha = M_E * 8 * mp.catalan
    kappa = 2 * alpha * mp.log(q)

    wit = json.loads((COMP / "mass-table-comprehensive.witness.json").read_text())
    by = {(r["Z"], r["N"]): r for r in wit["data"]["rows"]}
    ame = json.loads((COMP / "data" / "ame2020.json").read_text())
    ame = ame if isinstance(ame, list) else next(v for v in ame.values() if isinstance(v, list))

    rows = []  # same filter as generate-accuracy-scorecard.py Table 3.4b
    for e in ame:
        z, n = int(e["Z"]), int(e["N"])
        if e.get("beta_decay_energy_estimated") or e.get("beta_decay_energy_keV") is None:
            continue
        q_exp = mp.mpf(str(e["beta_decay_energy_keV"])) / 1000
        if q_exp <= mp.mpf("0.01"):
            continue
        a, b = by.get((z, n)), by.get((z + 1, n - 1))
        if not a or not b:
            continue
        mk = "m_ruled_MeV" if a.get("m_ruled_MeV") else "m_symbolic_MeV"
        if not b.get(mk):
            continue
        q0 = mp.mpf(a[mk]) - mp.mpf(b[mk]) - M_E
        rows.append((z, n, q0, q_exp))

    report = {}
    for name, wr in [("no_term", None)] + list(WRITHES.items()):
        rels, exo = [], 0
        for z, n, q0, q_exp in rows:
            A = z + n
            dq = mp.mpf(0)
            if wr is not None and A >= 2:
                # mass = ... + coeff * T(T+1)  (B = -coeff*T(T+1)); Q = M(parent) - M(daughter)
                dq = coeff(kappa, A, wr(A)) * (tt1(z, n) - tt1(z + 1, n - 1))
            qp = q0 + dq
            rels.append(abs(qp - q_exp) / q_exp)
            exo += qp > 0
        report[name] = {"median_rel_pct": mp.nstr(100 * median(rels), 6),
                        "exothermic": f"{exo}/{len(rows)}"}

    samples = {}
    for nm, (z, n) in {"48Ca": (20, 28), "56Fe": (26, 30), "132Sn": (50, 82), "208Pb": (82, 126)}.items():
        A = z + n
        samples[nm] = {k: mp.nstr(-coeff(kappa, A, wr(A)) * tt1(z, n), 6) for k, wr in WRITHES.items()}

    # Block-dimension observation: ln d_T - ln d_0 vs the Gaussian -2T^2/N, at 208Pb.
    N, t = 3 * 208, 44
    dlog = log_dim_two_row(N, t) - log_dim_two_row(N, 0)
    gauss = -mp.mpf(2) * (t / 2) ** 2 / N
    dim_obs = {"N": N, "T": t // 2, "lnd_T_minus_lnd_0": mp.nstr(dlog, 8),
               "gaussian_minus_2T2_over_N": mp.nstr(gauss, 8),
               "ln_2T_plus_1": mp.nstr(mp.log(t + 1), 8),
               "alpha_times_2_over_3_MeV_per_T2_over_A": mp.nstr(alpha * 2 / 3, 8)}

    # Lean-side identities re-checked over the range in use.
    lean_checks = all(
        2 * (A - 1) * 9 * A <= 2 * 3 * A * (3 * A - 1)          # coeff <= 2/(9A)
        and 9 * A * 2 * (A - 1) >= 3 * A * (3 * A - 1)            # coeff >= 1/(9A), A >= 2
        for A in range(2, 400)
    )
    checks = {
        "n_rows_incl_free_neutron": (len(rows), 1010),
        "full_twist_reproduces_9706_median_315.8": (report["full_twist"]["median_rel_pct"][:5], "315.8"),
        "chain_coeff_bounds_1_over_9A_to_2_over_9A": (lean_checks, True),
    }
    ok = all(a == b for a, b in checks.values())

    print(f"alpha = {mp.nstr(alpha, 10)} MeV, kappa = 2 alpha ln q = {mp.nstr(kappa, 10)} MeV")
    print(f"Table 3.4b rows: {len(rows)}")
    for k, v in report.items():
        print(f"  {k:14s} median |dQ|/Q = {v['median_rel_pct']:>10s} %   exothermic {v['exothermic']}")
    print("T(T+1) share of B (MeV), lowest block:")
    for k, v in samples.items():
        print(f"  {k:6s} {v}")
    print(f"block dimension at 208Pb: {dim_obs}")
    for k, (a, b) in checks.items():
        print(f"  [{'PASS' if a == b else 'FAIL'}] {k}: {a}")

    if WitnessBuilder is not None:
        wb = WitnessBuilder("isospin-twist-writhe-scaling", engine="mpmath")
        wb.set_description(
            "A-scaling of the G2 braid-channel T(T+1) term: block log-det per dimension of a "
            "word of writhe e is e*2c ln q/(N(N-1)) (Lean QOU.Nuclear.IsospinTwistWrithe). "
            "Full twist (e = N(N-1), #9706) vs the corpus nucleus words (chain e = A-1, "
            "T3 e = 3 floor(A/2)); Table 3.4b Q_beta medians as a comparison only."
        )
        for k, (a, b) in checks.items():
            wb.add_assertion(k, computed=str(a), expected=str(b), tolerance="0")
        wb.add_data("alpha_MeV", mp.nstr(alpha, 15))
        wb.add_data("kappa_MeV", mp.nstr(kappa, 15))
        wb.add_data("table_3_4b", report)
        wb.add_data("TT1_share_of_B_MeV", samples)
        wb.add_data("block_dimension_observation", dim_obs)
        wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
