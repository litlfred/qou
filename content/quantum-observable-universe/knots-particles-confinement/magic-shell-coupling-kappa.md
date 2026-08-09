*The per-unit-excess magic-shell coupling slope $\kappa$, which controls the $(n_{pp} - n_{nn})$ excess contribution to atomic binding at the single-magic anchors $(Z, N) = (2, 1)$ and $(1, 2)$, is conjectured to admit the closed categorical form*

$$
  \boxed{\,
  \kappa \;=\; -\,\frac{E_0 \cdot \log(1/h)}{[2]_q \cdot [3]_q}
  \,}
$$

*where $E_0 = m_e / (q(q-1))$ is the Hecke energy scale, $h = q - q^{-1}$ is the Hecke deformation parameter, and $[n]_q = (q^n - q^{-n}) / (q - q^{-1})$ is the q-bracket.*

## Why this is a conjecture and not a proposition

The shape of the right-hand side was not derived from the categorical substrate. Both of its factors were identified against the $(2,2)$ doubly-magic anchor: the magic-shell quantum $E_0 \cdot \log(1/h)$ and the normalization $[2]_q \cdot [3]_q$ were selected so that the expression reproduced the coupling slope measured there. An expression obtained that way is a fit, whatever the structural motivation attached to its factors afterwards.

The three-calibration discipline admits exactly three inputs — $m_e$, $\mathfrak{D}_\beta$, and $\mathfrak{D}_\pi$ — so there is no fourth calibration slot into which an anchor-identified form could be declared. That leaves two dispositions for a block of this kind, and only one of them is honest: demote it to a conjecture. The alternative, a provable block kind carrying an acknowledgement that its content was fitted, states a fit in the voice of a derivation.

What remains open is therefore not the arithmetic but the derivation: whether $-E_0 \log(1/h) / ([2]_q [3]_q)$ can be obtained from the substrate without consulting the anchor at all.

## Numerical evidence

Evaluating at the substrate parameter $q_0 = 1.109978595554181\ldots$:

$$
  \kappa_{\mathrm{categorical}} \approx -\frac{4.1860 \cdot 1.5651}{6.1206}
  \approx -1.0704239\;\text{MeV}
$$

Against the observed physical value at the single-magic anchors:

$$
  \kappa_{\mathrm{observed}} \approx -1.0707908\;\text{MeV}
$$

The ratio is $0.999657$, a relative residual of

$$
  \delta \;=\; \left| \frac{\kappa_{\mathrm{categorical}} - \kappa_{\mathrm{observed}}}{\kappa_{\mathrm{observed}}} \right|
  \;\approx\; 3.4 \times 10^{-4}.
$$

Two things are worth separating here. The anchors $(2,1)$ and $(1,2)$ were **not** used to fix the form — that was done at $(2,2)$ — so the agreement at them is a genuine cross-check rather than a restatement of the fit. That is the whole of the evidence for the conjecture. But $\delta \approx 3.4 \times 10^{-4}$ is not zero, and nothing in the present account says what it is. It is recorded here as an open quantity, not absorbed into the word "agreement": a derivation of the closed form would have to either predict $\delta$ or predict a corrected form that removes it.

## Structural motivation

The two factors carry the following readings, which motivate the shape but do not derive it.

1. **H7a energy quantum** $E_0 \cdot \log(1/h)$ — the per-shell magic-coupling magnitude, read as the logarithm of the Hecke deformation.
2. **q-deformed dimension product** $[2]_q \cdot [3]_q$ — the quantum dimension of the $V_2 \otimes V_3$ Schur–Weyl tensor product, normalizing the H7a quantum to a per-excess slope.

$$
  \kappa \;=\; \underbrace{-E_0 \cdot \log(1/h)}_{\text{H7a quantum}}
  \;\cdot\; \underbrace{\frac{1}{[2]_q \cdot [3]_q}}_{\text{LR-fusion normalization}}
$$

The negative sign tracks the orientation convention for the $(n_{pp} - n_{nn})$ excess. Unlike the shape itself, the sign is not fitted: it follows from $E_0 > 0$, $\log(1/h) > 0$ for $0 < h < 1$, and $[2]_q, [3]_q > 0$ at $q > 1$, and is proved in the Lean sibling as `kappaClosed_neg`.

## What would settle it

The conjecture is discharged by a derivation of the closed form from the substrate that does not consult a magic anchor at any step. Two structural facts already available constrain such a derivation: the sign is forced, as above; and the $q$-brackets appearing in the denominator are the canonical balanced brackets, tied to `QOU.QInteger.qIntBal` by `qBracket_eq_canonical` in the Lean sibling, so the normalization is not free to be reinterpreted as a geometric or rescaled bracket.
