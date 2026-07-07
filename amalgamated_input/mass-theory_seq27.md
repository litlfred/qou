<!-- FILE_START: lepton-mass-tower-canonical.md -->
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
no $1/\hbar$ blow-up — whereas the **Faddeev** quantum dilogarithm
$\Phi_q$ has $\log\Phi_q \sim \mathrm{Li}_2/\hbar$, an $O(1/\hbar)$
enhancement (two such factors give the $1/\hbar_q^2 \approx 102$ that the
SUPERSEDED scalar carries). The concrete next direction is therefore to
test the tower with the **Faddeev $\Phi_q$** in place of the symmetric
$\mathrm{Li}_2^q$: $\Phi_q$ is nonzero on torus knots (preserving C1) and
its $1/\hbar$ asymptotic can supply the $O(10^2)$ ratio magnitude
(targeting C2). This is the $\Phi_q$ (Faddeev) vs $\mathrm{Li}_2^q$
(Rogers) context-sorting flagged in the canonical-derivation cheat sheet —
the lepton sector is where the choice is decisive rather than cosmetic.

> **Scope (per the refuted-claim discipline).** This is a
> **scope-limited negative**: the *hyperbolic-volume* and the
> *universal-scalar $\times$ symmetric-$\mathrm{Li}_2^q$-tower* candidate
> families, **as stated**, do not reproduce the lepton ratios. It is
> **not** a structural exclusion of $\mathrm{Vol}_q^{\mathrm{tower}}$ or of
> a categorical $\xi_\ell$ — the Faddeev-$\Phi_q$ tower is untested and is
> the indicated next probe. The muon *accuracy* (not the structural form)
> remains Subgoal-2-blocked (q₀-repin out of scope, owner directive
> 2026-05-08).

## Faddeev $\Phi_q$ probe (Phase 5 finding)

The Phase-4 resolution was tested directly: swap the symmetric
$\mathrm{Li}_2^q$ for the Faddeev (q-Pochhammer) quantum dilogarithm
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
   symmetric (Rogers) dilog — is borne out: the Faddeev form *does* inject
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
> ratios. It is **not** an exclusion of the Faddeev-$\Phi_q$ direction —
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
<!-- FILE_END: lepton-mass-tower-canonical.md -->

<!-- FILE_START: lepton-bring-surface-h3-3channel.md -->
**Proposition (lepton Bring-surface = H_3 3-channel convention).**
*For any torus-knot lepton candidate $K_\ell = \sigma_1^{2m+1}$ (electron $m=1$,
candidate muon $m=2$, candidate tau $m=3$), the framework's "additive
Wedderburn" volume $\hat V_\ell^{\mathrm{full}}$ — used in the per-braid mass
tower and matching `mass-endomorphism-tower.md`'s published $\hat V_e \approx 0.594$ —
is given by the **H_3 3-channel Plancherel-weighted character sum** with
Markov-traced standard channel:*

$$
\boxed{\;\hat V_\ell^{\mathrm{full}}
\;=\;
W_{\mathrm{sym}} \cdot q^{2m+1}
\;+\;
W_{\mathrm{std}} \cdot (z \cdot a_{2m+1} + b_{2m+1})
\;+\;
W_{\mathrm{alt}} \cdot (-q^{-1})^{2m+1}\;}
$$

*where:*

- *$W_\lambda = d_q(\lambda)^2 / [3]_q!$ are H_3 Plancherel weights:
  $W_{\mathrm{sym}} = W_{\mathrm{alt}} = 1/[3]_q!$,
  $W_{\mathrm{std}} = [2]_q^2/[3]_q!$;*
- *$(a_{2m+1}, b_{2m+1})$ are the Hecke recursion coefficients from
  $\sigma_1^{2m+1} = a_{2m+1} \cdot \sigma_1 + b_{2m+1}$
  (per the proved theorem
  [`torus_knot_odd_reduction_exists`](lepton-mass-tower-canonical.md));*
- *$z = 1/(q^{1/2} + q^{-1/2})$ is the Markov parameter;*
- *the std-channel term $(z \cdot a + b)$ is the Hoefsmit-basis Markov
  trace of $\sigma_1^{2m+1}$ in the 2-dimensional standard
  representation of $H_3(q)$.*

