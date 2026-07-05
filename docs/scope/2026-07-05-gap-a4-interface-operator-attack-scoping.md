# GAP-A-4 class-D scoping — the A=4 interface operator (Δ_λ magnitude closure)

**Date:** 2026-07-05 · **Discipline:** formalize-first (AGENTS.md §Formalize-first
probe discipline). Read-only scoping; no new fit-based ansatz (Δ_λ gate). This
note maps the ~40-probe A=4 (⁴He) interface-operator graveyard, isolates the one
genuinely-untried structural lever, and states the formalize-first invariant that
should gate it *before* any wide search — the class-D complement to the landed
I-1/I-6/I-2 gate trio (`QOU/MassTheory/TraceConventionGate.lean`,
`QOU/MassTheory/BarParityExclusion.lean`).

## 1. The gap

The per-isotope binding closure `B(K)/m_e = Σ_λ y_λ χ^λ(β_K) Δ_λ(K)` is closed
for the co-Casimir-refuted / bar-parity-pruned classes (the gate trio). The open
frontier is the **⁴He magnitude**. The complete 77-partition signed Wedderburn
sum `Σ_f = −10.867` gives **B(⁴He)_f ≈ 5.55 MeV** against **B_AME = 28.296 MeV**
(−80.4%, a **×5.10** gap; `option_e_a4_full_reconciliation`).

**The gap is a missing higher-order term, not a weight and not a sign** — three
already-proved facts pin this:

1. **Not a wrong per-λ weight.** The per-bond factors `z, z−h, z−h/2` are
   Lean-exact and `Δ_λ = sgn·dim` is Lean-proved (`deltaSign_mixed`). "Inaccurate
   alone" ≠ "excluded" (AGENTS.md §Before declaring "refuted", principle 1).
2. **Not closable by sign reassignment.** `DeltaLambdaL1Ceiling.lean` proves
   (scope-**(b)**, triangle inequality) `‖c‖₁/|target| = 0.41 < 1` at ⁴He — a
   magnitude-*adding* term is **necessary**, no re-signing of existing data reaches
   the target.
3. **≥4-body and ⁴He-LOCAL.** The connected 4-body Ursell cluster is measured at
   `b₄/b₂ = 4.16`; pairwise assembly caps at `6.08×D` vs the `12.72×D` needed
   (**2.09× super-pairwise at ⁴He**, vanishing to `super× = 0.94` by ⁶Li — the
   α-shell-closure signature). Even a KL-Betti uplift ceilings at ~11 MeV.

So the missing object is **magnitude-side, ≥4-body, sharply localized at A=4**.

## 2. Refutation map (representative of ~40 probes)

| Probe / lever | Tried | Verdict + scope | Invariant backs a (b)? |
|---|---|---|---|
| **T2** per-knot `Vol(K)` convention | `λ_emp` near-constant under "right" Vol | REFUTED **(a)** (+132% best swing) | no |
| **T3** mass-side q-Pochhammer | bar-sym depth-3A weights | REFUTED **(a)** (−98%; I-1/I-2 pre-applied) | no |
| **T4–T8** Schur-Weyl functors (5) | A₅-fibre → Borromean `h⁴` via q-Schur/RT/Bratteli | REFUTED, leans **(b)** (`V₂` absent at `sl₂`; `H` = two distinct `sl₃` irreps) | rep-theory facts |
| **T9–T14** q-modular / icosahedral (McKay / Klein / Eisenstein / Hermite) | pull back through `q=1` | REFUTED **(b)** | **yes** — `E₄,E₆` diverge as `q→1⁻` vs polynomial `h⁴` |
| **T15–T18** polynomial / R-matrix | derive `χ^{(2,1)}(β_Bor)=2−3h⁴−h⁶`, `tr_M h⁴=−3/4` | **POSITIVE** — closes the *single-Borromean* `h⁴`, **not** the A=4 magnitude | — |
| multiplicative `1−∏f` 4-body | chain vs tetrahedron | topology not the scale **(a)**; Lean **(b)**: `productModel_3body_nonpos` + `markovParam_le_half` exclude attractive 3-body from any saturating pairwise product | **yes** (Lean) |
| additive / log linked-cluster | `Σ(−log f)`, `Σ(1−f)` | direction confirmed **(a)**; DV/complete ⁴He **+1.07%** but overshoots light atoms | no |
| chirality-weighted 3-body | `sgn(w₀)·χ` combiner | sign **solved** (escapes the nonpos theorem); magnitude 10–24× short **(a)** | — |
| structured combiner | `|χ|`-mag + chiral sign | best; relocates gap to **pairwise-trace magnitude −40%** (A=3) **(a)** | — |
| KL-Betti `B_λ` (magnitude leg) | swap `f^λ → B_λ` | `B_λ` **not cell-invariant** → no canonical value; ⁴He ceiling ~11 MeV **(a)** | sign leg Lean **(b)** |
| sign-only ℓ¹ ceiling | any sign reassignment | **(b)** `‖c‖₁/|target|=0.41 < 1` at ⁴He ⇒ magnitude term necessary | **yes** (Lean) |
| pairwise-assembly ceiling | max over `{mult,add}×{chain,complete}` | `6.08×D` at ⁴He vs `12.72` needed ⇒ **2.09× super-pairwise, ⁴He-LOCAL** **(a)** | no |
| `a4_option_e_color_tube` (10³) | numerology | −79%, **UNSUBSTANTIATED** (Rule-14 hidden DOF) | no |
| link-volume braid closure | close word, SnapPy vol | dead (5-comp non-hyperbolic ≠ binding link); `Vol₄≈8.046` unverified, **gated on #604 R5-full SDP** | no |
| full `f^λ` reconciliation (77 partitions) | all partitions signed | 5.55 MeV, −80.4%, **needs ×5.10** | no |

