import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:q-gl-kummer-filtration",
  lean: { ref: "qou:QOU.QGeometricLanglands.q_gl_kummer_filtration", validation: "not_checked" },
  title: "Kummer filtration on $q$-local systems",
  uses: [
    "prop:q-gl-obstruction-calc",
    "prop:q-geometric-langlands",
  ],
  cites: ["yekutieli2010"],
  tags: ["geometric-langlands", "kummer", "filtration"],
});
