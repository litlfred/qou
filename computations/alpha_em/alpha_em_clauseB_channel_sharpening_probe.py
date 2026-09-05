#!/usr/bin/env python3
"""alpha_em_clauseB_channel_sharpening_probe.py

Sharpens Clause B of the per-loop conjecture (the "1/2 = two Hecke channels"
factor) with exact discriminants, building on what is ALREADY derived (lever-2
`3f4ebbc1f`: the 2-channel factorization of the loop tower; main `ba606720e`:
the GB form). Answers: WHERE exactly does the 1/2 live, and what precisely
remains to derive?

Established inputs (not re-derived): the loop tower
  Sum_{L>=0} (-1)^L [L+1]_q x^L = 1/((1+q x)(1+q^{-1} x))
(two Hecke eigenchannels q, -q^{-1} of A(x)A; lever-2, verified O(x^12) there).

FINDINGS (exact, sympy):
  F1. CHANNEL COUNT = 2 is STRUCTURAL: the Hecke relation (sigma-q)(sigma+q^{-1})=0
      is quadratic => H_2(q) splits into exactly two idempotent channels
      e+ = (sigma+q^{-1})/(q+q^{-1}), e- = (q-sigma)/(q+q^{-1}):
      e+ + e- = 1, e+e- = 0, e+^2 = e+, sigma = q e+ - q^{-1} e-.  [derived]
  F2. THE 1/2 IS NOT A CHANNEL WEIGHT: the resummed propagator's partial
      fractions are w+ = q^2/(q^2-1), w- = -1/(q^2-1) — w+ + w- = 1 but
      (w+,w-) = (1/2,1/2) IFF q^2 = -1 (never at real q). At the substrate
      q0 = 1.10998: (w+,w-) ~ (5.31, -4.31). So any derivation of the 1/2 as
      "equal channel weights at q0" is EXCLUDED (scope-(a)).
  F3. WHERE THE 1/2 LIVES: the tower's 1-loop coefficient is exactly -[2]_q x
      (the FULL channel sum), so matching the working term alpha [2]_q/(8 pi)
      forces x = alpha/(8 pi) with NO q->1 limit — the q-dependence is carried
      entirely by [2]_q, the measure x is q-independent. The 1/2 is then
      x/(alpha a0) with a0 = 1/(4 pi): a CLASSICAL-LIMIT NORMALIZATION —
      at q=1 the 1-loop total is 2x, and 2x = alpha/(4 pi) (the standard unit)
      iff x = alpha/(8 pi).
  => CLAUSE B REDUCES TO ONE STATEMENT: "the q->1 one-loop total of the tower
     equals the universal heat-kernel unit a0*alpha" (the correspondence
     normalization). Channel count (2) is derived; the half-as-weights reading
     is excluded; the correspondence normalization is the remaining conjecture.

Scope guard: no fit; nothing wired; 1/(8pi) stays phase-4 (R1 canonical); this
NARROWS Clause B, it does not derive it. Self-contained (sympy).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    q, x, s = sp.symbols('q x sigma')
    u = 1 / q
    hecke = sp.expand((s - q) * (s + u))          # sigma^2 - (q - q^{-1}) sigma - 1
    h = q + u                                      # [2]_q, invertible generically

    def red(expr):
        # reduce polynomials in sigma modulo the Hecke relation
        return sp.simplify(sp.rem(sp.expand(expr), hecke, s))

    # F1: exactly two idempotent channels (structural: quadratic Hecke relation)
    ep = (s + u) / h
    em = (q - s) / h
    f1 = (sp.simplify(red(ep + em) - 1) == 0
          and sp.simplify(red(sp.expand(ep * em))) == 0
          and sp.simplify(red(sp.expand(ep * ep - ep))) == 0
          and sp.simplify(red(sp.expand(em * em - em))) == 0
          and sp.simplify(red(q * ep - u * em - s)) == 0)
    check("channel_count_2_structural_idempotents", f1,
          "e+ = (sigma+q^{-1})/[2]_q, e- = (q-sigma)/[2]_q satisfy e+ + e- = 1, e+e- = 0, "
          "e+^2 = e+, e-^2 = e-, sigma = q e+ - q^{-1} e- EXACTLY mod the Hecke relation "
          "=> the channel COUNT is 2 because the Hecke relation is QUADRATIC — structural, "
          "derived (not conjectural)")

    # F2: the 1/2 is NOT a channel weight — partial fractions of the resummed tower
    wp = q ** 2 / (q ** 2 - 1)
    wm = -1 / (q ** 2 - 1)
    pf = sp.simplify(wp / (1 + q * x) + wm / (1 + u * x) - 1 / ((1 + q * x) * (1 + u * x)))
    eq_half = sp.solve(sp.Eq(wp, sp.Rational(1, 2)), q)
    q0 = sp.Rational(110998, 100000)
    wp0, wm0 = float(wp.subs(q, q0)), float(wm.subs(q, q0))
    f2 = (pf == 0 and sp.simplify(wp + wm - 1) == 0
          and all(not sym.is_real for sym in eq_half)
          and abs(wp0 - 5.309) < 0.01 and abs(wm0 + 4.309) < 0.01)
    check("half_is_not_a_channel_weight", f2,
          f"partial fractions: w+ = q^2/(q^2-1), w- = -1/(q^2-1) (sum 1, exact); "
          f"(w+,w-) = (1/2,1/2) iff q^2 = -1 (roots {eq_half}, never real); at q0: "
          f"({wp0:.3f}, {wm0:.3f}) — so deriving the 1/2 as equal channel WEIGHTS at "
          "real q is EXCLUDED (scope-(a)); the channels are counted democratically, "
          "not weighted democratically")

    # F3: the 1-loop coefficient is -[2]_q x exactly => x is q-independent; the 1/2 is
    #     the classical-limit normalization 2x = alpha*a0 at q=1
    tower = 1 / ((1 + q * x) * (1 + u * x))
    c1 = sp.series(tower, x, 0, 2).removeO().coeff(x, 1)
    f3 = (sp.simplify(c1 + h) == 0
          and sp.simplify(sp.series(tower.subs(q, 1), x, 0, 2).removeO().coeff(x, 1) + 2) == 0)
    check("half_lives_in_classical_limit_normalization", f3,
          "tower 1-loop coefficient = -[2]_q x EXACTLY (q-dependence all in [2]_q; the "
          "measure x is q-independent, matching the working alpha[2]_q/(8pi) with "
          "x = alpha/(8pi) and NO q->1 limit); at q=1 the 1-loop total is 2x, so "
          "x = alpha/(8pi) IFF the q->1 one-loop equals the standard unit alpha/(4pi) "
          "= alpha*a0 — Clause B REDUCES to this single correspondence normalization")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "CLAUSE B SHARPENED TO ONE STATEMENT (scope-(a); no fit; nothing wired; 1/(8pi) "
        "stays phase-4): (F1) the channel COUNT 2 is structural/derived — the Hecke relation "
        "is quadratic, giving exactly the two idempotent channels e+/e-; (F2) the 1/2 is NOT "
        "an equal channel WEIGHT — partial-fraction weights are (q^2/(q^2-1), -1/(q^2-1)), "
        "equal only at q^2 = -1, and (5.31, -4.31) at the substrate q0; (F3) the 1/2 lives in "
        "the per-loop parameter via the CLASSICAL-LIMIT NORMALIZATION: the tower's 1-loop is "
        "-[2]_q x exactly, so x = alpha/(8pi) iff the q->1 one-loop equals the universal "
        "heat-kernel unit alpha*a0 = alpha/(4pi). REMAINING CONJECTURE (all of Clause B): the "
        "correspondence normalization 'q->1 one-loop = a0*alpha'. Nothing else is open in "
        "Clause B. NO tier change."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    _here = os.path.dirname(os.path.abspath(__file__))

    def _sha():
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not out:
            raise RuntimeError("empty commitSha")
        return out

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "alpha-em-clauseB-channel-sharpening",
        "description": "Sharpens Clause B (the 1/2 = two Hecke channels) of the per-loop conjecture: "
                       "(F1) channel count 2 is structural (quadratic Hecke relation, idempotents e+/e- "
                       "exact); (F2) the 1/2 is NOT an equal channel weight (partial fractions "
                       "(q^2/(q^2-1), -1/(q^2-1)), equal only at q^2=-1; (5.31,-4.31) at q0) — excluded; "
                       "(F3) the 1-loop coefficient is -[2]_q x exactly, so the 1/2 is the classical-"
                       "limit normalization 2x = alpha*a0. Clause B reduces to that single "
                       "correspondence statement. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-perloop-conjecture-statement.md",
        "tier": "symbolic-exact (sympy; quotient-ring identities + partial fractions + series)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "channel_count": "2 — structural (degree of the Hecke relation), DERIVED",
            "half_as_weights": "EXCLUDED (weights equal only at q^2=-1; (5.31,-4.31) at q0)",
            "half_location": "classical-limit normalization: q->1 one-loop = alpha*a0 = alpha/(4pi)",
            "clauseB_remaining": "the single correspondence normalization statement",
            "verdict": verdict,
        },
        "context": {
            "builds_on": "lever-2 3f4ebbc1f (2-channel factorization, derived) + main ba606720e (GB "
                         "form) + the two-clause conjecture statement (this PR)",
            "narrows": "Clause B from 'the 1/2 is the Hecke channel split' to the precise open piece: "
                       "'the q->1 one-loop total equals the universal heat-kernel unit a0*alpha' — "
                       "channel count derived, weights reading excluded",
            "scope_guard": "no fit; nothing wired; derives neither clause; 1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-clauseB-channel-sharpening.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
