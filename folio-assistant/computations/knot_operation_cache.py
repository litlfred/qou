#!/usr/bin/env python3
"""
F4: Knot-operation discovery cache + factorization composer.

Per the user directive (Phase F4): "if SDP computation finds a new knot
operation/shell/valence/type ... cache that and scan/reuse to quicken
SDP computations or shadow prices.  Then the physics names are just
names given to observed knot operations from the math."

This module provides the **cache infrastructure** and **composer
interface** for recurring categorical structures discovered in the
Hecke algebra Wedderburn decomposition of atomic braids.

## Architecture

  ┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────┐
  │  Discovery layer    │ →  │   Cache (JSON)      │ ←  │ Composer layer  │
  │  (existing 33       │    │  knot-operation-    │    │  (chi via       │
  │   scripts + new     │    │  cache.json         │    │   factorization)│
  │   SDP / shadow LP)  │    │                     │    │                 │
  └─────────────────────┘    └─────────────────────┘    └─────────────────┘
                                       │
                                       ↓
                              ┌──────────────────┐
                              │  Naming layer    │
                              │  physics-names.  │
                              │  json (Ch 7      │
                              │   table)         │
                              └──────────────────┘

## Status

  - Schema: defined (KnotOperation, FactorizationWitness)
  - Cache load/save: implemented
  - Discovery: STUB — feeders from existing 33 scripts deferred
  - Composer: STUB — chi_via_factorization() raises NotImplementedError
  - HYBRID feeders: deferred (per F4.3 todo)

@module folio-assistant/computations/knot_operation_cache
"""
from __future__ import annotations
import hashlib
import json
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


CACHE_PATH = Path(__file__).parent / "knot-operation-cache.json"


@dataclass
class KnotOperation:
    """A recurring categorical structure in the Hecke algebra.

    Identifies a sub-block of a Wedderburn decomposition that appears
    in multiple atomic braids.  The mathematical content is the
    `braid_word_normal_form` (NF in H_n(q)); physics names are
    attached separately via the naming layer.

    Cache key: `cache_key()` returns a stable hash of (n, NF) for
    cross-script identification.
    """
    n: int
    """Number of strands the operation lives on (e.g. 3 for proton)."""

    braid_word_normal_form: list[tuple[int, int]]
    """Sorted Hecke NF as list of (sign, generator_index_1based)."""

    discovered_in: list[str] = field(default_factory=list)
    """Script names that have observed this operation."""

    plancherel_signature: dict[str, float] = field(default_factory=dict)
    """For each Wedderburn block λ, the Plancherel weight w_λ.
    Used as a fingerprint: two operations are 'equivalent' iff they
    have the same plancherel_signature (within tolerance).

    Keys are partition strings like '(3,2,1)'.
    """

    fingerprint: dict[str, str] = field(default_factory=dict)
    """**Discovery-time fingerprint** (Copilot review #r3144...).
    Holds non-NF binning identifiers used by feeders that don't
    extract a real Hecke normal form (e.g., bin labels, channel
    signatures, character magnitude bins).  Cache keys are derived
    from `(n, fingerprint)` when `braid_word_normal_form` is empty,
    so cache stability across binning tweaks is governed by this
    field's contents, not the NF.
    """

    discovered_at: str = ""
    """ISO-8601 timestamp of first discovery."""

    physics_name_candidate: Optional[str] = None
    """If a recognized physics structure (set by naming layer)."""

    def cache_key(self) -> str:
        """Stable hash of `(n, NF or fingerprint)` for cross-script
        identification.  When `braid_word_normal_form` is empty (a
        feeder has only a fingerprint, not an NF), the fingerprint
        contents are hashed instead so different bins still produce
        different cache keys.
        """
        if self.braid_word_normal_form:
            payload = ",".join(f"{s}:{g}" for s, g in self.braid_word_normal_form)
        else:
            payload = "fp|" + "|".join(
                f"{k}={self.fingerprint[k]}" for k in sorted(self.fingerprint)
            )
        h = hashlib.sha256(f"{self.n}|{payload}".encode()).hexdigest()[:16]
        return f"op_n{self.n}_{h}"


