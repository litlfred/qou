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
    "prop:vertex-algebra-jet-relations",
    "prop:vertex-algebra-relations",
    "prop:cohomological-embedding",
    "thm:embeddability-closure",
    "prop:torus-knot-generators",
    "thm:jones-markov-trace",
    "prop:shell-structure-eigenvalues",
    "prop:nuclear-shell-intruder",
    "rem:fivefold-symmetry",
    "rem:symmetric-quotient-colour",
  ],
  cites: ["kassel1995", "jones1987"],
});
