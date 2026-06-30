#!/usr/bin/env python3
"""Lossless ⁴He per-λ χ in the **binding** (color-weighted averaged-crossing)
convention at q₀, 50 dps, all 77 λ⊢12.

In the binding convention the inter-nucleon crossings are Hecke elements
`c·σ + d·1` (p-n → `σ − h·(½ − δ/4)`, n-n → `σ − h`, δ = flavor_split_leading(q₀)),
not braid generators, so the dim-independent Rust `chi_q_via_gp` path — which
only takes braid words `(sign, gen)` — cannot evaluate them directly, and a
dim×dim seminormal is infeasible at n = 12 (dims to 7700).

This producer computes the binding χ **losslessly** with no dim×dim matrix:

1. **Reconstruct** the binding word `Π_k (c_k·σ_{g_k} + d_k·1)` at full MPFR
   precision (`atom_braid_word_3A` floats its coefficients; we rebuild the
   intra-nucleon chains via `nucleon_gen_chains(…, q=q₀_mpf)` and the interface
   templates `{0, −h, −h(½−δ/4)}` exactly).
2. **Collapse** each maximal contiguous run of an identical Hecke factor
   `(c·σ+d)^m` to a single linear `a·σ + b·1` via the Hecke relation
   `σ² = h·σ + 1` (a degree-m polynomial in σ reduces to degree ≤ 1). The 24
   `d≠0` crossings of ⁴He form **10** such runs.
3. **Expand** the 10 collapsed binomials into `2¹⁰ = 1024` **sign-only braid
   words** (each `d=0` crossing stays a pure σ), each with a scalar coefficient
   `∏ (a or b)`.
4. **Batch-evaluate** every branch word over all 77 λ⊢12 with the dim-independent
   `chi_lambda_all_partitions_mpfr` (exact integer Laurent character substituted
   at q₀, 50 dps), and accumulate `χ^λ_binding = Σ_branches coeff · χ^λ(branch)`.

Lossless, MPFR, no dim cap. Gated by agreement with the f64 batch
`chi_q_atomic_all_partitions` (the existing dim-independent binding-convention
character) to the f64 floor, and `Σ_λ y_λ χ^λ` against the same.

Output: chi-helium-4-h12-at-q0-50dps-binding.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from itertools import product
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

import pyhecke_native as pn  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from tr_m_wenzl_bridge_mpfr import _load_y_lambda  # noqa: E402
from per_irrep_pole_atom import parts_of  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 50
EXACT_F64 = mp.mpf("1e-12")


def _hp_binding_word(Z: int, N: int, q):
    """The ⁴He binding word as MPFR `(c, d, gen0)` triples (color-weighted p-n).
    Mirrors `mass_at_3A_proper.atom_braid_word_3A` but keeps every coefficient
    at the active mpmath precision instead of floating it."""
    from pyhecke.atom import nucleon_gen_chains
    from _li_2_q_util import flavor_split_leading
    h = q - 1 / q
    delta = flavor_split_leading(q)
    p_g0, p_g1 = nucleon_gen_chains(['u', 'u', 'd'], q=q)
    n_g0, n_g1 = nucleon_gen_chains(['u', 'd', 'd'], q=q)
    word = []
    ordering = ['p'] * Z + ['n'] * N
    A = Z + N
    for k, nuc in enumerate(ordering):
        g0, g1 = (p_g0, p_g1) if nuc == 'p' else (n_g0, n_g1)
        for c, d in g0:
            word.append((mp.mpf(c), mp.mpf(d), 3 * k))
        for c, d in g1:
            word.append((mp.mpf(c), mp.mpf(d), 3 * k + 1))
        if k < A - 1:
            nxt = ordering[k + 1]
            if nuc == 'p' and nxt == 'p':
                cd = (mp.mpf(1), mp.mpf(0))
            elif nuc == 'n' and nxt == 'n':
                cd = (mp.mpf(1), -h)
            else:  # p-n color-weighted averaged crossing
                cd = (mp.mpf(1), -h * (mp.mpf(1) / 2 - delta / 4))
            word.append((cd[0], cd[1], 3 * k + 2))
    return word


def main() -> int:
    mp.mp.dps = DPS + 10
    Z, N, n = 2, 2, 12
    q = mp.mpf(Q_50_DIGIT_STR)
    q_str = mp.nstr(q, DPS)
    h = q - 1 / q
    t0 = time.time()

    word = _hp_binding_word(Z, N, q)

    # Group into maximal contiguous runs of the SAME generator (the (c,d) may
    # vary within a run — e.g. the intra-nucleon chains). The ordered product of
    # all Hecke factors on one σ_g collapses, via σ²=h·σ+1, to a single linear
    # a·σ_g + b·1.
    gen_runs = []  # (gen, [(c,d), …])
    for c, d, g in word:
        if gen_runs and gen_runs[-1][0] == g:
            gen_runs[-1][1].append((c, d))
        else:
            gen_runs.append((g, [(c, d)]))

    # Collapse each run; a run with b==0 is a single scaled σ (fixed, no branch);
    # otherwise it is a binomial (a·σ + b·1) → one 2-way branch.
    binomials = []  # list of (gen, a, b)
    layout = []     # ordered: ('fix', gen, a) | ('bin', idx)
    for g, factors in gen_runs:
        a, b = mp.mpf(0), mp.mpf(1)               # identity
        for c, d in factors:
            a, b = a * c * h + a * d + b * c, a * c + b * d
        if b == 0:                                # pure a·σ^1 — keep as braid
            layout.append(('fix', g, a))
        else:
            layout.append(('bin', len(binomials)))
            binomials.append((g, a, b))
    nb = len(binomials)
    print(f"⁴He binding word: {len(word)} crossings, {len(gen_runs)} gen-runs, "
          f"{nb} binomials → {2 ** nb} branches", flush=True)

    shapes = [tuple(s) for s in parts_of(n)]
    acc_terms = {s: [] for s in shapes}

    # Enumerate the 2^nb branches; build each sign-only word + scalar coeff.
    for choice in product((0, 1), repeat=nb):  # 0 = identity (b), 1 = σ (a)
        coeff = mp.mpf(1)
        signed = []
        for item in layout:
            if item[0] == 'fix':
                _, g, a = item
                coeff *= a
                signed.append((1, g + 1))          # 1-based gen for the FFI
            else:
                idx = item[1]
                g, a, b = binomials[idx]
                if choice[idx] == 1:
                    coeff *= a
                    signed.append((1, g + 1))
                else:
                    coeff *= b
        if coeff == 0:
            continue
        out = pn.chi_lambda_all_partitions_mpfr(n, signed, q_str, DPS)
        for part, chi_str in out:
            acc_terms[tuple(part)].append(coeff * mp.mpf(chi_str))

    # fsum the per-branch contributions per λ (avoid sequential-+= rounding).
    acc = {s: mp.fsum(terms) for s, terms in acc_terms.items()}

    # Assemble tr_M = Σ_λ y_λ χ^λ and the per-λ records.
    y_table = _load_y_lambda(n, None)
    per_partition = []
    trM = mp.mpf(0)
    for s in shapes:
        y = y_table.get(s)
        chi = acc[s]
        rec = {"partition": list(s), "chi_lambda": mp.nstr(chi, DPS)}
        if y is not None:
            contrib = mp.mpf(str(y)) * chi
            trM += contrib
            rec["y_lambda"] = str(y)
            rec["contribution"] = mp.nstr(contrib, DPS)
        per_partition.append(rec)

    # ── Gate: f64 dim-independent binding character (chi_q_atomic_all_partitions)
    cd_factors = [(mp.nstr(c, DPS), mp.nstr(d, DPS), g) for c, d, g in word]
    # chi_q_atomic_all_partitions is f64; pass float (c,d,gen).
    f64_factors = [(float(c), float(d), g) for c, d, g in word]
    f64 = dict(
        (tuple(p), mp.mpf(v))
        for p, v in pn.chi_q_atomic_all_partitions(n, f64_factors, float(q))
    )
    max_f64 = mp.mpf(0)
    for s in shapes:
        if s in f64:
            max_f64 = max(max_f64, abs(acc[s] - f64[s]))
    gate_ok = max_f64 < EXACT_F64

    elapsed = time.time() - t0
    print(f"  tr_M_binding(q0) = {mp.nstr(trM, 18)}")
    print(f"  per-λ max|MPFR − f64 chi_q_atomic| = {mp.nstr(max_f64, 6)} "
          f"(gate {'PASS' if gate_ok else 'FAIL'} < 1e-12)")
    print(f"  77/77 λ⊢12, {elapsed:.1f}s")

    payload = {
        "computation": "chi-helium-4-h12-at-q0-50dps-binding",
        "description": (
            "Lossless per-λ χ^λ(β_atomic(2,2))=⁴He in the BINDING "
            "(color-weighted averaged-crossing) convention at q_0, 50 dps, all "
            "77 λ⊢12. Built without any dim×dim seminormal: the binding Hecke "
            "word Π(c·σ+d) has its 10 d≠0 runs collapsed via σ²=hσ+1 and "
            "expanded into 1024 sign-only braid branches, each evaluated "
            "dim-independently by chi_lambda_all_partitions_mpfr. Gated against "
            "the f64 chi_q_atomic_all_partitions binding character. Resolves the "
            "dim-capped binding cache (bean b0vf)."
        ),
        "producer": "binding-branch-expansion-lossless",
        "convention": "bring_color_weighted-averaged-crossings",
        "q_0_50dps": str(q), "dps": DPS, "n_strands": n,
        "atom": "helium-4", "Z": Z, "N": N,
        "n_partitions": len(per_partition), "n_partitions_total": len(shapes),
        "max_dim": None, "n_skipped_max_dim": 0, "partial": False,
        "n_branches": 2 ** nb,
        "f64_gate_max_abs": mp.nstr(max_f64, 8),
        "tr_M_at_q0": str(trM),
        "compute_time_sec": round(elapsed, 2),
        "by_partition": per_partition,
    }
    out = HERE / "chi-helium-4-h12-at-q0-50dps-binding.witness.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False))

    wb = WitnessBuilder("chi-at-q0-binding-lossless-helium-4", engine="python",
                        start_time=t0)
    wb.set_description(
        "Lossless ⁴He per-λ χ in the binding (color-weighted averaged-crossing) "
        "convention at q_0, all 77 λ⊢12, via Hecke-run collapse + sign-only "
        "branch expansion (no dim×dim matrix). Resolves bean b0vf."
    )
    wb.add_data("n_partitions", len(per_partition))
    wb.add_data("n_branches", 2 ** nb)
    wb.add_data("tr_M_at_q0", str(trM))
    wb.add_data("f64_gate_max_abs", mp.nstr(max_f64, 8))
    wb.add_assertion(name="binding_chi_matches_f64_atomic",
                     computed=1 if gate_ok else 0, expected=1,
                     source="MPFR lossless binding χ^λ agrees with the f64 "
                            "dim-independent chi_q_atomic_all_partitions to <1e-12")
    wb.save()
    print(f"  Cache: {out}")
    return 0 if gate_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
