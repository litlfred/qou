# PRE-REGISTRATION — colour in the full Hecke tower (bean `qou-ni4b`)

Date 2026-11-22. Branch `claude/qcd-heat-kernel-beta0-sign-2026-11-22`, PR #9059.
This file is committed and pushed **before** the probe is written. It is not edited
afterwards; results go to `RESULT.md`.

Owner question (verbatim): *"What about looking in the full Tower for the color"*.
Owner ruling 2026-09-03: derivations use the full tower, meaning all `n` of `H_n(q)` and all
orders in `q`. Here "all orders in `q`" means exact arithmetic over ℚ(q); "all n" means
statements proved for general `n`, or checked exactly for `n ≤ 9` where only finite checks exist.

## 0. Prior art (corpus-grep, 2026-11-22)

`corpus_search` (CLI) on "colour tower Schur-Weyl three-row", "colour Schur-Weyl",
"relative commutant", "SU(3) colour" and "three-row" (`--limit 200`) returned **0 seeds**.
"basic construction" returned only `library/0310279v5` (Birman–Menasco, braid
stabilization; not about colour). The authored KG gave no hit, so step 0 was uninformative
and the grep paths carry the search.

Grep paths 1–3 and 6 (`docs/audits`, `folio`, `computations`, `beans/defs`) found these:

