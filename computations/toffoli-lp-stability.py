
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401,E402
#!/usr/bin/env python3
"""
LP-dual stability of the q-Toffoli braid.

Witness for prop:toffoli-lp-stability.

Computes, at a grid of substrate parameters q:
  • P_{7,7}(q) = (q + q^{1/2} - 1)/(q + 1)         — Toffoli diagonal
  • Phi(q)    = (q-1)(q^{3/2}+q^{1/2}-1)(q^{3/2}+q+1) / (2(q+1)^2)
                                                   — q-AND amplitude
  • Gram matrix G(q) on NF basis {γ, σ₀, σ₁, L₊, L₋, e⁻}
  • Full eigenvalue spectrum of G(q); min and max eigenvalues
  • Gram condition number κ(G) = λ_max(G) / |λ_min(G)| (positive
    definition consistent with the manuscript proposition)

The golden-ratio threshold is q⋆ = 1/φ² = (3-√5)/2 ≈ 0.382 — the
real zero of P_{7,7}(q) in (0, ∞). Substrate q₀ ≈ 1.110 sits well
inside the stable regime.

Usage:
    python3 toffoli-lp-stability.py
Output:
    toffoli-lp-stability.witness.json
"""
import json
from datetime import datetime, timezone
from pathlib import Path
import subprocess
import math
from mpmath import mp

import numpy as np
# NF_BASIS moved to pyhecke.gram (M2b inversion).
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[1] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import NF_BASIS as _PG_NF_BASIS  # noqa: E402



# ── constants ─────────────────────────────────────────────────
PHI = (1.0 + float(mp.sqrt(5))) / 2.0          # golden ratio (substrate-precision sqrt, coerced to float for downstream float math)
Q_STAR = 1.0 / (PHI ** 2)                   # ≈ 0.38197
Q0 = 1.1099785955573347                     # physical substrate q

NF_BASIS_NAMES = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
NF_BASIS = _PG_NF_BASIS  # moved to pyhecke.gram
def repo_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=str(Path(__file__).resolve().parent.parent.parent),
        ).decode().strip()
    except Exception:
        return "unknown"


def toffoli_diagonal(q):
    """P_{7,7}(q) = (q + q^{1/2} - 1) / (q + 1)."""
    return (q + float(mp.sqrt(q)) - 1.0) / (q + 1.0)


def q_and_amplitude(q):
    """Φ(q) = (q - 1)(q^{3/2} + q^{1/2} - 1)(q^{3/2} + q + 1) / (2(q+1)^2)."""
    s = float(mp.sqrt(q))
    return (q - 1.0) * (q * s + s - 1.0) * (q * s + q + 1.0) / (2.0 * (q + 1.0) ** 2)


def hecke_mul(t1, t2, ha):
    """Multiply two Hecke elements given as dict {word: coeff}."""
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}


