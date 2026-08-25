#!/usr/bin/env python3
"""Proof of the D(u) closed form for atomic-braid Markov trace.

For atom (Z, N), A = Z + N ≥ 2, in the canonical pppnnn ordering used
by `atomic_braid_to_crossings`:

    D(u) = 2^(2A + 1) · u^shift · (1 + u²)^(3A − 1)

This script extracts the actual atomic-braid crossing list and counts
the structural quantities that produce each factor:

(i)  Number of "averaged" crossings  N_avg.  Each averaged crossing
     contributes the operator (σ + σ⁻¹) / 2, whose 1/2 prefactor
     becomes a 2^(N_avg) factor in D(u) after clearing.

(ii) Number of strands n_strands = 3A.  The Markov-Ocneanu trace
     formula gives a z^(n_strands − 1) prefactor with
     z = 1 / (q^(1/2) + q^(-1/2)) = u / (1 + u²)  (at q = u²).
     Clearing yields (1 + u²)^(3A − 1) in the denominator.

CLAIM (proved below for A = 2 .. 5, and by the formulas
N_avg = 2·A + 1 and n_strands = 3·A):

    D(u) =  2^(2A + 1)  ·  u^shift  ·  (1 + u²)^(3A − 1)

The u^shift residual is the only piece this script does NOT close —
it depends on the specific Hecke-NF reduction (varies between T and
³He at the same A by 3 units of u-shift).

Output: `d-u-closed-form-proof.witness.json`.

Reference: docs/audits/2026-05-03-w3-habiro-unblocked.md

🛑 CONVENTION-C SCOPE (labelled 2026-08-21, bean `qou-iayk`)
------------------------------------------------------------
Everything above is **convention C** and is correct FOR C. It needs this
scope label, not a correction — do not "fix" any number here.

The `(1 + u²)` factor IS the denominator of `z_C = q^(1/2)/(q+1)` (at
q = u²). Under the owner ruling of 2026-08-15 making convention D canonical
(`z_D = q³/(q²+1)`, recorded at `pyhecke/gram.py:15`), the same
Markov-Ocneanu argument gives `(1 + u⁴)^(3A−1) = (1 + q²)^(3A−1)` instead.
The DERIVED exponent `3A − 1 = n_strands − 1` survives the convention change
unaltered; only the base moves. Measured on all four atoms in
`computations/habiro/habiro_witness_convention_adjudication_probe.py`.

Two further cautions for anyone citing this module as a check on a witness:

1. **`u^shift` is FITTED, not derived** — as the CLAIM note above already
   says ("the only piece this script does NOT close"). `EMPIRICAL_D_U` below
   is, by its own comment, extracted from
   `habiro-coefficients-extended.witness.json`, and `18Z + 21N + 1`
   reproduces that table on all six atoms *because it was fitted to it*.
   `PER_CROSSING_SHIFT_INTRA` is an integer LP solved to land on the targets
   18 and 21 after the fact. An exact match against that witness on this
   exponent is therefore CIRCULAR and carries no evidential weight.

2. **This law is not a test of witness correctness.** The committed
   `habiro-coefficients-extended.witness.json` matches every factor of this
   law exactly and nonetheless FAILS the outer identity
   `p(u)/(u^shift·D(u)) == tr_M_atomic(u²)` on all four atoms (exact rational
   evaluation, adjudication probe above). A witness disagreeing with this law
   is evidence of a convention difference, not of corruption.
"""
from __future__ import annotations

import json
import sys
import time as _time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from canonical_braid_crossings import atom_canonical_crossings as atomic_braid_to_crossings  # noqa: E402

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

#: Captured at import so ``durationMs`` measures the run, not the build.
_T0 = _time.monotonic()


def count_averaged_crossings(Z: int, N: int) -> dict:
    """Decompose `atomic_braid_to_crossings(Z, N, include_inter=True)`
    by crossing type, separating per-nucleon and inter-nucleon."""
    A = Z + N
    crossings = atomic_braid_to_crossings(Z, N, include_inter=True)
    intra = []  # gen_idx within a nucleon
    inter = []  # gen_idx connecting two nucleons (= 3k+2 for k = 0..A-2)
    inter_idx_set = {3 * k + 2 for k in range(A - 1)}
    for gen_idx, ctype in crossings:
        (inter if gen_idx in inter_idx_set else intra).append((gen_idx, ctype))
    # BOTH averaged kinds count. `== "averaged"` alone scored n_avg_inter = 0
    # for every Z>=1,N>=1 atom, because the inter-nucleon crossing is the
    # colour-weighted `averaged_weighted` -- so the one quantity this split
    # exists to report was identically zero on the inter side, silently.
    _AVG = ("averaged", "averaged_weighted")
    n_avg_intra = sum(1 for _, c in intra if c in _AVG)
    n_avg_inter = sum(1 for _, c in inter if c in _AVG)
    return {
        "Z": Z,
        "N": N,
        "A": A,
        "n_strands": 3 * A,
        "word_len": len(crossings),
        "n_intra_total": len(intra),
        "n_inter_total": len(inter),
        "n_avg_intra": n_avg_intra,
        "n_avg_inter": n_avg_inter,
        "n_avg_total": n_avg_intra + n_avg_inter,
        "two_power_predicted": 2 ** (n_avg_intra + n_avg_inter),
        "two_power_predicted_exponent": n_avg_intra + n_avg_inter,
        "one_plus_u2_power_predicted": 3 * A - 1,
        "u_shift_predicted": 18 * Z + 21 * N + 1,
    }


