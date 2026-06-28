**Conjecture (canonical lepton-mass tower).**
*Let $\ell \in \{\mathfrak{e}, \mu, \tau\}$ be a charged lepton with
canonical braid representative $K_\ell$ (electron $K_\mathfrak{e} = \sigma_1^3$
in $H_2(q)$; muon $K_\mu = (\sigma_1\sigma_2^{-1})^2$ in $H_3(q)$; tau analogously).
There exists a categorical formula*

$$
\mathfrak{m}(K_\ell)
\;=\;
m_e \cdot \mathcal{F}_\ell(q)
$$

*expressing the lepton mass as a per-braid Markov-trace-weighted sum
over $K_\ell$'s braid representative, evaluated entirely within the
canonical [`per-braid mass tower`](per-braid-mass-tower.md), WITHOUT
invoking the SUPERSEDED scalar substrate density $\rho_q = 1/\hbar_q^2$
as a dimensional factor.*

## Motivation

The atomic graded expansion
[`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md) gives the
canonical mass formula for nuclei:

$$
m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)| \cdot \rho_K
\;=\;
\underbrace{Z m_\mathfrak{p} + N m_\mathfrak{n} + Z m_e}_{\rho_K^{\mathrm{LO}}\text{-piece}}
\;+\;
\tfrac{\alpha}{2} \sum_i \ln\bigl(\hat V_i^{\mathrm{full}} \cdot \overline{\hat V_i^{\mathrm{full}}}\bigr)
\;+\;
\tfrac{\alpha z^2}{2} \sum_{i<j} \ln\bigl(\hat V_i \hat V_j \cdot \overline{\hat V_i \hat V_j}\bigr)\!\big|_{\mathrm{Wedderburn}}
\;+\;\dots
$$

For a **lepton** (single-particle, no nucleon constituents), $Z = N = 0$
in the nuclear sense, so the LO piece is **zero**. The atomic graded
expansion does not apply to leptons; a separate canonical formula is
needed.

The current operative formula for leptons is the **Skein formula**:

$$
\frac{m_\mu}{m_e}
\;\stackrel{\text{LO}}{=}\;
\frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
$$

([Skein mass relation](../../observations/skein-mass-relation.md)),
but this uses:

1. **Hyperbolic volume Vol(4_1) $\approx$ 2.0299** — the **Kashaev $q \to 1$
   limit** of $|\mathrm{tr}_M(4_1)|$, not the value at $q_0$.
2. **Dimensional factor $1/\hbar_q^2$** — the **SUPERSEDED** scalar
   substrate density per
   [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md).
3. **Electron as calibration unit** — $m_e$ is CAL-1; the electron's
   own Markov trace does not appear.

## Phase 3 finding

Per audit
[`docs/audits/-m-mu-over-m-e-operator-rederivation.md`](../../../docs/audits/-m-mu-over-m-e-operator-rederivation.md),
the direct operator-level ratio at the substrate $q_0 \approx 1.10998$
is:

| Quantity | Value | Source |
|---|---:|---|
| $\|\mathrm{tr}_M((\sigma_1\sigma_2^{-1})^2)\|$ (muon, figure-eight) | $0.1995$ | algebraic reduction in $H_3(q)$ |
| $\|\mathrm{tr}_M(\sigma_1^3)\|$ (electron, trefoil) | $0.7302$ (conv A) | algebraic reduction in $H_2(q)$ |
| **Direct ratio** | $0.2732$ | quotient |
| CODATA $m_\mu/m_e$ | $206.7683$ | empirical |
| Skein LO $\mathrm{Vol}(4_1)/\hbar_q^2$ | $206.7683$ | matches CODATA |

**The direct Markov-trace ratio is ~0.27 — three orders of magnitude
smaller than CODATA.** This confirms that the Skein formula is a
Kashaev-LIMIT identity (using hyperbolic volumes + SUPERSEDED $\rho_q$),
**NOT** a direct operator-level ratio.

## Conjectural form

The canonical $\mathcal{F}_\ell(q)$ is expected to have the structure

$$
\mathcal{F}_\ell(q)
\;\stackrel{\text{conj}}{=}\;
\xi_\ell(q) \cdot \mathrm{Vol}_q^{\mathrm{tower}}(K_\ell)
$$

where:

- $\mathrm{Vol}_q^{\mathrm{tower}}(K_\ell) \in \mathbb{Z}[q^{1/2}, q^{-1/2}]$
  is the per-braid q-volume of the lepton's braid (computable via the
  per-braid mass tower at finite $q$, NOT a hyperbolic-volume limit).
- $\xi_\ell(q)$ is a **lepton-sector dimensional factor** replacing the
  SUPERSEDED $1/\hbar_q^2$. Its explicit form is **OPEN**.

In the Kashaev $q \to 1$ limit, $\mathrm{Vol}_q^{\mathrm{tower}}(K_\ell) \to
\mathrm{Vol}_{\mathrm{hyp}}(K_\ell)$ (per the Kashaev volume conjecture),
recovering the Skein formula's hyperbolic volume. The OPEN question is
the explicit form of $\xi_\ell(q)$ at substrate $q_0$, and how it
differs from the SUPERSEDED $1/\hbar_q^2$.

## Properties of the conjectural formula

1. **Im(q) robustness.** By the modulus-projection argument
   ([`prop:categorical-mass-markov`](categorical-mass-markov.md)),
   both numerator and denominator of $\mathcal{F}_\mu(q)/\mathcal{F}_e(q)$
   are $|\cdot|$-projected; the ratio is real-valued and insensitive
   to $\mathrm{Im}(q)$ at leading order.
2. **Bar covariance.** Per
   [`bar-involution.md`](bar-involution.md), the canonical projection
   is `P_avg` (bar-symmetric). The conjectural $\mathcal{F}_\ell(q)$
   must be bar-symmetric (in $P_{\mathrm{avg}}$); the SUPERSEDED
   $1/\hbar_q^2$ is NOT bar-covariant (becomes $q^2/\hbar_q^2$ under
   bar), which is one structural reason it's superseded.
3. **Kashaev recovery.** $\mathcal{F}_\ell(q) / \mathrm{Vol}(K_\ell) \to
   \xi_\ell(q \to 1)$ should give the Skein formula's dimensional factor
   in the appropriate limit, providing a constraint on $\xi_\ell$'s
   form.
4. **Three-calibration consistency.** $\mathcal{F}_e(q_0) = 1$ by
   construction ($m_e$ is the calibration unit). $\mathcal{F}_\mu(q_0)
   = 206.7683$ matches CODATA. The OPEN piece is whether the same
   formal $\mathcal{F}_\ell$ correctly predicts $\mathcal{F}_\tau(q_0)
   = m_\tau/m_e = 3477.23$ (CODATA 2022).

## Derivation paths (queued as open work)

| Path | What | Cost |
|---|---|---|
| **A** | Derive $\xi_\ell(q)$ analytically from the per-braid mass tower applied to each lepton's braid; identify how the SUPERSEDED $\rho_q$ emerges as the Kashaev limit | 1-2 days analytical |
| **B** | Compute $|\mathrm{tr}_M(K_\ell)|$ at substrate $q_0$ + tower corrections; fit a functional form for $\xi_\ell$ that matches CODATA for all 3 leptons; check consistency | 4-6 hours canonical |
| **C** | Bypass: postulate $\xi_\ell$ as the Kashaev-limit identity (equivalent to keeping the Skein formula as the operative LO) | done (current state) |

The Phase 3 audit conjecturally identifies path (A) as the substantive
analytical direction; path (B) is a complementary empirical check.

## Lean formalization

The Hecke-algebra reductions used in the audit are pure algebra and can
be Lean-formalized:

```lean
namespace QOU.BraidKnot.LeptonMassTowerCanonical

-- Setup: Hecke algebra H_n(q) with parameter q (substrate-generic)
variable {R : Type*} [CommRing R] (q : R) (h z : R)
  (hh : h = q - q⁻¹) (hz : z * (q^(1/2 : ℚ) + q^(-(1/2 : ℚ))) = 1)

/-- The conjectural lepton mass formula. -/
noncomputable def lepton_mass_ratio (ℓ : LeptonType) : R := sorry
  -- Ref: [manuscript] conj:lepton-mass-tower-canonical

/-- Im(q) robustness at leading order. -/
theorem lepton_mass_ratio_im_q_invariant
    {R : Type*} [Field R] [Invo R] (q : R)
    (ℓ : LeptonType) :
    lepton_mass_ratio q ℓ = lepton_mass_ratio (conj q) ℓ := by
  sorry  -- Ref: [manuscript] conj:lepton-mass-tower-canonical, property 1

end QOU.BraidKnot.LeptonMassTowerCanonical
```

## Cross-references

- [`docs/audits/-m-mu-over-m-e-operator-rederivation.md`](../../../docs/audits/-m-mu-over-m-e-operator-rederivation.md) — Phase 3 finding (the audit this conjecture answers)
- [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md) — the SUPERSEDED ρ_q purge that motivates the lepton re-derivation
- [`docs/audits/-muon-knot-id-conflict.md`](../../../docs/audits/-muon-knot-id-conflict.md) — muon = $4_1$ canonical
- [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md) — atomic canonical form (parallel structure)
- [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) — operator-level mass formula
- [`prop:categorical-mass-markov`](categorical-mass-markov.md) — $\|\cdot\|$ modulus projection
- [`bar-involution.md`](bar-involution.md) — $P_{\mathrm{avg}}$ / $P_{\mathrm{skew}}$ projection
- [`prop:skein-mass-relation`](../../observations/skein-mass-relation.md) — operative LO formula (SUPERSEDED-$\rho_q$-bannered)
- Sibling  — `BarSymmetricBarAntiSymmetricIdentities.lean` (bar-decomp infrastructure)
- Sibling  — `Q_m` torus-knot sinh identity (related P_skew framework)
