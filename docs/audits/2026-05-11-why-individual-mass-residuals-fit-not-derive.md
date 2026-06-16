# Why individual-mass residuals are large — fitting vs derivation audit

**Date:** 2026-05-11
**Branch:** `claude/neutron-mass-50dps-chain`
**Trigger:** "we are fitting/guessing not relying on derivation" +
"1ppb target for ALL" + "make sure compute and paper don't have
wrong E_0's".

## Headline finding (updated 2026-05-11 after E_0 audit)

The framework has **three E_0 conventions** in `derivation_chain.E_0_CONVENTIONS`:

- **Conv A** — $E_0 = m_e/(q_0(q_0-1)) \approx 4.186$ MeV — **substrate-derived** from CAL-1 + CAL-2 alone (the "categorical E_0").
- **Conv B** — $E_0 = Q_\beta^{\text{CODATA}}/|\Delta(\text{net})| \approx 4.179$ MeV — calibration to CAL-3 directly.
- **Conv C** — $E_0 \approx 200$ MeV — back-fit to CODATA $m_p$. The registry flags this as **"⚠️ DISCIPLINE VIOLATION. Do not consume in new production chains."**

### Compute audit — Conv C consumers (2 scripts)

| File | Line | Pattern |
|------|------|---------|
| `atomic_braid_mass_table.py` | 441 | `E_0 = (M_p - p_terms["t6_MeV"]) / p_terms["total_hecke"]` |
| `atomic_braid_mass_table_modes_sweep.py` | 259 | same back-fit pattern |

These two scripts explicitly back-fit $E_0$ to CODATA $m_p$, then "predict" other atoms with the fitted value. Both are already flagged in `E_0_CONVENTIONS["C_proton_back_fit"]` as discipline-violating. Per the registry, downstream production should consume Conv A (mass / Q_β predictions) or Conv B (binding predictions), not C.

### Paper audit — Conv C in content blocks

**Zero hits.** No `.md` content block cites $E_0 = 200$ MeV or "proton back-fit" as a paper-level formula. The paper consistently uses Conv A ($m_e/(q(q-1))$ ≈ 4.186 MeV) per `energy-scale-planck.md` and `calibration-inputs.md` — both substrate-derived. ✓ paper clean.

### Where the residual really comes from

With paper + Conv-A compute clean, the 999M ppb residual on the substrate-only neutron mass chain is NOT due to a wrong E_0. The chain uses
$$m_n^{\text{pred}} = (m_n^{\text{Hecke}} / m_e^{\text{Hecke}}) \cdot m_e^{\text{CODATA}}$$
— a cat-units ratio, not an E_0 prediction. The "fit" is the **implicit ansatz** that cat-units ratios equal physical mass ratios. Empirically the cat-units ratio is $\sim 1.17$ while the physical ratio is $\sim 1836$ — a structural gap of $\sim 1570\times$.

Substituting Conv A explicitly: $m_p \approx E_0 \cdot |\mathrm{tr}_M(\beta_p)| \approx 4.186 \cdot 1.065 \approx 4.46$ MeV — also $\sim 99.5\%$ off. So Conv A applied directly to a single nucleon does not close the gap either. The framework's individual-mass formula is structurally incomplete regardless of which derived $E_0$ is used.

**The 1ppb target on ALL quantities requires either:**
1. Closure of the `brane-tower-z-habiro` $n_\star$ conjecture (open R&D, may close binding-energy residuals to ~5%, much further still to 1ppb).
2. A **substrate-derived $\lambda_{\text{scale}}$** for the Borromean baryon-mass formula
   $m(B) = \mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2 \cdot \lambda_{\text{scale}} + \text{Skein corrections}$
   from `borromean-baryon-interpretation.md`. **Status:** $\lambda_{\text{scale}}$ is **declared but not defined** anywhere in `content/` or `computations/` — it's an undefined symbol in the paper's mass formula. This is the next concrete "open derivation" needed.
3. Quark-mass / QCD-scale inputs (would expand the 3-cal discipline; needs author authorization).

**The 999M ppb residual on PR #640 is honest substrate-only exposure of the missing $\lambda_{\text{scale}}$ / $n_\star$ closure.** Not noise to close via tweaks.

## What works (genuinely derived)

