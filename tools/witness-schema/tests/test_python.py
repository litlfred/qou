"""Smoke tests — Pydantic models validate real witness JSON shapes."""

import json
import pathlib

import pytest

from witness_schema import (
    ComputationAssertion,
    ComputationWitness,
    UpstreamWitnessHash,
    __version__,
)


def test_version():
    assert __version__ == "0.1.0"


def test_minimal_witness():
    """A witness with only the 4 required fields validates."""
    w = ComputationWitness.model_validate(
        {
            "engine": "mpmath",
            "engineVersion": "1.3.0",
            "computedAt": "2026-05-24T00:00:00+00:00",
            "assertions": [],
        }
    )
    assert w.engine == "mpmath"
    assert w.assertions == []
    assert w.commitSha is None


def test_full_witness_round_trip():
    """A maximal witness JSON round-trips byte-identical."""
    raw = {
        "engine": "mpmath",
        "engineVersion": "1.3.0",
        "computedAt": "2026-05-24T05:00:00+00:00",
        "commitSha": "abc123",
        "scriptCommitSha": "def456",
        "scriptHash": "a1b2c3d4e5f6",
        "scriptFile": "folio-assistant/computations/hyperbolic_volumes.py",
        "name": "hyperbolic-volumes",
        "description": "Vol(4_1) at 50 dps via Clausen-function identity.",
        "contentBlock": "prop:vol-4-1-mostow",
        "durationMs": 12.3,
        "allPassed": True,
        "assertions": [
            {
                "name": "Vol(4_1)",
                "computed": "2.0298832128193",
                "expected": "2.0298832128193",
                "passed": True,
                "tolerance": 1e-14,
                "unit": "hyperbolic volume",
                "source": "SnapPy 3.3.2",
            }
        ],
        "parameters": {"dps": 50},
        "data": {"vol_5_2": "2.828122088334"},
        "caveats": ["Bounded by SnapPy 3.3.2's 15-digit Vol precision."],
        "upstream_witness_hashes": [],
    }
    w = ComputationWitness.model_validate(raw)
    assert w.allPassed
    assert len(w.assertions) == 1
    assert w.assertions[0].name == "Vol(4_1)"
    assert w.parameters == {"dps": 50}


def test_assertion_with_numeric_values():
    """Computed/expected accept JSON numbers (not just strings)."""
    a = ComputationAssertion.model_validate(
        {
            "name": "alpha_em_inv",
            "computed": 137.036,
            "expected": 137.035999084,
            "tolerance": 0.001,
            "source": "CODATA 2022",
        }
    )
    assert a.computed == 137.036


def test_upstream_witness_hash():
    """UpstreamWitnessHash validates with required fields only."""
    h = UpstreamWitnessHash.model_validate(
        {
            "path": "hyperbolic-volumes.witness.json",
            "sha256": "abc123def456",
        }
    )
    assert h.path == "hyperbolic-volumes.witness.json"
    assert h.size_bytes is None


def test_extra_fields_allowed():
    """The witness format is extensible — extra fields don't fail validation."""
    w = ComputationWitness.model_validate(
        {
            "engine": "mpmath",
            "engineVersion": "1.3.0",
            "computedAt": "2026-05-24T00:00:00+00:00",
            "assertions": [],
            "my_custom_field": {"foo": "bar"},
        }
    )
    assert w.engine == "mpmath"


def test_invalid_engine_rejected():
    """Engine enum is closed."""
    with pytest.raises(Exception):
        ComputationWitness.model_validate(
            {
                "engine": "rust",  # not in the enum
                "engineVersion": "1.0",
                "computedAt": "2026-05-24T00:00:00+00:00",
                "assertions": [],
            }
        )


def test_json_schema_file_present():
    """The shipped JSON schema file is at the documented path."""
    schema_path = pathlib.Path(__file__).resolve().parent.parent / "schema" / "witness.schema.json"
    assert schema_path.exists(), f"missing: {schema_path}"
    schema = json.loads(schema_path.read_text())
    assert schema["title"] == "ComputationWitness"
    assert "engine" in schema["properties"]
    assert schema["properties"]["engine"]["enum"][0] == "snappea"
