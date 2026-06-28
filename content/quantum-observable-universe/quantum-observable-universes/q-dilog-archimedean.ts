import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-dilog-archimedean",
  interprets: "def:q-dilogarithm",
  title: "Archimedean realisation of $\\mathrm{Li}_2^q$ (Kirillov dilogarithm)",
  tags: ["hopf-algebra", "dilogarithm", "archimedean", "q-series"],
  uses: [
    "def:q-dilogarithm",
  ],
});