| Quantity | Substrate path | Result | Status |
|----------|---------------|--------|--------|
| $Q_\beta$ | $\|\Delta(\text{net})\| \cdot E_0$, $E_0 = m_e/(q(q-1))$ | 0.7836 MeV (CODATA 0.7823, **+0.17%**) | ✓ derived from CAL-1 ($m_e$) + CAL-2 ($q_0$) alone |
| $\Phi_q$ closed form | $Q_\beta = m_e \cdot \|q_0^2 - 2 q_0 - 1\| \cdot (q_0+1)/(2 q_0^3)$ | 0.7836 MeV | ✓ pure CAL-1 + CAL-2 |
| $\hbar_q$, $c_q$ | $\hbar_q = (q-1)/q$, $c_q = 1/(q-1)$ | CODATA-matched | ✓ pure CAL-2 |

Pattern: **differences and dimensionless constants** are reachable.

## What doesn't work (fits / guesses creep in)

### Numerical diagnostic — `m_p_pred` is off by ~1570× from Path A alone

Substrate-only Path A (T1 + T4) at $q_0$, **no CODATA mass injection**:

```
m_e_Hecke  =  2.0027  (cat units)
m_p_Hecke  =  2.3414
m_n_Hecke  =  2.1993

Path A ratio  m_p_Hecke / m_e_Hecke  =  1.1691
CODATA       m_p / m_e               =  1836.15
→ Off by factor 1570×  (3 orders of magnitude)
```

The framework's cat-units ratios for individual particles **do not
carry the physical mass hierarchy**. Multiplying by $m_e^{\text{CODATA}}$
gives $m_p \approx 0.597$ MeV, not 938 MeV.

### E_0 conventions don't rescue it — all of them require fitting

Per `docs/audits/2026-05-10-hbar-q-scaling-audit.md`:

| Convention | $E_0$ value | $m_p$ via $E_0 \cdot |\mathrm{tr}_M(\beta_p)|$ | Error |
|------------|-------------|---------------------------------------------|-------|
| A — single-tick $m_e/(q(q-1))$ | 4.186 MeV | 9.80 MeV | −98.96% |
| B — $Q_\beta$-absorbed $Q_\beta/\|\Delta(\mathrm{net})\|$ | 4.179 MeV | 9.78 MeV | −98.96% |
| C — **proton back-fit** | 200 MeV | 468.3 MeV | −50.09% |

Conventions A and B are substrate-derived (CAL-1 + CAL-2 only) but
give $m_p \approx 10$ MeV — far from 938 MeV. Convention C is
**explicitly back-fitted** to give the right ballpark, and even
then it's 50% off.

**No $E_0$ convention reaches $m_p = 938$ MeV from the framework's
$|\mathrm{tr}_M|$-based formula.** The framework is structurally
missing the QCD binding scale.

### Where the "fit" is hiding

| Site | Fitting form | Severity |
|------|--------------|----------|
| `atomic_mass_via_rho_k.py:188` (LO formula) | $\rho_K^{LO} = (Z m_p + N m_n)/(m_e\|\mathrm{tr}_M\|)$ consumes CODATA $m_p, m_n$ | Hard violation per `2026-05-11-three-calibration-discipline-violations.md`; flagged in #637 as "LO TAUTOLOGY NOTICE" |
| `E_0_CONVENTIONS["C"]` | Back-fitted to 200 MeV "proton" anchor | Audited in `2026-05-10-hbar-q-scaling-audit.md`; flagged but not removed |
| Old `M_HECKE_PIPELINE_AT_Q0_LEGACY["p"] = 1.4283` | Numerologically tuned to $(m_p - m_e)/m_e$ ratio | Quarantined to `_LEGACY` dict by #637 |
| **Cat-units $\to$ MeV via ratio with $m_e$** | Assumes `m_X_Hecke / m_e_Hecke = m_X / m_e` | **Implicit ansatz, not derived**; this is the structural issue |

The last row is the deepest issue and the one closest to "fitting
by assumption". The framework writes:

$$
  m_X^{\text{pred}}\;=\;\frac{m_X^{\text{Hecke}}}{m_e^{\text{Hecke}}}\cdot m_e^{\text{CODATA}}
$$