@dataclass
class FactorizationWitness:
    """Records that braid `β` factors as β_1 ⊗ β_2 ⊗ ... ⊗ β_k."""
    parent_n: int
    parent_braid_id: str  # hash of parent NF
    factors: list[str]  # cache_key() of each KnotOperation factor
    discovered_at: str
    discovered_by: str  # script name


class KnotOperationCache:
    """Persistent cache of discovered knot operations + factorizations."""

    def __init__(self, path: Path = CACHE_PATH):
        self.path = path
        self.operations: dict[str, KnotOperation] = {}
        self.factorizations: list[FactorizationWitness] = []
        self.load()

    def load(self) -> None:
        if not self.path.exists():
            return
        try:
            data = json.loads(self.path.read_text())
        except (json.JSONDecodeError, OSError):
            return
        for op_data in data.get("operations", {}).values():
            op = KnotOperation(**op_data)
            self.operations[op.cache_key()] = op
        for fact_data in data.get("factorizations", []):
            self.factorizations.append(FactorizationWitness(**fact_data))

    def save(self) -> None:
        out = {
            "operations": {
                k: asdict(v) for k, v in self.operations.items()
            },
            "factorizations": [asdict(f) for f in self.factorizations],
            "saved_at": datetime.now(timezone.utc).isoformat(),
        }
        self.path.write_text(json.dumps(out, indent=2, default=str))

    def add_operation(self, op: KnotOperation, discovered_in: str) -> str:
        """Register an operation; if already present, merge metadata."""
        key = op.cache_key()
        if key in self.operations:
            existing = self.operations[key]
            if discovered_in not in existing.discovered_in:
                existing.discovered_in.append(discovered_in)
        else:
            if not op.discovered_at:
                op.discovered_at = datetime.now(timezone.utc).isoformat()
            if discovered_in not in op.discovered_in:
                op.discovered_in.append(discovered_in)
            self.operations[key] = op
        return key

    def add_factorization(
        self, parent_n: int, parent_braid_id: str,
        factor_keys: list[str], discovered_by: str,
    ) -> None:
        # Idempotency: a factorization is fully determined by
        # (parent_braid_id, factor_keys, discovered_by).  Re-running a
        # feeder must not append a duplicate witness — only the first
        # occurrence's timestamp is kept.
        for existing in self.factorizations:
            if (existing.parent_braid_id == parent_braid_id
                    and existing.factors == factor_keys
                    and existing.discovered_by == discovered_by):
                return
        self.factorizations.append(FactorizationWitness(
            parent_n=parent_n,
            parent_braid_id=parent_braid_id,
            factors=factor_keys,
            discovered_at=datetime.now(timezone.utc).isoformat(),
            discovered_by=discovered_by,
        ))

    def report(self) -> str:
        lines = [
            f"KnotOperationCache: {len(self.operations)} operations, "
            f"{len(self.factorizations)} factorizations",
        ]
        for key, op in sorted(self.operations.items()):
            phys = f" [{op.physics_name_candidate}]" if op.physics_name_candidate else ""
            lines.append(
                f"  {key}: n={op.n}, NF length={len(op.braid_word_normal_form)}, "
                f"observed in {len(op.discovered_in)} scripts{phys}"
            )
        return "\n".join(lines)


# ─── Discovery interface ──────────────────────────────────────────────

