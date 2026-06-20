# Canonical derivation cheat sheet — substrate → observables

**Audience**: math/phys starting grad — a one-page-up map of "where every QOU formula comes from" and "which script computes it". Treats the chain as a cookbook so you don't have to dig through 700+ scripts to find what's canonical.

**Paper-side companion**: [`prop:pre-archimedean-derivation-chain`](../content/quantum-observable-universe/braids-and-knots/pre-archimedean-derivation-chain.md) (the rendered version that appears in the paper). This doc adds the **compute-pipeline mapping**, **Phase 5 findings**, and the **migration backlog** that don't belong in the paper but are essential for code review.

**Highlight to Claude** — referenced from AGENTS.md so any agent picking up final-stage QOU work has the full canonical chain visible.

---

## 0. This is the PRIMARY coordination document for the canonical chain

This cheat-sheet is the **coordination hub for the 11-step substrate→observable
chain**, the same role [`duality-tracker.md`](duality-tracker.md) plays for the
D1–D24 dualities. Every agent working a chain step coordinates **through this
table**: it records, per step, what is **proved** (→ Lean), what is **derived**,
what is **fitted/open**, and **which sibling PR owns the gap**. Update the
relevant row when you open/land work on a step — do not fork a parallel status
doc.

**Coordination infra this plugs into** (the "good infra around this"):

| Layer | Doc | Role |
|---|---|---|
| Chain steps (this doc) | `canonical-derivation-cheat-sheet.md §0/§2` | per-step status + owner PR |
| Dualities used per step | [`duality-tracker.md`](duality-tracker.md) | D1–D24 status + closure paths |
| Per-goal ledgers | `docs/coordination/*.md` | `1ppb-categorical-chain.md`, `1ppq-qbeta.md`, `2026-05-24-low-isotope-mass-anatomy-ledger.md`, `2026-05-22-cheat-sheet-manager.md` |
| Automated watchers | `todos/{proof,canonical,compute,detangler}-*-queue.json` | integration-watcher backlog |
| Precision targets | [`precision-goals.md`](precision-goals.md) | L1 (compute) / L2 (100×) |

**Status legend.** ✅ proved (sorry-free Lean) · 🟢 derived (categorical, no fit) ·
🟡 conjecture-conditional / partial · 🔴 fitted / open gate · ⬜ not started.

### Per-step status + owner index (the coordination table)

