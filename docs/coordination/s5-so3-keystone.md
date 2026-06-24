# Coordination ledger — `conj:s5-so3-fiber-action` (the s5-so3 fibre-action keystone)

**Goal.** Discharge the keystone the QOU framework's open derivation math reduces to: the geometric
fibre map `S₅ ⊃ A₅ ≅ I ⊂ SO(3)` tying the partition-wise Wedderburn action on `H₅(q)` (combinatorial)
to icosahedral rotations on Bring's quintic surface (geometric). It is the single open object for
m_τ (lepton tower), GAP-A-3 binding Δ_λ, and GAP-A-4 mass λ(K).

**Status (2026-06-16).** Reduced — by formalize-first pruning — to **one differential-geometry
problem**. Everything combinatorial / representation-theoretic / algebraic is done or refuted; no fit
was introduced anywhere.

**Status (2026-06-22).** The single open object is **not** differential geometry — it is the
colored Σ(2,3,5) WRT / `E_q(2)` q-Bessel q-series whose `q₀`-evaluation must reproduce `W_λ`
(the Markov-trace surface is now exhausted — projector-weight shift refuted, [#2584](https://github.com/litlfred/qou/pull/2584)).
See the 2026-06-22 update banner below.

> **⚠ Corrections (2026-06-16, late session) — the "OPEN" row + the colour-arena framing are superseded.**
> Three findings (mine + sibling) refine the open object below; read them over the "Current state" table:
> - **No finite colour-SU(3) arena** (#2406, reconciling sibling #2389). The "colour ℂ³ ✅ forced" row is a
>   *lower* bound only (spinor ℂ² can't host the electron). The full production trace needs **>3-row** blocks
>   too (SU_q(3)/colour-ℂ³ misses 3.4% @⁴He) — it is the **full Hecke / Wenzl principal specialization**
>   `s_λ(1,q,q²,…)`, *not* a finite ℂ^N. So there is **no finite colour-SU(3) Sasakian arena**.
> - **SU(3)/SO(3) (Wu-manifold) arena ruled out** (#2398): the spacetime SO(3) is the *isotropy* and has no
>   continuous centralizer in SU(3) (Schur) — no spacetime-fixing Reeb exists there. ⇒ **spacetime ⊥ colour**
>   (= corpus `S5 = S2×S3`), confirmed.
> - **`W_λ` is the q-Plancherel measure, NOT the production trace weight** (sibling `e269ca12ea`); the production
>   weight is the Wenzl principal specialization. So the "OPEN: W_λ via SU(3)/SO(3) Sasakian" row's *both* the
>   arena and the weight are corrected.
>
> **Corrected open object:** does the **full-Hecke principal-specialization trace** (infinite-variable,
> intrinsically `p(3A)`-dimensional) admit *any* geometric realization whose index reproduces the canonical
> Markov weights? A finite-dimensional Sasakian is ruled out. The Δ_λ magnitude×chirality decomposition and the
> PROBE-4 prune (abstract `H_n(q)`) are unaffected. Audits: `2026-06-16-{keystone-arena-is-full-hecke-not-su3,
> keystone-wu-manifold-reeb-obstruction}.md`; sibling `2026-06-16-s5-s3-symmetry-review-and-suq3-trace-question.md`.

> **⚠ Update (2026-06-22) — the arena is the non-compact `E_q(2)` contraction, NOT a compact Sasakian; the Markov-trace surface is exhausted.** Four 2026-06-22 sessions (bean `s5bb`, all merged) supersede the "Wu-manifold Sasakian / differential-geometry" framing above:
> - **q-deformed projector-weight shift REFUTED as the 210 ppb mechanism** ([#2584](https://github.com/litlfred/qou/pull/2584), merged). The E_λ-projected H₅ Markov trace gives `δ = T_μ − T_e = 0.2075` — non-null, so the q-deformed home-block weighting *does* break the (2,1) symmetry classical multiplicity preserved — but it is 6–7 orders too large for the 209.8 ppb gap and **bar-mixed** (fails the bar-even precondition). The Markov-trace surface (multiplicity / home-block weight / projected trace) is now **exhausted**; any surviving q-closure must leave the trace-weighting entirely. ([`2026-06-22-keystone-qdeform-projector-shift.md`](../audits/2026-06-22-keystone-qdeform-projector-shift.md))
> - **No compact Sasakian / compact MTC can host `W_λ`** at the substrate anchor: `q₀ ≈ 1.10998` is real `> 1` (growth regime, `[m]_q = sinh(mη)/sinh(η)`, `η = log q₀` real), not a root of unity. The `W_λ`-producing structure is the non-compact `SU_q(2) → E_q(2)` contraction whose matrix coefficients are **Hahn–Exton q-Bessel** functions (already named in the corpus, `2026-06-13-reeb-phase-qbessel-identification.md`). ([`2026-06-22-keystone-modular-category-identification.md`](../audits/2026-06-22-keystone-modular-category-identification.md))
> - **Sharpened open object:** pin the **colored Σ(2,3,5) WRT / Habiro-ring q-series** whose evaluation at `q₀` reproduces the `W_λ` family — reached from the convergent WRT series via the `q ↦ q⁻¹` bar involution (`q₀ ↔ 1/q₀ ≈ 0.901`, inside the disk). The bare `Σ(2,3,5)` Lawrence–Zagier false-theta `Ψ(1/q₀) = 2.32958` is operational but is **one** number vs a **λ-family** (type mismatch — *not* claimed equal to `W_λ`; the numerology trap the discipline forbids). ([`2026-06-22-keystone-habiro-wrt-s3-2i.md`](../audits/2026-06-22-keystone-habiro-wrt-s3-2i.md), [`2026-06-22-keystone-geometric-level-route-reduction.md`](../audits/2026-06-22-keystone-geometric-level-route-reduction.md))
> - **Falsifiable, `q₀`-free sub-target:** any index realizing `W_λ` must reproduce the heat-kernel defect coefficient `144·C(n) = −n(n−1)(2n−13)` exactly (the `n = 7` sign change). The algebra is Lean-proved sorry-free ([`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean), `n144C_closed_form` / `n144C_pos` / `n144C_neg`); the **one** carried representation-theoretic input is **Identity I** `M(n) = (1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c} h_c² = n(3n−1)/2`, held as a `def twoM` (compute-verified `n = 2..14`). Proving Identity I from the partition squared-hook sum needs SYT-dimension / hook-length infrastructure **not currently in Mathlib** — a multi-session infra fill, not a single-session lemma. ([`2026-06-20-keystone-wlambda-C-n-closed-form.md`](../audits/2026-06-20-keystone-wlambda-C-n-closed-form.md))
>
> **Active open work (unmerged — this ledger reports merged facts; the live geometric frontier is these PRs, consistent with the E_q(2)/colored-WRT reframing above since WRT(S³/2I) = colored Σ(2,3,5) WRT is the same object):** [#2524](https://github.com/litlfred/qou/pull/2524) supplies a candidate **index mechanism** — `W_λ` as the MTC Plancherel measure `d_q²/D²` from **Beasley–Witten non-abelian Chern–Simons localization** on the Seifert 3-manifold `S³/2I` (Reeb = Seifert `S¹`) — and proposes the C1 normalization answer `d_q²/D²` (Σ = 1). [#2503](https://github.com/litlfred/qou/pull/2503) is the formalize-first DG attack plan (a *finite-dimensional* Sasakian is ruled out ⇒ the construction is infinite-dimensional WRT(S³/2I) = Lawrence–Zagier). [#2603](https://github.com/litlfred/qou/pull/2603)/[#2608](https://github.com/litlfred/qou/pull/2608) work the λ-coloured WRT colour-resolution + Schur–Weyl.
>
> **Owner-decisions to confirm (some now addressed by the open PRs):** (1) `W_λ` normalization — `d_q²/[n]_q!` (Σ ≈ 0.982) vs `d_q²/D²` (Σ = 1); **#2524 proposes `d_q²/D²`**. (2) **Gate status — CONFIRMED REVERSED (2026-06-22, owner).** The owner reversed the subgoal-2 geometric-derivation gate (2026-06-19; #2503/#2524) **for the keystone geometric `W_λ` DG construction** — now recorded in [`AGENTS.md §Precision-goals`](../../AGENTS.md) + [`docs/precision-goals.md`](../precision-goals.md). The reversal is **narrow**: it does not reopen fit-based q_0 derivation, and the Δ_λ "no seventh fit-based ansatz" rule stands. (3) Identity-I Mathlib infra fill scope. Outside-view (critical-distance): a Beasley–Witten/RT *reduction* gives `W_λ` a categorical *name*, not a new mass prediction — watch the tautology risk that the "geometric origin" is the harmonic analysis of the same `SU_q(2)` the framework already postulates.

## Current state

| Layer | Status |
|---|---|
| Combinatorial backbone `Res^{S₅}_{S₃}` + `SO(3)↓A₅↪S₅` bridge | ✅ verified |
| Geometry: 2I spin lift; geometric A₅ forced to icosahedral T₁; chirality = T₁/T₂ | ✅ verified |
| Algebraic functor target (Bratteli = box removal; Ocneanu trace) | ✅ forced |
| Strand fibre = colour ℂ³ (Schur–Weyl: spinor ℂ² kills the electron (3,1,1)) | ✅ forced |
| Static coupling `V_ℓ→E_λ` (Schur: dim Hom = 1) | ✅ forced |
| **Generation selection ℓ→λ = the Hopf moment map μ** (spatial SO(3)-equivariance) | ✅ **realized** |
| 210 ppb muon mechanism (Wedderburn-projector correction) | ❌ refuted (6–8 orders too coarse) |
| colour⊗spin = (3,1,1) dim-6 shortcut | ❌ refuted (spin-parity mismatch) |
| Reeb-eigenvalue resonance | ❌ refuted (no parameter-free ≥3-anchor match) |
| q-deformed projector-weight as the 210 ppb mechanism | ❌ refuted (#2584: `δ=0.2075` non-null but 6–7 orders too large, bar-mixed) |
| **OPEN:** `W_λ` geometric origin — colored Σ(2,3,5) WRT / `E_q(2)` q-Bessel q-series (**NOT** a compact Sasakian; see the 2026-06-22 banner) | ⛔ q-series (owner-gated) |

**The single open object.** Does the SU(3)/SO(3) (Wu-manifold) Sasakian with spatial-SO(3)_colour Reeb
admit a structure whose S¹-equivariant index reproduces the Ocneanu weights `W_λ = d_q(λ)²/[n]_q!`?
(dim 5 odd ✓; χ(Wu)=0 ✓ — Boothby–Wang necessary conditions met, not obstructed at that level.) The
sibling A≥3 operator-branching compute (#2369/#2371/#2372) produces `W_λ` algebraically; the open piece
is its *geometric origin*.

> **Superseded (2026-06-22).** This paragraph's Wu-manifold/Sasakian framing is retained for history but
> **superseded** — at the substrate anchor `q₀ ≈ 1.10998` (real `> 1`, growth regime) **no** compact Sasakian /
> MTC hosts `W_λ`; the arena is the non-compact `SU_q(2) → E_q(2)` Hahn–Exton q-Bessel contraction and the
> sharpened object is the colored Σ(2,3,5) WRT q-series. See the 2026-06-22 update banner above.

## Refutations not to re-walk (canonical-no-negative-result discipline)

1. **210 ppb muon via (1,1,1) sign-block / Wedderburn projector** — the correction is O(16 %) (sign-block)
   to ×15 (channel ratio), 6–8 orders too large for the 209.8 ppb gap; the bare `m_e·Vol(4₁)/ℏ_q²` is
   already good to 209.8 ppb. The structural identity `χ^{(1,1,1)}(β_Bor)=1` is exact but magnitude-wrong.
2. **electron block (3,1,1) = colour ℂ³ ⊗ spin ℂ²** — refuted on the central character (spin parity): (3,1,1)
   is an A₅ rep (central +1), ℂ³⊗ℂ² has central −1. dim-6 = chirality T₁⊕T₂, not a tensor.
3. **Reeb-eigenvalue resonance** — the ℓ=1,2 content matches (`c(λ)=ℓ(ℓ−1)`) are non-unique and fail at ℓ=3
   (tau, multi-block). No parameter-free ≥3-anchor resonance.
4. **Cyclotomic-Galois / `Li₃(ζ₅)` period as a keystone "falsifier"** — recorded 2026-06-20 after a fresh
   agent (`claude/kind-ptolemy-acladr`) independently re-derived the cyclotomic-Galois / fifth-root-of-unity
   period angle and mis-aimed it at the keystone coupling as a falsifier. That angle lives on the **period /
   z-Habiro axis**, which the 2026-06-17 sessions-log note flags as **orthogonal to the keystone coupling — "do
   not conflate"**: the z-side completion `varprojlim ℤ[q^±1][z]/(P_n)` (quantum-dilog Φ_q tower) is parallel-
   but-independent of the q-side Habiro/full-Hecke Markov trace. Forcing the period↔knot bridge is exactly the
   **unfalsifiable correspondence-chain the Habiro lead refused**
   ([`2026-06-16-keystone-habiro-coupling-lead-and-ck-exposition.md`](../audits/2026-06-16-keystone-habiro-coupling-lead-and-ck-exposition.md)).
   Inoculation for the next agent: a period-axis cyclotomic-Galois result is **not** an s5-so3 keystone
   constraint; the keystone's single open object is the q-Plancherel-measure geometric-realization problem
   (below), not a period identity. Verify the axis (period/z vs coupling/q) before treating any Galois fact as
   keystone-bearing.
   **Twice-demonstrated recurrence (strengthened 2026-06-20, PR #2506 / bean `wlk9`).** A *second*, independent
   agent (`claude/tender-darwin-sw4zo1`, the #2506 hyperbolic-hurdle audit) re-derived the identical
   cyclotomic-Galois / `Li₃(ζ₅)` angle from scratch and again mis-aimed it at the keystone as a falsifier — with
   no knowledge of the #2517 record (it was 475 commits stale). Two agents re-walking the same dead end within
   one day is exactly the recurrence the canonical-no-negative-result discipline exists to stop; treat this item
   as high-priority inoculation, not a one-off footnote.

## Sessions log

| Date | PR | What landed |
|---|---|---|
| 2026-06-16 | #2352 | S₅↓S₃ backbone + SO(3)↓A₅↪S₅ bridge verified; ing-4/5 close-out (210 ppb **refuted**) |
| 2026-06-16 | #2361 | propagate refutation to the GAP-A-4 doc; ingredient-4 geometric-leg formalize-first prune |
| 2026-06-16 | #2364 | Schur–Weyl: strand fibre forced to colour ℂ³ (spinor kills electron) |
| 2026-06-16 | #2367 | two-Sasakian decomposition; static coupling Schur-forced |
| 2026-06-16 | #2368 | Reeb-eigenvalue resonance **refuted** (numerology-guarded negative) |
| 2026-06-16 | #2370 | canonical coupling = Hopf moment map μ; round-S⁵ colour Reeb transverse; **selection realized by μ** |
| 2026-06-16 | #2373 | Markov-weighting scope: forced `W_λ` + Wu-manifold Sasakian handoff |
| 2026-06-16 | #2369 (sibling) | coordination note: A≥3 `tr_M` compute = algebraic realization of the open weighting |
| 2026-06-16 | #2398 | **derive-attempt:** SU(3)/SO(3) Wu-manifold arena ruled out — spacetime-fixed Schur-centralizer obstruction ⇒ spacetime ⊥ colour |
| 2026-06-16 | #2406 | **correction:** no finite colour-SU(3) arena — production trace is full-Hecke principal specialization, not SU_q(3) ≤3-row (reconciles sibling #2389) |
| 2026-06-17 | #2416 | **Lean:** Δ_λ = chirality sign × Wedderburn magnitude (sorry-free); `deltaSign_mixed` = the PROBE-4 KL-positivity-prune premise machine-checked |
| 2026-06-17 | #2424 | **Lean:** McKay 2I↔E₈ anchors (Σdim²=120, Σmarks=h=30, \|2I\|=4h, dimE₈=8·31) + A₅ branching content (V₁→T₁, V₂→H, V₃→T₂⊕G; (3,1,1) self-conj T₁⊕T₂) |
| 2026-06-17 | #2431 | **Lean:** S₅↓S₃ restriction dimension-consistency for all 7 blocks (the branching backbone, embedding-independent) |
| 2026-06-17 | #2436 | **Lean:** S₃-rotation branching dimension-consistency (ℓ≤4) — completes the dim-check for the `s3RotBranchingMult` table |
| 2026-06-17 | #2442 | **Lean (full Mathlib):** z-Habiro `c_n` localisation pinned — `eulerCoeff` (Euler `b_n` in `S^{-1}ℤ[q^±1]`, `S=⟨1-q^{-j}⟩`) + `braneMonic_coords_unique` (coordinates unique); analytic↔algebraic identification stays open |
| 2026-06-17 | (this PR) | **Lean (full Mathlib):** z-Habiro `braneMonic_coords_exist` — monic basis spans `R[X]_{≤n}`; with #2442's uniqueness, cyclotomic coordinates are a bijection `R[X]_{≤n} ≅ R^{n+1}` staying in the localised `R` (item 2(i) base-ring half) |
| 2026-06-17 | (coord note) | **z-Habiro on main is ORTHOGONAL to the keystone coupling — do not conflate.** The z-Habiro Lean work (#2417-era: `ZHabiroCompletion`, `zHabiroLimit`, `cyclotomicPartialSum_isCauchy`) builds the **z-side** completion `varprojlim ℤ[q^±1][z]/(P_n)` for the quantum-dilog Φ_q truncation tower. The keystone coupling is the **q-side** Habiro element (full-Hecke Markov trace = WRT(S³/2I) = Lawrence–Zagier). These are parallel-but-independent completions; bridging them needs a simultaneous (q,z)-bicompletion, which the z-Habiro file itself flags "construction open." No fit-free Lean bridge exists yet — forcing one is the unfalsifiable correspondence-chain the Habiro lead (`2026-06-16-keystone-habiro-coupling-lead-and-ck-exposition.md`) explicitly refused. The keystone coupling stays OPEN. |
| 2026-06-20 | #2520 | **Scope (consumer side, no fit):** what the mass-ratio needs from the W_λ frontier. Since #2516/#2519 prove the knot layer is null on the generation difference, the geometric frontier carries the **entire O(1) generation skeleton** (consumer weight `y_(3,2)/y_(3,1,1)=3.68` at q₀) and **none** of the 210 ppb fine shift (2.1e-7, anchor artifact). Forward necessary condition complementing producer-side C1–C7; no edit to producer docs. |
| 2026-06-20 | #2519 | **Probe (no fit):** the (2,1)/h⁴ cancellation is **robust to q-deformation**. Generic-q Hecke branching H₃⊂H₅ carries classical multiplicities → `χ_μ^H5(β)=Σ m·χ` exactly (max |Δ|=8.9e-16) and `χ_(3,1,1)−χ_(3,2)=χ_(1,1,1)=1` identically, h-indep up to h⁴≈0.9. Closes the q-deformed-Wenzl escape #2516 left at the **character** level — only surviving μ/e asymmetry is the O(1) `W`/`y` block-weight ratio (#2488 frontier). |
| 2026-06-20 | #2516 | **Probe (no fit):** ran the functor-resolution §4 object via `pyhecke_native` (built in-sandbox, #2511) — the H₃ Borromean Markov-trace shift between muon `E_(3,2)` and electron `E_(3,1,1)` projectors via the classical `S₅→S₃` branchings. The h⁴-bearing `(2,1)` block enters both with the **same** multiplicity 2 (classical, q-indep) → **cancels exactly** in the μ/e difference (6.9e-18). Classical-multiplicity baseline is **null**; residual split is the `(1,1,1)` sign channel (h-indep, ~1.5e-2). Sharpens the W_λ frontier (#2488): the q-deformed `W_λ = d_q(λ)²/[n]_q!` weights are **necessary**, not optional — pure multiplicity counting cannot produce a generation shift. |
| 2026-06-20 | #2517 | **Lead + inoculation:** (a) §Refutations item 4 — cyclotomic-Galois / `Li₃(ζ₅)` period is period-axis, NOT a keystone falsifier; (b) **q-heat-kernel / q-Bessel(2nd-kind) geometric-realization lead** — precheck found `W_λ=d_q²/[n]!` is **sub-normalized** (`Z=0.98222` at q_0, P1 fail; symmetry P2 + audit P3 pass); the mass defect `1−Z` is the geometric quantity to explain. Bridges the existing q-Bessel infra (2026-06-13) to the keystone target. `2026-06-20-keystone-qbessel-heat-kernel-lead.md` + `scripts/keystone_qbessel_plancherel_precheck.py`. NOT a closure. |
| 2026-06-20 | #2506 | **Inoculation + corpus trace:** (a) §Refutations item 4 strengthened — the cyclotomic-Galois falsifier was re-walked a **second** time independently (`claude/tender-darwin`, #2506), now a twice-demonstrated recurrence; (b) pieces-1–3 corpus-object trace consolidated into [`docs/audits/2026-06-20-s5so3-pieces-1-3-corpus-trace.md`](../audits/2026-06-20-s5so3-pieces-1-3-corpus-trace.md) — every settled ingredient mapped to its verified `.md`/`.lean`/checker source. No new math; reporting only. |
| 2026-06-20 | #2528 | **Probe (no fit) — binding-side target for the Step-1 gate:** wired the owner-gated deuteron `f_pn = 0.588` (reproduces AME `B(²H)` exactly) against the gate's `W_λ = d_q²/[n]_q!`. The pn std-channel block is the standard rep `λ=(2,1)` at `n=3`; gate `W_(2,1)=0.661` UNDER-binds (E 1.74), the bare std channel `0.395` OVER-binds (E 3.89) → required `0.58776` (E 2.2246) is **strictly bracketed** `0.395 < 0.588 < 0.661`. REFUTE the naive direct-weight map; algebraic `W_λ` does not land 0.588 but brackets it. Hands the geometric `W_λ` (WRT(S³/2I)) a sharp **second** binding-side target alongside the m_τ tower: any index reproducing `W_λ` must land `f_pn` in `(0.395, 0.661)`. Harness `deuteron_fpn_from_Wmap` consumes any future geometric `W_λ` unchanged. `2026-06-20-deuteron-fpn-wlambda-wiring.md`. |
| 2026-06-18 | #2480 | **Lean (formalization fix):** de-vacuify `BringFiberAction` — remove the provably-false `respects_conjugate` (angle sign-flip) + vacuous `hits_five_conjugacy_classes : True` + trivial instance; correct the fibre-map domain to the 5 A₅ irreps (new `A5Irrep` + `conjugate_same_a5_irrep`), substantive `five_distinct_classes`. Per `2026-06-13-bring-fiber-action-falsification.md`. Formalization correction, **not** a closure — the geometric map stays open. |
| 2026-06-22 | #2605 (re-land #2500) | **colour-arena block-count THEOREM** (`ColourArenaBlockCount.lean`, sorry-free): the colour-`ℂ^N`-missed Wedderburn blocks contain an injected copy of *every* partition of size `n−(N+1)` (`appendUnitRows`/`missedEmbedding`) ⇒ missed-block count **unbounded + monotone** in `A` (verifier `colour_arena_missed_block_count.py`, B1–B5). Upgrades #2406's *weighted* 3.4%→6.0% from data points to a **block-count theorem**; gives **C6 (full support)** quantitative teeth (no finite-`N` Sasakian). Weighted-share monotonicity stays **empirical** (q₀/braid-dependent). Audit `2026-06-19-colour-arena-block-count-theorem.md`. |
| 2026-06-22 | #2605 (re-land #2500) | **combiner branching completeness / non-degeneracy** (`CombinerBranchingCompleteness.lean`, sorry-free): `exists_subpartition_of_size` — every `λ⊢n` (`n≥k`) has a sub-partition of size `n−k`, so `interface_blocks` returns ≥1 child for every block and the operator combiner drops none (Frobenius reciprocity; verifier `combiner_branching_completeness.py` over splits 6/9/12, self-contained). Formalizes the **dual** non-degeneracy of the already-corpus-established per-λ completeness — a correctness guarantee, not a new derivation. Audit `2026-06-19-combiner-branching-completeness.md`. |
| 2026-06-22 | #2605 (re-land #2500) | **C2 chirality involution formalized** (`KeystoneChiralityInvolution.lean`, sorry-free): facets of C2 (`W_λ=W_{λ'}`) — content negates under transpose `c(j,i)=−c(i,j)`, electron `(3,1,1)` self-conjugate (`c=0`, central A₅ rep `T₁⊕T₂`), `[2]↔[1,1]` flip. The strongest pruning lever now machine-checked at the cell/example level; global `W_λ=W_{λ'}` stays cited + witnessed. |
| 2026-06-22 | #2584 | **Probe (no fit) — q-deformed projector shift REFUTED:** E_λ-projected H₅ Markov trace `T_g = y_{λ_g}^{H5}·χ^{λ_g}(ι(β_Bor))` gives non-null `δ = T_μ − T_e = 0.2075` (the q-deformed home-block weighting breaks the (2,1) symmetry classical multiplicity preserved) but 6–7 orders too large + **bar-mixed** → not the 210 ppb mechanism. Markov-trace surface (multiplicity / home-block weight / projected trace) **exhausted**; branching cross-check to 9.6e-50. |
| 2026-06-22 | (audits) | **Reframe + route reduction (no fit):** at real `q₀ > 1` no compact Sasakian / MTC hosts `W_λ` → arena = non-compact `SU_q(2) → E_q(2)` Hahn–Exton q-Bessel contraction; sharpened object = colored Σ(2,3,5) WRT q-series via the `q ↦ q⁻¹` bar involution. `Ψ(1/q₀) = 2.32958` operational (one number, **not** the λ-family — no numerology match). On-main (level,chirality) Lean gives class *separation*, not a mass functional. Falsifiable `q₀`-free sub-target `144·C(n) = −n(n−1)(2n−13)` Lean-proved (`WLambdaDefectClosedForm.lean`); the one carried input **Identity I** `M(n) = n(3n−1)/2` needs SYT/hook-length infra not in Mathlib. Docs: `2026-06-22-keystone-{modular-category-identification,habiro-wrt-s3-2i,geometric-level-route-reduction,geometric-angles-preflight}.md`. |
| 2026-06-22 | `fe3a83d6b4` (capstone) | **Schur–Weyl dual-sides — deflationary capstone (no fit):** WRT↔`W_λ` is a Schur–Weyl **DUALITY**, **not** an equality. Corpus `W_λ` = Hecke (S_n-side) hook-content `d_q(λ)`; WRT/Poincaré modular data = SU(2) (V_λ-side) `[2j+1]_q`. They DIFFER (muon (3,2): `[5]_q=5.22` vs `[2]_q=2.01`; coincide only at (4,1)) ⇒ paired, **not** equal. A direct `WRT=W_λ` equality is a category error; the Poincaré sphere is the icosahedral *selector*, `W_λ` the dual S_n-side q-dims. Deflationary terminus of the WRT line — structural gains, **no closure / no mass prediction**; reinforces the banner's tautology-risk read. Doc: `2026-06-22-keystone-schurweyl-dual-sides.md`. |
| 2026-06-23 | [#2634](https://github.com/litlfred/qou/pull/2634) | **Identity I content decomposition (no fit) — sharpens the line-133 "needs SYT/hook-length infra" note.** The one carried RT input `M(n)=n(3n−1)/2` (to the falsifiable defect `144·C(n)=−n(n−1)(2n−13)`) factors as `binom(n,2)+n²` via **(A)** per-partition `Σ_c h_c²=Σ_c c(c)²+n²` (a single-Young-diagram fact, no dims; exhaustively verified — all 4507 partitions, `n≤22`) + **(B)** the Jucys–Murphy / Plancherel content-square mean `binom(n,2)` (**proved**: `Σ_k X_k²` central, identity-coeff `Σ(k−1)`). Net: the hard **Frame–Robinson–Thrall hook-length FORMULA is OFF the critical path** — residual fill is (A) `YoungDiagram` defs + a combinatorial identity, (B) standard `ℂ[S_n]` Wedderburn/JM (the SYT-*dimension* part of line 133 stands; the *formula* does not). Lean `twoM_content_decomposition` sorry-free (lean-direct exit 0). Docs: `2026-06-23-keystone-identity-I-content-decomposition.md`. |
| 2026-06-24 | [#2655](https://github.com/litlfred/qou/pull/2655) | **Identity-(A) PROVED sorry-free for ALL partitions (closes the (A) half of the line-135 residual fill).** Per-partition `Σ_c h_c² = Σ_c c(c)² + n²` is now Lean-proved for every weakly-decreasing partition (was exhaustive-only `n≤22`) — **merged to main**, superseding the prior `fd724f18` length-≤1 partial. Self-contained `List ℕ` model (no Mathlib `YoungDiagram`): hook-square expansion `H²=P²+Q²+1+2PQ−2P−2Q` → nine cell sums → row forms via reflection / the Fubini cell-transpose / K-moment + λ- and j-weighted min-sums; the `+n²` is the λ-weighted min-sum residue. **Residual for the full carried `twoM` (Identity I) is now ONLY (B)** — the Plancherel content-square mean `binom(n,2)` + `Σ_λ dim(λ)²=n!` (the SYT-*dimension* / `ℂ[S_n]`-Wedderburn infra of line 133 still stands; the (A) combinatorial half is DONE). **Wiring caveat:** (A) is per-partition; `WLambdaDefectClosedForm.twoM` is the *Plancherel-weighted* `M(n)`, so connecting (A) to `twoM` still needs the (B)/`Σdim²=n!` infra — (A) firms the per-partition step, not the weighted mean. `IdentityIContentDecomposition.lean` sorry-free (lean-direct exit 0). **Dedup:** sibling #2689 is a *full* alternative (A) proof (`cellSum_swap`+`abel_tri`, six reduction lemmas) with **no** keystone-consumer delta (3 files = bean + Identity proof + audit doc) → fully superseded by #2655, advised to close; #2700 (`YoungDiagram` scaffold, still sorry'd) closed as superseded. Docs: `2026-06-23-keystone-identity-I-content-decomposition.md`. |
| 2026-06-24 | [#2709](https://github.com/litlfred/qou/pull/2709) | **(B) Plancherel mean made conditional-rigorous (§3b-cond, merged).** `IdentityIPlancherelConditional.lean`: `class PlancherelSnData n` axiomatises the two standard facts the pinned Mathlib lacks — (i) `Σ_λ dim²=n!`, (ii) the JM/OV content-square mean `2·Σ dim²·Σc²=n(n−1)·n!`. `two_sum_dim_sq_hooks` proves Identity I `2·Σ_λ dim²·Σ_c h_c² = n(3n−1)·n!` from (i)+(ii)+the proved (A); `twoM_eq_plancherel_hook_sum` wires it to `WLambdaDefect.twoM`. Non-vacuity instance `PlancherelSnData 2` decide-checked. So `twoM` (Identity I) is no longer a bare carried `def` — it's a theorem modulo two named axioms. Companion scope doc `docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md` plans the multi-PR Specht/JM build to discharge them (honest: rigor hygiene, not frontier). Lean sorry-free (lean-direct exit 0). |
| 2026-06-24 | [#2717](https://github.com/litlfred/qou/pull/2717) | **Step-1 gate RUN (no fit) — SU(2)/WRT(S³/2I) does NOT reproduce `W_λ`; full-Hecke arena forced.** Ran the #2503 gate systematically at n=3,4,5 (was n=5 spot-check only, #2608): compares SU(2)-side `[2j+1]_q` to S_n-side `d_q(λ)` per block. **(b) structural exclusion of the SU(2) sub-route**, two grounds: COVERAGE — all ≥3-row blocks (incl. electron `(3,1,1)`) are outside the GL₂ Schur–Weyl image, no SU(2) weight (rigorous form of #2406); VALUE — `d_q=[2j+1]_q` ONLY on the standard rep `(n−1,1)` ∀n (both `=[n−1]_q`), sharpening #2608's single-point `(4,1)` to the `(n−1,1)` family. ⇒ geometric index must live full-Hecke side (the open object is **unchanged**, just the SU(2) branch pruned). Normalization (owner Q): per-block ratios within fixed n are normalization-invariant; only `Z(n)` (defect `1−Z(n)`) is sensitive → the defect is the fixed falsifiable content; `Z(5)=0.98222` reproduced. Docs: `2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md`. |
| 2026-06-24 | [#2727](https://github.com/litlfred/qou/pull/2727) | **SU(2)-route foreclosure machine-checked + full-Hecke program scoped.** (b) `Su2SchurWeylForeclosure.lean` (sorry-free): `gl2_image_eq_le2row` (GL₂ Schur–Weyl image = `{(5),(4,1),(3,2)}`), `electron_not_in_gl2_image`, capstone `su2_index_ne_wlambda` (any GL₂-supported index ≠ any `W` nonzero on `(3,1,1)`) — the prose/Python foreclosure of #2406/#2608/#2717 now Lean-proved as a **(b) structural exclusion** (row-count invariant; abstract codomain, no q₀). (c)+(d) `docs/scope/2026-06-24-keystone-fullhecke-geometric-index-program.md`: the multi-PR full-Hecke geometric-index program (phases G1–G4 on #2524's Beasley–Witten mechanism; falsifiable targets defect-cubic / `a_D=lw` / `f_pn`-bracket / conjugation-symmetry; foreclosed sub-routes catalogued; **(d)** Bring/Jacobian sub-lead cites #2710/#2722 under a STRICT numerology guardrail — formalize the monodromy *operator*, never fit `τ=2.6424`). Honest: rigor frontier, not a new prediction; the open full-Hecke object is **unchanged**. |
| 2026-06-24 | [#2704](https://github.com/litlfred/qou/pull/2704) | **Residual (ii) DISCHARGED (Lean, no fit):** `Reeb = Res^{S₅}_{S₃}` scaffold formalized sorry-free + axiom-free (`S5SO3FiberAction.lean`: `s3SignTwist`, `restriction_intertwines_conjugation` = `Res(λ')=s3SignTwist(Res(λ))` ∀λ⊢5, `std_irrep_conjugation_fixed` = the `(2,1)`/h⁴-carrier multiplicity is conjugation-fixed, capstone `reeb_eq_restriction_scaffold [BringFiberAction]`). The *algebraic* restriction-commutes-with-conjugation identity only; conjunct (i) still **uses** `BringFiberAction` (geometric map stays open). Residual (i) (MTC-matching) stays owner-gated; **210 ppb stays refuted**. Audit `2026-06-24-keystone-reeb-restriction-lean-formalization.md`. |
| 2026-06-24 | [#2744](https://github.com/litlfred/qou/pull/2744) | **Falsifiable target (1) PINNED EXACTLY (no fit, q₀-free):** cross-checked the `W_λ` defect cubic `C(n) = −n(n−1)(2n−13)/144` (`WLambdaDefectClosedForm.lean`, from Identity I) against the **directly-computed** `1−Z(n)=1−Σ_λ d_q²/[n]_q!` for n=2..10 via Richardson `h=q−1/q→0` (60 dps). Empirical small-h coefficient matches the closed form to **<4e-14** ∀n, **n=7 sign flip identical** (empirical 7 = closed-form 7). Closes the loop the empirical defect script (`keystone_wlambda_Z_defect_n_scaling.py`) left open — it disclaimed a closed form, having refuted a *different* (hook-moment) ansatz; the Identity-I cubic is the real one. Hardens phase-**G2** gate from "Lean derivation" to "exact number cross-checked against direct `W_λ` compute". **Plus a SECOND target:** the sub-leading h⁴ coefficient `D(n)` is *also* an exact degree-6 polynomial — `D(n)=n(n−1)(−100n⁴+1472n³−5273n²−203n−828)/1036800` (`1036800=50·144²`), Taylor-extracted (method-validated: h² coeff reproduces exact `C(n)` to 0.0; Δ⁶ constant to ~1e-120; held-out validated n=9,10). Both `C(n)` and `D(n)` carry the `n(n−1)` factor (vanish for the single-box partition). So G2 now gates on **two** q₀-free polynomial targets (2nd + 4th heat-kernel coeff). `D(n)` not yet Lean-proved (follow-on). **And a LADDER:** the h^{2k} coefficient `c_{2k}(n)` is polynomial of degree **3k** (C deg 3, D deg 6, E deg 9; each held-out validated), denominator `m_k·144^k` (m_k∈{1,50,7350}) — so the index's *entire* heat-kernel expansion is polynomial-in-n (unbounded target family, not just two). Expected from Plancherel-moment / Kerov-polynomial theory; QOU content = the sharp `3k` ladder + `144^k` denom. Degree-3k law is a CONJECTURE (k≤3 evidence). Probes `keystone_wlambda_defect_cn_closedform_crosscheck.py` + `keystone_wlambda_defect_dn_subleading.py` + `keystone_wlambda_defect_coeff_ladder.py` + witnesses; audit `2026-06-24-wlambda-defect-cn-closedform-crosscheck.md`. |

## Key artifacts

- Audit docs: `docs/audits/2026-06-16-s5so3-*.md` (branching-backbone-verified, ingredient4-fibre-schur-weyl-constraint,
  two-sasakian-construction-attempt, reeb-resonance-probe-negative, hopf-coupling-and-reeb-obstruction,
  markov-weighting-sasakian-scope) + the corrected `2026-06-13-gap-a4-operator-valued-muon-branching.md`.
- Verifiers (all exit 0): `docs/audits/scripts/s5so3_*.py` (branching backbone, ingredient 4/5 markov shift,
  fibre Schur–Weyl, coupling Schur, Reeb resonance, Hopf coupling obstruction, markov weighting facts).
- Lean scaffold: `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean` (open `irrepToRotation` on the corrected A₅-irrep domain — de-vacuified in #2480; was the falsified `partition_to_rotation`).

## Cross-references

- Synthesis: [`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](../audits/2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md)
- Construction program: [`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md`](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md)
- Sibling A≥3 compute cluster: #2369 / #2371 / #2372 (produces `W_λ` algebraically)

## qbk2 q-Bessel "quadratic action" binding direction — FORECLOSED (2026-06-20, double-sourced)

Two independent routes agree the q-Bessel 2nd-kind "quadratic action" is **not** the
binding mechanism:

- **#2521** (session 01Q34jUc): retired via the `2026-06-14` joint-J⊕I combiner (³He
  +17.4%→+117.9% NO-GO); the legitimate "quadratic action" is the content-Casimir `μ_λ`
  already wired into `prop:q-heat-kernel-peter-weyl`; the precheck "P1 fail" is a
  normalizer artifact (`Z(0)=Σd²`, not `[n]_q!`).
- **#2549** (this session, fresh rigorous arc #2530→#2549): forced `y_λ` Markov weighting
  collapses the rigorous reduction-of-order correction from `2.23×` (unweighted) to
  **1–6%** of `B(D)` (~20–80× too small). Refuted by its own forced weighting.

**Convergent negative** (different methods) ⇒ do not re-walk the q-Bessel binding probe.
**Machinery that stands** (additive, from #2549): the resonance-free reduction-of-order
2nd-solution construction + sorry-free Lean lemma `QOU/QBeta/QCasoratianAbel.lean`
(q-Casoratian/Abel law, axioms `[propext, Quot.sound]` only). The C(n) defect closed
form `−n(n−1)(2n−13)/144` (#2527) is the falsifiable sub-leading target for the
*geometric* W_λ index continuation (#2503/#2524/#2488). bean `qbk2` carries both notes;
owner closes.

---

**`a_D=lw` bridge (2026-06-24, #2674).** Merged #2612 lever-1 established the binding
kernel's SW-period anchors as selection-rule values `a_D^(n)=lw(n−1)`,
`lw(c)=(1/(c+1))·Σ_{λ⊢c+1} dim_q` (canonical q-hook `dim_q`), confirmed c=1,2,3 +
the proved depth-2 `det=1` recurrence `R=x²−τx+1`, τ(q₀)=2.6424
(`binding_selection_rule_tau_closure.py`). The open residual — **SW-period =
selection-rule value** — IS this ledger's W_λ geometric-origin frontier: the
Seifert–CS index (#2524) at q₀ on the partition blocks must reproduce the Hecke
q-hook `lw(c)`. Per #2608, this is a **functional-level** identification (same W_λ
family), NOT a naive ~8%-off number-match. Shared validation target: the
`144·C(n)=−n(n−1)(2n−13)` defect. Coordinated on #2488. c=2 status: `lw(2)=(q+1)²/(3q)`
is derivation-tight but **untested** (no independent c=2 observable; Hopf-diquark the
candidate) — `docs/audits/2026-06-24-lw2-c2-prediction-untested-status.md`.

**Geometric `W` constraint — `H^{1,0}(Bring)` is A₅-irreducible (2026-06-24, #2701).**
Working the `a_D=lw` bridge above, the relevant Bring fact is now computed exactly in
Sage (character theory, no numerics): Bring is the canonical genus-4 curve in
`P³ = P(`std 4-dim S₅ rep`)`, so `H^{1,0}(Bring)` **is** the standard rep — verified
irreducible over S₅ (`⟨χ,χ⟩=1`) and **A₅-irreducible** (`χ|_{A₅}=[4,0,1,−1,−1]`,
`⟨·,·⟩=1`). Two consequences for the geometric `W_λ`/`W` build:
1. **No A₅-invariant rank-2 subspace of the holomorphic differentials** ⇒ the
   cheat-sheet `H¹(Bring)=2W` cannot be an A₅-subrep of the forms; `W` must be an
   **isogeny/CM factor of `Jac(Bring)`** (Riera–Rodríguez decomposition), realized at
   the de Rham / abelian-variety level.
2. **`tr B` (= τ(q₀)=2.6424, the `a_D=lw` recurrence trace) is a q-_family_
   Gauss–Manin _monodromy_ trace**, not a fixed-curve period — so the Seifert–CS index
   at q₀ must come from the q-family matrix `M` (this keystone), confirming the
   "functional-level, not naive number-match" framing. The torus shortcut is separately
   refuted: `τ_torus = 2cosh2η₀ = 2.0437 ≠ 2.6424`. Probe/audit only, no fit:
   [`computations/substrate/lever1_bring_period_trB.sage`](../../computations/substrate/lever1_bring_period_trB.sage),
   audit `docs/audits/2026-06-24-lever1-trB-geometric-target.md`. Coordinated on #2608/#2488.

**The rank-2 `W` is the elliptic curve `Bring/S₄`; `Jac(Bring) ~ E⁴` (2026-06-24, #2710).**
Exact extension of the A₅-irreducibility above (character theory, `genus(Bring/H) =
dim std^H`, no fit): `Bring/S₄` is an **elliptic curve** `E` (8 subgroup classes give
genus-1 quotients). Since `H^{1,0}(Bring) = std` is irreducible, `Jac(Bring)` is
isotypic ⟹ a power of one simple factor; the elliptic quotient pins it: **`Jac(Bring)
~ E⁴`** (Riera–Rodríguez). So the framework's **rank-2 "W-plane" is literally
`E = Bring/S₄`** (period = scale + modulus, 2 real DOF), and `H¹(Bring) = H¹(E)⊗std =
2·std`. **Keystone reduction:** the q-family Gauss–Manin monodromy `M` drops from
genus-4 (`Sp(8)`) to a **2×2 `SL₂` monodromy on a q-family `E(q)`**, with the lever-1
target `tr B = 2.6424` literally `tr M` — and the lever-1 depth-2 `det=1` kernel
`R = x²−τx+1` *is* the `SL₂` characteristic polynomial. **Open keystone, now genus-1:**
identify `E(q)` (the q-deformation of `Bring/S₄`; candidate = the elliptic fibre of the
`S³/2I` Seifert build #2524) and test `tr M(q₀) = 2.6424`. `E ≠` substrate torus
(`τ_torus = 2.0437 ≠ 2.6424`). Probe/audit only, no fit:
[`computations/substrate/bring_jacobian_isogeny_factors.sage`](../../computations/substrate/bring_jacobian_isogeny_factors.sage),
audit `docs/audits/2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`. Coordinated on #2524/#2608.
---

**Residual (ii) DISCHARGED — `Reeb = Res^{S₅}_{S₃}` Lean formalization (2026-06-24, [#2704](https://github.com/litlfred/qou/pull/2704), merged `83edee35`).**
[#2524](https://github.com/litlfred/qou/pull/2524)'s honest scope left residual (ii) — the Lean
formalization of the *"Reeb = Res^{S₅}_{S₃}"* identity at the keystone-scaffold level — open. It now
lands sorry-free + axiom-free in
[`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean):

- **The identity.** The Seifert fibration `S³/2I → S²(2,3,5)` has Reeb = the Seifert `S¹` fibre;
  localization restricts along it, algebraic shadow `Res^{S₅}_{S₃}`. The geometric Reeb symmetry
  (conjugate partitions share a fibre, `conjugate_same_a5_irrep`) matches the exact algebraic symmetry
  **restriction commutes with conjugation**: `V_{λ'}=V_λ⊗sgn_{S₅}`, `sgn_{S₅}|_{S₃}=sgn_{S₃}`, so
  `Res(λ')=s3SignTwist(Res(λ))` — swapping `S₃` triv↔sign, **fixing the standard `(2,1)`** (the
  Borromean `h⁴`-carrier).
- **Decls.** `def s3SignTwist`; `restriction_intertwines_conjugation` (∀λ⊢5);
  `std_irrep_conjugation_fixed`; capstone `reeb_eq_restriction_scaffold [BringFiberAction]`. All three
  theorems `#print axioms` = *does not depend on any axioms*.
- **Scope (honest — this is NOT a keystone closure).** Discharges residual (ii) ONLY: the *algebraic*
  restriction-commutes-with-conjugation identity. The capstone's conjunct (i) still **uses** the
  `BringFiberAction` class (the geometric fibre map stays open). **Residual (i) — MTC-matching: pin the
  Beasley–Witten gauge datum on `S³/2I` to the Hecke `Rep U_q(sl_N)` blocks so the localization
  `W_λ = d_q²/D²` is provably OUR Hecke category's Plancherel measure, not "some MTC's" — stays
  owner-gated**, and IS the live `W_λ` geometric-origin frontier in the banners above. **210 ppb stays
  refuted** (the keystone delivers the O(1) generation skeleton, not the 2×10⁻⁷ fine shift). No fit, no
  production wiring, no registry tier change. Audit
  [`docs/audits/2026-06-24-keystone-reeb-restriction-lean-formalization.md`](../audits/2026-06-24-keystone-reeb-restriction-lean-formalization.md).
