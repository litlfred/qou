"""Unit tests for `scripts/lean-kg-detangler.py` and `scripts/lean-best-practices-lint.py`."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent


def _load_script(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS_DIR / filename)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


detangler = _load_script("lean_kg_detangler", "lean-kg-detangler.py")
linter = _load_script("lean_best_practices_lint", "lean-best-practices-lint.py")


def test_strip_comments_and_strings_nested_and_line_preserving():
    raw = (
        "/- outer\n"
        "   /- nested theorem fake : True := trivial -/\n"
        "   still comment sorry\n"
        "-/\n"
        "def msg : String := \"sorry import QOU.Fake 1.234\"\n"
        "-- inline sorry comment\n"
        "theorem real_thm : 1 = 1 := rfl\n"
    )
    stripped = detangler.strip_comments_and_strings(raw)
    assert stripped.count("\n") == raw.count("\n")
    assert "sorry" not in stripped
    assert "QOU.Fake" not in stripped
    assert "1.234" not in stripped
    assert "theorem real_thm" in stripped


def test_parse_header_imports_ignores_docstring_imports_and_detects_order():
    good_src = (
        "/- Copyright (c) 2026 litlfred. Apache 2.0 -/\n"
        "import Mathlib.Algebra.Ring.Basic\n"
        "import QOU.Core.Basic\n\n"
        "/-!\n"
        "# Example\n"
        "Docstring quoting:\n"
        "import QOU.FakeCycle\n"
        "-/\n\n"
        "theorem ok : 1 = 1 := rfl\n"
    )
    imps, order_ok, has_doc, has_copy = detangler.parse_header_imports_and_doc_order(good_src)
    assert imps == ["Mathlib.Algebra.Ring.Basic", "QOU.Core.Basic"]
    assert order_ok is True
    assert has_doc is True
    assert has_copy is True

    bad_src = (
        "/-! # Bad Lean 4.24 order -/\n"
        "import Mathlib.Algebra.Ring.Basic\n"
    )
    imps2, order_ok2, has_doc2, has_copy2 = detangler.parse_header_imports_and_doc_order(bad_src)
    assert imps2 == ["Mathlib.Algebra.Ring.Basic"]
    assert order_ok2 is False
    assert has_doc2 is True
    assert has_copy2 is False


def test_tarjan_scc_cycles_and_dag():
    nodes = ["A", "B", "C", "D"]
    adj = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A", "D"],
        "D": [],
    }
    sccs = detangler.tarjan_scc(nodes, adj)
    nontrivial = [c for c in sccs if len(c) > 1]
    assert nontrivial == [["A", "B", "C"]]


def test_ring_regime_and_intrinsic_purity():
    pure_gen = "theorem sq_expand {R : Type*} [CommRing R] (x : R) : (x + 1) * (x - 1) = x * x - 1 := by ring"
    assert detangler.classify_ring_regime(pure_gen, False) == "pure_generic"
    assert detangler.classify_intrinsic_purity(pure_gen, "QOU.MathlibExt.SqExpand") == ("pure_math", [])

    grat_real = "theorem bad_real (q : ℝ) : (q + 1) - 1 = q := by ring"
    assert detangler.classify_ring_regime(grat_real, False) == "gratuitous_real_candidate"

    just_real = "noncomputable def f (q : ℝ) : ℝ := Real.sqrt (q ^ 2 + 1)"
    assert detangler.classify_ring_regime(just_real, False) == "archimedean_real"

    mixed = "theorem a {R : Type*} [CommRing R] (x : R) : x = x := rfl\ndef b (y : ℝ) : ℝ := y"
    assert detangler.classify_ring_regime(mixed, False) == "mixed_generic_and_real"

    emp_code = "def proton_mev : ℝ := 938.272"
    purity, reasons = detangler.classify_intrinsic_purity(emp_code, "QOU.Mass.Proton")
    assert purity == "qou_empirical_comparison"
    assert "decimal_literal" in reasons


def test_detangler_mini_corpus_cut_edges_and_orphans(tmp_path: Path):
    qou_root = tmp_path / "quantum-observable-universe"
    lean_root = qou_root / "lean"
    (lean_root / "QOU" / "MathlibExt").mkdir(parents=True)
    (lean_root / "QOU" / "LiftingDescent").mkdir(parents=True)
    (lean_root / "QOU" / "Mass").mkdir(parents=True)
    (qou_root / "braids-and-knots").mkdir(parents=True)

    # Root aggregator imports SweedlerFrobenius and ProtonMass, leaving PLDeltaMove orphaned from QOU.lean
    (lean_root / "QOU.lean").write_text(
        "import QOU.LiftingDescent.SweedlerFrobenius\n"
        "import QOU.Mass.ProtonMass\n",
        encoding="utf-8",
    )

    # Pure cone-clean Tier-B candidate
    (lean_root / "QOU" / "LiftingDescent" / "SweedlerFrobenius.lean").write_text(
        "import Mathlib.Algebra.Ring.Basic\n/-! # Sweedler -/\n"
        "theorem sweedler_dim {R : Type*} [CommRing R] (x : R) : x + 0 = x := by simp\n",
        encoding="utf-8",
    )

    # QOU physics module
    (lean_root / "QOU" / "Mass" / "ProtonMass.lean").write_text(
        "import Mathlib.Data.Real.Basic\n/-! # Proton -/\n"
        "def protonMass : ℝ := 938.272\n",
        encoding="utf-8",
    )

    # Pure Tier-B candidate with a cut-edge importing ProtonMass
    (lean_root / "QOU" / "MathlibExt" / "PLDeltaMove.lean").write_text(
        "import QOU.Mass.ProtonMass\n/-! # PL Delta Move -/\n"
        "def plStep (n : Nat) : Nat := n + 1\n",
        encoding="utf-8",
    )

    # Content-block sibling + .ts manifest referencing PLDeltaMove
    (qou_root / "braids-and-knots" / "delta-move.ts").write_text(
        'export default definition({ label: "def:delta", lean: { ref: "qou:QOU.MathlibExt.PLDeltaMove.plStep" } });\n',
        encoding="utf-8",
    )
    (qou_root / "braids-and-knots" / "delta-move.lean").write_text(
        "import QOU.MathlibExt.PLDeltaMove\n/-! # Sibling -/\n"
        "theorem step_zero : plStep 0 = 1 := rfl\n",
        encoding="utf-8",
    )

    report = detangler.analyze_corpus(qou_root)
    assert report["process_gate_status"]["Task_Declare"]["unassigned_library_modules"] == 0
    assert report["process_gate_status"]["GW_Detangled"]["unassigned_resolved_edges"] == 0
    assert report["corpus_totals"]["qou_library_modules_excluding_root_and_scratch"] == 3
    assert report["corpus_totals"]["content_block_sibling_lean_files"] == 1
    assert report["root_reachability_and_orphans"]["orphaned_from_qou_lean_count"] == 1
    cuts = report["tier_a_and_tier_b_reservoir_packages"]["community_to_qou_cut_edges"]
    assert len(cuts) == 1
    assert cuts[0]["src_module"] == "QOU.MathlibExt.PLDeltaMove"
    assert cuts[0]["dst_module"] == "QOU.Mass.ProtonMass"


def test_linter_clean_gold_standard_reservoir_module(tmp_path: Path):
    f = tmp_path / "TwistedFrobenius.lean"
    f.write_text(
        "/- Copyright (c) 2026 litlfred. Released under Apache 2.0 license. -/\n"
        "import Mathlib.Algebra.Ring.Defs\n\n"
        "/-!\n"
        "# Twisted Frobenius Pairing\n"
        "-/\n\n"
        "set_option autoImplicit false\n\n"
        "namespace TwistedFrobeniusHopf\n\n"
        "/-- A Nakayama-twisted pairing carrier. -/\n"
        "structure TwistedPairing (R : Type*) [CommRing R] where\n"
        "  traceVal : R\n\n"
        "/-- Identity on traceVal. -/\n"
        "theorem trace_val_add_zero {R : Type*} [CommRing R] (p : TwistedPairing R) :\n"
        "    p.traceVal + 0 = p.traceVal := by\n"
        "  simp\n\n"
        "end TwistedFrobeniusHopf\n",
        encoding="utf-8",
    )
    findings = linter.lint_file(
        f,
        detangler_mod=detangler,
        community_mode=True,
        community_partition="TierB.TwistedFrobeniusHopf",
        allowed_community_modules=set(),
        strict_zero_qou_prefix=True,
    )
    assert findings == []


def test_linter_catches_all_defect_classes(tmp_path: Path):
    bad = tmp_path / "folio" / "quantum-observable-universe" / "lean" / "QOU" / "BrandNewSynonymDir" / "Bad.lean"
    bad.parent.mkdir(parents=True)
    bad.write_text(
        "/-! # Doc before imports (BP002a) -/\n"
        "import Mathlib\n"
        "import QOU.Mass.ProtonMass\n\n"
        "set_option autoImplicit true\n\n"
        "structure bad_camel where\n"
        "  holds : True\n"
        "  claim_foo : 1 = 1\n\n"
        "theorem BadUpperName (d : bad_camel) (q : ℝ) : True := trivial\n\n"
        "theorem self_proj (d : bad_camel) : 1 = 1 := d.claim_foo\n\n"
        "theorem refl_taut (x : Nat) : x = x := rfl\n\n"
        "def emp_const : Float := 1.1097\n\n"
        "axiom mystery_ax : 1 = 2\n\n"
        "theorem uses_nd : 2 + 2 = 4 := by native_decide\n\n"
        "theorem has_sorry : 1 = 1 := by\n"
        "  sorry\n",
        encoding="utf-8",
    )
    # Patch REPO_ROOT resolution temporarily via relative check or direct call
    orig_root = linter.REPO_ROOT
    linter.REPO_ROOT = tmp_path
    try:
        findings = linter.lint_file(
            bad,
            detangler_mod=detangler,
            community_mode=True,
            community_partition="TierB.HeckeTemperleyLieb",
            allowed_community_modules=set(),
            is_newly_added_in_diff=True,
        )
    finally:
        linter.REPO_ROOT = orig_root

    rules = {f.rule for f in findings}
    assert "BP001" in rules    # autoImplicit true + missing false
    assert "BP002a" in rules   # doc before import
    assert "BP002c" in rules   # missing copyright
    assert "BP002d" in rules   # missing decl docstring
    assert "BP003a" in rules   # umbrella import Mathlib
    assert "BP004a" in rules   # structure bad_camel
    assert "BP004b" in rules   # theorem BadUpperName
    assert "BP006a" in rules   # decimal literal 1.1097
    assert "BP006b" in rules   # Float
    assert "BP007a" in rules   # : True field and : True conclusion
    assert "BP007b" in rules   # self_proj & refl_taut
    assert "BP007c" in rules   # axiom, native_decide, sorry
    assert "BP008" in rules    # forbidden upward import QOU.Mass.ProtonMass
    assert "BP009" in rules    # unapproved BrandNewSynonymDir
