import { definition } from "../../schema/builders";

/**
 * The expression κ_closed, and its proved properties.
 *
 * Split from the former `conj:magic-shell-coupling-kappa` (2026-08-10). The
 * physical identification — that this expression is the per-(n_pp − n_nn)
 * excess slope of a magic-shell coupling — is **withdrawn**. The value it was
 * matched against, ≈ −1.0708 MeV, was the Coulomb energy of ³He's pp pair.
 *
 * What survives is an expression and four proved facts about it, none of which
 * depend on any claim about nature:
 *   - `qBracket_eq_canonical` — the bracket is the canonical `qIntBal`
 *   - `qBracket_normaliser_eq_qFactorial` — `[2]_q·[3]_q = [3]_q!`, hence
 *     `q³/y_(3)(q)`, the inverse Markov weight of the trivial partition
 *   - `hParam_pos`, `E0_pos` — positivity of the Hecke deformation and scale
 *   - `kappaClosed_neg` — the forced sign of the expression
 *
 * Evidence for the withdrawal, in order of decisiveness:
 *   - `probe_kappa_coulomb_reconciliation.py` — the two anchors reconcile once
 *     ³He's electrostatic energy is restored; the surviving residual is
 *     excess-INDEPENDENT, so it cannot be a coupling to the p/n asymmetry
 *   - `probe_kappa_provenance.py` — the original fit recorded
 *     `hypothesis_supported: false`; the published value is one of its two arms
 *   - `probe_kappa_mirror_split_shell_test.py` — no term of this form and size
 *     appears in mirror-split binding data at A = 3, 15, 39
 *
 * The removed Lean (`observedMagicShellSlope`, `MagicShellSlopeIsCategorical`,
 * `observedMagicShellSlope_neg`) carried the withdrawn claim and nothing else.
 */
export default definition({
  label: "def:magic-shell-coupling-kappa",
  title:
    "The expression $\\kappa_{\\mathrm{closed}} = -E_0 \\log(1/h) / [3]_q!$ and its proved properties",
  lean: {
    ref: "qou:QOU.BraidKnot.MagicShellCouplingKappa",
    validation: "not_checked",
  },
  uses: [],
  cites: [],
  tags: [
    "q-bracket",
    "q-factorial",
    "markov-weight",
    "hecke-energy-scale",
    "withdrawn-identification",
  ],
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). The bracket content is generic; `Real.log` and the ordering are what force $\\mathbb{R}$." },
    {
      kind: "status",
      date: "2026-08-10",
      body:
        "**Split `conjecture` → `definition`.** The physical identification is withdrawn: the matched value $\\approx -1.0708$ MeV is the Coulomb energy of ${}^{3}$He's $pp$ pair, and the excess coefficient is zero. What remains is the expression and its proved properties, which are untouched by the withdrawal. The block was previously demoted `proposition` → `conjecture` (2026-08-09) for being anchor-identified; that demotion is superseded by this split rather than reversed.",
    },
    {
      kind: "note",
      date: "2026-08-10",
      body:
        "A separate open question was surfaced and deliberately **not** attached to this block: after the electrostatic correction, an excess-*independent* offset of order $0.2$ MeV survives at $A = 3$ that the H7a form does not exhibit at $A = 4$. That is a real unexplained baseline, but it is not $\\kappa$ and should not inherit this block's name.",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/probe_kappa_coulomb_reconciliation.py",
    witness: [
      "computations/kappa-coulomb-reconciliation.witness.json",
      "computations/kappa-provenance.witness.json",
      "computations/kappa-mirror-split-shell-test.witness.json",
      "computations/sigma-f-electron-shell-chain.witness.json",
    ],
    status: "verified",
  },
});
