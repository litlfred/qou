**Chain map.**
The table below lists the eleven canonical steps of the substrate
$\to$ observable chain together with the propositions that justify
each step and the Python entry point that realises it. Detailed
per-step algorithm blocks appear in the sections that follow; this
table is the high-level index.

| # | Step | Required propositions | Python API entry point | Witness JSON | Status |
|---|------|----------------------|-------------------------|---------------|:------:|
| 1 | Categorical action $\rho_n\colon B_n \to \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})$ | categorical-action of the braid group | `tools/hecke-engine/src/lib.rs` (Rust crate) | — | proved |
| 2 | Non-abelian Stokes $\to$ Hecke relation $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ | Hecke relation; GS-rewriter confluence | `pyhecke.build_nucleon_nf` / `pyhecke.build_atom_nf` (Rust core via `pyhecke-native`) | `hecke-core-symbolic-migration.witness.json` | proved |
| 3 | Markov trace $\mathrm{tr}_M$ on $H_n(q)$ | Alexander–Markov; uniqueness of $\mathrm{tr}_M$ | `qou_mass.compute_tr_M(Z, N)` / `pyhecke.nf_tr(nf)` | `markov-free-energy-qvalues.witness.json` | derived |
| 4 | Bring $\chi = -6$ brane | (settled — Bring surface) | script `folio-assistant/computations/bring_chiral_fibre_figure.py`; constants in `qou_substrate.constants` | `bring-chiral-fibre-figure.witness.json` | derived |
| 5 | Wedderburn decomposition $\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi^\lambda$ | Wedderburn / Wenzl decomposition | `pyhecke.wedderburn_weight(λ, q)` + `pyhecke.partitions_of(n)` | `wedderburn-lp-ew-wiring.witness.json` | derived |
| 6 | Frobenius pairing $\langle a,b\rangle_F$ + self-duality $\Psi = S^2 = \mathrm{id}$ | Frobenius pairing; D3/D23 self-duality | `pyhecke.check_frobenius(x)` (script: `audit_frobenius_pairing.py`) | — | proved |
| 7 | Gröbner–Shirshov filtration / $E_2$ collapse | GB spectral sequence | script `folio-assistant/computations/gb_filtration_jet_tracker.py` | `gb-filtration-jet-order.witness.json` | derived |
| 8 | Jet-prefix transport ($q \to 1$ limit) | jet-order proposition | script `folio-assistant/computations/gb_filtration_jet_order_reader.py` | `gb-filtration-jet-order-reader.witness.json` | conditional |
| 9a | Mass identity $m(K) = m_e \cdot \mathrm{VolDensity}(K, q_0)$ | $\mathrm{Geom}$-universality; mass identity | `qou_mass.predict(atom)` | `per-observable-100x-status.witness.json` | conditional |
| 9b | Per-isotope binding $B(K) = m_e \cdot \sum_\lambda y_\lambda\,\chi^\lambda\,\Delta_\lambda$ | binding-energy density ($\Delta_\lambda$ open) | `qou_mass.predict(atom, observable="binding_energy")` | `canonical-mass-table-242ppb.witness.json` | open |
| 10 | Confinement SDP and canonical $T_w$ | operator-selection LP; LP–SDP duality | script `folio-assistant/computations/confinement-operator-selection.py` (Python solver shim: `pyhecke.lp_dual_solver`) | `confinement-operator-selection.witness.json` | derived |
| 11 | $\beta$-decay $\mathfrak{Q}_\beta = Q_{\mathrm{base}} \cdot \prod_k (1 + c_k\,u^k)$ | $\mathfrak{Q}_\beta$ derivation; $c_k$ truncation order | script `folio-assistant/computations/q_beta_predicted.py` (CAL-3 pin: `build_cal_3_q_beta_witness.py`) | `cal-3-q-beta.witness.json` (CAL-3 pin), `q-beta-predicted.witness.json` (predictions) | derived |

**Status legend.**
*proved* (sorry-free Lean);
*derived* (categorical, no fit);
*conditional* (conjecture-conditional / partial);
*open* (open gate).

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
canonical Python signature. One should be able to reproduce
every numerical prediction in the paper from this appendix alone,
without recourse to the implementation source.
