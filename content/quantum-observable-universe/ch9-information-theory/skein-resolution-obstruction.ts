import { definition } from "../../schema/builders";

export default definition({
  label: "def:skein-resolution-obstruction",
  title:
    "Skein resolution obstruction $\\kappa_c^{\\mathrm{comp}}(L, q)$",
  tags: [
    "obstruction",
    "yekutieli",
    "skein-resolution",
    "computational-horizon",
    "P-vs-NP",
    "q-dependent",
    "cohomology",
  ],
  lean: {
    decl: "QOU.SkeinResolutionObstruction",
    validation: "not_checked",
  },
  uses: [
    "def:computational-horizon",
    "def:quantum-characteristic-classes",
    "prop:jet-prolongation",
    "rem:skein-turing-machine",
    "def:descent-involution",
    "prop:descent-eigenspaces",
    "def:information-speed-of-light",
    "prop:ns-obstruction-tower",
  ],
});
