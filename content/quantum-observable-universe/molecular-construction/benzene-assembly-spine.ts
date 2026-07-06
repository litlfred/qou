import { remark } from "../../schema/builders";

/**
 * The γγ-from-light assembly spine to benzene.
 *
 * Chains the existing light→nucleon→atom propositions (Breit–Wheeler →
 * qq̄ → Borromean nucleon → ¹²C) into the molecular layer and validates
 * the molecular-layer bond-order predictions (acetylene 3, benzene 3/2,
 * cyclohexane 1) against observed structural orders. Backed by
 * benzene_assembly_spine.py; the predictive model is confirmed.
 */
export default remark({
  label: "rem:benzene-assembly-spine",
  title: "The $\\gamma\\gamma$-from-light assembly spine to benzene",
  interprets: "prop:co-lp-dual-binding",
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/benzene_assembly_spine.py",
    witness: [
      "computations/benzene-assembly-spine.witness.json",
    ],
  },
  uses: [
    "def:molecular-assembly-projector",
    "def:embeddable-knot-operator",
    "def:quark-antiquark-production",
    "rem:meson-to-proton-via-borromean",
    "rem:breit-wheeler-observation",
    "def:f-bor-borromean-observable",
  ],
  tags: [
    "benzene",
    "acetylene",
    "assembly-spine",
    "gamma-gamma",
    "bond-order",
    "aromatic",
  ],
});