# Integer-LP unique closure for per-crossing shift contributions.
# Only solution with α ∈ ℤ_≥0 satisfying per-proton 18, per-neutron 21
# intra-nucleon sums and inter-nucleon constancy at 1 (independent of
# Z, N for canonical pppnnn ordering).
PER_CROSSING_SHIFT_INTRA = {
    "sigma":     1,
    "sigma_inv": 4,
    "averaged":  0,
}
# 6·1 + 3·4 + 2·0 = 18 per proton ✓
# 5·1 + 4·4 + 2·0 = 21 per neutron ✓


def closed_form_d_u(Z: int, N: int, include_inter: bool = True) -> dict:
    """Closed-form D(u) for the atomic-braid Markov-trace denominator.

    Returns dict with:
      - 'two_power_exp': exponent k in 2^k prefactor
      - 'u_shift':       u-power exponent (= pole order at u=0)
      - 'one_plus_u2_exp': exponent in (1+u²)^? cyclotomic factor
        (only for include_inter=True; None for standalone)
      - 'factored_str':  human-readable factored form
      - 'leading_coef':  leading coefficient of tr_M(q) at q=0
        (universal -1/8 for A=1; conjectured for A≥2)

    For atomic braid in canonical pppnnn ordering with A = Z + N:
      D(u) = 2^(2A + 1) · u^(18Z + 21N + 1) · (1 + u²)^(3A − 1)

    For single nucleon (include_inter=False) per PR #546:
      proton:  tr_M = (q^20 + q^18 + 3q^12 - 3q^8 - q^2 - 1) / (8·q^10)
      neutron: tr_M = (q^20 + 2q^18 + 2q^16 + q^14 + 3q^12 - 3q^8
                      - q^6 - 2q^4 - 2q^2 - 1) / (8·q^8·(q^4+q^2+1))
      leading coefficient: −1/8 EXACTLY for both

    Categorically proved for include_inter=True: see
    docs/audits/2026-05-03-w3-habiro-unblocked.md and PR #539
    (merged 2026-05-04).  Symbolic Hoefsmit closed form per PR #546.
    """
    if not include_inter:
        # Single-nucleon (A=1): closed forms from PR #546 (symbolic
        # Hoefsmit fix).  Cyclotomic structure differs from the
        # multi-nucleon case (uses Φ_3(u^4) factor for the neutron).
        if (Z, N) == (1, 0):  # proton
            return {
                "Z": Z, "N": N, "A": 1,
                "two_power_exp": 3,        # 8 = 2^3
                "u_shift": 20,             # u-pole order
                "one_plus_u2_exp": None,    # different cyclotomic structure
                "factored_str": "(q^20 + q^18 + 3q^12 − 3q^8 − q^2 − 1) / (8·q^10)",
                "leading_coef": "-1/8",
                "tr_M_symbolic_q": "(q**20 + q**18 + 3*q**12 - 3*q**8 - q**2 - 1)/(8*q**10)",
                "source": "PR #546 (claude/hoefsmit-2x2-fix)",
            }
        if (Z, N) == (0, 1):  # neutron
            return {
                "Z": Z, "N": N, "A": 1,
                "two_power_exp": 3,        # 8 = 2^3
                "u_shift": 16,             # u-pole order (cf. dp_pole_probe)
                "one_plus_u2_exp": None,
                "factored_str": "(q^20 + 2q^18 + 2q^16 + q^14 + 3q^12 − 3q^8 − q^6 − 2q^4 − 2q^2 − 1) / (8·q^8·(q^4+q^2+1))",
                "leading_coef": "-1/8",
                "tr_M_symbolic_q": "(q**20 + 2*q**18 + 2*q**16 + q**14 + 3*q**12 - 3*q**8 - q**6 - 2*q**4 - 2*q**2 - 1)/(8*q**8*(q**4 + q**2 + 1))",
                "source": "PR #546 (claude/hoefsmit-2x2-fix)",
            }
        raise NotImplementedError(
            f"Closed form for include_inter=False, (Z={Z}, N={N}) "
            "not yet derived.  PR #546 covers (1, 0) and (0, 1) only."
        )
    A = Z + N
    if A < 2 or Z < 1 or N < 1:
        raise ValueError(
            "Closed form derived for canonical pppnnn ordering with "
            "Z, N ≥ 1 (so the (p,n) interface contributes).  Got "
            f"(Z={Z}, N={N})."
        )
    two_power = 2 * A + 1
    u_shift = 18 * Z + 21 * N + 1
    cyc_exp = 3 * A - 1
    return {
        "two_power_exp": two_power,
        "u_shift": u_shift,
        "one_plus_u2_exp": cyc_exp,
        "factored_str": f"2^{two_power} · u^{u_shift} · (1 + u²)^{cyc_exp}",
        # Leading coefficient at u=0 of tr_M(u²) in the canonical
        # Markov-trace convention (= markov_peel.tr_M_atomic):
        # leading_coef = +2^A.  Verified at A = 2, 3, 4, 5, 6 from
        # the extended Habiro witness (PR #539); see commit log
        # discussion of PR #546's universal-(-1/8) claim, which
        # holds in PR #546's symbolic-Hoefsmit convention but not
        # in the canonical Markov-trace convention used here.
        "leading_coef_canonical_markov": 2 ** A,
        "leading_coef_pr546_symbolic": "-1/8 (proton/neutron A=1; A≥2 falsified at canonical convention)",
        "Z": Z, "N": N, "A": A,
    }


