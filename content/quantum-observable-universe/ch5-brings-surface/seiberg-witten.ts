import { remark } from "../../schema/builders";

export default remark({
  label: "rem:seiberg-witten",
  title: "Geometric resolution and the Seiberg--Witten differential",
  uses: [
    "rem:brings-smoothness",
    "rem:lagrange-resolvents",
    "rem:chiral-bundles",
    "def:quantum-observable-universe",
    "lem:volume-from-rigidity",
    "rem:holonomy-trefoil",
  ],
});
