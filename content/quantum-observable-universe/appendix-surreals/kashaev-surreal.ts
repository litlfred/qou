import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:kashaev-surreal",
  title:
    "Kashaev volume conjecture as a surreal standard-part identity",
  lean: { ref: "qou:QOU.AppendixSurreals.KashaevSurreal", validation: "stub" },
  tags: [
    "tier:famous",
    "surreal-numbers",
    "kashaev",
    "volume-conjecture",
    "hyperbolic-volume",
    "standard-part",
    "open-problem",
    "reformulation",
  ],
  uses: [
    "rem:kashaev-volume-density",
    "conj:kashaev-volume-conjecture",
    "def:surreal-blowup-calculus",
    "def:ecalle-borel-resummation",
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
    "berarducci-mantova2018",
    "ecalle1981",
    "garoufalidis-zagier-2024",
    "garoufalidis-gu-marino2021",
    "fantini-rella2024",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-13",
      body:
        "**Figure-eight instance discharged (conditional on the transfer " +
        "equivalence only).** For $K = 4_1$ the classical Kashaev limit is " +
        "the Murakami–Murakami theorem, so the surreal standard-part " +
        "identity holds with $=$ for $4_1$; Garoufalidis–Zagier quantum " +
        "modularity supplies the exact all-orders cocycle refinement and " +
        "Garoufalidis–Gu–Mariño the integer Stokes data. General knots " +
        "remain open. See the 2026-07-13 alien-calculus ↔ surreal " +
        "integration review audit.",
    },
  ],
});
