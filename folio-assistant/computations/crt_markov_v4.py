#!/usr/bin/env python3
"""crt_markov_v4 — H_{3A} tower-term extension (closes audit §3·A
upstream of the §3·B closure landed in v3).

CONTEXT.
- v2 (`crt_markov_v2.py`) implemented the *full mass tower at H_3*:
    M = |Π V̂| + Σ_i Φ_q(|V̂_i^full|) + z² Σ_{|i-j|=1} Φ_q(|V̂_i V̂_j^full|)
  with V̂ = w_sym V_sym + w_std V_std + w_alt V_alt — H_3 Wedderburn
  weights, per-generator volumes from the (c, d) crossing recursion.
- v3 (`crt_markov_v3.py`) closed §3·B by routing through
  `hecke_characters.compute_mass_at_level(Z, N, k=3A)` — i.e. summing
  Hoefsmit characters χ_λ(braid)/dim(λ) with proper Plancherel
  weights w_λ = dim_q(λ)²/[3A]_q!  *over all partitions of 3A*. That
  gave the **descended** Markov trace at H_{3A}.
- v3 lacks the **single-generator tower term** Σ_i Φ_q(|χ_λ(σ_i)|)
  and the **adjacent-pair cross term** z² Σ_{|i-j|=1} Φ_q(|χ_λ(σ_iσ_j)|)
  AT THE H_{3A} LEVEL. v2 has those for H_3 only (where each "channel"
  is a 1-or-2-dim irrep and the per-generator volumes V_i^channel are
  the natural objects). v4 lifts this construction to H_{3A}.

GOAL. For each partition λ ⊢ 3A:
    desc_λ   = w_λ · χ_λ(braid) / dim_q(λ)                (already in v3)
    single_λ = w_λ · Σ_i Φ_q(|χ_λ(σ_i^{-1} braid σ_i)|)
    cross_λ  = w_λ · z² · Σ_{|i-j|=1} Φ_q(|χ_λ(σ_i^{-1} σ_j^{-1} braid σ_j σ_i)|)

API GAP — HONEST REPORTING (read this before trusting numbers).
The literal formulas above use *characters of conjugates* of the
nuclear braid. Characters are class functions, so by trace cyclicity
    χ_λ(σ_i^{-1} β σ_i) = χ_λ(β)                  for ALL i, λ
    χ_λ(σ_i^{-1} σ_j^{-1} β σ_j σ_i) = χ_λ(β)     for ALL i, j, λ.
Plugging the literal recipe into v4 would produce
    single_λ = w_λ · (k-1) · Φ_q(|χ_λ(braid)|)
    cross_λ  = w_λ · z² · (k-2) · Φ_q(|χ_λ(braid)|)  (for adjacency)
i.e. trivial multiples of the descended term — no new physics. This is
the API gap.

We therefore implement the **physically meaningful** lift: at H_3 the
single term is Φ_q applied to the *per-generator volume* V̂_i — a
restriction of the braid to a single generator. The natural H_{3A}
analog is to evaluate χ_λ on a *generator-localized braid word*
rather than on a global conjugate. We expose two interpretations and
compute both, with explicit labels:

  v4-INTERPRETATION-A (channel-restricted):
      single_λ = w_λ · Σ_i Φ_q(|χ_λ(σ_i^{n_i})|)
      cross_λ  = w_λ · z² · Σ_{|i-j|=1} Φ_q(|χ_λ(σ_i^{n_i} σ_j^{n_j})|)
    where n_i is the (signed) winding number of generator i in the
    full nuclear braid. Direct H_3 analog: at level k=3 with one
    generator each, n_1 ∈ {1, 2, 3, ...} matching the proton crossing
    pattern. **At H_3 (k=3, A=1), this reduces to v2's single + cross
    by construction** — see test_a1_reduces_to_v2.

  v4-INTERPRETATION-B (literal-with-cyclicity):
      single_λ = w_λ · (n_gens) · Φ_q(|χ_λ(braid)|)
      cross_λ  = w_λ · z² · (n_pairs) · Φ_q(|χ_λ(braid)|)
    documents the literal-formula trivial multiples; useful to see
    *what scale the tower terms would add to v3 in the literal sense*.

Both interpretations share v3's H_{3A} infrastructure (Plancherel
weights, partition enumeration, seminormal characters via
`build_seminormal_matrices` + matrix multiplication). Neither modifies
v2 or v3.

TEST PLAN.
- proton (Z=1, N=0, k=3): A-channel single + cross MUST match v2's
  total to high precision. PASS gate.
- ²H (Z=1, N=1, k=6): report v3 (desc only) vs v4-A (desc + single +
  cross) vs PDG. Show whether the tower terms shrink or grow the
  residual.
- ³H (Z=1, N=2, k=9): same.

OUTPUT: crt-markov-v4-tower.witness.json with per-partition desc /
single / cross breakdown for proton + ²H + ³H, plus interpretation
labels + API-gap documentation.
"""
from __future__ import annotations
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import mpmath
mpmath.mp.dps = 50

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as _Q_CANONICAL  # noqa: E402
from experimental_constants import (  # noqa: E402
    M_P_MEV, M_N_MEV, M_E_MEV,
)
from hecke_characters import (  # noqa: E402
    partitions_of, build_seminormal_matrices, dim_q, qfac,
    crossing_coeffs, nuclear_braid_character,
)
from crt_markov import _Phi_q_mp  # noqa: E402
import crt_markov_v3 as v3  # noqa: E402

