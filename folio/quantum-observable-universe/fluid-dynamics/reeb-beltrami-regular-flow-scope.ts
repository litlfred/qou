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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (The inherited identification of $V$ as the Boothby--Wang Reeb field.) It is taken from `docs/audits/2026-09-03-bring-cone-link-is-the-unit-tangent-bundle.md` and `docs/audits/2026-10-12-ns-rescue-reformulations.md`." },
  ],
});
