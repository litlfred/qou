import { proof } from "../../schema/builders";

export default proof({
  label: "prf:borromean-h4-categorical-derivation",
  title: "Proof of borromean h4 categorical derivation",
  uses: ["prop:borromean-h4-categorical-derivation"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/gap_a4_T15_character_polynomial_probe.py",
    witness: "computations/probes/gap-a4-T15-character-polynomial-probe.witness.json",
    status: "verified",
  },
});
