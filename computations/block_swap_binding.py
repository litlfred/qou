#!/usr/bin/env python3
"""Task 1 — exact block-swapped bound symmetrization S_atom for ⁴He (S₂×S₂).

#2103 found (`symmetrized_binding_probe.py`) that the identical-nucleon
symmetrization factor CANCELS in the log-ratio binding IF the bound symmetrization
S_atom equals the free S_free — so the binding signal is the RESIDUAL
log(S_free/S_atom). The orbit identity (`atom_orbit_reduction.py`) does NOT give
S_atom: it proves tr_M is invariant under RELABELING (σ leaves the word
p…pn…n unchanged ⇒ conjugation, Markov M1). The Young SYMMETRIZER instead
COMPOSES the block-swap braid β_σ:

    S_atom · tr_atom = tr_atom_sym = |G|⁻¹ Σ_{σ∈S_Z×S_N} tr_M(W_atom · β_σ)

with β_σ the positive permutation braid swapping nucleon blocks (3 strands each).
The bonds make tr_M(W_atom·β_σ) ≠ tr_M(W_atom) for σ≠id — that residual IS the
binding-relevant content. This computes it for ⁴He: G = S₂×S₂ (4 block-perms:
id, swap-protons [0,1,2]↔[3,4,5], swap-neutrons [6,7,8]↔[9,10,11], swap-both),
sign-only convention (Rust chi_q_via_gp, matches the matrix-M backend; the
averaged-binding convention is the slow-path refinement).

Cross-check: the FREE version (no bonds, include_inter=False) must reproduce the
Frobenius cycle product — tr_M(W_free·β_swap_p) = tr_M(B_p²)·τ_p^0·(neutron part),
so S_free recomputed here matches `symmetrized_constituent_general` h₂/e₂.

Output: block-swap-binding.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from per_irrep_pole_atom import parts_of  # noqa: E402
from tr_m_wenzl_bridge_mpfr import _load_y_lambda  # noqa: E402
import pyhecke_native as _ph  # noqa: E402 — batched GP entry point
from derived_chi_catalogue_matrix_m_mpfr import chi_rust_at_q_mpf  # noqa: E402,F401
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


def signonly_word(Z: int, N: int, include_inter: bool) -> list[tuple[int, int]]:
    """Atom braid word as sign-only (sign, gen_1based) pairs (chi_q_via_gp form)."""
    triples = atom_braid_word_3A(Z, N, include_inter=include_inter)
    return [(1 if c >= 0 else -1, g + 1) for (c, _d, g) in triples]


def _block_swap_perm(s: int, m: int, n: int) -> list[int]:
    """One-line permutation swapping adjacent size-m blocks at s and s+m."""
    perm = list(range(n))
    for p in range(s, s + m):
        perm[p] = p + m
    for p in range(s + m, s + 2 * m):
        perm[p] = p - m
    return perm


def _apply(word_gens: list[int], n: int) -> list[int]:
    """Permutation realized by a 0-based adjacent-transposition word (perm[i]=pos of i)."""
    arr = list(range(n))
    for j in word_gens:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    pos = [0] * n
    for idx, strand in enumerate(arr):
        pos[strand] = idx
    return pos


def block_swap_word(s: int, m: int, n: int) -> list[int]:
    """Reduced word (0-based gens) for the block swap — SELF-VERIFIED vs the perm."""
    target = _block_swap_perm(s, m, n)
    inv = [0] * n
    for i, t in enumerate(target):
        inv[t] = i                       # inv[pos] = strand that belongs at pos
    cur = list(range(n))
    word: list[int] = []
    for pos in range(n):
        ci = cur.index(inv[pos])
        while ci > pos:
            cur[ci], cur[ci - 1] = cur[ci - 1], cur[ci]
            word.append(ci - 1)
            ci -= 1
    assert _apply(word, n) == target, "block-swap braid does not realize the block perm"
    return word


def _two_row_shapes(n: int, y_table) -> list[tuple[int, ...]]:
    """The shapes that can contribute: two-row, and present in y_table.

    The restriction is EXACT, not a tolerance. `QOU.MassTheory
    .TwoRowCapDerived.traceSum_eq_twoRow_of_wenzl` (sorry-free, `#print
    axioms` clean) proves that restricting `Σ_λ y_λ χ_λ` to `ℓ(λ) ≤ 2` is
    an identity under convention D (Wenzl level r = 2), for ARBITRARY `χ` —
    the dropped terms die through the weight, so nothing depends on which
    observable is summed. `threeRowPart_eq_zero_of_wenzl` states the
    residual is `0`, not "small".

    The `y_table.get(st) is None` guard this replaces could never fire:
    `_load_y_lambda(12, ·)` returns all 77 shapes as nonzero, the two-row
    ones at 2.3e-4 … 4.0e-3 and the other 70 topping out at 1.03e-73 —
    solver residue against a value the Lean says is exactly zero. Without
    a row test the loop computed 77 characters where 7 carry the answer.
    """
    return [tuple(sh) for sh in parts_of(n)
            if len(tuple(sh)) <= 2 and y_table.get(tuple(sh)) is not None]


def tr_M_of_word(word: list[tuple[int, int]], n: int, y_table, q) -> mp.mpf:
    """tr_M(word) = Σ_λ y_λ · χ_λ(word) at q₀ (sign-only, Rust GP path).

    Uses the SEMINORMAL mpfr engine, not the Geck–Pfeiffer path.

    GP searches for minimal-length class representatives (cyclic-shift
    completion) and that search has a cliff in word length. Measured here,
    batched and restricted to the same seven shapes:

        |word|      GP                   seminormal
          47        0.12 s                 1.26 s
          56        > 90 s (unfinished)    1.56 s
          65        —                      2.12 s

    GP wins on short words and then falls off a cliff; the seminormal
    route is ~linear and has none. This producer's words run 47…65
    letters, so all but the shortest sit past the cliff — which is why it
    timed out at 25 s, 180 s (twice) and 900 s while doing nothing wrong.

    The two engines are independent implementations and agree to the
    50-dps floor on this producer's own words (`W_atom`, `W_free`: rel
    2.6e-50 and 5.4e-50), which is what licenses the swap.
    """
    shapes = _two_row_shapes(n, y_table)
    chis = _ph.chi_lambdas_braid_mpfr(
        [list(st) for st in shapes], list(word), Q_50_DIGIT_STR, 50)
    total = mp.mpf(0)
    for st, chi in zip(shapes, chis):
        total += mp.mpf(str(y_table[st])) * mp.mpf(str(chi))
    return total


def main() -> int:
    t0 = time.monotonic()
    Z, N = 2, 2
    n = 3 * (Z + N)                      # 12
    q = mp.mpf(Q_50_DIGIT_STR)
    # Select the y_λ table from the SAME pin the characters are evaluated at.
    #
    # `_load_y_lambda(n, None)` takes the module default, which is the proton
    # table. This producer evaluates χ at `Q_50_DIGIT_STR`, which today also
    # resolves to proton — so the two agree by COINCIDENCE, not construction.
    # Verified: the default and the pin-derived table are byte-identical as of
    # 2026-08-27.
    #
    # The bridge's own docstring records why that is not good enough. It
    # "accepts q_str and then ignored it when choosing weights, so a proton-q₀
    # caller got muon-pinned y_λ with nothing in the output saying so";
    # repointing the default at proton fixed that and left the mirror live —
    # a muon-q₀ caller now silently gets proton y_λ. Passing the pin closes
    # both directions here, so a future re-pin moves the weights with the
    # characters instead of desynchronising them silently.
    #
    # Measured cost of the desync if it ever happened: the two tables differ
    # at the 8th digit (2.899588321 vs 2.899588372, ~18 ppb) — the μ–p
    # substrate tension itself, per AGENTS.md "never straddle the two layers
    # inside one quantity".
    y_table = _load_y_lambda(n, None, q_str=Q_50_DIGIT_STR)

    # Block-swap braids as (sign=+1, gen_1based) pairs.
    swp = {
        "id": [],
        "swap_p": [(1, g + 1) for g in block_swap_word(0, 3, n)],     # protons
        "swap_n": [(1, g + 1) for g in block_swap_word(6, 3, n)],     # neutrons
        "swap_pn": [(1, g + 1) for g in
                    (block_swap_word(0, 3, n) + block_swap_word(6, 3, n))],
    }

    w_atom = signonly_word(Z, N, include_inter=True)    # bound (with bonds)
    w_free = signonly_word(Z, N, include_inter=False)   # free (no bonds)

    print("=" * 84)
    print(" Block-swapped symmetrization S_atom for ⁴He (S₂×S₂, sign-only)")
    print(f"   q₀ = {Q_50_DIGIT_STR[:20]}…   n = {n}")
    print("=" * 84)
    print(f" {'σ block-perm':>14}{'tr_M(W_atom·β)':>18}{'tr_M(W_free·β)':>18}")
    print(" " + "-" * 60)
    atom_traces, free_traces = {}, {}
    for name, beta in swp.items():
        ta = tr_M_of_word(w_atom + beta, n, y_table, q)
        tf = tr_M_of_word(w_free + beta, n, y_table, q)
        atom_traces[name] = ta
        free_traces[name] = tf
        print(f" {name:>14}{float(ta):>18.8f}{float(tf):>18.8f}")
    print(" " + "-" * 60)

    # Bosonic (symmetric) projector average over the 4 block-perms.
    G = len(swp)
    tr_atom_sym = sum(atom_traces.values()) / G
    tr_free_sym = sum(free_traces.values()) / G
    tr_atom_naive = atom_traces["id"]      # tr_M(W_atom) — the canonical bound trace
    tr_free_naive = free_traces["id"]      # tr_M(W_free) = τ_p²τ_n² (naive constituent)
    S_atom = tr_atom_sym / tr_atom_naive
    S_free = tr_free_sym / tr_free_naive
    binding_signal = mp.log(S_free / S_atom)

    print(f"  tr_atom (naive, id)     = {float(tr_atom_naive):.8f}")
    print(f"  tr_atom_sym (¼Σ)        = {float(tr_atom_sym):.8f}   S_atom = {float(S_atom):.6f}")
    print(f"  tr_free (naive, id)     = {float(tr_free_naive):.8f}")
    print(f"  tr_free_sym (¼Σ)        = {float(tr_free_sym):.8f}   S_free = {float(S_free):.6f}")
    print(f"\n  BINDING SIGNAL  log(S_free/S_atom) = {float(binding_signal):.6f}")
    if abs(float(binding_signal)) < 1e-9:
        print("  ⇒ S_atom = S_free: the symmetrization CANCELS — no binding shift.")
    else:
        print("  ⇒ S_atom ≠ S_free: the bonds break block symmetry — REAL binding signal.")

    w = WitnessBuilder("block-swap-binding", engine="python+rust", start_time=t0)
    w.set_description(
        "Exact block-swapped bound symmetrization S_atom for ⁴He (task-1, #2103 "
        "follow-up). tr_atom_sym = ¼Σ_{σ∈S₂×S₂} tr_M(W_atom·β_σ) with β_σ the "
        "positive block-swap braid (NOT the orbit identity's relabeling — that is "
        "conjugation; the Young symmetrizer composes the braid). Sign-only "
        "(chi_q_via_gp). The binding signal of identical-nucleon exchange is the "
        "residual log(S_free/S_atom): if the bonds break block symmetry, S_atom ≠ "
        "S_free and the symmetrization does NOT cancel in the log-ratio binding."
    )
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("atom_traces", {k: float(v) for k, v in atom_traces.items()})
    w.add_data("free_traces", {k: float(v) for k, v in free_traces.items()})
    w.add_data("S_atom", float(S_atom))
    w.add_data("S_free", float(S_free))
    w.add_data("binding_signal_log_Sfree_over_Satom", float(binding_signal))
    w.add_data("convention", "sign-only (chi_q_via_gp); averaged-binding is the slow refinement")
    # `computed=0.0, expected=0.0` was a constant standing in for a check that
    # lives in a bare `assert` inside `block_swap_word`. That assert aborts
    # before `w.save()`, so a braid failing to realise its block permutation
    # produced NO witness rather than a failing one — and under `python -O`
    # it produces no check at all. Re-run the same comparison here, at the
    # one place whose outcome the witness can carry (bean qou-26f2).
    block_swaps_ok = sum(
        1 for s in (0, 6)
        if _apply(block_swap_word(s, 3, n), n) == _block_swap_perm(s, 3, n)
    )
    w.add_assertion(
        name="block_swap_braids_realize_block_perms",
        computed=block_swaps_ok, expected=2, tolerance=0,
        source="_apply(block_swap_word(s,3,n), n) == _block_swap_perm(s,3,n) "
               "re-evaluated at witness time for swap_p (s=0) and swap_n "
               "(s=6) — the braids are the correct S₂×S₂ block "
               "transpositions.",
    )
    out = w.save()
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
