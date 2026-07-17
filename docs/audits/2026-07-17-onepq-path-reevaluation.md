# Path to 1 ppq — re-evaluation after the 2026-07-11…17 week

**Date:** 2026-07-17 · **Tier:** strategic re-evaluation (survey of main landings +
active siblings). **Supersedes the ranked-lever section of**
[`2026-07-11-path-to-1ppq-alpha-em-opportunity.md`](2026-07-11-path-to-1ppq-alpha-em-opportunity.md)
(landed `60158ad0`). **No c_k wired; scope-(a); critical-distance.**

> **Coordination (2026-07-17): the general reassessment here is superseded by the
> merged parallel audit
> [`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md)
> (`6a529aa744`)**, which is more complete — it adds **L1 CLOSED (6/6 atoms
> 1ppQ-certified, ⁴He 07-13)**, and supersedes any raw-ratio Borel-`A` reading with
> the **conformal-mapped Borel plane `A ≈ 0.646–0.657 vs Vol(4₁)/π = 0.6461`
> (Vol/π *back in play*, "consistent not identified")**, with the derived-Stokes
> route now the **GGM 3d-index counts (G3), under active attack on #3805**. **Lever 1
> (the odd-channel Stokes datum) is that line's — this session does not duplicate
> it.** The distinctive, non-duplicated contribution retained here is the **§Lever-2
> re-scope** below (the α_EM per-loop measure channel-split), which the parallel
> audit names as a wall but does not re-scope. The lever ranking in §"Re-ranked path"
> stays as an independent second read; where the two audits differ on lever 1, defer
> to `6a529aa744` (L1 closure + conformal Borel are firmer).
>
> **Update (2026-07-17, this session): lever 1 attacked independently — the
> odd-channel divergence class is characterized (§Lever-1 below).** Per the owner
> directive not to defer, this session did *not* wait on the parallel line; it
> measured the bar-odd D-ladder's Gevrey class directly and found the
> even-channel plain-Borel method (Vol/π on the κ rungs) **does not transfer** to
> the odd channel (drifting order). That is a non-duplicated constraint on the G3
> route (#3805), not a re-run of the even-channel Borel.

## Lever-2 advance (this session): the α_EM per-loop measure is the standard loop unit, not a Betti factor

The 2-loop derivability map isolated one underived factor: the per-loop measure
`1/(πb₁) = 1/(8π)`, labeled "parallel to the zero-mode `1/(π·dim H¹)`" but shown
inconsistent (the proved `1/Area = 1/(12π)` fails at 1-loop by −1419 ppb). This
session **re-scopes that wall structurally** (probe
[`alpha_em_channel_split_loop_measure_probe.py`](../../computations/alpha_em_channel_split_loop_measure_probe.py),
all steps symbolically verified):

1. **The loop tower factors into the two braiding channels** (re-verified to
   `O(x¹²)`, sympy): `Σ_{L≥0}(−1)^L[L+1]_q x^L = 1/((1+qx)(1+q⁻¹x))` — the two
   Hecke eigenchannels `q`, `−q⁻¹` of `A⊗A` (singlet/adjoint idempotents), each a
   geometric series with per-loop ratio `q^{±1}x`.
2. **At `q→1` with `x = α/(8π)` the one-loop term is exactly `α/(4π)`** — the
   *standard 4D gauge-theory loop unit*, carried jointly by the two channels
   (each `α/(8π)`).
3. **Therefore `1/(8π) = ½·(1/(4π))` structurally**, and the `π·b₁` form is a
   **genus-4 coincidence**: `π·b₁ = 2·(4π) ⟺ b₁ = 8 = 2g`. The structural constant
   is `2×4π` (two channels × loop unit), **not** `π·(Betti number)`.

**Honest tier — a re-scope, not a closure.** The underived *geometric*
identification `1/(π·dim H¹)` is replaced by **(derived two-channel factorization)
+ (one input: the `q→1` correspondence normalization = the standard gauge loop unit
`α/(4π)`)**. That input is standard-QFT, not a new geometric claim — but it *is*
still an input. **Discriminant:** the channel-split predicts a **genus-independent**
measure (`2×4π` always); the `π·b₁` reading scales with genus. Not separable at fixed
`g=4` by data, but decisive for any multi-genus construction and consistent with the
derivability map's own finding that the `b₁`-parallel is unsound. Numerics unchanged
(form-B proton residual `+0.313 ppb = 2.1σ`). No coefficient fitted.

## Lever-1 advance (this session): the odd-channel Stokes datum is drifting-order q-Gevrey — plain Borel does not transfer

The G3 keystone (`z(q₀) → S` = a Stokes constant `A_ω`) lives in the **bar-odd**
channel. The parallel line pinned the **even** κ-channel via a plain/conformal
Borel (`A ≈ 0.646 ≈ Vol(4₁)/π`, "consistent not identified"); the odd channel had
only been characterized by *negatives* (not q-holonomic base-3; no coupled ℚ(√3)
recurrence; 2-adic parity grading). This session measures the odd channel's
divergence class directly (probe
[`qbeta_odd_channel_stokes_borel_probe.py`](../../computations/qbeta/qbeta_odd_channel_stokes_borel_probe.py)
+ witness; exact ℚ(√3) ladder `d₁…d₂₁` at ORD 44, `d₁…d₂₇` at ORD 56,
odd-order over-determination = 0):

1. **Root test rises only slowly** — `|dₖ|^{1/k}`: 5.70→5.91 over k=16…21, no
   doubling. So the ladder is **not q-Gevrey-1 in any base > 1** (that would blow
   the root test up geometrically).
2. **The effective Gevrey order DRIFTS DOWN** with the tail:
   `C(lo=4,8,12) = 0.099, 0.067, 0.058` (ORD 44); `0.081, 0.059, 0.051` (ORD 56).
   Not a fixed Gevrey-s — no single Borel–Leroy order canonically resums it.
3. **The Borel–Leroy pole is therefore s-dependent** — `0.147 (s=0.02) → 0.165
   (s=0.10) → 0.249 (s=0.30)`. The stability-optimal low-s window band is
   **≈0.147–0.168**, which brackets `1/(2π)=0.1592`, `Vol(4₁)/(4π)=0.1615` (=
   even-channel `Vol/π` ÷ 4 — the same factor-4 as the α_EM two-channel loop
   split), and `1/6=0.1667`. The ~12 % s-systematic makes this
   **consistent-not-identified**, not an identification.

**Honest tier — scope-(a) NEGATIVE** (per AGENTS.md "refuted/ruled-out"): the
fixed-order Borel–Leroy method, *alone*, does not extract a clean odd-channel
action; the order drifts. This does **not** exclude an odd-channel Stokes
constant (no proved invariant forbids one) — it says the **even-channel
plain-Borel route does not transfer**, and G3 (#3805) needs the true **q-Borel /
alien-derivative chain** (base `q₀` or base-3), not a fixed-order Leroy. No fit;
no `c_k` wired; comparison-only. *Constraint delivered to the G3 line:* don't
apply a fixed-order Borel to the odd ladder — measure/deform the q-Borel base.

### Cross-link to the landed A1 saddle data (main `360a1b22d9`, `57a0fcd02f`)

Two commits landed on `main` in parallel with this session, from the saddle
(Φ_b 2-loop) side, and they **corroborate the finding and explain the band**:

- **Independent confirmation of the negative.** `57a0fcd02f` feeds the certified
  complete-structure `A1 = 1/3 + 0.2726i` into the F1 acceleration and finds the
  b-dictionary is a **scale-invariant prefactor** — "root-test & ratio radii
  (both degree-0 in scale) are UNCHANGED (gap 0.0194→0.0194) — A1 does NOT rescue
  the k=21 gate; it fixes the resummed value's normalization, **not the
  singularity location** … the gate needs more rungs (k=31 drift persists)." That
  is exactly this probe's scope-(a) negative, reached from the saddle side: the
  singularity/action is not perturbatively extractable, and the order drifts.
- **The band is the saddle's own data.** The A1 derivation (`360a1b22d9`) is
  gated on **G2: `|−V″(z\*)| = √3`** (adjoint Reidemeister torsion) at the 4₁
  saddle `z\* = e^{iπ/3} = (1+i√3)/2`, with `−V″(z\*) = −3/2 + i√3/2` (verified
  to 30 digits) and **G1: `Im V(z\*) = Vol(4₁) = 2.0298832`**. So:
  - the odd ladder is **ℚ(√3)-valued** because the bar-odd (imaginary) part of the
    saddle Hessian is `√3/2` — the same √3, same 6th-root-of-unity saddle;
  - `Vol(4₁)/(4π) = Im V(z\*)/(4π) = 0.16153` sits **inside** this probe's odd-face
    band `[0.147, 0.168]` — i.e. the "consistent-not-identified" candidate is the
    saddle's imaginary potential (hyperbolic volume) over the `4π` two-channel loop
    measure, not an arbitrary constant. `Vol(4₁)/(4π) = (even-face Vol/π)/4`.

  This upgrades "band brackets `Vol(4₁)/(4π)`" from numerical coincidence toward a
  **structural expectation** (both faces are shadows of one saddle datum) — but it
  is *still not an identification*: the 12 % s-systematic stands, and the exact
  odd-face action needs the non-perturbative q-Borel/3d-index (#3805). Note also
  `57a0fcd02f`'s **D1 refutation** of the naive meridian-deformed potential
  `V_u = Li₂(z) − Li₂(1/z) − u log z` (`V_u′(z\*) ≠ 0`): the correct 4₁
  meridian-deformed potential is a **named open piece**, so no deformed odd-face
  `A1` is claimed here either. Formalize-first: the perturbative route is pruned
  from both sides; the live instrument is the 3d-index.

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
