import { definition } from "../../schema/builders";

/**
 * The Schwinger proper-time measure ς·ds/s and its unit ς — the
 * normalization object downstream per-loop-measure consumers
 * reference (R2-core).
 *
 * The SHAPE is Lean-proved rigid (unique scale-invariant density up
 * to the scalar ς; QOU.Archimedean.SchwingerMeasureShape). The
 * definition fixes the CANONICAL choice ς = 1 (one nat per
 * proper-time e-fold under k_B = 1), whose canonicity is
 * conjecturally backed by conj:schwinger-measure-computational-time —
 * see the narrative note. Defining the object does not assert the
 * conjecture; wiring 1/(8π) as derived remains owner-gated per the
 * 2026-07-19 R2 ruling.
 *
 * Unit symbol: ς (varsigma) — register-safe; plain c is reserved for
 * color, c_q and c_k are taken.
 */
export default definition({
  label: "def:schwinger-measure-unit",
  title: "Schwinger proper-time measure and its unit $\\varsigma$",
  lean: {
    ref: "qou:QOU.Archimedean.SchwingerMeasureUnit.density",
    validation: "not_checked",
  },
  uses: [
    "conj:schwinger-measure-computational-time",
    "prop:horizon-conformal-invariance",
    "def:boltzmann-constant",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): , [Boltzmann constant in QOU natural units](#def:boltzmann-constant)" },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): Scale invariance is inherited from the conformal invariance of the horizon boundary datum ([Conformal invariance at the jet horizon](#prop:horizon-conformal-invariance)): the loop's ultraviolet end has no preferred proper-time scale." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The archimedean Lean shell writes $c$ for the same scalar;" },
    {
      kind: "status",
      date: "2026-07-25",
      body:
        "Created as the downstream-referenceable normalization object for the R2-core Schwinger measure (docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md). The sibling Lean states the fibre-level density shape over a generic Field per §7c (no ℝ, no ordering) and proves the scale-invariance functional equation sorry-free (lean-direct exit 0); the archimedean shell (shape uniqueness, nat-per-e-fold, e-fold Jacobian, unit assembly to 1/(8π)) is the existing library file QOU/Archimedean/SchwingerMeasureShape.lean. Canonicity of ς = 1 is CONJECTURAL (conditionally forced by conj:schwinger-measure-computational-time or by owner premises P1/P2); unconditionally it is a unit convention per the 2026-07-19 owner ruling — this block does not upgrade any tier and nothing wires on it.",
      see: "docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md",
    },
  ],
  tags: [
    "alpha-em",
    "r2-core",
    "schwinger-measure",
    "proper-time",
    "haar-measure",
    "normalization",
  ],
});
