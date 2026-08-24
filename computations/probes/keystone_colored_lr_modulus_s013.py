#!/usr/bin/env python3
"""s013 Front-2 — the COLORED Lawrence–Rozansky modulus vs the McKay value map.

Front 2 of the 2026-07-17 three-front attack spec
(`docs/audits/2026-07-17-three-front-attack-specs.md §2`), the W_λ keystone /
m_p·m_μ root-cause wall. Target (open piece named by
`docs/coordination/s5-so3-keystone.md`, framing-is-phase #3703):

    |S_{0λ}^{Σ(2,3,5)}(ζ)|  =  d_ζ(λ) / D(ζ)      at fibre roots of unity,

with colours mapped by McKay(2I↔Ê₈)∘(A₅⊂S₅) onto the **marks** {1,4,5,6}
(`keystone_mckay_e8_valuemap.py`: `d_q(λ)=[mark]_q`, split node (3,1,1) is
`[5]_q+1`, NOT `[6]_q`). The genuine construction the spec asks for: take the
machine-validated Σ(2,3,5) S-matrix of `keystone_valuemap_genuine_smatrix_s013.py`
(τ_N Gauss sum, Thm-10 exact anchor — cited, not re-derived) and **colour the
p₃=5 fibre** by a Wilson line of colour α (α=1 reproduces the bare vacuum row).

## The decisive structural computation (all exact; the spec's own kill criteria)

The genuine vacuum row of the Σ(2,3,5) false-theta theory is D=2 (two flat
connections, CS = −1/120, −49/120; s013 verdict). A Wilson line of colour α on
the order-p₃=5 fibre multiplies each flat connection k∈{1,2} by the SU(2)
quantum dimension of colour α at that flat's effective fifth root:

    [α]_{k} = sin(α·k·π/5) / sin(k·π/5),   α = 1..4   (colours on a p=5 fibre).

This probe computes, EXACTLY (fifth-root / golden-ratio closed forms):

  (K1) **α=1 anchor** — [1]_k = 1 at both flats (bare vacuum row recovered).
  (K2) **D=2 collapse, per flat** — the four colours reflection-collapse
       α=4≡α=1, α=3≡α=2 at flat 1 (and the ±-mirror at flat 2), because
       sin((5−α)kπ/5) = ±sin(αkπ/5). So colouring the p₃=5 fibre yields at most
       TWO independent moduli — it does NOT escape D=2.
  (K3) **bounded-root vs growing-q₀ type gap** — every fifth-root colored dim
       obeys |[α]_k| ≤ 1/sin(π/5) ≈ 1.7013, while the target ratios
       (1, [4]_{q₀}, [5]_{q₀}, [5]_{q₀}+1) ≈ (1, 4.110, 5.220, 6.220) grow past
       it. The target ratio-vector is realized at REAL q₀>1 (Habiro-continued
       growing quantum integers), NOT at any Σ(2,3,5) fibre root.
  (K4) **split-node / mark-6 obstruction** — the electron node's mark is 6,
       exceeding the fibre order 5, so it is NOT a single p₃=5 Wilson colour
       (colours run 1..4). Its A₅ 3⊕3′ split would need a TWO-block insertion;
       we test whether 2·[3]_k reproduces the target `[5]_{q₀}+1` (it does not
       at the root: 2·[3]_1 = 2φ ≈ 3.236 ≠ 6.220) — the spec's "[6]_ζ vs
       [5]_ζ+1" criterion, decided.

## Verdict framing (scope discipline, AGENTS.md)

Refined, NOT contradicted, vs the ledger's standing "q₀-continuation
deferred/open": the colored-LR construction at the Σ(2,3,5) fibre roots is
**scope-(a) excluded** as the carrier of the value map — it re-derives the D=2
collapse (K2) and cannot reach the growing target ratios at the root (K3), and
the split mark-6 node is outside the single-fibre colour range (K4). What
remains genuinely open is exactly the **q₀-continuation** (real-q₀ growing
[mark]_q₀ is the value map; the root-level modular object is not) — so a carrier,
if any, is a Habiro/q₀-continued or larger-D geometric family (more exceptional
fibres, or genuinely colored knot-complement blocks), as s013 already concluded.
No fit; nothing wired; the Lean `loc_matches` gate stays open (evidence, not
proof).

# Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694
# Ref: [lawrence-zagier-1999] https://doi.org/10.4310/AJM.1999.v3.n1.a5
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
import sympy as sp  # noqa: E402
from mpmath import mp, mpf  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Q0 = mpf("1.1099785955541805")           # substrate q₀ (s013 / mckay convention)
P3 = 5                                     # order of the coloured exceptional fibre


def qint_q0(m):
    """[m]_{q₀} balanced quantum integer at the REAL substrate (growing)."""
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


def qdim_root(alpha, k):
    """SU(2) quantum dim of colour α at the k-th Σ(2,3,5) flat (fifth root):
    [α]_k = sin(α k π / 5)/sin(k π / 5), EXACT via sympy."""
    num = sp.sin(sp.pi * alpha * k / P3)
    den = sp.sin(sp.pi * k / P3)
    return sp.simplify(num / den)


def run():
    out = {"q0": float(Q0), "p3_fibre_order": P3}

    # ── McKay value-map target at real q₀ (the 4 classes, marks 1,4,5,6) ──────
    marks = [1, 4, 5, 6]
    dq_target = {1: qint_q0(1), 4: qint_q0(4), 5: qint_q0(5),
                 6: qint_q0(5) + 1}          # split node = [5]_q0 + 1, NOT [6]
    D = mp.sqrt(mp.fsum(v * v for v in dq_target.values()))
    out["target_dq_q0"] = {str(m): float(dq_target[m]) for m in marks}
    out["target_bwS0"] = {str(m): float(dq_target[m] / D) for m in marks}
    out["target_ratios_over_mark1"] = [float(dq_target[m] / dq_target[1]) for m in marks]
    out["split_node_is_qint5_plus_1_not_qint6"] = {
        "qint5_plus_1": float(qint_q0(5) + 1), "qint6": float(qint_q0(6)),
        "distinct": bool(abs((qint_q0(5) + 1) - qint_q0(6)) > mpf("1e-6"))}

    # ── (K1)+(K2) colored fifth-root quantum dims, EXACT, both flats ──────────
    colored = {}
    for k in (1, 2):
        colored[k] = {a: qdim_root(a, k) for a in (1, 2, 3, 4)}
    out["colored_qdim_flat1_exact"] = {str(a): str(colored[1][a]) for a in (1, 2, 3, 4)}
    out["colored_qdim_flat2_exact"] = {str(a): str(colored[2][a]) for a in (1, 2, 3, 4)}
    out["colored_qdim_flat1_float"] = {str(a): float(colored[1][a]) for a in (1, 2, 3, 4)}
    out["colored_qdim_flat2_float"] = {str(a): float(colored[2][a]) for a in (1, 2, 3, 4)}

    # (K1) α=1 anchor: [1]_k = 1 at both flats
    anchor_ok = all(sp.simplify(colored[k][1] - 1) == 0 for k in (1, 2))
    out["K1_alpha1_anchor_is_unit_both_flats"] = bool(anchor_ok)

    # (K2) reflection collapse: [5−α]_k = ±[α]_k ⇒ ≤ 2 independent moduli
    #   flat 1: |[4]| = |[1]|, |[3]| = |[2]|  (D=2 collapse under |·|)
    refl1 = (sp.simplify(sp.Abs(colored[1][4]) - sp.Abs(colored[1][1])) == 0 and
             sp.simplify(sp.Abs(colored[1][3]) - sp.Abs(colored[1][2])) == 0)
    refl2 = (sp.simplify(sp.Abs(colored[2][4]) - sp.Abs(colored[2][1])) == 0 and
             sp.simplify(sp.Abs(colored[2][3]) - sp.Abs(colored[2][2])) == 0)
    indep1 = len({sp.nsimplify(sp.Abs(colored[1][a])) for a in (1, 2, 3, 4)})
    indep2 = len({sp.nsimplify(sp.Abs(colored[2][a])) for a in (1, 2, 3, 4)})
    out["K2_reflection_collapse_flat1"] = bool(refl1)
    out["K2_reflection_collapse_flat2"] = bool(refl2)
    out["K2_independent_moduli_flat1"] = indep1
    out["K2_independent_moduli_flat2"] = indep2
    out["K2_D2_collapse_confirmed"] = bool(refl1 and refl2 and indep1 <= 2 and indep2 <= 2)

    # (K3) bounded-root vs growing-q₀: max fifth-root |[α]_k| = 1/sin(π/5)
    bound = sp.simplify(1 / sp.sin(sp.pi / P3))
    out["K3_root_qdim_bound_1_over_sin_pi5"] = float(bound)
    max_target_ratio = max(out["target_ratios_over_mark1"])
    out["K3_max_target_ratio"] = max_target_ratio
    out["K3_target_exceeds_root_bound"] = bool(max_target_ratio > float(bound))

    # (K4) mark-6 split node: 6 > fibre order 5 ⇒ not a single p₃=5 colour;
    #      the 3⊕3′ two-block insertion 2·[3]_k vs target [5]_q0+1
    two_block1 = float(2 * colored[1][3])       # 2·[3] at flat 1
    two_block2 = float(2 * colored[2][3])
    out["K4_mark6_exceeds_fibre_order"] = bool(6 > P3)
    out["K4_two_block_2x_qdim3_flat1"] = two_block1
    out["K4_two_block_2x_qdim3_flat2"] = two_block2
    out["K4_target_split_value"] = float(dq_target[6])
    out["K4_two_block_reproduces_split"] = bool(
        abs(two_block1 - float(dq_target[6])) < 1e-6 or
        abs(two_block2 - float(dq_target[6])) < 1e-6)

    # overall verdict
    out["verdict_colored_lr_carries_valuemap"] = bool(
        out["K2_D2_collapse_confirmed"] is False and False)  # never: K2 collapses
    out["verdict_scope_a_excluded_at_root"] = bool(
        out["K2_D2_collapse_confirmed"] and out["K3_target_exceeds_root_bound"]
        and not out["K4_two_block_reproduces_split"])
    return out


def report(res):
    print("# s013 Front-2 — colored Lawrence–Rozansky modulus vs McKay value map\n")
    print("## Target (McKay value map at real q₀, marks 1,4,5,6)\n")
    print(f"- d_q₀ on marks: {res['target_dq_q0']}")
    print(f"- ratios over mark 1: {[round(x,4) for x in res['target_ratios_over_mark1']]}")
    print(f"- split node (3,1,1): [5]_q₀+1 = {res['split_node_is_qint5_plus_1_not_qint6']['qint5_plus_1']:.4f}"
          f"  ≠ [6]_q₀ = {res['split_node_is_qint5_plus_1_not_qint6']['qint6']:.4f}: "
          f"**{res['split_node_is_qint5_plus_1_not_qint6']['distinct']}**\n")

    print("## (K1) α=1 anchor: bare vacuum row recovered\n")
    print(f"- [1]_k = 1 at both flats: **{res['K1_alpha1_anchor_is_unit_both_flats']}**\n")

    print("## (K2) D=2 collapse — colouring the p₃=5 fibre does NOT escape it\n")
    print(f"- colored [α] at flat 1 (ζ=e^{{iπ/5}}): {[round(v,4) for v in res['colored_qdim_flat1_float'].values()]}")
    print(f"- colored [α] at flat 2 (ζ=e^{{2iπ/5}}): {[round(v,4) for v in res['colored_qdim_flat2_float'].values()]}")
    print(f"- reflection collapse α=4≡1, α=3≡2 (|·|): flat1 **{res['K2_reflection_collapse_flat1']}**, "
          f"flat2 **{res['K2_reflection_collapse_flat2']}**")
    print(f"- independent moduli: flat1 = {res['K2_independent_moduli_flat1']}, "
          f"flat2 = {res['K2_independent_moduli_flat2']}  ⇒ D=2 collapse: "
          f"**{res['K2_D2_collapse_confirmed']}**\n")

    print("## (K3) bounded fifth-root vs growing real-q₀\n")
    print(f"- max |[α]_k| at fifth root = 1/sin(π/5) = {res['K3_root_qdim_bound_1_over_sin_pi5']:.4f}")
    print(f"- max target ratio = {res['K3_max_target_ratio']:.4f} "
          f"(> root bound: **{res['K3_target_exceeds_root_bound']}**)")
    print("  ⇒ the target ratio-vector is a REAL-q₀ (growing) object; the root modulus cannot reach it.\n")

    print("## (K4) split node / mark-6 obstruction\n")
    print(f"- mark 6 > fibre order 5 ⇒ not a single p₃=5 Wilson colour: **{res['K4_mark6_exceeds_fibre_order']}**")
    print(f"- 3⊕3′ two-block 2·[3]_k = {res['K4_two_block_2x_qdim3_flat1']:.4f} (flat1), "
          f"{res['K4_two_block_2x_qdim3_flat2']:.4f} (flat2) vs target [5]_q₀+1 = "
          f"{res['K4_target_split_value']:.4f}: reproduces = **{res['K4_two_block_reproduces_split']}**\n")

    print("## VERDICT\n")
    print(f"- colored-LR-at-Σ(2,3,5)-root carries the value map: "
          f"**{res['verdict_colored_lr_carries_valuemap']}**")
    print(f"- scope-(a) EXCLUDED at the fibre root (K2+K3+K4): "
          f"**{res['verdict_scope_a_excluded_at_root']}**")
    print("  Refines (does not contradict) the ledger: the genuine open object is the")
    print("  **q₀-continuation** — [mark]_q₀ (growing) is the value map; the root-level")
    print("  modular object is D=2/bounded and cannot be it. A carrier, if any, is a")
    print("  Habiro/q₀-continued or larger-D geometric family. No fit; nothing wired.")


def main():
    res = run()
    report(res)
    w = WitnessBuilder("keystone-colored-lr-modulus-s013", engine="sympy")
    w.set_description(
        "s013 Front-2: the COLORED Lawrence-Rozansky modulus vs the McKay value map. "
        "Colours the p3=5 fibre of the machine-validated Sigma(2,3,5) S-matrix "
        "(keystone_valuemap_genuine_smatrix_s013, cited) by a Wilson line alpha=1..4 and "
        "computes the fifth-root quantum dims [alpha]_k = sin(alpha k pi/5)/sin(k pi/5) at "
        "both flat connections EXACTLY. K1: alpha=1 recovers the unit anchor. K2: reflection "
        "alpha=4=1, alpha=3=2 collapses to <=2 independent moduli per flat -> colouring the "
        "p3=5 fibre does NOT escape the D=2 vacuum row. K3: |[alpha]_k| <= 1/sin(pi/5)=1.7013 "
        "while the target ratios (1,[4]_q0,[5]_q0,[5]_q0+1)~(1,4.11,5.22,6.22) grow past it -- "
        "the value map is a REAL-q0 growing object, not a root-level modulus. K4: mark 6 "
        "(electron split node) exceeds the fibre order 5, and the 3+3' two-block 2[3]_k~3.24 "
        "does not reproduce the target [5]_q0+1=6.22 ('[6]_zeta vs [5]_zeta+1' criterion). "
        "Verdict: colored-LR-at-Sigma(2,3,5)-root is scope-(a) EXCLUDED as the value-map "
        "carrier; refines (not contradicts) the ledger -- the genuine open object is the "
        "q0-continuation. No fit; nothing wired; Lean loc_matches gate stays open."
    )
    for k, v in res.items():
        w.add_data(k, v)
    w.add_assertion(
        "colored_lr_at_root_scope_a_excluded_as_valuemap_carrier",
        computed=1 if res["verdict_scope_a_excluded_at_root"] else 0,
        expected=1, tolerance=0,
        source="Exact fifth-root arithmetic: colouring the p3=5 fibre reflection-collapses to "
               "D=2 (K2), is bounded by 1/sin(pi/5) < the growing target ratios (K3), and the "
               "mark-6 split node is outside the single-fibre colour range with 2[3] != [5]_q0+1 "
               "(K4). The value map [mark]_q0 is a real-q0 growing object; the Sigma(2,3,5) "
               "root-level colored modulus cannot be it. Scope-(a): this specific root-level "
               "construction; the q0-continuation remains the genuine open gap.",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
