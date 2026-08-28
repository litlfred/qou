#!/usr/bin/env python3
"""Is N = 2 forced by the mass pipeline, or is the Ocneanu parameter free?
(beans qou-w5fw / T3f, qou-8p1x)

The question
------------
T3f (`docs/audits/2026-08-04-ocneanu-trace-parameter-audit.md`) established that
the Ocneanu/Markov trace on the Hecke tower carries a free parameter
`a = q^{N-1}` selecting which `gl_N`-weighted invariant the trace computes:

    a = q    -> Jones      (gl_2)  -- what the mass pipeline uses
    a = q^2  -> gl_3 invariant     -- the eightfold way

and left the status **GENUINELY OPEN**: "Neither 'derived' nor 'freely chosen'
is established."  Its §3c argued the mass pipeline is *structurally* tied to
`N = 2` because `dim V_{(2,1)}` is 2 at `N = 2` but 8 at `N = 3`, and called
this a **soft constraint** -- "not a theorem, but a structural compatibility".

This probe upgrades that from soft to hard, using only objects the framework
already has.

The mechanism
-------------
The framework's canonical trace is the Frobenius pairing over partitions,

    tr_M(beta) = sum over lambda of  y_lambda * chi_lambda(beta),

where the `chi_lambda` are Hecke-algebra characters -- **independent of N** --
and the weights `y_lambda` are the **principal specialisations** of Schur
functions (hence the corpus module name `schur_principal_mpmath`):

    y_lambda  ~  s_lambda(1, q, q^2, ..., q^{N-1}).

So *all* of the N-dependence of the trace sits in the weights, and it is fully
explicit via the q-analogue of the hook-content formula:

    s_lambda(1, q, ..., q^{N-1})
        = q^{n(lambda)} * prod over cells (i,j) of [N + j - i]_q / [h(i,j)]_q

with `[m]_q = (1 - q^m)/(1 - q)` and `h` the hook length.  This is computed here
in exact arithmetic.

What is checked
---------------
  C1  **Cross-check against the Lean.** At `q = 1` the principal specialisation
      must reproduce `RowCapObstruction.lean`'s Weyl dimensions:
        s_{(3)}   (1^N) = C(N+2,3)   = `weylDimSym N`
        s_{(2,1)} (1^N) = N(N^2-1)/3 = `weylDimMixed N` = 2*C(N+1,3)
        s_{(1^3)} (1^N) = C(N,3)     = `weylDimAlt N`
      This ties the probe to already-formalised content rather than asserting a
      formula.

  C2  **The row cap is the vanishing of a weight.** `y_{(1^3)} = 0` at `N = 2`
      for every `q`, because the cell content `-2` contributes the factor
      `[N-2]_q = [0]_q = 0`.  At `N = 3` it is nonzero.  So "the row cap kills
      the singlet at N = 2" and "the Ocneanu weight vanishes at N = 2" are the
      *same fact*.

  C3  **The two traces are not proportional.** If the `N = 2` and `N = 3`
      traces differed only by an overall scale, the mass pipeline would be
      insensitive to `N` after normalisation.  They do not:

          y_{(2,1)} / y_{(3)}  =  q * [2]_q * [N-1]_q / [N+2]_q

      which is `q[2][1]/[4]` at `N = 2` and `q[2][2]/[5]` at `N = 3` -- different
      rational functions of `q`.  Checked at several exact rational `q`.

Result
------
**N = 2 is locked in for the mass pipeline.**  Moving to `N = 3` does not merely
add the singlet channel; it *re-weights the surviving channels relative to one
another*, so `tr_M` changes on elements the mass pipeline already evaluates.
The constraint is therefore not soft: any `N = 3` flavour channel must be a
**separate trace**, not a re-parameterisation of the mass trace.

This is the good outcome for the eightfold programme, not the bad one.  T3b §2c
asked whether the Hecke tower can support "BOTH an N = 2 Jones trace (for mass)
and an N = 3 HOMFLY trace (for flavour) simultaneously, as two different
functors on the same algebraic object".  The answer is yes -- the Ocneanu trace
is a *family* and each member is a perfectly good Markov trace on `H_n(q)`;
`HnMarkovTrace.lean` already types the parameter as a free class **field**
(only `z_pos`), so two instances are typeable today.  What this probe shows is
that the separation is **mandatory** rather than optional: you cannot get the
flavour channel by re-tuning the mass channel, because that would move the mass
numbers.

Scope
-----
**scope-(b)** for the specific claim "the `N = 2` and `N = 3` Ocneanu traces on
`H_3(q)` differ by an overall normalisation" -- excluded by an exact
computation of the weight ratio.

NOT claimed:
  * that `N = 2` is derived from the Descartes condition.  It is not; this
    probe shows only that the *mass pipeline* cannot be re-tuned to `N = 3`.
    Why the mass channel is the `N = 2` one remains open.
  * that the `N = 3` trace reproduces any physical flavour observable.  That is
    the Gavrilik test (TG), untouched here.
  * anything about *colour* `SU(3)`.  This is the flavour channel.

Exact arithmetic only: `Fraction`-valued polynomials in `q`, no floating point.
"""
from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
_OUT = HERE / "ocneanu-N-lockin.witness.json"


