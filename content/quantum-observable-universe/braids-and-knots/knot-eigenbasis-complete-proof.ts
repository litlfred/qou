import { proof } from "../../schema/builders";

export default proof({
  label: "prf:knot-eigenbasis-complete",
  title: "Proof of Completeness of the knot-type eigenbasis",
  uses: ["prop:knot-eigenbasis-complete"],
  lean: { ref: "qou:QOU.PathIntegrals.KnotEigenbasisComplete",
    validation: "leanok",
  },
});
