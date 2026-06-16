# Δ_coupling closed-form: alternative substrate-derivation

**Date:** 2026-05-17
**Branch:** `claude/post-670-story-b-mp-c5-c6`
**Status:** Proposes a substrate-derivation pathway for the empirical
leading-form $\Delta_{\text{coupling}}(2,2) \approx (A-2) \cdot E_0 \cdot \log(1/h(q_0))$
that PR #644 / 2026-05-12-delta-coupling-leading-term-followup
identified at 0.71% gap.

## Where each factor comes from in QOU substrate

Decomposing the leading-form $(A-2) \cdot E_0 \cdot \log(1/h(q_0))$:

### Factor 1: $(A - 2)$ — excess nucleon-pair count

The factor $(A - 2)$ counts **excess strands beyond the seed nucleon
pair** in the multi-nucleon braid. For doubly-magic ⁴He at $(Z, N) = (2, 2)$:

- $A = Z + N = 4$
- $A - 2 = 2$ = number of nucleon-pairs the inter-nucleon brane tower
  stabilises beyond the base $\sigma_{p}, \sigma_{n}$ atoms

This is a **purely topological** quantity (strand count of the
canonical atomic braid in $B_{3A}$) — no substrate parameter
dependence. Per [`prop:atom-canonical-crossings`](#prop:atom-canonical-crossings)
the 3A-strand braid has exactly $A$ atom blocks plus $(A-1)$
inter-nucleon binding crossings; the "excess pair" count for
shell-stabilization is $A - 2$.

### Factor 2: $E_0 = m_e / (q(q-1))$ — Hecke energy unit

This is the **canonical Hecke energy scale** per
[`def:hecke-e0`](#def:hecke-e0). It is the QOU substrate's
natural unit of binding-energy density:

$$
  E_0(q_0) = \frac{m_e}{q_0 (q_0 - 1)} \approx 4.186 \text{ MeV}.
$$

Derived from CAL-1 ($m_e$) + CAL-2 ($q_0$) only; no fitting.

### Factor 3: $\log(1/h(q_0))$ — substrate-thermodynamic log

This is the factor whose **categorical origin** is the open question.
Numerical leading-form ($+0.71$% gap) uses $h = q - q^{-1}$ (skein
convention). Two complementary substrate-derivations are available:

**(i) Thermodynamic free-energy log via $\hbar_q$.** Per the QOU
[`def:boltzmann-constant`](#def:boltzmann-constant):
$$
  k_B \cdot T_q = \hbar_q = \frac{q - 1}{q}.
$$
The thermodynamic free-energy log at the Hecke-thermal scale is
$\log(1/\hbar_q) = \log(q/(q-1))$. At $q_0$:
$\log(1/\hbar_q(q_0)) \approx 2.312$.

The numerical leading-form uses $\log(1/h(q_0)) \approx 1.565$
instead. Relation: $h = q - q^{-1} = (q + 1)/q \cdot (q - 1) = (q + 1) \cdot \hbar_q$,
so $\log(1/h) = \log(1/\hbar_q) - \log(q + 1)$. At $q_0$:
$2.312 - 0.747 = 1.565 (exact match).

So:
$$
  \boxed{
  \log\frac{1}{h(q_0)} = \log\frac{1}{k_B T_q} - \log(q_0 + 1).
  }
$$

The leading factor $\log(1/(k_B T_q)) \approx 2.312$ is the **Shannon-
Boltzmann entropy** of the substrate thermal state per excess pair.
The subtractive term $\log(q_0 + 1) \approx 0.747$ is a substrate-
specific normalization that reduces the bare thermodynamic log to the
skein-convention $\log(1/h)$ form.

**(ii) Reeb operational entropy.** Per
[`def:operational-entropy`](#def:operational-entropy):
$$
  \eta_q = \frac{2q - 1}{q^3}.
$$
At $q_0$: $\eta_q(q_0) = 1.220 / 1.368 \approx 0.892$. This is **not
directly equal** to $\log(1/h(q_0))$, but the Manning-McCluskey
formula relates it to the Lyapunov: $\eta_q = d_H \cdot \chi_q =
((2q-1)^2/q^3) \cdot 1/(2q-1) = (2q-1)/q^3$. The relationship to
$\log(1/h)$ is via the Reeb-flow logarithm of the inverse exit-rate.

### Proposed categorical-derivation chain

$$
  \Delta_{\text{coupling}}(Z, N) \;\overset{?}{=}\;
  (A - 2) \cdot E_0 \cdot \Bigl[\log(1/(k_B T_q)) - \log(1 + q_0)\Bigr]
$$

with:
- $(A-2)$ from the canonical-atomic-braid strand-count topology
- $E_0$ from the Hecke energy unit (CAL-1 + CAL-2)
- $\log(1/(k_B T_q)) = \log(q_0/(q_0-1))$ from the QOU thermodynamic
  scale (def:boltzmann-constant)
- $\log(1+q_0)$ as a substrate normalization that completes the skein-
  convention form $h = q - q^{-1}$

All three factors trace to substrate primitives. The substrate-
derivation is:

> **Magic-shell stabilization energy at finite A** is the
> **thermodynamic free-energy correction** per excess nucleon pair,
> evaluated at the QOU Hecke-thermal scale $k_B T_q = \hbar_q$, with
> a skein-convention normalization $\log(1+q_0)$ accounting for the
> two-sided Hecke deformation.

## What remains open

1. **Cross-anchor verification**: the 0.71% gap at $(2, 2)$ may
   improve or degrade at $(2, 1)$ ³He=D+p and $(1, 2)$ T=D+n once
   PR #644's $\Delta_{\text{cat}}$ data for proton and neutron lands
   on main.

2. **Why $(A-2)$ exactly?** The substrate-derivation above takes
   $(A-2)$ as topological (excess strand count). A deeper categorical
   derivation would obtain it from operator-selection LP active-set
   cardinality at magic shells.

3. **Sign of the residual**: $\Delta_{\text{coupling}}(2,2) = +13.20$
   MeV (over-binding); leading-form predicts $+13.10$ MeV (slight
   under-prediction). The $+0.10$ MeV residual could be:
   - Next-order correction in the q-Edgeworth expansion (tested in
     `probe_delta_coupling_q_edgeworth.py`; κ_3 has WRONG SIGN, so
     not from leading q-skewness)
   - Higher-order term in the $\log(1/h)$ expansion
   - Substrate normalization correction beyond $\log(1+q_0)$

4. **Generalisation beyond $A = 4$**: at $A = 8, 16, 20, 28, …$
   (additional magic numbers) the $(A-2)$ factor would predict
   $\Delta_{\text{coupling}}$ values for $^{16}$O, $^{40}$Ca, etc.
   Empirical AME data exists for verification.

## Recommended next-PR scope

1. Verify the substrate-derivation $(A-2) \cdot E_0 \cdot [\log(1/(k_B T_q)) - \log(1+q_0)]$
   numerically (this probe — should equal the existing leading-form
   to within $10^{-15}$ since it's algebraically equivalent).
2. Cross-anchor verification on $(2, 1)$ and $(1, 2)$ once PR #644's
   $\Delta_{\text{cat}}$ data lands on main.
3. Write up the substrate-derivation as a content-block triple
   (`prop:delta-coupling-substrate-derivation`) once cross-anchor
   verification holds.
4. Lean formalization conditional on the categorical derivation
   completing.

## Cross-references

- [`def:hecke-e0`](../../content/quantum-observable-universe/braids-and-knots/hecke-e0.md) — E_0 definition
- [`def:boltzmann-constant`](../../content/quantum-observable-universe/information-theory/boltzmann-constant.md) — k_B = 1, k_B·T_q = ℏ_q
- [`def:operational-entropy`](../../content/quantum-observable-universe/information-theory/operational-entropy.md) — η_q = (2q-1)/q³
- [`conj:magic-shell-stabilization`](../../content/quantum-observable-universe/braids-and-knots/conj-magic-shell-stabilization.md) — the conjecture stating Δ_coupling exists
- [`2026-05-12-delta-coupling-leading-term-followup.md`](2026-05-12-delta-coupling-leading-term-followup.md) — original leading-form analysis
- [`probe_delta_coupling_q_edgeworth.py`](../../computations/probe_delta_coupling_q_edgeworth.py) — q-Edgeworth attempt
