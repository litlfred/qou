"""A witness whose rows are exception text must not serialise as passing.

The failure this locks down (bean qou-qe81).
`computations/phase5/phase3_triton_binding_convention_b.py` was broken on
2026-08-01 by a keyword rename that missed a caller.  It caught the
`AssertionError` per atom, wrote the exception TEXT into each row, and emitted

    {"atom": "T", "Z": 1, "N": 2, "A": 3, "hecke_level": "H_9",
     "error": "AssertionError: binding_canonical: the `E_0` keyword is
               deprecated; ..."}

    allPassed: true      assertions: 0

Four rows, every one an error string, and the witness passed.  It sat in the
corpus in that state for a month.  `allPassed` is
`all(a.passed for a in self.assertions)`, and `all([])` is `True`, so a
producer that registers no assertions is green no matter what its payload
says; nothing else in the write path read the payload.

The producer was fixed in 372872149.  These tests are the GATE, because the
producer was one instance of a general shape: three more witnesses in the
corpus are green today with recorded exceptions in them
(`delta-coupling-closed-form-probe`, `paper-six-term-isotope-sweep`,
`term6-residues-at-roots`).

The two tests that carry the most weight are:

* `test_numeric_error_field_stays_green` — `error` is OVERLOADED in this
  corpus.  Five witnesses use it for a NUMERICAL error
  (`mass-from-q-symbolic` has `.data.proton.volumes[0].error = 9.98e-13`),
  and the sibling key `err` is numeric in all 34 of its occurrences.  A gate
  keyed on the presence of the key would be wrong about half the time and
  would be switched off.  It is keyed on the SHAPE OF THE VALUE, and this
  test is what holds that line.
* `test_vacuous_green_is_labelled_not_flipped` — 359 of the 2522 witnesses
  carrying an `allPassed` field are green over an EMPTY assertion array.
  Flipping that verdict is a 14 %-of-corpus red wall, and it was already
  tried and withdrawn once (bean qou-vfy1: `allPassed: null` turns a silent
  false positive into a loud false negative for the ~dozen producers that
  write `return 0 if wit["allPassed"] else 1`).  This test pins the decision
  that the state gets a LABEL and not a flip, so a later pass does not quietly
  re-litigate it.

Precision note: this module sets no `mp.dps` and must not.  pytest imports
every test module at collection time, so an `mp.mp.dps = N` at module scope
leaks into sibling modules whose exact-equality tests then fail for reasons
nothing in them explains.  Nothing here needs a precision; if that ever
changes, scope it with an autouse `mp.workdps(...)` fixture.
"""

from __future__ import annotations

import json
import pathlib
import sys

import pytest

# Import THIS worktree's substrate, not whatever `qou_substrate` a stray
# install might resolve to — the whole point is to exercise the file under
# test.  `tools/qou-substrate/pyproject.toml` does this for its own tests via
# `[tool.pytest.ini_options] pythonpath`, which does not reach this directory.
ROOT = pathlib.Path(__file__).resolve().parent.parent
_SUBSTRATE = ROOT / "tools" / "qou-substrate" / "python"
if str(_SUBSTRATE) not in sys.path:
    sys.path.insert(0, str(_SUBSTRATE))

WitnessBuilder = pytest.importorskip("qou_substrate.witness").WitnessBuilder

# Any real file works; the builder only hashes it.
SCRIPT = __file__

# The exact string the broken producer wrote into every row.
TRITON_ERROR = (
    "AssertionError: binding_canonical: the `E_0` keyword is deprecated; "
    "pass Q_beta_n_mev= instead"
)


def _builder(name: str = "error-row-gate-test") -> WitnessBuilder:
    return WitnessBuilder(name, engine="python", _script_path=SCRIPT)


# ── the gate bites ──────────────────────────────────────────────────────


def test_error_rows_with_zero_assertions_are_not_green():
    """The phase3_triton shape, exactly: four error rows, no assertions."""
    b = _builder()
    b.add_data("rows", [
        {"atom": a, "Z": 1, "N": n, "A": 1 + n, "hecke_level": "H_9",
         "error": TRITON_ERROR}
        for a, n in (("D", 1), ("T", 2), ("3He", 1), ("4He", 2))
    ])
    w = b.build()

    assert w["assertions"] == []
    assert w["allPassed"] is False, (
        "four rows of AssertionError text serialised as a passing witness")
    assert w["allPassedBasis"] == "error-rows"
    # The reason is written into the file, not only into stderr.
    assert any("qou-qe81" in c for c in w["caveats"])


def test_error_rows_beat_passing_assertions():
    """`paper-six-term-isotope-sweep` is green WITH two passing assertions.

    So the gate cannot be a function of the assertion count — a producer whose
    side-checks pass while its actual rows failed is the harder half of this
    failure, not an easier one.
    """
    b = _builder()
    b.add_assertion("row_count", 6, 6)
    b.add_assertion("mode_count", 3, 3)
    b.add_data("rows", [
        {"atom": "6Li",
         "error": "FileNotFoundError: missing Model B T1 witness"},
    ])
    w = b.build()

    assert all(a["passed"] for a in w["assertions"])
    assert w["allPassed"] is False
    assert w["allPassedBasis"] == "error-rows"


