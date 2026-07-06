# Binding-energy notation catalogue + disambiguation (2026-06-15)

**Status:** notation/ontology reference. The corpus accumulated **18 distinct
"binding energy" notions**, almost all written as a bare `B` / `B(K)` — a
collision. This doc is the authoritative reference; the concise canonical table
+ the `B_sym`/`B_lin` distinction live in the notation register
(`content/quantum-observable-universe/notation/notation-collisions.md`
§"Binding-energy notions"). Owner decisions (2026-06-15): encode `B_sym`
(exact) vs `B_lin` (linear) as **distinct**, rename `B_canonical`/`B_pred` →
`B_lin`; record here + in the register.

**Notation constraint.** `𝔅` (fraktur B) is **bandwidth** (AGENTS.md §7aa), so
binding stays **plain `B` + systematic subscripts**.

## Full catalogue

| # | Symbol | Definition / formula | Trace convention | Exact/approx | Status | Source |
|---|--------|----------------------|------------------|--------------|--------|--------|
| 1 | `B_AME` | AME 2020 measurement | — (measured) | experimental | **ground truth** | `binding_canonical.py:61` |
| 2 | `B_sym` | `−α ln\|τ_M(K)\|` (log-trace) | Jones–Markov canonical | **exact** symbolic, light A | **kept** | `standard-part-functor.md:117` |
| 3 | `B_qCLT` | `−α Σ_i ln\|V_i\|` | qCLT macroscopic limit | asymptotic, A→∞ | **kept** | `standard-part-functor.md:118` |
| 4 | `B_lin` (was `B_canonical`/`B_pred`) | `Q_β(n)·(tr_M(W_free) − tr_M(W_atom))` | Jones–Markov canonical (signed difference) | **linear truncation** of `B_sym` | canonical compute | `binding_canonical.py:144` |
| 5 | `B_depth` | `Σ_k α_k·[Φ_k(free) − Φ_k(atom)]` | Wedderburn–Frobenius depth grading | exact per-depth; empirical α_k | default compute | `binding_depth_stratified.py:39` |
| 6 | `B_magic` | `2·m_e·A·Vol(L6a4) = 2 m_e·4·8G` (⁴He) | flat magic-A | exact flat | ⁴He canonical (+5.87%) | `2026-06-09-binding-canonical-default-depth-stratified.md:97` |
| 7 | `B_λ` | `m_e·Σ_λ y_λ(q₀)·χ^λ(K)·Δ_λ(K)` | Wedderburn–Frobenius full | exact form; Δ_λ open | Δ_λ-gated | `mba-step09b-per-isotope-binding.md:2` |
| 8 | `B_reeb` | per-rep q-Reeb phase `θ_λ = arccos(χ_λ/d_λ)` | per-representation rotation/growth | diagnostic (no scalar) | exploratory | `binding_reeb_phase_decomposition.py` |
| 9 | `B_endo` | endomorphism tower 1st-order (chirality + writhe) | mass-tower operator-valued | partial (D +0.19% / −9%) | exploratory | `2026-05-28-binding-endomorphism-analogy.md` |
| 10 | `B_block` | `T_1 + T_2`, block factors `v_p,v_n,\|V_inter\|` | interface-knot per-block | fitted block factors | exploratory | `binding_block_multiplicative.py:23` |
| 11 | `B_int` | `Δ_I^K` interface-knot series (Li_2^q) | interface-knot q-shuffle | divergent A≥2 | exploratory | `binding_via_interface_knot.py` |
| 12 | `B_factor_f` | `m_e Σ_λ y_λ χ^λ·f(Z,N)`, f from AME | per-block × empirical f | **fitted** (falsified ⁴He) | exploratory | `binding_factor_f_decomposition.py` |
| 13 | `B_Ksolve` | direct Hoefsmit per-block at H_{3A} | operator-selection LP | exact per-block; gated | status-reporter | `binding_k_solver.py:27` |
| 14 | `B_αshift` | per-isotope ρ₀ (deuteron-pinned) | block-multiplicative + α_shift | fitted ρ₀ | exploratory | `2026-06-13-binding-method-reconciliation...md` |
| 15 | `B_plnc` | Plancherel-weighted `markov_trace_3A` | Plancherel measure w_λ | off-convention | **deprecated** | `mass_at_3A_proper.py:354` |
| 16 | `B_abs` | `m_e Σ_λ y_λ\|χ^λ\|` (double-modulus) | abs-sum of \|χ\| | non-archimedean misuse | **rejected** | `2026-06-09-binding-trace-convention-split.md:19` |
| 17 | `B_bar` | `tr_M(q₀)·tr_M(q₀⁻¹)` (bar product) | bar-involution q→q⁻¹ | underbinds ~10⁴× | **rejected** | `2026-06-09-binding-trace-convention-split.md:42` |
| 18 | `m_λ` | `m_e Σ_□ y_λ\|c(□)\|Δ_λ` (per-partition density) | per-partition Markov weight | exact form; Δ_λ open | merges into `B_λ` | cheat-sheet §9 |

## Mergeable vs genuinely distinct

- **Merge** `m_λ` (#18) into `B_λ` (#7) — same Wedderburn–Frobenius sum, different emphasis (partition weight vs knot).
- **Do NOT merge** `B_sym` (#2, exact log) with `B_lin` (#4, linear): `B_lin` is the *linearization* of `B_sym` (Kashaev `tr_M ~ exp(Vol)`; the scalar `Δtr` is first-order). They differ by the binding deficit
  $$ B_{\mathrm{sym}}/B_{\mathrm{lin}} \approx q_0^{\,5(2A-1)} $$
  — the same `q₀^(5·sites)` exponent derived in `2026-06-14-qlommel-delta-lambda-second-kind-derived-b.md`. The rename `B_canonical`→`B_lin` exists so this identity (and the binding deficit it names) is statable in one line.

## Discipline

- Always subscript `B`. Bare `B` in prose denotes the production `B_lin`.
- `Δ_λ = B_AME / B_lin` (the residual ≈ `q₀^(5·sites)`); the exact target is `B_sym`.
- No 7th `Δ_λ` ansatz (AGENTS.md Δ_λ gate); the rejected/deprecated forms (#15–17) must not be reused.
- **Follow-up (bean):** the *code-level* rename of `B_canonical`/`B_pred` →
  `B_lin` in `binding_canonical.py` + callers is a separate refactor (this doc
  + the register establish the *terminology*; the variable rename is downstream).
