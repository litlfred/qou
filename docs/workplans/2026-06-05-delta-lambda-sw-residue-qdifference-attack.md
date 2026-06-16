# Closing the step-9 derivation gap — SW-residue / jet-filtration / q-difference

**Deep analysis + three-legged workplan (paper · compute · Lean).**
**Goal:** close the last open box of the canonical chain (cheat-sheet **step 9b**, A≥3 binding), and **promote the cheat sheet to a paper appendix** with a reader-ordered story.

**Status:** design captured + corpus-grounded; framing reconciled against cheat-sheet §9.3 (2026-06-02/03); formalize-first lemmas stated; **no probe launched**.
**Owner direction:** 2026-06-05 session (litlfred).
**Disciplines obeyed:** *formalize-first* (state the invariant before the scan), *corpus-grep* (inventory before declaring open), *no-7th-fit* (the closure is a **derivation**, not a per-partition fit — see §6).

---

## 0. TL;DR — the one-paragraph thesis

The pre-archimedean chain (steps 1–8) is settled; the only open box is **step 9b: A≥3 binding**. The cheat-sheet §9.3 audit (2026-06-02/03) **dissolved the old "Δ_λ density" framing**: binding is an **additive many-body series** `B(K)=Σ_b B_b`, not a per-block weight. This workplan's thesis is that **the many-body series *is* the jet-order filtration** — body-order `n` = vertical/jet degree `n` = the `n`-th prolonged Seiberg–Witten differential `λ_SW^(n)` (already in the corpus, `mi-sw-abelianisation`). Each `n`-body term is then **a Seiberg–Witten period = an algebraic residue sum over the *hyperbolic* link-components** (non-hyperbolic components contribute `Vol=0`, the magic-A 8G being the 4-body hyperbolic term). The per-order terms **and** the open "scale rule `ρ·A`" are **determined, not fitted**, by a **q-difference equation on the binding generating function** (fibre-level; = flatness/abelianisation of the SW connection), which **post-archimedean (after `τ`) becomes a Dirac-type PDE**. Validation is the **γγ / Breit–Wheeler** regime-switch (`SW+Frob` for A≤2 → `BW+χ` for A≥3), the C-even mirror channel tied to the bar-odd difference observable. Closing this completes step 9 ⇒ the chain is end-to-end ⇒ the cheat sheet becomes a clean paper appendix.

---

## 1. The reader-ordered story (topic breakdown)

This is the order the **paper appendix** should present it — each topic is one section.

