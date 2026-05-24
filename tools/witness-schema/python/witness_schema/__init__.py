"""witness-schema — Pydantic models for the QOU witness JSON format.

The canonical schema is `tools/witness-schema/schema/witness.schema.json`.
This module ships Pydantic v2 models that validate against the same
shape. Used by any Python consumer that reads `*.witness.json` files
produced by `qou_substrate.witness.WitnessBuilder`.

Example::

    from witness_schema import ComputationWitness
    import json

    with open("hyperbolic-volumes.witness.json") as f:
        w = ComputationWitness.model_validate_json(f.read())

    assert w.allPassed
    print(w.engineVersion, w.commitSha)
    for a in w.assertions:
        print(a.name, "→", a.computed, "vs", a.expected, "→", a.passed)
"""

from __future__ import annotations

from typing import Any, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict

__version__ = "0.1.0"

ComputationEngine = Literal[
    "snappea",
    "snappy",  # legacy name for `snappea`; new witnesses should prefer `snappea`
    "sympy",
    "mpmath",
    "sage",
    "python",
    "numpy",
    "scipy",
    "closed-form",
    "python+mpmath",
    "python+numpy+cvxpy",
]


class ComputationAssertion(BaseModel):
    """A single named claim with computed vs expected values."""

    model_config = ConfigDict(extra="allow")

    name: str
    computed: Union[float, str]
    expected: Union[float, str]
    passed: Optional[bool] = None
    tolerance: Optional[float] = None
    unit: Optional[str] = None
    source: Optional[str] = None


class UpstreamWitnessHash(BaseModel):
    """Recorded so a stale-witness validator can detect upstream drift."""

    model_config = ConfigDict(extra="allow")

    path: str
    sha256: str
    size_bytes: Optional[int] = None
    commitSha: Optional[str] = None
    scriptCommitSha: Optional[str] = None
    computedAt: Optional[str] = None


class ComputationWitness(BaseModel):
    """Top-level shape of a `*.witness.json` file.

    Field names match the JSON keys (camelCase for git / timestamp
    fields). `model_validate_json(raw_bytes)` performs a *validation*
    round-trip — the parsed object can be re-serialised but Pydantic
    does not guarantee byte-identical JSON output (key ordering,
    whitespace and float formatting may differ from the source file).

    `upstream_witness_hashes` lives under `data` per the in-repo
    convention; access via `witness.data["upstream_witness_hashes"]`.
    """

    model_config = ConfigDict(extra="allow")

    engine: ComputationEngine
    engineVersion: str
    computedAt: str
    assertions: list[ComputationAssertion]

    # Common but optional
    commitSha: Optional[str] = None
    scriptCommitSha: Optional[str] = None
    scriptHash: Optional[str] = None
    scriptFile: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    contentBlock: Optional[str] = None
    auditOnly: Optional[str] = None
    durationMs: Optional[float] = None
    allPassed: Optional[bool] = None
    parameters: Optional[dict[str, Any]] = None
    data: Optional[dict[str, Any]] = None
    caveats: Optional[list[str]] = None


__all__ = [
    "__version__",
    "ComputationEngine",
    "ComputationAssertion",
    "UpstreamWitnessHash",
    "ComputationWitness",
]
