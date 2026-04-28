import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-irreducible",
  title: "Proof of Irreducibility from observability",
  uses: ["lem:categorical-irreducible"],
  lean: { ref: "qou:QOU.categorical_irreducible",
    validation: "leanok",
  },
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-irreducible-proof-0.svg", blockIndex: 0, hash: "42efeb538a22" },
  ],

});
