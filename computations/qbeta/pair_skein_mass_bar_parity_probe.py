#!/usr/bin/env python3
"""
THE BAR-EVEN DENOMINATOR IN S_ab IS FORCED.  IT IS NOT A SIGN SLIP.

Answers a flag raised by sibling PR #6820 (bean `qou-8bxv`) on PR #6823.

THE QUESTION
------------
`prf:hadron-half-life` item 4 (predicted-spectra/hadron-half-life-proof.md:37)
gives the pair Skein mass formula

    S_ab(q) = (q mu_a + q^-1 mu_b) / (q^(1/2) + q^(-1/2))

Its NUMERATOR carries the asymmetric convention-(J) weights (q, q^-1), but its
DENOMINATOR is the bar-EVEN cofactor `q^(1/2) + q^(-1/2)`, not the bar-ODD
bridge `s = q^(1/2) - q^(-1/2)` that (J) would put there.  #6820 left three
readings open and asked whoever is in the derivation to decide:

    (R1) a third normalisation,
    (R2) a sign slip for `s`,
    (R3) a deliberate symmetrising normalisation, because S_ab is a MASS and
         not an amplitude.

VERDICT: (R3).  Two independent structural arguments, both decisive, neither
numerical -- this is a formalize-first prune, not a search.

ARGUMENT 1 -- BAR-COVARIANCE.  A mass must map to a mass under q -> 1/q.
  even denominator:  S_ab(1/q) = +S_ba(q)   the bar involution EXCHANGES the
                                            two constituents.  A mass maps to
                                            a mass; this is what a mirror does.
  odd  denominator:  S_ab(1/q) = -S_ba(q)   the mirror of a mass is a NEGATIVE
                                            mass.  Excluded.
  Both are exact identities, not approximations: the numerator picks up the
  a<->b swap under q -> 1/q, and the denominator is even (+) or odd (-).

ARGUMENT 2 -- THE CLASSICAL LIMIT q -> 1, and this one is fatal.
  even:  S_ab -> (mu_a + mu_b)/2, the arithmetic mean; and the self-pair
         S_aa -> mu_a exactly.  Both are the right classical answers.
  odd:   the numerator tends to mu_a + mu_b != 0 while the denominator tends
         to 0, so S_ab DIVERGES like (mu_a + mu_b)/(q - 1).
  This contradicts the corpus's own stated classical limit.
  `hadron-half-life-fermi.md`:
      "In the classical limit q = 1, s = 0 and [2]_1 = 2; crossing asymmetry
       vanishes, isobars become degenerate (Q = 0) and beta decay ceases."
  Under the odd bridge Q would DIVERGE at q = 1, and since f(Q) ~ Q^5 the decay
  rate would diverge rather than cease -- the exact opposite of the corpus's
  own limit.  So (R2) is not merely unattractive; adopting it would break a
  statement the framework already makes.

ARGUMENT 3 (corroborating, not independent) -- THE ROLE SPLIT IS CONSISTENT.
  The corpus puts the bar-ODD `s` in the NUMERATOR of amplitudes -- the matrix
  element is |M_q|^2 = s^2 * prod_i |V_i^par / V_i^dau|^2, which correctly
  tends to 0 at q = 1 -- and the bar-EVEN cofactor in the DENOMINATOR of
  masses.  Bar-odd where vanishing is wanted, bar-even where finiteness is
  wanted.  That is a coherent convention, not an inconsistency.

SCOPE.  (b) structural exclusion for the odd bridge in THIS formula, on the
proved invariant that a q -> 1 limit must be finite and a mass must not change
sign under the bar involution.  It says nothing about which Skein normalisation
is canonical elsewhere in the corpus -- that is #6820's question and is
untouched here.

PRECISION.  mpmath at 60 dps; the identities are exact and are checked as such.
No float64.  float() appears nowhere.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent)]

mp.mp.dps = 60

from substrate.q_parameter import Q_50_DIGIT_STR as Q0  # noqa: E402 -- proton pin


def S_even(q, ma, mb):
    """S_ab exactly as prf:hadron-half-life item 4 writes it (bar-EVEN cofactor)."""
    return (q * ma + mb / q) / (mp.sqrt(q) + 1 / mp.sqrt(q))


def S_odd(q, ma, mb):
    """The convention-(J)-consistent alternative #6820 asks about (bar-ODD bridge s)."""
    return (q * ma + mb / q) / (mp.sqrt(q) - 1 / mp.sqrt(q))