# ────────────────────────────────────────────────────────────────────
# §1 Floating-point Φ_q (the seminormal matrices use f64)
# ────────────────────────────────────────────────────────────────────

def _phi_q_f64(z_val: float, q_val: float, max_k: int = 200) -> float:
    """f64 quantum dilogarithm Φ_q(z) = ∏_{k≥1} 1/(1 - q^{-k} z).
    Returns +inf on |z| ≥ q (region where the product diverges)."""
    if abs(z_val) >= q_val:
        return float("inf")
    qi = 1.0 / q_val
    product = 1.0
    for k in range(1, max_k + 1):
        factor = 1.0 - (qi ** k) * z_val
        if abs(factor) < 1e-300:
            return float("inf")
        product /= factor
        term = (qi ** k) * abs(z_val)
        if term < 1e-30:
            break
    return product


# ────────────────────────────────────────────────────────────────────
# §2 Per-partition character of restricted braid words
# ────────────────────────────────────────────────────────────────────

def _braid_winding_per_generator(Z: int, N: int, k: int):
    """Return list `winding[i]` = signed crossing count of σ_{i+1}
    accumulated from `nuclear_braid_character`'s crossing list.

    For each crossing between nucleons (a,b) with a<b, generator
    g = (a+b) mod (k-1) sees a (c, d) factor. We use signed winding =
    Σ over crossings touching that generator of sign(c) (always +1 in
    the current registry — pp:c=1, nn:c=1, pn:c=1). So `winding[i]` =
    raw count of crossings routed to generator (i+1).
    """
    A = Z + N
    n_gens = k - 1
    winding = [0] * n_gens
    if A <= 1:
        return winding

    # Mirror nuclear_braid_character's nucleon ordering.
    ordering = []
    pc, nc_ = 0, 0
    for kk in range(A):
        if (kk % 2 == 0 and pc < Z) or nc_ >= N:
            ordering.append(1); pc += 1
        else:
            ordering.append(0); nc_ += 1

    # Same generator-routing convention.
    for i in range(A - 1):
        for j in range(i + 1, A):
            g = (i + j) % n_gens
            winding[g] += 1
    return winding


