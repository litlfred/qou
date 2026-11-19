import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:reeb-beltrami-regular-flow",
  label: "rem:reeb-beltrami-regular-flow-scope",
  title: "Scope of the regular fibre-rotation flow",
  uses: [
    "prop:reeb-beltrami-regular-flow",
    "def:reeb-bundle",
    "ex:torus-ns-regular",
  ],
  tags: ["navier-stokes", "regularity", "scope", "reeb", "descartes"],
  authorNotes: [
    {
      kind: "note",
      body: "Boothby-Wang contact identification of V on the link of Bring's cone: see `docs/audits/2026-09-03-bring-cone-link-is-the-unit-tangent-bundle.md` and `docs/audits/2026-10-12-ns-rescue-reformulations.md`.",
    },
  ],
});
