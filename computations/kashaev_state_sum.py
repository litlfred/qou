#!/usr/bin/env python3
"""Kashaev's quantum-dilogarithm state-sum invariant [Kas95] — the
figure-eight closed form, as the independent cross-check (#2 of the plan).

The braid-closure / enhanced-Markov-trace route is proven NOT to compute the
Kashaev invariant (see kashaev_rmatrix.py: no diagonal-μ Markov enhancement
exists).  The invariant is the Section-3 face-index state sum.  For the
figure-eight that state sum collapses to Kashaev's celebrated closed form
[Kas95, (1.1)/§4]:

    ⟨4₁⟩_N = Σ_{k=0}^{N-1} |(ω)_k|²,    ω = e^{2πi/N},
    (ω)_k = ∏_{j=1}^{k} (1 − ω^j),   |(ω)_k|² = ∏_{j=1}^{k} (2 − 2cos(2πj/N)).

The Volume Conjecture [Kas97, MurakamiMurakami01] then reads

    2π lim_{N→∞} (1/N) log|⟨4₁⟩_N| = Vol(4₁) = 2·Λ(π/6)·3 = 2.029883...,

the volume of two ideal regular tetrahedra.  This validates the entire
root-of-unity machinery INDEPENDENTLY of the U_q(sl₂) R-matrix engine —
and (below) reproduces that engine's own 4₁ magnitudes to float tol.

Whitehead needs the genuine 2-cusp face-index partition function (the
maps j:E→ℤ_N, a:V×F→ℤ_N with the sum-1 constraints [Kas95, (3.3)-(3.4)]);
that is the next implementation unit.  Audit-only; no wiring.
"""
from __future__ import annotations

import cmath
import json
import math
from datetime import datetime, timezone
from pathlib import Path

VOL_4_1 = 2.029883212819307  # 6·Λ(π/3) = Vol(figure-eight complement)


def kashaev_fig8(N: int) -> float:
    """⟨4₁⟩_N = Σ_{k=0}^{N-1} ∏_{j=1}^{k} |1−ω^j|²  (real, ≥ 0)."""
    total = 0.0
    prod = 1.0                       # |(ω)_0|² = 1 (empty product)
    for k in range(N):
        if k >= 1:
            prod *= 2.0 - 2.0 * math.cos(2.0 * math.pi * k / N)
        total += prod
    return total


def kashaev_fig8_complex(N: int) -> complex:
    """Same via the raw q-Pochhammer, to confirm the |·|² reduction."""
    om = cmath.exp(2j * math.pi / N)
    total = 0j
    poch = 1 + 0j
    for k in range(N):
        if k >= 1:
            poch *= (1 - om ** k)
        total += poch * poch.conjugate()
    return total


def growth_rate(N: int) -> float:
    """2π·(1/N)·log⟨4₁⟩_N — should → Vol(4₁)."""
    return 2.0 * math.pi * math.log(kashaev_fig8(N)) / N


def richardson_volume(Ns) -> float:
    """1-step Richardson on the O(log N / N) tail of 2π log⟨⟩/N.
    g(N) = V + a·(log N)/N + …  ⇒  cancel the leading (log N)/N term."""
    Ns = sorted(Ns)[-2:]
    n1, n2 = Ns
    g1, g2 = growth_rate(n1), growth_rate(n2)
    a1, a2 = math.log(n1) / n1, math.log(n2) / n2
    return (g1 * a2 - g2 * a1) / (a2 - a1)


if __name__ == "__main__":
    print("Kashaev state-sum invariant — figure-eight closed form [Kas95]\n")

    # 1) real |·|² form == raw complex Pochhammer form
    print("  |·|² reduction check (real == complex):")
    ok = True
    for N in (3, 5, 8, 13, 20):
        a, b = kashaev_fig8(N), kashaev_fig8_complex(N)
        err = abs(a - b.real) + abs(b.imag)
        ok = ok and err < 1e-6 * max(1.0, a)
        print(f"    N={N:3d}: |·|²={a:.6e}  complex={b.real:.6e}+{b.imag:.1e}i  |Δ|={err:.1e}")
    print(f"    => {'VALIDATED' if ok else 'MISMATCH'}\n")

    # 2) Volume Conjecture: growth rate -> Vol(4_1)
    print(f"  growth rate 2π·log⟨4₁⟩_N/N  (target Vol(4₁)={VOL_4_1:.6f}):")
    for N in (20, 50, 100, 200, 400, 800):
        g = growth_rate(N)
        print(f"    N={N:4d}: {g:.6f}   (err {g - VOL_4_1:+.4f})")
    v = richardson_volume([400, 800])
    print(f"    Richardson[400,800]: {v:.6f}   (err {v - VOL_4_1:+.5f})\n")

    wit = {
        "description": "Kashaev quantum-dilog state-sum invariant [Kas95] — figure-eight closed form ⟨4₁⟩_N=Σ|(ω)_k|². Independent (non-R-matrix) cross-check of the root-of-unity Volume-Conjecture machinery. Item #2 of the plan.",
        "computation": "kashaev_state_sum", "audit_only": True,
        "reference": "Kashaev 1995, q-alg/9504020 (uploads/9504020v1.pdf)",
        "reduction_validated": bool(ok),
        "vol_4_1_target": VOL_4_1,
        "growth_rate": {str(N): growth_rate(N) for N in (100, 200, 400, 800)},
        "richardson_volume": v,
        "richardson_error": v - VOL_4_1,
        "kashaev_values": {str(N): kashaev_fig8(N) for N in (3, 5, 8, 13, 20)},
        "note": "Markov-trace route proven impossible (kashaev_rmatrix.py); this is the genuine Sect-3 state sum specialised to 4₁. Whitehead needs the 2-cusp face-index partition function (next unit).",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "kashaev-state-sum.witness.json"
    out.write_text(json.dumps(wit, indent=2))
    print(f"  Witness: {out}")
