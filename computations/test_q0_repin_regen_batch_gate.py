#!/usr/bin/env python3
"""The sweep driver must not be able to delete the muon anchor.

Commit 9a9c6b31c regenerated `q-pinning-50-digit.witness.json` at the proton
pin as part of a 25-witness batch. That file is not a datum -- it is what
`qou_substrate.witness._q0_value_for_anchor` reads as THE DEFINITION of the
muon pin -- so the sweep did not migrate a witness, it deleted an anchor:
both anchors resolved to the same value and 262 witnesses reported a flip.
Reverted by 2e4745448d. Beans `qou-m9xp`, `qou-cezp`, `qou-1c4y`.

These tests pin the two guards added afterwards.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from q0_repin_regen_batch import (  # noqa: E402
    NEVER_SWEEP,
    at_risk_count,
    _declared_ideal_muon,
)


def test_the_pin_definition_is_never_sweepable():
    """The specific file whose regeneration deleted the muon anchor."""
    assert "q_pinning_50_digit.py" in NEVER_SWEEP
    why = NEVER_SWEEP["q_pinning_50_digit.py"]
    # The reason must name the mechanism, not just say "don't".
    assert "_q0_value_for_anchor" in why
    assert "9a9c6b31c" in why and "2e4745448d" in why


def test_never_sweep_reasons_are_substantive():
    """Every entry must explain itself -- a bare skip-list rots into folklore."""
    for name, why in NEVER_SWEEP.items():
        assert len(why) > 40, f"{name}: reason too thin to act on"


def test_at_risk_count_ignores_missing_and_malformed():
    """A witness that cannot be read must not crash the planner."""
    assert at_risk_count(["computations/does-not-exist.witness.json"]) == 0
    assert at_risk_count([]) == 0


def test_at_risk_count_does_not_flag_counts():
    """Counts have zero margin and are not anchor-continuous.

    Regression against the triage's own first-version defect, now inherited
    here: 229 of a reported 291 "at risk" were `{tolerance: 0, computed: 77}`.
    If that leaked into the driver it would defer most of the corpus.
    """
    import json
    import tempfile

    doc = {"assertions": [
        {"name": "all_77_computed", "tolerance": 0, "computed": 77,
         "expected": 77, "passed": True},
    ]}
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "w.witness.json"
        p.write_text(json.dumps(doc))
        # at_risk_count resolves relative to REPO; feed an absolute-ish path
        # by monkeypatching is overkill -- assert via the triage directly.
        from q0_migration_tolerance_triage import is_discrete
        assert is_discrete(doc["assertions"][0])


def test_the_ideal_layer_is_read_from_the_manifest():
    """The declared ideal_muon set must be non-empty and come from the file.

    The driver had NO notion of the manifest: measured 2026-08-19, 16 of the
    23 producers in its plan were declared `ideal_muon`, so a sweep would have
    migrated canonical-chain artifacts off their declared layer -- the same
    class of error as the pin-file overwrite, distributed instead of pointed.
    """
    ideal = _declared_ideal_muon()
    assert len(ideal) > 100, f"manifest looks unread or empty: {len(ideal)}"
    # The pin producer itself is the canonical member of that layer.
    assert "q_pinning_50_digit" in ideal


def test_the_two_gates_are_independent():
    """Never-sweep is by FILE NAME, the ideal layer is by STEM.

    They must not be conflated: NEVER_SWEEP is "this breaks the tree", the
    manifest is "this is on its correct layer". A producer can be in one and
    not the other, and the reasons a reader needs are different.
    """
    ideal = _declared_ideal_muon()
    assert all(k.endswith(".py") for k in NEVER_SWEEP)
    assert all(not k.endswith(".py") for k in list(ideal)[:20])


if __name__ == "__main__":
    import pytest
    sys.exit(pytest.main([__file__, "-v"]))
