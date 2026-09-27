import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:vertex-is-exceptional-divisor",
  label: "rem:six-operators-via-vertex-factorisation",
  title:
    "Six canonical knot operators are the named vertex-factorisation instances",
  tags: [
    "vertex-factorisation",
    "knot-operator",
    "s3-galois",
    "reeb-flow",
    "exceptional-divisor",
  ],
  uses: [
    "prop:six-canonical-knot-operators",
    "prop:ramified-disc-fusion",
  ],
});
