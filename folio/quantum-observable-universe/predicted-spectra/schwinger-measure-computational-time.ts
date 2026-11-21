import { conjecture } from "../../schema/builders";

/**
 * The computational-time identification of the Schwinger variable —
 * the R2-core unit lead, formally recorded.
 *
 * PRIMARY conjecture: the binding sector's (q-)Borel variable and the
 * one-loop Schwinger proper-time variable are the same substrate
 * object (under owner premise P2, both are the substrate's
 * computation-step count). Quantitative shadow: the keystone-forced
 * binding normalizer N(n) = (n−1)! is the n-th moment of the loop's
 * proper-time measure ς·ds/s against e^{−s}.
 *
 * Conditional consequences (stated in the .md, neither a derivation):
 *   (i)  ς = 1 forced via the Lean-proved keystone identity
 *        n·N(n) = n! (QOU.Mass.KeystoneBridgeC1Binding);
 *   (ii) the ½ of the per-channel coefficient ½·a₀ = 1/(8π) is
 *        located per-channel bar-even (exact fold identity).
 *
 * Source of record:
 *   docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md §5
 * following the Quillen mismatch finding of
 *   docs/audits/2026-07-25-alpha-em-r2-quillen-curvature-attack.md.
 */
export default conjecture({
  label: "conj:schwinger-measure-computational-time",
  title:
    "Computational-time identification: the binding Borel variable is the loop proper time",
  lean: {
    ref: "qou:QOU.Archimedean.SchwingerMeasureComputationalTime.BorelProperTimeIdentification",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "computations/probes/r2core_schwinger_measure_explore_probe.py",
    witness: [
      "computations/probes/r2core-schwinger-measure-explore.witness.json",
    ],
    status: "verified",
    requires: ["mpmath", "sympy"],
  },
  uses: [
    "conj:qdifference-kernel-prolongation-symbol",
    "def:boltzmann-constant",
    "prop:em-coupling-fixed-point",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean-proved identity $n \\cdot N(n) = n!$\n\n(an exact distinguisher, proved unconditionally in the sibling Lean)\n\nand the binding side's is Lean-forced;\n\ntightness is Lean-proved from the second-moment confluence\n\ntheorems, carried as instance-free Lean classes)\n\nthe bar-fixed classes are Lean-proved to be exactly\n\n— Lean-proved at general order\n\nBoth ratio identities and the vanishing are Lean-proved." },
    {
      kind: "status",
      date: "2026-07-25",
      body:
        "Recorded from the 2026-07-25 R2-core Schwinger-measure exploration (docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md §5). The identification is the keystone's unproved geometric leg — a dictionary premise of the same species as R2 itself. The 2026-07-19 owner ruling stands: R2 is NOT derived-proved, 1/(8π) stays a phase-4 identification, and nothing wires on this block. Owner premises P1 (substrate scale-freedom) and P2 (proper time = computational time) are framework premises, not derived. The sibling Lean class `BorelProperTimeIdentification` is a content-bearing primary conjecture class (§3b-tax; one parameter-quantified equation field) with NO instance — the honest open state. The conditional theorem `unit_eq_one_of_keystone_normalizer` derives ς = 1 from the class field plus the keystone-proved normalizer identity n·N(n) = n! (QOU.Mass.KeystoneBridgeC1Binding), and `half_unit_breaks_normalizer` proves the ς = 1/2 distinguisher unconditionally; both sorry-free (lean-direct exit 0, generic Field + CharZero per §7c). Probe: 10/10 exact assertions (B5 moment identity n = 1..6; B2 bar-even fold). Complementary same-tranche record: the library file QOU/Archimedean/BorelProperTimeMoment.lean carries the analytic (ℝ-side) face — moment integral, Carleman determinacy hypothesis, bar-covariance falsifier — with its own §3b-tax class, also instance-free; this block is the fibre-algebraic content-block face of the same open premise. The measure unit is written ς (varsigma) in content blocks — the audits' c is register-reserved for color.",
      see: "docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md",
    },
    {
      kind: "status",
      date: "2026-08-01",
      body:
        "State after the representability + kernel-selection campaigns (beans qou-u5p0/ry7x/mee2/q5zq/334t). (1) Determination: the corpus performs NO integral resummation of the binding series — the binding OGF is used purely formally (keystone strip, depth-2 recurrence, formal q-Borel weights) — so the conjecture's (REP) content is a CANONICAL-CHOICE claim, not a matching to an existing corpus operation (docs/audits/2026-08-01-rep-jackson-identification.md). (2) Archimedean leg: DERIVED (closed for the constructed family) — e^{-s}ds is Carleman-unique for the factorial moments, the balanced kernel family is tight (Lean-proved, BalancedKernelTightness.lean, lean-direct exit 0), and every Prokhorov subsequential limit is the Schwinger measure, conditional only on the classical Prokhorov-selection/moment-passage package carried as instance-free classes (docs/audits/2026-08-01-rep-tightness-archimedean.md). (3) Fibre leg: the choice is EXACTLY the self-adjoint-extension circle of the canonically derived Jacobi operator J(q) of the balanced moments (indeterminate at q ≠ 1, deficiency (1,1)); the u-translate continuum, the Poisson dual-mode sector, and the extension circle are one object in three frames (docs/audits/2026-08-01-ksel2-gns-favard-canonicity.md, 2026-08-01-ksel3-modular-double-covariance.md). The open question is now the DISTINGUISHED EXTENSION: Friedrichs/Krein are the canonical Stieltjes candidates; bar-reflection acting on the Nevanlinna parameter is the identified derivation route. Selection principles tested: singularity matching is uniquely selective in form but data-blind on current corpus data (docs/audits/2026-08-01-ksel1-singularity-selection.md); modular-double covariance organizes (one Gaussian in dual frames) but its two natural strengthenings pin DIFFERENT kernels. The Lean class BorelProperTimeIdentification is UNCHANGED (still content-bearing, still no instance — the honest open state); nothing is wired on this block; the conjecture stands, its open content relocated from kernel choice to extension choice.",
      see: "docs/audits/2026-08-01-rep-jackson-identification.md",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Schwinger proper-time measure and its unit $\\varsigma$](#def:schwinger-measure-unit); the shape is the unique scale-invariant density, the unit is what remains open)" },
  ],
  tags: [
    "alpha-em",
    "r2-core",
    "schwinger-measure",
    "proper-time",
    "computational-time",
    "borel-transform",
    "keystone",
    "binding",
    "open-problem",
  ],
});
