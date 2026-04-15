import { definition } from "../../schema/builders";

export default definition({
  label: "def:poisson-object",
  title: "Internal Poisson object",
  lean: {
    decl: "QOU.PoissonObject",
    validation: "not_checked",
  },
  uses: [
    "def:frobenius-pairing",
    "def:higher-forms",
  ],
  tags: ["poisson", "bivector", "pullback", "differential-calculus"],
  cites: ["kock2004"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/poisson-object-0.svg", blockIndex: 0, hash: "e3e1eea5dc53" },
  ],

});
