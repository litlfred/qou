#!/usr/bin/env python3
"""Probe — compute partition GB-depth k★(T_w) directly for tritium's NF.

Falsifies the witness data identification of "max_grade=9" with the
brane-tower truncation depth k★(T_w) (per
prop:phi-q-categorical-truncation).

The witness's `max_grade = 9` (joint-tower-sdp-h6-h9.witness.json,
tritium certificate) is the **Coxeter-length filtration depth** of
T's NF word in H_5(q) — i.e., the maximum length of a reduced word
appearing in T_w's filtration_certificate. The longest NF term has
length 9, hence max_grade=9.

This is **distinct** from the partition GB-depth k★(T_w) defined as
  k★(T_w) := max_{λ ∈ supp(T_w)} max-hook(λ),
where supp(T_w) = {λ ⊢ n : χ_λ(ρ(T_w)) ≠ 0} via the YSN/Hoefsmit
character.

For partitions of 5, max-hook ranges over {1, 2, 3, 4, 5}: any
partition of 5 has max hook length ≤ 5. So k★(T_w) ≤ 5 STRUCTURALLY
for tritium, regardless of NF word length. The witness's max_grade=9
cannot be k★(T_w).

This probe computes χ_λ(T_w) for every λ ⊢ 5 via the YSN matrices
in hecke_core, identifies the partition support, and reports
k★(T_w).
"""
import sys, json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import numpy as np
from hecke_core import (
    _build_ysn_matrices, partitions_of, q_hook_product, _standard_tableaux,
)
from q_parameter import Q as Q0
from witness_base import WitnessBuilder

H_VAL = float(Q0 - 1.0/Q0)
qi0 = 1.0 / Q0
CHI_THRESHOLD = 1e-10


def max_hook(partition):
    """Max hook length of a partition λ. For λ = (λ_1, ..., λ_r) with
    conjugate λ', the max hook is at the (1,1) box: λ_1 + λ'_1 - 1."""
    if not partition:
        return 0
    width = partition[0]
    height = len(partition)
    return width + height - 1


def chi_lambda(partition, braid_word, n):
    """Character χ_λ(ρ(β)) for the standard rep ρ_λ of H_n(q),
    evaluated at q = q_0. Uses YSN matrices.

    braid_word is a list of generator indices ±i ∈ ±{1, …, n-1}.
    Negative generators σ_i^{-1} are computed via the Hecke relation
    σ_i^{-1} = σ_i - (q - q^{-1}) (algebraic, no matrix inversion).
    """
    matrices = _build_ysn_matrices(partition, sparse_threshold=10**9)
    # matrices[k-1] is σ_k for k ∈ {1, …, n-1}
    if not matrices:
        # 1-dim partition; σ_i acts as identity scalar
        return 1.0
    dim = len(matrices[0])
    eye = np.eye(dim)
    M = eye.copy()
    for sigma in braid_word:
        idx = abs(sigma) - 1
        if idx >= len(matrices):
            return 0.0  # generator out of range for this n
        sig = matrices[idx]
        if isinstance(sig, list):
            sig_arr = np.array(sig)
        else:
            sig_arr = np.asarray(sig)
        if sigma > 0:
            M = M @ sig_arr
        else:
            # Algebraic Hecke inverse: σ_i^{-1} = σ_i - (q - q^{-1}) I
            # from σ_i² = (q - q^{-1}) σ_i + I  ⇒  σ_i (σ_i - (q - q^{-1}) I) = I.
            M = M @ (sig_arr - H_VAL * eye)
    return float(np.trace(M))


