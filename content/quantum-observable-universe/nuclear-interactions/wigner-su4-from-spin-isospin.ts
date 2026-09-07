import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:wigner-su4-from-spin-isospin",
  title:
    "Wigner $\\mathrm{SU}(4) = \\mathrm{SU}(2)_S \\times \\mathrm{SU}(2)_I$ as the categorical source for nuclear-shell binding",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.WignerSU4FromSpinIsospin",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-05",
      body:
        "**§7c archimedean specialisation, acknowledged.** The Lean carrier " +
        "`QOU.BraidsAndKnots.WignerSU4FromSpinIsospin` is stated over `ℝ`, not over a " +
        "generic `{R : Type*}`. This is deliberate and not a §7c default violation: the " +
        "capacity law is `E_gate = E₀ · ln(1 / W_λ)`, so `Real.log` appears in the " +
        "statement itself and there is no weaker base ring that admits it. The " +
        "specialisation is confined to that one construct — no ordering, no `Real.sqrt`, " +
        "no `Real.exp` — and the block sits on the observable side of the wall, where the " +
        "Plancherel weight `W_λ` and the AME binding `B_AME` are both measured quantities.",
    },
    {
      kind: "status",
      date: "2026-09-05",
      body:
        "**Ref repointed; the previous carrier could have no instance.** This block's " +
        "`lean.ref` used to name `QOU.BraidsAndKnots.WignerSu4FromSpinIsospin` (lower-case " +
        "`u`) — a sibling stub whose only field was `holds : Prop`, i.e. a carrier " +
        "asserting nothing — while the substantive class sat unread under `namespace QOU` " +
        "at `QOU/ParticleInteractions/`. The stub is deleted and the real carrier moved to " +
        "`QOU/BraidsAndKnots/` so the declaration path matches the file path and §0a " +
        "candidate-2 resolution applies, following the disposition `TFromTraceCyclicity` " +
        "already established.\n\n" +
        "The moved carrier also needed repair, in the opposite direction from the stub's. " +
        "Its two content-bearing fields quantified over *all* reals with no hypothesis " +
        "relating them, so `E_gate = E₀ · ln(1/W_λ)` instantiated at `E_gate := 1`, " +
        "`E₀ := 0` forced `1 = 0`: no instance could exist, and every conditional theorem " +
        "on the class would have been vacuously true. The quantities are now " +
        "caller-supplied parameters, and both directions are discharged as theorems — " +
        "`wignerSU4FromSpinIsospin_refutable` (it can be false) and " +
        "`wignerSU4FromSpinIsospin_satisfiable` (an instance can exist), the latter " +
        "recorded so that \"no instance is provided\" reads as *the conjecture is open* " +
        "rather than *none could exist*.",
    },
  ],
  uses: [
    "conj:isospin-from-canonical-bowtie",
    "conj:spin-from-so3-fiber",
  ],
  cites: [
    "wigner1937",
    "elliott1958",
    "kashiwara1991",
    "khovanovlauda2009",
  ],
  tags: [
    "wigner-su4",
    "duality-d11",
    "spin-isospin",
    "nuclear-shell",
    "l3-binding",
    "magic-shell",
    "cluster-b-closure",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
  ],
});
