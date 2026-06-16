# ρ_F · V_hyp inversion analysis (interpretive, NOT a 1ppb gate)

**Status.** Interpretive audit (Layer 4 of
[`onepb-status-dashboard.md`](onepb-status-dashboard.md)).
**Witness:**
[`rho-f-volume-binding-gap.witness.json`](https://github.com/litlfred/qou/blob/main/computations/rho-f-volume-binding-gap.witness.json).

**Script.** [`rho_f_volume_binding_gap.py`](https://github.com/litlfred/qou/blob/main/computations/rho_f_volume_binding_gap.py).

## Position in the audit stack

QOU's structural prediction is the LP dual + GB NF stack
(Layer 1 of the 1ppb dashboard).  This audit lives in **Layer 4
(empirical AME data, informational only)** — it inverts the
`E_binding = ρ_F · V_hyp` relation against AME's Δ_binding column
to ask: "what V_hyp / ρ_F would each isotope need under
[`rem:frobenius-packing-density`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/particle-interactions/frobenius-packing-density.md)
for the simplest atomic-link-primitive candidates?"

This is an **interpretive** question — does the QOU LP-dual
shadow-price machinery *also* reproduce empirical nuclear
binding? — not a **structural-prediction** gate.  QOU does not
curve-fit against AME.  The 1ppb gate lives in Layers 1–3 of
the dashboard.

## Why this exists

`atom_mass_additive_baseline.py` reports the per-isotope nuclear
binding energy $\Delta_{\text{binding}}(A, Z)$ as the residual
between the additive constituent baseline
$Z M_p + N M_n + Z M_e$ and AME2020.
[`rem:frobenius-packing-density`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/particle-interactions/frobenius-packing-density.md)
predicts this binding to be the product

$$
  E_{\text{binding}}(K) \;=\; \rho_F(K) \cdot V_{\text{hyp}}(K),
$$

with $\rho_F \in \{m_e,\,2 m_e\}$ from Type-B fold-orbit closure
([`prop:cpt-orbit-closure-density`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/particle-interactions/cpt-orbit-closure-density.md))
and $V_{\text{hyp}}$ the Thurston volume of the atomic-link
complement.

This script inverts the law: given empirical $\Delta_{\text{binding}}$
and SnapPy-known $V_{\text{hyp}}$ for the available link primitives
(figure-eight, three-twist, Borromean), it reports the **required
$\rho_F / m_e$** that each candidate would need.  Complementary to
`atomic_mass_via_rho_k.py` on main, which evaluates a related
$\rho_K \cdot m_e \cdot |\mathrm{tr}_M(K)|$ density formula
*directly* rather than inverting the law.

## Findings

| isotope | A | Δ_binding (MeV) | ρ/m_e via 4_1 | ρ/m_e via 5_2 | ρ/m_e via 6³_2 |
|---------|---|-----------------|---------------|----------------|------------------|
| ⁴He     | 4 |  28.296         |   27.28       |   19.58        |    7.56          |
| ⁷Li     | 7 |  39.244         |   37.83       |   27.16        |   10.48          |
| ⁹Be     | 9 |  58.165         |   56.08       |   40.25        |   15.53          |
| ¹²C     |12 |  92.161         |   88.85       |   63.77        |   24.61          |
| ¹⁶O     |16 | 127.619         |  123.03       |   88.31        |   34.08          |
| ²⁰Ne    |20 | 160.650         |  154.88       |  111.16        |   42.90          |

**Match count within ±10% of $\rho_F \in \{m_e, 2 m_e\}$: 0.**

So no single link primitive reproduces $\Delta_{\text{binding}}$
under a clean $\rho_F \in \{m_e, 2 m_e\}$ assumption.  Two
non-mutually-exclusive interpretations:

1. **Atomic links are composites.** The atomic-link
   $K_{(A, Z)}$ is built from many primitive links (e.g. one
   Borromean per nucleon triple).  Required $V_{\text{hyp}}$ would
   then scale roughly with $A$ or $\binom{A}{2}$.

2. **$\rho_F$ takes a different value at the binding scale.** If
   the QOU formula is exact but $\rho_F$ is parametrised by
   per-nucleon character data rather than a strict $\{m_e, 2 m_e\}$
   dichotomy, the bound state's "effective" $\rho_F$ could land
   anywhere in $[m_e,\,160 m_e]$.

## What this audit does NOT do

This is **not** a 1ppb gate.  Closing the gap is not a
prerequisite for QOU's structural correctness — the LP-dual
shadow prices `y_λ*` from
[`prop:operator-selection-lp`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/operator-selection-lp.md)
are the QOU prediction for which Wedderburn blocks the bound
state saturates.  Whether those LP-active blocks *also* match
AME's empirical nuclear binding is an interpretive question.

## What this audit IS useful for

If the interpretive question is positively answered, this audit
becomes the validation table.  Three follow-on inputs would
turn it into a closure check:

1. **Atom→atomic-link map.** A canonical assignment $(A, Z)
   \mapsto K_{(A, Z)}$ recording the JSJ-decomposed link
   complement for each isotope.  Paper-side content.

2. **SnapPy V_hyp for each $K_{(A, Z)}$.** For the simplest
   cases (Hopf link $\to$ deuteron, Borromean $\to$ ³He, …),
   the values are tractable.

3. **$\rho_F$ link to LP active set.** If $\rho_F$ is determined
   by the LP-active set's Type-B fold-orbit closure
   (`prop:cpt-orbit-closure-density`), then $\rho_F \in
   \{m_e, 2 m_e\}$ is fixed by structural data already in
   Layer 1 of the dashboard, and the V_hyp side is the only
   degree of freedom.

Once those land, the witness this script emits becomes the
per-isotope check that the interpretive question has been
answered.  Until then, it is informational only.

## How to update

```bash
cd computations
python3 atom_mass_additive_baseline.py    # refresh Δ_binding column
python3 rho_f_volume_binding_gap.py        # invert ρ_F · V_hyp
```

The output's `matches_within_10pct` field is the bound for which
isotopes are explained by a single link primitive at canonical
$\rho_F$.  When the atom→link map lands and that field becomes
non-empty for the simplest isotopes, the next step is wiring
predictions back into `codata-reconciliation.witness.json` as
non-anchor rows.
