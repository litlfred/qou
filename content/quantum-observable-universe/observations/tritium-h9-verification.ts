import { proof } from "../../schema/builders";

/**
 * Computational proof: ³H β-decay Q-value via H₉(q) Gröbner reduction.
 *
 * This proof block verifies the tritium β-decay Q-value by computing
 * the full Gröbner--Shirshov normal form of the 9-strand nuclear braid
 * in H₉(q) with Borromean confinement.  The witness records parent/daughter
 * NF terms, net traces, and derived Q-values at three levels:
 *   1. Borromean NF (full confinement braid B₃ = (σ·σ⁻¹)³)
 *   2. Flat L1 (quark-level, no confinement)
 *   3. T₃,₅ weak vertex insertion
 *
 * Trust chain:
 *   h9_beta Rust engine → JSON output → content block
 */
export default proof({
  label: "prf:tritium-h9-verification",
  title:
    "$H_9(q)$ Gröbner--Shirshov verification of tritium $\\beta$-decay $Q$-value",
  tags: [
    "computation",
    "hecke-engine",
    "tritium",
    "beta-decay",
    "borromean",
    "groebner-shirshov",
    "h9",
    "q-value",
    "verification",
  ],
  uses: [
    "ex:tritium-decay-knot-equation",
    "prop:trace-ratio-observable",
  ],
  computation: {
    engine: "sympy",
    script: "tools/hecke-engine/src/bin/h9_beta.rs",
    witness: "tools/hecke-engine/h9_beta.witness.json",
    status: "verified",
    requires: ["rustc>=1.75", "hecke-engine"],
  },
});
