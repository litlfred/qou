#!/usr/bin/env python3
"""tr_m_atom_via_transfer — scalable canonical tr_M(β_atom) / tr_M(β_free)
for every atom, via the monotone-word fine-Bratteli transfer matrix.

This is the end-to-end consumer of `chi_monotone_transfer`: it assembles
the canonical Markov trace

    tr_M(β) = Σ_{λ ⊢ 3A} y_λ(q₀) · χ^λ(β)

for the bound atom word β_atom = atom_braid_word_3A(…, include_inter=True)
and the free word β_free (include_inter=False), at the canonical
color-weighted p-n convention. The transfer gives all χ^λ in one sweep
(d_λ-free), and y_λ comes from the Jones–Markov weights
(`wedderburn_jones_markov.y_lambda_at`, mpmath hook-length fast path).

WHY THIS MATTERS: `canonical_tr_m_via_branching` was end-to-end only for
A=2; A ≥ 3 fell back to Path-3 / markov_peel (binding_combiner_markov_peel
_fallback) because the per-basis-vector tr_M hit the d_λ wall (3.6-year
wall at ⁶Li, audit §7a). The transfer closes that gap: canonical tr_M for
⁶Li/⁷Li (and beyond) in SECONDS, no Path-3 needed.

Cross-checks (assertions): tr_M^atom(D) ≈ 0.388 (matches the #2080
canonical_tr_m_via_branching value); the free χ ≡ chi_free_via_lr (the
independent parabolic-LR formula) to the 50-dps floor.

The trace-difference Δtr_M = |tr_M^free| − |tr_M^atom| is the Path-3
binding baseline (B = E_0·Δtr_M); it under-binds without the operator-
valued / magic-A factor (documented in the combiner), so we report Δtr_M
itself as the scalable canonical observable, not a closed binding number.

NO float64 (owner ruling 2026-06-09): all mpmath at the 50-dps floor.

Usage:
    python3 tr_m_atom_via_transfer.py                 # D..⁷Li + witness
    python3 tr_m_atom_via_transfer.py 6Li 7Li 9Be     # named atoms
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from reduced_block_kernel import chi_all_lambda_reduced_block
from chi_free_via_lr import chi_free_lr  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from host_info import host_info  # noqa: E402

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2),
      "6Li": (3, 3), "7Li": (3, 4), "9Be": (4, 5), "10B": (5, 5)}

# atoms whose full per-λ χ we serialise (the NEW large-A data, no prior
# oracle existed — D..⁴He are already covered by cached witnesses).
_EMIT_BY_PARTITION = {"6Li", "7Li"}


def _trM(chi: dict, y: dict) -> "mp.mpf":
    return mp.fsum(y[lam] * chi.get(lam, mp.mpf(0)) for lam in y)


def tr_m_atom_zn(Z: int, N: int, *, m_pp: int = 1, m_pn: int = 1,
                 m_nn: int = 1, dps: int = 50, q=None):
    """`(tr_M_atom, tr_M_free, chi_atom, wall_sec)` for nucleon counts
    `(Z, N)` at q₀ — the (Z,N)-keyed entry point for binding consumers
    (`binding_canonical`, `canonical_tr_m_via_branching`).

    `q` defaults to the canonical substrate q₀ at full 50-digit precision
    (`Q_50_DIGIT_STR`, via `chi_all_lambda_reduced_block`; y_λ at `Q0`).
    When `q` is
    given it is threaded to BOTH the y_λ Jones–Markov weights and the
    transfer χ^λ. NOTE: the canonical color-weighted atom word is
    **q₀-baked** — its interface `d` carries `flavor_split_subleading(q₀)`
    — so `chi_all_lambda_reduced_block`'s `word_to_mpfr` can only re-lift
    it at q₀;
    passing q ≠ q₀ with that convention raises `ValueError` (a true q-sweep
    needs a q-parameterised word builder). q-agnostic conventions
    (σ / σ⁻¹ / averaged) re-lift at any q.

    Canonical color-weighted p-n convention, summed over ALL `p(3A)`
    partitions — LOSSLESS: no `max_dim` cap, no active-set truncation
    (the active-set truncation is a ~10⁻³ error, rejected for 1-ppQ; see
    `docs/audits/2026-06-10-binding-active-set-compute-optimization.md`).
    The speed comes from the fine-Bratteli transfer matrix (no d_λ wall),
    NOT from dropping partitions. This is the scalable replacement for the
    symbolic `tr_M_element` and native `chi_lambda_all_partitions_mpfr`
    per-partition paths: ⁶Li in ~0.2 s vs markov_peel's ~17 min (~5000×),
    validated transfer ≡ full Hoefsmit (`char_fast`) to the 50-dps floor.
    """
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    n = 3 * (Z + N)
    # q=None → canonical q₀: y_λ at Q0 and χ at the 50-digit Q_50_DIGIT_STR
    # (chi_all_lambda's own default — NOT the ~16-digit float Q0, which
    # would regress the validated 50-dps χ). A custom q is threaded to
    # BOTH y_λ and χ so the trace is evaluated consistently at that q.
    y_q = Q0 if q is None else q
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, y_q).items()}
    t0 = time.time()
    chi_atom = chi_all_lambda_reduced_block(
        atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                           include_inter=True), n, q=q)
    chi_free = chi_all_lambda_reduced_block(
        atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                           include_inter=False), n, q=q)
    wall = time.time() - t0
    return _trM(chi_atom, y), _trM(chi_free, y), chi_atom, wall


def tr_m_atom(atom: str, *, dps: int = 50):
    """`(tr_M_atom, tr_M_free, chi_atom, wall_sec)` for named `atom` at q₀."""
    Z, N = ZN[atom]
    return tr_m_atom_zn(Z, N, dps=dps)


def main() -> int:
    atoms = sys.argv[1:] or ["D", "T", "3He", "4He", "6Li", "7Li"]
    mp.mp.dps = 50
    rows = []
    by_partition = {}
    d_check = None
    free_lr_max = mp.mpf(0)
    for atom in atoms:
        if atom not in ZN:
            print(f"  unknown atom {atom!r}; skip"); continue
        Z, N = ZN[atom]
        n = 3 * (Z + N)
        tA, tF, chi_atom, wall = tr_m_atom(atom)
        dtr = abs(tF) - abs(tA)
        rows.append({
            "atom": atom, "n_strands": n, "n_partitions": len(chi_atom),
            "tr_M_atom": mp.nstr(tA, 30), "tr_M_free": mp.nstr(tF, 30),
            "delta_tr_M_abs": mp.nstr(dtr, 30), "wall_sec": round(wall, 3),
        })
        print(f"  {atom:<5} n={n:<3} λ={len(chi_atom):<5} {wall:7.2f}s  "
              f"tr_M_atom={mp.nstr(tA,8):>12}  tr_M_free={mp.nstr(tF,8):>12}  "
              f"Δtr_M={mp.nstr(dtr,8):>12}")
        if atom == "D":
            d_check = tA
        if atom in _EMIT_BY_PARTITION:
            by_partition[atom] = [
                {"partition": list(lam), "chi_lambda": mp.nstr(chi_atom[lam], 50)}
                for lam in sorted(chi_atom, key=lambda t: (-len(t), t))
            ]
        # free χ ≡ chi_free_via_lr cross-check (independent parabolic-LR)
        if n <= 21:
            chf_lr = chi_free_lr(Z, N)
            chf = chi_all_lambda_reduced_block(atom_braid_word_3A(Z, N, include_inter=False), n)
            free_lr_max = max(free_lr_max,
                              max(abs(chf[l] - chf_lr.get(l, mp.mpf(0))) for l in chf))

    w = WitnessBuilder("tr-m-atom-via-transfer", engine="python")
    w.set_description(
        "Canonical Markov trace tr_M(β_atom)/tr_M(β_free) = Σ y_λ χ^λ for "
        "every atom, via the monotone-word fine-Bratteli transfer matrix "
        "(chi_monotone_transfer) + Jones-Markov y_λ. Canonical color-weighted "
        "p-n convention, q₀, 50 dps. Closes the A≥3 canonical-tr_M gap that "
        "needed Path-3/markov_peel — ⁶Li/⁷Li in seconds (no d_λ wall). "
        "Δtr_M = |tr_M_free|−|tr_M_atom| is the Path-3 binding baseline."
    )
    w.add_data("rows", rows)
    w.add_data("convention", "bring_color_weighted")
    w.add_data("q_str", str(Q0))
    w.add_data("host", host_info())
    if by_partition:
        w.add_data("by_partition", by_partition)
    if d_check is not None:
        w.add_assertion(
            "trM_atom_deuteron_matches_canonical_branching",
            computed=float(d_check), expected=0.388357, tolerance=1e-5,
            source="canonical_tr_m_via_branching (#2080) D value",
        )
    w.add_assertion(
        "free_chi_matches_parabolic_lr_50dps",
        computed=float(free_lr_max), expected=0.0, tolerance=1e-40,
        source="chi_free_via_lr (independent parabolic-LR formula)",
    )
    w.save()
    print(f"  free χ ≡ chi_free_via_lr: max|Δ|={mp.nstr(free_lr_max,3)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
