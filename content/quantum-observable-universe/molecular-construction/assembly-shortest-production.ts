import { remark } from "../../schema/builders";

/**
 * The assembly path is canonical: the Hecke/GS normal form of the assembly
 * braid word, selected by the confinement min-action. Retrosynthesis is
 * non-unique; the forward categorical path is canonical up to molecular
 * symmetry. WS-D, D4.
 */
export default remark({
  label: "rem:assembly-shortest-production",
  title: "The assembly path is canonical: shortest word up to symmetry",
  interprets: "prop:confinement-lp",
  uses: [
    "rem:benzene-assembly-spine",
    "def:hecke-normal-form",
  ],
  tags: [
    "assembly-spine",
    "normal-form",
    "canonical-path",
    "min-action",
    "retrosynthesis",
  ],
});
