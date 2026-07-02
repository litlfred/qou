# 2026-07-02 — Step-9b binding gap: PROBE 2 (α_k assignment structure) + PROBE 4 (per-λ brane tower)

**Branch:** `claude/cheat-sheet-derivation-gaps-0ykco4` · **Beans:** `nf8d` (PROBE 2), `v292` (PROBE 4)

Two owner-approved derive-or-refute probes on the step-9b binding gap.
Scripts (assertion-bearing, witness-emitting, 50 dps per
`computations/_precision.py`, q₀ from the canonical 50-digit pinning
witness):

- [`computations/probe_9b_alphak_structure.py`](../../computations/probe_9b_alphak_structure.py)
  → [`probe-9b-alphak-structure.witness.json`](../../computations/probe-9b-alphak-structure.witness.json) (8 assertions, all pass)
- [`computations/probe_9b_perlambda_brane_tower.py`](../../computations/probe_9b_perlambda_brane_tower.py)
  → [`probe-9b-perlambda-brane-tower.witness.json`](../../computations/probe-9b-perlambda-brane-tower.witness.json) (9 assertions, all pass)

Context: the depth-stratified tower's unclosed gap is the per-depth
**assignment rule** α_0 = α_1 = α_3 = 1, α_2 = z² ≈ 0.2493,
α_{k≥4} = m_e·8G ≈ 3.7445
([2026-06-09 audit](2026-06-09-binding-canonical-default-depth-stratified.md));
the Borromean single pipeline converges ∀Z with the right shape but a
~2.3× normalization miss at ¹⁶O
([2026-06-28 plan](2026-06-28-brane-tower-formalize-first-plan.md),
[deuteron doc](2026-06-28-brane-tower-higher-order-deuteron.md)).
No new fit constants anywhere below; the Δ_λ gate (no 7th ansatz) is
respected — no per-λ constant is introduced, only re-decompositions of
quantities the pipelines already collapse.

---

## PROBE 2a — α_3 centrality check (bean nf8d)

**Question.** Does the natural Markov-marker series α_k = z^k
degenerate at k = 3 *because* the depth-3 GB layer of H_3 is the
Garside element Δ = σ₁σ₂σ₁ (a character computation, not a fit)?

### Verdicts (tiered)

| claim | tier | key numbers |
|---|---|---|
| The z^k series **breaks at k = 3** | **DERIVED (exact)** | tr_M(T_Δ) = z + h·z² = z·(1 + q^{1/2} − q^{-1/2}) ≠ z³; symbolic (sympy, exact in q) + 50 dps (dev ≤ 5.4e-71) |
| Mechanism: χ^{(2,1)}(T_Δ) = 0 | **DERIVED (exact)** | ρ_{(2,1)}(Δ)² is the central full-twist **scalar** and det ρ_{(2,1)}(Δ) = −1 < 0 ⇒ eigenvalues ±√c ⇒ **traceless**. The standard block drops out of the depth-3 trace; the weight collapses onto the outer 1-dim blocks (q³, −q⁻³) |
| "Because the element **is central**" (as literally stated) | **REFUTED-scope-(a)** | Δ is **not** central in H_3 (ρ_{(2,1)}(Δ) has off-diagonal −b ≠ 0; conjugation by Δ swaps σ₁ ↔ σ₂). It is Δ² (full twist) that is central; centrality-of-Δ² **+ det < 0** is what forces the collapse. The corrected mechanism is derived (row above) |
| The observed **value** α_3 = 1 | **NEAR-MATCH (10.4 %)** | collapsed depth-3 weight relative to depth-1: tr_M(T_Δ)/tr_M(T_1) = 1 + q^{1/2} − q^{-1/2} ≈ **1.10439** at q₀ vs assigned α_3/α_1 = 1; **exact as q → 1**. The break is derived; the normalization to exactly 1 is not |

### Detail

Per-element Markov weights of the six GB basis layers of H_3 at q₀
(50 dps; y_λ solved **exactly** from the depth ≤ 2 Markov data, so the
depth-3 value is *forced*, not fitted):

| depth k | layer | tr_M(T_w) | z^k |
|---|---|---|---|
| 0 | 1 | 1 | 1 ✓ |
| 1 | T₁, T₂ | 0.4993203… = z | z ✓ |
| 2 | T₁₂, T₂₁ | 0.2493208… = z² | z² ✓ |
| 3 | T_Δ | **0.5514434… = z + h·z²** | z³ = 0.124491 ✗ |

