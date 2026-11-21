import { table } from "../../schema/builders";
export default table({
  label: "tbl:topology-geometry-boundary-table-data",
  title: "Data table from rem:topology-geometry-boundary",
  uses: ["rem:topology-geometry-boundary"],
  tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21): the emission-topology row uses the trefoil electron, so its status changes from 'Derived' to 'Backup model only'." },
  ],
});
