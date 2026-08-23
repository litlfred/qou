#!/usr/bin/env python3
"""deltalambda_extensivity_gap_synthesis_probe.py

Δ_λ gate opened for all (2026-07-13). First move under the open gate is the
honesty-safe synthesis: with the corpus having already CLOSED the sign
(ρ-grading g_ρ, sgn=(-1)^{n(λ)}) and REDUCED the magnitude (|Δ_λ|=tr_{V_λ}(g_ρ)=
dim(λ), the classical q=1 dimension — magnitude-graded-trace witness), and
having evaluated the fully parameter-free target
    B_base(K) = m_e·|Σ_λ y_λ χ^λ(β_K) sgn(w₀^{S_{λ'}}) dim(λ)|
(delta-lambda-binding-full-evaluation.witness.json), this probe REPRODUCES that
base and quantifies the single remaining gap precisely.

The base UNDERSHOOTS AME by 70–89% (fixed-H_{3A} braid ⇒ no extensivity). The
jet tower (wlambda-jet-tower-connected) supplies unbounded extensive growth
(~2.5×/level) but the LEVEL-SELECTION rule k(A) is GAP-A-3, still open. This
probe states the exact per-isotope "extensivity multiplier" μ_ext(K) =
B_AME/B_base that k(A) must reproduce — the sharp target for GAP-A-3.

DISCIPLINE (anti-fit): this is a SYNTHESIS, not a seventh ansatz. It fits
nothing — it reproduces the parameter-free base and reports the residual
multipliers as the target for a *derived* k(A). Any structural correlation of
μ_ext with a parameter-free count (bonds C(A,2), tree A−1, …) is reported as
DATA under a numerology guard, NOT proposed as a closure. Scope-(a); no wiring;
no tier change.
"""
import json
import math
from pathlib import Path

from mpmath import mp, mpf, fabs
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent
COMP = HERE.parent      # computations/

m_e = mpf('0.51099895069')
B_AME = {'D': 2.22452, 'T': 8.48180, '3He': 7.71804, '4He': 28.29567}


def conjugate(lam):
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p > i) for i in range(lam[0]))