> **T6 status — gap (a) RESOLVED; gap (c) IMPLICATED.** This
> proposition closes the $\hat{V}$-convention ambiguity (T6 gap (a)) by
> documenting the H_3 3-channel formula. Applying the canonical Li_2^q
> per-braid mass tower to the resulting $\hat{V}$ values gives lepton mass
> ratios off CODATA by 99% — the missing factor `206.77 / 1.36 ≈ 152`
> equals **(3/2) $\times$ (1/ℏ_$q^{2}$)**, structurally identical to the
> SUPERSEDED scalar substrate density. Full diagnosis:
> [`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/-lepton-bring-surface-h3-3channel-convention.md).

## Bring-surface analog with nucleons

The framework places nucleons on the Bring surface ($\Sigma_4$, genus 4)
with 3 quark color tubes per nucleon (3 sheets carrying $\mu_u, \mu_u, \mu_d$
for proton; $\mu_u, \mu_d, \mu_d$ for neutron). This is the **3-sheet
nucleon Bring representation**.

The analogous lepton representation uses the **3 H_3 Wedderburn channels**:

| Sector | 3-sheet Bring structure | Underlying symmetry |
|---|---|---|
| Nucleon | 3 quark color tubes | $\mathrm{SU}(3)$ color |
| Lepton | 3 H_3 Wedderburn irreps | partitions $\lambda \vdash 3$ |

Both are 3-fold representations on the substrate; both project through
Plancherel weighting to a single observable. The 3-channel structure
for leptons is the **canonical "where leptons live"** on the
Bring surface: even though $\sigma_1^{2m+1}$ is naturally an $H_2$
element (2 strands, 1 generator), the mass formula sits at $H_3$
because that is where the cohomological discipline
([`prop:three-parameters-wedderburn`](three-parameters-wedderburn.md))
fixes the 3-CAL $\leftrightarrow$ 3-channel mapping.

## Verification — calibration matches paper

At $q_0 \approx 1.10998$:

| Quantity | Value |
|---|---:|
| $[2]_q$ | 2.0109 |
| $[3]_q! = [1]_q[2]_q[3]_q$ | 6.1206 |
| $W_{\mathrm{sym}}$ | 0.1634 |
| $W_{\mathrm{std}}$ | 0.6607 |
| $W_{\mathrm{alt}}$ | 0.1634 |
| $\sum W$ | 0.9874 |

For electron $\sigma_1^3$:

| Channel | Value |
|---|---:|
| $\chi_{(3)}(\sigma_1^3) = q^3$ | $1.367$ |
| $\chi_{(1,1,1)}(\sigma_1^3) = -q^{-3}$ | $-0.731$ |
| std Markov trace $= z(h^2 + 1) + h$ | $0.730$ |
| **$\hat V_e^{\mathrm{full}}$ (computed)** | **$0.586$** |
| $\hat V_e^{\mathrm{full}}$ (paper, `mass-endomorphism-tower.md:351`) | $\approx 0.594$ |

Match within $1.3\%$ (small discrepancy is paper's 3-significant-figure
rounding; the algebraic formula above is exact).

## Application to the lepton tower

Computed $\hat V_\ell$ and Li_2^q-tower mass ratios at $q_0$:

| Lepton | Braid | $\hat V_\ell$ | $\|\hat V\| < q_0$? | $m_{\mathrm{dim}}$ | Ratio | CODATA | Δ |
|---|---|---:|:---:|---:|---:|---:|---:|
| Electron | $\sigma_1^3$ T(2,3) | $+0.586$ | yes | $0.518$ | $1$ (cal) | — | — |
| Muon T(2,5) | $\sigma_1^5$ | $+0.834$ | yes | $0.705$ | $1.36$ | $206.77$ | $-99.3\%$ |
| Muon T(2,7) | $\sigma_1^7$ | $+1.119$ | no | diverges | — | — | — |
| Tau T(2,7) | $\sigma_1^7$ | $+1.119$ | no | diverges | — | — | — |
| Tau T(2,9) | $\sigma_1^9$ | $+1.452$ | no | diverges | — | — | — |

The convention is internally consistent (electron calibrates correctly),
but **mass ratios do not close** under the canonical Li_2^q tower
alone — the missing dimensional factor is structurally identical to
the SUPERSEDED scalar $\rho_q = 1/\hbar_q^2$ (see Caveat above).

**Tau divergence**: T(2,7) and T(2,9) both yield $\hat V > q_0$, outside
the Li_2^q convergence radius. Either the canonical tau braid is **not**
in the T(2, 2m+1) family, or higher-tower terms regulate the divergence
(consistent with the open status of `prop:rho-k-pair-gen-canonical-form`).

## Lowest/highest weight structure (6-dim NF diamond)

The framework's NF basis of $H_3(q)$ has dimension $6 = 1^2 + 2^2 + 1^2$
(sym + std + alt). **The sym and alt are the 1-dimensional
highest-weight and lowest-weight irreps** of the symmetric group $S_3$
(equivalently the classical limit of $H_3(q)$):

| Wedderburn channel | Partition | Dim | Weight | $\sigma_i$ eigenvalue |
|---|:---:|:---:|---|:---:|
| sym | $(3)$ | 1 | **highest** | $+q$ |
| std | $(2, 1)$ | 2 (so $d^2 = 4$ in NF count) | mixed | $+q$ and $-q^{-1}$ mixed |
| alt | $(1,1,1)$ | 1 | **lowest** | $-q^{-1}$ |

The 1 + 4 + 1 = 6 NF-diamond structure is therefore **symmetric around
the std midpoint**: 1-dim endpoints at lowest and highest weight, with
the 4-dim std irrep filling the middle. This is the canonical $S_n$
representation-theory structure.

### Lepton $\leftrightarrow$ channel mapping (conjectural)

Per [`prop:three-parameters-wedderburn`](three-parameters-wedderburn.md):

- sym (highest weight, $+q$ only) $\leftrightarrow$ CAL-2 $q_0$ (substrate deformation)
- std (mixed eigenvalues) $\leftrightarrow$ CAL-1 $m_e$ (mass scale)
- alt (lowest weight, $-q^{-1}$ only) $\leftrightarrow$ CAL-3 $\mathfrak{Q}_\beta$ (interaction)

A natural conjecture maps the 3 lepton generations to the 3 H_3 channels
respecting this lowest/highest-weight structure:

| Lepton | Candidate channel | Reasoning |
|---|---|---|
| Electron | std (middle, calibration unit) | electron IS the mass-scale calibration (CAL-1 = $m_e$); most natural to live in the std channel that controls mass |
| Muon | sym (highest weight) OR alt (lowest weight) | the 2 "endpoint" leptons fill the 1-dim irreps |
| Tau | the other endpoint | (sym if muon = alt; alt if muon = sym) |

The tau divergence finding above (T(2, 2m+1) at $m \geq 3$ gives $\hat V > q_0$)
is consistent with one endpoint channel saturating the 1D irrep's
representation capacity at high crossing count.

### Elementary-particle count in 6-dim NF basis

A plausible elementary-particle count fitting the 6-dim NF diamond:

- 2 lepton generations $\times$ 2 chiralities (L, R) = 4 dimensions
- 1 Higgs (figure-eight $4_1$, "Higgs field / mass mechanism" per `the formal derivation:58`)
- 1 photon ($\gamma$, identity element of $H_3$)
- **Total = 6 dimensions = $\dim H_3(q)$**

Alternative count:
- 3 leptons $\times$ 1D irrep each (e/μ/τ in sym/std/alt) = 3 dimensions
- But std is 2D ($d^{2}$ = 4), so it contributes more — would give 1 + 4 + 1 = 6
- If electron occupies std (4 dim = electron-LH + electron-RH + electron-neutrino-LH + electron-neutrino-RH?), then muon + tau fill sym + alt (1 + 1)
- **Total still = 6 dimensions**

This is conjectural; explicit mapping NF-diamond $\leftrightarrow$ elementary-particle
content is open. If correct, the lowest/highest-weight 1-dim irreps
correspond to the 2 extreme leptons (muon and tau), with the
electron in the 4-dim middle std channel hosting both chiralities
and possibly weak-isospin partner (neutrino).

## Cross-references

- [`prop:three-parameters-wedderburn`](three-parameters-wedderburn.md) — 3-CAL $\leftrightarrow$ 3-channel cohomological discipline
- [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) — Li_2^q canonical mass formula
- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md) — F_ℓ existence conjecture
- [`rem:bar-involution`](bar-involution.md) — P_avg / P_skew projection (real-q mechanism)
- Convention source: `tools/pyhecke/python/pyhecke/the formal derivation:156` (V_HAT_ELECTRON)
- Compute infrastructure: the formal derivation (generalises `per_generator_V_hat_3A`)
- T6 closure attempt: the formal derivation
- Audit: [`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/-lepton-bring-surface-h3-3channel-convention.md)
- SUPERSEDED ρ_q purge (now understood as incomplete): [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md)
<!-- FILE_END: lepton-bring-surface-h3-3channel.md -->

<!-- FILE_START: conj-lepton-tower-h-n-plus-1-branching.md -->
**Conjecture (lepton-tower closure factor — unifying form).** *Let
$K_\ell$ be the canonical knot for the lepton at tower-index $m$
(electron $m=1$ trefoil / muon $m=2$ figure-eight / tau $m=3$
amphichiral $10_{43}$ candidate). The canonical operator-level
mass-tower $\xi_m$ correction factor is*

$$
\boxed{\;\xi_m \;=\; \frac{[2m-1]_q \cdot [m]_q}{[2m]_q}\;}
$$

*where $[n]_q = q^{n-1} + q^{n-3} + \cdots + q^{-(n-1)}$ is the
symmetric q-integer. The triple $(2m-1, m, 2m)$ is symmetric in
$h = q - q^{-1}$ — bar-anti-symmetric upper jet, middle index,
bar-symmetric closing trace. This is the **structural** factor
(matching the Lean `lepton_xi` and the verification table below); the
full mass closure additionally carries the universal substrate scalar
$1/\hbar_q^2$, common to all leptons and hence cancelling in the
inter-lepton ratios validated here.*