def discover_factorization(
    braid_nf: list[tuple[int, int]],
    n: int,
    discovered_by: str = "unknown",
) -> list[KnotOperation]:
    """Decompose a braid word into its constituent knot operations.

    **Phase 3 (post-#428)**: detects **trivial tensor-product
    structure** — disjoint blocks of strands acted on by disjoint
    generator-index ranges.  E.g. word `[σ_1, σ_3, σ_1, σ_5]` on
    n = 6 splits into three factors:

      - β_1 = σ_1·σ_1 on strands {1, 2}  (n_1 = 2)
      - β_2 = σ_1       on strands {3, 4}  (n_2 = 2)
      - β_3 = σ_1       on strands {5, 6}  (n_3 = 2)

    so `chi_λ(β) = Σ c^λ_{μ_1 μ_2 μ_3} χ_{μ_1}(β_1) χ_{μ_2}(β_2) χ_{μ_3}(β_3)`.

    Algorithm: build a union-find on strands {0, ..., n-1} where
    `σ_i` (1-based generator) connects strands `i-1` and `i`.  After
    processing the word, each connected component is one factor; the
    sub-word for that factor is the subsequence of letters touching
    that component, with generator indices re-based to the component's
    minimum strand.  Output factors are returned in left-to-right
    component order (smallest minimum strand first).

    For words with **non-trivial entanglement** (generators bridging
    components), this returns a single full-braid `KnotOperation` —
    the caller can then run the SDP / shadow-price decomposition on
    that operation downstream.  See the F4 roadmap for the SDP path.
    """
    if not braid_nf:
        return [KnotOperation(
            n=n, braid_word_normal_form=[], discovered_in=[discovered_by],
        )]

    # Union-find on n strands (0-indexed internally).
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[max(ra, rb)] = min(ra, rb)

    for _sign, gen in braid_nf:
        i = gen - 1  # 0-indexed strand
        if 0 <= i < n - 1:
            union(i, i + 1)

    # Group strands by component root.
    components: dict[int, list[int]] = {}
    for s in range(n):
        components.setdefault(find(s), []).append(s)

    # If only one component, we have no tensor-product structure to
    # exploit — return the whole braid as a single op (preserves
    # generator order, per Copilot review #r3143789507).
    if len(components) == 1:
        return [KnotOperation(
            n=n,
            braid_word_normal_form=list(braid_nf),
            discovered_in=[discovered_by],
        )]

    # Sort components by their minimum strand (= leftmost in the
    # one-line braid layout).  Each component becomes one factor.
    ordered = sorted(components.values(), key=min)
    ops: list[KnotOperation] = []
    for comp in ordered:
        comp_set = set(comp)
        comp_n = len(comp)
        comp_min = min(comp)
        # Subsequence of letters that belong to this component.
        comp_word: list[tuple[int, int]] = []
        for sign, gen in braid_nf:
            i = gen - 1
            if i in comp_set:
                # Re-base generator index so the factor lives on
                # strands {0, ..., comp_n - 1}.
                comp_word.append((sign, gen - comp_min))
        ops.append(KnotOperation(
            n=comp_n,
            braid_word_normal_form=comp_word,
            discovered_in=[discovered_by],
        ))
    return ops


# ─── SDP / shadow-price discovery for entangled braids ───────────────


