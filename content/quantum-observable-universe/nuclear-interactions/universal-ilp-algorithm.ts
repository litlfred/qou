import { definition } from "../../schema/builders";

/**
 * Universal ILP algorithm for operator selection at every level.
 *
 * The same algorithm derives confinement (B₃), gluon (2σ₀),
 * electron attachment (σ₁⁻¹), and molecular bonding (inv trefoil).
 */
export default definition({
  label: "def:universal-ilp-algorithm",
  title: "Universal ILP algorithm for operator selection",
  lean: { ref: "qou:QOU.Interactions.UniversalILP",
    validation: "not_checked",
  },
  uses: [
  ],
  tags: [
    "ILP",
    "operator-selection",
    "confinement",
    "gluon",
    "covalent-bond",
    "universal",
    "algorithm",
  ],
  computation: {
    engine: "python",
    script: "computations/universal-ilp.py",
    witness: "computations/universal-ilp.witness.json",
    // NOT "verified" — the producer cannot regenerate this witness (bean
    // `qou-uilp`). `universal-ilp.py` calls `apply_atom_nf` at :191/:202 for
    // LEVEL 4 (H₂ bond) and LEVEL 4b (C-C bond); that function has never been
    // defined anywhere in the repo (`git log -S'def apply_atom_nf'` is empty),
    // so the run raises NameError before `results['bond_HH']` is assigned.
    // The committed witness (computedAt 2026-04-14) reports both bond values
    // regardless. The `witness` link is KEPT — that file is genuinely the
    // artifact this block refers to, and it is the only surviving record of
    // the April computation. What was false is the status.
    status: "error",
  },
});
