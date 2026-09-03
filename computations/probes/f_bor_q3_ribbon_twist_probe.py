#!/usr/bin/env python3
"""Is F_Bor's ``/q^3`` the ribbon twist, or a coincidence of shape?

Bean ``qou-w1j9``; answers question Q2 of ``qou-gzs0``.

THE QUESTION
------------
``canonical_mass`` builds the proton from

    F_Bor(q) = |tr_M(beta_Bor, q)| * [3]_q! / q^3

and ``qou-gzs0`` observed that ``q^-3 = q^{T/2}`` at ``T = -6`` EXACTLY, i.e.
"-2 per Borromean component", which has *framing shape*.  But the Borromean
word ``(s1 s2^-1)^3`` has writhe 0, so it is not ``q^writhe``.  gzs0 concluded
the corpus must **declare** which framing the mass path uses, because
``FramingIsAChoice.lean`` proves ``T = 0`` is a convention and not derivable.

``qou-w1j9`` re-opened this as a *computation*: in a ribbon category the twist
is not a free label, it is a scalar determined by the object (Habiro,
``library/1172-3`` sec.6: one full twist acts on the JW idempotent ``e_n`` by
``(-1)^n A^{n(n+2)}``).  So the exponent is predicted, and a prediction can be
checked.

WHAT THIS PROBE TESTS
---------------------
Four things, all exact (sympy rational functions in ``q``), no float anywhere:

  T1  bar-parity accounting.  Which factor of F_Bor breaks ``q -> 1/q``?
  T2  the H_3 RIBBON-twist eigenvalues theta_lambda = ``q^{c(lambda)}`` per
      Wedderburn block.  Are they {q^3, 1, q^-3}?
  T3  does ``q^-3`` coincide with the twist eigenvalue on a *block*?
  T4  the two competing per-component readings: gzs0's ``-2 per component``
      against the ribbon/Casimir ``n(n+2) = 3`` at the fundamental colour.

NO-FLOAT64 (AGENTS.md, STRICT, probes are NOT exempt): every quantity below is
a sympy exact expression or an ``mpmath.mpf``.  ``float()`` appears nowhere.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction

import sympy as sp

q = sp.Symbol("q", positive=True)


# ---------------------------------------------------------------- the factors

def q_int(n: int):
    """Balanced q-integer [n]_q = (q^n - q^-n)/(q - q^-1) -- the convention
    ``m_p_substrate_identity_50dps.q_int`` actually uses (checked, not assumed:
    its docstring says 'Balanced')."""
    return sp.simplify((q ** n - q ** (-n)) / (q - 1 / q))


def qfact_three():
    """[3]_q! = [3][2][1], balanced."""
    return sp.simplify(q_int(3) * q_int(2) * q_int(1))


def trM_borromean():
    """tr_M(beta_Bor, q) = (4 + h^2 - 3h^4 - h^6)/(h^2 + 4), h = q - q^-1.
    Closed form from BorromeanMarkovTrace.lean (convention D)."""
    h = q - 1 / q
    return sp.simplify((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))


def bar(expr):
    """The bar involution q -> q^-1."""
    return sp.simplify(expr.subs(q, 1 / q))


def bar_parity(expr, name):
    """Classify expr as bar-even, bar-odd, or neither."""
    e = sp.simplify(sp.together(expr))
    b = bar(e)
    if sp.simplify(b - e) == 0:
        return "even"
    if sp.simplify(b + e) == 0:
        return "odd"
    return "neither"


# --------------------------------------------------- H_3 full-twist exponents

PARTITIONS_3 = {"(3)": [3], "(2,1)": [2, 1], "(1^3)": [1, 1, 1]}


def content_sum(shape: list[int]) -> int:
    """Sum of contents (j - i) over the Young diagram, 0-indexed rows/cols.

    TWO DISTINCT TWISTS, and conflating them is the trap this probe fell into
    on its first pass:

      ribbon twist (modular T-matrix) theta_lambda = q^{c(lambda)}
      full twist   Delta^2                        = theta^2 = q^{2c(lambda)}

    The first is `QOU.BraidKnot.Keystone.theta` in
    `lean/QOU/BraidKnot/KeystoneModularTwist.lean` -- `q ^ contentSum l`,
    SORRY-FREE, over a generic `[GroupWithZero R]`. The second is what
    `computations/chi-content-eigenbasis.witness.json` reports as `q^{2c}`.
    Both are correct; they are different objects, and `q^-3` is the FIRST."""
    return sum(j - i for i, row in enumerate(shape) for j in range(row))


def dim_specht(shape: list[int]) -> int:
    """Hook-length formula -- exact integer arithmetic, no float."""
    n = sum(shape)
    conj = [sum(1 for r in shape if r > j) for j in range(shape[0])]
    num = 1
    for k in range(1, n + 1):
        num *= k
    den = 1
    for i, row in enumerate(shape):
        for j in range(row):
            den *= (row - j) + (conj[j] - i) - 1
    assert num % den == 0, "hook-length formula did not divide exactly"
    return num // den


# ------------------------------------------------------------------ the tests

def main() -> int:
    results: dict = {}
    failures: list[str] = []

    trM = trM_borromean()
    fact = qfact_three()
    framing = q ** -3
    f_bor = sp.simplify(trM * fact * framing)

    # ---- T1: bar-parity accounting -------------------------------------
    par = {
        "tr_M(beta_Bor)": bar_parity(trM, "trM"),
        "[3]_q!": bar_parity(fact, "fact"),
        "q^-3": bar_parity(framing, "framing"),
        "F_Bor (product)": bar_parity(f_bor, "F_Bor"),
    }
    results["T1_bar_parity"] = par

    # The claim under test: the /q^3 is the UNIQUE bar-symmetry-breaking
    # factor in F_Bor.  If tr_M and [3]! are both bar-even and q^-3 is not,
    # then F_Bor's bar-asymmetry is entirely carried by the framing factor.
    t1_ok = (par["tr_M(beta_Bor)"] == "even"
             and par["[3]_q!"] == "even"
             and par["q^-3"] == "neither")
    results["T1_framing_is_sole_bar_breaker"] = bool(t1_ok)
    if not t1_ok:
        failures.append(f"T1: expected (even, even, neither), got {par}")

    # ---- T2: H_3 full-twist eigenvalues --------------------------------
    twist = {}
    for name, shape in PARTITIONS_3.items():
        c = content_sum(shape)
        twist[name] = {
            "content_sum": c,
            "dim": dim_specht(shape),
            "twist_eigenvalue": sp.srepr(sp.simplify(q ** c)),
            "twist_exponent": c,
        }
    results["T2_H3_ribbon_twist_by_block"] = twist
    exps = sorted(v["twist_exponent"] for v in twist.values())
    t2_ok = exps == [-3, 0, 3]
    results["T2_exponents_are_minus3_0_3"] = bool(t2_ok)
    if not t2_ok:
        failures.append(f"T2: content sums {exps}, expected [-3, 0, 3]")

    # ---- T3: does q^-3 sit on a block? ---------------------------------
    match = [n for n, v in twist.items() if v["twist_exponent"] == -3]
    results["T3_block_matching_q_minus_3"] = match
    t3_ok = match == ["(1^3)"]
    results["T3_q_minus_3_is_a_block_twist_eigenvalue"] = bool(t3_ok)
    results["T3_CONVENTION_STATUS"] = (
        "RESOLVED, and NOT the way this probe first recorded it. alpha = 1 "
        "is not a cited convention: QOU.BraidKnot.Keystone.theta is defined "
        "as q ^ contentSum l and is SORRY-FREE. What alpha = 2 belongs to is "
        "a DIFFERENT object, the full twist Delta^2 = theta^2. So q^-3 is the "
        "RIBBON twist on (1^3) and q^-6 is the full twist -- and gzs0's "
        "q^{T/2} at T = -6 is exactly the ribbon twist, so its arithmetic was "
        "right all along. Residual softness: the Lean docstring itself hedges "
        "'up to convention', which nothing in the corpus discharges."
    )
    if not t3_ok:
        failures.append(f"T3: q^-3 matched blocks {match}, expected ['(1^3)']")

    # ---- T4: the two competing per-component readings ------------------
    # gzs0 reads q^-3 = q^{T/2} with T = -6, i.e. -2 per component (3 comps).
    # The ribbon/Casimir reading at the fundamental colour n=1 gives
    # n(n+2) = 3 per component, hence 9 across three components.
    gzs0_T = -6
    gzs0_per_component = Fraction(gzs0_T, 3)
    casimir_per_component = 1 * (1 + 2)          # n(n+2) at n = 1
    casimir_total = 3 * casimir_per_component
    results["T4_readings"] = {
        "gzs0_total_T": gzs0_T,
        "gzs0_per_component": str(gzs0_per_component),
        "casimir_n_times_n_plus_2_at_n1": casimir_per_component,
        "casimir_total_three_components": casimir_total,
        "readings_agree": gzs0_per_component == casimir_per_component,
        "content_sum_1cubed": content_sum([1, 1, 1]),
    }
    # This is a DISCRIMINATOR, not a pass/fail: it records which reading the
    # exponent -3 is compatible with.  -3 is the (1^3) content sum exactly;
    # it is NOT -2 per component (that would need T/2 = -3 with 3 components
    # each contributing -1) and NOT the 3-component Casimir total 9.
    results["T4_verdict"] = (
        "q^-3 equals the (1^3) content sum exactly (-3). It is NOT the "
        "three-component fundamental-colour Casimir total (9), and gzs0's "
        "'-2 per component' is a re-reading of the same -3 total via T/2, "
        "not an independent per-component fact: nothing in F_Bor is indexed "
        "by component."
    )

    # ---- T5: WHY the twist is the sole bar-breaker (explains T1) --------
    # Keystone.theta_conjugate (sorry-free): theta_{lambda'} = (theta_lambda)^-1,
    # from the signed content flip c(lambda') = -c(lambda). So the ribbon twist
    # is precisely the bar-ODD half of the modular data -- the S-matrix half is
    # bar-EVEN (qDim_conj: d_q(lambda') = d_q(lambda)). T1 found q^-3 to be the
    # unique bar-breaker in F_Bor; T5 says that is forced, not incidental.
    conj_pairs = {"(3)": "(1^3)", "(1^3)": "(3)", "(2,1)": "(2,1)"}
    t5_rows = {}
    t5_ok = True
    for name, cname in conj_pairs.items():
        c, cc = twist[name]["content_sum"], twist[cname]["content_sum"]
        ok = (cc == -c)
        t5_ok = t5_ok and ok
        t5_rows[name] = {"conjugate": cname, "c": c, "c_conj": cc,
                         "content_flip_holds": ok}
    results["T5_content_flip_by_block"] = t5_rows
    results["T5_theta_conj_consistent"] = bool(t5_ok)
    results["T5_note"] = (
        "c(lambda') = -c(lambda) holds on every H_3 block, so "
        "theta_{lambda'} = theta_lambda^-1 (Keystone.theta_conjugate, "
        "sorry-free). (1^3) is the TRANSPOSE of (3), so theta_{(1^3)} = "
        "theta_{(3)}^-1 = q^-3. The ribbon twist is the bar-ODD half of the "
        "modular data; the S-matrix half is bar-EVEN (qDim_conj). That is WHY "
        "T1 finds the twist factor to be F_Bor's unique bar-symmetry breaker: "
        "it is the only piece of the modular data that can be."
    )
    if not t5_ok:
        failures.append(f"T5: content flip failed: {t5_rows}")

    # ---- numeric cross-check at the proton pin (mpmath, never float) ----
    try:
        from mpmath import mp, mpf
        from qou_substrate.constants import Q_50_DIGIT_STR
        mp.dps = 60
        q0 = mpf(Q_50_DIGIT_STR)
        f_num = sp.lambdify(q, f_bor, modules="mpmath")
        results["numeric_at_proton_pin"] = {
            "q0": mp.nstr(q0, 30),
            "F_Bor": mp.nstr(f_num(q0), 30),
            "q0_pow_minus_3": mp.nstr(q0 ** -3, 30),
            "note": "mpmath end-to-end; no float64 anywhere in this probe",
        }
    except Exception as exc:                      # pragma: no cover
        results["numeric_at_proton_pin"] = {"skipped": repr(exc)}

    # ---------------------------------------------------------------- report
    print("=" * 70)
    print("F_Bor's /q^3 -- ribbon twist, or coincidence of shape?")
    print("=" * 70)
    print("\nT1  bar-parity of each factor")
    for k, v in par.items():
        print(f"      {k:<22} {v}")
    print(f"    framing is the sole bar-breaker: {t1_ok}")

    print("\nT2  H_3 RIBBON-twist eigenvalue theta_lambda by Wedderburn block")
    print(f"      {'block':<10} {'dim':>4} {'content sum':>12}   twist")
    for name, v in twist.items():
        print(f"      {name:<10} {v['dim']:>4} {v['content_sum']:>12}   "
              f"q^{v['content_sum']}")

    print(f"\nT3  q^-3 matches block(s): {match}")
    print("    theta = q^{c} is Keystone.theta, SORRY-FREE Lean -- not a cited")
    print("    convention. The full twist Delta^2 = theta^2 = q^-6 is a")
    print("    different object; gzs0's q^{T/2} at T=-6 IS this ribbon twist.")
    print(f"\nT4  {results['T4_verdict']}")

    print("\nT5  content flip c(lambda') = -c(lambda) on every block: "
          f"{t5_ok}")
    print("    => theta_{lambda'} = theta_lambda^-1 (Keystone.theta_conjugate).")
    print("    (1^3) is the transpose of (3), so theta_{(1^3)} = q^-3.")
    print("    The twist is the bar-ODD half of the modular data -- which is")
    print("    WHY T1 finds it to be F_Bor's unique bar-symmetry breaker.")

    print("\n" + "=" * 70)
    if failures:
        print("FAILED:")
        for f in failures:
            print("  -", f)
    else:
        print("All assertions held.")
    print("=" * 70)

    out = __import__("pathlib").Path(__file__).with_suffix(".result.json")
    with out.open("w") as fh:
        json.dump(results, fh, indent=2, default=str)

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
