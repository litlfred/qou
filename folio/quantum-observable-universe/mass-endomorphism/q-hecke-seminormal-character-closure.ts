import { proposition } from "../../schema/builders";

/**
 * The q-Hecke character gap is closed: the partition-sum form of
 * the Markov trace
 *
 *     tr_M(β) = Σ_{λ ⊢ 3A} y_λ(q) · χ^λ_q(β)
 *
 * agrees with the canonical Markov-axiom reducer to numerical
 * precision (1e-13 for proton/neutron, 1e-10 for deuteron at
 * float64; 1.4e-16 at 50-dps mpmath via PR #564's
 * `rho_k_h3a_refinement.py`).
 *
 * The closure has two ingredients, both already in the repo:
 *   1. y_λ(q): Wenzl's Schur principal specialization
 *      (`markov_weights_symbolic.solve_y_lambda` →
 *       `wedderburn_jones_markov.y_lambda_at`,
 *       numerical-q-from-start).
 *   2. χ^λ_q(β): trace of the Hoefsmit seminormal representation
 *      ρ_λ(β) at q (`hecke_characters.build_seminormal_matrices` +
 *      `mass_at_3A_proper.chi_lambda_of_word`).
 *
 * The composition lives in
 * `wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`.
 *
 * Verified by `tr_m_q_hecke_seminormal.py` against
 * `markov_trace_recursive` (canonical) for proton, neutron, deuteron.
 *
 * No new sorrys: the proposition is an equality between three
 * already-implemented numerical paths.  This block records that
 * agreement so downstream consumers know the partition-sum form is
 * usable for ρ_K binding-fraction analysis (#564 P3') without
 * re-deriving.
 */
