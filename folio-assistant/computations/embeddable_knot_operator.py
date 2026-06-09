#!/usr/bin/env python3
"""Generic embeddable knot operator with geometric overlap weighting.

Reusable infrastructure for lateral-vs-axial channel weighting — the
categorical expression of σ > π bond strength. Import it from any example
that decomposes binding into orthogonal embedded channels (diatomics,
aromatic rings, shell closures, …) and supply the per-channel overlap
weights from the embedding geometry.

## Model

A knot operator (a covalent channel, a linking sub-braid, …) embeds into
the ambient 3-manifold along a direction relative to the bond axis.
Its binding contribution scales by an OVERLAP WEIGHT w ∈ (0, 1] set by that
embedding geometry:

  * AXIAL (σ-type):       w = 1            (head-on, maximal overlap)
  * TRANSVERSE (π-type):  w = w_perp < 1   (lateral overlap)

The total binding of a composite is the overlap-weighted sum over its
embeddable operators. Two invariants worth stating:

  * CARDINALITY is unchanged by weighting — every channel with w > 0 is
    still "occupied", so the active-set = bond-order result is untouched.
  * Weighting only corrects the ENERGY, which the equal-channel (all w=1)
    model overbinds.

`w_perp` is the transverse/axial overlap ratio — a GEOMETRIC property of
the embedding (the orbital overlap integral, per system), NOT a fitted
universal constant.

Content block: def:embeddable-knot-operator
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class EmbeddableKnotOperator:
    """A knot operator embedded into the 3-manifold with a geometric overlap weight."""

    label: str
    base_binding: float          # un-embedded channel binding (energy units)
    overlap_weight: float        # geometric overlap factor in (0, 1]; 1 = axial/σ

    def __post_init__(self) -> None:
        if not (0.0 < self.overlap_weight <= 1.0 + 1e-12):
            raise ValueError(
                f"overlap_weight must be in (0, 1]; got {self.overlap_weight}"
            )

    def binding(self) -> float:
        """Embedded binding contribution = base × geometric overlap weight."""
        return self.base_binding * self.overlap_weight


def axial(label: str, base: float) -> EmbeddableKnotOperator:
    """σ-type channel: full (head-on) overlap, w = 1."""
    return EmbeddableKnotOperator(label, base, 1.0)


def transverse(label: str, base: float, w_perp: float) -> EmbeddableKnotOperator:
    """π-type channel: lateral overlap, w = w_perp < 1."""
    return EmbeddableKnotOperator(label, base, w_perp)


def total_binding(ops: Iterable[EmbeddableKnotOperator]) -> float:
    """Overlap-weighted total binding of a composite of embeddable operators."""
    return sum(o.binding() for o in ops)


def multiple_bond(base_sigma: float, order: int, w_perp: float) -> List[EmbeddableKnotOperator]:
    """An order-k bond as 1 axial σ + (k−1) transverse π embeddable operators.

    The cardinality (number of operators) equals the bond order; the energy
    is total_binding = base_sigma · (1 + (order−1)·w_perp).
    """
    if order < 1:
        raise ValueError("bond order must be >= 1")
    ops = [axial("sigma", base_sigma)]
    for i in range(order - 1):
        ops.append(transverse(f"pi_{i + 1}", base_sigma, w_perp))
    return ops


# ── Demo / witness (not imported; runs the σ+2π triple-bond example) ──────
if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent))
    import _path_bridge  # noqa: F401
    from experimental_constants import D0_N2_EV
    from witness_base import WitnessBuilder

    HERE = Path(__file__).parent
    w = WitnessBuilder("embeddable-knot-operator", engine="python")
    w.set_description(
        "Generic embeddable knot operator with geometric overlap weighting "
        "(axial σ w=1, transverse π w=w_perp<1). Demonstrates the lateral-π "
        "energy reduction on the σ+2π triple bond; reusable downstream."
    )
    w.set_content_block("def:embeddable-knot-operator")

    # De-hardcoded: source the single-channel σ binding from the computed
    # CO bond-order witness. add_upstream records its sha256 + commit-SHA
    # under data.upstream_witness_hashes so witness_dependency_drift.py flags
    # this witness as stale if the CO witness changes (Copilot review).
    co_w = w.add_upstream(HERE / "co-bond-order-active-set.witness.json")
    sigma_b = float(co_w["data"]["sigma_channel_eV"])     # +4.62 eV (computed, drift-tracked)

    print("=" * 68)
    print("EMBEDDABLE KNOT OPERATOR — lateral-π overlap weighting")
    print("=" * 68)
    print(f"single axial (σ) channel binding b_σ = {sigma_b:.4f} eV (computed)")
    print(f"reference D_0(N≡N, pure-covalent triple) = {D0_N2_EV} eV\n")

    print(f"{'w_perp':>8} {'E(σ+2π) eV':>12} {'vs D_0(N2)':>12}  note")
    print("-" * 56)
    sweep = {}
    for w_perp in (1.0, 0.7, 0.5, 0.3):
        ops = multiple_bond(sigma_b, order=3, w_perp=w_perp)
        E = total_binding(ops)
        sweep[w_perp] = E
        note = ("equal-channel — OVERBINDS" if w_perp == 1.0
                else "lateral-reduced")
        print(f"{w_perp:>8.2f} {E:>12.4f} {E / D0_N2_EV:>11.2f}x  {note}")
    print()
    print("Reading: the equal-channel model (w=1) gives "
          f"{sweep[1.0]:.2f} eV, {sweep[1.0]/D0_N2_EV:.2f}x over D_0(N2); a")
    print("physical lateral weight w_perp in [0.3, 0.7] brackets the observed")
    print("D_0 — but w_perp is the per-system orbital overlap ratio (geometric,")
    print("from the embedding), NOT fitted here. Cardinality (3 channels = bond")
    print("order 3) is independent of w_perp.")

    w.add_parameter("sigma_channel_eV", sigma_b)
    w.add_parameter("D0_N2_eV", D0_N2_EV)
    w.add_data("triple_bond_energy_vs_w_perp",
               {f"{k:.2f}": v for k, v in sweep.items()})
    w.add_assertion(
        "lateral weighting (w_perp<1) reduces the equal-channel overbind",
        computed=bool(sweep[0.5] < sweep[1.0]),
        expected=True,
        source="E(σ+2π) = b_σ·(1 + 2·w_perp) is monotone increasing in w_perp",
    )
    w.add_assertion(
        "cardinality (3 channels) independent of overlap weight",
        computed=len(multiple_bond(sigma_b, 3, 0.3)) == len(multiple_bond(sigma_b, 3, 1.0)),
        expected=True,
        source="multiple_bond builds order operators regardless of w_perp",
    )
    w.save()
    print("\nDone. Witness saved.")
