import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-dilog-three-contexts",
  interprets: "def:q-dilogarithm",
  title: "$\\mathrm{Li}_2^q$ in $\\mathbb{F}_p$, $\\mathbb{Q}_p$, $\\mathbb{C}_p$",
  tags: ["hopf-algebra", "dilogarithm", "p-adic", "finite-field", "q-series"],
  uses: [
    "def:q-dilogarithm",
  ],
  cites: ["besser2000", "besser-dejeu2008", "schlesinger2001"],
});
