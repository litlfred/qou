#!/usr/bin/env python3
"""derived_chi_catalogue.py — 3-axis (knot, partition, atom) derived-
characters catalogue.

Owner direction (2026-06-07): "I want all derived wired up into compute.
3 axis framing."

This module is the Python-side schema + lookup API for the catalogue
work-plan documented in
`docs/audits/2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md`.

## Three axes

- K  : knot operator (PR #1677 census entry — Borromean, T(2,3), T(2,5), …)
- λ  : partition of n_K, indexing a Wedderburn block of H_{n_K}(q)
- A  : atom / physical observable target (the per-atom SDP routes (K, λ) → A)

## Per-cell record

Each (K, λ, A) cell carries: a derived χ^λ(β_K)(q) q-polynomial,
Hoefsmit |μ|-eigenvalues, the per-partition truncation order k_λ
(`prop:per-partition-k-lambda-rule`), the leading Markov weight
y_λ(0), the SDP shadow price y_λ⋆, and a `tier` provenance flag.

## Provenance tiers

- `derived`      — categorically derived (T17 R-matrix template +
                    T18 Markov-normalisation template). Wireable to
                    production with no Δ_λ-gate concern.
- `cal-anchored` — extracted from CODATA / experimental fit
                    (e.g. c_3 = -2.0693 at q_proton). Cached for
                    reuse but NEVER counted as a prediction.
- `extracted`    — back-solved from a related compute (e.g. empirical
                    Markov trace at a given q₀). Even weaker than
                    cal-anchored; do not promote without re-derivation.

The `tier` flag drives the Phase-3 failing-loud guard: any compute
site that claims a `derived` input but only gets `cal-anchored` from
the catalogue raises.

## Module status (Phase 1 — scaffold)

Schema + lookup API only. The first concrete derived cells
(`χ⁽²,¹⁾(β_Bor)`, `χ⁽³⁾(β_Bor)`) land in subsequent commits on this
branch.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Literal

# ── Provenance tier ────────────────────────────────────────────────

# ── Schema version (validated at load time) ───────────────────────

_SCHEMA_VERSION = "1.0.0"
# Bump when the on-disk witness shape changes incompatibly. The loader
# rejects unknown versions with a clear error so production compute
# can't silently consume a corrupted/mis-versioned witness.


# Tier of catalogue-cell provenance.
# - 'derived':      structurally derived, safe to wire as a prediction.
# - 'cal-anchored': extracted from CODATA (circular, never counted toward L2).
# - 'extracted':    back-solved from a related compute (weaker than cal-anchored).
Tier = Literal["derived", "cal-anchored", "extracted"]

_VALID_TIERS: frozenset[str] = frozenset({"derived", "cal-anchored", "extracted"})

# Variable convention for the stored `chi_lambda_q_laurent`:
# - 'kauffman': Rust / pyhecke_native canonical (Kauffman bracket t = q²);
#   degrees are integer for every (knot, partition). Default for new cells.
# - 'kassel':   skein-relation convention used by the sympy R-matrix build
#   (degrees half the Kauffman ones; kept only for legacy cells derived
#   via sympy before the Phase 3 migration).
QConvention = Literal["kauffman", "kassel"]

_VALID_Q_CONVENTIONS: frozenset[str] = frozenset({"kauffman", "kassel"})


# ── Per-cell record ────────────────────────────────────────────────


@dataclass(frozen=True)
class KnotPartitionAtomCell:
    """One catalogue entry — a single (K, λ, A) cell.

    Fields are stored as strings (mpf-serialised) where high precision
    matters; downstream consumers re-parse with `mpmath.mpf` at the
    declared dps. q-polynomial coefficients are stored as a list of
    (degree, coefficient) pairs so Laurent forms survive serialisation.
    """

    # ── 3-axis index ──
    # `knot`: knot-operator name (must appear in the PR #1677 census).
    knot: str
    # `partition`: λ ⊢ n_K, in non-increasing order, e.g. (2, 1).
    partition: tuple[int, ...]
    # `atom`: QOU atom / observable target (e.g. 'electron',
    # 'borromean-baryon', '4He', 'muon'). Multiple atoms may share a (K, λ) row.
    atom: str

    # ── Structural data ──
    # `braid_word`: canonical braid word for K in B_{n_K}, as a sigma-string,
    # e.g. 'σ_1·σ_2⁻¹·σ_1·σ_2⁻¹·σ_1·σ_2⁻¹' (Borromean).
    braid_word: str
    # `strand_count`: n_K, the strand count of the braid representative.
    strand_count: int
    # `chi_lambda_q_laurent`: χ^λ(β_K) as a Laurent polynomial in q, stored
    # as a list of (q-degree, coefficient-string) pairs. Negative degrees
    # allowed. Convention recorded in `q_convention`. Examples:
    #   χ⁽²,¹⁾(β_Bor) = −q⁶ + 3q⁴ − 3q² + 4 − 3q⁻² + 3q⁻⁴ − q⁻⁶
    #     [(−6,'−1'), (−4,'3'), (−2,'−3'), (0,'4'), (2,'−3'), (4,'3'), (6,'−1')]
    #   χ⁽²⁾(σ_1³) = q³ → [(3, '1')]
    #   χ⁽¹,¹⁾(σ_1³) = −q⁻³ → [(−3, '−1')]
    chi_lambda_q_laurent: list[tuple[int, str]]
    # `mu_eigenvalues`: eigenvalues |μ_a^(λ)| of ρ_λ(β_K) in Hoefsmit
    # seminormal form, as mpf strings, in non-increasing magnitude order.
    # Feeds k_λ.
    mu_eigenvalues: list[str]
    # `k_lambda`: per-partition truncation order. 1 iff λ is the max-|μ|
    # partition of β_H (per `prop:per-partition-k-lambda-rule`), 2 otherwise.
    k_lambda: int
    # `y_lambda_at_zero`: leading Markov-normalisation weight y_λ(0), as an
    # mpf string. Derived via T18 template (Markov axioms on the Wedderburn
    # block).
    y_lambda_at_zero: str
    # `y_star_shadow_price`: dual variable y_λ⋆ from the per-atom SDP active
    # set (`prop:operator-selection-lp`). None if this (K, λ, A) cell is NOT
    # in the active set for atom A — useful for negative entries.
    y_star_shadow_price: str | None

    # ── Provenance ──
    # `tier`: provenance flag (see `Tier` module-level comment).
    tier: Tier
    # `derivation_ref`: citation — commit-sha or audit-doc path of the
    # structural derivation (R-matrix script for `derived` cells; CODATA-
    # extraction audit for `cal-anchored`). Required for every cell.
    derivation_ref: str

    # `q_convention`: variable convention for `chi_lambda_q_laurent` (see
    # `QConvention` module-level comment). Defaults to `kauffman` (Rust /
    # pyhecke_native native); legacy sympy R-matrix cells from before
    # Phase 3 may carry `kassel`.
    q_convention: QConvention = "kauffman"
    # `notes`: optional human notes (open caveats, partial derivations, etc.).
    notes: str = ""


# ── Catalogue container ────────────────────────────────────────────


@dataclass
class DerivedChiCatalogue:
    """In-memory catalogue indexed by the three axes. The on-disk
    representation is the corresponding witness JSON.

    Cells are stored in `cells` (preserves insertion order) and indexed
    via `_index` (dict keyed by `(knot, partition, atom)`) for O(1)
    `add()`/`lookup()`/duplicate checks."""

    cells: list[KnotPartitionAtomCell] = field(default_factory=list)
    # Private O(1) index — (knot, partition, atom) → position in `cells`.
    # Maintained by `add()`; consumers should not touch directly.
    _index: dict[tuple[str, tuple[int, ...], str], int] = field(
        default_factory=dict, repr=False
    )

    # ── Mutation ──

    def add(self, cell: KnotPartitionAtomCell) -> None:
        key = (cell.knot, cell.partition, cell.atom)
        if key in self._index:
            raise ValueError(
                f"duplicate catalogue cell {key}; re-derive or update the "
                "existing record explicitly."
            )
        self._index[key] = len(self.cells)
        self.cells.append(cell)

    # ── Lookup ──

    def lookup(
        self, knot: str, partition: tuple[int, ...], atom: str
    ) -> KnotPartitionAtomCell:
        """Strict lookup — raises if the cell is missing."""
        key = (knot, partition, atom)
        idx = self._index.get(key)
        if idx is None:
            raise KeyError(
                f"no catalogue cell for {key} — the expected (K, λ, A) "
                "triple has not been derived (or recorded). Run "
                "`derived_chi_catalogue_build.py` to regenerate, or add the "
                "missing derivation."
            )
        return self.cells[idx]

    def lookup_derived(
        self, knot: str, partition: tuple[int, ...], atom: str
    ) -> KnotPartitionAtomCell:
        """Lookup that REQUIRES `tier == 'derived'`. This is the
        Phase-3 failing-loud guard: production compute sites that claim
        they consume a derived value must use this entry point, so any
        unintended `cal-anchored` consumption surfaces as a raise."""
        cell = self.lookup(knot, partition, atom)
        if cell.tier != "derived":
            raise ValueError(
                f"catalogue cell {(knot, partition, atom)} has tier "
                f"{cell.tier!r}; this site requires `derived` provenance "
                f"(see Phase-3 wiring policy in "
                "`docs/audits/2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md`)."
            )
        return cell

    def filter(
        self,
        *,
        knot: str | None = None,
        atom: str | None = None,
        tier: Tier | None = None,
    ) -> Iterable[KnotPartitionAtomCell]:
        """Iterate cells matching the given axis filters."""
        for cell in self.cells:
            if knot is not None and cell.knot != knot:
                continue
            if atom is not None and cell.atom != atom:
                continue
            if tier is not None and cell.tier != tier:
                continue
            yield cell

    # --- summary ---

    def tier_counts(self) -> dict[str, int]:
        out: dict[str, int] = {"derived": 0, "cal-anchored": 0, "extracted": 0}
        for cell in self.cells:
            out[cell.tier] = out.get(cell.tier, 0) + 1
        return out

    # --- serialisation ---

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": _SCHEMA_VERSION,
            "cell_count": len(self.cells),
            "tier_counts": self.tier_counts(),
            "cells": [
                {
                    "knot": c.knot,
                    "partition": list(c.partition),
                    "atom": c.atom,
                    "braid_word": c.braid_word,
                    "strand_count": c.strand_count,
                    "chi_lambda_q_laurent": [
                        {"q_degree": d, "coefficient": v}
                        for (d, v) in c.chi_lambda_q_laurent
                    ],
                    "mu_eigenvalues": list(c.mu_eigenvalues),
                    "k_lambda": c.k_lambda,
                    "y_lambda_at_zero": c.y_lambda_at_zero,
                    "y_star_shadow_price": c.y_star_shadow_price,
                    "tier": c.tier,
                    "q_convention": c.q_convention,
                    "derivation_ref": c.derivation_ref,
                    "notes": c.notes,
                }
                for c in self.cells
            ],
        }


# ── Singleton accessor ─────────────────────────────────────────────

_CATALOGUE_WITNESS = (
    Path(__file__).resolve().parent
    / "derived-chi-catalogue.witness.json"
)
"""Canonical on-disk catalogue path (populated by derived_chi_catalogue_build.py)."""


def load_catalogue() -> DerivedChiCatalogue:
    """Read the on-disk catalogue witness and return a populated
    `DerivedChiCatalogue`. Raises if the witness does not exist (Phase 1
    has not yet emitted any cells)."""
    import json

    if not _CATALOGUE_WITNESS.exists():
        raise FileNotFoundError(
            f"catalogue witness not found at {_CATALOGUE_WITNESS}; "
            "build it with `python3 derived_chi_catalogue_build.py`."
        )
    # Explicit utf-8 encoding so behaviour is deterministic in CI /
    # containers / dev machines regardless of platform default.
    raw = json.loads(_CATALOGUE_WITNESS.read_text(encoding="utf-8"))
    data = raw.get("data", raw)
    # The build script emits the catalogue under `data.catalogue` (a
    # dedicated sub-section of the witness), keeping room for non-cell
    # data alongside (e.g. `h_convention`, `rmatrix_trace_*`). Accept
    # either shape — top-level for hand-authored witnesses or nested
    # for the build-script output.
    cells_root = data.get("catalogue", data)
    # Fail fast on unknown schema versions so production compute can't
    # silently consume a mis-versioned witness. The `schema_version` is
    # optional for the legacy in-flight witnesses written before this
    # check landed; new emissions always include it.
    schema_version = cells_root.get("schema_version")
    if schema_version is not None and schema_version != _SCHEMA_VERSION:
        raise ValueError(
            f"catalogue witness schema_version={schema_version!r} does not "
            f"match the expected {_SCHEMA_VERSION!r}. Either upgrade the "
            "catalogue with a migration script or pin the loader to the "
            "older schema. Refusing to load to avoid silent data corruption."
        )
    cat = DerivedChiCatalogue()
    for c in cells_root.get("cells", []):
        # Accept either the canonical `chi_lambda_q_laurent` (q-degree
        # encoding) or the legacy `chi_lambda_q_taylor` (h-degree) for
        # backward compatibility with witnesses emitted before the
        # Phase 2 schema migration. New code emits only the Laurent form.
        if "chi_lambda_q_laurent" in c:
            # Each term provides EITHER `q_degree` (legacy field name) OR
            # `half_exp` (clearer name introduced post-Copilot review on
            # PR #1952). The semantic interpretation of the integer key
            # depends on the cell's `q_convention` field, NOT on which
            # name is used:
            #
            #   - `q_convention == 'kauffman'` ⇒ key is a half-exponent
            #     (key = 2 · math_q_exp), per pyhecke_native LaurentPolyQ.
            #   - `q_convention == 'kassel'` ⇒ key is the math q-exponent
            #     directly (legacy Phase-2 sympy emissions).
            #
            # The field name and the encoding are decoupled: a Phase-2
            # cell may write `q_degree: 2` meaning math q^2 (direct), while
            # a Phase-3 cell may write `q_degree: 2` meaning math q^1
            # (half-exp). Consumers must read `q_convention` to interpret.
            # Both field names are accepted here for forward / backward
            # compatibility.
            chi_entries: list[tuple[int, str]] = []
            for t in c["chi_lambda_q_laurent"]:
                raw_key = t.get("half_exp", t.get("q_degree"))
                if raw_key is None:
                    raise ValueError(
                        f"catalogue cell for "
                        f"{(c['knot'], tuple(c['partition']), c['atom'])} has a "
                        f"chi_lambda_q_laurent term missing both 'half_exp' and "
                        f"'q_degree' keys: {t!r}. Every term must carry exactly "
                        "one of these (legacy or current name) so the loader "
                        "can resolve the integer exponent."
                    )
                chi_entries.append((int(raw_key), str(t["coefficient"])))
        else:
            raise ValueError(
                f"catalogue cell for {(c['knot'], tuple(c['partition']), c['atom'])} "
                "is missing chi_lambda_q_laurent — regenerate via "
                "`derived_chi_catalogue_build.py` (the h-degree encoding was "
                "retired in the Phase 2 schema migration)."
            )
        tier = c["tier"]
        if tier not in _VALID_TIERS:
            raise ValueError(
                f"catalogue cell for {(c['knot'], tuple(c['partition']), c['atom'])} "
                f"has unknown tier {tier!r}; valid tiers are "
                f"{sorted(_VALID_TIERS)}. Refusing to load — the provenance "
                "guard depends on this field being one of the known values."
            )
        q_convention = c.get("q_convention", "kauffman")
        if q_convention not in _VALID_Q_CONVENTIONS:
            raise ValueError(
                f"catalogue cell for {(c['knot'], tuple(c['partition']), c['atom'])} "
                f"has unknown q_convention {q_convention!r}; valid values are "
                f"{sorted(_VALID_Q_CONVENTIONS)}. Refusing to load."
            )
        cat.add(KnotPartitionAtomCell(
            knot=c["knot"],
            partition=tuple(c["partition"]),
            atom=c["atom"],
            braid_word=c["braid_word"],
            strand_count=c["strand_count"],
            chi_lambda_q_laurent=chi_entries,
            mu_eigenvalues=[str(x) for x in c["mu_eigenvalues"]],
            k_lambda=int(c["k_lambda"]),
            y_lambda_at_zero=str(c["y_lambda_at_zero"]),
            y_star_shadow_price=(
                str(c["y_star_shadow_price"])
                if c.get("y_star_shadow_price") is not None else None
            ),
            tier=tier,
            q_convention=q_convention,
            derivation_ref=c["derivation_ref"],
            notes=c.get("notes", ""),
        ))
    return cat