def test_error_row_outside_data_is_caught():
    """Top-level `rows[]`, the shape `wrap_legacy` produces.

    `paper-six-term-isotope-sweep` carries its error rows at TOP level, not
    under `data`, so a gate that only walked `self.data` would miss the
    largest measured offender (30 rows).
    """
    w = WitnessBuilder.wrap_legacy(
        "legacy-error-rows",
        {"computation": "legacy-error-rows",
         "rows": [{"n": 1, "error": "ValueError: non-finite"}]},
        script_path=SCRIPT,
    ).build()

    assert w["allPassed"] is False
    assert w["allPassedBasis"] == "error-rows"


def test_gate_reruns_over_save_extra(tmp_path):
    """`save(extra=…)` merges AFTER `build()`, so the gate runs again there."""
    b = WitnessBuilder("save-extra-error-rows", engine="python",
                       output_dir=tmp_path, _script_path=SCRIPT)
    b.add_assertion("sane", 1, 1)
    out = b.save(extra={"rows": [{"error": "TypeError: no supported conversion"}]})

    written = json.loads(pathlib.Path(out).read_text(encoding="utf-8"))
    assert written["allPassed"] is False
    assert written["allPassedBasis"] == "error-rows"


def test_dotted_exception_name_is_caught():
    w = _builder().add_data(
        "rows", [{"error": "json.JSONDecodeError: Expecting value: line 1"}]
    ).build()
    assert w["allPassed"] is False


# ── and does not bite what it must not ──────────────────────────────────


def test_numeric_error_field_stays_green():
    """`error` also means "the numerical error is". Measured, 5 witnesses.

    `mass-from-q-symbolic` -> `.data.proton.volumes[0].error = 9.98e-13`;
    `qbeta-ck-local-taylor-around-u0-probe` -> a 50-digit decimal STRING;
    `m-p-spectral-corrected-50dps` -> a dict of error components.  If any of
    these went red the gate would be a corpus-wide false alarm, which is how a
    checker gets turned off.
    """
    b = _builder()
    b.add_assertion("volume", "2.029883212819", "2.029883212819")
    b.add_data("proton", {"volumes": [{"n": 0, "error": 9.975853476618112e-13}]})
    b.add_data("c_2_gate", {
        "error": "0.70624086598312472751184406713152191233971302314357"})
    b.add_data("spectral", {"error": {"leading_pct": 2.96, "full_ppm": -130.16}})
    w = b.build()

    assert w["allPassed"] is True
    assert w["allPassedBasis"] == "assertions"
    assert "caveats" not in w


def test_prose_mentioning_an_exception_stays_green():
    """A description is not a recorded failure."""
    b = _builder()
    b.add_assertion("ok", 1, 1)
    b.add_data("note", "raises ValueError: non-Laurent factor when q is a root")
    b.add_data("rows", [{"detail": "TypeError: only if numpy is absent"}])
    w = b.build()

    assert w["allPassed"] is True


def test_expect_errors_declaration_keeps_the_verdict():
    """`producer-importability-audit` collects 13 ModuleNotFoundErrors as its
    RESULT. The opt-out is a declaration IN the witness, not an env var."""
    b = _builder()
    b.expect_errors("this audit's payload IS the collected import failures")
    b.add_assertion("producers_scanned", 812, 812)
    b.add_data("findings", {"optional-dep": [
        {"script": "x.py", "error": "ModuleNotFoundError: No module named 'snappy'"},
    ]})
    w = b.build()

    assert w["allPassed"] is True
    assert w["expectErrors"]
    assert w["allPassedBasis"] == "assertions"


def test_expect_errors_needs_a_reason():
    with pytest.raises(ValueError):
        _builder().expect_errors("   ")


# ── allPassedBasis: the vacuous-green discriminator ─────────────────────


def test_vacuous_green_is_labelled_not_flipped():
    """359 of 2522 witnesses are green over `assertions: []`.

    The verdict is deliberately NOT flipped — see the module docstring. What
    changes is that the state is now sayable: a consumer reading only
    `allPassed` could not tell earned green from vacuous green, and one
    reading `allPassedBasis` can.
    """
    w = _builder().add_data("rows", [{"atom": "D", "B_MeV": "2.224"}]).build()

    assert w["assertions"] == []
    assert w["allPassed"] is True
    assert w["allPassedBasis"] == "vacuous"


def test_earned_green_is_labelled():
    w = _builder().add_assertion("x", 1, 1).build()
    assert w["allPassed"] is True
    assert w["allPassedBasis"] == "assertions"


def test_failed_assertion_is_labelled():
    w = _builder().add_assertion("x", 1, 2).build()
    assert w["allPassed"] is False
    assert w["allPassedBasis"] == "failed-assertions"


def test_basis_is_declared_in_the_json_schema():
    """A field the schema does not know about is a field consumers cannot rely
    on. `durationMsBaseline` set this precedent for the same class of fix."""
    schema = json.loads(
        (ROOT / "schemas" / "witness-schema" / "schema" / "witness.schema.json")
        .read_text(encoding="utf-8"))
    props = schema["properties"]
    assert set(props["allPassedBasis"]["enum"]) == {
        "assertions", "vacuous", "failed-assertions", "error-rows"}
    assert "expectErrors" in props
