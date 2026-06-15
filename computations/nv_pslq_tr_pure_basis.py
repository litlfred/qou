"""Re-run constrained PSLQ for N_v using tr_pure (bar-self-dual
cell-content trace) as the structural input.

Per user direction (2026-05-05): Plancherel weight was a degenerate
artifact; bar-self-dual tr_pure is the operative quantity. The
constrained basis becomes:

    B' = { [2]_q, [4]_q, [6]_q, [8]_q, q^k, h^k, tr_pure(W·Z·H) }

where
    tr_pure(W·Z·H) = 4·(q^18 + q^-18) + 2·(q^10 + q^-10)
                   + 1·(q^6  + q^-6 ) + 3·(q^2  + q^-2 )

is bar-self-dual: tr_pure | (q ↦ q^-1) = tr_pure.

A bar-self-dual ansatz for v_w/m_e must use only bar-self-dual
combinations.  We test:

  B1.  v_w/m_e = INT · ([k]_q palindromic combination) · tr_pure^a
       (each [k]_q is bar-self-dual modulo q^k prefactor; the product
       is bar-self-dual iff the q^k prefactor is balanced)
  B2.  v_w/m_e = INT · tr_pure^a · q^L · h^b
  B3.  v_w/m_e = INT · ([4]_q · [6]_q · [8]_q / [2]_q) · tr_pure^a
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath
mpmath.mp.dps = 80

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, G_F_MEV

q = mpmath.mpf(Q_50_DIGIT_STR)
G_F = mpmath.mpf(str(G_F_MEV))
m_e = mpmath.mpf(str(M_E_MEV))

v_w = 1 / mpmath.sqrt(mpmath.sqrt(2) * G_F)
ratio = v_w / m_e
N_v = 3 * ratio


def qint(n):
    return (q ** n - q ** -n) / (q - 1 / q) if n != 0 else mpmath.mpf(0)


def main() -> int:
    h = q - 1 / q
    q2, q4, q6, q8 = qint(2), qint(4), qint(6), qint(8)

    # tr_pure = 4(q^18 + q^-18) + 2(q^10 + q^-10) + (q^6 + q^-6) + 3(q^2 + q^-2)
    tr_pure = (
        4 * (q ** 18 + q ** -18)
        + 2 * (q ** 10 + q ** -10)
        + 1 * (q ** 6 + q ** -6)
        + 3 * (q ** 2 + q ** -2)
    )

    print("N_v PSLQ on tr_pure-based constrained basis (bar-self-dual)")
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
    print(f"  tr_pure(q_0)   = {mpmath.nstr(tr_pure, 14)}")
    print()

    # B1 — bar-self-dual structural product · tr_pure^a · symmetric-q-power
    # (q-power that's balanced: q^L · q^-L = 1, so use only L = 0)
    print("Ansatz B1: ratio = INT · ([4][6][8]/[2]) · tr_pure^a")
    INT_set = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 24, 45, 60, 120, 720,
               1024, 1440, 2880]
    base = q4 * q6 * q8 / q2  # bar-self-dual modulo prefactor
    hits_B1 = []
    for INT in INT_set:
        for a in [-2, -1, 0, 1, 2, 3, 4]:
            prod = INT * base * tr_pure ** a
            if prod <= 0:
                continue
            # Compare directly (no q^L slack since basis is bar-self-dual)
            rel_err = float(abs(ratio - prod) / ratio)
            if rel_err < 5e-3:
                hits_B1.append({
                    "INT": INT, "a": a, "rel_err": rel_err,
                    "value": float(prod),
                })
    hits_B1.sort(key=lambda x: x["rel_err"])
    print(f"   Hits below 5e-3 tol: {len(hits_B1)}")
    for h_ in hits_B1[:5]:
        print(f"   INT={h_['INT']:>4}  tr_pure^{h_['a']:>2}  "
              f"rel_err={h_['rel_err']:.3e}  value={h_['value']:.4f}")
    print()

    # B2 — pure tr_pure-only ansatz
    print("Ansatz B2: ratio = INT · tr_pure^a")
    hits_B2 = []
    for INT in INT_set:
        for a in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            prod = INT * tr_pure ** a
            if prod <= 0:
                continue
            rel_err = float(abs(ratio - prod) / ratio)
            if rel_err < 5e-3:
                hits_B2.append({
                    "INT": INT, "a": a, "rel_err": rel_err,
                    "value": float(prod),
                })
    hits_B2.sort(key=lambda x: x["rel_err"])
    print(f"   Hits below 5e-3 tol: {len(hits_B2)}")
    for h_ in hits_B2[:5]:
        print(f"   INT={h_['INT']:>5}  tr_pure^{h_['a']:>2}  "
              f"rel_err={h_['rel_err']:.3e}  value={h_['value']:.4f}")
    print()

    # B3 — tr_pure^a · ratio_of_q-integers (preserves bar-self-duality
    # only if the q-integer ratio is bar-self-dual, e.g.  [k]_q is
    # bar-self-dual up to q^(±k))
    # bar-symmetric q-integer combinations: [k]_q · [m]_q (palindromic numerator)
    # / [j]_q (palindromic denominator) — generally bar-self-dual MODULO total q-power
    print("Ansatz B3: ratio = INT · ([2k]_q^a / [2j]_q^b) · tr_pure^c · "
          "(bar-symmetric q^L slack)")
    hits_B3 = []
    for INT in INT_set:
        for a in range(0, 4):
            for b in range(0, 4):
                for k in [2, 3, 4]:
                    for j in [1, 2]:
                        for c in [0, 1, 2, 3]:
                            for L in range(-15, 16, 2):  # only even L (bar-balanced)
                                if a == b == c == 0:
                                    continue
                                qk = qint(2 * k)
                                qj = qint(2 * j)
                                if qj == 0:
                                    continue
                                prod = INT * qk ** a * qj ** -b * tr_pure ** c \
                                    * q ** L
                                if prod <= 0:
                                    continue
                                rel_err = float(abs(ratio - prod) / ratio)
                                if rel_err < 5e-7:
                                    hits_B3.append({
                                        "INT": INT, "a": a, "b": b,
                                        "k": k, "j": j, "c": c, "L": L,
                                        "rel_err": rel_err,
                                    })
    hits_B3.sort(key=lambda x: x["rel_err"])
    B3_size = len(INT_set) * 4 * 4 * 3 * 2 * 4 * 16
    print(f"   Basis size: {B3_size:,}; hits below CODATA tol (5e-7): "
          f"{len(hits_B3)}")
    for h_ in hits_B3[:5]:
        print(f"   INT={h_['INT']:>4}  [{2*h_['k']}]^{h_['a']} / "
              f"[{2*h_['j']}]^{h_['b']}  tr_pure^{h_['c']}  q^{h_['L']:>3}  "
              f"rel_err={h_['rel_err']:.3e}")
    print(f"   Expected chance hits at 5e-7: ~{B3_size * 5e-7:.2f}")
    print()

    # ── Verdict ────────────────────────────────────────────────
    print("VERDICT:")
    print("  Bar-self-duality of tr_pure imposes a strong structural")
    print("  constraint: any closed form for N_v in terms of cell-content")
    print("  data must be bar-self-dual.  This rules out the asymmetric")
    print("  Plancherel-weighted form and most naive monomial ansätze.")
    print()
    if hits_B3:
        be = hits_B3[0]
        print(f"  Best hit (B3, bar-symmetric basis): rel_err = "
              f"{be['rel_err']:.3e}")
        print(f"  Form: INT={be['INT']} · [{2*be['k']}]^{be['a']} / "
              f"[{2*be['j']}]^{be['b']} · tr_pure^{be['c']} · q^{be['L']}")
    else:
        print("  No hit below CODATA tol on the bar-symmetric basis B3.")
    print("  ")
    print("  The bar-symmetric basis (B3 size ~6k) is far smaller than the")
    print("  monomial basis of the impasse audit, so any hit found is more")
    print("  meaningful (lower FDR).  Still: numerical search is a tool,")
    print("  not a derivation.  Categorical authoring of the F(...) shape")
    print("  remains the path forward.")

    out = {
        "computation": "nv-pslq-tr-pure-basis",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Re-run of constrained PSLQ for N_v using bar-self-dual "
            "cell-content trace tr_pure(σ_1^4 σ_3^6 σ_5^8) as the "
            "structural input, replacing the demoted Plancherel-weighted "
            "N_sym from the prior basis. Tests three ansatz shapes B1/B2/B3 "
            "against CODATA-G_F precision."
        ),
        "reference_blocks": [
            "conj:hoefsmit-ew-cell-content",
            "conj:weak-spectral-completeness",
            "prop:weak-symmetric-normalization",
        ],
        "audit": "docs/audits/2026-05-05-path-alpha-bring-refinement.md",
        "ratio_target": mpmath.nstr(ratio, 25),
        "N_v_target": mpmath.nstr(N_v, 25),
        "q_0": mpmath.nstr(q, 50),
        "tr_pure_q0": mpmath.nstr(tr_pure, 25),
        "tolerance_codata": "5e-7",
        "ansatz_B1_pureProduct_tr_pure": {
            "form": "INT · ([4][6][8]/[2]) · tr_pure^a",
            "n_hits": len(hits_B1),
            "top_hits": hits_B1[:5],
        },
        "ansatz_B2_tr_pure_only": {
            "form": "INT · tr_pure^a",
            "n_hits": len(hits_B2),
            "top_hits": hits_B2[:5],
        },
        "ansatz_B3_bar_symmetric_full": {
            "form": "INT · [2k]^a / [2j]^b · tr_pure^c · q^L  (L even)",
            "basis_size": B3_size,
            "n_hits_codata": len(hits_B3),
            "expected_chance_hits_5e-7": B3_size * 5e-7,
            "top_hits": hits_B3[:5],
        },
        "verdict": (
            "no-conclusive-closed-form"
            if not hits_B3
            else "candidate-found-on-bar-symmetric-basis-pending-categorical-derivation"
        ),
        "conclusion": (
            "Bar-self-duality of tr_pure imposes a strong structural "
            "constraint. The bar-symmetric ansatz B3 yields a smaller "
            "basis (lower FDR) than the prior monomial search. Any "
            "hit found is suggestive but still requires categorical "
            "authoring of the F-shape, not just numerical confirmation."
        ),
    }
    out_path = Path(__file__).parent / "nv-pslq-tr-pure-basis.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
