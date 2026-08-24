import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:operator-selection-lp",
  lean: { ref: "qou:QOU.ParticleInteractions.operator_selection_lp", validation: "not_checked" },
  title: "Knot operator selection as linear program with LP duality",
  tags: [
    "linear-programming",
    "operator-selection",
    "lp-duality",
    "frobenius-dual",
    "gram-matrix",
    "knot-operator",
    "motivic-shadows",
  ],
  uses: ["prop:confinement-lp"],
  computation: {
    engine: "python",
    script: "computations/operator_selection_lp_symbolic_qq.py",
    witness: "computations/operator-selection-lp-symbolic-qq.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-22",
      body:
        "**The dual certificate exists, and the LP is degenerate — both " +
        "exactly, in $\\mathbb{Q}(q)$, 18/18 assertions.** The witness now " +
        "wired above is stdlib-only by design: the question turns on whether " +
        "$\\det G$ is *zero*, not small, and `gram.py` records " +
        "$|\\lambda_{\\min}| = 3.9\\times10^{-17}$ through its NF path at 60 " +
        "dps while `np.linalg.inv` returns $\\|GG^{-1} - I\\| = 1.64$ " +
        "without raising. It carries `q0Anchor: \"independent\"` — it never " +
        "reads $q_0$, which is the point: a numeric check at a pinned $q_0$ " +
        "cannot distinguish \"the certificate exists\" from \"the certificate " +
        "exists at this $q_0$\". For $H_3(q)$: $t$ is row 0 of $G$ " +
        "structurally (the basis contains $\\mathbf{1}$), $\\det G = 0$ " +
        "identically, rank 5, radical the $q$-antisymmetriser, and " +
        "$\\langle\\mathbf{1}, v\\rangle = -(q-1)(q^2-q+1) \\ne 0$ for every " +
        "$q \\ne 1$ — so $y_0 = 0$ is **forced** for every dual-feasible " +
        "pair, and the optimal value is $0$ for every $n_{\\mathrm{target}}$. " +
        "$H_2(q)$ is non-singular, so this is a fact about $H_3$ rather than " +
        "about how the LP was written down. Each assertion names the Lean " +
        "hypothesis it discharges, so the two sides audit against each " +
        "other. The content consequence — $y_0^*$ cannot price the " +
        "constraint it is supposed to price — is bean `qou/8na1` and needs " +
        "an owner ruling, not a mechanical check.",
    },
  ],
});
