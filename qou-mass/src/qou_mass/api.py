"""Public API for qou_mass — thin orchestration over the
canonical-derivation pipeline.

This module is intentionally small. All heavy lifting (Markov trace,
χ^λ, Wedderburn weights, knot-operator catalogue) lives in dedicated
submodules. The public functions here:

  predict(atom, observable=...) -> Prediction
  predict_nucleon(particle, ...) -> Prediction
  compute_tr_M(Z, N, ...) -> Decimal
  canonical_braid(Z, N) -> BraidWord
  predict_table(atoms, ...) -> list[Prediction]

P1 STATUS (2026-05-19): Skeleton only. Heavy paths are stubbed to
NotImplementedError pending the module-vendoring pass (`canonical_
mass_table_extended.py`, `m_p_borromean_verification_50dps.py`,
`canonical_braid_crossings.py`, `markov_trace_recursive.py`,
`wedderburn_jones_markov.py`, `witness_base.py`,
`isotope_record_schema.py`, `active_set_pruning.py` — see
qou-mass-architecture-plan §4 Phase 2 for the migration steps).
"""
from __future__ import annotations

from decimal import Decimal
from typing import Iterable, Literal

from .prediction import BraidWord, Prediction, Witness


AtomLabel = str | tuple[int, int]
Observable = Literal["binding_energy", "mass", "tr_M", "mass_excess"]
Method = Literal["auto", "markov_peel", "rust_canonical_chi",
                 "alpha_cluster", "borromean"]
Particle = Literal["p", "n", "mu"]


def predict(
    atom: AtomLabel,
    observable: Observable = "binding_energy",
    *,
    q: Decimal | float | None = None,
    precision_dps: int = 50,
    method: Method = "auto",
    emit_witness: bool = False,
    witness_path: str | None = None,
) -> Prediction:
    """Predict a physical observable for the given atom.

    Args:
      atom: Either a label like ``"4He"`` / ``"He-4"`` / ``"helium-4"``
            or a ``(Z, N)`` tuple.
      observable: ``"binding_energy"`` (default; MeV), ``"mass"``
            (MeV), ``"tr_M"`` (dimensionless), ``"mass_excess"`` (MeV).
      q: Substrate parameter; defaults to the QOU canonical
            ``q_0 ≈ 1.10998``.
      precision_dps: Internal mpmath precision (decimal places).
      method: Compute path. ``"auto"`` picks the fastest backend that
            covers the (Z, N) requested.
      emit_witness: If True, the returned Prediction carries a full
            Witness object whose ``to_json()`` reproduces the QOU
            witness-JSON shape.
      witness_path: Convenience — if set, the witness JSON is also
            written to disk at this path.
    """
    raise NotImplementedError(
        "qou_mass v0.1.0a1 (P1) — skeleton only. Vendoring of the "
        "canonical-mass-table-extended pipeline is the next P2 step "
        "(see qou-mass-architecture-plan §4 Phase 2)."
    )


def predict_nucleon(
    particle: Particle,
    *,
    precision_dps: int = 50,
    emit_witness: bool = False,
    witness_path: str | None = None,
) -> Prediction:
    """Predict the mass of a single nucleon (or muon) via the Borromean tower."""
    raise NotImplementedError("v0.1.0a1 P1 skeleton — vendoring pending.")


def predict_table(
    atoms: Iterable[AtomLabel],
    **kwargs,
) -> list[Prediction]:
    """Predict every observable for every atom in the iterable."""
    return [predict(a, **kwargs) for a in atoms]


def compute_tr_M(
    Z: int,
    N: int,
    *,
    q: Decimal | None = None,
    precision_dps: int = 50,
    backend: Literal["python_mpmath", "rust"] = "python_mpmath",
    cache: bool = True,
) -> Decimal:
    """Compute |tr_M(β_atom(Z,N), q_0)| — the raw Markov-trace observable."""
    raise NotImplementedError("v0.1.0a1 P1 skeleton — vendoring pending.")


def canonical_braid(Z: int, N: int) -> BraidWord:
    """Return the canonical braid word for atom (Z, N)."""
    raise NotImplementedError("v0.1.0a1 P1 skeleton — vendoring pending.")