# ---------------------------------------------------------------------------
# Partitions of 3, with the cell data the hook-content formula needs.
# ---------------------------------------------------------------------------
PARTITIONS = {
    "(3)": (3,),
    "(2,1)": (2, 1),
    "(1^3)": (1, 1, 1),
}


def cells(lam):
    return [(i, j) for i, row in enumerate(lam) for j in range(row)]


def hook_length(lam, i, j):
    """Arm + leg + 1, with 0-indexed (i, j)."""
    arm = lam[i] - j - 1
    leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
    return arm + leg + 1


def content(i, j):
    """Cell content j - i (0-indexed)."""
    return j - i


def n_of(lam):
    """n(lambda) = sum (i-1)*lambda_i, 1-indexed = sum i*lam[i] 0-indexed."""
    return sum(i * part for i, part in enumerate(lam))


def q_int(m: int, q: Fraction) -> Fraction:
    """[m]_q = 1 + q + ... + q^{m-1}.  [0]_q = 0."""
    if m <= 0:
        # [0]_q = 0; negative m does not occur for the N values used here,
        # but guard anyway -- a negative content factor would signal an error.
        return Fraction(0)
    return sum((q ** k for k in range(m)), Fraction(0))


def principal_spec(lam, N: int, q: Fraction) -> Fraction:
    """s_lambda(1, q, ..., q^{N-1}) via the q-hook-content formula."""
    num = Fraction(1)
    den = Fraction(1)
    for (i, j) in cells(lam):
        num *= q_int(N + content(i, j), q)
        den *= q_int(hook_length(lam, i, j), q)
    return (q ** n_of(lam)) * num / den


