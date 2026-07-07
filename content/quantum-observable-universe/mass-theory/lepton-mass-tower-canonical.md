> **⚠ Resolution update (2026-06-30, owner-ruled) — read first.** The
> muon knot-ID is settled
> ([`docs/audits/2026-06-30-muon-knot-id-phi-q-evidence.md`](../../../docs/audits/2026-06-30-muon-knot-id-phi-q-evidence.md)):
> **the muon is the torus knot $T(2,5)$, and $4_1$ is the Higgs**, not the
> muon. Torus-knot leptons have $\mathrm{Vol}_q = 0$, so a charged lepton
> has **no intrinsic volume-mass**; its mass comes from coupling to the
> **Higgs ($4_1$)**. This **reframes the premise below**: the $\xi_\ell$ /
> $\mathrm{Vol}_q^{\mathrm{tower}}$ obstruction (Phases 4–5) measured the
> *lepton's own* per-braid tower (correctly $O(1)$) — but that is the
> lepton's *intrinsic* (non-Higgs) part, **not** its mass. The mass scale
> $\sim10^2$ lives in the Higgs coupling $\mathrm{Vol}(4_1)/\hbar_q^2$, a
> *different* object. The genuine open question is therefore **not** "find
> $\xi_\ell$ for the lepton's own tower" but "**derive the Higgs ($4_1$)
> coupling and its generation modulation** ($T(2,3)/T(2,5)/T(2,7)$, framing
> $q^{n}$) so $m_\tau \neq m_\mu$." The Phase 4–5 material below is retained
> as a correct *scope-limited negative* on the own-tower object, not deleted.

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

## Two-constraint obstruction (Phase 4 finding)

Any working $\mathcal{F}_\ell(q) = \xi_\ell(q)\cdot\mathrm{Vol}_q^{\mathrm{tower}}(K_\ell)$
must satisfy **two constraints simultaneously**. The two candidate
families explored so far each satisfy only one — they are
*complementary* failures, which sharpens the open problem:

**C1 — nonzero on torus knots.** The electron $K_\mathfrak{e} = T(2,3)$
(trefoil) and tau $K_\tau = T(2,7)$ (septafoil) are **torus** knots,
hence non-hyperbolic: $\mathrm{Vol}_{\mathrm{hyp}} = 0$. Only the muon
$4_1$ is hyperbolic. So a hyperbolic-volume object gives
$\mathfrak{m}(\mathfrak{e}) \propto 0$ and $\mathfrak{m}(\tau) \propto 0$.
The production Skein form $\mathrm{Vol}(4_1)/\hbar_q^2$ therefore "works"
for the muon **only by CAL-2 calibration** (with $m_e$ set to the unit),
and **cannot predict $m_\tau/m_e$** — it would require
$\mathrm{Vol}_{\mathrm{hyp}}(T(2,7)) = (m_\tau/m_e)\,\hbar_q^2 \approx 34.1$,
but a torus knot has $\mathrm{Vol}_{\mathrm{hyp}} = 0$. $\mathrm{Vol}_{\mathrm{hyp}}$
**fails C1**.

**C2 — $O(10^2)$ mass ratios.** CODATA $m_\mu/m_e = 206.77$,
$m_\tau/m_e = 3477.23$. If $\xi_\ell(q)$ is lepton-**independent** (a
universal dimensional scalar, as the reading "$1/\hbar_q^2$" suggests), it
**cancels in every ratio**, leaving
$m_\mu/m_e = \mathrm{Vol}_q^{\mathrm{tower}}(K_\mu)/\mathrm{Vol}_q^{\mathrm{tower}}(K_\mathfrak{e})$.
The descended-dropped per-braid $\mathrm{Li}_2^q$ tower with **proper
Plancherel-weighted Wedderburn $\hat V_i$** (not the earlier crude
$|\mathrm{tr}_M|^{1/n}$ placeholder;
`per-generator-V-hat-general.witness.json`) gives

| $K_\ell$ | $\mathrm{Vol}_q^{\mathrm{tower}}$ | ratio to $\mathfrak{e}$ | CODATA |
|---|---:|---:|---:|
| $\mathfrak{e}$ $T(2,3)$ | $0.2945$ | $1$ | $1$ |
| $\mu$ $T(2,5)$ | $0.4830$ | $1.64$ | $206.77$ |
| $\mu$ $4_1$ | $1.8669$ | $6.34$ | $206.77$ |
| $\tau$ $T(2,7)$ | $0.6749$ | $2.29$ | $3477.23$ |

