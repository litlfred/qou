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
| 2026-06-18 | #2480 | **Lean (formalization fix):** de-vacuify `BringFiberAction` — remove the provably-false `respects_conjugate` (angle sign-flip) + vacuous `hits_five_conjugacy_classes : True` + trivial instance; correct the fibre-map domain to the 5 A₅ irreps (new `A5Irrep` + `conjugate_same_a5_irrep`), substantive `five_distinct_classes`. Per `2026-06-13-bring-fiber-action-falsification.md`. Formalization correction, **not** a closure — the geometric map stays open. |

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
