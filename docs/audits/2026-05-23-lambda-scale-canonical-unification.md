# λ_scale canonical unification: Yekutieli + Bring color-tube + where h^k corrections come from

**Date:** 2026-05-23
**Branch:** `claude/lambda-scale-alts-strategy-d-2026-05-22`
**Status:** Structural articulation; no proof.

## User questions (verbatim)

> "how canonical includes Yekutieli and Brings together? canonical h^4 or
> other terms? where are they coming from? some ODE/PDE on Φ_q or Dilog?"

This audit answers structurally. The canonical-only landscape (per
user 2026-05-23 "no empirical fitting, canonical only") has THREE
independent substrate-natural mechanisms, all living on Bring's
surface (genus 4, S_5 symmetry, χ = −6). Their relationship is
NOT additive in the naive sense — it's a hierarchy of categorical
integrations on the same underlying surface.

## How canonical includes Yekutieli + Bring together

The Borromean rings `𝓑_3` are **embedded** in Bring's surface (per
[`prop:bring-z5-descent`](../../content/quantum-observable-universe/braids-and-knots/bring-z5-descent.md)).
So all three mechanisms below live on the SAME categorical object:

1. **Canonical Wedderburn (leading-order substrate, q=1 limit).**
   The Markov trace `tr_M` at q=1 evaluates the half-symmetric H_4
   Wedderburn count to `5/2` (5 = # partitions of 4; half-symmetric
   averaging gives 5/2). This is the **classical projection** of the
   q-deformed Markov trace.

2. **Yekutieli categorical Stokes (q-deformation corrections).**
   The q-deformation curvature 2-form `F = dA + A ∧ A` integrated
   over the surface gives the per-cell hyperbolic-volume contribution.
   For 𝓑_3's 8 ideal octahedra, per-cell `−G`. At h² order this gives
   `−G · h²`. At higher orders (h^4, h^6, ...) the SAME per-cell
   tessellation argument extends, but the explicit categorical
   derivation of the higher-order coefficients is the **audit Step 4
   R&D open item**.

3. **Bring color-tube weighted averaging (color-sheet structure).**
   Bring's surface admits 5-fold S_5 symmetry → 3-strand color
   tubes per nucleon (3 quarks × 3 colors). The p-n boundary
   averages over 9 color-pair assignments + diagonal direction = 10
   (per cheat-sheet §"Bring color-tube weighted averaging" — Phase
   5q open audit finding). The form `1/(1 − h_q · q_0^{10})`
   (commit `d348ad8c`) is the Faddeev Φ_q-pentagon resummation
   with this 10-fold color-tube structure embedded as `q^{10}`.

## Unifying picture: Φ_q-resummed Yekutieli on Bring's surface

The canonical full λ_scale should be a **single Yekutieli
categorical-Stokes integral over Bring's surface**, evaluated at
q_0:

```
λ_scale^canonical  =  (Markov trace at identity)  +  (Yekutieli integral over Bring's surface, q-deformed)
                   =  5/2                          +  (Φ_q-resummed curvature contribution)
```

The Φ_q-resummed integral is THE all-orders categorical Stokes for
the Bring-surface bundle. Truncated at first order in h, it gives
`−G · h²` (per-cell octahedral volume on the Borromean sub-surface).
Truncated at the Φ_q functional-equation level with the 10-fold
color-tube structure, it gives `1/(1 − h_q · q_0^{10})` (commit
`d348ad8c`).

**Open question:** are the additive form `5/2 + (3/4 − G)·h²`
(canonical h² + Yekutieli h² additive) and the resummed form
`5/2 + (1/(1 − h_q·q_0^{10}) − 1)` (canonical leading + Bring
color-tube subtracted of its own leading 1) **the same categorical
object** truncated at different orders, or are they **independent
mechanisms**?

This is the load-bearing question. Two structurally-distinct answers:

