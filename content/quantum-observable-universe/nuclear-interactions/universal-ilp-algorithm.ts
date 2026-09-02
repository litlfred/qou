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
    // `error`, not `failed`: main's vocabulary, kept. This merge briefly
    // carried BOTH — my `failed` above main's `error` — which TypeScript
    // accepts as a duplicate key with the last one silently winning. A
    // conflict resolved by "keep both sides" is safe for an array of notes
    // and is not safe for an object key.
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
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-24",
      body:
        "**`computation.status` demoted `verified` -> `failed`** (bean " +
        "`qou-v5fp`). `failed` rather than a new `stale` value because the " +
        "corpus's established set is `verified` / `experimental` / `failed` " +
        "/ `not_run`. Three independent reasons, each sufficient alone. " +
        "(1) The producer **raises before finishing**: " +
        "`computations/universal-ilp.py` dies at Level 4 with " +
        "`NameError: apply_atom_nf is not defined`, and " +
        "`apply_atom_nf` exists nowhere in the repository. It never reaches " +
        "`w.save()`. (2) The witness is therefore **not reproducible**: " +
        "`universal-ilp.witness.json` carries `computedAt: 2026-04-14` and " +
        "`commitSha: 95eb85e4`, four months and many conventions ago. " +
        "(3) Its assertions were **tautological**: all five read " +
        "`computed=sel[0], expected=sel[0]`, so the file records " +
        "`\"computed\": \"sigma_1\", \"expected\": \"sigma_1\"` and " +
        "`allPassed: true` was guaranteed regardless of what the script " +
        "produced.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "What was and was not repaired. The tautology is fixed at source: " +
        "the witness block now asserts that the reported operator label " +
        "re-parses to its own crossing count, which is independent of the " +
        "selection rule and can fail. Two more obvious repairs were " +
        "considered and rejected as tautologies in longer form — asserting " +
        "the selection is Frobenius-feasible, or that it is minimum-crossing " +
        "among feasible — because `universal_ilp` scans crossing number " +
        "upward and takes the first feasible candidate, so both hold by " +
        "construction. The comment at the site records this so the next " +
        "author does not re-introduce one.",
    },
    {
      kind: "caveat",
      date: "2026-08-24",
      body:
        "`apply_atom_nf` was **not** reconstructed. `build_atom_nf(Z, N)` " +
        "builds an atom NF from scratch; the missing function applied an " +
        "atom's construction to an *existing* NF, and nothing in the tree " +
        "records what that composition was. Guessing it would fabricate the " +
        "molecular levels rather than restore them. Until someone recovers " +
        "the intended semantics, levels 4 and 4b (H-H and C-C bonds) produce " +
        "nothing and this block's molecular claims have no live producer.",
    },
    {
      kind: "note",
      date: "2026-08-24",
      body:
        "The tautological-assertion shape is **not local to this producer**: " +
        "an AST sweep of 3,253 Python files found **266 of 3,482** " +
        "`add_assertion` calls (7.6%, across 195 files) passing the same " +
        "expression as `computed` and `expected`. Tracked as bean " +
        "`qou-26f2`; this block is one instance and its repair is not a " +
        "template for the other 265, several of which will have real " +
        "expected values that were simply mis-wired.",
    },
  ],
});
