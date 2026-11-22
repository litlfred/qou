import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:c1-ggm-bar-parity-faces",
  lean: {
    ref: "qou:QOU.Mass.DoorVParityNoIdentity.doorV_parity_no_identity",
    validation: "validated",
  },
  title:
    "The binding q-lift module and the resurgent Stokes carrier are bar-parity " +
    "conjugate faces",
  uses: [
    "conj:qdifference-kernel-prolongation-symbol",
  ],
  cites: ["mcspirit-rolen2025"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): measured in\n[`door_v_residual_scope_probe.py`](../../../computations/probes/door_v_residual_scope_probe.py))." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (`QOU.Mass.GGMAlternationOnset.ggm_solution_no_double_flip`, over an\nordered field)." },
    {
      kind: "note",
      body: "An earlier version of this note denied that the recurrence oscillates inside the window; it does, but never at two consecutive pairs.",
    },
    {
      kind: "status",
      date: "2026-08-08",
      body:
        "**Created by the F3 split** (owner-confirmed 2026-08-08). The parent " +
        "block `conj:qdifference-kernel-prolongation-symbol` used to assert an " +
        "equivalence between its kernel's carrier and the GGM/Stokes datum. " +
        "That equivalence is refuted at the module level — the Newton polygons " +
        "differ ({1/2,1/2} vs {-1,+1}), now machine-checked from the operators' " +
        "coefficient valuations by " +
        "`QOU.Mass.ThetaSlopeArithmetic.newtonSlopes_c1_ne_ggm`, and by " +
        "[rsz2013] Thm 2.2.1(i) + Thm 2.2.4 the slope multiset is a gauge " +
        "invariant. The clause was removed there.\\n\\n" +
        "This block exists so the surviving relationship is stated as content " +
        "rather than lost. It is not a weakened restatement of the refuted " +
        "clause: the Door-iv/v probes MEASURED the residual and found it " +
        "minimal and named. The tensor square is anisoclinic with slopes " +
        "{+1,0,-1}, which CONTAINS the Stokes carrier's {+1,-1} — the first " +
        "construction with the right graded module, circumventing the " +
        "Newton-polygon obstruction that blocks the rank-2 comparison. On that " +
        "graded piece the unipotent part is trivial and the connecting matrix " +
        "is constant, so there is no Stokes obstruction either. The sole " +
        "difference is a diagonal Z/2 character (-1)^m.\\n\\n" +
        "**What is Lean-proved is the obstruction half, and it is not " +
        "vacuous**: `doorV_parity_no_identity` shows no non-negative-cone " +
        "combination of the tensor-square sequences can equal a " +
        "sign-alternating target, because the left side lies in the " +
        "non-negative cone (a real square is non-negative) while a single " +
        "consecutive sign flip already excludes it. That is a scope-(b) " +
        "exclusion citing a proved invariant, not a numerical near-match. This " +
        "block gives that theorem its first content-block home — it had none.\\n\\n" +
        "**What remains conjectural** is the positive half: that after the " +
        "bar-parity twist the two agree exactly, i.e. that the twist is the " +
        "WHOLE difference and not merely a difference. The graded and Stokes " +
        "comparisons are probe-level (docs/audits/2026-07-20-qlift-doorIV-matrix.md, " +
        "2026-07-20-qlift-doorV-stokes.md); the exact-coefficient identity is " +
        "the Door-iii target, bean qou-ceg6. Nothing is wired on this block.\n\n" +
        "**Update, same day: one reading of the positive half is now EXCLUDED.** " +
        "The twist inverts EVERY consecutive-pair sign, not only the " +
        "alternating ones (`barTwist_consecutive_product`), so it can clear the " +
        "non-negativity obstruction only for a target alternating at every pair " +
        "— and the Stokes carrier's solution is flip-free below " +
        "m+1 = log2/log q, where 2 - q^{m+1} > 0. Hence the twisted sequence " +
        "acquires flips exactly where the untwisted one had none and " +
        "`doorV_parity_no_identity` fires on it too: the twist RELOCATES the " +
        "obstruction rather than removing it. Proved as " +
        "`obstruction_fires_on_one_of` and " +
        "`twist_clears_only_if_everywhere_alternating`; measured in " +
        "`computations/qbeta/c3_w2_bar_parity_twist_probe.py` (4/4), which " +
        "records the twisted flip positions. So the residual claim must be read " +
        "at MODULE level, up to a gauge over the q-difference field — not as " +
        "'(-1)^m z is a non-negative combination of the squares'. That scalar " +
        "reading is excluded by the very invariant that supplies the " +
        "obstruction. The module reading is untouched and is what the block " +
        "conjectures. A scalar least-squares fit against a prose-reconstructed " +
        "f_+/f_- was run and is deliberately NOT reported: the reconstruction " +
        "is not trustworthy enough to carry a negative result, and the finding " +
        "above needs only the carrier's own recurrence.",
      see: "docs/audits/2026-07-20-qlift-doorV-stokes.md",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note — the Lean file already says this, but the " +
        "checker cannot read it.** `DoorVParityNoIdentity.lean`'s own module " +
        "docstring states: *\"§7c: this is genuinely archimedean (sign / " +
        "ordering of `ℝ`), so `ℝ` is the correct base ring here — not a " +
        "gratuitous specialization.\"* The `wall-side-correct` criterion reads " +
        "only the block `.md` and this `.ts` `authorNotes`, never the `.lean` " +
        "docstring, so that acknowledgement never reached it. This note is " +
        "the missing carrier.\\n\\n" +
        "The substance stands on its own: the whole theorem is an **ordering** " +
        "claim. `nonneg_not_signalternating (s : ℕ → ℝ) (hs : ∀ n, 0 ≤ s n)` " +
        "concludes `¬ (s n * s (n+1) < 0)` from `mul_nonneg`; " +
        "`posCone_nonneg` builds the non-negative cone from `add_nonneg`; and " +
        "`doorV_parity_no_identity` derives the scope-(b) exclusion from a " +
        "single sign flip `y m * y (m+1) < 0`. The cited invariant *is* the " +
        "non-negativity of a real square. Delete the ordering and there is no " +
        "statement left.",
    },
  ],
  tags: [
    "q-difference",
    "binding",
    "stokes",
    "colored-jones",
    "open-problem",
  ],
});
