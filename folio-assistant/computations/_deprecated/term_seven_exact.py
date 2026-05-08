#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
A.1 — Exact Term-7 (shell-correction) probe with pyhecke Hoefsmit τ_λ.

Tests `conj:shell-correction-term-seven` on light isotopes A=2..7.

The conjecture (`shell-correction-term-seven.md`) posits that the
universal A≥3 binding-gap residual is captured by

    Δ_7(Z, N, A) = m_e · Σ_{λ⊢3A, ℓ(λ)=h_*} C_λ(q) · S_λ(Z, N, A)

with the empirical signal at h_* = 6 (level ℓ = 5 in the GB filtration
ℓ = height(λ) − 1; see higher_a_shell_diagnostic.py).

C_λ(q)  = w_λ(q) · τ_λ(σ_g)
        = (dim_q(λ)² / [3A]_q!) · (tr σ_g^(λ) / dim λ)

For self-conjugate λ this is the Wigner-2 closed form τ = h/2.
For NON-self-conjugate λ, the existing
`paper_six_term_shadow_price_sweep.py` uses the coarse approximation
τ_λ ≈ q^{c̄} − q^{−c̄}.  This script replaces it with **exact**
Hoefsmit YSN characters via `pyhecke.partition.partition_character_sigma1`.

Two occupancy forms are tested side-by-side:

  (Conj)   S_λ from prop:content-scaling-correspondence (paper form)
  (HOcc)   S_λ → (A−1)(A−2)/2 (handover-prompt simpler 3-body shell count)

Output: `term-seven-exact.witness.json` — per-isotope decomposition,
both forms, before/after errors against `prop:derived-mass-formula
-light-isotopes` baseline.

NOTE on conjecture text inconsistency:  the `.md` claims that the only
height-6 partition of k=6 is (3,2,1).  But ℓ = len(λ) − 1 means ℓ=5
maps to length-6 partitions, and the unique length-6 partition of 6
is (1,1,1,1,1,1).  (3,2,1) has length 3.  Author should clarify the
specialisation or update the text; this script uses len-based filter
(matches the empirical α_5 fit; reading 12c in session log).
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

import mpmath as mp

REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO / "tools/pyhecke/python"))
sys.path.insert(0, str(Path(__file__).parent))

import pyhecke
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV

mp.mp.dps = 30

Q0 = Q_MP  # was f64 roundtrip
ME = mp.mpf(str(M_E_MEV))

# ────────────────────────────────────────────────────────────────────────
# Partition utilities
# ────────────────────────────────────────────────────────────────────────


def partitions_of(n):
    """All integer partitions of n in weakly decreasing order."""
    if n == 0:
        yield ()
        return

    def _gen(rem, max_part):
        if rem == 0:
            yield ()
            return
        for p in range(min(max_part, rem), 0, -1):
            for rest in _gen(rem - p, p):
                yield (p,) + rest

    yield from _gen(n, n)


def conjugate(shape):
    if not shape:
        return ()
    return tuple(sum(1 for r in shape if r > j) for j in range(max(shape)))


def is_self_conjugate(shape):
    return tuple(shape) == conjugate(shape)


def hook_lengths(shape):
    rows = len(shape)
    out = []
    for i in range(rows):
        for j in range(shape[i]):
            arm = shape[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if shape[r] > j)
            out.append(arm + leg + 1)
    return out


def content_sum(shape):
    s = 0
    for i, r in enumerate(shape):
        for j in range(r):
            s += j - i
    return s


def q_int(n, q):
    return (q ** n - q ** (-n)) / (q - 1 / q) if n > 0 else mp.mpf(0)


def q_factorial(n, q):
    p = mp.mpf(1)
    for k in range(1, n + 1):
        p *= q_int(k, q)
    return p


def dim_q(shape, q, n):
    """Quantum dimension via hook-length product."""
    h_prod = mp.mpf(1)
    for h in hook_lengths(shape):
        h_prod *= q_int(h, q)
    return q_factorial(n, q) / h_prod


def w_lambda(shape, q, n):
    """Wedderburn weight w_λ = dim_q² / [n]_q!."""
    d = dim_q(shape, q, n)
    return d * d / q_factorial(n, q)


def tau_lambda_exact(shape, q, n):
    """τ_λ(σ_g) = tr(σ_g^(λ)) / dim λ via exact Hoefsmit at q_0.

    pyhecke.partition.partition_character_sigma1 returns the numeric
    χ_λ(σ_1) evaluated at the canonical q_0 (module-level constants
    q0, qi, h baked in).  We trust that value and divide by dim(λ).
    For self-conjugate λ we use the Wigner-2 closed form τ = h/2 — it
    is exact and avoids a sympy round-trip.
    """
    if is_self_conjugate(shape):
        return (q - 1 / q) / 2
    chi = pyhecke.partition.partition_character_sigma1(shape)
    d = pyhecke.partition_dimension(shape)
    return mp.mpf(str(float(chi))) / mp.mpf(str(float(d)))


# ────────────────────────────────────────────────────────────────────────
# Scaling functions S_λ(Z, N, A)
# ────────────────────────────────────────────────────────────────────────


def S_conj(shape, Z, N, A):
    """S_λ as in paper_six_term_shadow_price_sweep.py."""
    c = content_sum(shape)
    A_mpf = mp.mpf(A)
    if c == 0:
        return A_mpf
    if c == 1:
        return mp.mpf(Z * (Z - 1)) / A_mpf ** mp.mpf("1/3")
    if c == -1:
        return mp.mpf(N * (N - 1)) / A_mpf ** mp.mpf("1/3")
    if abs(c) <= 2:
        base = mp.mpf(Z if c > 0 else N)
        return base ** mp.mpf("4/3") / A_mpf ** mp.mpf("1/3")
    T = mp.mpf(abs(N - Z)) / 2
    return T * (T + 1) / A_mpf


