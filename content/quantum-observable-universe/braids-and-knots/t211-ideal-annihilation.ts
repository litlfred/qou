import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:vertex-algebra-jet-relations",
  label: "rem:t211-ideal-annihilation",
  title: "Behaviour of $T_{2,11}$ on the jet bundle ideals",
  tags: [
    "torus-knot", "genus-bound", "spectral-filter",
    "hecke-algebra", "knot-coordinates", "ideal",
  ],
  uses: [
    "prop:genus-filtration-ideal",
    "prop:vertex-algebra-jet-relations",
    "prop:shell-structure-eigenvalues",
    "prop:nuclear-shell-intruder",
    "rem:fivefold-symmetry",
    "thm:embeddability-closure",
  ],
  cites: ["kassel1995", "jones1987"],
});
