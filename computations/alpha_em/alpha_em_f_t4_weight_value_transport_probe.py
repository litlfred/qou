#!/usr/bin/env python3
"""alpha_em_f_t4_weight_value_transport_probe.py

F-construction **T4 — weight-value transport (¾, ¼)**, the derivation leg of
milestone `qou-a46k` (T1 cover #4039, T2 Burau-at-i #4040, T3 deck reality
merged; T5 assembly open).

T1 derived the isotypic DIMS (3,1) of H¹(Bring) under the degree-4 deck action
(Chevalley–Weil, zero adjustable input). T4 must derive the framework-side
weight VALUES and pin where the transport is anchored. Three exact facts do it
(each numerically certified here; Lean siblings in
`QOU/Archimedean/MarkovWeightValueTransport.lean`):

1. **VALUE IDENTITY.** The canonical Jones–Markov H₂ weights (corpus
   `wedderburn_jones_markov.y_lambda_at`, Wenzl normalization, s = √q):

       y_[2](s)   = (s³+s²+1) / ((s²+1)(s⁴+1)),
       y_[1,1](s) = s³(s³+s−1) / ((s²+1)(s⁴+1)),   y_[2]+y_[1,1] = 1,

   evaluate at the classical point s = 1 to EXACTLY (¾, ¼) = (3,1)/4 — the
   T1 Chevalley–Weil dims over g = 4. The framework's canonical weight at
   q = 1 IS the normalized isotypic projector trace of the T1 cover.

2. **THE ANCHOR IS FORCED.** q = 1 is the UNIQUE positive matching point:

       4(s³+s²+1) − 3(s²+1)(s⁴+1) = −(s−1)(3s⁵+3s⁴+6s³+2s²+s+1),

   and the quintic cofactor is strictly positive for s > 0, so
   y_[2](s) = 3/4 ⟺ s = 1 on s > 0. The transport point is derived, not
   chosen — no dictionary freedom (the tranche-5 vacuity prune does not
   apply to a forced anchor).

3. **TRANSPORT CANNOT HAPPEN AT THE MONODROMY POINT.** The weight
   denominator in the q-variable is q³+q²+q+1 = (q+1)(q²+1), which VANISHES
   at the T2 Hecke evaluation q = i. The Markov weights have a genuine pole
   at the monodromy point — the (¾,¼) values can only be carried at the
   forced classical anchor, while the module structure lives at q = i. The
   two evaluations are complementary, not interchangeable.

Together: F(canonical Markov weight) at the forced anchor = the normalized
(3,1) projector trace on H¹(Bring) — the weight-value premise of the #3999
Reality realization now has both its dims (T1) and its values (this) derived.

Scope guard (STRICT): T4 of the plan only — T5 (assembly + F = framework-τ
residual, the functorial provenance itself) remains THE open wall; nothing
here inhabits `ArchimedeanTauRealization` with provenance. No fit (all
identities exact); no 8π; nothing wired; `1/(8π)` stays phase-4.

Self-contained (sympy + mpmath + corpus y_lambda_at).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp
import sympy as sp

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_here))
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def y2_closed(s):
    return (s ** 3 + s ** 2 + 1) / ((s ** 2 + 1) * (s ** 4 + 1))


def y11_closed(s):
    return s ** 3 * (s ** 3 + s - 1) / ((s ** 2 + 1) * (s ** 4 + 1))


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # 0. closed forms == corpus canonical y_lambda_at (symbolic, exact)
    ys = y_lambda_at(2)
    qs = sp.Symbol('q', positive=True)
    y2_corpus = list(ys[(2,)].free_symbols)
    subs_var = y2_corpus[0]
    s = sp.sqrt(qs)
    d2 = sp.simplify(ys[(2,)].subs(subs_var, qs) - y2_closed(s))
    d11 = sp.simplify(ys[(1, 1)].subs(list(ys[(1, 1)].free_symbols)[0], qs) - y11_closed(s))
    check("closed_forms_equal_corpus_y_lambda",
          d2 == 0 and d11 == 0,
          f"y_[2] − closed = {d2}; y_[1,1] − closed = {d11} (symbolic zero, s=√q)")

    # 0b. normalization: y2 + y11 = 1 identically
    ss = sp.Symbol('s', positive=True)
    tot = sp.simplify(y2_closed(ss) + y11_closed(ss) - 1)
    check("weights_normalized", tot == 0, f"y_[2]+y_[1,1]−1 = {tot}")

    # 1. VALUE IDENTITY at the classical point: (¾,¼) = CW dims (3,1)/4
    v2, v11 = y2_closed(sp.Integer(1)), y11_closed(sp.Integer(1))
    check("values_at_one_are_cw_dim_fractions",
          v2 == sp.Rational(3, 4) and v11 == sp.Rational(1, 4),
          f"y_[2](1) = {v2} = 3/4 (moving dim 3 / g=4); y_[1,1](1) = {v11} = 1/4 "
          "(invariant dim 1 / g=4) — T1 Chevalley–Weil dims transported to values")

    # 2. THE ANCHOR IS FORCED: factorization + positivity ⇒ unique s>0 solution
    lhs = 4 * (ss ** 3 + ss ** 2 + 1) - 3 * (ss ** 2 + 1) * (ss ** 4 + 1)
    fact = -(ss - 1) * (3 * ss ** 5 + 3 * ss ** 4 + 6 * ss ** 3 + 2 * ss ** 2 + ss + 1)
    ok_fact = sp.expand(lhs - fact) == 0
    # strict positivity of the quintic cofactor on s > 0: all coefficients > 0
    quintic = sp.Poly(3 * ss ** 5 + 3 * ss ** 4 + 6 * ss ** 3 + 2 * ss ** 2 + ss + 1, ss)
    ok_pos = all(c > 0 for c in quintic.all_coeffs())
    # numeric confirmation: no other crossing on a wide grid
    grid_ok = all(abs(float(y2_closed(mp.mpf(x))) - 0.75) > 1e-6
                  for x in [0.05, 0.3, 0.7, 0.9, 1.1, 1.5, 3.0, 10.0])
    check("anchor_q1_forced_unique",
          ok_fact and ok_pos and grid_ok,
          "4·num − 3·den = −(s−1)·(3s⁵+3s⁴+6s³+2s²+s+1); quintic has all-positive "
          "coefficients ⇒ y_[2](s)=3/4 has s=1 as its ONLY positive solution "
          "(grid-confirmed) — the transport anchor is derived, not chosen")

    # 3. SINGULAR AT THE MONODROMY POINT: denominator (q+1)(q²+1) = 0 at q = i
    qc = sp.Symbol('q')
    den_q = qc ** 3 + qc ** 2 + qc + 1
    at_i = sp.simplify(den_q.subs(qc, sp.I))
    fact_q = sp.factor(den_q)
    check("weights_singular_at_monodromy_q_i",
          at_i == 0 and sp.expand(fact_q - (qc + 1) * (qc ** 2 + 1)) == 0,
          f"q³+q²+q+1 = (q+1)(q²+1) → 0 at q=i (T2 Hecke point): the Markov weights "
          "have a pole exactly at the monodromy evaluation — value transport is "
          "anchored at q=1, module structure at q=i; complementary, never interchangeable")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "T4 WEIGHT-VALUE TRANSPORT — DERIVED (scope-(a) within the F-construction plan; "
        "T5 stays the wall): the canonical H₂ Jones–Markov weights equal the T1 "
        "Chevalley–Weil dimension fractions (¾,¼) = (3,1)/4 EXACTLY at q=1; the anchor "
        "q=1 is the unique positive matching point (factorization + positivity — forced, "
        "not chosen); and the weights are singular at the T2 monodromy point q=i, so the "
        "value leg and the module leg are structurally complementary. The #3999 premise "
        "now has dims (T1) AND values (T4) derived. Nothing inhabits the target spec "
        "with provenance — T5 (F = framework-τ) remains open. No fit; no 8π; nothing "
        "wired; 1/(8π) stays phase-4."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    def _sha():
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not out:
            raise RuntimeError("empty commitSha")
        return out

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "alpha-em-f-t4-weight-value-transport",
        "description": "F-construction T4: the canonical H₂ Jones–Markov weight VALUES "
                       "(¾,¼) equal the T1 Chevalley–Weil dims (3,1)/4 exactly at q=1; "
                       "the anchor q=1 is forced (unique positive matching point, "
                       "factorization + positivity); the weights are singular at the T2 "
                       "monodromy point q=i ((q+1)(q²+1) pole). Dims (T1) + values (T4) "
                       "of the #3999 premise both derived; T5 assembly remains the wall. "
                       "No fit; no 8π; nothing wired.",
        "auditOnly": "docs/audits/2026-07-19-alpha-em-f-t4-weight-value-transport.md",
        "tier": "symbolic-exact (sympy identities + factorization; corpus y_lambda_at "
                "cross-check) — Lean sibling QOU/Archimedean/MarkovWeightValueTransport.lean",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy+mpmath",
        "engineVersion": sp.__version__ + "/" + mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "y2_at_1": "3/4", "y11_at_1": "1/4",
            "cw_dims": [3, 1], "genus": 4,
            "anchor": "q = 1 (unique positive matching point — forced)",
            "monodromy_pole": "q = i, denominator (q+1)(q^2+1)",
            "verdict": verdict,
        },
        "context": {
            "plan": "milestone qou-a46k: T1 #4039 (dims), T2 #4040 (module at q=i), "
                    "T3 merged (rho-equivariance), T4 THIS (values), T5 open (assembly)",
            "scope_guard": "T5 functorial provenance untouched — nothing inhabits "
                           "ArchimedeanTauRealization with provenance; no fit; no 8π; "
                           "nothing wired; no tier change",
        },
    }
    out = os.path.join(_here, "alpha-em-f-t4-weight-value-transport.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
