import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "caveat",
      date: "2026-08-11",
      body:
        "**The caption's precision claim was wrong and is now scoped.** It " +
        "read *\"match CODATA to sub-keV precision\"* over a table whose own " +
        "binding-energy row differs by 1 keV, and whose proof closes at a " +
        "$-0.53\\%$ residual on $m_n - m_p$ — about 6.9 keV, seven times the " +
        "figure claimed. The neighbouring `rem:dressed-quark-numerology-at-q0` " +
        "already stated the residual plainly, so the caption was the outlier " +
        "in its own neighbourhood.\n\n" +
        "**Two things this did not fix, both derivation work rather than " +
        "wording.** (1) The formula column and the proof are different routes: " +
        "the column applies $Q(q)$ to a Hopf-link mass, the proof sums Skein " +
        "crossing pairs over dressed quark masses. Nothing here shows they " +
        "agree. (2) The deuteron and binding-energy rows are not derived by " +
        "the accompanying proof; whether another block derives them was not " +
        "established. Either derive them here or move them to the block that " +
        "does. Surfaced by the adversarial second reader on PR #4921.",
    },
  ],
  label: "prop:terminal-resolution",
  lean: { ref: "qou:QOU.Experimental.TerminalResolution",
    validation: "not_checked",
  },
  title: "Terminal Resolution of Hadronic Mass",
  uses: [
    // Was rem:skein-mass-relation, reached only for "q = q_0 fixed by the
    // lepton mass ratio". q_0 is fixed by the CAL-2 calibration, which is a
    // definition; the remark's route went through conj:topological-mass-formula.
    // Retargeted 2026-11-20 (owner, option 2 on the q_0 pair; bean qou-tm3c).
    "def:three-calibration-discipline",
    "cor:mass-identity-C",
  ],
  proofs: ["prf:terminal-resolution"],
  tags: ["mass", "hadronic"],
});
