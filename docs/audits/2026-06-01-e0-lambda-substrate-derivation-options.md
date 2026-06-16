# 2026-06-01 — Substrate-derived per-block energy E₀^λ: ranked candidate-construction options

**Branch:** `claude/e0-lambda-map-options-2026-06-01`
**Audience:** any agent attempting to close the L2-Subgoal-1 binding gap (Q_β / m_n / Δ_pn) by replacing the deprecated `fit_three_E0` with a parameter-free χ^λ(K) → M_λ(K) map.
**Status:** SCOPING / OPTION-ENUMERATION ONLY. No fit implemented, no back-solve, nothing tuned to B_AME or to the {e⁻, p, n} anchors. The {e⁻, p, n} per-block energies are the **falsification test**, not fit targets.

---

## BLUF

The L2-Subgoal-1 binding gap localizes to ONE missing object: a parameter-free map
**χ^λ(K) → M_λ(K)** (substrate-derived per-block energies E₀^λ in MeV). This doc
enumerates and ranks five candidate constructions for that map.

**Verdict (short):** Four of the five candidates (Archimedean per-block VolDensity,
q-dimension weighting, co-Casimir, ribbon twist) are killed by the **same proved
impossibility theorem** (GAP-A-4 verifier, `rho-prefactor-structural-verifier.witness.json`,
`allPassed: True`): **any function `f(χ_λ, y_λ, q₀)` of the H_3-level Wedderburn data is
constant across the Markov-equivalent atoms {p, n, ³He}, yet their physical M_λ / ρ
differ.** A per-block energy that is a function of the block's own character + q-dimension
*cannot* be the map, by theorem, not by failed fit. These are flagged 🔴 LATENT FIT or
🔴 PROVED-INSUFFICIENT.

**The one candidate that carries genuine information beyond χ^λ** is the per-vertex
**seminormal eigenphase / q-Reeb phase** (Candidate 3, the subtle one the task flagged).
The summed-trace loophole `Σ_w ρ_w = χ^λ` IS closed (2026-05-31 design note), but the
**per-vertex eigenphase θ_λ = arccos(χ_λ/d_λ)** is provably NOT a function of the scalar
χ^λ alone — it resolves the rotation vs growth channel split that the scalar trace
collapses. This is the only object with a non-circular path. **However**, it has already
been probed (v4/v5/v6) and to date it closes only *differences* (the ³H−³He mirror pair to
2%, B_D to −9%), not absolute E₀^λ — and the v6 combination re-introduces a free scale `γ`.
It is ranked #1 to attempt next, but with eyes open that it is a *narrow* opening, not a
guaranteed closure.

**If forced to bet:** the honest read is that the χ^λ → M_λ map is **probably impossible
from H_3-level substrate data alone** (GAP-A-4 impossibility theorem), and the only escape
is the **off-diagonal / per-vertex eigenphase content at H_{3A}** (Candidate 3) or
upstream **GAP-A-1 binding-operator-K identification** (which determines K's block content
at H_{3A} directly, bypassing the need for a χ^λ→M_λ rule). If even Candidate 3 collapses
to a difference-only object with no absolute scale, that is itself a profound valid result:
L2 Subgoal-1 would be **unreachable without a new substrate axiom** (an absolute per-block
energy normalization), bordering on Subgoal-2.

---

## The problem, precisely (verified against artifacts)

The Path-D atomic mass formula (`docs/audits/2026-05-18-delta-lambda-gating-context.md`):

$$B(K) = m_e \sum_{\lambda \vdash 3A} y_\lambda(q_0)\, \chi^\lambda(\beta_K)\, \Delta_\lambda(K),
\qquad \Delta_\lambda(K) = \frac{M_\lambda(K) - m_e\,y_\lambda\,\chi^\lambda}{m_e\,y_\lambda\,\chi^\lambda}.$$

