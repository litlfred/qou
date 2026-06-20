#!/usr/bin/env python3
"""Convention-invariance check for the categorical Markov trace.

Witness producer for `prop:rigid-monoidal-structural-gap-invariance`
(content/quantum-observable-universe/mass-theory/
prop-rigid-monoidal-structural-gap-invariance.{ts,md}).

The proposition claims the categorical structural gap depends only on
the Markov-trace invariant tau(beta) — any two evaluation conventions
for the same braid word give the SAME trace. This probe verifies that
operationally by evaluating tr_M of canonical H_3 braid words through
two structurally independent, FULLY SYMBOLIC routes (no float64
anywhere; both routes are exact sympy expressions in q, compared
symbolically AND at substrate q_0 to 50 dps / 1e-40):

  Route A (NF-algebra): right-multiplication algebra on the 6-dim
      normal-form basis {1, s0, s1, s0s1, s1s0, s0s1s0} of H_3(q)
      with Groebner-style Hecke reduction folded into the
      multiplication table, then the Ocneanu trace vector
      TR = [1, z, z, z^2, z^2, h z^2 + z].

  Route B (axiomatic): derivation from the Markov axioms alone —
      M1 cyclicity, M2 peel tr(x s_max) = z tr(x) (s_max appearing
      exactly once), M3 tr(1) = 1, plus the Hecke quadratic — with
      no NF basis at all.

Conventions (AGENTS.md §7a): Hecke quadratic (s - q)(s + q^{-1}) = 0,
i.e. s_i^2 = h s_i + 1 with h = q - q^{-1}; Markov parameter
z = 1/(sqrt(q) + 1/sqrt(q)).

Words covered (H_3): s0 -> z; s0 s1 -> z^2; s0 s1 s0 -> h z^2 + z;
(s0 s1)^3 (trefoil closure word).

Historical note (recorded in the witness): the deprecated
`lp-duality-check.py` asserted tr_M(s0 s1 s0) = z^3 via an invalid
Markov-move chain (the M2 peel requires the maximal generator to
appear exactly once; in s1 s0 s1 it appears twice). The pyhecke fix
of 2026-05-19 (z^3 -> h z^2 + z, commit be773569) corrected the
trace; this probe re-derives the corrected value from the axioms and
supersedes lp-duality-check.py as this block's witness producer.

Diagnostic; no production wiring beyond the block's `computation`
pointer. Emits `rigid-monoidal-gap-invariance.witness.json`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# ── Shared symbols (AGENTS.md §7a conventions) ───────────────────
Q = sp.Symbol("q", positive=True)
H = Q - 1 / Q                          # Hecke parameter: s^2 = h s + 1
Z = 1 / (sp.sqrt(Q) + 1 / sp.sqrt(Q))  # Markov parameter

# NF basis order: b0=1, b1=s0, b2=s1, b3=s0s1, b4=s1s0, b5=s0s1s0.
BASIS_NAMES = ["1", "s0", "s1", "s0*s1", "s1*s0", "s0*s1*s0"]

# Ocneanu trace of each basis word (M2 peel on basis words, where the
# maximal generator appears exactly once — valid for b1..b4; b5 via
# cyclicity + Hecke: tr(s0 s1 s0) = tr(s0^2 s1) = h z^2 + z).
TR_SYM = [sp.Integer(1), Z, Z, Z ** 2, Z ** 2, H * Z ** 2 + Z]

# Right-multiplication table: RIGHT_MUL[g][i] = NF vector of b_i * s_g
# as a length-6 list of sympy coefficients. Derived once by hand from
# the braid relation s0 s1 s0 = s1 s0 s1 and the Hecke quadratic:
#   b5 * s0 = s0 s1 (s0^2) = h b5 + b3
#   b5 * s1 = s0 (s1 s0 s1) = s0 (s0 s1 s0) = (s0^2) s1 s0 = h b5 + b4
_z6 = lambda: [sp.Integer(0)] * 6  # noqa: E731
def _vec(**kw):
    v = _z6()
    for idx, coeff in kw.items():
        v[int(idx[1:])] = coeff
    return v

RIGHT_MUL = {
    0: [
        _vec(c1=sp.Integer(1)),                 # 1·s0       = s0
        _vec(c0=sp.Integer(1), c1=H),           # s0·s0      = h s0 + 1
        _vec(c4=sp.Integer(1)),                 # s1·s0      = s1s0
        _vec(c5=sp.Integer(1)),                 # s0s1·s0    = s0s1s0
        _vec(c2=sp.Integer(1), c4=H),           # s1s0·s0    = h s1s0 + s1
        _vec(c3=sp.Integer(1), c5=H),           # s0s1s0·s0  = h s0s1s0 + s0s1
    ],
    1: [
        _vec(c2=sp.Integer(1)),                 # 1·s1       = s1
        _vec(c3=sp.Integer(1)),                 # s0·s1      = s0s1
        _vec(c0=sp.Integer(1), c2=H),           # s1·s1      = h s1 + 1
        _vec(c1=sp.Integer(1), c3=H),           # s0s1·s1    = h s0s1 + s0
        _vec(c5=sp.Integer(1)),                 # s1s0·s1    = s1s0s1 = s0s1s0
        _vec(c4=sp.Integer(1), c5=H),           # s0s1s0·s1  = h s0s1s0 + s1s0
    ],
}


def route_a_nf(word: list[int]) -> sp.Expr:
    """Symbolic NF reduction + Ocneanu trace (no floats)."""
    nf = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for g in word:
        out = _z6()
        for i, c in enumerate(nf):
            if c == 0:
                continue
            for j, m in enumerate(RIGHT_MUL[g][i]):
                if m != 0:
                    out[j] = out[j] + c * m
        nf = [sp.expand(x) for x in out]
    return sp.expand(sum(c * t for c, t in zip(nf, TR_SYM)))


def route_b_axiomatic() -> dict[str, sp.Expr]:
    """Markov-axiom symbolic traces — no NF basis used."""
    # tr(s0)    = z                          [M2 peel in H_2]
    tr_s0 = Z
    # tr(s0 s1) = z tr(s0) = z^2             [M2 on s1, then s0]
    tr_s0s1 = Z * tr_s0
    # tr(s0 s1 s0) = tr(s0^2 s1)             [M1 cyclicity]
    #              = h tr(s0 s1) + tr(s1)    [Hecke quadratic]
    tr_s0s1s0 = H * tr_s0s1 + Z
    # (s0 s1)^3: expand with braid + Hecke (s1 s0 s1 = s0 s1 s0):
    #   (s0 s1)^3 = s0 (s1 s0 s1) s0 s1 = s0^2 s1 s0^2 s1
    #             = (h s0 + 1) s1 (h s0 + 1) s1
    #             = h^2 s0 s1 s0 s1 + h s0 s1^2 + h s1 s0 s1 + s1^2
    # with s1^2 = h s1 + 1 and
    #   s0 s1 s0 s1 = s0 (s1 s0 s1) = s0^2 s1 s0 = h s0 s1 s0 + s1 s0:
    tr_trefoil = sp.expand(
        H ** 2 * (H * tr_s0s1s0 + tr_s0s1)
        + H * (H * tr_s0s1 + tr_s0)
        + H * tr_s0s1s0
        + H * Z
        + 1
    )
    return {
        "s0": tr_s0,
        "s0*s1": tr_s0s1,
        "s0*s1*s0": tr_s0s1s0,
        "(s0*s1)^3": tr_trefoil,
    }


def main() -> int:
    set_compute_dps(50)
    q0_sp = sp.Float(Q_50_DIGIT_STR, 50)

    w = WitnessBuilder(
        "rigid-monoidal-gap-invariance",
        engine="python+sympy+mpmath",
    )
    w.set_description(
        "Convention-invariance of the categorical Markov trace "
        "(prop:rigid-monoidal-structural-gap-invariance): tr_M of "
        "canonical H_3 braid words evaluated through two structurally "
        "independent FULLY SYMBOLIC routes — NF-algebra "
        "right-multiplication table vs Markov-axiom derivation (M1 "
        "cyclicity + M2 peel + M3 + Hecke quadratic) — must agree "
        "symbolically (sympy simplify == 0) and at substrate q_0 to "
        "1e-40 (50 dps). No float64 anywhere. Includes the corrected "
        "tr_M(s0 s1 s0) = h z^2 + z with h = q - q^{-1} per AGENTS.md "
        "§7a (the deprecated lp-duality-check.py's z^3 claim used an "
        "invalid Markov-move chain and is superseded)."
    )
    w.set_content_block("prop:rigid-monoidal-structural-gap-invariance")

    tol = mp.mpf("1e-40")
    words = {
        "s0": [0],
        "s0*s1": [0, 1],
        "s0*s1*s0": [0, 1, 0],
        "(s0*s1)^3": [0, 1, 0, 1, 0, 1],
    }
    sym_b = route_b_axiomatic()

    print("=" * 72)
    print(" Markov-trace convention-invariance — NF algebra vs Markov axioms")
    print(" (both routes fully symbolic; h = q - 1/q per AGENTS.md §7a)")
    print("=" * 72)

    all_sym_ok = True
    all_num_ok = True
    results = {}
    for name, word in words.items():
        expr_a = route_a_nf(word)
        expr_b = sym_b[name]

        # Symbolic identity check (the strong form).
        sym_zero = sp.simplify(expr_a - expr_b) == 0

        # Numeric cross-check at q_0, 50 dps.
        tr_a = mp.mpf(str(sp.N(expr_a.subs(Q, q0_sp), 50)))
        tr_b = mp.mpf(str(sp.N(expr_b.subs(Q, q0_sp), 50)))
        diff = mp.fabs(tr_a - tr_b)
        num_ok = diff <= tol

        all_sym_ok = all_sym_ok and sym_zero
        all_num_ok = all_num_ok and num_ok
        results[name] = {
            "route_a_nf_symbolic": str(sp.simplify(expr_a)),
            "route_b_axiomatic_symbolic": str(sp.simplify(expr_b)),
            "symbolically_equal": bool(sym_zero),
            "at_q0_50dps": mp.nstr(tr_a, 30),
            "abs_diff_at_q0": mp.nstr(diff, 6),
        }
        print(f"  {name:12s} sym-equal={str(sym_zero):5s} "
              f"q0-value={mp.nstr(tr_a, 15):22s} diff={mp.nstr(diff, 4)}")

    # Historical-bug regression guard: the superseded z^3 value must
    # DISAGREE with the corrected trace.
    z0 = mp.mpf(str(sp.N(Z.subs(Q, q0_sp), 50)))
    z3_wrong = z0 ** 3
    correct = mp.mpf(results["s0*s1*s0"]["at_q0_50dps"])
    bug_distinct = mp.fabs(z3_wrong - correct) > mp.mpf("1e-6")
    print(f"\n  superseded z^3 value      = {mp.nstr(z3_wrong, 15)}")
    print(f"  corrected h*z^2 + z value = {mp.nstr(correct, 15)}")
    print(f"  distinct (bug detectable): {bug_distinct}")

    w.add_data("results", results)
    w.add_data("hecke_convention",
               "s^2 = (q - q^{-1}) s + 1 per AGENTS.md §7a; "
               "z = 1/(sqrt(q) + 1/sqrt(q))")
    w.add_data("tolerance_at_q0", "1e-40 (both routes symbolic, 50 dps)")
    w.add_data("superseded_producer",
               "lp-duality-check.py (z^3 claim via invalid Markov-move "
               "chain; see pyhecke fix be773569, 2026-05-19 catalog)")
    w.add_data("z3_superseded_value", mp.nstr(z3_wrong, 30))

    w.add_assertion(
        "markov_trace_convention_invariant_symbolic",
        computed=1 if all_sym_ok else 0,
        expected=1,
        tolerance=0,
        source=("All four H_3 test words give IDENTICAL tr_M through "
                "the NF-algebra route and the Markov-axiom route as "
                "symbolic expressions in q (sympy simplify of the "
                "difference == 0). The strong, anchor-independent form "
                "of the convention-invariance claim."),
    )
    w.add_assertion(
        "markov_trace_convention_invariant_at_q0",
        computed=1 if all_num_ok else 0,
        expected=1,
        tolerance=0,
        source=("Numeric cross-check at substrate q_0: both routes "
                "agree to 1e-40 at 50 dps for all four words."),
    )
    w.add_assertion(
        "superseded_z3_distinct_from_corrected",
        computed=1 if bug_distinct else 0,
        expected=1,
        tolerance=0,
        source=("The superseded z^3 value differs from the corrected "
                "h z^2 + z by > 1e-6, so the historical bug class is "
                "detectable by this probe (regression guard)."),
    )

    w.save()
    ok = all_sym_ok and all_num_ok and bug_distinct
    print(f"\n  {'ALL AGREE' if ok else 'MISMATCH FOUND'}; witness saved.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
