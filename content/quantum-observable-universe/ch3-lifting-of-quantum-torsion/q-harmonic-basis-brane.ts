import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:recursive-brane-tower",
  label: "rem:q-harmonic-basis-brane",
  title: "$q$-Harmonic basis of the brane tower",
  tags: ["q-harmonic", "brane-tower", "self-duality"],
  uses: [
    "def:recursive-brane-tower",
    "def:substrate-parameter",
    "prop:jet-prolongation",
    "rem:betti-numbers-brane",
  ],
});
