import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "**Lean scope (disclosure, not a change of claim).** The `lean.ref` theorem is a finite `decide` check: the trace of one explicit 2×2 Gaussian-integer matrix sum (six fixed quaternion crossings with fixed signs) equals −12, and −12 = dim V · χ with dim V := 2 and χ := 2 − 2·4 defined as constants. It verifies the number, not an identity between the curvature trace and dim V·χ(Σ₄) for a crossed module in general. The narrative also reverses the direction of Φ₀ relative to the statement and asserts the intermediate matrix and the Bring-bridge table without proof. Found by the blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B09; bean qou-zxuy).",
    },
  ],
  label: "prop:crossed-module-euler-characteristic",
  title: "Hecke crossed module h² trace equals $\\dim(V) \\cdot \\chi(\\Sigma_4)$",
  uses: [
    // broken-ref removed (Phase 7): def:borromean-baryon-mass-formula
    // broken-ref removed (Phase 7): prop:quaternion-from-hecke-eigenspaces
  ],
  lean: { ref: "qou:QOU.BraidKnot.CrossedModuleEulerCharacteristic.crossed_module_euler_characteristic" },
  computation: {
    engine: "python",
    script: "computations/hecke/hecke_crossed_module_q8.py",
    witness:
      "computations/hecke/hecke-crossed-module-q8.witness.json",
    status: "verified",
  },
});
