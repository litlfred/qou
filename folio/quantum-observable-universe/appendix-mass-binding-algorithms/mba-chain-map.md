**Chain map.**
The following table outlines the eleven canonical steps of the substrate-to-observable chain, their justifying propositions, and Python entry points. Detailed per-step algorithm blocks follow.

| # | Step | Required propositions | Python API entry point | Witness JSON | Status |
|---|------|----------------------|-------------------------|---------------|:------:|
| 1 | Categorical action $\rho_n\colon B_n \to \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})$ | categorical-action of the braid group | `tools/hecke-engine/src/lib.rs` (Rust crate) | — | proved |
| 2 | Non-abelian Stokes $\to$ Hecke relation $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ | Hecke relation; GS-rewriter confluence | `pyhecke.build_nucleon_nf` / `pyhecke.build_atom_nf` (Rust core via `pyhecke-native`) | `hecke-core-symbolic-migration.witness.json` | proved |
| 3 | Markov trace $\mathrm{tr}_M$ on $H_n(q)$ | Alexander–Markov; uniqueness of $\mathrm{tr}_M$ | `qou_mass.compute_tr_M(Z, N)` / `pyhecke.nf_tr(nf)` | `markov-free-energy-qvalues.witness.json` | derived |
| 4 | Bring $\chi = -6$ brane | (settled — Bring surface) | script `bring_chiral_fibre_figure.py`; constants in `qou_substrate.constants` | `bring-chiral-fibre-figure.witness.json` | derived |
| 5 | Wedderburn decomposition $\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi^\lambda$ | Wedderburn / Wenzl decomposition | `pyhecke.wedderburn_weight(λ, q)` + `pyhecke.partitions_of(n)` | `wedderburn-lp-ew-wiring.witness.json` | derived |
| 6 | Frobenius pairing $\langle a,b\rangle_F$ + self-duality $\Psi = S^2 = \mathrm{id}$ | Frobenius pairing; self-duality | `pyhecke.check_frobenius(x)` (script: `audit_frobenius_pairing.py`) | — | proved |
| 7 | Gröbner–Shirshov filtration / $E_2$ collapse | GB spectral sequence | script `gb_filtration_jet_tracker.py` | `gb-filtration-jet-order.witness.json` | derived |
| 8 | Jet-prefix transport ($q \to 1$ limit) | jet-order proposition | script `gb_filtration_jet_order_reader.py` | `gb-filtration-jet-order-reader.witness.json` | conditional |
| 9a | Nucleon mass ratio $m_{\mathfrak{p}}/m_e$ via the muon-anchored Hecke energy $m_{\mathfrak{p}} = 2\,(m_\mu F_{\mathrm{Bor}} - 6 m_e)\cdot R_{\mathrm{s5bb}}$ | muon anchor $m_\mu = m_e\,\mathrm{Vol}(4_1)/\hbar_q^2$; Borromean dressing $F_{\mathrm{Bor}}$ | `qou_mass.predict(atom)` | `per-observable-100x-status.witness.json` | conditional |
| 9b | Per-isotope binding $B(K) = m_e \cdot \sum_\lambda y_\lambda\,\chi^\lambda\,\Delta_\lambda$ | binding-energy density ($\Delta_\lambda$ open) | `qou_mass.predict(atom, observable="binding_energy")` | `canonical-mass-table-242ppb.witness.json` | open |
| 10 | Confinement SDP and canonical $T_w$ | operator-selection LP; LP–SDP duality | script `confinement-operator-selection.py` (Python solver shim: `pyhecke.lp_dual_solver`) | `confinement-operator-selection.witness.json` | derived |
| 11 | $\beta$-decay $\mathfrak{Q}_\beta = Q_{\mathrm{base}} \cdot \prod_k (1 + c_k\,u^k)$ | $\mathfrak{Q}_\beta$ derivation; $c_k$ truncation order | script `q_beta_predicted.py` (CAL-3 pin: `build_cal_3_q_beta_witness.py`) | `cal-3-q-beta.witness.json` (CAL-3 pin), `q-beta-predicted.witness.json` (predictions) | derived |

**Sidecar algorithms.**
Five standalone algorithms support the production pipeline:

1. **$\Delta_\lambda$ closure ansätze.** The per-partition density at each isotope; currently open.
2. **$c_k$ truncation ladder.** The convergent series whose truncation order $N$ is fixed by precision $N \geq \lceil \log_{10}(1/\varepsilon) / 2.07 \rceil - 1$.
3. **LP/SDP dual emission contract.** Every operator-selection compute must emit primal and dual variables, enforced by `lp_dual_witness_validator.py`.
4. **Witness-JSON pipeline.** Cross-language interchange schema and the `WitnessBuilder` pattern.
5. **Atomic electron layer (Level 6).** $M_{\mathrm{atom}} = M_{\mathrm{nuclear}} + Z\,m_e - B_{\mathrm{el}}(Z)$ with $B_{\mathrm{el}}$ the bare-$Z$ hydrogenic shell sum at the canonical e-Hartree scale $E_h = \alpha_{EM}^2 m_e c^2$ (CS-corrected $\alpha_{EM}$ at arbitrary precision). Producer `atom_electron_mass.py`, witness `atom-electron-mass.witness.json`; consumed by the mass dashboard's atomic table (using the derived hydrogenic $B_{\mathrm{el}}$, with the AME empirical fit retained for comparison). Inter-electron screening ($Z_{\mathrm{eff}}$) is open.

**Location of the algorithm statements.**
The per-step blocks provide the precise input/output contract, correctness conditions, complexity estimate, and Python signature. These specifications alone suffice to reproduce every numerical prediction without referencing implementation source code.
