**Definition (Quantum dilogarithm disambiguation).**
*Two distinct functions appear in the QOU mass formulae and must
not be conflated:*

| Name | Symbol | Closed form | Behaviour near $z = 1$ |
|---|---|---|---|
| **Quantum dilogarithm product** | $\Phi_q(z)$ | $\prod_{k=1}^{\infty} (1 - q^{-k}z)^{-1}$ | Unbounded ($\Phi_q(0.989) \approx 6.7 \cdot 10^5$ at $q_0$) |
| **Symmetric q-dilogarithm (Kashaev limit)** | $\mathrm{Li}_2^q(z)$ | $\sum_{n \geq 1} \dfrac{z^n}{n \cdot [n]_q}$ | Bounded; $-\mathrm{Li}_2^q(-z) \in [0.1, 0.82]$ for $z \in (0,1)$ at $q_0$ |

*The historical paper-level identity*

$$
  \Phi_q(z) \;\stackrel{?}{=}\; \int_0^z \frac{\ln_q(1+t)}{t}\,dt
       \;\stackrel{?}{=}\; \prod_{k\geq 1}(1 - q^{-k}z)^{-1}
$$

*is **false**: the integral evaluates to $-\mathrm{Li}_2^q(-z)$ (bounded),
not $\Phi_q(z)$ (unbounded). The two sides differ by 6 orders of
magnitude at $z = 0.989$ — see the
[mass-endomorphism-tower audit](#prop:mass-endomorphism-tower)
for the numerical probe and the $-737$ MeV mirror-nucleus pathology
that the conflation produced.*

## Discipline

**The corrected canonical form of the mass-endomorphism tower uses
$-\mathrm{Li}_2^q(-|V|)$, not $\Phi_q(|V|)$**, on every per-generator
amplitude. Two production compute paths follow this discipline:

- [`canonical_plus_multibrane.py`](computations/canonical_plus_multibrane.py)
  with `tower_mode="li2q"` — the canonical mass tower.
- [`paper_six_term_isotope_sweep.py`](computations/sweeps/paper_six_term_isotope_sweep.py)
  using the symmetric q-dilogarithm series identity.

The $\Phi_q$ product form survives in
[`brane_tower_isospin_diagnosis.py`](computations/brane_tower_isospin_diagnosis.py)
**only as a diagnostic** — it documents the $\sim 10^5 \times$
amplification at $|V| \to 1$ that originally produced the $-737$ MeV
pathology, but the corrected mass formula does not use it.

## Lean anti-regression class

The Lean stub
[`QOU.BraidKnot.QuantumDilogarithm`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/QuantumDilogarithm.lean)
provides:

- `phi_q : ℝ → ℝ → ℝ` — formal noncomputable def of the product form.
- `li2_q : ℝ → ℝ → ℝ` — formal noncomputable def of the symmetric q-dilog.
- `phi_q_ne_li2_q : ¬ (phi_q = fun q z => -li2_q q (-z))` — the two are
  not equal under the historical identity.
- `towerTerm q V := -li2_q q (-|V|)` — the **corrected** per-generator
  tower term.
- `class HasCorrectedMassEndomorphismTower` — type-level discipline:
  any instance must use `towerTerm`, not `phi_q`, as the archimedean
  specialisation.

Together with the production wiring, this discipline prevents the
$\Phi_q$ pathology from re-entering the mass formula.
