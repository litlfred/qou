import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lepton-meson-torus-knot-dictionary",
  lean: { ref: "qou:QOU.ParticleInteractions.lepton_meson_crossing_match" },
  title:
    "Torus-knot dictionary: leptons at $H_2$ vs mesons at $H_3$",
  uses: ["def:categorical-meson"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-01",
      body:
        "The parenthetical **(odd primes)** in the opening line is the " +
        "only occurrence of the primality condition anywhere in the " +
        "corpus, and it is **asserted, not derived**. It carries real " +
        "weight: `torus-embeddable-complete-proof` proves the genus " +
        "bound $g(T(2,n)) = (n-1)/2 \\le 4$, admitting $n \\in \\{3,5,7,9\\}$ " +
        "— four knots — while this table assigns three generations. So " +
        "*odd prime* plus the genus bound would give exactly three " +
        "generations, and the three-generation question reduces to the " +
        "single lemma **what excludes $T(2,9)$?** Candidate structural " +
        "reason, unproved: for odd $n \\ge 3$, $n$ factors into smaller " +
        "odd windings iff $n$ is composite, so $\\sigma^9 = (\\sigma^3)^3$ " +
        "is a harmonic of generation 1. Probe + routes: " +
        "`generation-count-t29-truncation.witness.json` (bean qou-4dxs).",
    },
    {
      kind: "status",
      date: "2026-08-01",
      body:
        "Quark-flavour column realigned to match the charm/bottom " +
        "assignment in `knot-particle-dictionary-table4-data` " +
        "($\\mathfrak{c} \\leftarrow T_{2,5}$ at generation 2, " +
        "$\\mathfrak{b} \\leftarrow T_{2,7}^{\\sigma}$ at generation 3). " +
        "The prior text listed $s$ at **both** generation 2 and " +
        "generation 3 (as *heavy-strange*) and omitted $c$, $b$, $t$ " +
        "entirely — stale relative to the realignment. The meson column " +
        "is left unchanged and is **not** asserted to be consistent " +
        "with the corrected quark column: $\\phi = s\\bar{s}$ carries " +
        "generation-2 flavour content while sitting in the " +
        "generation-3 row, which is a separate open question.",
    },
  ],
  cites: [
    "jones1987",
    "kashaev1997",
  ],
  tags: [
    "lepton",
    "meson",
    "torus-knot",
    "hecke-algebra",
    "dictionary",
  ],
});
