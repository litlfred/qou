import { table } from "../../schema/builders";

export default table({
  label: "tbl:borromean-quark-table-data",
  title: "Torus-knot particle spectrum ($n = 2$ to $9$)",
  caption:
    "The $T(2, n)$ family from the Hopf link ($n = 2$, gluon) through " +
    "the genus-saturating $T(2, 9)$: name, type (knot/link), component " +
    "count, Seifert genus, and physical role.",
  uses: ["conj:borromean-quark"],
  tags: ["torus-knot", "particle-spectrum", "borromean"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21): the trefoil row is the backup electron; the ruled electron's closure is the Hopf link. Muon and tau words are not ruled, so those rows carry a question mark like the boson rows." },
  ],
});