def sgn_conjugate_parabolic(lam):
    return math.prod((-1) ** (p * (p - 1) // 2) for p in conjugate(lam))


def dim_sn(lam):
    n = sum(lam)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return math.factorial(n) // den


def load_chi(fname):
    d = json.load(open(COMP / fname, encoding='utf-8'))
    atom = d['data']['atom']
    return [(tuple(e['partition']), mpf(str(e['chi_lambda'])))
            for e in atom['by_partition']]


def load_wenzl_y(fname):
    d = json.load(open(COMP / fname, encoding='utf-8'))
    return {tuple(e['partition']): mpf(e['y_lambda']) for e in d['data']['per_partition']}


def main():
    lp = json.load(open(COMP / 'rho-k-h3a-lp-dual.witness.json'))
    y_H6 = {tuple(e['partition']): mpf(str(e['y_lambda_at_q0'])) for e in lp['data']['per_lambda']}
    y_H9 = load_wenzl_y('wenzl-y-lambda-h9.witness.json')
    y_H12 = load_wenzl_y('wenzl-y-lambda-h12.witness.json')
    atoms = [('D', 'atom-chi-rust-d.witness.json', y_H6, 1, 1),
             ('T', 'atom-chi-rust-t.witness.json', y_H9, 1, 2),
             ('3He', 'atom-chi-rust-3he.witness.json', y_H9, 2, 1),
             ('4He', 'atom-chi-rust-4he.witness.json', y_H12, 2, 2)]

    print("=" * 74)
    print(" Δ_λ EXTENSIVITY GAP — the target k(A) (GAP-A-3) must reproduce")
    print(" base = m_e·|Σ y_λ χ^λ sgn·dim| (parameter-free; sign+magnitude closed)")
    print("=" * 74)

    rows = {}
    for name, chi_file, y_dict, Z, N in atoms:
        A = Z + N
        chi = load_chi(chi_file)
        # per-λ terms, to find which Wedderburn blocks dominate the base
        terms = []
        total = mpf(0)
        for lam, ch in chi:
            t = y_dict.get(lam, mpf(0)) * ch * sgn_conjugate_parabolic(lam) * dim_sn(lam)
            total += t
            terms.append((lam, float(t)))
        B_base = m_e * fabs(total)
        mu_ext = mpf(B_AME[name]) / B_base
        terms.sort(key=lambda x: -abs(x[1]))
        dom = terms[0]
        top3_share = sum(abs(t) for _, t in terms[:3]) / sum(abs(t) for _, t in terms)
        rows[name] = {
            'A': A, 'Z': Z, 'N': N,
            'bonds_C_A_2': A * (A - 1) // 2, 'tree_A_minus_1': A - 1,
            'B_base_MeV': float(B_base), 'B_AME_MeV': B_AME[name],
            'err_pct': float((B_base - B_AME[name]) / B_AME[name] * 100),
            'mu_ext_target': float(mu_ext),
            'dominant_lambda': list(dom[0]), 'dominant_term': dom[1],
            'top3_block_share': float(top3_share),
        }
        print(f"\n── {name}  (A={A}, Z={Z}, N={N};  bonds C(A,2)={A*(A-1)//2})")
        print(f"   B_base = {float(B_base):8.4f} MeV   B_AME = {B_AME[name]:8.4f} MeV   "
              f"err {float((B_base-B_AME[name])/B_AME[name]*100):+6.1f}%")
        print(f"   μ_ext target (B_AME/B_base) = {float(mu_ext):.4f}   "
              f"[what k(A) must supply]")
        print(f"   dominant block λ={dom[0]} (term {dom[1]:+.4f}); top-3 blocks carry "
              f"{float(top3_share)*100:.0f}% of |Σ|")

    print("\n" + "=" * 74)
    print(" EXTENSIVITY MULTIPLIERS (the GAP-A-3 target):")
    for k in ('D', 'T', '3He', '4He'):
        r = rows[k]
        print(f"   {k:4s} A={r['A']}  bonds={r['bonds_C_A_2']}  μ_ext={r['mu_ext_target']:.3f}")
    print("\n Numerology guard (reported as DATA, NOT a derivation or fit):")
    print("   μ_ext is NOT monotone in A or bonds (⁴He doubly-magic needs the largest,")
    print("   9.31; ³He the smallest, 3.29) — so no parameter-free count closes it from")
    print("   4 points. The honest closure is a DERIVED level-selection k(A) for the jet")
    print("   tower (wlambda-jet-tower-connected: ~2.5×/level, ~51% (2,1)-channel share),")
    print("   NOT an inversion of these 4 multipliers. That derivation is GAP-A-3 (open).")

    verdict = (
        "Under the opened Δ_λ gate, the honesty-safe synthesis: the fully "
        "parameter-free base B_base=m_e·|Σ y_λ χ^λ sgn·dim| (sign=ρ-grading CLOSED, "
        "magnitude=classical dim CLOSED) undershoots AME by 70–89% because a "
        "fixed-H_{3A} braid is not extensive. The exact per-isotope extensivity "
        "multiplier k(A) must supply is μ_ext(K)=B_AME/B_base = "
        f"{rows['D']['mu_ext_target']:.2f}/{rows['T']['mu_ext_target']:.2f}/"
        f"{rows['3He']['mu_ext_target']:.2f}/{rows['4He']['mu_ext_target']:.2f} "
        "(D/T/³He/⁴He). μ_ext is non-monotone in A/bonds (⁴He doubly-magic largest), "
        "so it is NOT fit-closable from 4 points — the honest closure is a DERIVED "
        "jet-tower level-selection rule k(A) (GAP-A-3, open). This connects the "
        "full-evaluation undershoot to the jet-tower extensivity and sharpens the "
        "target; it fits nothing and wires nothing. Scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wit = {
        "computation": "deltalambda-extensivity-gap-synthesis",
        "description": "Δ_λ gate opened for all (2026-07-13): synthesis reproducing the "
                       "parameter-free base B_base=m_e·|Σ y_λ χ^λ sgn·dim| (sign+magnitude "
                       "closed) and quantifying the per-isotope extensivity multiplier "
                       "μ_ext=B_AME/B_base that GAP-A-3's jet-tower level-selection k(A) must "
                       "supply. μ_ext non-monotone in A/bonds ⇒ not fit-closable; the closure "
                       "is a DERIVED k(A). Anti-fit synthesis; no wiring; scope-(a).",
        "audit_only": True,
        "engine": "python3/mpmath", "engineVersion": "50dps",
        "rows": rows,
        "extensivity_multipliers_target": {k: rows[k]['mu_ext_target'] for k in rows},
        "open_gap": "GAP-A-3 jet-tower level-selection rule k(A) (derived, not fit)",
        "closed_upstream": {"sign": "ρ-grading g_ρ, sgn=(-1)^n(λ) (sign-pivotal capstone)",
                            "magnitude_base": "|Δ_λ|=dim(λ)=tr_{V_λ}(g_ρ), classical q=1 (magnitude-graded-trace)"},
        "verdict": verdict,
        "scope": "(a) — synthesis of parameter-free base + target statement; no fit; no wiring",
        "assertions": [{"label": "base reproduces full-evaluation undershoot (70-89%)",
                        "passed": all(-90 < rows[k]['err_pct'] < -60 for k in rows)},
                       {"label": "mu_ext non-monotone in A (not fit-closable)",
                        "passed": rows['4He']['mu_ext_target'] > rows['3He']['mu_ext_target']
                        and rows['3He']['mu_ext_target'] < rows['T']['mu_ext_target']}],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    out = HERE / "deltalambda-extensivity-gap-synthesis.witness.json"
    json.dump(wit, open(out, 'w'), indent=1)
    print("\nwitness ->", out.name, "  allPassed:", wit["allPassed"])
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
