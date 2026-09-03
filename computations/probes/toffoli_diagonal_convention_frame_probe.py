#!/usr/bin/env python3
"""toffoli_diagonal_convention_frame_probe.py — is the q-GoL golden-ratio threshold
a feature of the mathematics, or of convention C?

BEAN qou-3j5m.

WHAT IS BEING TESTED.  `content/.../information-theory/toffoli-transfer-matrix.md`
states the Toffoli diagonal in closed form,

    P_77(q) = (q + q^{1/2} - 1) / (q + 1),

and records that it "vanishes exactly at the golden ratio threshold q = 1/phi^2".
The same block states the traced volume as `V_1 = z(q)*c + d`.  The Markov
parameter `z` is exactly the quantity the owner ruling of 2026-08-15 fixes to
convention D (`z = q^3/(q^2+1)`), convention C (`z = sqrt(q)/(q+1)`) having been
excised.  So: which z is that closed form built from, and does the golden ratio
survive the other one?

THIS IS NOT A PATTERN-MATCH ON `sqrt`.  Half-integer powers are suggestive but not
proof -- a sqrt can enter from a framing factor with nothing to do with z.  The
probe RECONSTRUCTS the closed form from the stated recipe instead, which either
matches identically or does not.

GATES:
  1. P_77 as published == z_C * 1 + (q-1)/(q+1), at several q, to 1e-40.  This is
     what identifies the frame; a near-match would not do.
  2. P_77 as published vanishes at 1/phi^2.
  3. The same recipe with z_D does NOT vanish at 1/phi^2.

SCOPE -- (a), and the boundary matters.  Substituting z_D into the recipe is NOT a
migration, and AGENTS.md says so in terms for the c_k ladder: a z-swap does not
re-derive an object.  The D column below is therefore NOT a claim about what the
convention-D Toffoli diagonal IS.  It establishes only that the golden-ratio root
is NOT INVARIANT under the convention, i.e. that the threshold is a property of
the frame rather than of the gate.  What the D-frame diagonal actually is remains
open, and is content work.

NO-FLOAT64: mpmath end to end at 50 dps; float() appears only inside f-strings.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402 — the mpf, not the float64 `Q`

set_compute_dps(50)

TOL = mp.mpf(10) ** -40


def z_C(q):
    """Convention C, excised 2026-08-09: z = sqrt(q)/(q+1)."""
    return mp.sqrt(q) / (q + 1)


def z_D(q):
    """Convention D, canonical: z = q^3/(q^2+1)."""
    return q ** 3 / (q ** 2 + 1)


def d_pp(q):
    """The control-pair offset d that reproduces the published diagonal."""
    return (q - 1) / (q + 1)


def p77_published(q):
    """P_77(q) = (q + q^{1/2} - 1)/(q + 1), verbatim from the content block."""
    return (q + mp.sqrt(q) - 1) / (q + 1)


def main() -> int:
    print("=" * 88)
    print(" Toffoli diagonal — which convention is its closed form built from?")
    print("=" * 88)

    phi = (1 + mp.sqrt(5)) / 2
    q_golden = 1 / phi ** 2

    # GATE 1 — reconstruct the published closed form from the stated recipe.
    samples = [mp.mpf(s) for s in ("0.4", "0.75", "1.5", "2.0", "3.7")] + [Q0, q_golden]
    worst_C = mp.mpf(0)
    worst_D = mp.inf
    for q in samples:
        worst_C = max(worst_C, abs(p77_published(q) - (z_C(q) + d_pp(q))))
        worst_D = min(worst_D, abs(p77_published(q) - (z_D(q) + d_pp(q))))
    recon_C = worst_C < TOL
    print(f"\n  P_77 published  ==  z_C + (q-1)/(q+1)   over {len(samples)} values")
    print(f"    worst |difference| = {mp.nstr(worst_C, 6)}    identical: {recon_C}")
    print(f"  the same against z_D: SMALLEST |difference| = {mp.nstr(worst_D, 6)}"
          f"   (never identical)")

    # GATE 2/3 — the golden-ratio root, and whether it is frame-invariant.
    p_at_golden_C = p77_published(q_golden)
    root_C_is_golden = abs(p_at_golden_C) < TOL
    p_at_golden_D = z_D(q_golden) + d_pp(q_golden)
    root_D_is_golden = abs(p_at_golden_D) < TOL
    root_D = mp.findroot(lambda q: z_D(q) + d_pp(q), mp.mpf("0.5"))

    print(f"\n  1/phi^2                       = {mp.nstr(q_golden, 20)}")
    print(f"  P_77(1/phi^2), published (C)  = {mp.nstr(p_at_golden_C, 6)}"
          f"   vanishes: {root_C_is_golden}")
    print(f"  same recipe with z_D there    = {mp.nstr(p_at_golden_D, 12)}"
          f"   vanishes: {root_D_is_golden}")
    print(f"  its root instead              = {mp.nstr(root_D, 20)}")
    print(f"  displacement from 1/phi^2     = {mp.nstr(root_D - q_golden, 8)}"
          f"   ({float((root_D - q_golden) / q_golden) * 100:+.1f}% of the C value)")

    # At the substrate anchor: does the STABILITY VERDICT move, or only the number?
    c_at_q0, d_at_q0 = p77_published(Q0), z_D(Q0) + d_pp(Q0)
    print(f"\n  at q0 = {mp.nstr(Q0, 20)}")
    print(f"    published (C frame)  = {mp.nstr(c_at_q0, 12)}   positive: {c_at_q0 > 0}")
    print(f"    same recipe, z_D     = {mp.nstr(d_at_q0, 12)}   positive: {d_at_q0 > 0}")
    print(f"    gap                  = {float((d_at_q0 - c_at_q0) / c_at_q0) * 100:+.1f}%"
          f"  — the VERDICT survives, the NUMBER and the THRESHOLD do not")

    gates_ok = recon_C and root_C_is_golden and not root_D_is_golden

    print("\n" + "=" * 88)
    print(" RESULT")
    print("  * The published Toffoli diagonal IS the z*c + d recipe at z_C, exactly —")
    print("    reconstructed, not inferred from the presence of a square root.")
    print("  * Its golden-ratio zero is therefore a CONVENTION-C feature of that closed")
    print("    form. Under the canonical z it is not a zero at all.")
    print("  * scope-(a): a z-swap is not a migration, so this does NOT say what the")
    print("    D-frame diagonal is. It says the threshold is not frame-invariant, so")
    print("    'vanishes exactly at the golden ratio' cannot be quoted unconditionally.")
    print("=" * 88)

    w = WitnessBuilder("toffoli-diagonal-convention-frame",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("published_P77_reconstructs_from_z_C", 1 if recon_C else 0, 1)
    w.add_assertion("published_P77_vanishes_at_golden_ratio",
                    1 if root_C_is_golden else 0, 1)
    w.add_assertion("z_D_recipe_does_not_vanish_at_golden_ratio",
                    0 if root_D_is_golden else 1, 1)
    w.add_parameter("q0", mp.nstr(Q0, 30))
    w.add_parameter("recipe", "V_1 = z(q)*c + d, c = 1, d = (q-1)/(q+1)")
    w.add_data("worst_abs_diff_vs_z_C", mp.nstr(worst_C, 12))
    w.add_data("smallest_abs_diff_vs_z_D", mp.nstr(worst_D, 12))
    w.add_data("golden_threshold_q", mp.nstr(q_golden, 30))
    w.add_data("z_D_recipe_root", mp.nstr(root_D, 30))
    w.add_data("P77_at_q0_published_C", mp.nstr(c_at_q0, 30))
    w.add_data("P77_at_q0_z_D_recipe", mp.nstr(d_at_q0, 30))
    w.add_caveat(
        "The z_D column is NOT the convention-D Toffoli diagonal. Substituting z_D "
        "into a closed form derived under C is not a migration -- AGENTS.md states "
        "this for the c_k ladder and it applies verbatim here. The column establishes "
        "only that the golden-ratio root is not invariant under the convention. What "
        "the D-frame diagonal is remains open and is content work."
    )
    w.set_description(
        "Reconstructs the published Toffoli diagonal P_77 = (q + q^{1/2} - 1)/(q+1) "
        "from the transfer-matrix block's own recipe V_1 = z*c + d, and finds it is "
        "exactly z_C + (q-1)/(q+1) -- convention C, excised 2026-08-09. Its "
        "golden-ratio zero at q = 1/phi^2 is therefore a C-frame feature: the same "
        "recipe at the canonical z_D has its root at 0.6631 instead, 74% away. At q0 "
        "the two differ by 21% and both stay positive, so the q-GoL stability VERDICT "
        "survives the convention while the threshold and the number do not. scope-(a)."
    )
    w.save()
    return 0 if gates_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
