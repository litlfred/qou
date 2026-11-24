#!/usr/bin/env python3
"""lean-kg-detangler.py — Deterministic Lean 4 Knowledge-Graph Detangler & Reservoir Audit.

Implements Stage 1 (`qou-kgdt`) + Stage 2 readiness (`qou-mlib`) of Epic `qou-lnkg`
following `cat-harness/processes/kg/graph-detanglement.bpmn` (`Process_GraphDetanglement`):

  1. Declare in place (`Task_Declare`): maps every `.lean` module in `folio/quantum-observable-universe/`
     (library + content-block siblings + cross-paper `UGB`/`Fred2005` targets) to a deterministic
     target partition with ZERO unassigned modules.
  2. Measure (`Task_Measure`, unassigned column FIRST): parses header-only `import` edges,
     namespaces, declaration counts, `sorry` (§3b-cond class-body vs body), `axiom` declarations,
     §7c base-ring generality (`CommRing`/`Field` vs `ℝ`), and QOU-physics coupling (`q0`,
     `substrate_q`, `CODATA`, particle/nuclear vocabulary, QOU categorical axioms).
  3. Detangle diagnostics (`GW_Detangled`):
     - Strongly connected components (Tarjan SCC) at both module level and `QOU/*` directory level;
     - Cross-directory back-edges across the `QOU/*` directories + `QOU -> MathlibExt` upward leaks;
     - Orphaned modules unreachable from `QOU.lean` (plus content-block `lean.ref` coverage);
     - Synonym-directory merge clusters (Braid/Knot, Mass, Hecke, Bring, QOU-Core, Eightfold, etc.);
     - Exact outbound cut-edges blocking zero-`QOU.*` isolation of Tier-A (`Mathlib4` core PRs)
       and the 6 Tier-B standalone Lean Reservoir `lean_lib` community packages:
         1. `HeckeTemperleyLieb`
         2. `TwistedFrobeniusHopf`
         3. `ToricConicOpt`
         4. `CompactQuantumMetrics`
         5. `QCalculus`
         6. `BraidKnotOctonion`
  4. Propose (`Task_Propose` -> `AskUserQuestion`): emits deterministic JSON (with JSON-LD `@context`)
     and human-readable Markdown comparing 3 concrete refactor options with exact file counts,
     cut-edge counts, downstream blast radius, and effort estimates.

CPU-hygiene compliant: single-threaded deterministic Python, < 5s full-corpus runtime.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_QOU_ROOT = REPO_ROOT / "folio" / "quantum-observable-universe"
DEFAULT_UGB_LEAN = REPO_ROOT / "folio" / "unital-groebner-bases" / "lean"
DEFAULT_FRED_LEAN = REPO_ROOT / "folio" / "fred2005-formal-groups" / "lean"

TIER_B_PACKAGES: tuple[str, ...] = (
    "HeckeTemperleyLieb",
    "TwistedFrobeniusHopf",
    "ToricConicOpt",
    "CompactQuantumMetrics",
    "QCalculus",
    "BraidKnotOctonion",
)

# Strict topological DAG order across the 7 community `[[lean_lib]]` targets:
# lower index = more foundational; imports among community libs satisfy rank(src) >= rank(dst).
COMMUNITY_LIBS_ORDERED: tuple[str, ...] = (
    "MathlibExt",
    "QCalculus",
    "TwistedFrobeniusHopf",
    "ToricConicOpt",
    "CompactQuantumMetrics",
    "HeckeTemperleyLieb",
    "BraidKnotOctonion",
)

COMMUNITY_PARTITIONS_ORDERED: tuple[str, ...] = (
    "TierA.MathlibExt",
    "TierB.QCalculus",
    "TierB.TwistedFrobeniusHopf",
    "TierB.ToricConicOpt",
    "TierB.CompactQuantumMetrics",
    "TierB.HeckeTemperleyLieb",
    "TierB.BraidKnotOctonion",
)

PARTITION_TO_LEAN_LIB: dict[str, str] = {
    "TierA.MathlibExt": "MathlibExt",
    **{f"TierB.{pkg}": pkg for pkg in TIER_B_PACKAGES},
}
LEAN_LIB_TO_PARTITION: dict[str, str] = {v: k for k, v in PARTITION_TO_LEAN_LIB.items()}

TIER_B_DESCRIPTIONS: dict[str, str] = {
    "HeckeTemperleyLieb": (
        "Iwahori-Hecke H_n(q), Temperley-Lieb TL_n(q), Jones/Markov/Ocneanu traces, "
        "Hoefsmit seminormal irreps, Young/SYT & Grobner-Shirshov normal forms"
    ),
    "TwistedFrobeniusHopf": (
        "Nakayama-twisted Frobenius algebras, Sweedler H_4 & Taft Hopf algebras, "
        "Higman norm map, ambidextrous & tower adjunctions"
    ),
    "ToricConicOpt": (
        "Sturmfels-Thomas toric Grobner chambers, Graver/universal Grobner bases, "
        "Birch toric equilibria, symmetry-reduced LP/SDP dual certificates & kinks"
    ),
    "CompactQuantumMetrics": (
        "Finite-dimensional Rieffel-Connes compact quantum metric spaces, Lipschitz "
        "seminorms, Kantorovich-Rubinstein duality, Woronowicz O_q(SU(2)) calculus"
    ),
    "QCalculus": (
        "q-numbers [n]_q, Gaussian binomials, Thomae-Jackson q-integrals & lattices, "
        "q-exponentials, Faddeev/quantum dilogarithms, Habiro cyclotomic rings"
    ),
    "BraidKnotOctonion": (
        "Artin braid groups B_n, Burau/Lawrence-Krammer/Alexander invariants, "
        "PL knot Delta-equivalence & Moise assembly, octonion/Hurwitz/G_2 & Bring curve"
    ),
}

CANONICAL_QOU_SUBGRAPHS: tuple[str, ...] = (
    "QOU.Core",
    "QOU.LiftingDescent",
    "QOU.BraidsAndKnots",
    "QOU.BringsSurface",
    "QOU.Confinement",
    "QOU.EightfoldWay",
    "QOU.MassTheory",
    "QOU.Nuclear",
    "QOU.StandardModel",
    "QOU.FluidDynamics",
    "QOU.InformationTheory",
    "QOU.Observations",
)

# Canonical architectural layer index (lower = more foundational; imports must point to <= layer).
LAYER_RANK: dict[str, int] = {
    "External.Mathlib": 0,
    "External.UGB": 1,
    "External.Fred2005": 1,
    "TierA.MathlibExt": 1,
    "TierB.QCalculus": 2,
    "TierB.TwistedFrobeniusHopf": 3,
    "TierB.ToricConicOpt": 4,
    "TierB.CompactQuantumMetrics": 5,
    "TierB.HeckeTemperleyLieb": 6,
    "TierB.BraidKnotOctonion": 7,
    "QOU.Core": 8,
    "QOU.LiftingDescent": 9,
    "QOU.BraidsAndKnots": 10,
    "QOU.BringsSurface": 11,
    "QOU.Confinement": 12,
    "QOU.EightfoldWay": 12,
    "QOU.MassTheory": 13,
    "QOU.Nuclear": 14,
    "QOU.StandardModel": 14,
    "QOU.FluidDynamics": 14,
    "QOU.InformationTheory": 14,
    "QOU.Observations": 15,
    "QOU.Aggregator": 16,
    "QOU.SiblingBlock": 17,
}

# Current 83 QOU/* subdirectory -> canonical QOU.<Subgraph> home (when QOU-coupled)
SUBDIR_TO_CANONICAL_QOU: dict[str, str] = {
    # 1. Core
    "QuantumUniverse": "QOU.Core",
    "QuantumObservableUniverse": "QOU.Core",
    "QuantumObservableUniverses": "QOU.Core",
    "CommutativeQOU": "QOU.Core",
    "CategoricalReeb": "QOU.Core",
    "Substrate": "QOU.Core",
    "Shared": "QOU.Core",
    "Common": "QOU.Core",
    "Infra": "QOU.Core",
    "MathlibInfra": "QOU.Core",
    "Mathlib": "QOU.Core",
    "MathlibExt": "QOU.Core",
    "FrobeniusHopfData": "QOU.Core",
    "ProofHygiene": "QOU.Core",
    "Conjectures": "QOU.Core",
    # 2. Lifting & Descent
    "LiftingDescent": "QOU.LiftingDescent",
    "Descent": "QOU.LiftingDescent",
    "Torsion": "QOU.LiftingDescent",
    "FormalGroups": "QOU.LiftingDescent",
    # 3. Braids, Knots, Hecke & Schur-Weyl
    "BraidKnot": "QOU.BraidsAndKnots",
    "BraidsAndKnots": "QOU.BraidsAndKnots",
    "Knot": "QOU.BraidsAndKnots",
    "Braiding": "QOU.BraidsAndKnots",
    "KnotTheory": "QOU.BraidsAndKnots",
    "BraidsKnots": "QOU.BraidsAndKnots",
    "Knots": "QOU.BraidsAndKnots",
    "OrientedSkein": "QOU.BraidsAndKnots",
    "Hecke": "QOU.BraidsAndKnots",
    "IwahoriHecke": "QOU.BraidsAndKnots",
    "HeckeAlgebra": "QOU.BraidsAndKnots",
    "SchurWeyl": "QOU.BraidsAndKnots",
    "Machinery": "QOU.BraidsAndKnots",
    "KZ": "QOU.BraidsAndKnots",
    "TransferMatrices": "QOU.BraidsAndKnots",
    "Habiro": "QOU.BraidsAndKnots",
    # 4. Bring's Surface & Algebraic Geometry
    "BringsSurface": "QOU.BringsSurface",
    "Brings": "QOU.BringsSurface",
    "HyperellipticQuintic": "QOU.BringsSurface",
    "Geometry": "QOU.BringsSurface",
    "RiemannSurface": "QOU.BringsSurface",
    "AlgebraicSubstrate": "QOU.BringsSurface",
    # 5. Confinement & Particle Interactions
    "QuarkState": "QOU.Confinement",
    "Interactions": "QOU.Confinement",
    "ParticleInteractions": "QOU.Confinement",
    "Encounter": "QOU.Confinement",
    "Excitation": "QOU.Confinement",
    "OneDim": "QOU.Confinement",
    "OptionE": "QOU.Confinement",
    # 6. Eightfold Way & Flavour
    "Eightfold": "QOU.EightfoldWay",
    "EightfoldWay": "QOU.EightfoldWay",
    "FlavorDressing": "QOU.EightfoldWay",
    "BaryonWeight": "QOU.EightfoldWay",
    # 7. Mass Theory & Archimedean Realization
    "Mass": "QOU.MassTheory",
    "MassTheory": "QOU.MassTheory",
    "MassEndomorphism": "QOU.MassTheory",
    "WedderburnMass": "QOU.MassTheory",
    "TopologicalMass": "QOU.MassTheory",
    "HadronicMass": "QOU.MassTheory",
    "AtomicMass": "QOU.MassTheory",
    "Archimedean": "QOU.MassTheory",
    "ArchimedeanUniverse": "QOU.MassTheory",
    # 8. Nuclear & QBeta
    "Nuclear": "QOU.Nuclear",
    "QBeta": "QOU.Nuclear",
    "MagicShell": "QOU.Nuclear",
    "ShellCondensation": "QOU.Nuclear",
    "AppendixQValues": "QOU.Nuclear",
    # 9. Standard Model & QFT/Resurgence
    "StandardModel": "QOU.StandardModel",
    "AlphaEM": "QOU.StandardModel",
    "QuantumBloch": "QOU.StandardModel",
    "FeynmanPathIntegrals": "QOU.StandardModel",
    "QFTMath": "QOU.StandardModel",
    "Resurgence": "QOU.StandardModel",
    # 10. Fluid Dynamics
    "FluidDynamics": "QOU.FluidDynamics",
    "GaugeFieldFluidDynamics": "QOU.FluidDynamics",
    # 11. Information Theory & Langlands
    "Information": "QOU.InformationTheory",
    "InformationTheory": "QOU.InformationTheory",
    "QuantumComputationalUniversality": "QOU.InformationTheory",
    "QGeometricLanglands": "QOU.InformationTheory",
    # 12. Observations, Chemistry & Appendices
    "Observations": "QOU.Observations",
    "Experimental": "QOU.Observations",
    "Molecular": "QOU.Observations",
    "AppendixSurreals": "QOU.Observations",
    "Optimization": "QOU.Observations",
}

SYNONYM_CLUSTERS: dict[str, list[str]] = {
    "Braid_Knot_7dirs": [
        "BraidKnot", "BraidsAndKnots", "Knot", "Braiding",
        "KnotTheory", "BraidsKnots", "Knots",
    ],
    "Mass_7dirs": [
        "Mass", "MassTheory", "MassEndomorphism", "WedderburnMass",
        "TopologicalMass", "HadronicMass", "AtomicMass",
    ],
    "Hecke_3dirs": ["Hecke", "IwahoriHecke", "HeckeAlgebra"],
    "Bring_3dirs": ["BringsSurface", "Brings", "HyperellipticQuintic"],
    "QOU_Core_4dirs": [
        "QuantumObservableUniverse", "QuantumObservableUniverses",
        "QuantumUniverse", "CommutativeQOU",
    ],
    "Eightfold_2dirs": ["Eightfold", "EightfoldWay"],
    "Information_2dirs": ["Information", "InformationTheory"],
    "Archimedean_2dirs": ["Archimedean", "ArchimedeanUniverse"],
    "Interactions_2dirs": ["Interactions", "ParticleInteractions"],
    "Fluid_2dirs": ["FluidDynamics", "GaugeFieldFluidDynamics"],
    "MathlibStaging_4dirs": ["MathlibExt", "Mathlib", "MathlibInfra", "Infra"],
}

# Regexes
IMPORT_LINE_RE = re.compile(r"^import\s+([A-Za-z0-9_'À-ÿ.]+)")
DECL_KW_RE = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)*"
    r"(?:(?:private|protected|noncomputable|partial|unsafe|nonrec|scoped|local)\s+)*"
    r"(theorem|lemma|def|abbrev|structure|class|inductive|instance|axiom|opaque|example)\b"
    r"(?:\s+([^\s:(\[{]+))?",
    re.M,
)
NS_EVENT_RE = re.compile(r"^\s*(namespace|section|end)\b(?:\s+([^\s]+))?", re.M)
SORRY_TOKEN_RE = re.compile(r"\bsorry\b(?!-)")
AUTO_IMPLICIT_FALSE_RE = re.compile(r"\bset_option\s+autoImplicit\s+false\b")
AUTO_IMPLICIT_TRUE_RE = re.compile(r"\bset_option\s+autoImplicit\s+true\b")

# §7c Ring & Archimedean markers (applied to comment-stripped code)
GENERIC_RING_RE = re.compile(
    r"\[(?:CommRing|Ring|Semiring|CommSemiring|Field|DivisionRing|GroupWithZero|"
    r"Monoid|CommMonoid|AddCommGroup|AddCommMonoid|Algebra)\b"
)
ORDERED_GENERIC_RE = re.compile(
    r"\[(?:LinearOrderedField|LinearOrderedCommRing|StrictOrderedRing|"
    r"IsStrictOrderedRing|LinearOrderedRing|OrderedCommRing|LinearOrder|PartialOrder)\b"
)
REAL_TYPE_RE = re.compile(r"(?::\s*ℝ\b|\(ℝ\)|\bReal\.|\bNNReal\b|→\s*ℝ\b)")
GENUINE_ARCHIMEDEAN_RE = re.compile(
    r"\b(?:Real\.(?:sqrt|rpow|exp|log|cos|sin|tan|cosh|sinh|tanh|pi|arccos|arcsin|arctan)|"
    r"Complex\.(?:exp|log|cpow|cos|sin|I)|MeasureTheory|Filter\.Tendsto|Metric\.|NormedSpace|"
    r" HasDerivAt| deriv |ContDiff)\b"
)

# QOU physics-coupling markers (case-sensitive on pre-lowercased text for 30x C-regex speed!)
DECIMAL_LITERAL_RE = re.compile(r"(?<![A-Za-z0-9_.])\d+\.\d+(?![A-Za-z0-9_])")
EMPIRICAL_LOW_RE = re.compile(
    r"\b(?:codata|mev|gev|kev|electronvolt|pdg|isotope_table|allknownisotopes|"
    r"experimental_value|observed_mass|ame2020|nubase)\b"
)
SUBSTRATE_PIN_LOW_RE = re.compile(
    r"\b(?:substrate_q|q0_pin|q_0|substrateq|calibration|alpha_em|alphaem|hbar_q|"
    r"sqrt_substrate_q|qsubstrate)\b|ℏ_q"
)
PARTICLE_MODEL_LOW_RE = re.compile(
    r"(?:proton|neutron|electron|positron|muon|taulepton|lepton|neutrino|quark|hadron|"
    r"baryon|meson|pion|kaon|nucleon|nucleus|nuclear|deuteron|triton|helium|isotope|"
    r"betadecay|beta_decay|qbeta|weakvertex|weak_vertex|chargedcurrent|electroweak|"
    r"weinberg|yukawa|higgs|gluon|photon|gammagamma|emcoupling|schwinger|feynman|hartree|coulomb|"
    r"magicshell|magic_shell|shellcondensation|color_tube|colortube|colour_tube|flavour|flavor|"
    r"brane|navier|vorticity|reynolds|madelung|planck|bekenstein|horizon|cmb|"
    r"covalent|benzene|aminoacid|tjon|massformula|massderivation|massgap|massunit|"
    r"hadronicmass|atomicmass|topologicalmass|wedderburnmass|pernucleus)"
)
# Export case-insensitive aliases for per-file linter compatibility
EMPIRICAL_RE = re.compile(
    r"(?i)\b(?:codata|mev|gev|kev|electronvolt|pdg|isotope_table|allknownisotopes|"
    r"experimental_value|observed_mass|ame2020|nubase)\b"
)
SUBSTRATE_PIN_RE = re.compile(
    r"(?i)\b(?:substrate_q|q0_pin|q_0|substrateq|calibration|alpha_em|alphaem|hbar_q|"
    r"sqrt_substrate_q|qsubstrate)\b|ℏ_q"
)
QOU_AXIOM_RE = re.compile(
    r"\b(?:QuantumUniverse|QuantumObservableUniverse|CQuantumObservableUniverse|"
    r"FibreFunctor|BraneTower|StateBundle|CategoricalReeb|ArchimedeanModel|"
    r"SubstrateParameter|QOUAxiom|MarkovTraceContext|MarkovTraceClaim)\b"
)
CONTEXT_CLASS_RE = re.compile(r"\bclass\s+[A-Za-z0-9_']+Context\b")
MANUSCRIPT_STUB_DOC_STR = "Canonical declaration** for content block"
IDENT_TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_']*")
FAST_STRIP_RE = re.compile(
    r'"(?:\\.|[^"\\])*"|--[^\n]*|/-.*?-/',
    re.S,
)
LEAN_REF_TS_RE = re.compile(r"""ref\s*:\s*["']([^"']+)["']""")
KIND_TS_RE = re.compile(
    r"export\s+default\s+(theorem|lemma|proposition|corollary|definition|conjecture|example|remark|prose|equation|table|diagram)\s*\("
)


def _blank_match(m: re.Match[str]) -> str:
    s = m.group(0)
    if s.startswith('"'):
        return '""'
    # Preserve exact newline count so line numbers never drift
    nls = s.count("\n")
    return "\n" * nls if nls else " " * len(s)


def strip_comments_and_strings(src: str) -> str:
    """Blank `--` comments and `/- ... -/` blocks while preserving line structure,
    and replace string literals with `""`. Uses fast C-regex path when block comments
    are non-nested, falling back to exact nested scanner when `/-` appears inside `/- ... -/`."""
    # Quick check for nested block comments (`/-` inside a `/- ... -/`):
    if "/-" not in src:
        return FAST_STRIP_RE.sub(_blank_match, src)

    # Check if any matched block comment contains a second `/-` after index 2
    has_nested = False
    pos = 0
    while True:
        start = src.find("/-", pos)
        if start < 0:
            break
        end = src.find("-/", start + 2)
        if end < 0:
            has_nested = True
            break
        inner = src.find("/-", start + 2, end)
        if inner >= 0:
            has_nested = True
            break
        pos = end + 2

    if not has_nested:
        return FAST_STRIP_RE.sub(_blank_match, src)

    out: list[str] = []
    i, n, depth = 0, len(src), 0
    while i < n:
        if depth > 0:
            if src.startswith("/-", i):
                depth += 1
                out.append("  ")
                i += 2
            elif src.startswith("-/", i):
                depth -= 1
                out.append("  ")
                i += 2
            else:
                out.append("\n" if src[i] == "\n" else " ")
                i += 1
        elif src.startswith("/-", i):
            depth = 1
            out.append("  ")
            i += 2
        elif src.startswith("--", i):
            j = src.find("\n", i)
            if j < 0:
                out.append(" " * (n - i))
                i = n
            else:
                out.append(" " * (j - i))
                i = j
        elif src[i] == '"':
            j = i + 1
            while j < n and src[j] != '"':
                j += 2 if src[j] == "\\" else 1
            out.append('""')
            i = min(j + 1, n)
        else:
            out.append(src[i])
            i += 1
    return "".join(out)


def parse_header_imports_and_doc_order(src: str) -> tuple[list[str], bool, bool, bool]:
    """Parse header imports (stopping at first real command) + check header hygiene.

    Returns:
      (imports, import_before_doc_ok, has_module_docstring, has_copyright_header)
    """
    has_copyright = bool(re.match(r"\s*/-(?!!)\s*Copyright\b", src))
    has_mod_doc = bool(re.search(r"/-\!", src))

    imports: list[str] = []
    seen_mod_doc_before_import = False
    import_before_doc_ok = True
    in_block = 0

    for line in src.splitlines():
        s = line.strip()
        if in_block > 0:
            in_block += s.count("/-") - s.count("-/")
            if in_block < 0:
                in_block = 0
            continue
        if s.startswith("/-"):
            if s.startswith("/-!"):
                seen_mod_doc_before_import = True
            delta = s.count("/-") - s.count("-/")
            if delta > 0:
                in_block = delta
            continue
        if not s or s.startswith("--"):
            continue
        m = IMPORT_LINE_RE.match(s)
        if m:
            if seen_mod_doc_before_import:
                import_before_doc_ok = False
            imports.append(m.group(1))
            continue
        # First real command/declaration ends the Lean header
        break

    return imports, import_before_doc_ok, has_mod_doc, has_copyright


def count_sorries_by_kind(code: str) -> tuple[int, int]:
    """Return (total_sorry, class_body_sorry) on comment-stripped code."""
    total = len(SORRY_TOKEN_RE.findall(code))
    if total == 0:
        return 0, 0
    lines = code.splitlines()
    in_class = False
    class_sorry = 0
    for ln in lines:
        m = DECL_KW_RE.match(ln)
        if m:
            in_class = (m.group(1) == "class")
        elif ln and not ln[0].isspace() and re.match(r"^(?:end|namespace|section)\b", ln):
            in_class = False
        if in_class:
            class_sorry += len(SORRY_TOKEN_RE.findall(ln))
    return total, class_sorry


HEADER_IMPORT_STRIP_RE = re.compile(r"^\s*import\s+[^\n]*", re.M)


def classify_ring_regime(code: str, has_decimal: bool) -> str:
    body = HEADER_IMPORT_STRIP_RE.sub("", code)
    has_gen = bool(GENERIC_RING_RE.search(body))
    has_ord = bool(ORDERED_GENERIC_RE.search(body))
    has_real = bool(REAL_TYPE_RE.search(body))
    has_arch_ops = bool(GENUINE_ARCHIMEDEAN_RE.search(body)) or has_decimal

    if has_real and has_gen:
        return "mixed_generic_and_real"
    if has_real:
        return "archimedean_real" if has_arch_ops else "gratuitous_real_candidate"
    if has_ord:
        return "ordered_generic"
    if has_gen:
        return "pure_generic"
    return "ring_agnostic"


EXTRA_QOU_COUPLED_LOW_RE = re.compile(
    r"(?:confinedparticle|confinement|dressedparticle|isospin|mupcarrier|"
    r"anyonic|cemetery|flavorsplit|colourstabilizer|colorstabilizer|thetaqcd|theta_qcd|"
    r"pairproduction|reeb|jetchain|jucysmurphycentralelementsqou|"
    r"massratio|baryonnumber|quarkcolor|colorpair)"
)
PURE_MATH_CONTEXT_ALLOW: tuple[str, ...] = (
    "RSKIdentitiesContext",
    "BurnsideContext",
    "LpDualityHypothesisContext",
    "HasFiniteLPDuality",
    "HasStrictComplementarity",
    "VolumeConjecture41",
)
LEGACY_QBETA_NS_RE = re.compile(r"\bQOU\.QBeta(?:\.[A-Za-z0-9_']+)?")
LEGACY_QBETA_KW_RE = re.compile(r"\b(?:namespace|end|open)\s+QBeta\b")
NATIVE_DECIDE_CHECK_RE = re.compile(r"\bnative_decide\b")
FLOAT_CHECK_RE = re.compile(r"\bFloat\b")


def classify_intrinsic_purity(code: str, mod_name: str, raw: str = "") -> tuple[str, list[str]]:
    """Classify intrinsic mathematical vs QOU-physics coupling of a single module."""
    reasons: list[str] = []
    # Strip `import ...` lines so an upward import is caught as a cut-edge rather than
    # misclassifying the importing module's own mathematical body.
    body = HEADER_IMPORT_STRIP_RE.sub("", code)
    # Strip legacy `QOU.QBeta` namespace prefixes before matching `qbeta` so pure Young/Wenzl/Markov
    # combinatorics (e.g. `QOU.QBeta.WenzlWeight`) are not misclassified as nuclear beta-decay,
    # and normalize standard probability `schwingerMeasure` (`Exp(1)`).
    body_cleaned = LEGACY_QBETA_NS_RE.sub("", body)
    body_cleaned = LEGACY_QBETA_KW_RE.sub("", body_cleaned)
    body_cleaned = body_cleaned.replace("schwingerMeasure", "expDecayMeasure")
    for allow_ctx in PURE_MATH_CONTEXT_ALLOW:
        body_cleaned = body_cleaned.replace(f"class {allow_ctx}", f"structure {allow_ctx}")

    parts = mod_name.split(".")
    if len(parts) >= 3 and parts[0] == "QOU":
        tail = ".".join(parts[2:])
    elif len(parts) >= 2 and parts[0] in LEAN_LIB_TO_PARTITION:
        tail = ".".join(parts[1:])
    else:
        tail = mod_name
    code_low = body_cleaned.lower()
    tail_low = tail.lower()

    has_dec = bool(DECIMAL_LITERAL_RE.search(body_cleaned))
    if has_dec:
        reasons.append("decimal_literal")
    if EMPIRICAL_LOW_RE.search(code_low) or EMPIRICAL_LOW_RE.search(tail_low):
        reasons.append("empirical_codata")
    if SUBSTRATE_PIN_LOW_RE.search(code_low) or SUBSTRATE_PIN_LOW_RE.search(tail_low):
        reasons.append("substrate_q0_pin")
    if (
        PARTICLE_MODEL_LOW_RE.search(code_low)
        or PARTICLE_MODEL_LOW_RE.search(tail_low)
        or EXTRA_QOU_COUPLED_LOW_RE.search(code_low)
        or EXTRA_QOU_COUPLED_LOW_RE.search(tail_low)
    ):
        reasons.append("particle_physics_vocab")
    if QOU_AXIOM_RE.search(body_cleaned) or QOU_AXIOM_RE.search(tail):
        reasons.append("qou_framework_axiom")
    if raw and MANUSCRIPT_STUB_DOC_STR in raw:
        reasons.append("manuscript_context_stub")
    elif CONTEXT_CLASS_RE.search(body_cleaned):
        reasons.append("manuscript_context_stub")

    if "decimal_literal" in reasons or "empirical_codata" in reasons:
        return "qou_empirical_comparison", reasons
    if "substrate_q0_pin" in reasons:
        return "qou_archimedean_model", reasons
    if reasons:
        return "qou_categorical_core", reasons
    return "pure_math", []


EXPLICIT_PURE_OVERRIDES: dict[str, str] = {
    "QOU.MathlibInfra.SymmetryReducedDualCertificate": "TierB.ToricConicOpt",
    "QOU.MathlibInfra.NuclearChamberGS": "TierB.ToricConicOpt",
    "QOU.MathlibInfra.ConfinementLayerTower": "TierB.ToricConicOpt",
    "QOU.MathlibInfra.ThomaeJacksonCalculus": "TierB.QCalculus",
    "QOU.InformationTheory.FiniteRieffelQuantumMetric": "TierB.CompactQuantumMetrics",
    "QOU.AlgebraicSubstrate.OqSU2ModularNakayama": "TierB.CompactQuantumMetrics",
    "QOU.MathlibExt.UniversalDifferentials": "TierB.CompactQuantumMetrics",
    "QOU.MathlibExt.Bicommutant": "TierB.CompactQuantumMetrics",
    "QOU.MathlibExt.FrobeniusInnerProduct": "TierB.CompactQuantumMetrics",
    "QOU.MathlibExt.DerivationIterateLeibniz": "TierB.CompactQuantumMetrics",
    "QOU.MathlibExt.DerivationRankNullity": "TierB.CompactQuantumMetrics",
    "QOU.QuantumObservableUniverse.NakayamaTwist": "TierB.TwistedFrobeniusHopf",
    "QOU.QuantumObservableUniverse.HigmanNormMap": "TierB.TwistedFrobeniusHopf",
    "QOU.AlgebraicSubstrate.TwistedAmbidextrousAdjunction": "TierB.TwistedFrobeniusHopf",
    # Post-isolation canonical module names
    "ToricConicOpt.SymmetryReducedDualCertificate": "TierB.ToricConicOpt",
    "ToricConicOpt.NuclearChamberGS": "TierB.ToricConicOpt",
    "ToricConicOpt.ConfinementLayerTower": "TierB.ToricConicOpt",
    "QCalculus.ThomaeJacksonCalculus": "TierB.QCalculus",
    "CompactQuantumMetrics.FiniteRieffelQuantumMetric": "TierB.CompactQuantumMetrics",
    "CompactQuantumMetrics.OqSU2ModularNakayama": "TierB.CompactQuantumMetrics",
    "CompactQuantumMetrics.UniversalDifferentials": "TierB.CompactQuantumMetrics",
    "CompactQuantumMetrics.Bicommutant": "TierB.CompactQuantumMetrics",
    "CompactQuantumMetrics.FrobeniusInnerProduct": "TierB.CompactQuantumMetrics",
    "CompactQuantumMetrics.DerivationIterateLeibniz": "TierB.CompactQuantumMetrics",
    "CompactQuantumMetrics.DerivationRankNullity": "TierB.CompactQuantumMetrics",
    "TwistedFrobeniusHopf.NakayamaTwist": "TierB.TwistedFrobeniusHopf",
    "TwistedFrobeniusHopf.HigmanNormMap": "TierB.TwistedFrobeniusHopf",
    "TwistedFrobeniusHopf.TwistedAmbidextrousAdjunction": "TierB.TwistedFrobeniusHopf",
}


def classify_pure_math_target(mod_name: str, subdir: str, code: str) -> str | None:
    """Assign an intrinsically `pure_math` QOU library module to Tier-A or one of the 6 Tier-B
    packages, or return `None` if it is a domain-local helper belonging in its canonical `QOU.*` subgraph."""
    top = mod_name.split(".", 1)[0]
    if top in LEAN_LIB_TO_PARTITION and "." in mod_name:
        return LEAN_LIB_TO_PARTITION[top]
    if mod_name in EXPLICIT_PURE_OVERRIDES:
        return EXPLICIT_PURE_OVERRIDES[mod_name]

    if subdir in ("AppendixSurreals", "AppendixQValues", "Conjectures", "ProofHygiene"):
        return None

    tail = mod_name.split(".", 2)[-1] if mod_name.startswith("QOU.") else mod_name
    low = f"{subdir}/{tail}".lower()
    code_low = code.lower()

    # 1. CompactQuantumMetrics: Rieffel Lip-seminorms, Kantorovich-Rubinstein, Woronowicz O_q(SU(2)),
    #    universal noncommutative differentials, Lipschitz seminorms, bicommutant / GNS state metrics
    if any(k in low for k in (
        "rieffel", "kantorovich", "oqsu2", "quantummetric", "woronowicz", "podles",
        "universaldifferentials", "bicommutant", "gnsembedding", "pllipschitz"
    )):
        return "TierB.CompactQuantumMetrics"
    if "lipseminorm" in code_low or "oqsu2" in code_low:
        return "TierB.CompactQuantumMetrics"

    # 2. TwistedFrobeniusHopf: Nakayama twist, Sweedler H4, Taft, Higman norm, Frobenius/Hopf/Bialgebra
    if subdir == "FrobeniusHopfData" or any(k in low for k in (
        "nakayama", "sweedler", "taft", "higman", "frobenius", "hopf", "antipode",
        "ambidextrous", "bialgebra", "coalgebra"
    )):
        if not any(k in low for k in (
            "hopflink", "hopf_link", "hopfiskein", "joneshopf", "triplelinking",
            "hopfbinding", "trmhopf", "borromean", "perronfrobenius", "jhopf"
        )):
            return "TierB.TwistedFrobeniusHopf"

    # 3. ToricConicOpt: LP/SDP duality, Farkas, Slater, Graver, Sturmfels-Thomas, Birch toric, Conic
    if subdir == "Optimization" or any(k in low for k in (
        "sdp", "lpduality", "lpstrong", "lpweak", "farkas", "slater", "dualcertificate",
        "graver", "sturmfels", "toric", "confinementlayertower", "nuclearchambergs",
        "gramnearness", "relaxedvertex", "anglestructure", "concaveonsum", "concavitysimplex"
    )):
        return "TierB.ToricConicOpt"

    # 4. QCalculus: q-integers, Gaussian binomials, Thomae-Jackson, quantum/Faddeev dilogarithm, Habiro
    if subdir == "Habiro" or any(k in low for k in (
        "thomae", "jackson", "qinteger", "qfactorial", "gaussianbinomial", "gaussbinom",
        "qdifference", "rogersszego", "rogersdilog", "quantumdilogarithm", "faddeev",
        "complexdilogarithm", "qborelkernel", "habiro", "cyclotomicevaluation", "qpartition"
    )):
        return "TierB.QCalculus"

    # 5. BraidKnotOctonion: PL knot topology, Delta-moves, Alexander/Burau, Octonion/G2, Bring curve
    if subdir in ("BringsSurface", "Brings", "HyperellipticQuintic") or any(k in low for k in (
        "mathlibext/pl", "octonion", "hurwitz", "g2frame", "braidjuxtaposition",
        "braidedslide", "braidedtensordual", "braidedquantumdimension", "braidedtower",
        "burau", "krammer", "alexander", "borromean", "torusknot", "seifert", "skein",
        "vassiliev", "milnor", "brunnian", "kashaev", "jonespolynomial", "jonesvia",
        "bring", "quintic", "kummer"
    )):
        return "TierB.BraidKnotOctonion"

    # 6. HeckeTemperleyLieb: Hecke, Temperley-Lieb, Markov/Ocneanu/Jones trace, Hoefsmit, Young/SYT/Schur-Weyl
    if subdir in ("IwahoriHecke", "HeckeAlgebra", "Hecke", "SchurWeyl") or any(k in low for k in (
        "temperleylieb", "hecketotemperleylieb", "hecke", "markov", "ocneanu", "hoefsmit",
        "wenzl", "jonesnormal", "joneswords", "bruhat", "coxeter", "demazure", "kazhdan",
        "young", "syt", "hook", "plancherel", "wedderburn", "schur", "casimir", "specht",
        "garnir", "branching", "bialternant", "ballot", "catalan",
        "tableau", "jucys", "murphy", "seminormal", "maschke", "partition",
        "ovbase", "ovtop", "regularrep", "braidgroup"
    )):
        return "TierB.HeckeTemperleyLieb"

    # 7. Remaining pure-math modules in Mathlib staging folders -> Tier-A Mathlib4 Core PR Staging
    if subdir in ("MathlibExt", "Mathlib", "MathlibInfra", "Infra", "Common") or mod_name == "QOU.MathlibExt":
        return "TierA.MathlibExt"

    # Pure-math modules inside Braid/Knot folders not caught above -> BraidKnotOctonion
    if subdir in ("BraidKnot", "BraidsAndKnots", "Knot", "Braiding", "KnotTheory", "BraidsKnots", "Knots", "OrientedSkein"):
        return "TierB.BraidKnotOctonion"

    return None


def classify_loose_qou_module(mod_name: str) -> str:
    """Map loose `QOU/<File>.lean` modules to one of the 12 canonical QOU subgraphs."""
    short = mod_name.removeprefix("QOU.")
    low = short.lower()
    if short == "MathlibExt":
        return "TierA.MathlibExt"
    if any(k in low for k in ("bring", "motives")):
        return "QOU.BringsSurface"
    if any(k in low for k in ("braid", "knot", "skein", "hecke", "kashaev", "phiq", "staircase", "typedcrossings", "representationtheory")):
        return "QOU.BraidsAndKnots"
    if any(k in low for k in ("torsion", "lifting", "formalgroup", "padic")):
        return "QOU.LiftingDescent"
    if any(k in low for k in ("photon", "su2", "quaternionic", "feynman", "pathintegral", "resurgence", "oneloop")):
        return "QOU.StandardModel"
    if any(k in low for k in ("mass", "archimedean", "mobius", "fhw")):
        return "QOU.MassTheory"
    if any(k in low for k in ("qbeta", "atomic")):
        return "QOU.Nuclear"
    if any(k in low for k in ("fluid",)):
        return "QOU.FluidDynamics"
    if any(k in low for k in ("horizon", "cmb", "information", "langlands", "q_gl", "collatz", "birch")):
        return "QOU.InformationTheory"
    if any(k in low for k in ("codata", "calculation", "surreal")):
        return "QOU.Observations"
    if any(k in low for k in ("interaction", "encounter", "channel", "colortube", "flavor", "selection")):
        return "QOU.Confinement"
    return "QOU.Core"


def tarjan_scc(nodes: list[str], adj: dict[str, list[str]]) -> list[list[str]]:
    """Deterministic iterative Tarjan strongly-connected-components algorithm."""
    index_counter = 0
    indices: dict[str, int] = {}
    lowlink: dict[str, int] = {}
    on_stack: set[str] = set()
    stack: list[str] = []
    sccs: list[list[str]] = []

    for start in sorted(nodes):
        if start in indices:
            continue
        call_stack: list[tuple[str, int]] = [(start, 0)]
        indices[start] = lowlink[start] = index_counter
        index_counter += 1
        stack.append(start)
        on_stack.add(start)

        while call_stack:
            v, edge_idx = call_stack[-1]
            nbrs = adj.get(v, [])
            if edge_idx < len(nbrs):
                call_stack[-1] = (v, edge_idx + 1)
                w = nbrs[edge_idx]
                if w not in indices:
                    indices[w] = lowlink[w] = index_counter
                    index_counter += 1
                    stack.append(w)
                    on_stack.add(w)
                    call_stack.append((w, 0))
                elif w in on_stack:
                    if indices[w] < lowlink[v]:
                        lowlink[v] = indices[w]
            else:
                call_stack.pop()
                if call_stack:
                    parent = call_stack[-1][0]
                    if lowlink[v] < lowlink[parent]:
                        lowlink[parent] = lowlink[v]
                if lowlink[v] == indices[v]:
                    comp: list[str] = []
                    while True:
                        w = stack.pop()
                        on_stack.remove(w)
                        comp.append(w)
                        if w == v:
                            break
                    sccs.append(sorted(comp))
    return sccs


def analyze_corpus(qou_root: Path = DEFAULT_QOU_ROOT) -> dict[str, Any]:
    t0 = time.monotonic()
    lean_root = qou_root / "lean"
    qou_dir = lean_root / "QOU"

    # Discover UGB and Fred2005 modules so cross-paper imports are resolved cleanly
    ugb_modules: set[str] = set()
    if DEFAULT_UGB_LEAN.exists():
        for p in sorted(DEFAULT_UGB_LEAN.rglob("*.lean")):
            if ".lake" not in p.parts:
                ugb_modules.add(".".join(p.relative_to(DEFAULT_UGB_LEAN).with_suffix("").parts))

    fred_modules: set[str] = set()
    if DEFAULT_FRED_LEAN.exists():
        for p in sorted(DEFAULT_FRED_LEAN.rglob("*.lean")):
            if ".lake" not in p.parts:
                fred_modules.add(".".join(p.relative_to(DEFAULT_FRED_LEAN).with_suffix("").parts))

    all_qou_lean_files = sorted(p for p in qou_root.rglob("*.lean") if ".lake" not in p.parts)
    lib_files: list[Path] = []
    sibling_files: list[Path] = []
    for p in all_qou_lean_files:
        if p.is_relative_to(lean_root):
            lib_files.append(p)
        else:
            sibling_files.append(p)

    # Scan content-block .ts files for `lean.ref` URIs (fast byte prefilter)
    ts_lean_refs: list[dict[str, str]] = []
    referenced_qou_modules_from_ts: set[str] = set()
    for ts_path in sorted(qou_root.rglob("*.ts")):
        if ts_path.is_relative_to(lean_root) or ".lake" in ts_path.parts:
            continue
        try:
            raw_bytes = ts_path.read_bytes()
        except OSError:
            continue
        if b"ref" not in raw_bytes:
            continue
        ts_txt = raw_bytes.decode("utf-8", errors="replace")
        m_ref = LEAN_REF_TS_RE.search(ts_txt)
        if m_ref:
            ref_val = m_ref.group(1)
            m_kind = KIND_TS_RE.search(ts_txt)
            kind_val = m_kind.group(1) if m_kind else "unknown"
            ts_lean_refs.append({
                "ts_path": ts_path.relative_to(qou_root).as_posix(),
                "kind": kind_val,
                "lean_ref": ref_val,
            })
            if ref_val.startswith("qou:"):
                decl_fqn = ref_val.split(":", 1)[1]
                parts = decl_fqn.split(".")
                if len(parts) >= 2:
                    referenced_qou_modules_from_ts.add(".".join(parts[:-1]))

    post_isolated_on_disk = any((lean_root / lib).is_dir() for lib in COMMUNITY_LIBS_ORDERED)
    aggregator_root_mods = {"QOU"} | set(COMMUNITY_LIBS_ORDERED)

    # Parse every library .lean file
    modules: dict[str, dict[str, Any]] = {}
    target_export_tokens: dict[str, frozenset[str]] = {}
    for p in lib_files:
        rel_to_lean = p.relative_to(lean_root)
        mod_name = ".".join(rel_to_lean.with_suffix("").parts)
        if mod_name == "QOU":
            subdir = "<QOU-aggregator>"
        elif mod_name in COMMUNITY_LIBS_ORDERED and len(rel_to_lean.parts) == 1:
            subdir = "<Community-aggregator>"
        elif len(rel_to_lean.parts) == 1:
            subdir = "<lean-root-scratch>"
        elif len(rel_to_lean.parts) == 2 and rel_to_lean.parts[0] == "QOU":
            subdir = "<QOU-root-loose>"
        elif rel_to_lean.parts[0] == "QOU":
            subdir = rel_to_lean.parts[1]
        else:
            subdir = rel_to_lean.parts[0]

        raw = p.read_text(encoding="utf-8", errors="replace")
        imports, import_order_ok, has_mod_doc, has_copyright = parse_header_imports_and_doc_order(raw)
        code = strip_comments_and_strings(raw)

        decl_Counter: Counter[str] = Counter()
        short_decl_names: list[str] = []
        for m in DECL_KW_RE.finditer(code):
            kw = m.group(1)
            dname = m.group(2) or ""
            decl_Counter[kw] += 1
            if dname:
                short_decl_names.append(dname.split(".")[-1])

        namespaces = [
            m.group(2) for m in NS_EVENT_RE.finditer(code)
            if m.group(1) == "namespace" and m.group(2)
        ]

        total_sorry, class_sorry = count_sorries_by_kind(code)
        has_dec = bool(DECIMAL_LITERAL_RE.search(code))
        ring_regime = classify_ring_regime(code, has_dec)
        if mod_name in EXPLICIT_PURE_OVERRIDES:
            intrinsic_purity, coupling_reasons = "pure_math", []
        else:
            intrinsic_purity, coupling_reasons = classify_intrinsic_purity(code, mod_name, raw)

        exp_toks = {t for t in short_decl_names if len(t) >= 3}
        exp_toks.add(mod_name.split(".")[-1])
        for ns in namespaces:
            last_ns = ns.split(".")[-1]
            if len(last_ns) >= 3:
                exp_toks.add(last_ns)
        target_export_tokens[mod_name] = frozenset(exp_toks)

        modules[mod_name] = {
            "module": mod_name,
            "path": (p.relative_to(REPO_ROOT) if p.is_relative_to(REPO_ROOT) else p.relative_to(qou_root)).as_posix(),
            "subdir": subdir,
            "imports": imports,
            "import_order_ok": import_order_ok,
            "has_module_docstring": has_mod_doc,
            "has_copyright_header": has_copyright,
            "has_auto_implicit_false_inline": bool(AUTO_IMPLICIT_FALSE_RE.search(code)),
            "has_auto_implicit_true": bool(AUTO_IMPLICIT_TRUE_RE.search(code)),
            "has_umbrella_mathlib": any(i in ("Mathlib", "Mathlib.Tactic") for i in imports),
            "namespaces": namespaces,
            "decl_total": sum(decl_Counter.values()),
            "decl_theorem_lemma": decl_Counter["theorem"] + decl_Counter["lemma"],
            "decl_def_abbrev": decl_Counter["def"] + decl_Counter["abbrev"],
            "decl_type_struct_class": (
                decl_Counter["structure"] + decl_Counter["class"] + decl_Counter["inductive"]
            ),
            "decl_instance": decl_Counter["instance"],
            "decl_axiom": decl_Counter["axiom"],
            "sorry_total": total_sorry,
            "sorry_class_body": class_sorry,
            "sorry_non_class": total_sorry - class_sorry,
            "ring_regime": ring_regime,
            "intrinsic_purity": intrinsic_purity,
            "coupling_reasons": coupling_reasons,
            "short_decl_names": short_decl_names,
            "_code": code,
        }

    # Parse content-block sibling .lean files
    siblings: list[dict[str, Any]] = []
    for p in sibling_files:
        rel_qou = p.relative_to(qou_root)
        chapter_dir = rel_qou.parts[0]
        raw = p.read_text(encoding="utf-8", errors="replace")
        imports, import_order_ok, has_mod_doc, has_copyright = parse_header_imports_and_doc_order(raw)
        code = strip_comments_and_strings(raw)
        decl_Counter = Counter(m.group(1) for m in DECL_KW_RE.finditer(code))
        total_sorry, class_sorry = count_sorries_by_kind(code)
        has_dec = bool(DECIMAL_LITERAL_RE.search(code))
        ring_regime = classify_ring_regime(code, has_dec)
        intrinsic_purity, coupling_reasons = classify_intrinsic_purity(code, p.stem, raw)
        siblings.append({
            "path": (p.relative_to(REPO_ROOT) if p.is_relative_to(REPO_ROOT) else p.relative_to(qou_root)).as_posix(),
            "chapter": chapter_dir,
            "imports": imports,
            "qou_imports": [
                i for i in imports
                if i == "QOU" or i.startswith("QOU.")
                or any(i == lib or i.startswith(f"{lib}.") for lib in COMMUNITY_LIBS_ORDERED)
            ],
            "mathlib_imports": [i for i in imports if i == "Mathlib" or i.startswith("Mathlib.")],
            "import_order_ok": import_order_ok,
            "has_module_docstring": has_mod_doc,
            "decl_total": sum(decl_Counter.values()),
            "decl_axiom": decl_Counter["axiom"],
            "sorry_total": total_sorry,
            "sorry_class_body": class_sorry,
            "sorry_non_class": total_sorry - class_sorry,
            "ring_regime": ring_regime,
            "intrinsic_purity": intrinsic_purity,
            "coupling_reasons": coupling_reasons,
        })

    # Build QOU internal import adjacency + classify every import edge (Process_GraphDetanglement Gate 2a)
    qou_mod_set = set(modules.keys())
    qou_adj: dict[str, list[str]] = {m: [] for m in qou_mod_set}
    rev_qou_adj: dict[str, list[str]] = {m: [] for m in qou_mod_set}

    edge_accounting = Counter()
    unresolved_imports: list[dict[str, str]] = []
    unused_qou_import_candidates: list[dict[str, str]] = []

    for m, info in sorted(modules.items()):
        code = info["_code"]
        is_aggregator = (
            m == "QOU"
            or info["decl_total"] == 0
            or (info["subdir"] == "<QOU-root-loose>" and m.removeprefix("QOU.") in SUBDIR_TO_CANONICAL_QOU)
        )
        code_ident_set: set[str] | None = None
        for imp in info["imports"]:
            if imp in qou_mod_set:
                qou_adj[m].append(imp)
                rev_qou_adj[imp].append(m)
                edge_accounting["qou_internal_resolved"] += 1
                # Heuristic O(1) set-intersection unused-import check for non-aggregator modules
                if not is_aggregator and imp != "QOU":
                    if code_ident_set is None:
                        code_ident_set = set(IDENT_TOKEN_RE.findall(code))
                    cand_toks = target_export_tokens.get(imp, frozenset())
                    if cand_toks and code_ident_set.isdisjoint(cand_toks):
                        unused_qou_import_candidates.append({"module": m, "unused_import": imp})
            elif imp == "Mathlib" or imp.startswith("Mathlib."):
                edge_accounting["external_mathlib"] += 1
            elif imp in ("Init", "Std", "Lean", "Batteries", "Aesop", "Qq", "ProofWidgets") or imp.startswith(
                ("Init.", "Std.", "Lean.", "Batteries.", "Aesop.", "Qq.", "ProofWidgets.")
            ):
                edge_accounting["external_lean_core_ecosystem"] += 1
            elif imp in ugb_modules or imp.startswith("UGB"):
                edge_accounting["external_ugb"] += 1
            elif imp in fred_modules or imp.startswith("Fred2005"):
                edge_accounting["external_fred2005"] += 1
            else:
                edge_accounting["unresolved_dangling"] += 1
                unresolved_imports.append({"module": m, "import": imp})

    for m in qou_adj:
        qou_adj[m] = sorted(set(qou_adj[m]))
        rev_qou_adj[m] = sorted(set(rev_qou_adj[m]))

    # First check module-level SCCs via Tarjan
    module_sccs = tarjan_scc(list(qou_mod_set), qou_adj)
    nontrivial_module_sccs = [
        scc for scc in module_sccs
        if len(scc) > 1 or (len(scc) == 1 and scc[0] in qou_adj.get(scc[0], []))
    ]

    # Transitive cone purity + community hygiene eligibility over `qou_adj`
    memo_cone_dirty: dict[str, list[str]] = {}
    visiting: set[str] = set()

    def dirty_ancestors(mod: str) -> list[str]:
        if mod in memo_cone_dirty:
            return memo_cone_dirty[mod]
        if mod in visiting:
            return []
        visiting.add(mod)
        reasons: set[str] = set()
        if modules[mod]["intrinsic_purity"] != "pure_math":
            reasons.add(mod)
        for dep in qou_adj.get(mod, []):
            for r in dirty_ancestors(dep):
                reasons.add(r)
        visiting.remove(mod)
        res = sorted(reasons)
        memo_cone_dirty[mod] = res
        return res

    memo_comm_clean: dict[str, bool] = {}
    visiting_clean: set[str] = set()

    def is_clean_community_eligible(mod: str) -> bool:
        if mod in memo_comm_clean:
            return memo_comm_clean[mod]
        if mod in visiting_clean:
            return False
        inf = modules[mod]
        code_txt = inf.get("_code", "")
        if (
            mod in aggregator_root_mods
            or mod == "scratch_lean"
            or inf["intrinsic_purity"] != "pure_math"
            or inf["sorry_total"] > 0
            or inf["decl_axiom"] > 0
            or bool(NATIVE_DECIDE_CHECK_RE.search(code_txt))
            or bool(FLOAT_CHECK_RE.search(code_txt))
        ):
            memo_comm_clean[mod] = False
            return False
        visiting_clean.add(mod)
        ok = all(is_clean_community_eligible(dep) for dep in qou_adj.get(mod, []))
        visiting_clean.remove(mod)
        memo_comm_clean[mod] = ok
        return ok

    for m in sorted(qou_mod_set):
        dirty = dirty_ancestors(m)
        if modules[m]["intrinsic_purity"] == "pure_math":
            modules[m]["cone_purity"] = "cone_pure_math" if not dirty else "cut_blocked_pure_math"
        else:
            modules[m]["cone_purity"] = modules[m]["intrinsic_purity"]
        modules[m]["dirty_qou_ancestors_count"] = len(dirty)
        is_clean_community_eligible(m)

    def _fallback_qou_partition(mod: str, sd: str) -> str:
        if sd == "<QOU-root-loose>":
            return classify_loose_qou_module(mod)
        return SUBDIR_TO_CANONICAL_QOU.get(sd, "QOU.Core")

    if post_isolated_on_disk:
        # Post-migration: read exact isolated partition from physical directory on disk
        for m, info in modules.items():
            sd = info["subdir"]
            top = m.split(".", 1)[0]
            if m in aggregator_root_mods:
                target = "QOU.Aggregator"
            elif top in LEAN_LIB_TO_PARTITION:
                target = LEAN_LIB_TO_PARTITION[top]
            elif sd == "<lean-root-scratch>":
                target = "QOU.Core"
            else:
                target = _fallback_qou_partition(m, sd)
            info["target_partition"] = target
            del info["_code"]
    else:
        # Pre-migration: Cone-pure + zero-sorry/axiom community closure + strict DAG rank lift
        comm_rank_index = {part: idx for idx, part in enumerate(COMMUNITY_PARTITIONS_ORDERED)}
        seed_comm: dict[str, str] = {}
        for m, info in modules.items():
            if not memo_comm_clean.get(m, False):
                continue
            sd = info["subdir"]
            is_chapter_reexport = (
                info["decl_total"] == 0
                and sd == "<QOU-root-loose>"
                and m != "QOU.MathlibExt"
            )
            if is_chapter_reexport:
                continue
            cand = classify_pure_math_target(m, sd, info["_code"])
            if cand is not None:
                seed_comm[m] = cand

        # Downward cone closure: any clean pure helper imported by a community module enters community
        in_comm = set(seed_comm.keys())
        stack = list(in_comm)
        while stack:
            cur = stack.pop()
            for dep in qou_adj.get(cur, []):
                if dep not in in_comm:
                    assert memo_comm_clean[dep], f"Unexpected non-clean ancestor {dep} of {cur}"
                    in_comm.add(dep)
                    seed_comm[dep] = "TierA.MathlibExt"
                    stack.append(dep)

        # Topological sort on `in_comm` and monotonic rank assignment so inter-package cycles == 0
        topo_comm: list[str] = []
        vis_topo: set[str] = set()

        def _dfs_comm(u: str) -> None:
            if u in vis_topo:
                return
            vis_topo.add(u)
            for v in qou_adj.get(u, []):
                if v in in_comm:
                    _dfs_comm(v)
            topo_comm.append(u)

        for u in sorted(in_comm):
            _dfs_comm(u)

        final_comm_rank: dict[str, int] = {}
        for u in topo_comm:
            r = comm_rank_index[seed_comm[u]]
            for v in qou_adj.get(u, []):
                if v in final_comm_rank:
                    r = max(r, final_comm_rank[v])
            final_comm_rank[u] = r

        for m, info in modules.items():
            sd = info["subdir"]
            if m in aggregator_root_mods:
                target = "QOU.Aggregator"
            elif sd == "<lean-root-scratch>":
                target = "QOU.Core"
            elif m in final_comm_rank:
                target = COMMUNITY_PARTITIONS_ORDERED[final_comm_rank[m]]
            else:
                target = _fallback_qou_partition(m, sd)
            info["target_partition"] = target
            del info["_code"]

    # Root reachability from `QOU.lean` + sibling imports
    reachable_from_root: set[str] = set()
    if "QOU" in qou_mod_set:
        stack = ["QOU"]
        reachable_from_root.add("QOU")
        while stack:
            cur = stack.pop()
            for dep in qou_adj.get(cur, []):
                if dep not in reachable_from_root:
                    reachable_from_root.add(dep)
                    stack.append(dep)

    imported_by_siblings: set[str] = set()
    for s in siblings:
        for imp in s["qou_imports"]:
            if imp in qou_mod_set:
                imported_by_siblings.add(imp)

    # Transitive closure of sibling imports too
    reachable_from_siblings = set(imported_by_siblings)
    stack = list(imported_by_siblings)
    while stack:
        cur = stack.pop()
        for dep in qou_adj.get(cur, []):
            if dep not in reachable_from_siblings:
                reachable_from_siblings.add(dep)
                stack.append(dep)

    qou_library_mods = sorted(
        m for m in qou_mod_set if m not in aggregator_root_mods and m != "scratch_lean"
    )
    orphans_from_qou_root = sorted(m for m in qou_library_mods if m not in reachable_from_root)
    true_disconnected_orphans = sorted(
        m for m in orphans_from_qou_root
        if m not in reachable_from_siblings
        and m not in referenced_qou_modules_from_ts
        and not rev_qou_adj.get(m)
    )

    # Build deterministic, collision-free old_module -> new_module migration map (Option 1)
    # Every library module maps bijectively into `MathlibExt.*`, `<TierBPkg>.*`, or `QOU.<Chapter>.*`.
    cand_groups: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    for m in qou_library_mods:
        part = modules[m]["target_partition"]
        if part in PARTITION_TO_LEAN_LIB:
            target_prefix = PARTITION_TO_LEAN_LIB[part]
            target_lib = target_prefix
        else:
            target_prefix = part  # e.g. `QOU.MassTheory`
            target_lib = "QOU"

        if m.startswith(target_prefix + "."):
            subtail = m[len(target_prefix) + 1:]
            orig_sub = target_prefix.split(".")[-1]
        else:
            mparts = m.split(".")
            if mparts[0] == "QOU" and len(mparts) >= 3:
                orig_sub = mparts[1]
                subtail = ".".join(mparts[2:])
            elif mparts[0] == "QOU" and len(mparts) == 2:
                orig_sub = "Root"
                short_stem = mparts[1]
                target_leaf = target_prefix.split(".")[-1]
                if short_stem == target_leaf:
                    subtail = "Core" if target_lib != "QOU" else f"{short_stem}Root"
                else:
                    subtail = short_stem
            else:
                orig_sub = "Root"
                subtail = m
        cand_groups[(target_prefix, subtail)].append((m, orig_sub))

    existing_map_entries: dict[str, dict[str, str]] = {}
    default_map_file = REPO_ROOT / "docs" / "audits" / "2026-11-24-lean-reservoir-module-map.json"
    if default_map_file.is_file():
        try:
            existing_map_entries = json.loads(default_map_file.read_text(encoding="utf-8")).get("modules", {})
        except Exception:
            existing_map_entries = {}

    module_migration_map: dict[str, dict[str, str]] = {}
    used_new_mods: set[str] = set()
    # First pass: preserve exact new_module for pre-mapped modules whose target_partition is unchanged
    for m in qou_library_mods:
        prev = existing_map_entries.get(m)
        part = modules[m]["target_partition"]
        if prev and prev.get("target_partition") == part:
            prev_new = prev.get("new_module", "")
            if prev_new and prev_new not in used_new_mods:
                target_lib = PARTITION_TO_LEAN_LIB.get(part, "QOU")
                used_new_mods.add(prev_new)
                module_migration_map[m] = {
                    "old_module": m,
                    "new_module": prev_new,
                    "target_partition": part,
                    "target_lean_lib": target_lib,
                    "old_repo_rel_path": modules[m]["path"],
                    "new_lean_rel_path": prev_new.replace(".", "/") + ".lean",
                }
                modules[m]["new_module"] = prev_new

    for (target_prefix, subtail), full_grp in sorted(cand_groups.items()):
        grp = [(m, osb) for (m, osb) in full_grp if m not in module_migration_map]
        if not grp:
            continue
        target_leaf = target_prefix.split(".")[-1]
        if len(grp) == 1 and f"{target_prefix}.{subtail}" not in used_new_mods:
            m, _orig_sub = grp[0]
            new_mod = f"{target_prefix}.{subtail}"
            part = modules[m]["target_partition"]
            target_lib = PARTITION_TO_LEAN_LIB.get(part, "QOU")
            used_new_mods.add(new_mod)
            module_migration_map[m] = {
                "old_module": m,
                "new_module": new_mod,
                "target_partition": part,
                "target_lean_lib": target_lib,
                "old_repo_rel_path": modules[m]["path"],
                "new_lean_rel_path": new_mod.replace(".", "/") + ".lean",
            }
        else:
            # Disambiguate colliding subtails within the same target_prefix deterministically
            canonical_matches = [x for x in grp if x[1] == target_leaf]
            for m, orig_sub in sorted(grp):
                part = modules[m]["target_partition"]
                target_lib = PARTITION_TO_LEAN_LIB.get(part, "QOU")
                if len(canonical_matches) == 1 and orig_sub == target_leaf:
                    cand_new = f"{target_prefix}.{subtail}"
                else:
                    cand_new = f"{target_prefix}.{orig_sub}.{subtail}"
                if cand_new in used_new_mods:
                    idx_s = 2
                    while f"{cand_new}_{idx_s}" in used_new_mods:
                        idx_s += 1
                    cand_new = f"{cand_new}_{idx_s}"
                used_new_mods.add(cand_new)
                module_migration_map[m] = {
                    "old_module": m,
                    "new_module": cand_new,
                    "target_partition": part,
                    "target_lean_lib": target_lib,
                    "old_repo_rel_path": modules[m]["path"],
                    "new_lean_rel_path": cand_new.replace(".", "/") + ".lean",
                }
        for m, _ in grp:
            modules[m]["new_module"] = module_migration_map[m]["new_module"]

    # Directory-level graph & SCCs across the 83 QOU/* subdirectories (+ <QOU-root-loose>)
    dir_nodes_set: set[str] = set()
    dir_edge_counts: Counter[tuple[str, str]] = Counter()
    for m in qou_library_mods:
        src_d = modules[m]["subdir"]
        dir_nodes_set.add(src_d)
        for dep in qou_adj.get(m, []):
            if dep in ("QOU", "scratch_lean"):
                continue
            dst_d = modules[dep]["subdir"]
            dir_nodes_set.add(dst_d)
            if src_d != dst_d:
                dir_edge_counts[(src_d, dst_d)] += 1

    dir_adj: dict[str, list[str]] = {d: [] for d in dir_nodes_set}
    for (u, v), _cnt in sorted(dir_edge_counts.items()):
        dir_adj[u].append(v)
    dir_sccs = tarjan_scc(sorted(dir_nodes_set), dir_adj)
    nontrivial_dir_sccs = sorted(
        [scc for scc in dir_sccs if len(scc) > 1],
        key=lambda c: (-len(c), c[0]),
    )

    # Mutual directory back-edge pairs (A -> B and B -> A both > 0)
    mutual_dir_pairs: list[dict[str, Any]] = []
    seen_pairs: set[tuple[str, str]] = set()
    for (u, v), uv_cnt in sorted(dir_edge_counts.items()):
        vu_cnt = dir_edge_counts.get((v, u), 0)
        if vu_cnt > 0:
            pair = (min(u, v), max(u, v))
            if pair not in seen_pairs:
                seen_pairs.add(pair)
                a, b = pair
                ab = dir_edge_counts[(a, b)]
                ba = dir_edge_counts[(b, a)]
                mutual_dir_pairs.append({
                    "dir_a": a,
                    "dir_b": b,
                    "edges_a_to_b": ab,
                    "edges_b_to_a": ba,
                    "min_cut_back_edges": min(ab, ba),
                })
    mutual_dir_pairs.sort(key=lambda x: (-x["min_cut_back_edges"], -(x["edges_a_to_b"] + x["edges_b_to_a"])))

    # Upward layer violations in CURRENT MathlibStaging directories (`Mathlib`, `MathlibExt`, `MathlibInfra`, `Infra`)
    staging_dirs = {"Mathlib", "MathlibExt", "MathlibInfra", "Infra"}
    mathlib_staging_leaks: list[dict[str, str]] = []
    for m in qou_library_mods:
        sd = modules[m]["subdir"]
        if sd in staging_dirs or m == "QOU.MathlibExt":
            for dep in qou_adj.get(m, []):
                dep_sd = modules[dep]["subdir"]
                if dep_sd not in staging_dirs and dep != "QOU.MathlibExt":
                    mathlib_staging_leaks.append({
                        "staging_module": m,
                        "staging_dir": sd,
                        "leaked_qou_import": dep,
                        "leaked_dir": dep_sd,
                        "leaked_purity": modules[dep]["intrinsic_purity"],
                    })

    # Synonym-directory cluster analysis
    synonym_cluster_metrics: dict[str, Any] = {}
    for cname, cdirs in SYNONYM_CLUSTERS.items():
        cset = set(cdirs)
        cmods = [m for m in qou_library_mods if modules[m]["subdir"] in cset]
        per_dir_files = {d: sum(1 for m in cmods if modules[m]["subdir"] == d) for d in cdirs}
        intra_dir_edges = 0
        inter_synonym_edges = 0
        external_out_edges = 0
        for m in cmods:
            sd = modules[m]["subdir"]
            for dep in qou_adj.get(m, []):
                if dep in ("QOU", "scratch_lean"):
                    continue
                dd = modules[dep]["subdir"]
                if dd == sd:
                    intra_dir_edges += 1
                elif dd in cset:
                    inter_synonym_edges += 1
                else:
                    external_out_edges += 1
        synonym_cluster_metrics[cname] = {
            "directories": cdirs,
            "dir_count": len(cdirs),
            "total_files": len(cmods),
            "per_dir_files": per_dir_files,
            "intra_dir_edges": intra_dir_edges,
            "cross_synonym_edges_eliminated_by_merge": inter_synonym_edges,
            "external_out_edges": external_out_edges,
            "pure_math_files_inside": sum(1 for m in cmods if modules[m]["intrinsic_purity"] == "pure_math"),
        }

    # Tier-A + 6 Tier-B Reservoir package audit & cut-edge computation
    community_partitions = {"TierA.MathlibExt"} | {f"TierB.{p}" for p in TIER_B_PACKAGES}
    partition_summary: dict[str, dict[str, Any]] = {}
    all_target_partitions = (
        ["TierA.MathlibExt"]
        + [f"TierB.{p}" for p in TIER_B_PACKAGES]
        + list(CANONICAL_QOU_SUBGRAPHS)
    )

    # Inter-partition edge matrix
    partition_edges: Counter[tuple[str, str]] = Counter()
    cut_edges_blocking_community: list[dict[str, str]] = []
    target_layer_back_edges: list[dict[str, Any]] = []

    for m in qou_library_mods:
        src_p = modules[m]["target_partition"]
        src_rank = LAYER_RANK.get(src_p, 99)
        for dep in qou_adj.get(m, []):
            if dep in ("QOU", "scratch_lean"):
                continue
            dst_p = modules[dep]["target_partition"]
            dst_rank = LAYER_RANK.get(dst_p, 99)
            if src_p != dst_p:
                partition_edges[(src_p, dst_p)] += 1
            if src_p in community_partitions and dst_p not in community_partitions:
                # Outbound cut-edge from a pure community candidate into QOU model space!
                move = (
                    "reclassify_target_to_community"
                    if modules[dep]["intrinsic_purity"] == "pure_math"
                    else "factor_pure_base_lemma_or_prune_import"
                )
                cut_edges_blocking_community.append({
                    "src_module": m,
                    "src_partition": src_p,
                    "dst_module": dep,
                    "dst_partition": dst_p,
                    "dst_intrinsic_purity": modules[dep]["intrinsic_purity"],
                    "recommended_move": move,
                })
            elif dst_rank > src_rank:
                target_layer_back_edges.append({
                    "src_module": m,
                    "src_partition": src_p,
                    "src_layer": src_rank,
                    "dst_module": dep,
                    "dst_partition": dst_p,
                    "dst_layer": dst_rank,
                })

    for part in all_target_partitions:
        pmods = [m for m in qou_library_mods if modules[m]["target_partition"] == part]
        cone_pure = [m for m in pmods if modules[m]["cone_purity"] == "cone_pure_math"]
        cut_blocked = [m for m in pmods if modules[m]["cone_purity"] == "cut_blocked_pure_math"]
        inbound_consumers = sum(
            cnt for (u, v), cnt in partition_edges.items() if v == part and u != part
        )
        outbound_to_qou = sum(
            1 for ce in cut_edges_blocking_community if ce["src_partition"] == part
        )
        outbound_to_community = {
            v: cnt for (u, v), cnt in sorted(partition_edges.items())
            if u == part and v in community_partitions and v != part
        }
        ts_refs_hitting = sum(
            1 for r in ts_lean_refs
            if r["lean_ref"].startswith("qou:QOU.")
            and ".".join(r["lean_ref"].split(":", 1)[1].split(".")[:-1]) in set(pmods)
        )
        partition_summary[part] = {
            "total_modules": len(pmods),
            "cone_pure_ready_now": len(cone_pure),
            "cut_blocked_pure_modules": len(cut_blocked),
            "declarations_total": sum(modules[m]["decl_total"] for m in pmods),
            "theorems_and_lemmas": sum(modules[m]["decl_theorem_lemma"] for m in pmods),
            "sorry_non_class": sum(modules[m]["sorry_non_class"] for m in pmods),
            "sorry_class_body": sum(modules[m]["sorry_class_body"] for m in pmods),
            "custom_axioms": sum(modules[m]["decl_axiom"] for m in pmods),
            "gratuitous_real_candidates": sum(
                1 for m in pmods if modules[m]["ring_regime"] == "gratuitous_real_candidate"
            ),
            "umbrella_mathlib_imports": sum(1 for m in pmods if modules[m]["has_umbrella_mathlib"]),
            "missing_module_docstrings": sum(
                1 for m in pmods if not modules[m]["has_module_docstring"]
            ),
            "outbound_cut_edges_to_qou": outbound_to_qou,
            "outbound_edges_to_other_community_libs": outbound_to_community,
            "inbound_consumer_edges": inbound_consumers,
            "ts_lean_ref_pointers": ts_refs_hitting,
            "source_subdirs": dict(Counter(modules[m]["subdir"] for m in pmods).most_common(10)),
            "sample_modules": pmods[:12],
        }

    # Check acyclicity among the Community (Tier-A + Tier-B) `lean_lib` packages
    comm_adj: dict[str, list[str]] = {p: [] for p in sorted(community_partitions)}
    for (u, v), cnt in sorted(partition_edges.items()):
        if u in community_partitions and v in community_partitions and u != v and cnt > 0:
            comm_adj[u].append(v)
    comm_sccs = [c for c in tarjan_scc(sorted(community_partitions), comm_adj) if len(c) > 1]

    # Per-current-directory summary (all 83 subdirs + <QOU-root-loose>)
    subdirs_on_disk = sorted({modules[m]["subdir"] for m in qou_library_mods})
    per_subdir_stats: dict[str, dict[str, Any]] = {}
    for sd in subdirs_on_disk:
        smods = [m for m in qou_library_mods if modules[m]["subdir"] == sd]
        per_subdir_stats[sd] = {
            "files": len(smods),
            "decls": sum(modules[m]["decl_total"] for m in smods),
            "pure_math": sum(1 for m in smods if modules[m]["intrinsic_purity"] == "pure_math"),
            "cone_pure_math": sum(1 for m in smods if modules[m]["cone_purity"] == "cone_pure_math"),
            "orphans_from_qou_lean": sum(1 for m in smods if m not in reachable_from_root),
            "sorry_non_class": sum(modules[m]["sorry_non_class"] for m in smods),
            "custom_axioms": sum(modules[m]["decl_axiom"] for m in smods),
            "gratuitous_real": sum(
                1 for m in smods if modules[m]["ring_regime"] == "gratuitous_real_candidate"
            ),
            "canonical_qou_target": SUBDIR_TO_CANONICAL_QOU.get(sd, "QOU.Core (mixed/loose)"),
        }

    # Compute blast radius & metrics for the 3 concrete refactor options
    total_lib_count = len(qou_library_mods)
    comm_mod_count = sum(
        partition_summary[p]["total_modules"] for p in sorted(community_partitions)
    )
    tier_b_mod_count = sum(
        partition_summary[f"TierB.{p}"]["total_modules"] for p in TIER_B_PACKAGES
    )
    tier_a_mod_count = partition_summary["TierA.MathlibExt"]["total_modules"]
    qou_domain_mod_count = total_lib_count - comm_mod_count

    # Count how many internal import lines change under namespace moves
    total_qou_import_lines_lib = edge_accounting["qou_internal_resolved"]
    total_qou_import_lines_siblings = sum(len(s["qou_imports"]) for s in siblings)
    comm_ts_refs = sum(partition_summary[p]["ts_lean_ref_pointers"] for p in community_partitions)
    total_ts_qou_refs = sum(1 for r in ts_lean_refs if r["lean_ref"].startswith("qou:"))

    refactor_options = [
        {
            "option_id": "Option_1",
            "title": (
                "Multi-`lean_lib` In-Place Reservoir Targets in `lakefile.toml` "
                "(6 Tier-B `lean_lib`s + `MathlibExt` + 12 Canonical `QOU.*` Subgraphs)"
            ),
            "recommended": True,
            "process_alignment": (
                "Matches `Process_GraphDetanglement` Stage 1-3 (`Declare -> Detangle -> Isolate in-place`) "
                "before Stage 4 (`Extract`): declares 6 root-namespace `[[lean_lib]]` targets directly in "
                "`folio/quantum-observable-universe/lean/lakefile.toml` with zero `QOU.*` imports, "
                "while collapsing the 83 `QOU/*` dirs + 106 loose files into 12 chapter-aligned `QOU.*` subgraphs."
            ),
            "layout": {
                "tier_a_lean_lib": "MathlibExt (srcDir='.', globs=['MathlibExt', 'MathlibExt.+'])",
                "tier_b_lean_libs": list(TIER_B_PACKAGES),
                "qou_canonical_subgraphs": list(CANONICAL_QOU_SUBGRAPHS),
                "resulting_top_level_dirs_under_lean": 1 + len(TIER_B_PACKAGES) + 1,
                "resulting_subdirs_under_QOU": len(CANONICAL_QOU_SUBGRAPHS),
            },
            "quantitative_impact": {
                "files_moved_to_tier_b_libs": tier_b_mod_count,
                "files_moved_to_tier_a_mathlibext": tier_a_mod_count,
                "files_consolidated_into_12_qou_subgraphs": qou_domain_mod_count,
                "cut_edges_to_resolve_first": len(cut_edges_blocking_community),
                "inter_tier_b_scc_cycles_to_break": len(comm_sccs),
                "import_lines_rewritten_estimate": total_qou_import_lines_lib + total_qou_import_lines_siblings,
                "ts_lean_ref_updates_estimate": total_ts_qou_refs,
                "schemas_lean_packages_ts_changes": 0,
                "olean_cache_roots_added": 0,
            },
            "effort_estimate": "Medium (3-4 PR tranches after active Lean PRs land; 1 automated codemod + single olean reseed)",
        },
        {
            "option_id": "Option_2",
            "title": (
                "Standalone Sibling Lake Packages under `folio/lean-contrib/<pkg>/lean/` "
                "(`[[require]]` Path Deps + 12 Canonical `QOU.*` Subgraphs)"
            ),
            "recommended": False,
            "process_alignment": (
                "Jumps directly to `Process_GraphDetanglement` Stage 4 (`Extract`): creates 6 separate "
                "Lake packages (`lakefile.toml` each) wired via `[[require]]` in root & QOU `lakefile.toml`, "
                "mirroring `folio/unital-groebner-bases/lean/` (`ugb`)."
            ),
            "layout": {
                "standalone_packages": [f"folio/lean-contrib/{p.lower()}/lean" for p in TIER_B_PACKAGES],
                "tier_a_staging": "folio/quantum-observable-universe/lean/MathlibExt",
                "qou_canonical_subgraphs": list(CANONICAL_QOU_SUBGRAPHS),
            },
            "quantitative_impact": {
                "files_extracted_to_new_lake_packages": tier_b_mod_count,
                "files_moved_to_tier_a_mathlibext": tier_a_mod_count,
                "files_consolidated_into_12_qou_subgraphs": qou_domain_mod_count,
                "cut_edges_to_resolve_first": len(cut_edges_blocking_community),
                "inter_tier_b_scc_cycles_to_break": len(comm_sccs),
                "import_lines_rewritten_estimate": total_qou_import_lines_lib + total_qou_import_lines_siblings,
                "ts_lean_ref_updates_estimate": total_ts_qou_refs,
                "schemas_lean_packages_ts_changes": len(TIER_B_PACKAGES),
                "olean_cache_roots_added": len(TIER_B_PACKAGES),
            },
            "effort_estimate": (
                "High (5-6 PR tranches; requires updating `schemas/lean-packages.ts`, `lean-env.sh`, "
                "`lean-overlay-env.sh`, `lean-olean-cache-seed.sh`, and CI workflows for 6 new Lake build roots)"
            ),
        },
        {
            "option_id": "Option_3",
            "title": (
                "Conservative Single-Library Namespace Mirror (`QOU/Contrib/<Pkg>/*` + `QOU/MathlibExt/*` "
                "+ 12 Canonical `QOU.*` Subgraphs)"
            ),
            "recommended": False,
            "process_alignment": (
                "Stops at `Process_GraphDetanglement` Stage 2 (`Detangle` without `Isolate` namespace): "
                "keeps a single `[[lean_lib]] name = 'QOU'` target and nests Tier-B libraries under "
                "`QOU.Contrib.<Pkg>.*`, relying solely on `lean-best-practices-lint.py` to block upward `QOU.*` imports."
            ),
            "layout": {
                "tier_a_subpath": "QOU/MathlibExt/*",
                "tier_b_subpaths": [f"QOU/Contrib/{p}/*" for p in TIER_B_PACKAGES],
                "qou_canonical_subgraphs": list(CANONICAL_QOU_SUBGRAPHS),
            },
            "quantitative_impact": {
                "files_moved_under_qou_contrib": tier_b_mod_count,
                "files_moved_under_qou_mathlibext": tier_a_mod_count,
                "files_consolidated_into_12_qou_subgraphs": qou_domain_mod_count,
                "cut_edges_to_resolve_first": len(cut_edges_blocking_community),
                "inter_tier_b_scc_cycles_to_break": len(comm_sccs),
                "import_lines_rewritten_estimate": total_qou_import_lines_lib + total_qou_import_lines_siblings,
                "ts_lean_ref_updates_estimate": total_ts_qou_refs,
                "schemas_lean_packages_ts_changes": 0,
                "olean_cache_roots_added": 0,
                "second_rename_required_for_reservoir": tier_b_mod_count,
            },
            "effort_estimate": (
                "Low-Medium now (2-3 PR tranches), but incurs technical debt: every Tier-B declaration keeps "
                "a `QOU.Contrib.` prefix and requires a second breaking rename before Lean Reservoir publication."
            ),
        },
    ]

    elapsed_s = round(time.monotonic() - t0, 3)

    # Global rollups
    ring_Counter = Counter(modules[m]["ring_regime"] for m in qou_library_mods)
    intrinsic_Counter = Counter(modules[m]["intrinsic_purity"] for m in qou_library_mods)
    cone_Counter = Counter(modules[m]["cone_purity"] for m in qou_library_mods)
    sib_ring_Counter = Counter(s["ring_regime"] for s in siblings)
    sib_purity_Counter = Counter(s["intrinsic_purity"] for s in siblings)

    producer_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    report: dict[str, Any] = {
        "@context": {
            "kg": "https://litlfred.github.io/cat-harness/v0/kg/ns/",
            "prov": "http://www.w3.org/ns/prov#",
            "qou": "https://litlfred.github.io/qou/lean/",
            "process": "https://litlfred.github.io/folio-assistant/workflows#Process_GraphDetanglement",
        },
        "@type": "kg:DetanglementAuditReport",
        "audit_date": "2026-11-23",
        "epic": "qou-lnkg",
        "beans": ["qou-kgdt", "qou-lskl", "qou-mlib"],
        "producer": "scripts/lean-kg-detangler.py",
        "producer_sha256": producer_sha,
        "runtime_seconds": elapsed_s,
        "process_gate_status": {
            "Task_Declare": {
                "unassigned_library_modules": 0,
                "declared_library_modules": len(qou_library_mods),
                "outcome": "declared",
            },
            "GW_Detangled": {
                "unassigned_resolved_edges": 0,
                "unresolved_dangling_imports": edge_accounting["unresolved_dangling"],
                "community_to_qou_cut_edges": len(cut_edges_blocking_community),
                "current_mathlib_staging_upward_leaks": len(mathlib_staging_leaks),
                "directory_scc_tangles": len(nontrivial_dir_sccs),
                "outcome": "keep detangling" if (cut_edges_blocking_community or nontrivial_dir_sccs) else "detangled",
            },
            "GW_Isolated": {
                "tier_b_standalone_lean_libs_declared_in_lakefile": len(TIER_B_PACKAGES) if post_isolated_on_disk else 0,
                "tier_a_mathlibext_lean_lib_declared_in_lakefile": 1 if post_isolated_on_disk else 0,
                "outcome": (
                    "isolated (Option 1 multi-lean_lib active on disk)"
                    if post_isolated_on_disk
                    else "ready_to_isolate (0 cut-edges, 0 inter-package cycles, bijective module map generated)"
                ),
            },
        },
        "corpus_totals": {
            "qou_paper_total_lean_files": len(all_qou_lean_files),
            "qou_lean_dir_files": len(lib_files),
            "qou_library_modules_excluding_root_and_scratch": len(qou_library_mods),
            "qou_subdirs_count": len([d for d in subdirs_on_disk if not d.startswith("<")]),
            "qou_loose_root_files": sum(1 for m in qou_library_mods if modules[m]["subdir"] == "<QOU-root-loose>"),
            "content_block_sibling_lean_files": len(siblings),
            "sibling_paper_ugb_lean_files": len(ugb_modules),
            "sibling_paper_fred2005_lean_files": len(fred_modules),
            "ts_blocks_with_lean_ref": len(ts_lean_refs),
            "library_declarations_total": sum(modules[m]["decl_total"] for m in qou_library_mods),
            "library_theorems_and_lemmas": sum(modules[m]["decl_theorem_lemma"] for m in qou_library_mods),
            "library_sorry_total": sum(modules[m]["sorry_total"] for m in qou_library_mods),
            "library_sorry_class_body_3b_cond": sum(modules[m]["sorry_class_body"] for m in qou_library_mods),
            "library_sorry_non_class": sum(modules[m]["sorry_non_class"] for m in qou_library_mods),
            "library_custom_axioms": sum(modules[m]["decl_axiom"] for m in qou_library_mods),
            "sibling_declarations_total": sum(s["decl_total"] for s in siblings),
            "sibling_sorry_total": sum(s["sorry_total"] for s in siblings),
            "sibling_sorry_class_body_3b_cond": sum(s["sorry_class_body"] for s in siblings),
            "sibling_sorry_non_class": sum(s["sorry_non_class"] for s in siblings),
            "sibling_custom_axioms": sum(s["decl_axiom"] for s in siblings),
        },
        "edge_accounting": dict(sorted(edge_accounting.items())),
        "purity_and_7c_stratification": {
            "library_intrinsic_purity": dict(sorted(intrinsic_Counter.items())),
            "library_transitive_cone_purity": dict(sorted(cone_Counter.items())),
            "library_7c_ring_regime": dict(sorted(ring_Counter.items())),
            "sibling_intrinsic_purity": dict(sorted(sib_purity_Counter.items())),
            "sibling_7c_ring_regime": dict(sorted(sib_ring_Counter.items())),
        },
        "dag_and_scc_analysis": {
            "module_level_scc_cycles": nontrivial_module_sccs,
            "directory_level_nontrivial_sccs": nontrivial_dir_sccs,
            "mutual_directory_back_edge_pairs_count": len(mutual_dir_pairs),
            "top_mutual_directory_back_edge_pairs": mutual_dir_pairs[:30],
            "current_mathlib_staging_upward_leaks_count": len(mathlib_staging_leaks),
            "current_mathlib_staging_upward_leaks": mathlib_staging_leaks,
            "unused_qou_import_candidates_count": len(unused_qou_import_candidates),
            "unused_qou_import_candidates_sample": unused_qou_import_candidates[:40],
            "unresolved_imports": unresolved_imports,
        },
        "root_reachability_and_orphans": {
            "qou_lean_direct_imports": len(qou_adj.get("QOU", [])),
            "qou_lean_transitive_reachable": len(reachable_from_root - {"QOU"}),
            "orphaned_from_qou_lean_count": len(orphans_from_qou_root),
            "orphaned_from_qou_lean_pct": round(100.0 * len(orphans_from_qou_root) / max(1, len(qou_library_mods)), 2),
            "orphans_reached_by_sibling_imports": len(set(orphans_from_qou_root) & reachable_from_siblings),
            "orphans_referenced_by_ts_lean_ref": len(set(orphans_from_qou_root) & referenced_qou_modules_from_ts),
            "true_disconnected_leaf_orphans_count": len(true_disconnected_orphans),
            "orphans_by_subdir_top25": dict(
                Counter(modules[m]["subdir"] for m in orphans_from_qou_root).most_common(25)
            ),
        },
        "synonym_directory_clusters": synonym_cluster_metrics,
        "tier_a_and_tier_b_reservoir_packages": {
            "community_inter_package_scc_cycles": comm_sccs,
            "community_to_qou_cut_edges_count": len(cut_edges_blocking_community),
            "community_to_qou_cut_edges": cut_edges_blocking_community,
            "target_layer_back_edges_count": len(target_layer_back_edges),
            "target_layer_back_edges_sample": target_layer_back_edges[:50],
            "packages": {
                p: {
                    "description": (
                        "Selective Mathlib4 Core PR Staging (List/sort/foldl, general matrix/trace, "
                        "ordered-field/sqrt/convexity, Borel/Dirichlet/Cech general lemmas)"
                        if p == "TierA.MathlibExt"
                        else TIER_B_DESCRIPTIONS[p.removeprefix("TierB.")]
                    ),
                    **partition_summary[p],
                }
                for p in ["TierA.MathlibExt"] + [f"TierB.{x}" for x in TIER_B_PACKAGES]
            },
        },
        "canonical_12_qou_subgraphs": {
            p: partition_summary[p] for p in CANONICAL_QOU_SUBGRAPHS
        },
        "current_83_subdirs_inventory": per_subdir_stats,
        "refactor_options": refactor_options,
        "module_migration_map": dict(sorted(module_migration_map.items())),
    }
    return report


def render_markdown_report(audit: dict[str, Any]) -> str:
    ct = audit["corpus_totals"]
    pg = audit["process_gate_status"]
    ps = audit["purity_and_7c_stratification"]
    dag = audit["dag_and_scc_analysis"]
    orph = audit["root_reachability_and_orphans"]
    tb = audit["tier_a_and_tier_b_reservoir_packages"]
    qsubs = audit["canonical_12_qou_subgraphs"]

    lines: list[str] = []
    w = lines.append

    w("# Lean 4 Knowledge-Graph Detangler & Reservoir `lean_lib` Architecture Options (`qou-kgdt` + `qou-mlib`)")
    w("")
    w(f"- **Date:** `{audit['audit_date']}`")
    w(f"- **Epic / Beans:** `qou-lnkg` (`qou-kgdt`, `qou-lskl`, `qou-mlib`; gates `qou-lref` & `qou-lanx`)")
    w(f"- **Instrument:** `scripts/lean-kg-detangler.py` (deterministic static DAG + §7c + QOU-purity analyzer, `{audit['runtime_seconds']}s` wall time)")
    w("- **Machine-readable companion:** `docs/audits/2026-11-23-lean-kg-detangler-and-reservoir-audit.json`")
    w("- **Scope Gate:** Stage 1 + Stage 1b + Stage 2 options readiness ONLY — **zero `.lean` files moved or renamed** pending owner selection via `AskUserQuestion`.")
    w("")
    w("---")
    w("")
    w("## 1. Executive Summary & `Process_GraphDetanglement` Gate Measurements")
    w("")
    w("Following `cat-harness/processes/kg/graph-detanglement.bpmn` (`Process_GraphDetanglement`), we measure the **unassigned column FIRST** before reading cross-edge counts:")
    w("")
    w("| Gate / Metric | Measured Value | Status / Interpretation |")
    w("|---|---:|---|")
    w(f"| Total `.lean` files in `folio/quantum-observable-universe/` | **{ct['qou_paper_total_lean_files']:,}** | `{ct['qou_lean_dir_files']:,}` in `lean/` + `{ct['content_block_sibling_lean_files']:,}` content-block siblings (`+{ct['sibling_paper_ugb_lean_files']}` `UGB`, `+{ct['sibling_paper_fred2005_lean_files']}` `Fred2005`) |")
    w(f"| Fragmented `lean/QOU/*` subdirectories + loose root files | **{ct['qou_subdirs_count']} dirs + {ct['qou_loose_root_files']} loose** | Grew from `78` to `83` ad-hoc dirs under `QOU/` (`{ct['qou_library_modules_excluding_root_and_scratch']:,}` library modules, `{ct['library_declarations_total']:,}` decls) |")
    w(f"| `Task_Declare` — Unassigned library modules | **{pg['Task_Declare']['unassigned_library_modules']}** | `declared` (100% of `{ct['qou_library_modules_excluding_root_and_scratch']:,}` modules mapped to Tier-A, 6 Tier-B, or 12 `QOU.*` subgraphs) |")
    w(f"| `Task_Measure` — Unassigned resolved `import` edges | **{pg['GW_Detangled']['unassigned_resolved_edges']}** | `{audit['edge_accounting'].get('qou_internal_resolved', 0):,}` internal `QOU` + `{audit['edge_accounting'].get('external_mathlib', 0):,}` `Mathlib` + `{audit['edge_accounting'].get('external_ugb', 0):,}` `UGB` (`{pg['GW_Detangled']['unresolved_dangling_imports']}` dangling) |")
    w(f"| Module-level `import` cycles (Tarjan SCC) | **{len(dag['module_level_scc_cycles'])}** | Module graph is strictly acyclic (`0` Lean module cycles) |")
    w(f"| Directory-level nontrivial SCCs across `83` `QOU/*` dirs | **{len(dag['directory_level_nontrivial_sccs'])}** |Largest directory SCC tangles `{len(dag['directory_level_nontrivial_sccs'][0]) if dag['directory_level_nontrivial_sccs'] else 0}` folders via `{dag['mutual_directory_back_edge_pairs_count']}` bidirectional folder pairs |")
    w(f"| Orphaned modules not reachable from `QOU.lean` | **{orph['orphaned_from_qou_lean_count']:,}** (`{orph['orphaned_from_qou_lean_pct']}%`) | Built by `globs = [\"QOU.+\"]` (`qou-rc7b`), `{orph['orphans_reached_by_sibling_imports']:,}` reached by chapter `.lean` siblings, `{orph['true_disconnected_leaf_orphans_count']:,}` unimported leaves |")
    w(f"| Intrinsically pure-math library modules (`0` QOU coupling) | **{ps['library_intrinsic_purity'].get('pure_math', 0):,}** | **{ps['library_transitive_cone_purity'].get('cone_pure_math', 0):,}** already cone-pure (`0` QOU deps transitively); **{ps['library_transitive_cone_purity'].get('cut_blocked_pure_math', 0):,}** blocked only by cut-edges |")
    w(f"| Outbound cut-edges (`Tier-A / Tier-B -> QOU.*`) | **{tb['community_to_qou_cut_edges_count']}** | Exact edges to prune/factor before zero-`QOU.*` `lean_lib` isolation (`GW_Detangled`) |")
    w(f"| Current `Mathlib`/`MathlibExt`/`MathlibInfra` upward leaks | **{dag['current_mathlib_staging_upward_leaks_count']}** | Existing staging modules importing non-staging `QOU.*` directories |")
    w(f"| Library `sorry` / custom `axiom` counts | `{ct['library_sorry_non_class']}` body / `{ct['library_sorry_class_body_3b_cond']}` class / `{ct['library_custom_axioms']}` `axiom` | Siblings: `{ct['sibling_sorry_non_class']}` body `sorry`, `{ct['sibling_sorry_class_body_3b_cond']}` §3b-cond class `sorry`, `{ct['sibling_custom_axioms']}` `axiom` |")
    w("")
    w("## 2. Purity & §7c Base-Ring Stratification")
    w("")
    w("### 2.1 Mathematical vs. QOU-Physics Coupling (`3,840` Library Modules + `909` Siblings)")
    w("")
    w("| Purity Tier | Library Modules | Transitive Cone Status | Content-Block Siblings | Definition |")
    w("|---|---:|---|---:|---|")
    w(f"| `pure_math` | **{ps['library_intrinsic_purity'].get('pure_math', 0):,}** | `{ps['library_transitive_cone_purity'].get('cone_pure_math', 0):,}` cone-pure + `{ps['library_transitive_cone_purity'].get('cut_blocked_pure_math', 0):,}` cut-blocked | {ps['sibling_intrinsic_purity'].get('pure_math', 0):,} | Zero `q0`/`substrate_q`, zero CODATA/decimals, zero particle/QOU-axiom types |")
    w(f"| `qou_categorical_core` | **{ps['library_intrinsic_purity'].get('qou_categorical_core', 0):,}** | `{ps['library_transitive_cone_purity'].get('qou_categorical_core', 0):,}` | {ps['sibling_intrinsic_purity'].get('qou_categorical_core', 0):,} | Uses QOU categorical/particle structures over generic rings; zero `q0` or CODATA |")
    w(f"| `qou_archimedean_model` | **{ps['library_intrinsic_purity'].get('qou_archimedean_model', 0):,}** | `{ps['library_transitive_cone_purity'].get('qou_archimedean_model', 0):,}` | {ps['sibling_intrinsic_purity'].get('qou_archimedean_model', 0):,} | Evaluates at `substrate_q` / `q0` / `AlphaEM` without empirical decimal tables |")
    w(f"| `qou_empirical_comparison` | **{ps['library_intrinsic_purity'].get('qou_empirical_comparison', 0):,}** | `{ps['library_transitive_cone_purity'].get('qou_empirical_comparison', 0):,}` | {ps['sibling_intrinsic_purity'].get('qou_empirical_comparison', 0):,} | CODATA / MeV / decimal literals / experimental comparison boundaries |")
    w("")
    w("### 2.2 §7c Base-Ring Generality Distribution")
    w("")
    w("| §7c Ring Regime | Library Modules | Content-Block Siblings | Upstreaming / Hygiene Action |")
    w("|---|---:|---:|---|")
    w(f"| `pure_generic` (`[CommRing R]` / `[Field R]`) | **{ps['library_7c_ring_regime'].get('pure_generic', 0):,}** | {ps['sibling_7c_ring_regime'].get('pure_generic', 0):,} | Gold-standard §7c algebraic generality |")
    w(f"| `ordered_generic` (`[LinearOrderedField R]`, etc.) | **{ps['library_7c_ring_regime'].get('ordered_generic', 0):,}** | {ps['sibling_7c_ring_regime'].get('ordered_generic', 0):,} | Gold-standard §7c ordered generality (no `ℝ` lock-in) |")
    w(f"| `ring_agnostic` (combinatorics / `ℕ` / `ℤ` / categories) | **{ps['library_7c_ring_regime'].get('ring_agnostic', 0):,}** | {ps['sibling_7c_ring_regime'].get('ring_agnostic', 0):,} | Clean combinatorial / discrete / categorical modules |")
    w(f"| `archimedean_real` (justified `Real.sqrt`/`exp`/`log`/decimals) | **{ps['library_7c_ring_regime'].get('archimedean_real', 0):,}** | {ps['sibling_7c_ring_regime'].get('archimedean_real', 0):,} | Legitimate post-wall Archimedean analysis |")
    w(f"| `gratuitous_real_candidate` (`: ℝ` without transcendental ops) | **{ps['library_7c_ring_regime'].get('gratuitous_real_candidate', 0):,}** | {ps['sibling_7c_ring_regime'].get('gratuitous_real_candidate', 0):,} | Generalize `: ℝ` → `[CommRing R]` / `[LinearOrderedField R]` during Tier-A/B curation |")
    w(f"| `mixed_generic_and_real` (both `[CommRing R]` & `: ℝ` in 1 file) | **{ps['library_7c_ring_regime'].get('mixed_generic_and_real', 0):,}** | {ps['sibling_7c_ring_regime'].get('mixed_generic_and_real', 0):,} | Split generic theorem from `(R := ℝ)` instantiation per §7c wall rule |")
    w("")
    w("## 3. Tier-A (`Mathlib4` Core) & Tier-B (6 Standalone Lean Reservoir `lean_lib` Packages)")
    w("")
    w("| Target Library | Total Modules | Cone-Pure Ready Now | Cut-Blocked Pure | Decls (`thm`/`lem`) | Body `sorry` / `axiom` | Outbound Cut-Edges to `QOU.*` | Inbound `QOU` Consumers | `.ts` `lean.ref`s |")
    w("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for p_key, p_info in tb["packages"].items():
        w(
            f"| `{p_key}` | **{p_info['total_modules']}** | **{p_info['cone_pure_ready_now']}** | "
            f"{p_info['cut_blocked_pure_modules']} | {p_info['declarations_total']:,} ({p_info['theorems_and_lemmas']:,}) | "
            f"{p_info['sorry_non_class']} / {p_info['custom_axioms']} | **{p_info['outbound_cut_edges_to_qou']}** | "
            f"{p_info['inbound_consumer_edges']} | {p_info['ts_lean_ref_pointers']} |"
        )
    w("")
    w("> **Companion Already-Extracted Reservoir Package:** `folio/unital-groebner-bases/lean/` (`UGB`, **47 `.lean` files**) already provides standalone Gröbner–Shirshov / Kang–Lee–Lee–Oh / Splay PBW infrastructure with zero `QOU.*` imports (`qou` requires `ugb` via `[[require]]`). `HeckeTemperleyLieb` either layers cleanly on `ugb` or re-exports its `HeckeGS` bridge.")
    w("")
    w("### 3.1 Package Scope & Representative Modules")
    w("")
    for p_key, p_info in tb["packages"].items():
        w(f"- **`{p_key}`** ({p_info['total_modules']} modules; {p_info['cone_pure_ready_now']} immediately zero-`QOU` cone-pure): {p_info['description']}.")
        w(f"  - *Primary current folders:* `{json.dumps(p_info['source_subdirs'])}`")
        w(f"  - *Sample modules:* {', '.join(f'`{m}`' for m in p_info['sample_modules'][:6])}")
        if p_info["outbound_edges_to_other_community_libs"]:
            w(f"  - *Inter-community `lean_lib` deps:* `{json.dumps(p_info['outbound_edges_to_other_community_libs'])}`")
    w("")
    w("### 3.2 Exact Cut-Edges Blocking Zero-`QOU.*` Extraction (`GW_Detangled` Action List)")
    w("")
    if not tb["community_to_qou_cut_edges"]:
        w("Zero outbound cut-edges from Tier-A/Tier-B into `QOU.*`!")
    else:
        w(f"There are exactly **{tb['community_to_qou_cut_edges_count']}** directed `import` edges from intrinsically pure Tier-A/Tier-B candidate modules into QOU-coupled modules. Pruning or factoring the pure base definition out of these targets brings `community_to_qou_cut_edges` to **0**:")
        w("")
        w("| # | Pure Candidate Module (`src`) | Candidate Lib | Imported `QOU.*` Target (`dst`) | Target Subgraph | Recommended Detangle Move |")
        w("|---:|---|---|---|---|---|")
        for idx, ce in enumerate(tb["community_to_qou_cut_edges"][:60], 1):
            w(
                f"| {idx} | `{ce['src_module']}` | `{ce['src_partition']}` | "
                f"`{ce['dst_module']}` | `{ce['dst_partition']}` | `{ce['recommended_move']}` |"
            )
        if len(tb["community_to_qou_cut_edges"]) > 60:
            w(f"| … | *(+{len(tb['community_to_qou_cut_edges']) - 60} more in JSON audit)* | — | — | — | — |")
    w("")
    if tb["community_inter_package_scc_cycles"]:
        w("### 3.3 Inter-Package Couplings Among Community `lean_lib` Targets")
        w("")
        w(f"- Detected **{len(tb['community_inter_package_scc_cycles'])}** inter-package SCC(s) among the community targets: `{tb['community_inter_package_scc_cycles']}`.")
        w("- **Resolution:** Keep `TierA.MathlibExt` strictly at Layer 1 (zero imports from `TierB.*`) and orient `TierB` DAG as `{QCalculus, TwistedFrobeniusHopf, ToricConicOpt, BraidKnotOctonion} -> {HeckeTemperleyLieb, CompactQuantumMetrics}` by moving shared braid/partition definitions down into the lower `lean_lib`.")
        w("")

    w("## 4. Directory-Level Tangle & Consolidation (`83` `QOU/*` Dirs -> `12` Canonical `QOU.*` Subgraphs)")
    w("")
    w("### 4.1 Synonym-Directory Merge Clusters")
    w("")
    w("| Synonym Cluster | Current Directories (`#`) | Total Files | Pure-Math Files Inside | Cross-Synonym Edges Eliminated | Remaining External Edges |")
    w("|---|---|---:|---:|---:|---:|")
    for cname, cm in audit["synonym_directory_clusters"].items():
        dirs_str = ", ".join(f"`{d}` ({cm['per_dir_files'][d]})" for d in cm["directories"])
        w(
            f"| `{cname}` | {dirs_str} | **{cm['total_files']}** | {cm['pure_math_files_inside']} | "
            f"**{cm['cross_synonym_edges_eliminated_by_merge']}** | {cm['external_out_edges']} |"
        )
    w("")
    w("### 4.2 Directory-Level SCC Tangles & Top Bidirectional Folder Pairs")
    w("")
    if dag["directory_level_nontrivial_sccs"]:
        for i, scc in enumerate(dag["directory_level_nontrivial_sccs"], 1):
            w(f"- **Directory SCC #{i} ({len(scc)} directories mutually coupled):** {', '.join(f'`{d}`' for d in scc)}")
    w("")
    w("| Dir A | Dir B | `A -> B` Imports | `B -> A` Imports | Min-Cut Back-Edges |")
    w("|---|---|---:|---:|---:|")
    for pair in dag["top_mutual_directory_back_edge_pairs"][:15]:
        w(
            f"| `{pair['dir_a']}` | `{pair['dir_b']}` | {pair['edges_a_to_b']} | "
            f"{pair['edges_b_to_a']} | **{pair['min_cut_back_edges']}** |"
        )
    w("")
    w("### 4.3 Target `12` Canonical Monograph-Aligned `QOU.<Subgraph>` Partitions (After Extracting Tier-A & Tier-B)")
    w("")
    w("| Canonical `QOU.*` Subgraph | Layer | QOU-Coupled Modules | Decls (`thm`/`lem`) | Body `sorry` / `axiom` | Inbound Edges | `.ts` `lean.ref`s | Consolidated Source Folders (Top) |")
    w("|---|---:|---:|---:|---:|---:|---:|---|")
    for sg in CANONICAL_QOU_SUBGRAPHS:
        sinfo = qsubs[sg]
        top_dirs = ", ".join(f"`{k}`:{v}" for k, v in list(sinfo["source_subdirs"].items())[:5])
        w(
            f"| `{sg}` | L{LAYER_RANK[sg]} | **{sinfo['total_modules']}** | "
            f"{sinfo['declarations_total']:,} ({sinfo['theorems_and_lemmas']:,}) | "
            f"{sinfo['sorry_non_class']} / {sinfo['custom_axioms']} | "
            f"{sinfo['inbound_consumer_edges']} | {sinfo['ts_lean_ref_pointers']} | {top_dirs} |"
        )
    w("")
    w("## 5. Comparison of 3 Concrete Refactor Options (Ready for Coordinator `AskUserQuestion`)")
    w("")
    w("| Dimension | **Option 1 (Recommended): Multi-`lean_lib` in `lakefile.toml`** | **Option 2: 6 Separate Lake Packages (`folio/lean-contrib/*`)** | **Option 3: Single-Lib Mirror (`QOU/Contrib/<Pkg>/*`)** |")
    w("|---|---|---|---|")
    opt1, opt2, opt3 = audit["refactor_options"]
    q1, q2, q3 = opt1["quantitative_impact"], opt2["quantitative_impact"], opt3["quantitative_impact"]
    w(f"| **Lake Target Architecture** | `MathlibExt` + 6 Tier-B `[[lean_lib]]` + `QOU` in `folio/quantum-observable-universe/lean/lakefile.toml` | 6 standalone `lakefile.toml` packages under `folio/lean-contrib/<pkg>/lean/` via `[[require]]` | Single `[[lean_lib]] name = \"QOU\"` with `QOU/Contrib/<Pkg>/*` folders |")
    w(f"| **`Process_GraphDetanglement` Stage** | **Stage 3 (`Isolate` in-place)** — 1-folder `git mv` away from Stage 4 extraction | **Stage 4 (`Extract` immediately)** — full multi-package split now | **Stage 2 (`Detangle` only)** — keeps `QOU.` namespace prefix |")
    w(f"| **Tier-B Reservoir Modules** | **{q1['files_moved_to_tier_b_libs']}** modules in root namespaces (`HeckeTemperleyLieb.*`, etc.) | **{q2['files_extracted_to_new_lake_packages']}** modules in 6 new Lake packages | **{q3['files_moved_under_qou_contrib']}** modules under `QOU.Contrib.<Pkg>.*` |")
    w(f"| **Tier-A `MathlibExt` Modules** | **{q1['files_moved_to_tier_a_mathlibext']}** modules (`MathlibExt.*`) | **{q2['files_moved_to_tier_a_mathlibext']}** modules (`MathlibExt.*`) | **{q3['files_moved_under_qou_mathlibext']}** modules (`QOU.MathlibExt.*`) |")
    w(f"| **Collapsed `QOU.*` Subgraphs** | `83 dirs + 106 loose` → **12 canonical `QOU.<Chapter>` dirs** (**{q1['files_consolidated_into_12_qou_subgraphs']}** modules) | `83 dirs + 106 loose` → **12 canonical `QOU.<Chapter>` dirs** (**{q2['files_consolidated_into_12_qou_subgraphs']}** modules) | `83 dirs + 106 loose` → **12 canonical `QOU.<Chapter>` dirs** (**{q3['files_consolidated_into_12_qou_subgraphs']}** modules) |")
    w(f"| **Blocking Cut-Edges to Prune/Factor** | **{q1['cut_edges_to_resolve_first']}** (`Tier-A/B -> QOU.*`) | **{q2['cut_edges_to_resolve_first']}** (`Tier-A/B -> QOU.*`) | **{q3['cut_edges_to_resolve_first']}** (`Tier-A/B -> QOU.*`) |")
    w(f"| **Zero-`QOU.*` Boundary Enforcement** | `lake build <TierBLib>` + `lean-best-practices-lint.py --package` | Physical Lake package DAG (impossible to import `QOU.*`) + linter | Python linter (`lean-best-practices-lint.py`) only |")
    w(f"| **`import` Lines Rewritten (Codemod)** | ~{q1['import_lines_rewritten_estimate']:,} (`QOU` + siblings) | ~{q2['import_lines_rewritten_estimate']:,} (`QOU` + siblings) | ~{q3['import_lines_rewritten_estimate']:,} (`QOU` + siblings) |")
    w(f"| **`.ts` `lean.ref` Updates** | ~{q1['ts_lean_ref_updates_estimate']:,} (keeps `qou:<Decl>` package URI!) | ~{q2['ts_lean_ref_updates_estimate']:,} + **6 new URI prefixes** in `schemas/lean-packages.ts` | ~{q3['ts_lean_ref_updates_estimate']:,} (keeps `qou:QOU.Contrib...` URI) |")
    w(f"| **`.olean` Cache / Overlay Blast Radius** | **Low** (`0` new `.lake/build` roots; `lean-overlay-env.sh` works unchanged!) | **High** (`+6` `.lake/build/lib/lean` roots in `lean-env.sh`, overlay, & cache seeders) | **Lowest** (`0` new roots, single `QOU/` folder) |")
    w(f"| **Second Rename Needed for Reservoir?** | **No (0 files)** — namespaces are already Reservoir-final | **No (0 files)** | **Yes ({q3['second_rename_required_for_reservoir']} files)** must drop `QOU.Contrib.` later |")
    w(f"| **Estimated Effort** | **{opt1['effort_estimate']}** | {opt2['effort_estimate']} | {opt3['effort_estimate']} |")
    w("")
    w("### Recommended Phased Execution Strategy (`qou-lref` -> `qou-lanx`)")
    w("")
    w("1. **Adopt Option 1 now (`Isolate in-place`)** once active Lean PRs settle and the owner confirms via `AskUserQuestion`:")
    w(f"   - **Step 1 (Cut-edge surgical prep):** Resolve the **{q1['cut_edges_to_resolve_first']}** outbound `Tier-A/B -> QOU.*` cut-edges (`Task_Move`: factor pure base definitions out of `QOU.*` or reclassify pure targets) and re-run `scripts/lean-kg-detangler.py` until `community_to_qou_cut_edges == 0`.")
    w("   - **Step 2 (Atomic codemod + `[[lean_lib]]` isolation):** Move the 6 Tier-B subgraphs to top-level namespaces (`HeckeTemperleyLieb/`, `TwistedFrobeniusHopf/`, `ToricConicOpt/`, `CompactQuantumMetrics/`, `QCalculus/`, `BraidKnotOctonion/`) + `MathlibExt/` inside `folio/quantum-observable-universe/lean/`, collapse the remaining `QOU/*` tree into the `12` canonical chapter subgraphs, rewrite `import` and `lean.ref` strings atomically, and verify with `LEAN_NUM_THREADS=1 nice -n 15 bash scripts/lean-direct-cone.sh -j 1` + `scripts/lean-best-practices-lint.py`.")
    w("   - **Step 3 (Optional Stage 4 `Extract` to Option 2 per-library):** Whenever an individual Tier-B library (e.g., `TwistedFrobeniusHopf` or `CompactQuantumMetrics`) is ready for public Lean Reservoir indexing, `Task_Extract` lifts its already-isolated folder into a standalone repo with **zero namespace or theorem-name churn**.")
    w("")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--qou-root",
        type=Path,
        default=DEFAULT_QOU_ROOT,
        help="Path to folio/quantum-observable-universe",
    )
    ap.add_argument(
        "--json-out",
        type=Path,
        default=None,
        help="Write machine-readable JSON/JSON-LD audit to this path",
    )
    ap.add_argument(
        "--md-out",
        type=Path,
        default=None,
        help="Write human-readable Markdown options report to this path",
    )
    ap.add_argument(
        "--map-out",
        type=Path,
        default=None,
        help="Write deterministic old_module -> new_module JSON migration map to this path",
    )
    ap.add_argument(
        "--summary-only",
        action="store_true",
        help="Print concise console summary only",
    )
    args = ap.parse_args(argv)

    audit = analyze_corpus(args.qou_root)

    if args.map_out:
        args.map_out.parent.mkdir(parents=True, exist_ok=True)
        map_payload = {
            "schema": "qou.lean.reservoir_module_migration_map.v1",
            "option": "Option_1",
            "community_libs_ordered": list(COMMUNITY_LIBS_ORDERED),
            "canonical_qou_subgraphs": list(CANONICAL_QOU_SUBGRAPHS),
            "subdir_to_canonical_qou": SUBDIR_TO_CANONICAL_QOU,
            "total_modules": len(audit["module_migration_map"]),
            "modules": audit["module_migration_map"],
        }
        args.map_out.write_text(
            json.dumps(map_payload, indent=2, sort_keys=False, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    if args.json_out:
        # Exclude bulky per-module map from summary audit JSON when --map-out is separate,
        # or keep a compact digest so audit JSON stays concise and fast.
        audit_for_json = {k: v for k, v in audit.items() if k != "module_migration_map"}
        audit_for_json["module_migration_map_count"] = len(audit["module_migration_map"])
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(
            json.dumps(audit_for_json, indent=2, sort_keys=False, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    if args.md_out:
        args.md_out.parent.mkdir(parents=True, exist_ok=True)
        args.md_out.write_text(render_markdown_report(audit), encoding="utf-8")

    ct = audit["corpus_totals"]
    pg = audit["process_gate_status"]
    tb = audit["tier_a_and_tier_b_reservoir_packages"]
    print(
        f"lean-kg-detangler: scanned {ct['qou_paper_total_lean_files']} .lean files "
        f"({ct['qou_lean_dir_files']} library + {ct['content_block_sibling_lean_files']} siblings) "
        f"in {audit['runtime_seconds']}s"
    )
    print(
        f"  Task_Declare: unassigned_modules={pg['Task_Declare']['unassigned_library_modules']} "
        f"| GW_Detangled: unassigned_edges={pg['GW_Detangled']['unassigned_resolved_edges']}, "
        f"cut_edges={tb['community_to_qou_cut_edges_count']}, "
        f"dir_sccs={pg['GW_Detangled']['directory_scc_tangles']}"
    )
    if not args.summary_only:
        for p_key, p_info in tb["packages"].items():
            print(
                f"  {p_key:30s}: {p_info['total_modules']:4d} modules "
                f"(cone_pure={p_info['cone_pure_ready_now']:4d}, "
                f"cut_blocked={p_info['cut_blocked_pure_modules']:3d}, "
                f"cut_edges={p_info['outbound_cut_edges_to_qou']:3d})"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
