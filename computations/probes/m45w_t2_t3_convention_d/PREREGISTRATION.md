# Pre-Registration: `qou-m45w` Remainder — `T2` / `T3` on Convention-D Interleaved vs Plancherel Per-Generator $\hat{V}$ (2026-11-28)

Bean `qou-m45w` remainder & $\Phi_q$ pole diagnostic `qou-2tuv` (under Stability Epic `qou-s028`).
Written, committed, and pushed **before** evaluating the Convention-D `T2` / `T3` arms across `{D, T, 3He}` and the 16-atom sequence of `binding_block_multiplicative.py`.

## 1. Calibration, Anti-Fit & Precision Discipline (STRICT)

- **Working precision:** `mpmath.workdps(80)` (`OUT_DPS = 50` serialized), `json.load(..., parse_float=str)`, zero `float64` on all 80-dps algebraic and $q$-dilogarithm paths.
- **Aether pin:** `q0Anchor = "proton"` (`qou_substrate.constants.q_at(dps=80)`).
- **Zero fitting & witness safety:** No parameter, sign convention, or scale factor is tuned to match `AME2020`. Contended and downstream witnesses (`binding-block-multiplicative.witness.json`, `binding-via-interface-knot.witness.json`) are read-only comparison baselines and are NOT overwritten.

## 2. Background & Question Being Measured

Commit `10a20aeed52` (`qou-m45w`) corrected `T1_free` in `computations/binding_block_multiplicative.py` from the grouped Plancherel product $(v_{p,0}v_{p,1})^Z (v_{n,0}v_{n,1})^N$ to the exact Convention-D ($z_D = q_0^3 / (q_0^2 + 1)$) Markov trace of the **interleaved** 3-strand nucleon words (`trP^Z * trN^N`), while leaving `T2_diff` and `T3_diff` on the per-generator `weight_scheme="normalized_plancherel"` factors from `binding-via-interface-knot.witness.json`.

Two coupled structural issues govern `T2` and `T3`:
1. **Trace weight & non-commutativity (`qou-m45w`):** Per-generator bucketing commutes non-commuting braid letters across strands (`σ_0` vs `σ_1`) and evaluates them under `normalized_plancherel` ($z_{\mathrm{Pl}}$) rather than Convention-D ($z_D = q_0^3 / (q_0^2 + 1)$) or the interleaved nucleon block traces $(\mathrm{tr}_D(W_p), \mathrm{tr}_D(W_n))$ and Markov interface scalars $(f_{pp}, f_{nn}, f_{pn})$.
2. **$\Phi_q$ / $\mathrm{Li}_2^q$ pole at $z = +q_0$ (`qou-2tuv`):** $\mathrm{Li}_2^q(z) = \sum_{n \ge 1} \frac{z^n}{n(q_0^n - q_0^{-n})}$ converges for $|z| < q_0 \approx 1.10997858$ and has its first $\Phi_q$ pole on the positive real axis at $z = +q_0$. `binding_block_multiplicative.py` evaluates `li_2_q(+|V|)` (which diverges to $+\infty$ whenever $|V| \ge q_0$), whereas `binding_via_interface_knot.py` evaluates `-li_2_q_pentagon(-|V|)` (which continues across $z < -q_0$ along the negative real axis at the cost of a $\log^2$ branch cut imaginary residue when $|V| > q_0$).

## 3. Pre-Registered Evaluation Arms

Across `{D, T, 3He}` and the full 16-atom sequence of `binding_block_multiplicative.py`, using exact 80-dps `mpmath` derived parameters ($q_0$, $h_0 = q_0 - q_0^{-1}$, $\hbar_q = 1 - q_0^{-1}$, $z_D = q_0^3/(q_0^2 + 1)$, $\delta_{\mathrm{int}}$, $\delta_{\mathrm{flav}}$, $Q_\beta^{\mathrm{CAL3}}$):

- **Arm P0 (`hybrid_main_baseline`):** Reproduces `binding_block_multiplicative.py` (`10a20aeed52`): Convention-D interleaved `T1_free = trP^Z * trN^N` plus `normalized_plancherel` per-generator `T2_diff`, `T3_diff` with positive-argument `li_2_q(+|V|)`.
- **Arm D1 (`per_generator_convention_D`):** Exact 80-dps Convention-D Markov trace $\hat{V}_i^D = \alpha_i z_D + \beta_i$ of each per-generator bucketed polynomial $W_i = \alpha_i \sigma_i + \beta_i \mathbf{1}$ (`p_0, p_1, n_0, n_1` and single-crossing interfaces `pp, nn, pn`, cross-checked against `per_generator_V_hat_3A(..., weight_scheme="jones_wenzl")` at $A = 2, 3$):
  - **D1a (`pos_arg_li2q`):** `li_2_q(+|V|)` (`binding_block_multiplicative.py` sign convention), recording every $|\hat{V}_i^D| \ge q_0$ and $|\hat{V}_i^D \hat{V}_j^D| \ge q_0$ $\Phi_q$-pole hit in both uncancelled (`T2_free`, `T2_atom`, `T3_free`, `T3_atom`) and `free - atom` difference forms.
  - **D1b (`neg_arg_pentagon`):** `-li_2_q_pentagon(-|V|)` (`binding_via_interface_knot.py` sign convention), recording finite real parts, `divergent_pairs` ($|z| > q_0$), `t3_imag_residue`, `T2_diff`, `T3_diff`, and `B_MeV`.
- **Arm D2 (`interleaved_block_factors_convention_D`):** Replaces per-generator bucketing with the Convention-D interleaved nucleon block traces `trP`, `trN` (`Z` proton factors, `N` neutron factors) and exact Markov interface scalars $f_{pp} = z_D$, $f_{nn} = z_D - h_0$, $f_{pn} = z_D - \frac{1}{2}(h_0 - \delta_{\mathrm{flav}})$ (`free` interface $= 1$, `atom` interface $= f_e$), evaluated under both `li_2_q(+|V|)` (**D2a**) and `-li_2_q(-|V|)` (**D2b**), testing global pole-freedom ($\max |z| < q_0$).
- **Arm D3 (`whole_word_trace_convention_D`):** Evaluates the single-trace dilogarithm tower (`T1 + T2 + T3`) on the exact whole-word Convention-D Markov traces $\mathrm{tr}_D(W_{\mathrm{free}}) = \mathrm{trP}^Z\,\mathrm{trN}^N$ and $\mathrm{tr}_D(W_{\mathrm{atom}}) = \mathrm{trP}^Z\,\mathrm{trN}^N \prod_e f_e$ (both $\in (0, 1) \subset (-q_0, q_0)$), alongside the extensive log-ratio benchmark $B_{\log} = E_0 \ln(\mathrm{tr}_{\mathrm{free}} / \mathrm{tr}_{\mathrm{atom}})$.
