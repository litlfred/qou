# Q_β c_k — state of play (recursion + q-difference axes) — full-corpus synthesis

**Date:** 2026-06-10
**Status:** SYNTHESIS + STALENESS AUDIT. This doc does **not** change any rung
tier — per the flip-flop guard, tiers live only in
[`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
(authoritative, 2026-06-04) and method-level closures live in the
[refuted-class map](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md).
It consolidates the ~30 c_k probes (2026-05-26 → 2026-06-06) into one current
picture, answers "is the recursive formula proved?", "where did the
q-difference investigations land?", and records the staleness corrections
found during the 2026-06-10 review.

---

## 1. Per-rung state (unchanged since registry 2026-06-04)

`Q_β = Q_base · ∏_{k≥2} (1 + c_k·u^k)`, `u = b·ℏ_q² ≈ 0.00852`, each rung buys
~2.07 digits; 100× target needs N=3, 1 ppQ needs N=7.

| rung | tier | note |
|---|---|---|
| c_2 = −1 | **CANONICAL** (proved, Taylor-exact, anchor-stable; Kashiwara f̃₁², bar-even) | the only derived rung |
| c_3 ≈ −2.07 (p) / −2.02 (μ) | empirical near-match; **refuted as any real-q formula** | 2.37 % anchor swing; `dc_3/dq ≈ 4.6×10⁶` rigidity kills all real-q forms |
| c_4 | empirical (CODATA fit / normalisation artifact) | |
| c_5 | empirical outlier | |
| c_6, c_7 | imposed in extraction (self-consistent only) | |
| c_8–c_10 | silver-ratio (q=1+√2) Pell-Lucas identities PROVED there; pattern breaks at the first free rung c_8 | stays empirical |
| kernel R(q,ξ) / element F(q) | **the open keystone** | constrained, not constructed |

**Production wiring: c_2 only.** Q_β dashboard: 1279 ppb = 164× off the
7.8 ppb 100× target (post proton re-pin). The 0.17 % gap is the c_2-level
truncation residual, and `Q_A(q₀)` alone already supplies the scale
CODATA-Q_β-free to 0.168 % (PR #1752).

## 2. The recursion — what is actually proved vs open

The user-visible claim "there is a recursive formula" decomposes into four
distinct objects; only the first two are proved:

1. **The conditional recursion engine (proved, sorry-free).**
   [`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
   proves: *IF* `F(qξ) = R(q,ξ)·F(ξ)` (depth-d q-difference equation) *THEN*
   `c_{k+1} = Σ_{j=1}^d a_j(q₀)·c_{k+1−j}` via the Habiro `(u;u)_m → u^k`
   change of basis. It is titled "Proposition (scaffolding)" for a reason: it
   produces **no c_k values** until R and F are constructed.
2. **The pre-archimedean z-recursion backbone (proved, sorry-free).**
   `MarkovParameterRecursion.lean` + `qbeta_prearchimedean_z_recursion.py`
   (PR #1739): `4(n+1)a_{n+1} + 6n·a_n + (2n−1)a_{n−1} = 0` for the Markov
   parameter `z(q) = √q/(1+q)` and its `z^k` family — exact to all orders,
   no q₀/CODATA. This is the recursion ↔ q-difference identity **for z**,
   NOT for the c_k; connecting them is the open f-map.
3. **The kernel R(q,ξ) (open, but tightly constrained).** Accumulated
   constraints: depth ≥ 2 (`c_1 = 0, c_2 = −1 ≠ 0`); **constant kernels
   refuted through depth 4** (commit `eca145ca`); **constant depth-2 kernel
   refuted** (PR #1900 — it over-determines `c_4 = 1 − c_3² ≈ −3.28` vs
   fitted −0.97, 3.4× miss) ⇒ depth ≥ 3 **or non-constant q-rational**
   coefficients; leading coefficient `a_1 = −c_3 = √2·Φ₂` is **bar-ODD** —
   confirmed by three independent routes (Reeb-sinh parity #1887/#1900,
   Hoefsmit `α_eff = (z−1)h/2` #1907, Habiro bar-dual of α_EM #1911);
   ζ₄ residue; `√u → u²` lift.
4. **The element F(q) / the phase Φ(u) (open).** The #1887 reframe is the
   cleanest current statement: `Q_β/Q_A = cos(Φ(u))` with `Φ₁ = √2`
   **anchor-exact** (forced by c_2 = −1, sorry-free Lean) and
   `Φ₂ = −c_3/√2 = 1.46324616887618 (p) / 1.42849728553818 (μ)` as the open
   object the kernel must generate. #1907 closed the "easy path": the on-main
   N=2 angle `α = (z−1)h/2` is a DISTINCT phase (gives c_2 = −9/8, not −1);
   `Φ₂` does **not** follow from it by reparametrisation.

## 3. q-difference investigations — consolidated verdicts

| finding | verdict | source |
|---|---|---|
| `g(u) = Σ c_k u^k` has radius of convergence **exactly u_substrate**; `c_{k+1}/c_k → 1/u ≈ 117.41` (4 sig figs at k=8,9,10) | structural fact; kills any constant-coefficient 2-term recurrence | PR #1713 |
| Singularity type: **simple pole at u_substrate, fibre-level**; same location at both anchors (210 ppb) | structural fact; residue `A ≈ 1.804×10⁻¹⁵ ≈ 1 ppQ` | PR #1727 |
| Residue A categorical ID | 38 candidates / 6 families exhausted; formally accepted **CAL-3-anchored** (2026-06-03); 4 KLR composite preflights (Wenzl×qPoch, Demazure×qPoch, Lusztig-dual, Type-B folded crystal) ALL refuted at u² in one-session gates (PRs #1914, #1924) | registry §3; cont. 16–18 |
| Habiro q-difference Fourier spectrum | d=2 (bar-even) mode has Δtr_M = 0; d=3≡6 period-3 resonance; ζ₄ pole | 2026-06-01 audits |
| Holonomic (D-finite) recurrence on c_2..c_10 | **no low-order holonomic recurrence** — but the test is blocked at the data level (below) | PR #1844 |
| Scalar exact-Δ(net) route to c_k | **ruled out structurally**: u is quadratic in t = q−1 ⇒ u-reversion is singular ⇒ c_k are **operator-valued ladder coefficients** (Hoefsmit T_β matrix N=k levels), not scalar-q Taylor coefficients | 2026-06-04 keystone recipe §"Execution finding" |
| T_β operator basis-dependence | T_β collapses to `S·I` under the Markov pairing, but the **c_k are L2/Markov-invariant** (they live in the constraint `τ_M(T_β) = S(q)`, not the objective) | PR #1750 |
| Symbolic SDP strict complementarity (replace min-L2-at-q₀) | honest PARTIAL: Frobenius Gram is **indefinite** ⇒ LP objective degenerate; but the selector **direction is S-independent and q-rational** ⇒ the c_k ratios carry NO CODATA-Q_β; the single archimedean leak is the scalar `S = Q_β/E₀` which cancels in c_k | PR #1752 |
| 6 NF coordinates of T_β | now q-rational closed forms × the single scalar S (`x_i = A_i(q)·S/‖A‖²`) — the archimedean input to the whole chain is **one number, not six** | PR #1739 step-1 closure |

### 3-bis. Pre-archimedean depth-1 backbone — the q-heat route (2026-06-10, this branch)

The corpus's q-exponential is the **abstract grouplike `exp_q ∈ G(ℋ_q)` over
`ℤ[q,q⁻¹]`** (`def:q-exponential`); the familiar power series is explicitly its
*archimedean realisation* (`prop:q-exponential-taylor` — "a theorem about the
ℂ-fibre of the moduli of grouplikes"). Its defining Jackson equation
`D_q exp_q = exp_q`, cleared of denominators, IS a depth-1 q-difference
equation — the prototype cyclotomic kernel, exact at the fibre level:

```
exp_q(q·x) = (1 + (q-1)·x) · exp_q(x)
```

Consequences (Lean, sorry-free, generic `CommRing` per §7c —
`QOU.BraidKnot.QBetaPreArchHeatDepthOneKernel`, this branch):

- **Per-mode kernel.** Each Peter–Weyl heat mode `f_λ(t) = exp_q(−μ_λ·t)`
  satisfies `f_λ(q·t) = (1 − (q−1)·μ_λ·t)·f_λ(t)`, with
  `μ_λ(q) = ℏ_q²·Σ_cells [c]_q[c+1]_q` the content-Casimir spectrum
  (`prop:q-heat-kernel-peter-weyl`) — q-rational, fibre-level, zeros located
  by the spectrum (`[c]_q` factors degenerate at roots of unity → a natural
  source for the proved ζ₄ structure).
- **Division-free composition.** Sums of two depth-1 modes satisfy the explicit
  depth-2 relation `(B−A)(t)·[S(q²t) − A(qt)·S(qt)] = (B−A)(qt)·B(t)·[S(qt) −
  A(t)·S(t)]` — valid over any commutative ring (no Casoratian division). This
  is the assembly step toward heat-trace kernels `Π_λ (1 − (q−1)·μ_λ·t)` for
  truncations of the partition function `Z_q(t) = Σ_λ d_λ(q)·exp_q(−μ_λ·t)`.

**Status: candidate FAMILY for the §2 kernel `R`, ungated.** Structural (which
blocks are active is forced by the operator, not tuned — compatible with the
June-9 anti-fit rule), but it must still produce a bar-odd `a₁ = −c₃ ≈ 2.07`
and survive the constant-depth-2 `c₄` refutation (§2). The Stage-B probe on
this branch evaluates the `R_λ` factors alongside the unbiased `c₄..c₈`
extraction. This is the second exact pre-archimedean backbone, alongside the
`z(q) = √q/(1+q)` 3-term recursion (PR #1739); the f-map question — how the
ladder `F` is assembled from such atoms — is unchanged.

## 4. The unifying result — the extraction precision floor (read this first)

[`2026-06-04-qbeta-ck-holonomic-c11-attempt-verdict.md`](2026-06-04-qbeta-ck-holonomic-c11-attempt-verdict.md)
§"The deeper layer" proves the information-theoretic wall:

```
σ(c_k) = σ_R / u^k,   σ_R ≈ 6×10⁻⁷  (AME2020 neutron Q-value precision)
```

| k | σ(c_k)/\|c_k\| | data-determined? |
|---|---|---|
| 2 | 0.8 % | yes |
| 3 | 49 % | marginal |
| 4 | 101× | **no** |
| 7+ | 10⁷×+ | no (free-rung "values" are noise) |

**Only c_2 and c_3 are data-determined — at any anchor count** (multi-anchor
averaging is short by ~10⁴×). This single fact *derives* the registry tiers,
the 4-sig-fig ceiling, the erratic c_8–c_10, and why every structural test
beyond k=3 came back ambiguous: they were run against below-floor data.
⇒ **c_k≥4 can only ever come from a framework derivation** (the fibre-level
Habiro element / kernel), never from extraction. This retroactively justifies
the registry's "empirical" tier for every fitted rung and closes the debate
about whether more anchors or more precision would help.

## 5. Are the many agent pieces mutually consistent? (correctness review)

Verdict: **the authoritative spine is consistent** (registry → refuted-class
map → formalize-first gates → ledger sessions log), and the flip-flop guard
has held since entry #5 (2026-05-31) — no c_k≥3 has been re-wired. Four
staleness items found:

1. **STALE (fixed in this PR):** `1ppq-qbeta.md` §Open-probes blockquote still
   named "trace-level Markov-stabilization `Ind_{H₃}^{H₄}`" as *the* open
   axis. That axis is itself **REFUTED** (PR #1850, refuted-class row C12,
   post-update §3); the open axis is **decay-side fibre-level F(q) only**.
2. **STALE (fixed in this PR):** cheat-sheet §5 manager-view #2 cited
   "live work in PR #1739" — superseded by the June-4–6 arc (refuted-class
   map; precision floor; 4 KLR preflight refutations; kernel constraints).
   Currency note + registry pointer added.
3. **Flagged, not changed:** `CLAUDE.md` "2026-05-31 c_3 SETTLED" note — the
   registry §7 already lists it as drifted (the settle was re-litigated
   2026-06-03/04 and re-closed harder). Owner-visible file; left to owner.
4. **Flagged, not changed:** legacy witness
   `qbeta-transfer-eigenvalue-proof.witness.json` still carries flip-flop-era
   prose ("c_3 = J − ℏ² at 0.004% (hypothesis)"). Superseded by the registry;
   a future qa-sweep pass could stamp it.

Minor cross-doc nits that are NOT errors: the ledger's c_k table (2026-06-03)
says c_6 "NOT derived" while the registry says "applied in extraction
(self-consistent)" — same empirical tier, different wording; the deep-audit's
"4/7 / 6/7" L2 counts are pre-re-pin stale and already superseded (live count
**3/7**: m_p, m_e, m_K/m_π).

## 6. What we need to do — the live menu

The search space is now so pruned that the options enumerate cleanly:

1. **Hoefsmit Stage B — exact operator-level c_4..c_8** (deterministic
   compute, ~1–2 sessions). Stage A validated the per-block χ^λ infra; the
   symbolic-candidate probe's own verdict names the next step: "build
   Hoefsmit-rep ρ_λ(𝓑₃) per Wedderburn block, form net(T_w), take Tr
   symbolically for exact unbiased c_4..c_8" (probe 6.d′), with c_2 = −1 /
   c_3 ≈ −2 as per-stage gates. Per §4 these values can't be data-validated —
   their value is internal consistency + feeding the kernel search with
   clean rungs (replacing the +1.7 %-biased SDP extraction).
2. **Kernel R(q,ξ) / Φ₂(q) derivation** (the genuine keystone; owner-gated
   multi-session research). All constraints are in place: depth ≥ 3 or
   non-constant; bar-ODD leading coefficient `a_1 = √2·Φ₂` (3 independent
   confirmations); ζ₄ residue; simple pole at u_substrate; q=1 shadow
   `c_3 → −2`; bar-even F overall; anchor-stability gate. The 7-step
   pre-flight checklist (2026-06-05 gates consolidation) makes any candidate
   cheap to evaluate. Sibling machine: #1871's `G(x;q)` recurrence, which
   must reproduce the Φ₂ targets.
3. **Option A — accept CAL-3-anchored permanently** (status quo, heavily
   backed: 3 corpus closures + 4 preflight refutations + 3 structural
   narrowings). Q_β stays c_2-only in production; m_n and Δ_pn inherit the
   acceptance; the only remaining theoretical escapes are exotic-signed
   Lusztig / Demazure-Lusztig variants (research-grade, preflight-gated).
4. **Doc hygiene** — items §5.3 / §5.4 (CLAUDE.md note; legacy witness
   stamp), owner discretion.

Options 1 and 2 are complementary (1 feeds 2); option 3 is the default if
neither is pursued. Nothing here re-wires production — any future wiring of a
c_k≥3 still requires owner approval + a passing proton+muon cross-anchor test
per registry §8.

## 7. Cross-references

- Tiers: [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) ·
  Methods: [refuted-class map](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md) ·
  Gates: [2026-06-05 consolidation](2026-06-05-qbeta-formalize-first-gates-consolidation.md)
- Precision floor: [holonomic c_11 verdict](2026-06-04-qbeta-ck-holonomic-c11-attempt-verdict.md) ·
  Operator-route recipe: [1ppQ keystone recipe](2026-06-04-qbeta-1ppq-keystone-exact-construction-recipe.md)
- Recursion status: [pre-archimedean recursion](2026-06-02-qbeta-prearchimedean-recursion-status.md) ·
  Ledger: [`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) (sessions cont. 1–18)

## 8. Update (2026-06-16) — the two keystones are one complex volume `𝔙`

The §2 open objects — kernel `R(q,ξ)` (Q_β brane-tower) and element `F(q)/Φ(u)`
— are **Re/Im of a single complex-volume observable**
`𝔙 = E₀·tr_M((Π_free−1)∘𝓜)` (`conj:binding-qbeta-complex-volume`): `Re 𝔙` is
binding (bar-even/cosh), `Im 𝔙` is `𝔔_β` (bar-odd/sinh), the QOU analogue of
Neumann–Zagier `Vol + i·CS`. Consequences for this synthesis:

- The two parallel searches collapse to **one**: find a complex `𝔙` matching
  the binding channel (`Re`) and the `𝔔_β` channel (`Im`) at one normalisation.
  The shared constraints (ζ₄ residue, bar-odd `a₁`, simple pole at `u_substrate`)
  are constraints on `𝔙`'s two parts simultaneously.
- The Hoefsmit Stage-B "two `c₂`" (net-route `≈−8` vs brane-tower `−1`) is the
  expected `Re`/`Im` split, **not** route-dependence
  ([Stage B verdict §reframe](2026-06-16-hoefsmit-stage-b-attempt-verdict.md)).
- **Still open** (the §4 precision-floor question): are the per-channel `c_k`
  constants or fibre q-functions? Candidate resolution (owner, 2026-06-16): the
  `c_k(q)` are fibre q-functions **evaluated** by the non-degeneracy of the
  Markov pairing at `Vol = 1` — i.e. `R(q,ξ)` is a q-function and the
  unit-normalised pairing is the evaluation map to the observed rungs.
