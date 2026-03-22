"""Shared configuration constants for the QOU pipeline.

All repository paths, chapter metadata, LaTeX-to-Lean mappings, and
GitHub metadata used by multiple scripts are defined here.
"""

import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CHAPTERS_DIR = REPO_ROOT / "chapters"
LEAN_DIR = REPO_ROOT / "lean-archive"
SCHEMA_PATH = REPO_ROOT / "schemas" / "proof-objects.schema.json"
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
DEFAULT_MANIFEST = REPO_ROOT / "proof-objects.json"

# ---------------------------------------------------------------------------
# GitHub / publishing
# ---------------------------------------------------------------------------

GITHUB_REPO = "litlfred/qou"
GH_PAGES_BASE = "https://litlfred.github.io/qou"
DEFAULT_PDF_URL = f"{GH_PAGES_BASE}/quantum-observable-universe.pdf"

# ---------------------------------------------------------------------------
# Chapter metadata
# ---------------------------------------------------------------------------

# Chapter file order (matches main.tex \input order).
CHAPTER_FILES = [
    "quantum-observable-universe.tex",
    "qou-elaboration.tex",
    "path-integrals-and-braiding.tex",
    "lifting-of-quantum-torsion.tex",
    "brings-surface.tex",
    "descartes-universe.tex",
    "p-adic-quantum-groups.tex",
    "gauge-field-fluid-dynamics.tex",
    "information-theory.tex",
    "interpretations.tex",
    "experimental-evidence.tex",
    "speculations.tex",
]

# Map chapter number to Lean file (relative to lean/).
CHAPTER_LEAN_FILES = {
    1: "QOU/QuantumObservableUniverse.lean",
    2: "QOU/Elaboration.lean",
    3: "QOU/PathIntegrals.lean",
    4: "QOU/Torsion.lean",
    5: "QOU/BringsSurface.lean",
    6: "QOU/DescartesUniverse.lean",
    7: "QOU/PAdicQuantumGroups.lean",
    8: "QOU/GaugeFieldFluidDynamics.lean",
    9: "QOU/InformationTheory.lean",
}

# Chapter titles for display (e.g. in dependency graph).
CHAPTER_TITLES = {
    1: "Ch.1 Quantum Observable Universe",
    2: "Ch.2 Categorical & Analytic Foundations",
    3: "Ch.3 Path Integrals and Braiding",
    4: "Ch.4 Lifting of Quantum Torsion",
    5: "Ch.5 Bring's Surface",
    6: "Ch.6 The Descartes Universe",
    7: "Ch.7 p-Adic Quantum Groups",
    8: "Ch.8 Gauge Field Fluid Dynamics",
    9: "Ch.9 Information Theory",
    10: "Ch.10 Interpretations",
    11: "Ch.11 Experimental Evidence",
    12: "Ch.12 Speculations",
}

# ---------------------------------------------------------------------------
# LaTeX environment ↔ proof-object type mapping
# ---------------------------------------------------------------------------

# Map from LaTeX environment name to object_type in the schema.
ENV_TYPES = {
    "theorem": "theorem",
    "lemma": "lemma",
    "proposition": "proposition",
    "corollary": "corollary",
    "definition": "definition",
    "example": "example",
    "remark": "remark",
    "conjecture": "conjecture",
}

# Map object_type to Lean keyword.
LEAN_KEYWORDS = {
    "theorem": "theorem",
    "lemma": "lemma",
    "proposition": "theorem",  # Lean doesn't have proposition keyword
    "corollary": "theorem",
    "definition": "def",
    "conjecture": "theorem",  # conjectures become theorems with sorry
}

# Short prefixes for display labels.
TYPE_PREFIX = {
    "definition": "Def",
    "theorem": "Thm",
    "lemma": "Lem",
    "proposition": "Prop",
    "corollary": "Cor",
    "conjecture": "Conj",
    "example": "Ex",
    "remark": "Rem",
}

# ---------------------------------------------------------------------------
# LaTeX regex patterns
# ---------------------------------------------------------------------------

# Matches \begin{theorem}, \begin{lemma}[title], etc.
BEGIN_RE = re.compile(
    r"\\begin\{(" + "|".join(ENV_TYPES.keys()) + r")\}(?:\[([^\]]*)\])?"
)
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
LEAN_RE = re.compile(r"\\lean\{([^}]+)\}")
USES_RE = re.compile(r"\\uses\{([^}]+)\}")
LEANOK_RE = re.compile(r"\\leanok\b")

# Maximum lines to scan within a LaTeX environment body.
MAX_ENV_SCAN_LINES = 50

# Keys to preserve when merging Lean linkage data from existing records.
LEAN_MERGE_KEYS = ("url", "file", "sorry_free", "mathlib_links")

# ---------------------------------------------------------------------------
# Review / agent configuration
# ---------------------------------------------------------------------------

VALID_VERDICTS = {"APPROVE", "REQUEST_CHANGES", "NEEDS_DISCUSSION"}
REQUIRED_REVIEW_SECTIONS = ["Summary", "Issues Found", "Suggestions", "Verdict"]

# ---------------------------------------------------------------------------
# Ontologist / Formalizer paths
# ---------------------------------------------------------------------------

DEFAULT_GLOSSARY = REPO_ROOT / "glossary.json"
DEFAULT_MAPPING = REPO_ROOT / "mapping.json"
GLOSSARY_LEAN = LEAN_DIR / "QOU" / "Glossary.lean"

# Tactic mapping: narrative phrases → Lean tactics (used by formalizer).
NARRATIVE_TACTIC_MAP = {
    "by calculation": ("ring", ["field_simp", "polyrith"]),
    "clearly follows from": ("aesop", ["linarith", "omega"]),
    "by the universal property": ("exact Limits.IsLimit.lift", ["exact Limits.IsLimit.hom_ext"]),
    "diagram commutes": ("aesop_cat", ["slice_lhs 1 2 => { simp [Category.assoc] }"]),
    "naturality": ("aesop_cat", ["slice_lhs 1 2 => { rw [NatTrans.naturality] }"]),
    "by contradiction": ("by_contra", ["exfalso"]),
    "by definition": ("rfl", ["unfold", "simp only"]),
}