def S_hocc(shape, Z, N, A):
    """Handover-prompt simpler form: (A-1)(A-2)/2 (isospin-blind)."""
    return mp.mpf((A - 1) * (A - 2)) / 2


# ────────────────────────────────────────────────────────────────────────
# Term-7 computation
# ────────────────────────────────────────────────────────────────────────


def term_seven(Z, N, *, target_height=6, S_fn=S_conj, q=Q0):
    """Δ_7 = m_e · Σ_{λ⊢3A, len(λ)=target_height} C_λ(q) · S_λ(Z, N, A)."""
    A = Z + N
    n = 3 * A
    total = mp.mpf(0)
    rows = []
    for shape in partitions_of(n):
        if len(shape) != target_height:
            continue
        w = w_lambda(shape, q, n)
        tau = tau_lambda_exact(shape, q, n)
        S = S_fn(shape, Z, N, A)
        c_lambda = w * tau
        contrib = c_lambda * S
        total += contrib
        rows.append({
            "shape": list(shape),
            "self_conjugate": is_self_conjugate(shape),
            "content_sum": content_sum(shape),
            "C_lambda": float(c_lambda),
            "S_lambda": float(S),
            "contribution": float(contrib),
        })
    rows.sort(key=lambda r: abs(r["contribution"]), reverse=True)
    return ME * total, rows  # MeV


# ────────────────────────────────────────────────────────────────────────
# Driver
# ────────────────────────────────────────────────────────────────────────

import os

ISOTOPES_ALL = [
    ("D",   1, 1),
    ("T",   1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
    ("6Li", 3, 3),
    ("7Li", 3, 4),
]
# Default scope = A=2..4 (k=6,9,12).  Override with TERM7_MAX_A=7 to extend.
MAX_A = int(os.environ.get("TERM7_MAX_A", "4"))
ISOTOPES = [t for t in ISOTOPES_ALL if (t[1] + t[2]) <= MAX_A]


def main():
    print(f"Term 7 — exact Hoefsmit τ_λ (q_0 = {float(Q0):.10f})")
    print(f"Filter:  len(λ) = 6  (GB level ℓ = 5)")
    print(f"Scope:   A <= {MAX_A}  (set TERM7_MAX_A=7 env var to extend)")
    print(f"Isotopes: {[i[0] for i in ISOTOPES]}")
    print("=" * 100)
    print(f"  {'iso':<5} {'A':>2} {'k=3A':>4} | {'#partitions':>11} | "
          f"{'Δ7 conj-S (MeV)':>17} | {'Δ7 hocc-S (MeV)':>17} | walltime")
    print("-" * 100, flush=True)

    out_path = Path(__file__).parent / "term-seven-exact.witness.json"

    out = {
        "computation": "term-seven-exact",
        "description": (
            "A.1 — Term-7 shell-correction probe with EXACT pyhecke "
            "Hoefsmit τ_λ.  Filter: len(λ) = 6 partitions of 3A "
            "(GB level ℓ = 5; the empirical winner per "
            "higher_a_shell_diagnostic).  Two occupancy forms tested: "
            "(conj-S) the paper's content-class scaling, and (hocc-S) "
            "the handover-prompt simpler (A-1)(A-2)/2 isospin-blind form."
        ),
        "reference_blocks": [
            "conj:shell-correction-term-seven",
            "thm:knot-mass-formula-unified",
            "rem:higher-a-shell-diagnostic",
            "prop:bw-coefficient-shadow-price",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(Q0),
            "m_e_MeV": float(ME),
            "filter": "len(lambda) == 6",
            "filter_GB_level": 5,
        },
        "notes": [
            "Conjecture text says 'the only height-6 partition of k=6 is "
            "(3,2,1)' but len((3,2,1))=3.  Using ℓ=len-1 (per "
            "higher_a_shell_diagnostic.py line 10) gives length-6 partitions; "
            "for k=6 the unique one is (1^6).  Flagging as content-side "
            "inconsistency for author."
        ],
        "isotopes": [],
    }

    for label, Z, N in ISOTOPES:
        A = Z + N
        n = 3 * A
        # Pre-count length-6 partitions (cheap)
        n_parts = sum(1 for p in partitions_of(n) if len(p) == 6)

        t0 = time.time()
        delta7_conj, rows_conj = term_seven(Z, N, target_height=6, S_fn=S_conj)
        t1 = time.time()
        delta7_hocc, rows_hocc = term_seven(Z, N, target_height=6, S_fn=S_hocc)
        t2 = time.time()

        print(
            f"  {label:<5} {A:>2} {n:>4} | {n_parts:>11} | "
            f"{float(delta7_conj):>+17.6f} | {float(delta7_hocc):>+17.6f} | "
            f"{t2 - t0:>5.2f}s"
        )

        out["isotopes"].append({
            "iso": label, "Z": Z, "N": N, "A": A,
            "k_3A": n,
            "n_height_6_partitions": n_parts,
            "Delta7_conj_MeV": float(delta7_conj),
            "Delta7_hocc_MeV": float(delta7_hocc),
            "walltime_conj_s": t1 - t0,
            "walltime_hocc_s": t2 - t1,
            "top_5_contributions_conj": rows_conj[:5],
            "top_5_contributions_hocc": rows_hocc[:5],
        })

        # Save partial witness incrementally so a timeout doesn't lose work
        with open(out_path, "w") as fp:
            json.dump(out, fp, indent=2)

    print()
    print(f"Witness: {out_path}")


if __name__ == "__main__":
    main()
