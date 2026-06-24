**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark) — 𝔔_β spectral bridge).**

*Let $\mathcal{B}_n$ be the canonical free-neutron braid word with single
wrap $A = 1$, let $q = q_0$ be the substrate parameter, let
$h := q - q^{-1}$, and let*

$$
  z \;:=\; \frac{1}{\sqrt q + 1/\sqrt q}
$$

*be the Markov–Jones parameter (Hecke–Skein normalization).
Write $E_0 := m_e \cdot c_q^2 \cdot \hbar_q = m_e/(q(q-1))$ for the
single-tick energy scale per
[rem:energy-scale-planck](#rem:energy-scale-planck), and let*

$$
  \mathfrak{Q}_\beta^{\mathrm{A}} \;:=\;
  \lvert \Delta(\mathrm{net}) \rvert \cdot E_0
  \qquad
  \mathfrak{Q}_\beta^{\mathrm{B}} \;:=\;
  \ln\!\frac{V_{\mathrm{pp}}}{V_{\mathrm{nn}}} \cdot \frac{E_0}{z}
$$

*denote the closed-form $Q$-value in the NF-counit basis
(Form A, [prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic))
and in the transfer-matrix eigenfunction basis
(Form B, [prop:beta-decay-transfer-matrix](#prop:beta-decay-transfer-matrix)),
respectively. Then both are finite-depth truncations of the same
spectral decomposition and agree as*

$$
  \frac{\mathfrak{Q}_\beta^{\mathrm{A}}}{\mathfrak{Q}_\beta^{\mathrm{B}}}
  \;=\;
  1 \;+\; \frac{(z-1)\,h}{2} \;+\; O(h^2),
$$

*with bridge identity*

$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \ln\!\frac{V_{\mathrm{pp}}}{V_{\mathrm{nn}}} \cdot \frac{E_0}{z}
  \cdot \Bigl(1 + \tfrac{(z-1)\,h}{2} + O(h^2)\Bigr).
$$

*The remainder at depth $N$ in the brane-tower truncation satisfies*

$$
  \bigl\lvert \mathfrak{Q}_\beta^{(N)} - \mathfrak{Q}_\beta^{\mathrm{exact}} \bigr\rvert
  \;\le\;
  C(K) \cdot e^{-c(K)\,N}
$$

*per conj:archimedean-remainder-exponential-decay, with $C, c > 0$ depending only on the free-neutron sector data $K$.*

## Reading

The bridge formula

$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \mathfrak{Q}_\beta^{\mathrm{B}} \cdot \bigl(1 + \tfrac{(z-1)\,h}{2} + O(h^2)\bigr)
$$

says that **Form A and Form B are not competing predictions but a
single observable expressed in two bases** — the NF-counit basis
where $\Delta(\mathrm{net})$ is a discrete combinatorial datum, and
the transfer-matrix basis where $\ln V_{\mathrm{pp}}/V_{\mathrm{nn}}$ is
the natural eigenfunction observable. The $1/z$ factor in Form B's
expression $E_0/z$ is **not a calibration knob**; it is the
Markov–Jones normalization required to map eigenfunction space onto
MeV.

The exponential-remainder bound supplies the eigenfunction
**dampening** principle (rendered explicit in
conj:archimedean-remainder-exponential-decay):
finite-depth truncations recover the exact $\mathfrak{Q}_\beta$ exponentially
fast in GB depth $N$, which is why the single-wrap symbolic form
(Form A at $N = 0$) already achieves $+0.168\%$ accuracy.
## Provenance

This proposition was derived during the cycle-6/7 audit on 
([`docs/audits/-q-beta-form-A-vs-form-B-canonical-choice.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-q-beta-form-A-vs-form-B-canonical-choice.md))
and verified numerically at 50 dps via
[`q_beta_spectral_bridge_witness.py`](https://github.com/litlfred/qou/blob/main/computations/q_beta_spectral_bridge_witness.py)
([`q-beta-spectral-bridge.witness.json`](https://github.com/litlfred/qou/blob/main/computations/q-beta-spectral-bridge.witness.json)):

See [Table](#tbl:q-beta-spectral-bridge-table-data).

The residual sits inside the $O(h^2)$ Taylor bound; the agreement
is unconditional algebra modulo the bound. The MeV-level discrepancy
between $\mathfrak{Q}_\beta^{\mathrm{A}}$ and $\mathfrak{Q}_\beta^{\mathrm{B}}$ is **not** a
prediction inconsistency — it is the same next-order correction
$(z-1)h/2 \approx -0.052$ to the bridge ratio that the witness's
first assertion bounds. Both forms agree with CODATA $0.7823$ MeV
within $7\%$; the canonical predictor used elsewhere remains
Form A at $+0.168\%$ residual via the single-wrap symbolic closed
form of [prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic).
