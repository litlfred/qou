#!/usr/bin/env python3


# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Typed dataclass schema for Habiro completion witnesses.

Mirrors the Lean class `QOU.BraidKnot.HabiroCompletion` in
`content/quantum-observable-universe/braids-and-knots/full-pole-structure-mass-trace.lean`:

    class HabiroCompletion where
      trace : Polynomial ℤ
      coeff : ℕ → Polynomial ℤ
      tail_in_ideal : ∀ N, qPochhammerPoly N ∣ ...

The Python side stores polynomials as sympy-parseable strings in
the variable `u = q^{1/2}` (matching `habiro_coefficients_atomic.py`)
and exposes typed deserialization so downstream scripts (validator,
Lean witness emitters) can avoid ad-hoc dictionary parsing.

Usage:

    from habiro_types import HabiroAtomicWitness
    w = HabiroAtomicWitness.from_json("habiro-coefficients-atomic.witness.json")
    for record in w.records:
        record.atom_label, record.p_in_u, record.habiro_coefficients[0].a_m
"""

from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass
class HabiroCoeff:
    """One cyclotomic coefficient `a_m(u) ∈ ℤ[u]`.

    Mirrors Lean `coeff m : Polynomial ℤ`. The polynomial is held
    as a sympy-parseable string in the indeterminate `u`. The
    `integral` flag and `remainder_nonzero` flag are diagnostics
    from the producing cyclotomic-division algorithm.
    """
    m: int
    a_m: str
    deg_a_m: int
    integral: bool
    remainder_nonzero: bool

    @classmethod
    def from_dict(cls, d: dict) -> "HabiroCoeff":
        return cls(
            m=int(d["m"]),
            a_m=str(d["a_m"]),
            deg_a_m=int(d["deg_a_m"]),
            integral=bool(d["integral"]),
            remainder_nonzero=bool(d["remainder_nonzero"]),
        )


@dataclass
class HabiroCompletionRecord:
    """One atom's Habiro completion data.

    Mirrors Lean `HabiroCompletion`:
      - `p_in_u` ↔ `trace : Polynomial ℤ`
      - `habiro_coefficients[m].a_m` ↔ `coeff m : Polynomial ℤ`
    The Python record carries additional metadata (`Z`, `N`,
    `denom_in_u`, etc.) needed to reconstruct the trace from
    upstream Markov / Hecke-character computations.
    """
    atom_label: str
    Z: int
    N: int  # neutron count (NOT the truncation order)
    include_inter: bool
    tr_M_in_q: str
    shift: int
    denom_in_u: str
    p_in_u: str
    deg_p_u: int
    habiro_coefficients: List[HabiroCoeff]

    @classmethod
    def from_witness_entry(cls, atom_label: str, d: dict) -> "HabiroCompletionRecord":
        return cls(
            atom_label=atom_label,
            Z=int(d["Z"]),
            N=int(d["N"]),
            include_inter=bool(d["include_inter"]),
            tr_M_in_q=str(d["tr_M_in_q"]),
            shift=int(d["shift"]),
            denom_in_u=str(d["denom_in_u"]),
            p_in_u=str(d["p_in_u"]),
            deg_p_u=int(d["deg_p_u"]),
            habiro_coefficients=[
                HabiroCoeff.from_dict(c) for c in d["habiro_coefficients"]
            ],
        )


@dataclass
class HabiroAtomicWitness:
    """Full atomic-Habiro witness (matches `habiro-coefficients-atomic.witness.json`)."""
    computation: str
    description: str
    reference_blocks: List[str]
    computed_at: str
    parameters: dict
    records: List[HabiroCompletionRecord]

    @classmethod
    def from_dict(cls, data: dict) -> "HabiroAtomicWitness":
        return cls(
            computation=str(data["computation"]),
            description=str(data["description"]),
            reference_blocks=list(data.get("reference_blocks", [])),
            computed_at=str(data.get("computedAt", "")),
            parameters=dict(data.get("parameters", {})),
            records=[
                HabiroCompletionRecord.from_witness_entry(label, entry)
                for label, entry in data.get("results", {}).items()
            ],
        )

    @classmethod
    def from_json(cls, path: str | Path) -> "HabiroAtomicWitness":
        with Path(path).open() as f:
            return cls.from_dict(json.load(f))
