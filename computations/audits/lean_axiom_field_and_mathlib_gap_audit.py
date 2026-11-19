#!/usr/bin/env python3
# polynomial_q_not_applicable: static Lean 4 AST and import-graph audit; emits integer counts and string taxonomy only.
"""Comprehensive Audit of All Lean `class` / `structure` Axiom Fields & Missing Mathlib4 Infrastructure.

Owner directive (2026-11-19):
  "audit axioms fields - sign of a gap to be filled. lots of missing mathlib infra. bean up epic"

Scans EVERY `.lean` file in `folio/quantum-observable-universe/lean/` (library scope) AND
all chapter-level `folio/quantum-observable-universe/*/*.lean` files (excluding `.lake/`).
Complements existing static gates in `scripts/`:
  - `scripts/lean-assumption-surface.py` (comment-stripped `sorry`, `axiom`, `native_decide`, `: True`)
  - `scripts/lean-self-assuming-audit.py` & `scripts/lean-class-hypothesis-vacuity-probe.py`
  - `scripts/trivially-inhabiting-instance-census.py` & `scripts/lean-context-class-inhabitation-probe.py`
  - `scripts/free-prop-field-audit.py` & `scripts/lean-structure-field-law-audit.py`

Extracts every `class` and `structure` carrying `Prop`-valued fields (or `: Prop` / `extends` /
class-level bundled data+law premises), plus all standalone `axiom` and `opaque` declarations,
and classifies each declaration along two orthogonal axes:

  Axis 1 — Instantiation Status Across the Entire Repo (import-graph & transitive-shim aware):
    - `UNINSTANTIATED_AXIOM_CLASS` : Quantified in theorem/def binders (or standalone), with zero
      concrete non-trivial `instance` or constructor proofs on a real mathematical carrier
      (includes axiom-shim classes whose only instances forward an uninstantiated QOU axiom class).
    - `TOY_ONLY_INSTANCE`          : Inhabited only on trivial/toy carriers (`Unit`, `PUnit`,
      `Fin 0`, `Fin 1`, `Empty`) or via constant zero/trivial data fields (`0`, `fun _ => 0`, `True`).
    - `GENUINELY_INSTANTIATED`     : Backed by >= 1 non-trivial proved `instance` or constructor
      proof grounded without uninstantiated QOU axiom shims.

  Axis 2 — Root-Cause Taxonomy (Why Is It an Axiom Field Today?):
    - `MISSING_MATHLIB_INFRA` (`Type M`, partitioned into cohesive clusters `M1..M7`)
    - `QOU_BRIDGE_OR_PHYSICS_GAP` (`Type P`)
    - `LEGITIMATE_ALGEBRAIC_INTERFACE` (`Type D`)

Rule compliance:
  - Zero binary64 / `float` / `math` / `numpy` anywhere (`probe-float64-guard.py --strict` = 0 hits).
  - Stamped `q0Anchor: "independent"` with explicit `q0AnchorReason`.
  - Emits `computations/audits/lean-axiom-field-and-mathlib-gap-audit.witness.json`.
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any
import re

HERE = Path(__file__).resolve().parent
COMP_ROOT = HERE.parent
REPO_ROOT = COMP_ROOT.parent
QOU_FOLIO_ROOT = REPO_ROOT / "folio" / "quantum-observable-universe"

sys.path.insert(0, str(COMP_ROOT))
sys.path.insert(0, str(COMP_ROOT / "substrate"))
sys.path.insert(0, str(REPO_ROOT / "tools" / "qou-substrate" / "python"))

import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder  # noqa: E402

getcontext().prec = 28

# ── Comment stripping with docstring capture (line-preserving) ────────────────


def strip_comments_and_extract_docstrings(text: str) -> tuple[str, dict[int, str]]:
    """Blank `--` and nested `/- ... -/` comments while preserving line numbers.
    Also maps `end_line_1based -> docstring_text` for `/-- ... -/` declaration docstrings.
    """
    out: list[str] = []
    docstrings_by_end_line: dict[int, str] = {}
    i = 0
    n = len(text)
    line_no = 1
    while i < n:
        if text.startswith("/-", i):
            is_doc = text.startswith("/--", i) and not text.startswith("/---", i)
            depth = 1
            j = i + 2
            while j < n and depth > 0:
                if text.startswith("/-", j):
                    depth += 1
                    j += 2
                elif text.startswith("-/", j):
                    depth -= 1
                    j += 2
                else:
                    j += 1
            segment = text[i:j]
            nl_count = segment.count("\n")
            out.append("\n" * nl_count)
            line_no += nl_count
            if is_doc:
                inner = segment[3:-2].strip() if len(segment) >= 5 else ""
                docstrings_by_end_line[line_no] = inner
            i = j
        elif text.startswith("--", i):
            j = text.find("\n", i)
            i = n if j < 0 else j
        else:
            ch = text[i]
            out.append(ch)
            if ch == "\n":
                line_no += 1
            i += 1
    return "".join(out), docstrings_by_end_line


# ── Lean declaration & field parsers ─────────────────────────────────────────

PROP_OPS = ("=", "≠", "<", "≤", ">", "≥", "∈", "∉", "∣", "↔", "∧", "∨", "¬", "∀", "∃")
PROP_WORDS_RE = re.compile(
    r"\b(?:Prop|True|False|Nonempty|Injective|Surjective|Bijective|StrictMono|StrictAnti|"
    r"Monotone|Antitone|Continuous|ContinuousOn|Differentiable|DifferentiableAt|HasDerivAt|"
    r"Summable|Tendsto|Measurable|Integrable|IsOpen|IsClosed|IsCompact|Connected|Irrational|"
    r"Prime|Nat\.Prime|Coprime|Disjoint|Subsingleton|Nontrivial|Finite|Infinite|Fintype|"
    r"Exact|ShortExact|IsIso|Mono|Epi|Faithful|Full|EssSurj|LinearIndependent|"
    r"PosDef|PosSemidef|Hermitian|Symmetric|IsUnit|Irreducible|Determinate|Converges)\b"
)


def is_prop_field_type(ty: str) -> bool:
    t = ty.replace("->", " ").replace("←", " ")
    if any(op in t for op in PROP_OPS):
        return True
    return bool(PROP_WORDS_RE.search(t))


CARRIER_RE = re.compile(
    r"^(?P<indent>[ \t]*)(?:@\[[^\]]*\]\s*)*(?:noncomputable\s+|scoped\s+|private\s+|protected\s+)*"
    r"(?P<kind>class|structure)\s+(?P<name>[A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)*)(?P<hdr>.*)$"
)
FIELD_RE = re.compile(
    r"^(?P<indent>[ \t]+)(?P<fname>[A-Za-z_α-ωΑ-ΩΔΛΣΠΦΨΩ][A-Za-z0-9_'₀-₉α-ωΑ-Ω]*)\s*"
    r"(?P<fbind>[^:=\n]*?)\s*:\s*(?P<ftype>.*)$"
)
TOP_DECL_RE = re.compile(
    r"^(?P<indent>[ \t]*)(?:@\[[^\]]*\]\s*)*(?:noncomputable\s+|scoped\s+|local\s+|private\s+|protected\s+|unsafe\s+)*"
    r"(?P<kw>instance|def|abbrev|theorem|lemma|example)\b(?P<rest>.*)$"
)
AXIOM_OPAQUE_RE = re.compile(
    r"^(?P<indent>[ \t]*)(?:@\[[^\]]*\]\s*)*(?:noncomputable\s+|private\s+|protected\s+)*"
    r"(?P<kw>axiom|opaque)\s+(?P<name>[A-Za-z_][A-Za-z0-9_'.]*)\s*(?P<rest>.*)$"
)

TOY_TYPE_RE = re.compile(
    r"\b(?:Unit|PUnit|PEmpty|Empty|Fin\s+[01]|ULift\s+Unit)\b"
)
TRIVIAL_VAL_RE = re.compile(
    r"^(?:"
    r"\(?\s*(?:-\s*)?0\s*(?::[^)]*)?\)?"
    r"|True|trivial|PUnit\.unit|Unit\.unit|⟨⟩|\(\)|∅"
    r"|Unit|PUnit|Fin\s+1|Bool"
    r"|fun\s+[^=]*=>\s*(?:\(?\s*(?:-\s*)?0\s*(?::[^)]*)?\)?|True|trivial|PUnit\.unit|Unit\.unit|\(\)|∅)"
    r")$"
)

# ── Root-Cause Taxonomy (Type M Clusters M1..M7 vs Type P vs Type D) ─────────

MATHLIB_CLUSTERS: dict[str, dict[str, Any]] = {
    "M1_DILOG_BLOCH_SUSLIN": {
        "short_label": "M1: Polylog / Li₂ / Bloch–Wigner 5-Term / Bloch–Suslin B₂,B₃",
        "mathlib_target": (
            "Mathlib.Analysis.SpecialFunctions.Polylogarithm (Li_2, Faddeev quantum dilog), "
            "Bloch–Wigner D_2(z) 5-term pentagon relation, PreBlochGroup / BlochGroup B_2(C) & B_3(C), "
            "scissors congruence, and Borel regulator"
        ),
        "existing_beans": ["mlgp", "qou-o41q", "qou-mlbg", "qou-gkco", "qou-tc8y"],
        "pattern": re.compile(
            r"(?:Polylog|Dilog|Trilog|LiTwo|Li2|Li_2|Clausen|Cl_2|Lobachevsky|BlochWigner|"
            r"PreBloch|BlochGroup|BlochSuslin|PentagonRelation|PentagonUV|FiveTerm|RogersPair|"
            r"ScissorsCongruence|BorelRegulator|BorelZagier|KummerRadial|FaddeevQuantumDilog|"
            r"QuantumDilog|QuantumBloch|ZagierPolylog|Goncharov)",
            re.I,
        ),
    },
    "M2_RIEMANN_SURFACES_HODGE_CONTOUR": {
        "short_label": "M2: Riemann Surfaces / Riemann–Roch / Hodge / Contour & Hadamard",
        "mathlib_target": (
            "Compact Riemann surfaces, divisors & linear systems, Riemann–Roch & Serre duality, "
            "Hodge decomposition H^{1,0} + H^{0,1}, analytic Gauss–Bonnet 4*pi*(g-1), "
            "Weierstrass p-function, windingNumber / Cauchy residue / argument principle, "
            "and Hadamard entire-function factorization"
        ),
        "existing_beans": ["qou-bmyx", "qou-dgtf", "qou-kp89", "qou-n4pv", "qou-nuxb", "qou-wdgz", "qou-z4jb"],
        "pattern": re.compile(
            r"(?:RiemannSurface|RiemannRoch|RiemannHurwitz|RiemannZeta|RiemannHypothesis|"
            r"SerreDuality|DivisorDegree|EllipticDivisor|IsElliptic|"
            r"HodgeDecomp|HodgeStar|HodgeInvolution|HarmonicForm|Dolbeault|Kahler|GaussBonnet|Weierstrass|"
            r"ArgumentPrinciple|WindingNumber|ResidueTheorem|ParallelogramContour|CauchyResidue|"
            r"HadamardFactorization|JensenFormula|Nevanlinna|BorelCaratheodory|Meromorphic|"
            r"AbelianDifferential|HolomorphicOneForm|GenusFormula|SWPeriodResidue)",
            re.I,
        ),
    },
    "M3_HYPERBOLIC_UNIFORMIZATION_3MANIFOLDS": {
        "short_label": "M3: Hyperbolic 2D/3D / Triangle Groups Δ(p,q,r) / Mostow / Ohtsuki",
        "mathlib_target": (
            "Hyperbolic 2D/3D manifolds, Fuchsian/Kleinian triangle groups Delta(p,q,r) & Poincare "
            "uniformization, Thurston hyperbolization & Mostow rigidity, Casson–Rivin constrained "
            "angle-structure concavity, SL(2,C) Chern–Simons invariant, and Ohtsuki stationary-phase / "
            "steepest-descent saddle-point asymptotics"
        ),
        "existing_beans": ["qou-5gai", "qou-322e", "qou-h2mb", "qou-i0sr", "qou-m8xt", "qou-sd8y", "qou-6x4m"],
        "pattern": re.compile(
            r"(?:TriangleGroup|Fuchsian|Kleinian|Uniformization|PoincareMetric|UpperHalfPlane|"
            r"HyperbolicManifold|Hyperbolic3Manifold|HyperbolicVolume|HyperbolicMetric|"
            r"HypMinimizer|IdealTetrahedr|IdealTriangulation|AngleStructure|RivinConcavity|"
            r"GluingEquation|ThurstonHyperbol|MostowRigidity|CuspedManifold|JSJDecomp|"
            r"DehnSurgery|Ohtsuki|SaddlePoint|StationaryPhase|SteepestDescent|Kashaev|"
            r"VolumeConjecture|ChernSimons|HyperbolicKnot|SnapPy|GeodesicUniqueness)",
            re.I,
        ),
    },
    "M4_HECKE_MARKOV_SPECHT_MACDONALD": {
        "short_label": "M4: Iwahori–Hecke H_n(q) / Hoefsmit / Ocneanu Markov / Macdonald",
        "mathlib_target": (
            "General-n Iwahori–Hecke algebras H_n(q), Coxeter/braid presentation, Hoefsmit seminormal "
            "& Murphy cellular / Kazhdan–Lusztig bases, Ocneanu–Jones–Wenzl Markov trace & "
            "Temperley–Lieb tower, Specht / RSK / skew-SYT branching, Macdonald hook-content / "
            "Demazure / Kashiwara crystals / q-Plancherel Feray–Meliot CLT, and Grobner–Shirshov diamond"
        ),
        "existing_beans": ["qou-59vq", "qou-k4oq", "qou-0cyu", "qou-1oif", "qou-1o8n", "qou-utb3", "qou-ep0a"],
        "pattern": re.compile(
            r"(?:IwahoriHecke|HeckeAlgebra|HeckeTower|HeckeBraided|HeckeConditional|HeckeCoset|"
            r"MarkovTrace|MarkovStabilization|Ocneanu|JonesWenzl|WenzlProjector|WenzlTower|"
            r"WenzlSemisimplicity|TemperleyLieb|JonesBasicConstruction|Hoefsmit|Seminormal|"
            r"JucysMurphy|MurphyBasis|CellularAlgebra|KazhdanLusztig|Specht|YoungTableau|"
            r"YoungSymmetrizer|SkewStandardYoung|RSK|HookLength|HookContent|Macdonald|"
            r"QPlancherel|PartitionFunction|FerayMeliot|Sniady|Kerov|BrundanKleshchev|KLR|"
            r"CrystalGraph|StembridgeCrystal|TypeACrystal|Demazure|GrobnerShirshov|DiamondLemma|"
            r"BraidGroupNStrand|CoxeterSwap|ArtinWedderburn|WedderburnDecomp)",
            re.I,
        ),
    },
    "M5_QUANTUM_GROUPS_RIBBON_GPMT": {
        "short_label": "M5: Quantum Groups U_q(sl_N) / R-Matrix / Ribbon MTC / GPMT Traces",
        "mathlib_target": (
            "Drinfeld–Jimbo quantum groups U_q(sl_N) & quantum Casimir, universal R-matrix & Yang–Baxter, "
            "Jimbo quantum Schur–Weyl duality, pivotal / spherical / ribbon / modular tensor categories, "
            "Reshetikhin–Turaev tangle functor, and Geer–Patureau-Mirand–Turaev (GPMT) modified traces "
            "& modified quantum dimensions"
        ),
        "existing_beans": ["qou-o9ge", "rtqd", "rtrb", "bwrt", "hkmt", "qou-ga7i", "qou-xsmr"],
        "pattern": re.compile(
            r"(?:QuantumGroup|QuantumSu2|QuantumSl|QCasimir|DrinfeldJimbo|UniversalRMatrix|"
            r"RMatrix|YangBaxter|JimboSchurWeyl|QuantumSchurWeyl|PivotalCategory|SphericalCategory|"
            r"RibbonCategory|ModularTensor|MTCTruncation|Verlinde|ReshetikhinTuraev|KauffmanBracket|"
            r"HOMFLY|JonesPolynomial|Vassiliev|ChordDiagram|Kontsevich|GPMT|ModifiedTrace|"
            r"ModifiedQuantumDim|Ambiprojectiv|NegligibleMorphism|Semisimplification|"
            r"Tannakian|Octonion|ExceptionalG2)",
            re.I,
        ),
    },
    "M6_SIEGEL_THETA_MODULAR_CURVES": {
        "short_label": "M6: Siegel H_g / Theta Characteristics / Bring S₅ / X₀(15) Periods",
        "mathlib_target": (
            "Siegel upper half-space H_g & Sp(2g,Z) modular action, Riemann theta functions & "
            "even/odd theta characteristics, Jacobian & Prym varieties, Bring's genus-4 curve S_5 "
            "automorphism representation & period matrix, modular curve X_0(15) & elliptic period "
            "isogenies, Kronecker limit formula, and polarized Epstein zeta"
        ),
        "existing_beans": ["qou-k7ad", "qou-r7qm", "5lcg"],
        "pattern": re.compile(
            r"(?:SiegelUpper|SiegelModular|SiegelTheta|PeriodMatrix|RiemannTheta|ThetaChar|"
            r"ThetaNullwert|ThetaZeroLocus|JacobianVariety|PrymVariety|Torelli|Schottky|"
            r"BringsCurve|BringSurface|KleinBring|IcosahedralBridge|Humbert|ModularCurve|"
            r"X0_15|X015|EllipticIsogeny|EllipticPeriod|PeriodLattice|KroneckerLimit|"
            r"DedekindEta|EisensteinSeries|EpsteinZeta|ChowlaSelberg)",
            re.I,
        ),
    },
    "M7_HOCHSCHILD_GERBES_STOKES_QBOREL_SDP": {
        "short_label": "M7: Hochschild HKR / Gerbes / 2-Stokes / q-Borel / Surreals / SDP",
        "mathlib_target": (
            "Hochschild homology/cohomology HH_* & HKR isomorphism, O^x-gerbe cohomology & spectral "
            "sequences, manifold differential k-forms / contact forms & Yekutieli non-abelian Stokes "
            "2-holonomy, Conway surreal / Hahn / hyperreal transfer, q-Gevrey / q-Borel–Laplace / "
            "Ramis–Sauloy alien derivations, Carleman–Frechet–Shohat moment determinacy, and conic "
            "SDP strong duality under Slater / Goldman–Tucker strict complementarity"
        ),
        "existing_beans": [
            "qou-a8rj", "qou-6ers", "qou-ghc6", "qou-jvua", "qou-vspi", "qou-pan0",
            "qou-7b7v", "qou-x1rm", "qou-yc05", "qou-9h4t", "hypr",
        ],
        "pattern": re.compile(
            r"(?:Hochschild|HKR|CyclicHomology|Gerbe|CechCohomology|CechColimit|LongExactSequence|"
            r"SpectralSequence|E2Degenerates|DifferentialForm|ContactForm|ContactDist|LeviForm|"
            r"Sobolev|NonAbelianStokes|Yekutieli|TwoHolonomy|MultiplicativeIntegral|CrossedModule|"
            r"Surreal|Hyperreal|HahnSubstrate|StandardPart|ClassicalLimitStpart|"
            r"ArchimedeanInfinitesimal|OmegaOrder|QGevrey|QBorel|BorelResummation|BorelTransform|"
            r"BorelSummable|AlienDerivation|AlienBridge|RSZIsoformal|JacksonIntegral|QDifference|"
            r"Carleman|FrechetShohat|Stieltjes|MomentProblem|StrictComplementarity|SlaterCondition|"
            r"ConicDuality|FiniteLPDuality|LPDuality|GoldmanTucker|SemidefiniteProgram|"
            r"HabiroZeta|HabiroRigidity|HabiroFlow)",
            re.I,
        ),
    },
}

# Explicit QOU physics / manuscript-conjecture / particle-calibration markers (Type P)
QOU_PHYSICS_NAME_RE = re.compile(
    r"(?:WittenKappa|BringZeroMode|Confinement|ConfinedParticle|DressedParticle|Particle|Boson|Fermion|"
    r"EmCoupling|UnifiedGauge|KnotMass|Baryon|Meson|Nucleon|Proton|Neutron|Muon|TauLepton|"
    r"Lepton|Quark|Electron|Photon|Gluon|WBoson|ZBoson|Higgs|Electroweak|Weinberg|"
    r"FineStructure|AlphaEm|Cabibbo|CKM|PMNS|Neutrino|Pion|Kaon|Hadron|ColemanGlashow|"
    r"USpin|Eightfold|ColourStabilizer|ColorTube|ColorSector|ColorElliptic|"
    r"Isotope|Nuclide|Deuteron|Deuterium|Tritium|Helium|"
    r"Lithium|Beryllium|Carbon|Oxygen|Iron|Lead|MagicNumber|ShellClosure|NobleGas|"
    r"BindingEnergy|MassFormula|SixTermMass|BorromeanMass|MassEndomorphism|VolDensity|"
    r"LambdaScale|BetaDecay|QBeta|FreeNeutron|Nuclear|Coulomb|NolenSchiffer|MirrorSplit|"
    r"Molecular|Benzene|Covalent|BondAngle|Hartree|Rydberg|Orbital|OrganicChem|"
    r"Cosmolog|BigBang|HeatDeath|DarkEnergy|Hubble|BaryonAsymmetry|Inflation|BlackHole|"
    r"Gravity|Einstein|Spacetime|Fluid|NavierStokes|Turbulence|Enstrophy|Vorticity|"
    r"Reynolds|Kolmogorov|StochasticMech|NelsonDiffusion|BornRule|MeasurementCollapse|"
    r"Cemetery|ComputationalHorizon|HorizonTransfer|PNeqNP|SubstrateClock|SingleCalibration|"
    r"ThreeCalibration|CalibrationInput|TowerSummandRealization|QuantumUniverse|"
    r"QuantumObservableUniverse|RecursiveBraneTower|Instanton|YangMills)",
    re.I,
)

QOU_PHYSICS_FIELD_RE = re.compile(
    r"(?:euler_eq\b|eulerChar\s*=\s*-\s*6|938\.27|939\.56|137\.03|105\.65|0\.51099|"
    r"\bq₀\b|\bq_0\b|\bm_e\b|\bm_p\b|\bm_n\b|\bm_μ\b|\balpha_em\b|\bVol_4_1\b)",
    re.I,
)

ALGEBRAIC_INTERFACE_LAW_NAMES = frozenset({
    "add_assoc", "add_comm", "zero_add", "add_zero", "neg_add_cancel", "add_left_neg",
    "sub_eq_add_neg", "mul_assoc", "mul_comm", "one_mul", "mul_one", "left_distrib",
    "right_distrib", "zero_mul", "mul_zero", "inv_mul_cancel", "mul_inv_cancel",
    "star_invol", "star_add", "star_mul", "bar_invol", "bar_add", "bar_mul",
    "le_refl", "le_trans", "le_antisymm", "lt_iff_le_not_le",
    "id_comp", "comp_id", "assoc", "map_id", "map_comp", "map_add", "map_mul", "map_one", "map_zero",
    "smul_add", "add_smul", "mul_smul", "one_smul", "zero_smul", "smul_zero",
    "bilin_add_left", "bilin_add_right", "bilin_smul_left", "bilin_smul_right", "bilin_symm",
})

ALGEBRAIC_INTERFACE_CARRIER_RE = re.compile(
    r"^(?:CommRingOps|CommRingCarrier|RingOps|SemiringOps|StarRingOps|InvolutionRingOps|"
    r"LaurentRingOps|FieldOps|ModuleOps|AlgebraOps|BilinearFormOps|SymmetricFormOps|"
    r"GroupoidOps|CategoryOps|MonoidalOps|PosetOps|MetricOps|NormedOps|FilteredOps|"
    r"GradedRingOps)$"
)

PHYSICS_CHAPTER_DIRS = frozenset({
    "mass-theory",
    "quantum-observable-universes",
    "predicted-spectra",
    "knots-particles-confinement",
    "information-theory",
    "mass-endomorphism",
    "braids-and-knots",
    "nuclear-interactions",
    "observations",
    "quantum-universes",
    "molecular-construction",
    "climax-volume-mass",
    "fluid-dynamics",
    "stochastic-mechanics",
    "models-of-qous",
    "organic-chemistry",
    "appendix-standard-model",
    "measurement-observation",
    "appendix-knot-periodic-table",
    "appendix-qvalues",
    "eightfold-way",
    "gravity-spacetime",
})

MATHLIB_DIRS_RE = re.compile(
    r"^(?:lean/QOU/(?:Mathlib|MathlibExt|Machinery|Foundations)/|"
    r"brings-surface/|lifting-and-descent/|q-geometric-langlands/|appendix-surreals)"
)


def classify_free_prop_fields(
    fields: list[tuple[str, str]]
) -> list[tuple[str, str]]:
    """Mirror `scripts/free-prop-field-audit.py`: detect `: Prop` fields and classify
    each as `PINNED`, `UNPINNED-FAKE-IF`, or `UNPINNED-EMPTY`.
    """
    out: list[tuple[str, str]] = []
    for fname, ftype in fields:
        if ftype.strip() != "Prop":
            continue
        f_esc = re.escape(fname)
        tok_re = re.compile(rf"\b{f_esc}\b")
        pin_re = re.compile(
            rf"(?:(?<![A-Za-z0-9_']){f_esc}\s*(?:↔|(?<![<>=!])=(?!=))"
            rf"|(?:↔|(?<![<>=!])=(?!=))\s*{f_esc}(?![A-Za-z0-9_']))"
        )
        ante_re = re.compile(rf"(?<![A-Za-z0-9_']){f_esc}\s*(?:→|->)")
        verdict = "UNPINNED-EMPTY"
        saw_ante = False
        for other_name, other_ty in fields:
            if other_name == fname or not tok_re.search(other_ty):
                continue
            if pin_re.search(other_ty):
                verdict = "PINNED"
                break
            if ante_re.search(other_ty):
                saw_ante = True
        if verdict != "PINNED" and saw_ante:
            verdict = "UNPINNED-FAKE-IF"
        out.append((fname, verdict))
    return out


def find_unconstrained_data_fields(
    data_fields: list[tuple[str, str]], prop_fields: list[tuple[str, str]]
) -> list[str]:
    """Mirror `scripts/lean-structure-field-law-audit.py`: data fields never mentioned
    in any Prop/law field's type (only meaningful when >= 1 Prop field exists).
    """
    if not prop_fields or not data_fields:
        return []
    law_text = " ".join(ft for _, ft in prop_fields)
    free_data: list[str] = []
    for dn, _ in data_fields:
        if not re.search(rf"(?<![A-Za-z0-9_.']){re.escape(dn)}(?![A-Za-z0-9_'])", law_text):
            free_data.append(dn)
    return free_data


def classify_root_cause(carrier: dict[str, Any]) -> tuple[str, str | None, str]:
    """Return `(taxonomy, mathlib_cluster_or_none, rationale)` for a carrier."""
    short = carrier["short_name"]
    fqn = carrier["fqn"]
    rel = carrier["file"]
    status = carrier["instantiation_status"]
    n_non_toy = carrier["non_toy_witness_count"]
    prop_fields = carrier["prop_fields"]
    all_field_text = " ".join(
        f"{fn} : {ft}" for fn, ft in (carrier["data_fields"] + prop_fields)
    )
    search_blob = f"{fqn} {rel} {carrier['extends']} {all_field_text} {carrier['docstring'][:400]}"

    # 1. Pure §7c universal-algebraic interface or multi-instance / concrete grounded interface
    prop_field_names = {fn for fn, _ in prop_fields}
    is_pure_alg_laws = bool(prop_field_names) and prop_field_names.issubset(
        ALGEBRAIC_INTERFACE_LAW_NAMES
    )
    if ALGEBRAIC_INTERFACE_CARRIER_RE.match(short) or is_pure_alg_laws:
        return (
            "LEGITIMATE_ALGEBRAIC_INTERFACE",
            None,
            "Universal algebraic ring/module/category/poset law interface (§7c polymorphic carrier)",
        )

    if status == "GENUINELY_INSTANTIATED":
        has_physics_claim = bool(
            QOU_PHYSICS_NAME_RE.search(fqn) or QOU_PHYSICS_FIELD_RE.search(all_field_text)
        )
        if n_non_toy >= 2 or not has_physics_claim:
            return (
                "LEGITIMATE_ALGEBRAIC_INTERFACE",
                None,
                f"Backed by {n_non_toy} concrete non-toy instance/constructor proof(s) on target carrier",
            )
        # Even when instantiated once on a QOU physics struct (e.g. a proved numerical certificate),
        # treat proved concrete data/certificate structures as Type D.
        return (
            "LEGITIMATE_ALGEBRAIC_INTERFACE",
            None,
            f"Constructed QOU certificate/bundle with {n_non_toy} proved non-toy witness(es)",
        )

    # 2. Uninstantiated or Toy-Only: distinguish QOU Physics Bridge (Type P) vs Missing Mathlib4 (Type M)
    # Explicit QOU physics/bridge check on name or field equations FIRST (captures BringZeroModeBlochClass,
    # WittenKappaGramDeterminant, ConfinementSdpDual, euler_eq : eulerChar = -6, etc.)
    if QOU_PHYSICS_NAME_RE.search(fqn) or QOU_PHYSICS_FIELD_RE.search(all_field_text):
        return (
            "QOU_BRIDGE_OR_PHYSICS_GAP",
            None,
            "QOU-specific physical identification, calibration, or conjecture premise encoded as carrier field",
        )

    # Score against cohesive Mathlib4 clusters M1..M7
    best_cluster: str | None = None
    best_score = 0
    name_file_blob = f"{fqn} {rel} {carrier['extends']}"
    for cid, meta in MATHLIB_CLUSTERS.items():
        pat = meta["pattern"]
        # Weight matches in FQN/filepath/extends 3x higher than body/docstring mentions
        score = 3 * len(pat.findall(name_file_blob)) + len(pat.findall(all_field_text + " " + carrier["docstring"][:300]))
        if score > best_score:
            best_score = score
            best_cluster = cid

    if best_cluster is not None and best_score > 0:
        return (
            "MISSING_MATHLIB_INFRA",
            best_cluster,
            f"Standard pure-math infrastructure absent from Mathlib v4.24.0 ({MATHLIB_CLUSTERS[best_cluster]['short_label']})",
        )

    # Directory-based fallback when no keyword fired
    top_dir = Path(rel).parts[0]
    if top_dir in PHYSICS_CHAPTER_DIRS or any(
        seg in rel
        for seg in (
            "/Mass/",
            "/AtomicMass/",
            "/ParticleInteractions/",
            "/Interactions/",
            "/Molecular/",
            "/FluidDynamics/",
            "/Eightfold/",
            "/QBeta/",
            "/Cosmology/",
            "/QuantumObservableUniverse/",
        )
    ):
        return (
            "QOU_BRIDGE_OR_PHYSICS_GAP",
            None,
            "QOU domain/chapter premise carrier without concrete realization",
        )

    # Remaining pure-math carriers in Mathlib/MathlibExt/Machinery/Foundations/Archimedean/BraidKnot/Torsion
    if "/Archimedean/" in rel:
        fallback_cluster = "M3_HYPERBOLIC_UNIFORMIZATION_3MANIFOLDS"
    elif "/BraidKnot/" in rel or "/Torsion/" in rel:
        fallback_cluster = "M4_HECKE_MARKOV_SPECHT_MACDONALD"
    elif "brings-surface" in rel:
        fallback_cluster = "M6_SIEGEL_THETA_MODULAR_CURVES"
    else:
        fallback_cluster = "M7_HOCHSCHILD_GERBES_STOKES_QBOREL_SDP"

    if MATHLIB_DIRS_RE.search(rel) or "/Archimedean/" in rel or "/BraidKnot/" in rel or "/Torsion/" in rel:
        return (
            "MISSING_MATHLIB_INFRA",
            fallback_cluster,
            f"Pure-math structural gap in {Path(rel).parent.as_posix()} ({MATHLIB_CLUSTERS[fallback_cluster]['short_label']})",
        )

    return (
        "QOU_BRIDGE_OR_PHYSICS_GAP",
        None,
        "Uninstantiated QOU manuscript premise carrier",
    )


def classify_standalone_axiom_or_opaque(
    rel: str, name: str, sig: str, doc: str
) -> tuple[str, str | None]:
    blob = f"{name} {rel} {sig} {doc[:300]}"
    if QOU_PHYSICS_NAME_RE.search(name) or QOU_PHYSICS_FIELD_RE.search(sig):
        return "QOU_BRIDGE_OR_PHYSICS_GAP", None
    best_cluster: str | None = None
    best_score = 0
    for cid, meta in MATHLIB_CLUSTERS.items():
        pat = meta["pattern"]
        sc = 3 * len(pat.findall(f"{name} {rel}")) + len(pat.findall(blob))
        if sc > best_score:
            best_score = sc
            best_cluster = cid
    if best_cluster is not None and best_score > 0:
        return "MISSING_MATHLIB_INFRA", best_cluster
    if Path(rel).parts[0] in PHYSICS_CHAPTER_DIRS:
        return "QOU_BRIDGE_OR_PHYSICS_GAP", None
    return "MISSING_MATHLIB_INFRA", "M7_HOCHSCHILD_GERBES_STOKES_QBOREL_SDP"


# ── Main Corpus Scanner ──────────────────────────────────────────────────────


def run_audit() -> dict[str, Any]:
    lean_files = sorted(
        p for p in QOU_FOLIO_ROOT.rglob("*.lean") if ".lake" not in p.parts
    )

    cleaned_by_file: dict[str, str] = {}
    docs_by_file: dict[str, dict[int, str]] = {}
    imports_by_file: dict[str, list[str]] = {}
    mod_to_file: dict[str, str] = {}

    n_library_files = 0
    n_chapter_files = 0
    sorry_count = 0
    native_decide_count = 0
    true_vacuity_count = 0

    sorry_re = re.compile(r"(?<![\w.])sorry(?![\w])")
    native_re = re.compile(r"(?<![\w.])native_decide(?![\w])")
    true_vac_re = re.compile(r":\s*True\s*:=")

    for f in lean_files:
        rel = f.relative_to(QOU_FOLIO_ROOT).as_posix()
        if Path(rel).parts[0] == "lean":
            n_library_files += 1
        else:
            n_chapter_files += 1
        raw = f.read_text(encoding="utf-8", errors="replace")
        clean, doc_map = strip_comments_and_extract_docstrings(raw)
        cleaned_by_file[rel] = clean
        docs_by_file[rel] = doc_map
        imports_by_file[rel] = re.findall(r"^\s*import\s+([\w.]+)", clean, re.M)

        if rel == "lean/QOU.lean":
            mod_to_file["QOU"] = rel
        elif rel.startswith("lean/QOU/") and rel.endswith(".lean"):
            mod = "QOU." + rel[len("lean/QOU/") : -5].replace("/", ".")
            mod_to_file[mod] = rel

        for ln in clean.splitlines():
            if sorry_re.search(ln):
                sorry_count += 1
            if native_re.search(ln):
                native_decide_count += 1
            if true_vac_re.search(ln):
                true_vacuity_count += 1

    # Transitive import closure across QOU modules
    trans_imports: dict[str, set[str]] = {}

    def get_trans(rel: str) -> set[str]:
        if rel in trans_imports:
            return trans_imports[rel]
        vis = {rel}
        stack = [
            mod_to_file[m]
            for m in imports_by_file.get(rel, [])
            if m in mod_to_file
        ]
        while stack:
            cur = stack.pop()
            if cur not in vis:
                vis.add(cur)
                for m in imports_by_file.get(cur, []):
                    if m in mod_to_file and mod_to_file[m] not in vis:
                        stack.append(mod_to_file[m])
        trans_imports[rel] = vis
        return vis

    for rel in cleaned_by_file:
        get_trans(rel)

    # Pass 1: Extract all `class`, `structure`, `axiom`, and `opaque` declarations
    carriers: list[dict[str, Any]] = []
    standalone_axioms: list[dict[str, Any]] = []
    total_raw_classes = 0
    total_raw_structures = 0
    pure_data_structures_excluded = 0

    for rel, clean in cleaned_by_file.items():
        lines = clean.splitlines()
        doc_map = docs_by_file[rel]
        scope = "library" if Path(rel).parts[0] == "lean" else "chapter"
        ns_stack: list[str] = []
        i = 0
        while i < len(lines):
            ln_raw = lines[i]
            ns_m = re.match(r"^\s*namespace\s+([\w.]+)", ln_raw)
            end_m = re.match(r"^\s*end\s+([\w.]+)", ln_raw)
            if ns_m:
                ns_stack.append(ns_m.group(1))
                i += 1
                continue
            if end_m:
                if ns_stack and ns_stack[-1] == end_m.group(1):
                    ns_stack.pop()
                i += 1
                continue

            ax_m = AXIOM_OPAQUE_RE.match(ln_raw)
            if ax_m:
                base_ind = len(ax_m.group("indent"))
                kw = ax_m.group("kw")
                ax_name = ax_m.group("name")
                rest = ax_m.group("rest").strip()
                u = i + 1
                while u < min(i + 8, len(lines)):
                    nxt = lines[u]
                    if not nxt.strip():
                        break
                    if len(nxt) - len(nxt.lstrip()) <= base_ind:
                        break
                    rest += " " + nxt.strip()
                    u += 1
                doc = doc_map.get(i, "") or doc_map.get(i + 1, "")
                ns_prefix = ".".join(ns_stack)
                fqn = f"{ns_prefix}.{ax_name}" if ns_prefix else ax_name
                tax, clus = classify_standalone_axiom_or_opaque(rel, fqn, rest, doc)
                standalone_axioms.append({
                    "file": rel,
                    "line": i + 1,
                    "scope": scope,
                    "kind": kw,
                    "fqn": fqn,
                    "short_name": ax_name.split(".")[-1],
                    "signature": rest[:240],
                    "root_cause_taxonomy": tax,
                    "mathlib_cluster": clus,
                })
                i = u
                continue

            m = CARRIER_RE.match(ln_raw)
            if not m:
                i += 1
                continue

            base_ind = len(m.group("indent"))
            kind = m.group("kind")
            if kind == "class":
                total_raw_classes += 1
            else:
                total_raw_structures += 1

            name = m.group("name")
            hdr = m.group("hdr")
            start_line = i + 1
            doc = doc_map.get(i, "") or doc_map.get(i + 1, "")

            k = i
            while (
                k < min(i + 14, len(lines))
                and "where" not in lines[k]
                and ":=" not in lines[k]
            ):
                if k > i:
                    hdr += " " + lines[k].strip()
                k += 1
            has_where = k < min(i + 14, len(lines)) and "where" in lines[k]
            if has_where and k > i:
                hdr += " " + lines[k].split("where", 1)[0].strip()

            fields: list[tuple[str, str]] = []
            j = (k + 1) if has_where else (i + 1)
            if has_where:
                while j < len(lines):
                    ln = lines[j]
                    if not ln.strip():
                        j += 1
                        continue
                    ind = len(ln) - len(ln.lstrip())
                    if ind <= base_ind:
                        break
                    stripped = ln.lstrip()
                    if stripped.startswith("|") or stripped.startswith("deriving"):
                        j += 1
                        continue
                    fm = FIELD_RE.match(ln)
                    if fm and ":=" not in fm.group("ftype"):
                        fname = fm.group("fname")
                        ftype = fm.group("ftype").strip()
                        f_ind = len(fm.group("indent"))
                        u = j + 1
                        while u < len(lines):
                            nxt = lines[u]
                            if not nxt.strip():
                                u += 1
                                continue
                            n_ind = len(nxt) - len(nxt.lstrip())
                            if n_ind <= base_ind or nxt.lstrip().startswith("deriving"):
                                break
                            if FIELD_RE.match(nxt) and n_ind <= f_ind:
                                break
                            ftype = (ftype + " " + nxt.strip()).strip()
                            u += 1
                        fields.append((fname, ftype))
                        j = u
                        continue
                    j += 1

            extends_m = re.search(r"\bextends\s+([^\n:=]+)", hdr)
            extends_str = extends_m.group(1).strip() if extends_m else ""
            is_prop_carrier = bool(re.search(r":\s*Prop\b", hdr))
            prop_fields = [(fn, ft) for fn, ft in fields if is_prop_field_type(ft)]
            data_fields = [(fn, ft) for fn, ft in fields if not is_prop_field_type(ft)]

            if kind == "structure" and not prop_fields and not is_prop_carrier and not extends_str:
                pure_data_structures_excluded += 1
                i = max(j, i + 1)
                continue

            ns_prefix = ".".join(ns_stack)
            fqn = f"{ns_prefix}.{name}" if ns_prefix else name
            free_props = classify_free_prop_fields(fields)
            free_data = find_unconstrained_data_fields(data_fields, prop_fields)

            carriers.append({
                "id": len(carriers),
                "file": rel,
                "line": start_line,
                "scope": scope,
                "kind": kind,
                "name": name,
                "fqn": fqn,
                "short_name": name.split(".")[-1],
                "is_prop_carrier": is_prop_carrier,
                "extends": extends_str,
                "data_fields": data_fields,
                "prop_fields": prop_fields,
                "data_field_names": {fn for fn, _ in data_fields},
                "free_prop_fields": free_props,
                "unconstrained_data_fields": free_data,
                "docstring": doc,
            })
            i = max(j, i + 1)

    by_short: dict[str, list[int]] = defaultdict(list)
    for c in carriers:
        by_short[c["short_name"]].append(c["id"])

    def resolve_carrier(sh: str, use_file: str) -> list[int]:
        cands = by_short.get(sh, [])
        if not cands:
            return []
        same = [cid for cid in cands if carriers[cid]["file"] == use_file]
        if same:
            return same
        vis = trans_imports.get(use_file, {use_file})
        imp = [cid for cid in cands if carriers[cid]["file"] in vis]
        if imp:
            return imp
        # If unique across the entire 4,226-file corpus and length >= 4 (not a 1-letter var), allow match
        if len(cands) == 1 and len(sh) >= 4:
            return cands
        return []

    # Pass 2: Scan all `instance`, `def`, `abbrev`, `theorem`, `lemma`, `example` declarations
    witness_edges: dict[int, list[dict[str, Any]]] = defaultdict(list)
    theorem_consumers: Counter[int] = Counter()
    def_consumers: Counter[int] = Counter()

    for rel, clean in cleaned_by_file.items():
        lines = clean.splitlines()
        n = len(lines)
        i = 0
        while i < n:
            m = TOP_DECL_RE.match(lines[i])
            if not m:
                i += 1
                continue
            base_ind = len(m.group("indent"))
            kw = m.group("kw")
            start_i = i
            j = i + 1
            while j < n:
                ln = lines[j]
                if not ln.strip():
                    j += 1
                    continue
                if len(ln) - len(ln.lstrip()) <= base_ind:
                    break
                j += 1
            block = "\n".join(lines[start_i:j])
            sp = re.search(r"\bwhere\b|:=", block)
            sig = block[: sp.start()] if sp else block
            body = block[sp.end() :] if sp else ""

            colon_pos = -1
            d_par = d_brk = d_brc = 0
            for pos, ch in enumerate(sig):
                if ch == "(":
                    d_par += 1
                elif ch == ")":
                    d_par = max(0, d_par - 1)
                elif ch == "[":
                    d_brk += 1
                elif ch == "]":
                    d_brk = max(0, d_brk - 1)
                elif ch == "{":
                    d_brc += 1
                elif ch == "}":
                    d_brc = max(0, d_brc - 1)
                elif ch == ":" and d_par == 0 and d_brk == 0 and d_brc == 0:
                    colon_pos = pos
            binders_part = sig[:colon_pos] if colon_pos >= 0 else sig
            ret_type = sig[colon_pos + 1 :].strip() if colon_pos >= 0 else ""

            hyp_zone = binders_part
            if "→" in ret_type or "->" in ret_type:
                parts_arr = re.split(r"→|->", ret_type)
                hyp_zone += " " + " ".join(parts_arr[:-1])

            guard_cids: set[int] = set()
            for tok in set(re.findall(r"[A-Za-z_][A-Za-z0-9_']*", hyp_zone)):
                if tok in by_short:
                    for gcid in resolve_carrier(tok, rel):
                        guard_cids.add(gcid)
                        if kw in ("theorem", "lemma"):
                            theorem_consumers[gcid] += 1
                        elif kw in ("def", "abbrev"):
                            def_consumers[gcid] += 1

            target_cids: list[int] = []
            if kw == "instance" and ret_type:
                final_ret = re.split(r"→|->", ret_type)[-1].strip()
                hm = re.match(r"(?:∀[^,]+,\s*)*@?([A-Za-z_][A-Za-z0-9_'.]*)", final_ret)
                if hm:
                    sh = hm.group(1).split(".")[-1]
                    if sh in by_short:
                        target_cids = [
                            c for c in resolve_carrier(sh, rel) if c not in guard_cids
                        ]
            elif kw in ("def", "abbrev", "theorem", "lemma", "example"):
                if ret_type:
                    final_ret = re.split(r"→|->", ret_type)[-1].strip()
                    hm = re.match(
                        r"(?:Nonempty\s+\(?|∃\s+[^:]+:\s*)?@?([A-Za-z_][A-Za-z0-9_'.]*)",
                        final_ret,
                    )
                    if hm:
                        sh = hm.group(1).split(".")[-1]
                        if sh in by_short:
                            target_cids = [
                                c for c in resolve_carrier(sh, rel) if c not in guard_cids
                            ]
                for mk_m in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_']*)\.mk\b", body):
                    sh = mk_m.group(1)
                    if sh in by_short:
                        for c in resolve_carrier(sh, rel):
                            if c not in guard_cids and c not in target_cids:
                                target_cids.append(c)

            for tcid in target_cids:
                cobj = carriers[tcid]
                is_toy = bool(TOY_TYPE_RE.search(ret_type))
                if not is_toy:
                    assigns = re.findall(
                        r"^\s+([A-Za-z_α-ωΑ-ΩΔΛΣΠΦΨΩ][A-Za-z0-9_'₀-₉α-ωΑ-Ω]*)\s*[^:=\n]*:=\s*(.+)$",
                        body,
                        re.M,
                    )
                    if assigns:
                        data_assigns = [
                            (fn, val.strip())
                            for fn, val in assigns
                            if fn in cobj["data_field_names"]
                        ]
                        if data_assigns and all(
                            TRIVIAL_VAL_RE.match(val) for _, val in data_assigns
                        ):
                            is_toy = True
                        elif not cobj["data_field_names"]:
                            if any(val.strip() == "True" for _, val in assigns):
                                is_toy = True
                    else:
                        b_strip = body.strip()
                        if b_strip in ("⟨⟩", "{}") or re.fullmatch(
                            r"⟨(?:\s*(?:0|\(0\s*:[^)]+\)|True|trivial|rfl|PUnit\.unit|\(\))\s*,?)+⟩",
                            b_strip,
                        ):
                            if cobj["data_field_names"]:
                                is_toy = True

                witness_edges[tcid].append({
                    "file": rel,
                    "line": start_i + 1,
                    "kw": kw,
                    "is_toy": is_toy,
                    "guards": guard_cids,
                })
            i = j

    # Pass 3: Transitive grounding fixed-point (catches axiom-shim forwarding!)
    # Note: §7c polymorphic algebraic interfaces (e.g. CommRingOps R) are valid typeclass bounds
    # on generic proofs, NOT uninstantiated axiom shims blocking grounding.
    polymorphic_alg_cids = {
        c["id"]
        for c in carriers
        if ALGEBRAIC_INTERFACE_CARRIER_RE.match(c["short_name"])
        or (
            bool(c["prop_fields"])
            and {fn for fn, _ in c["prop_fields"]}.issubset(ALGEBRAIC_INTERFACE_LAW_NAMES)
        )
    }

    grounded: set[int] = set()
    changed = True
    while changed:
        changed = False
        for cid in range(len(carriers)):
            if cid in grounded:
                continue
            for e in witness_edges.get(cid, []):
                if not e["is_toy"] and all(
                    (g in grounded or g in polymorphic_alg_cids) for g in e["guards"]
                ):
                    grounded.add(cid)
                    changed = True
                    break

    toy_grounded: set[int] = set()
    changed = True
    while changed:
        changed = False
        for cid in range(len(carriers)):
            if cid in grounded or cid in toy_grounded:
                continue
            for e in witness_edges.get(cid, []):
                if all(
                    (g in grounded or g in toy_grounded or g in polymorphic_alg_cids)
                    for g in e["guards"]
                ):
                    toy_grounded.add(cid)
                    changed = True
                    break

    # Pass 4: Finalize per-carrier status & root-cause taxonomy
    records_out: list[dict[str, Any]] = []
    status_counter: Counter[str] = Counter()
    taxonomy_counter: Counter[str] = Counter()
    matrix_counter: Counter[tuple[str, str]] = Counter()
    cluster_counter: Counter[str] = Counter()
    cluster_gap_counter: Counter[str] = Counter()
    cluster_consumer_counter: Counter[str] = Counter()

    n_shim_guarded = 0
    n_with_free_prop = 0
    n_with_free_data = 0

    for c in carriers:
        cid = c["id"]
        edges = witness_edges.get(cid, [])
        non_toy_grounded_edges = [
            e
            for e in edges
            if not e["is_toy"]
            and all((g in grounded or g in polymorphic_alg_cids) for g in e["guards"])
        ]
        if cid in grounded:
            status = "GENUINELY_INSTANTIATED"
        elif cid in toy_grounded:
            status = "TOY_ONLY_INSTANCE"
        else:
            status = "UNINSTANTIATED_AXIOM_CLASS"

        is_shim_guarded = status == "UNINSTANTIATED_AXIOM_CLASS" and len(edges) > 0
        if is_shim_guarded:
            n_shim_guarded += 1

        if any(v != "PINNED" for _, v in c["free_prop_fields"]):
            n_with_free_prop += 1
        if c["unconstrained_data_fields"]:
            n_with_free_data += 1

        c["instantiation_status"] = status
        c["non_toy_witness_count"] = len(non_toy_grounded_edges)
        c["raw_witness_count"] = len(edges)
        c["is_shim_guarded"] = is_shim_guarded
        c["theorem_consumers"] = theorem_consumers[cid]
        c["def_consumers"] = def_consumers[cid]
        c["total_consumers"] = theorem_consumers[cid] + def_consumers[cid]

        tax, clus, rationale = classify_root_cause(c)
        c["root_cause_taxonomy"] = tax
        c["mathlib_cluster"] = clus
        c["rationale"] = rationale

        status_counter[status] += 1
        taxonomy_counter[tax] += 1
        matrix_counter[(status, tax)] += 1
        if clus is not None:
            cluster_counter[clus] += 1
            if status in ("UNINSTANTIATED_AXIOM_CLASS", "TOY_ONLY_INSTANCE"):
                cluster_gap_counter[clus] += 1
                cluster_consumer_counter[clus] += c["total_consumers"]

        records_out.append({
            "file": c["file"],
            "line": c["line"],
            "scope": c["scope"],
            "kind": c["kind"],
            "fqn": c["fqn"],
            "short_name": c["short_name"],
            "is_prop_carrier": c["is_prop_carrier"],
            "extends": c["extends"],
            "n_data_fields": len(c["data_fields"]),
            "n_prop_fields": len(c["prop_fields"]),
            "prop_field_names": [fn for fn, _ in c["prop_fields"][:12]],
            "free_prop_fields": [
                {"field": fn, "verdict": vd} for fn, vd in c["free_prop_fields"]
            ],
            "unconstrained_data_fields": c["unconstrained_data_fields"],
            "instantiation_status": status,
            "is_shim_guarded": is_shim_guarded,
            "raw_witness_count": c["raw_witness_count"],
            "non_toy_witness_count": c["non_toy_witness_count"],
            "theorem_consumers": c["theorem_consumers"],
            "def_consumers": c["def_consumers"],
            "total_consumers": c["total_consumers"],
            "root_cause_taxonomy": tax,
            "mathlib_cluster": clus,
            "rationale": rationale,
        })

    # Summarize standalone `axiom` / `opaque` declarations
    ax_by_kind = Counter(a["kind"] for a in standalone_axioms)
    ax_by_tax = Counter(a["root_cause_taxonomy"] for a in standalone_axioms)
    ax_by_cluster = Counter(
        a["mathlib_cluster"] for a in standalone_axioms if a["mathlib_cluster"]
    )

    # Build per-cluster summaries for M1..M7
    cluster_summaries: dict[str, Any] = {}
    for cid, meta in MATHLIB_CLUSTERS.items():
        c_rows = [
            r
            for r in records_out
            if r["mathlib_cluster"] == cid
            and r["instantiation_status"] in ("UNINSTANTIATED_AXIOM_CLASS", "TOY_ONLY_INSTANCE")
        ]
        c_rows_sorted = sorted(
            c_rows,
            key=lambda r: (-r["total_consumers"], -r["n_prop_fields"], r["file"], r["line"]),
        )
        c_axioms = [a for a in standalone_axioms if a["mathlib_cluster"] == cid]
        cluster_summaries[cid] = {
            "short_label": meta["short_label"],
            "mathlib_target": meta["mathlib_target"],
            "existing_beans": meta["existing_beans"],
            "uninstantiated_or_toy_carriers": len(c_rows),
            "uninstantiated_classes": sum(
                1 for r in c_rows if r["kind"] == "class" and r["instantiation_status"] == "UNINSTANTIATED_AXIOM_CLASS"
            ),
            "uninstantiated_structures": sum(
                1 for r in c_rows if r["kind"] == "structure" and r["instantiation_status"] == "UNINSTANTIATED_AXIOM_CLASS"
            ),
            "toy_only_carriers": sum(
                1 for r in c_rows if r["instantiation_status"] == "TOY_ONLY_INSTANCE"
            ),
            "standalone_axioms": sum(1 for a in c_axioms if a["kind"] == "axiom"),
            "standalone_opaques": sum(1 for a in c_axioms if a["kind"] == "opaque"),
            "total_downstream_consumers": sum(r["total_consumers"] for r in c_rows),
            "total_prop_fields": sum(r["n_prop_fields"] for r in c_rows),
            "distinct_files": len({r["file"] for r in c_rows}),
            "top_carriers": c_rows_sorted[:25],
        }

    physics_gap_rows = sorted(
        [
            r
            for r in records_out
            if r["root_cause_taxonomy"] == "QOU_BRIDGE_OR_PHYSICS_GAP"
            and r["instantiation_status"] in ("UNINSTANTIATED_AXIOM_CLASS", "TOY_ONLY_INSTANCE")
        ],
        key=lambda r: (-r["total_consumers"], -r["n_prop_fields"], r["file"], r["line"]),
    )

    toy_only_rows = sorted(
        [r for r in records_out if r["instantiation_status"] == "TOY_ONLY_INSTANCE"],
        key=lambda r: (-r["total_consumers"], r["file"], r["line"]),
    )

    return {
        "corpus_scope": {
            "root": "folio/quantum-observable-universe",
            "total_lean_files": len(lean_files),
            "library_lean_files": n_library_files,
            "chapter_lean_files": n_chapter_files,
            "total_raw_classes": total_raw_classes,
            "total_raw_structures": total_raw_structures,
            "pure_data_structures_excluded": pure_data_structures_excluded,
            "audited_axiom_or_law_carriers": len(records_out),
            "comment_stripped_sorry_lines": sorry_count,
            "comment_stripped_native_decide_lines": native_decide_count,
            "comment_stripped_true_vacuity_lines": true_vacuity_count,
            "standalone_axiom_declarations": ax_by_kind["axiom"],
            "standalone_opaque_declarations": ax_by_kind["opaque"],
        },
        "instantiation_summary": {
            "UNINSTANTIATED_AXIOM_CLASS": status_counter["UNINSTANTIATED_AXIOM_CLASS"],
            "TOY_ONLY_INSTANCE": status_counter["TOY_ONLY_INSTANCE"],
            "GENUINELY_INSTANTIATED": status_counter["GENUINELY_INSTANTIATED"],
            "shim_guarded_uninstantiated": n_shim_guarded,
            "carriers_with_unpinned_free_prop_field": n_with_free_prop,
            "carriers_with_unconstrained_data_field": n_with_free_data,
        },
        "taxonomy_summary": {
            "MISSING_MATHLIB_INFRA": taxonomy_counter["MISSING_MATHLIB_INFRA"],
            "QOU_BRIDGE_OR_PHYSICS_GAP": taxonomy_counter["QOU_BRIDGE_OR_PHYSICS_GAP"],
            "LEGITIMATE_ALGEBRAIC_INTERFACE": taxonomy_counter["LEGITIMATE_ALGEBRAIC_INTERFACE"],
        },
        "status_by_taxonomy_matrix": {
            f"{st}__{tx}": cnt for (st, tx), cnt in sorted(matrix_counter.items())
        },
        "standalone_axiom_opaque_summary": {
            "by_kind": dict(ax_by_kind),
            "by_taxonomy": dict(ax_by_tax),
            "by_mathlib_cluster": dict(ax_by_cluster),
            "declarations": standalone_axioms,
        },
        "mathlib_clusters": cluster_summaries,
        "physics_bridge_gap_summary": {
            "uninstantiated_or_toy_carriers": len(physics_gap_rows),
            "uninstantiated_classes": sum(
                1 for r in physics_gap_rows if r["kind"] == "class" and r["instantiation_status"] == "UNINSTANTIATED_AXIOM_CLASS"
            ),
            "uninstantiated_structures": sum(
                1 for r in physics_gap_rows if r["kind"] == "structure" and r["instantiation_status"] == "UNINSTANTIATED_AXIOM_CLASS"
            ),
            "toy_only_carriers": sum(
                1 for r in physics_gap_rows if r["instantiation_status"] == "TOY_ONLY_INSTANCE"
            ),
            "standalone_axioms": sum(
                1 for a in standalone_axioms if a["root_cause_taxonomy"] == "QOU_BRIDGE_OR_PHYSICS_GAP" and a["kind"] == "axiom"
            ),
            "standalone_opaques": sum(
                1 for a in standalone_axioms if a["root_cause_taxonomy"] == "QOU_BRIDGE_OR_PHYSICS_GAP" and a["kind"] == "opaque"
            ),
            "total_downstream_consumers": sum(r["total_consumers"] for r in physics_gap_rows),
            "total_prop_fields": sum(r["n_prop_fields"] for r in physics_gap_rows),
            "distinct_files": len({r["file"] for r in physics_gap_rows}),
            "top_carriers": physics_gap_rows[:40],
        },
        "toy_only_carriers": toy_only_rows,
        "carriers": records_out,
    }


def _pct_str(num: int, den: int) -> str:
    if den == 0:
        return "0.0%"
    val = (Decimal(num) * Decimal(100)) / Decimal(den)
    return f"{val:.1f}%"


def print_ascii_report(res: dict[str, Any]) -> None:
    cs = res["corpus_scope"]
    ins = res["instantiation_summary"]
    tax = res["taxonomy_summary"]
    mat = res["status_by_taxonomy_matrix"]

    print("=" * 108)
    print("QOU LEAN 4 AXIOM-FIELD & MISSING MATHLIB4 INFRASTRUCTURE AUDIT")
    print("=" * 108)
    print(
        f"  Scope: {cs['root']}  |  .lean files: {cs['total_lean_files']} "
        f"(library: {cs['library_lean_files']}, chapters: {cs['chapter_lean_files']})"
    )
    print(
        f"  Raw declarations : {cs['total_raw_classes']} classes, "
        f"{cs['total_raw_structures']} structures "
        f"({cs['pure_data_structures_excluded']} pure-data structs excluded -> "
        f"{cs['audited_axiom_or_law_carriers']} audited carriers)"
    )
    print(
        f"  Standalone       : {cs['standalone_axiom_declarations']} `axiom`, "
        f"{cs['standalone_opaque_declarations']} `opaque`, "
        f"{cs['comment_stripped_sorry_lines']} real `sorry`, "
        f"{cs['comment_stripped_native_decide_lines']} `native_decide`"
    )
    print(
        f"  Cross-audit hits : {ins['shim_guarded_uninstantiated']} axiom-shim guarded, "
        f"{ins['carriers_with_unpinned_free_prop_field']} unpinned `: Prop` carriers, "
        f"{ins['carriers_with_unconstrained_data_field']} with unconstrained data fields"
    )
    print()

    print("-" * 108)
    print(
        f"TABLE 1: INSTANTIATION STATUS x ROOT-CAUSE TAXONOMY MATRIX "
        f"({cs['audited_axiom_or_law_carriers']:,} AUDITED CARRIERS)"
    )
    print("-" * 108)
    hdr = f"{'Instantiation Status':<30} | {'Type M (Mathlib Gap)':>20} | {'Type P (QOU Bridge)':>20} | {'Type D (Alg Interf)':>20} | {'Total':>8}"
    print(hdr)
    print("-" * 108)
    for st in ("UNINSTANTIATED_AXIOM_CLASS", "TOY_ONLY_INSTANCE", "GENUINELY_INSTANTIATED"):
        m_v = mat.get(f"{st}__MISSING_MATHLIB_INFRA", 0)
        p_v = mat.get(f"{st}__QOU_BRIDGE_OR_PHYSICS_GAP", 0)
        d_v = mat.get(f"{st}__LEGITIMATE_ALGEBRAIC_INTERFACE", 0)
        tot = m_v + p_v + d_v
        print(f"{st:<30} | {m_v:>20d} | {p_v:>20d} | {d_v:>20d} | {tot:>8d}")
    print("-" * 108)
    print(
        f"{'TOTAL':<30} | {tax['MISSING_MATHLIB_INFRA']:>20d} | "
        f"{tax['QOU_BRIDGE_OR_PHYSICS_GAP']:>20d} | "
        f"{tax['LEGITIMATE_ALGEBRAIC_INTERFACE']:>20d} | "
        f"{cs['audited_axiom_or_law_carriers']:>8d}"
    )
    print()

    print("-" * 108)
    print("TABLE 2: MISSING MATHLIB4 INFRASTRUCTURE CLUSTERS (M1..M7) + QOU PHYSICS BRIDGE (P1)")
    print("-" * 108)
    print(
        f"{'Cluster':<50} | {'Carriers':>8} | {'Cls/Str/Toy':>13} | {'Ax/Opq':>7} | {'PropFlds':>8} | {'Consumers':>9}"
    )
    print("-" * 108)
    for cid, csum in res["mathlib_clusters"].items():
        cst = f"{csum['uninstantiated_classes']}/{csum['uninstantiated_structures']}/{csum['toy_only_carriers']}"
        ao = f"{csum['standalone_axioms']}/{csum['standalone_opaques']}"
        print(
            f"{csum['short_label'][:50]:<50} | {csum['uninstantiated_or_toy_carriers']:>8d} | "
            f"{cst:>13} | {ao:>7} | {csum['total_prop_fields']:>8d} | {csum['total_downstream_consumers']:>9d}"
        )
    psum = res["physics_bridge_gap_summary"]
    pcst = f"{psum['uninstantiated_classes']}/{psum['uninstantiated_structures']}/{psum['toy_only_carriers']}"
    pao = f"{psum['standalone_axioms']}/{psum['standalone_opaques']}"
    print("-" * 108)
    print(
        f"{'P1: QOU Physics / Calibration / Bridge Premises':<50} | {psum['uninstantiated_or_toy_carriers']:>8d} | "
        f"{pcst:>13} | {pao:>7} | {psum['total_prop_fields']:>8d} | {psum['total_downstream_consumers']:>9d}"
    )
    print("-" * 108)
    print()

    print("-" * 108)
    print("TABLE 3: TOP HIGH-CONSUMER UNINSTANTIATED / TOY CARRIERS PER MATHLIB4 CLUSTER (M1..M7)")
    print("-" * 108)
    for cid, csum in res["mathlib_clusters"].items():
        print(f"  [{csum['short_label']}] (existing beans: {', '.join(csum['existing_beans'])})")
        for r in csum["top_carriers"][:6]:
            tag = "TOY" if r["instantiation_status"] == "TOY_ONLY_INSTANCE" else ("SHIM" if r["is_shim_guarded"] else "UNIN")
            loc = f"{r['file']}:{r['line']}"
            print(
                f"    {tag:<4} {r['kind']:<9} {r['short_name'][:32]:<32} "
                f"cons={r['total_consumers']:<3d} prop={r['n_prop_fields']:<2d} {loc}"
            )
        print()

    print("-" * 108)
    print("TABLE 4: TOP HIGH-CONSUMER QOU PHYSICS-BRIDGE AXIOM CARRIERS (TYPE P)")
    print("-" * 108)
    for r in psum["top_carriers"][:18]:
        tag = "TOY" if r["instantiation_status"] == "TOY_ONLY_INSTANCE" else ("SHIM" if r["is_shim_guarded"] else "UNIN")
        loc = f"{r['file']}:{r['line']}"
        print(
            f"  {tag:<4} {r['kind']:<9} {r['short_name'][:34]:<34} "
            f"cons={r['total_consumers']:<3d} prop={r['n_prop_fields']:<2d} {loc}"
        )
    print("=" * 108)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--quiet", action="store_true", help="Suppress full ASCII tables on stdout."
    )
    args = parser.parse_args(argv)

    res = run_audit()
    if not args.quiet:
        print_ascii_report(res)

    cs = res["corpus_scope"]
    ins = res["instantiation_summary"]
    tax = res["taxonomy_summary"]

    sum_status = (
        ins["UNINSTANTIATED_AXIOM_CLASS"]
        + ins["TOY_ONLY_INSTANCE"]
        + ins["GENUINELY_INSTANTIATED"]
    )
    sum_tax = (
        tax["MISSING_MATHLIB_INFRA"]
        + tax["QOU_BRIDGE_OR_PHYSICS_GAP"]
        + tax["LEGITIMATE_ALGEBRAIC_INTERFACE"]
    )

    builder = (
        WitnessBuilder("lean-axiom-field-and-mathlib-gap-audit", engine="python")
        .set_description(
            "Comprehensive AST & import-graph audit of all Lean 4 `class`, `structure`, "
            "`axiom`, and `opaque` declarations across `folio/quantum-observable-universe/` "
            "(both `lean/` library and chapter `.lean` files), classifying each declaration "
            "by instantiation status (`UNINSTANTIATED_AXIOM_CLASS`, `TOY_ONLY_INSTANCE`, "
            "`GENUINELY_INSTANTIATED`) and root-cause taxonomy (`MISSING_MATHLIB_INFRA` "
            "clusters `M1..M7`, `QOU_BRIDGE_OR_PHYSICS_GAP`, `LEGITIMATE_ALGEBRAIC_INTERFACE`)."
        )
        .add_parameter("scope_root", cs["root"])
        .add_parameter("total_lean_files", cs["total_lean_files"])
        .add_parameter("audited_carriers", cs["audited_axiom_or_law_carriers"])
        .add_assertion(
            "status_partition_exhaustive",
            computed=sum_status,
            expected=cs["audited_axiom_or_law_carriers"],
            tolerance=0,
            source="Every audited carrier is partitioned into UNINSTANTIATED_AXIOM_CLASS, TOY_ONLY_INSTANCE, or GENUINELY_INSTANTIATED",
        )
        .add_assertion(
            "taxonomy_partition_exhaustive",
            computed=sum_tax,
            expected=cs["audited_axiom_or_law_carriers"],
            tolerance=0,
            source="Every audited carrier is partitioned into Type M (MISSING_MATHLIB_INFRA), Type P (QOU_BRIDGE_OR_PHYSICS_GAP), or Type D (LEGITIMATE_ALGEBRAIC_INTERFACE)",
        )
        .add_assertion(
            "raw_structures_accounted",
            computed=cs["audited_axiom_or_law_carriers"] + cs["pure_data_structures_excluded"],
            expected=cs["total_raw_classes"] + cs["total_raw_structures"],
            tolerance=0,
            source="Audited carriers + excluded pure-data structures equals total raw classes + structures",
        )
        .add_data("corpus_scope", cs)
        .add_data("instantiation_summary", ins)
        .add_data("taxonomy_summary", tax)
        .add_data("status_by_taxonomy_matrix", res["status_by_taxonomy_matrix"])
        .add_data("mathlib_clusters", res["mathlib_clusters"])
        .add_data("physics_bridge_gap_summary", res["physics_bridge_gap_summary"])
        .add_data("standalone_axiom_opaque_summary", res["standalone_axiom_opaque_summary"])
        .add_data("toy_only_carriers", res["toy_only_carriers"])
        .add_data("carriers", res["carriers"])
    )

    out_path = builder.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Static AST and import-graph audit of Lean 4 class/structure/axiom/opaque "
            "declarations across folio/quantum-observable-universe; no numerical substrate q_0 is read."
        ),
    })
    print(f"\nWitness: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