def reduce_nf(terms, ha):
    """Reduce to NF basis using Hecke relation σ² = ha·σ + 1 and braid relation."""
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            # σ_i² = ha·σ_i + 1
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    key1 = pre + (i,) + suf
                    new_terms[key1] = new_terms.get(key1, 0.0) + coeff * ha
                    new_terms[pre + suf] = new_terms.get(pre + suf, 0.0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            # braid relation σ_iσ_jσ_i = σ_jσ_iσ_j for |i-j|=1, canonical order
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    if new_trip < (a, b, a):
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True
                        break
            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def gram_matrix(q):
    """6×6 Gram matrix G_{ij} = tr_M(b_i · b_j) on the NF basis."""
    ha = q - 1.0 / q
    z = q**3 / (q**2 + 1)
    # tr_M of each basis element: tr_M(σ_i₁ σ_i₂ ... σ_iₖ) = z^(k reduced)
    # Precompute tr_M for each NF basis element length
    tr_basis = np.array([1.0, z, z, z ** 2, z ** 2, z ** 3])
    # Compute b_i · b_j in NF, then dot with tr_basis on the resulting coeffs
    n = len(NF_BASIS)
    G = np.zeros((n, n))
    for i, wi in enumerate(NF_BASIS):
        for j, wj in enumerate(NF_BASIS):
            product = hecke_mul({wi: 1.0}, {wj: 1.0}, ha)
            product = reduce_nf(product, ha)
            # Take Markov trace: sum_{word w} coeff(w) * z^{length of reduced w}
            tr = 0.0
            for w, c in product.items():
                # Reduce tr_M of σ-word: closure trace for H_n, z^|w| for linear basis
                tr += c * (z ** len(w))
            G[i, j] = tr
    return G


def main():
    out_path = Path(__file__).parent / "toffoli-lp-stability.witness.json"
    q_grid = [
        0.30,        # below threshold
        0.35,        # below threshold
        Q_STAR,      # threshold: P_{7,7} = 0
        0.45,        # above threshold
        0.60,
        0.80,
        0.95,
        1.00,        # classical limit
        1.05,
        Q0,          # physical substrate
        1.25,
        1.50,
        2.00,
        3.00,
    ]
    scan = []
    for q in q_grid:
        G = gram_matrix(q)
        evals = sorted(np.linalg.eigvalsh(G).tolist())
        row = {
            "q": q,
            "P_77": toffoli_diagonal(q),
            "Phi_qAND": q_and_amplitude(q),
            "gram_eigenvalues": evals,
            "gram_lambda_min": evals[0],
            "gram_lambda_max": evals[-1],
            "gram_condition": evals[-1] / abs(evals[0]) if evals[0] != 0 else float("inf"),
            "P_77_sign": "+" if toffoli_diagonal(q) > 0 else ("0" if toffoli_diagonal(q) == 0 else "-"),
            "Phi_sign": "+" if q_and_amplitude(q) > 0 else ("0" if q_and_amplitude(q) == 0 else "-"),
        }
        scan.append(row)

    # Sanity check: P_{7,7}(q⋆) ≈ 0
    p77_at_star = toffoli_diagonal(Q_STAR)
    phi_at_star = q_and_amplitude(Q_STAR)

    witness = {
        "computation": "toffoli-lp-stability",
        "description": "LP-dual stability of the q-Toffoli braid: P_{7,7}(q), Φ(q), Gram spectrum on a q-grid spanning the golden-ratio threshold q⋆ = 1/φ².",
        "label": "prop:toffoli-lp-stability",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "git_sha": repo_sha(),
        "constants": {
            "phi_golden": PHI,
            "q_star": Q_STAR,
            "q_star_closed_form": "(3 - sqrt(5))/2",
            "q0_physical": Q0,
        },
        "threshold_verification": {
            "P_77_at_q_star": p77_at_star,
            "Phi_at_q_star": phi_at_star,
            "P_77_vanishes_at_q_star": abs(p77_at_star) < 1e-12,
            "Phi_vanishes_at_q_star": abs(phi_at_star) < 1e-12,
        },
        "nf_basis": NF_BASIS_NAMES,
        "gram_matrix_at_q0": gram_matrix(Q0).tolist(),
        "scan": scan,
        "conclusions": {
            # LP threshold: q > q⋆ ensures P_{7,7}(q) > 0 (Toffoli
            # diagonal positive). Full physical stability additionally
            # requires Φ(q) > 0 — Φ has a zero at q_Φ ≈ 0.4656 and
            # becomes negative on (q_Φ, 1), so the joint-positivity
            # regime splits as (q⋆, q_Φ) ∪ (1, ∞).
            "stable_regime_lp": f"q > q⋆ ≈ {Q_STAR:.6f}  (P_77 > 0)",
            "stable_regime_physical": "q ∈ (q⋆, q_Φ) ∪ (1, ∞)  (P_77 > 0 and Φ > 0)",
            "stable_regime": f"q > q⋆ ≈ {Q_STAR:.6f}",  # back-compat alias
            "physical_q0_stable": toffoli_diagonal(Q0) > 0 and q_and_amplitude(Q0) > 0,
            "classical_limit_q_equals_1": {
                "P_77": toffoli_diagonal(1.0),
                "Phi": q_and_amplitude(1.0),
                "note": "Φ(1) = 0 by construction (classical reversible Toffoli trivialises q-AND)",
            },
        },
    }

    with open(out_path, "w") as f:
        json.dump(witness, f, indent=2, default=float)

    print(f"wrote {out_path}")
    print(f"q⋆ = {Q_STAR:.10f}")
    print(f"P_{{7,7}}(q⋆) = {p77_at_star:.3e}  (should ≈ 0)")
    print(f"Φ(q⋆)       = {phi_at_star:.3e}  (non-zero: Φ zero is at q_Φ ≈ 0.4656, not q⋆)")
    print(f"P_{{7,7}}(q₀) = {toffoli_diagonal(Q0):.6f}")
    print(f"Φ(q₀)       = {q_and_amplitude(Q0):.6f}")


if __name__ == "__main__":
    main()
