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

Tier = Literal["derived", "cal-anchored", "extracted"]
"""Catalogue-cell provenance. `derived` is the only tier safe to
wire as a prediction; the other two are cached and audited but never
counted toward an L2 pass."""


# ── Per-cell record ────────────────────────────────────────────────


@dataclass(frozen=True)
class KnotPartitionAtomCell:
    """One catalogue entry — a single (K, λ, A) cell.

    Fields are stored as strings (mpf-serialised) where high precision
    matters; downstream consumers re-parse with `mpmath.mpf` at the
    declared dps. q-polynomial coefficients are stored as a list of
    (degree, coefficient) pairs so Laurent forms survive serialisation.
    """

    # --- 3-axis index ---
    knot: str
    """Knot operator name (must appear in the PR #1677 census)."""

    partition: tuple[int, ...]
    """Partition λ of n_K, in non-increasing order, e.g. (2, 1)."""

    atom: str
    """QOU atom / observable target (e.g. 'electron', 'borromean-baryon',
    '4He', 'muon'). Multiple atoms may share a (K, λ) row."""

    # --- structural data ---
    braid_word: str
    """The canonical braid word for K in B_{n_K}, as a sigma-string,
    e.g. 'σ_1·σ_2⁻¹·σ_1·σ_2⁻¹·σ_1·σ_2⁻¹' (Borromean)."""

    strand_count: int
    """n_K, the strand count of the braid representative."""

    chi_lambda_q_taylor: list[tuple[int, str]]
    """Polynomial expression of χ^λ(β_K) in the canonical Kassel-Faddeev
    variable `h = q − q⁻¹`, as a list of (h-degree, coefficient-string)
    pairs. The expansion is in **`h`, not `q − 1`** — see T17 (PR #1933)
    and `2026-06-07-knot-partition-atom-catalogue-3-axis-workplan.md` §
    notation for why. Example for χ⁽²,¹⁾(β_Bor) = 2 − 3h⁴ − h⁶ with
    h = q − q⁻¹:
        [(0, '2'), (4, '-3'), (6, '-1')]."""

    mu_eigenvalues: list[str]
    """Eigenvalues |μ_a^(λ)| of ρ_λ(β_K) in Hoefsmit seminormal form,
    as mpf strings, in non-increasing magnitude order. Feeds k_λ."""

    k_lambda: int
    """Per-partition truncation order. 1 iff λ is the max-|μ| partition
    of β_H (β-Hadamard, per `prop:per-partition-k-lambda-rule`), 2
    otherwise."""

    y_lambda_at_zero: str
    """Leading Markov-normalisation weight y_λ(0), as an mpf string.
    Derived via T18 template (Markov axioms on the Wedderburn block)."""

    y_star_shadow_price: str | None
    """Dual variable y_λ⋆ from the per-atom SDP active set
    (`prop:operator-selection-lp`). None if this (K, λ, A) cell is
    NOT in the active set for atom A — useful for negative entries."""

    # --- provenance ---
    tier: Tier
    """Provenance flag (see module docstring)."""

    derivation_ref: str
    """Citation: commit-sha or audit-doc path of the structural
    derivation (R-matrix script for `derived` cells; CODATA-extraction
    audit for `cal-anchored`). Required for every cell."""

    notes: str = ""
    """Optional human notes (open caveats, partial derivations, etc.)."""


# ── Catalogue container ────────────────────────────────────────────


@dataclass
class DerivedChiCatalogue:
    """In-memory catalogue indexed by the three axes. The on-disk
    representation is the corresponding witness JSON."""

    cells: list[KnotPartitionAtomCell] = field(default_factory=list)

    # --- mutation ---

    def add(self, cell: KnotPartitionAtomCell) -> None:
        for existing in self.cells:
            if (
                existing.knot == cell.knot
                and existing.partition == cell.partition
                and existing.atom == cell.atom
            ):
                raise ValueError(
                    f"duplicate catalogue cell {(cell.knot, cell.partition, cell.atom)}; "
                    f"re-derive or update the existing record explicitly."
                )
        self.cells.append(cell)

    # --- lookup ---

    def lookup(
        self, knot: str, partition: tuple[int, ...], atom: str
    ) -> KnotPartitionAtomCell:
        """Strict lookup — raises if the cell is missing."""
        for cell in self.cells:
            if (
                cell.knot == knot
                and cell.partition == partition
                and cell.atom == atom
            ):
                return cell
        raise KeyError(
            f"no catalogue cell for {(knot, partition, atom)} — the "
            "expected (K, λ, A) triple has not been derived (or recorded). "
            "Run `derived_chi_catalogue_build.py` to regenerate, or add the "
            "missing derivation."
        )

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
            "schema_version": "1.0.0",
            "cell_count": len(self.cells),
            "tier_counts": self.tier_counts(),
            "cells": [
                {
                    "knot": c.knot,
                    "partition": list(c.partition),
                    "atom": c.atom,
                    "braid_word": c.braid_word,
                    "strand_count": c.strand_count,
                    "chi_lambda_q_taylor": [
                        {"h_degree": d, "coefficient": v}
                        for (d, v) in c.chi_lambda_q_taylor
                    ],
                    "mu_eigenvalues": list(c.mu_eigenvalues),
                    "k_lambda": c.k_lambda,
                    "y_lambda_at_zero": c.y_lambda_at_zero,
                    "y_star_shadow_price": c.y_star_shadow_price,
                    "tier": c.tier,
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
    raw = json.loads(_CATALOGUE_WITNESS.read_text())
    data = raw.get("data", raw)
    # The build script emits the catalogue under `data.catalogue` (a
    # dedicated sub-section of the witness), keeping room for non-cell
    # data alongside (e.g. `h_convention`, `rmatrix_trace_*`). Accept
    # either shape — top-level for hand-authored witnesses or nested
    # for the build-script output.
    cells_root = data.get("catalogue", data)
    cat = DerivedChiCatalogue()
    for c in cells_root.get("cells", []):
        cat.add(KnotPartitionAtomCell(
            knot=c["knot"],
            partition=tuple(c["partition"]),
            atom=c["atom"],
            braid_word=c["braid_word"],
            strand_count=c["strand_count"],
            chi_lambda_q_taylor=[
                (int(t["h_degree"]), str(t["coefficient"]))
                for t in c["chi_lambda_q_taylor"]
            ],
            mu_eigenvalues=[str(x) for x in c["mu_eigenvalues"]],
            k_lambda=int(c["k_lambda"]),
            y_lambda_at_zero=str(c["y_lambda_at_zero"]),
            y_star_shadow_price=(
                str(c["y_star_shadow_price"])
                if c.get("y_star_shadow_price") is not None else None
            ),
            tier=c["tier"],
            derivation_ref=c["derivation_ref"],
            notes=c.get("notes", ""),
        ))
    return cat
