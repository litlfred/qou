**Conjecture (atom-braid exterior-algebra structure; partial-closure: verified at $A \leq 4$, general $A$ open).** *Let `A = Z + N` with $Z \geq 1$, $N \geq 0$, and let $T_w(Z, N) \in B_{3A}$ denote the canonical atom-braid word `atom_braid_word_3A(Z, N)` (`mass_at_3A_proper.py` recipe). Its image in the Iwahori–Hecke algebra $H_{3A}(q)$ under the standard $\sigma_i \mapsto T_i$ representation generates a sub-algebra whose GB-NF filtration shape is given by*

$$
\dim_R \bigl(F_k(T_w(Z, N))\bigr) \;=\; \binom{3A - Z}{\,k - (Z - 1)\,} \qquad (k = Z - 1, Z, \ldots, 3A - 1).
$$

*Equivalently, the sub-algebra is isomorphic (as a graded $R$-vector space, $R$ any field of characteristic 0 — typically $\mathbb{Q}$ for the GB-NF rational arithmetic, $\mathbb{R}$ for the substrate evaluation at $q_0 \in \mathbb{R}$) to the **exterior algebra** $\Lambda^*(R^{3A - Z})$, with grade shift $\delta = Z - 1$, total dimension $2^{3A - Z}$.*

## Empirical verification (PR following R5-full $^4$He registry extension)

The conjecture is verified across all 4 atoms with canonical `atom_braid_word_3A` recipes implemented in the Rust R5-SDP solver (post-`BraidLetter` extension):

| Atom | $(Z, N)$ | $n_0 = 3A$ | $3A - Z$ | $\delta = Z - 1$ | Filtration shape | Total |
|---|---|---|---|---|---|---|
| D $^2$H | (1, 1) | 6 | 5 | 0 | $\{1, 5, 10, 10, 5, 1\} = \binom{5}{k}$ | $2^5 = 32$ |
| T $^3$H | (1, 2) | 9 | 8 | 0 | $\{1, 8, 28, 56, 70, 56, 28, 8, 1\} = \binom{8}{k}$ | $2^8 = 256$ |
| $^3$He | (2, 1) | 9 | 7 | 1 | $\{1, 7, 21, 35, 35, 21, 7, 1\} = \binom{7}{k}$ | $2^7 = 128$ |
| $^4$He | (2, 2) | 12 | 10 | 1 | $\{1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1\} = \binom{10}{k}$ | $2^{10} = 1024$ |

Each row's shape is **exactly Pascal's triangle row $(3A - Z)$** with the appropriate grade shift, and totals are $2^{3A - Z}$.

## Structural interpretation

The exterior-algebra structure says: the canonical atom-braid lives in a **fermion Fock-space subalgebra** of $H_{3A}(q)$, with each "interface" between adjacent strands contributing one $\mathbb{Z}/2\mathbb{Z}$ degree of freedom. The proton-count $Z$ enters twice:

1. **Dimension reduction** ($\Lambda^*(R^{3A - Z})$ instead of $\mathbb{C}^{3A}$): each proton imposes one constraint, removing one degree of freedom.
2. **Grade shift** ($\delta = Z - 1$): each proton beyond the first shifts the filtration's lower bound by one — analogous to a chemical-potential or fermion-number offset.

This is fundamentally different from the standard Wedderburn decomposition $H_n(q) \cong \bigoplus_\lambda V_\lambda^{\oplus d_\lambda}$ (which for $H_{12}$ has dimension $12! \approx 5 \times 10^8$, **8 orders of magnitude larger** than the observed $2^{10} = 1024$ for $^4$He).

### Load-bearing factoring — PR-D Step 4

The 5-step structural argument that produces the exterior-algebra
shape factors so that *one* step carries all the genuine new
representation-theory content. Steps 1, 2, 3, and 5 are mechanical
($G_0/G_1$ pattern reductions in $H_3 \subset H_{3A}$, bar-involution
constraint counting, and `Nat.sum_range_choose`). **Step 4** —
"inter-nucleon Avg crossings $\sigma_{3k+2} - h/2$ preserve the
Boolean grading" — is the load-bearing categorical claim.

The Lean sibling file factors Step 4 into a dedicated
[`AtomBraidStep4Hypothesis (Z N : ℕ)`](conj-atom-braid-exterior-algebra.lean)
§3b-cond class with a `Prop` hypothesis field
`avg_crossing_preserves_grade`, plus a bridging theorem
`step4_implies_exterior_algebra_structure` that derives the full
`AtomBraidExteriorAlgebraStructure` instance once Step 4 is
discharged. This makes the conjectural input citable,
`lean_verify`-auditable, and individually closable as a single PR
once Sprint 3–4 IwahoriHecke infrastructure is in place to give
mechanical proofs for Steps 1–3.

## Falsified inference: LP/SDP under-determination implication

**Status:** the inference below was **FALSIFIED** by direct computation in [`atom_braid_active_partitions.py`](../../../computations/atom_braid_active_partitions.py). All `p(n_0)` partitions have non-trivial `χ_λ(T_w)` — the claimed "active set $\leq n^* + 1$" prediction does NOT hold on the Wedderburn basis. See [`docs/audits/-exterior-algebra-lp-claim-falsified.md`](../../../docs/audits/-exterior-algebra-lp-claim-falsified.md) for the full retraction.

**What's still valid:** the Pascal-row `C(n*, k)` filtration shape on the **NF basis** (permutation-indexed, ordered by Coxeter length) — the Rust solver's empirical finding from  stands.

