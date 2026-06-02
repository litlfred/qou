#!/usr/bin/env python3
"""
Wenzl-bridge closed-form y_λ for the generic Markov trace.

Verified result (independently confirmed against my MPFR witness at
n = 2, 3, 4 to ~10⁻¹¹):

    y_λ(q, z) = s_{λ, X}(Q) / Σ_μ d_μ s_{μ, X}(Q),
    Q = q²,
    X = q · z / (1 - Q + q · z),
    s_{λ, X}(Q) := Q^{n(λ)} · ∏_{x ∈ λ} (1 - X · Q^{c(x)}) / (1 - Q^{h(x)}),

where d_μ is the classical Hecke irrep dimension (number of SYT of
shape μ).  This is a "fractional Wenzl" specialisation: the principal
Schur evaluation $s_λ(1, Q, Q², …, Q^{r-1}) = Q^{n(λ)} ∏ (1-Q^{r+c})/
(1-Q^h)$ extends analytically to non-integer $r$ via $X = Q^r$, and
the Markov-trace constraint determines $X$ algebraically.

Key features beyond the linear-system pipeline:
- O(n) work per partition (vs O(p(n)² · max d_λ³) for linear-solve)
- Arbitrary precision via mpmath at any dps
- Symbolic q via sympy (no Hoefsmit-matrix bottleneck)
- 270 closed forms for n=2..12 in seconds, NOT minutes

Earlier session claim "no closed-form exists for our generic z" was
WRONG — it confused integer-N Wenzl SU_q(N) (which our z is not)
with the analytic continuation in X (which IS valid).

References:
- Macdonald, "Symmetric Functions and Hall Polynomials", I.3 ex.1
  (principal specialisation of Schur functions)
- Wenzl 1988, "Hecke algebras of type A_n and subfactors", Invent.
  Math. 92 (Markov trace via SU_q(N))
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import functools
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT
from partition_utils import hook_lengths_with_cells as hook_lengths  # noqa: E402


def n_lambda(partition):
    """N(λ) = Σ i · λ_{i+1} (0-indexed)."""
    return sum(i * partition[i] for i in range(len(partition)))


def classical_dim(partition):
    """f_λ = n! / ∏ h(x) — number of standard Young tableaux."""
    n = sum(partition)
    cells = hook_lengths(partition)
    nfact = 1
    for k in range(2, n + 1):
        nfact *= k
    hprod = 1
    for (_, _, h) in cells:
        hprod *= h
    return nfact // hprod


def partitions_of(n):
    """All partitions of n in descending-parts list form."""
    if n == 0:
        return [[]]
    result = []

    def rec(remaining, max_part, prefix):
        if remaining == 0:
            result.append(list(prefix))
            return
        for k in range(min(remaining, max_part), 0, -1):
            rec(remaining - k, k, prefix + [k])

    rec(n, n, [])
    return result


def schur_principal(partition, X, Q):
    """s_{λ, X}(Q) = Q^{n(λ)} · ∏_x (1 - X · Q^{c(x)}) / (1 - Q^{h(x)})."""
    cells = hook_lengths(partition)
    prod = Q ** n_lambda(partition)
    for (i, j, h) in cells:
        c = j - i
        prod *= (1 - X * Q ** c) / (1 - Q ** h)
    return prod


def y_lambda_wenzl_bridge_numeric(partition, q_val, dps: int = 50):
    """y_λ via Wenzl-bridge at numerical q, arbitrary dps.

    The Wenzl normalization Σ_µ d_µ · s_{µ,r}(Q) is cached per
    (n, q_val_str, dps) so callers iterating over all partitions of
    n at a fixed q_val (e.g. `markov_trace_numerical`) avoid the
    O(p(n)²) recomputation; this drops `markov_trace_numerical(D, q_0)`
    from O(11²)=121 schur_principal calls to O(11)=11 calls.
    """
    return _y_lambda_wenzl_bridge_numeric_impl(
        tuple(partition), str(q_val), int(dps)
    )


@functools.lru_cache(maxsize=None)
def _wenzl_norm_numeric_cached(n: int, q_str: str, dps: int):
    """Cached Wenzl normalization Σ_µ d_µ · s_{µ,r}(Q) at numerical q."""
    mp.mp.dps = dps
    q = mp.mpf(q_str)
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    Q = q ** 2
    X = q * z / (1 - Q + q * z)
    parts = partitions_of(n)
    return sum(classical_dim(mu) * schur_principal(mu, X, Q) for mu in parts)


@functools.lru_cache(maxsize=None)
def _y_lambda_wenzl_bridge_numeric_impl(partition: tuple, q_str: str, dps: int):
    """Per-partition y_λ at numerical q, cached by (partition, q, dps).

    Per compute-pipeline-audit §Optimization #2: y_λ depends only on
    the partition shape and q — it is the SAME for every atom at the
    same H_n level. Caching avoids recomputing schur_principal + the
    norm division for each atom.
    """
    mp.mp.dps = dps
    q = mp.mpf(q_str)
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    Q = q ** 2
    X = q * z / (1 - Q + q * z)
    s_self = schur_principal(list(partition), X, Q)
    norm = _wenzl_norm_numeric_cached(sum(partition), q_str, dps)
    return s_self / norm


def y_lambda_wenzl_bridge_symbolic(partition):
    """y_λ via Wenzl-bridge with q kept symbolic in sympy.

    Returns a sympy expression in the symbol q (positive).

    Optimizations:

    - Pre-populates the cache at module import from
      `y-lambda-wenzl-bridge-symbolic-witness.json` (32 partitions
      across n = 2..12 in sub-second).  Eliminates the first-call
      symbolic compute cost (6.1s for n=3 partition (3); >60s for
      n=6 partitions).  Cache miss falls back to recompute.
    - `@lru_cache` per-partition result for repeat calls.
    - The Wenzl normalization `Σ_µ d_µ · s_{µ,r}(Q)` is cached per
      `n` (instead of recomputed for every partition λ of size n).
    - The trailing `sp.simplify` is dropped — `sp.cancel` alone is
      sufficient and `simplify` on a rational expression with
      sqrt(q) terms dominates runtime (>30x slower per audit
      `docs/audits/2026-05-08-p3-h-3a-divergence.md`).
    """
    return _y_lambda_wenzl_bridge_symbolic_cached(tuple(partition))


@functools.lru_cache(maxsize=None)
def _y_lambda_wenzl_bridge_symbolic_cached(partition: tuple) -> "sp.Expr":
    """Cached symbolic y_λ; partition keyed as tuple for hashability.

    Lazy lookup: on first call per partition, checks the committed
    `y-lambda-wenzl-bridge-symbolic-witness.json` for a pre-computed
    symbolic string and `sp.sympify` parses it (avoiding the expensive
    Schur-principal recomputation).  Falls back to symbolic recompute
    if the witness has no entry.  Witness covers n = 2..12.
    """
    witness_strings = _load_witness_strings()
    if partition in witness_strings:
        q_pos = sp.Symbol("q", positive=True)
        try:
            return sp.sympify(witness_strings[partition], locals={"q": q_pos})
        except (sp.SympifyError, SyntaxError, ValueError):
            pass
    return sp.cancel(
        _schur_self_unnormalized(partition) / _wenzl_norm_for_n(sum(partition))
    )


# Lazy witness map: partition tuple → raw sympy-string (parsed on first
# request, NOT at import — sympifying all 32 cached y_λ at import would
# itself take 30+ seconds, defeating the optimization).
_WITNESS_STRINGS: dict[tuple, str] | None = None


def _load_witness_strings() -> dict[tuple, str]:
    """Load (and memoize) the partition → sympy-string map from the
    committed `y-lambda-wenzl-bridge-symbolic-witness.json`.  Lazy: only
    runs on first cache miss in `_y_lambda_wenzl_bridge_symbolic_cached`.
    """
    global _WITNESS_STRINGS
    if _WITNESS_STRINGS is not None:
        return _WITNESS_STRINGS
    out: dict[tuple, str] = {}
    witness_path = (
        Path(__file__).parent / "y-lambda-wenzl-bridge-symbolic-witness.json"
    )
    if witness_path.exists():
        try:
            with witness_path.open() as f:
                doc = json.load(f)
            tables = doc.get("tables_by_n") or doc.get("data", {}).get(
                "tables_by_n", {}
            )
            for _n_key, n_data in (tables or {}).items():
                weights = n_data.get("weights") if isinstance(n_data, dict) else None
                if not isinstance(weights, list):
                    continue
                for w in weights:
                    try:
                        lam = tuple(w["partition"])
                        out[lam] = w["y_lambda_symbolic"]
                    except (KeyError, TypeError):
                        continue
        except Exception:
            pass
    _WITNESS_STRINGS = out
    return out


@functools.lru_cache(maxsize=None)
def _wenzl_norm_for_n(n: int) -> "sp.Expr":
    """Wenzl normalization Σ_µ d_µ · s_{µ,r}(Q) for n, cached per n."""
    parts = partitions_of(n)
    return sum(
        classical_dim(mu) * _schur_self_unnormalized(tuple(mu))
        for mu in parts
    )


@functools.lru_cache(maxsize=None)
def _schur_self_unnormalized(partition: tuple) -> "sp.Expr":
    """schur_principal(partition, X, Q) with X, Q as the canonical Wenzl
    substitutions in q.  Cached per partition shape."""
    q = sp.Symbol("q", positive=True)
    z = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
    Q = q ** 2
    X = q * z / (1 - Q + q * z)
    return schur_principal(list(partition), X, Q)


# ════════════════════════════════════════════════════════════════════
#  Numeric Hecke characters (mpmath) — used by the validation suite
# ════════════════════════════════════════════════════════════════════

def _young_diagram_cells(shape):
    """List of (row, col) cells of a Young diagram in row-major order."""
    return [(r, c) for r, row in enumerate(shape) for c in range(row)]


def _standard_young_tableaux(shape):
    """All SYT of given shape; returns (syts, cells, contents) where
    each SYT is a dict {entry: cell_index}."""
    n = sum(shape)
    cells = _young_diagram_cells(shape)
    contents = [c - r for r, c in cells]
    nc = len(cells)
    results = []

    def _fill(entry, filled, cell_available):
        if entry > n:
            results.append(dict(filled))
            return
        for ci in range(nc):
            if not cell_available[ci]:
                continue
            r, c = cells[ci]
            if c > 0:
                # if the left neighbour is still available, skip — SYTs
                # require left-to-right increase along each row
                left_avail = any(
                    rr == r and cc == c - 1 and cell_available[k]
                    for k, (rr, cc) in enumerate(cells)
                )
                if left_avail:
                    continue
            if r > 0:
                above_avail = any(
                    rr == r - 1 and cc == c and cell_available[k]
                    for k, (rr, cc) in enumerate(cells)
                )
                if above_avail:
                    continue
            filled[entry] = ci
            cell_available[ci] = False
            _fill(entry + 1, filled, cell_available)
            del filled[entry]
            cell_available[ci] = True

    _fill(1, {}, [True] * nc)
    return results, cells, contents


def _seminormal_block_data(shape, q):
    """Sparse per-generator data for the seminormal representation.

    For each generator σ_k (k = 1 … n-1) returns a list of "block"
    descriptors:

      ('diag', i, a)              — basis vector i picks up coefficient a
      ('mix',  i, j, a, ap, b)    — basis vectors i, j mix as the 2×2
                                    block [[a, b], [b, a']]

    Together these cover every basis index exactly once per generator.
    Multiplying by σ_k acts independently on each block, so a vector
    with k nonzeros expands to at most 2k nonzeros.  This is the same
    information as the Hoefsmit matrix but stored as O(dim) entries
    instead of dim² entries — essential for n ≥ 10 where dim can
    reach several thousand.
    """
    n = sum(shape)
    syts, cells, contents = _standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0, syts
    # Precompute a stable signature → index lookup so the swap-partner
    # search below is O(1) per (i, k) instead of O(dim).  Per Copilot
    # review on PR #467: the O(dim²) inner scan dominates for n ≥ 10.
    sig_to_idx = {
        tuple(sorted(syts[i].items())): i for i in range(dim)
    }
    h = q - 1 / q
    blocks_per_gen = []
    for k in range(1, n):
        blocks = []
        processed = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = h / (1 - q ** (-2 * rho))
            swap_map = dict(syts[i])
            swap_map[k] = ci_k1
            swap_map[k + 1] = ci_k
            j_lookup = sig_to_idx.get(tuple(sorted(swap_map.items())))
            j = j_lookup if (j_lookup is not None and j_lookup != i) else None
            if j is None:
                blocks.append(("diag", i, a))
                processed.add(i)
            else:
                a_prime = h / (1 - q ** (2 * rho))
                b_sq = a * a_prime + 1
                b = mp.sqrt(b_sq)
                blocks.append(("mix", i, j, a, a_prime, b))
                processed.add(i)
                processed.add(j)
        blocks_per_gen.append(blocks)
    return blocks_per_gen, dim, syts


def _apply_generator_sparse(vec: dict, blocks):
    """Apply σ_k (described by `blocks`) to a sparse vector represented
    as a dict {index: mpmath value}.  Returns the new sparse vector
    (the input is not mutated).
    """
    new = {}
    for block in blocks:
        if block[0] == "diag":
            _, i, a = block
            v = vec.get(i)
            if v is not None:
                new[i] = a * v
        else:
            _, i, j, a, ap, b = block
            vi = vec.get(i, 0)
            vj = vec.get(j, 0)
            if vi == 0 and vj == 0:
                continue
            # Action on column basis: σ_k e_i = a e_i + b e_j,
            #                        σ_k e_j = b e_i + a' e_j.
            # As linear map on a column vector v:
            # new[i] = a * vi + b * vj,  new[j] = b * vi + a' * vj.
            ni = a * vi + b * vj
            nj = b * vi + ap * vj
            if ni != 0:
                new[i] = ni
            if nj != 0:
                new[j] = nj
    return new


def chi_lambda_mpmath(partition, word, q_val, dps: int = 50):
    """χ_λ(σ_{i_1} … σ_{i_k}) at mpmath precision (dps decimal places).

    Computes tr(ρ_λ(σ_{i_1} … σ_{i_k})) via sparse seminormal action:
    for each basis index i, propagate e_i through the word using
    block-sparse matvecs and accumulate the i-th diagonal component.
    Cost is O(dim · 2^len(word)) mpmath ops, which is tractable up to
    n = 12 for the extreme cycle classes (word length ≤ n-1).
    """
    mp.mp.dps = dps
    q = mp.mpf(str(q_val))
    blocks_per_gen, dim, _ = _seminormal_block_data(partition, q)
    if dim == 0:
        return mp.mpf(0)
    # Empty word → identity → trace = dim.  Return as mpf for type
    # consistency with the non-empty case.
    if len(word) == 0:
        return mp.mpf(dim)
    trace = mp.mpf(0)
    for i in range(dim):
        vec = {i: mp.mpf(1)}
        for idx in word:
            vec = _apply_generator_sparse(vec, blocks_per_gen[idx - 1])
            if not vec:
                break
        trace += vec.get(i, mp.mpf(0))
    return trace


def cycle_type_word(mu):
    """Reduced word realising cycle type μ on n = sum(μ) strands."""
    word = []
    s = 0
    for m in mu:
        for j in range(m - 1):
            word.append(s + j + 1)
        s += m
    return word


def markov_m3_sum_numeric(n: int, q_val, dps: int = 50):
    """Σ_λ y_λ(q_val) · d_λ at mpmath precision.  Should equal 1 by
    the Markov axiom (M3) tr_M(1) = 1 — *not* the Plancherel identity
    Σ_λ d_λ²/n! = 1.  See docs/audits/2026-05-11-plancherel-usage-audit.md
    (Finding D)."""
    mp.mp.dps = dps
    parts = partitions_of(n)
    total = mp.mpf(0)
    for lam in parts:
        y = y_lambda_wenzl_bridge_numeric(lam, q_val, dps)
        total += y * classical_dim(lam)
    return total


# Backward-compat alias; remove after downstream callers are updated.
plancherel_sum_numeric = markov_m3_sum_numeric


def markov_trace_lhs_numeric(n: int, mu, q_val, dps: int = 50):
    """Σ_λ y_λ(q_val) · χ_λ(σ_w_μ) at mpmath precision."""
    mp.mp.dps = dps
    word = cycle_type_word(tuple(mu))
    parts = partitions_of(n)
    total = mp.mpf(0)
    for lam in parts:
        y = y_lambda_wenzl_bridge_numeric(lam, q_val, dps)
        chi = chi_lambda_mpmath(lam, word, q_val, dps)
        total += y * chi
    return total


def markov_trace_target_numeric(n: int, mu, q_val, dps: int = 50):
    """z^{n-len(μ)} at mpmath precision (the RHS of the defining identity)."""
    mp.mp.dps = dps
    q = mp.mpf(str(q_val))
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    return z ** (n - len(tuple(mu)))


def main(ns: list[int], dps: int = 100, do_symbolic: bool = True) -> None:
    out_path = Path(__file__).parent / "y-lambda-wenzl-witness.json"
    if out_path.exists():
        out = json.loads(out_path.read_text())
    else:
        out = {"tables_by_n": {}}
    out["description"] = (
        "Wenzl-bridge closed-form y_λ for the generic Markov trace. "
        "Uses fractional principal Schur specialisation s_{λ, X}(Q) "
        "with Q = q² and X = qz/(1 - Q + qz).  Numerical at arbitrary "
        "precision (default 100 dps); symbolic in q via sympy."
    )
    out["formula"] = (
        "y_λ = s_{λ, X}(Q) / Σ_μ d_μ s_{μ, X}(Q)  where "
        "s_{λ, X}(Q) = Q^{n(λ)} ∏_x (1-X·Q^c)/(1-Q^h), Q=q², "
        "X = q·z/(1-Q+q·z)."
    )
    out["computedAt"] = datetime.now(timezone.utc).isoformat()
    out.setdefault("tables_by_n", {})

    for n in ns:
        parts = partitions_of(n)
        print(f"n={n} ({len(parts)} partitions, dps={dps})...", flush=True)
        rows = []
        for p in parts:
            y_num = y_lambda_wenzl_bridge_numeric(p, Q0_FLOAT, dps)
            entry = {
                "partition": p,
                "depth": max(0, len(p) - 1),
                "classical_dim": classical_dim(p),
                "y_lambda_numeric": str(y_num),
            }
            if do_symbolic and n <= 4:
                # Symbolic for small n only — sympy.factor is slow at n ≥ 5
                # despite the closed form being algorithmically simple
                # (sympy spends time canonicalising sqrt(q) expressions).
                # The Wenzl-bridge formula itself works for any n; the
                # symbolic OUTPUT just gets large quickly.
                y_sym = y_lambda_wenzl_bridge_symbolic(p)
                entry["y_lambda_symbolic"] = sp.sstr(y_sym)
            rows.append(entry)
        out["tables_by_n"][str(n)] = {
            "n": n,
            "dps": dps,
            "num_partitions": len(parts),
            "weights": rows,
        }
        # Incremental save.
        out_path.write_text(json.dumps(out, indent=2))

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    args = sys.argv[1:]
    dps = 100
    if args and args[0] == "--dps":
        dps = int(args[1])
        args = args[2:]
    ns = [int(a) for a in args] or list(range(2, 13))
    main(ns, dps=dps, do_symbolic=True)