### Earlier framing (superseded by  unifying formula)

> **SUPERSEDED .** The earlier conjecture
> $\xi_m = d_q((n,1)) \cdot [2]_q / [n+1]_q$ (with $n = 2m+1$, then
> revised to $n = m+1$) matched muon but **falsified at tau**
> ($\xi_3 = [4]_q \cdot [2]_q / [5]_q$ predicted $\approx$ 1.59 vs required
> $\approx$ 2.47, off by 35 %). The  amphichiral filter identified
> the actual closure $\xi_3 = [5]_q \cdot [3]_q / [6]_q$ and the
> unifying form above. The earlier framing is preserved below for
> pedagogical trajectory; the "Resolution" section is
> the current authoritative statement.

## Provenance — empirical fit (categorical derivation open)

The structural factor was identified **empirically** as the best of
28 candidate q-bracket ratios (matching the required lepton ratios to
$0.034\%$, the best by $20\times$ over the next-best candidate;
[`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/-lepton-bring-surface-h3-3channel-convention.md)).
It is therefore a **conjecture** (fit-identified), not a derived
result. The categorical derivation — why the q-bracket triple
$(2m-1, m, 2m)$ falls out of the per-braid mass tower's
operator-valued $A^\lambda_{\mu,\nu}(I)$ branching at the lepton's
amphichiral knot — remains open work for Option E (Kashiwara crystal).

The algebraic identity
$\frac{[3]_q \cdot [2]_q}{[4]_q} = \frac{3 + h^2}{2 + h^2}$ (the muon
case) is Lean-proved in
[`three-halves-structural-factor.lean`](three-halves-structural-factor.lean).

> **History.** Earlier indexing attempts ($n = 2m+1$, then $n = m+1$)
> and a tau probe that carried the substrate scalar $1/\hbar_q^2$
> explicitly were superseded by the unifying structural form above;
> those working notes have been removed to keep the conjecture clean.

## Categorical interpretation candidates

Three readings of the ξ_m formula:

### (A) H_{m+2} std-irrep dimension

ξ_m couples the lepton braid (at H_2 or H_3 substrate) to the
$S_{m+2}$ standard representation. The factor $d_q((m+1, 1)) = [m+1]_q$
is the **q-dimension** of this rep; the $[2]_q / [m+2]_q$ normalisation
is a Schur-Weyl reciprocity factor.

### (B) LR coefficient branching

$\xi_m$ as a Littlewood-Richardson coefficient
$c^{(m+1, 1)}_{(m+1), (1)} \cdot \text{q-bracket normalisation}$.
The LR coefficient $c^{(m+1, 1)}_{(m+1), (1)} = 1$ (one standard
Young tableau for the corresponding skew shape), so the formula
becomes $\text{q-bracket}$.

### (C) Operator-valued $A^\lambda_{\mu, \nu}(I)$

Per [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) §SUPERSEDED,
the canonical dimensional factor is the **operator-valued** $A^\lambda_{\mu, \nu}(I)$
from [`prop:hecke-branching-trace-decomposition`](hecke-branching-trace-decomposition.md).
For the lepton sector, this would specialise to the conjectured
$d_q(\lambda) \cdot [2]_q / [n]_q$ form.

All three readings are consistent with the muon (m=2) canonical
match; distinguishing them requires the derivation work that's
currently open.

## Resolution — unifying formula

The "simple extension" pattern `[m+1]_q · [2]_q / [m+2]_q` is FALSIFIED for tau (predicted ξ_3 = `[4]_q · [2]_q / [5]_q` $\approx$ 1.59 vs required $\approx$ 2.47, off by 35 %).

The **correct unifying formula**:

$$
\boxed{\;\xi_m \;=\; \frac{[2m-1]_q \cdot [m]_q}{[2m]_q}\;}
$$

canonical structural verification at $q_0 \approx 1.110$ (the formal derivation witness):

| m | Lepton | Formula | At $q_0$ | Required | Δ |
|---|---|---|---:|---:|---:|
| 1 | Electron | (calibration unit) | 1.000 | 1.0 | 0 % |
| 2 | Muon | $[3]_q \cdot [2]_q / [4]_q$ | 1.48931 | 1.48929 | **+0.001 %** |
| 3 | Tau | $[5]_q \cdot [3]_q / [6]_q$ | 2.48736 | 2.46776 | **+0.79 %** |
| 4 | (no SM lepton) | $[7]_q \cdot [4]_q / [8]_q$ | 3.50311 | — | — |

The triple $(2m-1, m, 2m)$ is **symmetric in $h = q - q^{-1}$** at every step:
- $2m-1$ odd $\to$ bar-anti-symmetric q-bracket contribution from the upper jet
- $m$ $\to$ middle index (symmetric / anti-symmetric depending on parity)
- $2m$ even $\to$ bar-symmetric q-bracket from the closing trace

This pattern is precisely what the lepton's amphichirality should produce — the upper and lower indices are reflections of each other across the middle, consistent with the **knot-operator = symmetry equivalence** in the owner's  directive.

## Lean formalization

The unifying formula's algebraic content is **Lean-proved** in two places:

- [`three-halves-structural-factor.lean`](three-halves-structural-factor.lean):
    - Muon: `three_halves_factor_eq_q_brackets` — $(3 + h^2)/(2 + h^2) = [3]_q \cdot [2]_q / [4]_q$
    - Tau: `bracket6_eq_bracket2_bracket3_times_one_plus_h_sq` — $[6]_q = [2]_q \cdot [3]_q \cdot (1 + h^2)$
    - Tau closure: `bracket5_bracket3_div_bracket6` — $[5]_q \cdot [3]_q / [6]_q = [5]_q / ([2]_q \cdot (1+h^2))$

- [`conj-lepton-tower-h-n-plus-1-branching.lean`](conj-lepton-tower-h-n-plus-1-branching.lean):
    - `lepton_xi` — concrete definition for electron/muon/tau (no `sorry`)
    - `lepton_xi_muon_eq_closed_form` — muon ξ_2 closed form
    - `lepton_xi_tau_eq_reduced_form` — tau ξ_3 reduced form
    - `br6_eq_br2_br3_times_one_plus_h_sq` — fundamental tau identity (mirror of sibling file's theorem)
    - `lepton_xi_electron_eq_one` — calibration convention

All proofs are `field_simp; ring` over generic `[Field R]` per AGENTS.md §7c.

The categorical derivation (why $\xi_m = [2m-1]_q \cdot [m]_q / [2m]_q$ specifically — i.e., how the q-bracket triple $(2m-1, m, 2m)$ falls out of the per-braid mass tower's operator-valued $A^\lambda_{\mu, \nu}(I)$ branching at the lepton's H_{2m+1}-substrate amphichiral knot) remains open work for Option E (Kashiwara crystal).

## Cross-references

- [`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/-lepton-bring-surface-h3-3channel-convention.md) — T6 gap (c) full diagnosis (muon side)
- [`docs/audits/-t6-f-ell-derivation-attempt.md`](../../../docs/audits/-t6-f-ell-derivation-attempt.md) — T6/F_ℓ workplan +  tau followup section
- the canonical formalism — muon categorical canonical evaluation
- the canonical formalism — tau amphichiral q-bracket canonical evaluation
- [`prop:three-halves-structural-factor`](three-halves-structural-factor.md) — Lean-proved structural identities (muon + tau)
- [`prop:lepton-bring-surface-h3-3channel`](lepton-bring-surface-h3-3channel.md) — $\hat{V}_e$ convention (calibration check)
- [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) — canonical mass formula
- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md) — F_ℓ existence (partially closed: muon + tau q-bracket forms now identified; categorical derivation open for Option E)
<!-- FILE_END: conj-lepton-tower-h-n-plus-1-branching.md -->

