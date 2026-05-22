# Agent brief — `λ_scale` from q-dilog tower direct parametrisation

> **Audience.** A future agent picking up the CAL-4 closure work
> for the Borromean baryon mass formula. The Bring-Bloch path has
> been exhausted (6-tier consistent negative); this brief sets up
> the **q-dilog tower direct parametrisation** as the alternative.
>
> **Status when this brief was written (2026-05-22).** `λ_scale` is
> a hardcoded literal in production. Migration Backlog #1 per
> [`docs/canonical-derivation-cheat-sheet.md §5`](../canonical-derivation-cheat-sheet.md).

## TL;DR

Find a closed-form expression for `λ_scale ≈ 2.4599527869` (proton
closure target for the Borromean baryon mass formula) using the
q-dilog tower at `q = q_0` directly, **bypassing the Bring-Bloch
hyperbolic-volume search** which the 6-tier consistent negative has
ruled out for the proton's Bring-decomposition class.

## Background — what is `λ_scale` and why does it matter

The **Borromean baryon mass formula**
([`conj:borromean-baryon-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-mass-formula.md)):

$$
\mathfrak{m}(B) = m_e \cdot \left[\frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2} \cdot \lambda_{\mathrm{scale}} + S(B)\right]
$$

- `m_e` (CAL-1) and `q_0` (CAL-2 via `m_μ/m_e`) are the only
  calibration inputs.
- `Vol(𝓑₃) = 8G ≈ 7.32772...` is a fixed topological invariant
  (Catalan's constant identity per
  [`prop:binding-scale-catalan`](../../content/quantum-observable-universe/braids-and-knots/binding-scale-catalan.md);
  see also the 100-dps witness chain referenced from
  [`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md)).
- `ℏ_q = (q-1)/q` is the q-deformed Planck constant; at `q_0`
  this gives `Vol(𝓑₃)/ℏ_q² ≈ 746.4`.
- `S(B)` is the Skein-orientation correction (different for proton
  vs neutron); structurally derivable.
- **`λ_scale` is currently hardcoded:** `LAMBDA_PROTON_DOC =
  mp.mpf("2.4599527869")` in
  [`folio-assistant/computations/m_p_borromean_verification_50dps.py:100`](../../folio-assistant/computations/m_p_borromean_verification_50dps.py).
  It was solved against CODATA `m_p` (a CAL-4 violation in
  disguise; see
  [`docs/audits/2026-05-18-210x-scale-gap-root-cause-v2.md`](../audits/2026-05-18-210x-scale-gap-root-cause-v2.md)).
  Closing `λ_scale` in closed form would resolve the only known
  CAL-4 violation in the production mass pipeline.

## Why Bring-Bloch is exhausted

