#!/usr/bin/env python3
"""
Sym-alt mirror-symmetry probe — test whether χ_sym − χ_alt (the
Wedderburn mirror-symmetry descriptor) combined with Jones(q₀)
predicts the ρ_F^eff density deviation.

For each atom:
  - Build atom braid word via atom_braid_word_3A
  - Compute χ_sym(β) = χ_(n)(β) and χ_alt(β) = χ_(1ⁿ)(β)
    via seminormal matrix trace at q₀
  - Compute (χ_sym − χ_alt) and (χ_sym + χ_alt)
  - Compute Plancherel-weighted full trace |tr_M|
  - Fetch Jones polynomial at q₀² (from rho_f_complexity_sweep)
  - Correlate with empirical deviation ρ_F^eff/nominal − 1

Extended from d_wedderburn_profile.py (D only) to T, ³He, ⁴He.
"""
from __future__ import annotations

import sys
import json
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
import mpmath as mp

from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A
from q_parameter import Q as Q0
from rho_f_complexity_sweep import j_at_q0, EMPIRICAL


def is_alt_partition(shape: tuple) -> bool:
    return all(s == 1 for s in shape)


def is_sym_partition(shape: tuple, n: int) -> bool:
    return shape == (n,)


def chi_at_q0(shape: tuple, word) -> complex:
    """Character χ_λ(W) at q = q₀."""
    sigmas, dim, _ = _cached_seminormal(shape)
    if dim == 0:
        return 0.0 + 0j
    q_sym = sp.Symbol("q")
    sigmas_num = []
    for S in sigmas:
        S_arr = S.toarray() if hasattr(S, "toarray") else np.asarray(S)
        out = np.zeros((dim, dim), dtype=complex)
        for i in range(dim):
            for j in range(dim):
                e = S_arr[i, j]
                out[i, j] = (complex(sp.N(e.subs(q_sym, Q0)))
                              if hasattr(e, "subs") else complex(e))
        sigmas_num.append(out)
    I = np.eye(dim, dtype=complex)
    prod = I.copy()
    for (c, d, g) in word:
        if g < len(sigmas_num):
            prod = prod @ (c * sigmas_num[g] + d * I)
        else:
            return 0.0 + 0j
    return complex(np.trace(prod))


def atom_wedderburn_profile(Z: int, N: int, max_partitions: int = 100):
    """Compute χ_sym, χ_alt, and the full Plancherel-weighted trace."""
    A = Z + N
    n = 3 * A
    word = atom_braid_word_3A(Z, N)
    parts = list(partitions_of(n))

    chi_sym = chi_alt = None
    nfac_q0 = complex(float(qfac(n)))
    trace_total = 0 + 0j

    # For efficiency: only compute sym, alt, and largest contributors
    # (sym/alt are always 1-dim so cheap).
    for shape in parts:
        if is_sym_partition(shape, n):
            chi_sym = chi_at_q0(shape, word)
        elif is_alt_partition(shape):
            chi_alt = chi_at_q0(shape, word)

    # Full Plancherel trace — only for small n to keep runtime reasonable
    if n <= 9:
        for shape in parts:
            _, dim, _ = _cached_seminormal(shape)
            if dim == 0:
                continue
            dq = complex(float(dim_q(shape)))
            w = dq * dq / nfac_q0
            chi = chi_at_q0(shape, word)
            trace_total += w * chi / dim
    else:
        trace_total = complex("nan")   # too many partitions

    return {
        "Z": Z, "N": N, "A": A, "n": n,
        "n_factors": len(word),
        "n_partitions": len(parts),
        "chi_sym": chi_sym,
        "chi_alt": chi_alt,
        "chi_sym_minus_alt": (chi_sym - chi_alt
                                if chi_sym is not None and chi_alt is not None
                                else None),
        "chi_sym_plus_alt": (chi_sym + chi_alt
                               if chi_sym is not None and chi_alt is not None
                               else None),
        "trace_total": trace_total if trace_total == trace_total else None,
    }


