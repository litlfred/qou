import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:z-eq-n-rho-correction",
  title:
    "Z=N substrate-q correction to the Kashaev law: $B = m_e \\cdot \\mathrm{Vol}_{\\rm hyp}(K_A) \\cdot (\\rho_{\\rm struct} + A - [A]_q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.ZeqNRhoCorrection",
    validation: "not_checked",
  },
  uses: [
    "def:substrate-parameter",
  ],
  cites: [],
  tags: [
    "tier:E",
    "binding-energy",
    "kashaev",
    "z-equals-n",
    "q-deformation",
    "rho-substrate",
    "1ppb",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "This conjecture is an **empirical regularity** at the $10^{-3}$\nprecision level — falsifiable by any single Z=N atom whose binding\ndeviates from the formula by more than $10^{-3}$. The natural\nfalsification target is **${}^{20}$Ne** ($n_\\alpha = 5$) once its native\nnon-α-cluster knot pairing is identified.\n\nA categorical derivation requires three lemmas:\n\n1. **L-1** (total-host-count): the Kashaev coefficient at finite $q$\n   is intrinsically $\\rho_{\\rm struct} + A - [A]_q$, with the\n   integer $\\rho_{\\rm struct}$ as its $q\\to 1$ limit. **Open** —\n   the proposed identification of $[A]_q$ as a Markov-trace\n   evaluation has not been written up yet.\n2. **L-2** (selective q-deformation): the Wedderburn-block\n   multiplicity $\\rho_{\\rm struct}$ is q-independent on the generic\n   locus. **Essentially classical** — proof sketch deferred to a\n   follow-up audit.\n3. **L-3** (Z=N decoupling): the isospin-asymmetry correction\n   $\\delta_{\\rm asym}(Z, N)$ vanishes at $Z = N$. Should follow from\n   the Z$\\leftrightarrow$N substrate symmetry; **tractable**.\n\nThis block is the **conjectural form**; downstream theorems consume\nit via the Lean class\n`QOU.BraidKnot.ZeqNRhoCorrection` (resolved via the `lean.ref` field on this block; the `.lean` source lives at `content/quantum-observable-universe/lean/QOU/BraidKnot/ZeqNRhoCorrection.lean`) per\nthe conditional-class policy of\n[AGENTS.md §3b](../../../AGENTS.md).",
    },
  ],
});