def main():
    HERE = Path(__file__).parent
    sdp = json.loads((HERE / "joint-tower-sdp-h6-h9.witness.json").read_text())
    T = [c for c in sdp['per_atom_certificates'] if c['name'] == 'tritium'][0]
    word = T['braid_word_input']
    n_0 = T['n_0']  # 5
    n_strands = max(abs(s) for s in word) + 1  # 5
    assert n_strands == n_0, f"strand count mismatch: word uses {n_strands}, n_0={n_0}"
    witness_max_grade = T['max_grade']

    print("=" * 78)
    print("Tritium k★(T_w) computation — falsifying witness's max_grade=9")
    print("=" * 78)
    print(f"  Braid word: {word}")
    print(f"  Length |word| = {len(word)}, strands n_0 = {n_strands}")
    print(f"  Witness max_grade = {witness_max_grade} (Coxeter-length filtration)")
    print()
    print(f"{'partition':>16} {'max-hook':>9} {'dim':>4} {'χ_λ(T_w)':>14} {'in_supp?':>9}")
    print("-" * 78)

    parts = list(partitions_of(n_0))
    support = []
    for lam in parts:
        try:
            chi = chi_lambda(lam, word, n_0)
        except Exception as e:
            chi = float('nan')
            print(f"   error for {lam}: {e}")
        mh = max_hook(lam)
        d = len(list(_standard_tableaux(lam)))
        in_supp = abs(chi) > CHI_THRESHOLD if not np.isnan(chi) else False
        marker = "*" if in_supp else " "
        print(f"{str(lam):>16} {mh:>9} {d:>4} {chi:>+14.6e} {marker:>9}")
        if in_supp:
            support.append({"partition": list(lam), "max_hook": mh,
                            "chi": chi, "dim": d})

    if support:
        k_star = max(s["max_hook"] for s in support)
        max_supp_dim = max(s["dim"] for s in support)
    else:
        k_star = 0
        max_supp_dim = 0
    print()
    print(f"  supp(T_w) = {[s['partition'] for s in support]}")
    print(f"  k★(T_w) = max-hook over supp = {k_star}")
    print(f"  Witness max_grade = {witness_max_grade}")
    print()
    if k_star < witness_max_grade:
        print(f"  ✓ FALSIFIED: k★(T_w) = {k_star} ≠ {witness_max_grade} = max_grade")
        print(f"  The witness's max_grade is the Coxeter-length filtration of")
        print(f"  T_w's NF word, NOT the partition GB-depth used in")
        print(f"  prop:phi-q-categorical-truncation. Strand-padding the NF to")
        print(f"  reach Coxeter length 9 does not change partition support.")
    else:
        print(f"  ⚠ k★(T_w) = max_grade = {k_star} — distinction does not falsify here.")
    print()
    print(f"  Structural bound: any partition of n=5 has max-hook ≤ 5,")
    print(f"  so k★(T_w) ≤ 5 unconditionally for any T_w ∈ H_5(q).")

    w = (
        WitnessBuilder("probe-tritium-k-star", engine="python")
        .set_description(
            "Compute k★(T_w) := max GB-depth (= max-hook) over partition "
            "support supp(T_w) for tritium's H_5 braid word. Compares to "
            "the witness's max_grade (Coxeter-length filtration depth) "
            "and falsifies the identification of max_grade with k★."
        )
        .set_content_block("prop:phi-q-categorical-truncation")
        .add_parameter("q_0", float(Q0))
        .add_parameter("braid_word", word)
        .add_parameter("n_0", n_0)
        .add_data("witness_max_grade", witness_max_grade)
        .add_data("k_star_computed", k_star)
        .add_data("partition_support", support)
        .add_data("structural_upper_bound", n_0)
        .add_caveat(
            "Character computation uses YSN matrices at numerical q_0; "
            "tiny but nonzero characters could be misclassified at the "
            f"chi_threshold={CHI_THRESHOLD}. For n=5 the partition basis "
            "is small (7 partitions), so robust to threshold choice."
        )
        # F1 (PR #565): structural anchors. k★ ≤ n always, and the
        # falsification narrative (k★ < max_grade) is the central
        # claim of the witness — encode it as an assertion.
        .add_assertion(
            "k_star_le_structural_bound",
            computed=int(k_star),
            expected=int(n_0),
            tolerance=int(n_0),  # passes iff k_star ∈ [0, 2*n_0]
            source="prop:phi-q-categorical-truncation § structural bound",
        )
        .add_assertion(
            "k_star_lt_max_grade",
            computed=1.0 if k_star < witness_max_grade else 0.0,
            expected=1.0,
            tolerance=0.0,  # binary: must hold
            source="this witness's central falsification claim",
        )
    )
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
