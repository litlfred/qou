# Model B (knot-canonical) in the compute pipeline — new mass table

**Date**: 2026-05-11
**Branch**: `claude/neutron-mass-50dps-chain`
**Status**: Model B end-to-end pipeline lands; single-term mass formula
falsified at 87–100% level on light isotopes.

## What is Model B

Per the τ_M / τ_SW conflation diagnosis in
[`why-individual-mass-residuals-fit-not-derive.md`](./2026-05-11-why-individual-mass-residuals-fit-not-derive.md)
§"Update 2026-05-11", the framework had two parallel "deuteron" braid
encodings:

| Encoding | Strands | Structure | Path |
|----------|--------:|-----------|------|
| **Model A** (`atom_braid_word_3A`) | $3A$ | Each nucleon = 3 quark strands; inter-nucleon binding crossings | Production (`markov_peel.tr_M_atomic`, Hoefsmit+Wenzl bridge) |
| **Model B** (SDP-canonical) | minimum | Each nucleus = canonical hyperbolic knot in $B_n$ for minimum $n$ | `from_scratch/derive_*.py`, `probe_sdp_canonical_paper_formula.py` |

Per owner directive (2026-05-11): **Model B → full compute pipeline; new
mass table.**

## Pipeline status

[`probe_sdp_canonical_paper_formula.py`](../../computations/probe_sdp_canonical_paper_formula.py)
runs Model B end-to-end:

1. Read SDP-canonical braid words from
   [`joint-tower-sdp-h6-h9.witness.json`](../../computations/joint-tower-sdp-h6-h9.witness.json).
2. Compute $\tau_M(T_w(\beta))$ via the Wenzl-bridge $y_\lambda$ table from
   [`y-lambda-wenzl-witness.json`](../../computations/y-lambda-wenzl-witness.json).
3. Apply paper formula $B = m_e \cdot \rho \cdot \tau_M(T_w)$.
4. Emit
   [`probe-sdp-canonical-paper-formula.witness.json`](../../computations/probe-sdp-canonical-paper-formula.witness.json)
   with full per-$\lambda$ breakdown.

## New mass table (Model B canonical-knot at $q_0$)

Binding energies via the **single-term** topological-mass formula
$B = m_e \cdot \rho \cdot |\tau_M(T_w)|$:

| Atom | knot | $n_0$ | $\rho$ | braid word | $\tau_M$ (Plancherel) | $B_{pred}^{\mathrm{Pl}}$ (MeV) | $\tau_M$ (Wenzl-Schur) | $B_{pred}^{\mathrm{W}}$ (MeV) | $B_{AME}$ (MeV) | error (Wenzl) |
|------|------|------:|-------:|------------|---------------------:|------------------------------:|----------------------:|-----------------------------:|----------------:|--------------:|
| D    | $6_2$  | 3 | 1 | $[1, -2, 1, 1, 1, -2]$ | $0.04944$ | $0.0253$  | $0.28833$ | $0.1473$ | $2.2246$ | $-93.4\%$ |
| T    | $8_{11}$ | 5 | 2 | $[-1, 2, -3, 2, 1, -3, -3, 4, -3, -2, -3, -4, -3, 2]$ | $-0.00100$ | $-0.0010$ | $0.01289$ | $0.0132$ | $8.4818$ | $-99.8\%$ |
| ³He  | $L6a4$ | 3 | 2 | $[-1, 2, -1, 2, -1, 2]$ ($\beta_{\mathrm{Bor}}$) | $0.98552$ | $1.0072$ | $0.99837$ | $1.0203$ | $7.7181$ | $-86.8\%$ |

## Verdict

The single-term Model B formula $B = m_e \cdot \rho \cdot |\tau_M|$ **fails
empirically by 87–100% on every light isotope**, regardless of whether
the Markov weights are Plancherel ($w_\lambda = (\dim V_\lambda)^2/n!$) or
Wenzl-Schur ($w_\lambda = s_\lambda(q, q^{-1})/H_q(\lambda)$).

**This is not a Model B bug — it is the **known structural gap** in
the single-term mass formula** (per
[`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)).
The unified multi-term formula
$$
  B = T_1 |\tau_M| + (T_2 + T_3)\,\text{brane tower} + T_4 \sum 1/\dim_q + T_5 \,\text{chirality} + T_6 \,\text{jet-prefix}
$$
is needed; Model B contributes only $T_1$.

## What's wired vs what's not (Model B side)

| Term | What it is | Model B wiring |
|------|-----------|----------------|
| $T_1 = m_e \cdot \rho \cdot |\tau_M|$ | Single-term topological mass | ✓ `probe_sdp_canonical_paper_formula.py` (this PR) |
| $T_2 + T_3$ | Brane-tower $\Phi_q$ dilogarithm sum | ✗ Open R&D (`brane-tower-z-habiro` conjecture; PR #638 refutes scalar form) |
| $T_4$ | $m_e \cdot \sum_\lambda 1/\dim_q(\lambda)$ Frobenius co-Casimir | ✓ `derive_m_p_hecke_path_a.py` / `derive_m_n_hecke_path_a.py` (Wenzl-bridge T4) |
| $T_5$ | Chirality / Bloch-Wigner | ◐ Quarantined sign-indefinite (per `delta-skein-substrate-identity.md`) |
| $T_6$ | Jet-prefix / GB filtration | ✗ Open R&D |

## Open questions

1. **Multi-term assembly in Model B**: write
   `build_canonical_knot_mass_table.py` that runs the full T1+...+T6
   formula on Model B's SDP-canonical braids (currently the only
   assembly is on Model A's `atom_braid_word_3A`).

2. **Markov-equivalence bridge to Model A**: per the user's
   "A is an approx of B" framing — verify $\tau_M^{H_{3A}}(\text{atomic}(Z,N))$
   reduces to $\rho^{?} \cdot \tau_M^{H_n}(\text{canonical-knot})$ under
   Markov stabilisation. Diagnostic: ratios
   $\tau_M^A/\tau_M^B$ at $q_0$:
   - D: $0.388286 / 0.28833 = 1.346$
   - T: $0.10405 / 0.01289 = 8.072$
   - ³He: $0.20654 / 0.99837 = 0.207$

   No common ratio — confirms the two encodings are not Markov-equivalent
   under simple stabilisation.

3. **Individual hadron masses** (proton, neutron alone) — Model B
   currently has $D$, $T$, ³He, ⁴He (composite nuclei) but no canonical
   knot for a free proton/neutron. The "Borromean baryon" content blocks
   on this branch propose $\beta_{\mathrm{Bor}}$ as the proton/neutron
   shared canonical braid, with orientation partition $(2,1)$ vs $(1,2)$
   distinguishing them — but the Skein corrections that should give
   $m_p \neq m_n$ are not yet derived.
