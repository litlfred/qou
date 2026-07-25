# A_ω from the resurgence vantage — the boundedness route to Φ_b rigidity (2026-07-25)

**PR:** #4207. **Branch:** `claude/aomega-resurgent-modular-2026-07-25`.
**Axis:** A_ω monodromy datum, Faddeev–Volkov uniqueness leg (route 2, beans
`qou-aanp` / `qou-2cvs`). **Continues:** #4155 (brick (c) + elliptic-freedom
obstruction, merged).

## Where the leg stood after #4155

#4155 proved:

- **brick (c)** — *same divisor ⇒ the normal-form ratio is entire*
  (`RatioEntire.entire_toMeromorphicNFOn_div_of_same_order`), and
- the **elliptic-freedom obstruction** — the `FaddeevPhi` class (three fields, all
  quasi-periodicity, **no growth condition**) underdetermines the divisor: a
  nonconstant elliptic factor `e` on the lattice `⟨ib, i/b⟩` gives `e·Φ`, another
  `FaddeevPhi` solution with a **different** divisor
  (`FaddeevPhiEllipticFreedom.faddeevPhi_mul_elliptic`).

So the leg closes only with a **class strengthening** that excludes the elliptic
factor. #4155 named two candidates: the `PhiBProd` **same divisor**, or a **growth
bound**.

## This PR — the growth-bound route (the resurgence-vantage one)

The resurgence / state-integral representation of `Φ_b` (Faddeev's quantum
dilogarithm; Écalle–Borel resurgent, `ecalle-borel-resurgence-vocabulary.md`) makes
it analytic with controlled growth in a fundamental strip. So the prefactor-cancelled
ratio of two genuine solutions is **bounded** on `ℂ`. And a nonconstant elliptic
℘-factor has **poles** — it is **unbounded**. Hence boundedness excludes the elliptic
freedom directly, with no divisor matching:

`QOU/QBeta/BoundedMeromorphicLiouville.lean` (sorry-free, `lean`-direct exit 0):

- `meromorphicOrderAt_nonneg_of_bounded` — `‖f‖ ≤ C ⇒ order ≥ 0` everywhere (a pole
  forces `f → ∞` via `tendsto_cobounded_of_meromorphicOrderAt_neg`, impossible under
  a uniform bound on the `NeBot` punctured neighbourhood);
- `entire_toMeromorphicNFOn_of_bounded` — bounded normal form ⇒ analytic everywhere ⇒
  entire (`MeromorphicNFAt.meromorphicOrderAt_nonneg_iff_analyticAt`).

`QOU/QBeta/FaddeevUniquenessBoundedCapstone.lean`
(`faddeevPhi_proportional_of_bounded_ratio`, exit 0) plugs this into
`FaddeevPhiUniquenessAssembly.faddeevPhi_proportional_of_ratio_entire`, giving a
**second, independent closure** of the leg.

| capstone | endowment | brick |
|---|---|---|
| `FaddeevUniquenessCapstone` (#4155) | same divisor (`PhiBProd`) | `RatioEntire.entire_toMeromorphicNFOn_div_of_same_order` |
| `FaddeevUniquenessBoundedCapstone` (this) | **state-integral strip boundedness** | `BoundedMeromorphicLiouville.entire_toMeromorphicNFOn_of_bounded` |

Both are **§3b-cond**: the endowment is a **named, non-axiomatised** hypothesis — a
growth statement that does *not* assume the conclusion (constancy is strictly
stronger than boundedness; bounded non-constant functions exist). No fit is wired;
`conj:algebraic-geometric-dilog-equivalence` stays open.

## What is genuinely still open (honest, corpus-checked)

The uniqueness leg proves A_ω carries **zero fitting freedom** (rigidity). It is
**not** the A_ω value itself. Per the corpus survey (grep of `content/`, `docs/`,
`.beans/`, 2026-07-25):

1. **The boundedness endowment for the concrete `Φ_b`** — that the ratio's normal
   form is bounded on `ℂ` — is a real analytic fact of the state integral, but is
   **not yet Lean-proved from a `Φ_b` construction**. It is the honest remaining
   input of this route, exactly as the same-divisor premise is for the divisor route.
   Neither is axiomatised.
2. **The A_ω *value* (odd face) is a separate, still-open capstone**: the geometric
   `Im 𝔙_q(q₀) = N_odd(q)` normalization
   (`docs/scope/2026-07-18-im-vq-to-nodd-normalization-capstone.md`), anchor-dependent,
   bar-odd, `O(10⁻⁸)`. It is **not** touched here.
3. **Already-settled facts this PR does NOT re-open** (corpus-grep discipline):
   - the `u=0` `4₁` Stokes constant is the **integer 3 = DT/BPS invariant**, and this
     is **bar-even**, *not* the trace-field discriminant `−3`
     (`docs/audits/2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`,
     scope-a refutation of the "Stokes = disc" reading);
   - `no_anchor_invariant_realizes_swing` (Lean-proved) — no anchor-invariant datum
     realizes the 2.44% cross-anchor swing, so the odd A_ω must be
     deformation-carried (`u ≠ 0`).

## Net

The analytic wall of the uniqueness leg is now down on **two** independent honest
routes (divisor-matching and boundedness). The boundedness route is the one the
resurgence/state-integral vantage supplies, and it excludes the elliptic freedom in
the cleanest way (℘ is unbounded). What remains for the *rigidity* leg is to
establish one endowment for the concrete `Φ_b` — same-divisor **or** strip-bound —
from its state-integral / `PhiBProd` construction; the *value* of the odd A_ω remains
the separate `Im 𝔙_q → N_odd` normalization capstone. Nothing fitted, nothing
axiomatised.
