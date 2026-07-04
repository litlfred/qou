**Proposition (Magic-shell coupling slope — categorical closed form).**
*The per-unit-excess magic-shell coupling slope $\kappa$, which
controls the $(n_{pp} - n_{nn})$ excess contribution to atomic
binding at single-magic anchors $(Z, N) = (2, 1)$ and $(1, 2)$,
admits the closed categorical form*

$$
  \boxed{\,
  \kappa \;=\; -\,\frac{E_0 \cdot \log(1/h)}{[2]_q \cdot [3]_q}
  \,}
$$

*where $E_0 = m_e / (q(q-1))$ is the Hecke energy scale, $h = q - q^{-1}$
is the Hecke deformation parameter, and $[n]_q = (q^n - q^{-n}) / (q - q^{-1})$
is the q-bracket.*

## Numerical verification at $q_0$

Evaluating at the substrate parameter $q_0 = 1.109978595554181\ldots$ (50 dps):

See [Table](#tbl:magic-shell-coupling-kappa-table-data).

$$
  \kappa_{\mathrm{categorical}} = -\frac{4.1860 \cdot 1.5651}{6.1206}
  \approx -1.0704239\;\text{MeV}
$$

Against the observed physical value from v6 single-magic anchor data:

$$
  \kappa_{\mathrm{observed}} \approx -1.0707908\;\text{MeV}
$$

The ratio is $0.999657$ — **within $0.034\%$** at the single-magic
anchors. The *numerical* inputs are substrate parameters ($m_e$,
$q_0$) and structural q-brackets; the *form* of the closed
expression — the $E_0 \cdot \log(1/h)$ magic-shell quantum and the
$[2]_q \cdot [3]_q$ normalization — was identified empirically against
the $(2,2)$ doubly-magic anchor (an **acknowledged CAL-4 shape
selection**; see §"Structural interpretation"). The $0.034\%$
agreement at the single-magic $(2,1)$ / $(1,2)$ anchors is therefore a
**near-match cross-check** of that anchor-identified form, not a
zero-parameter prediction.

## Structural interpretation

The closed form decomposes into two pieces:

1. **H7a energy quantum** $E_0 \cdot \log(1/h)$ — the per-shell
   magic-coupling magnitude, motivated structurally as the logarithm
   of the Hecke deformation and identified empirically against the
   doubly-magic anchor $(2, 2)$ (acknowledged CAL-4; the original
   verifier `computations/probe_kappa_categorical_h7a_closed.py` is no
   longer in the tree — a re-derivation / fresh witness is pending).
   This is the candidate "magic-shell energy unit" of the categorical
   substrate.

2. **q-deformed dimension product** $[2]_q \cdot [3]_q$ — the
   quantum dimension of the $V_2 \otimes V_3$ Schur–Weyl tensor
   product, which is the relevant LR fusion multiplicity for
   $A = 3$ single-magic anchors. The product normalizes the H7a
   quantum to the per-(n_{pp} - n_{nn}) excess slope.

Putting these together:

$$
  \kappa \;=\; \underbrace{-E_0 \cdot \log(1/h)}_{\text{H7a quantum}}
  \;\cdot\; \underbrace{\frac{1}{[2]_q \cdot [3]_q}}_{\text{LR-fusion normalization}}
$$

The negative sign tracks the orientation convention for the
$(n_{pp} - n_{nn})$ excess in
[`prop:compound-beta-shell-calibration`](#prop:compound-beta-shell-calibration).

## Closure of the κ derivation work-item

This proposition supplies a categorical *form* for the κ derivation
requested in user work-list item #4. The observed
$\kappa \approx -1.07\;\text{MeV}/\text{excess}$ from v6 is reproduced
to $0.034\%$ at the single-magic anchors by a structurally-motivated
expression whose magic-shell quantum $E_0 \cdot \log(1/h)$ was
identified at the $(2,2)$ doubly-magic anchor (acknowledged CAL-4).
Full closure — a parameter-free derivation of that quantum purely from
$q_0$, with a fresh verifying witness replacing the removed probe
script — remains open.
