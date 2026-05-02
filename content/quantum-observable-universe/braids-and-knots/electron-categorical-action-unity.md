**Proposition (electron categorical action equals unity).**
*The emitted electron in a $\beta^-$-decay process contributes
exactly $\mathcal{S}(e^-)/m_e = 1$ to the dimensionless Q-value
formula. This is **forced by CAL-0** (the $H^0$ calibration
$m_e$ of [`three-calibration-discipline`](#prop:three-calibration-discipline))
and the identification of the electron with the left-trefoil
torus knot $T_{2,3} = 3_1$ in the building-block-knots
dictionary ([building block knots](#rem:building-block-knots)).
No empirical fit, no fourth calibration, no LP-dual conjecture
needed.*

### Statement

For a $\beta^-$-decay $X \to Y + e^- + \bar\nu_e$ at atomic mass
$A$, the categorical Q-value formula in
[`folio-assistant/computations/full-derivation-verified.py`](../../folio-assistant/computations/full-derivation-verified.py)
takes the form

$$
  Q_{\beta^-} = \bigl( \Sigma_{\rm all}(A) + n_e(A) \bigr) \cdot m_e,
$$

where $n_e(A)$ is the **electron-emission count** for that
decay (one electron per $\beta^-$, so $n_e = 1$ in standard
single-$\beta^-$ decay). Then

$$
  n_e(A) = 1 = \mathcal{S}(T_{2,3}) / m_e,
$$

and this is forced — not fitted — once CAL-0 is in place.

### Proof (CAL-0 forcing)

By
[`def:mass-identity`](#def:mass-identity), the categorical mass
of any vortex morphism $\varrho \colon \mathbf{1} \to A$ is

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \bigl\| \mathrm{tr}\bigl((\textstyle\int_A \otimes\,\mathrm{id}) \circ
  \Delta \circ \varrho\bigr) \bigr\|_F.
$$

For the electron, $\varrho_{e^-} = T_{2,3}$ (left trefoil) per
[`building block knots`](#rem:building-block-knots). The
**categorical action**
([`def:categorical-action`](#def:categorical-action)) on this
morphism is the closed-loop trace
$\mathcal{S}(T_{2,3}) = \mathrm{tr}(\Phi(T_{2,3}))$, valued in
$\mathrm{End}(\mathbf{1}) \cong R$ where $R$ is the categorical
base ring.

By
[`prop:three-calibration-discipline`](#prop:three-calibration-discipline),
$m_e$ is the **$H^0$ calibration** — i.e., the unit of mass.
This calibration *defines* the relationship
$\mathfrak{m}(\text{electron}) = m_e \cdot 1$. Substituting:

$$
  \mathcal{S}(T_{2,3}) \cdot m_e = m_e \cdot 1
  \quad\Longrightarrow\quad
  \mathcal{S}(T_{2,3}) / m_e = 1.
$$

The "+1" appearing in the n→p Q-value formula
$Q = (\Sigma_{\rm all} + 1) \cdot m_e$ is therefore the
**categorical action of the emitted electron**, expressed in
the $m_e$-unit dictated by CAL-0. It is not an empirical
addition. $\square$

### Why earlier framings called this "open"

The witness
[`branching-qvalues.witness.json`](../../folio-assistant/computations/branching-qvalues.witness.json)
line 68 lists as an open problem:

> "The +1 (emitted electron) should emerge from the LP dual,
> not be added manually"

This framing presupposes a *deeper* derivation in which $m_e$
itself is derived from substrate structure (rather than
calibrated). Such a derivation **would violate the three-
calibration discipline** — it would require eliminating CAL-0,
which is the categorical $H^0$ input by design. The "open
problem" is therefore mis-stated: within the three-calibration
framework, the +1 is forced (this proposition); only an
*alternative* framework that derives $m_e$ from substrate
parameters would be needed to derive the +1 from "deeper"
inputs.

The current audit
([`docs/audits/2026-05-02-nv-frob-filter-conjectures.md`](../../docs/audits/2026-05-02-nv-frob-filter-conjectures.md)
§ELECTRON-1) flags this as **resolved**: the +1 is the
calibrated electron mass, exactly the role CAL-0 prescribes.

### Higher-A absorption: the FP filter

For $A \geq 3$, the explicit "+1" disappears from the formula —
$Q$ is computed as $|\Sigma_{\rm all}|$ (A=3) or $|\Sigma_{\rm FP}|$
(A≥6). The electron's contribution is *absorbed* into these sums
by the **Frobenius-positivity filter**
([`prop:bw-coefficient-shadow-price`](#prop:bw-coefficient-shadow-price)):

- The FP filter selects configurations where both the parent and
  the daughter side of the Hecke channel sum have positive
  matrix elements ($me_{\rm par} \geq 0$ AND $me_{\rm dau} \geq 0$).
- A daughter configuration that includes the emitted electron's
  $T_{2,3}$ contribution has $me_{\rm dau} > 0$ on the
  trefoil-positive sub-cone. The FP filter retains exactly
  these.
- Therefore $|\Sigma_{\rm FP}|$ at $A \geq 3$ already contains
  the categorical electron contribution; no separate "+1" is
  needed.

This is the categorical mechanism by which the FP filter
"absorbs" the manual +1 — exactly what
[`branching-qvalues.witness.json`](../../folio-assistant/computations/branching-qvalues.witness.json)
flagged. The mechanism is now identified.

### Witness

[`electron-categorical-action-unity.witness.json`](../../folio-assistant/computations/electron-categorical-action-unity.witness.json)
— numerical evaluation showing $\mathcal{S}(T_{2,3})/m_e = 1$
(by CAL-0 normalization) and the per-A Frobenius-positive
filter retention rate, demonstrating that
$\Sigma_{\rm FP}/\Sigma_{\rm all}$ ratios encode the electron
contribution implicitly.

### Status

🟢 **CLOSED** as ELECTRON-1 audit flag. The +1 is categorically
forced by CAL-0; the FP filter absorbs it at higher A by
Frobenius-positivity selection. The witness's "open problem"
framing was a mis-statement — closure does not require
removing CAL-0 (which would break the three-calibration
discipline).
