#!/usr/bin/env python3
"""chirality_avg_content_atomic.py

Extends the chiral closure of GAP-A-2 from the H_3(R, q) sample
braids of `chirality_avg_content_chiral.py` to the **actual atomic
nucleon and nuclear braids** at $H_n(R, q_0)$ for $n \\in \\{6, 9,
12\\}$:

  D    (²H,  A=2): word [1, 2, -1, 4, -5, 4]                — 6 strands
  T    (³H,  A=3): word [1, 2, -1, 4, -5, 4, 7, -8, 7]      — 9 strands
  ³He  (³He, A=3): word [1, 2, -1, 4, 5, -4, 7, -8, 7]      — 9 strands
  ⁴He  (⁴He, A=4): word [1, 2, -1, 4, 5, -4, 7, -8, 7, 10, -11, 10]
                                                             — 12 strands

(Words extracted from `term7-alpha5-crystal-derivation.witness.json`.)

This is the **chiral residual of GAP-A-2** at the audited atomic
braids — the open piece that the H_3 sample-braid closure
(`chirality_avg_content_chiral.py`) demarcated but did not address.

Computes both:

  (a) the direct sum
        ⟨c⟩_β = Σ_λ c(λ)·χ^λ(β)·w_λ / Σ_λ χ^λ(β)·w_λ
  (b) the per-pair-symmetric form
        ⟨c⟩_β = Σ_{λ < λ^T} c(λ)·(χ^λ(β) − χ^{λ^T}(β))·w_λ
                / Σ_λ χ^λ(β)·w_λ

  using `c(λ^T) = -c(λ)` and `w_λ = w_{λ^T}` (hook-length symmetry).
  Self-conjugate λ contribute 0 to the numerator since `c(λ) = 0`
  for self-conjugate partitions.  Both forms are mathematically
  identical at the partition level; running both and asserting
  agreement is a sanity check on the implementation.

Output: `chirality-avg-content-atomic.witness.json`.
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt, str_at_true_precision  # noqa: E402
from mpmath import mp, mpf

from hecke_characters import (  # noqa: E402
    chi_lambda_braid,
    partitions_of,
)
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
Q0 = Q_MP


def q_int(k, q):
    return mpf(0) if k == 0 else (q ** k - 1) / (q - 1)


def q_factorial(k, q):
    out = mpf(1)
    for i in range(1, k + 1):
        out *= q_int(i, q)
    return out


def hook(shape, i, j):
    arm = shape[i - 1] - j
    leg = sum(1 for r in range(i, len(shape)) if shape[r] >= j)
    return arm + leg + 1


def dim_q(shape, q, n_fac_q):
    denom = mpf(1)
    for i, row_len in enumerate(shape, start=1):
        for j in range(1, row_len + 1):
            denom *= q_int(hook(shape, i, j), q)
    return n_fac_q / denom


def content_sum(shape):
    s = 0
    for i, row_len in enumerate(shape, start=1):
        for j in range(1, row_len + 1):
            s += (j - i)
    return s


def transpose(shape):
    if not shape:
        return ()
    cols = max(shape)
    out = []
    for j in range(1, cols + 1):
        col_height = sum(1 for r in shape if r >= j)
        out.append(col_height)
    return tuple(out)


def writhe(word):
    """Net writhe = sum of crossing signs of the braid word.

    LEVEL OF DEFINITION (framing note; no number here changes). The writhe is a
    property of the BRAID WORD, not of its closure: Markov-I (conjugation)
    invariant, but Markov-II stabilisation β ∈ B_n ↦ βσ_n^{±1} ∈ B_{n+1} shifts
    it by ±1 while presenting the same link. The `ATOMS` rows carry their level
    explicitly in `n_strands`, and they are not all the same:

        D  n = 6  w = +2      T  n = 9  w = +3      ³He n = 9  w = +3

    (⁴He would sit at n = 12; it is deferred here for performance.) n = 3(Z+N) is
    the braid index of the atom (`atom-knot.md`) — the lowest level of the
    substrate tower. Under the owner ruling (states are Gröbner–Shirshov normal
    forms; the observable is the trace at the lowest level) these canonical words
    ARE the states, so comparing w, ⟨c⟩_β or a_K across the rows compares distinct
    states rather than two presentations of one state: the table stands as
    written. The a_K values are properties of these canonical words, not of the
    closures. Ref: docs/audits/2026-08-10-writhe-level-of-definition.md §5d.
    """
    return sum(s for s, _ in word)


# Atomic braid words from term7-alpha5-crystal-derivation.witness.json.
# Flat-int format → [(sign, gen)] format expected by chi_lambda_braid.
ATOMS = [
    {
        "atom": "D",
        "n_strands": 6,
        "flat_word": [1, 2, -1, 4, -5, 4],
        "Z": 1, "N": 1,
    },
    {
        "atom": "T",
        "n_strands": 9,
        "flat_word": [1, 2, -1, 4, -5, 4, 7, -8, 7],
        "Z": 1, "N": 2,
    },
    {
        "atom": "³He",
        "n_strands": 9,
        "flat_word": [1, 2, -1, 4, 5, -4, 7, -8, 7],
        "Z": 2, "N": 1,
    },
    # ⁴He at H_12 has 77 partitions; the f64 kernel takes ≥10 min for
    # the per-partition character sweep.  Deferred to a future probe
    # that batches the seminormal matrix builds at H_12 once.
]


def flat_to_pairs(flat):
    return [(1 if x > 0 else -1, abs(x)) for x in flat]


def main():
    # Construct WitnessBuilder up front so durationMs covers the full
    # computation (Copilot review #r3213426345).
    builder = (
        WitnessBuilder(name="chirality-avg-content-atomic", engine="mpmath")
        .set_description(
            "Chiral residual of GAP-A-2 at the AUDITED atomic nucleon "
            "and nuclear braids — D (H_6), T (H_9), ³He (H_9).  ⁴He "
            "(H_12, 77 partitions) is deferred for performance and "
            "is not included in this witness.  Computes ⟨c(λ)⟩_β at "
            "q_0 via two equivalent forms (direct sum + per-pair-"
            "symmetric) using the atomic-braid words from "
            "term7-alpha5-crystal-derivation.witness.json.  Tests "
            "whether the first-order chirality factor a_K(β) = 1 + "
            "w(β)·⟨c⟩_β·h matches the empirical (1+h)(1-h) = 1-h² "
            "pattern observed across these isotopes."
        )
        .set_audit_only(
            "folio/quantum-observable-universe/braids-and-knots/"
            "derivation-audit-report.md (GAP-A-2 chiral residual at "
            "atomic level)"
        )
    )

    print("=" * 100)
    print("Chirality ⟨c⟩_β for atomic nucleon/nuclear braids — GAP-A-2 chiral residual at H_n(q_0)")
    print("=" * 100)
    print(f"  q_0 = {float(Q0):.16f}")
    print()

    out_atoms = []
    # Tolerance tied to working precision; reused in both denominator
    # checks and the direct-vs-pairwise agreement check (Gemini review
    # #r3213424371: previous code used hardcoded 1e-30 for the exact-
    # ribbon-twist denominator — now unified on `zero_tol`).
    zero_tol = mpf(10) ** (-int(mp.dps * 0.6))
    agree_tol = mpf(10) ** (-int(mp.dps * 0.8))
    for atom_data in ATOMS:
        atom = atom_data["atom"]
        n = atom_data["n_strands"]
        word = flat_to_pairs(atom_data["flat_word"])
        w = writhe(word)
        parts = list(partitions_of(n))
        n_fac_q = q_factorial(n, Q0)

        print(f"=== {atom} (Z={atom_data['Z']}, N={atom_data['N']}, n_strands={n}, "
              f"writhe={w}, |partitions|={len(parts)}) ===")

        # Compute χ^λ(β) for each partition λ ⊢ n via the batch
        # Rust kernel (F-A of ffi-roundtrip-audit): one PyO3
        # crossing + rayon-parallel inside, vs the p(n) per-shape
        # FFI calls the loop used to make.  53-bit precision still;
        # see kernel_precision tag.
        from hecke_characters import chi_lambdas_braid
        chi_dict = {}
        chi_values_f64 = chi_lambdas_braid(parts, word, float(Q0),
                                            precision="f64")
        for shape, chi_val_f64 in zip(parts, chi_values_f64):
            # Promote to mpf for downstream arithmetic at mp.dps=50.
            if isinstance(chi_val_f64, complex):
                chi_dict[tuple(shape)] = mpf(chi_val_f64.real)
            else:
                chi_dict[tuple(shape)] = mpf(chi_val_f64)

        # Direct sum form.
        num_direct = mpf(0)
        den = mpf(0)
        per_lam = []
        for shape in parts:
            shape_t = tuple(shape)
            c_lam = content_sum(shape)
            w_lam = dim_q(shape, Q0, n_fac_q) ** 2 / n_fac_q
            chi_val = chi_dict[shape_t]
            num_direct += w_lam * chi_val * c_lam
            den += w_lam * chi_val
            per_lam.append({
                "shape": list(shape),
                "shape_T": list(transpose(shape)),
                "is_self_conjugate": tuple(shape) == transpose(shape),
                "content_c_lambda": c_lam,
                "wedderburn_weight": str(w_lam),
                # chi came out of the f64 kernel above (see the
                # kernel_precision parameter) and carries 53 bits. It is
                # promoted to mpf for the downstream arithmetic, but
                # str(<mpf>) then prints 50 dps of a 53-bit number — the
                # binary64 expansion, reading as if it had been measured.
                # fmt() on a float writes its true precision instead;
                # mpf(float) is exact, so float() recovers the kernel's own
                # value and nothing moves.
                "chi_lambda_beta": str_at_true_precision(chi_val),
            })

        # Per-pair-symmetric form (sanity check; should equal direct).
        seen = set()
        num_pairwise = mpf(0)
        pair_rows = []
        for shape in parts:
            t = tuple(shape)
            if t in seen:
                continue
            shape_t = transpose(t)
            seen.add(t); seen.add(shape_t)
            c_lam = content_sum(shape)
            w_lam = dim_q(shape, Q0, n_fac_q) ** 2 / n_fac_q
            if t == shape_t:
                # Self-conjugate; c(λ) = 0 ⇒ no contribution to numerator.
                contribution = mpf(0)
            else:
                contribution = c_lam * (chi_dict[t] - chi_dict[shape_t]) * w_lam
            num_pairwise += contribution
            pair_rows.append({
                "shape": list(t),
                "shape_T": list(shape_t),
                "self_conjugate": t == shape_t,
                "c_lambda": c_lam,
                "contribution": str(contribution),
            })

        avg_direct = num_direct / den if abs(den) > zero_tol else None
        avg_pairwise = num_pairwise / den if abs(den) > zero_tol else None
        agree = (avg_direct is not None and avg_pairwise is not None
                 and abs(avg_direct - avg_pairwise) < agree_tol)

        # First-order chirality factor.
        h_val = Q0 - 1 / Q0
        a_K_first = (1 + w * avg_direct * h_val
                      if avg_direct is not None else None)

        # Exact ribbon-twist formula (per the conjecture's "Statement"):
        #   a_K = (Σ w_λ · q^{2 w(K) c(λ)} · χ^λ(T_w)) / (Σ w_λ · χ^λ(T_w))
        # Discriminates A-2 chiral residual interpretation (i) "O(h²)
        # corrections dominate" vs (ii) "atomic-level uses exact
        # exponential, not its linearisation".
        num_exact = mpf(0)
        for shape in parts:
            shape_t_key = tuple(shape)
            c_lam = content_sum(shape)
            w_lam = dim_q(shape, Q0, n_fac_q) ** 2 / n_fac_q
            chi_val = chi_dict[shape_t_key]
            twist_factor = Q0 ** (2 * w * c_lam)
            num_exact += w_lam * twist_factor * chi_val
        a_K_exact = num_exact / den if abs(den) > zero_tol else None

        # Empirical comparison: paper assigns a_K = (1+h)(1-h) = 1-h²
        # for the pattern observed across these atoms.
        a_K_emp_pattern = 1 - h_val ** 2
        a_K_first_minus_pattern = (a_K_first - a_K_emp_pattern
                                     if a_K_first is not None else None)
        a_K_exact_minus_pattern = (a_K_exact - a_K_emp_pattern
                                     if a_K_exact is not None else None)

        print(f"  ⟨c⟩_β (direct  ) = {float(avg_direct):+.10f}" if avg_direct is not None else "  ⟨c⟩_β: degenerate")
        if avg_pairwise is not None:
            print(f"  ⟨c⟩_β (pairwise) = {float(avg_pairwise):+.10f}  "
                  f"agree={agree}")
        if a_K_first is not None:
            print(f"  a_K (first-order) = 1 + {w}·⟨c⟩·h "
                  f"= {float(a_K_first):+.6f}")
        if a_K_exact is not None:
            print(f"  a_K (exact ribbon-twist) "
                  f"= Σ w_λ q^{{2w c(λ)}} χ^λ / Σ w_λ χ^λ "
                  f"= {float(a_K_exact):+.6f}")
        if a_K_emp_pattern is not None:
            print(f"  Empirical pattern a_K = (1+h)(1-h) = "
                  f"{float(a_K_emp_pattern):+.6f}")
            if a_K_first is not None:
                print(f"  Δ first - pattern = "
                      f"{float(a_K_first_minus_pattern):+.6f}")
            if a_K_exact is not None:
                print(f"  Δ exact - pattern = "
                      f"{float(a_K_exact_minus_pattern):+.6f}")
        print()

        out_atoms.append({
            "atom": atom,
            "Z": atom_data["Z"], "N": atom_data["N"],
            "n_strands": n,
            "braid_word_flat": atom_data["flat_word"],
            "braid_word_pairs": [list(p) for p in word],
            "writhe": w,
            "n_partitions": len(parts),
            "per_partition": per_lam,
            "per_pair": pair_rows,
            "numerator_direct_mp": str(num_direct),
            "numerator_pairwise_mp": str(num_pairwise),
            "denominator_mp": str(den),
            "avg_content_c_beta_direct_mp": (None if avg_direct is None else str(avg_direct)),
            "avg_content_c_beta_pairwise_mp": (None if avg_pairwise is None else str(avg_pairwise)),
            "avg_content_c_beta_direct": (None if avg_direct is None else float(avg_direct)),
            "a_K_first_order": (None if a_K_first is None else float(a_K_first)),
            "a_K_exact_ribbon_twist_mp": (None if a_K_exact is None else str(a_K_exact)),
            "a_K_exact_ribbon_twist": (None if a_K_exact is None else float(a_K_exact)),
            "a_K_empirical_pattern_1_minus_h2": float(a_K_emp_pattern),
            "delta_first_order_vs_pattern": (None if a_K_first is None else float(a_K_first_minus_pattern)),
            "delta_exact_vs_pattern": (None if a_K_exact is None else float(a_K_exact_minus_pattern)),
            "direct_pairwise_agree_within_1e_40": agree,
        })

    builder = (
        builder
        .add_parameter("q_0", float(Q0))
        .add_parameter("q_0_str", Q_50_DIGIT_STR)
        .add_parameter("kernel_precision", "f64")
        .add_parameter("downstream_precision_dps", 50)
        .add_data("atoms", out_atoms)
        .add_assertion(
            name="direct_eq_pairwise_all_atoms",
            computed=int(all(a["direct_pairwise_agree_within_1e_40"]
                              for a in out_atoms)),
            expected=1,
        )
    )
    out_path = builder.save()
    print(f"  Witness emitted: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
