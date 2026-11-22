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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): - Composite CPT: [CPT-saturation as Type-B fold-orbit closure: deriving $\\rho_F \\in \\{m_e, 2m_e\\}$ from crystal structure](#conj:cpt-orbit-closure-density)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): - [CPT-saturation as Type-B fold-orbit closure: deriving $\\rho_F \\in \\{m_e, 2m_e\\}$ from crystal structure](#conj:cpt-orbit-closure-density)\n  becomes a corollary of $\\mathrm{CPT} = C \\cdot P \\cdot T$ once all\n  three factors are established." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean axiomatisation (sketch)\n\n```lean\nclass PFromBraidMirror (M : Type*) [BrCategory M] [Hecke M] where\n  /-- The braid-mirror involution on braid-group elements. -/\n  p_action : Braid n → Braid n\n  /-- P^2 = id. -/\n  p_involution : ∀ β, p_action (p_action β) = β\n  /-- P flips the sign of every Hecke generator. -/\n  p_on_generator : ∀ i, p_action (Hecke.sigma i) = Hecke.sigma_inv i\n  /-- P fixes q (no bar-action). -/\n  p_preserves_q : ∀ q, p_q_action q = q\n  /-- Bar-involution factorisation: bar = P · C · T. -/\n  bar_eq_p_c_t : bar_involution = p_action ∘ c_action ∘ t_action\n```\n\n\n\n2. Closing the conjecture needs an instance of the class above, and a\n   derivation of bar $= P \\cdot C \\cdot T$ as an identity rather than an axiom." },
    { kind: "note", date: "2026-11-15", body: "Scope at the Hecke-letter level (owner instruction 2026-11-15, \"Scope conj:p-from-braid-mirror\", relayed by the coordinator; bean qou-hlx7). Kind and every number unchanged. Lean (`QOU/QuarkState/HelicityCommonSource.lean`): `QOU.QuarkState.Helicity.no_linear_flip` (no scalar-linear algebra map sends a letter to its inverse unless 2(q - 1/q) = 0); `QOU.QuarkState.Helicity.flip_hecke` (the inverse letter satisfies the Hecke relation at 1/q); Klein four-group `flip_flip`, `swap_swap`, `flip_neg`, `flip_swap`, `neg_hecke`; profiles `flip_Pp`, `swap_Pp`, `neg_Pp`, `positron_ne_electron`, `swap_electron`, `neg_electron`; `swap_hecke`, `swap_braid`; `no_linear_neg`. That q -> 1/q has no field automorphism of the reals behind it is a standard fact, not formalised. The §What-remains-open item 1 claim that P preserves the quadratic at q is contradicted by `flip_hecke` and is scoped in the new section, not deleted." },
  ],
});