| item | what it settles |
|---|---|
| `qou-8iru` (todo) | Convention D is Temperley–Lieb. `y_λ = 0` for every λ with ≥ 3 rows, and `dim H_n/rad = Catalan(n)`. The radical of the D trace is the TL ideal. |
| `qou-ezhi` (completed) | Level family `z_r = q^r/[r]_q`, with D as `r = 2`. At `r = 2` the weight `y_(1,1,1)` is exactly 0 ("no colour singlet"). The one-gluon ratio `|C(3̄)/C(6)|` comes out 1, where QCD gives 2. |
| `qou-lxh5` / `2026-10-10-level3-su3-channel-test.md` | The level-3 trace `z_3 = q^5/(q^4+q^2+1)` substituted into the proton identity is about 1100× worse than level 2. Scope (a). |
| `2026-06-16-keystone-arena-is-full-hecke-not-su3.md` | No finite `ℂ^N` carries the full Hecke principal-specialisation trace. The SU_q(3) trace is a different functional. |
| `ColourHeckeRegularHost.lean` | Hecke centraliser on the regular `H_3`: `dim ≤ 6 < 8`. |
| `ThreeStrandColourTowerCP.lean` (PR #8139) | `H_3(q)` is too small for su(3). |
| `ColourBridge.q_eq_one_of_e01_mem`, `primitive_commute_rCheckN_iff` | A classical gl₃ field commuting with the Jimbo Ř forces `q = 1`. |
| `qcd_colour_action/RESULT.md` (this branch) | K0–K4. Transport plus Hecke in K4 forces `q² = 1`. |

What is **not** in the corpus, and is therefore what this probe adds:

- whether convention D can be written as a *colour-twisted* quantum trace on the
  `U_q(gl₃)` module `(ℂ³)^⊗n`, and what that does to the colour symmetry;
- where the colour-singlet sectors of the whole tower `n = 3A` sit relative to D's radical;
- the relative commutants `H_{n-k}' ∩ H_n` of the tower, for full Hecke and for D/TL;
- a ℤ₃ structure: the period-3 element `V = σ₀σ₁⁻¹`, and automorphisms of the branching graph.

## 1. Candidates

**T1 — Schur–Weyl dual of the full `H_n(q)` on `(ℂ³)^⊗n` (Jimbo).**
- The commutant is the image of `U_q(gl₃)`. It is compatible with `H_n ⊂ H_{n+1}` through the
  iterated coproduct.
- Sub-test T1-twist: find every diagonal twist `K = diag(k₁,k₂,k₃)` that makes
  `x ↦ tr_{(ℂ³)^⊗n}(K^{⊗n} x)` a Markov trace on the tower. The condition is that the partial
  trace `tr₂((1⊗K)Ř)` is a scalar multiple of `Id_V`. Record the `z` of each solution.
- Then ask which solution (if any) gives `z_D`, and what part of gl₃ its twist preserves.

**T2 — relative commutants / basic construction.**
- Compute the block sizes of `H_{n-k}' ∩ H_n` from the branching graph. Each block size is the
  number of skew standard tableaux of `λ/μ`, `|λ/μ| = k`.
- Do this for the full Hecke tower (Young's lattice) and for the D tower (≤ 2 rows), with
  `k ≤ 3` and `n ≤ 9`. Report whether an `M₃` block (hence an `sl₃` derived algebra) appears,
  and at which `(n, k)`.
- Then test acceptance (b) on it: does the block commute with the full braiding of `H_n`?

**T3 — period-3 structure at `n = 3A`.**
- (i) Eigenvalues of `V = σ₀σ₁⁻¹` on each irrep of `H_3(q)`, exact. Ask for which `q` the
  operator `V³` is a scalar on every block, i.e. when ℤ₃ acts.
- (ii) Automorphism group of the graded branching graph truncated at level `n ≤ 9`, by brute
  force, for Young's lattice and for its two-row (D) part. Ask whether it contains a ℤ₃.
- (iii) D weights `y_λ` along `n = 3A`, `A = 1, 2, 3`. Look for any period-3 pattern.

**T4 — does D keep three-row data in a non-trace part?**
- The colour-singlet subspace of `(ℂ³)^⊗3A` under `U_q(sl₃)` is the isotypic block of the
  rectangular shape `λ = (A, A, A)`.
- Locate it relative to the radical of D's trace form on `H_{3A}`: the dimension of the radical,
  and whether the singlet block is inside it.

## 2. Acceptance tests (the sibling's (a)–(f), applied where they make sense)

(a) injective colour action (`sl₃` or `U_q(sl₃)`, dimension 8);
(b) it commutes with the braiding (all `σ_i` of the tower);
(c) Hecke + braid relations hold;
(d) the colour-singlet sector reproduces convention D (the D trace is the singlet / colour-invariant reading);
(e) the singlet is unique;
(f) colour moves with the strand.

## 3. Predictions, written before computing

- **T1:** (a)(b)(c)(f) pass for Jimbo `U_q(gl₃)` (already known as K1).
  - Markov twists: a full-rank `q`-power solution gives `z_3`. I *expect*, but am not sure, that
    degenerate rank-2 and rank-1 twists give `z_2 = z_D` and `z_1`.
  - If the rank-2 twist gives `z_D`, its kernel is a colour direction, so the twist cannot be
    `sl₃`-invariant. Then (d) fails. The functional is invariant under gl₂ ⊕ gl₁ at most.
- **T2:** depth 2 gives blocks of size ≤ 2, so no `M₃`.
  - Depth 3, full Hecke: blocks of size 1, 2, 3 and 6.
  - Depth 3, D tower: blocks of size ≤ 3, with `M₃` from a box + domino.
  - (b) fails structurally: an element of `H_n` commuting with every `σ_i` is central, and
    `Z(H_n)` is commutative, so it hosts no non-abelian colour. Scope (b), invariant:
    commutativity of the centre.
- **T3:**
  - (i) On `(2,1)`, `tr V = −1 − h²` and `det V = 1`, `h = q − q⁻¹`. `V³` is scalar there only
    for `h² ∈ {0, −2}`. Not at real `q > 1`.
  - (ii) Young's lattice has automorphisms {id, transpose} only, and the two-row part only id.
    No ℤ₃.
  - (iii) No period 3, because `y_(n-k,k) = [n-2k+1]_q/[2]_q^n`.
- **T4:** the radical has dimension `n! − Catalan(n)`. Every colour singlet `(A,A,A)`, `A ≥ 1`,
  is inside it, so D gives weight 0 to every colour singlet of the whole tower. Scope (b),
  invariant: `ocneanuWeight_conventionD_eq_zero_of_three_rows`.

## 4. Coincidences declared in advance (do not count)

- At `N = 3`, `2/N = 1 − 1/N = 2/3`.
- Any `3` that comes from "three strands", any `[3]_q` that comes from `n = 3`, and any `M₃`
  block: every 3-dimensional matrix block has `sl₃` as its derived Lie algebra. That is
  generic and is not colour unless (b) also holds.
- `f^{(2,1)} = 2` and `Catalan(3) = 5`.
- `8 = 3² − 1` from any `M₃`.

## 5. Discipline

- Exact sympy / `Fraction` only. No float. `q₀` is not used: every result is over ℚ(q).
- Nothing is selected against a target. The gluon is not identified.
- Negatives are scope (a) unless a proved invariant is cited.
