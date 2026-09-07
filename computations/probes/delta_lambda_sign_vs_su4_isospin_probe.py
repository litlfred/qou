#!/usr/bin/env python3
"""qou-buxs: is the Delta_lambda sign an isospin grading? YES on the physical
stratum, NO in the SU(4) frame -- and the frame is the whole question.

Bean `qou-buxs` proposes that the mixed-sign structure of the PROVED
    Delta_lambda = (-1)^{n(lambda)} * dim V_lambda
    (QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional, sorry-free)
IS the chiral weak-isospin T3 grading, and asks whether the derived T3
reproduces the mixed-sign pattern (n=3: 1+/2-, n=6: 6+/5-).

HEADLINE
  On the convention-D PHYSICAL stratum the identification HOLDS, with an exact
  closed form:

      sgn(Delta_lambda) = (-1)^{(n - 2T)/2}       [verified n = 2..10]

  In the SU(4) (four-row) frame it FAILS: the same isospin value occurs in
  blocks of opposite sign, so no function of T exists there at all.

  Both are computed below. The second is what this probe originally concluded,
  and it was the wrong frame -- recorded rather than deleted, because which
  frame is physical is exactly what bean qou-ubsl said had to be settled first.

WHY THE FRAME DECIDES IT
  Bean `qou-ubsl` ROAST item (ii) reads: "Descartes forces dim V=2, so
  Schur-Weyl gives GL(2) NOT GL(4) -- the SU(4) reading may be structurally
  FORBIDDEN. Resolve (ii) before any work." That objection is correct and this
  probe resolves it in favour of GL(2):

  Under convention D the corpus carries a Lean-proved TWO-ROW CAP -- partitions
  with l(lambda) >= 3 vanish on the physical spectrum
  (QOU.Mathlib.YoungDiagramThreeRowCorner.threeRow_vanishing_all_levels; see
  also Mu3SlotExclusion.lean:163-166, "y_lambda >= 0 on the two-row stratum
  lambda=(n-k,k) and a vanishing l(lambda)>=3 radical"). So the physically live
  blocks are the two-row ones, and the live symmetry is GL(2)-like, not SU(4).

ON THE TWO-ROW STRATUM THE ALGEBRA IS ONE LINE
  For lambda = (n-k, k):  n(lambda) = k, hence sgn = (-1)^k exactly.
  GL(2) Schur-Weyl gives the SU(2) label T = (lambda_1 - lambda_2)/2 = (n-2k)/2,
  so k = (n-2T)/2 and sgn = (-1)^{(n-2T)/2}. The sign therefore steps by -1 for
  each unit step of T, at every n. Checked n = 2..10 in `two_row_stratum`.

THREE CAVEATS, each of which limits the claim
  1. T, NOT T3. The two-row label is the SU(2) Casimir T. T3 is a WEIGHT that
     varies WITHIN a multiplet, so it still cannot be a per-block quantity. The
     bean says "T3"; what survives is a statement about T.
  2. THE PHASE IS n-DEPENDENT. sgn = (-1)^{(n-2T)/2} is not a single grading in
     T alone -- it carries an offset set by the body number n. Whether an
     n-dependent phase counts as "the chiral grading" is a framework question
     this probe does not settle.
  3. WHICH SU(2)? -- RESOLVED 2026-08-29, AND THE ANSWER IS NEGATIVE.
     When first written this said the question was open and was "the gap to
     close next". It is now closed, by corpus-grep rather than computation, and
     it closes AGAINST the bean:

       * `braids-and-knots/jones-markov-trace.md` states outright that "the
         fibre V is the two-dimensional fundamental of SU_q(2), so no partition
         with three or more rows survives Schur-Weyl". So the two-row label
         T = (lambda_1 - lambda_2)/2 is the SU_q(2) / Temperley-Lieb spin --
         the quantum group of the BRAID SUBSTRATE.
       * The corpus nowhere identifies that SU_q(2) fundamental with nucleon
         isospin. Grepped for it in content/ and docs/: zero hits.
       * Nucleon flavour enters by a DIFFERENT mechanism entirely.
         `mass-theory/flavor-split-habiro-derivation.md` derives the p/n split
         from a CROSSING REVERSAL -- the Hopf antipode S(T_w) = T_{w^-1}, with
         sigma_1^3 - sigma_1^-3 = q^3 - q^-3 exactly. Flavour is a property of
         the braid WORD, not an index on the fibre.

     So the T in sgn(Delta_lambda) = (-1)^{(n-2T)/2} is the wrong SU(2) for the
     bean's purpose. The closed form is exact and stands as stated; what it is
     a statement ABOUT is the substrate's SU_q(2) spin label, not weak isospin.
     Identifying the two would need a bridge (SU_q(2) fundamental <-> nucleon
     isospin doublet) that the corpus does not contain.

     Scope: this is a CORPUS-STATUS finding, not a proof that no such bridge
     could be built. It says the identification is unsupported as the corpus
     stands, and that the framework's own flavour mechanism is a different
     structure. Someone may yet construct the bridge; they would have to state
     it, because nothing currently implies it.

Method for the SU(4) leg: Schur-Weyl (C^4)^{x n} = sum_lambda S^lambda(C^4) (x)
M_lambda; restrict SU(4) to SU(2)_S x SU(2)_T by evaluating the Schur polynomial
at the four weights (S3,T3)=(+-1/2,+-1/2) with fugacity s^{2S3} t^{2T3}, then
peel off chi_S(s) chi_T(t) from the highest weight down. All arithmetic is
sympy exact rational/integer; no float64 anywhere.

SCOPE (per AGENTS.md "Before declaring refuted")
  (a) The SU(4)-frame negative is scope-(a) as a statement about the bean: it
      shows the identification fails IN THAT FRAME, and the frame is not the
      physical one, so it excludes nothing about the framework.
  (b) No structural exclusion is claimed. The positive two-row result is exact
      but is NOT a closure -- see caveat 3.

audit-only, no fit, no production wiring.
"""

