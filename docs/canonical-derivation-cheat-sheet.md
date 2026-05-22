# Canonical derivation cheat sheet — substrate → observables

**Audience**: math/phys starting grad — a one-page-up map of "where every QOU formula comes from" and "which script computes it". Treats the chain as a cookbook so you don't have to dig through 700+ scripts to find what's canonical.

**Paper-side companion**: [`prop:pre-archimedean-derivation-chain`](../content/quantum-observable-universe/braids-and-knots/pre-archimedean-derivation-chain.md) (the rendered version that appears in the paper). This doc adds the **compute-pipeline mapping**, **Phase 5 findings**, and the **migration backlog** that don't belong in the paper but are essential for code review.

**Highlight to Claude** — referenced from CLAUDE.md so any agent picking up final-stage QOU work has the full canonical chain visible.

---

## 1. The chain in one diagram

```
            ┌─────────────────────────────────────────┐
            │  3 calibration inputs (only)            │
            │   m_e ─── leptonic scale                │
            │   m_μ/m_e ─── fixes q_0 (substrate)     │
            │   Q_β ─── fixes 𝔈₀ (hadronic scale)    │
            └─────────────────────────────────────────┘
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
                            │     tr_M(β) = Σ_λ y_λ(q) · χ_λ(β)
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
| **3. Alexander+Markov** | Unique trace $\mathrm{tr}_M$ invariant under braid + stabilization moves; $J_K(q) = \mathrm{tr}_M(\beta)$ | `thm:jones-markov-trace`, [jones1987] | `hecke_characters.chi_lambda_braid`; `pyhecke_native` (Rust) | per-witness |
| **4. Bring χ=−6** | $\dim H_3(q) = 6 = $ # embeddable torus knots in $\Sigma_4$; particle content fixed | `prop:x5-bring-weight-identification`, `prop:spectral-sequence-h3-explicit` | `hecke_core._PROTON_G0/G1`, `_NEUTRON_G0/G1` (canonical H_3 chains) | — |
| **5. Wedderburn + partitions** | $H_n(q) \cong \bigoplus_{\lambda \vdash n} M_{d_\lambda}(\mathbb{Q}(q))$; $\mathrm{tr}_M = \sum y_\lambda \chi_\lambda$ | `prop:alpha-k-derivation-procedure`, [wenzl1988] §1 | `y_lambda_wenzl_bridge.py` (numeric + symbolic) | `y-lambda-at-q0.witness.json` |
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
| **5l.1** | Closed-form Laurent rationals for $\chi^\lambda(\mathcal{B}_p, q)$ for $\lambda \vdash 3$ | clean χ_λ closed forms (PR #854); y_λ normalization reconciliation queued as 5l.2 | partial closed form for $\mathrm{tr}_M^3(\mathcal{B}_p)$ |
| **5n** | Comprehensive notation refactor: $\beta_K \to \mathcal{B}_K$, $\Delta_I^K \to \bowtie_K$, $\mathbf{E} \to \mathfrak{E}$, $\mathcal{B}(q) \to \mathfrak{B}(q)$, $\tau_M \to \mathrm{tr}_M$ | **MERGED** (PR #853) — register expansions: cal admits Hecke structurals; fraktur admits energies | notation discipline |
| **5o** | Functor disambiguation — $\tau$ (fibre, $\mathbf{C} \to \mathbf{Arch}$) vs $U$ (forgetful, $\mathbf{Arch} \to \mathbf{Vec}_\mathbb{R}$) vs $R \mapsto \mathbb{R}$ realisation (base-ring substitution, not a categorical functor) | doc note added to `notation-collisions.md` | terminology discipline |
| **5q** | Closed-form $\mathrm{tr}_M(\mathcal{B}_K)$ shared utility (`closed_form_tau_M.py`) for production migration; combines Phase 5c.1 + 5l | new branch `claude/phase-5q-pipeline-discipline`; verification witness in progress | unblocks cheat-sheet §5 action #4 |

**Combined Z-step factor at full tr_M level (post-5l + 5c.1):**

$$\frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})} \;=\; z(q) \cdot \mathrm{tr}_M^3(\mathcal{B}_p, q)$$

— exact, no residuals. (`z = 1/(q^{1/2} + q^{-1/2})` from Markov axiom; `tr_M^3(B_p)` from Wenzl disjoint multiplicativity.)

**Full closed-form $\mathrm{tr}_M(\mathcal{B}_K)$ (Phase 5q):**

$$\mathrm{tr}_M(\mathcal{B}_K) \;=\; \mathrm{tr}_M^3(\mathcal{B}_p, q)^Z \cdot \mathrm{tr}_M^3(\mathcal{B}_n, q)^N \cdot \prod_{i \in \bowtie_K} f_i(q),$$

with per-interface factors $f_i \in \{z, \, z - h\}$ for positive ($\sigma$, both p-p and **p-n**) and negative ($\sigma^{-1}$, n-n) interfaces. **Convention finding (Phase 5q v2).** The production marshalling for `chi_lambda_braid` — implemented in [`canonical_braid_marshalling.marshal_to_chi_lambda_braid`](../folio-assistant/computations/canonical_braid_marshalling.py) — silently maps the canonical averaged p-n form `(c=1, d=-h/2, gen)` to `(sign=+1, gen)` (the explicit `# averaged → σ convention` line), so `chi_lambda_braid` itself never sees the averaging coefficient. The closed form for production-matching purposes uses $f_{pn} = z$, NOT $z - h/2$. The strict averaged convention (math-correct $z - h/2$) is available as an opt-in via `pn_convention="strict_averaged"` for audit-trail probes; the default in [`closed_form_tau_M.py`](../folio-assistant/computations/closed_form_tau_M.py) matches the production marshalling. Verification witness: `closed-form-tau-M-verification-phase5q.witness.json`.

