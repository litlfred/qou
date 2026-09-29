import { proof } from "../../schema/builders";

export default proof({
  label: "prf:descent-condition",
  title: "Proof of Descent condition --- twisted $2$-cocycle",
  uses: ["prop:descent-condition", "lem:descent-cocycle-deviation"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/descent-condition-proof-0.svg", blockIndex: 0, hash: "bb93a7875439" },
  ],

});
