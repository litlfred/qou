#!/usr/bin/env python3
"""
Probe variant writhe-ribbon formulas for chirality factor.

Target: a_D = 1 + h ≈ 1.2091 for the deuteron.
Tests several candidate formulas:

  V1. a = 1 + w · ⟨c⟩_{w_λ=dim_q²/[n]!} · h    (original)
  V2. a = 1 + w · ⟨c⟩_{w_λ=dim_q} · h         (dim_q weighted)
  V3. a = 1 + w_top · ⟨c⟩ · h                 (topological writhe)
  V4. a = 1 + ⟨c⟩ · h                         (no writhe factor)
  V5. a = 1 + h · Σ χ^λ · c(λ) / [n]!_q       (unweighted char sum)
  V6. a = 1 + h · Σ_λ (χ^λ c(λ) / dim_q(λ))   (inverse-dim weighted)
  V7. a = Σ_λ w_λ · q^{2w·c(λ)} · χ^λ / Σ_λ w_λ χ^λ  (full ribbon)

Writhe variants:
  - w_net = #σ - #σ⁻¹ (algebraic, averaged = 0)
  - w_top = #σ - #σ⁻¹ + 0.5·(#averaged)    (averaged half-counts)
  - w_all = #σ - #σ⁻¹ + 1·(#averaged)       (averaged full-counts)

Witness: chirality-variants-probe.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
from scipy import sparse as sp_sparse

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0
from hecke_characters import (
    partitions_of, build_seminormal_matrices, qfac, dim_q,
)
from hecke_character_symbolic import atomic_braid_to_crossings


H_VAL = float(Q0 - 1.0 / Q0)


def content_sum(partition):
    s = 0
    for r, row_len in enumerate(partition):
        for c in range(row_len):
            s += (c - r)
    return s


def chi_lambda(shape, crossings):
    sigmas, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return 0.0, 0
    is_sp = sp_sparse.issparse(sigmas[0]) if sigmas else False
    I = sp_sparse.eye(dim, format='csr') if is_sp else np.eye(dim)
    prod = sp_sparse.eye(dim, format='csr') if is_sp else np.eye(dim)
    d_for = {"sigma": 0.0, "sigma_inv": -H_VAL, "averaged": -H_VAL / 2}
    for gi, ct in crossings:
        if gi >= len(sigmas):
            raise IndexError
        M = sigmas[gi] + d_for[ct] * I
        prod = prod @ M
    return (float(prod.diagonal().sum()) if is_sp else float(np.trace(prod))), dim


def collect(Z, N, include_inter):
    A = Z + N
    k = 3 * A
    nfac = qfac(k)
    crossings = atomic_braid_to_crossings(Z, N, include_inter)
    entries = []
    for shape in partitions_of(k):
        chi, d = chi_lambda(shape, crossings)
        if d == 0:
            continue
        d_q_val = float(dim_q(shape))
        entries.append({
            "shape": shape, "chi": chi, "dim": d,
            "dim_q": d_q_val, "nfac": float(nfac),
            "c": content_sum(shape),
            "w_plancherel": d_q_val ** 2 / float(nfac),
            "w_dim_q": d_q_val,
            "w_one": 1.0,
        })
    pos = sum(1 for _, c in crossings if c == "sigma")
    neg = sum(1 for _, c in crossings if c == "sigma_inv")
    avg = sum(1 for _, c in crossings if c == "averaged")
    return entries, pos, neg, avg, crossings


def variant(entries, weights_key, content_fn, writhe):
    """a = 1 + writhe · ⟨c⟩_{weights} · h."""
    num = sum(e[weights_key] * e["chi"] * content_fn(e) for e in entries)
    den = sum(e[weights_key] * e["chi"] for e in entries)
    if den == 0:
        return None, 0.0
    c_avg = num / den
    return 1 + writhe * c_avg * H_VAL, c_avg


def variant_ribbon(entries, writhe):
    """a = Σ_λ w_λ · q^{2w·c(λ)} · χ^λ / Σ_λ w_λ · χ^λ (full ribbon)."""
    num = sum(e["w_plancherel"] * (Q0 ** (2 * writhe * e["c"])) * e["chi"]
              for e in entries)
    den = sum(e["w_plancherel"] * e["chi"] for e in entries)
    return num / den if den != 0 else None


if __name__ == "__main__":
    print("CHIRALITY VARIANT PROBE")
    print("=" * 80)
    print(f"q_0 = {Q0}, h = {H_VAL:.4f}")
    target = 1 + H_VAL
    print(f"Target: paper's a_D = 1 + h = {target:.4f}")
    print()

    # Focus on D atom (where the discrepancy is large)
    for label, Z, N, incl in [("D atom", 1, 1, True),
                              ("D free", 1, 1, False),
                              ("T atom", 1, 2, True),
                              ("T free", 1, 2, False)]:
        A = Z + N
        entries, p, n, avg, crossings = collect(Z, N, incl)
        w_net = p - n
        w_top = p - n + 0.5 * avg
        w_all = p - n + 1.0 * avg
        paper = (1 - H_VAL ** 2 if A == 3 else
                 (1 - H_VAL ** 2) ** 2 if A == 4 else
                 target if A == 2 else None)
        print(f"── {label} (A={A}) — paper target: {paper} ──")
        print(f"  crossings: {p}σ + {n}σ⁻¹ + {avg} averaged")
        print(f"  writhe: net={w_net}, top={w_top}, all={w_all}")

        probes = [
            ("V1 (w_net, Planch, c)",
             variant(entries, "w_plancherel", lambda e: e["c"], w_net)),
            ("V2 (w_net, dim_q, c)",
             variant(entries, "w_dim_q", lambda e: e["c"], w_net)),
            ("V3 (w_top, Planch, c)",
             variant(entries, "w_plancherel", lambda e: e["c"], w_top)),
            ("V4 (w=1, Planch, c)",
             variant(entries, "w_plancherel", lambda e: e["c"], 1)),
            ("V5 (w_net, unweighted, c)",
             variant(entries, "w_one", lambda e: e["c"], w_net)),
            ("V6 (w_net, 1/dim_q, c)",
             (lambda: variant(entries, "w_dim_q", lambda e: e["c"], w_net))()),
            ("V7 full ribbon (w_net)",
             (variant_ribbon(entries, w_net), None)),
            ("V7 full ribbon (w_top)",
             (variant_ribbon(entries, w_top), None)),
        ]
        target_vs = paper if paper else target
        for name, (a, cavg) in probes:
            if a is None:
                print(f"    {name:<32} FAILED")
                continue
            err = abs(a - target_vs) / abs(target_vs) * 100 if target_vs else 0
            mark = "★" if err < 5 else "·"
            cstr = f" ⟨c⟩={cavg:+.3f}" if cavg is not None else ""
            print(f"    {name:<32} a = {a:+.4f} ({err:>6.2f}%){cstr} {mark}")
        print()

    witness = {
        "computation": "chirality-variants-probe",
        "description": (
            "Probe 8 candidate writhe-ribbon formulas against paper's "
            "assigned chirality factors for D, T, ⁴He. Searches for a "
            "matching structural form beyond my original "
            "(1 + w·⟨c⟩·h) formula which fails for D."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q_0": float(Q0), "h": H_VAL,
                       "paper_D": target,
                       "paper_T_3He": 1 - H_VAL ** 2,
                       "paper_4He": (1 - H_VAL ** 2) ** 2},
    }
    out = Path(__file__).parent / "chirality-variants-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"Witness: {out}")
