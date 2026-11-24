#!/usr/bin/env python3
"""lean-best-practices-lint.py — Mathlib4 & Lean Reservoir Best-Practices Hygiene Linter.

Implements Stage 1b / Stage 2 (`qou-lskl` + `qou-mlib`, Epic `qou-lnkg`) static style,
generality, vacuity, and import-boundary gates across QOU and its Tier-A / Tier-B
community contribution candidates (`MathlibExt`, `HeckeTemperleyLieb`, `TwistedFrobeniusHopf`,
`ToricConicOpt`, `CompactQuantumMetrics`, `QCalculus`, `BraidKnotOctonion`).

Modes:
  1. `--diff [<base-ref>]`: lints changed/added `.lean` files on the current branch vs `origin/main`
     (plus uncommitted staged/unstaged `.lean` files), blocking new synonym directories (`BP009`),
     import-order bugs (`BP002a`), vacuity (`BP007`), umbrella imports (`BP003a`), and upward leaks (`BP008`).
  2. `--package <NameOrDir>`: lints a named Reservoir candidate package (`HeckeTemperleyLieb`,
     `TwistedFrobeniusHopf`, `ToricConicOpt`, `CompactQuantumMetrics`, `QCalculus`,
     `BraidKnotOctonion`, `MathlibExt`, or `all-community`) or an explicit directory path.
  3. Positional `<file.lean> [...]`: lints explicit `.lean` files.

Rule Catalog:
  - BP001 (`auto_implicit`)         : `set_option autoImplicit false` compliance; ban `autoImplicit true`
  - BP002 (`headers_and_docstrings`): imports-first (Lean 4.24+), `/-! ... -/` module docs, copyright, `/-- ... -/`
  - BP003 (`minimal_imports`)       : ban bare `import Mathlib` / `import QOU`; flag broad `import Mathlib.Tactic`
  - BP004 (`naming_conventions`)    : `UpperCamelCase` structures/classes/inductives; `snake_case` theorems/lemmas
  - BP005 (`generality_7c`)         : §7c gratuitous `: ℝ` vs `[CommRing R]`/`[Field R]`, mixed-wall, `Category.{v}`
  - BP006 (`zero_empirical`)        : zero decimal literals / `Float` / CODATA / `substrate_q` in community & pre-wall
  - BP007 (`zero_vacuity`)          : zero `: True`, self-assuming projection, `X - X = 0`, `native_decide`, uncited `sorry`
  - BP008 (`zero_qou_imports`)      : zero forbidden `QOU.*` upward imports inside community `lean_lib` candidates
  - BP009 (`no_synonym_dir_sprawl`) : block creating new ad-hoc subdirectories under `lean/QOU/`

CPU-hygiene compliant: single-threaded deterministic Python, < 5s across all community candidates.
"""

from __future__ import annotations

import argparse
import functools
import importlib.util
import json
import re
import subprocess
import sys
import time
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR / "lib"))

import lean_decl_scan as lds  # noqa: E402


def _load_detangler():
    spec = importlib.util.spec_from_file_location(
        "lean_kg_detangler", SCRIPTS_DIR / "lean-kg-detangler.py"
    )
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["lean_kg_detangler"] = mod
    spec.loader.exec_module(mod)
    return mod


SEVERITY_ORDER = {"critical": 3, "major": 2, "minor": 1, "info": 0}

COMMUNITY_TOP_DIRS: frozenset[str] = frozenset({
    "MathlibExt",
    "HeckeTemperleyLieb",
    "TwistedFrobeniusHopf",
    "ToricConicOpt",
    "CompactQuantumMetrics",
    "QCalculus",
    "BraidKnotOctonion",
})

PRE_WALL_CHAPTERS = {
    "quantum-universes",
    "quantum-observable-universes",
    "lifting-and-descent",
    "braids-and-knots",
    "brings-surface",
    "knots-particles-confinement",
    "eightfold-way",
}