def discover_via_wedderburn_sdp(
    braid_nf: list[tuple[int, int]],
    n: int,
    q: float | None = None,
    discovered_by: str = "discover_via_wedderburn_sdp",
    tolerance: float = 1e-10,
    y_lambda_table: dict | None = None,
) -> list[KnotOperation]:
    """Shadow-price / Wedderburn-block decomposition for entangled braids.

    Complements [`discover_factorization`]: that handles
    tensor-decomposable braids (disjoint generator-index ranges); this
    handles the *entangled* case via per-irrep character evaluation.

    For a braid `β` on `n` strands, the Markov trace decomposes as

      `tr_M(T_β) = Σ_{λ ⊢ n} y_λ · χ_λ(T_β)`,

    where `y_λ` is the Plancherel / Jones-Markov weight (from the
    witness file) and `χ_λ` is the irreducible Hecke character at q.
    Each `λ` with `|χ_λ(T_β)| > tolerance` corresponds to an *active
    Wedderburn block* — a sub-component of `β` that lives in the
    `S^λ`-summand of `H_n(q)`.

    **Shadow-price interpretation** (Schrijver §4):  the dual LP
    `max  c·u  s.t.  Σ_λ u_λ · y_λ · χ_λ(T_β) ≥ tr_M(T_β),  u_λ ≥ 0`
    has a non-zero dual price `u_λ` exactly when block `λ` is active.
    Computing `χ_λ(T_β)` for every `λ` and filtering by the
    tolerance gives the support of the dual optimum directly,
    without invoking a full LP solver — adequate for fingerprinting
    purposes.  Callers needing the explicit `u_λ` values can run the
    LP downstream using `confinement-lp.py` as a template.

    Returns one KnotOperation per active block.  Each op carries:
      - `n` = strand count
      - `braid_word_normal_form` = []  (per-block fingerprint, not the
        original word — keeps `cache_key` stable across braids that
        activate the same blocks at the same q)
      - `plancherel_signature` = {`y_lambda`, `chi_value`, `partition_<i>`}
        where `partition_<i>` encodes the partition coordinates as
        floats (since `plancherel_signature` is a dict of floats).
      - `fingerprint` = {`feeder`, `n`, `partition`} — same shape as
        the y_λ feeder, so the two feeders' caches interoperate.

    `y_lambda_table` (optional): pre-loaded `{tuple(partition): y_λ}`
    dict.  If `None`, the function loads `y-lambda-jones-markov-
    witness.json` lazily.  Provide explicitly if running in a tight
    inner loop or against a non-default witness.

    `tolerance`: characters with `|χ_λ| < tolerance` are treated as
    inactive.  Default `1e-10` is conservative for f64 evaluation;
    the mpfr variant should pass a tighter tolerance.
    """
    if not braid_nf:
        # Empty braid: every block is "active" with χ_λ = dim S^λ.
        # Emit nothing (caller can use the y_λ feeder for that case).
        return []

    if q is None:
        from q_parameter import Q as Q0
        q = float(Q0)

    import pyhecke_native as p_native
    parts = [list(lam) for lam in p_native.partitions_of(n)]
    chars = p_native.chi_lambdas_braid(parts, list(braid_nf), q)

    if y_lambda_table is None:
        y_lambda_table = _load_y_lambda_table(n)

    new_ops: list[KnotOperation] = []
    for lam, chi in zip(parts, chars):
        chi_val = float(chi)
        if abs(chi_val) < tolerance:
            continue
        partition = tuple(lam)
        partition_str = "(" + ",".join(str(p_) for p_ in partition) + ")"
        plancherel_sig: dict[str, float] = {
            "y_lambda": float(y_lambda_table.get(partition, 0.0)),
            "chi_value": chi_val,
            "partition_depth": float(len(partition) - 1),
        }
        # Encode partition coordinates as part_0, part_1, ... so the
        # signature uniquely determines the partition (otherwise two
        # partitions with the same depth would collide).
        for i, p_i in enumerate(partition):
            plancherel_sig[f"part_{i}"] = float(p_i)
        fingerprint = {
            "feeder": discovered_by,
            "n": str(n),
            "partition": partition_str,
        }
        op = KnotOperation(
            n=n,
            braid_word_normal_form=[],
            plancherel_signature=plancherel_sig,
            fingerprint=fingerprint,
        )
        new_ops.append(op)
    return new_ops


def _load_y_lambda_table(n: int) -> dict:
    """Lazy-load the y_λ table for strand-count `n` from the
    Jones-Markov witness.  Returns `{tuple(partition): y_λ}`; missing
    entries default to 0.0 in callers."""
    witness_path = (
        Path(__file__).parent / "y-lambda-jones-markov-witness.json"
    )
    if not witness_path.exists():
        return {}
    with open(witness_path, encoding="utf-8") as f:
        data = json.load(f)
    table = data.get("tables_by_n", {}).get(str(n))
    if table is None:
        return {}
    return {
        tuple(entry["partition"]): float(entry["y_lambda"])
        for entry in table["weights"]
    }


# ─── Composer interface ──────────────────────────────────────────────

