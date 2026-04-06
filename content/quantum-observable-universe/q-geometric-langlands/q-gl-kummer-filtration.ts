import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-gl-kummer-filtration",
  lean: { decl: "QOU.q_gl_kummer_filtration", validation: "not_checked" },
  title: "Kummer filtration on $q$-local systems",
  uses: [
    "prop:q-gl-obstruction-calc",
    "conj:q-geometric-langlands",
    "def:q-local-system",
  ],
  cites: ["yekutieli2010"],
  tags: ["geometric-langlands", "kummer", "filtration"],
});