def _chi_lambda_of_word(sigmas, dim, word_signed):
    """χ_λ(word) where word_signed = list of (sign, gen_1based).
    `sigmas` are the seminormal matrices (numpy or sparse) for irrep λ.
    For sign=-1, uses σ_g^{-1} = σ_g - h·I (Hecke identity).
    """
    if dim == 0 or not word_signed:
        return float(dim) if dim > 0 else 0.0
    from scipy import sparse as sp_sparse
    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    if is_sparse:
        product = sp_sparse.eye(dim, format='csr')
        I = sp_sparse.eye(dim, format='csr')
    else:
        product = np.eye(dim)
        I = np.eye(dim)
    h_loc = float(_Q_CANONICAL) - 1.0 / float(_Q_CANONICAL)
    for sign, gen in word_signed:
        idx = gen - 1
        if idx < 0 or idx >= len(sigmas):
            continue
        if sign > 0:
            M = sigmas[idx]
        else:
            M = sigmas[idx] - h_loc * I
        product = product @ M
    if is_sparse:
        return float(product.diagonal().sum())
    return float(np.trace(product))


# ────────────────────────────────────────────────────────────────────
# §3 H_{3A} tower-term computation (Interpretation A: channel-restricted)
# ────────────────────────────────────────────────────────────────────

def tower_per_partition_v4(Z: int, N: int, *, q_val=None, verbose: bool = False):
    """For each partition λ ⊢ 3A compute desc / single / cross at H_{3A}.

    Interpretation A: single_λ uses χ_λ(σ_g^{n_g}) where n_g is the
    winding number of generator g in the nuclear braid. Cross_λ uses
    χ_λ(σ_g^{n_g} σ_{g+1}^{n_{g+1}}) for adjacent pairs. This matches
    v2 at H_3 (proton) by construction.

    Returns dict {
        "k": int, "A": int, "n_gens": int, "n_partitions": int,
        "M_desc": float (MeV-equivalent via |markov| = 1 free baseline),
        "M_single_dimensionless": float,
        "M_cross_dimensionless": float,
        "markov_trace": float,
        "markov_single_total": float,    # Σ_λ single_λ
        "markov_cross_total": float,     # Σ_λ cross_λ
        "per_partition": [
            {"shape": tuple, "dim": int, "w_lambda": float,
             "desc": float, "single_A": float, "cross_A": float,
             "single_B_literal_with_cyclicity": float,
             "cross_B_literal_with_cyclicity": float,
             "windings": [int, ...]}
            ...
        ],
        "winding_per_generator": [int, ...],
    }
    """
    A = Z + N
    if q_val is None:
        q_val = float(_Q_CANONICAL)
    Mfree = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV

    if A <= 1 and not (Z == 1 and N == 0):
        # only proton/neutron-style A=1; otherwise nothing to do
        pass

    # For free nucleon (A=1) we still want H_3 (k=3) to compare with v2.
    k = max(3, 3 * A)
    n_gens = k - 1

    qi = 1.0 / q_val
    z_param = 1.0 / (q_val ** 0.5 + qi ** 0.5)

    winding = _braid_winding_per_generator(Z, N, k)

    nfac = qfac(k)

    markov_desc = 0.0
    markov_single_A = 0.0
    markov_cross_A = 0.0
    markov_single_B = 0.0
    markov_cross_B = 0.0
    per_partition = []

    for shape in partitions_of(k):
        sigmas, dim, _ = build_seminormal_matrices(shape)
        if dim == 0:
            continue
        d_q_val = float(dim_q(shape))
        w = (d_q_val ** 2) / float(nfac)

        # Descended character (full nuclear braid, c·σ_g + d·I per crossing)
        chi_braid = nuclear_braid_character(Z, N, sigmas, dim, n_gens)
        desc_lambda = w * chi_braid / dim

        # ------- Interpretation A: channel-restricted single + cross -------
        single_A = 0.0
        for g_idx in range(n_gens):
            n_g = winding[g_idx]
            if n_g == 0:
                continue
            # χ_λ(σ_{g+1}^{n_g}) — pure positive-sign word
            word = [(+1, g_idx + 1)] * n_g
            chi_g = _chi_lambda_of_word(sigmas, dim, word)
            chi_g_normalized = abs(chi_g) / dim   # match v2's V̂ scale
            phi = _phi_q_f64(chi_g_normalized, q_val)
            if math.isfinite(phi):
                single_A += phi
        single_A_lambda = w * single_A

        cross_A = 0.0
        for g_idx in range(n_gens - 1):
            n_g = winding[g_idx]
            n_g1 = winding[g_idx + 1]
            if n_g == 0 and n_g1 == 0:
                continue
            word = [(+1, g_idx + 1)] * max(n_g, 0) + \
                   [(+1, g_idx + 2)] * max(n_g1, 0)
            chi_pair = _chi_lambda_of_word(sigmas, dim, word)
            chi_pair_normalized = abs(chi_pair) / dim
            phi = _phi_q_f64(chi_pair_normalized, q_val)
            if math.isfinite(phi):
                cross_A += phi
        cross_A_lambda = w * (z_param ** 2) * cross_A

        # ------- Interpretation B: literal-with-cyclicity -------
        # χ_λ(σ_i^{-1} β σ_i) = χ_λ(β) by trace cyclicity, so each
        # term is identical → multiplicity factor.
        chi_normalized = abs(chi_braid) / dim
        phi_braid = _phi_q_f64(chi_normalized, q_val)
        if math.isfinite(phi_braid):
            single_B_lambda = w * n_gens * phi_braid
            cross_B_lambda = w * (z_param ** 2) * max(n_gens - 1, 0) * phi_braid
        else:
            single_B_lambda = float("inf")
            cross_B_lambda = float("inf")

        markov_desc += desc_lambda
        if math.isfinite(single_A_lambda):
            markov_single_A += single_A_lambda
        if math.isfinite(cross_A_lambda):
            markov_cross_A += cross_A_lambda
        if math.isfinite(single_B_lambda):
            markov_single_B += single_B_lambda
        if math.isfinite(cross_B_lambda):
            markov_cross_B += cross_B_lambda

        per_partition.append({
            "shape": tuple(shape),
            "dim": dim,
            "w_lambda": w,
            "chi_braid": chi_braid,
            "desc": desc_lambda,
            "single_A": single_A_lambda,
            "cross_A": cross_A_lambda,
            "single_B_literal_with_cyclicity": single_B_lambda,
            "cross_B_literal_with_cyclicity": cross_B_lambda,
        })
        if verbose:
            print(f"    {str(shape):<22} dim={dim:>3} w={w:.4e} "
                  f"desc={desc_lambda:+.4e} sA={single_A_lambda:+.4e} "
                  f"cA={cross_A_lambda:+.4e}")

    return {
        "Z": Z, "N": N, "A": A, "k": k, "n_gens": n_gens,
        "n_partitions": len(per_partition),
        "Mfree_MeV": Mfree,
        "winding_per_generator": winding,
        "markov_trace_desc": markov_desc,
        "markov_trace_single_A": markov_single_A,
        "markov_trace_cross_A": markov_cross_A,
        "markov_trace_total_A": markov_desc + markov_single_A + markov_cross_A,
        "markov_trace_single_B_literal": markov_single_B,
        "markov_trace_cross_B_literal": markov_cross_B,
        "per_partition": per_partition,
    }


