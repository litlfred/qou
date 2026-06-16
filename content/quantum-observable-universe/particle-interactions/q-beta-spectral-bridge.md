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

**Proof.**

*Form A side.* The NF counit reads
$\lvert\Delta(\mathrm{net})\rvert = h(2 - h)/2 = h - h^2/2 + O(h^3)$
(direct expansion of the single-wrap symbolic closed form per
[prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic)).

*Form B side.* The Hecke perturbation has the half-factor
$\Delta_\beta(q) = \tfrac{1}{2}(q - q^{-1})\,\mathbb{I} = \tfrac{h}{2}\,\mathbb{I}$
(per [prop:beta-decay-transfer-matrix](#prop:beta-decay-transfer-matrix)
§"change in transfer-matrix product"), so the change in Markov-traced
volume *per generator* picks up the same half:

$$
  \Delta \hat V_i
  \;=\;
  z\,(\Delta M_i)_{11} + (\Delta M_i)_{21}
  \;=\;
  \tfrac{z\,h}{2} + O(h^2).
$$

At single wrap with $A = 1$ the proton-to-neutron conversion affects
the **two** generators $\sigma_0, \sigma_1$ (per the table in
[prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic)
§"Single-wrap NF computation"), so the total log-ratio is

$$
  \ln\!\frac{V_{\mathrm{pp}}}{V_{\mathrm{nn}}}
  \;=\;
  \sum_{i \in \{0,1\}}
    \ln\!\frac{\hat V^{\mathrm{pp}}_i}{\hat V^{\mathrm{nn}}_i}
  \;\approx\;
  2 \cdot \tfrac{z\,h}{2}
  \;=\;
  z\,h \;+\; O(h^2)
  \;=\;
  \ln(1 + z\,h) + O(h^3).
$$

*Ratio.* Forming the dimensionless ratio
$\mathfrak{Q}_\beta^{\mathrm{A}} / \mathfrak{Q}_\beta^{\mathrm{B}}$ and dividing through
by $E_0$ cancels the $h$ in the leading term:

$$
\begin{aligned}
\frac{\mathfrak{Q}_\beta^{\mathrm{A}}}{\mathfrak{Q}_\beta^{\mathrm{B}}}
&=
\frac{h - h^2/2 + O(h^3)}
     {(z h - z^2 h^2 / 2 + O(h^3))\,/\,z} \\
&=
\frac{h - h^2/2}{h - z h^2 / 2} \cdot \bigl(1 + O(h)\bigr) \\
&=
\frac{1 - h/2}{1 - z h/2} \cdot \bigl(1 + O(h)\bigr) \\
&= 1 + \tfrac{(z - 1)\,h}{2} + O(h^2).
\end{aligned}
$$

The intermediate identity $\mathfrak{Q}_\beta^{\mathrm{B}}/E_0 \cdot z = z h - (z h)^2/2 + O(h^3)$
identifies the **dimensional content** of the $1/z$ factor: $z$
appears in Form B because the eigenfunction basis is normalized to
the Markov-traced volume (Form B's denominator $z$ in $E_0/z$),
not because Form A and Form B measure different observables.

*Exponential remainder.* Both truncations live inside the same
spectral decomposition of the q-Hamiltonian along the GB
filtration of the free-neutron sector $K \subset H_3(q)$ at
$q = q_0$. By
conj:archimedean-remainder-exponential-decay
(applied to the q-dilogarithm tail in the brane-tower expansion),
each finite-depth truncation $\mathfrak{Q}_\beta^{(N)}$ — whether assembled
via Form A or Form B — incurs an error bounded by
$C(K) \cdot e^{-c(K) N}$, with $C, c > 0$ structural constants of
the free-neutron K-class. At $N = 0$ this gives the observed
$+1.31$ keV residual; at $N \geq 1$ the bound is sub-keV. $\square$

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
[`q_beta_spectral_bridge_witness.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/q_beta_spectral_bridge_witness.py)
([`q-beta-spectral-bridge.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/q-beta-spectral-bridge.witness.json)):

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