Per [`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md),
the conjecture was `λ_scale = (1/8G) · D(Σ_i n_i^(p) [Z_K_i])` where
`D` is the Bloch-Wigner dilogarithm and `n_i^(p)` is an integer
multiset over hyperbolic-knot Bring-decomposition classes. The
search for this multiset via PSLQ has been run at 6 tiers:

| Tier | Basis | PSLQ tol | maxcoeff | Result |
|---|---:|---:|---:|---|
| 0 | 8 (Atlas) | — | 10³⁰ at 80 dps | NULL |
| 1 | 11 (Birman–Hilden 3-braid) | 1e-15 | 10⁸ at 100 dps | NULL |
| 2 | 16 (+ bridge-3) | 1e-12 | 10⁶ | NULL |
| 3 | 33 (+ 9-cross primes) | 1e-12 | 10⁵ | NULL |
| 4 | 40 (+ 10-cross primes) | 1e-12 | 10⁵ | NULL |
| 5 | 52 (+ 11-cross primes) | 1e-10 | 10⁵ | NULL |

52 hyperbolic-knot volumes searched, brackets the target `Vol(K_p^eff)
≈ 18.026` from below and above. The proton's Bring-decomposition is
**not** a ℤ-linear combination of prime hyperbolic-knot volumes
≤ 11 crossings.

Tier-search scripts:
[`folio-assistant/computations/bring_bloch_tier{1..5}_search_m_p.py`](../../folio-assistant/computations/).

## What "q-dilog tower direct parametrisation" means

Two q-dilogarithms are used in the framework
([`docs/canonical-derivation-cheat-sheet.md §4`](../canonical-derivation-cheat-sheet.md)):

| | Φ_q (Faddeev) | Li_2^q (Rogers) |
|---|---|---|
| Bar-symmetry | NOT (mass-anchor, asymmetric) | YES (binding, bar-symmetric) |
| Context | MASS | BINDING |
| Reference | [faddeev1996] | [kashaev1995] / [kirillov1995] |

**The hypothesis to test:** at the substrate point `q_0`, the
proton's `λ_scale` should be expressible as a **closed-form
combination of values of one of the two q-dilogarithms evaluated at
algebraic points in `ℚ(q_0)`** — bypassing the hyperbolic-volume
detour entirely. Candidate forms:

1. **Rogers-only** (bar-symmetric, binding-side): `λ_scale = α ·
   Li_2^q(z_1) + β · Li_2^q(z_2) + ...` for integer `α, β, ...`
   and `z_i ∈ ℚ(q_0)`.
2. **Faddeev-only** (bar-asymmetric, mass-side): `λ_scale = α ·
   Φ_q(w_1) + β · Φ_q(w_2) + ...` similar form.
3. **Mixed via the three-layer synthesis** (post-Phase 5b, PR #819):
   `Li_2^q ↔ cos_q(h) ↔ cosh(h)` — three avatars of the same
   bar-symmetric kernel at series / phase / closed-form levels.
   So `λ_scale` may admit a `cosh(h)` closed form via the
   `cosh ↔ Li_2^q` ladder.
4. **Kashaev-style integration identity** — Φ_q satisfies an
   integration identity that produces algebraic numbers when
   integrated against specific contours; check if the proton
   value emerges from such an integral at q_0.

## What's already known structurally

From [`prop:lambda-scale-bring-bloch-identity §Open work`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md):

> Three tasks remain:
> 1. Find K_p's explicit decomposition (Tier 1+ PSLQ search;
>    or derive from knot-operator LP/SDP).
> 2. Verify universe-level closure Σ_p D([Z]^(p)) = 2/(3π).
> 3. Categorically derive C2-inflection mechanism from
>    Bring-Bloch action.

Task #1 is the hard one. Task #3 hints at a **C2-inflection** at
the substrate point — `λ_scale` may emerge from where the q-dilog
tower has a curvature feature (inflection point) at q_0.

From the cheat sheet, the Phase 5b synthesis
`Li_2^q ↔ cos_q(h) ↔ cosh(h)` provides three avenues for the
same bar-symmetric kernel. The **mass-side equivalent**
(Faddeev tower, bar-anti-symmetric) is queued as the §7 #4
open frontier in
[`docs/audits/2026-05-20-compute-wiring-audit-pr-852.md`](../audits/2026-05-20-compute-wiring-audit-pr-852.md):
> "q-dilog tower direct λ_p_scale derivation (post-bar-anti-sym,
> given 6-tier negative Bring-Bloch)"

## Concrete search strategies

In approximate order of expected ROI:

### Strategy A — Rogers `Li_2^q` PSLQ at algebraic substrate points

Build a basis of `Li_2^q(z)` values for `z` in `ℚ(q_0)`'s natural
algebraic locus: `z ∈ {q_0, 1/q_0, q_0², 1-q_0, -q_0, q_0·(q_0-1),
1/(q_0(q_0-1)), q_0³, q_0/(q_0+1), ...}`. Run PSLQ against the
target `λ_scale = 2.4599527869...` at 80–100 dps.

**Compute kernel.** Use `folio-assistant/computations/li2q.py`
(or whichever script wraps Li_2^q in the framework — search via
`grep -l li2q folio-assistant/computations/*.py`). MPFR 50 dps,
PSLQ via `mpmath.pslq`.

**Estimated cost.** Hours, similar to Bring-Bloch tier searches.

### Strategy B — Faddeev `Φ_q` mass-side PSLQ

Same as Strategy A but with `Φ_q(w)` (bar-asymmetric). The
mass-anchor context is the right side for `λ_scale` which
multiplies the topological volume → mass scale.

**Compute kernel.** `folio-assistant/computations/phi_q.py` or
similar; CMP per `Φ_q` definition in
[`prop:mass-tower-operator-valued`](../../content/quantum-observable-universe/braids-and-knots/mass-tower-operator-valued.md).

### Strategy C — cosh / cos_q ladder

Via the Phase 5b synthesis, try `λ_scale = a · cosh(b·h) + c ·
cosh(d·h)` for small integers `a, b, c, d` and `h = q − q⁻¹`.
The closed-form `cosh` level is the easiest to PSLQ.

Already tried (negative): the "5/2 − h²·G ansatz" was an
empirical PSLQ coincidence at `h, h²` order;
[`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md)
notes this. Look for **higher-order combinations** (`h³`, `h⁵`)
or different basis functions (`sinh`, `cosh(h)^n`).

### Strategy D — Direct categorical derivation from `𝓑_p`

Compute `λ_scale` directly from the canonical proton Hecke
element `𝓑_p` (canonical braid construction;
[`folio-assistant/computations/canonical_braid_marshalling.py`](../../folio-assistant/computations/canonical_braid_marshalling.py))
via a knot-operator-LP/SDP problem. This bypasses PSLQ entirely:
solve for the canonical structural object whose evaluation at
q_0 yields `λ_scale`.

**Compute kernel.** Extend
[`folio-assistant/computations/lp_dual_solver.py`](../../folio-assistant/computations/lp_dual_solver.py)
with a `lambda_scale_from_braid_p` solver that takes 𝓑_p and the
Vol(𝓑₃) topological invariant and produces `λ_scale` as an LP/SDP
output.

### Strategy E — Universe-level closure

Per the `prop:lambda-scale-bring-bloch-identity` §Open work item #2:
verify `Σ_p D([Z]^(p)) = 2/(3π)`. This is a **constraint** the
correct `λ_scale` parametrisation must satisfy. If you find a
candidate via A/B/C, plug it into the closure identity and check.

## Alternatives to Strategy D (added 2026-05-22)

Strategy D requires extending `lp_dual_solver.py` with a
`lambda_scale_from_braid_p` solver — substantial infrastructure
work. The strategies below are structural alternatives that
either bypass LP/SDP or use existing infrastructure with smaller
incremental cost. They occupy the same "structural / non-PSLQ"
solution slot as Strategy D and should be exhausted before
committing to D's infrastructure lift.

Empirical results from the 2026-05-22 first-pass execution are
recorded inline.

### Strategy F — Markov-trace identity test on β_Bor

Test the hypothesis that the two formalisms (Markov-trace, Vol-form)
agree on the bare 6-crossing Borromean braid:

  `λ_scale  ?=  |tr_M(β_Bor, q_0)| · ℏ_q² / Vol(𝓑_3)`

where `β_Bor = (σ_1^{-1} σ_2)^3 ∈ B_3 ⊆ H_3(q)`.

**Compute kernel.** `lambda_scale_alt_f_markov_trace_beta_bor.py`
(this brief; uses existing `hecke_character_symbolic` and
`y_lambda_wenzl_bridge` infrastructure). Single 5-min compute.

**Estimated cost.** ~5 min single compute; instant verdict.

**Result (2026-05-22, witness
`lambda-scale-alt-f-markov-trace-beta-bor.witness.json`):**
**FALSIFIED.**

  | quantity | value at q_0 |
  |---|---:|
  | `tr_M(β_Bor, q_0)` | 0.998366621839... |
  | `ℏ_q² / Vol(𝓑_3)` | 1.339903... × 10⁻³ |
  | candidate (above product) | 0.001337543870979 |
  | target λ_p | 2.4599527869 |
  | rel diff | −99.95 % (three orders of magnitude off) |

The naive identity fails by ~1836× — exactly the m_p/m_e ratio,
which IS the quantity the framework is trying to derive.
Consistent with the 2026-05-11 brief's PR #487 agent finding #6:
"the Vol-based mass formula's `λ_scale` may NOT have a substrate
derivation independent of the bridging map to the τ_M
formalism." The Markov-trace formalism produces `O(1)` numbers
(binding-energy decomposition, cheat-sheet step 9); the Vol-form
produces `O(1836)` numbers (absolute rest mass). They do not
coincide on β_Bor.

**Implication.** The bridging factor between Markov-trace and
Vol-form formalisms IS what `λ_scale` measures structurally —
the naive identity is the wrong shape. Strategy F is closed.

### Strategy G — Skein-family polynomial direct evaluation at q_0

The Borromean Jones, Kauffman bracket, and HOMFLYPT polynomials
all have closed forms (Murasugi, Lickorish-Millett). Evaluate
each at standard substrate substitutions and check whether any
single polynomial value, or natural ratio/root thereof, equals
λ_p. No PSLQ — these are categorical invariants with known
closed forms; the test is just whether one matches.

**Compute kernel.** `lambda_scale_alt_g_skein_polynomial_direct.py`
(this brief). Standard Skein-family polynomial evaluators in
`mpmath`. Single 5-min compute.

**Result (2026-05-22, witness
`lambda-scale-alt-g-skein-polynomial-direct.witness.json`):**
**WEAK SIGNAL** — best match is `5/2 − ℏ_q² · ⟨𝓑_3⟩(q_0^{1/2})`
at +165 ppm, but all direct Jones / HOMFLYPT evaluations are off
by 18–630 % from λ_p.

  | candidate | value at q_0 | |rel diff| |
  |---|---:|---:|
  | V(𝓑_3, q_0) | 4.0105 | 63 % |
  | V(𝓑_3, q_0²) | 4.0379 | 64 % |
  | √V(𝓑_3, q_0²) | 2.0094 | 18 % |
  | V(𝓑_3, q_0)^{1/3} | 1.5888 | 35 % |
  | P_HOMFLYPT(𝓑_3, q_0^−1, q_0−q_0^−1) | 14.397 | 485 % |
  | **5/2 − ℏ_q² · ⟨𝓑_3⟩(q_0^{1/2})** | **2.4604** | **165 ppm** |

Note the best-match form `5/2 − ℏ_q² · ⟨𝓑_3⟩(q_0^{1/2})`
parallels the earlier `5/2 − h² · G` PSLQ coincidence
(2026-05-18 audit) but is **structurally different**: `ℏ_q² ≠
h²` (they differ by `(q − q⁻¹)² vs ((q − 1)/q)²`), and `⟨𝓑_3⟩`
is the Kauffman bracket vs `G` Catalan. Both share the
"5/2 − topological·O(h²)" template but resolve different
substructure. The 165 ppm gap is the same magnitude as the
known PSLQ-fit coincidence: neither form is the categorical
λ_scale, but both reveal the **template** `5/2 − topological-h²-term`.

**Implication.** Strategy G is closed for the single-polynomial
identity. The next refinement is **Strategy H** below: scan
alternative Wedderburn linear functionals for the substrate
form, since 5/2 is robustly the leading coefficient.

### Strategy H — Wedderburn linear-functional scan (Family A variants)

The "Family A" theorem proves that
`λ_A(q) := (1/4) · Σ_{λ ⊢ 4} dim_q V_λ = 5/2 + (3/4)·h²` exactly
([`lambda_scale_all_c_i_family_a.py`](../../folio-assistant/computations/lambda_scale_all_c_i_family_a.py)).
This is the algebraically correct closed form of the linear
functional `(1/4) Σ dim_q` on H_4, but the identification
`λ_scale = λ_A` is **falsified**: at q_0, λ_A = 2.5328 vs target
λ_p = 2.4600, off by **+2.96 %** with **wrong sign on h²**
(c_2 = +3/4 vs target ≈ −G).

The probe `probe_family_a_variants.py` already scans seven other
natural linear functionals V_2 — V_8 on the H_4 character table:

  | variant | h² coeff | at q_0 | rel vs target |
  |---|---:|---:|---|
  | V_1 = (1/4) Σ dim_q V_λ (Family A) | +3/4 | 2.5328 | +2.89 % |
  | V_2 = (1/(48·5)) Σ dim_q² V_λ (Plancherel) | +5/3 | 2.5734 | +4.54 % |
  | V_3 = (1/(48·5)) Σ dim_q · dim_cl | +5/6 | 2.5364 | +3.04 % |
  | V_4 = (1/48) Σ hook_cl · dim_q | +7/12 | 2.5255 | +2.59 % |
  | V_6 = (1/(4·5)) · dim_q V_(2,2) only | +5/4 | 2.5546 | +3.78 % |
  | **V_7 = Σ dim_q V_λ / [4]_q** | **−13/16** | **2.4652** | **+0.144 %** |
  | V_8 = harmonic of dim_q V_λ | +85/361 | 1.5891 | −35.4 % |

**V_7 is the structural signal.** Among the eight natural
Wedderburn linear functionals on H_4, **only V_7 has the right
sign on h²**, with magnitude `|c_2| = 13/16 ≈ 0.8125` —
order-of-magnitude correct vs the target `−G ≈ −0.916`. The
value at q_0 lands within **+0.144 %** (1440 ppm) of λ_p.

**Why V_7 is structurally natural.** Σ dim_q V_λ is the sum of
all irreducible Hecke characters at the identity (the regular
trace); dividing by `[4]_q` is the **q-deformed Plancherel
normalisation** that makes the functional dimensionally correct.
At q = 1, `[4]_q → 4` reproduces 5/2 = (1+3+2+3+1)/4. The
negative h² coefficient is a categorical-derivation artifact:
the q-correction of the denominator `[4]_q = q³ + q + q⁻¹ + q⁻³
≈ 4 + 4h² + ...` over-cancels the numerator's leading 3/4·h²,
producing a NET negative h² for the quotient.

**Next step.** Try the refined Wedderburn family `V_7^{(k)} = (Σ
dim_q V_λ + correction(k)) / [4]_q` for small categorical
corrections (e.g. subtract a single
dim_q V_(2,2) contribution; add a half-symmetric projector
factor). The target c_2 = −0.916 is 13 % below V_7's −0.8125;
a single sub-leading character contribution can plausibly close
the gap.

**Status.** WEAK-POSITIVE — V_7 is the first Wedderburn linear
functional with the right sign and right order-of-magnitude on
c_2; identifies the **family of candidate substrate forms**.

**Anti-pattern to avoid (per
[`CLAUDE.md §Δ_λ gate`](../../CLAUDE.md)):** do not fit a
seven-parameter `α · V_7 + β · V_8 + γ · ...` ansatz against
m_p. Find the categorical justification for the specific
correction term first, then verify the numerical match.

### Strategy J — HOMFLYPT cross-orientation closure

The Borromean rings is a **3-component link**, so its HOMFLYPT
polynomial admits orientation refinements per component. For the
proton-vs-neutron quark partition `(2,1)` vs `(1,2)`, evaluate

  `P(𝓑_3; (2,1)) (a = q_0^{-1}, z = q_0 − q_0^{-1})`
  `P(𝓑_3; (1,2)) (a = q_0^{-1}, z = q_0 − q_0^{-1})`

and check whether the ratio matches the empirical `m_p / m_n`
ratio at q_0. If yes, the Skein orientation correction `S(p) /
S(n)` is **structurally pinned**, leaving `λ_scale` as a
single-unknown observable — over-determinable from a 2-equation
system instead of a 1-equation fit.

This was **Lead #1 from the PR #487 agent** in the 2026-05-11
brief; never executed. Existing infra:
[`skein_proton_canonical.py`](../../folio-assistant/computations/skein_proton_canonical.py)
computes the Kauffman bracket for the canonical proton braid,
but does not yet emit a per-orientation HOMFLYPT.

**Compute kernel (to write).** Extend
`lambda_scale_alt_g_skein_polynomial_direct.py` to use
orientation-dependent multi-variable HOMFLYPT (or use SnapPy /
SnapPyHP for explicit closed-form polynomial). ~1 day.

**Estimated cost.** 1 day if HOMFLYPT closed form is available;
2-3 days if it requires symbolic Skein-reduction from scratch.

**Status.** Deferred (out of this tranche's scope).

### Strategy I — Yekutieli holonomy with per-cell curvature

Categorical derivation of `Σ_geom(q)` such that
`λ_scale = π_alg(q) − Σ_geom(q)`, where `π_alg` is Family A
(`5/2 + (3/4)h²`) and `Σ_geom` is the per-cell hyperbolic
curvature 2-form integrated over the Borromean ribbon surface
via Yekutieli non-abelian Stokes (cheat-sheet step 2).

Already partially explored in
[`lambda_scale_rd1_geometric.py`](../../folio-assistant/computations/lambda_scale_rd1_geometric.py)
with the ansatz `Σ_geom = (3/4 + G)·h²`. The categorical
derivation of the `(3/4 + G)` coefficient is the gap. If
Yekutieli integration is computed structurally (not fit), it
should produce the empirical match WITHOUT introducing a 4th
calibration constant.

**Compute kernel.** New script under
`folio-assistant/computations/lambda_scale_alt_i_yekutieli_curvature.py`
that integrates the per-cell curvature 2-form on `𝓑_3`'s 8
ideal octahedral cells. Each cell contributes
`Λ(π/4) = G/2`; the total of 8 cells gives `8 · G/2 = 4G`
naturally — needs to be related to the empirical `3/4 + G`
coefficient.

**Estimated cost.** 2-3 days (deriving the 2-form is the work,
not the integration).

**Status.** Deferred; Strategy H's V_7 finding may obsolete this
direction.

### Strategy K — Bloch class via explicit triangulation

INVERT the failed 6-tier Bring-Bloch PSLQ search. The 52-knot
search ruled out `[Z_p] = Σ_i n_i [Z_K_i]` as a ℤ-linear
combination of prime hyperbolic-knot Bloch classes ≤ 11
crossings. But the **decomposition basis** was the wrong
formalism; the Bloch class itself can be constructed directly.

Procedure:
1. Take the canonical 11-crossing proton braid
   ([`canonical_braid_marshalling.py`](../../folio-assistant/computations/canonical_braid_marshalling.py),
   `atomic-braid-recipe-p`).
2. Compute its braid closure as a knot or link in S³.
3. Triangulate that closure via SnapPy.
4. Extract ideal-tetrahedron z-parameters.
5. Compute `D([Z_K_p]) = Σ_i D(z_i)` where `D` is the
   Bloch-Wigner dilogarithm.
6. Check if `λ_scale = (1/8G) · D([Z_K_p])`.

This is the categorical identity from
[`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md)
with the **integer multi-set** replaced by the **explicit
triangulation**. The 6-tier negative ruled out the existence of
the multi-set decomposition; it did NOT rule out the underlying
Bloch class.

**Compute kernel.** New SnapPy-bridge script.

**Estimated cost.** 2-3 days; needs SnapPy (separate Python env;
may not work in the production mpmath environment).

**Status.** Deferred; highest theoretical payoff if it lands,
but also the largest implementation lift.

### Strategy M — Cross-isotope over-determination

The common-scale conjecture asserts ONE `λ_scale` applies to
EVERY Borromean baryon (proton, neutron, and any Σ, Λ, Δ
extension). Use the mass table as additional constraints: a
candidate λ_scale that matches proton might still fail on the
2nd or 3rd Borromean baryon.

Procedure:
1. For each known Borromean baryon `B_i` with mass `m_{B_i}`
   from CODATA/AME and orientation partition `(p_i, n_i)`,
   compute its empirical λ_scale closure target.
2. A correct substrate parametrisation gives a single λ_scale;
   if the closure targets disagree by more than the Skein-
   contribution refinement, the conjecture is **falsified** at
   the second observable.
3. Use this to filter candidates from Strategies A/B/C/G/H.

**Compute kernel.** Extend
[`lambda_scale_proof_step5_skein_anchor.py`](../../folio-assistant/computations/lambda_scale_proof_step5_skein_anchor.py)
to emit per-baryon closure targets.

**Estimated cost.** 1 day, once Strategies F-H produce
candidates worth filtering.

**Status.** Verification scaffold; runs against any candidate
from F/G/H/I/K.

### Recommended ordering (revised after 2026-05-22 results)

  1. **Strategy H finding** — V_7 = Σ dim_q V_λ / [4]_q is the
     first Wedderburn functional with the right sign on h².
     Pursue refined V_7 family (categorical correction terms)
     **first**, since the substrate justification of a
     small-correction Wedderburn functional is the most
     theoretically defensible path.
  2. **Strategy I (Yekutieli curvature)** — derive the
     `Σ_geom = (3/4 + G)·h²` coefficient categorically. If V_7
     refinement (H) doesn't yield exact match, the residual is
     where Yekutieli enters.
  3. **Strategy A / B (Rogers / Faddeev PSLQ)** — the original
     brief's primary direction; viable but more
     fit-prone. Run only after H/I to constrain the basis.
  4. **Strategy J (HOMFLYPT cross-orientation)** — secondary
     verification of the Skein term; pins S(p)/S(n) ratio.
  5. **Strategy K (Bloch class explicit construction)** — if
     all categorical approaches fail, fall back to the
     SnapPy-triangulation route.
  6. **Strategy D (LP/SDP on 𝓑_p)** — only if 1-5 all fail.
     The LP/SDP infrastructure lift is large and the alternative
     non-PSLQ approaches (F-H above) are cheaper to refute.

### Strategies closed by 2026-05-22 first-pass

  - **Strategy F (Markov-trace identity on β_Bor).** FALSIFIED;
    candidate value 0.00134 vs target 2.46 (3 orders of
    magnitude off). The naive identity is the wrong shape; the
    bridging factor between Markov-trace and Vol-form
    formalisms IS λ_scale, so an identity between them is
    structurally impossible.
  - **Strategy G (single-polynomial Skein identity).** No
    direct Jones / Kauffman / HOMFLYPT value at q_0 equals λ_p.
    The best ratio-form `5/2 − ℏ_q² · ⟨𝓑_3⟩(q_0^{1/2})` at
    +165 ppm reveals the same `5/2 − topological-h²` template
    as the earlier PSLQ-coincidence form, but is itself another
    coincidence (different structural ingredient with similar
    magnitude). Closed for the single-polynomial form; the
    multi-polynomial linear combinations still allow A/B/J.

## Verification criteria

A candidate parametrisation is acceptable iff it satisfies ALL:

1. **Numerical agreement** with the target at 50 dps:
   `|λ_scale^candidate − 2.4599527869...|/λ_scale < 1e-15`.
2. **Type discipline** — uses only `m_e, q_0, Vol(𝓑₃)` and rational
   numbers; no other calibration constants.
3. **q_0-locality** — the parametrisation must be well-defined as a
   function of q (not just a numerical accident at q_0). Verify by
   evaluating at q' = q_0 + ε for small ε and confirming smoothness
   + analytic continuation.
4. **Universe-level closure** — passes the
   `Σ_p D([Z]^(p)) = 2/(3π)` check (Task #2 in
   `prop:lambda-scale-bring-bloch-identity`).
5. **Falsifiability** — predicts a non-trivial `λ_scale` at a
   different substrate point (e.g., the C2-inflection point where
   `q = (1+√5)/2`-like algebraic neighbour), and that prediction
   agrees with the parallel computation done via Bring-Bloch's
   universal-volume integral.

Conditions 1+2+3 are mandatory; 4+5 are strong cross-checks that
distinguish a structural identity from a numerical coincidence.

## Anti-patterns (do NOT do)

1. **Do not introduce new calibration constants.** A 7th-ansatz fit
   for `λ_scale` against m_p is the same CAL-4 violation as the
   hardcoded literal. The strict 3-calibration rule is enforced
   per CLAUDE.md `Δ_λ gate`. Six closure ansätze have already
   failed on the deuteron, and a seventh fit-based attempt will be
   caught by the canonical-watcher.
2. **Do not lower precision.** PSLQ at < 50 dps will produce false
   positives. Use mpmath `mp.dps = 100` for the PSLQ runs and
   verify the candidate at `mp.dps = 200`.
3. **Do not silently switch q_0 conventions.** The substrate value
   is `Q_50_DIGIT_STR =
   "1.10997859555418057528159407960950937799328227995870"` in
   [`folio-assistant/computations/q_parameter.py`](../../folio-assistant/computations/q_parameter.py).
   Any candidate must be evaluated at exactly this q_0.

## Deliverables (when this work is done)

1. **Witness JSON** —
   `folio-assistant/computations/lambda-scale-qdilog-direct.witness.json`
   with the candidate expression, the numerical agreement at 50 dps,
   the q_0-locality check, and the universe-closure verification.
2. **Production wire-up** — replace `LAMBDA_PROTON_DOC` literal in
   `m_p_borromean_verification_50dps.py:100` with a call to the new
   derived expression. Same for `LAMBDA_NEUTRON_DOC` at line 101.
3. **Audit doc** — `docs/audits/2026-05-DD-lambda-scale-qdilog-direct.md`
   documenting which strategy (A–E) succeeded, what was tried and
   rejected, and the verification chain.
4. **Migration Backlog #1 closure** — update
   [`docs/canonical-derivation-cheat-sheet.md §5`](../canonical-derivation-cheat-sheet.md)
   to remove the backlog item.
5. **Paper-side block update** — promote
   `prop:lambda-scale-bring-bloch-identity` either to a closed
   theorem (if Strategy A/B/C/D yields a proof) or to a falsified
   conjecture with the q-dilog-tower derivation as the canonical
   replacement.

## Cross-references

- [`conj:borromean-baryon-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-mass-formula.md)
  — the formula that uses `λ_scale`.
- [`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md)
  — the now-incomplete Bring-Bloch hypothesis.
- [`prop:li2q-phiq-bar-symmetrization`](../../content/quantum-observable-universe/braids-and-knots/li2q-phiq-bar-symmetrization.md)
  — the Φ_q ↔ Li_2^q bar-symmetry identity.
- [`docs/audits/2026-05-18-210x-scale-gap-root-cause-v2.md`](../audits/2026-05-18-210x-scale-gap-root-cause-v2.md)
  — diagnostic identifying `λ_scale` as the CAL-4 problem.
- [`docs/audits/2026-05-20-compute-wiring-audit-pr-852.md`](../audits/2026-05-20-compute-wiring-audit-pr-852.md)
  §7 — open frontier #4 (this work).
- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
  §4 (Φ_q vs Li_2^q) and §5 #1 (Migration Backlog).
- [`folio-assistant/computations/q_parameter.py`](../../folio-assistant/computations/q_parameter.py)
  — substrate q_0 canonical pin.
- [`folio-assistant/computations/bring_bloch_tier{1..5}_search_m_p.py`](../../folio-assistant/computations/)
  — the exhausted Bring-Bloch path; use as PSLQ scaffolding template.
- [`folio-assistant/computations/lp_dual_solver.py`](../../folio-assistant/computations/lp_dual_solver.py)
  — LP/SDP infrastructure for Strategy D.

## Why this work matters

Closing CAL-4 in `λ_scale` is the **only** known path to
first-principles m_p, m_n, m_He absolute predictions in the QOU
framework. Without it, the production mass pipeline retains an
empirically-calibrated literal that the cheat sheet itself flags as
a 3-calibration discipline violation. The Bring-Bloch path is
exhausted; q-dilog-tower-direct is the next-best lead.

If successful, this resolves the headline "L2 100×" obstacle for
m_p, m_n absolute (currently at CAL-2 floor ~780 ppb; the
substrate-only derivation would push toward arbitrary 50-dps
precision). It also closes Migration Backlog #1.
