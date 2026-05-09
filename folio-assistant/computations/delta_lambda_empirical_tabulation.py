#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer; symbolic-q
# polynomials live upstream in chi-{atom}-h{n}.witness.json + y-lambda-
# wenzl-bridge-symbolic-witness.json.
"""Proposal 1 (workplan 2026-05-09-rho-k): empirical Δ_λ tabulation.

Per `prop:rho-k-h3a-refinement` the full ρ_K mass formula reads

    M(K) = m_e · Σ_{λ ⊢ 3A} y_λ(q) · χ^λ(β_K) · (1 + Δ_λ(K))

with per-Wedderburn-block binding fractions Δ_λ(K).  The leading-
order ansatz Δ_λ ≡ 0 reproduces the constituent mass ρ_K^LO
(Z · m_p + N · m_n) but misses the binding-energy correction
ΔM(K) = M_codata - (Z · m_p + N · m_n) by 0.1-0.8 % per atom.

This script solves the underdetermined system

    Σ_{λ ⊢ 3A} c_λ(K) · Δ_λ(K) = ΔM(K) / m_e          (★)

(where c_λ(K) := y_λ(q_0) · χ^λ(β_K)(q_0)) under four candidate
ansätze:

    (a) **single-block** — Δ_λ ≠ 0 only for one λ*; sweep all
        partitions of 3A and report which yields the smallest |Δ|.
    (b) **shell-supported** — Δ_λ ≠ 0 only for the staircase
        λ_shell ⊢ 3A (per `prop:sigma-shell-from-beta-chain-derivation`).
    (c) **Δ-monotonic via c(λ)** — Δ_λ = α · c(λ) (content sum,
        per the full-twist scalar action data from #548).
    (d) **Δ-isotypic via dim_q** — Δ_λ = α · dim_q(λ) / [n]_q!
        (the Plancherel weight, recycled as a Δ scaling).

For each ansatz, report:
  - which partition (or scaling factor) closes the system;
  - the resulting ‖Δ‖₂ (Occam's-razor minimal-perturbation choice);
  - whether the same `λ*` (for ansatz a) recurs across atoms — that
    would be evidence for a categorical rule.

Atoms covered: {D, T, ³He, ⁴He}.  Cached χ data is loaded from
`chi-{atom}-h{n}.witness.json`; y_λ(q_0) is evaluated from
`y-lambda-wenzl-bridge-symbolic-witness.json` once and reused.

Output: `delta-lambda-empirical-tabulation.witness.json`.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from math import factorial
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

mp.mp.dps = 50

from q_parameter import Q_MP  # noqa: E402

Q0 = mp.mpf(str(Q_MP))

# ── CODATA 2022 anchors (CAL-3, no derivation) ─────────────────
M_E_MEV = mp.mpf("0.51099895")
M_P_MEV = mp.mpf("938.27208816")
M_N_MEV = mp.mpf("939.56542052")

ATOMS_CODATA = {
    "D":   {"Z": 1, "N": 1, "n": 6,  "M_MeV": "1875.61294257",
            "chi_witness": "chi-deuteron-h6.witness.json"},
    "T":   {"Z": 1, "N": 2, "n": 9,  "M_MeV": "2808.92113298",
            "chi_witness": "chi-tritium-h9.witness.json"},
    "3He": {"Z": 2, "N": 1, "n": 9,  "M_MeV": "2808.39160743",
            "chi_witness": "chi-helium-3-h9.witness.json"},
    "4He": {"Z": 2, "N": 2, "n": 12, "M_MeV": "3727.379378",
            "chi_witness": "chi-helium-4-h12.witness.json"},
}


# ── Partition + content-sum + dim_q utilities ──────────────────
from schur_weyl_symbolic import partitions_of, hook_lengths  # noqa: E402


def content_sum(lam: tuple[int, ...]) -> int:
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def staircase_partition(n: int) -> tuple[int, ...]:
    """Return the staircase partition (k, k-1, ..., 1) summing closest
    to n, padded with the surplus added to the largest part if needed.

    For n = 6 → (3, 2, 1); n = 9 → (4, 3, 2); n = 12 → (5, 4, 3) all
    exact staircase fits.  For non-triangular n, prepend the leftover
    to the largest part.
    """
    # find k such that 1 + 2 + ... + k ≤ n
    k = 0
    cumulative = 0
    while cumulative + (k + 1) <= n:
        k += 1
        cumulative += k
    leftover = n - cumulative
    parts = list(range(k, 0, -1))
    if leftover:
        parts[0] += leftover
    return tuple(parts)


def dim_q_at_q0(lam: tuple[int, ...]) -> mp.mpf:
    """dim_q(λ) at q_0 via [n]_q! / Π[h(x)]_q (mpmath; preserves dps)."""
    n = sum(lam)
    if n == 0:
        return mp.mpf(1)
    denom = Q0 - 1 / Q0
    nfac_q = mp.mpf(1)
    for k in range(1, n + 1):
        nfac_q *= (Q0 ** k - 1 / Q0 ** k) / denom
    prod_h = mp.mpf(1)
    for h in hook_lengths(lam):
        prod_h *= (Q0 ** h - 1 / Q0 ** h) / denom
    return nfac_q / prod_h


def n_factorial_q_at_q0(n: int) -> mp.mpf:
    denom = Q0 - 1 / Q0
    val = mp.mpf(1)
    for k in range(1, n + 1):
        val *= (Q0 ** k - 1 / Q0 ** k) / denom
    return val


# ── Loaders ────────────────────────────────────────────────────
def load_chi_per_lambda(witness_file: str) -> list[dict]:
    """Return list of {partition, y_at_q0, chi_q_at_q0, contribution}.

    Different witnesses use slightly different shapes; this loader
    normalises them.  Some witnesses store symbolic χ only; others
    have a per_partition table at q_0.
    """
    path = HERE / witness_file
    if not path.exists():
        raise FileNotFoundError(f"missing chi witness: {path}")
    d = json.loads(path.read_text())
    # Shape A: 4He-style `per_partition` with numeric y_at_q0 + chi_q_at_q0.
    if "per_partition" in d:
        return d["per_partition"]
    # Shape B: deuteron / T / ³He chi_lambda_symbolic; needs y_at_q0
    # from y-lambda-wenzl-bridge-symbolic-witness.json + symbolic
    # chi evaluated at q_0.
    if "chi_lambda_symbolic" in d:
        # Need to evaluate symbolic χ at q_0 and pair with y_λ(q_0)
        return None  # signal caller to use load_chi_via_symbolic
    raise KeyError(f"unknown chi witness shape: {witness_file}")


def _sympy_to_mpf(expr: sp.Expr) -> mp.mpf:
    """Robust sympy → mpmath conversion via lambdify.

    The plain `.subs(q, value).evalf()` path silently fails when the
    sympified expression's `q` symbol has different assumptions
    (e.g. `positive=True` vs default) than the substitution target;
    evalf then returns the unevaluated symbolic expression.
    lambdify binds via signature matching and is also ~20× faster
    than evalf on large expressions."""
    free = list(expr.free_symbols)
    if not free:
        # Constant.
        try:
            return mp.mpf(str(complex(expr).real))
        except Exception:
            return mp.mpf(str(expr))
    # Take the first free symbol (assume single-variable in q).
    q_sym = free[0]
    func = sp.lambdify(q_sym, expr, modules=["mpmath"])
    val = func(mp.mpf(str(Q_MP)))
    if hasattr(val, "imag") and abs(val.imag) > mp.mpf("1e-30"):
        return mp.mpf(str(val.real))
    if hasattr(val, "real"):
        return mp.mpf(str(val.real))
    return mp.mpf(str(val))


def load_y_lambda_at_q0(n: int) -> dict[tuple, mp.mpf]:
    """Get y_λ(q_0) for every λ ⊢ n.  Loads from the pre-computed
    `y-lambda-at-q0.witness.json` cache when available; falls back
    to live symbolic evaluation otherwise.  Memoised per n."""
    cache_attr = f"_cache_n{n}"
    if hasattr(load_y_lambda_at_q0, cache_attr):
        return getattr(load_y_lambda_at_q0, cache_attr)

    # Try cached witness first (fast path).
    cache_path = HERE / "y-lambda-at-q0.witness.json"
    if cache_path.exists():
        try:
            cache_d = json.loads(cache_path.read_text())
            by_n = cache_d.get("data", cache_d).get("by_n", {})
            if str(n) in by_n:
                out: dict[tuple, mp.mpf] = {}
                for entry in by_n[str(n)]:
                    lam = tuple(entry["partition"])
                    out[lam] = mp.mpf(entry["y_at_q0_50dps"])
                setattr(load_y_lambda_at_q0, cache_attr, out)
                return out
        except (json.JSONDecodeError, KeyError):
            pass  # fall through to live evaluation

    # Slow path: live symbolic evaluation.
    path = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"
    d = json.loads(path.read_text())
    tab = d["tables_by_n"][str(n)]
    weights = tab["weights"]
    out = {}
    for entry in weights:
        lam = tuple(entry["partition"])
        y_sym = sp.sympify(entry["y_lambda_symbolic"])
        # _sympy_to_mpf binds via lambdify on the expression's own
        # free symbol — no need to pre-substitute with a possibly-
        # mismatched local q symbol.
        out[lam] = _sympy_to_mpf(y_sym)
    setattr(load_y_lambda_at_q0, cache_attr, out)
    return out


_CHI_CACHE: dict | None = None


def _load_chi_cache() -> dict[str, list[dict]]:
    """Load chi-lambda-at-q0.witness.json once if it exists."""
    global _CHI_CACHE
    if _CHI_CACHE is not None:
        return _CHI_CACHE
    cache_path = HERE / "chi-lambda-at-q0.witness.json"
    if not cache_path.exists():
        _CHI_CACHE = {}
        return _CHI_CACHE
    try:
        d = json.loads(cache_path.read_text())
        by_atom = d.get("data", d).get("by_atom", {})
        # by_atom: {atom_name: [{partition, chi_q_at_q0_50dps}, ...]}
        # Convert to {atom_name: {tuple(partition): mp.mpf}}
        out: dict[str, dict[tuple, mp.mpf]] = {}
        for atom, entries in by_atom.items():
            out[atom] = {tuple(e["partition"]): mp.mpf(e["chi_q_at_q0_50dps"])
                         for e in entries}
        _CHI_CACHE = out
        return _CHI_CACHE
    except (json.JSONDecodeError, KeyError):
        _CHI_CACHE = {}
        return _CHI_CACHE


# Map chi witness filenames to cached atom keys.
_WITNESS_TO_ATOM_CACHE_KEY = {
    "chi-deuteron-h6.witness.json": "deuteron",
    "chi-tritium-h9.witness.json": "tritium",
    "chi-helium-3-h9.witness.json": "helium-3",
}


def load_chi_via_symbolic(witness_file: str, n: int) -> list[dict]:
    """Load symbolic χ from witness, evaluate at q_0, pair with y_λ(q_0).

    Fast path: load numeric χ from `chi-lambda-at-q0.witness.json` if
    present.  Slow path: live symbolic evaluation."""
    chi_cache = _load_chi_cache()
    atom_key = _WITNESS_TO_ATOM_CACHE_KEY.get(witness_file)
    cached_chi = chi_cache.get(atom_key) if atom_key else None

    path = HERE / witness_file
    d = json.loads(path.read_text())
    chi_sym_table = d["chi_lambda_symbolic"]
    y_at_q0 = load_y_lambda_at_q0(n)
    out: list[dict] = []
    for entry in chi_sym_table:
        lam = tuple(entry["partition"])
        if cached_chi is not None and lam in cached_chi:
            chi_val = cached_chi[lam]  # fast path
        else:
            chi_sym = sp.sympify(entry["chi_q_symbolic"])
            chi_val = _sympy_to_mpf(chi_sym)
        y_val = y_at_q0.get(lam, mp.mpf(0))
        out.append({
            "partition": list(lam),
            "y_at_q0": str(y_val),
            "chi_q_at_q0": str(chi_val),
            "contribution": str(y_val * chi_val),
        })
    return out


# ── Direct numerical path via wedderburn_jones_markov ──────────
# (Preferred: gives ALL partitions for any (Z, N) in seconds via
# numerical-q-from-start, no symbolic intermediate.  Per PR #572
# audit, agrees with the recursive reducer to 1e-13 (A=1) — 1e-10
# (A=2) at float64.  For higher precision, the rho_k_h3a_refinement
# 50-dps mpmath path agrees at 1.4e-16.)
def load_chi_via_numerical_path(Z: int, N: int) -> tuple[list[dict], mp.mpf]:
    """Returns (per_partition_rows, abs_tr_M_total) computed at q_0
    via global_wedderburn_sum_q_hecke_seminormal.  All partitions of
    n = 3A included (no partial cache concerns)."""
    from wedderburn_jones_markov import global_wedderburn_sum_q_hecke_seminormal
    q0_float = float(Q_MP)
    tr_M_total, terms = global_wedderburn_sum_q_hecke_seminormal(
        Z=Z, N=N, q_val=q0_float
    )
    rows = []
    for term in terms:
        rows.append({
            "partition": term["partition"],
            "y_at_q0": str(term["y_at_q0"]),
            "chi_q_at_q0": str(term["chi_q_at_q0"]),
            "contribution": str(term["y_at_q0"] * term["chi_q_at_q0"]),
        })
    return rows, mp.mpf(abs(tr_M_total))


# ── Per-atom data assembly ─────────────────────────────────────
def assemble_per_atom(atom_label: str, info: dict) -> dict:
    Z = info["Z"]; N = info["N"]; n = info["n"]
    # Tier 1: per-atom witness with full numeric per_partition (e.g.
    # 4He's chi-helium-4-h12.witness.json).  Instant.
    chi_data = load_chi_per_lambda(info["chi_witness"])
    if chi_data is not None:
        # `chi_data` from load_chi_per_lambda has per-partition numeric
        # y/chi already; check it covers ALL partitions of n.
        from schur_weyl_symbolic import partitions_of
        all_parts = {tuple(p) for p in partitions_of(n)}
        cached_parts = {tuple(e["partition"]) for e in chi_data}
        if all_parts.issubset(cached_parts):
            print(f"      [tier 1: per-atom numeric witness covers all "
                  f"{len(all_parts)} partitions]")
        else:
            chi_data = None  # fall through

    if chi_data is None:
        # Tier 2: numerical-q-from-start path (PR #572).  Fast for
        # n ≤ 9; slow for n = 12 (~20 min).
        try:
            print(f"      [tier 2: wedderburn_jones_markov numerical path]")
            chi_data, _ = load_chi_via_numerical_path(Z, N)
        except Exception as exc:
            # Tier 3: symbolic-witness path (legacy / 50-dps).
            print(f"      [tier 2 failed: {type(exc).__name__}: {exc}; "
                  f"tier 3 = symbolic witness path]")
            chi_data = load_chi_via_symbolic(info["chi_witness"], info["n"])
    M_codata = mp.mpf(info["M_MeV"])
    constituent = Z * M_P_MEV + N * M_N_MEV  # = ρ_K^LO · m_e · |tr_M|
    delta_M = M_codata - constituent           # binding-energy + np-mass shift
    target = delta_M / M_E_MEV                 # RHS of (★) before sign

    # Per-λ products c_λ = y_λ · χ^λ; tr_M = Σ c_λ
    rows = []
    tr_M = mp.mpf(0)
    for entry in chi_data:
        lam = tuple(entry["partition"])
        y_l = mp.mpf(entry["y_at_q0"])
        chi_l = mp.mpf(entry["chi_q_at_q0"])
        c_l = y_l * chi_l
        rows.append({"lambda": lam, "y": y_l, "chi": chi_l, "c": c_l})
        tr_M += c_l

    # Sign of tr_M (the per-block formula uses the SIGNED tr_M).
    # ρ_K · m_e · |tr_M| = M ⇒ tr_M of opposite sign would flip.
    sign = mp.mpf(1) if tr_M > 0 else mp.mpf(-1)
    abs_tr_M = abs(tr_M)
    target_signed = sign * target  # so that Σ c_λ Δ_λ = target_signed

    return {
        "atom": atom_label, "Z": Z, "N": N, "A": Z + N, "n": n,
        "n_partitions": len(rows),
        "M_codata_MeV": M_codata,
        "constituent_MeV": constituent,
        "delta_M_MeV": delta_M,
        "tr_M": tr_M,
        "abs_tr_M": abs_tr_M,
        "target_signed": target_signed,
        "rows": rows,
    }


# ── Ansatz solvers ─────────────────────────────────────────────
def ansatz_a_single_block(atom_data: dict) -> dict:
    """Sweep all λ; for each, solve δ * c_{λ*} = target_signed.
    Report the λ* with smallest |δ| ('minimal perturbation')."""
    target = atom_data["target_signed"]
    candidates = []
    for r in atom_data["rows"]:
        if abs(r["c"]) < mp.mpf("1e-30"):
            continue  # singular
        delta = target / r["c"]
        candidates.append({
            "lambda": list(r["lambda"]),
            "delta": delta,
            "abs_delta": abs(delta),
            "y": r["y"], "chi": r["chi"], "c": r["c"],
        })
    candidates.sort(key=lambda x: float(x["abs_delta"]))
    return {
        "ansatz": "a_single_block",
        "best_lambda": candidates[0]["lambda"] if candidates else None,
        "best_delta": str(candidates[0]["delta"]) if candidates else None,
        "best_abs_delta": str(candidates[0]["abs_delta"]) if candidates else None,
        "candidates_top5": [
            {"lambda": c["lambda"],
             "delta": str(c["delta"]),
             "abs_delta": str(c["abs_delta"])}
            for c in candidates[:5]
        ],
        "n_candidates_skipped_singular": len(atom_data["rows"]) - len(candidates),
    }


def ansatz_b_shell(atom_data: dict) -> dict:
    """Δ_λ = δ · 1_{λ=staircase(n)}.  Single fixed partition."""
    n = atom_data["n"]
    lam_shell = staircase_partition(n)
    target = atom_data["target_signed"]
    c_shell = None
    for r in atom_data["rows"]:
        if tuple(r["lambda"]) == lam_shell:
            c_shell = r["c"]
            break
    if c_shell is None:
        return {"ansatz": "b_shell_supported", "lambda_shell": list(lam_shell),
                "error": "staircase partition not in chi witness"}
    if abs(c_shell) < mp.mpf("1e-30"):
        return {"ansatz": "b_shell_supported", "lambda_shell": list(lam_shell),
                "error": f"c_shell ≈ 0 ({c_shell}); cannot solve"}
    delta = target / c_shell
    return {
        "ansatz": "b_shell_supported",
        "lambda_shell": list(lam_shell),
        "c_shell": str(c_shell),
        "delta": str(delta),
        "abs_delta": str(abs(delta)),
    }


def ansatz_c_content_monotonic(atom_data: dict) -> dict:
    """Δ_λ = α · c(λ).  Single linear scaling: Σ c_λ · α · c(λ) = target."""
    target = atom_data["target_signed"]
    weighted_sum = mp.mpf(0)
    detail = []
    for r in atom_data["rows"]:
        cs = content_sum(tuple(r["lambda"]))
        weighted_sum += r["c"] * cs
        detail.append({"lambda": list(r["lambda"]),
                       "content_sum": cs, "c": r["c"]})
    if abs(weighted_sum) < mp.mpf("1e-30"):
        return {"ansatz": "c_content_monotonic", "error":
                f"Σ c_λ · c(λ) ≈ 0 ({weighted_sum}); ansatz infeasible"}
    alpha = target / weighted_sum
    # ‖Δ‖₂ = |α| · sqrt(Σ c(λ)²)
    norm_c2 = mp.sqrt(sum(content_sum(tuple(r["lambda"])) ** 2 for r in atom_data["rows"]))
    return {
        "ansatz": "c_content_monotonic",
        "alpha": str(alpha),
        "weighted_sum_yChi_cContent": str(weighted_sum),
        "norm_delta_2": str(abs(alpha) * norm_c2),
    }


def ansatz_d_isotypic(atom_data: dict) -> dict:
    """Δ_λ = α · dim_q(λ) / [n]_q!  (Plancherel-style scaling)."""
    target = atom_data["target_signed"]
    n = atom_data["n"]
    nfac_q = n_factorial_q_at_q0(n)
    weighted_sum = mp.mpf(0)
    norm_d2 = mp.mpf(0)
    for r in atom_data["rows"]:
        d_q = dim_q_at_q0(tuple(r["lambda"]))
        scaling = d_q / nfac_q
        weighted_sum += r["c"] * scaling
        norm_d2 += scaling ** 2
    if abs(weighted_sum) < mp.mpf("1e-30"):
        return {"ansatz": "d_isotypic", "error":
                f"Σ c_λ · dim_q/[n]_q! ≈ 0 ({weighted_sum})"}
    alpha = target / weighted_sum
    return {
        "ansatz": "d_isotypic",
        "alpha": str(alpha),
        "weighted_sum_yChi_planch": str(weighted_sum),
        "norm_delta_2": str(abs(alpha) * mp.sqrt(norm_d2)),
    }


# ── Cross-atom pattern check ───────────────────────────────────
def find_recurring_lambda_star(per_atom_results: dict[str, dict]) -> dict:
    """For ansatz (a), check if the same λ* appears in the top-3
    minimal-|Δ| candidates across atoms (evidence for a categorical
    pattern)."""
    top3_by_atom = {
        atom: [tuple(c["lambda"]) for c in r["a_single_block"]["candidates_top5"][:3]]
        for atom, r in per_atom_results.items()
        if "a_single_block" in r
    }
    # Frequency table: how often does each λ appear in any atom's top-3?
    freq: dict[tuple, int] = {}
    for top3 in top3_by_atom.values():
        for lam in top3:
            freq[lam] = freq.get(lam, 0) + 1
    most_common = sorted(freq.items(), key=lambda kv: -kv[1])
    return {
        "top3_by_atom": {a: [list(l) for l in t] for a, t in top3_by_atom.items()},
        "lambda_frequency_in_top3": [
            {"lambda": list(lam), "n_atoms_in_top3": n}
            for lam, n in most_common[:10]
        ],
        "max_recurrence": most_common[0][1] if most_common else 0,
    }


def main() -> int:
    print("=" * 96)
    print("  Empirical Δ_λ tabulation across atoms (Proposal 1)")
    print("=" * 96)
    print(f"\n  q_0 = {Q0}")
    print(f"  m_e = {M_E_MEV}, m_p = {M_P_MEV}, m_n = {M_N_MEV}")

    per_atom: dict[str, dict] = {}
    for atom, info in ATOMS_CODATA.items():
        print(f"\n  ── {atom} (Z={info['Z']}, N={info['N']}, n={info['n']}) ──")
        try:
            data = assemble_per_atom(atom, info)
        except Exception as exc:
            print(f"    ERROR loading χ: {type(exc).__name__}: {exc}")
            continue
        print(f"    n_partitions = {data['n_partitions']}")
        print(f"    M_codata     = {mp.nstr(data['M_codata_MeV'], 14)} MeV")
        print(f"    constituent  = {mp.nstr(data['constituent_MeV'], 14)} MeV "
              f"(= ρ_K^LO · m_e · |tr_M|)")
        print(f"    ΔM           = {mp.nstr(data['delta_M_MeV'], 14)} MeV "
              f"(binding-energy correction)")
        print(f"    tr_M         = {mp.nstr(data['tr_M'], 14)} (signed)")
        print(f"    target_signed = {mp.nstr(data['target_signed'], 14)} "
              f"= sign(tr_M) · ΔM/m_e")

        # Run all four ansätze
        a_result = ansatz_a_single_block(data)
        b_result = ansatz_b_shell(data)
        c_result = ansatz_c_content_monotonic(data)
        d_result = ansatz_d_isotypic(data)

        print(f"\n    ansatz (a) single-block — best λ*: {a_result['best_lambda']}")
        print(f"      |δ_min| = {a_result['best_abs_delta'][:18]}")
        print(f"      top-3 by |δ|:")
        for c in a_result["candidates_top5"][:3]:
            print(f"        λ = {str(c['lambda']):<20} |δ| = {c['abs_delta'][:14]}")

        print(f"\n    ansatz (b) shell-supported — λ_shell = {b_result.get('lambda_shell')}")
        if "error" in b_result:
            print(f"      → ERROR: {b_result['error']}")
        else:
            print(f"      δ = {b_result['delta'][:18]}")

        print(f"\n    ansatz (c) Δ-monotonic via c(λ):")
        if "error" in c_result:
            print(f"      → ERROR: {c_result['error']}")
        else:
            print(f"      α = {c_result['alpha'][:20]}, ‖Δ‖₂ = {c_result['norm_delta_2'][:18]}")

        print(f"\n    ansatz (d) Δ-isotypic via dim_q:")
        if "error" in d_result:
            print(f"      → ERROR: {d_result['error']}")
        else:
            print(f"      α = {d_result['alpha'][:20]}, ‖Δ‖₂ = {d_result['norm_delta_2'][:18]}")

        per_atom[atom] = {
            "Z": data["Z"], "N": data["N"], "n": data["n"],
            "n_partitions": data["n_partitions"],
            "M_codata_MeV": str(data["M_codata_MeV"]),
            "constituent_MeV": str(data["constituent_MeV"]),
            "delta_M_MeV": str(data["delta_M_MeV"]),
            "tr_M": str(data["tr_M"]),
            "abs_tr_M": str(data["abs_tr_M"]),
            "target_signed": str(data["target_signed"]),
            "a_single_block": a_result,
            "b_shell_supported": b_result,
            "c_content_monotonic": c_result,
            "d_isotypic": d_result,
        }

    # Cross-atom pattern check (ansatz a)
    pattern = find_recurring_lambda_star(per_atom)
    print(f"\n  ── Cross-atom pattern check (ansatz a) ──")
    print(f"    top-3 minimal-|δ| λ per atom:")
    for atom, t3 in pattern["top3_by_atom"].items():
        print(f"      {atom}: {t3}")
    print(f"\n    λ frequency in top-3 (across atoms):")
    for entry in pattern["lambda_frequency_in_top3"]:
        if entry["n_atoms_in_top3"] >= 2:
            print(f"      λ = {str(entry['lambda']):<20} appears in {entry['n_atoms_in_top3']} atoms")
    print(f"\n    max recurrence: {pattern['max_recurrence']} / {len(per_atom)} atoms")
    if pattern["max_recurrence"] >= 3:
        print(f"    ✅ Strong pattern: a single λ* dominates across ≥3 atoms.")
    elif pattern["max_recurrence"] == 2:
        print(f"    ✓ Weak pattern: a λ* recurs in 2 atoms.")
    else:
        print(f"    ✗ No cross-atom pattern in single-block ansatz.")

    # Emit witness via WitnessBuilder
    from witness_base import WitnessBuilder
    w = (WitnessBuilder("delta-lambda-empirical-tabulation", engine="mpmath")
         .set_description(
            "Empirical tabulation of per-Wedderburn-block binding "
            "fractions Δ_λ(K) for K ∈ {D, T, ³He, ⁴He} per the full "
            "ρ_K mass formula M(K) = m_e · Σ_λ y_λ · χ^λ · (1 + Δ_λ). "
            "Solves the underdetermined Σ c_λ Δ_λ = ΔM/m_e under four "
            "ansätze: (a) single-block sweep over all λ ⊢ 3A, "
            "(b) shell-supported λ_shell = staircase, (c) Δ-monotonic "
            "via content sum c(λ), (d) Δ-isotypic via dim_q(λ)/[n]_q!. "
            "Reports best λ* per ansatz, ‖Δ‖₂, and cross-atom "
            "recurrence pattern. Proposal 1 of "
            "docs/audits/2026-05-09-workplan-update-rho-k.md."
         )
         .set_content_block("prop:rho-k-h3a-refinement"))
    w.parameters.update({
        "q_0": str(Q0),
        "m_e_MeV": str(M_E_MEV),
        "m_p_MeV": str(M_P_MEV),
        "m_n_MeV": str(M_N_MEV),
    })
    w.add_data("per_atom", per_atom)
    w.add_data("cross_atom_pattern_ansatz_a", pattern)
    w.add_data("reference_blocks", [
        "prop:rho-k-h3a-refinement",
        "prop:sigma-shell-from-beta-chain-derivation",
        "prop:categorical-mass-markov",
        "conj:categorical-neutrality-saturated-shells",
    ])
    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
