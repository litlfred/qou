import { definition } from "../../schema/builders";

export default definition({
  label: "def:surreal-blowup-calculus",
  lean: {
    ref: "qou:QOU.AppendixSurreals.BlowupCalculus",
    validation: "not_checked",
  },
  title:
    "Surreal blow-up calculus: named infinite surreals for renormalisation",
  tags: [
    "surreal-numbers",
    "renormalisation",
    "blow-up",
    "infinite-surreal",
    "regularisation",
    "named-infinity",
  ],
  uses: ["def:standard-part-functor"],
  cites: ["conway1976", "ehrlich2012"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-09",
      body: `**Base ring (§7c) — \`ℝ\` is load-bearing, and unavoidably so.** \`BlowupField\` carries \`st : K → ℝ\`, the **standard-part map**, with \`st_natCast : st (n : K) = (n : ℝ)\`; the canonical instance is \`ℝ*\` (\`Hyperreal\`) with \`Hyperreal.omega\` and \`Hyperreal.st\`. The codomain of a standard-part map *is* \`ℝ\` by definition — the construction's entire purpose is to land a non-archimedean field's finite part in the archimedean reals. Genericising the codomain would delete the content.`,
    },
  ],
});
