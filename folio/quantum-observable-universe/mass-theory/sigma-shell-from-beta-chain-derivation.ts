import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:sigma-shell-from-beta-chain-derivation",
  title:
    "Staircase-partition closed form for the $\\sigma_{\\mathrm{shell}}$ magnitude (convention C; identically zero under convention D)",
  lean: {
    ref: "qou:QOU.BraidKnot.SigmaShellFromBetaChainDerivation",
    validation: "not_checked",
  },
  uses: [
    "prop:compound-beta-shell-calibration",
    "prop:rho-k-h3a-refinement",
  ],
  cites: ["wenzl1988", "kassel1995"],
  tags: [
    "sigma-shell",
    "beta-decay",
    "AME",
    "shell-magnitude",
    "y-target",
    "magic-numbers",
    "1ppb",
    "derivation",
    "convention-c",
    "scope-b-excluded",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`, general $n$)" },
    {
      kind: "caveat",
      body: "This block previously reported 12 % agreement with B(D)/(2m_p); that figure was computed in convention C, on the superseded grouped deuteron word.",
    },
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "**Demoted proposition → conjecture (owner decision S1, 2026-11-15).** " +
        "Under production convention D ($z = q^3/(q^2+1)$) the formula is identically zero: " +
        "every staircase $\\lambda_{\\mathrm{shell}} \\vdash 3A_{\\mathrm{magic}}$ with " +
        "$A_{\\mathrm{magic}} \\ge 2$ has at least three rows, and the Ocneanu weight of every " +
        "such partition vanishes at that $z$ " +
        "(`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`, sorry-free, general $n$; " +
        "stated for this closed form over any field as " +
        "`QOU.BraidKnot.sigma_shell_staircase_vanishes_conventionD` in the Lean sibling). " +
        "So $y_{(3,2,1)}(q_0) = 0$ and $y_{\\mathrm{target}}(2) = 0$ against the benchmark " +
        "$B(D)/(2m_p) \\approx 0.0012$ (witness `sigma-shell-from-beta-chain`, re-run 2026-11-15 " +
        "on the canonical deuteron trace). This is a **scope-(b) exclusion** of the staircase " +
        "construction under convention D, by that proved invariant; it says nothing about other " +
        "constructions of the shell magnitude. The 12 % agreement previously reported was computed " +
        "in convention C on the superseded grouped deuteron word, and was only ever an " +
        "order-of-magnitude match against an order-of-magnitude benchmark. The Lean sibling's " +
        "projection theorem (`sigma_shell_from_beta_chain := inst.identity data`) was a " +
        "self-assuming projection and is removed; the class remains as the conjecture carrier, " +
        "with no instance. Read under convention D, the carrier's single field " +
        "($y_{\\mathrm{target}} = C \\cdot y \\cdot |\\chi| / |\\mathrm{tr}_M|$) therefore asserts only " +
        "$y_{\\mathrm{target}} = 0$ at every magic staircase: as stated, the conjecture predicts no " +
        "shell magnitude at all.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/sigma_shell_from_beta_chain.py",
    witness: "computations/sigma-shell-from-beta-chain.witness.json",
    status: "experimental",
  },
});
