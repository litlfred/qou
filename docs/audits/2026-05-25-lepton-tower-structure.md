# Lepton tower algebraic structure — T(2, 2m+1) family + categorical dual (2026-05-25)

**Branch**: `claude/gifted-feynman-U7ckD` → [#1127](https://github.com/litlfred/qou/pull/1127)
**Triggered by**: owner directive "implication for Im(q) being lepton_mass_ratio for muon/tau... is this because we walking up lepton tower from q=m_μ/m_e guess? or something else? is there an additional algebraic structure on lepton tower we are not exploring yet? maybe use categorical dual to get that structure?"
**Status**: identifies a real underused structure; opens a concrete probe path

## The lepton tower as T(2, 2m+1) torus-knot family

### What the framework currently has

| Lepton | Braid identification | Source |
|---|---|---|
| Electron | $\sigma_1^3$ = trefoil = T(2, 3) | `mass-endomorphism-tower.md` line 351 |
| Muon | figure-eight $(\sigma_1\sigma_2^{-1})^2 = 4_1$ | `skein-mass-relation.md` line 32 (CANONICAL) |
| Muon (alt, since corrected) | cinquefoil $\sigma_1^5$ = T(2, 5) | `knot-volumes.py:67-73` (was muon, now W boson) |
| Tau | septafoil $\sigma_1^7$ = T(2, 7) | `knot-volumes.py:84-91` |

**Structural inconsistency**: electron and tau are 2-strand torus knots T(2, 2m+1) for m=1, 3; muon is a 3-strand non-torus hyperbolic knot.

### The underused structure (PR #1153 framework)

PR #1153 (sinh-bar-antisymmetric-partner-probe) derived for T(2, 2m+1):

$$P_m(\eta) = \frac{\cosh((2m+1)\eta)}{2 \cosh \eta}, \qquad Q_m(\eta) = \frac{\sinh((2m+1)\eta)}{2 \cosh \eta}$$

with $\eta = \log q$. P_m is bar-symmetric (P_avg, mass channel); Q_m is bar-anti-symmetric (P_skew, EM channel).

For m=1 (trefoil/electron, T(2,3)), m=2 (cinquefoil, T(2,5)), m=3 (septafoil, T(2,7)) — **the natural odd-index torus-knot tower is m=1, 2, 3 for e, μ, τ**.

If muon = T(2,5) instead of 4_1, the framework's lepton-tower mass formula would be uniform:

$$\frac{m_\ell}{m_{\ell-1}} = \frac{P_m(\eta_0)}{P_{m-1}(\eta_0)} = \frac{\cosh((2m+1)\eta_0)}{\cosh((2m-1)\eta_0)}$$

At $q_0 \approx 1.10998$, $\eta_0 \approx 0.10434$:
- $P_1(\eta_0) = \cosh(3 \eta_0) / (2\cosh\eta_0) \approx 0.5552$ (electron base)
- $P_2(\eta_0) = \cosh(5 \eta_0) / (2\cosh\eta_0) \approx 0.5872$ (cinquefoil/"muon"?)
- $P_3(\eta_0) = \cosh(7 \eta_0) / (2\cosh\eta_0) \approx 0.6373$ (septafoil/tau?)

**Ratios via this LO Skein-style formula DO NOT match CODATA**:
- $P_2/P_1 = 1.058$ vs CODATA $m_\mu/m_e = 206.77$  → **MASSIVE shortfall**
- $P_3/P_1 = 1.148$ vs CODATA $m_\tau/m_e = 3477.23$  → **MASSIVE shortfall**

So the bare $P_m$ ratios do NOT give lepton mass ratios. There's an additional structural factor missing — the `ξ_ℓ(q)` from [`conj:lepton-mass-tower-canonical`](../../content/quantum-observable-universe/braids-and-knots/lepton-mass-tower-canonical.md).

### Conjecture: T(2, 2m+1) tower + ξ_m(q) prefactor

The canonical lepton mass formula might be:

$$F_\ell(q) = \xi_m(q) \cdot P_m(\eta) \quad \text{where } m = \text{lepton tower index}$$

with $\xi_m(q)$ as the (lepton-sector) dimensional factor satisfying:
- $\xi_0(q) = 1$ (calibration, electron)
- $\xi_m(q_0) \cdot P_m(\eta_0) / P_0(\eta_0) = $ CODATA $m_\ell / m_e$

This is the lepton variant of `conj:lepton-mass-tower-canonical` made concrete on the T(2, 2m+1) tower.

## Categorical dual structure

### Bar-involution as categorical dual

In the Hecke algebra $H_n(q)$, the **bar involution** $\sigma_i \mapsto \sigma_i^{-1}$ is a ring anti-involution that flips:
- $L_+ \leftrightarrow L_-$ (positive/negative crossing)
- T(2, 2m+1) $\leftrightarrow$ T(2, -(2m+1)) (orientation reversal)
- $P_m \leftrightarrow P_m$ (bar-symmetric, invariant)
- $Q_m \leftrightarrow -Q_m$ (bar-anti-symmetric, flips sign)

The categorical dual of a braid $\beta$ is its bar-conjugate $\bar\beta$. For torus knots T(2, n), the dual is T(2, -n) — same underlying knot but opposite chirality.

### What the dual gives for the lepton tower

| Operation | Action on m-index | Action on Q_m / P_m | Action on Im(q) |
|---|---|---|---|
| Identity | $m \to m$ | $P_m, Q_m$ preserved | $\mathrm{Im}(q) \to \mathrm{Im}(q)$ |
| Bar / dual | $m \to m$ (same knot) | $P_m \to P_m$, $Q_m \to -Q_m$ | $\mathrm{Im}(q) \to -\mathrm{Im}(q)$ |
| Charge conjugation | $m \to m$ (mass unchanged) | mass-sector $P_m$ invariant; EM-sector $Q_m$ flips | matches bar |
| Parity inversion | depends on orientation | depends on lift | possibly via Im(q) flip |

The bar / dual operation **fixes m** (lepton mass tower index unchanged) and **fixes the mass channel** ($P_m$ invariant), but **flips the EM channel** ($Q_m$) and **flips Im(q)**. This is **consistent with bar-involution being charge conjugation / CP** at the lepton-tower level.

### Im(q) connection

Per [`conj:im-q-physical-role`](../../content/quantum-observable-universe/braids-and-knots/conj-im-q-physical-role.md) candidate (i) chirality/orientation:

$\mathrm{Im}(q) \neq 0$ ↔ off-real-axis position in q-plane ↔ chirality / orientation parameter

The bar involution flips $\mathrm{Im}(q)$ (since $\bar q = q^{-1}$ for real $q$, but $\bar{(u+iv)} = (u-iv)^{-1}$ for complex; modulus-projection invariant under conjugation). So:

- For real $q_0$: $\mathrm{Im}(q) = 0$ is the self-dual axis. Both lepton chiralities give the same mass (modulus projection).
- For complex $q$ with $\mathrm{Im}(q) \neq 0$: the bar / dual operation takes $q \to \bar q$ (different complex value); chiralities are distinct.

**Concrete statement**: $\mathrm{Im}(q)$ is the categorical-dual-orbit parameter on the lepton tower. Walking up the lepton tower via $m \to m+1$ (e.g. e → μ → τ) is ORTHOGONAL to walking around the dual orbit via $\mathrm{Im}(q)$.

## Implications for the user's question

**"Is Im(q) affecting lepton_mass_ratio because we walk up the tower from q = m_μ/m_e guess?"**

NO — the m-index walk (along the tower) and the Im(q) walk (around the dual orbit) are **independent** directions. The m-index changes the lepton; Im(q) changes the chirality/orientation (categorical-dual position). They commute structurally.

**"Is there additional algebraic structure?"**

YES — the T(2, 2m+1) torus-knot tower + bar-involution dual orbit forms a **2D parameter space**:
- m-axis: lepton index (e=1, μ=2 if T(2,5), τ=3)
- Im(q)-axis: dual / chirality coordinate

The canonical paper currently:
- Uses the m-axis at the wrong knot for muon (4_1 instead of T(2,5))
- Sets the Im(q) axis to 0 by convention

**"Categorical dual structure?"**

The bar-involution IS the categorical dual. It's used (in `bar-involution.md`, PR #1153, PR #1196). But the COUPLING between the m-walk and the dual-walk is unexplored. This is the new structure the user is suggesting.

## Concrete probe path

### Probe 1 — fit cinquefoil-as-muon hypothesis

Recompute m_μ/m_e using muon = T(2, 5) = cinquefoil instead of 4_1:
- Compute $|tr_M(\sigma_1^5)|$ in $H_2$ at q_0 (closed form via torus_knot_odd_reduction_exists Lean theorem)
- Compare ratio $|tr_M(σ_1^5)|/|tr_M(σ_1^3)|$ to CODATA m_μ/m_e
- Identify the ξ_2(q_0) needed to close

### Probe 2 — m-walk consistency check

Using the same ξ_m formula (whatever it turns out to be), check whether ξ_3 · P_3 / P_1 matches CODATA m_τ/m_e = 3477.23 at q_0:
- Same q_0 (fixed by CAL-2)
- Same ξ_m formal structure (whatever Probe 1 finds)
- Different m (3 instead of 2)
- Should give 3477.23 if the lepton tower is the correct structure

### Probe 3 — Im(q) chirality test

For a chirality-sensitive observable (e.g., parity-violating decay), check whether the prediction depends on Im(q):
- Compute prediction at real q_0 (current default)
- Compute prediction at q_0 + iδ for small δ
- If they differ, Im(q) HAS physical content as chirality
- If they're identical (modulus invariance), Im(q) is unphysical for that observable

Probe 1 + 2 are 2-4 hours of compute. Probe 3 requires a chirality observable definition (not in the framework).

## Resolution path for the framework

If Probe 1 + 2 succeed (i.e., muon = T(2,5) and the same ξ formula works for tau):

1. **Reframe muon = T(2,5)** in `skein-mass-relation.md` (currently 4_1). This would resolve the muon-knot-id conflict.
2. **Promote `conj:lepton-mass-tower-canonical`** to a theorem with explicit ξ_m(q) form.
3. **The "4_1 = muon" identification was an early-framework artifact** that the T(2, 2m+1) tower discipline resolves.

If Probe 1 fails (T(2, 5) doesn't give muon mass):

1. The muon = 4_1 identification stands.
2. The framework's lepton tower is NOT uniformly T(2, 2m+1) — it's {e, τ} on the torus tower with μ as an outlier on a different knot type.
3. The "structural inconsistency" is real, not an artifact.

Either outcome is informative.

## Lean status

`lepton-mass-tower-canonical.lean` (commit pending) adds:
- `torus_knot_odd_reduction_exists` theorem PROVED by induction: for any m ∈ ℕ, $\sigma^{2m+1} = P_m \cdot \sigma + Q_m$ for some $P_m, Q_m \in R$. This is the recursive closed form underlying PR #1153's P_m / Q_m identities.
- `lepton_tower_index` definition: e → 1, μ → 2 (cinquefoil candidate), τ → 3
- `lepton_tower_index_injective` theorem PROVED via `cases`
- `lepton_mass_ratio_electron_eq_one` PROVED by rfl

## Cross-references

- [`conj:lepton-mass-tower-canonical`](../../content/quantum-observable-universe/braids-and-knots/lepton-mass-tower-canonical.md) — F_ℓ conjecture
- [`conj:im-q-physical-role`](../../content/quantum-observable-universe/braids-and-knots/conj-im-q-physical-role.md) — Im(q) candidate roles
- [`rem:im-q-vs-p-skew`](../../content/quantum-observable-universe/braids-and-knots/rem-im-q-vs-p-skew.md) — bar vs modulus mechanisms
- [`docs/audits/2026-05-24-muon-knot-id-conflict.md`](2026-05-24-muon-knot-id-conflict.md) — muon ID dispute (4_1 vs 5_1)
- Sibling PR #1153 — P_m / Q_m for T(2, 2m+1), `tanh((2m+1) η_0)` table
- `mass-endomorphism-tower.md` — electron as σ_1³ identification
- `knot-volumes.py` — tau as T(2, 7); now muon = 4_1 with cinquefoil = W boson
