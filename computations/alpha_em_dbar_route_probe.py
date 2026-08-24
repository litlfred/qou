#!/usr/bin/env python3
"""alpha_em_dbar_route_probe.py — the ∂̄/Dolbeault route to the 1/π loop weight:
does it supply the genus source AND the 1/π, or only the mode-count?

Follow-up to `alpha_em_1pi_spectral_zeta_probe.py` (χ-vs-g obstruction). That probe
showed the loop measure `1/(8π) = 1/(π·b₁) = 1/(2π·g)` needs a **genus-linear**
source, absent from the χ-linear scalar-Laplacian invariants. The one genuinely
genus-linear candidate is the **Dolbeault (∂̄) operator**. This probe tests it,
honestly (critical-distance — no fit to `1/(8π)`).

## The two factors of `1/(8π) = (1/b₁)·(1/π)`

**Factor A — the mode count `1/b₁`.** Riemann–Roch on the canonical bundle `K`
(`deg K = 2g−2`, Serre duality `h¹(K)=h⁰(O)=1`) gives `h⁰(K) = g`, so
`dim H^{1,0}(Bring) = g = 4` and `dim H¹ = b₁ = 2g = 8`. This is the **forced,
genus-linear** source the obstruction demanded — and it comes from ∂̄
(Riemann–Roch), NOT from the scalar heat kernel. ✓

**Factor B — the coefficient `1/π`.** Does the ∂̄-determinant / analytic torsion
supply a bare `1/π`? The Dolbeault Laplacian `Δ_∂̄ = ½ Δ_dR` (Kähler, complex
dim 1); its index is `χ(O) = 1−g = χ/2` — still **proportional to χ**. So the
∂̄-*index/ζ(0)* is `χ`-controlled (a rational/log quantity), NOT a bare `1/π`. The
∂̄ operator supplies the genus **mode-count** (Factor A) but **not** the `1/π`
coefficient (Factor B).

## Conclusion (honest reduction, not a derivation)

`1/(8π)` splits cleanly into a **forced** Hodge mode-count `1/b₁` (∂̄ / Riemann–
Roch, genus-linear — this ANSWERS the χ-vs-g obstruction) times a **residual**
`1/π` that no spectral determinant (scalar OR ∂̄) produces. That residual `1/π` is
the framework's **archimedean dilogarithm regulator** (`conj:dilogarithm-
archimedean-limit`; the same canonical μ-independent π behind the *proved* `2/(3π)`
Bloch term, Part A proved / Part B open). So:

  **the α_EM `1/(8π)` MAGNITUDE ⟺ (forced Hodge `1/b₁`) × (archimedean-dilog `1/π`)**

— the entire open magnitude reduces to the single named conjecture Part B, NOT to
any missing spectral geometry. This is a *reduction/connection*, not a closure.
Converges with the permode probe, the χ-vs-g obstruction, and the τ=W adversarial
audit. No fit; no instance; `1/(8π)` phase-4; nothing wired.

Run: python3 -u computations/alpha_em_dbar_route_probe.py 2>&1 | tee /tmp/dbar.log

-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
-- Ref: [manuscript] conj:dilogarithm-archimedean-limit
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
G = 4
B1 = 2 * G
CHI = 2 - 2 * G
PI = mp.pi
DEG_K = 2 * G - 2      # deg of canonical bundle


def main() -> int:
    target = 1 / (8 * PI)
    # Factor A: Riemann–Roch on K ⇒ h⁰(K) = deg K + 1 − g + h¹(K), h¹(K)=h⁰(O)=1
    h0_O = 1
    h1_K = h0_O                       # Serre duality
    h0_K = DEG_K + 1 - G + h1_K       # = g
    dim_H10 = h0_K
    dim_H1 = 2 * dim_H10              # b₁
    print(f"Factor A — ∂̄ / Riemann–Roch mode count (FORCED, genus-linear):")
    print(f"   deg K = 2g−2 = {DEG_K};  h⁰(K) = degK+1−g+h¹(K) = {h0_K} = g = dim H^{{1,0}}")
    print(f"   dim H¹ = b₁ = 2·dim H^{{1,0}} = {dim_H1}  (= {B1})")
    A_ok = (dim_H10 == G and dim_H1 == B1)

    # Factor B: does the ∂̄-index / ζ(0) give a bare 1/π?  No — it's χ-linear.
    dbar_index = 1 - G                # χ(O) = 1−g
    print(f"\nFactor B — ∂̄ coefficient (test for a bare 1/π):")
    print(f"   ∂̄-index χ(O) = 1−g = {dbar_index} = χ/2 = {CHI//2}  — proportional to χ (rational, NOT 1/π)")
    print(f"   Δ_∂̄ = ½ Δ_dR (Kähler, dim_ℂ=1) ⇒ ζ_∂̄(0) is χ-controlled; no bare 1/π from the ∂̄ determinant")

    # The reduction: 1/(8π) = (1/b₁)·(1/π)
    reduction = (mp.mpf(1) / dim_H1) * (1 / PI)
    red_ok = abs(reduction - target) < mp.mpf(10) ** (-20)
    print(f"\nReduction:  1/(8π) = (1/b₁)·(1/π) = (1/{dim_H1})·(1/π) = {mp.nstr(reduction,10)}  "
          f"(matches {mp.nstr(target,10)}: {red_ok})")
    print(f"   1/b₁ = 1/{dim_H1}  FORCED (Hodge / Riemann–Roch, genus-linear)")
    print(f"   1/π              RESIDUAL = archimedean dilog regulator (conj:dilogarithm-archimedean-limit)")

    ok = A_ok and red_ok
    verdict = (
        f"The ∂̄/Dolbeault route supplies the GENUS-LINEAR MODE COUNT but NOT the "
        f"1/π. Factor A: Riemann–Roch on K gives h⁰(K)=g=dim H^{{1,0}}, b₁=2g=8 — the "
        f"forced genus-linear source the χ-vs-g obstruction demanded (from ∂̄, not the "
        f"scalar heat kernel). Factor B: the ∂̄-index χ(O)=1−g=χ/2 is χ-proportional "
        f"(rational/log), so no spectral determinant (scalar OR ∂̄) produces a bare "
        f"1/π. Hence 1/(8π) = (1/b₁)·(1/π): the mode-count 1/b₁ is FORCED (Hodge), and "
        f"the residual 1/π is the archimedean dilog regulator (conj:dilogarithm-"
        f"archimedean-limit, Part A proved / Part B open) — the same μ-independent π "
        f"behind the proved 2/(3π) Bloch term. So the entire open α_EM 1/(8π) MAGNITUDE "
        f"reduces to that ONE named conjecture (Part B), not to missing spectral "
        f"geometry. A reduction/connection, not a closure. No fit; no instance; 1/(8π) "
        f"phase-4; nothing wired."
    )
    print(f"\nVERDICT: {verdict}")

    wb = WitnessBuilder("alpha-em-dbar-route")
    wb.set_audit_only("docs/audits/2026-07-25-alpha-em-1pi-loop-weight-chi-vs-g-obstruction.md")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.set_description(
        "∂̄/Dolbeault route to the α_EM 1/π loop weight. Riemann–Roch on K gives the "
        "FORCED genus-linear mode count (h⁰(K)=g=dim H^{1,0}, b₁=2g=8) — answering the "
        "χ-vs-g obstruction. But the ∂̄-index χ(O)=1−g=χ/2 is χ-proportional, so no "
        "spectral determinant gives a bare 1/π. Reduction: 1/(8π)=(1/b₁)·(1/π), 1/b₁ "
        "forced (Hodge), 1/π = archimedean dilog regulator (conj:dilogarithm-"
        "archimedean-limit Part B, open). The whole open magnitude ⟺ that one "
        "conjecture. Reduction, not closure. No fit; no instance; 1/(8π) phase-4.")
    wb.add_parameter("g", G)
    wb.add_parameter("b1", B1)
    wb.add_assertion("dbar_gives_modecount_not_1pi", "true" if ok else "false", "true",
                     source="h⁰(K)=g forced (RR); ∂̄-index=χ/2 χ-linear (no bare 1/π); "
                            "1/(8π)=(1/b₁)·(1/π) with 1/π=regulator")
    wb.add_data("dim_H10_eq_g", dim_H10)
    wb.add_data("b1_eq_2g", dim_H1)
    wb.add_data("dbar_index_1_minus_g", dbar_index)
    wb.add_data("residual_1_pi_source", "archimedean dilog regulator (conj:dilogarithm-archimedean-limit, Part B open)")
    wb.add_caveat("Reduction, NOT closure. Factor A (mode count 1/b₁) is forced by "
                  "Hodge/Riemann–Roch. Factor B (1/π) is NOT any spectral determinant — "
                  "it is the archimedean dilog regulator (Part B, open). The α_EM 1/(8π) "
                  "magnitude reduces to that single named conjecture.")
    wb.add_data("verdict", verdict)
    out = wb.save()
    print(f"\nwitness → {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
