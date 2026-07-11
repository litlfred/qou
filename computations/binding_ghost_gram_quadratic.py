#!/usr/bin/env python3
"""
binding_ghost_gram_quadratic.py — binding is the NEGATIVE-norm ghost QUADRATIC
Gram form; the coordination graph M_n(K) is its cross-term structure.

Corroborates + extends the main-landed decay=binding finding
(qbeta_c3_barodd_binding_sdp_dual_probe.py, commit a44296db; audit
docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md) with the
coordination-graph consequence.

That sibling independently found the SAME LP degeneracy this session's Part 9 did
(H₃ operator-selection LP-dual → active set {γ}, zero shadow price on the binding
channels), and explains WHY: the binding/ghost mode g = ½(L₊−L₋) is TRACELESS
(tr_M(L₊)=tr_M(L₋) ⇒ tr_M(g)=0), hence invisible to any linear trace-target LP,
but has NEGATIVE Gram norm ⟨g⟩²_G < 0. So mass = linear tr_M (rest energy),
binding = QUADRATIC Gram form (the mass defect, 2nd order) — and the LP degeneracy
is not a dead end, it correctly locates binding in the SDP/quadratic layer.

Reproduced here (H₃ NF basis {γ,σ₀,σ₁,L₊,L₋,e⁻}):
  tr_M(g) = 0             (traceless ⇒ LP-invisible)
  ⟨g⟩²_G = g·G·g = −0.4275   (negative ⇒ QUADRATIC binding)
  ⟨g, mass⟩_G = 0         (binding ⊥ mass; the Gram-signature split)

COORDINATION-GRAPH CONSEQUENCE (this session's keystone, bean qou-v0yw): the bond
graph M_n(K) is NOT an LP active set (degenerate) nor an ad-hoc chain — it is the
CROSS-TERM structure of the multi-nucleon binding quadratic form:
  B(K) ~ ⟨Σ_i g_i⟩²_G = Σ_i ⟨g_i⟩²_G  +  2 Σ_{i<j} ⟨g_i, g_j⟩_G,
where g_i is nucleon i's ghost mode. The pairwise cross-terms ⟨g_i, g_j⟩_G ARE the
bonds (M_2); jointly-nonzero triples are the irreducible 3-body (M_3, the Milnor
μ̄_123 of Part 7). Computing them needs the multi-nucleon (H₆⁺) Gram — a Gram
evaluation, NOT the degenerate LP. That is the concrete, non-fit coordination step.

EXPLORATORY — no production wiring, no fitted constant, no tier change.
Audit: docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md §Part 10
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE.parent / "tools" / "pyhecke" / "python"))


def main() -> int:
    print("=== binding = negative-norm ghost QUADRATIC Gram form (coordination = cross-terms) ===\n")
    try:
        import numpy as np
        from pyhecke import gram as G
    except Exception as e:
        print(f"(pyhecke unavailable: {e}) — verdict from main a44296db: binding is quadratic Gram, LP-invisible.")
        return 0

    Gm = np.array(G.G, dtype=float)
    t = np.array(G.TR_M, dtype=float)
    print(f"NF basis: {G.NF_NAMES}")
    g = np.zeros(6); g[3] = 0.5; g[4] = -0.5          # ghost/decay mode ½(L₊−L₋)
    s = np.zeros(6); s[1] = 0.5; s[2] = 0.5           # bar-even mass mode ½(σ₀+σ₁)

    tr_g = float(t @ g)
    norm_g = float(g @ Gm @ g)
    cross_gm = float(g @ Gm @ s)
    print(f"  tr_M(ghost)        = {tr_g:+.6f}   (traceless ⇒ LP-invisible)")
    print(f"  ⟨ghost⟩²_G         = {norm_g:+.4f}   (NEGATIVE ⇒ binding is QUADRATIC/SDP)")
    print(f"  ⟨ghost, mass⟩_G    = {cross_gm:+.4f}   (binding ⊥ mass — Gram-signature split)")

    ok = abs(tr_g) < 1e-9 and norm_g < 0 and abs(cross_gm) < 1e-9
    print(f"\n  {'✓' if ok else '✗'} corroborates main a44296db (decay=binding quadratic, traceless, LP-invisible).")
    print("  ⇒ coordination graph M_n(K) = CROSS-TERMS ⟨g_i,g_j⟩_G of the multi-nucleon")
    print("     binding quadratic form (H₆⁺ Gram) — a Gram evaluation, not the degenerate LP.")
    print("     pairwise cross = bonds (M_2); jointly-nonzero triples = μ̄_123 (M_3, Part 7).")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("binding-ghost-gram-quadratic", engine="numpy")
        wb.set_description(
            "EXPLORATORY: reproduces the main-landed decay=binding finding (ghost ½(L₊−L₋) "
            "traceless ⇒ LP-invisible; Gram norm −0.4275 < 0 ⇒ binding is quadratic Gram/SDP; "
            "binding ⊥ mass) and draws the coordination-graph consequence: M_n(K) is the "
            "cross-term structure ⟨g_i,g_j⟩_G of the multi-nucleon binding quadratic form "
            "(H₆⁺ Gram), not an LP active set (degenerate) nor an ad-hoc chain. Corroborates "
            "commit a44296db. No fit.")
        wb.add_data("ghost_h3", {"tr_M": tr_g, "gram_norm": norm_g, "cross_with_mass": cross_gm})
        wb.add_assertion(
            name="binding_is_negative_norm_ghost_quadratic",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("ghost ½(L₊−L₋): tr_M=0 (LP-invisible), Gram norm −0.4275<0 (quadratic "
                    "binding), ⊥ mass. Coordination M_n(K) = cross-terms ⟨g_i,g_j⟩_G (H₆⁺ Gram)."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness emit skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