<!-- FILE_START: conj-atom-braid-exterior-algebra.md -->
**Conjecture (atom-braid exterior-algebra structure; partial-closure: verified at $A \leq 4$, general $A$ open).** *Let `A = Z + N` with $Z \geq 1$, $N \geq 0$, and let $T_w(Z, N) \in B_{3A}$ denote the canonical atom-braid word `atom_braid_word_3A(Z, N)` (the formal derivation recipe). Its image in the Iwahori–Hecke algebra $H_{3A}(q)$ under the standard $\sigma_i \mapsto T_i$ representation generates a sub-algebra whose GB-NF filtration shape is given by*

$$
\dim_R \bigl(F_k(T_w(Z, N))\bigr) \;=\; \binom{3A - Z}{\,k - (Z - 1)\,} \qquad (k = Z - 1, Z, \ldots, 3A - 1).
$$

*Equivalently, the sub-algebra is isomorphic (as a graded $R$-vector space, $R$ any field of characteristic 0 — typically $\mathbb{Q}$ for the GB-NF rational arithmetic, $\mathbb{R}$ for the substrate evaluation at $q_0 \in \mathbb{R}$) to the **exterior algebra** $\Lambda^*(R^{3A - Z})$, with grade shift $\delta = Z - 1$, total dimension $2^{3A - Z}$.*

## Empirical verification (PR following R5-full $^4$He registry extension)

The conjecture is verified across all 4 atoms with canonical `atom_braid_word_3A` recipes implemented in the Rust R5-SDP solver (post-`BraidLetter` extension):

| Atom | $(Z, N)$ | $n_0 = 3A$ | $3A - Z$ | $\delta = Z - 1$ | Filtration shape | Total |
|---|---|---|---|---|---|---|
| D $^2$H | (1, 1) | 6 | 5 | 0 | $\{1, 5, 10, 10, 5, 1\} = \binom{5}{k}$ | $2^5 = 32$ |
| T $^3$H | (1, 2) | 9 | 8 | 0 | $\{1, 8, 28, 56, 70, 56, 28, 8, 1\} = \binom{8}{k}$ | $2^8 = 256$ |
| $^3$He | (2, 1) | 9 | 7 | 1 | $\{1, 7, 21, 35, 35, 21, 7, 1\} = \binom{7}{k}$ | $2^7 = 128$ |
| $^4$He | (2, 2) | 12 | 10 | 1 | $\{1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1\} = \binom{10}{k}$ | $2^{10} = 1024$ |

Each row's shape is **exactly Pascal's triangle row $(3A - Z)$** with the appropriate grade shift, and totals are $2^{3A - Z}$.

## Structural interpretation

The exterior-algebra structure says: the canonical atom-braid lives in a **fermion Fock-space subalgebra** of $H_{3A}(q)$, with each "interface" between adjacent strands contributing one $\mathbb{Z}/2\mathbb{Z}$ degree of freedom. The proton-count $Z$ enters twice:

1. **Dimension reduction** ($\Lambda^*(R^{3A - Z})$ instead of $\mathbb{C}^{3A}$): each proton imposes one constraint, removing one degree of freedom.
2. **Grade shift** ($\delta = Z - 1$): each proton beyond the first shifts the filtration's lower bound by one — analogous to a chemical-potential or fermion-number offset.

This is fundamentally different from the standard Wedderburn decomposition $H_n(q) \cong \bigoplus_\lambda V_\lambda^{\oplus d_\lambda}$ (which for $H_{12}$ has dimension $12! \approx 5 \times 10^8$, **8 orders of magnitude larger** than the observed $2^{10} = 1024$ for $^4$He).

### Load-bearing factoring — PR-D Step 4

The 5-step structural argument that produces the exterior-algebra
shape factors so that *one* step carries all the genuine new
representation-theory content. Steps 1, 2, 3, and 5 are mechanical
($G_0/G_1$ pattern reductions in $H_3 \subset H_{3A}$, bar-involution
constraint counting, and `Nat.sum_range_choose`). **Step 4** —
"inter-nucleon Avg crossings $\sigma_{3k+2} - h/2$ preserve the
Boolean grading" — is the load-bearing categorical claim.

The Lean sibling file factors Step 4 into a dedicated
[`AtomBraidStep4Hypothesis (Z N : ℕ)`](conj-atom-braid-exterior-algebra.lean)
§3b-cond class with a `Prop` hypothesis field
`avg_crossing_preserves_grade`, plus a bridging theorem
`step4_implies_exterior_algebra_structure` that derives the full
`AtomBraidExteriorAlgebraStructure` instance once Step 4 is
discharged. This makes the conjectural input citable,
`lean_verify`-auditable, and individually closable as a single PR
once Sprint 3–4 IwahoriHecke infrastructure is in place to give
mechanical proofs for Steps 1–3.

## Falsified inference: LP/SDP under-determination implication

**Status:** the inference below was **FALSIFIED** by direct computation in the canonical formalism. All `p(n_0)` partitions have non-trivial `χ_λ(T_w)` — the claimed "active set $\leq n^* + 1$" prediction does NOT hold on the Wedderburn basis. See [`docs/audits/-exterior-algebra-lp-claim-falsified.md`](../../../docs/audits/-exterior-algebra-lp-claim-falsified.md) for the full retraction.

**Surviving claims:** the Pascal-row `C(n*, k)` filtration shape on the **NF basis** (permutation-indexed, ordered by Coxeter length) — the Rust solver's empirical finding from  stands.

**Source of the inference failure:** I conflated two different bases of `H_{3A}(q)` — the NF basis (where the Pascal-row shape lives) and the Wedderburn basis (where LP `y_λ` variables live). These are different decompositions of the same algebra; the filtration-shape claim does NOT directly imply Wedderburn-channel reduction.

The section below is retained as a historical record of the falsified inference; the structural-filtration-shape finding above remains the substantive contribution of this conjecture.

## (Retained for record — falsified inference)

### Implications for LP/SDP under-determination

The exterior-algebra structure has a direct consequence for the operator-selection LP/SDP that consumes the canonical atom-braid as input.

**Previously (Wedderburn-channel framing):** the LP/SDP variables `y_λ` for $\lambda \vdash 3A$ have $p(3A)$ partition channels — $p(12) = 77$ for $^4$He alone. The LP feasibility region is correspondingly $\geq 77$-dimensional (before constraint cuts). Empirical observations have noted under-determination — multiple feasible solutions, ambiguous extraction.

