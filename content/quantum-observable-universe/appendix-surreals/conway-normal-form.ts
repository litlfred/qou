import { remark } from "../../schema/builders";

export default remark({
  label: "rem:conway-normal-form",
  title:
    "Conway normal form unifies Big-O / little-o / Θ / $\\sim$",
  tags: [
    "surreal-numbers",
    "conway-normal-form",
    "big-o",
    "little-o",
    "asymptotic",
    "leading-exponent",
    "notation",
    "cross-reference",
  ],
  interprets: "def:birthday-grading",
  uses: ["def:surreal-blowup-calculus"],
  cites: ["conway1976", "gonshor1986", "ehrlich2012"],
  authorNotes: [
    {
      kind: "status",
      body: "A full formalisation of Conway normal form requires Hahn series\nwith surreal-valued exponents — partially present in mathlib\n(`Mathlib.RingTheory.HahnSeries`) but not yet integrated with\nthe `SurrealField` axiomatic class. The $\\ordw$ function\nas a group homomorphism can be stated once that integration\nlands; meanwhile the valuation-ring structure\n([valuation ring](#rem:valuation-ring-finite-surreals)) gives\nenough infrastructure to support the asymptotic dictionary at\nthe level of the standard-part map.",
    },
  ],
});
