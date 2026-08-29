#!/usr/bin/env python3
"""
Xi_k moment family -- the general-mu companion of the proved
`2z - h = [2]_q * Xi_2` loop-mean identity.

CONTEXT. The 2026-08-21 ladder-phase audit proved (sorry-free Lean
`loopMean_eq_twoQ_mul_moment`) that, in ANY convention,

    2z - h = [2]_q * Xi ,    Xi := sum_lambda chi^lambda(tau) * y_lambda

with `chi^lambda(tau)` the ORDINARY S_n character at a transposition, and that
`Xi` is independent of `n` (forced by the identity, since `2z - h` carries no
`n`). Under convention D the weights are the two-variable Schur measure
`y_lambda = s_lambda(1,Q)/(1+Q)^n`, `Q = q^2` (Wenzl level r = 2), giving
`Xi_D = (1+Q^2)/(1+Q)^2`.

WHAT THIS PROBE ADDS. `tau` is the class `(2,1^(n-2))`. Nothing about the
argument is special to a transposition: for ANY class `mu`, Frobenius
(`sum_lambda chi^lambda(mu) s_lambda = p_mu`) gives

    Xi_mu = p_mu(1,Q) / (1+Q)^n ,

and for the k-cycle classes `mu = (k, 1^(n-k))` this collapses to the
n-INDEPENDENT family

    Xi_k = (1 + Q^k) / (1 + Q)^k .

Checked here from the ACTUAL Murnaghan-Nakayama characters against the actual
D weights -- not from the Frobenius shortcut -- so the identity is measured,
not assumed. `k = 2` must reproduce the corpus's proved loop-mean identity;
that is the harness calibration and it is asserted.

WHY IT MATTERS (and what it does NOT claim). Bean `qou-cds1`'s D-frame
eigenphase result leaves ONE undetermined object: the residual
`ce = z* - z_D^even`, which is BAR-EVEN and therefore not excluded by the
parity argument that fixes the bar-odd half (`co = -h/2` uniquely). The
`Xi_k` are, as far as a four-path corpus grep can find, the only DERIVED,
parameter-free, n-independent family of bar-even weight functionals the
framework has. Their numerators `1 + Q^k = 1 + q^(2k)` are CYCLOTOMIC
(k=1,2,3,4 -> 1, Phi_8, Phi_12, Phi_16).

Registry KC20's "the bar-odd carrier is NOT a root-of-unity object" does NOT
bind here: KC20 is a statement about the bar-ODD carrier. The bar-EVEN channel
has not been examined cyclotomically.

*** ANTI-FIT NOTICE -- READ BEFORE USING THIS FAMILY. ***
`ce` is resolved to only 1.45% by sigma(Q_beta)/Q_beta (bean `qou-cds1`:
68.8 sigma). A family with a free index `k` will supply a member inside a 1.45%
window by arithmetic alone. This probe therefore DELIBERATELY does not compare
any `Xi_k` to `ce`, and no such comparison may be quoted as evidence. The
family's value is STRUCTURAL -- as a derived source for the even channel a
derivation may draw on -- not as a match. Selecting `k` against the data is a
fit and is banned by this bean's own discipline.

Exact symbolic over Q(q). NO anchors, NO c_k value, NO fit, NO wiring.
"""
import datetime
import hashlib
import json
import os
import subprocess

import sympy as sp
from functools import lru_cache
from sympy.utilities.iterables import partitions


def _repo_head_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True,
        ).strip()
    except Exception:
        return None


def parts_of(n):
    out = []
    for p in partitions(n):
        lam = []
        for k in sorted(p, reverse=True):
            lam += [k] * p[k]
        out.append(tuple(lam))
    return out


@lru_cache(maxsize=None)
def mn_char(lam, mu):
    """Ordinary S_n character chi^lam(mu) by Murnaghan-Nakayama on beta-numbers."""
    lam = tuple(x for x in lam if x > 0)
    mu = tuple(x for x in mu if x > 0)
    if not mu:
        return 1 if not lam else 0
    k, rest = mu[0], mu[1:]
    r = len(lam)
    beta = [lam[i] + (r - 1 - i) for i in range(r)]
    total = 0
    for i in range(r):
        nb = beta[i] - k
        if nb < 0 or nb in beta:
            continue
        newbeta = sorted([b for j, b in enumerate(beta) if j != i] + [nb], reverse=True)
        ht = sum(1 for b in beta if nb < b < beta[i])
        m = len(newbeta)
        newlam = tuple(sorted([newbeta[j] - (m - 1 - j) for j in range(m)], reverse=True))
        total += (-1) ** ht * mn_char(newlam, rest)
    return total


