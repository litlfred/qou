import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-gl-obstruction-calc",
  label: "rem:q-gl-obstruction-classical-compatibility",
  title: "Perpetual obstruction and the classical limit",
  uses: [
    "prop:q-gl-obstruction-calc",
    "conj:q-gl-classical-limit",
  ],
  tags: ["geometric-langlands", "classical-limit", "obstruction"],
});