- `y_λ(q₀)` (Wenzl) and `χ^λ(β_K)` (Hoefsmit/Markov) are **known** (cached 50 dps).
- `M_λ(K)` — the per-block mass-functor component in MeV — is the missing object.
  `E₀^λ` is the per-block energy scale such that `M_λ(K) = E₀^λ · (substrate block data)`.
- The deuteron gives **1 equation in p(6)=11 unknowns Δ_λ** → 10-dim solution set.
  χ^λ(K) does NOT determine M_λ(K).

**The only existing χ^λ → M_λ map in the repo** is
`computations/_deprecated/per_block_phi_q.py :: fit_three_E0` — a linear
least-squares fit of THREE free scales `(E₀^sym, E₀^std, E₀^alt)` to the three anchors
{e⁻, p, n} (3 equations, 3 unknowns, rank 3, exact). That is the thing to **replace** with
a derivation. Its per-block MeV outputs on {e⁻, p, n} are the falsification target: a real
candidate must REPRODUCE the {e⁻, p, n} per-block energies from substrate data with **zero
free scales**.

---

## The unifying obstruction (read this before evaluating candidates)

`docs/audits/2026-05-31-gap-a3-a4-feasibility-assessment.md` §3.2 records a **proved
impossibility** (`rho-prefactor-structural-verifier.witness.json`, `allPassed: True`):

> At the braid strand count H_3, the canonical operators for **proton, neutron, and ³He
> are Markov-equivalent** — their per-λ character profiles `(χ_λ, y_λ)` are bit-for-bit
> identical (e.g. all share `χ^{[2,1]} = 1.994185810381214`, `y = 0.2809296339798641`),
> yet observed ρ ∈ {1, 1, 2}. **No `(χ, y)`-only rule can distinguish them.**

Five candidate rules (`exact dim_q`, `round dim_q`, `floor dim_q`, `hook-special-case`,
`classical d_λ`) all fail. This is a **theorem**, not a failed fit: any function of the
H_3-level character data is constant across {p, n, ³He}.

**Consequence for E₀^λ candidates.** Any candidate of the form
`E₀^λ = g(χ_λ, y_λ, dim_q λ, q₀)` — i.e. a function of the block's own representation-
theoretic + character data — is constant on Markov-equivalent atoms and therefore **cannot
be the χ^λ→M_λ map**. This single theorem kills Candidates 1, 2, 4 (and 5, which is also a
content-only function). Candidate 3's per-vertex eigenphase is the **only** proposal that
is provably NOT a function of `(χ_λ, y_λ)` alone.

---

## Ranked candidates

### 🟢 #1 (attempt next) — Candidate 3: per-vertex seminormal eigenphase / q-Reeb phase

**Idea.** The Hoefsmit/Young seminormal representation `ρ_λ : H_n(q) → End(V_λ)` has an
orthonormal basis `{v_T : T ∈ SYT(λ)}`. On each rotation block the braid eigenvalues are
unit-modulus `e^{±iθ}`; the per-vertex / per-rep **q-Reeb phase** is
`θ_λ = arccos(χ_λ / dim_λ)` (the normalized character clamped to [−1,1]).
Source object: the **off-diagonal + eigenphase content** of `ρ_λ(β_K)`, NOT the diagonal
trace. (`computations/binding_reeb_phase_decomposition.py` docstring is the
authoritative statement of the rotation-vs-growth channel split.)

**Why it is NOT killed by the GAP-A-4 theorem.** The theorem kills functions of `(χ_λ, y_λ)`.
The eigenphase `θ_λ = arccos(χ_λ/d_λ)` and especially the **free-vs-atom difference**
`Δθ_λ = arccos(χ_atom/d) − arccos(χ_free/d)` use the *atom* and *free* character separately
and the per-rep eigen-structure — information the scalar trace `tr_M = Σ y_λ χ_λ` provably
collapses (cheat-sheet line 113/136; `binding_volume_difference_probe.py` shows every scalar
observable refuted A≥3 *because* the growth channel cancels in the difference). So the
per-vertex object genuinely carries information beyond χ^λ.