if __name__ == "__main__":
    print("=" * 110)
    print("SYM-ALT MIRROR PROBE — extending Wedderburn profile to D, T, ³He, ⁴He")
    print(f"  q₀ = {Q0}")
    print("=" * 110)

    # Compute profile for D, T, ³He (n ≤ 9) — fast.
    # 4He has n=12, 77 partitions → slow; compute sym/alt only.
    ATOMS = [
        ("D",   1, 1, "6_2"),
        ("T",   1, 2, "8_11"),
        ("3He", 2, 1, "L6a4"),
        ("4He", 2, 2, "4·L6a4"),
    ]
    print(f"\n  {'atom':>4} {'A':>2} {'n':>3} {'parts':>6} "
          f"{'χ_sym(β)':>15} {'χ_alt(β)':>15} "
          f"{'χ_sym-χ_alt':>15} {'χ_sym+χ_alt':>15}")
    rows = []
    for name, Z, N, knot in ATOMS:
        prof = atom_wedderburn_profile(Z, N)
        chi_s = prof["chi_sym"]
        chi_a = prof["chi_alt"]
        diff = prof["chi_sym_minus_alt"]
        summ = prof["chi_sym_plus_alt"]
        print(f"  {name:>4} {prof['A']:>2} {prof['n']:>3} "
              f"{prof['n_partitions']:>6} "
              f"{chi_s.real:>+9.4f}{chi_s.imag:+.1e}j "
              f"{chi_a.real:>+9.4f}{chi_a.imag:+.1e}j "
              f"{diff.real:>+9.4f}{diff.imag:+.1e}j "
              f"{summ.real:>+9.4f}{summ.imag:+.1e}j")
        rows.append({
            "atom": name, "Z": Z, "N": N, "A": prof["A"], "n": prof["n"],
            "knot": knot,
            "chi_sym_re": chi_s.real, "chi_sym_im": chi_s.imag,
            "chi_alt_re": chi_a.real, "chi_alt_im": chi_a.imag,
            "chi_sym_minus_alt_re": diff.real,
            "chi_sym_plus_alt_re": summ.real,
            "trace_total_re": (prof["trace_total"].real
                                 if prof["trace_total"] else None),
        })

    # Correlate with density deviations
    print(f"\n{'=' * 100}")
    print("CORRELATION vs EMPIRICAL ρ_F DEVIATION")
    print("=" * 100)

    dev_table = {}
    for name, Z, N, knot in ATOMS:
        d = EMPIRICAL[name]
        rho_eff = d["B_AME"] / d["V_hyp"]
        dev_factor = rho_eff / d["nominal_rho"]
        dev_pct = float(dev_factor - 1) * 100
        dev_table[name] = dev_pct

    print(f"  {'atom':>4} {'dev%':>8} {'χ_s':>10} {'χ_a':>10} "
          f"{'χ_s-χ_a':>10} {'χ_s+χ_a':>10} "
          f"{'ln|J(q₀²)|':>12} {'χ_s·χ_a':>10}")
    for r in rows:
        name = r["atom"]
        dev = dev_table[name]
        cs = r["chi_sym_re"]
        ca = r["chi_alt_re"]
        Jv = j_at_q0(r["knot"])
        try:
            ln_J = float(mp.log(abs(Jv))) if Jv != 0 else -99
        except Exception:
            ln_J = 0
        prod_sa = cs * ca
        print(f"  {name:>4} {dev:>+7.3f}% "
              f"{cs:>+9.4f} {ca:>+9.4f} "
              f"{cs - ca:>+9.4f} {cs + ca:>+9.4f} "
              f"{ln_J:>+12.4f} {prod_sa:>+9.4f}")
        r["dev_pct"] = dev
        r["ln_abs_J"] = ln_J
        r["chi_prod"] = prod_sa

    # Compute simple correlations
    import math as pmath
    def pearson(xs, ys):
        n = len(xs)
        if n < 2:
            return float("nan")
        mx, my = sum(xs) / n, sum(ys) / n
        num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
        dx = pmath.sqrt(sum((x - mx) ** 2 for x in xs))
        dy = pmath.sqrt(sum((y - my) ** 2 for y in ys))
        return num / (dx * dy) if dx > 0 and dy > 0 else float("nan")

    devs = [r["dev_pct"] for r in rows]
    xs_diff = [r["chi_sym_minus_alt_re"] for r in rows]
    xs_sum = [r["chi_sym_plus_alt_re"] for r in rows]
    xs_prod = [r["chi_prod"] for r in rows]
    xs_sym = [r["chi_sym_re"] for r in rows]
    xs_alt = [r["chi_alt_re"] for r in rows]
    xs_lnJ = [r["ln_abs_J"] for r in rows]

    print(f"\n  Pearson correlation (deviation %) vs:")
    print(f"    χ_sym - χ_alt      : {pearson(devs, xs_diff):+.4f}")
    print(f"    χ_sym + χ_alt      : {pearson(devs, xs_sum):+.4f}")
    print(f"    χ_sym · χ_alt      : {pearson(devs, xs_prod):+.4f}")
    print(f"    χ_sym alone        : {pearson(devs, xs_sym):+.4f}")
    print(f"    χ_alt alone        : {pearson(devs, xs_alt):+.4f}")
    print(f"    ln|J(q₀²)|         : {pearson(devs, xs_lnJ):+.4f}")

    # Two-parameter candidate: a · ln|J| + b · (χ_sym - χ_alt)
    # Simple LSQ fit
    try:
        import numpy as np
        A_mat = np.column_stack([xs_lnJ, xs_diff, np.ones(len(devs))])
        b_vec = np.array(devs)
        coeffs, *_ = np.linalg.lstsq(A_mat, b_vec, rcond=None)
        pred = A_mat @ coeffs
        resid = pred - b_vec
        print(f"\n  Two-parameter LSQ: dev% = {coeffs[0]:+.4f}·ln|J| "
              f"+ {coeffs[1]:+.4f}·(χ_sym − χ_alt) + {coeffs[2]:+.4f}")
        print(f"  {'atom':>4} {'obs':>8} {'pred':>8} {'resid':>8}")
        for r, p, rs in zip(rows, pred, resid):
            print(f"  {r['atom']:>4} {r['dev_pct']:>+7.3f}% "
                  f"{p:>+7.3f}% {rs:>+7.3f}%")
    except Exception as e:
        print(f"  LSQ fit failed: {type(e).__name__}: {e}")

    witness = {
        "computation": "sym-alt-mirror-probe",
        "description": (
            "Per-atom sym/alt Wedderburn characters χ_sym(β), χ_alt(β) "
            "at q₀ extended from D to T, ³He, ⁴He.  Tests if the mirror-"
            "symmetry descriptors (χ_sym - χ_alt), (χ_sym + χ_alt), or "
            "their product correlate with the empirical ρ_F^eff/nominal "
            "deviation better than the single-parameter ln|J(q₀²)|."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": str(Q0),
        "atoms": rows,
    }
    out = Path(__file__).parent / "sym-alt-mirror-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
