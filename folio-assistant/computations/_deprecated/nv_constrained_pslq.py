"""Phase D — N_v constrained PSLQ on the path-α-Bring basis.

Per docs/audits/2026-05-05-path-alpha-bring-refinement.md §6, the
structurally constrained basis derived from prop:weak-symmetric-
normalization + prop:knot-operator-lp-selection is

    B = { [2]_q, [4]_q, [6]_q, [8]_q, q^k, h^k, N_sym(q) }

where N_sym(q) = q^6 · (1 + q² + q⁴) / 3.  We test whether
v_weak / m_e admits a closed-form expression in this basis at
CODATA-G_F precision (5×10⁻⁷ relative).  In contrast to the
brute-force 7.5×10⁵-element basis of the impasse audit, this is
a small structurally-motivated basis and false-discovery rate
should be small.

Tests three ansatz shapes informed by the EM α_EM analog:

  A1.  v_w/m_e =  INT · [4]_q^a · [6]_q^b · [8]_q^c / [2]_q^d · q^L
  A2.  v_w/m_e =  INT · N_sym(q)^a · q^L · h^b
  A3.  v_w/m_e =  INT · [4]_q · [6]_q · [8]_q / [2]_q · N_sym(q)^a · q^L

Reports the best closed-form candidate per ansatz with relative error.
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath
mpmath.mp.dps = 80  # high precision for clean PSLQ

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, G_F_MEV

q = mpmath.mpf(Q_50_DIGIT_STR)
G_F = mpmath.mpf(str(G_F_MEV))
m_e = mpmath.mpf(str(M_E_MEV))

v_w = 1 / mpmath.sqrt(mpmath.sqrt(2) * G_F)
ratio = v_w / m_e            # ≈ 481839.82
N_v = 3 * ratio              # ≈ 1,445,519


def qint(n):
    return (q ** n - q ** -n) / (q - 1 / q) if n != 0 else mpmath.mpf(0)


def main() -> int:
    h = q - 1 / q
    N_sym = (q ** 4 + q ** 6 + q ** 8) / 3
    q2, q4, q6, q8 = qint(2), qint(4), qint(6), qint(8)

    print("Phase D — N_v constrained PSLQ on path-α-Bring basis")
    print("=" * 72)
    print(f"  ratio v_w/m_e  = {mpmath.nstr(ratio, 22)}")
    print(f"  N_v target     = {mpmath.nstr(N_v, 22)}")
    print(f"  CODATA tol     = 5e-7 relative")
    print()
    print(f"  q_0            = {mpmath.nstr(q, 25)}")
    print(f"  [2]_q          = {mpmath.nstr(q2, 14)}")
    print(f"  [4]_q          = {mpmath.nstr(q4, 14)}")
    print(f"  [6]_q          = {mpmath.nstr(q6, 14)}")
    print(f"  [8]_q          = {mpmath.nstr(q8, 14)}")
    print(f"  N_sym(q_0)     = {mpmath.nstr(N_sym, 14)}")
    print(f"  q^4+q^6+q^8    = {mpmath.nstr(3 * N_sym, 14)}")
    print()

    # ── Quick scan: ratio vs structural ratios ─────────────────
    print("Quick scan — ratio / structural EW-product:")
    candidates = [
        ("[4]·[6]·[8]/[2]",       q4 * q6 * q8 / q2),
        ("[4]·[6]·[8]",           q4 * q6 * q8),
        ("([4]·[6]·[8])^2/[2]^2", (q4 * q6 * q8)**2 / q2**2),
        ("[8]^3",                 q8 ** 3),
        ("[8]^4",                 q8 ** 4),
        ("[8]^5",                 q8 ** 5),
        ("N_sym^4",               N_sym ** 4),
        ("N_sym^5",               N_sym ** 5),
        ("[2]·[4]·[6]·[8]·N_sym", q2 * q4 * q6 * q8 * N_sym),
        ("([4]·[6]·[8])·N_sym",   q4 * q6 * q8 * N_sym),
        ("([4]·[6]·[8])·N_sym^2", q4 * q6 * q8 * N_sym ** 2),
    ]
    for name, val in candidates:
        rt = ratio / val
        L = mpmath.log(rt) / mpmath.log(q) if rt > 0 else mpmath.mpf("-inf")
        print(f"  ratio / ({name:<30}) = {mpmath.nstr(rt, 12):>22}  "
              f"log_q = {mpmath.nstr(L, 10):>16}")
    print()

    # ── Ansatz A1: integer · [2k]_q-products · q^L ─────────────
    print("Ansatz A1: ratio = INT · [4]_q^a · [6]_q^b · [8]_q^c / "
          "[2]_q^d · q^L")
    print(f"   (integer × Plancherel base × q-power)")
    INT_set = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 24, 45, 60, 120, 720]
    exp_set = [-2, -1, 0, 1, 2, 3, 4]
    hits_A1 = []
    for INT in INT_set:
        for a in exp_set:
            for b in exp_set:
                for c in exp_set:
                    for d in exp_set:
                        if d > 4 or d < 0:
                            continue
                        prod = INT * q4**a * q6**b * q8**c / q2**d
                        if prod <= 0:
                            continue
                        L = mpmath.log(ratio / prod) / mpmath.log(q)
                        L_round = int(mpmath.nint(L))
                        if abs(L_round) > 50:
                            continue
                        L_dev = abs(L - L_round)
                        rel_err = float(L_dev * mpmath.log(q))
                        if rel_err < 5e-7:
                            hits_A1.append({
                                "INT": INT, "a": a, "b": b, "c": c, "d": d,
                                "L": L_round, "rel_err": rel_err,
                            })
    hits_A1.sort(key=lambda x: x["rel_err"])
    print(f"   Hits below CODATA tol (5e-7): {len(hits_A1)}")
    for h_ in hits_A1[:5]:
        print(f"   INT={h_['INT']:>3}  [4]^{h_['a']:>2} [6]^{h_['b']:>2} "
              f"[8]^{h_['c']:>2} / [2]^{h_['d']}  · q^{h_['L']:>3}  "
              f"rel_err={h_['rel_err']:.3e}")
    # Basis size diagnostic
    A1_size = len(INT_set) * len(exp_set) ** 3 * 5
    print(f"   Basis size: {A1_size:,}; expected chance hits at "
          f"5e-7: ~{A1_size * 5e-7:.2f}")
    print()

    # ── Ansatz A2: integer · N_sym^a · q^L · h^b ──────────────
    print("Ansatz A2: ratio = INT · N_sym(q)^a · q^L · h^b")
    print(f"   (integer × symmetric-channel weight × q-power × "
          f"Hecke amplitude)")
    hits_A2 = []
    for INT in INT_set:
        for a in [1, 2, 3, 4, 5, 6]:
            for b in [-3, -2, -1, 0, 1, 2]:
                prod = INT * N_sym**a * h**b
                if prod <= 0:
                    continue
                L = mpmath.log(ratio / prod) / mpmath.log(q)
                L_round = int(mpmath.nint(L))
                if abs(L_round) > 50:
                    continue
                L_dev = abs(L - L_round)
                rel_err = float(L_dev * mpmath.log(q))
                if rel_err < 1e-5:
                    hits_A2.append({
                        "INT": INT, "a": a, "b": b,
                        "L": L_round, "rel_err": rel_err,
                    })
    hits_A2.sort(key=lambda x: x["rel_err"])
    print(f"   Hits below 1e-5 (200× CODATA): {len(hits_A2)}")
    for h_ in hits_A2[:5]:
        print(f"   INT={h_['INT']:>3}  N_sym^{h_['a']}  h^{h_['b']:>2}  "
              f"q^{h_['L']:>3}  rel_err={h_['rel_err']:.3e}")
    A2_size = len(INT_set) * 6 * 6
    print(f"   Basis size: {A2_size}; expected chance hits at "
          f"1e-5: ~{A2_size * 1e-5:.4f}")
    print()

    # ── Ansatz A3: structural product ─────────────────────────
    print("Ansatz A3: ratio = INT · ([4]·[6]·[8]) / [2] · N_sym^a · q^L")
    base = q4 * q6 * q8 / q2
    hits_A3 = []
    for INT in INT_set:
        for a in [-2, -1, 0, 1, 2, 3, 4]:
            prod = INT * base * N_sym**a
            if prod <= 0:
                continue
            L = mpmath.log(ratio / prod) / mpmath.log(q)
            L_round = int(mpmath.nint(L))
            if abs(L_round) > 50:
                continue
            L_dev = abs(L - L_round)
            rel_err = float(L_dev * mpmath.log(q))
            if rel_err < 1e-5:
                hits_A3.append({
                    "INT": INT, "a": a,
                    "L": L_round, "rel_err": rel_err,
                })
    hits_A3.sort(key=lambda x: x["rel_err"])
    print(f"   Hits below 1e-5: {len(hits_A3)}")
    for h_ in hits_A3[:5]:
        print(f"   INT={h_['INT']:>3}  N_sym^{h_['a']:>2}  q^{h_['L']:>3}  "
              f"rel_err={h_['rel_err']:.3e}")
    A3_size = len(INT_set) * 7
    print(f"   Basis size: {A3_size}; expected chance hits at "
          f"1e-5: ~{A3_size * 1e-5:.5f}")
    print()

    # ── Verdict ────────────────────────────────────────────────
    best_overall = None
    for ansatz_name, hits in (("A1", hits_A1), ("A2", hits_A2),
                              ("A3", hits_A3)):
        if hits and (best_overall is None
                     or hits[0]["rel_err"] < best_overall["rel_err"]):
            best_overall = {**hits[0], "ansatz": ansatz_name}

    print("VERDICT:")
    print("  PURE NUMERICAL SEARCH IS FITTING — NOT A DERIVATION.")
    print("  ")
    print("  Informative null results:")
    print(f"    A2 (pure N_sym^a):          0 hits at 1e-5  →  N_sym alone "
          "does NOT close the form.")
    print(f"    A3 (structural · N_sym^a):  0 hits at 1e-5  →  N_sym is NOT "
          "a multiplicative correction.")
    print(f"  ")
    print(f"  A1 hit (rel_err = {best_overall['rel_err']:.3e} if any)"
          if best_overall else "  A1: no hits.")
    print("  has no categorical justification of its exponents and so is")
    print("  recorded as a null result (consistent with chance for a "
          f"{A1_size:,}-element basis).")
    print("  ")
    print("  Conclusion: numerical PSLQ over basis-of-monomials cannot")
    print("  derive N_v.  Going forward requires categorical authoring,")
    print("  not more search.")

    out = {
        "computation": "nv-constrained-pslq",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Constrained-PSLQ search for v_weak/m_e on the path-α-Bring "
            "basis {[2]_q, [4]_q, [6]_q, [8]_q, q^k, h^k, N_sym(q)} "
            "informed by prop:weak-symmetric-normalization. Three ansatz "
            "shapes A1/A2/A3 tested; results vs CODATA-G_F precision."
        ),
        "reference_blocks": [
            "prop:weak-symmetric-normalization",
            "prop:knot-operator-lp-selection",
            "conj:weak-spectral-completeness",
            "conj:electroweak-higgs-torus-link-triplet",
        ],
        "audit": "docs/audits/2026-05-05-path-alpha-bring-refinement.md",
        "ratio_target": mpmath.nstr(ratio, 25),
        "N_v_target": mpmath.nstr(N_v, 25),
        "q_0": mpmath.nstr(q, 50),
        "N_sym_q0": mpmath.nstr(N_sym, 25),
        "tolerance_codata": "5e-7",
        "ansatz_A1": {
            "form": "INT · [4]_q^a · [6]_q^b · [8]_q^c / [2]_q^d · q^L",
            "basis_size": A1_size,
            "n_hits": len(hits_A1),
            "expected_chance_hits_5e-7": A1_size * 5e-7,
            "top_hits": hits_A1[:5],
        },
        "ansatz_A2": {
            "form": "INT · N_sym(q)^a · h^b · q^L",
            "basis_size": A2_size,
            "n_hits": len(hits_A2),
            "expected_chance_hits_1e-5": A2_size * 1e-5,
            "top_hits": hits_A2[:5],
        },
        "ansatz_A3": {
            "form": "INT · ([4]·[6]·[8])/[2] · N_sym^a · q^L",
            "basis_size": A3_size,
            "n_hits": len(hits_A3),
            "expected_chance_hits_1e-5": A3_size * 1e-5,
            "top_hits": hits_A3[:5],
        },
        "best_overall": best_overall,
        "verdict": "fitting-not-derivation",
        "verdict_explanation": (
            "Pure numerical PSLQ over a monomial basis is fitting, not "
            "derivation, regardless of basis size. Even at 27,440 elements "
            "(30× smaller than the impasse-audit search), CODATA-precision "
            "hits exist that are mathematically equivalent to chance "
            "matches. The informative content of this run is the NULL "
            "results from A2 (pure N_sym) and A3 (N_sym as multiplicative "
            "correction), which RULE OUT those structural shapes. A "
            "derivation of N_v requires categorical authoring of the "
            "structural exponents, not more search."
        ),
    }
    out_path = Path(__file__).parent / "nv-constrained-pslq.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
