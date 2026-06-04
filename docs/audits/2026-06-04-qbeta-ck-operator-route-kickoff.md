# Q_β c_k operator-valued derivation — tranche kickoff

**Date:** 2026-06-04
**Branch:** `claude/qbeta-ck-habiro-operator-route-2026-06-04`
**Status:** OPEN — foundation gate landed; operator-valued execution (Stages 1–5) is the next compute
**Builds on:** precision floor (#1844), residue-A kernel deepening (#1839), α_EM Habiro template (#1521), keystone recipe (audit 2026-06-04)

## Why this tranche exists (necessity)

The [precision-floor result (#1844)](2026-06-04-qbeta-ck-holonomic-c11-attempt-verdict.md)
proves the `c_k≥4` of the Q_β ladder `Q_β = Q_base·∏_k(1 + c_k·u^k)` **cannot be
data-extracted**: the extraction uncertainty is `σ(c_k) = σ_R/u^k` with
`σ_R ≈ 6e-7` (measured neutron Q_β), so only `c_2` (0.8 %) and `c_3` (≈49 %,
marginal) clear the floor; `c_4..c_10` are noise at any anchor count. The `c_k≥4`
must therefore be **derived from framework structure**, not fitted. This tranche
pursues that derivation.

## The structural gate (foundation, landed)

Before any compute, the **formalize-first** invariant that prunes the dead
hypothesis class — probe
[`qbeta_ck_scalar_reversion_obstruction.py`](../../folio-assistant/computations/qbeta/qbeta_ck_scalar_reversion_obstruction.py):

- `ℏ_q = (q−1)/q` is **linear** in `t = q−1` (`ℏ_q = t − t² + t³ − …`), so
  `u = b·ℏ_q²` has a **b-independent double zero** at `q=1`
  (`u = b(1)·t² + O(t³)`).
- The reversion `t(u)` therefore needs a `u^{1/2}` branch, so `R(q)` is a clean
  series in **integer** powers of `u` **only if `R` is even in `t`** (bar-even,
  since `q ↦ q⁻¹` acts as `t ↦ −t + O(t²)`).
- **α_EM** succeeded with a scalar Habiro element because `H(q)=[2]_q·(1−h²α)`
  **is** bar-even; the **Q_β** trace-difference is **not** bar-fixed
  archimedean, so its scalar `c_k` series is singular.

⇒ the `c_k` are **operator-level (`N=k`) coefficients of the Hoefsmit `T_β`
chain** (each representation level contributes `b^k·ℏ_q^{2k} = u^k` by substrate
scaling), **not** scalar-`q` Taylor coefficients. This is the single open axis.

## Refuted classes (do NOT re-attempt — corpus-grep complete)

Per [`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
and the [`ck-dk` registry](../coordination/ck-dk-canonical-registry.md):
real-q single/composite `c_3` (C1, C2), constant-kernel recursion (C5),
Pell-Lucas into free rungs (C6), SDP extraction (C7), algebra-tower box-adding
(C8), trace-level Markov-stabilisation (C12), literal Wenzl-projector Markov
trace (Family α), literal Kashaev-dilog (Family β). **All scalar.** The
obstruction above explains *why* they share a wall.

## Established (do NOT re-derive)

`c_2 = −1` (proved, Kashiwara `f̃₁²`, sorry-free Lean PR #1602); Φ_8 universality
across all 10 pair-differences (level-2 SU(2) Wenzl annihilator, PR #1625);
simple pole at `u_substrate` (fibre-level, PR #1727); Markov-trace invariance of
the `c_k` (PR #1750).

## The open axis — operator-valued Hoefsmit `T_β` chain (roadmap)

Executable recipe:
[`2026-06-04-qbeta-1ppq-keystone-exact-construction-recipe.md`](2026-06-04-qbeta-1ppq-keystone-exact-construction-recipe.md).
Stages, with `free-neutron-decay.py` (Δ(net) producer) + `hecke/hecke_characters.py`
(Hoefsmit seminormal `ρ_λ(σ_i)`):

1. **Stage 1** — exact symbolic `net(T_w)(q)` per particle word (GB-Shirshov reduction) → Laurent polynomials.
2. **Stage 2** — exact `Δ(net)(q)`; `Q_β(q) = |Δ(net)|·𝔈₀(q)`; validate `Q_β(q_0) ≈ 0.78233` MeV.
3. **Stage 3 (first gate)** — build the Hoefsmit `T_β` matrix from `ρ_λ(σ_i)`; read the per-level (`N=k`) operator coefficients; **verify `N=2` reproduces `c_2 = −1` exactly** (structural anchor, PR #1786). The next sub-gate is bar-evenness of the level-graded form under the Hoefsmit trace-bilinear (the un-tried constraint, registry §5).
4. **Stage 4** — operator-level log-match to extract `c_3..c_8` (the `ladder_ck` routine applied to the matrix, not the scalar).
5. **Stage 5** — evaluate `Q_β(q_0)` to 1 ppQ at `N=8` truncation.

## Coordination

- **#1844** (precision floor) — the necessity; this tranche is its constructive sequel.
- **#1839** (residue-A kernel deepening) — overlapping residue-A/`c_k` work; flagged the floor result there so the cleaner-`c_k` re-run isn't over-invested.
- **#1521** (α_EM Habiro) — the bar-even template that this obstruction contrasts against.
- **#1811** (Q_β fibre composite-4 + Habiro machinery) — the fibre-level Habiro arm; the operator route is complementary (level-grading, not fibre root-of-unity).

## Guards

Formalize-first invariant (not a fit); the obstruction is b-independent + witness-anchored; diagnostic-only; tiers governed by the registry.