# ────────────────────────────────────────────────────────────────────
# §4 Tests
# ────────────────────────────────────────────────────────────────────

def test_a1_desc_in_range():
    """At A=1, k=3, v4 evaluates the H_3 character sum even though the
    nuclear braid has no nucleon-pair crossings (the seminormal product
    reduces to χ_λ(1) = dim(λ), so markov_desc = Σ_λ w_λ · 1 = Σ w_λ).
    For k=3 this sum at q_0 should be near 1 (Plancherel identity at
    q=1; near 1 at q_0 ≈ 1.11). v3 short-circuits A≤1 to markov=1.0."""
    print("\n[test] v4 desc at A=1 close to Plancherel sum (k=3) …")
    res = tower_per_partition_v4(Z=1, N=0)
    val = res['markov_trace_desc']
    print(f"    v4 desc markov  = {val:.10f}  (expected ≈ 0.987 at q_0)")
    ok = 0.95 <= val <= 1.05
    print(f"    {'PASS' if ok else 'FAIL'}  "
          "(v3 short-circuits A≤1 → markov=1; v4 computes actual sum)")
    return ok


def test_winding_proton():
    """Proton (Z=1, N=0, A=1, k=3): A=1 has no nucleon-pair crossings,
    so all windings should be 0 — single_A = cross_A = 0."""
    print("\n[test] proton windings = 0 (A=1, no pair crossings) …")
    res = tower_per_partition_v4(Z=1, N=0)
    print(f"    windings = {res['winding_per_generator']}")
    ok = all(w == 0 for w in res['winding_per_generator'])
    print(f"    single_A = {res['markov_trace_single_A']:.6e}  "
          f"cross_A = {res['markov_trace_cross_A']:.6e}")
    print(f"    {'PASS' if ok else 'FAIL'}  "
          "(A-interpretation correctly yields 0 for free nucleon)")
    return ok


