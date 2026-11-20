import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean axiomatisation (sketch)\n\n```lean\n-- Conditional on the color-tube channel-assignment class:\nclass CFromColorFlavorSwap\n    (M : Type*) [BrCategory M] [ColorTube M]\n    [InterNucleonChannelColorTube M] where\n  /-- The Z/2 flavor-conjugation involution on color-sheet flavors. -/\n  c_action : ColorSheetFlavor → ColorSheetFlavor\n  /-- C^2 = id. -/\n  c_involution : ∀ f, c_action (c_action f) = f\n  /-- C commutes with the color-tube weight tensor (flavors are\n      conjugation invariant). -/\n  c_commutes_W :\n    ∀ (F₁ F₂ : NucleonFlavorContent) (c₁ c₂ : ColorSheet),\n      color_tube_weight (c_action F₁) (c_action F₂) c₁ c₂\n        = color_tube_weight F₁ F₂ c₁ c₂\n  /-- CPT factorisation: C · P · T = bar-involution. -/\n  cpt_factorisation :\n    bar_involution = c_action ∘ p_braid_mirror ∘ t_trace_reverse\n```\n\nThe class becomes inhabited by the color-tube data once [Inter-nucleon Hecke channel assignment from Bring color-tube weighting](#conj:inter-nucleon-channel-color-tube) is instantiated.\n\nType-B folding for chirality and CPT (`conj:type-b-folding-cpt`)\n\n([`verify_c_color_swap.py`](../../../computations/verify_c_color_swap.py), [`verify-c-color-swap.witness.json`](../../../computations/verify-c-color-swap.witness.json))\n\nThe statement is conjectural only for as long as [...] and the $S_5 \\leftrightarrow \\mathrm{SO}(3)$ fiber-action class `conj:s5-so3-fiber-action` remain uninhabited; supplying both makes it unconditional.\n\n—the CPT composite, already formalised" },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "Tracker/working-channel pointers pulled out of the published prose " +
        "when this block was rewritten from a branch work plan into a paper " +
        "section: this is D6 of the duality tracker (`docs/duality-tracker.md` " +
        "§1, and §2 Cluster A for the D5 -> D6 + D7 + D8 CPT decomposition); " +
        "D7 = `conj:p-from-braid-mirror`, D8 = `conj:t-from-trace-cyclicity` " +
        "-- both now authored. Type-B folding for chirality/CPT is D22 " +
        "(AGENTS.md §7b, `conj:type-b-folding-cpt`). Upstream " +
        "`conj:inter-nucleon-channel-color-tube` landed in PR #1111; its own " +
        "supplier class `conj:s5-so3-fiber-action` is PR #1081. The former " +
        "`## Diagnostics` stanza was written against " +
        "`.claude/skills/local/canonical-watcher.md` §Slot J; its content " +
        "(GB filtration level, jet order, bar-symmetry status) is retained in " +
        "the block as the `## Structural position` section.",
    },
  ],
  label: "conj:c-from-color-flavor-swap",
  title:
    "Charge conjugation $C$ as the color-sheet flavor-swap $u \\leftrightarrow \\bar u$, $d \\leftrightarrow \\bar d$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.CFromColorFlavorSwap",
    validation: "not_checked",
  },
  uses: [
    "conj:cpt-d6-d7-d8-closure",
    "conj:inter-nucleon-channel-color-tube",
    "conj:cpt-orbit-closure-density",
    "def:bar-involution",
  ],
  cites: [
    "kashiwara1991",
    "khovanovlauda2009",
    "wigner1937",
  ],
  tags: [
    "charge-conjugation",
    "color-tube",
    "duality-d6",
    "cpt-decomposition",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
  ],
});
