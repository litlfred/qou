"""A=3 (³H, ³He) end-to-end validation of the recursion-kernel A-operator at H_9.

The A=3 analogue of `a_operator_recursive_he4_crosscheck.py`. It is the
closure-(b) STEP 3 "H_9 universality" case named in
`docs/audits/2026-06-16-categorical-interface-operator-closure-b-design.md`:
the categorical interface operator `A^λ_{ξν}(I) = Π_{ξν} ρ_λ(I) Π_{ξν}` peels the
last nucleon (an H_3 block) off the canonical A=3 atom word and reconstructs the
production binding observable `tr_M = Σ_λ y_λ χ^λ` — the case the *fitted*
least-squares extract (`A_operator_extract_at_level.py`) misses by 21–42 %.

Two checks per nucleus (³H = (Z,N)=(1,2), ³He = (2,1)):

  (a) per-λ combiner χ^λ vs direct `young_seminormal.chi_young` on the *same*
      A=3 word — the airtight, construction-internal check (exact, ≪ 1e-25);
  (b) end-to-end `tr_M = Σ_λ y_λ χ^λ`: combiner vs the canonical fine-Bratteli
      transfer matrix (`reduced_block_kernel.chi_all_lambda_reduced_block`).

Honest framing (mirrors the A=4 crosscheck): this is a *correctness* validation
of the operator-valued combiner — it reproduces the canonical `tr_M`, it does
**not** change the binding value or close the CAL-2-floor residual. Its point is
that the CATEGORICAL recursion is exact at A=3 (no test-word fit), unlike the
rank-deficient fitted extract — confirming the "universal by construction"
property formalized in Lean as `QOU.BraidKnot.InterfaceOperator.trace_block_diagonal`.

H_9 structure (A=3): inner = H_6 (gens σ_0..σ_4), bridge = σ_{3A-4} = σ_5,
block = strands 7,8,9 (gens σ_6,σ_7 → relabelled σ_0,σ_1). Cost: d_λ ≤ 42 over
the 30 partitions of 9 — a few minutes at 50 dps (vs ~25 min for A=4 at H_12).

Run: `python3 a_operator_recursive_a3_crosscheck.py`
"""
import time, mpmath as mp
mp.mp.dps = 60
import a_operator_categorical as aoa
import a_operator_recursive as rec
from young_seminormal import chi_young, standard_tableaux
from mass_at_3A_proper import atom_braid_word_3A
from reduced_block_kernel import chi_all_lambda_reduced_block
from wedderburn_jones_markov import y_lambda_at
from q_parameter import Q as Q0
from lr_coefficients import partitions_of

A = 3
N_INNER = 3 * (A - 1)          # 6  (inner Young factor H_6)
N_BLOCK = 3                    # one nucleon
BRIDGE_GEN = 3 * A - 4         # 5  (σ_5 couples strand 6 to strand 7)
BLOCK_OFFSET = 3 * (A - 1)     # 6  (relabel block gens σ_6,σ_7 → σ_0,σ_1)
TOTAL = 3 * A                  # 9

dps = 50
q = aoa.q0_mp(dps); q_str = mp.nstr(q, dps)


def prod(mats, word):
    M = mp.eye(mats[0].rows)
    for (c, d, g) in word:
        M = M * (mp.mpf(c) * mats[g] + mp.mpf(d) * mp.eye(mats[0].rows))
    return M


def trace_A_kron(Amat, RWx, RBn, d_mu, d_nu):
    # Tr[A . kron(RWx,RBn)] = Σ A[a·d_nu+b, a'·d_nu+b'] RWx[a',a] RBn[b',b]
    s = mp.mpf(0)
    for a in range(d_mu):
        for ap in range(d_mu):
            rwa = RWx[ap, a]
            if rwa == 0:
                continue
            for b in range(d_nu):
                for bp in range(d_nu):
                    rbb = RBn[bp, b]
                    if rbb == 0:
                        continue
                    s += Amat[a * d_nu + b, ap * d_nu + bp] * rwa * rbb
    return s