COMMUNITY_PACKAGE_ALIASES: dict[str, str] = {
    "mathlibext": "TierA.MathlibExt",
    "tiera.mathlibext": "TierA.MathlibExt",
    "hecketemperleylieb": "TierB.HeckeTemperleyLieb",
    "tierb.hecketemperleylieb": "TierB.HeckeTemperleyLieb",
    "twistedfrobeniushopf": "TierB.TwistedFrobeniusHopf",
    "tierb.twistedfrobeniushopf": "TierB.TwistedFrobeniusHopf",
    "toricconicopt": "TierB.ToricConicOpt",
    "tierb.toricconicopt": "TierB.ToricConicOpt",
    "compactquantummetrics": "TierB.CompactQuantumMetrics",
    "tierb.compactquantummetrics": "TierB.CompactQuantumMetrics",
    "qcalculus": "TierB.QCalculus",
    "tierb.qcalculus": "TierB.QCalculus",
    "braidknotoctonion": "TierB.BraidKnotOctonion",
    "tierb.braidknotoctonion": "TierB.BraidKnotOctonion",
}

# Frozen set of existing QOU/* dirs (plus the 12 canonical target names) so BP009 blocks 84th+ synonym sprawl
APPROVED_OR_LEGACY_QOU_DIRS: frozenset[str] = frozenset({
    # Canonical 12 QOU.* subgraph target folder names
    "Core", "LiftingDescent", "BraidsAndKnots", "BringsSurface", "Confinement",
    "EightfoldWay", "MassTheory", "Nuclear", "StandardModel", "FluidDynamics",
    "InformationTheory", "Observations", "Contrib",
    # Existing 83 legacy folders on origin/main (frozen against further sprawl)
    "AlgebraicSubstrate", "AlphaEM", "AppendixQValues", "AppendixSurreals",
    "Archimedean", "ArchimedeanUniverse", "AtomicMass", "BaryonWeight",
    "BraidKnot", "Braiding", "BraidsKnots", "Brings", "CategoricalReeb",
    "Common", "CommutativeQOU", "Conjectures", "Descent", "Eightfold",
    "Encounter", "Excitation", "Experimental", "FeynmanPathIntegrals",
    "FlavorDressing", "FormalGroups", "FrobeniusHopfData",
    "GaugeFieldFluidDynamics", "Geometry", "Habiro", "HadronicMass",
    "Hecke", "HeckeAlgebra", "HyperellipticQuintic", "Information", "Infra",
    "Interactions", "IwahoriHecke", "KZ", "Knot", "KnotTheory", "Knots",
    "Machinery", "MagicShell", "Mass", "MassEndomorphism", "Mathlib",
    "MathlibExt", "MathlibInfra", "Molecular", "OneDim", "Optimization",
    "OptionE", "OrientedSkein", "ParticleInteractions", "ProofHygiene",
    "QBeta", "QFTMath", "QGeometricLanglands", "QuantumBloch",
    "QuantumComputationalUniversality", "QuantumObservableUniverse",
    "QuantumObservableUniverses", "QuantumUniverse", "QuarkState",
    "Resurgence", "RiemannSurface", "SchurWeyl", "Shared",
    "ShellCondensation", "Substrate", "TopologicalMass", "Torsion",
    "TransferMatrices", "WedderburnMass",
})

