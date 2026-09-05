#!/usr/bin/env python3
"""
qb8e item 1, attacked formalize-first: prune the hypothesis class before scanning.

Item 1 of `qou-qb8e` asks for "a HABIRO-RING element whose archimedean evaluation
at q0 ~ 1.10998 reproduces c_3 at THAT anchor", by assembling root-of-unity
values "over all zeta". Two structural facts decide the whole class before any
assembly is attempted.

FACT A -- the evaluation dichotomy.
  A Habiro element is a series  sum_n a_n(q) (q;q)_n,  a_n in Z[q], convergent in
  the cyclotomic completion because (q;q)_n -> 0 there. A continuous evaluation
  at a point q0 therefore requires (q0;q0)_n -> 0 in C. But

      |q| > 1  =>  |(q;q)_n| ~ (1/q;1/q)_inf * q^(n(n+1)/2)   -> +infinity
      |q| < 1  =>  (q;q)_n   -> (q;q)_inf != 0                (nonzero limit)
      q^N = 1  =>  (q;q)_n = 0 for all n >= N                 (eventually zero)

  so the ONLY points admitting a continuous evaluation are the roots of unity.
  The substrate anchor q0 ~ 1.10998 is real and > 1: a genuinely infinite Habiro
  element HAS NO archimedean value there. Item 1 as written is ill-posed, not
  merely hard.

  The dichotomy, not a blanket prune: the Markov trace of a CLOSED BRAID is the
  one-variable Jones polynomial, a Laurent polynomial, so ITS (q;q)_m expansion
  TERMINATES (2026-05-30-qbeta-recursive-pair-rules-and-habiro-pde.md, stage 2).
  A finite expansion is a Laurent polynomial and evaluates fine at q0. So the
  class splits, and the two halves fail differently:

      finite   -> evaluable, but then it is an INTEGER Laurent polynomial and
                  FACT B applies
      infinite -> not evaluable at q0 at all; needs an analytic representative,
                  whose natural convergent point is qt = 1/q0 < 1

FACT B -- the target has no resolving power.
  Whatever the carrier, it is tested against c_3. Three facts about that target,
  all already in the corpus, taken together:

    (i)  c_3's ABSOLUTE value is unresolved: +/-1.262 propagated CAL-3, against a
         central value ~ -2.02 (aomega_o2_stokes_to_observable_mechanism.py:19).
    (ii) the ZERO location q*_S IS resolved -- but only to sigma(q*) = 3.288e-7
         (qbeta_qstar_experimental_budget.py).
    (iii) the genericity window (-c_3(mu), -c_3(p)), width 0.0491, maps ONTO the
         anchor interval, of width |q_p - q_mu| = 1.28e-8
         (sleak_offset_genericity_check.py).

  (ii) vs (iii) is the kill: the entire set of constants that "put a zero between
  the anchors" occupies a q*-interval 25.7x NARROWER than one experimental error
  bar on q*_S. So reproducing q*_S cannot presently distinguish Vol(4_1) from any
  of the 7/7 unrelated constants already known to pass. The gate has no test
  power until sigma(Q_beta) improves by that same factor.

This probe computes all of it. It is arithmetic on committed values: no fit, no
new measurement, no c_k wired.
"""

import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath
from mpmath import mp

mp.dps = 60

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools", "qou-substrate", "python"))


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "unknown"


def q_pochhammer(q, n):
    """(q;q)_n = prod_{k=1..n} (1 - q^k), computed directly."""
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= (1 - q ** k)
    return out