**Geom ↔ tr_M unification (Phase 5p, queued).** The downstream `ω` stage of `prop:hoefsmit-scattering-pipeline` (`braid β → tr_M → J_K(q) → ω → Geom(K) → × m_e → 𝔪`) consumes $J_K = \mathrm{tr}_M(\mathcal{B}_K)$. The Phase 5q closed form gives the input to ω in closed form; verifying that the propagation through ω → Geom(K) matches the canonical mass-table chain is the Phase 5p task (queued, depends on Phase 5q verification landing).

**Bring color-tube weighted averaging — open audit finding (Phase 5q).** The p-n interface "averaging" in the canonical atomic braid is currently the **uniform bar-invariant projection** $\sigma_{\mathrm{avg}} = (\sigma + \sigma^{-1})/2 = \sigma - h/2$ (per [`prop:averaging-resonance-rule`](#prop:averaging-resonance-rule)). However, the owner's intuition — recorded in [`probe_pn_flavor_asymmetry.py`](../folio-assistant/computations/probe_pn_flavor_asymmetry.py) and [`probe_per_sheet_flavor_nonin.py`](../folio-assistant/computations/probe_per_sheet_flavor_nonin.py) — is that the canonical form should be **Bring color-tube weighted**: each nucleon carries 3 quark color sheets (proton uud → $(\mu_u, \mu_u, \mu_d)$; neutron udd → $(\mu_u, \mu_d, \mu_d)$), and the p-n boundary should average over the 9 color-pair assignments weighted by quark content. Empirically (Scheme 4, per-sheet PL integration on Bring's surface) this reproduces $\Delta m_{n-p}$ to ~0.14% of CODATA. **Status**: this is a research-level open item; substrate H_{3A} compute (where [`closed_form_tau_M.py`](../folio-assistant/computations/closed_form_tau_M.py) operates) doesn't carry quark-mass inputs, so the weighted averaging is a downstream/mass-level operation. The module exposes `pn_convention="bring_color_weighted"` as a placeholder that raises `NotImplementedError` with the queue context. Implementing it requires (a) extending the closed form to accept quark-mass inputs, (b) defining the canonical color-sheet ↔ quark-flavor mapping (open per `probe_pn_flavor_asymmetry.py` conclusion: "research-level color-sheet ↔ quark-flavor mapping not explicitly stated in the paper").

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

---

## 5. Compute-pipeline migration backlog (canonical-derivation gaps)

Per the deep review of last 10 days of math improvements (2026-05-20 audit), the following **pipeline-discipline migrations** are queued. The MATH is correct; the COMPUTE has not migrated to the new canonical sources yet.

| # | Action | Where | Risk |
|---|---|---|---|
| 1 | Replace `LAMBDA_PROTON_DOC / LAMBDA_NEUTRON_DOC` literals with `conj:lambda-scale-bring-bloch-identity` derivation | `m_p_borromean_verification_50dps.py` | 3-calibration discipline violation; production m_p chain uses calibrated literal |
| 2 | Migrate 20 importers of SUPERSEDED `mass_endomorphism.py` to the new `mass_tower_operator_valued` API (after extending the 2-factor verification to (Z+N)) | 20 scripts including `build_proton_mass_50dps_chain.py`, `mass_formula_6term.py`, `mass_at_3A_proper.py` | SUPERSEDED dependency in production |
| 3 | Wire the Rust LR convention adapter (PR #829) into `atomic_tr_m_*` scripts for A ≥ 3 — expected ~500× speedup at ⁴He, ~10⁶× at ¹⁰B | `atomic_tr_m_helium4.py`, `atomic_tr_m_mpfr_50dps.py` + 6 mass scripts | massive compute speedup available, untaken |
| 4 | Refactor 4 production tr_M scripts to use `tr_M(𝓑_K) = tr_M(𝓑_K^vac) · z^{p_+} · (z-h)^{p_-}` closed form (Phase 5c.1 + 5l) | `atomic_chirality_residue.py`, `atom_level_wedderburn_tower.py`, `binding_canonical.py`, `binding_depth_stratified*.py` | re-computes H_{3A} character per atom; closed form sidesteps this |
| 5 | Add compute verification for the Reeb-flow / Garside closed-form (4 paper-only commits — `b6ed74635`, `88d7934b4`, `172263c6e`, `6ce96b4ce`) | new script needed | substrate-side derivation unverified |

These are the **5 final-stage bug-finding actions** identified from the 10-day audit. Each is a discrete, mechanical migration — the math is settled.

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
| 7 first-principles entry points + trust basis hierarchy | `folio-assistant/computations/DERIVATION-CHAIN-METHODOLOGY.md` |
| Canonical-derivation discipline (production scripts) | `folio-assistant/computations/derivation_chain.py` |
| q_0 50-dps canonical pin | `folio-assistant/computations/q_parameter.Q_50_DIGIT_STR` |
| Wenzl y_λ (numeric + symbolic) | `folio-assistant/computations/y_lambda_wenzl_bridge.py` |
| Hecke characters at varying q | `folio-assistant/computations/hecke_characters.chi_lambda_braid` (Python + Rust kernel) |
| Hoefsmit symbolic matrices | `folio-assistant/computations/hecke_character_symbolic.hoefsmit_matrices_symbolic` |
| Canonical atomic braid construction | `folio-assistant/computations/mass_at_3A_proper.atom_braid_word_3A` |
| LP duality (operator selection) | `folio-assistant/computations/lp_dual_solver.py` (`solve_operator_selection_lp`) |
| Notation register (post-Phase 5n) | [`content/quantum-observable-universe/notation/notation-register.md`](../content/quantum-observable-universe/notation/notation-register.md) |
| 1ppb coordination ledger | [`docs/coordination/1ppb-categorical-chain.md`](coordination/1ppb-categorical-chain.md) |
| Precision dashboards | `folio-assistant/computations/onepb-status-dashboard.witness.json` (L1) + `per-observable-100x-status.witness.json` (L2) |

---

## 8. The "everything is derivation, not fit" discipline (CLAUDE-facing)

**The 3-calibration rule** is strict: only $m_e$, $m_\mu/m_e$, $Q_\beta$ may be calibrated against experiment. Everything else MUST derive from these three via the chain above.

**Common pitfalls** (look for these in code review):
- Hardcoded literal values where a categorical derivation exists → **discipline violation**. Example: `LAMBDA_PROTON_DOC = 2.4599527869` should derive from `conj:lambda-scale-bring-bloch-identity`.
- Φ_q in a binding-context script → **bar-symmetry violation**. The binding context wants Li_2^q.
- Calibration parameters not in the 3-input set → **4th-calibration violation**. The CLAUDE.md `Δ_λ gate` (Track A blocker) explicitly forbids a 7th closure ansatz.
- Substrate-side compute using $q$ as $\mathbb{R}$ before the Archimedean functor → **§7c base-ring violation**. Everything categorical should be generic over `[Field R]` until step 9.

**Final-stage discipline**: every script in `folio-assistant/computations/` (non-deprecated) should either (a) be backed by a `derivation_chain.py`-tracked DerivationChain, or (b) be marked `SCRIPT_CITED` against a canonical script that IS so backed.

---

## See also

- [`pre-archimedean-derivation-chain.md`](../content/quantum-observable-universe/braids-and-knots/pre-archimedean-derivation-chain.md) — paper-side rendering of this chain
- [`DERIVATION-CHAIN-METHODOLOGY.md`](../folio-assistant/computations/DERIVATION-CHAIN-METHODOLOGY.md) — compute-side discipline
- [`docs/precision-goals.md`](precision-goals.md) — L1 vs L2 precision targets
- [`CLAUDE.md`](../CLAUDE.md) — repo-wide agent discipline (§3b-cond, §7c, §7aa)
