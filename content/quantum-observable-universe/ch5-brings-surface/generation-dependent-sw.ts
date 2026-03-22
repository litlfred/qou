import { remark } from "../../schema/builders";

export default remark({
  label: "rem:generation-dependent-sw",
  title: "Generation-Dependent Seiberg-Witten Differentials",
  uses: [
    "rem:seiberg-witten",
    "rem:color-tube-cubic",
    "rem:brings-smoothness",
  ],
});