**Why the inference failed:** I conflated two different bases of `H_{3A}(q)` — the NF basis (where the Pascal-row shape lives) and the Wedderburn basis (where LP `y_λ` variables live). These are different decompositions of the same algebra; the filtration-shape claim does NOT directly imply Wedderburn-channel reduction.

The section below is retained as a historical record of the falsified inference; the structural-filtration-shape finding above remains the substantive contribution of this conjecture.

## (Retained for record — falsified inference)

### Implications for LP/SDP under-determination

The exterior-algebra structure has a direct consequence for the operator-selection LP/SDP that consumes the canonical atom-braid as input.

**Previously (Wedderburn-channel framing):** the LP/SDP variables `y_λ` for $\lambda \vdash 3A$ have $p(3A)$ partition channels — $p(12) = 77$ for $^4$He alone. The LP feasibility region is correspondingly $\geq 77$-dimensional (before constraint cuts). Empirical observations have noted under-determination — multiple feasible solutions, ambiguous extraction.

**Under the conjecture:** the physical content lives in the sub-algebra $\Lambda^*(R^{3A - Z})$ of dimension $2^{3A - Z}$. The non-trivial Wedderburn channels (those with $y_\lambda \neq 0$ on the atom-braid's image) are a **proper subset** of the $p(3A)$ partitions — exactly those $\lambda$ corresponding to non-zero homogeneous components of $\Lambda^k(R^{3A - Z})$ under the projection $H_{3A}(q) \to \Lambda^*(R^{3A - Z})$.

For Pascal-row $\binom{3A - Z}{k}$ at each grade $k$:
- The number of non-zero $y_\lambda$ channels per grade is **at most one per binomial entry**, suggesting a much smaller active partition set than $p(3A)$.
- For $^4$He: at most $(3A - Z + 1) - \delta = 10$ active channels (one per non-zero binomial position), down from $77$ — **a ${\sim}7\times$ constraint tightening**.

**Concrete predicted reductions:**

| Atom | $p(3A)$ | Predicted max active channels | Reduction |
|---|---:|---:|---:|
| D $^2$H | $p(6) = 11$ | $\leq 6$ | $\geq 1.8\times$ |
| T $^3$H | $p(9) = 30$ | $\leq 9$ | $\geq 3.3\times$ |
| $^3$He | $p(9) = 30$ | $\leq 8$ | $\geq 3.8\times$ |
| $^4$He | $p(12) = 77$ | $\leq 11$ | **$\geq 7.0\times$** |

If the conjecture holds, the LP/SDP under-determination noted in prior probes (Δ_λ closure synthesis, joint-tower SDP feasibility) is structurally resolved: the previously-ambiguous $y_\lambda$ extraction has a **categorically-restricted active set** corresponding to the exterior-algebra graded components.

**Identifying the active partition set** (next step): for each grade $k \in [\delta, \delta + n^*]$, the contributing $\lambda \vdash 3A$ should be determinable from the Schur–Weyl decomposition of $\Lambda^k(R^{3A - Z})$ under the $H_{3A}(q)$-action. Likely candidates (per crystal-basis intuition):
- Pascal row $\binom{3A - Z}{k}$ position correlates with hook-shape partitions $(k+1, 1^{3A - k - 1})$
- More precisely: ribbon / border-strip tableaux of length $3A - Z$

This identification is the natural follow-up — would close the LP/SDP constraint-set explicitly + give a recipe for computing the categorical active set per atom.

## Crystal-basis projection (open)

The exterior algebra $\Lambda^*(V)$ arises in Kashiwara–Lusztig theory as the **fermion Fock space** (the *q*-deformed sector of the Heisenberg-Weyl algebra at $|q| < 1$). The Z-dependent grade shift looks like a **charge sector** label in this framework. Open: identify the specific crystal-basis projection $H_{3A}(q) \to \Lambda^*(\mathbb{C}^{3A - Z})$ that the canonical atom-braid factors through.

A categorical proof would likely use:
1. Schur–Weyl duality $H_n(q) \otimes \mathrm{GL}_m \curvearrowright V^{\otimes n}$ at appropriate $V$ choice
2. The specific structure of `_PROTON_G0 / _PROTON_G1 / _NEUTRON_G0 / _NEUTRON_G1` 3-strand patterns (cf. `mass_at_3A_proper.py`)
3. KLR diagrammatics to identify the fermion-sector subalgebra

## Cross-references

- [`computations/mass_at_3A_proper.py`](../../../computations/mass_at_3A_proper.py) — canonical `atom_braid_word_3A` recipe
- [`tools/hecke-engine/src/gb_nf_reducer.rs`](../../../tools/hecke-engine/src/gb_nf_reducer.rs) — `BraidLetter` + `right_mul_t_avg` (R5-full extension supporting σ_avg)
- [`tools/hecke-engine/src/bin/joint_tower_sdp.rs`](../../../tools/hecke-engine/src/bin/joint_tower_sdp.rs) — joint-tower SDP solver (registry with 4 canonical-3A test atoms + $^4$He)
- [`computations/joint-tower-sdp-rust.witness.json`](../../../computations/joint-tower-sdp-rust.witness.json) — observed filtration shapes
- [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) — canonical mass formula that consumes this structure
- [`prop:lepton-bring-surface-h3-3channel`](lepton-bring-surface-h3-3channel.md) — bring-surface analog for lepton sector
