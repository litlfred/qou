import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:psd-trace-orthogonality",
  title:
    "PSD-vs-trace orthogonality of canonical atom-braid Wedderburn blocks. At q₀, the partitions λ ⊢ 3A that dominate the Markov trace `Σ_λ y_λ χ^λ(T_w)` and the partitions that dominate the PSD obstruction `α* = 1/(1 − ε_min)` live in *disjoint shape-class subcategories*: trace-dominant = 1/2-row long-string partitions, PSD-dominant = 3+row multi-step narrow partitions. Empirically supported with 10⁵ magnitude separation at A=4 and 10⁹ at A=6.",
  lean: { ref: "qou:QOU.BraidKnot.PSDTraceOrthogonality.psd_trace_orthogonality_holds_for_all_atoms" },
  uses: ["conj:atom-braid-exterior-algebra"],
  cites: [],
  authorNotes: [
    {
      kind: "status",
      date: "2026-05-25",
      body:
        "**Empirically verified across A=4 (⁴He) and A=6 (⁶Li) via the " +
        "Lanczos LinearOperator probe** on canonical T_w. At A=4 the PSD-" +
        "dominant pair (4,4,4)/(3,3,3,3) contributes 0.030% / 0.0002% of " +
        "|tr_M_partial|. At A=6 the PSD-dominant (3,3,3,3,2,2,2) has " +
        "y_λ ≈ −7.85×10⁻¹⁵ vs trace-dominant [17,1] y_λ ≈ +7.08×10⁻⁶ — " +
        "a 9 OOM separation. **Note (2026-05-25):** the *specific* PSD-" +
        "dominant shape varies with A — at A=4 it is the (A,A,A) " +
        "rectangle; at A=6 it is multi-step (3,3,3,3,2,2,2) (post-Probe 4c " +
        "falsification of the rectangular-form conjecture). The " +
        "shape-class-disjointness is what's conjectured to be universal, " +
        "NOT the specific dominant shape.",
    },
    {
      kind: "note",
      date: "2026-05-25",
      body:
        "Sign pattern: the 3 deepest PSD-dominant shapes at A=6 all have " +
        "NEGATIVE y_λ. They would *subtract* from any positive χ " +
        "contribution. This encodes the bar-anti-symmetric content of " +
        "the σ_avg crossings structurally — these blocks are the " +
        "carriers of the obstruction, not the carriers of the mass.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean sibling is otherwise entirely " +
        "combinatorial — `Partition n` is a subtype of `List ℕ`, and " +
        "`numRows` / `maxRow` are `ℕ`-valued. Its single `ℝ` is " +
        "`etaLowerBound : ℝ` on the `PSDTraceOrthogonalDecomp` class, which " +
        "carries the **empirical magnitude separation** " +
        "`η(A) := max|y_trace| / |y_PSD|` (η(4) ≈ 1.6×10⁵, η(6) ≈ 9×10⁸, from " +
        "the Lanczos probes recorded above). That is a measured ratio bounded " +
        "below — a quantity that is both experimental and order-theoretic, so " +
        "`ℝ` by two independent §7c rows. The shape-class disjointness the " +
        "conjecture actually asserts needs no base ring at all.",
    },
  ],
  tags: [
    "tier:S",
    "atom-braid",
    "wedderburn-decomposition",
    "markov-trace",
    "psd-cone",
    "shape-class-orthogonality",
    "hecke-algebra",
    "open-conjecture",
    "bar-involution",
  ],
  computation: {
    engine: "python",
    script: "computations/atom_level_wedderburn_tower.py",
    witness: "computations/atom-level-wedderburn-tower.witness.json",
    status: "verified",
  },
});
