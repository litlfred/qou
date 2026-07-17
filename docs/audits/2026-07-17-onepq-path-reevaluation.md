# Path to 1 ppq — re-evaluation after the 2026-07-11…17 week

**Date:** 2026-07-17 · **Tier:** strategic re-evaluation (survey of main landings +
active siblings; no new compute). **Supersedes the ranked-lever section of**
[`2026-07-11-path-to-1ppq-alpha-em-opportunity.md`](2026-07-11-path-to-1ppq-alpha-em-opportunity.md)
(landed `60158ad0`). **No c_k wired; scope-(a); critical-distance.**

## Headline

L2 is still **2/7** (`beats_100x_count = 2`: m_e, m_K/m_π) — but the week
**replaced both frontier problems with sharper, better-posed ones**:

- the Q_β "wall" is **gone** (proved a representation artifact; the live route is
  now a *resurgent Stokes-constant computation* with machinery that landed this week);
- α_EM collapsed from "c₂ uncomputable" to **one underived factor** (`1/(πb₁)`),
  with a parameter-free 2-loop candidate already sitting at **1.3σ**.

## 1. Q_β / m_n / Δ_pn trio (3-for-1 → 5/7) — the wall was an artifact

The week's capstone ([`2026-07-12-c3-wall-resolution-capstone.md`](2026-07-12-c3-wall-resolution-capstone.md), PRs #3600/#3636/#3654) resolved the four-session "near-singular `u(q₀)` map":

- **`dc₃/dq ≈ 4.66×10⁶` is a `1/u³` ladder artifact over smooth geometry** — the
  extractor divides a *smooth* numerator zero by `u³ ≈ 6×10⁻⁷`. No singularity exists.
- **The sign-flip is structural bar-odd parity** (Lean sorry-free: `fig8Trace_im_odd`):
  `S` is bar-odd, so with `q = q₀ + iε`, `sign S = sign ε` — no real `q₀` flips it.
  (This *supersedes* the branch-selector framing of #3573 as the operative story: the
  complexification is `Im(q)`, and it is smooth.)
- **`q*` (the `S=0` point) is a third, decay-sector determination of `q₀`** — the μ–p
  tension is now a **μ–p–Q_β three-way**.
- **Φ_b status** ([`2026-07-13-phib-proof-status…`](2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md)):
  G2 **closed** (cyclic fibre-branch construction, 5 sorry-free Lean results, PR #3768);
  the analytic real-integral `Φ_b` also landed sorry-free (`95169c15`). **The single
  remaining keystone is G3: the monodromy datum `z(q₀) → S` = a Stokes constant `A_ω`
  via the alien derivative** — a *resurgent* computation.
- **The machinery for exactly that computation landed this week:** Ohtsuki rungs
  `κ₁..κ₈` derived symbolically exact (`179b2afa`); exact-rung Borel analysis
  (`37cbf722`: `A≈0.758`, Vol/π refuted, `β≈2`); binding-side precedent of a
  **closed-form Stokes constant** `A_ω = 4√2·e^{−3/8}` at `ω₀=1/√2` (`c7fdd8ae`);
  Gevrey-1/2 proof; deformed rungs `κ̃₁, κ̃₃` at tall-ladder precision. And registry
  rows **KC21/KC22** close the (q-)holonomic search class — the odd channel is
  Écalle-class, so **the resurgent chain is the unique live route** (plus KC19's
  `w(q)` from the state integral and canonical `c₄^even` via H₄ Hoefsmit).

**Re-evaluation:** a week ago this was "characterize the target, hand to Φ_b."
Now it is a **well-posed single computation** (G3: extract `A_ω` for the odd channel)
with the alien-calculus toolchain landed and a solved same-class exemplar. This is
the top lever, and it is *closer* than it has ever been.

## 2. α_EM — from "c₂ uncomputable" to ONE underived factor

The [2-loop derivability map](2026-07-14-alpha-em-2loop-derivability-map.md) supersedes
my week-old "c₂ is entropy-blocked/observational-floor" verdict via **structure, not
fitting** (exactly the formalize-first escape route):

- **Derived now:** tree; zero-mode count `b₁=8` + measure `1/Area` (proved); the
  **graph grammar** (loop `L ↦ [L+1]_q`, θ-graph = unique 1PI 2-loop topology
  `= [3]_q`); the full **loop resummation** `Σ(−1)^L[L+1]_q x^L = 1/((1+qx)(1+q⁻¹x))`
  (the two braiding channels).
- **The single wall:** the **per-loop measure `1/(πb₁) = 1/(8π)`** is underived — and
  provably *not* the zero-mode measure (`1/Area` fails at 1-loop by −1419 ppb). The
  measure consistency probe isolated it cleanly.
- **The prize:** with the underived measure, the θ-graph 2-loop gives
  **−0.20 ppb = 1.3σ** — parameter-free, the best number in the corpus, contingent on
  that one factor.

**Re-evaluation:** α_EM's path is now *derive one geometric factor* (`1/(πb₁)`:
why `π·b₁` rather than `Area` as the per-loop denominator) ⇒ the entire tower
through 2-loop follows ⇒ ~1.3σ. Sharper and more valuable than the trio in
$/insight, but the trio remains 3-for-1 on the dashboard.

## 3. Absolute masses / binding — Subgoal-1 progress, 1ppq unchanged

Real motion (bond-count `M_n = n−1` → ³H at −0.16% zero-fit; classical `q=1` binding
kernel derived sorry-free; McKay `d_q(λ)=[mark]_q` exact; framing-is-phase) — but all
Subgoal-1/keystone material. The CAL-2 floor argument for absolute-mass 1 ppq is
unchanged. The week also demonstrated healthy self-policing (the SU(4) split
laundering caught by adversarial review — [`…na-stokes…adversarial-review.md`](2026-07-13-na-stokes-ck-recursion-binding-adversarial-review.md)).

## Re-ranked path to 1 ppq (2026-07-17)

| # | lever | payoff | state |
|---|---|---|---|
| 1 | **G3 monodromy datum**: extract the odd-channel Stokes constant `A_ω` (`z(q₀)→S`) via the alien-derivative chain on the exact `κ` rungs | **2/7 → 5/7** (Q_β, m_n, Δ_pn) | well-posed; toolchain + same-class solved exemplar landed this week |
| 2 | **α_EM per-loop measure**: derive `1/(πb₁)` | α_EM → **1.3σ** via the θ-graph; a structural derivation of α to ~experimental precision | single isolated wall; everything else in the tower is derived |
| 3 | canonical `c₄^even` via H₄ Hoefsmit (bean `8we6`) | next even rung, de-noises the ladder | routine-hard compute |
| — | absolute-mass 1 ppq | — | unchanged: CAL-2 floor; s5-so3/keystone long-track |

**Meta-corrections to my own week-old framings** (for the record): the #3573
"branch-selector/near-singular" story is superseded by the capstone (smooth `Im(q)`,
`1/u³` artifact); the "c₂ permanently observational" verdict is superseded by the
θ-graph grammar (a structural candidate exists — the posture cost now attaches only
to the *measure*, not the whole coefficient).

## Cross-references
- Capstone: [`2026-07-12-c3-wall-resolution-capstone.md`](2026-07-12-c3-wall-resolution-capstone.md)
- Φ_b gaps: [`2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md`](2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md)
- α_EM map: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md)
- Ledger: [`../coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) (KC21/KC22)
- Machinery week-review: [`2026-07-13-last-5-days-machinery-for-mass-binding.md`](2026-07-13-last-5-days-machinery-for-mass-binding.md)
