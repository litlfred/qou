import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chern-character-and-riemann-roch",
  title: "The Chern character and Riemann–Roch on a curve",
  interprets: "lem:brings-euler-characteristic",
  uses: ["lem:brings-euler-characteristic"],
  cites: ["hartshorne-1977", "fulton-harris1991"],
  tags: ["chern-character", "riemann-roch", "euler-characteristic", "brings-surface"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-15",
      body:
        "Expository, for the reader who has met cohomology of manifolds but not sheaf cohomology: the two facts the chi chain needs are that the Euler characteristic of a bundle is a linear function of its degree and rank, and that the tangent bundle of Bring's surface has `h^1 = 9`. The nine-dimensional deformation space and its `S_5` decomposition are proved in `QOU/Brings/S5CharactersOnBringDeformations.lean`.",
    },
  ],
});