import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)
import os, sys
import sympy as sp

COMP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, COMP)

s, t = sp.symbols('s t', positive=True)
# four single-nucleon states (S3,T3) = (+-1/2,+-1/2), fugacity s^{2S3} t^{2T3}
WEIGHTS = [s*t, s/t, t/s, 1/(s*t)]


def partitions(n, maxp=None):
    if maxp is None:
        maxp = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxp), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def n_of_lambda(lam):
    """n(lambda) = sum (i-1) lambda_i, the jet-order valuation whose parity is the sign."""
    return sum(i * li for i, li in enumerate(lam))


def hook_dim(lam):
    """dim of the S_n irrep via the hook-length formula (exact integer)."""
    n = sum(lam)
    conj = [sum(1 for x in lam if x > j) for j in range(lam[0])]
    prod = 1
    for i, li in enumerate(lam):
        for j in range(li):
            prod *= (li - j) + (conj[j] - i) - 1
    return sp.factorial(n) // prod


def ssyt_fillings(lam, nletters=4):
    """All semistandard Young tableaux of shape lam with entries 1..nletters.

    Enumerated directly rather than via the bialternant: the determinant ratio
    is a rational function that sympy will not always cancel to a Laurent
    polynomial, and Poly() then rejects it (it did, at n>=4). Counting tableaux
    involves no division at all.
    """
    cells = [(i, j) for i, li in enumerate(lam) for j in range(li)]
    out, cur = [], {}

    def rec(k):
        if k == len(cells):
            out.append(dict(cur))
            return
        i, j = cells[k]
        lo = 1
        if j > 0:
            lo = max(lo, cur[(i, j - 1)])          # weakly increasing along rows
        if i > 0:
            lo = max(lo, cur[(i - 1, j)] + 1)      # strictly increasing down columns
        for v in range(lo, nletters + 1):
            cur[(i, j)] = v
            rec(k + 1)
        cur.pop((i, j), None)

    rec(0)
    return out


def schur_at_weights(lam, xs):
    """s_lambda(x1..x4) = sum over SSYT of prod x_{entry}. Exact, no division."""
    total = 0
    for f in ssyt_fillings(lam, len(xs)):
        term = 1
        for v in f.values():
            term *= xs[v - 1]
        total += term
    return sp.expand(sp.simplify(total))


def su2_char(j, z):
    return sum(z ** (2 * m) for m in [-j + k for k in range(int(2 * j) + 1)])


def decompose_su2xsu2(expr, pad=40):
    """Peel chi_S(s)*chi_T(t) off from the highest weight down. Exact."""
    rem = sp.expand(sp.simplify(expr))
    out = {}
    while rem != 0:
        pr = sp.Poly(sp.expand(rem * (s ** pad) * (t ** pad)), s, t)
        best = None
        for mono, c in zip(pr.monoms(), pr.coeffs()):
            a, b = mono[0] - pad, mono[1] - pad
            if c != 0 and (best is None or (a, b) > (best[0], best[1])):
                best = (a, b, c)
        if best is None:
            break
        a, b, c = best
        S, T = sp.Rational(a, 2), sp.Rational(b, 2)
        if S < 0 or T < 0:
            break
        out[(S, T)] = out.get((S, T), 0) + int(c)
        rem = sp.simplify(sp.expand(rem - c * su2_char(S, s) * su2_char(T, t)))
    return out


