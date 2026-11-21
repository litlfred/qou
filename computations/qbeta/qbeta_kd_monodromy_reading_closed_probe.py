#!/usr/bin/env python3
"""qou-pdix branch 3: the MONODROMY reading is CLOSED, by trace-invariance —
no associator computation needed. Only the open-path/Stokes reading survives.

Entry 5 defines the one contentful branch as

    3. M = exponential/holonomy of an INDEPENDENTLY-DEFINED connection whose
       monodromy reproduces the Hecke braiding

and says it "escapes (1) because a holonomy is transcendental". **That escape
does not work for the monodromy reading**, and the reason is one line:

    CONJUGATION PRESERVES THE TRACE, and the carrier condition is ON the trace.

A connection whose monodromy reproduces the Hecke braiding has, by
Kohno-Drinfeld, holonomy matrices gauge-conjugate to the Hecke braid-image
matrices. Gauge-conjugate matrices have the SAME TRACE. So the monodromy's trace
is exactly some tr rho(w) — and those are computed below and are Laurent
polynomials. The transcendence of a holonomy's matrix ENTRIES along the way buys
nothing: the closed-loop trace is pinned by the very requirement that the
monodromy reproduce the braiding.

*** FALSIFIER A — det, checked first ***

    det rho(sigma_0) = det rho(sigma_1) = det rho(sigma_0^-1)
                     = det rho(sigma_1^-1) = -1   EXACTLY, all q

so an EVEN-length braid word has det = +1 exactly. **The carrier's second field,
`M.det = 1`, is automatic and free on the braid image** — it was never the
obstruction. (Had det been q-dependent, the even-word normalisation argument
would need care.)

*** FALSIFIER B — is the trace really Laurent? ***

The seminormal off-diagonal carries sqrt(q^4+q^2+1), so a word's trace could
have been irrational over Q(q). It is not: on ten even-length words the radical
cancels identically and every trace lies in Z[q,q^-1] —

    sigma_0 sigma_1                     -1
    sigma_0 sigma_1^-1                  -(q^4 - q^2 + 1)/q^2
    sigma_0 sigma_1 sigma_1 sigma_0     (q^4 + 1)/q^2
    (sigma_0 sigma_1)^2                 -1
    (sigma_0 sigma_1)^3                 2

as characters must. So the FIRST carrier field asks a Laurent polynomial to equal
2*cos(alpha), and entry 4 proves 2*cos((z-1)h/2) is TRANSCENDENTAL over Q(q,z).
Impossible. Sharper than "characters are algebraic": it names which field is free
(det) and which is impossible (trace).

*** THE FULL TWIST IS THE IDENTITY ***

    (sigma_0 sigma_1)^3 = I   EXACTLY in the (2,1) block, for every q

verified as a matrix identity, not just a trace. The full twist generates the
CENTRE of B_3, so the (2,1) representation factors through B_3/<Delta^2>, i.e.
through PSL(2,Z). The available traces are therefore indexed by conjugacy
classes in that quotient — a countable set of Laurent polynomials, and 2*cos of
an algebraic angle is in none of them.

*** WHAT THIS CLOSES, AND WHAT SURVIVES ***

CLOSED: branch 3 **as entry 5 words it** — "whose monodromy reproduces the Hecke
braiding". Any such connection's monodromies have Hecke traces, hence cannot
carry alpha. This needs no Drinfeld associator, no zeta(3) computation, and no
construction: it follows from trace-invariance under the gauge equivalence
Kohno-Drinfeld supplies.

SURVIVES: the **open-path / non-abelian Stokes** reading. A holonomy along an
OPEN path is not a monodromy — not a closed loop, not a braid-group image — so
it is not trace-pinned by the braiding requirement, and it is gauge-DEPENDENT
(it transforms by the endpoint frames rather than by conjugation). Entry 5 cites
"Yekutieli non-abelian Stokes", so this IS the corpus's intended shape; its own
wording just does not capture it, and the escape clause it offers ("a holonomy is
transcendental") is the wrong reason.

SUPERSEDES the note added earlier today proposing a zeta(3) test of the KZ
holonomy angle's t^3 coefficient. That test was aimed at the monodromy reading,
which is now closed by a cheaper argument; on the open-path reading the
associator coefficients are not the obstruction either, because nothing forces
that holonomy to be algebraic in the first place.

SCOPE. Scope-(a). Nothing derived, proposed, wired or readmitted; no convention
adjudicated. Anchor: none required (exact symbolic identities in q).
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate"),
                str(HERE.parent / "hecke")]
import _path_bridge  # noqa: E402, F401

QS = sp.Symbol("q", positive=True)
HS = QS - 1 / QS
RAD = sp.sqrt(QS ** 4 + QS ** 2 + 1)


def generators():
    t0 = sp.Matrix([[QS, 0], [0, sp.Rational(-1) / QS]])
    a = -1 / (QS ** 3 + QS)
    b = RAD / (QS ** 2 + 1)
    t1 = sp.Matrix([[a, b], [b, HS - a]])
    return {"0": t0, "1": t1,
            "a": sp.simplify(t0 - HS * sp.eye(2)),   # sigma_0^-1
            "A": sp.simplify(t1 - HS * sp.eye(2))}   # sigma_1^-1


def word(gens, s):
    m = sp.eye(2)
    for ch in s:
        m = m * gens[ch]
    return m


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    t_start = time.monotonic()
    print("=" * 78)
    print(" qou-pdix branch 3: the MONODROMY reading is closed by trace-invariance")
    print("=" * 78)
    g = generators()

    # sanity: it really is the Hecke (2,1) rep
    hecke_ok = all(sp.simplify((g[k] - QS * sp.eye(2)) * (g[k] + sp.eye(2) / QS))
                   == sp.zeros(2, 2) for k in ("0", "1"))
    braid_ok = sp.simplify(g["0"] * g["1"] * g["0"]
                           - g["1"] * g["0"] * g["1"]) == sp.zeros(2, 2)
    print(f"\n[0] it is the Hecke (2,1) rep: quadratic {hecke_ok}, braid {braid_ok}")

    # [1] falsifier A
    dets = {nm: sp.simplify(m.det()) for nm, m in g.items()}
    all_minus_one = all(d == -1 for d in dets.values())
    print(f"\n[1] FALSIFIER A — det of each generator")
    for nm, d in dets.items():
        print(f"    det rho({nm}) = {d}")
    print(f"    all equal -1 : {all_minus_one}")
    print(f"    -> an EVEN-length word has det = +1 EXACTLY, so the carrier's")
    print(f"       second field `M.det = 1` is AUTOMATIC and free on the braid")
    print(f"       image. It was never the obstruction.")

    # [2] falsifier B
    words = ["01", "10", "0A", "1a", "0110", "01aA", "0101", "aA01", "0A1a", "010101"]
    print(f"\n[2] FALSIFIER B — do the traces lie in Z[q,q^-1]?")
    print(f"    {'word':10s}{'len':>4s}{'det':>5s}   trace")
    rows, laurent_ok = [], True
    for w in words:
        m = word(g, w)
        tr = sp.simplify(sp.expand(sp.simplify(m.trace())))
        dt = sp.simplify(m.det())
        has_rad = tr.has(RAD) or any(
            x.is_Pow and x.exp.is_Rational and x.exp.q != 1 for x in tr.atoms(sp.Pow))
        laurent_ok &= (not has_rad)
        rows.append({"word": w, "len": len(w), "det": str(dt),
                     "trace": str(sp.factor(tr)), "radical_free": not has_rad})
        print(f"    {w:10s}{len(w):>4d}{str(dt):>5s}   {sp.factor(tr)}")
    print(f"    every trace radical-free (the sqrt cancels) : {laurent_ok}")

    # [3] the full twist
    ft = sp.simplify((g["0"] * g["1"]) ** 3)
    ft_is_id = sp.simplify(ft - sp.eye(2)) == sp.zeros(2, 2)
    print(f"\n[3] the FULL TWIST (sigma_0 sigma_1)^3")
    print(f"    equals the identity matrix, for every q : {ft_is_id}")
    print(f"    -> it generates the CENTRE of B_3, so the (2,1) rep factors")
    print(f"       through B_3/<Delta^2> = PSL(2,Z). The achievable traces are")
    print(f"       indexed by conjugacy classes there — a countable set of")
    print(f"       Laurent polynomials.")

    # [4] the closure
    print(f"\n[4] WHAT CLOSES, AND WHY NO ASSOCIATOR IS NEEDED")
    print(f"    Kohno-Drinfeld: a connection whose monodromy reproduces the Hecke")
    print(f"    braiding has holonomies GAUGE-CONJUGATE to the braid-image")
    print(f"    matrices. Conjugation PRESERVES THE TRACE, and the carrier")
    print(f"    condition is ON the trace. So such a monodromy's trace is some")
    print(f"    tr rho(w) in Z[q,q^-1], while the carrier needs 2*cos(alpha),")
    print(f"    transcendental over Q(q,z) by entry 4. IMPOSSIBLE.")
    print(f"    Entry 5's escape clause — 'a holonomy is transcendental' — is the")
    print(f"    wrong reason: transcendental ENTRIES do not buy a transcendental")
    print(f"    closed-loop TRACE when the loop must reproduce the braiding.")
    print(f"\n    SURVIVES: the OPEN-PATH / non-abelian Stokes reading. An open-path")
    print(f"    holonomy is not a monodromy — not a closed loop, not a braid image —")
    print(f"    so it is not trace-pinned, and it is gauge-DEPENDENT (it transforms")
    print(f"    by the endpoint frames, not by conjugation). Entry 5 cites")
    print(f"    'Yekutieli non-abelian Stokes', so that IS the intended shape; the")
    print(f"    wording just does not capture it.")

    a = [
        {"name": "generators_have_det_minus_one_so_the_det_field_is_free",
         "passed": bool(all_minus_one and hecke_ok and braid_ok),
         "detail": "in the (2,1) block det rho(sigma_0) = det rho(sigma_1) = "
                   "det rho(sigma_0^-1) = det rho(sigma_1^-1) = -1 exactly, for every q, "
                   "so an EVEN-length braid word has det = +1 exactly. The carrier's "
                   "second field `M.det = 1` is automatic and free on the braid image — it "
                   "was never the obstruction. (Quadratic and braid relations verified, so "
                   "this really is the Hecke (2,1) rep.)"},
        {"name": "word_traces_are_laurent_polynomials_the_radical_cancels",
         "passed": bool(laurent_ok),
         "detail": "the seminormal off-diagonal carries sqrt(q^4+q^2+1), so a trace could "
                   "have been irrational over Q(q). On ten even-length words it cancels "
                   "identically and every trace lies in Z[q,q^-1], as characters must. So "
                   "the carrier's FIRST field asks a Laurent polynomial to equal "
                   "2*cos(alpha), which entry 4 proves transcendental over Q(q,z)"},
        {"name": "full_twist_is_the_identity_so_the_rep_factors_through_PSL2Z",
         "passed": bool(ft_is_id),
         "detail": "(sigma_0 sigma_1)^3 = I exactly in the (2,1) block for every q — "
                   "verified as a matrix identity, not merely a trace. The full twist "
                   "generates the centre of B_3, so the representation factors through "
                   "B_3/<Delta^2> = PSL(2,Z) and the achievable traces are indexed by "
                   "conjugacy classes there: a countable set of Laurent polynomials"},
        {"name": "the_monodromy_reading_of_branch_3_is_closed_by_trace_invariance",
         "passed": bool(all_minus_one and laurent_ok and ft_is_id),
         "detail": "Kohno-Drinfeld gives holonomies gauge-conjugate to the braid-image "
                   "matrices for any connection whose monodromy reproduces the Hecke "
                   "braiding; conjugation PRESERVES THE TRACE and the carrier condition is "
                   "ON the trace, so such a monodromy's trace is some tr rho(w) in "
                   "Z[q,q^-1] and cannot be 2*cos(alpha). Branch 3 AS ENTRY 5 WORDS IT is "
                   "closed, with no Drinfeld associator and no zeta(3) computation. Entry "
                   "5's escape clause 'a holonomy is transcendental' is the wrong reason: "
                   "transcendental entries do not buy a transcendental closed-loop trace "
                   "when the loop must reproduce the braiding. SURVIVES: the open-path / "
                   "non-abelian Stokes reading, which is not a monodromy, not trace-pinned, "
                   "and gauge-dependent rather than conjugation-covariant"},
    ]
    ok = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {ok}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-kd-monodromy-reading-closed",
        "engine": "sympy",
        "description": (
            "qou-pdix branch 3. Entry 5 defines the one contentful branch as a connection "
            "'whose monodromy reproduces the Hecke braiding', escaping the rationality "
            "exclusion 'because a holonomy is transcendental'. That escape fails for the "
            "monodromy reading: Kohno-Drinfeld gives holonomies GAUGE-CONJUGATE to the "
            "braid-image matrices, conjugation PRESERVES THE TRACE, and the carrier "
            "condition is on the trace. Verified symbolically: every generator has "
            "det = -1 exactly so an even-length word has det = +1 and the carrier's "
            "`M.det = 1` field is AUTOMATIC and free (it was never the obstruction); every "
            "word trace is a Laurent polynomial in Z[q,q^-1], the seminormal radical "
            "cancelling identically; and (sigma_0 sigma_1)^3 = I exactly, so the rep "
            "factors through B_3/centre = PSL(2,Z) and the achievable traces are a "
            "countable set of Laurent polynomials. 2*cos((z-1)h/2) is transcendental over "
            "Q(q,z) by entry 4, so the trace field is impossible. Branch 3 AS WORDED is "
            "closed, with no associator and no zeta(3) computation — superseding the "
            "zeta(3) proposal noted earlier today. SURVIVES: the open-path / non-abelian "
            "Stokes reading, which is not a monodromy, not trace-pinned, and "
            "gauge-dependent rather than conjugation-covariant."),
        "contentBlock": "def:three-calibration-discipline",
        "assertions": a,
        "allPassed": ok,
        "parameters": {"block": "(2,1)", "symbolic": True, "anchor": "none required"},
        "data": {"generator_dets": {k: str(v) for k, v in dets.items()},
                 "words": rows,
                 "full_twist_is_identity": bool(ft_is_id),
                 "quotient": "B_3 / <Delta^2> = PSL(2,Z)"},
        "context": {
            "axis": "qou-pdix branch 3: does a KZ/Stokes connection escape the "
                    "rationality exclusion?",
            "answer": "Not in the MONODROMY reading. Conjugation preserves the trace, so a "
                      "monodromy reproducing the Hecke braiding has a Hecke trace — a "
                      "Laurent polynomial — and cannot equal the transcendental "
                      "2*cos(alpha). Only the open-path / non-abelian Stokes reading "
                      "survives.",
            "supersedes": "the zeta(3) t^3 test proposed earlier today, which targeted "
                          "the monodromy reading now closed by a cheaper argument.",
            "scope": "Scope-(a). Nothing derived, proposed, wired or readmitted.",
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t_start) * 1000),
    }
    out_p = HERE / "qbeta-kd-monodromy-reading-closed.witness.json"
    with open(out_p, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="sympy",
            q0_anchor="independent",
            q0_anchor_reason=(
                "exact symbolic identities in q: every quantity here is a "
                "Laurent polynomial in the sympy symbol q, and no pin is "
                "read anywhere in the file or its import cone (stdlib + "
                "sympy only). No q0Value is recorded because a single "
                "value would assert the one pin this label denies."))
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
