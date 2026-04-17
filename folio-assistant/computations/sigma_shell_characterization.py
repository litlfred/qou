#!/usr/bin/env python3
"""
σ_shell characterization via LP-dual + Young's lattice (branching rule).

Per user: σ_shell parameters are NOT new parameters but derived from:
  (a) LP-dual shadow price at shell partition (A_magic - 1, 1)
  (b) skew-SYT branching at the shell level

σ_shell in H_{A_magic}(q) at the standard rep (A_magic - 1, 1) has
SAME Hecke eigenvalues (q, -q⁻¹) as any σ.  The "shell" character is:

  1. POSITION: placed at shell-boundary generators (gens 3·A_magic_cumulative - 1)
  2. WEIGHT: LP-dual shadow price at shell-partition (A_magic-1, 1)
  3. MULTIPLICITY: ILP at level 4 — # crossings per shell boundary

Contribution to atom tower mass:
  Δ𝔪_shell = z² · Φ_q(|V̂_shell|²) · y_shell(q) · f^{λ_atom/(A_magic-1,1)}

where y_shell(q) is the LP shadow price and f the skew-SYT count.
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import q0 as q0_f, qi0 as qi_f, z_mark, HA as h

MAGIC = [2, 8, 20, 28, 50, 82, 126]
mpmath.mp.dps = 50
q0 = mpmath.mpf(str(q0_f))
qi = 1 / q0


def q_int_mp(k):
    """q-integer [k]_q at q_0."""
    if k == 0:
        return mpmath.mpf(0)
    return (q0 ** k - qi ** k) / (q0 - qi)


def q_fact_mp(n):
    r = mpmath.mpf(1)
    for k in range(1, n + 1):
        r *= q_int_mp(k)
    return r


def classical_dim(partition, n):
    """d_λ via hook-length formula."""
    hooks = []
    for i, rl in enumerate(partition):
        for j in range(rl):
            arm = rl - j - 1
            leg = sum(1 for r2 in range(i + 1, len(partition))
                      if partition[r2] > j)
            hooks.append(arm + leg + 1)
    num = math.factorial(n)
    den = 1
    for hh in hooks:
        den *= hh
    return num // den if den > 0 else 0


def q_dim(partition, n):
    """d_q(λ) via q-hook formula."""
    hooks = []
    for i, rl in enumerate(partition):
        for j in range(rl):
            arm = rl - j - 1
            leg = sum(1 for r2 in range(i + 1, len(partition))
                      if partition[r2] > j)
            hooks.append(arm + leg + 1)
    num = q_fact_mp(n)
    den = mpmath.mpf(1)
    for hh in hooks:
        den *= q_int_mp(hh)
    return num / den if abs(den) > 0 else mpmath.mpf(0)


def partitions_of(n):
    """All partitions of n."""
    if n == 0:
        return [()]
    out = []
    def rec(rem, mx, cur):
        if rem == 0:
            out.append(tuple(cur))
            return
        for p in range(min(rem, mx), 0, -1):
            rec(rem - p, p, cur + [p])
    rec(n, n, [])
    return out


def shadow_price_at_partition(partition, k):
    """Generic shadow price y_λ at partition λ ⊢ k."""
    d_cl = classical_dim(partition, k)
    if d_cl == 0:
        return None
    d_q_lam = q_dim(partition, k)
    kq_fact = q_fact_mp(k)
    w_lam = (d_q_lam ** 2) / kq_fact
    y = w_lam / d_cl - 1 / kq_fact
    return {
        "partition": partition,
        "classical_dim": d_cl,
        "q_dim": d_q_lam,
        "wedderburn_weight": w_lam,
        "shadow_price_y": y,
        "shadow_price_abs": abs(y),
        "q_factorial_k": kq_fact,
    }


def maximal_weight_partition(A):
    """Find partition λ ⊢ A with maximal Wedderburn weight w_λ = d_q²/[A]_q!."""
    parts = partitions_of(A)
    best = None
    best_w = mpmath.mpf(0)
    for p in parts:
        w = (q_dim(p, A) ** 2) / q_fact_mp(A)
        if w > best_w:
            best_w = w
            best = p
    return best, best_w


def shell_shadow_price(A_magic, partition=None):
    """Shell shadow price at a GIVEN partition (default (A_magic-1, 1))."""
    if partition is None:
        partition = (A_magic - 1, 1)
    k = A_magic
    data = shadow_price_at_partition(partition, k)
    if data is None:
        return {"A_magic": A_magic, "error": "d_cl = 0"}
    return {
        "A_magic": A_magic,
        "shell_partition": partition,
        "classical_dim": data["classical_dim"],
        "q_dim": str(data["q_dim"]),
        "wedderburn_weight": str(data["wedderburn_weight"]),
        "shadow_price_y": str(data["shadow_price_y"]),
        "shadow_price_abs": str(data["shadow_price_abs"]),
        "q_factorial_A_magic": str(data["q_factorial_k"]),
    }


def shell_sigma_parameters():
    """σ_shell (c, d) parameters — same as any σ in the Hecke algebra.

    Per user insight: σ_shell is NOT a new-parameter operator. It has
    the standard Hecke eigenvalues (q, -q⁻¹) inherited from the
    (A_magic - 1, 1) standard rep of H_{A_magic}(q).

    What's different: POSITION (shell boundary) and ILP MULTIPLICITY.
    """
    return {
        "c": 1,
        "d": 0,
        "eigenvalues": "(q, -q⁻¹) in the (A-1, 1) standard rep",
        "comment": ("σ_shell has the same Hecke parameters as any σ. "
                    "The shell structure is encoded via POSITION "
                    "(shell-boundary generator) and LP-dual WEIGHT "
                    "(shell_shadow_price at the shell partition)."),
    }


def shell_position(A_magic):
    """Generator position of the shell boundary in the atom braid.

    For atom with A nucleons (on 3A strands), the shell at magic A_magic
    has its boundary at the generator separating the first A_magic
    nucleons from the rest.  Strand indices 3·A_magic - 1 and 3·A_magic
    are the boundary, so the inter-shell generator is at position
    3·A_magic - 1 (zero-indexed).
    """
    return 3 * A_magic - 1


def shell_contribution(atom_Z, atom_N, A_magic):
    """Shell-closure contribution to atom Markov trace at level 4.

    Contribution is the product of:
      - Shell position: gen at 3·A_magic - 1 (if within atom span)
      - σ_shell eigenvalue (q or -q⁻¹) in std rep, multiplied by
        integer multiplicity m_shell (ILP at level 4)
      - LP-dual shadow price weight y_shell(A_magic)
      - Branching weight from Young tableaux

    For first-cut: report the shadow-price magnitude times the
    bare σ contribution as the level-4 correction.
    """
    A = atom_Z + atom_N
    if A_magic > A:
        return {"applicable": False, "reason": "A_magic > A"}
    sp_data = shell_shadow_price(A_magic)
    y_abs = mpmath.mpf(sp_data["shadow_price_abs"])
    # Bare σ_shell contribution: (c·q + d) = q with (c, d) = (1, 0)
    sigma_shell_eval = q0  # std rep eigenvalue = q
    contribution = y_abs * sigma_shell_eval
    return {
        "applicable": True,
        "A_magic": A_magic,
        "A": A,
        "shell_position_gen": shell_position(A_magic),
        "sigma_shell_eval": str(sigma_shell_eval),
        "shadow_price_y_abs": sp_data["shadow_price_abs"],
        "bare_contribution": str(contribution),
        "shell_data": sp_data,
    }


if __name__ == "__main__":
    print("σ_SHELL CHARACTERIZATION (3 approaches)")
    print("=" * 80)
    print(f"q_0 = {q0}, precision = {mpmath.mp.dps} digits")
    print()
    print("Target binding scale: B_AME/(A·938) ≈ 0.009 (0.9% of rest mass)")
    print("→ expect y_shell ~ 10⁻³ to 10⁻² for physical binding")
    print()

    print("APPROACH 1: (A-1, 1) partition")
    print(f"  {'A_magic':>8} {'partition':>12} {'|y|':>14}")
    for A_m in [2, 8, 20, 28]:
        d = shell_shadow_price(A_m)
        print(f"  {d['A_magic']:>8d} {str(d['shell_partition']):>12} "
              f"{float(mpmath.mpf(d['shadow_price_abs'])):>14.4e}")
    print("  → Too small; shadow price drops exponentially.")
    print()

    print("APPROACH 3: Maximal-weight partition (argmax w_λ)")
    print(f"  {'A_magic':>8} {'argmax partition':>25} {'w_max':>14} {'|y|':>14}")
    max_wt_data = []
    for A_m in [2, 8, 20]:
        best_p, best_w = maximal_weight_partition(A_m)
        y_data = shadow_price_at_partition(best_p, A_m)
        print(f"  {A_m:>8d} {str(best_p):>25} "
              f"{float(best_w):>14.4e} "
              f"{float(y_data['shadow_price_abs']):>14.4e}")
        max_wt_data.append({
            "A_magic": A_m, "partition": str(best_p),
            "w_max": str(best_w),
            "y_abs": str(y_data["shadow_price_abs"]),
        })
    print()

    print("ENUMERATION: all partitions at each magic A, find y in physical range")
    print("(physical range: 10⁻³ to 10⁻¹)")
    enum_data = {}
    for A_m in [2, 8, 20]:
        print(f"\nA_magic = {A_m}:")
        parts = partitions_of(A_m)
        candidates = []
        for p in parts:
            y_data = shadow_price_at_partition(p, A_m)
            if y_data is None:
                continue
            y_abs = float(y_data["shadow_price_abs"])
            if 1e-4 < y_abs < 1e0:
                candidates.append((p, y_abs, float(y_data["wedderburn_weight"])))
        # Sort by |y| descending
        candidates.sort(key=lambda x: -x[1])
        print(f"  {'partition':>25} {'|y|':>14} {'w_λ':>14}")
        for p, y, w in candidates[:8]:  # top 8 by |y|
            print(f"  {str(p):>25} {y:>14.4e} {w:>14.4e}")
        enum_data[A_m] = [{"partition": str(p), "y_abs": y, "w_lam": w}
                           for p, y, w in candidates[:15]]

    # σ_shell parameters
    params = shell_sigma_parameters()
    shell_data = [shell_shadow_price(A_m) for A_m in MAGIC]

    # Atom-level shell contributions
    print("Atom-level shell contributions (for each shell within atom):")
    ATOMS = [
        ("D",    1,  1),
        ("4He",  2,  2),
        ("8Be",  4,  4),
        ("16O",  8,  8),
        ("40Ca", 20, 20),
    ]
    print(f"  {'Atom':>6} {'A':>3} {'A_magic':>8} {'pos':>5} "
          f"{'y_shell_abs':>16} {'σ·y':>16}")
    print("  " + "-" * 70)
    for atom, Z, N in ATOMS:
        for A_m in MAGIC:
            c = shell_contribution(Z, N, A_m)
            if not c.get("applicable"):
                continue
            print(f"  {atom:>6} {Z+N:>3d} {c['A_magic']:>8d} "
                  f"{c['shell_position_gen']:>5d} "
                  f"{float(mpmath.mpf(c['shadow_price_y_abs'])):>16.6e} "
                  f"{float(mpmath.mpf(c['bare_contribution'])):>16.6e}")
        print()

    witness = {
        "computation": "sigma-shell-characterization",
        "description": (
            "σ_shell characterization attempting 3 approaches to identify "
            "the shell partition: (1) (A-1, 1), (3) maximal-weight argmax, "
            "and enumeration. Target y_shell ~ 10⁻³ to 10⁻¹ for physical "
            "binding."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q_0": str(q0), "mpmath_dps": 50},
        "sigma_shell_parameters": params,
        "approach_1_shadow_prices": shell_data,
        "approach_3_maximal_weight": max_wt_data,
        "enumeration_top_by_magnitude": enum_data,
        "magic_numbers": MAGIC,
    }
    out = Path(__file__).parent / "sigma-shell-characterization.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"Witness: {out}")