- **They are the same.** Then `1/(1 − h_q · q_0^{10})` is the
  resummed Yekutieli categorical Stokes, and its h² coefficient
  agrees with `+3/4 + (−G)` (canonical + Yekutieli additive) at
  leading order. **Check this numerically** (see "Concrete test"
  below) — if the leading-order h² coefficient of `1/(1−h_q·q_0^{10})`
  matches `+3/4 − G`, this is strong evidence they are the same
  mechanism.

- **They are independent.** Then the full canonical prediction is
  the additive composition: `5/2 + (canonical h²) + (Yekutieli h²) +
  (Bring color-tube all-orders − 5/2 − all already-counted h² terms)`
  — i.e. we need to **subtract** the canonical and Yekutieli
  contributions from the Bring color-tube resummation to avoid
  double-counting.

## Where h^4 and higher corrections come from

The user asks: "some ODE/PDE on Φ_q or Dilog?" — **yes, exactly**.

The Faddeev quantum dilogarithm Φ_q satisfies the FUNCTIONAL
DIFFERENCE EQUATION:

```
Φ_q(q · z)  =  (1 / (1 − z)) · Φ_q(z)            (Faddeev recursion)
```

This is a **first-order multiplicative recursion** under q-scaling
of the argument. The Bring color-tube form is the direct
finite-difference at the n=10 power:

```
1 / (1 − h_q · q_0^{10})  =  Φ_q(h_q · q_0^{11}) / Φ_q(h_q · q_0^{10})
```

**Higher-order h^k corrections** come from THREE distinct sources,
all categorical:

### (i) Higher iterations of the Faddeev recursion

Applying the functional equation k times:

```
Φ_q(q^k · z) / Φ_q(z)  =  ∏_{j=0}^{k-1} 1 / (1 − q^j · z)
```

At k=10 (the Bring color-tube count): a product of 10 finite-difference
factors. The h^4 coefficient of this product is **algebraically
derivable** from the Faddeev recursion without empirical fitting.

### (ii) Φ_q power-series expansion

Faddeev's explicit formula:

```
Φ_q(z)  =  ∏_{n=0}^{∞} (1 − q^{2n+1} · z)^{-1}
log Φ_q(z)  =  Σ_{n=1}^{∞}  z^n / (n · (1 − q^{2n}))
```

The denominators `(1 − q^{2n})` introduce h-dependent factors;
expanding `log Φ_q` at small z gives a power series whose
coefficients are functions of q. At z = h_q · q_0^{10}, these are
NOT small at q_0 (h·q_0^{10} ≈ 0.59), so the series doesn't
converge cheaply — the resummed `1/(1−z)` form is the right
object. But the h^4-equivalent CORRECTIONS to the leading
resummation come from the higher Bernoulli-like factors in the
log expansion.

### (iii) Rogers Li_2^q pentagon identity (5-term functional equation)

The Rogers quantum dilogarithm Li_2^q satisfies the pentagon
identity:

```
Li_2^q(x) + Li_2^q(y)  =  Li_2^q(x + y − x·y) + Li_2^q(x · (1 − y)/(1 − x · y)) + Li_2^q(y · (1 − x)/(1 − x · y))
```

This 5-term consistency constrains the higher-order corrections to
λ_scale beyond what the Faddeev recursion (i) gives. If Yekutieli
categorical Stokes can be re-expressed via Li_2^q (rather than Φ_q),
the pentagon gives ADDITIONAL constraints that pin h^4 corrections.

**These three sources are not independent** — Faddeev and Rogers
are bar-conjugate q-dilogarithms (per `prop:li2q-phiq-bar-symmetrization`
on main); their h^k corrections must agree under bar-symmetrization.

### (iv) Yang-Baxter equation (braid-group relations)

The R-matrix satisfies the Yang-Baxter equation:

```
R_{12} · R_{13} · R_{23}  =  R_{23} · R_{13} · R_{12}
```

This is a CUBIC consistency on the braiding morphism. Its
h-expansion at the universal level (`R = 1 + h · r + h² · r⁽²⁾ + ...`)
yields the classical Yang-Baxter equation for the classical r-matrix
at leading order, and ITERATED Yang-Baxter constraints at higher
h^k orders. These constrain how the Hecke quadratic
`σ_i² = (q − q⁻¹)·σ_i + 1` propagates through h-expansion — and
hence constrain higher-order Yekutieli per-cell coefficients.