**Why the ρ_w summed-trace loophole is already closed (but a DIFFERENT object).**
`docs/audits/2026-05-31-rho-w-crystal-vertex-trace-design.md` PROVED that summing the
per-vertex *diagonal* trace over the crystal `Σ_w ρ_w = χ^λ` (trace = sum of diagonal),
reproducing the −82.9% deuteron miss. **That note explicitly scopes its negative result to
the diagonal trace and names the off-diagonal/eigenphase content as the un-tried direction.**
So Candidate 3 ≠ the closed ρ_w object; it is the eigenphase, which the design note flags as
open.

**Parameter-free?** The eigenphases θ_λ and Δθ_λ are parameter-free (Hoefsmit closed form +
substrate q₀). 🟡 **CAUTION**: turning a *phase* (dimensionless angle) into an *energy* (MeV)
needs a scale. The framework's derived candidate is `μ₀ = m_e/(3(q−q⁻¹)/2) ≈ 1.63 MeV`
(cheat-sheet, "universal-ilp-algorithm", PROVED derived). If `μ₀` is the only scale and it is
derived, the construction stays parameter-free. **The latent-fit risk** is the v6 combination
`B = μ₀·ℏ_q·J_q²(n/2) + γ·Σ_rot y_λ Δθ_λ` introducing a *new* scale `γ` "to be determined"
(`option_e_v6_combined_canonical.py` docstring). **If `γ` is fit, it is RED.** The
parameter-free version uses only μ₀.

**Reproduces {e⁻, p, n}?** Mixed / not yet. The eigenphase route has been probed:
- v4 (`option-e-q-reeb-phase-probe-v4.witness.json`): variant_A_with_chi and variant_B_phase_only
  both miss D/T/³He by **94–99.8%** (absolute binding).
- v5/v6 witnesses are empty on disk (scripts present, not freshly run).
- Cheat-sheet line 113/136: the *difference* observable closes the ³H−³He mirror pair to 2%
  and B_D to −9% with 0 free params — but that is a **difference**, not absolute E₀^λ.

So the honest status: the eigenphase carries real extra information and closes *differences*,
but no run to date reproduces the absolute {e⁻, p, n} per-block energies parameter-free. It is
the right place to push because it is the only non-circular object; it is NOT a demonstrated
closure.

