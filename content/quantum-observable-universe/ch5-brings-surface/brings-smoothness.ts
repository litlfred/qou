import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:brings-surface",
  label: "rem:brings-smoothness",
  title: "Smoothness of the Bring surface and resolution of spacetime defects",
  uses: [
    "def:brings-surface",
    "rem:chiral-bundles",
    "def:briggs-klein-chart",
    "rem:lagrange-resolvents",
  ],
});
