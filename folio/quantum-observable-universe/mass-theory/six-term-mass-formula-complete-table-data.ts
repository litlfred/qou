import { table } from "../../schema/builders";
export default table({
  label: "tbl:six-term-mass-formula-complete-table-data",
  title: "Derivation sources, computational formalisms, and archimedean convergence status of the six mass-formula terms",
  uses: ["thm:six-term-mass-formula-complete"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witnesses: atomic-tr-m-mpfr-exact representation.witness.json, term6-habiro-residue-mpfr-50dps.witness.json.",
    },
  ],
});
