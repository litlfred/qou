import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:p-from-braid-mirror",
  title:
    "Parity $P$ as mirror reflection of the braid diagram (writhe sign flip)",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.PFromBraidMirror",
    validation: "not_checked",
  },
  uses: [
    "conj:cpt-d6-d7-d8-closure",
    "def:bar-involution",
    "conj:cpt-orbit-closure-density",
    "prop:chirality-writhe-ribbon-derivation",
    "rem:breit-wheeler-vertex",
  ],
  cites: [
    "kassel1995",
    "jones1987",
    "kauffman1991",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "Scope at the Hecke-letter level (owner instruction 2026-11-15, \"Scope conj:p-from-braid-mirror\", relayed by the coordinator; bean qou-hlx7). Kind and every number unchanged. Lean (`QOU/QuarkState/HelicityCommonSource.lean`): `QOU.QuarkState.Helicity.no_linear_flip` (no scalar-linear algebra map sends a letter to its inverse unless 2(q - 1/q) = 0); `QOU.QuarkState.Helicity.flip_hecke` (the inverse letter satisfies the Hecke relation at 1/q); Klein four-group `flip_flip`, `swap_swap`, `flip_neg`, `flip_swap`, `neg_hecke`; profiles `flip_Pp`, `swap_Pp`, `neg_Pp`, `positron_ne_electron`, `swap_electron`, `neg_electron`; `swap_hecke`, `swap_braid`; `no_linear_neg`. That q -> 1/q has no field automorphism of the reals behind it is a standard fact, not formalised. The §What-remains-open item 1 claim that P preserves the quadratic at q is contradicted by `flip_hecke` and is scoped in the new section, not deleted.",
    },
  ],
  tags: [
    "tier:S",
    "parity",
    "duality-d7",
    "braid-mirror",
    "writhe",
    "cpt-decomposition",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
  ],
});