def main() -> int:
    # experimental (proton) pin — the default for all new compute per the
    # 2026-08-07 owner directive.
    from qou_substrate import constants as C  # noqa: E402

    q0 = mp.mpf(C.Q_50_DIGIT_STR) if hasattr(C, "Q_50_DIGIT_STR") else mp.mpf(str(C.Q))
    qt = 1 / q0

    print("=" * 74)
    print("qb8e item 1 — Habiro evaluation dichotomy + test power of the gate")
    print("=" * 74)
    print(f"\n  substrate anchor q0 = {mp.nstr(q0, 25)}   (experimental / proton pin)")
    print(f"  bar partner    1/q0 = {mp.nstr(qt, 25)}")

    # ---------------- FACT A ----------------
    print("\n" + "-" * 74)
    print("FACT A — where does a Habiro series admit a continuous evaluation?")
    print("-" * 74)

    print("\n  The EXACT reflection identity (not an asymptotic law) —")
    print("      (q;q)_n = (-1)^n * q^(n(n+1)/2) * (1/q;1/q)_n     for every n, every q != 0")
    print("  because  1 - q^k = -q^k (1 - q^-k)  termwise. This is the whole argument:")
    print("  the q > 1 branch carries an explicit q^(n(n+1)/2) blow-up factor relative")
    print("  to the |q| < 1 branch, which converges. Checked to working precision:\n")

    rows = []
    refl_max_err = mp.mpf(0)
    for n in (1, 5, 10, 20, 40, 60, 100):
        lhs = q_pochhammer(q0, n)
        rhs = (-1) ** n * q0 ** (mp.mpf(n * (n + 1)) / 2) * q_pochhammer(qt, n)
        err = abs(lhs - rhs) / abs(lhs)
        refl_max_err = max(refl_max_err, err)
        rows.append({"n": n,
                     "abs_qpoch_at_q0": mp.nstr(abs(lhs), 12),
                     "reflection_rhs": mp.nstr(abs(rhs), 12),
                     "relative_error": mp.nstr(err, 6)})
        print(f"    n={n:4d}   |(q0;q0)_n| = {mp.nstr(abs(lhs), 10):>16}"
              f"   reflection = {mp.nstr(abs(rhs), 10):>16}   rel.err = {mp.nstr(err, 6)}")

    reflection_ok = refl_max_err < mp.mpf("1e-40")
    print(f"\n    identity holds to max rel.err {mp.nstr(refl_max_err, 6)}"
          f"  (< 1e-40: {reflection_ok})")

    # the blow-up factor itself
    print("\n  The blow-up factor q0^(n(n+1)/2) alone:")
    for n in (10, 40, 100):
        print(f"    n={n:4d}   q0^(n(n+1)/2) = {mp.nstr(q0 ** (mp.mpf(n * (n + 1)) / 2), 8)}")
    diverges = q_pochhammer(q0, 100) != 0 and abs(q_pochhammer(q0, 100)) > mp.mpf("1e100")
    print(f"\n    => (q0;q0)_n DIVERGES super-exponentially: {diverges}."
          f"  No continuous evaluation at q0.")

    print("\n  (q;q)_n at 1/q0 < 1 — converges to a NONZERO limit:")
    amp = mp.mpf(1)
    for k in range(1, 400):
        amp *= (1 - qt ** k)
    amp = abs(amp)
    tail = []
    for n in (10, 40, 100, 200):
        val = q_pochhammer(qt, n)
        tail.append({"n": n, "qpoch_at_inv_q0": mp.nstr(val, 20)})
        print(f"    n={n:4d}   (1/q0;1/q0)_n = {mp.nstr(val, 20)}")
    limit = abs(mp.mpf(tail[-1]["qpoch_at_inv_q0"]))
    limit_nonzero = limit > mp.mpf("1e-12")
    limit_matches_amp = abs(limit - amp) / amp < mp.mpf("1e-7")
    print(f"\n    (1/q0;1/q0)_inf = {mp.nstr(amp, 20)}   nonzero: {limit_nonzero}"
          f"   tail matches: {limit_matches_amp}")
    print("    => (q;q)_n does NOT tend to 0 at 1/q0 either. A Habiro SERIES still")
    print("       has no continuous evaluation there — but an ANALYTIC representative")
    print("       (state integral / q-series) converges for |q| < 1, and 1/q0 is the")
    print("       only one of the pair inside the unit disc.")

    print("\n  roots of unity — (q;q)_n is eventually zero, EXACTLY and structurally:")
    print("    for zeta of order N the factor k=N is (1 - zeta^N) = 0, so")
    print("    (zeta;zeta)_n = 0 for every n >= N. Not a numerical near-zero —")
    print("    an exact vanishing factor. Numerically, at dps=60:")
    rou = []
    for N in (3, 5, 8):
        z = mp.exp(2j * mp.pi / N)
        v = mp.mpf(1)
        for k in range(1, N + 1):
            v = v * (1 - z ** k)
        rou.append({"N": N, "abs_qpoch_at_zeta_N": mp.nstr(abs(v), 6)})
        print(f"      N={N}: |(zeta_{N};zeta_{N})_{N}| = {mp.nstr(abs(v), 6)}")
    rou_vanishes = all(mp.mpf(r["abs_qpoch_at_zeta_N"]) < mp.mpf("1e-50") for r in rou)
    print(f"\n    vanishes to working precision: {rou_vanishes}")
    print("\n  => roots of unity are the ONLY points where (q;q)_n -> 0, hence the")
    print("     only points admitting a continuous evaluation of the completion.")

    # ---------------- FACT B ----------------
    print("\n" + "-" * 74)
    print("FACT B — the test power of 'reproduce the zero location q*_S'")
    print("-" * 74)

    # committed inputs, loaded not typed
    budget_w = os.path.join(ROOT, "docs", "audits", "scripts",
                            "qbeta-qstar-experimental-budget.witness.json")
    with open(budget_w) as f:
        bw = json.load(f)["result"]
    sigma_qstar = mp.mpf(bw["sigma_qstar_today_abs"])
    pin_spread = mp.mpf(bw["pin_spread_abs"])
    q_star = mp.mpf(bw["q_star"])

    print(f"\n    sigma(q*_S) today        = {mp.nstr(sigma_qstar, 8)}"
          f"   ({bw['sigma_qstar_today_ppb']} ppb)")
    print(f"    |q_proton - q_muon|      = {mp.nstr(pin_spread, 8)}"
          f"   ({bw['pin_spread_ppb']} ppb)")

    # the genericity window maps ONTO the anchor interval (that is what
    # sleak_offset_genericity_check establishes), so its image has that width.
    window_image_width = pin_spread
    power = sigma_qstar / window_image_width

    print(f"\n    genericity-window image in q* = the anchor interval,"
          f" width {mp.nstr(window_image_width, 8)}")
    print(f"    sigma(q*) / window image      = {mp.nstr(power, 8)}")
    print(f"\n    => every in-window constant sits inside ONE error bar of q*_S.")
    print(f"       The gate cannot separate Vol(4_1) from the 7/7 unrelated")
    print(f"       constants until sigma(Q_beta) improves by ~{mp.nstr(power, 4)}x.")

    # cross-check against the budget probe's own independently-computed factor
    arb = [b for b in bw["budget"] if "mu-p scale" in b["threshold"]
           or "μ–p scale" in b["threshold"]]
    cross_ok = False
    cross_factor = None
    if arb:
        # the committed value is stored rounded to 6 significant figures, so the
        # agreement bar is that rounding, not full precision.
        cross_factor = mp.mpf(arb[0]["improvement_factor_needed"])
        cross_ok = abs(cross_factor - power) / power < mp.mpf("1e-5")
        print(f"\n    cross-check: the budget probe's own factor = "
              f"{mp.nstr(cross_factor, 8)}  (agrees: {cross_ok})")

    print(f"\n    Separately, c_3's ABSOLUTE value is unresolved: +/-1.262 CAL-3")
    print(f"    against a central value ~ -2.02. So the magnitude channel carries")
    print(f"    no resolving power at all, which is why the gate was restated as")
    print(f"    the zero location in the first place. Both channels are now")
    print(f"    quantified: magnitude 0 bits, zero location 0 bits AT PRESENT.")

    assertions = [
        {"name": "reflection_identity_exact",
         "passed": bool(reflection_ok),
         "detail": "(q;q)_n = (-1)^n q^(n(n+1)/2) (1/q;1/q)_n, max rel.err "
                   + mp.nstr(refl_max_err, 6)},
        {"name": "qpoch_diverges_at_q0",
         "passed": bool(diverges)},
        {"name": "qpoch_limit_nonzero_at_inv_q0",
         "passed": bool(limit_nonzero and limit_matches_amp)},
        {"name": "qpoch_vanishes_at_roots_of_unity",
         "passed": bool(rou_vanishes)},
        {"name": "no_continuous_habiro_evaluation_at_q0",
         "passed": bool(diverges),
         "detail": "continuity would need (q0;q0)_n -> 0; it diverges"},
        {"name": "gate_test_power_below_one_error_bar",
         "passed": bool(power > 1),
         "detail": "sigma(q*) exceeds the whole genericity-window image"},
        {"name": "test_power_matches_budget_probe_factor",
         "passed": bool(cross_ok)},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(os.path.abspath(__file__), "rb") as f:
        src = f.read()

    witness = {
        "computation": "qbeta-habiro-evaluation-dichotomy-and-test-power",
        "description": (
            "qb8e item 1 pruned formalize-first. (A) A genuinely infinite Habiro "
            "element admits a continuous evaluation only at roots of unity: "
            "(q;q)_n diverges like q^(n(n+1)/2) for |q|>1 and tends to a nonzero "
            "limit for |q|<1, so the substrate anchor q0 ~ 1.10998 > 1 has no "
            "archimedean Habiro value and item 1 is ill-posed as written. A FINITE "
            "expansion (the closed-braid Markov trace = Jones Laurent polynomial) "
            "does evaluate, so the class splits rather than dying. (B) The gate "
            "'reproduce the zero q*_S' currently has NO test power: the image of "
            "the genericity window in q* is the anchor interval (1.28e-8), which is "
            "25.7x narrower than sigma(q*_S) = 3.29e-7. Arithmetic on committed "
            "values; no fit, no new measurement, no c_k wired."),
        "audit_only": True,
        "tier": "structural argument + error propagation (no fit)",
        # Declare the pin (AGENTS.md 2026-08-07 owner directive: "Any new
        # witness must record its q0 so a later reader can tell which layer
        # it belongs to"). Enforced by q0_anchor_consistency_audit.
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q0, 25),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mpmath.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "q0": mp.nstr(q0, 25),
            "inv_q0": mp.nstr(qt, 25),
            "q_star_S": mp.nstr(q_star, 25),
            "qpoch_amplitude_inv_q0_infinite": mp.nstr(amp, 25),
            "reflection_identity_table_at_q0": rows,
            "qpoch_at_roots_of_unity": rou,
            "reflection_max_relative_error": mp.nstr(refl_max_err, 6),
            "qpoch_tail_at_inv_q0": tail,
            "sigma_qstar_abs": mp.nstr(sigma_qstar, 12),
            "anchor_pin_spread_abs": mp.nstr(pin_spread, 12),
            "genericity_window_image_width_in_qstar": mp.nstr(window_image_width, 12),
            "gate_test_power_sigma_over_window": mp.nstr(power, 12),
            "budget_probe_cross_factor": (mp.nstr(cross_factor, 12)
                                          if cross_factor is not None else None),
            "c3_absolute_uncertainty_CAL3": "1.262",
            "c3_central_value_scale": "-2.02",
        },
        "context": {
            "axis": "qb8e item 1 — fibre carrier for c_3",
            "inputs": [
                "docs/audits/scripts/qbeta-qstar-experimental-budget.witness.json",
                "computations/qbeta/sleak_offset_genericity_check.py",
                "computations/probes/aomega_o2_stokes_to_observable_mechanism.py",
                "tools/qou-substrate/.../constants.py (proton pin, per the "
                "2026-08-07 owner directive)",
            ],
            "scope": (
                "Scope-(b) for the INFINITE branch: the named invariant is that a "
                "continuous evaluation of the cyclotomic completion forces "
                "(q0;q0)_n -> 0, which holds only at roots of unity. Scope-(a) for "
                "the test-power finding: it is a statement about the CURRENT "
                "experimental resolution, and a ~26x sharper neutron Q_beta lifts "
                "it. Neither refutes (H1)."),
        },
    }

    out = os.path.join(HERE, "qbeta-habiro-evaluation-dichotomy-and-test-power.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
    print(f"\nwitness -> {out}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
