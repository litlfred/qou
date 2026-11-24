import { proof } from "../../schema/builders";

/**
 * Computational proof: knot volumes verified via SnapPy.
 *
 * This proof block verifies all hyperbolic volume claims in the paper
 * by computing them independently using the SnapPea kernel (via SnapPy).
 * The witness file records computed values, expected values, and error bounds.
 *
 * Trust chain:
 *   SnapPy computation → witness JSON.  A numerical check, not a proof;
 *   it supplies no step of the mass chain (scope note, 2026-11-16).
 */
export default proof({
  label: "prf:knot-volumes-verification",
  title: "Knot volume check (SnapPy; a numerical check, not a proof)",
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-16",
      body: "Scope note added on owner ruling (decision card, 2026-11-16, \"scope note, cite exact volumes\"). The block stays a proof block for reference stability, but it is a numerical check of volumes and derives no step of the mass chain. Exact closed forms are now cited where they exist.",
    },
  ],
  tags: ["computation", "snappea", "hyperbolic", "verification"],
  // The derived quantities (Table 2) solve the CAL-2 calibration equation
  // m_mu/m_e = Vol(4_1)/hbar_q^2 for q. That equation defines q_0 (CAL-2);
  // it does not assume conj:topological-mass-formula. Retargeted 2026-11-20
  // (owner, option 2 on the q_0 pair; bean qou-tm3c).
  uses: [
    "def:three-calibration-discipline",
    "sec:hyperbolic-volumes-prose",
  ],
  computation: {
    engine: "snappea",
    script: "computations/knot-volumes.py",
    witness: "computations/substrate/knot-volumes.witness.json",
    status: "verified",
    requires: ["snappy>=3.3"],
  },
});