def chi_via_factorization(
    lam: tuple | list,
    factorization: list[KnotOperation],
    q: float,
) -> float:
    """Compute χ_λ(β) where β = β_1 ⊗ β_2 ⊗ ... ⊗ β_k from a
    tensor-product factorization (Phase 2 of F4 / post-#428).

    For each `op_i ∈ factorization` the character of the constituent
    braid β_i (its `braid_word_normal_form`) is computed via the
    Hoefsmit seminormal kernel — batched across all partitions
    `τ ⊢ op_i.n` in a single Rust call (per Copilot review #r3145...).
    The per-factor character vectors are then composed via
    Littlewood–Richardson coefficients, delegating the LR fold to
    `chi_via_factorization.compose_chi_lambda` (per Copilot review
    #r3145... — keeps the LR composition logic in one place).

    Args:
      lam: outer partition λ (must satisfy |λ| = Σ_i n_i).
      factorization: list of `KnotOperation`.  Each entry must carry
        concrete braid data: `braid_word_normal_form` may be empty
        only when the entry represents the identity factor (i.e.
        `fingerprint` is also empty).  `KnotOperation` entries
        produced by discovery feeders (which carry only a
        `fingerprint`, no NF) are rejected — build factor ops via
        `factor_op_from_word()` instead.
      q: substrate parameter for Hoefsmit evaluation.

    Returns: χ_λ(β) as float (Hoefsmit f64 path).  High-precision
    evaluation is not yet exposed by this module.

    Raises:
      ValueError: if `factorization` is empty, if `|λ|` does not
        equal the sum of factor strand counts, or if any factor has
        empty `braid_word_normal_form` *with* non-empty
        `fingerprint` (a discovery-only op with no concrete braid).
    """
    if not factorization:
        raise ValueError("factorization is empty")
    # Normalize λ to canonical descending order (Gemini #r3145...).
    # `compose_chi_lambda` looks up via `tuple(lam)` and partitions
    # are conventionally sorted non-increasing; an unsorted λ would
    # silently miss the entry and return 0.
    lam_list = sorted((int(p_) for p_ in lam), reverse=True)
    n_lam = sum(lam_list)
    n_total = sum(op.n for op in factorization)
    if n_lam != n_total:
        raise ValueError(
            f"|λ|={n_lam} but factorization spans {n_total} strands"
        )
    # Reject only discovery-fingerprint ops (empty NF + non-empty
    # `fingerprint`).  An empty NF on an op with empty fingerprint
    # is the legitimate identity-factor case.
    for i, op in enumerate(factorization):
        if not op.braid_word_normal_form and op.fingerprint:
            raise ValueError(
                f"factor {i} has empty braid_word_normal_form but "
                f"non-empty fingerprint metadata "
                f"({sorted(op.fingerprint.keys())}) — the F4 composer "
                "needs concrete braid data, not discovery-fingerprint "
                "metadata. Build factor ops via factor_op_from_word()."
            )

    # Lazy imports — keeps this module loadable even without the
    # wheel and without circular-import risk for the sibling module.
    import pyhecke_native as p  # type: ignore[import]
    from chi_via_factorization import compose_chi_lambda

    # Per-factor character vectors via batched Rust call.  Memoized
    # across calls by `(op.cache_key(), q)` so that recurring
    # KnotOperations (the whole point of the cache) avoid repeating
    # the Hoefsmit batch (Gemini #r3145...).
    def chars_for(op: KnotOperation) -> dict[tuple, float]:
        """χ_τ(β_op) for every τ ⊢ op.n, batched in one Rust call."""
        key = (op.cache_key(), float(q))
        cached = _CHARS_MEMO.get(key)
        if cached is not None:
            return cached
        taus = [list(tau) for tau in p.partitions_of(op.n)]
        if not taus:
            return {}
        word = list(op.braid_word_normal_form)
        values = p.chi_lambdas_braid(taus, word, q)
        out = {tuple(tau): float(v) for tau, v in zip(taus, values)}
        _CHARS_MEMO[key] = out
        return out

    factors_p = [op.n for op in factorization]
    factors_chi = [chars_for(op) for op in factorization]
    return compose_chi_lambda(lam_list, factors_p, factors_chi)


# Module-level cache keyed by `(cache_key, q)`.  The key is process-
# scoped — a KnotOperation with the same cache_key (= same braid NF
# at the same n) yields identical character vectors at fixed q.
# Cleared explicitly via `clear_chi_memo()`; not auto-bounded since
# realistic discovery-cache sizes (~10³ ops) × handful of q values
# remain in low MB.
_CHARS_MEMO: dict[tuple[str, float], dict[tuple, float]] = {}


def clear_chi_memo() -> None:
    """Drop the per-`(cache_key, q)` Hoefsmit-character cache used by
    `chi_via_factorization`.  Intended for tests and long-running
    pipelines that want to bound memory."""
    _CHARS_MEMO.clear()


def factor_op_from_word(
    n: int, word: list[tuple[int, int]],
    discovered_by: str = "factor_op_from_word",
) -> KnotOperation:
    """Convenience: build a KnotOperation directly from a braid word
    (typically used by tests or by callers that don't go through the
    discovery layer)."""
    return KnotOperation(
        n=n,
        braid_word_normal_form=list(word),
        discovered_in=[discovered_by],
    )


if __name__ == "__main__":
    # Smoke test: load (empty) cache, print report.
    cache = KnotOperationCache()
    print(cache.report())