**Under the conjecture:** the physical content lives in the sub-algebra $\Lambda^*(R^{3A - Z})$ of dimension $2^{3A - Z}$. The non-trivial Wedderburn channels (those with $y_\lambda \neq 0$ on the atom-braid's image) are a **proper subset** of the $p(3A)$ partitions — exactly those $\lambda$ corresponding to non-zero homogeneous components of $\Lambda^k(R^{3A - Z})$ under the projection $H_{3A}(q) \to \Lambda^*(R^{3A - Z})$.

For Pascal-row $\binom{3A - Z}{k}$ at each grade $k$:
- The number of non-zero $y_\lambda$ channels per grade is **at most one per binomial entry**, suggesting a much smaller active partition set than $p(3A)$.
- For $^4$He: at most $(3A - Z + 1) - \delta = 10$ active channels (one per non-zero binomial position), down from $77$ — **a ${\sim}7\times$ constraint tightening**.

**Concrete predicted reductions:**

| Atom | $p(3A)$ | Predicted max active channels | Reduction |
|---|---:|---:|---:|
| D $^2$H | $p(6) = 11$ | $\leq 6$ | $\geq 1.8\times$ |
| T $^3$H | $p(9) = 30$ | $\leq 9$ | $\geq 3.3\times$ |
| $^3$He | $p(9) = 30$ | $\leq 8$ | $\geq 3.8\times$ |
| $^4$He | $p(12) = 77$ | $\leq 11$ | **$\geq 7.0\times$** |

If the conjecture holds, the LP/SDP under-determination noted in prior probes (Δ_λ closure synthesis, joint-tower SDP feasibility) is structurally resolved: the previously-ambiguous $y_\lambda$ extraction has a **categorically-restricted active set** corresponding to the exterior-algebra graded components.

**Identifying the active partition set** (next step): for each grade $k \in [\delta, \delta + n^*]$, the contributing $\lambda \vdash 3A$ should be determinable from the Schur–Weyl decomposition of $\Lambda^k(R^{3A - Z})$ under the $H_{3A}(q)$-action. Likely candidates (per crystal-basis intuition):
- Pascal row $\binom{3A - Z}{k}$ position correlates with hook-shape partitions $(k+1, 1^{3A - k - 1})$
- More precisely: ribbon / border-strip tableaux of length $3A - Z$

This identification is the natural follow-up — would close the LP/SDP constraint-set explicitly + give a recipe for computing the categorical active set per atom.

## Crystal-basis projection (open)

The exterior algebra $\Lambda^*(V)$ arises in Kashiwara–Lusztig theory as the **fermion Fock space** (the *q*-deformed sector of the Heisenberg-Weyl algebra at $|q| < 1$). The Z-dependent grade shift looks like a **charge sector** label in this framework. Open: identify the specific crystal-basis projection $H_{3A}(q) \to \Lambda^*(\mathbb{C}^{3A - Z})$ that the canonical atom-braid factors through.

A categorical proof would likely use:
1. Schur–Weyl duality $H_n(q) \otimes \mathrm{GL}_m \curvearrowright V^{\otimes n}$ at appropriate $V$ choice
2. The specific structure of `_PROTON_G0 / _PROTON_G1 / _NEUTRON_G0 / _NEUTRON_G1` 3-strand patterns (cf. the formal derivation)
3. KLR diagrammatics to identify the fermion-sector subalgebra

## Cross-references

- the canonical formalism — canonical `atom_braid_word_3A` recipe
- [`tools/hecke-engine/src/gb_nf_reducer.rs`](../../../tools/hecke-engine/src/gb_nf_reducer.rs) — `BraidLetter` + `right_mul_t_avg` (R5-full extension supporting σ_avg)
- [`tools/hecke-engine/src/bin/joint_tower_sdp.rs`](../../../tools/hecke-engine/src/bin/joint_tower_sdp.rs) — joint-tower SDP solver (registry with 4 canonical-3A test atoms + $^4$He)
- [`computations/joint-tower-sdp-rust.witness.json`](../../../computations/joint-tower-sdp-rust.witness.json) — observed filtration shapes
- [`prop:per-braid-mass-tower`](per-braid-mass-tower.md) — canonical mass formula that consumes this structure
- [`prop:lepton-bring-surface-h3-3channel`](lepton-bring-surface-h3-3channel.md) — bring-surface analog for lepton sector
<!-- FILE_END: conj-atom-braid-exterior-algebra.md -->

<!-- FILE_START: conj-psd-trace-orthogonality.md -->
**Conjecture (PSD-vs-trace orthogonality of canonical atom-braid Wedderburn blocks).** *Let $T_w(Z, N) \in B_{3A}$ denote the canonical atom-braid word `atom_braid_word_3A(Z, N)`, viewed as an element of the Iwahori–Hecke algebra $H_{3A}(q)$ at the substrate parameter $q = q_0$. Decompose $H_{3A}(q)$ into Wedderburn blocks $H_{3A}(q) \cong \bigoplus_{\lambda \vdash 3A} V_\lambda^{\oplus d_\lambda}$. Then:*

**(O1) — Trace-dominance.** *The partitions maximising $|y_\lambda(q_0)|$ (Hecke Markov-trace weight) are **1- or 2-row "long-string" partitions** of the form $(n)$, $(n-1, 1)$, $(n-2, 2)$, ..., $(n - k, k)$.*

**(O2) — PSD-dominance.** *The partitions $\lambda^*$ minimising $\varepsilon_{\min}(\lambda) := \min \mathrm{spec}\,\frac{1}{2}(\rho_\lambda(T_w) + \rho_\lambda(T_w)^T)$ (which force the PSD-cone scaling $\alpha^* = 1 / (1 - \varepsilon_{\min}(\lambda^*))$) are **3+row multi-step "tall narrow" partitions** of the form $(c_1^{r_1}, c_2^{r_2}, ...)$ with several distinct row-lengths.*

**(O3) — Shape-class disjointness.** *No partition belongs to both classes. The magnitude separation*
$$
\eta(A) \;:=\; \frac{\max_\lambda |y_\lambda|}{|y_{\lambda^*}|}
$$
*satisfies $\eta(A) \to \infty$ as $A$ grows; empirically $\eta(4) \gtrsim 5 \times 10^5$ and $\eta(6) \gtrsim 9 \times 10^8$.*

## Empirical verification

Across the canonical atoms with `atom_braid_word_3A` recipes implemented in the Rust R5-SDP solver (post-`BraidLetter` extension):

### At A = 4 ($^4$He, $n_0 = 12$)

| family | top member | rows | $y_\lambda(q_0)$ |
|---|---|---:|---:|
| Trace-dominant | $(11, 1)$ | 2 | $7.67 \times 10^{-4}$ |
| Trace-dominant | $(10, 2)$ | 2 | $7.12 \times 10^{-4}$ |
| Trace-dominant | $(9, 3)$ | 2 | $5.87 \times 10^{-4}$ |
| PSD-dominant | $(4, 4, 4)$ | 3 | $1.26 \times 10^{-6}$ |
| PSD-dominant | $(3, 3, 3, 3)$ | 4 | $-4.66 \times 10^{-9}$ |

`η(4) = max trace |y| / min PSD |y| ≈ 7.67e-4 / 4.66e-9 ≈ 1.6×10⁵.`

### At A = 6 ($^6$Li, $n_0 = 18$)

| family | top member | rows | $\varepsilon_{\min}$ | $y_\lambda(q_0)$ |
|---|---|---:|---:|---:|
| Trace-dominant | $(17, 1)$ | 2 | — | $+7.08 \times 10^{-6}$ |
| Trace-dominant | $(18)$ | 1 | — | $+5.86 \times 10^{-6}$ |
| Trace-dominant | $(16, 2)$ | 2 | — | $+6.92 \times 10^{-6}$ |
| PSD-dominant | $(3, 3, 3, 3, 2, 2, 2)$ | 7 | $-116.71$ | $-7.85 \times 10^{-15}$ |
| PSD-dominant | $(5, 5, 5, 3)$ | 4 | $-110.31$ | $-2.84 \times 10^{-11}$ |
| PSD-dominant | $(4, 4, 4, 3, 3)$ | 5 | $-109.81$ | $-4.75 \times 10^{-14}$ |
| PSD-dominant | $(6, 6, 6)$ | 3 | $-95.72$ | $+2.45 \times 10^{-9}$ |

`η(6) = max trace |y| / deepest PSD |y| ≈ 7.08e-6 / 7.85e-15 ≈ 9 × 10⁸.`

### Sign pattern

At A = 6, the three deepest PSD-dominant partitions ($(3, 3, 3, 3, 2, 2, 2)$, $(5, 5, 5, 3)$, $(4, 4, 4, 3, 3)$) all have **negative $y_\lambda$** at $q_0$. They would *subtract* from any positive $\chi^\lambda$ contribution to $\mathrm{tr}_M$. This encodes the bar-anti-symmetric content of the $\sigma_{\mathrm{avg}}$ crossings structurally: the PSD-dominant blocks are the carriers of the *obstruction*, not the carriers of the *mass*.

## Structural interpretation

The conjecture says the categorical roles of "mass-carrier" and "obstruction-carrier" are **structurally separated** in the Wedderburn decomposition. The Markov trace formula $\mathrm{tr}_M(T_w) = \sum_\lambda y_\lambda \chi^\lambda(T_w)$ effectively splits into:

- **Mass-carrying sum** (concentrated in long-string partitions, $y \sim 10^{-6}$ at $n = 18$): this is what the Frobenius formula evaluates to give the physical $m(K)$.
- **Obstruction sum** (concentrated in narrow multi-step partitions, $|y| \sim 10^{-15}$ at $n = 18$): negligible contribution to $\mathrm{tr}_M$, but where $\varepsilon_{\min}$ pulls $\alpha^*$ toward $0$ via the PSD-cone bisection.

The orthogonality says: **the partitions that the canonical atom-braid is "most non-PSD against" are EXACTLY the partitions whose Markov-trace weight is smallest** — there is no overlap. This is a non-trivial categorical fact about how the bar-anti-symmetric content of $\sigma_{\mathrm{avg}}$ distributes across irreducibles.

## Connection to the bar-involution structure

The negative-$y_\lambda$ sign on the deepest PSD-dominant partitions at A=6 is the empirical fingerprint of the bar involution. The transpose-pair structure observed at A=4 ((4,4,4) paired with (3,3,3,3) — see [`conj:atom-braid-exterior-algebra`](conj-atom-braid-exterior-algebra.md) §"Lean structure") extends to a broader pattern: **tall-narrow partitions** (deeper PSD obstruction) and **wide-short partitions** (smaller PSD obstruction, more positive eigval pattern) are bar-paired via the transpose involution but with **asymmetric obstruction depth** — the tall-narrow side is uniformly deeper.

## Implications for the binding-energy Gap

Per canonical evaluation (1) and canonical evaluation (1b) in [`docs/audits/-dominant-partition-nucleon-structure.md`](../../../docs/audits/-dominant-partition-nucleon-structure.md):

The binding-energy gap $|B_{\mathrm{pred}}(K) - B_{\mathrm{AME}}(K)|$ lives in the **trace-dominant family** (the 1/2-row long-string partitions), NOT in the PSD-dominant family. Therefore:

1. Categorical refinement of the framework should focus on the **low-row partitions**, not the rectangular Schur-Weyl partner.
2. The PSD-dominant block is the structural "obstruction fingerprint" but does NOT carry the residual mass deficit.
3. The Δ_λ-gating problem (per AGENTS.md "Precision goals" section) is concretely about which low-row 2-row partitions contribute to the cancellation/imbalance of $\mathrm{tr}_M$.

## Non-claims of this conjecture

- It does NOT predict the *specific* PSD-dominant shape at each $A$. At $A=4$ the dominant is the (A,A,A) rectangle; at $A=6$ it is the multi-step (3,3,3,3,2,2,2) (the rectangular-form conjecture was [categorically falsified at A=6](../../../docs/audits/-dominant-partition-nucleon-structure.md#gap-narrowing-canonical evaluation-4c)).
- It does NOT claim a categorical proof — only an empirical pattern across A=4 and A=6 supported by Lanczos LinearOperator probes.
- It does NOT identify the bar-involution as the categorical mechanism — though the negative-$y_\lambda$ sign pattern is suggestive.

## Cross-references — empirical witnesses

- the canonical formalism — canonical evaluation (1) at A=4
- the canonical formalism — canonical evaluation (1b) at A=6
- the canonical formalism — Lanczos LinearOperator framework
- the canonical formalism — large-$d_\lambda$ scan that falsified the rectangular-form conjecture

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: conj-psd-trace-orthogonality.md -->

<!-- FILE_START: three-halves-structural-factor.md -->
**Proposition (lepton-tower closure structural identities).** *Let
$R$ be a field, $q \in R$ with $q \neq 0$, $h = q - q^{-1}$, and
$[n]_q = q^{n-1} + q^{n-3} + \cdots + q^{-(n-1)}$ the symmetric
q-integer. The following five algebraic identities hold:*

**Muon set** *(canonical for $T(2,5)$, used by `conj:lepton-tower-h-n-plus-1-branching` at $m = 2$):*

$$
3 + h^2 = [3]_q
$$
$$
(2 + h^2) \cdot [2]_q = [4]_q
$$
$$
\frac{3 + h^2}{2 + h^2} = \frac{[3]_q \cdot [2]_q}{[4]_q}
$$

**Tau set** *(canonical for amphichiral $10_{43}$ candidate, used by `conj:lepton-tower-h-n-plus-1-branching` at $m = 3$):*

$$
[6]_q = [2]_q \cdot [3]_q \cdot (1 + h^2)
$$
$$
\frac{[5]_q \cdot [3]_q}{[6]_q} = \frac{[5]_q}{[2]_q \cdot (1 + h^2)}
$$

## Lean

All five identities are proved in
[`three-halves-structural-factor.lean`](three-halves-structural-factor.lean)
over generic `[Field R]` per AGENTS.md §7c, using
`field_simp; ring`. Generic-ring proofs apply at the substrate
$q_0 \approx 1.110$ by specialisation; canonical cross-checks at
exact representation exact algebraic structures verify each identity to $\leq 10^{-40}$ in the
[`tau-amphichiral-sdp-canonical evaluation.witness.json`](../../../computations/canonical evaluations/tau-amphichiral-sdp-canonical evaluation.witness.json)
witness (assertions `lean_three_plus_h_sq_eq_bracket3`,
`lean_two_plus_h_sq_times_bracket2_eq_bracket4`,
`lean_bracket6_eq_bracket2_bracket3_times_one_plus_h_sq`).

## Role in the framework

The structural identities reveal that the canonical lepton-tower
closure factors $\xi_m$ live in a single $h$-graded family of
$q$-bracket products. Concretely:

- **Muon** ($m = 2$, $K_\mu = 4_1$): closure factor
  $\xi_2 = [3]_q \cdot [2]_q / [4]_q = (3+h^2)/(2+h^2)$ — closes
  $m_\mu/m_e$ via $\mathrm{Vol}(4_1)/\hbar_q^2$ to 0.034 % of CODATA
  (`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`).
- **Tau** ($m = 3$, $K_\tau = 10_{43}$ candidate): closure factor
  $\xi_3 = [5]_q \cdot [3]_q / [6]_q$ — closes $m_\tau/m_e$ via
  $\mathrm{Vol}(10_{43})/\hbar_q^2$ to +0.79 % of CODATA
  (`docs/audits/-t6-f-ell-derivation-attempt.md`
  followup section). The reduction
  $[6]_q = [2]_q \cdot [3]_q \cdot (1 + h^2)$ is the fundamental
  identity behind this closure.

The generic family is the subject of
`conj:lepton-tower-h-n-plus-1-branching`; this proposition supplies
the proved algebraic core for the muon (m=2) and tau (m=3) cases.
<!-- FILE_END: three-halves-structural-factor.md -->

<!-- FILE_START: rem-im-q-vs-p-skew.md -->
The framework has **two distinct projection mechanisms** that each
discard structural content. They are often conflated, yet **must
be kept separate**:

## Two mechanisms

### Mechanism 1 — bar projection (real-q phenomenon)

Per [bar-involution.md](bar-involution.md), every Hecke-algebra
element decomposes as $x = P_{\mathrm{avg}}(x) + P_{\mathrm{skew}}(x)$
under the bar involution $q \mapsto q^{-1}$ (equivalently
$\eta = \log q \mapsto -\eta$). The framework's **canonical
projection is $P_{\mathrm{avg}}$** (bar-symmetric, $\cos$/$\cosh$/$\mathrm{Li}_2^q$
content); the bar-anti-symmetric $P_{\mathrm{skew}}$ ($\sin$/$\sinh$/$\Phi_q$
content) is **discarded by construction**.

For **real** $q > 0$, $\eta = \log q$ is real, $\sinh(\eta)$ is a
real number, and $P_{\mathrm{skew}}$ content is **real-valued**.
Sibling makes
this explicit for torus knots:
$Q_m(\eta) = \sinh((2m+1)\eta) / (2 \cosh \eta)$ is real at real $q_0$.
Per
[`crossing-energy-interpretation.md`](../observations/crossing-energy-interpretation.md),
$\sinh(\log q)$ is the **EM / Coulomb channel**. So the EM /
P_skew content **exists** for real $q$ and is discarded by the
canonical projection.

### Mechanism 2 — modulus projection (complex-q phenomenon)

Per [`prop:categorical-mass-markov`](categorical-mass-markov.md),
the categorical mass formula is

$$\mathfrak{m}_{q, \mathcal{K}} = \mathrm{tr}_M(\rho(\beta_\mathcal{K})).$$

The $|\cdot|$ is the modulus. For real $q$, $\mathrm{tr}_M$ is real
and $|\cdot|$ is trivial (absolute value of a sign). For
**complex** $q$, $\mathrm{tr}_M$ becomes complex and $|\cdot|$
genuinely projects: $\mathrm{Im}(\mathrm{tr}_M)$ is discarded.

## A common incorrect claim

A natural-but-incorrect claim is "Im(q) = EM channel = P_skew channel".
This conflates the two mechanisms. The correct statements are:

| Quantity | Source | Status at real q |
|---|---|---|
| $P_{\mathrm{skew}}$ content (sinh, EM channel) | bar projection | **Real-valued, non-zero**, discarded |
| $\mathrm{Im}(q)$ content | complex-q parameter | **Zero by convention** (q real); would generate complex tr_M if non-zero |
| $\mathrm{Im}(\mathrm{tr}_M)$ content | modulus projection | **Zero by convention** for real q; generated by Im(q) $\ne$ 0 |

So:
- P_skew is **kept then discarded** by the framework even at real q.
- Im(q) is **set to zero** by the framework's real-q convention, not "discarded by a projection".
- These are independent.

## Significance

Quantitative consequences differ between the two mechanisms:

1. **Resolving the +0.17% $\mathfrak{Q}_\beta$ residual**: this requires either
   (a) the missing P_skew content at real q (the P_skew channel
   that bar-projection discards), or (b) Im(q) $\ne$ 0 producing
   complex tr_M whose modulus closes the residual.
   - Per [Phase A v2 audit](../../../docs/audits/-q-beta-net-ansatz-fitting-finding.md)
     §Path D + the audit at
     [`m-mu-over-m-e-operator-rederivation.md`](../../../docs/audits/-m-mu-over-m-e-operator-rederivation.md):
     **(b) is ruled out under the current ansatz** (residual is
     positive everywhere on the Apollonius circle).
   - **(a) is open** — accessible via the explicit Q_m P_skew
     content from .

2. **Resolving the canonical lepton-mass formula** $F_\ell(q)$
   ([`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md)):
   the ratio $|\mathrm{tr}_M(K_\mu)| / |\mathrm{tr}_M(K_e)|$ is
   robust against $\mathrm{Im}(q)$ at leading order (modulus
   projection invariance), but **NOT** robust against the
   bar-projection discarding $P_{\mathrm{skew}}$ content
   (the discarded sinh-channel could shift the LO ratio).

3. **Physical interpretation**: $P_{\mathrm{skew}} = $ EM/charge-distinguishing
   channel (sibling  documents this for torus knots).
   $\mathrm{Im}(q) = $ a substrate moduli parameter (not directly
   physical until tied to an observable Im observable, which the
   framework does not currently provide).

## Cross-references

- [`prop:lusztig-vs-hermitian-bar`](lusztig-vs-hermitian-bar.md) — bar vs Hermitian * involutions; this remark interprets/refines its complex-q discussion
- [`prop:q-zero-complex-extension`](q-zero-complex-extension.md) — substrate polymorphism (admits complex q)
- [`prop:categorical-mass-markov`](categorical-mass-markov.md) — modulus projection definition
- [`bar-involution.md`](bar-involution.md) — bar projection definition
- Sibling PR [#1153](https://github.com/litlfred/qou/pull/1153) — explicit P_skew = sinh formula for torus knots
- Audit: [`docs/audits/-complex-q-historical-trajectory.md`](../../../docs/audits/-complex-q-historical-trajectory.md) — historical context of ℂ in physics
- Audit: [`docs/audits/-m-mu-over-m-e-operator-rederivation.md`](../../../docs/audits/-m-mu-over-m-e-operator-rederivation.md) §Implications — Phase 3 finding distinguishing the two mechanisms
- [`crossing-energy-interpretation.md`](../observations/crossing-energy-interpretation.md) — `sinh(log q)` = Coulomb channel identification
<!-- FILE_END: rem-im-q-vs-p-skew.md -->

<!-- FILE_START: conj-im-q-physical-role.md -->
**Conjecture (physical role of Im(q)).**
*The substrate parameter $q$ admits a complex extension
([prop:q-zero-complex-extension](q-zero-complex-extension.md)).
The current QOU framework's observables (categorical masses
$\mathfrak{m}_{q,\mathcal{K}} = |\mathrm{tr}_M|$ and per-braid
mass tower) are real-valued and **insensitive to $\mathrm{Im}(q)$
at leading order** under modulus projection ($\mathrm{Im}(q)$
shifts both numerator and denominator of mass ratios in tandem
via the modulus operation). The physical role of $\mathrm{Im}(q)$
— if any — must therefore be sought in observables not currently
in the framework.*

*This conjecture catalogues three candidate roles, each
testable against a specific observable class. Identifying
which (if any) is the correct physical interpretation is open
work.*

## Exclusions for Im(q)

Per [`rem:im-q-vs-p-skew`](rem-im-q-vs-p-skew.md), Im(q) is **NOT**:
- The EM / $P_{\mathrm{skew}}$ channel (this is a real-q mechanism)
- A fourth calibration input (the 3-CAL count is cohomologically forced)
- An observable in the current framework (mass formula uses $|\cdot|$)
- Equal to $\mathrm{Im}(\mathrm{tr}_M(\rho(\beta)))$ — Im(q) is a parameter; Im(tr_M) is the value induced

## Three candidate physical roles

### Candidate (i) — chirality / orientation parameter

In the Kashaev regime ($q$ a root of unity, $q = e^{2\pi i/N}$),
the q-deformed Hecke algebra produces N-fold quantum symmetries
whose Markov traces give hyperbolic volumes (Kashaev volume
conjecture). For complex $q = |q| e^{i \arg q}$ near the unit
circle, $\arg q$ is naturally a **chirality coordinate** —
positive arg gives clockwise braid orientation; negative arg
gives counterclockwise. The categorical mass formula is invariant
under $q \mapsto \bar q$ (complex conjugation under modulus
projection), consistent with mass being chirality-invariant.

**Testable**: does the framework's prediction for an explicitly
chirality-sensitive observable (e.g., parity-violating decay
asymmetry; CP violation in $K^0$-$\bar K^0$ mixing) require
$\arg q \neq 0$?

### Candidate (ii) — phase coordinate dual to CAL-2

CAL-2 ($m_\mu/m_e = 206.7682830$) gives **one real equation** on
two real unknowns ($\mathrm{Re}(q), \mathrm{Im}(q)$). The solution
set is an **Apollonius circle** in the complex q-plane (center
$\approx 1.010$, radius $\approx 0.100$ per the formal derivation).
The framework's real-axis solution $q_0 \approx 1.10998$ is one
point on this circle; Im(q) is the arc coordinate parametrizing
the other admissible q values.

**Testable**: does another CAL-2-like independent constraint
(a second real equation from $m_\tau/m_e$, or from a different
observable) fix a unique complex $q_0$? If only real solutions
exist, candidate (ii) is closed; if a complex solution is needed,
the framework has missed an Im(q)-coupled measurement.

### Candidate (iii) — non-Hermitian deformation / open-system parameter

The Hoefsmit seminormal Hecke representation has real-coefficient
matrices for $q > 0$ real, giving **unitary** $H_n(q)$ representations.
For complex $q$ with $|q| \neq 1$, unitarity breaks: representations
become non-unitary; eigenvalues become complex. In quantum mechanics,
non-Hermitian operators arise in **open systems** (decay, dissipation,
resonance widths).

**Testable**: do decay widths (Γ for unstable particles — W, Z,
top, resonances) correlate with the Im(q) needed to make Hecke
representations describe their non-Hermitian dynamics? Most decay
widths in the Standard Model have categorical interpretations open
in the QOU framework.

## Obstacles to a current proof

Each candidate requires an observable the framework does not yet
provide:
- (i) needs explicit chirality-sensitive observables (CP violation, parity asymmetry)
- (ii) needs a second independent CAL-2-like constraint
- (iii) needs a categorical formula for decay widths $\Gamma$

The framework's mass formula explicitly **projects away** Im(q)
content via $|\cdot|$, so no mass observable can detect Im(q)
directly. The candidate roles are all in **non-mass observables**.

## Connection to other conjectures

- [`conj:lepton-mass-tower-canonical`](lepton-mass-tower-canonical.md) F_ℓ
  — the canonical lepton-mass formula is Im(q)-robust (modulus projection
  invariance); F_ℓ does NOT distinguish the three candidate Im(q) roles.
  Hence the F_ℓ conjecture is consistent with ALL three candidates.
- [`prop:rho-k-pair-gen-canonical-form`](conj-rho-k-pair-gen-canonical-form.md) —
  similarly Im(q)-robust at LO.
- The complex-q machinery is **decoupled** from the mass-formula closure;
  closing the $\mathfrak{Q}_\beta$ residual or deriving F_ℓ does **not** require resolving
  Im(q)'s role.

## Default value: Im(q) = 0

In the absence of an Im(q)-sensitive observable, the framework's
canonical choice is **$\mathrm{Im}(q_0) = 0$** (real q). This is:
- **Computationally simple**: real Hecke arithmetic, real
  $\mathrm{tr}_M$, real masses.
- **Empirically sufficient**: all known mass observables fit
  with real $q_0$ to the precision documented in `per-observable-100x-status.witness.json`.
- **NOT structurally forced**: nothing in the QOU framework's
  cohomological discipline requires $\mathrm{Im}(q) = 0$; it is a
  convention pending an Im-sensitive measurement.

## Cross-references

- [`prop:q-zero-complex-extension`](q-zero-complex-extension.md) — substrate polymorphism
- [`prop:lusztig-vs-hermitian-bar`](lusztig-vs-hermitian-bar.md) — involution split for complex q
- [`rem:im-q-vs-p-skew`](rem-im-q-vs-p-skew.md) — the distinction from P_skew
- [`prop:categorical-mass-markov`](categorical-mass-markov.md) — modulus projection
- Audit: [`docs/audits/-m-mu-over-m-e-operator-rederivation.md`](../../../docs/audits/-m-mu-over-m-e-operator-rederivation.md) — Phase 3 finding
- Audit: [`docs/audits/-complex-q-historical-trajectory.md`](../../../docs/audits/-complex-q-historical-trajectory.md) — historical context
- Audit: [`docs/audits/-q-beta-net-ansatz-fitting-finding.md`](../../../docs/audits/-q-beta-net-ansatz-fitting-finding.md) §Q3 — Apollonius parametrization

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: conj-im-q-physical-role.md -->