## 3. Untried lever + gating invariant

**Lever 1 (the one clean formalize-first probe) — connected 4-body [1⁴]
SU(4)-supermultiplet Ursell cluster.**

- **Hypothesis class.** The connected `C(A,4)` Mayer/Ursell term realized as the
  Markov trace of the closed **antisymmetric `[1⁴]` supermultiplet** operator,
  *added* to the structured (`|χ|`-magnitude + chiral-sign) combiner as the
  missing many-body magnitude term.
- **Formalize-first invariant (gate BEFORE the probe).** Prove
  **`e_A[h₃]` (the antisymmetric SU(4) plethysm) vanishes for `A > 4`** — a
  degree / orbit-count vanishing. This invariant *predicts* the ⁴He-locality
  already **measured** by the pairwise ceiling (spike at A=4, →0 by A=6, matching
  `super× = 0.94` at ⁶Li). Proving it **justifies a narrow probe** (compute the
  single `[1⁴]` connected term; check it supplies `2.09×` at A=4 and `0` at A=6)
  rather than a wide scan.
- **Caveat (not a re-proposal of a refuted item).** `e_A[h₃]` as the **sole
  per-λ weight** already underbinds (2026-06-22). The untried configuration is
  `e_A[h₃]` as the **connected 4-body magnitude term** on top of the combiner —
  a different role, not the refuted weight.

**Lever 2 (weaker, collapses to owner-gated) — A-structured scale
`E₀(A) = m_e·Vol_A/ℏ_q²` via a per-link hyperbolic volume.** Requires a
canonical-knot-ID selecting a *unique* hyperbolic link per A
(`conj:canonical-knot-id-sdp`, #604 / R5-full). Braid closure is dead
(2026-07-04), `Vol₄=8.046` unverified, A≤3 IDs deprecated — **not clean at the
formalize-first level**; folds into the owner-gated Subgoal-2 SDP.

## 4. Anti-duplication flags (do NOT re-propose)

- **Additive / log linked-cluster** → DONE (2026-06-23; DV/complete ⁴He +1.07%
  but overshoots light atoms; scope-(a)).
- **Chirality sign for the 3-body combiner** → DONE (2026-06-24; sign solved,
  magnitude 10–24× short).
- **Extend KL to `S₆/S₁₂` for Betti magnitude** → PRUNED (KL positivity,
  `deltaSign_mixed` Lean; `B_λ` not cell-invariant; ⁴He ceiling ~11 MeV).
- **q-modular / Eisenstein / Klein / Bring** → REFUTED T9–T14 (`q→1` divergence,
  scope-(b)).
- **Per-knot Vol convention / q-dim convention** → REFUTED T2 / hidden-DOF Rule-14.
- **"10³ color-tube" / "`B_(10,2)=584` closes A=4"** → UNSUBSTANTIATED numerology
  / single-partition scalar (the full 77-partition sum is 5.55 MeV).

## 5. Bottom line + recommended next step

At the formalize-first level there is essentially **one** genuinely-untried lever
with a clean provable gate: the connected 4-body **`[1⁴]` SU(4)-supermultiplet
Ursell cluster**, gated on the **`e_A[h₃]` `A>4` vanishing** (degree / orbit-count).
It is attractive precisely because that invariant *explains the ⁴He-locality
already measured* by the pairwise ceiling. Every other structural attack is tried
scope-(a), Lean-proved scope-(b), or collapses into the **owner-gated s5-so3 `W_λ`
keystone / canonical-knot-ID SDP (#604)** for the absolute magnitude.

**Recommended next unit (a subsequent session):** prove the `e_A[h₃]` `A>4`
vanishing as a sorry-free Lean lemma (degree/orbit-count, generic `R` per §7c);
*only if it holds*, run the single narrow `[1⁴]`-connected-term probe at A=4 and
A=6 and record the scope-(a)/(b) verdict. Do **not** run the wide combiner scan
before the gate.

## 6. Cross-references

- Gate trio (landed on main): `QOU/MassTheory/TraceConventionGate.lean` (I-1/I-6),
  `QOU/MassTheory/BarParityExclusion.lean` (I-2).
- `docs/scope/2026-07-02-gap-a4-perknot-density-rule-scoping.md` — the §I-1…I-6
  formalize-first invariants (**on PR #3205's branch `claude/stalled-agent-mg3lij`;
  not yet merged to main**).
- `docs/coordination/option-e.md` — PROBE 2 / A=4 non-closure rows.
- `docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md`.
- Probe scripts: `computations/option_e_a4_full_reconciliation.py` (the −80.4% /
  ×5.10 sum) and `computations/a4_interface_*.py` in the `computations/` root;
  the 17 T-probes `computations/probes/gap_a4_T2_per_knot_vol_probe.py` …
  `computations/probes/gap_a4_T18_markov_normalization_probe.py`, the
  `computations/probes/interface_*_probe.py` family, and
  `computations/a_operator/*.py`.
- `docs/coordination/s5-so3-keystone.md` — the geometric `W_λ` route (class C).
  Its hard core (G1, the S³/2I Seifert–CS index) is **owner-gated** (narrow
  2026-06-22 reversal); PRs #2524/#2503/#2603 are *active unmerged* attacks that
  supply candidate index mechanisms — none *owns*/closes the gated object.
