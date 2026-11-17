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
        "**OPEN — trace identity.** Step 1 reads the Descartes condition as `q + q^{-1} = -6`, i.e. `[2]_q = dim_q(V) = -6`. That forces `q = -3 +/- 2 sqrt 2`, a negative real substrate parameter, and the Descartes condition (`def:archimedean-condition`) no longer says this: it fixes the genus of the base, not a value of the trace. Under the owner ruling of 2026-09-15, `tr(id_A) = dim_q(A)` is a q-dependent quantum dimension, and `-6` is `chi_eu(M_0)`, the topological Euler characteristic of the base curve (`rem:three-euler-characteristics`). Flagged open on owner instruction 2026-11-17 (Bring foundations cleanup); the bare `chi(A)` here was not renamed because the step uses a trace identity, not only the genus. Bean `qou-qhcr`.",
    },
  ],
});