### (v) Hexagon equations (braiding ↔ fusion compatibility)

In a braided monoidal category, the hexagon equations relate
braiding to fusion (tensor product) at next-to-leading order. For
Rep(U_q(sl_2)) restricted to the H_4 sector, the hexagon equations
give explicit polynomial relations between h^k coefficients of
braided morphisms and fusion coefficients. These constrain how
canonical Wedderburn (which is fusion-based) and Yekutieli
categorical Stokes (which is braiding/curvature-based) MUST agree
at every h^k order.

### (vi) Frobenius reciprocity / pairing constraints

The Frobenius pairing `⟨a, b⟩_F = ∫_A (a · b)` is non-degenerate on
the half-symmetric H_4 sub-algebra. Frobenius reciprocity gives a
duality between h^k coefficients of the Markov trace and h^k
coefficients of the dual Frobenius form. This is a categorical
consistency that forces specific relations between Yekutieli and
canonical Wedderburn h^k contributions at every order — no
independent choice.

### (vii) Quantum 6j-symbol identities (Racah-Wigner)

For Rep(U_q(sl_2)) the quantum 6j-symbols satisfy explicit
recursions (Biedenharn-Elliott and orthogonality). At the H_4
partition level these give CLOSED FORMS for how partition-character
products decompose, with explicit h^k expansions. The h^4
coefficient of any natural Hecke-character functional on H_4 is
ALGEBRAICALLY DERIVABLE from the 6j data — not a fit.

### (viii) Modular dual / S-transformation

For modular tensor categories (Reshetikhin-Turaev TQFT), the
S-transformation `q ↔ q̃ = exp(2πi · 1/τ)` is a categorical
symmetry. For real q > 1 (our substrate), the dual q̃ is a small
COMPLEX root of unity; the q ↔ q̃ symmetry constrains the
asymptotic behavior of Φ_q and Li_2^q at large h. h^k corrections
that VIOLATE this symmetry are non-categorical.

### (ix) KLR positivity (Khovanov-Lauda-Rouquier)

KLR canonical bases for U_q(sl_n) have non-negative integer
coefficients. Per user direction "KLR only non-negative observables"
(2026-05-23), h^k coefficients of OBSERVABLES (vs corrections like
Yekutieli's `−G`) must be expressible as non-negative integer
combinations of KLR basis elements. This is a STRONG categorical
constraint: it filters which h^k corrections can be λ_scale
contributions vs subleading corrections to the categorical action.

### (x) MacMahon-style partition-algebra identities

For the partition algebra at H_4 (5 partitions of 4), MacMahon's
master theorem and related symmetric-function identities give
explicit h-expansions of dim_q V_λ and Σ_λ dim_q V_λ. These are
the source of canonical Wedderburn's `+3/4` h² coefficient (Family
A theorem). Higher-order h^k contributions to other partition-
algebra weighted sums are similarly derivable — the audit Step 4
"h^4 coefficient should be derivable from the partition algebra
at level n=4" cites exactly this.

### (xi) Lobachevsky / Catalan-G identities

`Vol(𝓑_3) = 8G` via the Adams 1985 octahedron decomposition is the
source of the per-cell `G = Vol(𝓑_3)/8` constant entering
Yekutieli. The Lobachevsky function `Λ(π/4) = G/2` and related
Cl_2 (Clausen) identities tie G to other transcendentals; if h^4
or higher coefficients involve G²/2, G·ζ(3), or Cl_2(π/3) factors,
these traceable transcendental identities pin them.

### (xii) Chern-Simons perturbative expansion (Ohtsuki series)

For Witten-Reshetikhin-Turaev TQFT at level k → ∞ with q =
exp(2πi/(k+2)), the Chern-Simons partition function admits a
perturbative expansion (Ohtsuki series) in 1/k = log(q)/2π. h^k
corrections to the Borromean WRT invariant at substrate q_0 are
derivable from this asymptotic series — yet another canonical
source of higher-order coefficients.