def reconstruct(Z: int, Nn: int, label: str) -> dict:
    print(f"\n================= {label}  (Z={Z}, N={Nn}) =================", flush=True)
    w = atom_braid_word_3A(Z, Nn)
    # split at the bridge generator that peels the last H_3 block
    idx = next(i for i, (c, d, g) in enumerate(w) if g == BRIDGE_GEN)
    W_inner = w[:idx]
    I_c, I_d, I_g = w[idx]
    assert I_g == BRIDGE_GEN, f"bridge gen mismatch: {I_g} != {BRIDGE_GEN}"
    block = [(c, d, g - BLOCK_OFFSET) for (c, d, g) in w[idx + 1:]]
    # sanity: inner gens < BRIDGE_GEN, block gens (post-relabel) in {0,1}
    assert all(g < BRIDGE_GEN for (_, _, g) in W_inner), "inner word leaks past the bridge"
    assert all(0 <= g < N_BLOCK - 1 + 1 for (_, _, g) in block), "block gens out of range"
    print(f"  W_inner={len(W_inner)}  bridge d={mp.nstr(I_d, 6)}  block={len(block)}", flush=True)

    p6, p3 = partitions_of(N_INNER), partitions_of(N_BLOCK)
    t0 = time.time()
    RW = {xi: prod(aoa.exact_seminormal_matrices(xi, q_str, dps)[0], W_inner) for xi in p6}
    RB = {nu: prod(aoa.exact_seminormal_matrices(nu, q_str, dps)[0], block) for nu in p3}
    print(f"  ρ builds: {time.time() - t0:.1f}s", flush=True)

    t0 = time.time(); chi_comb = {}
    for lam in partitions_of(TOTAL):
        Ablocks = rec.interface_blocks(lam, N_INNER, N_BLOCK, q_str, mp.mpf(I_d), dps)
        s = mp.mpf(0)
        for (xi, nu), info in Ablocks.items():
            s += trace_A_kron(info["A"], RW[xi], RB[nu], info["d_mu"], info["d_nu"])
        chi_comb[lam] = s
    print(f"  combiner all-{len(chi_comb)} χ: {time.time() - t0:.1f}s", flush=True)

    # (a) combiner vs direct chi_young on the same word
    worst_a = mp.mpf(0)
    for lam in partitions_of(TOTAL):
        worst_a = max(worst_a, abs(chi_comb[lam] - chi_young(lam, w, q)))
    print(f"  (a) max|χ_comb − χ_young| (all {len(chi_comb)} λ) = {mp.nstr(worst_a, 6)}", flush=True)

    # (b) end-to-end tr_M: combiner vs transfer reference
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(TOTAL, Q0).items()}
    chi_ref = chi_all_lambda_reduced_block(w, TOTAL, q=None)
    chi_ref = {tuple(k): (v if isinstance(v, mp.mpf) else mp.mpf(str(v)))
               for k, v in chi_ref.items()}
    worst_b = max(abs(chi_comb[k] - chi_ref[k]) for k in chi_comb)
    trM_comb = sum((y[k] * chi_comb[k] for k in chi_comb), mp.mpf(0))
    trM_ref = sum((y[k] * chi_ref[k] for k in chi_ref), mp.mpf(0))
    rel = abs(trM_comb - trM_ref) / abs(trM_ref) if trM_ref != 0 else mp.mpf('nan')
    print(f"  (b) max|χ_comb − χ_transfer| (all {len(chi_comb)} λ) = {mp.nstr(worst_b, 6)}", flush=True)
    print(f"      tr_M_combiner = {mp.nstr(trM_comb, 18)}", flush=True)
    print(f"      tr_M_transfer = {mp.nstr(trM_ref, 18)}", flush=True)
    print(f"      |Δtr_M| = {mp.nstr(abs(trM_comb - trM_ref), 6)}   rel = {mp.nstr(rel, 6)}", flush=True)

    return {
        "label": label, "Z": Z, "N": Nn,
        "max_chi_comb_vs_young": mp.nstr(worst_a, 8),
        "max_chi_comb_vs_transfer": mp.nstr(worst_b, 8),
        "trM_combiner": mp.nstr(trM_comb, 18),
        "trM_transfer": mp.nstr(trM_ref, 18),
        "rel_trM": mp.nstr(rel, 8),
    }


def main() -> int:
    print("=" * 84)
    print("  Categorical A-operator recursion — A=3 H_9 universality (³H, ³He)")
    print("=" * 84)
    results = [reconstruct(1, 2, "³H (triton)"), reconstruct(2, 1, "³He")]

    # PASS criterion: both checks agree with the seminormal/transfer ground truth
    # at the 1e-25 L1 floor (modulo the float64 word-constant convention floor
    # that the A=4 crosscheck documents as ~1e-15 on check (b)).
    A3_TOL_INTERNAL = mp.mpf("1e-25")   # (a): construction-internal, must be exact
    B_CONVENTION_FLOOR = mp.mpf("1e-12")  # (b): float64 atom-word constant floor
    all_ok = True
    print("\n" + "=" * 84)
    for r in results:
        a_ok = mp.mpf(r["max_chi_comb_vs_young"]) < A3_TOL_INTERNAL
        b_ok = mp.mpf(r["max_chi_comb_vs_transfer"]) < B_CONVENTION_FLOOR
        all_ok = all_ok and a_ok and b_ok
        print(f"  {r['label']:<14}  (a) exact={a_ok}  (b) transfer-match={b_ok}  "
              f"rel tr_M={r['rel_trM']}")
    print(f"\n  VERDICT: {'ALL PASS — categorical recursion reproduces tr_M(A=3)' if all_ok else 'FAILURES PRESENT'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
