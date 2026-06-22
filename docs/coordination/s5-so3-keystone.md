# Coordination ledger — `conj:s5-so3-fiber-action` (the s5-so3 fibre-action keystone)

**Goal.** Discharge the keystone the QOU framework's open derivation math reduces to: the geometric
fibre map `S₅ ⊃ A₅ ≅ I ⊂ SO(3)` tying the partition-wise Wedderburn action on `H₅(q)` (combinatorial)
to icosahedral rotations on Bring's quintic surface (geometric). It is the single open object for
m_τ (lepton tower), GAP-A-3 binding Δ_λ, and GAP-A-4 mass λ(K).

**Status (2026-06-16).** Reduced — by formalize-first pruning — to **one differential-geometry
problem**. Everything combinatorial / representation-theoretic / algebraic is done or refuted; no fit
was introduced anywhere.

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
| **OPEN:** Markov-trace weighting `W_λ` via Wu-manifold SU(3)/SO(3) Sasakian equivariant index | ⛔ differential geometry (owner-gated) |

**The single open object.** Does the SU(3)/SO(3) (Wu-manifold) Sasakian with spatial-SO(3)_colour Reeb
admit a structure whose S¹-equivariant index reproduces the Ocneanu weights `W_λ = d_q(λ)²/[n]_q!`?
(dim 5 odd ✓; χ(Wu)=0 ✓ — Boothby–Wang necessary conditions met, not obstructed at that level.) The
sibling A≥3 operator-branching compute (#2369/#2371/#2372) produces `W_λ` algebraically; the open piece
is its *geometric origin*.

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