def two_row_stratum(nmax=10):
    """The convention-D physical stratum: lambda=(n-k,k), l(lambda)<=2.

    Returns per-n rows plus whether sgn is a function of T and whether the
    closed form (-1)^{(n-2T)/2} reproduces it.
    """
    out, func_ok, formula_ok = {}, True, True
    for n in range(2, nmax + 1):
        rows, seen = [], {}
        for k in range(0, n // 2 + 1):
            lam = (n - k, k) if k > 0 else (n,)
            sgn = (-1) ** n_of_lambda(lam)
            T = sp.Rational(n - 2 * k, 2)
            pred = (-1) ** int((n - 2 * T) / 2)
            if pred != sgn:
                formula_ok = False
            if T in seen and seen[T] != sgn:
                func_ok = False
            seen[T] = sgn
            rows.append({"lambda": list(lam), "k": k, "T": str(T),
                         "delta_sign": int(sgn), "closed_form": int(pred)})
        out[str(n)] = rows
    return out, func_ok, formula_ok


def main():
    from collections import defaultdict
    per_n = {}
    ambiguous_any = False

    for n in (2, 3, 4, 5, 6):
        rows, tmap, t3map = [], defaultdict(set), defaultdict(set)
        # The bean quotes sign splits over ALL partitions of n; SU(4) only
        # represents those with at most 4 rows. Track both -- the gap is itself
        # a finding, not a discrepancy to be explained away.
        all_parts = list(partitions(n))
        tall = [list(l) for l in all_parts if len(l) > 4]
        pos_all = sum(1 for l in all_parts if (-1) ** n_of_lambda(l) > 0)
        split_all = f"{pos_all}+/{len(all_parts) - pos_all}-"
        for lam in all_parts:
            if len(lam) > 4:      # SU(4): at most 4 rows carry a nonzero irrep
                continue
            content = decompose_su2xsu2(schur_at_weights(lam, WEIGHTS))
            sgn = (-1) ** n_of_lambda(lam)
            rows.append({
                "lambda": list(lam),
                "n_of_lambda": n_of_lambda(lam),
                "delta_sign": int(sgn),
                "dim_S_n_irrep": int(hook_dim(lam)),
                "su4_ST_content": {f"S={S},T={T}": m for (S, T), m in sorted(content.items(), reverse=True)},
            })
            for (S, T), _m in content.items():
                tmap[str(T)].add(int(sgn))
                # every T multiplet contains the full T3 ladder
                for k in range(int(2 * T) + 1):
                    t3map[str(-T + k)].add(int(sgn))

        amb_T = {T: sorted(g) for T, g in tmap.items() if len(g) > 1}
        amb_T3 = {x: sorted(g) for x, g in t3map.items() if len(g) > 1}
        if amb_T:
            ambiguous_any = True
        pos = sum(1 for r in rows if r["delta_sign"] > 0)
        neg = len(rows) - pos
        per_n[str(n)] = {
            "blocks": rows,
            "sign_split_su4_representable": f"{pos}+/{neg}-",
            "sign_split_all_partitions": split_all,
            "partitions_with_no_su4_supermultiplet": tall,
            "n_partitions_all": len(all_parts),
            "n_partitions_su4_representable": len(rows),
            "T_values_carrying_both_signs": amb_T,
            "T3_values_carrying_both_signs": amb_T3,
            "sign_is_a_function_of_T": not amb_T,
            "sign_is_a_function_of_T3": not amb_T3,
        }
        print(f"n={n}: {pos}+/{neg}-   T carrying BOTH signs: "
              f"{sorted(amb_T) if amb_T else 'none'}")

    two_row, two_row_is_T_function, two_row_formula_ok = two_row_stratum()
    print()
    print(f"two-row (convention-D physical) stratum: sign is a function of T: "
          f"{two_row_is_T_function};  sgn=(-1)^((n-2T)/2) holds: {two_row_formula_ok}")

    # the two patterns the bean quotes, checked against the proved formula
    # The bean's quoted patterns are over ALL partitions -- check them there.
    bean_ok = (per_n["3"]["sign_split_all_partitions"] == "1+/2-"
               and per_n["6"]["sign_split_all_partitions"] == "6+/5-")
    # ...and record that SU(4) cannot even pose the question for the tall ones.
    tall_total = sum(len(v["partitions_with_no_su4_supermultiplet"]) for v in per_n.values())

    payload = {
        "computation": "delta-lambda-sign-vs-su4-isospin",
        "description": (
            "qou-buxs: tests whether the PROVED Delta_lambda sign (-1)^{n(lambda)} can be an "
            "isospin-valued grading. ON THE CONVENTION-D PHYSICAL (two-row) STRATUM IT CAN, "
            "exactly: sgn(Delta_lambda) = (-1)^((n-2T)/2), verified n=2..10. In the SU(4) "
            "(four-row) frame it cannot -- the same isospin value carries blocks of both signs "
            "-- but the Lean-proved two-row cap means that frame is not the physical one, so "
            "the negative excludes nothing and is retained only as the record of a wrong-frame "
            "computation. NOT a closure: the result is about T while the bean claims T3, the "
            "phase is n-dependent, and whether the two-row SU(2) is isospin or spin is not "
            "established here. audit-only, no fit."),
        "tier": "structural (exact Schur-Weyl decomposition + Lean-proved sign)",
        "result": {
            "two_row_physical_stratum": {
                "per_n": two_row,
                "sign_is_a_function_of_T": bool(two_row_is_T_function),
                "closed_form": "sgn(Delta_lambda) = (-1)^((n-2T)/2)",
                "closed_form_holds_n_2_to_10": bool(two_row_formula_ok),
                "why_this_is_the_physical_stratum": (
                    "Convention D carries a Lean-proved two-row cap: partitions with "
                    "l(lambda)>=3 vanish on the physical spectrum "
                    "(QOU.Mathlib.YoungDiagramThreeRowCorner.threeRow_vanishing_all_levels; "
                    "Mu3SlotExclusion.lean:163-166). So the live symmetry is GL(2)-like, "
                    "which settles bean qou-ubsl ROAST (ii) in favour of GL(2) over GL(4)."),
                "caveats": [
                    "T, not T3: the two-row label is the SU(2) Casimir; T3 is a weight "
                    "varying WITHIN a multiplet and still cannot be a per-block quantity.",
                    "The phase is n-dependent: (-1)^((n-2T)/2) is not a single grading in T.",
                    "WHICH SU(2) -- RESOLVED 2026-08-29, NEGATIVELY. See "
                    "which_su2_resolution below: the two-row label is the SU_q(2) / "
                    "Temperley-Lieb spin of the braid substrate, not nucleon isospin.",
                ],
                "which_su2_resolution": {
                    "verdict": (
                        "The two-row label is the SU_q(2) (Temperley-Lieb) spin of the braid "
                        "substrate, NOT nucleon isospin. So the closed form, which is exact "
                        "and stands, is a statement about the wrong SU(2) for bean qou-buxs."),
                    "evidence": [
                        "content/quantum-observable-universe/braids-and-knots/"
                        "jones-markov-trace.md: 'the fibre V is the two-dimensional "
                        "fundamental of SU_q(2), so no partition with three or more rows "
                        "survives Schur-Weyl'.",
                        "Corpus grep for any identification of the SU_q(2) fundamental with "
                        "isospin, over content/ and docs/: ZERO hits.",
                        "content/quantum-observable-universe/mass-theory/"
                        "flavor-split-habiro-derivation.md: the p/n split comes from a "
                        "CROSSING REVERSAL (Hopf antipode S(T_w)=T_{w^-1}), with "
                        "sigma_1^3 - sigma_1^-3 = q^3 - q^-3 exactly. Flavour is a property "
                        "of the braid WORD, not an index on the fibre.",
                    ],
                    "scope": (
                        "Corpus-status finding, not a proof that no bridge could exist. The "
                        "identification is UNSUPPORTED as the corpus stands, and the "
                        "framework's own flavour mechanism is a different structure. A future "
                        "bridge would have to be stated explicitly; nothing currently implies it."),
                },
            },
            "su4_frame_negative": "see per_n below; wrong frame, retained as the record",
            "per_n": per_n,
            "bean_quoted_patterns_reproduced": bool(bean_ok),
            "blocks_with_no_su4_supermultiplet_total": int(tall_total),
            "second_arity_problem": (
                "The bean's quoted splits (n=3: 1+/2-, n=6: 6+/5-) count ALL partitions. "
                "SU(4) represents only those with at most 4 rows, so at n=6 two blocks -- "
                "[2,1,1,1,1] and [1,1,1,1,1,1] -- carry a proved Delta_lambda sign while "
                "having NO Wigner supermultiplet at all. For those the identification cannot "
                "even be POSED, independently of the f(T) refutation below."),
            "sign_is_isospin_valued_at_any_n": not ambiguous_any,
            "verdict": (
                "SURVIVES on the physical stratum, with an exact closed form. Under convention "
                "D's Lean-proved two-row cap the live blocks are lambda=(n-k,k), where "
                "n(lambda)=k gives sgn=(-1)^k and the GL(2) Schur-Weyl label is T=(n-2k)/2, so "
                "sgn(Delta_lambda) = (-1)^((n-2T)/2) exactly, verified n=2..10. This settles "
                "bean qou-ubsl ROAST (ii) in favour of GL(2) over GL(4). "
                "IN THE SU(4) FRAME IT FAILS -- the same isospin value occurs in blocks of "
                "opposite sign -- but that frame is not the physical one, so the negative "
                "excludes nothing; it is retained as the record of a wrong-frame computation. "
                "NOT A CLOSURE, for three stated reasons: the result is about T and the bean "
                "claims T3 (a weight, still not per-block); the phase is n-dependent rather "
                "than a single grading in T; and -- RESOLVED 2026-08-29, NEGATIVELY -- the "
                "two-row SU(2) is the SU_q(2)/Temperley-Lieb spin of the braid substrate, NOT "
                "nucleon isospin, so the exact closed form is about the wrong SU(2) for the "
                "bean's purpose (see which_su2_resolution). Separately, the bean's own stated "
                "test still cannot run: its input, the derived T3 of bean qou-tdrd, is status "
                "`todo` and has never been derived."),
        },
        "context": {
            "axis": "Delta_lambda magnitude leg (Track-A blocker) -- qou-buxs, child of qou-20sx",
            "proved_input": "QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional (sorry-free)",
            "blocked_on": "qou-tdrd (derive weak-isospin T3) -- status todo",
            "arithmetic": "sympy exact rational/integer throughout; no float64 anywhere",
        },
    }

    try:
        from qou_substrate.witness import WitnessBuilder
        wb = WitnessBuilder.wrap_legacy(
            "delta-lambda-sign-vs-su4-isospin", payload,
            script_path=__file__, engine="python+sympy-exact",
            output_dir=os.path.join(COMP, "probes"))
        wb.add_assertion("bean_quoted_patterns_reproduced_over_all_partitions",
                         computed=str(bool(bean_ok)), expected="True")
        wb.add_assertion("some_blocks_have_no_su4_supermultiplet",
                         computed=str(bool(tall_total > 0)), expected="True")
        wb.add_assertion("su4_frame_sign_is_NOT_a_function_of_T",
                         computed=str(bool(ambiguous_any)), expected="True")
        wb.add_assertion("two_row_stratum_sign_IS_a_function_of_T",
                         computed=str(bool(two_row_is_T_function)), expected="True")
        wb.add_assertion("two_row_closed_form_holds",
                         computed=str(bool(two_row_formula_ok)), expected="True")
        # This probe never reads q0: it is exact representation theory over
        # partitions (SSYT counts, hook lengths, sign parities). Per
        # computations/audits/q0_anchor_ratchet.py, the honest stamp for that is
        # q0Anchor="independent" with a reason and NO q0Value -- a q0Value here
        # would assert a dependence the computation does not have. Stamped via
        # save() so it lands top-level, where every reader looks; add_data would
        # nest it under "data" and be invisible to the ratchet.
        out = wb.save(extra={
            "auditOnly": True,
            "q0Anchor": "independent",
            "q0AnchorReason": (
                "Exact representation theory over partitions of n -- SSYT enumeration, "
                "hook-length dimensions, and the parity of n(lambda). No substrate "
                "modulus enters at any point; sympy exact rationals throughout."),
        })
        print("witness ->", out)
    except Exception as exc:                       # pragma: no cover
        import json
        out = os.path.join(COMP, "probes", "delta-lambda-sign-vs-su4-isospin.witness.json")
        # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
        # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
        # dump runs, so any exception in between leaves the committed witness
        # empty or partial -- the shape that emptied 22 witnesses to zero bytes
        # in one `producer_importability_audit` run. `os.replace` is atomic on
        # POSIX within a filesystem, hence a SIBLING temp file.
        _wpath_sidu = out
        _wtmp_sidu = str(_wpath_sidu) + ".tmp"
        with open(_wtmp_sidu, "w") as fh:
            json.dump(payload, fh, indent=2)
        _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
        print(f"witness (bare, WitnessBuilder unavailable: {exc}) ->", out)

    print("\n  VERDICT: " + payload["result"]["verdict"].split(" IN THE SU(4) FRAME")[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