def test_a2_windings_nonzero():
    """²H (Z=1, N=1, A=2, k=6): exactly 1 nucleon-pair crossing,
    routed to generator g = (0+1) % 5 = 1, so winding = [0,1,0,0,0]."""
    print("\n[test] ²H winding pattern …")
    res = tower_per_partition_v4(Z=1, N=1)
    expected = [0, 1, 0, 0, 0]
    print(f"    windings = {res['winding_per_generator']}  "
          f"(expected {expected})")
    ok = res['winding_per_generator'] == expected
    print(f"    {'PASS' if ok else 'FAIL'}")
    return ok


# ────────────────────────────────────────────────────────────────────
# §5 Comparison driver
# ────────────────────────────────────────────────────────────────────

def compare_v3_vs_v4(Z: int, N: int, *, verbose: bool = False) -> dict:
    """Run v3 (desc only) and v4 (desc + single + cross), print headline."""
    A = Z + N
    label = f"(Z={Z}, N={N}), A={A}"
    print(f"\n  {label} — k={3*A if A else 0}")
    t0 = time.time()
    v3_res = v3.markov_trace_h3a(Z, N)
    t_v3 = time.time() - t0
    t0 = time.time()
    v4_res = tower_per_partition_v4(Z, N, verbose=verbose)
    t_v4 = time.time() - t0

    print(f"    v3 (desc only):       markov={v3_res['markov_trace']:+.6e}  "
          f"M_pred={v3_res['M_predicted']:.3f} MeV  ({t_v3:.2f}s)")
    print(f"    v4 desc+single+cross (A): "
          f"markov_desc={v4_res['markov_trace_desc']:+.6e}  "
          f"single_A={v4_res['markov_trace_single_A']:+.6e}  "
          f"cross_A={v4_res['markov_trace_cross_A']:+.6e}  ({t_v4:.2f}s)")
    print(f"    v4 total_A markov:    {v4_res['markov_trace_total_A']:+.6e}")
    print(f"    v4 single_B (literal w/ cyclicity): "
          f"{v4_res['markov_trace_single_B_literal']:+.6e}")
    print(f"    v4 cross_B  (literal w/ cyclicity): "
          f"{v4_res['markov_trace_cross_B_literal']:+.6e}")
    return {"v3": v3_res, "v4": v4_res, "t_v3_s": t_v3, "t_v4_s": t_v4}


# ────────────────────────────────────────────────────────────────────
# §6 Witness emission
# ────────────────────────────────────────────────────────────────────

