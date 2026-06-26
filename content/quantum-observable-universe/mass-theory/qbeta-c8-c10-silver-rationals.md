**Proposition ($\mathfrak{Q}_\beta$ c_8, c_9, c_10 closed-form values at the silver ratio).**

*At the silver ratio $q = 1 + \sqrt{2}$ where the Hoefsmit parameter takes
the exact rational value $b^2 = 7/8$, the closed-form $\mathfrak{Q}_\beta$ precision-ladder
coefficients $c_8$, $c_9$, $c_10$ extend the documented Pell-Lucas
$\sigma$-action pattern:*

$$
  c_8 = c_3^2 \cdot b^4 = 4 \cdot \left(\tfrac{7}{8}\right)^2
      = \tfrac{49}{16},
  \qquad
  c_9 = c_3^3 \cdot b^2 = -8 \cdot \tfrac{7}{8} = -7,
  \qquad
  c_{10} = c_3^2 \cdot b^6 = 4 \cdot \left(\tfrac{7}{8}\right)^3
         = \tfrac{343}{128}.
$$

*Each value matches the Pell-Lucas-clean prediction
(`is_pell_lucas_clean`-checked) recorded in the SDP-extraction witness
`qbeta-decay-sdp-extended-ck.witness.json` and is therefore a
PURE σ-action rung with no averaging-resonance $\tfrac{1}{2}$
fingerprint.*

## Why these values matter

The Pell-Lucas-clean classification at the silver ratio is the
**structural signal** for the $\mathfrak{Q}_\beta$ c_k precision ladder. Per the
SDP-extraction script's own caveat, the c_k values extracted at the
substrate anchor $q_0$ become noise-floor-dominated for $k \geq 8$;
the silver ratio is where the algebraic structure is visible.

The three closed forms extend the documented $c_4 = c_3 \cdot b^4$,
$c_6 = c_3^2 \cdot b^2$, $c_7 = c_3^3$ pattern by one rung in each
parity class.

## Lean proof structure

Three pure-rational identities, each closed by `norm_num`. The
Lean side fixes the silver-ratio $b^2 = 7/8$ as a `(7 : ℚ) / 8` constant
and computes the closed-form expression in rational arithmetic — no
transcendental or symbolic-q machinery required.

  - `qbeta_c8_at_silver`:  `4 * (7/8)^2 = 49/16`.
  - `qbeta_c9_at_silver`:  `-8 * (7/8) = -7`.
  - `qbeta_c10_at_silver`: `4 * (7/8)^3 = 343/128`.

All three closed by `norm_num` after expanding the closed-form
expression. The Lean theorems live as `Rat` equalities; they extend
to any field containing $\mathbb{Q}$.

## q-usage discipline

The silver ratio $q = 1 + \sqrt{2}$ is a real algebraic point
($q \in \mathbb{R}_{>0}$). The exact $b^2 = 7/8$ value arises from
the Hoefsmit q-rational evaluated at this $q$ (per the Pell-Lucas
companion-sequence identification). All three identities are
**fibre-level Laurent rationals** realised at a particular real
anchor: the identities hold over any field containing $\mathbb{Q}$ and
are specialised here to the silver-ratio rational point.

## Cross-references

- SDP-extraction witness with the Pell-Lucas check at the silver
  ratio: `qbeta-decay-sdp-extended-ck.witness.json` on `main`.
- Closed-form derivation probe + witness:
  `probes/qbeta_c8_c10_closed_form_predictions.py`.
- Closed-form wiring outcome at $q_0$ (companion empirical probe):
  `probes/qbeta_closed_form_wiring_n4_to_n10.py`.
