import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-identity-unique",
  title: "Uniqueness of the inertial mass identity",
  lean: { ref: "qou:QOU.MassIdentity.unique",
    validation: "not_checked",
  },
  uses: [
    "def:mass-identity",
    "prop:frobenius-pairing-unique",
  ],
  proofs: ["prf:mass-identity-unique"],
  tags: ["uniqueness", "mass-identity"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "**Scaling law restated in the ring (owner ruling 2026-11-27, bean qou-5o1v).** Rescaling the Frobenius form by a " +
        "unit $c$ multiplies the mass by $c$ in $R$. The absolute-value form $|\\varphi(c)|$ is the comparison corollary " +
        "`QOU.Transcendental.MassTheory.MassComparison.comparedMass_scale`.",
    },
  ],
});