def main() -> int:
    q0 = mp.mpf(str(Q0))
    # generic distinct positives -- every claim below is mu-independent
    ma, mb = mp.mpf("0.31"), mp.mpf("0.33")
    checks = []

    print("=" * 74)
    print(" S_ab's bar-EVEN denominator is FORCED -- answering PR #6820 item 2")
    print("=" * 74)

    # ---- ARGUMENT 1: bar-covariance ------------------------------------
    print("\n[1] bar involution q -> 1/q   (a mass must map to a mass)")
    e_lhs, e_rhs = S_even(1 / q0, ma, mb), S_even(q0, mb, ma)
    o_lhs, o_rhs = S_odd(1 / q0, ma, mb), S_odd(q0, mb, ma)
    print(f"    EVEN: S_ab(1/q) - S_ba(q) = {mp.nstr(e_lhs - e_rhs, 6)}   -> S_ab(1/q) = +S_ba(q)")
    print(f"    ODD : S_ab(1/q) + S_ba(q) = {mp.nstr(o_lhs + o_rhs, 6)}   -> S_ab(1/q) = -S_ba(q)")
    print(f"          i.e. the odd bridge sends {mp.nstr(o_rhs, 8)} -> {mp.nstr(o_lhs, 8)}: a NEGATIVE mass")
    checks.append({
        "name": "even_denominator_makes_bar_exchange_constituents",
        "pass": bool(abs(e_lhs - e_rhs) < mp.mpf("1e-50")),
        "detail": f"S_ab(1/q) - S_ba(q) = {mp.nstr(e_lhs - e_rhs, 6)} at 60 dps -- the bar "
                  "involution exchanges a and b and preserves the sign, so a mass maps to a mass",
    })
    checks.append({
        "name": "odd_bridge_makes_the_mirror_of_a_mass_negative",
        "pass": bool(abs(o_lhs + o_rhs) < mp.mpf("1e-50")),
        "detail": f"S_ab(1/q) + S_ba(q) = {mp.nstr(o_lhs + o_rhs, 6)}, i.e. S_ab(1/q) = -S_ba(q). "
                  f"The mirror of the mass {mp.nstr(o_rhs, 8)} is {mp.nstr(o_lhs, 8)}. Excluded "
                  "for a mass.",
    })

    # ---- ARGUMENT 2: the classical limit -------------------------------
    print("\n[2] classical limit q -> 1   (the corpus requires Q -> 0 and decay to CEASE)")
    mean = (ma + mb) / 2
    print(f"    arithmetic mean (mu_a+mu_b)/2 = {mp.nstr(mean, 12)}")
    rows = []
    for e in ("1e-3", "1e-6", "1e-9"):
        q = 1 + mp.mpf(e)
        se, so = S_even(q, ma, mb), S_odd(q, ma, mb)
        pred = (ma + mb) / mp.mpf(e)          # analytic: S_odd ~ (mu_a+mu_b)/(q-1)
        rows.append((e, se, so, pred))
        print(f"    q=1+{e}:  S_even = {mp.nstr(se, 12)}   S_odd = {mp.nstr(so, 8)}"
              f"   [predicted (mu_a+mu_b)/(q-1) = {mp.nstr(pred, 8)}]")
    conv = all(abs(r[1] - mean) < mp.mpf(r[0]) for r in rows)
    div = all(abs(r[2] / r[3] - 1) < mp.mpf("1e-2") for r in rows)
    checks.append({
        "name": "even_denominator_gives_the_arithmetic_mean_at_q_eq_1",
        "pass": bool(conv),
        "detail": f"S_even -> (mu_a+mu_b)/2 = {mp.nstr(mean, 12)}; the residual falls linearly "
                  "with q-1 at all three probe points",
    })
    checks.append({
        "name": "odd_bridge_DIVERGES_at_q_eq_1_like_one_over_q_minus_one",
        "pass": bool(div),
        "detail": "S_odd matches the analytic pole (mu_a+mu_b)/(q-1) to better than 1% at "
                  "q-1 = 1e-3, 1e-6, 1e-9. Since f(Q) ~ Q^5, the odd bridge makes the decay RATE "
                  "diverge at q=1 -- the exact opposite of the corpus's own stated limit "
                  "(hadron-half-life-fermi.md: 'isobars become degenerate (Q = 0) and beta "
                  "decay ceases'). This is what makes reading (R2), a sign slip, untenable.",
    })

    # ---- self-pair sanity ------------------------------------------------
    print("\n[3] self-pair S_aa at q -> 1 (even denominator)")
    for e in ("1e-6", "1e-12"):
        q = 1 + mp.mpf(e)
        print(f"    q=1+{e}: S_aa = {mp.nstr(S_even(q, ma, ma), 15)}   mu_a = {mp.nstr(ma, 15)}")
    saa = S_even(1 + mp.mpf("1e-12"), ma, ma)
    checks.append({
        "name": "even_denominator_gives_S_aa_eq_mu_a_at_q_eq_1",
        "pass": bool(abs(saa - ma) < mp.mpf("1e-10")),
        "detail": f"S_aa(1+1e-12) = {mp.nstr(saa, 15)} against mu_a = {mp.nstr(ma, 15)} -- the "
                  "self-pair reduces to the constituent mass, as a pair mass must",
    })

    # ---- at the substrate -------------------------------------------------
    print("\n[4] at the substrate q_0 (for the record)")
    print(f"    q_0      = {mp.nstr(q0, 20)}")
    print(f"    S_ab(q0) = {mp.nstr(S_even(q0, ma, mb), 15)}")
    print(f"    S_ba(q0) = {mp.nstr(S_even(q0, mb, ma), 15)}")

    print("\n" + "=" * 74)
    n = sum(1 for c in checks if c["pass"])
    print(f" {n}/{len(checks)} checks pass   ->   reading (R3): the symmetrising "
          "normalisation is FORCED")
    print("=" * 74)

    out = HERE / "pair-skein-mass-bar-parity.witness.json"
    out.write_text(json.dumps({
        "schema": "qou-probe/v1",
        "name": "pair-skein-mass-bar-parity",
        "description":
            "Answers PR #6820 item 2. The bar-EVEN denominator of the pair Skein mass "
            "S_ab(q) = (q mu_a + q^-1 mu_b)/(q^1/2 + q^-1/2) in prf:hadron-half-life item 4 "
            "is FORCED, not a sign slip: the bar-odd bridge s would make the mirror of a mass "
            "negative, and would make S_ab diverge at q=1 where the corpus requires Q -> 0 and "
            "decay to cease.",
        "q0_anchor": "physical_proton",
        "q0Value": mp.nstr(q0, 20),
        "verdict": "(R3) deliberate symmetrising normalisation -- S_ab is a mass, not an amplitude",
        "scope": "(b) structural exclusion of the odd bridge IN THIS FORMULA, on two proved "
                 "invariants (finiteness of the q->1 limit; sign-preservation of a mass under "
                 "the bar involution). Says nothing about which Skein normalisation is canonical "
                 "elsewhere -- that is #6820's separate question and is untouched.",
        "source": "content/quantum-observable-universe/predicted-spectra/hadron-half-life-proof.md:37",
        "checks": checks,
    }, indent=2) + "\n")
    print(f"\nwitness -> {out}")
    return 0 if n == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
