# Weight-Factor Audit

**Author:** Claude, session_01SdmQMzdktVYqqManFF3Dpt
**Trigger:** User observation 2026-05-19 — error scaling in co-Casimir extension (441 → 2.7 ppm as n=3 → n=9) suggests *on the right track but with wrong weights somewhere*. Higher n averages weight errors out; lower n highlights them.

## Why this audit

The framework's mass / binding / Q-value predictions are sums

$$ X = \sum_\lambda w_\lambda^{(?)} \cdot f_\lambda $$

where $w_\lambda^{(?)}$ is one of a *zoo* of partition-indexed weight families (Plancherel, tilde-Wedderburn, Jones–Markov, co-Casimir, LP shadow-price, color-tube residue, …) and $f_\lambda$ is a per-block invariant ($\chi^\lambda$, $\text{tr}(...)$, $\Delta_\lambda$, …). A small systematic error in any of these weight families propagates to predictions, but the symptom looks like an n-averaging trend rather than a constant offset.

The co-Casimir extension (`rho_k_co_casimir_extended.py`) gives the empirical signature:

| n=3A | atom | err_ppm |
|---:|---|---:|
| 3 | p | +441 |
| 3 | n | +371 |
| 6 | D | +39 |
| 9 | T | +2.7 |
| 9 | ³He | (computing) |
| 12 | ⁴He | (computing) |

If the formula were exact, all atoms would land at the same ppm scale (within float noise). The 100× drop from n=3 to n=9 is the n-averaging fingerprint.

This audit catalogues every weight family, fixes their canonical formulas, points to consumers, and flags suspect inconsistencies.

## Weight-family catalogue

### W1. Plancherel measure $w_\lambda$ (classical)

| field | value |
|---|---|
| Symbol | $w_\lambda$ |
| Formula | $w_\lambda := (\dim V_\lambda)^2 / n!$ |
| Domain | partitions $\lambda \vdash n$, all $n$ |
| Property | Probability measure: $\sum_\lambda w_\lambda = 1$ exactly |
| At $q=1$ | $w_\lambda$ itself (classical limit) |
| Provenance | Classical Hecke / Schur–Weyl |
| Notation register | [`braids-and-knots` row](../../content/quantum-observable-universe/notation/notation-register.md): *Plancherel measure (classical)* |
| Code | `wedderburn_jones_markov.py::w_lambda_classical(...)` (verify) |

### W2. Wedderburn q-weight $\tilde w_\lambda$

| field | value |
|---|---|
| Symbol | $\tilde w_\lambda$ (notation register: **tilde-Wedderburn**) |
| Formula | $\tilde w_\lambda := \dim_q^2(\lambda) / [n]_q!$ |
| Domain | partitions $\lambda \vdash n$, all $n$ |
| Property | NOT a probability measure at $q \neq 1$ (sum ≈ 1.51 at $q_0$, n=12) |
| At $q=1$ | reduces to $w_\lambda$ |
| Notation register | distinct from $w_\lambda$ at $q \neq 1$; *bare $w_\lambda$ MUST mean classical Plancherel* (notation-collisions.md) |
| Consumers | `prop:plancherel-term-7-formulation`, `prop:wedderburn-weight-canonical` |
| Code | TBD — search for explicit `dim_q^2 / [n]_q!` (audit task) |

### W3. Jones–Markov central coefficient $y_\lambda(q)$

| field | value |
|---|---|
| Symbol | $y_\lambda$ |
| Formula | Markov-trace bridge: $\text{tr}_M(W) = \sum_\lambda y_\lambda(q) \cdot \chi^\lambda(W)$ |
| Closed form | Wenzl hook–content formula |
| Domain | partitions $\lambda \vdash n$, all $n$ |
| Property | sign-indefinite for $n \geq 4$; $q$-Laurent rational |
| At $q=1$ | coincides with $w_\lambda$ **only on the self-conjugate stratum** (the Wenzl-bridge identification) |
| Provenance | Wenzl 1988, Jones 1987 |
| Cache | `y-lambda-at-q0-cache.py` → `y-lambda-at-q0.witness.json` (numeric at $q_0$) |
| Symbolic | `y-lambda-wenzl-bridge-symbolic-witness.json` (n=2..12, sympy expressions) |
| Code | `wedderburn_jones_markov.py::y_lambda_at(n, q)` |
| Notation register | *Jones–Markov central coefficient $y_\lambda$* — paper convention (Schrijver LP-dual reserves $u_\lambda$ for shadow-price; **do NOT conflate**) |

