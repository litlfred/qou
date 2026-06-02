**Chain map.**
The table below lists the eleven canonical steps of the substrate
$\to$ observable chain together with the propositions that justify
each step and the Python entry point that realises it. Detailed
per-step algorithm blocks appear in the sections that follow; this
table is the high-level index.

| # | Step | Required propositions | Python API entry point | Witness JSON | Status |
|---|------|----------------------|-------------------------|---------------|:------:|
| 1 | Categorical action $\rho_n\colon B_n \to \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})$ | categorical-action of the braid group | `hecke_engine::categorical_action` (Rust) | — | ✅ |
| 2 | Non-abelian Stokes $\to$ Hecke relation $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ | Hecke relation; GS-rewriter confluence | `pyhecke.gs_reduce(word, q)` | `hecke_normal_form.witness.json` | ✅ |
| 3 | Markov trace $\mathrm{tr}_M$ on $H_n(q)$ | Alexander–Markov; uniqueness of $\mathrm{tr}_M$ | `pyhecke.tr_M(word, q)` / `pyhecke_native.markov_trace` | `markov_trace.witness.json` | 🟢 |
| 4 | Bring $\chi = -6$ brane | (settled — Bring surface) | `qou_substrate.bring_brane` constants | — | 🟢 |
| 5 | Wedderburn decomposition $\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi^\lambda$ | Wedderburn / Wenzl decomposition | `pyhecke.wedderburn_decompose` | `wedderburn.witness.json` | 🟢 |
| 6 | Frobenius pairing $\langle a,b\rangle_F$ + self-duality $\Psi = S^2 = \mathrm{id}$ | Frobenius pairing; D3/D23 self-duality | `pyhecke.frobenius_pairing` | `frobenius_pairing.witness.json` | ✅ |
| 7 | Gröbner–Shirshov filtration / $E_2$ collapse | GB spectral sequence | `hecke_engine::gb_filtration` | `gb_filtration.witness.json` | 🟢 |
| 8 | Jet-prefix transport ($q \to 1$ limit) | jet-order proposition | `qou_substrate.jet_truncate` | — | 🟡 |
| 9a | Mass identity $m(K) = m_e \cdot \mathrm{Geom\_full}(K, q_0)$ | $\mathrm{Geom}$-universality; mass identity | `qou_mass.predict(K)` | `per_observable_100x_status.witness.json` | 🟡 |
| 9b | Per-isotope binding $B(K) = m_e \cdot \sum_\lambda y_\lambda\,\chi^\lambda\,\Delta_\lambda$ | binding-energy density (Δ_λ open) | `qou_mass.binding_energy(K, isotope)` | `mass_table.witness.json` | 🔴 |
| 10 | Confinement SDP and canonical $T_w$ | operator-selection LP; LP–SDP duality | `lp_dual_solver.solve_operator_selection_lp(t, G, n_target)` | `operator_selection_lp.witness.json` | 🟢 |
| 11 | $\beta$-decay $Q_\beta = Q_{\mathrm{base}} \cdot \prod_k (1 + c_k\,u^k)$ | $Q_\beta$ derivation; $c_k$ truncation order | `qou_mass.q_beta(N)` | `q_beta_ladder.witness.json` | 🟢 |

**Status legend.**
✅ proved (sorry-free Lean) ·
🟢 derived (categorical, no fit) ·
🟡 conjecture-conditional / partial ·
🔴 open gate.

**Sidecar algorithms.**
In addition to the chain steps, four standalone algorithms support
the production pipeline and appear in their own sections:

1. **$\Delta_\lambda$ closure ansätze** (Option E and related
   crystal-graph attempts). The per-partition density at each
   isotope; currently open.
2. **$c_k$ truncation ladder.** The convergent series whose
   truncation order $N$ is chosen by target precision via
   $N \geq \lceil \log_{10}(1/\varepsilon) / 2.07 \rceil - 1$.
3. **LP/SDP dual emission contract.** Every operator-selection
   compute must emit both primal and dual variables; the contract
   is enforced by `lp_dual_witness_validator.py` in CI.
4. **Witness-JSON pipeline.** Cross-language interchange schema
   (`witness-schema`) and the `WitnessBuilder` pattern used by every
   canonical script.

**Where the algorithms are stated.**
The per-step blocks that follow each algorithm carry the precise
input/output contract, the correctness conditions (referring to the
propositions cited above), the complexity estimate, and the
canonical Python signature. The reader should be able to reproduce
every numerical prediction in the paper from this appendix alone,
without recourse to the implementation source.