— all $O(1)$, missing CODATA by $\sim 30$–$130\times$. The universal-scalar
$\times\,\mathrm{Li}_2^q$-tower family **fails C2**: the scalar supplies no
ratio structure and the symmetric $\mathrm{Li}_2^q$ tower supplies the
wrong magnitude.

**Synthesis — the missing $\sim 10^2$ is a Kashaev $1/\hbar$ enhancement.**
The two failures are complementary: $\mathrm{Vol}_{\mathrm{hyp}}$ is nonzero
only for the hyperbolic muon (fails C1); the symmetric-$\mathrm{Li}_2^q$
tower is nonzero everywhere but $O(1)$ (fails C2). The structural reason
the $\mathrm{Li}_2^q$ tower stays $O(1)$ is that the **symmetric** (Rogers)
$\mathrm{Li}_2^q(z) = \sum z^n/(n[n]_q) \to \mathrm{Li}_2(z)$ as $q\to1$ —
no $1/\hbar$ blow-up — whereas the **compact** quantum dilogarithm
$\Phi_q$ has $\log\Phi_q \sim \mathrm{Li}_2/\hbar$, an $O(1/\hbar)$
enhancement (two such factors give the $1/\hbar_q^2 \approx 102$ that the
SUPERSEDED scalar carries). The concrete next direction is therefore to
test the tower with the **compact q-dilog $\Phi_q$** in place of the symmetric
$\mathrm{Li}_2^q$: $\Phi_q$ is nonzero on torus knots (preserving C1) and
its $1/\hbar$ asymptotic can supply the $O(10^2)$ ratio magnitude
(targeting C2). This is the $\Phi_q$ (compact q-dilog) vs $\mathrm{Li}_2^q$
(Rogers) context-sorting flagged in the canonical-derivation cheat sheet —
the lepton sector is where the choice is decisive rather than cosmetic.

> **Scope (per the refuted-claim discipline).** This is a
> **scope-limited negative**: the *hyperbolic-volume* and the
> *universal-scalar $\times$ symmetric-$\mathrm{Li}_2^q$-tower* candidate
> families, **as stated**, do not reproduce the lepton ratios. It is
> **not** a structural exclusion of $\mathrm{Vol}_q^{\mathrm{tower}}$ or of
> a categorical $\xi_\ell$ — the compact-q-dilog $\Phi_q$ tower is untested and is
> the indicated next probe. The muon *accuracy* (not the structural form)
> remains Subgoal-2-blocked (q₀-repin out of scope, owner directive
> 2026-05-08).

## Compact q-dilog $\Phi_q$ probe (Phase 5 finding)

The Phase-4 resolution was tested directly: swap the symmetric
$\mathrm{Li}_2^q$ for the compact (q-Pochhammer) quantum dilogarithm
$\Phi_q(z) = \prod_{k\ge1}(1-q^{-k}z)^{-1}$ in the per-braid tower, with
the **same** proper Plancherel-weighted Wedderburn $\hat V_i$
(`xi-ell-faddeev-phi-q-probe.witness.json`):

| ratio to $\mathfrak{e}$ | CODATA | (a) $\mathrm{Li}_2^q$ | (b) $\Phi_q$ direct | (c) $\log\Phi_q$ |
|---|---:|---:|---:|---:|
| $\mu$ $T(2,5)$ | $206.77$ | $1.64$ | $13.99$ | $1.85$ |
| $\mu$ $4_1$ | $206.77$ | $6.34$ | $116{,}611$ | $10.06$ |
| $\tau$ $T(2,7)$ | $3477.23$ | $2.29$ | $526.8$ | $3.01$ |

**The $1/\hbar$ enhancement is real, but neither bare variant closes.**

1. **Enhancement confirmed.** $\log\Phi_q$ raises *every* ratio above the
   symmetric $\mathrm{Li}_2^q$ ($\mu\,T(2,5)$: $1.64\!\to\!1.85$; $\tau$:
   $2.29\!\to\!3.01$); $\Phi_q$-direct far more. The Phase-4 claim — that
   the missing $\sim10^2$ is a Kashaev $1/\hbar$ effect absent in the
   symmetric (Rogers) dilog — is borne out: the compact-q-dilog form *does* inject
   it.

2. **But it does not reproduce CODATA.** $\Phi_q$-direct **overshoots
   catastrophically and knot-sensitively**: the muon $4_1$ has
   $\hat V \approx 1.009$, sitting essentially *on* the $\Phi_q$
   convergence radius $q_0 = 1.110$, so $\Phi_q(\hat V)$ is near-singular
   and the ratio explodes to $116{,}611$; the $T(2,5)$ muon
   ($\hat V \approx 0.543$) gives only $13.99$. $\log\Phi_q$ under-reaches
   at $O(10)$.

