# Last-5-days machinery — what actually improves mass / binding (commit-by-commit)

**Date:** 2026-07-13 · **Branch:** `claude/delta-lambda-gate-open-for-all-2026-07-13` ·
**License:** critical-distance. Classifies the 2026-07-08…12 landings for mass/
binding value, states what Lean proves, and names the one concrete parameter-free
closure path the new pieces open (the deuteron wall).

## A. New, Lean-backed, structurally sound (USABLE)

| commit | result | Lean status |
|---|---|---|
| `de1b0c62` | **Ohtsuki-tower bar-parity selection rule**: 𝔙 = Vol + i·CS splits by parity — **even rungs → Vol (mass/binding)**, **odd rungs → S (decay)** | `OhtsukiTowerBarParity.lean` `even_rung_real`/`odd_rung_imaginary` **sorry-free** |
| `7fee77ea` | **binding period is Gevrey-1/2** (`n! ≤ 4ⁿ·I(n)² ≤ 8ⁿ·n!`) | `BindingGevreyHalf.lean` **sorry-free** |
| `c7fdd8ae` | **Bridge-equation alien datum** at ω₀=1/√2: level-1/2 Borel singularity, Stokes constant `A_ω = 4√2·e^{−3/8}` (closed form, verified) | probe-verified |
| `1114895c` | **SW classical jet exactness** `λ_SW^(n) = d(X^(n−1))` | Lean + paper |
| `ac1ed765` | mass element **is** an endomorphism (faithful regular rep) | Lean |
| (2026-07-04, foundational) | **bond-count** `M_n(A)=(n−1)` ⇒ `B = m_e·Σ_n (n−1)·Vol_n` → ³H **−0.16%**, ³He −2.97%, **zero fit** | combinatorial (Lean-provable) |

## B. Over-claimed / laundered (NOT usable as-is)

- **NA-Stokes / depth-2 CKRecursion "closure"** (`universal-binding-architecture.md`).
  Adversarial review:
  [`2026-07-13-na-stokes-ck-recursion-binding-adversarial-review.md`](2026-07-13-na-stokes-ck-recursion-binding-adversarial-review.md).
  The isospin "SU(4) differential 1.4947 m_e" **is** the measured ³H–³He split
  (1.4946 m_e) — and its own Lean
  (`isospin-symmetry-breaking-su4-anomaly.lean`) **already carries a `⚠ VACUOUS
  — NOT A DERIVATION` banner (2026-07-11)**: `doublet_degeneracy_split` proves
  `(base+diff)−base=diff` by `ring` (universal tautology), `s3_su4_differential`
  is an unconstrained free parameter. The prose block over-claims what its own
  Lean disclaims. `r_res=2.596 ≠` advertised `5/2`; `c_3=10/3 ≠` canonical `−2`.

## C. Diagnostic / negatives (narrow the search)

- bar-odd-S resummation (#3691/#3716): odd-S sign-flip is representational, not
  resummable (this session).
- exact-rung Borel `A≈0.758`, `Vol/π` refuted (`37cbf722`); m(q₀) derivative-gate
  still blocked on branch prescription (`efd36e51`).

## What Lean can prove (summary)

- **Proved sorry-free:** bar-parity selection (even→Vol/odd→S), Gevrey-1/2
  sandwich, SW jet exactness, mass-endomorphism.
- **Provable (not yet):** bond-count `M_n(A)=(n−1)` (pure linear-chain
  combinatorics — the strongest un-formalized derived binding fact).
- **Not provable / vacuous:** the isospin SU(4) "closure" (self-marked vacuous),
  `r_res`, the CKRecursion "exact closure" (fit + relabel).

## The concrete improvement the new pieces open — the deuteron wall

The bond-count route derives A≥3 binding to ≤3% zero-fit, but leaves **one exact
wall**: the deuteron's 2-body sub-link is the **Hopf link, Vol = 0**, so the
leading even/Vol binding vanishes — yet `B_D = 2.225 MeV ≠ 0`. Three new pieces
compose to attack it *parameter-free*:

1. **bar-parity** puts binding in the **even/Vol sub-tower** (proved).
2. that sub-tower's period is **Gevrey-1/2** (proved) — divergent, so its value
   is the **Borel-resummed** one, not the (vanishing) perturbative Vol.
3. the **Bridge datum** gives the level-1/2 Borel singularity at `ξ=1/√2` with a
   **derived** Stokes constant `A_ω = 4√2·e^{−3/8}` — no free parameter.

**Proposal (derivation-grade, honesty-safe):** apply the Borel–Padé machinery
this session built for the odd/S tower to the **even/Vol tower at ξ=1/√2**,
evaluated for the deuteron. Where the perturbative Vol is 0 (Hopf), the resummed
even-tower value is the alien (non-perturbative) contribution, parameter-free
(derived `A_ω`, `ω₀`, scale `m_e`).

**First test (`deuteron_wall_alien_resummation_probe.py`) — leading term
undershoots; full route OPEN.** The single leading (m=1) level-1/2 alien term is
`m_e·A_ω·e^{−ω₀/√x}`, with a hard ceiling `m_e·A_ω = 1.987 MeV < B_D = 2.225 MeV`
and ~0.21 MeV at the substrate coupling. So the *leading* term alone does not
close the wall — but this is **not** a refutation (scope-(a), not (b)): the full
alien-calculus content is the whole trans-series
`B_D = m_e·Σ_{m≥1} S_m·A_ω^m·e^{−m ω₀/√x}·Φ_m(x)` (bridge equation), which is
**not** bounded by `A_ω` (as `x→∞` every sector → its constant). The Stokes
constants `S_m` and fluctuations `Φ_m` are uncomputed; the full median/Écalle
resummation remains open and can reach `B_D`.

**Physical frame (owner) — the dualized entanglement energy.** Read `B_D` as the
**entanglement energy** of the two-nucleon sub-braid bipartition. The
perturbative (Vol) face vanishes for the Hopf deuteron, so the binding is carried
entirely by the **dual** channel — and the alien calculus *is* the structure of
that dual. The non-perturbative trans-series is the dualized entanglement energy;
the derivation step is to compute the bipartition-dual `S_m/Φ_m`, not to stop at
the m=1 ceiling. This is the honest successor to the CKRecursion — only
Lean-proved structure + a derived Stokes datum, no inserted number.

## Resolve / preserve recommendation

For `universal-binding-architecture.md`: **preserve** the bond-count multiplicity,
the isospin-aware `Vol_n`, and the bar-parity organization (all real); **demote**
the "Theorem 1 / exact mass closure / geometric first principles" prose to match
its own Lean's vacuity banner; **relabel** `1.4947 m_e` as the measured ³H–³He
split (Coulomb-dominated, per the Lean banner), `r_res` as a q₀ datum (not the
invariant `5/2`), and reconcile `c_3=10/3` with the canonical `c_3≈−2`; **fix**
the cheat-sheet 9b "🟢 derived / sub-1ppq" to the actual tier (A≥3 bond-count
≤3% zero-fit; deuteron open). None of this deletes a real result — it aligns the
prose with the evidence and frees the deuteron-wall resummation as the live path.