The depth-3 layer collapses back toward the depth-1 weight because Δ
has cycle type (2,1) (it is conjugate to the depth-1 transposition
s₁): the Markov trace tracks cycle structure, not Coxeter depth, and
the χ^{(2,1)} = 0 vanishing (forced by Δ²-centrality + det = −1)
removes the only block that could distinguish them. This gives the
α-assignment's α_1 = α_3 = 1 pattern a structural *reason* at the
break level; the residual 10.4 % (→ 0 as q → 1) is the honest
distance between "depth-3 degenerates to depth-1" and "α_3 exactly 1".

## PROBE 2b — α_{k≥4} plateau as geometric resummation

**Question.** Does m_e·8G (8G = Vol(L6a4)) equal Σ_{k≥4} z^k·N_k at
q₀, with N_k the per-depth element count of the GB filtration
J^k/J^{k+1} of the relevant H_{3A}?

**Verdict: REFUTED-scope-(a)** — under all four N_k readings
(`cox` = Coxeter-length counts, i.e. coefficients of [3A]_t!;
`parts` / `dim` / `dimsq` = the depth-stratified compute's own
partition-depth layer data), for every atom. No (atom, reading) pair
is an IDENTITY at 1e-10; none is even a 10 % near-match:

| atom | cox | parts | dim | dimsq |
|---|---:|---:|---:|---:|
| nucleon (H₃) | 0 | 0 | 0 | 0 |
| D (H₆) | 8.091 | 0.0932 | 0.3418 | 1.585 |
| T/³He (H₉) | 119.35 | 0.4465 | 43.64 | 5696.1 |
| ⁴He (H₁₂) | 1111.6 | 1.3136 | 3690.2 | 1.498e7 |

target m_e·8G = **3.744460** MeV.

Structural kill (still scope-(a) — other weightings untested): the
tail sum is strongly **A-dependent** (cross-atom max/min from 14× up
to 9.4e6× per reading) whereas the plateau α_{k≥4} is A-independent
by construction — no per-atom counting of this shape can equal a
universal constant. This sharpens the 2026-06-09 audit's dimensional
objection (§(i)): the plateau constant is not a z-geometric
resummation of the filtration layer counts, as-is, alone.

---

## PROBE 4 — per-λ Borromean brane tower, collapse-last (bean v292)

**Question.** The scalar single-pipeline tower applies
g(x) = −Li₂^q(−x) to the collapsed τ = |tr_M(β_Bor)| ≈ 0.99856. The
¹⁶O 2.3× normalization miss is diagnosed as the missing per-λ weight.
Carry (y_λ(q₀), χ^λ(β_Bor)) for λ ⊢ 3 through g **per block** and
collapse **last** — does that close the 2.3× without breaking ∀Z
convergence or the shape?

**Discipline note.** This is **not** the refuted "Δ_λ per-block
density" (that refutation concerned multiplying an *intensive scalar*
density); here the weight rides an already-extensive tower, and no new
constant enters — the (y_λ, χ^λ) pairs are exactly the decomposition
the scalar pipeline collapses.

### Verdicts (tiered)

| claim | tier | key numbers |
|---|---|---|
| Pipeline τ **is** the SU(2)/Temperley–Lieb (Jones) Markov decomposition | **DERIVED (exact)** | τ = ([4]/[2]³)·χ^{(3)} + (1/[2]²)·χ^{(2,1)}, y_{(1³)} = 0, with χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶; identity holds to 9.1e-72 at 50 dps; χ^{(2,1)} cross-checked against the direct Hoefsmit seminormal matrix product (exact) |
| Trace-convention gap | **FINDING (recorded)** | the corpus-canonical Wenzl z-trace gives τ_W = Σ y_λ^W χ^λ ≈ 0.9983666 ≠ τ ≈ 0.9985622 — gap 1.955e-4. The single pipeline is the **Jones/TL** trace, not the Wenzl-bridge z-trace. Irrelevant at the 2.3× scale; matters for any future sub-0.1 % binding claim |
| RAW per-block tower (arguments χ_λχ_μ) | **EXCLUDED (invariant-backed)** | χ^{(2,1)}² ≈ 3.9768 > q₀ ≈ 1.10998 exceeds the **proved** Li₂^q convergence radius \|z\| < q (`_li_2_q_util.li_2_q`) — same divergence class as the 2026-06-28 atom-word refutation. Constructive consequence: per-block must carry *normalized* characters r_λ = χ^λ/d_λ with weights W_λ = y_λ·d_λ (Σ W_λ = 1 by Markov M3) |
| Normalized per-λ tower closes the ¹⁶O 2.3× | **REFUTED-scope-(a)** | all three collapse-last variants — per-λ Jones, per-λ Wenzl, and ambient-H₆ per-ν (exact Murnaghan–Nakayama + Littlewood–Richardson branching, validated against Wenzl disjoint multiplicativity Σ_ν y_ν^{(6)} χ^ν(β⊗β) = τ_W² at 9.1e-72) — reproduce the scalar tower to ≤ **6.6e-7** relative across D … ⁵⁶Fe. ¹⁶O errT: 2.2752 → 2.2752 (ambient 2.2763). ∀Z convergence and shape preserved, normalization untouched |

