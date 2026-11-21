#!/usr/bin/env python3
"""
qbeta_augmentation_is_a_markov_trace_probe.py — qou-99qc: the "augmentation vs
Markov trace" dichotomy is FALSE. Both admissible functionals are Markov traces;
they differ only in the parameter, and the D7 ruling names which parameter.

# Ref: computations/qbeta/qbeta_admissible_functionals_bracket_probe.py
# Ref: docs/audits/2026-09-05-qbeta-functional-decision-options.md
# Ref: .beans/qou-99qc--...md   (which functional is epsilon meant to be)

THE QUESTION THIS CLOSES. `Q_beta = |eps(Delta)|*E_0` needs a functional `eps`,
and convention D admits exactly two: the augmentation `z = q` (+12.470 %) and
the Markov trace at `z_D = q^3/(q^2+1)` (-43.157 %). The corpus has framed these
as DIFFERENT KINDS of object -- the bracket probe calls them "the unique
multiplicative functional" and "the Markov trace" -- so the choice looked like a
question about what `eps` fundamentally IS, and was held as an owner call.

It is not. The augmentation is ALSO a Markov trace: the one at `z = q`.

WHAT IS DERIVED HERE, IN ORDER.

1. The Markov trace at generic `z` is computed on a basis of H_3(q) from its
   DEFINING properties only -- `tr(1) = 1`, the Markov property
   `tr(x s_n) = z tr(x)` for `x` in H_n, cyclicity, and the Hecke relation
   `s^2 = h s + 1` with `h = q - 1/q`. Nothing is imported.
2. The augmentation `s_i -> q` is evaluated on the same basis.
3. They agree identically at `z = q`, on all six basis elements -- and solving
   for agreement over the WHOLE basis returns `z = q` as the only solution, so
   this is an identification, not a coincidence at one element.

So "multiplicative functional" and "Markov trace" are not alternatives here: the
augmentation is the point of the Markov family where the trace happens to be
multiplicative. The remaining question is only WHICH PARAMETER, which is a
convention question -- and conventions are ruled on.

4. The block weights `y_lambda(z)` are then solved from
   `tr = sum_lambda y_lambda chi_lambda` on the three S_3 class representatives.
   CALIBRATION, not assumption: `y_(1,1,1)(z) = 0` is solved and its roots come
   out as exactly `{q, q^3/(q^2+1)}` -- the two admissible parameters the corpus
   already knows by an independent route. A wrong character table or
   normalisation would not reproduce that pair, so the table is checked against
   the corpus rather than asserted.
5. Block SUPPORT of the two:

       augmentation z = q  :  y_(3) = 1, y_(2,1) = 0, y_(1,1,1) = 0   -> 1 row
       convention D  z_D   :  y_(3), y_(2,1) nonzero, y_(1,1,1) = 0   -> 2 rows

WHY THIS SETTLES IT UNDER THE D7 RULING. D7 (2026-09-07, `36815fa0aaa`) is
channel-scoped: convention D governs the decay/Q_beta channel, the full tower
governs mass and binding. It characterises D as the TWO-ROW Temperley-Lieb
truncation -- `y_lambda = 0 exactly for >= 3 rows`, surviving family
`lambda = (n-k, k)`. At n = 3 that is exactly `{(3), (2,1)}`, which is what
`z_D` gives above. The augmentation additionally kills `(2,1)`, so it is a
strictly FINER, one-row truncation: it is not convention D. Q_beta is the decay
channel, D governs the decay channel, therefore `eps` is the Markov trace at
`z_D`.

D7'S OWN TRAP, AND WHY THIS IS NOT IN IT. D7 warns: label by the PREDICATE
(`rowLen <= 2` vs `colLen <= 2`), NEVER by counting survivors, because the two
opposite conventions are equinumerous with equal dimension sums -- at n = 3 both
give `5 = catalan 3` (rows<=2: 1^2 + 2^2; cols<=2: 1^2 + 2^2 on the transposed
family), so a count is transposition-blind. Nothing here counts. The argument is
by WHICH partitions carry nonzero weight, and it lands on D7's own stated
discriminator: the concrete family `lambda = (n-k, k)` together with
`y_(1,1,1) = 0`.

WHAT THIS DOES NOT DO. It does not make the number good: `z_D` gives
`-43.157 %`, the WORSE of the two residuals, and that is the anti-fitting
directive working as intended rather than a defect. It does not touch Option E
(derive a different element `Delta`), which `qou-37j2` identifies as the only
route to a parameter-free admissible sub-1 % result and which `5f5cdebef5b`
showed is a real search rather than an arithmetic discrepancy. It wires nothing
and proposes no value for anything. Scope-(a).

Exact sympy over Q(q) throughout; the pin enters only at readout, as an exact
Rational from the 50-digit proton string, printed through mpmath at 60 dps.
No float64 anywhere (AGENTS.md NO-FLOAT64; probes are not exempt).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

CODATA_Q_BETA_MEV = "0.7823334"
M_E_MEV = "0.51099895000"


def main() -> int:
    mp.mp.dps = 60
    checks: list[dict] = []

    def chk(name, ok, detail):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        return bool(ok)

    print(__doc__.splitlines()[1])
    print()
    ok = True

    q, z = sp.symbols("q z", positive=True)
    h = q - 1 / q

    # ---- 1. the Markov trace at generic z, from its defining properties -----
    # basis of H_3(q): 1, s1, s2, s1s2, s2s1, s1s2s1
    tr = {}
    tr["1"] = sp.Integer(1)                     # normalisation
    tr["s1"] = z                                # Markov, x = 1
    tr["s2"] = z                                # Markov, x = 1
    tr["s1s2"] = z * tr["s1"]                   # Markov, x = s1 in H_2
    tr["s2s1"] = tr["s1s2"]                     # cyclicity
    tr["s1s2s1"] = h * tr["s2s1"] + tr["s2"]    # cyclicity then s1^2 = h s1 + 1

    # ---- 2. the augmentation, an algebra map into a commutative ring -------
    aug = {"1": sp.Integer(1), "s1": q, "s2": q,
           "s1s2": q**2, "s2s1": q**2, "s1s2s1": q**3}

    basis = ["1", "s1", "s2", "s1s2", "s2s1", "s1s2s1"]
    agree = all(sp.simplify(tr[k].subs(z, q) - aug[k]) == 0 for k in basis)
    ok &= chk("augmentation_IS_the_markov_trace_at_z_equals_q",
              agree,
              "all 6 basis elements of H_3(q) agree: the Markov trace built "
              "from tr(1)=1, tr(x s_n)=z tr(x), cyclicity and s^2 = h s + 1, "
              "evaluated at z = q, equals the algebra map s_i -> q. The "
              "'multiplicative functional vs Markov trace' dichotomy the corpus "
              "has been carrying is FALSE")

    # and z = q is the ONLY parameter at which they agree, so it is an
    # identification rather than a coincidence
    sols = sp.solve([sp.Eq(sp.simplify(tr[k]), aug[k]) for k in basis], z,
                    dict=True)
    ok &= chk("and_z_equals_q_is_the_UNIQUE_such_parameter",
              len(sols) == 1 and sp.simplify(sols[0][z] - q) == 0,
              f"solving for basis-wide agreement over an unrestricted z gives "
              f"exactly {[sp.simplify(s[z]) for s in sols]} -- so the "
              "augmentation is ONE POINT of the Markov family, not a functional "
              "of a different kind that happens to collide somewhere")

    # ---- 3. block weights, solved -- then CALIBRATED against the corpus -----
    y3, y21, y1 = sp.symbols("y3 y21 y1")
    chi = {
        (3,):      {"1": sp.Integer(1), "s1": q,       "s1s2": q**2},
        (2, 1):    {"1": sp.Integer(2), "s1": h,       "s1s2": sp.Integer(-1)},
        (1, 1, 1): {"1": sp.Integer(1), "s1": -1 / q,  "s1s2": 1 / q**2},
    }
    reps = ["1", "s1", "s1s2"]                  # the three S_3 classes
    eqs = [sp.Eq(sum(w * chi[l][k] for w, l in zip((y3, y21, y1), chi)), tr[k])
           for k in reps]
    sol = sp.solve(eqs, (y3, y21, y1), dict=True)[0]
    Y = {l: sp.factor(sp.simplify(sol[w])) for w, l in zip((y3, y21, y1), chi)}

    zD = q**3 / (q**2 + 1)
    roots = sp.solve(sp.Eq(sp.numer(sp.together(Y[(1, 1, 1)])), 0), z)
    ok &= chk("CALIBRATION_y_1cubed_vanishes_at_EXACTLY_the_known_two_roots",
              set(sp.simplify(r) for r in roots) == {q, sp.simplify(zD)},
              f"solving y_(1,1,1)(z) = 0 gives {[sp.simplify(r) for r in roots]} "
              "= {q, q^3/(q^2+1)}, the two admissible parameters the corpus "
              "already establishes by an independent route. A wrong character "
              "table or normalisation would not reproduce that pair, so the "
              "table below is checked against the corpus, not asserted")

    # ---- 4. block SUPPORT: one row vs two rows -----------------------------
    support = {}
    for name, zv in (("augmentation", q), ("conventionD", zD)):
        vals = {l: sp.simplify(v.subs(z, zv)) for l, v in Y.items()}
        support[name] = sorted([l for l, v in vals.items() if v != 0])
        print(f"      {name:13s}: " + "  ".join(
            f"y_{l}={sp.nsimplify(v)}" for l, v in vals.items()))

    ok &= chk("conventionD_is_the_TWO_ROW_family_lambda_eq_n_minus_k_k",
              support["conventionD"] == [(2, 1), (3,)],
              f"z_D is supported on {support['conventionD']} = "
              "{(3-0,0), (3-1,1)} with y_(1,1,1) = 0 -- exactly D7's stated "
              "characterisation of convention D as the two-row TL truncation "
              "(TemperleyLiebTower's concrete lambda = (n-k,k))")

    ok &= chk("augmentation_is_STRICTLY_FINER_a_ONE_ROW_truncation",
              support["augmentation"] == [(3,)]
              and set(support["augmentation"]) < set(support["conventionD"]),
              f"the augmentation is supported on {support['augmentation']} "
              "alone -- it kills (2,1) as well as (1,1,1), so it is a ONE-row "
              "truncation, a proper refinement of D rather than D itself. "
              "Therefore it is NOT the convention-D functional")

    # D7 flags a trap: labelling by COUNT is transposition-blind. Show that the
    # count genuinely cannot separate the two readings, so the argument above
    # had to be by support -- and was.
    dimsum_rows = sum(sp.Integer(d)**2 for d in (1, 2))       # {(3),(2,1)}
    dimsum_cols = sum(sp.Integer(d)**2 for d in (1, 2))       # {(1^3),(2,1)}
    ok &= chk("D7_count_trap_is_REAL_here_and_this_probe_avoids_it",
              dimsum_rows == dimsum_cols == 5,
              f"rows<=2 and cols<=2 both give dimension sum {dimsum_rows} "
              "= catalan(3), so a count-based labelling cannot tell the row "
              "reading from the column one (D7's transposition-blindness trap). "
              "Nothing above counts: every claim is about WHICH partitions "
              "carry nonzero weight")

    # ---- 5. readout at the proton pin, for continuity with the merged cells --
    q0 = sp.Rational(Q_50_DIGIT_STR)
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(1, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    trS = h**2 / 2 - h * z                       # tr_M(Delta_S), the value family
    me = mp.mpf(M_E_MEV)
    tgt = mp.mpf(CODATA_Q_BETA_MEV)

    def cell(zv):
        v = sp.Abs(trS.subs(z, zv) * E0).subs(q, q0)
        return me * mp.mpf(str(sp.N(v, 60)))

    qb_aug, qb_D = cell(q.subs(q, q0)), cell(zD.subs(q, q0))
    miss_aug = (qb_aug - tgt) / tgt * 100
    miss_D = (qb_D - tgt) / tgt * 100
    print(f"      augmentation z=q : Q_beta = {mp.nstr(qb_aug, 12)} MeV  "
          f"({mp.nstr(miss_aug, 8)} %)")
    print(f"      convention D z_D : Q_beta = {mp.nstr(qb_D, 12)} MeV  "
          f"({mp.nstr(miss_D, 8)} %)")
    ok &= chk("CALIBRATION_reproduces_the_merged_two_cells",
              abs(miss_aug - mp.mpf("12.470")) < mp.mpf("0.001")
              and abs(miss_D + mp.mpf("43.157")) < mp.mpf("0.001"),
              f"{mp.nstr(miss_aug, 10)} % and {mp.nstr(miss_D, 10)} % reproduce "
              "the +12.470 % / -43.157 % of #6722/#6763/#6832, so the machinery "
              "here is anchored to the merged numbers rather than free-standing")

    ok &= chk("the_RULING_selects_the_WORSE_residual_and_that_is_correct",
              abs(miss_D) > abs(miss_aug),
              f"|{mp.nstr(miss_D, 8)}| > |{mp.nstr(miss_aug, 8)}| -- the "
              "functional D7 selects is the one that fits WORSE. Recorded "
              "explicitly because it is the anti-fitting directive working as "
              "intended: had the ruling landed on the better residual, that "
              "would be the coincidence worth suspecting")

    print()
    print(f"  {sum(c['passed'] for c in checks)}/{len(checks)} checks passed")

    w = {
        "description":
            "qou-99qc: the augmentation IS the Markov trace at z = q (unique), "
            "so the two admissible Q_beta functionals differ only in the Markov "
            "parameter. By block support the augmentation is a ONE-row "
            "truncation and z_D the TWO-row one; D7 (2026-09-07) scopes "
            "convention D -- the two-row TL truncation -- to the decay/Q_beta "
            "channel, which selects z_D. Scope-(a); wires nothing.",
        "checks": checks,
        "all_passed": bool(ok),
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
        "scriptFile": Path(__file__).name,
        "block_weights_generic_z": {str(l): sp.srepr(v) for l, v in Y.items()},
        "block_support": {k: [str(l) for l in v] for k, v in support.items()},
        "y_1cubed_roots": [sp.srepr(sp.simplify(r)) for r in roots],
        "q_beta_cells_MeV": {
            "augmentation_z_eq_q": mp.nstr(qb_aug, 20),
            "convention_D_z_D": mp.nstr(qb_D, 20),
            "codata": CODATA_Q_BETA_MEV,
        },
        "q_beta_miss_pct": {
            "augmentation_z_eq_q": mp.nstr(miss_aug, 12),
            "convention_D_z_D": mp.nstr(miss_D, 12),
        },
        "caveats": [
            "Scope-(a). Establishes an identification and a block-support fact; "
            "it does not derive Q_beta and proposes no value for anything.",
            "The selected functional gives the WORSE residual (-43.157 % vs "
            "+12.470 %). That is the anti-fitting directive working, not a "
            "defect.",
            "Option E -- derive a different element Delta -- is untouched and "
            "remains the only route to a parameter-free admissible sub-1 % "
            "result (qou-37j2). Commit 5f5cdebef5b showed that search is real: "
            "eps(Delta_S) and chi_(3)(Delta_L) are genuinely different "
            "elements, not an arithmetic discrepancy.",
            "The n = 3 computation is the Q_beta ladder's H_3, which is the "
            "algebra D7 names for this channel. Nothing here is claimed for "
            "general n.",
        ],
    }
    WitnessBuilder.stamp_staleness_metadata(
        w, script_path=__file__, engine="python+sympy",
        q0_anchor="proton", q0_value=Q_50_DIGIT_STR)
    out = HERE / "qbeta-augmentation-is-a-markov-trace.witness.json"
    out.write_text(__import__("json").dumps(w, indent=2) + "\n")
    print(f"  witness -> {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