1. **Three calibrations → substrate `q₀`.** `m_e`, `m_μ/m_e`, `m_π`; `Q_β` derived. *(settled — cheat-sheet §1, §8)*
2. **Pre-archimedean chain → Markov trace.** Steps 1–8: cat action → Stokes/Hecke → Markov → Bring χ=−6 → Wedderburn `tr_M=Σ_λ y_λ χ^λ` → Frobenius → GB-filtration → jet order. *(settled; Lean debt L-1/L-2/L-3 only — §4.C)*
3. **Step 9 splits in two.** **9a** mass `m(K)=m_e·VolDensity(K,q₀)` (per-knot wire-up gap); **9b** binding. *(9a = known wire-up bug; 9b = the frontier)*
4. **Binding is extensive, the trace-difference is intensive.** The canonical `B=E_0(|tr_M^free|−|tr_M^atom|)` saturates (~3–4 MeV); physical binding ∝ A. ⇒ an **additive many-body series** is structurally required (not a density). *(cheat-sheet §9.3)*
5. **The many-body series = the jet-order filtration.** `B(K)=Σ_n B_n`, body-order `n` = vertical degree `n`. 2-body (pairwise bonds, A≤3 derived), 3-body (A=3 residual, open), 4-body (magic-A `2m_e·A·8G`, +5.87%). *(this doc's central identity)*
6. **Each term is a Seiberg–Witten period = residue sum.** `B_n = m_e·Σ_p Res_p λ_SW^(n)` over **hyperbolic** link-components; `λ_SW^(n)` is the `n`-th prolonged SW differential (`mi-sw-abelianisation`); the residue theorem on `S_c≅P¹` makes the period algebraic. *(Lemmas L1, L2)*
7. **The hyperbolicity gate.** Not all operators induce hyperbolic knots: torus/Seifert components give `Vol=0` (`D(z)=0`), so the SW-integral and Vol channels diverge there — this is the per-component bookkeeping as we split by Wedderburn block. *(Lemma L4)*
8. **The constraint that determines the terms: a q-difference equation → PDE.** The binding generating function `G(x;q)=Σ_n B_n x^n` satisfies a fibre-level q-difference equation (flat abelianised SW connection / Habiro recursion); under `τ` at real `q₀` it becomes the **Dirac/SW PDE**, fixing both the per-order terms and the scale rule `ρ·A`. *(Lemma L3 — the load-bearing piece)*
9. **Two-level decomposition.** Jet/body-order `n` **first**, Wedderburn partition `λ` **within** each term — the per-`λ` q-Reeb phase `θ_λ` is carried (not collapsed) until `τ`. *(cheat-sheet §9.2 "observe last")*
10. **γγ validation.** Breit–Wheeler regime-switch at A≥3; bar-even (C-even γγ) vs bar-odd (difference) split must reproduce. *(Lemma L5)*
11. **Chain closed ⇒ appendix.** Step 9 box flips to derived; the cheat sheet's narrative (minus coordination/backlog) becomes the appendix.

---

## 2. The unifying identity chain (load-bearing synthesis)

$$
B(K)\;=\;\sum_n B_n
\;=\;\sum_n m_e\!\oint_{\mathcal{S}_c}\!\lambda_{\mathrm{SW}}^{(n)}
\;=\;\sum_n m_e\cdot 2\pi i\!\!\sum_{p\,\in\,\mathcal{S}_c^{\mathrm{hyp}}}\!\!\operatorname{Res}_p\lambda_{\mathrm{SW}}^{(n)},
\qquad \mathcal{S}_c\cong\mathbb{P}^1(\mathbb{C}),
$$

with the generating function `G(x;q)=Σ_n B_n x^n` satisfying `G(q x;q)=R(q,x)·G(x;q)` (fibre), whose `τ`-image is the Dirac/SW PDE. The Wedderburn refinement is `B_n = Σ_λ B_{n,λ}`, `B_{n,λ}` carrying the per-block `θ_λ` until `τ`.

- `n=0`: electron period `a_D^{(e)}` (base scale).
- `n=2`: pairwise bonds (deuteron base case, derived).
- `n=4`: magic-A whole-α (`8G` Borromean L6a4, hyperbolic — +5.87%).
- **Scale rule `ρ·A`** = how the residue weight grows with body-order `n` — *output* of the q-difference recursion, not an input.

**Why this is the right tool for §9.3's open items:**

| §9.3 open item | This framework supplies |
|---|---|
| (i) canonical **link-volume assignment** per nucleus | the hyperbolic components of `S_c` at body-order `n` (L4); magic-A `8G` is the n=4 instance |
| (ii) the **scale rule `ρ·A`** (ρ=1 at A=2, 2A at A=4) | the residue-weight growth fixed by the q-difference recursion (L3) |
| (iii) **reconcile** 2-/3-/4-body into one additive series | the jet-order filtration *is* the body-order grading (§1.5); one generating function `G` |

---

## 3. Corpus inventory (what exists vs what's missing)

Sources: background corpus trace (2026-06-05) + direct reads of `mi-sw-abelianisation*`, cheat-sheet §9.

| Leg | Status | Key files |
|---|---|---|
| SW differential **already jet-graded** `‖MI∫‖_{J^n}=|a_D^{(n)}|=|∮λ_SW^{(n)}|` | **present** | [`mi-sw-abelianisation.md`](../../content/quantum-observable-universe/brings-surface/mi-sw-abelianisation.md), [`-proof.md`](../../content/quantum-observable-universe/brings-surface/mi-sw-abelianisation-proof.md) |
| Many-body series (2/3/4-body), magic-A `8G` | **present** (audits) | cheat-sheet §9.3; [`2026-06-02-binding-many-body-ceiling.md`](../audits/2026-06-02-binding-many-body-ceiling.md), [`2026-06-02-he4-binding-canonical-vs-full-theta-design.md`](../audits/2026-06-02-he4-binding-canonical-vs-full-theta-design.md), branch `he4-jsj-binding-link` |
| Jet-order filtration (grades the **trace**, not yet the per-body terms) | partial | [`mba-step07-gb-filtration.md`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step07-gb-filtration.md), [`mba-step08-jet-prefix.md`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step08-jet-prefix.md), [`jet-planck-steps.md`](../../content/quantum-observable-universe/information-theory/jet-planck-steps.md) |
| Hyperbolic vs non-hyperbolic | partial — volumes cached, **no per-knot hyperbolicity flag** | `qou-mass/.../knot_volumes.py`, [`climax-volume-mass/`](../../content/quantum-observable-universe/climax-volume-mass/), [`unmapped-torus-knots.md`](../../content/quantum-observable-universe/predicted-spectra/unmapped-torus-knots.md) |
| γγ / Breit–Wheeler / bar-involution | **present** | [`breit-wheeler-vertex.md`](../../content/quantum-observable-universe/mass-theory/breit-wheeler-vertex.md), [`q-beta-gamma-gamma-canonical-derivation.md`](../../content/quantum-observable-universe/stochastic-mechanics/q-beta-gamma-gamma-canonical-derivation.md), [`bar-involution.md`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md) |
| q-difference equation (form stated, kernel open) | scaffolding | [`q-beta-c-k-recursion-from-habiro-q-difference.md`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md), [`habiro-pochhammer-bridge.md`](../../content/quantum-observable-universe/braids-and-knots/habiro-pochhammer-bridge.md) |
| Fibre vs archimedean (`τ`) wall | **fully formalised** | [`kashaev-as-archimedean-realization.md`](../../content/quantum-observable-universe/mass-theory/kashaev-as-archimedean-realization.md), [`tau-all-orders-bridge.md`](../../content/quantum-observable-universe/mass-theory/tau-all-orders-bridge.md) |
| Dirac operator / spinor | mostly absent (S₅/Bring present, Dirac conjectural) | [`n-v-bring-action.md`](../../content/quantum-observable-universe/observations/n-v-bring-action.md) |
| Residue program (not yet tied to λ_SW) | present | [`2026-06-04-residue-a-unblock-kernel-scope.md`](../audits/2026-06-04-residue-a-unblock-kernel-scope.md), `atomic_chirality_residue.py`, `term6_full_pole_sum.py` |
| per-λ `θ_λ` carrier (un-collapsed) | **present** | [`binding_reeb_phase_decomposition.py`](../../computations/binding_reeb_phase_decomposition.py) |
| operator-valued combiner (additive series host) | in-flight | #1698 (m_avg combiner) |

**Owner checks (verified 2026-06-05):** (1) SW period via algebraic residues — machinery live (residue `A`, fibre-level, dual/shadow-price) but **not yet identified with `∮λ_SW^(n)`** → Lemma L1. (2) SW = decomposition of `τ` — **yes structurally** (jet prolongation `J^nE`, n=0 electron period) but the explicit `τ`-identification is unwritten → Lemma L2.

---

## 4. Three-legged workplan

### 4.A Paper (content blocks + the appendix promotion)

**New / edited content blocks** (each `.ts`+`.md`, `.lean` where the kind requires):

| # | Block | Kind | Where | Content |
|---|---|---|---|---|
| P1 | `prop:binding-manybody-eq-jet-filtration` | proposition | `appendix-mass-binding-algorithms/` | the central identity: `B(K)=Σ_n B_n`, body-order = vertical/jet degree; supersede the "Δ_λ density" language |
| P2 | `prop:sw-period-residue-sum` | proposition | `brings-surface/` | `∮_{S_c}λ_SW^(n)=2πi Σ Res` on `P¹` (Lemma L1) |
| P3 | `thm:jet-sw-tau-decomposition` | theorem (cond.) | `brings-surface/` | `τ(MI∫)=Σ_n a_D^(n)=Σ_n ∮λ_SW^(n)` (Lemma L2) |
| P4 | `prop:binding-genfun-qdifference` | proposition | `mass-theory/` | `G(qx)=R(q,x)G(x)` ⇒ residue recursion; post-`τ` Dirac/SW PDE (Lemma L3) |
| P5 | `prop:hyperbolicity-volume-gate` | proposition | `climax-volume-mass/` | non-hyperbolic components ⇒ `Vol=0` ⇒ no SW-residue contribution (Lemma L4) |
| P6 | `rem:gammagamma-binding-validation` | remark (`interprets` P4) | `observations/` or `stochastic-mechanics/` | BW regime-switch bar-even/odd split = γγ validation (Lemma L5) |
| P7 | **Mass-and-Binding-Algorithms appendix sync** | `alg:` blocks | `appendix-mass-binding-algorithms/` | update `mba-step08-jet-prefix`, `mba-chain-map` to carry per-body terms (STRICT per CLAUDE.md appendix-sync rule) |

**Appendix promotion (the cheat-sheet → paper appendix):**
- The paper already has [`pre-archimedean-derivation-chain.md`](../../content/quantum-observable-universe/braids-and-knots/pre-archimedean-derivation-chain.md) (steps 1–8). Extend it (or add a sibling `archimedean-derivation-chain` block) to render the **now-closed step 9** = the many-body/SW-residue story (§1 reader order).
- Port the cheat-sheet's **chain diagram + step table + bibliography** (§1, §2, §6 of the cheat sheet) into appendix prose; **leave behind** the coordination table (§0), Phase-5 findings (§3), and migration backlog (§5) — those stay in `docs/` (not paper voice).
- Add a one-line cheat-sheet → appendix cross-link both ways.

### 4.B Compute (wire-ups + witnesses)

| # | Task | File(s) | Witness |
|---|---|---|---|
| C1 | **Per-knot `VolDensity(K,q₀)` wire-up** (step 9a, the standing 64-script uniform-Vol bug) | migrate `mass_table_comprehensive.py:208` + 63 others off `vol_density_borromean(q)` to `vol_density_per_block(vol_K, tr_M_K, q)` per `atom_braid_word_3A` | refresh `mass-table-comprehensive.witness.json` |
| C2 | **Hyperbolicity flag + per-component `Vol`** | extend `knot_volumes.py` with `is_hyperbolic(K)` + `vol_components(link)`; `D(z)=0` for torus/Seifert | new `link-component-volumes.witness.json` |
| C3 | **Many-body series enumerator** | extend operator-valued combiner (#1698) to emit `B(K)=Σ_n B_n` with body-order `n`; reconcile 2-body bond-sum + 4-body magic-A | `binding-manybody-series.witness.json` |
| C4 | **SW-period residue computation** tied to `λ_SW^(n)` | new `sw_period_residue.py`: `∮λ_SW^(n)` as residue sum over hyperbolic components; cross-check vs `binding_reeb_phase_decomposition.py` `θ_λ` carrier | `sw-period-residue.witness.json` |
| C5 | **q-difference kernel `R(q,x)` extraction** | extend `habiro_ladder_bridge.py`: extract depth-`d` recursion of `B_n`; test `F(q)=λ_SW` hypothesis | `binding-qdifference-kernel.witness.json` |
| C6 | LP/SDP **duals** on every selection in C3/C4 | route through `lp_dual_solver.py` (CLAUDE.md LP-dual rule) | dual fields in each witness |

All long computes follow the `-u … | tee /tmp/<script>.log` discipline.

### 4.C Lean formalization

**New lemmas (this attack):**

- **L1** `QOU.Brings.sw_period_eq_residue_sum` — residue theorem on `S_c≅P¹` for the meromorphic `λ_SW^(n)`. *(Mathlib has `Complex` residue calculus — feasible.)*
- **L2** `QOU.Brings.jet_sw_tau_decomposition` — `τ`-image = `Σ_n a_D^(n)`; **conditional** on the MI-abelianisation class (§3b-cond).
- **L3** `QOU.Mass.binding_genfun_qdifference` — `G(qx)=R(q,x)G(x)` ⇒ depth-`d` linear recursion on `B_n` (mirror of the existing `c_k` recursion in `q-beta-c-k-recursion`); the `F(q)=λ_SW` identification is the open class instance.
- **L4** `QOU.Volume.nonhyperbolic_vol_zero` — torus/Seifert ⇒ `Vol=0` (reuse `QOU.Kashaev.VolumeConjecture` Vol=0 ⇒ sub-exponential `|J_N|`).
- **L5** `QOU.Mass.gammagamma_bar_split` — bar-even/odd projection reproduces the BW C-even vs difference channel (reuse `alpha-em-habiro-bar-involution` bar-fixed structure).

**Standing chain debt to discharge alongside (cheat-sheet §9.4):**
- **L-1** Schur character-orthogonality ⇒ `y_λ` uniqueness (`QOU.Hecke.Wedderburn`).
- **L-2** central-idempotent orthogonality `π_λπ_μ=δπ_λ`.
- **L-3** per-λ Frobenius block-orthogonality.

*(All `sorry` carry `-- Ref:`; route the debt under the proof-integration-watcher queue; lake-enabled session.)*

---

## 5. Sequencing (formalize-first; don't skip to a scan)

1. **P1 + P2 + L1/L2** — state the identity + residue/`τ` lemmas (pure structure, low risk, Lean-stubbable now).
2. **C2 + C4** — hyperbolicity flag + SW-period residue compute; cross-check vs the existing `θ_λ` carrier.
3. **C3** — many-body enumerator on the deuteron (n=2 base) then ⁴He (n=4 magic-A) — *reproduce the +5.87% no-fit number first*, as a regression anchor.
4. **P4 + L3 + C5** — the crux: identify `F(q)=λ_SW`, extract `R(q,x)`, derive the scale rule `ρ·A`. **Formalization, not a numerical sweep.**
5. **C1** — per-knot `VolDensity` wire-up (9a) — independent, can parallelize.
6. **P6 + L5 + C-validation** — γγ/BW bar-split cross-check (A≥3).
7. **Appendix promotion (4.A)** — only once step 9 box is green.

**Falsifiable kill-switch:** if step 4 cannot identify `F(q)=λ_SW` (or the derived `ρ·A` disagrees with the magic-A +5.87% anchor), the attack fails cleanly — a structural negative, not absorbed into a fit.

---

## 6. Why this is not a 7th fit (discipline)

The six refuted ansätze fit per-partition *constants*; the §9.3 audit proved no per-block weight can turn an intensive quantity extensive. This attack is **structurally different**: binding is an **additive many-body series** whose terms are **Seiberg–Witten periods = residues of a meromorphic differential constrained by a q-difference equation**. The term values are *determined* by L1 (residue theorem) + L3 (recursion) + L4 (hyperbolicity gate). The only open *input* is the categorical identity `F(q)=λ_SW^{fibre}` — a **derivation**, falsifiable against the magic-A anchor — not a free parameter. The scale rule `ρ·A` is an **output** of the recursion, not a fitted `C_knot`.

---

## 7. Coordination (siblings)

- **`he4-jsj-binding-link`** (magic-A 4-body `8G`) — this workplan's n=4 term; coordinate the enumerator (C3) so it reproduces that branch's +5.87%.
- **#1698** (operator-valued combiner) — the host for the additive series (C3).
- **#1871** (this branch's binding-difference `binding_difference_odd`, `ΔB=2B₀sinh θ_B`) — the **bar-odd** observable of L5.
- GAP-A audits (Option E / GAP-A-1 / Path B) — compatible cross-checks, not competitors.

Post intent on the overlapping siblings (per CLAUDE.md coordinate rule) before touching shared compute (`knot_volumes.py`, the combiner, `mass_table_comprehensive.py`).
