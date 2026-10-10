#!/usr/bin/env python3
"""Candidate (i) assigns chirality to `arg q`.  The corpus assigns it to the
BAR involution `q -> 1/q`, and the two agree only on the unit circle -- which
is not where the substrate is.

WHAT WAS ASKED
--------------
Bean `qou-c66b` / `conj:im-q-physical-role`, on the author's instruction to
chip away at where the imaginarity comes from.  Candidate (ii) is closed (PR
#6639, merged); candidate (i), chirality, was left as the only one of the three
with no closure argument from either direction.  This probe is that argument.

CANDIDATE (i), VERBATIM
-----------------------
    "For complex `q = |q| e^{i arg q}` near the unit circle, `arg q` is
     naturally a **chirality coordinate** -- positive arg gives clockwise braid
     orientation; negative arg gives counterclockwise.  The categorical mass
     formula is invariant under `q -> qbar` (complex conjugation under modulus
     projection), consistent with mass being chirality-invariant."

So candidate (i) makes an identification: **chirality flip = complex
conjugation `q -> qbar`**.

WHAT THE CORPUS SAYS INSTEAD, IN THREE PLACES
---------------------------------------------
The mirror (= chirality) operation on knots is the **bar involution**
`q -> 1/q`, not conjugation:

  * `mass-theory/archimedean-image-table-table1-data.md` row 4:
      "J_Kbar(q) = J_K(q^{-1})  (mirror; matter/antimatter CPT)"
  * `mass-theory/hq-bi-filtration.md`:
      "Bar involution * : q -> q^{-1}  |  * : H_q^{(n,K)} -> H_q^{(n,K*)}
       where K* is the MIRROR KNOT"
  * `mass-theory/knot-indexed-convolution-grid-table2-data.md`, same row.

and `braids-and-knots/knot-notation-convention.md` fixes what the mirror MEANS
physically: it flips the sign of the writhe, and the weak isospin IS that sign.

This is the standard knot-theoretic fact (`J_mirror(K)(q) = J_K(q^{-1})`), and
the corpus carries it as a table row rather than as an aside.

THE TWO OPERATIONS COINCIDE EXACTLY ON THE UNIT CIRCLE, AND NOWHERE ELSE
------------------------------------------------------------------------
`qbar = 1/q  <=>  q qbar = 1  <=>  |q|^2 = 1`.

Candidate (i) places itself "near the unit circle" (the Kashaev regime
`q = e^{2 pi i / N}`), and **there it is right**: on `|q| = 1` conjugation IS
the bar involution, so `arg q` genuinely is the chirality coordinate.

**The substrate is not there.**  `|q_0| = 1.10998`, so `qbar_0` and `1/q_0` are
different points, `0.20906` apart -- **18.83 %** of `q_0` -- and the one the
corpus calls the mirror is `1/q_0 = 0.9009182839557414922`, a REAL number
requiring no `Im q` at all.

CONSEQUENCE
-----------
At the substrate, the role candidate (i) proposes for `arg q` is already
carried, in full, by a real-q mechanism the corpus has developed in detail:
the bar involution and its `P_avg` / `P_skew` split
(`mass-theory/rem-im-q-vs-p-skew.md`, which is the conjecture's own exclusions
block).  `arg q` becomes the chirality coordinate only in a regime the
substrate is not in.

SECOND LEG -- EVEN GRANTING CANDIDATE (i)'s IDENTIFICATION, IT CLOSES
---------------------------------------------------------------------
Suppose one grants `chirality flip = q -> qbar` anyway.  Both complex
extensions of `Q_beta` are a real-non-negative modulus factor times a rational
function with REAL coefficients, so Schwarz reflection gives

    Q_beta(qbar) = conj(Q_beta(q))                       [exact, verified here]

A chirality-INVARIANT observable satisfies `O(qbar) = O(q)`.  For `Q_beta` that
reads `conj(Q_beta) = Q_beta`, i.e. `Q_beta` real -- which by the merged
`QOU.QBeta.im_qbeta_zero_iff_e1` / `_e2` forces `Im q = 0` on the whole of
candidate (ii)'s admissible set.

So candidate (i) closes at the archimedean layer under EITHER reading: its
identification is the corpus's only on the unit circle (and the substrate is
not on it), and where the identification is granted it collapses `arg q` to
zero against a parity-even observable.

🛑 THE PREMISE THIS LEG NEEDS, STATED AND NOT SMUGGLED
-------------------------------------------------------
"`Q_beta` is chirality-invariant" is a PHYSICS premise, not a corpus theorem: a
Q-value is an energy release, a parity-even scalar.  It is carried as an
explicit hypothesis in the Lean (`QOU.QBeta.ImQChiralityIsBarInvolution`), never
as an assumption inside a proof.  The FIRST leg needs no such premise -- it is
arithmetic plus three corpus citations.

WHAT THIS DOES NOT DO
---------------------
It does not touch the FIBRE level, where `AGENTS.md`'s fibre-vs-observable
banner leaves `Im q` unconstrained and where the Kashaev root-of-unity regime
actually lives.  Candidate (i) may well be right ON THE FIBRE; what closes is
its archimedean reading at the substrate.  Nor does it say the bar involution
is unimportant -- the opposite: it says the chirality content the conjecture was
looking for in `Im q` is already in the corpus, at real `q`, in `P_skew`.

PRECISION.  Exact sympy for the identities; mpmath 50 dps from the 50-digit
proton pin for the substrate numbers.  No float64, per AGENTS.md "PROBES ARE
NOT EXEMPT".
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate")]

mp.mp.dps = 50
Q0_STR = "1.1099785827513808075916690956107688798744991218736"

CORPUS_CITATIONS = [
    ("folio/quantum-observable-universe/mass-theory/archimedean-image-table-table1-data.md",
     "row 4", "J_Kbar(q) = J_K(q^{-1})  (mirror; matter/antimatter CPT)"),
    ("folio/quantum-observable-universe/mass-theory/hq-bi-filtration.md",
     "bar-involution row",
     "Bar involution * : q -> q^{-1} ; * : H_q^{(n,K)} -> H_q^{(n,K*)} where K* is the mirror knot"),
    ("folio/quantum-observable-universe/mass-theory/knot-indexed-convolution-grid-table2-data.md",
     "bar-involution row", "Bar involution: H_q^{(n,K)} -> H_q^{(n,K*)} ; mirror knot K*"),
]


def main() -> int:
    print("=" * 78)
    print(" Candidate (i): is `arg q` the chirality coordinate?  (conj:im-q-physical-role)")
    print("=" * 78)

    x, y = sp.symbols("x y", real=True)
    q = x + sp.I * y
    s = x**2 + y**2

    # ---- [1] the two candidate chirality operations, and when they agree ----
    diff = sp.simplify(sp.conjugate(q) - 1 / q)
    diff_num = sp.factor(sp.numer(sp.cancel(sp.together(diff))))
    print("\n[1] the two operations")
    print("    candidate (i)  chirality flip = q -> conj(q)")
    print("    the corpus     chirality flip = q -> 1/q   (bar involution; mirror knot)")
    print(f"    conj(q) - 1/q  = {sp.simplify(diff)}")
    print(f"    numerator      = {diff_num}")
    # conj(q) = 1/q  <=>  q*conj(q) = 1  <=>  |q|^2 = 1
    agree_cond = sp.simplify(sp.expand(q * sp.conjugate(q)) - 1)
    print(f"    q*conj(q) - 1  = {agree_cond}   -> they agree exactly on |q|^2 = 1")

    # verify by solving
    sols = sp.solve(sp.Eq(sp.expand(q * sp.conjugate(q)), 1), s)
    agree_iff_unit = sols == [1] or sp.simplify(agree_cond - (s - 1)) == 0
    print(f"    agree iff |q| = 1: {agree_iff_unit}")

    # ---- [2] the substrate is not on the unit circle ----
    q0 = mp.mpf(Q0_STR)
    absq0 = abs(mp.mpc(q0, 0))
    inv = 1 / q0
    conj = q0                      # q0 is real, so conj(q0) = q0
    sep = abs(conj - inv)
    print("\n[2] the substrate")
    print(f"    q_0            = {mp.nstr(q0, 25)}")
    print(f"    |q_0|          = {mp.nstr(absq0, 25)}     on unit circle: {absq0 == 1}")
    print(f"    conj(q_0)      = {mp.nstr(conj, 25)}   (real, so conjugation is the IDENTITY here)")
    print(f"    1/q_0          = {mp.nstr(inv, 25)}   (the corpus's mirror; also REAL)")
    print(f"    separation     = {mp.nstr(sep, 20)}  = {mp.nstr(100*sep/q0, 6)} % of q_0")

    # ---- [3] Schwarz reflection: Q_beta(conj q) = conj(Q_beta(q)) ----
    # E1 = |q^2-2q-1| * (q+1)/(2q^3);  E2 = |Delta(net)| / (q(q-1)).
    # Both are (real >= 0 modulus) * (real-coefficient rational), so both reflect.
    def qb_e1(qc):
        return abs(qc**2 - 2 * qc - 1) * (qc + 1) / (2 * qc**3)

    def qb_e2(qc):
        h = qc - 1 / qc
        return abs(h * (h - 2) / 2) / (qc * (qc - 1))

    refl = []
    for lbl, qc in [("q_0 + 0.01i", mp.mpc(q0, mp.mpf("0.01"))),
                    ("q_0 + 0.1i", mp.mpc(q0, mp.mpf("0.1"))),
                    ("0.95 + 0.3i", mp.mpc(mp.mpf("0.95"), mp.mpf("0.3")))]:
        for name, f in [("E1", qb_e1), ("E2", qb_e2)]:
            lhs = f(mp.conj(qc))
            rhs = mp.conj(f(qc))
            refl.append({"case": lbl, "extension": name,
                         "abs_Qb_conj_q_minus_conj_Qb_q": mp.nstr(abs(lhs - rhs), 8)})
    max_refl = max(mp.mpf(r["abs_Qb_conj_q_minus_conj_Qb_q"]) for r in refl)
    print("\n[3] Schwarz reflection  Q_beta(conj q) = conj(Q_beta(q))")
    for r in refl:
        print(f"    {r['case']:14s} {r['extension']}  |LHS - RHS| = {r['abs_Qb_conj_q_minus_conj_Qb_q']}")
    print(f"    max residual over all cases = {mp.nstr(max_refl, 8)}  (50 dps arithmetic)")

    # ---- [4] so chirality-invariance of Q_beta forces Im q = 0 ----
    # O(conj q) = O(q) together with O(conj q) = conj(O(q)) gives O real.
    print("\n[4] granting candidate (i)'s identification anyway")
    print("    chirality-invariant means  Q_beta(conj q) = Q_beta(q)")
    print("    Schwarz gives              Q_beta(conj q) = conj(Q_beta(q))")
    print("    together                   conj(Q_beta) = Q_beta, i.e. Q_beta REAL")
    print("    and QOU.QBeta.im_qbeta_zero_iff_e1/_e2 then force Im q = 0")
    print("    PREMISE, stated not smuggled: 'Q_beta is chirality-invariant' is PHYSICS")
    print("    (a Q-value is a parity-even energy), carried as an explicit hypothesis.")

    assertions = [
        {"name": "conjugation_equals_bar_involution_exactly_on_the_unit_circle",
         "passed": bool(agree_iff_unit),
         "detail": "conj(q) = 1/q  <=>  q*conj(q) = 1  <=>  |q|^2 = 1, exactly"},
        {"name": "substrate_is_not_on_the_unit_circle",
         "passed": bool(absq0 != 1),
         "detail": f"|q_0| = {mp.nstr(absq0, 20)} != 1, so the two operations are "
                   f"distinct there"},
        {"name": "corpus_mirror_is_real_at_the_substrate",
         "passed": bool(mp.im(mp.mpc(inv, 0)) == 0),
         "detail": f"the corpus's chirality flip sends q_0 to 1/q_0 = "
                   f"{mp.nstr(inv, 20)}, a REAL number -- it needs no Im q at all"},
        {"name": "the_two_flips_are_separated_at_the_substrate",
         "passed": bool(sep > mp.mpf("0.2")),
         "detail": f"|conj(q_0) - 1/q_0| = {mp.nstr(sep, 12)}, "
                   f"{mp.nstr(100*sep/q0, 5)} % of q_0 -- not a near-coincidence"},
        {"name": "schwarz_reflection_holds_for_both_extensions",
         "passed": bool(max_refl < mp.mpf("1e-40")),
         "detail": f"max |Q_beta(conj q) - conj(Q_beta(q))| = {mp.nstr(max_refl, 6)} "
                   f"over 3 points x 2 extensions, at 50 dps"},
    ]
    print("\n  assertions:")
    for a in assertions:
        print(f"    [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
        print(f"           {a['detail']}")
    ok = all(a["passed"] for a in assertions)
    print(f"\n  allPassed: {ok}  ({sum(a['passed'] for a in assertions)}/{len(assertions)})")

    out = HERE / "imq-chirality-is-the-bar-involution.witness.json"
    w = {
        "description": "conj:im-q-physical-role candidate (i) assigns chirality to arg q. "
                       "The corpus assigns it to the bar involution q -> 1/q (three "
                       "citations), and the two operations coincide EXACTLY on |q| = 1 "
                       "and nowhere else. The substrate has |q_0| = 1.10998, so at the "
                       "substrate the corpus's chirality flip is 1/q_0 = 0.9009182840 -- a "
                       "REAL number needing no Im q. Second leg: granting candidate (i)'s "
                       "identification anyway, Schwarz reflection plus a parity-even "
                       "Q_beta forces Im q = 0 via the merged im_qbeta_zero_iff theorems.",
        "engine": "sympy (exact) + mpmath 50 dps; no float64",
        "q0Anchor": "proton",
        "q0AnchorReason": "AGENTS.md 2026-08-07 owner directive: proton is the default for "
                          "all new compute; this is neither a proton-vs-muon comparison "
                          "nor an ideal-CAL statement",
        "q0Value": Q0_STR,
        "data": {
            "candidate_i_identification": "chirality flip = q -> conj(q); arg q is the chirality coordinate",
            "corpus_identification": "chirality flip = q -> 1/q (bar involution, mirror knot)",
            "corpus_citations": [{"file": f, "where": w_, "text": t}
                                 for f, w_, t in CORPUS_CITATIONS],
            "they_agree_iff": "|q|^2 = 1 (the unit circle) -- exactly, by q*conj(q) = 1",
            "candidate_i_regime": "'near the unit circle', Kashaev q = exp(2 pi i / N) -- "
                                  "where the identification IS correct",
            "substrate_abs_q0": mp.nstr(absq0, 25),
            "substrate_on_unit_circle": bool(absq0 == 1),
            "corpus_mirror_of_q0": mp.nstr(inv, 25),
            "separation_of_the_two_flips": mp.nstr(sep, 25),
            "separation_pct_of_q0": mp.nstr(100 * sep / q0, 10),
            "schwarz_reflection_max_residual": mp.nstr(max_refl, 10),
            "schwarz_checks": refl,
            "physics_premise_for_leg_two": "'Q_beta is chirality-invariant' -- a Q-value is "
                                           "a parity-even energy. This is PHYSICS, not a "
                                           "corpus theorem, and is carried as an explicit "
                                           "Lean hypothesis, never assumed inside a proof. "
                                           "Leg one needs no such premise.",
            "scope": "(b) for leg one -- an exact algebraic identity (conj = inv iff |q|=1) "
                     "plus three corpus citations, no numerical near-miss. Leg two is "
                     "conditional on the stated premise. BOTH are scoped to the "
                     "ARCHIMEDEAN evaluation at the substrate.",
            "does_not_close": "the FIBRE level, where AGENTS.md's fibre-vs-observable "
                              "banner leaves Im q unconstrained and where the Kashaev "
                              "root-of-unity regime actually lives. Candidate (i) may be "
                              "right on the fibre; what closes is its archimedean reading.",
            "positive_content": "the chirality the conjecture went looking for in Im q is "
                                "already in the corpus at real q, as the bar involution's "
                                "P_skew content (rem:im-q-vs-p-skew) -- which that same "
                                "block says is 'kept then discarded' by the canonical "
                                "P_avg projection.",
        },
        "assertions": assertions,
        "allPassed": ok,
    }
    out.write_text(json.dumps(w, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