3. **The muon knot-ID is now decisive, not a footnote.** The
   $4_1$-vs-$T(2,5)$ muon ambiguity widens from a $\sim 8.5\times$ spread
   under $\mathrm{Li}_2^q$ to $\sim 8000\times$ under $\Phi_q$-direct.
   Resolving the muon knot identity (`docs/audits/-muon-knot-id-conflict.md`)
   is therefore a **gating prerequisite** for any $\Phi_q$ closure.

4. **A structural tell.** That the hyperbolic muon $4_1$ — the *unique*
   hyperbolic lepton (C1) — is the one whose $\hat V$ sits at the $\Phi_q$
   radius is consistent with the Kashaev volume conjecture: $\Phi_q$
   growth at the radius is exactly where $\mathrm{Vol}_{\mathrm{hyp}}(4_1)$
   is encoded. The torus leptons ($T(2,3)$, $T(2,5)$, $T(2,7)$) stay away
   from the radius, matching $\mathrm{Vol}_{\mathrm{hyp}}=0$.

> **Scope (refuted-claim discipline).** A **scope-limited negative**:
> neither *bare* $\Phi_q$ variant, as stated, reproduces the lepton
> ratios. It is **not** an exclusion of the compact-q-dilog $\Phi_q$ direction —
> the $1/\hbar$ enhancement it supplies is validated. The missing piece is
> the correct *argument normalization* (the near-singular $4_1$ behaviour
> says $\Phi_q$ should act on a rescaled argument, not bare $\hat V$), the
> *jet-level geometric sum* not implemented in this leading-order probe,
> and the *muon knot resolution*.

**Rescaled-argument test (done — also negative).** The near-singular
$4_1$ behaviour in (b) motivated testing $\Phi_q$ on the normalised
argument $\hat V/q_0$. Result: rescaling tames the tau overshoot
($526.8\!\to\!209.9$) but the muon $4_1$ **still blows up**
($13{,}042\times$), because $\hat V(4_1)/q_0 \approx 0.91$ stays too close
to the radius. Neither $\hat V$ nor $\hat V/q_0$ closes. The durable
finding is the qualitative split: under *every* $\Phi_q$ normalization the
two muon candidates behave **oppositely** — $4_1$ overshoots, $T(2,5)$
undershoots — so the **muon knot identity is the decisive lever**, not the
dilog normalization.

> **Next steps, reordered by the probe outcome:** (i) **settle $4_1$ vs
> $T(2,5)$** — now the gating item (see
> [`docs/audits/2026-06-30-muon-knot-id-phi-q-evidence.md`](../../../docs/audits/2026-06-30-muon-knot-id-phi-q-evidence.md));
> (ii) implement the level-$N$ jet geometric sum (the only structural
> ingredient untested); (iii) the bare/rescaled single-level $\Phi_q$
> tower is **closed as a scope-limited negative**.

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

- [`docs/audits/2026-05-24-m-mu-over-m-e-operator-rederivation.md`](../../../docs/audits/2026-05-24-m-mu-over-m-e-operator-rederivation.md) — Phase 3 finding (the audit this conjecture answers)
- [`docs/audits/2026-05-24-superseded-rho-q-purge.md`](../../../docs/audits/2026-05-24-superseded-rho-q-purge.md) — the SUPERSEDED ρ_q purge that motivates the lepton re-derivation
- [`docs/audits/2026-05-24-muon-knot-id-conflict.md`](../../../docs/audits/2026-05-24-muon-knot-id-conflict.md) — muon = $4_1$ canonical **(SUPERSEDED 2026-06-30: muon = $T(2,5)$, $4_1$ = Higgs — see the resolution banner above and [`2026-06-30-muon-knot-id-phi-q-evidence.md`](../../../docs/audits/2026-06-30-muon-knot-id-phi-q-evidence.md))**
- [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md) — atomic canonical form (parallel structure)
- [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) — operator-level mass formula
- [`prop:categorical-mass-markov`](categorical-mass-markov.md) — $\|\cdot\|$ modulus projection
- [`bar-involution.md`](bar-involution.md) — $P_{\mathrm{avg}}$ / $P_{\mathrm{skew}}$ projection
- [`prop:skein-mass-relation`](../../observations/skein-mass-relation.md) — operative LO formula (SUPERSEDED-$\rho_q$-bannered)
- Sibling  — `BarSymmetricBarAntiSymmetricIdentities.lean` (bar-decomp infrastructure)
- Sibling  — `Q_m` torus-knot sinh identity (related P_skew framework)
