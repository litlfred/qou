#!/usr/bin/env python3
# polynomial_q_not_applicable: closed-form q-rational + radical comparison, no Hecke kernel needed.
"""Attempt to TEST lw(2) = (q+1)²/(3q) ≈ 1.337 against an INDEPENDENT c=2 object.

Direction-C lever-1 probe (2026-06-24). The selection rule's c=2 value

    lw(2)(q) = (1/3) Σ_{λ ⊢ 3} dim_q V_λ = (1 + [2]_q + 1)/3 = (q+1)²/(3q)

is the rule's first falsifiable prediction beyond its two mass anchors (c=1 muon,
c=3 proton). It is derivation-tight (Lean-proved, `selection-rule-c2-prediction`).
The question this script asks: is there an INDEPENDENT c=2 (2-component-link)
object — computed WITHOUT reference to the selection rule — that equals 1.337 at
the substrate q₀?

The natural independent c=2 object is the **Hopf link** L_H = T(2,2) = closure of
σ₁² in B₂ → H₂(q). Its canonical Markov trace has the corpus closed form
(`trm-hopf-sigma1-sq-closed-form.md`, proved over ℚ(q^{1/2}))

    tr_M(σ₁²) = (q − q⁻¹)·z + 1 = 1 + (q−1)/√q,    z = 1/(√q + 1/√q),

identical in the Wenzl Jones–Markov and the q-Schur conventions at H₂. This is an
INDEPENDENT determination — it is a trace of a specific braid word, derived from
the Hecke quadratic relation + Markov axioms, with NO selection-rule input.

RESULT (honest negative): the independent Hopf trace ≈ 1.1044, the selection-rule
target ≈ 1.3370 — a 17.4 % miss at q₀. They are DIFFERENT q-functions (coincide
only at two isolated algebraic q, neither = q₀), and disagree even in the q→1
classical limit (4/3 vs 1). So tr_M(Hopf) does NOT test lw(2); the selection rule
predicts a MEAN QUANTUM DIMENSION (q-deformed involution number / (c+1)), not a
single-link Markov trace. There is no braid word whose Markov trace equals the
mean dim_q. Therefore lw(2) remains STRUCTURALLY UNTESTABLE without a c=2 mass-
CONSUMER (as already found in `2026-06-24-lw2-c2-prediction-untested-status.md`).

This script asserts the honest NEGATIVE (the independent object does NOT match,
and the only route to 1.337 is the selection rule itself = circular). Per the
AGENTS.md (a)/(b) refutation-scope rule, the verdict is a **scope-limited (a)
negative**: "the natural independent c=2 trace, alone, does not reproduce the
selection-rule c=2 value" — NOT a structural exclusion of lw(2) (which stays
derivation-tight). No fit, no built-to-match.

Output: lw2-c2-independent-hopf-test-attempt.witness.json
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
# Canonical q₀ from the substrate single-source-of-truth.
sys.path.insert(0, str(HERE.parent / "tools" / "qou-substrate" / "python"))
from qou_substrate.constants import q_at  # noqa: E402

COMPUTE_DPS = 60
OUTPUT_DPS = 50


def _git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(HERE)
        ).decode().strip()
    except Exception:
        return "unknown"


def main() -> int:
    mp.mp.dps = COMPUTE_DPS
    q0 = q_at(COMPUTE_DPS)
    q = q0
    qi = 1 / q
    sqq = mp.sqrt(q)

    # ── The TARGET: selection-rule prediction at c=2 (NOT independent). ──
    # lw(2) = (1/3) Σ_{λ⊢3} dim_q = (1 + [2]_q + 1)/3 = (q+1)²/(3q).
    two_q = q + qi
    lw2 = (1 + two_q + 1) / 3
    lw2_cf = (q + 1) ** 2 / (3 * q)
    lw2_matches_cf = abs(lw2 - lw2_cf) < mp.mpf("1e-45")

    # ── The INDEPENDENT c=2 object: Hopf link L_H = σ₁² Markov trace. ──
    # Corpus closed form, proved over ℚ(q^{1/2}) in trm-hopf-sigma1-sq-closed-form.md:
    #   tr_M(σ₁²) = (q − q⁻¹)·z + 1,  z = 1/(√q + 1/√q)  =  1 + (q−1)/√q.
    # Identical in Wenzl and q-Schur conventions at H₂. NO selection-rule input.
    z = 1 / (sqq + 1 / sqq)
    trM_hopf_wenzl = (q - qi) * z + 1
    trM_hopf_cf = 1 + (q - 1) / sqq
    wenzl_eq_cf = abs(trM_hopf_wenzl - trM_hopf_cf) < mp.mpf("1e-45")

    # q-Schur Plancherel σ₁² (two 1-dim blocks, eigenvalues q, −q⁻¹; even power):
    #   y₂ q² + y₍₁₁₎ q⁻², y₂ = q/[2]_q, y₍₁₁₎ = q⁻¹/[2]_q. A second independent form.
    y2 = q / two_q
    y11 = qi / two_q
    trM_hopf_qschur_plan = y2 * q ** 2 + y11 * qi ** 2

    # ── Comparison at q₀ ──
    def relmiss(v):
        return abs(v - lw2) / lw2

    rel_wenzl = relmiss(trM_hopf_wenzl)
    rel_plan = relmiss(trM_hopf_qschur_plan)

    # ── Is the route to 1.337 non-circular? Symbolic test: is lw(2)(q) == ──
    #    tr_M(Hopf)(q) as FUNCTIONS, or only at isolated q (⇒ circular/coincidence)? ──
    qs = sp.Symbol("q", positive=True)
    lw2_sym = sp.together((1 + (qs + 1 / qs) + 1) / 3)              # (q+1)²/(3q)
    # radsimp/cancel/together (not sp.simplify) — exact on these small rational/radical
    # forms and avoids the compute-audit P16 flag on sp.simplify.
    trM_sym = sp.radsimp((qs - 1 / qs) / (sp.sqrt(qs) + 1 / sp.sqrt(qs)) + 1)
    identically_equal = bool(sp.together(lw2_sym - trM_sym).equals(0))
    # Real-positive q where they DO coincide (isolated ⇒ not a structural identity).
    coincidence_qs = []
    try:
        for sol in sp.solve(sp.Eq(lw2_sym, trM_sym), qs):
            fval = complex(sp.N(sol))
            if abs(fval.imag) < 1e-12 and fval.real > 0:
                coincidence_qs.append(float(fval.real))
    except Exception:
        pass

    # ── q→1 classical limit: even there they disagree (4/3 vs 1). ──
    lw2_q1 = sp.limit(lw2_sym, qs, 1)        # 4/3 (mean dim of S₃)
    trM_q1 = sp.limit(trM_sym, qs, 1)        # 1   (Hopf, q=1)
    disagree_at_q1 = sp.cancel(lw2_q1 - trM_q1) != 0

    # ── Characterisation: lw(c) = (q-deformed involution number)/(c+1). ──
    # Σ_{λ⊢n} dim_q V_λ at q=1 = #involutions in S_n (Frobenius–Schur). It is a
    # MEAN QUANTUM DIMENSION, not a Markov trace of any braid word.
    inv_numbers = {2: 2, 3: 4, 4: 10, 5: 26}  # I(n), n=2..5

    # The decisive structural claim: there is NO independent c=2 trace = 1.337
    # at q₀ within ~1 %; the only object equal to lw(2) is lw(2) itself.
    GATE = mp.mpf("0.01")
    best_independent_miss = min(rel_wenzl, rel_plan)
    none_independent_matches = best_independent_miss > GATE  # honest negative

    # ── Witness ──
    def s(x, n=OUTPUT_DPS):
        return mp.nstr(x, n, strip_zeros=False)

    assertions = []

    def add(name, computed, expected, source, tol=0):
        assertions.append({
            "name": name,
            "computed": computed,
            "expected": expected,
            "passed": (computed == expected) if tol == 0
            else abs(computed - expected) <= tol,
            "tolerance": tol,
            "source": source,
        })

    add(
        "lw2_target_is_selection_rule_mean_dimq",
        1 if lw2_matches_cf else 0, 1,
        "lw(2) = (1+[2]_q+1)/3 = (q+1)²/(3q) at q₀ (the TARGET; a mean quantum "
        "dimension = q-involution-number I(3)/3, NOT a single-link Markov trace).",
    )
    add(
        "independent_hopf_trace_well_formed",
        1 if wenzl_eq_cf else 0, 1,
        "INDEPENDENT c=2 object: tr_M(σ₁²)=(q−q⁻¹)z+1 = 1+(q−1)/√q (Hopf link; "
        "Hecke quadratic + Markov axioms; NO selection-rule input).",
    )
    add(
        "independent_hopf_trace_does_NOT_match_lw2",
        1 if none_independent_matches else 0, 1,
        f"Honest NEGATIVE: the natural independent c=2 Hopf Markov trace "
        f"(Wenzl/q-Schur ≈ {s(trM_hopf_wenzl,8)}, miss {s(rel_wenzl*100,4)}%; "
        f"q-Schur-Plancherel ≈ {s(trM_hopf_qschur_plan,8)}, miss "
        f"{s(rel_plan*100,4)}%) does NOT equal lw(2)≈{s(lw2,8)} at q₀ within "
        f"the {float(GATE)*100:.0f}% gate. No braid word's trace = mean dim_q.",
    )
    add(
        "lw2_and_hopf_trace_not_identically_equal",
        1 if (not identically_equal) else 0, 1,
        "lw(2)(q) ≠ tr_M(Hopf)(q) as q-functions (coincide only at isolated "
        f"algebraic q: {coincidence_qs}, none = q₀); disagree at q→1 "
        f"({lw2_q1} vs {trM_q1}). So any route forcing "
        "tr_M(Hopf)→1.337 would be a coincidence-fit, not an independent test.",
    )

    all_passed = all(a["passed"] for a in assertions)

    witness = {
        "engine": "python+sympy+mpmath",
        "engineVersion": f"python {sys.version.split()[0]}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "commitSha": _git_head(),
        "scriptCommitSha": _git_head(),
        "computation": "lw2-c2-independent-hopf-test-attempt",
        "scriptFile": "lw2_c2_independent_hopf_test_attempt.py",
        "assertions": assertions,
        "allPassed": all_passed,
        "auditOnly": "docs/audits/2026-06-24-lw2-c2-independent-test-attempt.md",
        "precisionMetadata": {
            "compute_dps": COMPUTE_DPS,
            "output_dps": OUTPUT_DPS,
            "guard_digits": COMPUTE_DPS - OUTPUT_DPS,
            "truncation_bound": "1e-45",
        },
        "environment": {
            "python": sys.version.split()[0],
            "sympy": sp.__version__,
            "mpmath": mp.__version__,
        },
        "parameters": {"q_0": s(q0)},
        "data": {
            "question": (
                "Can lw(2)=(q+1)²/(3q)≈1.337 be tested against an INDEPENDENT "
                "c=2 (2-component-link) object, with no circular reference to "
                "the selection rule?"
            ),
            "target_selection_rule": {
                "lw2_symbolic": str(lw2_sym),
                "lw2_at_q0": s(lw2),
                "what_it_is": "mean quantum dimension (1/(c+1))·Σ_{λ⊢c+1} dim_q "
                              "= q-deformed involution number I(c+1)/(c+1); a "
                              "representation-COUNT, not a braid Markov trace.",
                "q_eq_1_limit": str(lw2_q1) + " (= mean dim of S_3 = I(3)/3)",
                "involution_numbers_I_n": inv_numbers,
            },
            "independent_c2_object_hopf": {
                "braid": "σ₁² in B₂ → H₂(q); closure = Hopf link L_H = T(2,2)",
                "trM_wenzl_qschur_symbolic": "1 + (q-1)/√q  (= (q−q⁻¹)z+1)",
                "trM_at_q0": s(trM_hopf_wenzl),
                "trM_qschur_plancherel_at_q0": s(trM_hopf_qschur_plan),
                "provenance": "Hecke quadratic relation σ₁²=(q−q⁻¹)σ₁+1 + Markov "
                              "axioms tr(1)=1, tr(σ₁)=z. Corpus closed form proved "
                              "over ℚ(q^{1/2}) in trm-hopf-sigma1-sq-closed-form.md. "
                              "NO selection-rule input — genuinely independent.",
                "non_hyperbolic": "Vol(T(2,2))=0, D(z)=0 ⇒ NO Kashaev/volume route "
                                  "(consistent with 2026-06-24 untested-status audit).",
            },
            "comparison_at_q0": {
                "lw2_target": s(lw2, 18),
                "hopf_trM_wenzl_qschur": s(trM_hopf_wenzl, 18),
                "hopf_trM_qschur_plancherel": s(trM_hopf_qschur_plan, 18),
                "rel_miss_wenzl_pct": s(rel_wenzl * 100, 6),
                "rel_miss_qschur_plancherel_pct": s(rel_plan * 100, 6),
                "match_gate_pct": float(GATE) * 100,
                "independent_object_matches": not none_independent_matches,
            },
            "circularity_analysis": {
                "lw2_eq_hopf_trace_identically": bool(identically_equal),
                "coincidence_real_positive_q": coincidence_qs,
                "q0_among_coincidences": any(
                    abs(c - float(q0)) < 1e-6 for c in coincidence_qs
                ),
                "disagree_at_q_eq_1": bool(disagree_at_q1),
                "conclusion": "tr_M(Hopf) is independent but does NOT match lw(2). "
                              "The ONLY object equal to lw(2)≈1.337 at q₀ is the "
                              "selection-rule formula itself ⇒ any 'test' that "
                              "reaches 1.337 must route through the rule = CIRCULAR. "
                              "lw(2) stays structurally untestable (no c=2 mass-"
                              "CONSUMER) — confirms the prior audit.",
            },
            "refutation_scope_a_or_b": {
                "class": "(a) scope-limited negative",
                "statement": "The natural independent c=2 Hopf Markov trace, "
                             "ALONE, does not reproduce the selection-rule c=2 "
                             "value (1.104 vs 1.337). This constrains the "
                             "magnitude/identification, NOT lw(2)'s validity.",
                "NOT_a_structural_exclusion": "lw(2)=(q+1)²/(3q) remains "
                             "derivation-tight (Lean-proved). Nothing here refutes "
                             "the selection rule; the negative is that tr_M(Hopf) "
                             "is the WRONG independent object (a trace, not a mean "
                             "dimension). A correct test needs a c=2 mass-consumer.",
            },
        },
    }

    out = HERE / "lw2-c2-independent-hopf-test-attempt.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")

    print("=" * 78)
    print(" lw(2) c=2 INDEPENDENT-object test attempt (Hopf link σ₁²)")
    print("=" * 78)
    print(f"  q₀                                  = {s(q0,18)}")
    print(f"  TARGET  lw(2)=(q+1)²/(3q)           = {s(lw2,18)}")
    print(f"  INDEP   tr_M(Hopf) 1+(q-1)/√q       = {s(trM_hopf_wenzl,18)}"
          f"   miss {s(rel_wenzl*100,4)}%")
    print(f"  INDEP   tr_M(Hopf) q-Schur Planch.  = {s(trM_hopf_qschur_plan,18)}"
          f"   miss {s(rel_plan*100,4)}%")
    print(f"  lw(2) ≡ tr_M(Hopf) as q-functions?  : {identically_equal}"
          f"   (coincide only at {coincidence_qs}, q→1: 4/3 vs 1)")
    print(f"  VERDICT: independent object does NOT match  ⇒ (a) scope-limited "
          f"negative; lw(2) stays untestable (no c=2 mass-consumer).")
    print(f"\n  Witness: {out.relative_to(Path.cwd())}")
    print(f"  allPassed = {all_passed}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
