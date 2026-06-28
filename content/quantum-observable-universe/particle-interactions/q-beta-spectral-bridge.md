**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark) — $\mathfrak{Q}_\beta$ spectral bridge).**

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
