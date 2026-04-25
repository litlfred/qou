import { definition } from "../../schema/builders";

export default definition({
  label: "def:observable-mtc",
  lean: { ref: "qou:QOU.ObservableMTC", validation: "not_checked" },
  title: "Observable modular tensor category at $q = \\zeta_N$",
  tags: ["modular-tensor-category", "mtc", "root-of-unity", "anyons"],
  uses: [
    "rem:hopf-non-cocommutativity",
    "rem:berry-vortex-moduli",
  ],
  cites: ["moore-seiberg1989", "kitaev2006"],
});
