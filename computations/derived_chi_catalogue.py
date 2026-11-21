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
(basis OPEN -- see the `k_λ` note below), the leading Markov weight
y_λ(0), the SDP shadow price y_λ⋆, and a `tier` provenance flag.

## The `k_λ` rule is a FIT (established 2026-10-10)

    The `prop:`-prefixed `per-partition-k-lambda-rule` NEVER EXISTED, and the
    `rem:`-prefixed block it was presumably meant to name
    established no rule. It was the `rem:`-prefixed `per-partition-k-lambda-rule`,
    a remark whose
    body was a table of SIX candidate per-partition `k_lambda` selection ansaetze,
    ALL EMPIRICALLY REFUTED, removed in 690458d6b0 (2026-06-17) under the owner
    principle "refuted-ansatz lemmas -> audit doc only". Its record is preserved in
    docs/audits/2026-06-17-refuted-ansatz-lemmas.md, which states the surviving
    question -- "does a structural `k_lambda` / `n*` selector exist?" -- is **open**,
    and is the open part of `conj:brane-tower-z-habiro`.

    So the rule used here ("1 iff lambda is the max-|mu| partition, 2 otherwise") is
    NOT supported by the block it cited. Measured: "max-|mu|" appears NOWHERE in that
    audit doc, so it is not even one of the six refuted candidates, and NO live
    content block in folio/ establishes any `k_lambda` rule. Owner ruling via relay,
    2026-10-10: the carrier stays audit-doc-only and its citations point there.

    🛑 AND IT IS NOT MERELY "BASIS OPEN" -- IT IS A FIT. That weaker reading stood
    here for part of 2026-10-10 and is superseded. The rule's origin is PR #639
    cycle 5b, `probe_phiq_per_partition_klambda.py`, readable at
    `0763606e4f^:_deprecated/probes/probe_phiq_per_partition_klambda.py` (the
    `_deprecated/` tree is no longer on main -- cite it commit-pinned, as here).
    Its own docstring states the rule under test verbatim:

        "Candidate rule under test: k_lambda = 1 if lambda is the
         maximum-|contrib| outlier for the atom; k_lambda = atom-uniform-k
         otherwise."

    Selection by maximum-|contrib| is selection of the block that DOMINATES the
    quantity being reproduced. Per AGENTS.md §"NO FITTING, EXCEPT CAL-1/2/3",
    "Selection against the target -- choosing an OBJECT because the choice
    reproduces the measured value -- is a fit even though no continuous parameter
    is tuned."

    THE LABEL "max-|mu|" IS ALSO WRONG, and the probe's own data refutes it. For
    tritium the flipped block is [6, 3] (witness
    `/data/dominant_partitions/tritium/lambda`), while the probe's docstring puts
    T's max|mu| = 8.23 at [4, 3, 1, 1]. Two different partitions: the rule selected
    by contribution and was later relabelled by eigenvalue magnitude.

    "CLOSES" MEANT |tower| < 2 AND WAS NEVER COMPARED TO AME. The probe's own
    closure print reads "atoms collapse to small-magnitude towers (|tower| < 2)".
    It records `ame_MeV` alongside and does not test against it. Recomputed from
    its committed witness:

        atom      cut blk    rows   tower(signed)   AME B   provenance of the tower
        deuteron  [2,2,1,1]     4         +0.8764  2.2246   cut block's k=1 term is
                                                            a HARDCODED 0.0
        tritium   [6,3]         2         -1.9370  8.4818   WRONG SIGN; k=3 hardcoded
        he3       [5,4]         2         +1.0659  7.7181   the only fully computed row

    🛑 CORRECTED 2026-10-11, twice over, and the first correction is mine.

    (i) THIS TABLE FIRST REPORTED |tower|, so tritium appeared as 1.9370 with a
    "-77.2% miss". The signed value is -1.9370 against a binding of +8.4818:
    that is the WRONG SIGN, a different and worse statement than a shortfall.

    (ii) THREE OF THE PROBE'S NINE DOMINANT-BLOCK ENTRIES WERE NEVER COMPUTED.
    `DOMINANT_PARTITION` is a hand-written literal dict carrying
    `"contrib_k1": 0.0,  # negligible` for deuteron and `# approximate` k=3
    values for deuteron and tritium. For DEUTERON THIS VOIDS THE RESULT: the
    rule sets k=1 on the cut block, so the tower IS
    `non_dominant_sum + contrib_k1(cut)` = 0.87640 + 0.00000. The rule's whole
    effect on deuteron was that literal zero.

    Relayed from a sibling session (60 dps, two routes agreeing to 2e-58; NOT
    recomputed here): D's real k=1 term is -0.62148, giving towers D 0.2550 /
    T -1.9719 / 3He 1.0656 under the May setup, and 0.2222 / 2.8116 / -0.0098
    under convention D at the proton pin -- where TRITIUM FAILS |tower| < 2, so
    the closure criterion itself fails under the canonical convention. Checkable
    here: 0.87640 + (-0.62148) = 0.25492, consistent with the relayed 0.2550.

    AND UNDER CONVENTION D THE DEUTERON CUT IS A PROVABLE NO-OP, needing no
    compute: [2,2,1,1] has FOUR rows, and
    `QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows` (sorry-free,
    general n) gives y_lambda = 0 for any shape with a third row. The block the
    rule flips carries zero Ocneanu weight, so its truncation order cannot move
    the tower.

    The conclusion is unchanged and STRENGTHENED. No tower approaches its
    binding, T has the wrong sign, the |tower| < 2 criterion is still met by
    driving the tower toward zero -- and for deuteron there was never a
    computation for it to be anti-correlated with.

    THE VALUE IS UNCHANGED BY THIS NOTE. `k_lambda` is emitted as before, and
    nothing reads it numerically; what changes is that it is now labelled a fit
    instead of carrying an implied derivation. Three witnesses carry `k_lambda` as
    a field -- derived-chi-catalogue, derived-chi-catalogue-sweep, and
    delta-lambda-categorical-verification. 🛑 THE THIRD IS A DIFFERENT OBJECT: it
    is a jet-prolongation order (that file's own docstring, line 18), not a
    truncation order, and the shared name is a collision. Deriving a structural
    selector, or proving none exists, is bean qou-9f4h. Bean qou-3kni.

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
    # `k_lambda`: per-partition truncation order, 1 on one block and 2 elsewhere.
    #
    # 🛑 FITTED (selection against target), NOT DERIVED. The rule picks the block
    # that DOMINATES the tower -- "maximum-|contrib| outlier", in its originating
    # probe's own words -- which AGENTS.md §NO FITTING classifies as a fit with no
    # continuous parameter tuned. The "max-|μ|" label this comment carried is
    # additionally wrong: for tritium the flipped block is [6,3] while max|μ| sits
    # at [4,3,1,1]. See the module docstring's `k_λ` note for the probe quote, the
    # per-atom AME comparison (and the hardcoded inputs behind it), and
    # docs/audits/2026-06-17-refuted-ansatz-lemmas.md. Deriving a real selector is
    # bean qou-9f4h.
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

_TIER_RANK: dict[str, int] = {
    "extracted": 0,
    "cal-anchored": 1,
    "derived": 2,
}
_QCONV_RANK: dict[str, int] = {
    "kassel": 0,
    "kauffman": 1,
}


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
        """Insert a NEW cell. Raises on a repeated (knot, partition, atom).

        Deliberately strict: a caller that did not expect a collision has a
        bug, and silently overwriting would hide a changed derivation. A
        caller that DOES mean to re-derive says so with `upsert()`.
        """
        key = (cell.knot, cell.partition, cell.atom)
        if key in self._index:
            raise ValueError(
                f"duplicate catalogue cell {key}; re-derive or update the "
                "existing record explicitly with `upsert()`."
            )
        self._index[key] = len(self.cells)
        self.cells.append(cell)

    def upsert(self, cell: KnotPartitionAtomCell, *, allow_downgrade: bool = False) -> str:
        """Insert `cell`, or replace an existing one with the same key when
        its provenance tier (and q_convention at equal tier) is at least as
        strong as the stored cell's (bean `qou-5cyl` / `qou-4sqq`).

        Returns `"added"`, `"unchanged"`, `"replaced"`, or `"kept_higher_tier"`.
        `"kept_higher_tier"` means an incoming cell of weaker provenance (e.g. a
        `cal-anchored` / `extracted` cell or a legacy `kassel` sympy cell
        colliding with a `derived` `kauffman` Rust production cell) was refused
        unless `allow_downgrade=True`, so re-running a Phase-2 builder can never
        silently downgrade Phase-3 production cells in `tier_counts()`.
        """
        key = (cell.knot, cell.partition, cell.atom)
        idx = self._index.get(key)
        if idx is None:
            self._index[key] = len(self.cells)
            self.cells.append(cell)
            return "added"
        existing = self.cells[idx]
        if existing == cell:
            return "unchanged"
        if not allow_downgrade:
            old_rank = (
                _TIER_RANK.get(existing.tier, 0),
                _QCONV_RANK.get(existing.q_convention, 0),
            )
            new_rank = (
                _TIER_RANK.get(cell.tier, 0),
                _QCONV_RANK.get(cell.q_convention, 0),
            )
            if new_rank < old_rank:
                return "kept_higher_tier"
        self.cells[idx] = cell
        return "replaced"

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


def _selftest() -> int:
    """Fast self-test (bean qou-5cyl): verify upsert idempotency and tier
    preservation (higher-tier cell is never silently downgraded)."""
    cat = DerivedChiCatalogue()
    c_rust = KnotPartitionAtomCell(
        knot="borromean", partition=(2, 1), atom="borromean-baryon",
        braid_word="(s1 s2^-1)^3", strand_count=3,
        chi_lambda_q_laurent=[(0, "4")], mu_eigenvalues=["1"],
        k_lambda=1, y_lambda_at_zero="0.25", y_star_shadow_price=None,
        tier="derived", q_convention="kauffman", derivation_ref="rust-phase3",
    )
    assert cat.upsert(c_rust) == "added"
    assert cat.upsert(c_rust) == "unchanged"
    c_weaker = KnotPartitionAtomCell(
        knot="borromean", partition=(2, 1), atom="borromean-baryon",
        braid_word="(s1 s2^-1)^3", strand_count=3,
        chi_lambda_q_laurent=[(0, "99")], mu_eigenvalues=["1"],
        k_lambda=1, y_lambda_at_zero="0.25", y_star_shadow_price=None,
        tier="cal-anchored", q_convention="kauffman", derivation_ref="codata-fit",
    )
    assert cat.upsert(c_weaker) == "kept_higher_tier"
    assert cat.lookup("borromean", (2, 1), "borromean-baryon") == c_rust
    c_kassel = KnotPartitionAtomCell(
        knot="borromean", partition=(2, 1), atom="borromean-baryon",
        braid_word="(s1 s2^-1)^3", strand_count=3,
        chi_lambda_q_laurent=[(0, "4")], mu_eigenvalues=["1"],
        k_lambda=1, y_lambda_at_zero="0.25", y_star_shadow_price=None,
        tier="derived", q_convention="kassel", derivation_ref="sympy-phase2",
    )
    assert cat.upsert(c_kassel) == "kept_higher_tier"
    print("self-test: ok (upsert added/unchanged/kept_higher_tier)")
    return 0


if __name__ == "__main__":
    import sys as _sys
    if "--self-test" in _sys.argv or "--selftest" in _sys.argv:
        raise SystemExit(_selftest())
