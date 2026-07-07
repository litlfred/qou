import { remark } from "../../schema/builders";

/**
 * Scoping follow-on to prop:assembly-projector-exists: existence of the
 * symmetric-block projector is necessary but not sufficient; stability needs
 * the binding LP/SDP to select μ=(N) and the trace-weight gap, and aromatic
 * stability comes from irreducibility rather than bare existence.
 */
export default remark({
  label: "rem:assembly-projector-scope",
  title: "Scope of the assembly-projector existence result",
  interprets: "prop:assembly-projector-exists",
  uses: ["def:molecular-assembly-projector"],
  tags: [
    "assembly-projector",
    "existence",
    "stability",
    "LP-selection",
    "aromatic",
  ],
});