def main() -> int:
    print("=" * 74)
    print("T3f : is N = 2 locked in for the mass pipeline?")
    print("=" * 74)

    checks: dict[str, bool] = {}

    # -- C1 : q = 1 must reproduce the Lean's Weyl dimensions ---------------
    print("\nC1  q -> 1 cross-check against RowCapObstruction.lean")
    print("    %-8s %-6s %-10s %-10s %s" % ("lambda", "N", "s_lam(1^N)", "Lean", "match"))
    lean = {
        "(3)": lambda N: comb(N + 2, 3),          # weylDimSym
        "(2,1)": lambda N: 2 * comb(N + 1, 3),    # weylDimMixed
        "(1^3)": lambda N: comb(N, 3),            # weylDimAlt
    }
    c1_ok = True
    one = Fraction(1)
    for name, lam in PARTITIONS.items():
        for N in (2, 3, 4, 5):
            got = principal_spec(lam, N, one)
            want = lean[name](N)
            ok = got == want
            c1_ok &= ok
            if N in (2, 3):
                print("    %-8s %-6d %-10s %-10s %s" % (name, N, got, want, ok))
    checks["C1_q1_matches_lean_weyl_dims"] = c1_ok
    print(f"    all N in 2..5, all three partitions : {c1_ok}")

    # -- C2 : the row cap IS the vanishing of the Ocneanu weight -----------
    print("\nC2  the row cap = vanishing of y_(1^3) at N = 2")
    qs = [Fraction(2), Fraction(3), Fraction(5, 2), Fraction(11, 10), Fraction(7, 5)]
    c2_zero = all(principal_spec(PARTITIONS["(1^3)"], 2, q) == 0 for q in qs)
    c2_nonzero = all(principal_spec(PARTITIONS["(1^3)"], 3, q) != 0 for q in qs)
    checks["C2_singlet_weight_zero_at_N2"] = c2_zero
    checks["C2_singlet_weight_nonzero_at_N3"] = c2_nonzero
    print(f"    y_(1^3) = 0 at N=2 for every tested q : {c2_zero}")
    print(f"    y_(1^3) != 0 at N=3 for every tested q : {c2_nonzero}")
    print("    (cell content -2 gives the factor [N-2]_q = [0]_q = 0 at N=2)")

    # -- C3 : the two traces are NOT proportional --------------------------
    print("\nC3  ratio y_(2,1)/y_(3) -- equal would mean 'same trace up to scale'")
    print("    %-10s %-22s %-22s %s" % ("q", "N=2 ratio", "N=3 ratio", "differ?"))
    c3_ok = True
    ratios = []
    for q in qs:
        r2 = (principal_spec(PARTITIONS["(2,1)"], 2, q)
              / principal_spec(PARTITIONS["(3)"], 2, q))
        r3 = (principal_spec(PARTITIONS["(2,1)"], 3, q)
              / principal_spec(PARTITIONS["(3)"], 3, q))
        differ = r2 != r3
        c3_ok &= differ
        ratios.append({"q": str(q), "ratio_N2": str(r2), "ratio_N3": str(r3),
                       "differ": differ})
        print("    %-10s %-22s %-22s %s" % (q, r2, r3, differ))
    checks["C3_traces_not_proportional"] = c3_ok

    all_ok = all(checks.values())
    print("\n" + "=" * 74)
    print(f"ALL CHECKS PASS : {all_ok}")
    print("=" * 74)
    print("""
VERDICT (T3f / qou-w5fw, qou-8p1x)
----------------------------------
N = 2 IS LOCKED IN FOR THE MASS PIPELINE.  Moving to N = 3 does not merely add
the singlet channel: it RE-WEIGHTS the surviving channels relative to one
another (C3), so tr_M changes on elements the mass pipeline already evaluates.
T3f's "soft constraint" is therefore hard, for the specific and checkable
reason that the two traces are not proportional.

This is the GOOD outcome for the eightfold programme.  T3b section 2c asked
whether the Hecke tower can carry both an N = 2 Jones trace (mass) and an N = 3
HOMFLY trace (flavour) as two functors on one algebra.  It can -- the Ocneanu
trace is a family, every member is a valid Markov trace, and
HnMarkovTrace.lean already types the parameter as a free class field.  What
this probe adds is that the separation is MANDATORY, not optional: you cannot
reach the flavour channel by re-tuning the mass channel, because that moves the
mass numbers.

Also worth recording: C2 shows "the row cap kills the singlet at N = 2" and
"the Ocneanu weight y_(1^3) vanishes at N = 2" are the SAME FACT, not two
facts.  RowCapObstruction.lean's weylDimAlt N = N.choose 3 is the q -> 1 shadow
of the principal specialisation (C1).

NOT CLAIMED: that N = 2 is *derived* from the Descartes condition -- it is not,
and why the mass channel is the N = 2 one remains open.  Nor that the N = 3
trace reproduces any flavour observable (that is the Gavrilik test, untouched).
Nor anything about COLOUR SU(3); this is the flavour channel.
""")

    payload = {
        "schema": "witness/v1",
        "description": (
            "The N=2 and N=3 Ocneanu traces on H_3(q) are not proportional, so "
            "the mass pipeline cannot be re-tuned to N=3: T3f's soft constraint "
            "is hard, and an N=3 flavour channel must be a SEPARATE trace. "
            "Beans qou-w5fw (T3f), qou-8p1x."
        ),
        "computation": {
            "script": "computations/ocneanu_N_lockin_probe.py",
            "arithmetic": "exact Fraction; q-hook-content formula; no floating point",
        },
        "data": {
            "mechanism": (
                "tr_M = sum_lambda y_lambda chi_lambda with chi_lambda "
                "N-independent and y_lambda ~ s_lambda(1,q,...,q^{N-1}), the "
                "principal specialisation; all N-dependence sits in the weights"
            ),
            "q1_cross_check_against_lean": {
                "s_(3)": "C(N+2,3) = weylDimSym",
                "s_(2,1)": "N(N^2-1)/3 = 2*C(N+1,3) = weylDimMixed",
                "s_(1^3)": "C(N,3) = weylDimAlt",
                "verified_for_N": [2, 3, 4, 5],
                "passes": checks["C1_q1_matches_lean_weyl_dims"],
            },
            "row_cap_is_weight_vanishing": {
                "y_singlet_zero_at_N2": checks["C2_singlet_weight_zero_at_N2"],
                "y_singlet_nonzero_at_N3": checks["C2_singlet_weight_nonzero_at_N3"],
                "reason": "cell content -2 contributes [N-2]_q = [0]_q = 0 at N=2",
            },
            "traces_not_proportional": {
                "ratio_formula": "y_(2,1)/y_(3) = q * [2]_q * [N-1]_q / [N+2]_q",
                "samples": ratios,
                "passes": checks["C3_traces_not_proportional"],
            },
            "verdict": (
                "N = 2 is locked in for the mass pipeline; moving to N = 3 "
                "re-weights the surviving channels, not merely adds the "
                "singlet. T3f's soft constraint is hard. An N = 3 flavour "
                "channel must therefore be a SEPARATE trace, which is "
                "permitted -- the Ocneanu trace is a family and "
                "HnMarkovTrace.lean types the parameter as a free class field."
            ),
            "scope": (
                "scope-(b) for the claim 'the N=2 and N=3 Ocneanu traces on "
                "H_3(q) differ by an overall normalisation', excluded by exact "
                "computation of the weight ratio"
            ),
            "not_claimed": [
                "that N = 2 is derived from the Descartes condition -- why the "
                "mass channel is the N=2 one remains open",
                "that the N=3 trace reproduces any flavour observable (the "
                "Gavrilik test TG, untouched here)",
                "anything about colour SU(3) -- this is the flavour channel",
            ],
            "all_checks_pass": all_ok,
            "checks": checks,
        },
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    payload.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        payload, script_path=__file__, engine=None, q0_anchor=False)
    _OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {_OUT.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
