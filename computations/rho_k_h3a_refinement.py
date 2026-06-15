#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical sympy/mpmath consumer; symbolic-q polynomials live downstream in hoefsmit_symbolic / y_lambda_wenzl_bridge witnesses.
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

ρ_K refinement via H_{3A} Wedderburn weights — deuteron proof-of-concept (P3' from PR #564).

Implements the **first concrete instance** of the per-block binding-fraction
$\\Delta_\\lambda(K)$ closed form from `prop:rho-k-h3a-refinement`:

    ρ_K(q) - ρ_K^LO(Z, N)
       = (1 / |tr_M(β_K)|) · Σ_{λ ⊢ 3A} y_λ(q) · χ^λ(β_K) · Δ_λ(K)

For the **deuteron** (A=2, n=6, p(6)=11 partitions of 6) this script:

  1. Loads |tr_M(β_D)| from atomic-tr-m-mpfr-50dps.witness.json.
  2. Enumerates the 11 partitions of 6.
  3. For each λ ⊢ 6:
     a. Loads y_λ(q_0) from y-lambda-wenzl-bridge-symbolic-witness.json
        (closed form, evaluated at q_0 to 50 dps).
     b. Computes the Hoefsmit character χ^λ(β_D) via
        `hoefsmit_symbolic.chi_lambda_symbolic`, evaluated at q_0.
  4. Verifies the Schur-Weyl identity Σ_λ y_λ χ^λ = tr_M(β_D)
     (sanity check; should match to 50 dps numerical precision).
  5. **Dominant-partition heuristic.**  The single mass equation
     ρ_K - ρ_K^LO = (1/|tr_M|) Σ_λ y_λ χ^λ Δ_λ is underdetermined
     by 11 unknowns.  This proof-of-concept *assumes* Δ_λ is supported
     only on a single partition (default: the "balanced" (3,2,1)
     with content sum 0) and solves for the corresponding scalar.
     The script then sweeps every λ and reports which partition
     yields the **smallest** |Δ| (Occam's-razor minimal perturbation).
  6. Verifies that with the chosen Δ_λ, the predicted M(D)
     reproduces CODATA 1875.61294257 MeV exactly (by construction).

Output: `rho-k-h3a-refinement.witness.json` with the full deuteron
profile.  `compute_status: "deuteron"` flags the atom as tractable.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from multiprocessing import Pool, cpu_count
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from hecke_characters import standard_young_tableaux  # noqa: E402
from hoefsmit_symbolic import chi_lambda_symbolic, Q as Q_SYM  # noqa: E402
from q_parameter import Q_MP  # noqa: E402

set_compute_dps()


# ── Numeric Hoefsmit builder (mirrors _hoefsmit_build but at concrete q) ──
def hoefsmit_matrices_numeric(shape, q_mp):
    """Build Hoefsmit matrices at concrete mpmath q.  ~100× faster than
    the symbolic path: skips polynomial cancellation and uses mpmath
    arithmetic at the working precision (mp.mp.dps).

    Mirrors hecke_character_symbolic._hoefsmit_build exactly; only the
    field of entries differs (mpmath.mpf vs sympy expr in q).
    """
    n = sum(shape)
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0, []

    q = mp.mpf(q_mp)
    one = mp.mpf(1)
    h = q - one / q

    matrices = []
    for k in range(1, n):
        M = mp.matrix(dim, dim)
        processed = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = h / (one - q ** (-2 * rho))

            swap_map = dict(syts[i])
            swap_map[k], swap_map[k + 1] = ci_k1, ci_k
            j = None
            for jj in range(dim):
                if jj == i:
                    continue
                if syts[jj] == swap_map:
                    j = jj
                    break

            if j is None:
                M[i, i] = a
                processed.add(i)
            else:
                a_prime = h / (one - q ** (2 * rho))
                b_sq = a * a_prime + one
                b = mp.sqrt(b_sq)
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = b
                M[j, i] = b
                processed.add(i)
                processed.add(j)
        matrices.append(M)
    return matrices, dim, syts


def chi_numeric(shape, crossings, q_mp):
    """Numeric χ^λ_q(T_w) at concrete q via mpmath matrix product.

    Returns: mp.mpf trace.  Microseconds per crossing × ~22 crossings ×
    dim² ≤ 256 → milliseconds per partition (vs. minutes symbolic).
    """
    matrices, dim, _ = hoefsmit_matrices_numeric(shape, q_mp)
    if dim == 0:
        return mp.mpf(0)

    q = mp.mpf(q_mp)
    h = q - mp.mpf(1) / q
    d_lookup = {"sigma": mp.mpf(0), "sigma_inv": -h, "averaged": -h / 2}
    eye = mp.eye(dim)

    M = mp.eye(dim)
    for gen_idx, ctype in crossings:
        if gen_idx < 0 or gen_idx >= len(matrices):
            raise IndexError(f"gen_idx {gen_idx} out of range for shape {shape}")
        sigma = matrices[gen_idx]
        d_val = d_lookup[ctype]
        cross = sigma + d_val * eye
        M = M * cross

    tr = mp.mpf(0)
    for i in range(dim):
        tr += M[i, i]
    return tr


# Worker for multiprocessing — top-level so Pool can pickle it.
def _per_partition_numeric(args):
    lam, crossings, q_str_50dps, dps = args
    mp.mp.dps = dps
    q_mp = mp.mpf(q_str_50dps)
    chi = chi_numeric(lam, crossings, q_mp)
    # str(mpf) truncates to ~16 digits (Python repr); use nstr for full dps.
    return lam, mp.nstr(chi, dps, strip_zeros=False)


def _per_partition_symbolic(args):
    lam, crossings, q_str_50dps, dps = args
    mp.mp.dps = dps
    chi_sym = chi_lambda_symbolic(lam, crossings)
    sub = chi_sym.subs(Q_SYM, sp.sympify(q_str_50dps))
    return lam, str(sub.evalf(dps))

# ── Calibration anchors (CODATA) — centralised in codata_constants ──
from codata_constants import M_E_MEV, M_P_MEV, M_N_MEV, M_D_MEV  # noqa: E402

# ── Deuteron braid word (3A=6 strands) ─────────────────────────
# Canonical convention (matches atomic-tr-m-mpfr-50dps.witness.json):
# β_D = β_p · I · β_n in H_3 ⊗ H_3 ⊂ H_6 with interface I at σ_3 (gen_idx=2).
# Built by mass_at_3A_proper.atom_braid_word_3A(1, 1):
#   - per nucleon: intra g₀ (7 crossings: 3×σ + uu/ud + 2×σ),
#                  intra g₁ (4 crossings: 3×σ⁻¹ + ud/dd)
#   - inter (p,n): 1× averaged at gen_idx 2  (= σ_3, the interface I)
#   - total: 11 + 1 + 11 = 23 crossings (vs 22 in the legacy disjoint word)
#
# Per `hecke-branching-trace-decomposition.md`: this is NOT a disjoint
# product — the interface I = σ_3 - h/2·1 acts as an operator-valued
# A^λ_{μ,ν}(I), non-scalar for 9 of 11 partitions λ ⊢ 6.
#
# The legacy disjoint word σ₁⁷σ₂⁴σ₄⁶σ₅⁴σ₄⁻¹ from
# markov_trace_axiomatic_multi_atom.py does NOT reproduce
# |tr_M(β_D)| = 0.388286... in the witness (Schur-Weyl fails).
def deuteron_canonical_crossings():
    """Build the canonical 23-crossing deuteron word as
    (gen_idx, ctype) pairs for chi_numeric / chi_lambda_symbolic.

    Thin wrapper around the shared
    `canonical_braid_crossings.atom_canonical_crossings` utility
    (gemini-code-assist on PR #572).  Source of truth:
    `mass_at_3A_proper.atom_braid_word_3A(Z=1, N=1)`.
    """
    from canonical_braid_crossings import atom_canonical_crossings
    return atom_canonical_crossings(1, 1)


def word_to_crossings(word_1idx):
    """Convert a 1-indexed signed-int braid word to (gen_idx, ctype) pairs.

    Used only for the legacy disjoint test word; canonical deuteron
    extraction uses `deuteron_canonical_crossings()`.

    Positive `i` → σ_i  →  (i-1, 'sigma')
    Negative `-i` → σ_i^{-1}  →  (i-1, 'sigma_inv')
    """
    out = []
    for tok in word_1idx:
        if tok > 0:
            out.append((tok - 1, "sigma"))
        elif tok < 0:
            out.append((-tok - 1, "sigma_inv"))
        else:
            raise ValueError("braid generator index 0 is invalid (1-indexed)")
    return out


def partitions_of_n(n):
    """Enumerate partitions of n as tuples in weakly-decreasing order."""
    if n == 0:
        return [()]
    out = []

    def _rec(rem, max_part, acc):
        if rem == 0:
            out.append(tuple(acc))
            return
        for k in range(min(rem, max_part), 0, -1):
            _rec(rem - k, k, acc + [k])

    _rec(n, n, [])
    return out


def load_y_lambda_n6():
    """Load symbolic closed-form y_λ for n=6 from the Wenzl-bridge witness.

    Returns: dict mapping tuple(partition) → sympy expression in q.

    NOTE: We deliberately skip `sp.cancel` here. Each y_λ is a ~4000-char
    rational expression in q; `cancel` on the full y_λ (degree 30+ poly
    over degree 30+ poly with hundreds of terms) does not finish in
    minutes. We only need the *numeric value* at q_0, and `subs(q, q_0)
    .evalf(50)` is fast on the unsimplified expression.
    """
    path = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"
    d = json.loads(path.read_text())
    n6 = d["tables_by_n"]["6"]
    out = {}
    for w in n6["weights"]:
        lam = tuple(w["partition"])
        expr = sp.sympify(w["y_lambda_symbolic"])
        free = expr.free_symbols
        if free:
            qsym = next(iter(free))
            if qsym is not Q_SYM:
                expr = expr.subs(qsym, Q_SYM)
        out[lam] = expr
    return out


def load_deuteron_tr_M():
    """Load |tr_M(β_D)| at q_0 from atomic-tr-m-mpfr-50dps.witness.json."""
    path = _pb.witness_path("atomic-tr-m-mpfr-50dps.witness.json", HERE)
    d = json.loads(path.read_text())
    for r in d["results"]:
        if r["atom"] == "deuteron":
            tr = mp.mpf(r["tr_M_at_q0_50dps"])
            return tr
    raise RuntimeError("deuteron entry not found in atomic-tr-m-mpfr-50dps")


def evaluate_at_q0(expr) -> mp.mpf:
    """Evaluate sympy expr at q = q_0 to current mpmath precision.

    NOTE: `str(Q_MP)` truncates to ~16 digits (Python repr), capping
    precision at f64 epsilon. We use `mp.nstr(Q_MP, mp.mp.dps)` to
    preserve the full 50-dps q_0 value through sympy's substitution.
    """
    q0_str = mp.nstr(Q_MP, mp.mp.dps, strip_zeros=False)
    sub = expr.subs(Q_SYM, sp.sympify(q0_str))
    return mp.mpf(str(sub.evalf(mp.mp.dps)))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--symbolic", action="store_true",
        help="Use the slow symbolic-q path (sympy chi_lambda_symbolic). "
             "Default is the numeric mpmath path — ~100× faster, "
             "bit-identical to the symbolic path at q_0 (50 dps)."
    )
    parser.add_argument(
        "--workers", type=int, default=min(cpu_count(), 11),
        help="multiprocessing.Pool size (default = min(cpu_count, 11))."
    )
    args = parser.parse_args()
    engine = "symbolic" if args.symbolic else "numeric"

    print("=" * 96)
    print("  ρ_K H_{3A} Wedderburn refinement — DEUTERON proof-of-concept")
    print(f"  (P3' from AUDIT-DEEP-2026-05.md §7; PR #564)  engine={engine}, workers={args.workers}")
    print("=" * 96)

    print(f"\n  q_0 = {mp.nstr(Q_MP, 25)}")
    print(f"  m_e = {mp.nstr(M_E_MEV, 8)} MeV (CODATA)")
    print(f"  m_p = {mp.nstr(M_P_MEV, 8)} MeV (CODATA)")
    print(f"  m_n = {mp.nstr(M_N_MEV, 8)} MeV (CODATA)")
    print(f"  M(D) = {mp.nstr(M_D_MEV, 12)} MeV (CODATA)")

    # ── Step 1: |tr_M(β_D)| ───────────────────────────────────
    tr_M = load_deuteron_tr_M()
    abs_tr_M = abs(tr_M)
    print(f"\n  |tr_M(β_D)| (50 dps) = {mp.nstr(abs_tr_M, 30)}")

    # ── Step 2: ρ_K^LO and the residual to be explained ────────
    rho_K_LO = (M_P_MEV + M_N_MEV) / (M_E_MEV * abs_tr_M)
    M_pred_LO = rho_K_LO * M_E_MEV * abs_tr_M  # = m_p + m_n by construction
    rho_K_codata = M_D_MEV / (M_E_MEV * abs_tr_M)
    delta_rho = rho_K_codata - rho_K_LO
    err_pct_LO = (M_pred_LO - M_D_MEV) / M_D_MEV * 100
    print(f"\n  ρ_K^LO         = {mp.nstr(rho_K_LO, 25)}")
    print(f"  ρ_K^CODATA     = {mp.nstr(rho_K_codata, 25)}")
    print(f"  Δρ_K (residual) = {mp.nstr(delta_rho, 25)}")
    print(f"  M^LO(D)        = {mp.nstr(M_pred_LO, 14)} MeV  "
          f"(err = {mp.nstr(err_pct_LO, 4)} %)")
    print(f"  binding gap    = {mp.nstr(M_pred_LO - M_D_MEV, 8)} MeV  "
          f"(should be ≈ +2.225 MeV deuteron binding)")

    # ── Step 3: per-λ y_λ and χ^λ(β_D) at q_0 ─────────────────
    print("\n  Loading y_λ(q_0) from Wenzl-bridge witness …")
    y_lam_sym = load_y_lambda_n6()

    crossings = deuteron_canonical_crossings()
    parts = partitions_of_n(6)
    assert len(parts) == 11, f"expected 11 partitions, got {len(parts)}"
    print(f"  Computing χ^λ(β_D) via {engine} engine "
          f"({len(parts)} partitions, {len(crossings)} crossings on H_6) …")

    q_str_50 = mp.nstr(Q_MP, 50)
    worker = _per_partition_symbolic if args.symbolic else _per_partition_numeric
    work = [(lam, crossings, q_str_50, mp.mp.dps) for lam in parts]

    chi_at_q0 = {}
    if args.workers > 1 and len(parts) > 1:
        with Pool(args.workers) as pool:
            for lam, chi_str in pool.imap_unordered(worker, work):
                chi_at_q0[lam] = mp.mpf(chi_str)
    else:
        for w in work:
            lam, chi_str = worker(w)
            chi_at_q0[lam] = mp.mpf(chi_str)

    rows = []
    sw_sum = mp.mpf(0)
    for lam in parts:
        chi_q0 = chi_at_q0[lam]
        if lam not in y_lam_sym:
            raise RuntimeError(f"y_λ for partition {lam} missing from witness")
        y_q0 = evaluate_at_q0(y_lam_sym[lam])

        contribution = y_q0 * chi_q0
        sw_sum += contribution

        rows.append({
            "partition": list(lam),
            "y_lambda_at_q0": str(y_q0),
            "chi_lambda_beta_D_at_q0": str(chi_q0),
            "y_chi_product": str(contribution),
            "abs_y_chi": str(abs(contribution)),
        })

    # ── Step 4: Schur-Weyl identity sanity check ──────────────
    sw_err = abs(sw_sum - tr_M)
    sw_match = sw_err < mp.mpf("1e-40")
    print(f"\n  Schur-Weyl identity check:")
    print(f"    Σ_λ y_λ χ^λ(β_D)    = {mp.nstr(sw_sum, 30)}")
    print(f"    tr_M(β_D)           = {mp.nstr(tr_M, 30)}")
    print(f"    |residual|          = {mp.nstr(sw_err, 6)}  "
          f"{'✓ PASS' if sw_match else '✗ FAIL'}")
    if not sw_match:
        print("    WARNING: Schur-Weyl identity failed at 1e-40 tolerance.")
        print("    Δ_λ extraction below is meaningless without this identity.")

    # ── Step 5: dominant-partition heuristic ──────────────────
    # Δρ = (1/|tr_M|) · y_λ · χ^λ · Δ_λ   ⇒   Δ_λ = Δρ · |tr_M| / (y_λ χ^λ)
    target = delta_rho * abs_tr_M
    print(f"\n  Dominant-partition heuristic.  Δ_λ values for each λ ⊢ 6,")
    print(f"  assuming Δ_λ is supported on that partition alone:")
    print(f"    Δ_λ = Δρ · |tr_M| / (y_λ χ^λ)")
    print(f"\n    {'partition':<24}{'|y_λ χ^λ|':>20}{'Δ_λ':>22}")
    print("    " + "-" * 64)

    delta_table = []
    for r in rows:
        lam = tuple(r["partition"])
        y_chi = mp.mpf(r["y_chi_product"])
        if abs(y_chi) < mp.mpf("1e-40"):
            d_lam = mp.mpf("inf")
        else:
            d_lam = target / y_chi
        delta_table.append((lam, abs(y_chi), d_lam))
        r["Delta_lambda_solo_assumption"] = str(d_lam)
        r["abs_Delta_solo"] = str(abs(d_lam))
        print(f"    {str(list(lam)):<24}{mp.nstr(abs(y_chi), 8):>20}"
              f"{mp.nstr(d_lam, 8):>22}")

    # Find Occam's-razor minimum |Δ| (excluding inf / non-finite)
    finite = [(lam, _y, d) for (lam, _y, d) in delta_table
              if mp.isfinite(d)]
    occam = min(finite, key=lambda t: abs(t[2]))
    occam_lam, occam_y_chi, occam_delta = occam
    print(f"\n  Occam's-razor pick (minimum |Δ_λ| among singleton hypotheses):")
    print(f"    λ        = {list(occam_lam)}")
    print(f"    Δ_λ      = {mp.nstr(occam_delta, 16)}")
    print(f"    y_λ χ^λ  = {mp.nstr(occam_y_chi, 16)}")

    # Dominant heuristic: (3,2,1) is the "balanced" content-sum-zero pick
    DOMINANT = (3, 2, 1)
    dom_row = next((d for d in delta_table if d[0] == DOMINANT), None)
    if dom_row is not None:
        _, _y321, _d321 = dom_row
        print(f"\n  Heuristic-prior pick (balanced partition (3,2,1)):")
        print(f"    Δ_(3,2,1) = {mp.nstr(_d321, 16)}")
        print(f"    |Δ_(3,2,1)| = {mp.nstr(abs(_d321), 8)}")

    # ── Step 6: verify M(D) reconstructs CODATA exactly ───────
    # By construction (Step 5):  signed(y_λ χ^λ) · Δ_λ = target = Δρ · |tr_M|
    # so the contribution to ρ_K from the Occam pick is target / |tr_M| = Δρ
    # exactly.  Use `target` directly — `occam_y_chi` is unsigned (line 418
    # stores `abs(y_chi)`), and multiplying by `occam_delta` would flip sign
    # when the underlying y_λ χ^λ is negative (gemini-code-assist on PR #572).
    rho_K_check = rho_K_LO + target / abs_tr_M
    M_pred = rho_K_check * M_E_MEV * abs_tr_M
    closure_err_MeV = M_pred - M_D_MEV
    closure_err_ppm = closure_err_MeV / M_D_MEV * mp.mpf("1e6")
    print(f"\n  Closure verification (Occam Δ_λ inserted into ρ_K):")
    print(f"    ρ_K^refined       = {mp.nstr(rho_K_check, 25)}")
    print(f"    M(D)^pred         = {mp.nstr(M_pred, 16)} MeV")
    print(f"    M(D)^codata       = {mp.nstr(M_D_MEV, 16)} MeV")
    print(f"    closure error     = {mp.nstr(closure_err_MeV, 6)} MeV  "
          f"({mp.nstr(closure_err_ppm, 4)} ppm)")

    # ── Step 7: emit witness ──────────────────────────────────
    script_bytes = Path(__file__).read_bytes()
    script_hash = "sha256:" + hashlib.sha256(script_bytes).hexdigest()

    witness = {
        "computation": "rho-k-h3a-refinement",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Deuteron proof-of-concept for the H_{3A} Wedderburn "
            "refinement of ρ_K per prop:rho-k-h3a-refinement (PR #564). "
            "Computes y_λ(q_0) χ^λ(β_D) for all 11 partitions λ ⊢ 6, "
            "verifies the Schur-Weyl identity Σ_λ y_λ χ^λ = tr_M(β_D) "
            "to 50 dps, then extracts Δ_λ(D) under the singleton-support "
            "hypothesis (Δ supported on one partition).  Reports the "
            "Occam's-razor pick (smallest |Δ|) and the prior heuristic "
            "(balanced partition (3,2,1)).  Both reconstruct M(D) = "
            "1875.61294257 MeV exactly by construction (single equation, "
            "single unknown)."
        ),
        "engine": (
            f"mpmath numeric Hoefsmit at q_0 (50 dps), "
            f"multiprocessing.Pool({args.workers})"
            if not args.symbolic
            else "sympy symbolic-q + mpmath evaluation (50 dps), single-threaded"
        ),
        "scriptFile": "rho_k_h3a_refinement.py",
        "scriptHash": script_hash,
        "parameters": {
            "q_0_50dps": mp.nstr(Q_MP, 50),
            "atom": "deuteron",
            "Z": 1, "N": 1, "A": 2, "n_strands": 6,
            "braid_word_source": "mass_at_3A_proper.atom_braid_word_3A(1, 1)",
            "braid_word_str": (
                "β_p · I · β_n  (canonical: H_3 ⊗ H_3 ⊂ H_6 with "
                "interface I = σ_3 - h/2·1 at gen_idx=2)"
            ),
            "crossings_typed": [[g, t] for (g, t) in crossings],
            "n_crossings": len(crossings),
            "n_partitions": len(parts),
            "compute_status": "deuteron",
            "M_codata_MeV": str(M_D_MEV),
            "m_e_MeV": str(M_E_MEV),
            "m_p_MeV": str(M_P_MEV),
            "m_n_MeV": str(M_N_MEV),
        },
        "data": {
            "abs_tr_M_at_q0_50dps": str(abs_tr_M),
            "rho_K_LO": str(rho_K_LO),
            "rho_K_codata": str(rho_K_codata),
            "delta_rho_residual": str(delta_rho),
            "M_LO_pred_MeV": str(M_pred_LO),
            "M_LO_err_pct": str(err_pct_LO),
            "binding_gap_MeV": str(M_pred_LO - M_D_MEV),
            "schur_weyl_check": {
                "sum_y_chi": str(sw_sum),
                "tr_M": str(tr_M),
                "abs_residual": str(sw_err),
                "match_at_1e_40": bool(sw_match),
            },
            "per_lambda": rows,
            "occam_pick": {
                "partition": list(occam_lam),
                "Delta_lambda": str(occam_delta),
                "abs_Delta": str(abs(occam_delta)),
                "y_chi": str(occam_y_chi),
                "M_pred_MeV": str(M_pred),
                "closure_err_MeV": str(closure_err_MeV),
                "closure_err_ppm": str(closure_err_ppm),
            },
            "balanced_321_heuristic": {
                "partition": [3, 2, 1],
                "Delta_lambda": (str(dom_row[2]) if dom_row is not None else None),
                "abs_Delta": (str(abs(dom_row[2])) if dom_row is not None else None),
            },
        },
        "audit_reference": "AUDIT-DEEP-2026-05.md §7 P3 / P3'",
        "pr": "#564",
        "notes": (
            "The single mass equation  ρ_K^codata - ρ_K^LO = "
            "(1/|tr_M|) Σ_λ y_λ χ^λ Δ_λ  is **underdetermined**: 11 "
            "unknowns (Δ_λ for λ ⊢ 6), 1 constraint.  This proof-of-"
            "concept assumes singleton support for Δ_λ and reports "
            "(a) the Occam's-razor pick (minimum |Δ|), and (b) the "
            "balanced-partition heuristic (3,2,1).  Both reproduce "
            "M(D) exactly by construction.  The categorical question "
            "— *which* λ carries the binding, and why — is the open "
            "P3' problem.  Likely resolution paths: (i) Plancherel-"
            "truncation bound MAE(k) ≤ C₀·[2]_q^{-2(k-3)} via "
            "k_max = 12; (ii) jet-knot Hochschild-cohomology "
            "obstruction selecting a privileged Wedderburn block; "
            "(iii) variational principle minimising Σ_λ |Δ_λ|² "
            "subject to the mass constraint (Tikhonov / minimum-"
            "norm solution = Moore-Penrose pseudoinverse)."
        ),
        "follow_up": (
            "Extend to (T, ³He) at n=9 (p(9)=30) using the same "
            "pipeline; then to ⁴He at n=12 (p(12)=77).  Add a "
            "minimum-norm Δ_λ extraction (least-squares against "
            "all atoms simultaneously) once ≥ 2 atoms are wired."
        ),
    }
    out = HERE / "rho-k-h3a-refinement.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  Wrote {out.name} ({out.stat().st_size} bytes).")
    print("=" * 96)
    return 0 if sw_match else 2


if __name__ == "__main__":
    sys.exit(main())