with no derivation that the ratio $m_X^{\text{Hecke}}/m_e^{\text{Hecke}}$
equals the physical $m_X/m_e$. Empirically it doesn't:
$m_X^{\text{Hecke}}/m_e^{\text{Hecke}} = \mathcal{O}(1)$ for any
particle the framework's $|\mathrm{tr}_M|$-based formula touches,
while physical mass ratios span $\mathcal{O}(10^3)$ at the proton scale.

## Why differences work but absolutes don't (structural reason)

The framework's $|\mathrm{tr}_M|$ is a **topological invariant** of
the braid — it captures crossing structure, bar-involution behavior,
and Hecke-algebra normal forms. It does **not** capture:

- Quark masses ($m_u, m_d, m_s$) — these are SM inputs the
  framework doesn't currently consume.
- QCD binding scale ($\Lambda_{\text{QCD}} \approx 200$ MeV) — the
  dominant contribution to proton mass via gluon-field energy.
- Electromagnetic energy splitting.

The proton and neutron are both 3-strand braids in $H_3$ with 11
crossings. Their topological difference is small — one $\sigma$ vs
$\sigma^{-1}$ in the (u,u,d) vs (u,d,d) flavor encoding. Indeed
$|tr_M(\beta_p)| - |tr_M(\beta_n)| \approx 0.14$ at $q_0$ — small
compared to $|tr_M|$ itself ($\sim 1$). That topological difference
**can** be derived; multiplying by an $E_0$ derived from
CAL-1 + CAL-2 gives $Q_\beta = +0.78$ MeV, matching CODATA to
+0.17%.

But the absolute mass of either particle requires the full QCD
energy — which the topology-only framework doesn't carry.
Multiplying $|tr_M|$ by any $E_0$ derived from CAL-1+CAL-2 gives
$\mathcal{O}(\text{MeV})$, not $\mathcal{O}(\text{GeV})$. The
1570× / 3-orders-of-magnitude gap is **inherent**, not numerical.

This is what PR #637 calls "the substrate-only framework is
honest about the residual" — the 1.84% / −62.9% errors on
individual nucleon masses (via the Φ_q tower path) are the
framework's actual state, not a numerical issue to close.

## Recommended reframing

| Quantity | Status under current framework | Recommendation |
|----------|-------------------------------|----------------|
| $Q_\beta(n)$ | **DERIVED** to +0.17% via $\Delta(\text{net}) \cdot E_0$ | Keep as substrate-derived prediction (also CAL-3 calibration anchor, but the closed form ≈ CODATA). |
| $\Delta m = m_n - m_p$ | DERIVABLE via $Q_\beta + m_e$ (Δ(net) approach) | Same as $Q_\beta$. |
| $m_p$, $m_n$ individually | **NOT DERIVED** — gap of $\sim 10^3$ to CODATA | Reframe paper's claim: the substrate-only framework predicts mass DIFFERENCES (Q_β, isospin splits), not absolute hadron masses. Absolute masses require QCD binding-scale input. |
| $m_e$ | CAL-1 (definitional anchor) | Keep. |
| $m_\mu$ | DERIVED via $m_\mu = m_e \cdot \mathrm{Vol}(4_1) / \hbar_q^2$ | Keep. |

The current `recomputed-low-isotope-mass-table.md` already flags
the $(p, n)$ rows as "calibration tautology, not a prediction
quality" (post-#637). The next iteration should extend this honesty
to the broader **paper-level claim about predicting absolute
nucleon masses** — the framework does not currently do that.

## What this means for the neutron-chain residual on PR #640

The 999M ppb residual on `build_neutron_mass_50dps_chain.py` is the
**honest substrate-only deliverable**. No fitting needed to fix it
— the residual IS the deliverable. Closing it would require:

1. Adding a QCD-scale calibration input (would be CAL-4, violating the
   3-input discipline).
2. OR closing the brane-tower $n_\star$ truncation rule
   (`brane-tower-z-habiro` open conjecture) to bring T2+T3 in for A=1
   — speculative.
3. OR fundamentally restructuring the framework to encode flavor
   information ($u$ vs $d$ quark) at the braid level.