| Step | What | Status | Owner gap / active PR |
|---|---|---|---|
| 1. Cat action | `ρ_n: B_n → Aut_C(V^⊗n)` | ✅ proved | — (settled) |
| 2. Stokes → Hecke | `σ_i²=(q−q⁻¹)σ_i+1` | ✅ proved | — (settled) |
| 3. Alexander+Markov | unique `tr_M` | 🟢 derived (Lean `sorry=1`) | proof-watcher: discharge `markov_trace` sorry |
| 4. Bring χ=−6 | 6 ↔ torus knots | 🟢 derived | — (settled) |
| 5. Wedderburn / partitions | `H_n(q)≅⊕_λ M_{d_λ}`, `tr_M=Σ y_λ χ^λ` | 🟢 derived (Wenzl) | — (the per-block frame; everything downstream rides on it) |
| 6. Frobenius pairing + self-duality | `⟨a,b⟩_F`, `Ψ=S²=id` | ✅ proved (D3/D23) | partition-respecting audit (§9 below) |
| 7. GB filtration | `ℓ(w)`-graded, `E_2` collapse | 🟢 derived | — |
| 8. Jet order | jet-prefix → `q→1` limit | 🟡 partial (Lean `sorry=4`) | proof-watcher: `SkewSYT` jet sorries |
| 9a. Mass identity `m_p` | `m_e·VolDensity(K, q₀)` (knot-dependent) | 🟡 +2.89–3.73% gap (production uses uniform `Vol(𝓑₃)` for ALL atoms — the **lack of per-knot `VolDensity(K)` wire-up** is the bug: 64 of 65 atom-touching scripts use only `vol_density_borromean(q)`, so 63 of 65 isotopes (all A ≥ 2) get the wrong Vol(K); see [`vol-usage-audit`](audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)) | **per-knot `VolDensity(K)` wire-up** (NOT λ_scale); #1698 (m_avg combiner), `vol_density_per_block_wiring.py` testbed |
| 9b. Per-isotope binding `B(K)` | **canonical default**: depth-stratified `Σ_k α_k Φ_k(K)` via `binding_depth_stratified_rust.py` — α_k structural (Markov z² at k=2, m_e·8G at k≥4); per-depth ASSIGNMENT empirical. **Trace-canonical baseline** (2026-06-09 reconciliation): `binding_canonical.py` = `E_0·(tr_M(W_free)−tr_M(W_atom))` on the Jones–Markov trace (`markov/markov_trace_canonical`, per `prop:categorical-mass-markov`); other session objects (abs-sum, bar product, matrix-M signed tr_M) are off-convention ([convention-split audit](audits/2026-06-09-binding-trace-convention-split.md), PR #2082) | 🟡 canonical-with-empirical-assignment ([audit](audits/2026-06-09-binding-canonical-default-depth-stratified.md)); D/T/³He undershoots 67-73%, ⁴He -50% (Rust ≡ LR post-regen 2026-06-09); flat magic-A `2·m_e·4·8G` BEATS tower on ⁴He (+5.87%). **Trace-canonical residual is structured**: `Δ_λ(K)=B_AME/B_pred ≈ q₀^(10A−5)` — D exact to 0.01 q₀-units, T −0.07, ⁴He +0.27; ³He −1.40 (Z-dep) — near-match tier, NOT wired ([residual audit](audits/2026-06-09-delta-lambda-canonical-residual.md)) | **derive-or-refute `10A−5`** from W_free vs W_atom crossing/jet bookkeeping (formalize-first); substrate-derive per-depth α_k; reconcile tower ↔ q₀^(10A−5) residual ↔ magic-A flat |
| 10. Confinement SDP | canonical `T_w` | 🟢 derived | LP/SDP duals infra (`lp_dual_solver.py`) |
| 11. β-decay `Q_β` | `\|Δ(net)\|·𝔈₀` | 🟢 derived; `c_k` truncation | `ck-dk-canonical-registry.md` (rung tiers) + `1ppq-qbeta.md` ledger |

**The frontier is step 9** (everything else is settled or proof-cleanup). Two
gaps: **9a** = per-knot `VolDensity(K, q₀)` wire-up (production uses uniform
`Vol(𝓑₃)` for all atoms — +2.89% at p,n grows to +3.73% at ¹²C; root cause
is the Vol-uniform bug per [`vol-usage-audit`](audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)); **9b** = the **Δ_λ**
per-block density (the Track-A blocker). See §9 for the mass=density×volume
framing that unifies them. **9b status sharpened (2026-06-09):** on the
trace-canonical path the whole gap collapses to a near-integer q₀-power,
`Δ_λ(K) ≈ q₀^(10A−5)` (D exact to 0.01) — the open item is now
**derive-or-refute `10A−5`** from the canonical chain's crossing/jet
bookkeeping, not a search over closure ansätze
([residual audit](audits/2026-06-09-delta-lambda-canonical-residual.md)).
**9a flip decision settled (owner, 2026-06-13):** production stays on the
uniform shortcut until the per-A normalisation `R(K)` — the same object as
the 9b ρ/Δ_λ leg — is derived; the flip is a *derivation milestone*, not a
wiring choice, and flip+re-pin is **refuted** (`R(K)` runs 2.3→63× with A;
[decision package](audits/2026-06-13-step9a-flip-decision-package.md)).
Do not re-litigate per-knot production flips against this gate.

> ## ⚠ Critical framing — do NOT treat `λ_scale` as a separate object
>
> **`λ_scale` was ABSORBED into `VolDensity(K)` on 2026-05-23 (commit ffdd84409).** The numerical factor that older docs call `λ_scale` is *what the canonical `VolDensity(K)` evaluation produces per knot/link*. It is **not** a separate constant to derive, calibrate, or "close". There is **one** canonical mass formula:
>
> ```
> m(K) = m_e × VolDensity(K, q₀)
> ```
>
> per `prop:geom-universality`. `VolDensity` is **knot-dependent** — each atom's canonical K (proton 𝓑₃, deuteron β_D via `atom_braid_word_3A(1,1)`, etc.) gets its own `VolDensity(K, q₀)` evaluation. For the proton specifically, `VolDensity(𝓑₃, q₀)` factors as `(Vol(𝓑₃)/ℏ_q²) · linking_weight(q)` — but the linking weight is **part of Geom**, not separate. The current categorical computation gives m_p ≈ 965 MeV (+2.89%); the open R&D is **per-knot wire-up of `VolDensity(K)` across all atoms** (production uses `vol_density_borromean(q)` uniformly for ALL atoms — the Vol-uniform bug per [`vol-usage-audit`](audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)), not "refining `VolDensity(𝓑₃)`" alone. The Yekutieli per-cell route was briefly tried in production then PURGED 2026-05-24 (71d674da1) as non-canonical.
>
> See [`lambda-scale-absorbed-into-vol-density.md`](lambda-scale-absorbed-into-vol-density.md) for the canonical reference, including the numerical demonstration that no standard invariant produces 2.46 directly and the full list of refuted alternative derivations.
>
> Original numerical discussion: [`coordination/2026-05-23-algebraic-geometric-observable-consistency.md`](coordination/2026-05-23-algebraic-geometric-observable-consistency.md) §"λ_scale is NOT a separate object — it's what VolDensity produces".
>
> Agents recurrently rediscover and re-frame "λ_scale closure" as if it were the open problem — it is not. The problem is per-knot `VolDensity` refinement.

---

## 1. The chain in one diagram

```
            ┌─────────────────────────────────────────┐
            │  3 calibration inputs (only)            │
            │   m_e ─── leptonic scale (CAL-1)        │
            │   m_μ/m_e ─── fixes q_0 (CAL-2)        │
            │   m_π ─── chiral/Goldstone scale (CAL-3)│
            │   [Q_β derived from CAL-1+CAL-2]       │
            └─────────────────────────────────────────┘
            (phys-obs precision anchor: q_0 on m_p/m_e, re-pin 2026-05-28)
                            │
   step 1. Cat action  ↓  ρ_n : B_n → Aut_𝐂(V^⊗n) via R-matrix
                            │
   step 2. Stokes (Yekutieli)  ↓  σ_i² = (q − q⁻¹)σ_i + 1
                            │           (curvature 2-form ⇒ Hecke relation)
                            ▼
                       𝐇_n(q)  ─── Iwahori-Hecke algebra
                            │
   step 3. Alexander+Markov  ↓  knot ⇄ braid closure, unique trace tr_M
                            │
   step 4. Bring χ=−6  ↓  6 basis elements ↔ 6 torus knots ↔ particle content
                            │
   step 5. Wedderburn  ↓  𝐇_n(q) ≅ ⊕_{λ⊢n} M_{d_λ}(ℚ(q)),  Σ-rep over partitions
                            │
   step 6. Frobenius pairing  ↓  ⟨a,b⟩_F = ∫_A(a·b);  𝔪 = |∫_A ρ(β)| = |tr_M(𝓑_K)|
                            │
                            │  Markov-trace formula (Wenzl bridge):
                            │     tr_M(β) = Σ_λ y_λ(q) · χ^λ(β)
                            │           ↑           ↑
                            │     Wenzl weights    Hecke characters
                            │     (uniquely         (Hoefsmit
                            │      determined)      seminormal)
                            ▼
   step 7–8. GB-NF / jet  ↓  E_∞ = ⊕_λ M_{d_λ}(ℚ(q)); collapse at E_2 ⇒ finite-slice
                            │
                            ▼  T_w canonical, GB-NF ground truth
                            │
   step 9. Archimedean realization  ↓  τ : 𝐂 → Vec_ℝ at q = q_0
                            │
                            ▼
        B(𝔥) = m_e · ρ · [|tr_M(T_w)| + tower(T_w) + tr_M(C_{dim_q})] |_{q=q_0}
                            │
   step 10. Confinement SDP  ↓  selects canonical T_w
                            │
   step 11. β-decay Q  ↓  Q_β = |Δ(net(T_w))| · 𝔈₀
                            │
                            ▼
                    OBSERVABLES (MeV):
                    m_p, m_n, m_He, B_AME(K), Q_β, half-lives
```

Every arrow lives in $\mathbb{Q}(q)$ until the Archimedean functor in step 9. No fitting, no empirical nuclear-physics constants, no analytic limits in the pre-Archimedean chain.

---

## 2. Step-by-step: math + reference + compute script

| Step | Math | Key prop / paper ref | Canonical compute script | Witness |
|---|---|---|---|---|
| **1. Cat action** | $\rho_n: B_n \to \mathrm{Aut}_\mathbf{C}(V^{\otimes n})$ via R-matrix | `prop:braid-action-tensor` | `hecke_core.py` (σ_i seminormal matrices) | — |
| **2. Non-abelian Stokes** | Hecke quadratic $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ as curvature 2-form | `prop:hecke-spectral-sequence`, [yekutieli2015] | `hecke_core.py`, `hecke_character_symbolic.py` (Hoefsmit + Hecke) | — |
| **3. Alexander+Markov** | Unique trace $\mathrm{tr}_M$ invariant under braid + stabilization moves; $J_K(q) = \mathrm{tr}_M(\beta)$ | `thm:jones-markov-trace`, [jones1987] | `hecke_characters.chi_lambda_braid`; `pyhecke_native` (Rust) | per-witness. $\mathrm{tr}_M(\beta_{\mathrm{Bor}})$ closed form **Lean-proved** (`BorromeanMarkovTrace.lean`, modulo cited $V$). **Cross-method checkpoint:** the *narrative-only* per-rep $\chi^\lambda(\beta_{\mathrm{Bor}})$ ($\chi^{(3)}{=}\chi^{(1^3)}{=}1$, $\chi^{(2,1)}{=}2{-}3h^4{-}h^6$) confirmed numerically to $\le 4\mathrm{e}{-}50$ by the skein-validated seminormal engine (`borromean-chi-independent-crosscheck`; proof-status audit [`2026-06-07`](audits/2026-06-07-borromean-chi-crossmethod-proof-status.md)) |
| **4. Bring χ=−6** | $\dim H_3(q) = 6 = $ # embeddable torus knots in $\Sigma_4$; particle content fixed | `prop:x5-bring-weight-identification`, `prop:spectral-sequence-h3-explicit` | `hecke_core._PROTON_G0/G1`, `_NEUTRON_G0/G1` (canonical H_3 chains) | — |
| **5. Wedderburn + partitions** | $H_n(q) \cong \bigoplus_{\lambda \vdash n} M_{d_\lambda}(\mathbb{Q}(q))$; $\mathrm{tr}_M = \sum y_\lambda \chi^\lambda$ | `prop:alpha-k-derivation-procedure`, [wenzl1988] §1 | `y_lambda_wenzl_bridge.py` (numeric + symbolic); **3-axis (K, λ, A) derived-χ catalogue** [`derived_chi_catalogue_sweep.py`](../computations/derived_chi_catalogue_sweep.py) (PR #1952) — pre-emits $\chi^\lambda(\beta_K)(q)$ as exact q-Laurent for every production atom × every partition; backed by `pyhecke_native.chi_q_via_gp` (Rust Geck-Pfeiffer, GIL-released v0.9.0) | `y-lambda-at-q0.witness.json`; `derived-chi-catalogue.witness.json` |
| **6. Frobenius pairing** | $\langle a, b \rangle_F = \int_A(a \cdot b)$; $\Psi = S^2 = \mathrm{id}_A$ (symmetric); chirality $a_K = 1 + w(K)·h + O(h^2)$ | `def:frobenius-hopf-substrate`, `prop:chirality-writhe-ribbon-derivation` | `chi_lambda_braid` + `tau_M_*` family | various |
| **7. GB filtration** | Filtration by Coxeter length $\ell(w)$; spectral sequence collapses at $E_2$ | `prop:gb-spectral-sequence`, `prop:spectral-sequence-collapse` | `derivation_chain.py` (GB-NF tracker) | per-chain |
| **8. Jet order** | Slice-traversal order = jet-prefix partial order; jet tower → classical limit at $q \to 1$ | `prop:jet-convergence-classical-limit` | `derivation_chain.py` (jet-order log) | — |
| **9. Mass identity** | $\mathfrak{E}_0 = m_e/(q_0(q_0-1)) = m_e c_q^2 \hbar_q$ (lept); $\mathfrak{E}_0 = Q_\beta/|h(h-2)/2|$ (had). $B(K) = m_e ρ \cdot [|\mathrm{tr}_M| + \text{tower} + \mathrm{tr}_M(C_{\dim_q})]$ | `prop:atom-knot-mass-derivation` | `mass_table_ppb.py`, `m_p_borromean_verification_50dps.py`, `mass_formula_6term_mpfr_50dps.py` | `mass-table-ppb.witness.json` |
| **10. Confinement SDP** | $T_w$ canonical from joint mass-tower SDP; $\min \|\mathrm{tr}_M(T_w) \mathfrak{E}_0 - B_\mathrm{tgt}\|$ over GB-NF | `prop:confinement-sdp`, `conj:canonical-knot-id-sdp` | `lp_dual_solver.py`, `knot_operator_lp_selection.py` | `operator-selection-lp.witness.json` |
| **11. β-decay Q** | $Q_{\beta^-} = [\mathrm{net}(T_w^H) - \mathrm{net}(T_w^{H'})] · \mathfrak{E}_0$; free neutron: $\Delta(\mathrm{net}) = h(h-2)/2 \approx -0.1883$ | `prop:neutron-qvalue-symbolic` | `free-neutron-decay.py`, `qbeta_*.py` | `q-beta-*.witness.json` |

---

## 3. Phase 5 findings — what's settled vs open

| Phase | Finding | Status | Impact |
|---|---|---|---|
| **5b** | $\alpha \approx [3]_q^2 \cdot \cosh(h)$ at single-block $|\Delta_\lambda^*|$ level (0.022 % rel.err. at $q_0$) | conjecture, §3b-cond axiomatized | Z-step factor at single-block level |
| **5c.1** | Interface knot factor: $\mathrm{tr}_M(\mathcal{B}_K) / \mathrm{tr}_M(\mathcal{B}_K^{\mathrm{vac}}) = z^{p_+(K)} \cdot (z-h)^{p_-(K)}$ exactly | **PROVED sorry-free** in PR #819 | exact closed form for interface contribution |
| **5g** | Constit-side per-Z step matches $(2q - 1)$ to 0.033 % at $q_0$ | **falsified globally** (PR #842 / #854) — coincidence, not identity | bridge to 5l |
| **5k.1** | Residual against $(2q-1)$ matches $h^5(q_0)$ with c≈1.016 | **falsified globally** (PR #854) — numerical accident at $q_0$ | bridge to 5l |
| **5l** | $\rho_Z^{\mathrm{constit}}(q) = \mathrm{tr}_M^3(\mathcal{B}_p, q)$ exactly | **STRUCTURAL IDENTITY** (PR #854) — mpfr-50-dps precision; derivable from Wenzl §1.7 disjoint multiplicativity | constit-side closure |
| **5l.1** | Closed-form Laurent rationals for $\chi^\lambda(\mathcal{B}_p, q)$ for $\lambda \vdash 3$ | clean χ^λ closed forms (PR #854); y_λ normalization reconciliation queued as 5l.2 | partial closed form for $\mathrm{tr}_M^3(\mathcal{B}_p)$ |
| **5n** | Comprehensive notation refactor: $\beta_K \to \mathcal{B}_K$, $\Delta_I^K \to \bowtie_K$, $\mathbf{E} \to \mathfrak{E}$, $\mathcal{B}(q) \to \mathfrak{B}(q)$, $\tau_M \to \mathrm{tr}_M$ | **MERGED** (PR #853) — register expansions: cal admits Hecke structurals; fraktur admits energies | notation discipline |
| **5o** | Functor disambiguation — $\tau$ (fibre, $\mathbf{C} \to \mathbf{Arch}$) vs $U$ (forgetful, $\mathbf{Arch} \to \mathbf{Vec}_\mathbb{R}$) vs $R \mapsto \mathbb{R}$ realisation (base-ring substitution, not a categorical functor) | doc note added to `notation-collisions.md` | terminology discipline |
| **5q** | Closed-form $\mathrm{tr}_M(\mathcal{B}_K)$ shared utility (`closed_form_tau_M.py`) for production migration; combines Phase 5c.1 + 5l | new branch `claude/phase-5q-pipeline-discipline`; verification witness in progress | unblocks cheat-sheet §5 action #4 |
| **Bind** | A≥3 binding deficit is the **linear truncation** of the boundary holonomy: the scalar Δtr collapses the per-rep **q-Reeb phase** $\theta_\lambda$; binding is carried by $\theta_\lambda$ (Markov-weighted), closing the **A=3 mirror pair (³H, ³He) to 2% with no fit**. μ₀ = m_e/(3(q−q⁻¹)/2) ≈ 1.63 MeV **derived**; q-Hamiltonian rotational energy μ₀·ℏ_q·J_q²(j=n/2) reproduces **B_D to −9% with 0 free params**, A≥3 keeps the per-rep deficit | per-λ "closure" retracted as a C_knot fit; gate is the A≥3 per-rep structure, NOT the scale (PR #1417) | deuteron derived twice; A≥3 narrowed to one structural item |

**Combined Z-step factor at full tr_M level (post-5l + 5c.1):**

$$\frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})} \;=\; z(q) \cdot \mathrm{tr}_M^3(\mathcal{B}_p, q)$$

— exact, no residuals. (`z = 1/(q^{1/2} + q^{-1/2})` from Markov axiom; `tr_M^3(B_p)` from Wenzl disjoint multiplicativity.)

**Full closed-form $\mathrm{tr}_M(\mathcal{B}_K)$ (Phase 5q):**

$$\mathrm{tr}_M(\mathcal{B}_K) \;=\; \mathrm{tr}_M^3(\mathcal{B}_p, q)^Z \cdot \mathrm{tr}_M^3(\mathcal{B}_n, q)^N \cdot \prod_{i \in \bowtie_K} f_i(q),$$

with per-interface factors $f_i \in \{z, \, z - h\}$ for positive ($\sigma$, both p-p and **p-n**) and negative ($\sigma^{-1}$, n-n) interfaces. **Convention finding (Phase 5q v2).** The production marshalling for `chi_lambda_braid` — implemented in [`canonical_braid_marshalling.marshal_to_chi_lambda_braid`](../computations/canonical_braid_marshalling.py) — silently maps the canonical averaged p-n form `(c=1, d=-h/2, gen)` to `(sign=+1, gen)` (the explicit `# averaged → σ convention` line), so `chi_lambda_braid` itself never sees the averaging coefficient. The closed form for production-matching purposes uses $f_{pn} = z$, NOT $z - h/2$. The strict averaged convention (math-correct $z - h/2$) is available as an opt-in via `pn_convention="strict_averaged"` for audit-trail probes; the default in [`closed_form_tau_M.py`](../computations/closed_form_tau_M.py) matches the production marshalling. Verification witness: `closed-form-tau-M-verification-phase5q.witness.json`.

**Geom ↔ tr_M unification (Phase 5p, queued).** The downstream `ω` stage of `prop:hoefsmit-scattering-pipeline` (`braid β → tr_M → J_K(q) → ω → Geom(K) → × m_e → 𝔪`) consumes $J_K = \mathrm{tr}_M(\mathcal{B}_K)$. The Phase 5q closed form gives the input to ω in closed form; verifying that the propagation through ω → Geom(K) matches the canonical mass-table chain is the Phase 5p task (queued, depends on Phase 5q verification landing).

**Bring color-tube weighted averaging — open audit finding (Phase 5q).** The p-n interface "averaging" in the canonical atomic braid is currently the **uniform bar-invariant projection** $\sigma_{\mathrm{avg}} = (\sigma + \sigma^{-1})/2 = \sigma - h/2$ (per [`prop:averaging-resonance-rule`](#prop:averaging-resonance-rule)). However, the owner's intuition — recorded in [`probe_pn_flavor_asymmetry.py`](../computations/probe_pn_flavor_asymmetry.py) and [`probe_per_sheet_flavor_nonin.py`](../computations/probe_per_sheet_flavor_nonin.py) — is that the canonical form should be **Bring color-tube weighted**: each nucleon carries 3 quark color sheets (proton uud → $(\mu_u, \mu_u, \mu_d)$; neutron udd → $(\mu_u, \mu_d, \mu_d)$), and the p-n boundary should average over the 9 color-pair assignments weighted by quark content. Empirically (Scheme 4, per-sheet PL integration on Bring's surface) this reproduces $\Delta m_{n-p}$ to ~0.14% of CODATA. **Status**: this is a research-level open item; substrate H_{3A} compute (where [`closed_form_tau_M.py`](../computations/closed_form_tau_M.py) operates) doesn't carry quark-mass inputs, so the weighted averaging is a downstream/mass-level operation. The module exposes `pn_convention="bring_color_weighted"` as a placeholder that raises `NotImplementedError` with the queue context. Implementing it requires (a) extending the closed form to accept quark-mass inputs, (b) defining the canonical color-sheet ↔ quark-flavor mapping (open per `probe_pn_flavor_asymmetry.py` conclusion: "research-level color-sheet ↔ quark-flavor mapping not explicitly stated in the paper").

**A≥3 binding campaign — summary (PR #1417, 2026-05-29).** Full record:
[`docs/audits/2026-05-28-binding-endomorphism-analogy.md`](audits/2026-05-28-binding-endomorphism-analogy.md) §"A≥3 derivation campaign". Key chain (all derive-or-refute, no AME fit):
1. **Linear-truncation diagnosis** — `tr ~ exp(Vol)` (Kashaev), so the endomorphism's $\Delta\mathrm{tr}$ is the linearisation; exact for the deuteron, saturating for A≥3. Loci: chirality factor first-order ($a_K=1+wh+O(h^2)$); $\sinh(\ln q)$ Coulomb channel discarded by the canonical projection; $[F,F]$=Hecke-quadratic identified-but-unused.
2. **cosh/sinh bridge PROVED** (Lean + paper): $[n]_q=\sinh(n\lambda)/\sinh(\lambda)$ — algebraic q-integer = transcendental hyperbolic sine; cosh=strong / sinh=Coulomb is a theorem, not a fit.
3. **Yekutieli boundary↔surface form assembled** (Step 2 of the pre-archimedean chain).
4. **Binding carrier = per-rep q-Reeb phase** $\theta_\lambda=\arccos(\chi^\lambda/d_\lambda)$: Markov-weighted phase closes the **A=3 mirror pair (³H, ³He) to 2%, no fit**; the scalar $\mathrm{tr}_M$ collapses it. Volume-difference (log/cosh/SnapPy) and Lobachevsky-volume observables **refuted** — binding is *linear* in the angle.
5. **q-Hamiltonian rotational energy with derived μ₀** — μ₀ = m_e/(3(q−q⁻¹)/2) ≈ 1.63 MeV is the framework's per-crossing scale (`universal-ilp-algorithm`); E_rot = μ₀·ℏ_q·J_q²(j=n/2) reproduces **B_D = 2.02 MeV vs 2.225 (−9 %) from FULLY derived quantities (0 free params)** — a second independent deuteron derivation. A≥3 keeps the 44–72 % deficit (the per-rep structure, unchanged).

**Net:** deuteron derived twice (m_e·Vol(𝓑₃)·Δtr at +0.19 % and μ₀·ℏ_q·J_q²(3) at −9 %); A≥3 narrowed to one structural item — the per-rep highest-weight $j=n/2$ collapses the per-block Reeb phase just as the scalar trace does. **μ₀ is derived;** the gate is the A≥3 per-rep structure, not the scale. The per-λ "closure" with a fitted `C_knot=5.852` was **retracted**.

---

## 4. Φ_q (Faddeev) vs Li_2^q (Rogers) — context sorting

The QOU framework uses **two distinct q-dilogarithms**, NOT interchangeable. Confusion between them was a known historical bug (`mass-endomorphism-tower.md` SUPERSEDED banner; stage-1b audit in `126699b8c`).

| | $\Phi_q(z)$ (Faddeev) | $\mathrm{Li}_2^q(z)$ (Rogers) |
|---|---|---|
| **Context** | MASS-anchor compute | BINDING / symmetric-channel compute |
| **Bar-symmetry** | NOT bar-symmetric (carries dimensional mass scale) | bar-symmetric: $\mathrm{Li}_2^q = \overline{\Phi_q}$ under $q \mapsto q^{-1}$ |
| **Active in compute** | 37 scripts (mass-anchor: `mass_*`, `derived_masses`, `proton_*`, `m_p_*`) | 16 scripts (binding-context: `binding_block_multiplicative`, `binding_via_interface_knot`, bar-symmetric tools) |
| **Active in paper** | 133 content blocks | 77 content blocks |
| **Reference** | `prop:li2q-phiq-bar-symmetrization`, [faddeev1996] | [kashaev1995] for the q-deformed dilog series |
| **Stage-1b audit** | ✓ correctly used in 14 binding scripts? **NO** — they're Φ_q-free | ✓ binding compute pipeline is Li_2^q-only (verified `grep -c Phi_q` = 0 across 14 `binding_*.py`) |

**Key identity (Phase 5b):**

$$\mathrm{Li}_2^q(z) \;=\; \overline{\Phi_q(\bar z)} \quad \text{under bar-involution } q \mapsto q^{-1}$$

The two q-dilogarithms are **bar-conjugates** of each other on the substrate $q$. Using $\Phi_q$ in a binding-context script would import the bar-asymmetric (mass) component into a place that should be bar-symmetric — a discipline violation.

**Phase 5b three-layer synthesis (PR #819 §"synthesize"):**

$$\mathrm{Li}_2^q \;\leftrightarrow\; \cos_q(h) \;\leftrightarrow\; \cosh(h)$$

These are **three avatars of the same bar-symmetric kernel** at different levels of detail:
- $\mathrm{Li}_2^q$ — series / motivic level
- $\cos_q(h)$ — phase / oscillatory level  
- $\cosh(h)$ — gain / closed-form level

Pick the right avatar by context — same content, different "lens" on the substrate.

**Where this surfaces categorically** (added 2026-05-24): the torus-knot trace polynomial `P_m(h)` from `tr_M(σ_1^{2m})` reduces to `(q^{2m+1} + q^{-(2m+1)}) / (2[2]_q)`, which at the substrate is `cosh((2m+1)η_0) / (2 cosh η_0)` (hyperbolic avatar) and at a root-of-unity is `cos((2m+1)θ) / (2 cos θ)` (trigonometric avatar). The categorical Weinberg-angle identity `cos θ_W ≈ cosh(5 η_0) / cosh(7 η_0)` (within 1%) is a direct application — see §5 item 5 below.

---

## 5. Compute-pipeline migration backlog (canonical-derivation gaps)

Per the deep review of last 10 days of math improvements (2026-05-20 audit), the following **pipeline-discipline migrations** are queued. The MATH is correct; the COMPUTE has not migrated to the new canonical sources yet.

**Status legend.** ✅ closed · 🟡 in-flight · ⏸️ gated · ⬜ not started.
Tracker last updated: **2026-05-23 (ALL 5 ITEMS CLOSED)**.

| # | Status | Action | Where | Closure / PR |
|---|---|---|---|---|
| 1 | 🟡 | Per-knot `VolDensity(K, q₀)` wire-up (NOT just the proton — all 65 isotopes) | `m_p_borromean_verification_50dps.py` (proton) + `mass_table_comprehensive.py:208` (all 65 — currently `vol_density_borromean(q)` uniform) + 62 other atom-touching scripts (per [`vol-usage-audit 2026-06-02`](audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)) | **PARTIAL.** Closed for the **proton** specifically (#888 + #895 + #1056 — `m_e × VolDensity(𝓑₃, q₀)` via Family-A linking_weight, gives 965 MeV / +2.89%; **no separate `λ_scale`**, absorbed into the Geom functor per 2026-05-23 coord doc). **NOT closed for atoms A ≥ 2**: production uses `vol_density_borromean(q)` uniformly for ALL atoms instead of the canonical knot-dependent `VolDensity(K, q₀)` per each atom's `atom_braid_word_3A`. The per-knot infrastructure exists (`_li_2_q_util.py::vol_density_per_block(vol_K, tr_M_K, q)`; the only consumer is `vol_density_per_block_wiring.py` testbed) but 64 atom-touching scripts haven't migrated. Error budget mirrors the bug: m_p +2.89%, m_n +2.89%, ⁴He +3.65%, ¹²C +3.73%, ⁵⁶Fe +3.86%. The Yekutieli-extended derivation was briefly tried in production (a1f68d5e5) then PURGED (71d674da1) as non-canonical (bijection NEGATIVE per PR #985; Reading A was substrate-q₀ coincidence). Current PROVED categorical at the **proton**: `VolDensity(𝓑₃, q₀) = (Vol(𝓑₃)/ℏ_q²) · λ_A` with `λ_A = 5/2 + (3/4)h²` Family A from H_4 Wedderburn — but extending this per-K is the open work. |
| 2 | ✅ | Migrate 20 importers of SUPERSEDED `mass_endomorphism.py` to the new `mass_tower_operator_valued` API | 2 substantive callers (`mass_at_3A_proper.py`, `pn_alpha_lp_dual.py`) + 15 utility-only (no migration needed) | **Closed by #889 (block-graph hygiene, 15 `.ts` files) + #944 (H_12 Phase-1 extract unblocking) + #960 (scope-correction audit: 20 → 4) + #966 (canonical API surface in `mass_tower_operator_valued.py` + 2-caller migration).** Strict count: only 2 scripts actually called `mass_from_tower(`; 18 utility-only importers consume substrate helpers and need NO migration. Re-export at the canonical block-name location (`new is orig → True`); zero computation change. |
| 3 | ✅ | Wire the Rust LR convention adapter (PR #829) into `atomic_tr_m_*` scripts for A ≥ 3 | `atomic_tr_m_mpfr_50dps.py` + tr_m_wenzl_bridge + `atomic_tr_m_helium4.py` | **Closed by #901 (bridge-level wiring) + #895 (entry-point `--method canonical-rust` flag + 76-90× speedup at A ≥ 3) + #915 (helium4 refactor to Wenzl bridge — 300× speedup at H_3 cross-check, sub-second H_12 expected) + #946 (default-method flip).** Both `atomic_tr_m_*` files now Rust-backed; defaults flipped. |
| 4 | ✅ | Refactor 4 production tr_M scripts to use `tr_M(𝓑_K) = tr_M(𝓑_K^vac) · z^{p_+} · (z-h)^{p_-}` closed form (Phase 5c.1 + 5l) | `binding_canonical.py` (the one true scalar candidate); the other 3 (`atomic_chirality_residue.py`, `atom_level_wedderburn_tower.py`, `binding_depth_stratified*.py`) need per-partition χ^λ which the scalar closed form cannot supply | **Closed by #921 (opt-in `use_closed_form=True` in `binding_canonical.py` via Phase 5q identity; 3.58e-16 vs symbolic at deuteron, 251× faster).** The other 3 scripts use the per-partition Rust wire-up from PR #901 indirectly — they don't need the scalar closed form (scope clarified during the cluster). |
| 5 | ✅ | Add compute verification for the Reeb-flow / Garside closed-form (4 paper-only commits — `b6ed74635`, `88d7934b4`, `172263c6e`, `6ce96b4ce`) | new script `reeb_flow_garside_closed_form_verification.py` | **Closed by #935.** Verifies all six canonical knot operators (identity, σ_1, σ_2, σ_1σ_2σ_1 Garside, σ_1σ_2, σ_2σ_1) reproduce the closed-form trajectory at MPFR 50 dps. 13/13 assertions pass; Garside-thirds use rational ("1/3", "2/3", "1") to avoid f64 truncation. |

### Manager view — what's next (2026-05-24)

**All 5 cheat-sheet §5 migration items are CLOSED.** The "pipeline-discipline migrations" backlog is empty.

> **Framing correction (2026-05-23–24):** there is **no separate `λ_scale` to derive**. The numerical factor previously called `λ_scale` is *what the canonical `VolDensity(K, q₀)` evaluation produces per knot K* — it is absorbed into the Geom functor on a per-knot basis (per `prop:geom-universality` and the 2026-05-23 algebraic→geometric→observable consistency coord doc). The framework's open work is to refine the categorical computation of `VolDensity(K)` **knot-by-knot for each atom** (production currently uses `vol_density_borromean(q)` uniformly across all 65 isotopes — see [`vol-usage-audit`](audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md): 87 scripts uniform, 2 per-knot), not to "calibrate λ_scale". The Yekutieli per-cell variant of `VolDensity` was briefly tried in production (a1f68d5e5) and PURGED on 2026-05-24 (71d674da1) as non-canonical (bijection negative per PR #985). Current canonical at **the proton specifically**: Family A linking-weight inside `VolDensity(𝓑₃, q₀)`; analogous per-knot evaluations for atoms A ≥ 2 are the open wire-up work.
>
> **Per-isotope error budget under the current `VolDensity`:** m_p ≈ +2.89%, m_n ≈ +2.89%, Δ_pn ≈ +2.86%, ⁴He ≈ +3.65%, ⁵⁶Fe ≈ +3.86% — see `mass-table-comprehensive.witness.json` (65 isotopes). This is a **single** error, not a "λ_scale closure gap" — it is the gap between the framework's current `VolDensity` evaluation and the categorically-exact one. Refinements queued below address different routes to that refinement.

The forward work has shifted from §5 mechanics to scientific closure:

1. **Per-knot `VolDensity(K, q₀)` wire-up (canonical formula `m(K) = m_e · VolDensity(K, q₀)`, knot-dependent — NOT a single-knot refinement)**. **2026-06-03 reconciliation**: the prior framing "`VolDensity(𝓑₃, q₀)` refinement" collapsed the canonical knot-dependent formula to its single-knot Borromean instance, mirroring the production-compute bug. Reality (per [`vol-usage-audit 2026-06-02`](audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)): 87 of 89 production scripts use `vol_density_borromean(q)` (uniform `Vol(𝓑₃)`) for ALL atoms; only 2 use per-knot `vol_density_per_block(vol_K, tr_M_K, q)`. 64 atom-touching scripts have the uniform-Vol bug. Error budget mirrors it: +2.89% at p,n grows to +3.73% at ¹²C — this is **the same per-knot wire-up gap, not a single research refinement target**. The PROVED categorical at the **proton** is `VolDensity(𝓑₃, q₀) = (Vol(𝓑₃)/ℏ_q²) · λ_A` (Family-A linking_weight 2.532780, gives 965 MeV); analogous per-knot evaluations for atoms A ≥ 2 use `atom_braid_word_3A(Z, N)` and need their own `Vol(K)` + `tr_M(K)` inputs. Research-grade refinement routes (Yekutieli per-cell curvature, Bring color-tube weighted averaging, Reading-A geometrised form, q-dilog tower) sit ABOVE the per-knot wire-up — refining the proton's `VolDensity(𝓑₃)` while the rest of the table still uses `vol_density_borromean(q)` uniformly is a category error. Any refinement must round-trip the muon (4₁) anchor exactly; the production code uses Family A as the current best PROVED categorical input for the **proton specifically**.
2. **Q_β refinement (research-grade, open).** **2026-06-03 reconciliation**: the prior bullet "the 2026-05-24 dashboard shows it now passes 100×" + "c_3 = -2 = J_Hopf(q=1) categorical-closure-friendly" is **STALE**. Live state per `per-observable-100x-status.witness.json` (2026-06-03): Q_β err = 1279 ppb, **miss = 164×**, `beats_100x = False`. The 2026-05-28 q₀ re-pin (per `docs/audits/2026-05-30-q0-repin-stale-witness-audit.md`) reverted the temporary 2026-05-24 pass. The `c_3 = -2 = J_Hopf(q=1)` framing is itself **flip-flop entry #4** in [`docs/coordination/1ppq-qbeta.md`](coordination/1ppq-qbeta.md) — settled as NEAR-MATCH not Taylor-exact (PR #1593 order audit: the per-block Δtr_M is O(√u) ε¹, ladder c_3 is at u³ ε⁶ — accidental 5-ε-order coincidence). Current keystone: **Q_β Habiro element identification** (the scaling map `f: Δtr_M(√u) ↦ Q_β(c_3 at u³)`). **Currency update (2026-06-10):** per-rung tiers live in [`coordination/ck-dk-canonical-registry.md`](coordination/ck-dk-canonical-registry.md); eliminated methods in the [refuted-class map](audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md) (C1–C12 + 1309-candidate real-q saturation + 4 KLR composite preflights refuted at u², PRs #1914/#1924); the extraction precision floor `σ(c_k) = σ_R/u^k` (PR #1844) proves only c_2, c_3 are data-determined ⇒ c_k≥4 is framework-derivation-only. Open axis: fibre-level kernel `R(q,ξ)`/`Φ₂` (constraints: bar-odd `a_1 = √2·Φ₂`, depth ≥ 3 or non-constant, ζ₄ residue, simple pole at u_substrate). Full state of play: [2026-06-10 synthesis](audits/2026-06-10-qbeta-ck-state-of-play-synthesis.md).
3. **Phase-1b BlochWigner Lake-wiring** (PR #956's roadmap) — Lake-wire `QOU.Archimedean.BlochWigner_unit_circle` into the module tree, then strengthen `BringZeroModeBlochClass` field from `∃ z : ℝ, z = bringZeroModeValue` to `∃ θ : ℝ, BlochWigner_unit_circle θ = bringZeroModeValue`. Closes the literal-rfl loophole. Auxiliary to the `VolDensity` refinement.
4. **L2 100× Subgoal-1 close-out**. **2026-06-03 reconciliation**: live witness shows **3 of 7** observables pass 100× (m_p, m_e, m_K/m_π — the prior "3 of 6" predates the m_K/m_π closure landing). The remaining gaps are **(m_μ, Q_β, m_n, Δ_pn)** — the prior "(m_p, m_n, Δ_pn)" listing is wrong: m_p PASSES (substrate anchor; 0.0004 ppb), and m_μ is a separate gap (209.8 ppb, 963.6× miss — independent μ–p floor, see `docs/audits/2026-06-02-m-mu-pr1556-superseded-by-witness.md`). The (Q_β, m_n, Δ_pn) trio shares a single root cause documented in `docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`.
5. **Electroweak triplet (H/W/Z) torus-knot mass route — RT-chain only.** Higgs = T(2,8), Z = T(2,6), W± = T(2,4) per [`electroweak-higgs-torus-link-triplet.md`](../content/quantum-observable-universe/archimedean-universe/electroweak-higgs-torus-link-triplet.md). T(2, k) is Seifert-fibered with Vol = 0, so the canonical `VolDensity` chain in #1 above does **not** apply directly. Recent results:
   * **Unified binomial pattern (PR #1125 — `torus-knot-h-expansion-pattern.md`):** Every even-h coefficient of `tr_M(σ_1^{2m})` collapses to `c_{2j}(T(2, 2m)) = C(m+j, 2j) / 2`, verified symbolically across 54 cells. This is the lower-level validator for any candidate RT specialization.
   * **Closed cosh form for the trace polynomial — connects to Phase 5b `cos_q ↔ cosh` synthesis (§4 above).** The trace polynomial `P_m(h) = Σ_{j=0}^{m} C(m+j, 2j)/2 · h^{2j}` reduces (sympy-exact across `m = 1..6`) to a single bar-symmetric ratio:
     $$P_m(h) \;=\; \frac{q^{2m+1} + q^{-(2m+1)}}{2\,[2]_q}, \qquad h = q - q^{-1}.$$
     At substrate `q_0 ∈ ℝ_{>0}` set `η_0 = log q_0`: then `q^n + q^{-n} = 2 cosh(n η_0)` and `[2]_q = 2 cosh(η_0)`, so $P_m(h_0) = \cosh((2m+1)\,η_0) \,/\, (2\cosh η_0)$. The trace polynomial is the **hyperbolic-cos avatar** of the bar-symmetric kernel (Phase 5b § "three avatars: Li_2^q ↔ cos_q ↔ cosh"). At a root-of-unity `q = e^{iθ}` it becomes the trigonometric Chebyshev ratio `cos((2m+1)θ) / (2 cos θ)`.
   * **W/Z ≈ cos θ_W within 1% — categorical Weinberg-angle identity (commit `12b6c77c1`).** Combining the previous two bullets, `P_W / P_Z = \cosh(5 η_0) / \cosh(7 η_0)` (no `[2]_q` factor; it cancels). At `η_0 = log q_0 ≈ 0.10416`: `cosh(5η_0) / cosh(7η_0) = 0.8913` vs SM `cos θ_W = m_W/m_Z = 0.8814` — **+1.1% deviation, structurally derived, no empirical fit.** The trigonometric SM Weinberg angle is realised categorically as a *hyperbolic* cosh ratio at the substrate parameter — the substrate `q_0` is close enough to 1 that `cosh((2m+1)η_0) ≈ cos((2m+1)θ_W)` for the small integers in play (`2m+1 ∈ {5, 7}`). The 1% gap is the cosh-vs-cos discrepancy. Better than PR #1122's substrate-point √[2]_q fit (which was 7% per jet under jet-order check) — and now has a clean closed form.
   * **Z/H twist-count ratio is GENUINE.** `J_2(T(2,6))/J_2(T(2,8))` ratio = `6/8 = 0.75` at every jet order matches SM `m_Z²/m_H² ≈ 0.729` within ~3 %. Structurally real per the jet-order validation in commit `aa11d2f06`.
   * **W = √[2]_q STRONG claim RETRACTED** (commit `aa11d2f06`, PR #1122 / PR #1126 jet-order check + retraction audit `1e56c9464`): the substrate-point match was a jet-mixing coincidence, not a structural identity. A single multiplicative W-only correction cannot fix W/Z and W/H simultaneously (they need boosts in opposite directions). The √2 in the framework is implicitly recovering the SM Higgs-VEV doublet convention.
   * **Two-class normalization observation** (commit `12b6c77c1` §"structural-limit"): `mass(GeV) / P_m(h_0)` gives ≈ 143 for W and Z (gauge bosons), ≈ 171 for H (scalar). Reassessed in audit [`2026-05-24-gauge-vs-scalar-mass-factor-derivation-path.md`](audits/2026-05-24-gauge-vs-scalar-mass-factor-derivation-path.md) §5: empirically real but NOT a simple ratio of SM couplings. Three candidate paths (A: substrate-derived `v_VEV`, declined 2026-05-08; B: `g, g'` from categorical SU(2)_L × U(1)_Y; C: `λ/g²` from categorical chain — numerically inconsistent with simple SM combinations). Cleanest defensible statement: the absolute scale + W/H + Z/H ratios remain open.
   * **Lean infrastructure landed** (commit `555587685`, PR #1128 follow-up):
     - `QOU.QuantumObservableUniverses.CategoricalHiggsIdempotent` REFINED with explicit fields (`vev_v_GeV`, `vev_lower_component_GeV = vev_v_GeV / √2`, `gauge_coupling_g`, `gauge_coupling_g_prime`, `higgs_self_coupling`, `cos_theta_W`) and a PROVED theorem `m_W_over_m_Z_eq_cos_theta_W : m_W_GeV / m_Z_GeV = cos_theta_W` (via `field_simp + ring`, conditional on the class). The √2 is now explicit in `vev_lower_component_eq_v_over_sqrt2` — encoding the SM Higgs-doublet convention, NOT a deeper categorical fact (per PR #1126 retraction).
     - `QOU.BraidKnot.TorusKnotMass` (new): scaffolds RT-route mass-derivation with `poly_growth_degree`, `gauge_mass_factor`, `scalar_mass_factor`, `factors_distinct`, `WZ_mass_ratio`. Default instance carries `sorry` (open conjecture per §3b-cond).
     - `QOU.Kashaev.VolumeConjecture` (pre-existing, adaptable): encodes Vol=0 ⇒ sub-exponential `|J_N|`, already captures "torus knots need a different chain".
   * **Three substrate→EW empirical-match hypotheses + scaffolded Lean theorems** (probe `ew_couplings_substrate_derivation_probe.py` + audit [`2026-05-24-ew-couplings-substrate-empirical-matches.md`](audits/2026-05-24-ew-couplings-substrate-empirical-matches.md) + Lean `QOU.BraidKnot.SubstrateEWHypotheses` from commit `f16adbb17`). Probe tested ~50 candidates; three pass the triple test (match < 1%, uses only substrate + universal constants, plausible categorical origin):

     | hypothesis | predicted | dev | structural anchor |
     |---|---:|---:|---|
     | `g = π · h_0` | `π · 0.20856 = 0.6552` vs SM 0.6535 | **+0.26%** | π from connection 1-form integration on substrate (Yekutieli MI machinery; see [`yekutieli-mi-derivation-path.md`](audits/2026-05-24-yekutieli-mi-derivation-path.md)) |
     | `v_framework / v_SM = log(6)` | `log(6) = 1.7918` vs measured `443/246 = 1.8008` | **−0.50%** | 6 = `gsNFBasisCardinalityB3` = `|S_3|` = `dim_ℂ H_3(q)` (PROVED) — order of the 6 GS-NF knot operators (γ, σ_0, σ_1, L_+, L_-, e^-); Chern-Simons-style `log |G|` |
     | `scalar_mass_factor / gauge_mass_factor = 6/5` | `6/5 = 1.200` vs measured 1.196 | **+0.35%** | 6 = `|S_3|` (knot-operator basis); 5 = `partitionsOfFour` = Wedderburn-block count at H_4 ((4), (3,1), (2,2), (2,1,1), (1,1,1,1)) — both PROVED |

     Each hypothesis is encoded in `SubstrateEWHypotheses.lean` as a `class`-conditional `theorem` with a `sorry` marker for the empirical-match step; the structural anchors (`gsNFBasisCardinalityB3 := 6`, `partitionsOfFour := 5`) are PROVED unconditionally. **Epistemic discipline (per `production-vs-exploratory-discipline`):** these are *structurally suggestive empirical matches*, not theorems. The conversion to rigorous identities requires: (a) connection 1-form integration over the substrate loop to derive `π · h_0`, (b) knot-operator partition-function evaluation to derive `log |S_3|`, (c) cross-Wedderburn-block normalization ratio to derive `|S_3| / |Part(4)|`. Research-grade, 1-2 weeks each.
   * Open: prove the 3 structural→empirical hypotheses above (close the `sorry` markers in `SubstrateEWHypotheses.lean`) to upgrade them from "match within < 1%" to "categorical theorem".

### Adjacent open work (not in §5 but cited by the cluster)

- **Tier 1.A 4× gate** (PR #886): ⁶Li wall 84.5 s, target < 60 s. 1-2 day Rust optimisation (FxHashMap intermediate + defer-GCDs in `reduce_laurent`).
- **Tier 1.B orbit reduction** (gates A ≥ 8, ¹²C / ¹⁴N / ¹⁶O — organic chemistry): preflight required (`§4.2` of the handover doc; orbit-trace identity must validate at 1e-25 on ⁴He / ⁵Li / ⁶Li before implementation).
- **Bring color-tube quark-weighted p-n averaging**: closes Δm_{n−p} to ~0.14 % per `probe_pn_flavor_asymmetry.py` Scheme 4. Research-grade — a candidate refinement of the p-n cross-section of `VolDensity`.
- **Complex-$q_0$ categorical lift** (research-grade — PR #1127): the pre-Archimedean substrate is already generic over `{R : Type*} [CommRing R]`; $q_0 \in \mathbb{R}$ is an *engineering / empirical* commitment, not a theorem (audit: [`2026-05-24-q-zero-reality-audit.md`](audits/2026-05-24-q-zero-reality-audit.md)). On $|q| > 1$ with $\mathrm{Im}(q) \neq 0$ the **Lusztig bar** ($q \mapsto q^{-1}$) and the **Hermitian $\ast$** ($q \mapsto \bar q^{-1}$) involutions *split*; the split is the categorical home for any future $\mathrm{Im}(q_0)$ contribution. Note: the dominant 2.89 % L2 gap is **bar-symmetric** (m_p, m_n shift together), so complex $q_0$ is *not* a candidate fix for that gap — VolDensity refinement is. Complex lift is independently valuable infrastructure.

---

## 6. Key bibliography (paper-side BibTeX keys)

| Result | Reference |
|---|---|
| Hecke algebra of type A | `[iwahori1964]`, `[geck-pfeiffer2000]` |
| Iwahori-Hecke quadratic relation as Yang-Baxter | `[jimbo1986]` |
| Markov trace uniqueness + Jones polynomial | `[jones1987]` |
| Wenzl Markov-trace closed form + disjoint multiplicativity | `[wenzl1988]` §1.7 |
| Hoefsmit seminormal representations | `[hoefsmit1974]`, `[ram1991]` |
| Murnaghan-Nakayama for Hecke characters | `[ram1991]` |
| Frobenius pairing / Hopf algebra symmetric structure | `[majid1995]`, `[kassel1995]` |
| Yekutieli multiplicative integration | `[yekutieli2015]` |
| Quantum dilogarithm Φ_q (Faddeev) | `[faddeev1996]` |
| Rogers q-dilogarithm Li_2^q | `[kashaev1995]`, `[kirillov1995]` |
| Macdonald-Schur polynomials | `[macdonald1995]` |
| Bring surface χ = −6 | `[bring1786]`, `[klein1884]` (historical) |
| Gröbner-Shirshov basis (general) | `[bokut2007]`, `[chenhongbo2010]` |

---

## 7. Where to find things (quick index for Claude / future agents)

| Need | Look at |
|---|---|
| The full chain rendered in the paper | [`pre-archimedean-derivation-chain.md`](../content/quantum-observable-universe/braids-and-knots/pre-archimedean-derivation-chain.md) |
| 7 first-principles entry points + trust basis hierarchy | `computations/DERIVATION-CHAIN-METHODOLOGY.md` |
| Canonical-derivation discipline (production scripts) | `computations/derivation_chain.py` |
| q_0 50-dps canonical pin | `computations/q_parameter.Q_50_DIGIT_STR` |
| Wenzl y_λ (numeric + symbolic) | `computations/y_lambda_wenzl_bridge.py` |
| Hecke characters at varying q | `computations/hecke_characters.chi_lambda_braid` (Python + Rust kernel) |
| **3-axis (knot, partition, atom) derived-χ catalogue** | [`computations/derived_chi_catalogue.py`](../computations/derived_chi_catalogue.py) (schema), [`derived_chi_catalogue_sweep.py`](../computations/derived_chi_catalogue_sweep.py) (production sweep), `derived-chi-catalogue.witness.json` (cell witness) — PR #1952 |
| Catalogue parallel backend (auto-detects GIL release) | [`derived_chi_catalogue_parallel.py`](../computations/derived_chi_catalogue_parallel.py) — `ThreadPoolExecutor` when `pyhecke_native >= 0.9.0`, else `ProcessPoolExecutor` fallback |
| Catalogue Tier 2/3/4 optimisations | Tier 4 in-memory memoize: [`derived_chi_catalogue_memoize.py`](../computations/derived_chi_catalogue_memoize.py); Tier 3 bar-symmetry: [`derived_chi_catalogue_bar_symmetry_audit.py`](../computations/derived_chi_catalogue_bar_symmetry_audit.py) (1.9× sweep speedup); Tier 2 M_n disk cache: [`derived_chi_catalogue_mn_disk_cache.py`](../computations/derived_chi_catalogue_mn_disk_cache.py) |
| Catalogue Tier 1 LR factorisation (math + scaffold) | Audit: [`docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`](audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md); Scaffold: [`derived_chi_catalogue_lr_scaffold.py`](../computations/derived_chi_catalogue_lr_scaffold.py) |
| Catalogue Phase 3 production wire demo (1189× lookup speedup) | [`derived_chi_catalogue_production_wire_demo.py`](../computations/derived_chi_catalogue_production_wire_demo.py) |
| Catalogue Lean scaffold | [`content/quantum-observable-universe/lean/QOU/Machinery/DerivedCharacterCatalogue.lean`](../content/quantum-observable-universe/lean/QOU/Machinery/DerivedCharacterCatalogue.lean) |
| pyhecke_native GIL release + batched-GP roadmap | [`docs/audits/2026-06-07-pyhecke-native-gil-release-patch.md`](audits/2026-06-07-pyhecke-native-gil-release-patch.md) — Patch 1 (GIL) LANDED in v0.9.0; Patch 2 (batched chi_lambdas_via_gp + Rayon) LANDED but **NOT routed by default** — empirical perf showed threads + Tier 3 outperform batched-Rayon at medium n |
| Hoefsmit symbolic matrices | `computations/hecke_character_symbolic.hoefsmit_matrices_symbolic` |
| Canonical atomic braid construction | `computations/mass_at_3A_proper.atom_braid_word_3A` |
| LP duality (operator selection) | `computations/lp_dual_solver.py` (`solve_operator_selection_lp`) |
| Notation register (post-Phase 5n) | [`content/quantum-observable-universe/notation/notation-register.md`](../content/quantum-observable-universe/notation/notation-register.md) |
| 1ppb coordination ledger | [`docs/coordination/1ppb-categorical-chain.md`](coordination/1ppb-categorical-chain.md) |
| Precision dashboards | `computations/onepb-status-dashboard.witness.json` (L1) + `per-observable-100x-status.witness.json` (L2) |

---

## 8. The "everything is derivation, not fit" discipline (CLAUDE-facing)

**The 3-calibration rule** is strict: the canonical mathematical calibration triple is $m_e$, $m_\mu/m_e$, $m_\pi$. CAL-2 fixes $q_0$ from the lepton ratio $m_\mu/m_e$ (it dimensionalises to $\mathrm{Vol}(4_1)$). In the **Physical-Observations** layer one may anchor $q_0$ on a derived quantity of smaller experimental error — the proton ratio $m_p/m_e$ (0.06 ppb vs the muon ratio's 22 ppb; re-pin 2026-05-28, live solver `constants.py::q_at`), making $m_\mu/m_e$ a $9.5\sigma$ cross-check prediction (the μ–p tension — see `docs/audits/2026-05-28-mu-p-tension-substrate-floor.md`); this is a precision substitution, not a fourth calibration. $Q_\beta$ is **derived** from CAL-1 + CAL-2 via $Q_\beta = m_e |q_0^2 - 2q_0 - 1|(q_0+1)/(2q_0^3)$ (0.17% miss) — the bar-odd $\sinh$ partner of the bar-even $\cosh$ meson scale $m_\pi$. Everything else MUST derive from these three via the chain above.

**Common pitfalls** (look for these in code review):
- Hardcoded literal values where a categorical derivation exists → **discipline violation**. Example: `LAMBDA_PROTON_DOC = 2.4599527869` should derive from `prop:lambda-scale-bring-bloch-identity`.
- Φ_q in a binding-context script → **bar-symmetry violation**. The binding context wants Li_2^q.
- Calibration parameters not in the 3-input set → **4th-calibration violation**. The AGENTS.md `Δ_λ gate` (Track A blocker) explicitly forbids a 7th closure ansatz.
- Substrate-side compute using $q$ as $\mathbb{R}$ before the Archimedean functor → **§7c base-ring violation**. Everything categorical should be generic over `[Field R]` until step 9.

**Final-stage discipline**: every script in `computations/` (non-deprecated) should either (a) be backed by a `derivation_chain.py`-tracked DerivationChain, or (b) be marked `SCRIPT_CITED` against a canonical script that IS so backed.

---

## 9. Partition-respecting verification + mass = density × volume (2026-06-02)

The chain's frontier (step 9) is governed by one structural question the owner
posed: **do all the categorical invariants / functors / pairings respect the
Wedderburn partition decomposition `⊕_{λ⊢n} M_{d_λ}`?** If they do, the per-block
density `Δ_λ` is forced and `mass = density × volume` must be a per-λ sum.

### 9.1 Partition-respecting status

| Object | Respects partition? | Basis |
|---|---|---|
| Markov trace `tr_M = Σ_λ y_λ χ^λ` | ✅ **by construction** | Wenzl §1 — the `y_λ` ARE the per-block central weights; this IS the block decomposition |
| Wenzl weights `y_λ(q)` | ✅ derived | `y_lambda_wenzl_bridge.py`; one scalar per λ |
| Hecke characters `χ^λ(β_K)` | ✅ derived | Hoefsmit seminormal, per-irrep λ |
| Frobenius pairing `⟨a,b⟩_F`, self-duality `Ψ=S²=id` | ✅ formalised (D3/D23) | the pairing is central/symmetric; per-block orthogonality follows from Schur — **proved sorry-free** at the algebra level, finer per-λ orthogonality is the standing audit item |
| q-Reeb phase `θ_λ = arccos(χ^λ/d_λ)` | ✅ per-λ | `binding_reeb_phase_decomposition.py` |
| Categorical action / R-matrix (per generator) | ✅ **proved block-diagonal** | `MultiGeneratorSpectrum.lean` — 6×6 transfer matrix block-diagonal by induction; partition-*agnostic* until the Schur projection `π_λ` |
| Central idempotents `π_λ` (orthogonal, central) | 🟡 asserted (class axiom) | `Wedderburn.lean` — `trace_decomposition` PROVED *from* the axiom; the orthogonality `π_λπ_μ=0` is a classical theorem (Mathas §3.43) **awaiting Lean formalization**, not math |
| Confinement SDP (`T_w` selection) | ✅ per-block duals | `lp_dual_solver.py` emits `y_star[λ]` shadow prices |

**Verdict:** the binding/mass machinery is **manifestly block-graded** — every
load-bearing object is a per-λ quantity or a sum over λ, and the per-generator
block-diagonality is *proved by induction*. So `Δ_λ` is genuinely a per-block
density and the volume-Wedderburn framing is structurally legitimate. The gap is
not whether the objects respect the partition (they do) but **what the per-block
density numerically is** (§9.3).

**Two caveats the 1–6 audit surfaced** (both *formalization*, not math, gaps —
track in the proof-watcher queue):

1. **`y_λ` uniqueness rests on Schur character-orthogonality**, which is **not yet
   in Mathlib** (`wedderburn-as-noncomm-fourier.lean`); the cross-validation
   `Σ_λ y_λ χ^λ = z^{ℓ(w)}` passes numerically (n=3,4,5) but is unproved in Lean.
   Same for `π_λ` orthogonality and the per-λ Frobenius block-orthogonality
   `⟨a,b⟩_F = ⊕_λ ⟨a,b⟩_F^λ` (implied by §step 5+6, not formalized).
2. **The per-block q-Reeb phase `θ_λ` is DERIVED at step 2 (Yekutieli boundary
   holonomy) but COLLAPSED by the scalar trace** `tr_M = Σ_λ y_λ χ^λ`. This is an
   *information loss*: the framework computes the per-λ phase, then sums it away.
   **Retaining `θ_λ` per-block instead of collapsing it is the binding lever**
   (§9.3) — and the heaviest *unused* duality in steps 1–6.

### 9.2 mass = density × volume — the realized form

The owner's `mass = density × volume` IS the chain, with one correction the
compute has already established:

- **Volume is NOT the carrier** — it is the *exponential* of it. `tr_M ~ exp(Vol)`
  (Kashaev), so the binding endomorphism's `Δtr_M` is the **linearization** of the
  hyperbolic volume (§3, the *Bind* row; re-confirmed by the volume-Wedderburn
  probe in PR #1709, where *no* positive per-block volume reproduces even the
  **sign** of the ³H/³He split).
- **Density = per-rep q-Reeb phase** `θ_λ = arccos(χ^λ/d_λ)` (the "Hecke energy"
  per block) — a *signed, per-λ* angle. Markov-weighted it is a defensible
  per-block structural object, but its **magnitude closure of the A=3 mirror
  difference is NOT categorically derived**: the best *structural* combination
  reaches only ≈ 2.52 %, and the published 0.11 % relied on a **fitted `(1+q)/2`
  factor (CAL-4 antipattern)** that is also stale (canonical q₀ gives +0.12 %,
  sign-flipped). See §9.3 and [`2026-05-31-isospin-mirror-v9-discipline-assessment.md`](audits/2026-05-31-isospin-mirror-v9-discipline-assessment.md).
- **Volumes** enter as the knot volumes of the canonical braid — `Vol(𝓑₃)` (proton,
  step 9a), `Vol(6₂)`, Borromean `8G` — through the q-hyperbolic infra
  (`knot_volumes.py`, `Li_2^q` / Faddeev `Φ_q`, §4 context-sorting).

So: **`Δ_λ = (q-Reeb phase density)_λ`, evaluated through the q-hyperbolic
infrastructure, summed over the partition** — exactly the `density × volume`
shape, with the volume entering as `exp`-linearized angle, not raw `Vol`.

> **Guiding principle — preserve information until observation.** The
> archimedean functor `τ` (step 9) *is* the observation; it is the **only**
> place categorical structure should collapse to a real number. The production
> scalar `tr_M = Σ_λ y_λ χ^λ` collapses the per-block phase `θ_λ` at step 5 —
> *before* observation — which is an **information loss** that is harmless at
> A=2 (the linearization is exact) but destroys the per-block content needed at
> A≥3. The fix is to **carry the full per-λ `θ_λ` vector** (rotation
> `arccos` + growth `arccosh`) through the GB-filtration/jet tower and let `τ`
> (or the operator-valued combiner) do the collapse last. This is the same
> fibre-vs-observable cut as the `Im(q)` discipline and the "delta is
> pre-archimedean" result (`prop:delta-pre-archimedean`): **stay in the fibre as
> long as possible, observe last.** The per-λ vector is now emitted by
> [`binding_reeb_phase_decomposition.py`](../computations/binding_reeb_phase_decomposition.py)
> (`results[atom].by_partition`: `θ_free`, `θ_atom`, `Δθ_λ`, channel) — the
> un-collapsed carrier ready for downstream observation.

### 9.3 The gap, narrowed to one item

| Quantity | Status |
|---|---|
| Mirror-pair **differences** (³H/³He, A=3) | 🟡 **partial — signed structure real, magnitude not derived.** The bar-symmetric `(χ^λ + χ^{λᵀ})/2` isospin-mirror combination IS the signed per-block object the volume side proved necessary (#1709 T/³He obstruction), but its best *structural* result is ≈ 2.52 %. The widely-cited **0.11 % is a fitted `(1+q)/2` (CAL-4) near-match**, and is **stale** (canonical q₀ → +0.12 %). Not a derived closure. ([discipline assessment](audits/2026-05-31-isospin-mirror-v9-discipline-assessment.md)) |
| Deuteron **absolute** binding | 🟢 derived twice: `m_e·Vol(𝓑₃)·Δtr` (+0.19 %) and `μ₀·ℏ_q·J_q²(j=1)` (−9 %), `μ₀` derived |
| **A≥3 absolute** binding | 🔴 **the open gate** — the per-rep highest-weight `j=n/2` collapse of `θ_λ` saturates; needs the full per-rep `θ_λ` magnitude (not the linear truncation) |

**The narrowed compute item (REFRAMED 2026-06-02 — intensive vs extensive).**
A zero-fit derivation ([`2026-06-02-binding-intensive-vs-extensive-derivation.md`](audits/2026-06-02-binding-intensive-vs-extensive-derivation.md))
settles the framing: the canonical binding `B = E_0·(|tr_M_free| − |tr_M_atom|)`
is **INTENSIVE** — the trace difference *saturates* at ~3–4 MeV. The deuteron
(one inter-nucleon bond) is **derived to +3.6 %**, but A≥3 collapses (derived
A-growth 1.65× vs AME 12.72×). **Nuclear binding is EXTENSIVE (`∝ A`)**, so the
canonical trace-difference formula is **structurally missing the additive term**.

**Consequence — the Δ_λ gate was mis-framed.** No per-block *weight* `Δ_λ` can
turn an intensive quantity extensive (which is *why* the six prior ansätze + the
2026-06-02 probe series — volume, rotation/full-order `θ_λ`, content-energy,
content×phase — all failed). The closure is **not a density to multiply**; it is
an **additive sum over inter-nucleon bonds**:

$$B(K) = \sum_{b\,\in\,\bowtie_K} B_b,\qquad B_b = E_0\,\Delta|\mathrm{tr}_M|_b
\ \text{(the derived single-bond piece; deuteron = the base case)}.$$

Bond count `C(A,2)` already gives A-growth 6× (vs the intensive 1.65×); the
residual 6×→12.72× is the **per-bond growth** (each bond embedded in a denser
braid). The open compute item is therefore: **enumerate the `⨝_K` bonds and
derive each `B_b` from its embedded sub-braid trace difference** (the deuteron is
`n=6` base case, derived). This is a *derivation* (sum of derived pieces over the
structural bond set), the natural job of the operator-valued combiner (#1698) —
not a weight-fit. Tracking:
[`2026-05-28-binding-endomorphism-analogy.md`](audits/2026-05-28-binding-endomorphism-analogy.md),
Δ_λ gate context [`2026-05-18-delta-lambda-gating-context.md`](audits/2026-05-18-delta-lambda-gating-context.md),
inter-nucleon bonds [`inter-nucleon-channel-color-tube.md`](../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md).

**Update (2026-06-03) — the gate dissolves into a many-body series; the 4-body
term EXISTS.** The pairwise bond-sum has a ceiling: the canonical braid is a
**chain of A−1 interfaces** (verified), and the pairwise chain-sum captures only
**26 %** of ⁴He's binding ([`2026-06-02-binding-many-body-ceiling.md`](audits/2026-06-02-binding-many-body-ceiling.md)).
The 74 % residual is irreducible **many-body** binding — and the **4-body α term
already exists** as the sibling's canonical **magic-A** formula
`B(⁴He) = 2·m_e·A·Vol(L6a4) = 2·m_e·4·8G` → **+5.87 %, no fit**
([`2026-06-02-he4-binding-canonical-vs-full-theta-design.md`](audits/2026-06-02-he4-binding-canonical-vs-full-theta-design.md),
branch `he4-jsj-binding-link`). So the binding is a **many-body series**:

| body order | structure | regime | result |
|---|---|---|---|
| **2-body** | pairwise bond-sum (per-bond `E_0·Δtr_M`, abs convention) | A≤3 | correct T/³He ordering; A=2 derived |
| **3-body** | A=3 residual (the ~40 % pairwise gap) | T, ³He | **open** (whole-A link-volume — §below) |
| **4-body** | whole-α volume `2·m_e·A·8G` (magic-A) | ⁴He | **+5.87 %, no fit** |

**Common shape, per-isotope scale/assignment.** The deuteron (`m_e·Vol(6₂)`,
+1.1 %), the deprecated census A=3 (`2·m_e·Vol`, knot 8₁₁/Borromean), and magic-A
⁴He (`2·m_e·A·8G`, +5.87 %) all share the **shape** `(scale)·m_e·Vol(link)` —
but the scale (`ρ`, the `A` factor) and the link assignment **vary per isotope**
and are **not yet derived** (this is the residual heuristic/fitted aspect, NOT a
single law). The open items are therefore: (i) the **canonical link-volume
assignment** per nucleus (deuteron `6₂` is fixed; A=3/A=4 assignments are
heuristic-or-magic); (ii) the **scale rule** `ρ·A` (why ρ=1 at A=2 but ρ=2·A at
A=4); (iii) **reconciling** the pairwise (2-body) and whole-nucleus (4-body)
decompositions into one additive many-body series. The Δ_λ gate is dissolved —
it was never a per-block density — but the many-body series is not yet a closed
single form; the 4-body ⁴He piece (magic-A) is its most-derived member at +5.87 %.

### 9.4 Lean formalization debt (tracked — verification, NOT a compute gate)

The §9.1 partition-respecting objects are **already wired and numerically
cross-validated in compute** (Wenzl bridge n=3,4,5; `lp_dual_solver.py`; the
1ppb cross-check). The math is **classical and published** — the gap is only
that it isn't ported to Lean/Mathlib yet. **These do NOT block compute** (the
only compute gate is §9.3's full-order `θ_λ`); they are tracked here as
verification-debt for the proof-watcher / a Lean session (lake required).

| # | Statement to formalize | Target Lean | Classical ref | Status |
|---|---|---|---|---|
| **L-1** | Schur character-orthogonality on `H_n(q)` ⇒ `y_λ` uniqueness (`Σ_λ y_λ χ^λ = z^{ℓ(w)}` invertible at generic q) | `QOU.Hecke.Wedderburn` / `wedderburn-as-noncomm-fourier.lean` | Mathas (1999) §3.43; not in Mathlib | 🔴 debt |
| **L-2** | Central-idempotent orthogonality `π_λ π_μ = δ_{λμ} π_λ` (currently a class axiom) | `QOU.Hecke.Wedderburn` (`WedderburnDecomp`) | Mathas (1999) §3.43 | 🔴 debt |
| **L-3** | Per-λ Frobenius block-orthogonality `⟨a,b⟩_F = ⊕_λ ⟨a,b⟩_F^λ` (implied by §5+§6, not formalized) | `QOU.…FrobeniusHopfSubstrate` | follows from L-2 + `def:frobenius-hopf-substrate` | 🔴 debt |

These three close the "ASSUMED" entries in the §9.1 table. They are the
canonical chain's standing Lean backlog; pick them up in a lake-enabled session
(per AGENTS.md §1, every resulting `sorry` carries a `-- Ref:` citation until
discharged). Proof-watcher: route under the proof-integration-watcher queue.

### 9.5 The 6-knot multiplicative closure (tower interpretation)

Step 4 of the canonical chain establishes **6 H_3(q) basis elements**:

```
{ 1, σ_1, σ_2, σ_1σ_2, σ_2σ_1, σ_1σ_2σ_1 = σ_2σ_1σ_2 }   ← Bring χ = −6
```

A recurrent agent confusion is reading "6 basis elements" as **6 independent
SM-equivalent operators** that each contribute one slot of binding. That is
**wrong**: the 6 are **GENERATORS** of `H_3(q)` — the full binding spectrum is
the **multiplicative closure** of these generators climbing the **GB filtration /
jet tower** of Steps 7-8:

| GB depth k | tower layer | element class | count |
|---|---|---|---:|
| 0 | identity | `1` | 1 |
| 1 | length-1 | `σ_1, σ_2` | 2 |
| 2 | length-2 | `σ_1σ_2, σ_2σ_1` | 2 |
| 3 | length-3 (center) | `σ_1σ_2σ_1 = σ_2σ_1σ_2` | 1 |

Total: **6** — same 6 H_3 basis elements, viewed as the tower closure.

For atoms with `A ≥ 2`, the full braid lives in `H_{3A}` and the tower
extends to depth `3A − 1`. Each **depth band** `J^k / J^{k+1}` contributes
binding via the **depth-stratified canonical compute** (§9.5.1):

$$B(K) \;=\; m_e \cdot \sum_{k\,\geq\,0} \alpha_k \cdot
\sum_{w\,\in\,J^k/J^{k+1}}
y_w \cdot \bigl(\chi^\lambda_{\text{free}}(w) - \chi^\lambda_{\text{atom}}(w)\bigr).$$

So the binding spectrum is **NOT** 6 standalone contributions — it is the
sum over the whole tower closure, of which the 6 basis elements are the
generating set at depth ≤ 3.

#### 9.5.1 Canonical default compute

The default binding-energy compute IS the depth-stratified tower sum:

- **Production**: [`binding_depth_stratified_rust.py`](../computations/binding_depth_stratified_rust.py)
  (full H_{3A} via Geck-Pfeiffer + Hoefsmit Rust kernel, n ≥ 9)
- **LR variant** (per-nucleon H_3 → H_{3A} combiner for A ≥ 4):
  [`binding_depth_stratified_lr.py`](../computations/binding_depth_stratified_lr.py)
- **Python fallback**: [`binding_depth_stratified.py`](../computations/binding_depth_stratified.py)

α_k coefficients (NOT empirical fits):
- α_0 = α_1 = α_3 = 1 (trivial layers)
- α_2 = z² = (1/(√q+1/√q))² ≈ 0.2493 (Markov braid-trace marker²)
- α_{k≥4} = m_e · 8G ≈ 3.7445 (Vol(L6a4) Borromean plateau)

Current state (per witnesses 2026-06-09 — full audit at
[`docs/audits/2026-06-09-binding-canonical-default-depth-stratified.md`](audits/2026-06-09-binding-canonical-default-depth-stratified.md)):

| atom | tower B_pred | B_AME | ratio |
|---|---:|---:|---:|
| D | 0.607 MeV | 2.225 | −73 % |
| T | 2.808 MeV | 8.482 | −67 % |
| ³He | 2.653 MeV | 7.718 | −66 % |
| ⁴He | 14.063 MeV | 28.296 | −50 % |

LR and Rust direct now agree to 3 dp across all four atoms (verified
post-regen 2026-06-09). An earlier session reported a 4× LR vs Rust
disagreement on ⁴He (LR 2.089 vs Rust 0.497); this was 100 % an
artifact of a stale binding witness consuming a 24/77 partial cached
⁴He atom chi witness, since resolved. See the audit doc §Prevention
for the partition-completeness gate added to prevent recurrence.

**Tower sum does NOT close binding at the 10 % threshold.** The flat
**magic-A** formula `B(⁴He) = 2·m_e·A·8G` (+5.87 %, §9.3) BEATS the
depth-stratified tower on ⁴He (-50 % Rust direct). The unclosed gap
is in the **per-depth α_k ASSIGNMENT RULE** (which structural
constant goes to which k, why α_3 = 1 breaks the Markov-marker
series, why α_{k≥4} plateaus at m_e·8G) — NOT in the LR-vs-Rust
choice.

**Agent guidance for binding compute:**

1. ✅ DO use `binding_depth_stratified_rust.py` (or LR variant for A ≥ 4)
   as the **default canonical compute** — cite the witness JSON.
2. ✅ DO cite `canonical_status = canonical-with-empirical-assignment`
   when reporting binding numbers — flags the unclosed assignment-rule gap.
3. ✅ DO report `B_pred / B_AME` ratio alongside any number.
4. ❌ DO NOT invent new closure formulas (Coulomb correction, cross-
   isotope bar-symmetric, etc.) without first checking §9.3 + the
   audit doc. The Δ_λ gate is mis-framed; CAL-4 numerology is forbidden
   (cheat sheet §9.3 + isospin-mirror discipline assessment).
5. ❌ DO NOT treat the +5.87 % magic-A formula as universal binding —
   it applies only to ⁴He's doubly-magic shell.
6. ❌ DO NOT chase the retracted Option E v9 cross-isotope `(1+q)/2`
   0.11 % "closure" — see §9.3 retraction + audit doc.

---

## See also

- [`pre-archimedean-derivation-chain.md`](../content/quantum-observable-universe/braids-and-knots/pre-archimedean-derivation-chain.md) — paper-side rendering of this chain
- [`DERIVATION-CHAIN-METHODOLOGY.md`](../computations/DERIVATION-CHAIN-METHODOLOGY.md) — compute-side discipline
- [`docs/precision-goals.md`](precision-goals.md) — L1 vs L2 precision targets
- [`docs/duality-tracker.md`](duality-tracker.md) — coordinate-side classifier of every duality the framework uses or could use (D1-D24); status flags + closure paths; sibling-coordination index
- [`docs/audits/2026-06-09-binding-canonical-default-depth-stratified.md`](audits/2026-06-09-binding-canonical-default-depth-stratified.md) — depth-stratified `Σ_k α_k Φ_k` is the canonical binding default; α_k structural (z² Markov + m_e·8G Borromean), per-depth assignment rule is the unclosed gap
- [`docs/audits/2026-05-24-magic-shell-gs-filtration-exploitation.md`](audits/2026-05-24-magic-shell-gs-filtration-exploitation.md) — magic-shell + GS-NF wiring gap (L3 closure path)
- [`docs/audits/2026-05-24-isospin-categorical-source.md`](audits/2026-05-24-isospin-categorical-source.md) — D9 isospin closure path (operator-valued bowtie extension)
- [`.claude/skills/local/canonical-watcher.md`](../.claude/skills/local/canonical-watcher.md) §Slot J — probe follow-up discipline (GB filtration + jet order + bar-symmetry triple-check)
- [`AGENTS.md`](../AGENTS.md) — repo-wide agent discipline (§3b-cond, §7c, §7aa)