def schur_two_var(lam, a, b):
    """s_lambda(a,b); zero for l(lambda) > 2 (Wenzl level r = 2)."""
    lam = [x for x in lam if x > 0]
    if len(lam) > 2:
        return sp.Integer(0)
    l1 = lam[0] if lam else 0
    l2 = lam[1] if len(lam) >= 2 else 0
    d = l1 - l2
    return sp.expand((a * b) ** l2 * sum(a ** i * b ** (d - i) for i in range(d + 1)))


def main():
    q = sp.symbols("q", positive=True)
    Q = q ** 2
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # -- A1: the family, from real characters against the real D weights -----
    family_ok = True
    rows = []
    for n in range(2, 8):
        lams = parts_of(n)
        for k in range(1, n + 1):
            mu = tuple([k] + [1] * (n - k))
            Xi = sum(sp.Integer(mn_char(lam, mu)) * schur_two_var(lam, 1, Q)
                     for lam in lams) / (1 + Q) ** n
            pred = (1 + Q ** k) / (1 + Q) ** k
            agree = sp.simplify(sp.together(Xi) - pred) == 0
            family_ok &= agree
            if n == 7:
                rows.append({"k": k, "Xi_k": sp.srepr(sp.factor(pred)),
                             "Xi_k_str": str(sp.factor(pred))})
    check("xi_k_equals_one_plus_Qk_over_one_plus_Q_k__n_2_to_7", family_ok)

    # -- A2 (CALIBRATION): k=2 must reproduce the corpus's proved identity ----
    h, zD = q - 1 / q, q ** 3 / (q ** 2 + 1)
    Xi2 = (1 + Q ** 2) / (1 + Q) ** 2
    check("loopMean_identity_2z_minus_h_eq_bracket2_times_Xi2",
          sp.simplify((2 * zD - h) - (q + 1 / q) * Xi2) == 0)

    # -- A3: every member is exactly bar-EVEN (twist 1) ----------------------
    check("xi_k_exactly_bar_even_k_1_to_6",
          all(sp.simplify(((1 + Q ** k) / (1 + Q) ** k).subs(q, 1 / q)
                          - (1 + Q ** k) / (1 + Q) ** k) == 0 for k in range(1, 7)))

    # -- A4: numerators are cyclotomic ---------------------------------------
    check("xi_k_numerator_is_cyclotomic_k_1_to_4",
          all(sp.simplify(sp.expand(1 + Q ** k)
                          - sp.expand(sp.cyclotomic_poly(4 * k, q))) == 0
              for k in (1, 2, 4)) and
          sp.simplify(sp.expand(1 + Q ** 3)
                      - sp.expand((1 + Q) * sp.cyclotomic_poly(12, q))) == 0)

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "DERIVED FAMILY (scope: structural, nothing wired). The proved loop-mean "
        "identity 2z - h = [2]_q * Xi_2 is the k=2 member of an n-independent, "
        "parameter-free, exactly-bar-even family Xi_k = (1+Q^k)/(1+Q)^k with "
        "cyclotomic numerators, obtained from the SAME D weights and ordinary "
        "S_n characters at the k-cycle classes. It is the only derived source of "
        "bar-even weight functionals located by corpus grep, and KC20's "
        "no-root-of-unity exclusion does not bind it (KC20 is about the bar-ODD "
        "carrier). NOT COMPARED to the cds1 residual ce and must not be: ce is "
        "resolved to 1.45%, so any k selected against the data is a fit."
        if all_passed else
        "INCONCLUSIVE -- an identity assertion failed; re-derive before citing."
    )

    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-xi-moment-family",
        "description": "The k-cycle moment family Xi_k = (1+Q^k)/(1+Q)^k of the "
                       "convention-D Schur-measure weights, verified from "
                       "Murnaghan-Nakayama characters for n = 2..7; the corpus's "
                       "proved loop-mean identity is its k=2 member.",
        "engine": "sympy-exact",
        "markov_convention": "D",
        "assertions": assertions,
        "data": {"family": "Xi_k = (1 + Q^k)/(1 + Q)^k, Q = q^2",
                 "n_range_checked": [2, 7], "rows_at_n_7": rows,
                 "bar_parity": "exactly even (twist 1) for every k"},
        "verdict": verdict,
        "witness": {
            "scriptPath": "computations/qbeta/" + os.path.basename(__file__),
            "scriptHash": hashlib.sha256(src).hexdigest()[:12],
            "commitSha": _repo_head_sha(),
            "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        },
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "qbeta-xi-moment-family.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\n{verdict}\n\nWitness: {os.path.basename(out)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