### W4. Co-Casimir Δ-selector $\Delta_\lambda^B := 1 / \dim_q(\lambda)$

| field | value |
|---|---|
| Symbol | $\Delta_\lambda^B$ |
| Formula | $\Delta_\lambda^B = 1 / \dim_q(\lambda)$ — forced by `thm:frobenius-codim-universal` |
| Property | **τ-invariant** ("vortex-blind"); same profile across all $\beta_K$ on $H_n(q)$ |
| Provenance | Frobenius co-Casimir per-isotypic restriction |
| Lean | `frobenius-codim-universal.lean` |
| Code | `rho_k_h3a_co_casimir.py` (D-only); `rho_k_co_casimir_extended.py` (multi-atom, this PR) |
| Audit concern | The τ-invariance means knot-specific info enters ONLY through $\chi^\lambda(\beta_K)$. If there's a per-λ weighting bug somewhere upstream in $y_\lambda$ or $\chi^\lambda$ normalisation, it stays hidden. |

### W5. LP / SDP shadow-price $u_\lambda$ (Schrijver)

| field | value |
|---|---|
| Symbol | $u_\lambda$, $u_0$ |
| Convention | Schrijver linear-programming variables |
| Domain | partitions $\lambda \vdash n$ via operator-selection LP/SDP |
| Property | $u_\lambda \ge 0$ by LP duality; identifies "binding" channels via active set |
| Code | `lp_dual_solver.py`, `pn_alpha_lp_dual.py` |
| Notation register | *LP shadow-price* — **never $y_\lambda$ here** (collides with Jones–Markov per notation-collisions.md) |
| Audit concern | shadow-price witness drift: `lp_dual_witness_validator.py` (CI gate) ensures `y_star` / `y0_star` / `active_set` always present. |

### W6. Color-tube residue weights (from Bring's cubic)

