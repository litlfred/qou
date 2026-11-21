import { example } from "../../schema/builders";

export default example({
  interprets: "thm:descartes",
  label: "ex:terminal-morphism-brings",
  title:
    "Constructive terminal morphism to Bring's QOU",
  tags: [
    "brings-surface",
    "terminal-object",
    "constructive",
    "archimedean-universe",
  ],
  uses: [
    "thm:descartes",
    "ex:tannaka-krein-su2",
    "prop:vacuum-state",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-17",
      body:
        "**RESOLVED 2026-11-18 (owner choice: q is part of the data of the category).** Step 1 used to read the Descartes condition as `q + q^{-1} = -6`, which forces `q = -3 +/- 2 sqrt 2`, a single negative value, and contradicts `q` varying with `q_0` as the local value. Under the 2026-09-15 ruling `-6` is `chi_eu(M_0)`, a condition on the base curve, not a trace. Step 1 now fixes `q` as part of the objects of `C_{-6}`, so Steps 2-4 (which only need source and target at the same `q`) hold for each value of `q`, and `thm:descartes` is stated at fixed `q`. Bean `qou-qhcr`.",
    },
  ],
});