**Tractability.** Infrastructure exists (`binding_reeb_phase_decomposition.py`, v4–v6). A
focused attempt — "does μ₀ · (per-rep eigenphase functional) reproduce the e⁻/p/n per-block
energies the deprecated fit gets, with NO γ?" — is **this-session-to-few-days** tractable.
Risk: it likely closes only differences (the absolute-scale degree of freedom is exactly the
thing the scalar trace removed), in which case it confirms the impossibility (see "If all
fail" below).

**Risk rating:** MEDIUM tractability, HIGH scientific value (only non-circular object).

---

### 🟢 #2 (attempt next, upstream) — GAP-A-1 binding-operator-K identification (bypasses the χ^λ→M_λ map)

**Idea.** Rather than derive a per-block energy *rule*, fix the binding operator
`K(𝔥) ∈ H_{3A}(q₀)` itself via the R5-full SDP from substrate + constituents alone (no AME),
then read its dominant Wedderburn block λ*(K) and per-block profile directly. This *is* the
χ^λ→M_λ map: knowing K's block content at H_{3A} gives M_λ(K) without a separate rule.
Sources: `docs/audits/2026-05-31-gap-a3-a4-feasibility-assessment.md` §6 item 1; GAP-A-1 SDP
feasibility (K(²H) = σ₃² Hopf, PSD-feasible, duality gap 4e-7).

**Why parameter-free.** The SDP is solved against substrate + constituent data; if it has a
unique solution without an AME constraint, K is determined parameter-free. **Latent-fit risk:**
the SDP is underdetermined (the same 1-eq-in-11-unknowns system in disguise) UNLESS a
substrate-only objective uniquely pins K. The "binding-K solver mode that finds K without
fitting" is the open piece. 🟡 If the SDP needs B_AME to select among feasible K, it is RED.

**Reproduces {e⁻, p, n}?** Not directly testable as a per-block-energy reproduction — this
candidate produces K, not E₀^λ. The falsification test would be: does substrate-only SDP K
reproduce the *binding* of the three light anchors it can reach? Untested as a closure.

**Tractability.** MULTI-WEEK (needs the SDP "binding-K solver mode"). Highest leverage
(simultaneously gives ρ via GAP-A-4 and the block profile via Δ_λ) but largest effort.

**Risk rating:** LOW tractability (weeks), HIGHEST leverage. Recommend as the parallel
long-horizon track while Candidate 3 is the short-horizon probe.

---

### 🔴 #3 — Candidate 1: Archimedean functor per-block VolDensity

**Idea.** The mass formula `m(K) = m_e · VolDensity(K, q₀)`. Ask whether VolDensity acts
per-Wedderburn-block, giving `M_λ = m_e · VolDensity|_λ` directly from the functor's action on
the block's Specht module.

**Verdict: 🔴 PROVED-INSUFFICIENT (this is exactly the GAP-A-4 impossibility).** VolDensity
restricted to block λ is a function of that block's character + q-data, i.e.
`f(χ_λ, y_λ, q₀)`. By the H_3 impossibility theorem it is **constant across Markov-equivalent
{p, n, ³He}**, so it cannot supply the distinct M_λ they require. Additionally, the global
VolDensity is the object behind the **uniform +2.89% m_p/m_n gap** (cheat-sheet §5) — that gap
is bar-symmetric and block-uniform, i.e. a single scale error, the OPPOSITE of the
per-block-resolved structure binding needs. The deprecated `per_block_phi_q.mass_per_block`
*does* compute per-block masses `(m_sym, m_std, m_alt)` — but it then needs **three fitted
E₀^block scales** to hit MeV. Removing the fit leaves only `VolDensity|_λ ∝ f(χ_λ)`, which the
theorem forbids. **Latent fit.** Do not advance as a standalone closure.

**Reproduces {e⁻, p, n}?** Only via the 3 fitted E₀ scales (= the deprecated fit). No.

---

### 🔴 #4 — Candidate 2: q-dimension / quantum-dimension weighting

**Idea.** `E₀^λ ∝ dim_q(λ)` or a hook-content product at q₀.

**Verdict: 🔴 PROVED-INSUFFICIENT.** `dim_q(λ)` is the canonical example of an
`f(χ_λ, q₀)` content-only function and is one of the five rules the GAP-A-4 verifier
**explicitly tested and falsified** (`exact dim_q`, `round dim_q`, `floor dim_q`,
`hook-special-case`, `classical d_λ` — `rho-prefactor-structural-verifier.witness.json`,
0 of 5 reproduce ρ for all 4 atoms). It is constant on Markov-equivalent atoms. **Latent
fit** if a proportionality scale is then tuned. Do not advance.

**Reproduces {e⁻, p, n}?** No (falsified for the closely-related ρ problem; same obstruction).

---

### 🔴 #5 — Candidate 4: Casimir / co-Casimir eigenvalue

**Idea.** `E₀^λ` from the quadratic Casimir / Frobenius co-Casimir eigenvalue on block λ.

**Verdict: 🔴 PROVED-INSUFFICIENT and already failed as Option B.** The Frobenius co-Casimir
per-isotypic restriction is `tr_M(C_dim_q · 1_λ) = 1/dim_q(λ)`
(`rho_k_h3a_co_casimir.py`, `thm:frobenius-codim-universal`). It is **proved τ-invariant =
vortex-blind**: "every braid β_K on H_n(q) sees the SAME Δ_λ profile". That is the GAP-A-4
impossibility in its purest form — it literally cannot depend on K, so it cannot distinguish
{p, n, ³He}. It is also already logged as failed **Option B** (`docs/audits/2026-05-18`:
residual −2.30 MeV, wrong sign, vortex-blind). The Casimir-as-functor audit (2026-05-31)
separately shows the *physical* Casimir route has an unresolved mode-indexed `ε_n` obstruction
and is not a per-block energy source. Do not advance.

**Reproduces {e⁻, p, n}?** No (Option B failed; vortex-blind by theorem).

---

### 🔴 #6 — Candidate 5: ribbon / Frobenius twist θ_λ

**Idea.** The ribbon element's eigenvalue on block λ is `θ_λ = q^{2·content(λ)}` (a
content-sum power of q). Use `E₀^λ ← θ_λ`.

