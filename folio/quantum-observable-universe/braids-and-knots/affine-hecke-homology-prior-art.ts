import { remark } from "../../schema/builders";

export default remark({
  label: "rem:affine-hecke-homology-prior-art",
  title: "Prior art: Hochschild homology of affine Hecke algebras is independent of $q$",
  interprets: "rem:markov-trace-inductive-limit",
  cites: ["solleveld2022", "solleveld2013"],
  tags: ["affine-hecke-algebra", "hochschild-homology", "trace", "inductive-limit", "prior-art"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Bean qou-a8rj: registered the published J. Algebra 384 (2013) entry (`solleveld2013`) alongside the held 2022 arXiv v3 copy (`solleveld2022`), made the degree-zero cocentre identification HH_0(H(R, q)) ~= O(T-tilde)^W explicit, and contrasted continuous affine torus trace families against the finite p(n)-dimensional cocentre of H_n(q) (dim HH_0(H_2(q)) = 2 on the two-strand per-pair EM channel, pinned to a 1-parameter slice across the tower by Markov stabilisation).",
    },
    {
      kind: "note",
      date: "2026-11-23",
      body: "Relocated from block prose (Milnor Voice A; Lean talk out of prose): The note in the Lean scaffold that names the open construction as an inductive limit on the affine Hecke algebra should be read with this distinction in mind.",
    },
  ],
});
