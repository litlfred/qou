# Mass-sweep A≥4 atom→knot rule — 2026-06-02 status refresh

> Short status refresh for the A≥4 atom→knot rule gap, written as
> Branch C of the post-PR-#1690 dashboard tranche. Honest disposition:
> **no new derivation this session** — the gap is research-grade and
> blocked on objects being built by sibling PRs (#1712, #1443/#1524).

## What's open (STATUS.md row)

> Mass-sweep gap (A ≥ 4) | mean abs err 4.25%; ⁶Li / ⁷Li / ⁹Be / ¹¹B /
> ¹⁴N / ¹⁹F GAP (no atom→knot rule)

[`STATUS.md`](../../STATUS.md).

## Authoritative state of the gap

The honest current state is captured in two existing docs (no
new substantive math has landed since 2026-05-30):

1. [`docs/workplans/2026-05-29-a567-atom-knot-sdp.md`](../workplans/2026-05-29-a567-atom-knot-sdp.md)
   — the full workplan (with retraction).
2. [`docs/coordination/2026-05-30-a567-and-alpha-em-coupling.md`](2026-05-30-a567-and-alpha-em-coupling.md)
   — the cross-thread coordination state.

### What survives the discipline bar (2026-05-30 critical-audit)

| structural piece | status |
|---|---|
| Δtr = ‖tr_M(free)‖ − ‖tr_M(atom)‖ from canonical `atom_braid_word_3A` | derived |
| Vol(Borromean) = 8G (Catalan / dilog identity) | derived |
| Factorisation form B = m_e · Vol(K_bind) · Δtr (Kashaev-class) | derived in form |
| f(Z,N) = B_AME / (m_e · 8G · Δtr) | AME-extracted, **not derived** |

### What was retracted as derivation (remain leads)

- `f ≈ Z·N` for D / 6Li / 7Li (0.19–0.62% near-match) — selection-bias
  fitting, not compute-precision derivation.
- ⁴He shell bonus 2.07 ≈ 1+q (1.8%) and ≈ 2√q (1.7%) — also retracted.
- κ_Coulomb ≈ 2√3 / (3π) (935 ppm off) — also retracted.

Source: workplan §"Critical-discipline audit (2026-05-30)" +
[`#1444` retraction comment](https://github.com/litlfred/qou/pull/1444#issuecomment-4581427035).

## What's blocking each level

| Level | Object needed | Where derived |
|-------|--------------|---------------|
| **A=2** (²H) | binding-link PSD-feasibility of L_H (Hopf) at H_3 | live in [PR #1712](https://github.com/litlfred/qou/pull/1712) Test plan item 1 |
| **A=3** (³H, ³He) | binding-link PSD-feasibility of 8_11-class at H_5 | live in [PR #1712](https://github.com/litlfred/qou/pull/1712) Test plan item 2 |
| **A=4** (⁴He) | derived shell-closure bonus (≈ 2.07, retracted) | open — needs operator-valued LR branching, blocked on [#1443](https://github.com/litlfred/qou/pull/1443) + [PR #1524](https://github.com/litlfred/qou/pull/1524) IwahoriHecke Sprint 2 |
| **A≥5** (5/6/7Li, 9Be, 11B, 14N, 19F) | derived K_bind(Z, N) generator | gated on A=4 |

## Recent landings (since 2026-05-30 audit) that touch the gap

### 2026-06-02 17:00–17:35Z (during this doc's review window) — Δ_λ binding-measure probes

**Major narrowing.** Four commits landed in the hour after this doc
was first drafted, directly sharpening the binding-measure half of
the gap:

- **[`ba7af156c`](https://github.com/litlfred/qou/commit/ba7af156c)**
  per-block θ_λ carry via y_λ-weighted observation: B = E · Σ_λ y_λ
  |Δθ_λ|, tested D / T / ³He / ⁴He.  **Absolute binding NOT closed**
  (μ₀ 0-fit −99%; one-global-scale worst 228%): `|Δθ|` is
  A-independent like scalar Δtr.  But **T / ³He difference +8.18 %
  with NO isotope-fit** — the signed per-block object PR #1709
  proved necessary, *without* the fitted (1+q)/2.
- **[`d59bcb79d`](https://github.com/litlfred/qou/commit/d59bcb79d)**
  emit full per-λ θ_λ vector + cheat-sheet §9.2 "**preserve
  information until observation**" guiding principle (τ at step 9 is
  the only legitimate collapse site; scalar `tr_M` collapses θ_λ at
  step 5 prematurely — harmless A=2, lossy A≥3).  Adds Lean debt
  queue items L-1 / L-2 / L-3 (Schur character-orthogonality,
  π_λ idempotent orthogonality, per-λ Frobenius block-orthogonality)
  to the proof-watcher queue.
- **[`5e388f598`](https://github.com/litlfred/qou/commit/5e388f598)**
  full-order θ_λ (Re = rotation, Im = growth/volume): **`y_λ` is the
  WRONG measure for A≥3 absolute** — `Σ y_λ |Δθ|` *anti-correlates*
  with A (D 0.133 → ⁴He 0.006) while binding grows ~13×, because
  `y_λ` (the Markov / trace measure) **suppresses the growth
  channels** where the extensive binding lives.  Narrowed gap: per-
  block θ_λ carrier is right (differences work, +8 %, no fit), but
  `y_λ` is the wrong measure for binding.
- **[`d7c56c17e`](https://github.com/litlfred/qou/commit/d7c56c17e)**
  binding-measure search — `abs_content` (Σ |content| of the Young
  diagram) is the **standout from 6 candidates**: A-growth ratio
  S(⁴He) / S(D) = 13.40 vs target 12.72 (~5 %), worst |err| 20 %.
  `y_λ` failed (199 %); other candidates 600–90 000× off.  Refined
  target for the operator-valued combiner (#1698): **content × sign
  per-block measure ≠ y_λ**.  Discipline: 20 % is NOT closure;
  `abs_content` was selected from 6 candidates — a structural lead,
  not a derivation.

**Note on the `|·|` in these probes — it's the cautionary tale, not
endorsement.**  PRs [#1641](https://github.com/litlfred/qou/pull/1641)
and [#1643](https://github.com/litlfred/qou/pull/1643) established
that `|·|` in pre-archimedean (pre-τ) expressions is a structural
**choice**, not a convergence requirement; 34 non-archimedean misuse
sites were flagged on main for per-site author review.  The `|Δθ_λ|`
in the formula `B = E · Σ_λ y_λ |Δθ_λ|` is **exactly the
information-losing collapse** that the new cheat-sheet §9.2
"preserve information until observation" principle warns against —
and the probes ran the formula *as a falsification test* to confirm
that scalar `|·|`-collapse at step 5 (pre-τ) loses the growth
information that A≥3 binding lives in.  The conclusion of the
chain is: **don't use `|·|` at this step** — carry the full
per-λ θ_λ vector (Re = rotation, Im = growth/volume) to the τ
observation, then collapse.  The `abs_content` lead in `d7c56c17e`
also uses `|·|` (Σ |content|) for the same A-growth-test purpose;
upgrading it to a derived identity will require replacing `|·|`
with the signed / bar-symmetric counterpart that respects the
"preserve information" cut.

**Net effect on this doc's blocking table.**  The "A=4 (⁴He) shell-
closure bonus derivation" row above was already known to be open;
these landings narrow the open problem from "find the missing
combiner" to **"derive `|content|` (or its signed / bar-symmetric
upgrade) as the Hecke-energy density and combine it with the
signed per-block phase to get a binding-specific weight
`w_λ^bind`"**.  That is the productive next probe (see "What
WOULD be a productive next probe" below — now revised).

### 2026-05-30 → 2026-06-02 16:00Z — Q_β sub-attacks (cross-link)

- **#1690** (merged today, 14:00Z): dashboard wiring + Lean sibling fill + q₀
  drift fixes. **No new derivation**, just regenerates witnesses at
  current q₀.
- **#1593** (Q_β c_3 order audit): the per-block Δtr_M is O(√u); ladder
  c_3 is O(u³) — accidental cross-order coincidence. This is *upstream*
  of the binding-factor f decomposition: the Hecke-block structure of
  Δtr_M is now characterised at compute precision, which clarifies that
  any f(Z, N) derivation must respect the bar-symmetric / paired
  structure shown at u¹ in #1602.
- **#1602** (Q_β eigenphase Taylor in u): "eigenphase = f" FALSIFIED at
  u¹. The cos eigenphase has a nonzero u¹ coefficient `−√3 / 12`.
  Constraint on the Q_β scaling map carries over: any f(Z, N)
  derivation that goes through a single eigenphase will also
  inherit a u¹ obstruction.
- **#1622** (Habiro q-difference Fourier mode-solve): partial-fraction
  decomposition of Δtr_M(u = √q) into three sectors — entire poly + ζ₄
  cyclotomic + Laurent tower. The ζ₄ cyclotomic sector's bar-even
  content is **exactly 1/2** (a clean constant). This is a *structural
  characterisation* of Δtr_M that any A≥4 binding-factor derivation
  must respect.
- **#1641 / #1643** (Φ_q signed-vs-modulus): the `‖·‖` in the
  factorisation form is a structural CHOICE, not a convergence
  requirement; at v = ±0.142 the signed/modulus ratio diverges 13.3×.
  Per-site audit on the binding-factor pipeline still pending.

## Live sibling PRs in scope

| PR | Scope | This branch's relation |
|----|-------|------------------------|
| **[#1712](https://github.com/litlfred/qou/pull/1712)** | m_p linking_weight (2.532780 → 2.461648) + ²H/³H binding-link canonical object | **direct overlap on A=2, A=3 levels**. Will post intent comment. |
| **[#1709](https://github.com/litlfred/qou/pull/1709)** | volume-Wedderburn Δ_λ probe; q-6j saddle isolated | adjacent — Δ_λ closure path runs in parallel to f(Z, N) derivation |
| **[#1713](https://github.com/litlfred/qou/pull/1713)** | Q_β Habiro fibre F(q) categorical ID | upstream — closes the same Hecke-block structure that A≥4 derivation needs |
| **[#1714](https://github.com/litlfred/qou/pull/1714)** | KL recursion H_5 / H_6 scaffold (Iwahori-Hecke; the PR's title uses S_n but the q-deformed object is the Hecke algebra per AGENTS.md §7a) | upstream for Option-E PROBE 4; Demazure crystal closure path |
| **[#1516](https://github.com/litlfred/qou/pull/1516)** | Option-E Phase 2 H_3 + H_6 + PROBE 4 | parallel Δ_λ path |

## What WOULD be a productive next probe (next session, not this one)

Per AGENTS.md Δ_λ gate ("**do not propose a seventh fit-based
ansatz**") and the 2026-05-30 retraction (selection-bias fitting is
forbidden), the productive directions — **revised in light of the
17:00–17:35Z Δ_λ landings above** — are:

1. **(NEW, highest priority) Derive `|content|` as the Hecke-energy
   density.** The `d7c56c17e` finding is that `abs_content` matches
   A-growth at ~5 % vs `y_λ`'s 199 %.  This is a *categorical*
   lead: `content(λ) = Σ_{(i,j) ∈ λ} (j − i)` is the q-grading of
   the partition `λ` (the same quantity that appears in the q-Schur
   `ySchurClosedForm = q^{c(λ)} / [n]_q!`).  A *derived* identification
   of `|content|` with a Hecke-energy density (rather than selection
   from 6 candidates) would upgrade the lead from 20 % near-match to
   a categorical statement.  **Categorical scoping**:
   [`2026-06-02-abs-content-hecke-energy-scoping.md`](2026-06-02-abs-content-hecke-energy-scoping.md)
   — identifies 5 candidate categorical constructions (trace of `|Ω_q|`,
   arm + leg hook sum, etc.) and pre-states the falsification
   signatures any derivation must clear.  This is the productive
   direction for any next-session probe on this gap.
2. **Wait on PR #1712's PSD-feasibility test at A=2, A=3.** If L_H
   (Hopf) for ²H and 8_11-class for ³H pass PSD-feasibility at q₀,
   that's the binding-link canonical object derived. *Then* extend to
   A=4 via operator-valued LR branching (still gated on #1443 + Sprint 2).
3. **Wait on PR #1713's fibre F(q) identification.** If the Q_β Habiro
   element lands, the same fibre construction applies to the
   binding-factor f(Z, N) via the shared multi-Wedderburn-block
   structure recorded in the 2026-05-30 coord doc.
4. **No new ansatz attack** without one of the above first. The retracted
   leads stand as suggestive structure; they are NOT to be re-pitched
   as a new derivation candidate without a categorical chain replacing
   selection-bias fitting.  In particular, `abs_content` × signed-phase
   is **infrastructure** (a per-λ vector to feed the operator-valued
   combiner), **not** a new closed-form ansatz.

## This branch's scope

- One coord refresh (this doc)
- One intent comment on PR #1712 noting the A=2, A=3 overlap
- **No new derivations, no new code, no new witnesses, no production wiring**

This is a *coordination* PR, not a math PR. The math gap is real and
will close when #1712 + #1713 + #1443/#1524 each land their respective
upstream pieces.

## Cross-refs

- [`AGENTS.md`](../../AGENTS.md) §Precision goals (L2 trio shared root)
- [`AGENTS.md`](../../AGENTS.md) §Δ_λ gate (no 7th ansatz)
- [`AGENTS.md`](../../AGENTS.md) §"Before declaring open math" checklist (corpus-grep)
- [`docs/coordination/2026-05-30-a567-and-alpha-em-coupling.md`](2026-05-30-a567-and-alpha-em-coupling.md)
- [`docs/workplans/2026-05-29-a567-atom-knot-sdp.md`](../workplans/2026-05-29-a567-atom-knot-sdp.md)