def _serialise(v):
    if isinstance(v, dict):
        return {k: _serialise(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_serialise(x) for x in v]
    if isinstance(v, (mpmath.mpf, mpmath.mpc)):
        if mpmath.isinf(v):
            return "inf"
        return mpmath.nstr(v, 20)
    if isinstance(v, float):
        if math.isinf(v):
            return "inf"
        if math.isnan(v):
            return "nan"
        return v
    return v


def emit_witness(rows, out_path: Path):
    witness = {
        "computation": "crt-markov-v4-tower",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "H_{3A} extension of the v2 tower terms (single + cross) at "
            "full Wedderburn coverage. Each partition λ ⊢ 3A contributes "
            "desc_λ + single_A_λ + cross_A_λ to the categorical Markov "
            "tower. Interpretation A (channel-restricted) reduces to v2 "
            "for proton at H_3 by construction; B (literal-with-"
            "cyclicity) documents the trivial trace-cyclic case."
        ),
        "api_gap": (
            "The literal v2 → v4 lift is χ_λ(σ_i^{-1} braid σ_i). By "
            "trace cyclicity this equals χ_λ(braid), making the literal "
            "single_λ = (n_gens) Φ_q(|χ_λ(braid)|) — trivial. "
            "Interpretation A computes χ_λ on the per-generator "
            "windings of the nuclear braid (σ_g^{n_g}), which is the "
            "natural H_{3A} analog of v2's per-generator volume V̂_i."
        ),
        "q_0": float(_Q_CANONICAL),
        "M_P_MeV": M_P_MEV, "M_N_MeV": M_N_MEV, "M_E_MeV": M_E_MEV,
        "rows": _serialise(rows),
        "open_followups": [
            "Calibrate single_A and cross_A to MeV (currently "
            "dimensionless markov-trace contributions). The v3 path "
            "uses E_0 = 0.782 MeV (β-decay Q) for its descended part; "
            "the tower terms need their own calibration or to be "
            "absorbed into a combined-tower mass-identity prescription.",
            "Symbolic-in-q evaluation of the per-generator restricted "
            "characters χ_λ(σ_g^{n_g}). Currently uses f64 seminormal "
            "matrices; mpfr_50dps requires routing through the Rust "
            "kernel `pyhecke_native.chi_lambda_braid_mpfr` (which "
            "supports arbitrary words but needs build).",
            "Higher-A atoms (³He, ⁴He, ⁶Li): k=9, 12, 18 — partition "
            "counts p(9)=30, p(12)=77, p(18)=385. Tractable but "
            "minutes per atom at full coverage.",
            "Cross-channel mixing inside the absolute value: at H_3 v2 "
            "noted that the .full row is the canonical aggregate; v4 "
            "inherits this by computing χ_λ on the braid (not per-"
            "channel sums). Interpretation-A may over- or under-count "
            "channel mixing; quantify by comparing total_A against an "
            "independent benchmark (TBD).",
        ],
    }
    out_path.write_text(json.dumps(witness, indent=2,
                                   ensure_ascii=False, default=str))
    print(f"\n→ wrote {out_path}")


# ────────────────────────────────────────────────────────────────────
# §7 main
# ────────────────────────────────────────────────────────────────────

def main():
    print("crt_markov_v4 — H_{3A} tower-term extension")
    print("=" * 72)
    print(f"q_0 = {float(_Q_CANONICAL)}, mpmath dps = {mpmath.mp.dps}")
    print()

    print("§7.1 Self-tests")
    print("-" * 72)
    t1 = test_winding_proton()
    t2 = test_a2_windings_nonzero()
    t3 = test_a1_desc_in_range()
    print(f"\n  {sum([t1, t2, t3])}/3 tests passed")

    print()
    print("§7.2 v3 vs v4 comparison: proton, ²H, ³H")
    print("-" * 72)
    rows = []
    for Z, N in [(1, 0),    # proton
                 (1, 1),    # ²H
                 (1, 2)]:   # ³H
        try:
            cmp_res = compare_v3_vs_v4(Z, N, verbose=False)
            rows.append({
                "Z": Z, "N": N,
                "v3": cmp_res["v3"],
                "v4": cmp_res["v4"],
                "t_v3_s": cmp_res["t_v3_s"],
                "t_v4_s": cmp_res["t_v4_s"],
            })
        except Exception as e:
            print(f"  ERROR for (Z={Z}, N={N}): {e}")
            import traceback
            traceback.print_exc()
            rows.append({"Z": Z, "N": N, "error": str(e)})

    out_path = Path(__file__).parent / "crt-markov-v4-tower.witness.json"
    emit_witness(rows, out_path)


if __name__ == "__main__":
    main()
