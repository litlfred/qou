#!/usr/bin/env python3
"""Δ_λ parity exclusion: any conjugation-symmetric dressing Δ_λ = Δ_{λ'} gives ZERO bar-even binding,
so it cannot produce the deuteron's g₂ ≈ 1. Verified numerically against the derived H₆ characters;
Lean-proved backbone. A scope-(b) exclusion that narrows the Δ_λ search. Forward, no fit.

CHAIN (read first):
  * #4387: the deuteron binding B = m_e Σ_{λ⊢6} T_λ Δ_λ (T_λ = w_λ χ^λ) has a SIGNED conjugation
    parity — under the physical bar q↦q⁻¹, T_λ(q⁻¹) = (−1)^{n-1} T_{λ'}(q) (= −T_{λ'}(q) for n=6).
  * The bar-even total (carrying g₂) is B(q) + sgn·(bar image); for the deuteron sgn = −1 it equals
    ½ Σ_λ T_λ (Δ_λ − Δ_{λ'}) — the conjugate-pair ASYMMETRIES.

THE EXCLUSION (Lean ConjugationSymmetricDeltaExcluded.barEvenTotal_symmetric_zero_deuteron):
  If Δ_λ = Δ_{λ'} for all λ (conjugation-symmetric), the bar-even total VANISHES ⇒ g₂ = 0. Since the
  deuteron's g₂ ≈ 1 ≠ 0, NO conjugation-symmetric Δ_λ can produce the bar-even binding. scope-(b):
  the proved invariant is "conjugation symmetry ⇒ zero bar-even".

WHAT THIS PROBE VERIFIES (30 dps against the committed derived caches; no fit):
  A. CANDIDATE CLASSIFICATION. The natural Δ_λ families split by conjugation symmetry:
       EXCLUDED (symmetric):  Markov weight w_λ=(q−q⁻¹)^5/∏[hook]_q; classical dim(λ)²; hook-form
                              q-dimension [n]_q!/∏[hook]_q — all symmetric (hook multiset is transpose-
                              invariant) ⇒ bar-even total = 0.
       SURVIVES (covariant):  the Wenzl PRINCIPAL SPECIALIZATION s_λ(1,q,q²,…) — asymmetric via the
                              content power q^{n(λ)} (n(6)=0 vs n(1⁶)=15) ⇒ bar-even total ≠ 0.
  B. NUMERIC CONFIRMATION. bar-even total B(q₀)+B(q₀⁻¹): for Δ=w_λ it is ~1e-39 (= 0); for
     Δ=q^{n(λ)} it is −8.8e-5 (≠ 0). The exclusion and the survivor both check out.

CONVERGENCE (not fishing). The exclusion INDEPENDENTLY selects the conjugation-covariant principal
specialization — exactly the weight the s5-so3 keystone (docs/coordination/s5-so3-keystone.md)
identified as the production trace weight (Wenzl principal specialization, not the q-Plancherel /
Markov weight). Two independent routes agree on the weight *class*; neither fixes the Δ_λ magnitudes.

SCOPE (honest, scope-(b)): DERIVED — a structural exclusion (symmetric Δ_λ out; covariant class in),
narrowing the Δ_λ search via a proved invariant. NOT derived — the Δ_λ magnitudes themselves (still
the Track-A gate). No fit; nothing wired.

EXPLORATORY — audit + witness only.
"""
from __future__ import annotations

import json
import sys
from math import factorial, prod
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
PARTS = [(6,), (5, 1), (4, 2), (4, 1, 1), (3, 3), (3, 2, 1),
         (3, 1, 1, 1), (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)]


def conj(p):
    m = max(p)
    return tuple(sum(1 for x in p if x >= k) for k in range(1, m + 1))


def hooks(p):
    pc = conj(p)
    return [(row - j - 1) + (pc[j] - i - 1) + 1 for i, row in enumerate(p) for j in range(row)]


def nlam(p):
    return sum(i * part for i, part in enumerate(p))     # n(λ) = Σ (i−1) λ_i (0-indexed)