### (xiii) Crystal-graph / Kashiwara q → 0 limit

Per CLAUDE.md §7b, KLR canonical bases at q → 0 reduce to crystal
graphs (Kashiwara). The crystal structure is fully combinatorial
(no q dependence), and the q-deformation back from q → 0 to
q = q_0 gives explicit h^k expansions of crystal-basis matrix
elements. Higher-order corrections to half-symmetric H_4 sums are
derivable from the crystal graph's structure constants.

### Summary: the categorical-drivers menu

Every h^k coefficient in `λ_scale^canonical` should come from ONE
or MORE of these thirteen sources. Choosing a coefficient that
ISN'T derivable from any is the empirical-fitting antipattern the
user's "no empirical fitting" rule excludes. The framework's
canonical-only refinement direction is to take each load-bearing
open step (cell-↔-projection bijection, color-sheet ↔ flavor
mapping, second-order Yekutieli per-cell h^4) and identify which
of the thirteen sources gives its categorical derivation.

### Rule 14 — Author-escalation for off-menu coefficients (exploratory vs production)

Per user direction 2026-05-23: **if a candidate h^k coefficient
cannot be derived from any of the 13 categorical drivers above,
the agent MUST escalate to the author/owner explicitly via
`AskUserQuestion` (or equivalent surfaced query) BEFORE adopting
it in production. Empirical-fit candidates may be used for
EXPLORATORY shape-probing without escalation, but never for
production.**

**Exploratory shape-probing is permitted.** Per user clarification
2026-05-23: "suggestions of empirical fits are OK for exploratory
— what is the shape type of questions. but never for PROD pipeline".
An exploratory probe that surfaces an empirical-fit coefficient is
useful when it generates a STRUCTURAL HYPOTHESIS the author or
future agent can then attempt to derive categorically. The shape
hint is the value; the empirical fit is the scaffold.

**Production pipeline is the strict line.** No empirical-fit
coefficient may enter:
- `m_p_borromean_verification_50dps.py` (or any production mass-
  chain script)
- `LAMBDA_PROTON_*` / `LAMBDA_NEUTRON_*` / equivalent named
  constants
- The cheat-sheet §5 Migration Backlog "closed" status
- The framework's per-observable 100× dashboard

Without first either:
1. Identifying a 14th categorical driver this audit missed (which
   would extend the audit), OR