CONCLUSION_TRUE_RE = re.compile(r":\s*True\s*$")
TRUE_FIELD_RE = re.compile(r"^\s+[A-Za-z_][A-Za-z0-9_']*\s*:\s*(?:True\b|Prop\s*:=\s*True\b)", re.M)
SELF_PROJECTION_PROOF_RE = re.compile(
    r"^\s*(?:by\s+exact\s+|exact\s+)?[A-Za-z_][A-Za-z0-9_']*\."
    r"(?:claim_[A-Za-z0-9_']*|exists_[A-Za-z0-9_']*|[A-Za-z0-9_']*_holds|holds|result|main_claim)\s*$"
)
SUB_ZERO_TAUTOLOGY_RE = re.compile(
    r"-\s*\([^)]+\)\s*=\s*0\s*$", re.S
)
REFL_EQ_RE = re.compile(r":\s*([^\n:=]+?)\s*=\s*\1\s*$")
MONOMORPHIC_CAT_RE = re.compile(r"\(\s*[A-Za-z_][A-Za-z0-9_']*\s*:\s*Type\s*\)\s*\[Category\b(?!\.\{)")
NATIVE_DECIDE_RE = re.compile(r"\bnative_decide\b")
FLOAT_TYPE_RE = re.compile(r"\bFloat\b")
IND_DECL_RE = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*inductive\s+([A-Za-z_][A-Za-z0-9_'.]*)",
    re.M,
)


@dataclass(frozen=True)
class Finding:
    rule: str
    severity: str
    path: str
    line: int
    declaration: str
    message: str


@functools.lru_cache(maxsize=512)
def _dir_has_lakefile_auto_implicit_false(dir_path: Path, root: Path) -> bool:
    cur = dir_path
    while True:
        lf = cur / "lakefile.toml"
        if lf.is_file():
            txt = lf.read_text(encoding="utf-8", errors="replace")
            if re.search(r"^\s*autoImplicit\s*=\s*false\b", txt, re.M):
                return True
        if cur == root or cur.parent == cur:
            break
        cur = cur.parent
    return False


def _has_enclosing_lakefile_auto_implicit_false(file_path: Path) -> bool:
    return _dir_has_lakefile_auto_implicit_false(file_path.resolve().parent, REPO_ROOT.resolve())


def lint_file(
    file_path: Path,
    *,
    detangler_mod: Any,
    community_mode: bool = False,
    community_partition: str | None = None,
    allowed_community_modules: set[str] | None = None,
    strict_zero_qou_prefix: bool = False,
    is_newly_added_in_diff: bool = False,
    preloaded_raw: str | None = None,
    preloaded_code: str | None = None,
) -> list[Finding]:
    findings: list[Finding] = []
    abs_path = file_path.resolve()
    try:
        rel_path = abs_path.relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError:
        rel_path = file_path.as_posix()

    raw = preloaded_raw if preloaded_raw is not None else abs_path.read_text(encoding="utf-8", errors="replace")
    raw_lines = raw.splitlines()
    code = preloaded_code if preloaded_code is not None else detangler_mod.strip_comments_and_strings(raw)
    blanked = code

    imports, import_order_ok, has_mod_doc, has_copyright = (
        detangler_mod.parse_header_imports_and_doc_order(raw)
    )

    # Determine whether file is inside a pre-wall chapter or an isolated community lean_lib dir
    is_pre_wall_sibling = False
    in_isolated_comm_dir = False
    parts = Path(rel_path).parts
    if len(parts) >= 3 and parts[0] == "folio" and parts[1] == "quantum-observable-universe":
        if parts[2] in PRE_WALL_CHAPTERS:
            is_pre_wall_sibling = True
        elif len(parts) >= 4 and parts[2] == "lean":
            top_entry = parts[3].removesuffix(".lean")
            if top_entry in COMMUNITY_TOP_DIRS:
                in_isolated_comm_dir = True
                strict_zero_qou_prefix = True
                if not community_partition:
                    community_partition = (
                        "TierA.MathlibExt" if top_entry == "MathlibExt" else f"TierB.{top_entry}"
                    )

    # BP009: Block new ad-hoc synonym directories under folio/quantum-observable-universe/lean/QOU/
    # and unapproved top-level directories under folio/quantum-observable-universe/lean/
    if (
        len(parts) >= 6
        and parts[:4] == ("folio", "quantum-observable-universe", "lean", "QOU")
        and is_newly_added_in_diff
    ):
        subdir = parts[4]
        if subdir not in APPROVED_OR_LEGACY_QOU_DIRS:
            findings.append(Finding(
                rule="BP009",
                severity="critical",
                path=rel_path,
                line=1,
                declaration="<directory>",
                message=(
                    f"New unapproved QOU subdirectory 'QOU/{subdir}/' violates anti-sprawl gate; "
                    f"place modules into one of the 12 canonical subgraphs or Tier-A/B targets."
                ),
            ))
    elif (
        len(parts) >= 5
        and parts[:3] == ("folio", "quantum-observable-universe", "lean")
        and parts[3] not in ("QOU", ".lake", "blocks-shadow")
        and parts[3] not in COMMUNITY_TOP_DIRS
        and is_newly_added_in_diff
    ):
        findings.append(Finding(
            rule="BP009",
            severity="critical",
            path=rel_path,
            line=1,
            declaration="<directory>",
            message=(
                f"New unapproved top-level directory 'lean/{parts[3]}/'; allowed top-level "
                f"lean_lib roots are QOU and {sorted(COMMUNITY_TOP_DIRS)}."
            ),
        ))

    # BP001: autoImplicit compliance
    m_true = detangler_mod.AUTO_IMPLICIT_TRUE_RE.search(code)
    if m_true:
        ln = code[:m_true.start()].count("\n") + 1
        findings.append(Finding(
            rule="BP001",
            severity="critical",
            path=rel_path,
            line=ln,
            declaration="<file>",
            message="`set_option autoImplicit true` is forbidden; bind all type/ring variables explicitly.",
        ))

    has_inline_auto_false = bool(detangler_mod.AUTO_IMPLICIT_FALSE_RE.search(code))
    in_lean_pkg_dir = "/lean/" in f"/{rel_path}"
    has_lake_auto_false = _has_enclosing_lakefile_auto_implicit_false(abs_path) if in_lean_pkg_dir else False
    if community_mode and not has_inline_auto_false:
        findings.append(Finding(
            rule="BP001",
            severity="minor" if has_lake_auto_false else "major",
            path=rel_path,
            line=1,
            declaration="<file>",
            message=(
                "Community/Reservoir candidate lacks explicit `set_option autoImplicit false` "
                "(add inline so standalone extraction stays protected outside QOU's lakefile)."
            ),
        ))
    elif not in_lean_pkg_dir and not has_inline_auto_false and not has_lake_auto_false:
        # Content-block sibling verified via `lean`-direct outside `lean/`
        findings.append(Finding(
            rule="BP001",
            severity="minor",
            path=rel_path,
            line=1,
            declaration="<file>",
            message="Standalone sibling `.lean` lacks explicit `set_option autoImplicit false`.",
        ))

    # BP002: Header & docstring order/completeness
    if not import_order_ok:
        findings.append(Finding(
            rule="BP002a",
            severity="critical",
            path=rel_path,
            line=1,
            declaration="<header>",
            message="Lean 4.24+ parse error: `/-! ... -/` module docstring appears before `import` statements.",
        ))
    if not has_mod_doc:
        findings.append(Finding(
            rule="BP002b",
            severity="major" if community_mode else "minor",
            path=rel_path,
            line=1,
            declaration="<header>",
            message="Missing `/-! ... -/` module docstring summarizing main declarations and references.",
        ))
    if community_mode and not has_copyright:
        findings.append(Finding(
            rule="BP002c",
            severity="minor",
            path=rel_path,
            line=1,
            declaration="<header>",
            message="Missing Mathlib4/Reservoir `/- Copyright (c) ... Apache 2.0 ... -/` header.",
        ))

    # BP003 & BP008: Import hygiene & zero forbidden `QOU.*` upward imports
    # Scan comment-stripped `blanked` lines without `.strip()` so indented docstring examples
    # (e.g. `GroundRingCore.lean:18`) are never mistaken for header `import` statements.
    for idx, code_ln in enumerate(blanked.splitlines(), 1):
        m_imp = detangler_mod.IMPORT_LINE_RE.match(code_ln)
        if not m_imp:
            continue
        imp = m_imp.group(1)
        if imp in ("Mathlib", "QOU"):
            findings.append(Finding(
                rule="BP003a",
                severity="critical",
                path=rel_path,
                line=idx,
                declaration=f"import {imp}",
                message=f"Umbrella `import {imp}` is forbidden; import targeted submodules only.",
            ))
        elif imp == "Mathlib.Tactic":
            findings.append(Finding(
                rule="BP003b",
                severity="major" if community_mode else "minor",
                path=rel_path,
                line=idx,
                declaration="import Mathlib.Tactic",
                message="Broad `import Mathlib.Tactic` pulls ~3,000 modules; prefer targeted `Mathlib.Tactic.<Name>`.",
            ))

        if (community_mode or in_isolated_comm_dir) and (imp == "QOU" or imp.startswith("QOU.")):
            if strict_zero_qou_prefix or in_isolated_comm_dir:
                findings.append(Finding(
                    rule="BP008",
                    severity="critical",
                    path=rel_path,
                    line=idx,
                    declaration=f"import {imp}",
                    message=f"Isolated Reservoir `lean_lib` must have ZERO `QOU.*` imports (found `{imp}`).",
                ))
            elif allowed_community_modules is not None and imp not in allowed_community_modules:
                findings.append(Finding(
                    rule="BP008",
                    severity="critical",
                    path=rel_path,
                    line=idx,
                    declaration=f"import {imp}",
                    message=(
                        f"Forbidden upward import `{imp}` from community candidate "
                        f"({community_partition or 'community'}) into QOU model module."
                    ),
                ))

    # BP005: §7c base-ring generality & universe polymorphism
    has_dec = bool(detangler_mod.DECIMAL_LITERAL_RE.search(code))
    ring_regime = detangler_mod.classify_ring_regime(code, has_dec)
    if ring_regime == "gratuitous_real_candidate" and (community_mode or is_pre_wall_sibling):
        findings.append(Finding(
            rule="BP005a",
            severity="major",
            path=rel_path,
            line=1,
            declaration="<file>",
            message=(
                "§7c generality violation: file specialises to `ℝ` without transcendental/analytic `Real.*` "
                "operations; generalize to `{R : Type*} [CommRing R]`, `[Field R]`, or `[LinearOrderedField R]`."
            ),
        ))
    elif ring_regime == "mixed_generic_and_real" and (community_mode or is_pre_wall_sibling):
        findings.append(Finding(
            rule="BP005b",
            severity="major",
            path=rel_path,
            line=1,
            declaration="<file>",
            message="§7c wall violation: file mixes generic `[CommRing R]` and concrete `ℝ` declarations; split `(R := ℝ)` instantiation.",
        ))

    for m_cat in MONOMORPHIC_CAT_RE.finditer(code):
        ln = code[:m_cat.start()].count("\n") + 1
        findings.append(Finding(
            rule="BP005c",
            severity="minor",
            path=rel_path,
            line=ln,
            declaration="Category",
            message="Monomorphic `(C : Type) [Category C]`; prefer universe-polymorphic `(C : Type u) [Category.{v} C]`.",
        ))

    # BP006: Zero empirical / decimal / Float literals in community or pre-wall modules
    if community_mode or is_pre_wall_sibling:
        code_low = code.lower()
        for m_dec in detangler_mod.DECIMAL_LITERAL_RE.finditer(code):
            ln = code[:m_dec.start()].count("\n") + 1
            findings.append(Finding(
                rule="BP006a",
                severity="critical" if community_mode else "major",
                path=rel_path,
                line=ln,
                declaration=m_dec.group(0),
                message=f"Decimal literal `{m_dec.group(0)}` forbidden in pure/pre-wall Lean; use exact rationals or generic parameters.",
            ))
        for m_flt in FLOAT_TYPE_RE.finditer(code):
            ln = code[:m_flt.start()].count("\n") + 1
            findings.append(Finding(
                rule="BP006b",
                severity="critical",
                path=rel_path,
                line=ln,
                declaration="Float",
                message="IEEE-754 `Float` forbidden in formal proofs; use exact algebraic/rational types.",
            ))
        for m_emp in detangler_mod.EMPIRICAL_LOW_RE.finditer(code_low):
            ln = code_low[:m_emp.start()].count("\n") + 1
            findings.append(Finding(
                rule="BP006c",
                severity="critical" if community_mode else "major",
                path=rel_path,
                line=ln,
                declaration=m_emp.group(0),
                message=f"Empirical/CODATA identifier `{m_emp.group(0)}` forbidden in community/pre-wall module.",
            ))
        if community_mode:
            for m_sub in detangler_mod.SUBSTRATE_PIN_LOW_RE.finditer(code_low):
                ln = code_low[:m_sub.start()].count("\n") + 1
                findings.append(Finding(
                    rule="BP006d",
                    severity="critical",
                    path=rel_path,
                    line=ln,
                    declaration=m_sub.group(0),
                    message=f"QOU substrate pin `{m_sub.group(0)}` forbidden in community library module.",
                ))

    # BP007 (file-level): `: True` carrier fields & `native_decide`
    for m_tf in TRUE_FIELD_RE.finditer(blanked):
        ln = blanked[:m_tf.start()].count("\n") + 1
        findings.append(Finding(
            rule="BP007a",
            severity="critical",
            path=rel_path,
            line=ln,
            declaration="<field>",
            message="Vacuous `: True` (or `Prop := True`) carrier field carries zero mathematical content.",
        ))

    for m_nd in NATIVE_DECIDE_RE.finditer(code):
        ln = code[:m_nd.start()].count("\n") + 1
        findings.append(Finding(
            rule="BP007c",
            severity="critical" if community_mode else "major",
            path=rel_path,
            line=ln,
            declaration="native_decide",
            message="`native_decide` injects `Lean.ofReduceBool` into kernel trust boundary; use `decide` or structural proof.",
        ))

    # Inductive naming check (BP004a)
    for m_ind in IND_DECL_RE.finditer(blanked):
        iname = m_ind.group(1)
        short = iname.split(".")[-1]
        ln = blanked[:m_ind.start()].count("\n") + 1
        if short and not short[0].isupper():
            findings.append(Finding(
                rule="BP004a",
                severity="major" if community_mode else "minor",
                path=rel_path,
                line=ln,
                declaration=iname,
                message=f"Inductive type `{iname}` should use `UpperCamelCase`.",
            ))

    # Per-declaration checks via `scripts/lib/lean_decl_scan.py`
    for kind, dname, line_no, body in lds.decl_spans(blanked):
        short_name = dname.split(".")[-1] if dname else ""
        header_line = raw_lines[line_no - 1] if 1 <= line_no <= len(raw_lines) else ""
        is_private = bool(re.search(r"\bprivate\b", header_line))

        # BP002d: Public declaration docstring check in community mode
        if community_mode and not is_private and kind in ("theorem", "lemma", "def", "structure", "class"):
            doc = lds.docstring_before(raw_lines, line_no)
            if not doc:
                findings.append(Finding(
                    rule="BP002d",
                    severity="minor",
                    path=rel_path,
                    line=line_no,
                    declaration=dname or f"<{kind}>",
                    message=f"Public `{kind} {dname}` lacks `/-- ... -/` declaration docstring (`docBlame`).",
                ))

        # BP004: Mathlib4 naming conventions
        if short_name:
            if kind in ("structure", "class") and not short_name[0].isupper():
                findings.append(Finding(
                    rule="BP004a",
                    severity="major" if community_mode else "minor",
                    path=rel_path,
                    line=line_no,
                    declaration=dname,
                    message=f"`{kind} {dname}` must use `UpperCamelCase`.",
                ))
            elif kind in ("theorem", "lemma") and short_name[0].isupper():
                findings.append(Finding(
                    rule="BP004b",
                    severity="minor",
                    path=rel_path,
                    line=line_no,
                    declaration=dname,
                    message=f"`{kind} {dname}` starts with uppercase; Mathlib4 requires `snake_case` for proofs of `Prop`.",
                ))

        stmt, proof = lds.split_statement(body)
        stmt_clean = stmt.strip()
        proof_clean = proof.strip()

        # BP007a: `: True` conclusion on theorem/lemma/def
        if kind in ("theorem", "lemma", "def", "abbrev") and CONCLUSION_TRUE_RE.search(stmt_clean):
            findings.append(Finding(
                rule="BP007a",
                severity="critical",
                path=rel_path,
                line=line_no,
                declaration=dname or f"<{kind}>",
                message=f"Vacuous `: True` conclusion on `{kind} {dname}`.",
            ))

        # BP007b: Self-assuming field projection or reflexive / sub-zero tautology
        if kind in ("theorem", "lemma"):
            if SELF_PROJECTION_PROOF_RE.match(proof_clean):
                findings.append(Finding(
                    rule="BP007b",
                    severity="critical",
                    path=rel_path,
                    line=line_no,
                    declaration=dname,
                    message=f"Self-assuming conclusion projection (`{proof_clean}`) in `{dname}`.",
                ))
            elif REFL_EQ_RE.search(stmt_clean) and proof_clean in ("rfl", "by rfl"):
                findings.append(Finding(
                    rule="BP007b",
                    severity="critical",
                    path=rel_path,
                    line=line_no,
                    declaration=dname,
                    message=f"Reflexive `x = x` tautology in `{dname}`.",
                ))
            elif SUB_ZERO_TAUTOLOGY_RE.search(stmt_clean) and "dsimp" in proof_clean and (
                "omega" in proof_clean or "ring" in proof_clean
            ):
                findings.append(Finding(
                    rule="BP007b",
                    severity="critical",
                    path=rel_path,
                    line=line_no,
                    declaration=dname,
                    message=f"Definitional-subtraction `X - X = 0` tautology (`sub-zero-tautology`) in `{dname}`.",
                ))

        # BP007c: Custom `axiom` or `sorry`
        if kind == "axiom":
            if community_mode:
                findings.append(Finding(
                    rule="BP007c",
                    severity="critical",
                    path=rel_path,
                    line=line_no,
                    declaration=dname,
                    message=f"Custom `axiom {dname}` is forbidden in Mathlib4/Reservoir community libraries.",
                ))
            else:
                cone = lds.comment_cone(raw_lines, line_no, body.count("\n") + 1)
                if "-- Ref:" not in cone:
                    findings.append(Finding(
                        rule="BP007c",
                        severity="critical",
                        path=rel_path,
                        line=line_no,
                        declaration=dname,
                        message=f"Uncited `axiom {dname}` lacks `-- Ref: [<bibkey>]` justification.",
                    ))

        if detangler_mod.SORRY_TOKEN_RE.search(body):
            if community_mode:
                findings.append(Finding(
                    rule="BP007c",
                    severity="critical",
                    path=rel_path,
                    line=line_no,
                    declaration=dname or f"<{kind}>",
                    message=f"`sorry` in `{kind} {dname}` is forbidden in Reservoir/Mathlib4 community libraries.",
                ))
            elif kind != "class":
                cone = lds.comment_cone(raw_lines, line_no, body.count("\n") + 1)
                if "-- Ref:" not in cone:
                    findings.append(Finding(
                        rule="BP007c",
                        severity="critical",
                        path=rel_path,
                        line=line_no,
                        declaration=dname or f"<{kind}>",
                        message=f"Uncited `sorry` in `{kind} {dname}` (missing `-- Ref: [<bibkey>]`).",
                    ))

    return findings


def _git_diff_lean_files(base_ref: str | None) -> tuple[list[Path], set[Path]]:
    """Return (changed_or_added_lean_files, newly_added_lean_files) vs base_ref + working tree."""
    if base_ref is None:
        mb = subprocess.run(
            ["git", "merge-base", "origin/main", "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        base = mb.stdout.strip() if mb.returncode == 0 and mb.stdout.strip() else "HEAD"
    else:
        base = base_ref

    changed: set[Path] = set()
    added: set[Path] = set()

    for cmd in (
        ["git", "diff", "--name-status", "-M", f"{base}...HEAD", "--", "*.lean"],
        ["git", "diff", "--name-status", "-M", "HEAD", "--", "*.lean"],
        ["git", "ls-files", "--others", "--exclude-standard", "*.lean"],
    ):
        proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
        if proc.returncode != 0:
            continue
        for ln in proc.stdout.splitlines():
            if not ln.strip():
                continue
            if cmd[1] == "ls-files":
                p = REPO_ROOT / ln.strip()
                if p.is_file():
                    changed.add(p.resolve())
                    added.add(p.resolve())
                continue
            cols = ln.split("\t")
            status = cols[0]
            target_rel = cols[-1]
            if status.startswith("D"):
                continue
            p = REPO_ROOT / target_rel
            if p.is_file():
                changed.add(p.resolve())
                if status.startswith("A"):
                    added.add(p.resolve())

    return sorted(changed), added


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="*", type=Path, help="Explicit .lean files to lint")
    ap.add_argument(
        "--diff",
        nargs="?",
        const="__AUTO__",
        default=None,
        metavar="BASE_REF",
        help="Lint changed/added .lean files vs BASE_REF (default: merge-base with origin/main)",
    )
    ap.add_argument(
        "--package",
        default=None,
        metavar="PKG_OR_DIR",
        help=(
            "Lint a Reservoir/Mathlib4 candidate package (`MathlibExt`, `HeckeTemperleyLieb`, "
            "`TwistedFrobeniusHopf`, `ToricConicOpt`, `CompactQuantumMetrics`, `QCalculus`, "
            "`BraidKnotOctonion`, `all-community`) or directory path"
        ),
    )
    ap.add_argument(
        "--strict-isolated",
        action="store_true",
        help="In --package mode, reject ALL `QOU.*` imports (post-Stage-3 isolation check)",
    )
    ap.add_argument(
        "--fail-on",
        choices=["critical", "major", "minor", "none"],
        default=None,
        help="Minimum severity causing non-zero exit (default: `critical` for --diff/files, `none` report-mode for pre-refactor --package unless specified)",
    )
    ap.add_argument("--json-out", type=Path, default=None, help="Write JSON report to path")
    ap.add_argument("--max-print", type=int, default=50, help="Max individual findings printed to stdout")
    args = ap.parse_args(argv)

    t0 = time.monotonic()
    detangler = _load_detangler()

    targets: list[tuple[Path, bool, str | None, bool]] = []
    preloaded_cache: dict[Path, tuple[str, str]] = {}
    allowed_comm_mods: set[str] | None = None

    if args.package:
        key = args.package.strip().lower()
        cand_dir = Path(args.package)
        if cand_dir.is_dir():
            for p in sorted(cand_dir.rglob("*.lean")):
                if ".lake" not in p.parts:
                    targets.append((p, True, cand_dir.name, False))
        else:
            # Resolve package modules via detangler classification
            qou_root = detangler.DEFAULT_QOU_ROOT
            lean_root = qou_root / "lean"
            all_comm_parts = {"TierA.MathlibExt"} | {f"TierB.{x}" for x in detangler.TIER_B_PACKAGES}
            if key == "all-community":
                wanted_parts = all_comm_parts
            elif key in COMMUNITY_PACKAGE_ALIASES:
                wanted_parts = {COMMUNITY_PACKAGE_ALIASES[key]}
            else:
                print(
                    f"lean-best-practices-lint: unknown --package '{args.package}'. "
                    f"Valid: {', '.join(sorted(COMMUNITY_PACKAGE_ALIASES))} or all-community or a directory.",
                    file=sys.stderr,
                )
                return 2

            audit = detangler.analyze_corpus(qou_root)
            mig_map = audit.get("module_migration_map", {})
            allowed_comm_mods = set()
            for mod_name, minfo in sorted(mig_map.items()):
                part = minfo["target_partition"]
                if part in all_comm_parts:
                    allowed_comm_mods.add(mod_name)
                    allowed_comm_mods.add(minfo["new_module"])
                if part in wanted_parts:
                    p = REPO_ROOT / minfo["old_repo_rel_path"]
                    if p.is_file():
                        targets.append((p, True, part, False))
    elif args.diff is not None:
        base = None if args.diff == "__AUTO__" else args.diff
        diff_files, added_files = _git_diff_lean_files(base)
        for p in diff_files:
            targets.append((p, False, None, p in added_files))
    elif args.files:
        for p in args.files:
            if p.is_dir():
                for sub in sorted(p.rglob("*.lean")):
                    if ".lake" not in sub.parts:
                        targets.append((sub, False, None, False))
            elif p.is_file():
                targets.append((p, False, None, False))
            else:
                print(f"lean-best-practices-lint: file not found: {p}", file=sys.stderr)
                return 2
    else:
        ap.print_help()
        return 2

    all_findings: list[Finding] = []
    for p, comm_mode, comm_part, is_added in targets:
        pre = preloaded_cache.get(p)
        all_findings.extend(
            lint_file(
                p,
                detangler_mod=detangler,
                community_mode=comm_mode,
                community_partition=comm_part,
                allowed_community_modules=allowed_comm_mods,
                strict_zero_qou_prefix=args.strict_isolated,
                is_newly_added_in_diff=is_added,
                preloaded_raw=pre[0] if pre else None,
                preloaded_code=pre[1] if pre else None,
            )
        )

    all_findings.sort(
        key=lambda f: (-SEVERITY_ORDER[f.severity], f.path, f.line, f.rule)
    )

    by_sev = Counter(f.severity for f in all_findings)
    by_rule = Counter(f.rule for f in all_findings)
    elapsed = round(time.monotonic() - t0, 3)

    fail_on = args.fail_on
    if fail_on is None:
        fail_on = "none" if args.package else "critical"

    report = {
        "files_checked": len(targets),
        "runtime_seconds": elapsed,
        "mode": (
            f"package:{args.package}"
            if args.package
            else ("diff" if args.diff is not None else "explicit_files")
        ),
        "fail_on": fail_on,
        "severity_counts": dict(sorted(by_sev.items())),
        "rule_counts": dict(sorted(by_rule.items())),
        "findings": [asdict(f) for f in all_findings],
    }

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(
        f"lean-best-practices-lint ({report['mode']}): checked {len(targets)} .lean files in {elapsed}s — "
        f"critical={by_sev['critical']}, major={by_sev['major']}, minor={by_sev['minor']}"
    )
    if by_rule:
        rules_str = ", ".join(f"{r}:{c}" for r, c in sorted(by_rule.items()))
        print(f"  by rule: {rules_str}")
    for f in all_findings[: args.max_print]:
        print(f"  [{f.severity.upper():8s}] {f.rule:6s} {f.path}:{f.line} ({f.declaration}) — {f.message}")
    if len(all_findings) > args.max_print:
        print(f"  ... ({len(all_findings) - args.max_print} additional findings omitted; use --json-out for full list)")

    if fail_on != "none":
        thresh = SEVERITY_ORDER[fail_on]
        if any(SEVERITY_ORDER[f.severity] >= thresh for f in all_findings):
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
