#!/usr/bin/env python3
"""Probe: casimir-macdonald
(audit support for conj:casimir-epsilon-vacuum, Route A2 via Cherednik DAHA).

**Question.**  Macdonald polynomials P_λ(x; q, t) are the eigenfunctions
of the Macdonald operators Y_i in Cherednik's DAHA framework.  Their
two-parameter (q, t) norms ⟨P_λ, P_λ⟩_{q,t} — given explicitly by the
arm-leg formula — are the natural symmetric-function basis for QOU
Hecke-trace identities and may give access to Cherednik's q-zeta value
at negative integers without implementing the full DAHA machinery.

**Macdonald norm (arm-leg formula).**  For partition λ = (λ_1, λ_2, …):

  ⟨P_λ, P_λ⟩_{q,t}  =  ∏_{s ∈ λ}  (1 − q^{a(s)+1} t^{l(s)})
                                / (1 − q^{a(s)}    t^{l(s)+1})

where for cell s = (i, j) in λ's Young diagram:

  a(s) = arm length  = λ_i − j      (cells to the right of s in row i)
  l(s) = leg length  = λ'_j − i     (cells below s in column j)

**Cherednik-style q-zeta candidates.**  Without a published closed
form for ζ_q^Cher(−3), this probe explores natural combinations:

  ζ_q^Cher^{cand1}(−3)  ?=  Σ_{λ ⊢ 3} ⟨P_λ⟩_{q,t}^{-1}
  ζ_q^Cher^{cand2}(−3)  ?=  Σ_{λ ⊢ 3} ⟨P_λ⟩_{q,t}  / something
  ζ_q^Cher^{cand3}(−3)  ?=  (q,t)-Macdonald sums over |λ| = 3, 4

For each candidate, check raw value AND (× π²/6) against π²/720
(the Casimir prefactor target).

**Specializations of t.**  Macdonald reduces to:
  t = q  → Schur (Hall scalar product trivial; norm = ∏ hook-length)
  t = q² → "Jack-like" deformation
  t = 1  → Hall-Littlewood
  t = q^{1/2}, q^{2/3} → other Hecke-related specializations

This probe tries t ∈ {q, q², q^{1/2}, 1, q^{-1}} at substrate q₀.

Emits `casimir-macdonald-probe.witness.json`.

Ref: [macdonald1995] Macdonald, *Symmetric Functions and Hall
                     Polynomials*, 2nd ed., Oxford Univ. Press
Ref: [cherednik2006] Cherednik, *Double Affine Hecke Algebras*,
                     Cambridge Univ. Press
Ref: [casimir1948]   https://dwc.knaw.nl/DL/publications/PU00018547.pdf
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from mpmath import mp, mpf, pi as mp_pi  # noqa: E402

from q_parameter import Q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50


# ── Partition utilities ────────────────────────────────────────────

def partitions(n: int) -> list[tuple[int, ...]]:
    """All partitions of n in weakly-decreasing-tuple form."""
    if n == 0:
        return [()]
    out = []
    def _gen(remaining, max_part, prefix):
        if remaining == 0:
            out.append(tuple(prefix))
            return
        for k in range(min(remaining, max_part), 0, -1):
            _gen(remaining - k, k, prefix + [k])
    _gen(n, n, [])
    return out


def conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    """Transpose / conjugate of partition lam."""
    if not lam:
        return ()
    return tuple(sum(1 for x in lam if x >= j) for j in range(1, lam[0] + 1))


def arm_leg(lam: tuple[int, ...], i: int, j: int) -> tuple[int, int]:
    """Arm and leg lengths of cell (i, j) in partition lam.

    (i, j) is 0-indexed: row i, column j.
    a(s) = λ_i − j − 1     (number of cells STRICTLY right of s in row)
    l(s) = λ'_j − i − 1    (number of cells STRICTLY below s in column)
    """
    lam_t = conjugate(lam)
    arm = lam[i] - j - 1
    leg = lam_t[j] - i - 1
    return arm, leg


def macdonald_norm(
    lam: tuple[int, ...],
    q: "mpf",
    t: "mpf",
) -> "mpf":
    """⟨P_λ, P_λ⟩_{q,t} via the arm-leg formula.

    Convention: Macdonald's "norm" in the standard (q,t)-symmetric-
    function inner product, equal to
        ∏_{s ∈ λ} (1 − q^{a(s)+1} t^{l(s)}) / (1 − q^{a(s)} t^{l(s)+1}).
    """
    if not lam:
        return mpf(1)
    norm = mpf(1)
    for i, lam_i in enumerate(lam):
        for j in range(lam_i):
            a, l = arm_leg(lam, i, j)
            num = 1 - q ** (a + 1) * t ** l
            den = 1 - q ** a * t ** (l + 1)
            if den == 0:
                return mpf("inf")
            norm *= num / den
    return norm


# ── Cherednik q-zeta candidates ────────────────────────────────────

def cherednik_zeta_negn_candidate1(n: int, q: "mpf", t: "mpf") -> "mpf":
    """Σ_{λ ⊢ n} ⟨P_λ⟩_{q,t}^{-1}."""
    total = mpf(0)
    for lam in partitions(n):
        norm = macdonald_norm(lam, q, t)
        if norm != 0 and abs(norm) < mpf("inf"):
            total += 1 / norm
    return total


def cherednik_zeta_negn_candidate2(n: int, q: "mpf", t: "mpf") -> "mpf":
    """Σ_{λ ⊢ n} ⟨P_λ⟩_{q,t}."""
    total = mpf(0)
    for lam in partitions(n):
        norm = macdonald_norm(lam, q, t)
        if abs(norm) < mpf("inf"):
            total += norm
    return total


def cherednik_zeta_negn_candidate3(n: int, q: "mpf", t: "mpf") -> "mpf":
    """Alternating sum: Σ_{λ ⊢ n} (-1)^{l(λ)+1} ⟨P_λ⟩_{q,t}^{-1}."""
    total = mpf(0)
    for lam in partitions(n):
        norm = macdonald_norm(lam, q, t)
        if norm != 0 and abs(norm) < mpf("inf"):
            sign = mpf(-1) ** (len(lam) + 1)
            total += sign / norm
    return total


def main() -> int:
    builder = WitnessBuilder(
        "casimir-macdonald-probe",
        engine="mpmath",
    )

    q = mpf(Q)
    pi_sq = mp_pi ** 2
    pi_sq_720 = pi_sq / 720
    geom_mult = pi_sq / 6   # standard Casimir geometric factor

    # ─── Macdonald norms for small partitions at substrate ───
    t_specializations = [
        ("t=q  (Schur)", q),
        ("t=q²  (Jack-like)", q ** 2),
        ("t=q^½", mpf(1) ** mpf(0) * q ** mpf("0.5")),
        ("t=1  (Hall-Littlewood)", mpf(1)),
        ("t=q⁻¹", 1 / q),
        ("t=q^{1/3}", q ** mpf("1/3")),
        ("t=q^{2/3}", q ** mpf("2/3")),
    ]

    norms_table = {}
    for t_name, t_val in t_specializations:
        per_partition = {}
        for n in range(1, 6):  # |λ| = 1..5
            for lam in partitions(n):
                norm = macdonald_norm(lam, q, t_val)
                per_partition[str(lam)] = float(norm)
        norms_table[t_name] = per_partition

    # ─── Cherednik q-zeta candidates per (n, t) ───
    candidates = []
    for t_name, t_val in t_specializations:
        for n in [3, 4]:  # n = 3 is the Casimir target, n = 4 sanity
            for c_idx, c_fn in [
                (1, cherednik_zeta_negn_candidate1),
                (2, cherednik_zeta_negn_candidate2),
                (3, cherednik_zeta_negn_candidate3),
            ]:
                try:
                    val = c_fn(n, q, t_val)
                except Exception as e:
                    val = mpf(0)
                    note = f"computation error: {e}"
                else:
                    note = ""
                if not (abs(val) < mpf("inf")):
                    continue
                # Direct candidate (raw value)
                direct_res = abs(val - pi_sq_720) / pi_sq_720
                # Geom-multiplied candidate
                geom_val = abs(val) * geom_mult
                geom_res = abs(geom_val - pi_sq_720) / pi_sq_720
                candidates.append({
                    "form": (
                        f"cand{c_idx}(n={n}, {t_name}): "
                        f"sum_over_λ⊢{n}"
                    ),
                    "raw_value": float(val),
                    "rel_residue_direct": float(direct_res),
                    "geom_mult_value": float(geom_val),
                    "rel_residue_geom_mult": float(geom_res),
                    "note": note,
                })

    # ─── Best matches ───
    sub_one_pct_direct = [
        c for c in candidates
        if c["rel_residue_direct"] < 0.01
    ]
    sub_one_pct_geom = [
        c for c in candidates
        if c["rel_residue_geom_mult"] < 0.01
    ]
    n_sub_one_pct = len(sub_one_pct_direct) + len(sub_one_pct_geom)

    best_direct = min(candidates, key=lambda c: c["rel_residue_direct"])
    best_geom = min(candidates, key=lambda c: c["rel_residue_geom_mult"])

    (
        builder
        .set_description(
            "Empirical Macdonald-norm probe for Casimir prefactor "
            "via Cherednik DAHA-derived candidates.  Computes "
            "Macdonald norm ⟨P_λ, P_λ⟩_{q,t} via the arm-leg "
            "formula for all partitions λ of size 1..5 at substrate "
            "q ≈ 1.110 and seven t-specializations (t=q, q², q^½, "
            "1, q⁻¹, q^{1/3}, q^{2/3}).  Then forms three natural "
            "Cherednik-zeta candidate combinations: "
            "Σ⟨P_λ⟩^{-1}, Σ⟨P_λ⟩, and alternating-sign Σ.  "
            "Tests direct match vs π²/720 AND geometric-multiplier-"
            "applied match vs π²/720.  Reports count of sub-1% "
            "matches.  Null result reinforces sub-problem 3's "
            "genuine open status — even the Macdonald-norm route "
            "doesn't easily yield the Casimir prefactor at substrate."
        )
        .set_content_block("conj:casimir-epsilon-vacuum")
        .add_parameter("substrate_q", float(q))
        .add_parameter("target_pi_sq_720", float(pi_sq_720))
        .add_data(
            "macdonald_norms_per_t_specialization",
            norms_table,
        )
        .add_data("cherednik_candidates", candidates)
        .add_data(
            "best_direct",
            {
                "form": best_direct["form"],
                "raw_value": best_direct["raw_value"],
                "rel_residue": best_direct["rel_residue_direct"],
            },
        )
        .add_data(
            "best_geom_multiplied",
            {
                "form": best_geom["form"],
                "value": best_geom["geom_mult_value"],
                "rel_residue": best_geom["rel_residue_geom_mult"],
            },
        )
        .add_data(
            "sub_one_pct_matches_direct",
            sub_one_pct_direct,
        )
        .add_data(
            "sub_one_pct_matches_geom_multiplied",
            sub_one_pct_geom,
        )
        .add_assertion(
            name="zero_macdonald_candidates_within_one_percent",
            computed=float(n_sub_one_pct),
            expected=0.0,
            tolerance=0.5,
            unit=(
                "count of Macdonald-derived Cherednik-q-zeta "
                "candidates within 1% of π²/720 (across 7 "
                "t-specializations × 3 candidate formulas × 2 "
                "(n=3, n=4) × both direct and geom-mult)"
            ),
            source=(
                "Null assertion for Route A2 via Macdonald.  "
                "Passing this assertion documents that the "
                "Cherednik DAHA framework does NOT yield the "
                "Casimir prefactor π²/720 through any obvious "
                "low-degree Macdonald-norm combination at "
                "substrate q_0."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"Substrate q = {float(q):.10f}")
    print(f"Target π²/720 = {float(pi_sq_720):.8e}")
    print()
    print("─── Macdonald norms ⟨P_λ⟩_{q, t=q} (Schur specialization) ───")
    schur_norms = norms_table["t=q  (Schur)"]
    for n in range(1, 5):
        for lam in partitions(n):
            print(f"  λ = {lam:<14} ⟨P_λ⟩_{{q,t=q}} = {schur_norms[str(lam)]:.6e}")
    print()
    print(f"─── Best DIRECT candidate ───")
    print(f"  form:       {best_direct['form']}")
    print(f"  raw value:  {best_direct['raw_value']:.6e}")
    print(f"  rel residue (raw): {best_direct['rel_residue_direct']:.4e}")
    print()
    print(f"─── Best GEOM-MULTIPLIED (× π²/6) candidate ───")
    print(f"  form:  {best_geom['form']}")
    print(f"  value: {best_geom['geom_mult_value']:.6e}")
    print(f"  rel residue: {best_geom['rel_residue_geom_mult']:.4e}")
    print()
    if n_sub_one_pct > 0:
        print(f"→ {n_sub_one_pct} MATCH(ES) within 1%:")
        for m in sub_one_pct_direct[:5]:
            print(f"  DIRECT: {m['form']} = {m['raw_value']:.4e} (residue {m['rel_residue_direct']:.4e})")
        for m in sub_one_pct_geom[:5]:
            print(f"  GEOM:   {m['form']} = {m['geom_mult_value']:.4e} (residue {m['rel_residue_geom_mult']:.4e})")
    else:
        print("→ NULL RESULT: no Macdonald-derived candidate within 1%.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
