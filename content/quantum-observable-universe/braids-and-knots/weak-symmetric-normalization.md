**Proposition (weak-sector symmetric-channel Plancherel normalization).**

*Let $R$ be the categorical coefficient ring with $q \in R$ generic
(not a root of unity in $R$, $q \neq 1$). The
[weak-sector spectral completeness](#conj:weak-spectral-completeness)
identity*

$$
  e_W^{+} + e_W^{-} + e_Z^{+} + e_Z^{-} + e_H^{+} + e_H^{-}
  \;=\; \mathbf{1}_{H_2(q)}
$$

*assigns each EW projector $e_X^\pm$ ($X \in \{W, Z, H\}$) a
Plancherel weight $w_X^\pm = (\dim_q \mathrm{im}\, e_X^\pm)^2 /
[2]_q! \in R$. The **symmetric-channel normalization**
$\mathcal{N}_{\rm sym}(q) \in R$ is defined as the Frobenius-trace
ratio*

$$
  \mathcal{N}_{\rm sym}(q)
  \;:=\;
  \frac{\sum_{X \in \{W, Z, H\}} \tau\!\left( e_X^{+} \cdot
        \beta(T(2, 2k_X)) \cdot e_X^{+} \right)}
       {\sum_{X \in \{W, Z, H\}} w_X^{+}}
  \;\in\; R,
$$

*where $k_W = 2, k_Z = 3, k_H = 4$ are the even-twist parameters.
Equivalently, $\mathcal{N}_{\rm sym}(q)$ is the Plancherel-weighted
character product over the EW symmetric channel — exactly the analog
for the EW sector of [`prop:gram-determinant-plancherel-ratio`](#prop:gram-determinant-plancherel-ratio)
$\delta_{CS}(q)$ for the EM sector.*

### Statement (formal)

The Hecke algebra $H_2(q)$ over $R$ has Wedderburn decomposition
$H_2(q) \cong R e_+ \oplus R e_-$ with sym/alt block projectors

$$
  e_+ \;=\; \frac{\sigma_0 + q^{-1}}{q + q^{-1}},
  \qquad
  e_- \;=\; \frac{q - \sigma_0}{q + q^{-1}}.
$$

Per [`prop:even-twist-torus-link-psd-feasibility`](#prop:even-twist-torus-link-psd-feasibility),
$\sigma_0^{2k}$ acts as $q^{2k}$ on $e_+ H_2(q) e_+$ and as
$q^{-2k}$ on $e_- H_2(q) e_-$. The Frobenius trace satisfies

$$
  \tau(e_+) \;=\; \tau(e_-) \;=\; \frac{1}{[2]_q},
$$

(uniform across blocks since both are 1-dimensional). The
**symmetric channel** is the direct sum $e_W^+ \oplus e_Z^+ \oplus
e_H^+$ across the three even-twist parameters, and

$$
  \mathcal{N}_{\rm sym}(q)
  \;=\;
  \frac{\frac{1}{[2]_q}\,(q^4 + q^6 + q^8)}{\frac{3}{[2]_q}}
  \;=\;
  \frac{q^4 + q^6 + q^8}{3}
  \;=\;
  \frac{q^4 (1 + q^2 + q^4)}{3}.
$$

(One can equally express this as $q^6 \cdot [3]_{q^2} / 3$ where
$[3]_{q^2} = 1 + q^2 + q^4$ is the $q^2$-integer.) This is a
**closed-form $R$-element** with no free parameters once
[`conj:electroweak-higgs-torus-link-triplet`](#conj:electroweak-higgs-torus-link-triplet)
fixes $k \in \{2, 3, 4\}$.

### Numerical evaluation (for cross-checks)

At $q_0 \approx 1.10997859$ (50 dps):
- $q^4 \approx 1.5170$
- $q^6 \approx 1.8694$
- $q^8 \approx 2.3035$
- $\mathcal{N}_{\rm sym}(q_0) \approx (1.5170 + 1.8694 + 2.3035)/3 \approx 1.8966$

This is the **structural input** that the constrained-basis PSLQ
search for $N_v$ requires (Phase D of
`docs/audits/2026-05-05-path-alpha-bring-refinement.md`).

### Connection to the closed-form $N_v$ ansatz

Per the parallel pipeline with [`prop:alpha-em-categorical-trace`](#prop:alpha-em-categorical-trace),
the EW closed form for $N_v$ is conjecturally

$$
  N_v \;\stackrel{?}{=}\;
  \frac{[4]_q \cdot [6]_q \cdot [8]_q}{[2]_q^{\,a}}
  \cdot \mathcal{N}_{\rm sym}(q)^{\,b}
  \cdot (1 + \delta_{\rm EW}(q)),
$$

with $\delta_{\rm EW}(q)$ a small Plancherel correction (analog of
$\delta_{CS}$). Concrete exponents $a, b$ and the form of
$\delta_{\rm EW}$ are determined by the LP/SDP solve on the EW
sector + PSLQ uniqueness on the $\{[4]_q, [6]_q, [8]_q, [2]_q,
\mathcal{N}_{\rm sym}\}$ basis.

### Status

🟡 **Open** as a formal proposition. The closed-form expression
$\mathcal{N}_{\rm sym}(q) = q^6 \cdot [3]_{q^2} / 3 \in R$ is
straightforwardly derivable once
[`conj:weak-spectral-completeness`](#conj:weak-spectral-completeness)
is in place; the open inputs are:

1. **Discharge** the host-distinctness drop (this audit, §1) — done.
2. **Verify** the Frobenius-trace normalisation $\tau(e_X^\pm) =
   1/[2]_q$ is uniform across $X \in \{W, Z, H\}$ (follows
   mechanically from the projector formulas and Hecke relations,
   but should be authored as a small lemma).
3. **Connect** to the constrained-PSLQ ansatz: confirm that
   $\mathcal{N}_{\rm sym}(q)$ + the EW $[2k]_q$ basis suffices to
   reach CODATA-$G_F$ precision for $N_v$.

### Audit-flag impact

If $\mathcal{N}_{\rm sym}(q)$ is the right structural input,
**NV-1** closes:
$G_F = 1/(\sqrt{2} v^2)$ becomes a closed-form $R$-rational
expression in $\{q, [k]_q\}$ alone, with $v = N_v \cdot E_\times
\cdot \mu_0$ derived from the categorical EW spectral data.

**Audit doc.** [`docs/audits/2026-05-05-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-05-path-alpha-bring-refinement.md).
