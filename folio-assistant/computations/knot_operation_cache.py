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


# ─── Discovery interface (STUB) ───────────────────────────────────────

def discover_factorization(
    braid_nf: list[tuple[int, int]],
    n: int,
    discovered_by: str = "unknown",
) -> list[KnotOperation]:
    """Decompose a braid NF into its constituent knot operations.

    **STATUS: STUB.**

    The intended implementation:
      1. Run the SDP / shadow-price / Wedderburn-block decomposition
         on `braid_nf`.
      2. Identify recurring sub-blocks by matching against the cache.
      3. For each sub-block found, return its KnotOperation.

    Currently returns a single KnotOperation wrapping the whole braid.
    """
    # Per Copilot review #r3144...: do NOT sort braid_nf — sorting
    # changes generator order, which generally changes the underlying
    # braid/Hecke element. Preserve input order until a real
    # order-preserving normal-form algorithm is implemented.
    op = KnotOperation(
        n=n,
        braid_word_normal_form=list(braid_nf),
        discovered_in=[discovered_by],
    )
    return [op]


# ─── Composer interface (STUB) ───────────────────────────────────────

def chi_via_factorization(
    lam: tuple,
    factorization: list[KnotOperation],
    q: float,
) -> float:
    """Compute χ_λ(β) where β = ⊗ factorization.

    **STATUS: STUB.**

    The intended implementation: for a tensor-product factorization
    `β = β_1 ⊗ β_2 ⊗ ...`, the character factors as
    `χ_λ(β) = Σ_{λ_1 ⊗ λ_2 ⊗ ... ⊆ λ} χ_{λ_1}(β_1) · χ_{λ_2}(β_2) · ...`
    where the sum is over Littlewood-Richardson decompositions.

    For non-tensor factorizations (e.g. inter-nucleon couplings),
    the composition is more involved and uses Markov stabilization.
    """
    raise NotImplementedError(
        "chi_via_factorization is a stub — see F4 implementation roadmap"
    )


if __name__ == "__main__":
    # Smoke test: load (empty) cache, print report.
    cache = KnotOperationCache()
    print(cache.report())
