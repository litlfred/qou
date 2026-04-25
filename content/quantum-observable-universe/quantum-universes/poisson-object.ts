import { definition } from "../../schema/builders";

export default definition({
  label: "def:poisson-object",
  title: "Internal Poisson object",
  lean: { ref: "qou:QOU.PoissonObject",
    validation: "not_checked",
  },
  uses: [
    "def:frobenius-pairing",
    "def:higher-forms",
  ],
  tags: ["poisson", "bivector", "pullback", "differential-calculus"],
  cites: ["kock2004"],
});
