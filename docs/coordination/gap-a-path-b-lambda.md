# GAP-A / Path B per-atom λ(K) — coordination ledger

> Sibling-axis ledger to [`1ppq-qbeta.md`](1ppq-qbeta.md). Tracks the
> Path B / per-atom λ(K) closure chain that closes [#1762](https://github.com/litlfred/qou/pull/1762)'s
> Option D from the mass / binding-energy side.

## Goal

Identify whether the per-atom Path B multiplier `λ(K)` in
`m(K) = m_e · Vol(K)/ℏ_q² · λ(K) + S(K)` is substrate-derivable, and if not,
which sub-leading `S(K)` form bridges the residual gap.

## Status — cont. 1 (2026-06-05)

**17 + 1 no-fit closures.** The Δ_λ-gate ansatz family is closed
(8 in the gate doc + #1860 Kashiwara × 5 + #1870 brane-tower × 5 = 18); the
GAP-A-4 §4 direction 3 (³He residual structural lead) closes negative
under cross-isotope extrapolation (#1883). The Phase-4 per-atom
amplitude `A(K)` remains substrate-derived to ≤ 2.5 %. The remaining
productive directions are #1876 §4-2 (additive `S(K)`) and §4-4
(per-knot `Vol(K)` convention re-examination).

| PR | Outcome | Net |
|---|---|---|
| [#1816](https://github.com/litlfred/qou/pull/1816) | merged | Option A diagnostic — light-series Vol(K) wired, RED gate confirmed |
| [#1841](https://github.com/litlfred/qou/pull/1841) | merged | Option B Bratteli induction REFUTED (3/3 sub-hypotheses) |
| [#1850](https://github.com/litlfred/qou/pull/1850) | merged | Markov trace stabilization axis REFUTED (z<1 obstruction + M1/M2) |
| [#1853](https://github.com/litlfred/qou/pull/1853) | merged | H₃→H₄ both axes refuted (consolidation) |
| [#1860](https://github.com/litlfred/qou/pull/1860) | merged | Option E Kashiwara Δ_λ — 5/5 candidates REFUTED |
| [#1822](https://github.com/litlfred/qou/pull/1822) | merged | qbeta rung-lifts (cross-axis tie) |
| [#1864](https://github.com/litlfred/qou/pull/1864) | merged | 3-paths-refuted roadmap consolidation (recommends "linking_weight_family_a is CODATA-implied near-match" framing) |
| [#1868](https://github.com/litlfred/qou/pull/1868) | merged | GAP-A-3 scope (brane-tower content channels) |
| [#1870](https://github.com/litlfred/qou/pull/1870) | merged | GAP-A-3 deuteron P_λ — 5/5 channels REFUTED |
| [#1872](https://github.com/litlfred/qou/pull/1872) | merged | GAP-A-4 Path B scope (L1/L2/L3 candidates) |
| [#1874](https://github.com/litlfred/qou/pull/1874) | merged | GAP-A-4 L1 light-series — L1a/b/c REFUTED (proton +2.89 % gap recovered) |
| [#1876](https://github.com/litlfred/qou/pull/1876) | merged | L1 retrospective (4 next-probe directions; #1882's ³He +0.70 % flagged) |
| [#1882](https://github.com/litlfred/qou/pull/1882) | merged | ³He L1b residual — `sqrt([3]_q/[2]_q)` +0.70 % filed as NUMEROLOGY |
| [#1883](https://github.com/litlfred/qou/pull/1883) | merged | Cross-isotope extrapolation REFUTED (>1000 % worst rel_err) → ³He numerology CONFIRMED |
| [#1886](https://github.com/litlfred/qou/pull/1886) | merged | T1 — additive `S(K)` sub-leading REFUTED under uniform-λ (100× swing across light series) |

## Status — cont. 2 (2026-06-17)

The parallel **Δ_λ-route** arc (#2405 / #2417 / #2426 / #2430 / #2433) closed
its last two levers, and one of them touches this ledger:

- **Dense Wedderburn-projector SDP closed structurally** (the
  `claude/delta-lambda-open-levers-2026-06-17` branch,
  [`docs/audits/2026-06-17-wedderburn-sdp-structural-bound.md`](../audits/2026-06-17-wedderburn-sdp-structural-bound.md)).
  The `confinement-sdp.md` program reduces to `min⟨T,Φ⟩ s.t. Φ⪰0, trΦ=c` with
  block-constant diagonal `T = μ_λ`; the per-block / 2×2-pair constraints are
  redundant, and the optimum is a degenerate min-cost **face** (at `q₀`,
  `μ_[2,1]=μ_[1,1,1]<μ_[3]` ⇒ 5-of-6-dim) that selects no unique operator and
  excludes the trivial block — so it cannot select `𝓑₃`.
- **GAP-A-3 stale-claim correction.** #2433 listed GAP-A-3 as a "non-refuted"
  lever; per this ledger it is **already refuted** (#1868 scope + #1870 5/5
  `P_λ` channels; part of the 18-closure saturating chain). The audit above
  records the correction so the route is not re-opened.
- **T3 stale-row correction.** This ledger's T3 task row still read "scope
  landed; probe follow-up open" — also stale. The probe was built
  (`computations/probes/gap_a4_T3_mass_pochhammer_probe.py`) and ran **NEGATIVE**
  (R4, [#1897](https://github.com/litlfred/qou/pull/1897); 4 bar-symmetric
  q-Pochhammer candidates refuted, worst −98% at the P3 Markov-trace ratio;
  `2026-06-05-gap-a4-final-retrospective.md §2`). So **no nominally-open
  per-atom-`λ(K)` numerical thread remains.** The one genuinely-open *direction*
  is the owner-gated `conj:s5-so3-fiber-action` geometric fibre map (categorical
  research — partition-of-5 ↦ A₅ rotation on Bring — NOT a numerical `λ(K)`
  search; "no 7th fit ansatz").

## Status — cont. 3 (2026-06-18)

Two findings from the T/³He same-`n` differential test
([#2466](https://github.com/litlfred/qou/pull/2466),
[`docs/audits/2026-06-18-pauli-young-delta-lambda-the3-refutation.md`](../audits/2026-06-18-pauli-young-delta-lambda-the3-refutation.md)):

- **Pauli-Young / Wigner-SU(4) Δ_λ closed — the 19th no-fit closure.** The
  spin-isospin Young-symmetry projection proposed in
  [#2461](https://github.com/litlfred/qou/pull/2461) is a multiplicity
  (`Δ_λ ≥ 0`); on the sharp T/³He split `(B_T−B_³He)/m_e = +1.4947` the concrete
  `Δ_λ = dim GL(4)(λ)` gives **−45** (wrong sign, ~30×). An isospin-*symmetric*
  projection cannot supply the isospin-*breaking* split (the `h=q−q⁻¹` anomaly,
  `2026-05-24-isospin-categorical-source.md`). Also **not novel** —
  `wigner-su4-from-spin-isospin.md` + `schur-weyl-mass-decomposition.ts` already
  carry it (a too-narrow corpus-grep in #2461). The saturation chain is now 19.
- **Proved chirality sign is consistent with the T/³He split (structural plus).**
  Diagnostic (not a fit) on the *existing* proved weight
  `Δ_λ = sgn(w₀^{S_λ'})·dim` + its enumerated magnitude variants: the proved
  **sign gets the differential sign RIGHT** (`sgn·dim → +0.436` MeV = 57 % of
  target; `sgn·dimq → +0.596` = 78 %; undershoot, matching #2405's per-atom
  result), unlike the refuted non-negative projection. The residual is a pure
  **magnitude** question on an otherwise sign-correct structure; the **linear**
  binding model reproduces the T/³He ordering, the `|·|` model does not. This
  reaffirms the cont. 2 steer: the open frontier is the **owner-gated categorical
  `s5-so3-fiber` magnitude/Vol question, NOT a numerical magnitude fit** — a new
  fitted magnitude would be the gated 19th→20th ansatz.
- **Refinement of the 2026-06-02 necessary condition.** Direct `v_λ` sign census
  is 10+/20−, so the non-negative *cone* is **not** sign-blocked (correcting "a
  positive per-block volume cannot reproduce even the sign"); the obstruction is
  that the *principled symmetric shape* is wrong, and any sign-correct
  non-negative weight is a free fit.
- **Sparse interface-operator magnitude refuted (parameter-free).** The
  "binding concentrates on one dominant Wedderburn block" magnitude reading
  ([`binding-formula-closure`](../audits/2026-05-26-delta-lambda-binding-formula-closure.md)
  §"LP-dual single partition") fails the T/³He mirror ratio: the trace is *not*
  sparse (top block `[6,3]` only 34 %), the common dominant block's character
  ratio is 0.633 vs AME 1.099, and the *only* block with ratio ≈1.099
  (`[5,1,1,1,1]`) carries 0.1 % of the trace. ⇒ the magnitude is **irreducibly
  multi-block**; single-dominant-block concentration cannot respect the mirror.
  ([`2026-06-18-sparse-interface-magnitude-the3-prune.md`](../audits/2026-06-18-sparse-interface-magnitude-the3-prune.md)).

## Cross-axis hub

The step-9 binding closure ledger
[`2026-06-05-step9-binding-closure.md`](2026-06-05-step9-binding-closure.md) (PR
[#1871](https://github.com/litlfred/qou/pull/1871), flag-bearer
`claude/confident-newton-R8lIx`) is the **adjacent-axis hub** for the
broader step-9 derivation gap. The two ledgers track related but distinct
questions:

| Ledger | Question | Axis |
|---|---|---|
| this (`gap-a-path-b-lambda.md`) | substrate-derivability of the per-atom `λ(K)` in Path B | per-atom mass multiplier |
| [`2026-06-05-step9-binding-closure.md`](2026-06-05-step9-binding-closure.md) | additive many-body binding series via SW-residue + q-difference | many-body binding closure |

The two intersect on: (a) the per-knot Vol(K) convention (T2 here ≡ C2 there), (b) the per-block-vs-global density gate (T3 here ≡ §4.B C1 there), (c) the bar-odd binding-difference observable (∼ L5 there; merged in #1871). My chain's negative results (`Δ_λ` Kashiwara, Markov stab, brane-tower content, L1 carrier-transplant) constrain their q-difference kernel `R(q,x)` derivation.

## Active sibling-axis coordination

- **[#1762](https://github.com/litlfred/qou/pull/1762)** (1ppQ roadmap) —
  parent. Roadmap-status comments posted at cont. 0 ([#1762-c.0](https://github.com/litlfred/qou/pull/1762#issuecomment-4626482823))
  and cont. 1 ([#1762-c.1](https://github.com/litlfred/qou/pull/1762#issuecomment-4632431195)).
- **[#1871](https://github.com/litlfred/qou/pull/1871)** (SU(2)/SO(3)
  per-block density) — same per-block-vs-global RED gate from the
  M=Vol×Density side. Coord posted; supports their "no production
  swap" decision.
- **[#1784](https://github.com/litlfred/qou/pull/1784)** (binding-link
  assignment heuristic) — Path C `atom→knot assignment` gate; same
  ³He atom is where #1883's numerology localised. Coord posted; their
  "Jones-via-Markov-derived link" is the cleanest productive next step.

## Discipline observations (from this chain)

1. **"Fix as numerology unless derivable" rule** (author, 2026-06-05) —
   a NEAR-MATCH (<5 %) with no categorical derivation is filed as
   coincidence pending derivation. Single-atom matches are
   numerology unless backed by cross-isotope structural rule.
2. **18 no-fit closures form a saturating chain** — no per-partition
   ansatz survives (single statistic, brane-tower content channel,
   induction, stabilization, Bratteli, Kashiwara crystal, etc.).
3. **Productive direction has shifted** from "derive per-partition
   Δ_λ" (closed) to "derive per-atom mass closure via Path B" (the
   `S(K)` sub-leading term + the `Vol(K)` convention question).

## Tasks on this ledger

| # | Task | Status |
|---|---|---|
| T1 | Probe #1876 §4 direction 2 — additive `S(K)` sub-leading form | **closed NEGATIVE** ([#1886](https://github.com/litlfred/qou/pull/1886) merged) |
| T2 | Probe #1876 §4 direction 4 — per-knot `Vol(K)` convention for compound atoms (cross-link with [#1871](https://github.com/litlfred/qou/pull/1871), [#1784](https://github.com/litlfred/qou/pull/1784)) | **closed NEGATIVE** ([#1891](https://github.com/litlfred/qou/pull/1891) merged); all 3 conventions REFUTED, best swing +132 % |
| T3 | Derive `λ(K)` from a Path B-specific formulation (NOT a Phase-4 transplant; per #1876 O2) | **closed NEGATIVE** ([#1897](https://github.com/litlfred/qou/pull/1897)); R4 — 4 bar-symmetric q-Pochhammer candidates REFUTED (worst −98% at the P3 Markov-trace ratio; `2026-06-05-gap-a4-final-retrospective.md §2`). Scope: [`2026-06-05-gap-a4-T3-path-b-lambda-formulation-scope.md`](../audits/2026-06-05-gap-a4-T3-path-b-lambda-formulation-scope.md) |
