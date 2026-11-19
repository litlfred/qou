import { conjecture } from "../../schema/builders";

// Demoted from `proposition` to `conjecture` per AGENTS.md §3b
// (conjectural propagation): the leading-order closed form
// `N_v = |S_5| · q_0^{90}` depends on two upstream `conj:` blocks
// (`conj:n-v-bring-action` and `conj:n-v-tower-depth-ninety`),
// hence the conditional result is itself conjectural.  The prose
// already acknowledges "Conditional theorem"; the block kind now
// matches.  See `docs/audits/conjecture-cones.md` (`conj:mass-
// endomorphism` cone) for the audit that flagged this.
export default conjecture({
  label: "conj:n-v-leading-order-derivation",
  title: "Leading-order $N_v = |S_5| \\cdot q_0^{90}$ ($= 120 \\cdot q_0^{90}$)",
  cites: [],
  uses: [
    "conj:n-v-bring-action",
    "conj:n-v-tower-depth-ninety",
    "ex:hadron-half-life-verification",
  ],
  defines: [],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-03",
      body:
        "**The bridge is now a THEOREM, and the block is axiom-clean.** " +
        "`v_over_m_e_bridge` was an `axiom` asserting " +
        "`\u2203 \u03b5\u2081, |\u03b5\u2081| \u2264 0.006 \u2227 v/m_e = 40\u00b7q\u2080\u2079\u2070\u00b7(1+\u03b5\u2081)` \u2014 but q\u2080, m_e " +
        "and v are concrete decimal literals, so that is a finite arithmetic " +
        "fact about rationals, not an open claim. Assuming a decidable " +
        "numeric statement is the shape AGENTS.md \u00a7\u201cAxiomatization is NOT a " +
        "Proof\u201d warns about, and it cost something real: every result in this " +
        "file named the axiom in `#print axioms`. It is now proved (witness = " +
        "the exact residual, bound discharged by `norm_num`), and " +
        "`n_v_leading_order` went from naming it to " +
        "`[propext, Classical.choice, Quot.sound]`. lean-direct exit 0, zero " +
        "warnings, 3.2 s.",
    },
    {
      kind: "caveat",
      date: "2026-09-03",
      body:
        "**Proving the number did not derive the structure \u2014 bean `qou-5lib`.** " +
        "Fix the two integers (|S_5| = 120, tower depth = 90) and everything " +
        "else is arithmetic, which is precisely why the axiom carried **no " +
        "conjectural content**: it asserted the arithmetic and left the " +
        "categorical claim unstated. Still open, and expressed by no Lean " +
        "object: BraneTowerLevel as a Gr\u00f6bner\u2013Shirshov filtration grade; the " +
        "q\u2080-rescaling-per-generation lemma; the categorical derivation of " +
        "|S_5|/3 = 40; and the depth-90 Coxeter tower. No carrier was invented " +
        "for them on purpose \u2014 a class that merely re-pins 120 and 90 would be " +
        "provable, hence would assert nothing.",
    },
    {
      kind: "note",
      date: "2026-09-03",
      body:
        "**The file\u2019s own numeric check was wrong in all three figures, and the " +
        "bound is tighter than it looked.** Recomputed in exact rational " +
        "arithmetic (`fractions.Fraction`) and cross-checked at mp.dps=50: " +
        "`q\u2080\u2079\u2070 = 11977.4350` (the docstring said \u224812012, 0.29 % high), " +
        "`ratio = 40.2290` (said \u224840.11), `\u03b5 = 0.0057255983` (said \u22480.003). " +
        "So `|\u03b5| \u2264 0.006` holds with a headroom factor of **1.048** \u2014 the old " +
        "text understated \u03b5 by 1.9\u00d7 and made the bound look about twice as " +
        "slack as it is. Anyone tightening the bound or re-pinning q\u2080 should " +
        "know it is 4.8 % from failing.",
    },
  ],
  tags: ["n-v", "electroweak", "derivation", "conditional"],
  lean: { ref: "qou:QOU.Observations.n_v_leading_order" },
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/probes/bring-gerbe-obstruction-and-40-prefactor.witness.json",
    status: "verified",
  },
});