**Verdict: 🔴 LATENT FIT / PROVED-INSUFFICIENT, plus a dimensional problem.** The ribbon
twist on block λ is again a pure `f(content_λ, q₀)` content-only function → constant on
Markov-equivalent atoms → killed by the GAP-A-4 theorem. It is mathematically identical in
form to the q-dimension / co-Casimir family (content-sum based). Dimensionally it is a phase
`q^{2c}` (unit-modulus on the substrate's relevant blocks), so it needs an energy scale anyway
— and if that scale is tuned, RED. NOTE: the ribbon *content* is exactly what feeds the
eigenphase in Candidate 3 (the Jucys–Murphy `L_k v_T = q^{2c_T(k)} v_T` action) — so the
ribbon twist is not independently useful; its information is subsumed by Candidate 3 and used
there in a non-circular way (via the free-vs-atom phase difference). Do not advance as a
standalone.

**Reproduces {e⁻, p, n}?** No (content-only; same obstruction).

---

## Ranking summary

| Rank | Candidate | Object E₀^λ drawn from | Parameter-free? | Reproduces {e⁻,p,n}? | Tractability | Flag |
|------|-----------|------------------------|-----------------|----------------------|--------------|------|
| 1 | **3. per-vertex eigenphase / q-Reeb θ_λ** | seminormal eigenphases (off-diagonal, free-vs-atom Δθ_λ) | YES if scale = derived μ₀; RED if γ fit | not yet (closes *differences* only: ³H−³He 2%, B_D −9%) | this-session→days | 🟢 only non-circular object |
| 2 | **GAP-A-1 K-identification** | substrate-only SDP for binding operator K at H_{3A} | YES iff SDP uniquely pins K w/o AME | untested as closure | multi-week | 🟢 highest leverage |
| 3 | 1. Archimedean VolDensity per-block | f(χ_λ, y_λ, q₀) on Specht module | NO (needs 3 fitted E₀) | NO | — | 🔴 GAP-A-4 theorem |
| 4 | 2. q-dimension weighting | dim_q(λ) | NO | NO (5/5 rules falsified) | — | 🔴 GAP-A-4 theorem |
| 5 | 4. (co-)Casimir eigenvalue | 1/dim_q(λ), τ-invariant | NO (vortex-blind) | NO (Option B failed) | — | 🔴 GAP-A-4 theorem |
| 6 | 5. ribbon twist θ_λ = q^{2c} | content-sum power of q | NO (content-only + phase) | NO | — | 🔴 subsumed by #1 |

---

## Which 1–2 to attempt next

1. **Candidate 3 (per-vertex eigenphase), short-horizon, parameter-free version only.**
   The single non-circular object. Run the focused falsification CHECK:
   *does `μ₀ · (per-rep eigenphase functional, free-vs-atom)` reproduce the e⁻/p/n
   per-block energies the deprecated `fit_three_E0` gets, with NO γ and NO C_knot?*
   If yes → genuine closure. If it only closes differences → confirms the impossibility
   (a valid profound negative result; see below). **Do NOT introduce γ as a fit.**

2. **GAP-A-1 K-identification, long-horizon, in parallel.** Build the substrate-only
   "binding-K solver mode" SDP. If K is uniquely pinned without AME, M_λ(K) follows from
   K's H_{3A} block content directly — the cleanest route, but weeks of work.

## Which are latent fits (do not advance)

Candidates 1, 2, 4, 5 are all functions of `(χ_λ, y_λ, dim_q λ, content_λ, q₀)` — content-only
data killed by the **GAP-A-4 H_3 impossibility theorem** (constant on Markov-equivalent
{p, n, ³He}). Any of them "closes" only by re-introducing a per-block fitted scale (the
deprecated `fit_three_E0` three-scale fit, or a per-knot `C_knot` back-solve). 🔴 RED.

## If even Candidate 3 fails — the profound clean result

If the parameter-free eigenphase functional closes only *differences* and provably has no
absolute per-block scale derivable from substrate data (the scalar trace removed exactly that
degree of freedom; the eigenphase restores the *relative* structure but not the absolute MeV
normalization), then **the χ^λ → M_λ map is impossible from substrate-only data**. That would
mean **L2 Subgoal-1 is unreachable without a new substrate axiom** — specifically an *absolute
per-block energy normalization* — which is a Subgoal-2-class object (out of scope per
`docs/precision-goals.md`). Report cleanly; do not paper over with a 7th fit.

---

## Numerical CHECK performed this session

The deprecated fit's witness (`per-block-phi-q.witness.json`) is **not on disk** (the script
is deprecated and was not re-run). The falsification target is therefore the *structure*
documented in `_deprecated/per_block_phi_q.py`: a rank-3 linear least-squares fit of THREE
free scales `(E₀^sym, E₀^std, E₀^alt)` to {e⁻, p, n} (3 eq, 3 unknowns, exact). No candidate
in this doc was run against it (that would require executing a derivation; this is scoping
only). The honest comparison run for Candidate 3 is the **recommended next-session CHECK**
above; it must report the raw eigenphase-vs-anchor numbers whether they match or miss.

