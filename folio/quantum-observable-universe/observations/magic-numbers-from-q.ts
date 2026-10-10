import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:magic-numbers-from-q",
  title:
    "Some functional of the Wedderburn-weighted Hoefsmit character data at $q_0$ carries nuclear shell structure",
  tags: [
    "magic-numbers",
    "shell-closure",
    "hoefsmit",
    "wedderburn",
    "seminormal-form",
    "block-diagonal",
  ],
  lean: {
    ref: "qou:QOU.AtomicMass.magic_numbers_from_q",
    validation: "not_checked",
  },
  uses: [],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-09-03",
      body:
        "**The previous title asserted what this block's own scope section refutes**, and is retitled here rather than re-argued. It read *\"Wedderburn nuclear character signal at $q_0$ is **elevated at the magic numbers**\"*, while the scope below records three measurements against exactly that reading: the sign of $\\delta^2\\Phi$ is a parity test satisfied by every even $Z$ and so distinguishes no magic number; the local maxima over even $Z$ at $K=10$ are $Z \\in \\{4,12,16\\}$, none magic, with $Z=8$ ranking sixth of fourteen; and no $q$ in $1 < q < \\varphi$ repairs it. The new title is the block's own opening sentence — *the signal is conjectured to carry nuclear shell structure* — which is the claim that survives. Nothing in the body changed.\n\n**Consequence for §3b-cond: this conjecture must NOT be class-axiomatised.** It is the single largest blocker in the conjectural-propagation audit (17 of 29 violators, every one of them reaching it through the single edge `conj:diagrammatic-double-magic-lr-fusion` → `conj:magic-numbers-from-q`). A class carrier would have to encode *some* content, and the only sharply-stated content available is the identification this block measured and refuted — writing that as a Lean `class` and then discharging 17 provable blocks against it is the laundering AGENTS.md §1a bans, not a refactor. The honest disposition is that the 17 stay violators until either the surviving conjecture is stated precisely enough to axiomatise, or the choke-point edge is retargeted at the *construction* it actually needs.",
      see: "https://github.com/litlfred/qou/blob/main/docs/audits/2026-09-03-propagation-audit-detector-blindness-and-the-magic-number-chokepoint.md",
    },
  ],
});
