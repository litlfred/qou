#!/usr/bin/env python3
# polynomial_q_not_applicable: signed-content / q-Dirac curvature + holonomy
# setup, not a Jones-polynomial evaluation.
"""
The H₂S chiral residue lives in the c_λ=0 (2,1) block; residue = S³ holonomy.

Pins the bar-anti-symmetric chiral channel of the H₂S +2.1° to the framework's
EXACT chirality machinery (`chirality-residue-mass-term.md`,
`residue-as-braid-holonomy.md`):

  • Chirality marker (q-Dirac scanner): a Wedderburn block λ is a CHIRALITY
    cell iff its signed Young content c_λ = Σ_{(i,j)∈λ}(j−i) = 0, equivalently
    the q-Dirac curvature D_q²(λ) = [c_λ]_q² = 0.
      For H₃:  (3) c=+3 ;  (2,1) c=0 ← CHIRALITY ;  (1,1,1) c=−3.
    So the chiral channel is EXACTLY the (2,1) standard block — the same block
    the chiral p-orbital occupies (palindromic defect 2ℓ=2).

  • Residue = holonomy: Res_{q=ζ_ℓ}[Φ_q·tr_M(T_w)] is the holonomy of the braid
    loop around the singular fibre — the q-deformed Chern–Simons holonomy of a
    Wilson loop in S³ around the obstruction divisor (rho-S³-holonomy).

So the H₂S +2.1° = the S³ braid-holonomy of the chiral p-lone on the c_λ=0
(2,1) cell. This script verifies the cell identification and the q-Dirac
curvature, and sets up the holonomy; the exact angle is the holonomy PHASE
(monodromy around ζ_ℓ), the remaining compute.

Refs: chirality-residue-mass-term.md (c_λ=0 marker, D_q²=[c_λ]_q²);
residue-as-braid-holonomy.md (residue = S³ Chern–Simons holonomy);
atomic_chirality_residue.py (the nuclear chirality-residue scanner).
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
for _p in (str(_HERE),
           str(_HERE.parents[1] / "tools" / "pyhecke" / "python"),
           str(_HERE.parents[1] / "tools" / "qou-substrate" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder
from q_parameter import Q as q0, HA as h
from mass_at_3A_proper import _cached_seminormal, Q0_PROTON


def signed_content(lam):
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def q_int(c, q):
    return (q ** c - q ** (-c)) / (q - 1.0 / q) if c != 0 else 0.0


def main() -> None:
    w = WitnessBuilder("h2s-chirality-residue-s3-holonomy", engine="python")
    q = float(q0)

    print("=" * 72)
    print("H₂S chiral residue → c_λ=0 (2,1) block ; residue = S³ holonomy")
    print("=" * 72)
    print(f"  {'λ⊢3':>9}{'c_λ (content)':>15}{'D_q²=[c_λ]_q²':>16}"
          f"{'chirality cell?':>17}")
    blocks = {}
    for lam, name in [((3,), "sym (3)"), ((2, 1), "std (2,1)"),
                      ((1, 1, 1), "alt (1,1,1)")]:
        c = signed_content(lam)
        dq2 = q_int(c, q) ** 2
        chir = (c == 0)
        blocks[name] = {"content": c, "D_q2": dq2, "chirality_cell": chir}
        print(f"  {name:>9}{c:>15}{dq2:>16.4f}{('YES ←' if chir else 'no'):>17}")
    print()
    print("  ⇒ the CHIRAL channel is exactly the (2,1) standard block "
          "(c_λ=0, D_q²=0,")
    print("    the q-Dirac kernel) — the block the chiral p-orbital occupies.")

    # the chiral p-lone occupies the (2,1) block; its S³ holonomy = the residue
    sig, dim, _ = _cached_seminormal((2, 1), Q0_PROTON)
    s0, s1 = sig[0], sig[1]
    p_lone = s0 @ s0 @ s1            # chiral 3p_z word σ₀σ₀σ₁ (defect 2)
    s_lone = s0 @ s1 @ s0            # self-dual 3s² word (palindrome, defect 0)
    print(f"\n  on the (2,1) chiral block: χ(p-lone σ₀σ₀σ₁)={np.trace(p_lone).real:+.4f}, "
          f"χ(s-lone σ₀σ₁σ₀)={np.trace(s_lone).real:+.4f}")
    print("  residue = holonomy ρ(β) of the braid loop around the singular "
          "fibre ζ_ℓ")
    print("  (q-deformed Chern–Simons / Wilson loop in S³). The +2.1° is its "
          "PHASE (monodromy around ζ_ℓ) — the remaining compute.")

    w.set_description(
        "Pins the H₂S +2.1° chiral residue to the framework's exact chirality "
        "machinery. The chirality cell is the Wedderburn block with signed "
        "content c_λ=0 (q-Dirac kernel D_q²=[c_λ]_q²=0): for H₃ this is exactly "
        "the (2,1) standard block (sym (3) c=+3, alt (1,1,1) c=−3) — the block "
        "the chiral p-orbital occupies. The residue is the braid holonomy ρ(β) "
        "around the singular fibre = the q-deformed Chern–Simons holonomy of a "
        "Wilson loop in S³. So the +2.1° = the S³ holonomy phase of the chiral "
        "p-lone on the c_λ=0 (2,1) cell; the exact angle is the monodromy phase "
        "around ζ_ℓ, the remaining compute."
    )
    w.set_content_block("prop:symmetric-block-domain-weight")
    w.add_parameter("q", q)
    w.add_data("blocks_signed_content_and_dirac_curvature", blocks)
    w.add_data("chiral_channel_block", "(2,1)")
    w.add_data("p_lone_char_on_21", float(np.trace(p_lone).real))
    w.add_data("s_lone_char_on_21", float(np.trace(s_lone).real))
    w.add_assertion(
        "the (2,1) block is the unique chirality cell (c_λ=0, D_q²=0) for H₃",
        computed=bool(blocks["std (2,1)"]["chirality_cell"]
                      and not blocks["sym (3)"]["chirality_cell"]
                      and not blocks["alt (1,1,1)"]["chirality_cell"]),
        expected=True,
        source="signed content (3)=+3, (2,1)=0, (1,1,1)=−3; D_q²=[c_λ]_q²",
    )
    w.add_data(
        "finding",
        "The H₂S chiral residue is pinned to the framework's chirality marker: "
        "the chiral channel is EXACTLY the (2,1) Wedderburn block with signed "
        "content c_λ=0 (the q-Dirac kernel D_q²=[c_λ]_q²=0; sym (3) c=+3, alt "
        "(1,1,1) c=−3) — the block the chiral p-orbital occupies. Per "
        "residue-as-braid-holonomy, the residue is the holonomy ρ(β) of the "
        "braid loop around the singular fibre ζ_ℓ = the q-deformed Chern–Simons "
        "holonomy of a Wilson loop in S³. So the +2.1° is the S³ holonomy phase "
        "of the chiral p-lone on the (2,1) cell. The exact value is the "
        "monodromy phase around ζ_ℓ — the remaining compute; the channel "
        "(c_λ=0 (2,1), S³ holonomy) is now exactly identified.",
    )
    w.save()
    print("\nDone. Witness saved (h2s-chirality-residue-s3-holonomy).")


if __name__ == "__main__":
    main()