### Why the null result is structural (and useful)

The collapse-last pair term Σ W_λ W_μ [g(r_λ r_μ) − g(r_λ r_μ f_b)]
agrees with the scalar term at linear order in g by construction
(Σ W_λ r_λ = τ); the difference is the Jensen gap of g over the block
spread. For β_Bor the normalized block values are
r = (1, 0.997093, 1) — spread ~3e-3 — so the Jensen gap is O(10⁻⁶)
relative. **Conclusion:** the missing per-λ weight, if it exists,
cannot be the *un-weighted* Markov decomposition (y_λ, χ^λ) of the
same Borromean trace carried through the same g. It must inject
per-block information *beyond* the Jones trace of β_Bor — consistent
with the FR-restricted volume-enrichment reading (`χ^λ·χ^λ(e_{K*})`,
the GAP-A-3/A-4 levers) already identified as the Δ_λ frontier in the
2026-06-28 plan §7. This probe eliminates the cheapest candidate
(pure re-decomposition) with exact machinery, narrowing the Δ_λ search
per formalize-first.

### Per-isotope table (B_tower, MeV; err = B_AME/B)

| iso | B_AME | scalar (Jones) | err | per-λ (Jones) | ambient H₆ | err |
|---|---:|---:|---:|---:|---:|---:|
| ²H | 2.225 | 2.480 | 0.90 | 2.480 | 2.479 | 0.90 |
| ³H | 8.482 | 4.919 | 1.72 | 4.919 | 4.917 | 1.73 |
| ³He | 7.718 | 4.300 | 1.79 | 4.300 | 4.298 | 1.80 |
| ⁴He | 28.296 | 6.387 | 4.43 | 6.387 | 6.384 | 4.43 |
| ⁶Li | 31.995 | 10.515 | 3.04 | 10.515 | 10.508 | 3.04 |
| ⁷Li | 39.245 | 13.434 | 2.92 | 13.434 | 13.425 | 2.92 |
| ¹²C | 92.162 | 32.642 | 2.82 | 32.642 | 32.623 | 2.83 |
| ¹⁶O | 127.619 | 56.092 | **2.28** | 56.092 | 56.064 | **2.28** |
| ⁵⁶Fe | 492.254 | 685.115 | 0.72 | 685.114 | 684.864 | 0.72 |

Scalar baseline cross-checked against the committed
[`borromean-binding-recompute.witness.json`](../../computations/borromean-binding-recompute.witness.json)
at max rel dev 3.3e-16.

---

## Net effect on the step-9b gap

1. **α_3 = 1 is no longer a bare convention**: the break of the z^k
   marker series at k = 3 is a theorem of H_3 (Δ²-centrality +
   det ρ_{(2,1)}(Δ) = −1 ⇒ χ^{(2,1)}(T_Δ) = 0 ⇒ collapse to depth-1
   order), with the exact residual 1 + q^{1/2} − q^{-1/2} ≈ 1.1044
   quantifying what a genuine derivation of α_3 = 1 must still explain
   (10.4 % at q₀, 0 at q = 1). Natural Lean target:
   `chi21_garside_zero` (pure algebra, generic ring per §7c).
2. **The plateau α_{k≥4} = m_e·8G is not a filtration resummation**
   (scope-(a)); its A-independence positively rules out the whole
   per-atom layer-count family, redirecting derivation attempts to
   A-independent structures (the L6a4 volume itself).
3. **The Δ_λ frontier survives the cheapest closure candidate**: pure
   per-block re-decomposition of the same Borromean trace is now
   numerically excluded at 6.6e-7 (three independent collapse-last
   constructions, exact branching machinery), so per-λ closure work
   should go directly to weightings that carry *new* per-block content
   (knot-ideal projector / volume enrichment), not re-collapses.
4. **Bookkeeping finding**: the single pipeline's τ is the Jones/TL
   trace (y = dim_q^{SU(2)}/[2]³, (1³) killed), 1.955e-4 away from the
   corpus-canonical Wenzl z-trace. Any future sub-0.1 % binding claim
   through this pipeline must state which trace convention it uses.