def main() -> int:
    # Source q₀ from the SAME pinning the character caches were computed at (its `q_str`), so q₀ and
    # χ^λ(q₀) can never drift apart. (NOT qou_substrate.q_at / Q_50_DIGIT_STR: a ~11.7 ppb different
    # pin — muon↔proton — which would break consistency with these caches.)
    _q0cache = json.load(open(_COMP / 'chi-deuteron-free-h6-at-q0-50dps.witness.json'))
    q0 = mp.mpf(_q0cache['q_str'])
    qi = 1 / q0

    def qn(x, n):
        return (x ** n - x ** (-n)) / (x - 1 / x)

    def w(x, p):
        den = mp.mpf(1)
        for hh in hooks(p):
            den *= qn(x, hh)
        return (x - 1 / x) ** (sum(p) - 1) / den

    def dimq_hook(p):
        num = mp.mpf(1)
        for k in range(1, sum(p) + 1):
            num *= qn(q0, k)
        den = mp.mpf(1)
        for hh in hooks(p):
            den *= qn(q0, hh)
        return num / den

    c0 = {tuple(r['partition']): mp.mpf(r['chi_lambda']) for r in _q0cache['by_partition']}
    ci = {tuple(r['partition']): mp.mpf(r['chi_lambda'])
          for r in json.load(open(_COMP / 'chi-deuteron-free-h6-at-qinv-50dps.witness.json'))['by_partition']}
    T0 = {p: w(q0, p) * c0[p] for p in PARTS}
    Ti = {p: w(qi, p) * ci[p] for p in PARTS}

    tol = mp.mpf('1e-20')

    families = {
        "Markov w_λ = (q−q⁻¹)^5/∏[hook]": lambda p: w(q0, p),
        "classical dim(λ)²": lambda p: mp.mpf(factorial(sum(p)) // prod(hooks(p))) ** 2,
        "hook-form q-dim [n]_q!/∏[hook]": dimq_hook,
        "principal-spec q^{n(λ)} (covariant)": lambda p: q0 ** nlam(p),
    }

    def bar_even_total(delta):
        return sum((T0[p] + Ti[p]) * delta(p) for p in PARTS)

    classification = {}
    for name, f in families.items():
        symmetric = all(abs(f(p) - f(conj(p))) < tol for p in PARTS)
        be = bar_even_total(f)
        classification[name] = {
            "conjugation_symmetric": bool(symmetric),
            "bar_even_total": mp.nstr(be, 6),
            "verdict": "EXCLUDED (bar-even = 0)" if symmetric else "SURVIVES (bar-even ≠ 0)",
        }

    excluded_zero = all(
        abs(bar_even_total(f)) < mp.mpf('1e-30')
        for name, f in families.items()
        if all(abs(f(p) - f(conj(p))) < tol for p in PARTS)
    )
    ps_survives = abs(bar_even_total(families["principal-spec q^{n(λ)} (covariant)"])) > mp.mpf('1e-8')

    result = {
        "exclusion": {
            "statement": "conjugation-symmetric Δ_λ = Δ_{λ'} ⇒ bar-even total = 0 ⇒ g₂ = 0; since "
                         "g₂ ≈ 1 ≠ 0, no symmetric Δ_λ can produce the bar-even binding.",
            "lean": "ConjugationSymmetricDeltaExcluded.barEvenTotal_symmetric_zero_deuteron (sorry-free)",
            "scope": "(b) — proved invariant: conjugation symmetry ⇒ zero bar-even.",
        },
        "candidate_classification": classification,
        "numeric_confirmation": {
            "all_symmetric_families_bar_even_zero": bool(excluded_zero),
            "principal_specialization_survives": bool(ps_survives),
            "n_lambda_examples": {"(6)": nlam((6,)), "(1^6)": nlam((1, 1, 1, 1, 1, 1)),
                                  "(3,2,1)": nlam((3, 2, 1))},
        },
        "convergence": {
            "note": "the exclusion independently selects the conjugation-covariant principal "
                    "specialization — the weight the s5-so3 keystone identified as the production "
                    "trace weight (Wenzl principal spec, not q-Plancherel/Markov). Two routes agree "
                    "on the weight CLASS; neither fixes the Δ_λ magnitudes.",
            "keystone_ref": "docs/coordination/s5-so3-keystone.md",
        },
        "scope": {
            "derived": "a structural exclusion narrowing the Δ_λ search (symmetric families out; "
                       "covariant class in).",
            "not_derived": "the Δ_λ magnitudes (Track-A gate).",
            "no_fit": True,
        },
    }

    payload = {
        "computation": "deltalambda-conjugation-symmetric-excluded",
        "description": ("Δ_λ parity exclusion: any conjugation-symmetric dressing Δ_λ=Δ_{λ'} gives ZERO "
                        "bar-even binding (Lean-proved barEvenTotal_symmetric_zero_deuteron), so it "
                        "cannot produce the deuteron's g₂≈1 — a scope-(b) exclusion. Verified 30 dps "
                        "against the derived H₆ characters: the Markov weight w_λ, classical dim(λ)², "
                        "and hook-form q-dimension are all conjugation-symmetric (hook multiset "
                        "transpose-invariant) ⇒ bar-even total ~1e-39 (=0) ⇒ EXCLUDED; the "
                        "conjugation-covariant Wenzl principal specialization q^{n(λ)} (n(6)=0 vs "
                        "n(1⁶)=15) gives bar-even total −8.8e-5 (≠0) ⇒ SURVIVES. The exclusion "
                        "independently selects the principal specialization — the weight the s5-so3 "
                        "keystone identified as the production trace weight (convergence, not fishing). "
                        "DERIVED: the exclusion (narrows the search); NOT derived: the Δ_λ magnitudes "
                        "(Track-A gate). scope-(b), audit-only, nothing wired; no fit."),
        "audit_only": True,
        "tier": "scope-(b) structural exclusion (Lean-proved) + 30-dps candidate classification; no fit",
        "result": result,
        "context": {
            "axis": "Δ_λ binding — μ₀ −9% closure, parity exclusion narrowing the Δ_λ search",
            "lean": "QOU/MassTheory/ConjugationSymmetricDeltaExcluded.lean",
            "builds_on": "#4387 (signed conjugation parity), s5-so3-keystone.md (principal-spec weight)",
            "q0_convention": "muon-canonical (computations/ layer)",
            "no_fit": True,
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "deltalambda-conjugation-symmetric-excluded", payload,
        script_path=__file__, engine="mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("symmetric_families_bar_even_zero", computed=str(bool(excluded_zero)), expected="True")
    wb.add_assertion("principal_spec_survives", computed=str(bool(ps_survives)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Δ_λ parity exclusion: conjugation-symmetric Δ_λ ⇒ g₂ = 0 ===")
    for name, c in classification.items():
        print(f"  {name:38s} sym={c['conjugation_symmetric']!s:5s} bar-even={c['bar_even_total']:>12s}  {c['verdict']}")
    print(f"all symmetric families bar-even = 0: {excluded_zero}   principal-spec survives: {ps_survives}")
    print("⇒ symmetric Δ_λ (Markov/dim²/hook-q-dim) EXCLUDED; conjugation-covariant principal "
          "specialization SURVIVES (converges with the s5-so3 keystone weight).")
    print("SCOPE-(b): narrows the Δ_λ search; the Δ_λ magnitudes remain the Track-A gate. No fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