2. Owner authorisation of the conjecture-conditional adoption
   (analogous to PR #895's canonical Wedderburn move).

The escalation should include:
- The exact coefficient value (numerical, MPFR-50dps).
- The candidate categorical mechanism (if any partial hint exists).
- The structural meaning the agent has tried to assign (and why
  it failed to land in one of the 13 sources).
- A short statement of what closure of this open coefficient would
  unlock (1.4 % gap to ppm? Phase 5q? Bring-Bloch?).

The author may then either:
- Identify a 14th categorical driver the agent missed
  (in which case this audit is extended).
- Confirm the coefficient is genuinely outside the canonical
  menu, and decide whether to accept it as a conjecture-conditional
  refinement WITH explicit owner authorisation (analogous to PR
  #895's adoption of canonical Wedderburn as production with
  conjecture-conditional dependency).
- Direct the agent to wait until the underlying categorical
  derivation lands.

This rule supplements the existing CLAUDE.md three-calibration
discipline (no CAL-4 fits) and the `Δ_λ gate` anti-pattern. It
makes the escalation step explicit and traceable: every h^k
coefficient in the framework is either (a) derivable from a named
categorical driver, or (b) explicitly owner-authorised under
conjecture-conditional status.

This is the structural protection against the "seventh ansatz"
problem (per `docs/audits/2026-05-18-delta-lambda-gating-context.md`):
without rule 14, an agent could keep probing higher-order fits
indefinitely; with it, the search space is bounded by the 13-source
categorical menu, and excursions outside the menu require explicit
author input.

## Concrete test (canonical, fitting-free)

**Numerically check** whether the h² coefficient of `1/(1 − h_q · q_0^{10})`
in its small-h expansion AT q_0 matches `+3/4 − G` (the additive
canonical + Yekutieli h² coefficient).

If they match: the Bring color-tube IS the resummed Yekutieli
categorical Stokes, and the framework's canonical λ_scale is
`1/(1 − h_q · q_0^{10})` at all orders. No double-counting.

If they don't match: the two mechanisms are independent, and the
full canonical λ_scale needs explicit subtraction to avoid
double-counting:

```
λ_scale^canonical  =  canonical Wedderburn  +  Yekutieli additive  +  (Bring all-orders − resummed h² contribution)
                   =  5/2 + (3/4 − G)·h²    +  (1/(1−h_q·q_0^{10}) − leading h² extraction)
```

This is a **canonical numerical check**, not a fit — it tests
whether two independently-defined categorical objects produce the
same h² coefficient at q_0.

## No empirical h^4 coefficient

Per user direction 2026-05-23 "no empirical fitting, canonical
only", the h^4 (and higher) coefficients must come from one of (i),
(ii), (iii) above — **derived algebraically from the Faddeev
recursion / Φ_q power series / Rogers pentagon**, NOT fit to close
the CODATA residual.

The h^4 refinement probe
[`lambda_scale_refinement_h4_correction_bring.py`](../../computations/lambda_scale_refinement_h4_correction_bring.py)
was retired in commit `38afcf12` because its α = (3/4 + 1 − G)
empirically fits to the CODATA m_p residual; the "+1" leading h^4
coefficient has no canonical derivation.

## Open R&D directions (canonical, no fits)

1. **Test whether `1/(1 − h_q · q_0^{10})` h² coefficient matches
   canonical+Yekutieli `+3/4 − G`.** Concrete numerical check at
   q_0 ± ε; canonical (no fitting).
2. **Derive the h^4 coefficient of `1/(1 − h_q · q_0^{10})`
   structurally** via the Faddeev recursion / Φ_q power series. If
   it matches a partition-algebra contribution at H_4 (audit Step 4),
   the second-order Yekutieli per-cell is closed canonically.
3. **Verify the Φ_q ↔ Li_2^q bar-symmetrization** at h^4 order on
   Bring's surface — does the Rogers pentagon give the same h^4
   coefficient as the Faddeev recursion?
4. **Categorical bijection step** (audit Step 3 R&D item 1): the
   cell-↔-half-sym-projection at H_4. With this proof, the h²
   coefficient `−G` from Yekutieli is canonical (not just
   structural argument).

## Witness / probe

- [`lambda_scale_refinements_composed_predictions.py`](../../computations/lambda_scale_refinements_composed_predictions.py)
  — composes the three canonical-only options with the proved
  flavor-split from PR #942.
- [`lambda_scale_refinement_h4_correction_bring.py`](../../computations/lambda_scale_refinement_h4_correction_bring.py)
  — RETIRED (empirical fitting); preserved as documented dead-end.

## Cross-references

- [`docs/audits/2026-05-18-conjecture-proof-step3-yekutieli.md`](2026-05-18-conjecture-proof-step3-yekutieli.md)
  — original Yekutieli structural argument
- [`docs/audits/2026-05-22-faddeev-pentagon-operator-spike.md`](2026-05-22-faddeev-pentagon-operator-spike.md)
  — Bring color-tube `1/(1 − h_q · q_0^{10})` finding
- [`docs/audits/2026-05-22-yekutieli-percell-conjecture-formalized.md`](2026-05-22-yekutieli-percell-conjecture-formalized.md)
  — load-bearing categorical-bijection step
- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
  §"Bring color-tube weighted averaging" — Phase 5q open audit finding
- [`docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md`](../agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md)
  §Strategy I — current production-update options
- [`prop:li2q-phiq-bar-symmetrization`](../../content/quantum-observable-universe/braids-and-knots/li2q-phiq-bar-symmetrization.md)
  — Faddeev ↔ Rogers correspondence