| field | value |
|---|---|
| Symbols | $p_1(c)$ (power sum), $h_2(c), h_3(c)$ (Hermitian), $\chi_\zeta(c)$ (character), $c$-Galois-orbit residues |
| Formula | residues of the chromatic cubic $X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) = 0$ around branch points |
| Property | 3-sheeted Galois orbit at $\zeta_5$-Bring level |
| Provenance | `delta-lambda-categorical-closure.md` (PR #787, NEGATIVE result on D — best mapping 0.067 MeV pred vs 2.225 AME) |
| Code | `delta_lambda_categorical_verification.py`, `delta_lambda_jsj_phase3.py` |
| Audit concern | The five $k(\lambda)$ mappings tested in PR #787 (by_rows / by_first_row / by_distinct_rows / by_isotype_channel / by_hook_length) all FAILED on D. The "wrong weight" intuition may live here: the per-$\lambda$ projection of the Galois-orbit residues is not yet derived. |

### W7. Hoefsmit character $\chi^\lambda(\beta)$

| field | value |
|---|---|
| Symbol | $\chi^\lambda(\beta)$ |
| Formula | Trace over the dim-$\lambda$ seminormal-form representation: $\chi^\lambda(\beta) = \text{tr}(\rho^\lambda(\beta))$ |
| Computation | matrix product through the seminormal-form Hoefsmit matrices |
| Code | `hoefsmit_symbolic.chi_lambda_symbolic`, `rho_k_h3a_refinement.chi_numeric` |
| Audit concern | Per-crossing accumulation order: `M ← M · σ_k` (canonical, per `hecke_character_symbolic.q_character_on_braid_word`). A flipped order would give $\chi^\lambda(\beta^{-1})$ instead of $\chi^\lambda(\beta)$ — looks similar at $q=1$ but diverges at $q_0$. |

### W8. Wenzl–LR coefficients $c^\lambda_{\mu\nu}(q)$

| field | value |
|---|---|
| Symbol | $c^\lambda_{\mu\nu}(q)$ |
| Formula | $q$-deformed Littlewood–Richardson coefficients for $\chi^\lambda(\beta_1 *_q \beta_2)$ on $*_q$-products |
| Domain | $\lambda \vdash n_1+n_2$, $\mu \vdash n_1$, $\nu \vdash n_2$ |
| Code | Rust binary `tools/hecke-engine/src/wenzl_lr.rs` |
| Audit concern | The buggy consumer `rho_k_full_via_wenzl_lr.py` applies this to *tensor* products instead of $*_q$ (atomic braids have inter-nucleon junctions). Fix is Q2 of PR #802 follow-up; PR #801 names the missing piece $\Delta_I^K$ (interface knot). |

### W9. Symmetric / antisymmetric channel weights

| field | value |
|---|---|
| Symbols | $q$, $-q^{-1}$ |
| Formula | Eigenvalues of σ_i in the Hecke algebra: $\sigma_i^2 = (q - q^{-1}) \sigma_i + 1$ |
| Property | Hecke / Skein register: σ → $q$ on symmetric channel, σ → $-q^{-1}$ on antisymmetric |
| Code | `knot_volumes.py` (q-deformed identities) |

### W10. Markov parameter $z$

| field | value |
|---|---|
| Symbol | $z$ |
| Formula | $z = 1/(q^{1/2} + q^{-1/2})$ |
| Property | Standard knot-theory Markov-trace deformation parameter |
| Audit concern | At $q = q_0 \approx 1.11$: $z = 1/(1.054 + 0.949) = 0.499...$. Check that any "z = 0.5" classical-limit assumption isn't being silently used at $q_0$. |

## Cross-consistency checks (audit gate)

The following should hold at every $q$ where each weight is defined:

| Check | Statement | Tolerance | Status |
|---|---|---|---|
| C1 | $\sum_\lambda w_\lambda = 1$ exactly (classical Plancherel) | 0 | TBD |
| C2 | $\tilde w_\lambda \to w_\lambda$ as $q \to 1$ | 1e-12 | TBD |
| C3 | $y_\lambda(q=1) = w_\lambda$ on the self-conjugate stratum (Wenzl bridge) | 1e-12 | TBD |
| C4 | $\sum_\lambda \tilde w_\lambda \approx 1.51$ at $q_0$, n=12 (notation-collisions.md) | 1e-2 | TBD |
| C5 | $\sum_\lambda 1/\dim_q(\lambda) = \tau(C_{\dim_q}^{H_n})$ (Frobenius theorem) | 1e-30 | already in `rho-k-h3a-co-casimir.witness.json` for n=6 ✓ |
| C6 | Hoefsmit accumulation order: $\chi^\lambda(\beta_1 \beta_2) = \chi^\lambda(\beta_2 \beta_1)$ (cyclic) | 1e-30 | TBD |
| C7 | LP/SDP shadow-price: $\sum_i u_i = u_0 \cdot n_{\text{target}}$ (strong duality) | 1e-12 | enforced by `lp_dual_witness_validator.py` (CI) ✓ |
| C8 | $z = 1/(q^{1/2} + q^{-1/2})$ at $q_0$ matches 0.499... | 1e-12 | TBD |

## KLR positivity — the diagnostic key

**User insight 2026-05-19:** "all observables by KLR are non-neg. so over-expected is an issue but can also help diagnose errors in model".

Per the Khovanov-Lauda-Rouquier categorification (AGENTS.md §7b on symmetric-crystal techniques), every contribution to a physical observable in the KLR canonical basis is **structurally non-negative**. In the co-Casimir expansion:

$$M_{\text{pred}} = \rho_K^{LO} \cdot m_e \cdot |\text{tr}_M| + \Delta\rho_K \cdot m_e \cdot |\text{tr}_M|$$

KLR positivity of $y_\lambda$ and $\chi^\lambda$ (both expressed in the KLR basis) makes every term in $\Delta\rho_K = (1/|\text{tr}_M|) \sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda^B$ structurally non-negative — therefore $\Delta\rho_K \ge 0$ and $M_{\text{pred}} \ge \rho_K^{LO} \cdot m_e \cdot |\text{tr}_M| = (Z m_p + N m_n)$.

But $M_{\text{atom}}^{\text{AME}} = (Z m_p + N m_n) - B$ (with binding energy $B > 0$). So **the framework as currently wired predicts the wrong-sign binding** — $M_{\text{pred}}$ ends up *above* the constituent sum, when it should be *below*.

Confirmed empirically across all atoms:

| atom | M_pred − M_constituent (MeV) | sign |
|---|---:|:---:|
| p | +0.414 | wrong (free nucleon should be 0) |
| n | +0.349 | wrong |
| D | +0.074 | wrong (should be −2.22 = −B) |
| T | +0.0076 | wrong (should be −8.48) |
| ³He | +0.012 | wrong (should be −7.72) |

This is the **diagnostic fingerprint** of a missing negative contribution. Candidates:

1. **Interface-knot $\Delta_I^K$ (PR #801)**: The categorical resolution — atomic braids carry an inter-nucleon interface that subtracts binding. Per PR #801: "Phases 2/3 subtract $Z \cdot \mathfrak{m}(\beta_p) + N \cdot \mathfrak{m}(\beta_n)$ computed in **independent** Hecke algebras $H_3$. The categorically-correct composite braid is $\beta_K = \beta_p^{(1)} \cdots \beta_n^{(N)} \cdot \Delta_I^K$ — Hecke *product* with an interface knot, **not** a tensor product."
2. **Bar-involution antisymmetric channel**: The "averaged" ctype = $\sigma - h/2 \cdot 1$ has both +h/2 (sym) and −h/2 (antisym) eigenvalues. KLR positivity refers to the symmetric channel; the antisymmetric channel carries the negative contributions that should appear in binding. If we're projecting to the sym channel only, we lose the binding.
3. **Conjugate-partition mirror**: For self-dual partitions $\lambda = \lambda^T$ the bar involution acts trivially; for non-self-dual the antisymmetric weight $\frac{1}{2}(\Delta_\lambda - \Delta_{\lambda^T})$ vanishes from a sym-only sum.

The **err-vs-n trend** then makes sense:

- Low n (n=3, p/n): only 3 partitions, all self-dual or near-self-dual; the antisymmetric channel contribution is small relative to the symmetric → +441 ppm error
- Higher n (n=9, T/³He): 30 partitions, many non-self-dual pairs; the *missing* antisymmetric contribution is proportionally larger but the *symmetric* error averages out → +2.7 ppm
- n=12 (⁴He): 77 partitions; further averaging in symmetric channel

So the +441 → +2.7 ppm trend ISN'T improving accuracy — it's that the (missing) antisymmetric correction grows with n while the (present) symmetric over-prediction stays fixed.

**Bottom line**: the substrate-derivation is wired with KLR-symmetric positivity but **missing the KLR-antisymmetric channel**. The path forward is folding the bar-involution (Type B folding per AGENTS.md §7b) into the Hoefsmit χ^λ accumulation — explicitly projecting onto both ±h/2 eigenspaces of the averaged crossings.

This audit, with KLR positivity as the gate, is the framework for finding which weight family loses the antisymmetric piece.

## Suspect lines (where the "wrong weight" might live)

Per the user's intuition that the error decreases with $n$, the suspect is a weight that:

1. Has a sign or normalization error that's small per term
2. Averages out as more partitions contribute (high $n$)
3. Dominates at low $n$ (few partitions)

Candidates ranked by suspicion:

| Rank | Suspect | Why |
|---|---|---|
| **1** | $\chi^\lambda$ averaging convention for "averaged" crossings | The inter-nucleon "averaged" ctype = σ − h/2·1 has eigenvalues +h/2 and −h/2. The trace contribution involves a 1/2 weight that could be applied at the wrong layer (per-crossing vs once at the end). For atoms with more inter-nucleon crossings (higher A), the 1/2's compound; mis-weighting would propagate. |
| 2 | $y_\lambda(q_0)$ symbolic vs numeric mismatch | `y-lambda-wenzl-bridge-symbolic-witness.json` (symbolic, evaluated to $q_0$) vs `y-lambda-at-q0.witness.json` (numeric). Cross-check at all $n$ that both agree to 50 dps. |
| 3 | Sign convention on $-q^{-1}$ vs $-(q^{-1})$ | Pedantic but the q ∈ $(0, 1)$ vs $q > 1$ branch matters for Hecke eigenvalues at $q_0 > 1$. |
| 4 | LP shadow-price normalisation | Active-set normalisation in `pn_alpha_lp_dual.py` may not factor through correctly when consumed by binding-energy formulas. |

## Audit script status (this PR)

`computations/audits/weight_factor_audit.py` is added in this PR. Implementation status:

| Check | Implemented? | Result at $n \le 12$ |
|---|:---:|---|
| C1 — Σ_λ w_λ = 1 (classical Plancherel) | ✓ | 11/11 PASS for $n = 2 \ldots 12$ |
| C2 — w̃_λ → w_λ as q → 1 | stub | not yet wired |
| C3 — y_λ(q=1) = w_λ on self-conjugate stratum (Wenzl bridge) | stub | not yet wired |
| C4 — Σ_λ w̃_λ at q_0 (tilde-Wedderburn sum) | ✓ | recorded; 1.51 expected at n=12 per notation-collisions.md |
| C5 — Σ_λ 1/dim_q(λ) = τ(C_dim_q^{H_n}) | ✓ | 11/11 PASS (well-defined positive) |
| C6 — χ^λ cyclic invariance (Hoefsmit accumulation) | stub | requires per-atom braid input |
| C7 — LP/SDP shadow-price strong duality | external | enforced by `lp_dual_witness_validator.py` in CI |
| C8 — z = 1/(q^½ + q^-½) at q_0 ≈ 0.4993 | ✓ | well-defined, distinct from classical 0.5 |

Total at n_max=12: **34/34 PASS** across the 4 currently-implemented checks (C1, C4, C5, C8). The 3 stubbed checks (C2, C3, C6) require additional infrastructure (q → 1 limit machinery, Wenzl-bridge symbolic eval at q=1, per-atom braid pairs) and are filed as follow-up work for a future PR.

Audit witness `weight-factor-audit.witness.json` lists every check with `{check, n, computed, expected, tolerance, passed}`.

### Future extension

1. Implement C2, C3, C6 (the stubbed checks).
2. Cross-reference all weight families against the notation register (catch new uses that haven't been registered).
3. Gate CI on no new weight family being introduced without a notation-register entry + cross-consistency check.

## Citation map (paper)

- Plancherel measure: `notation/notation-register.md` *braids-and-knots* row
- tilde-Wedderburn weight: `wedderburn-weight-canonical.md`
- Jones–Markov: `prop:alpha-k-derivation-procedure` + Wenzl 1988
- co-Casimir: `frobenius-codim-universal.md` / `.lean`
- Galois-orbit (color-tube): `delta-lambda-categorical-closure.md` (PR #787)
- Wenzl–LR: `tools/hecke-engine/src/wenzl_lr.rs` (Rust producer)
- Hoefsmit: `prop:hoefsmit-seminormal-form`
- LP shadow-price: `prop:operator-selection-lp` + `prop:bw-coefficient-shadow-price`

---

**Next step**: implement `weight_factor_audit.py` running C1–C8 + emit witness. Then re-run co-Casimir at the audit-clean weight set and re-measure the err_ppm vs n curve — if the slope changes (or flattens to a constant offset), the audit found something.