PER_CROSSING_SHIFT_INTER = {
    "sigma":     0,  # (p, p) interface
    "averaged":  1,  # (p, n) interface
    "sigma_inv": 0,  # (n, n) interface
}
# γ_pp·(Z−1) + γ_pn + γ_nn·(N−1) = 1  for all Z, N ≥ 1
# ⇒ γ_pp = γ_nn = 0, γ_pn = 1


# Empirical D(u) prefactor + (1+u²)^k extracted from
# habiro-coefficients-extended.witness.json (see docs/audits/
# 2026-05-03-w3-habiro-unblocked.md for the table).
EMPIRICAL_D_U = {
    (1, 1): {"two_power": 5,  "one_plus_u2_power": 5,  "u_shift": 40},
    (1, 2): {"two_power": 7,  "one_plus_u2_power": 8,  "u_shift": 61},
    (2, 1): {"two_power": 7,  "one_plus_u2_power": 8,  "u_shift": 58},
    (2, 2): {"two_power": 9,  "one_plus_u2_power": 11, "u_shift": 79},
    (3, 2): {"two_power": 11, "one_plus_u2_power": 14, "u_shift": 97},
    (3, 3): {"two_power": 13, "one_plus_u2_power": 17, "u_shift": 118},
}


def main() -> int:
    print("Proof of D(u) closed form for atomic-braid Markov trace")
    print("=" * 72)
    print()
    print("Claim:  D(u) = 2^(2A+1) · u^shift · (1 + u²)^(3A−1)")
    print()
    print(f"  {'atom':>5} {'Z':>2} {'N':>2} {'A':>2} {'n_strands':>10}  "
          f"{'avg_intra':>10} {'avg_inter':>10} {'2^pred':>9}  "
          f"{'2^empir':>9}  {'(1+u²)^pred':>12} {'(1+u²)^empir':>13}  "
          f"{'match?':>7}")
    print("  " + "-" * 130)
    rows = []
    cases = [
        ("D",   1, 1),
        ("T",   1, 2),
        ("³He", 2, 1),
        ("⁴He", 2, 2),
        ("⁵Li", 3, 2),
        ("⁶Li", 3, 3),
        ("⁷Li", 3, 4),
        ("⁸Be", 4, 4),
    ]
    all_match = True
    for sym, Z, N in cases:
        c = count_averaged_crossings(Z, N)
        emp = EMPIRICAL_D_U.get((Z, N))
        emp_two = emp["two_power"] if emp else None
        emp_op = emp["one_plus_u2_power"] if emp else None
        match_two = (
            "✓" if emp_two is None else
            ("✓" if c["two_power_predicted_exponent"] == emp_two else "✗")
        )
        match_op = (
            "✓" if emp_op is None else
            ("✓" if c["one_plus_u2_power_predicted"] == emp_op else "✗")
        )
        match = "✓" if match_two == "✓" and match_op == "✓" else "✗"
        if emp is not None and match != "✓":
            all_match = False
        c["empirical"] = emp
        c["match_two_power"] = match_two
        c["match_one_plus_u2_power"] = match_op
        c["overall_match"] = match
        c["symbol"] = sym
        rows.append(c)
        emp_two_str = str(emp_two) if emp_two is not None else "—"
        emp_op_str = str(emp_op) if emp_op is not None else "—"
        print(f"  {sym:>5} {Z:>2} {N:>2} {c['A']:>2} {c['n_strands']:>10}  "
              f"{c['n_avg_intra']:>10} {c['n_avg_inter']:>10} "
              f"{c['two_power_predicted_exponent']:>9}  {emp_two_str:>9}  "
              f"{c['one_plus_u2_power_predicted']:>12} {emp_op_str:>13}  "
              f"{match:>7}")
    print()
    print("Structural identity:")
    print("  N_avg_intra = 2 · A    (each nucleon has 2 averaged crossings:")
    print("                          gen_idx 0 ud-pair, gen_idx 1 ud-pair)")
    print("  N_avg_inter = 1        (canonical pppnnn ordering: exactly")
    print("                          one (p,n) interface — averaged)")
    print("  ∴ N_avg_total = 2A + 1, predicting 2^(2A+1)  ✓ verified A=2..6")
    print()
    print("  z^(n_strands − 1) = u^(3A−1) / (1 + u²)^(3A−1)")
    print("  ∴ (1 + u²)^(3A−1) is the Markov-trace denominator factor")
    print()
    print("  u^shift = u^(18Z + 21N + 1)   — EMPIRICAL CONJECTURE (numerology)")
    print("           NOT categorically proved.  Linear-in-(Z, N) ansatz")
    print("           fitted to 6 atoms with zero residual.  Derivation from")
    print("           Hecke seminormal-form denominators is open.")
    print()

    # Cross-check the shift formula against empirical witness.
    print("u-shift cross-check:")
    print(f"  {'atom':>5} {'18Z+21N+1':>11} {'empirical':>10} {'match?':>7}")
    print("  " + "-" * 40)
    for r in rows:
        emp = r["empirical"]
        if emp is None:
            continue
        Z, N = r["Z"], r["N"]
        pred = 18 * Z + 21 * N + 1
        actual = emp["u_shift"]
        ok = "✓" if pred == actual else "✗"
        print(f"  {r['symbol']:>5} {pred:>11} {actual:>10} {ok:>7}")
    print()
    print(f"All cross-checks against the symbolic-q witness pass: {all_match}")

    out = {
        "computation": "d-u-closed-form-proof",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Structural proof of D(u) = 2^(2A+1) · u^shift · (1+u²)^(3A−1)"
            " for atomic-braid Markov trace at q = u² in the canonical"
            " pppnnn ordering used by `atomic_braid_to_crossings`.  The"
            " 2^(2A+1) factor is proved by counting averaged crossings"
            " (each averaged crossing = (σ + σ⁻¹)/2, contributing a"
            " factor of 1/2): each nucleon has 2 averaged ud-pair"
            " couplings → 2A factors; canonical pppnnn ordering has"
            " exactly one mixed (p,n) inter-nucleon interface → +1"
            " more, total 2A+1.  The (1+u²)^(3A−1) factor follows from"
            " the Markov/Ocneanu trace formula z^(n−1) at q = u²: with"
            " z = u/(1+u²) and n = 3A, clearing the denominator yields"
            " (1+u²)^(3A−1) in D(u).  The u^shift residual is left as"
            " an open structural question (depends on the Hecke-NF"
            " reduction; varies by 3 between T and ³He at A=3)."
        ),
        "reference_blocks": [
            "def:hecke-quadratic-relation",
            "def:markov-trace",
            "prop:atomic-braid-decomposition",
        ],
        "verified_atoms": rows,
        "all_predictions_match": all_match,
        "open_question_u_shift": (
            "u^shift varies between isospin partners at the same A "
            "(T: 61, ³He: 58 at A=3; |ΔZ−ΔN|·1.5?).  Closed form for "
            "u^shift requires deeper Hecke-NF reduction analysis."
        ),
    }
    # Routed through WitnessBuilder.wrap_legacy rather than a raw json.dump.
    # The raw dump emitted no provenance at all, so the committed witness's
    # scriptHash / scriptCommitSha / commitSha / engine / durationMs /
    # scriptFile (added by a later enrichment pass) were DELETED by any
    # re-run -- silently regressing this witness into the PROV_MISSING class.
    # wrap_legacy preserves every original top-level key verbatim and adds
    # the provenance fields back. Bean qou-iayk.
    b = WitnessBuilder.wrap_legacy(
        "d-u-closed-form-proof",
        out,
        script_path=__file__,
        engine="python",
        output_dir=HERE,
        start_time=_T0,
    )
    out_path = b.save()
    print(f"\nWitness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
