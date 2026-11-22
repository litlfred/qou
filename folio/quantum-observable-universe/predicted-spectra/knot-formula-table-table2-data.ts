import { table } from "../../schema/builders";
export default table({
  label: "tbl:knot-formula-table-table2-data",
  title: "Data table 2 from rem:knot-formula-table",
  uses: ["rem:knot-formula-table"],
  tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21): electron row is sigma_0 sigma_1 sigma_0 with Hopf-link closure; Seifert genus 0 and minimal crossing number 2 are from rem:electron-knot-example. Muon and tau rows keep their backup torus knots and say the words are not ruled." },
  ],
});
