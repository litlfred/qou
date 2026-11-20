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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean axiomatisation (sketch)\n\n```lean\nclass PFromBraidMirror (M : Type*) [BrCategory M] [Hecke M] where\n  /-- The braid-mirror involution on braid-group elements. -/\n  p_action : Braid n → Braid n\n  /-- P^2 = id. -/\n  p_involution : ∀ β, p_action (p_action β) = β\n  /-- P flips the sign of every Hecke generator. -/\n  p_on_generator : ∀ i, p_action (Hecke.sigma i) = Hecke.sigma_inv i\n  /-- P fixes q (no bar-action). -/\n  p_preserves_q : ∀ q, p_q_action q = q\n  /-- Bar-involution factorisation: bar = P · C · T. -/\n  bar_eq_p_c_t : bar_involution = p_action ∘ c_action ∘ t_action\n```\n\n\n\n2. Closing the conjecture needs an instance of the class above, and a\n   derivation of bar $= P \\cdot C \\cdot T$ as an identity rather than an axiom." },
  ],
});