export default proposition({
  label: "prop:q-hecke-seminormal-character-closure",
  title:
    "Partition-sum form of $\\mathrm{tr}_M$ via Wenzl $y_\\lambda$ and " +
    "Hoefsmit $\\chi^\\lambda_q$ agrees with the canonical Markov-axiom reducer",
  lean: {
    ref: "qou:QOU.BraidKnot.QHeckeSeminormalCharacterClosure.QHeckeSeminormalCharacterClosureContext",
    validation: "leanok",
  },
  uses: [],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
    "mathas1999",
    "jones1987",
    "jing-liu-2021",
  ],
  computation: {
    engine: "numpy",
    script: "computations/tr_m_q_hecke_seminormal.py",
    witness: [
      "computations/tr-m-q-hecke-seminormal.witness.json",
      "computations/atomic-tr-m-mpfr-50dps-proton.witness.json",
      "computations/atomic-tr-m-mpfr-50dps.witness.json",
      "computations/rho-k-h3a-refinement.witness.json",
      "computations/canonical-tr-m-three-path-comparison.witness.json",
      "computations/probes/the_character_closure_block_and_a_lean_file_publish_convention_c_probe.witness.json",
      "computations/laurentq-a5-ceiling-measure.witness.json",
      "computations/markov-z-full-bar-condition.witness.json",
    ],
    status: "verified",
    requires: ["numpy", "sympy"],
  },
  tags: [
    "q-hecke-character",
    "seminormal",
    "hoefsmit",
    "wenzl",
    "jones-markov",
    "partition-sum",
    "cross-check",
    "infrastructure",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body: "Moved from prose: The earlier claim that \"all three paths agree at the precision floor of their\nrespective layers\" is **withdrawn as stated**: that agreement was measured\nwithin convention C, and `canonical_tr_m_three_path_comparison.py` records that\nthe three paths do *not* all agree under D — `pyhecke` SW disagrees by orders of\nmagnitude and the legacy path by ~15 % — while `markov_peel`'s proton and\nneutron entries were deliberately removed as unreliable (`qou-46ab`). What holds\nis the narrower statement the block actually needs: bridge ≡ `markov_peel` where\nboth are recorded. (Bridge witness: atomic-tr-m-mpfr-50dps-proton.witness.json.)",
    },
    {
      kind: "refined-framing",
      date: "2026-09-05",
      body: "**Migrated C → D, 2026-09-05** (`qou-i229` → `qou-46ab`, owner-approved:\n*\"refresh and migrate\"*). Source: the canonical Hoefsmit + Wenzl bridge witness\n`atomic-tr-m-mpfr-50dps.witness.json`, which computes these five atoms by this\nblock's own stated method $\\sum_\\lambda y_\\lambda \\chi_\\lambda$ at\n`q0Anchor: muon`.\n\n" +
        /* <!-- literal-source: historical pre-intra-ordering-ruling (2026-08-29 grouped braid word) C->D migration table --> */
        "| atom | was (convention C) | now (convention D) | ratio |\n|---|---:|---:|---:|\n| Proton | $1.06530622859$ | $1.14575978232$ | $1.0755$ |\n| Neutron | $0.92323329717$ | $0.98774375682$ | $1.0699$ |\n| Deuteron | $0.38828647155$ | $0.57517232973$ | $1.4813$ |\n" +
        /* <!-- literal-source: historical pre-intra-ordering-ruling (2026-08-29 grouped braid word) C->D migration table --> */
        "| Tritium | $0.10405211868$ | $0.22931014615$ | $2.2038$ |\n| ${}^3$He | $0.20654085856$ | $0.40376713691$ | $1.9549$ |\n\nThe proton ratio is `qou-46ab`'s signature, established there to 50 digits:\nC-frame $1.0653062286131670594$ against D-frame $1.1457597822878355047$,\n$|D-C|/C = 0.0755215$.\n\n**The anchor is unchanged.** The C table was muon-anchored — its per-atom\n$D/C$ ratios match `qou-46ab`'s convention ratio at the muon pin to 8 digits\nand at the proton pin only to 7 — so this is a convention migration, not a\nre-anchoring. The muon pin used is the live one, the same target as the\n`q₀` refresh in this pass.\n\n**The two-column form is withdrawn, not recomputed.** The table used to print\n$|\\mathrm{tr}_M|$ *canonical* against *partition-sum* with a $\\sim 10^{-15}$\n\"relative error\", and that column read as a verification of the values. It was\nnot: it was the agreement of **two C-frame paths**, which says nothing about\nwhich convention both are in. The character-closure identity is\nconvention-independent and the declaring probe verifies it on abstract braids,\nso the two paths agree under D as well — but **that agreement has not been\nre-measured at these five nuclei**, because the second path is `markov_peel`,\nwhose proton and neutron entries `qou-46ab` deliberately removed as unreliable\n(`canonical_tr_m_three_path_comparison.py`). Printing a residual nobody has\nmeasured would repeat the defect this migration is fixing.",
    },
    {
      kind: "refined-framing",
      date: "2026-09-05",
      body: "**Ordering corrected 2026-09-05** (`qou-hu1f`). Earlier the same day these\nvalues were migrated C → D from `atomic-tr-m-mpfr-50dps.witness.json` — which\nwas computed **2026-08-29, before** the intra-ordering owner ruling, and had\nnever been regenerated. The producer has now been re-run under the ruling and\nthe table takes its output:\n\n" +
        /* <!-- literal-source: historical muon-pinned borromean vs grouped comparison table before 2026-11-15 proton-pin move --> */
        "| atom | grouped (superseded) | **borromean (the ruling)** |\n|---|---:|---:|\n| Proton | $1.14575978232$ | $0.62932842249$ |\n| Neutron | $0.98774375682$ | $0.47513351767$ |\n| Deuteron | $0.57517232973$ | $0.15196834396$ |\n" +
        /* <!-- literal-source: historical muon-pinned borromean vs grouped comparison table before 2026-11-15 proton-pin move --> */
        "| Tritium | $0.22931014615$ | $0.02914404235$ |\n| ${}^3$He | $0.40376713691$ | $0.05859625835$ |\n\nA factor of $1.8$ to $7.9$, growing with $A$ — far larger than the convention\nmigration that preceded it. `atom_braid_word_3A` lays each nucleon's\nconfinement core down alternating, `(σ₀σ₁⁻¹)³`, because `σ₀` and `σ₁` do not\ncommute and only the alternating word is `β_Bor`.\n\nBoth axes are now current: **convention D** and the **borromean** ordering, at\nthe muon pin, all three taken from the producer rather than substituted by hand.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body: "**Pin moved muon → proton, 2026-11-15** (owner-approved; the proton pin is the compute default\nby the 2026-08-07 directive). The values above are read from\n`atomic-tr-m-mpfr-50dps-proton.witness.json`, the same producer at `q0Anchor: proton`. The muon-pin\nvalues in the two history notes below differ from them by about $3 \\times 10^{-8}$ relative (the $\\mu$–p\nsubstrate tension), so read those notes as muon-pinned records.",
    },
    {
      kind: "refined-framing",
      date: "2026-09-06",
      body: "**Corrected 2026-09-06** (`qou-fq0f`). Bullet 1 used to discriminate on\n*vanishing*: that $s_\\lambda(q,q^{-1})/H_q(\\lambda)$ \"vanishes for partitions\nwith three or more rows and so cannot serve as the weight\". Under production\nconvention **D** that reason is vacuous, because $y_\\lambda(q)$ vanishes there\ntoo — see the row cap below. It was a **convention-C argument**, true when\nwritten and left untouched by the C → D migration of 2026-08-09.",
    },
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** The context " +
        "class types both compute paths — `tr_M_partition_sum` (Wenzl `y_λ` · " +
        "Hoefsmit `χ^λ_q`) and `tr_M_axiom_reducer` (canonical Markov-axiom " +
        "reducer) — over `ℝ`. This proposition records their *numerical* " +
        "agreement at the substrate anchor, so the specialisation is " +
        "intrinsic: a generic-ring restatement would assert a different, " +
        "symbolic proposition.",
    },
    {
      kind: "status",
      body: "The proposition is a numerical-equality claim between three\nimplemented paths, all of which agree to their precision floors.\nMathematical proof: the partition-sum form is the spectral\nexpansion of $\\mathrm{tr}_M$ in the Wedderburn–Artin basis. The\ncanonical Hecke character $\\chi^\\lambda_q$ is the diagonal of\n$\\rho_\\lambda^q$ in the seminormal basis (Hoefsmit 1974, Mathas\n1999 §3.4); $y_\\lambda(q)$ is the unique Jones-Markov weight given\nthe Markov axioms (Wenzl 1988). Combining: the partition-sum form\nidentically equals the recursive Markov ascent. Numerical\nverification confirms.",
    },
  ],
});
