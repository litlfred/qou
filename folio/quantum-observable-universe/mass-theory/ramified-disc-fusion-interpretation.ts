import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:ramified-disc-fusion",
  label: "rem:ramified-disc-fusion-interpretation",
  title: "Reeb trajectory to boundary Galois permutation dictionary",
  uses: [
    "prop:ramified-disc-fusion",
    "prop:six-canonical-knot-operators",
  ],
});