---

## Cross-references

- `docs/audits/2026-05-18-delta-lambda-gating-context.md` — the Δ_λ gate, six failed ansätze, the M_λ definition.
- `docs/audits/2026-05-31-gap-a3-a4-feasibility-assessment.md` — GAP-A-4 H_3 impossibility theorem (the unifying obstruction).
- `docs/audits/2026-05-31-rho-w-crystal-vertex-trace-design.md` — ρ_w summed-diagonal-trace = χ^λ (closed); names off-diagonal/eigenphase as un-tried.
- `docs/audits/2026-05-31-casimir-derivation-attempt.md` + `2026-05-31-casimir-as-functor.md` — Casimir mode-indexed ε_n obstruction.
- `docs/canonical-derivation-cheat-sheet.md` §"Bind" (lines 113, 131–139) — per-rep q-Reeb phase closes ³H−³He to 2%, B_D to −9%; μ₀ derived.
- `computations/_deprecated/per_block_phi_q.py` — the deprecated `fit_three_E0` (the thing to replace).
- `computations/binding_reeb_phase_decomposition.py` — rotation-vs-growth channel split (Candidate 3 infrastructure).
- `computations/option_e_{q_reeb_phase_probe_v4,canonical_reeb_v5,v6_combined_canonical}.py` — eigenphase probes (v4 misses 94–99.8%; v6 re-introduces γ).
- `computations/rho_k_h3a_co_casimir.py` — co-Casimir = 1/dim_q(λ), τ-invariant (vortex-blind, Option B).
- `rho-prefactor-structural-verifier.witness.json` — the proved 0/5-rules impossibility data.