None of these are 1ppb-trail items. The 1ppb target was always for
$Q_\beta$ (which works), not for individual $m_p / m_n$ (which
don't).

## Action items

1. **Update PR #640 description** to clearly state the residual is a
   structural exposure, not a fit-to-close target. (chain itself
   already says this in its notes.)
2. **Coordinate question for author**: should the paper claim that
   the framework predicts absolute nucleon masses, or only mass
   differences and ratios? Current state implies the former; the
   evidence supports only the latter.
3. **Optional**: deprecate `E_0_CONVENTIONS["C"]` (the 200 MeV
   back-fit) since it's explicit fitting per the 3-cal discipline.

## Cross-references

- `np-discrepancy-resolution.md` (on main, post-#637) — same finding from a different angle.
- `derived_masses.py` (on main, post-#637) — the Q_β closed form.
- `2026-05-10-non-calibrated-mass-state-of-play.md` — comprehensive state of play.
- `2026-05-10-hbar-q-scaling-audit.md` — three E_0 conventions audited.
- `2026-05-11-three-calibration-discipline-violations.md` — earlier audit on the m_p, m_n input violations.

## Update 2026-05-11 — τ_M / τ_SW conflation diagnosis

Synthesised from the Frobenius non-degeneracy proof (commit
[`25a204efa`](https://github.com/litlfred/qou/commit/25a204efa)
on `main`, which introduced
[`markov-trace-frobenius-selection.md`](../../content/quantum-observable-universe/braids-and-knots/markov-trace-frobenius-selection.md))
+ the PR #487 agent's reply documented in
[`docs/agent-briefs/2026-05-11-lambda-scale-borromean-baryon-derivation.md`](../agent-briefs/2026-05-11-lambda-scale-borromean-baryon-derivation.md).

### Two distinct Frobenius forms have been conflated

The Hecke-algebra Markov-trace registry contains values for **two
different** linear functionals, both labelled "tr_M":

| Form | Source | $\tau(D, q_0)$ | $\tau(p, q_0)$ |
|------|--------|---------------:|---------------:|
| **Jones-Markov** $\tau_M$ | Wenzl-bridge, `from_scratch/` chain | $0.3368$ | $1.7339$ (free) |
| **Schur-Weyl** $\tau_{\mathrm{SW}}$ | `schur-weyl-weight-*.derivation.json` | $0.1774$ | $2.1226$ |
| Registry (mixed) | `derivation_chain.TR_M_AT_Q0` | $0.3883$ | $1.0653$ |

The Frobenius proof on `main` proves $\tau_M$ is the **unique**
non-degenerate Frobenius pairing on $H_n(R, q)$ and is therefore
the canonical Markov trace for the QOU mass identity. $\tau_{\mathrm{SW}}$
is degenerate on height-$> 2$ partitions (Schur-vanishing) and so
cannot satisfy the Frobenius co-Casimir construction.

### Affected scripts

The `markov-trace-assembly-proton.derivation.json` chain combines
the three `schur-weyl-weight-{3,21,111}` chains via the
finite-Jones formula, producing $2.1226$ at $q_0$. The chain
description labels this "canonical Wenzl-bridge τ_M", but
the underlying weights $w_\lambda = s_\lambda(q, q^{-1}) / H_q(\lambda)$
**are** the Schur-Weyl weights — so the assembly chain is actually
computing $\tau_{\mathrm{SW}}$, not $\tau_M$.

The `habiro_coefficients_atomic.py` pipeline (mislabelled
"Markov trace") computes $\tau_{\mathrm{SW}}$ as well. The
PR #472 agreement between polynomial and residue paths is between
two computations of the *same* $\tau_{\mathrm{SW}}$ quantity — it
does not confirm the canonical $\tau_M$.

### Where the $\lambda_{\text{scale}} \approx 2.46$ might live

The PR #487 agent reports $|\tau_M(p_{\text{free}})| = 1.7339$
from the canonical `from_scratch/` pipeline (using the
single-component free-proton braid, not the 11-crossing canonical
recipe).

If $\lambda_{\text{scale}}$ is the **representation-translation
factor** between the Borromean (3-link, $\beta_{\text{Bor}}$,
6-crossing) and canonical (1-knot, 11-crossing) ansätze, then

$$
  \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2} \cdot \lambda_{\text{scale}}
  \;\overset{?}{=}\;
  m_e \cdot \rho_p \cdot |\tau_M(p_{\text{free}})|
$$

solves for $\rho_p$, but $\rho_p$ then becomes a free per-knot
parameter — not a substrate-only quantity. This is consistent
with the PR #487 agent's diagnosis that "the substrate-only
identity doesn't exist".

### Implication for 1ppb on individual hadron masses

The framework's individual-hadron mass formulas as currently written
are **two ansätze pinned at different braid representatives**, with
a representation-translation factor ($\lambda_{\text{scale}}$ in the
Vol formalism, $\rho_K$ in the $\tau_M$ formalism) that is **not
substrate-derivable** in either direction. Closing this requires:

- **Picking one ansatz** (3-link Borromean OR 1-knot canonical 11-crossing) and dropping the translation factor;
- **Or deriving the translation factor** from the categorical bridge between the two ansätze (open R&D).

Either way, the Vol-form Borromean baryon block on this branch
([`borromean-baryon-mass-formula.md`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-mass-formula.md))
documents the formalism honestly: the formula is a *conjecture*
because $\lambda_{\text{scale}}$ has no substrate derivation.

### Action items (added 2026-05-11)

4. **Relabel the registry**: rename `schur-weyl-weight-*.derivation.json`-derived
   `tr_M` values to `tau_SW` (per Frobenius proof recommendation in
   `markov-trace-frobenius-selection.md` § "Computational consequence").
5. **Audit `derivation_chain.TR_M_AT_Q0`**: confirm whether the values
   $p = 1.0653$, $n = 0.9232$, $D = 0.3883$ are $\tau_M$ or $\tau_{\mathrm{SW}}$;
   add a comment annotating which.
6. **Compute $J_{\mathcal{B}_3}(q_0; \text{orientation} = (k, 3-k))$
   symbolically** for $k \in \{0, 1, 2, 3\}$ — diagnostic (b) for
   pinning the Skein correction. (Per PR #487 agent's "most
   actionable next step".)

## Resolution 2026-05-29 (#1422, decision A')

The 2026-05-11 "$\tau_M$ / $\tau_{\mathrm{SW}}$ conflation" framing
above is **superseded**.  On closer reading the audit doc itself
records (line 248-251) that the from-scratch value
$|\tau_M(p_{\text{free}})| = 1.7339$ is "from the
**single-component free-proton braid**, *not* the 11-crossing
canonical recipe" — i.e. it is $\tau_M$ of a *different braid*,
not a different convention of the same braid.  No conflation of
$\tau_M$ vs $\tau_{\mathrm{SW}}$ for the canonical braid was ever
present in production.

Four independent production methods now agree on the canonical
$\tau_M(\beta_{\rm atom}, q_0)$ for the 11-crossing recipe to
$\leq 2 \times 10^{-15}$ at the proton-pinned $q_0$:

- proton  $1.0653061442544499$
- neutron $0.9232332299116371$
- deuteron $0.3882864240747888$

Lean theorem `qou_markov_trace_is_jones_markov`
(`content/quantum-observable-universe/mass-theory/markov-trace-frobenius-selection.lean`)
is refactored 2026-05-29 from a *selection-by-contrast* with
$\tau_{\mathrm{SW}}$ into a direct **uniqueness statement**
axiomatising Wenzl 1990 / Jones 1987 via a
`MarkovTraceUniqueness` class (CLAUDE.md §3b-cond pattern).

**Status of the rest:**

- $\tau_{\mathrm{SW}}$ (Schur–Weyl) and its supporting Lean theorems
  (`schur-weyl-vanishing.lean` and friends) are **fully purged**
  2026-05-29 — deleted from `mass-theory/`, dropped from the
  manifest, references removed from the `derivation_chain.py`
  resolution comment.  Not re-pursued.
- `from_scratch/` is **deprecated for production** (different
  braid; pedagogical derivation only) — kept on disk so existing
  pedagogy / cross-checks for the free-proton braid don't break.
  Not re-pursued.
- Action items 4 + 5 (re-label registry, audit `TR_M_AT_Q0`) are
  **superseded** — `derivation_chain.py` was re-pinned to the
  proton-q₀ canonical Jones–Markov values per #1422, and the
  rename to "$\tau_{\mathrm{SW}}$" is moot since the SW path is
  purged.  Item 6 (orientation-symbolic $J_{\mathcal{B}_3}$) remains
  open R&D under `prop:geom-universality` refinement.
- Broader uniqueness programme (T_w SDP, p-n averaging, VolDensity):
  queued in [`docs/uniqueness-theorems-backlog.md`](../uniqueness-theorems-backlog.md).
