import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-gl-kummer-filtration",
  lean: { ref: "qou:QOU.q_gl_kummer_filtration", validation: "not_checked" },
  title: "Kummer filtration on $q$-local systems",
  uses: [
    "prop:q-gl-obstruction-calc",
    "conj:q-geometric-langlands",
  ],
  cites: ["yekutieli2010"],
  tags: ["geometric-langlands", "kummer", "filtration"],
});
