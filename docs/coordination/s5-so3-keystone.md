# Coordination ledger — `conj:s5-so3-fiber-action` (the s5-so3 fibre-action keystone)

**Goal.** Discharge the keystone the QOU framework's open derivation math reduces to: the geometric
fibre map `S₅ ⊃ A₅ ≅ I ⊂ SO(3)` tying the partition-wise Wedderburn action on `H₅(q)` (combinatorial)
to icosahedral rotations on Bring's quintic surface (geometric). It is the single open object for
m_τ (lepton tower), GAP-A-3 binding Δ_λ, and GAP-A-4 mass λ(K).

> **🟧 GENERAL owner reversal — Subgoal-2 open for all (2026-07-11).** The 2026-06-19 reversal that
> first brought *this* keystone in scope has been **broadened generally**: all Subgoal-2 geometric /
> substrate-derivation routes (absolute m_p/m_n/m_⁴He, substrate q_0, the binding `M_n(K)` edge-set /
> coordination-graph closure, and this s5-so3 keystone) are now **in scope for all agents** — no
> per-item owner sign-off required. The anti-fit / anti-laundering honesty discipline is orthogonal
> and unchanged (a fit is still a fit; only derivations wire to production). Ruling:
> [`docs/audits/2026-07-11-subgoal2-owner-reversal-open-for-all.md`](../audits/2026-07-11-subgoal2-owner-reversal-open-for-all.md),
> [`docs/precision-goals.md`](../precision-goals.md).

**Status (2026-06-16).** Reduced — by formalize-first pruning — to **one differential-geometry
problem**. Everything combinatorial / representation-theoretic / algebraic is done or refuted; no fit
was introduced anywhere.

**Status (2026-06-22).** The single open object is **not** differential geometry — it is the
colored Σ(2,3,5) WRT / `E_q(2)` q-Bessel q-series whose `q₀`-evaluation must reproduce `W_λ`
(the Markov-trace surface is now exhausted — projector-weight shift refuted, [#2584](https://github.com/litlfred/qou/pull/2584)).
See the 2026-06-22 update banner below.

> **⚠ Corrections (2026-06-16, late session) — the "OPEN" row + the colour-arena framing are superseded.**
> Three findings (mine + sibling) refine the open object below; read them over the "Current state" table:
> - **No finite colour-SU(3) arena** (#2406, reconciling sibling #2389). The "colour ℂ³ ✅ forced" row is a
>   *lower* bound only (spinor ℂ² can't host the electron). The full production trace needs **>3-row** blocks
>   too (SU_q(3)/colour-ℂ³ misses 3.4% @⁴He) — it is the **full Hecke / Wenzl principal specialization**
>   `s_λ(1,q,q²,…)`, *not* a finite ℂ^N. So there is **no finite colour-SU(3) Sasakian arena**.
> - **SU(3)/SO(3) (Wu-manifold) arena ruled out** (#2398): the spacetime SO(3) is the *isotropy* and has no
>   continuous centralizer in SU(3) (Schur) — no spacetime-fixing Reeb exists there. ⇒ **spacetime ⊥ colour**
>   (= corpus `S5 = S2×S3`), confirmed.
> - **`W_λ` is the q-Plancherel measure, NOT the production trace weight** (sibling `e269ca12ea`); the production
>   weight is the Wenzl principal specialization. So the "OPEN: W_λ via SU(3)/SO(3) Sasakian" row's *both* the
>   arena and the weight are corrected.
>
> **Corrected open object:** does the **full-Hecke principal-specialization trace** (infinite-variable,
> intrinsically `p(3A)`-dimensional) admit *any* geometric realization whose index reproduces the canonical
> Markov weights? A finite-dimensional Sasakian is ruled out. The Δ_λ magnitude×chirality decomposition and the
> PROBE-4 prune (abstract `H_n(q)`) are unaffected. Audits: `2026-06-16-{keystone-arena-is-full-hecke-not-su3,
> keystone-wu-manifold-reeb-obstruction}.md`; sibling `2026-06-16-s5-s3-symmetry-review-and-suq3-trace-question.md`.

> **⚠ Update (2026-06-22) — the arena is the non-compact `E_q(2)` contraction, NOT a compact Sasakian; the Markov-trace surface is exhausted.** Four 2026-06-22 sessions (bean `s5bb`, all merged) supersede the "Wu-manifold Sasakian / differential-geometry" framing above:
> - **q-deformed projector-weight shift REFUTED as the 210 ppb mechanism** ([#2584](https://github.com/litlfred/qou/pull/2584), merged). The E_λ-projected H₅ Markov trace gives `δ = T_μ − T_e = 0.2075` — non-null, so the q-deformed home-block weighting *does* break the (2,1) symmetry classical multiplicity preserved — but it is 6–7 orders too large for the 209.8 ppb gap and **bar-mixed** (fails the bar-even precondition). The Markov-trace surface (multiplicity / home-block weight / projected trace) is now **exhausted**; any surviving q-closure must leave the trace-weighting entirely. ([`2026-06-22-keystone-qdeform-projector-shift.md`](../audits/2026-06-22-keystone-qdeform-projector-shift.md))
> - **No compact Sasakian / compact MTC can host `W_λ`** at the substrate anchor: `q₀ ≈ 1.10998` is real `> 1` (growth regime, `[m]_q = sinh(mη)/sinh(η)`, `η = log q₀` real), not a root of unity. The `W_λ`-producing structure is the non-compact `SU_q(2) → E_q(2)` contraction whose matrix coefficients are **Hahn–Exton q-Bessel** functions (already named in the corpus, `2026-06-13-reeb-phase-qbessel-identification.md`). ([`2026-06-22-keystone-modular-category-identification.md`](../audits/2026-06-22-keystone-modular-category-identification.md))
> - **Sharpened open object:** pin the **colored Σ(2,3,5) WRT / Habiro-ring q-series** whose evaluation at `q₀` reproduces the `W_λ` family — reached from the convergent WRT series via the `q ↦ q⁻¹` bar involution (`q₀ ↔ 1/q₀ ≈ 0.901`, inside the disk). The bare `Σ(2,3,5)` Lawrence–Zagier false-theta `Ψ(1/q₀) = 2.32958` is operational but is **one** number vs a **λ-family** (type mismatch — *not* claimed equal to `W_λ`; the numerology trap the discipline forbids). ([`2026-06-22-keystone-habiro-wrt-s3-2i.md`](../audits/2026-06-22-keystone-habiro-wrt-s3-2i.md), [`2026-06-22-keystone-geometric-level-route-reduction.md`](../audits/2026-06-22-keystone-geometric-level-route-reduction.md))
> - **Falsifiable, `q₀`-free sub-target:** any index realizing `W_λ` must reproduce the heat-kernel defect coefficient `144·C(n) = −n(n−1)(2n−13)` exactly (the `n = 7` sign change). The algebra is Lean-proved sorry-free ([`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean), `n144C_closed_form` / `n144C_pos` / `n144C_neg`); the one carried representation-theoretic input is **Identity I** `M(n) = (1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c} h_c² = n(3n−1)/2`. **Status (corrected 2026-07-11 — the earlier "held as a `def twoM`, multi-session infra fill" wording is stale):** Identity I is **conditional-proved sorry-free** (#2709, `IdentityIPlancherelConditional`, on a `class PlancherelSnData n` axiomatising the two standard `ℂ[S_n]` facts (i) `Σ_λ dim(λ)²=n!` and (ii) the Jucys–Murphy content-square mean) and **unconditional for `n=3..12`** via explicit `decide` instances (#2760, `IdentityIPlancherelInstances.lean`) — covering the deuteron `n=3`, keystone `n=5`, and defect sign-flip `n=7`. The `def twoM` is **eliminated** at those `n` (`n144C_eq_twelve_plancherel` / `defect_closedform_plancherel` re-express `n144C` via the genuine Plancherel squared-hook sum). The per-partition combinatorial half `Σh²=Σc²+n²` (`sumSqHooks_eq_sumSqContents_add_sq`, all `n`) and the JM core (`jm_identity_coeff_two`) are sorry-free. Only the **general-`n`** discharge (axioms (i)/(ii) for all `n` — Specht / RSK `RSKBurnsideHolds` / hook-length / representation theory) remains open, scoped as the P1–P5 program ([`2026-06-24-identity-i-plancherel-snrep-infra-program.md`](../scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md)). ([`2026-06-20-keystone-wlambda-C-n-closed-form.md`](../audits/2026-06-20-keystone-wlambda-C-n-closed-form.md))
>
> **Active open work (unmerged — this ledger reports merged facts; the live geometric frontier is these PRs, consistent with the E_q(2)/colored-WRT reframing above since WRT(S³/2I) = colored Σ(2,3,5) WRT is the same object):** [#2524](https://github.com/litlfred/qou/pull/2524) supplies a candidate **index mechanism** — `W_λ` as the MTC Plancherel measure `d_q²/D²` from **Beasley–Witten non-abelian Chern–Simons localization** on the Seifert 3-manifold `S³/2I` (Reeb = Seifert `S¹`) — and proposes the C1 normalization answer `d_q²/D²` (Σ = 1). [#2503](https://github.com/litlfred/qou/pull/2503) is the formalize-first DG attack plan (a *finite-dimensional* Sasakian is ruled out ⇒ the construction is infinite-dimensional WRT(S³/2I) = Lawrence–Zagier). [#2603](https://github.com/litlfred/qou/pull/2603)/[#2608](https://github.com/litlfred/qou/pull/2608) work the λ-coloured WRT colour-resolution + Schur–Weyl.
>
> **Owner-decisions to confirm (some now addressed by the open PRs):** (1) `W_λ` normalization — `d_q²/[n]_q!` (Σ ≈ 0.982) vs `d_q²/D²` (Σ = 1); **#2524 proposes `d_q²/D²`**. (2) **Gate status — CONFIRMED REVERSED (2026-06-22, owner).** The owner reversed the subgoal-2 geometric-derivation gate (2026-06-19; #2503/#2524) **for the keystone geometric `W_λ` DG construction** — now recorded in [`AGENTS.md §Precision-goals`](../../AGENTS.md) + [`docs/precision-goals.md`](../precision-goals.md). The reversal is **narrow**: it does not reopen fit-based q_0 derivation, and the Δ_λ "no seventh fit-based ansatz" rule stands. (3) Identity-I Mathlib infra fill scope. Outside-view (critical-distance): a Beasley–Witten/RT *reduction* gives `W_λ` a categorical *name*, not a new mass prediction — watch the tautology risk that the "geometric origin" is the harmonic analysis of the same `SU_q(2)` the framework already postulates.

> **Update (2026-06-30) — the localization obligation's necessary conditions are now pinned at the *physical* blocks.** [`WLambdaMTCLocalizationObligation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaMTCLocalizationObligation.lean) derives the keystone's C1 (normalization `Σ W_λ = 1`), C2 (chirality-blindness `W_{λ′} = W_λ`), C6 (full support `W_λ > 0`) as falsifiable necessary conditions any `S³/2I` gauge datum must satisfy, but its only worked model was the trivial `n = 2` (all `d_q = 1`). [`KeystoneWLambdaPhysicalBlocks.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneWLambdaPhysicalBlocks.lean) ([#3155](https://github.com/litlfred/qou/pull/3155)) supplies the named `n = 4`/`n = 5` witnesses via `heckeLocalizationOfPos`: at **n = 5** (the keystone `S₅`) C1/C2/C6 hold for the seven blocks `λ ⊢ 5`, including the **electron** `(3,1,1)` (self-conjugate) and **muon** `(3,2)` — `keystone_muon_transpose_eq` gives `W_{(3,2)} = W_{(2,2,1)}` (a genuine non-self-conjugate C2 pair), `keystone_{electron,muon}_pos` give `W_λ > 0`. lean-direct EXIT 0, sorry-free, axioms `[propext, Classical.choice, Quot.sound]`. So the geometric `W_λ` realization is now bound, at the physical electron/muon blocks, by three Lean-proved consistency obligations (C1/C2/C6) on top of the defect-cubic (`144·C(n)`) and `f_pn`-bracket gates. No fit; formalize-first.

## Current state

| Layer | Status |
|---|---|
| Combinatorial backbone `Res^{S₅}_{S₃}` + `SO(3)↓A₅↪S₅` bridge | ✅ verified |
| Geometry: 2I spin lift; geometric A₅ forced to icosahedral T₁; chirality = T₁/T₂ | ✅ verified |
| Algebraic functor target (Bratteli = box removal; Ocneanu trace) | ✅ forced |
| Strand fibre = colour ℂ³ (Schur–Weyl: spinor ℂ² kills the electron (3,1,1)) | ✅ forced |
| Static coupling `V_ℓ→E_λ` (Schur: dim Hom = 1) | ✅ forced |
| **Generation selection ℓ→λ = the Hopf moment map μ** (spatial SO(3)-equivariance) | ✅ **realized** |
| 210 ppb muon mechanism (Wedderburn-projector correction) | ❌ refuted (6–8 orders too coarse) |
| colour⊗spin = (3,1,1) dim-6 shortcut | ❌ refuted (spin-parity mismatch) |
| Reeb-eigenvalue resonance | ❌ refuted (no parameter-free ≥3-anchor match) |
| q-deformed projector-weight as the 210 ppb mechanism | ❌ refuted (#2584: `δ=0.2075` non-null but 6–7 orders too large, bar-mixed) |
| **OPEN:** `W_λ` geometric origin — colored Σ(2,3,5) WRT / `E_q(2)` q-Bessel q-series (**NOT** a compact Sasakian; see the 2026-06-22 banner) | ⛔ q-series (owner-gated) |

> **🟧 Frontier sharpening (2026-07-12, #3652 three-vector tranche).** The open object is now
> pinned to a **twist-free / conjugation-symmetric** amplitude, and two routes are pruned:
> - **Modular T-matrix `θ_λ = q^{c(λ)}` is now a Lean object** with the proved chirality law
>   `θ_{λ′} = θ_λ⁻¹` ([`KeystoneModularTwist.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneModularTwist.lean); the signed content-flip `c(λ′)=−c(λ)`, corpus had only the squared version). This is the **obstruction**: any framed colored-WRT weight `S_{0λ}·θ_λ^{f}` has `W_λ/W_{λ′}=θ_λ^{2f}≠1` while `d_q(λ)=d_q(λ′)` — the twist breaks a symmetry `d_q` has (vector 2, scope-(b) on that narrow hypothesis).
> - **q-Bessel `latticePt` structural index maps refuted** (vector 1, scope-(a)).
> - **The framing-cancellation reduces to the archimedean-continuation problem.** The only way to
>   kill `θ_λ^{f}` is in the squared modulus `|S_{0λ}θ_λ^{f}|²`, which needs `|θ_λ|=1` ⟺ `|q|=1`
>   (fibre-level root of unity, where `θ` is a phase). But there `|S_{0λ}θ_λ^f|² = S_{0λ}² = W_λ`
>   is the **Verlinde-measure definition** — so the genuine open content is the **archimedean
>   continuation** from the fibre root-of-unity to the substrate `q₀>1` (growth regime, `|θ_λ|≠1`).
>   That is *exactly* `bwS0_eq_hecke` (owner-gated), read through AGENTS.md's fibre-vs-observable-`q`
>   distinction: the RT/WRT amplitude lives at the fibre (root of unity, framing cancels in `|·|²`),
>   the mass observable is its archimedean evaluation at real `q₀`. **Do not re-chase
>   framing-cancellation as if it were new tractable ground — it is the archimedean-continuation
>   restatement of the standing open object.** Synthesis: [`2026-07-12-keystone-wlambda-construction-three-vectors.md`](../audits/2026-07-12-keystone-wlambda-construction-three-vectors.md).

**The single open object.** Does the SU(3)/SO(3) (Wu-manifold) Sasakian with spatial-SO(3)_colour Reeb
admit a structure whose S¹-equivariant index reproduces the Ocneanu weights `W_λ = d_q(λ)²/[n]_q!`?
(dim 5 odd ✓; χ(Wu)=0 ✓ — Boothby–Wang necessary conditions met, not obstructed at that level.) The
sibling A≥3 operator-branching compute (#2369/#2371/#2372) produces `W_λ` algebraically; the open piece
is its *geometric origin*.

> **Superseded (2026-06-22).** This paragraph's Wu-manifold/Sasakian framing is retained for history but
> **superseded** — at the substrate anchor `q₀ ≈ 1.10998` (real `> 1`, growth regime) **no** compact Sasakian /
> MTC hosts `W_λ`; the arena is the non-compact `SU_q(2) → E_q(2)` Hahn–Exton q-Bessel contraction and the
> sharpened object is the colored Σ(2,3,5) WRT q-series. See the 2026-06-22 update banner above.

## Literature scoping — the WRT domain question (2026-08-10, PR #4952)

**UPGRADED TO READ TIER 2026-08-10** — the owner supplied three of the six papers
([`95accb15`](https://github.com/litlfred/qou/commit/95accb153a132df290605fd2ad27930b2a47b8f9)),
and the domain finding below is now confirmed by direct quotation + measurement.
The reading list and route table remain a plan; math/0605314, 1411.6062 and
2412.04241 are still unread.

Counting `references.ts`: the corpus is deep on the q-Bessel/`E_q(2)` side
(Koelink 12, Woronowicz 12, Hahn 12, Exton 8) and on quantum modularity
(Garoufalidis 48, Habiro 29, Zagier 24), but thin exactly where the open object
lives — WRT 4, Brieskorn 4, Seifert 3, and **Beliakova 0**. Beliakova at zero is
the signal: a principal author of the *unified WRT* programme, and Σ(2,3,5) is a
Brieskorn sphere.

Two search-tier findings, the second load-bearing:

1. The unified-WRT programme (Habiro; extended by Beliakova, Le, Blanchet,
   Buehler) covers **Seifert fibered spaces**, with Brieskorn spheres
   `Σ(p₁,p₂,p₃)` studied in that context — the keystone's manifold family has an
   existing named construction.
2. Its **native domain is the roots of unity**: a Habiro-ring element is "a
   function whose domain is the set of roots of unity", quantum invariants being
   "analytic functions defined on the set of roots of unity". If that holds as
   stated, the substrate anchor `q₀ ≈ 1.10998` (real, `>1`) is **off** that domain
   — so the archimedean continuation this ledger names is not a gap a better
   construction closes, it is a request to leave the object's native domain, and
   the analytic route (state integrals / Faddeev `Φ_q`) is a different literature
   from the Habiro one.

Actionable consequence *if* (2) survives reading: the framework already carries
`Φ_q` (cheat-sheet §4 sorts it against `Li₂^q`), and `Φ_q` is the state-integral
kernel — so the question would become *which* state integral, not how to continue
a Habiro element.

**CONFIRMED (read tier).** Beliakova–Le arXiv:1106.6298 §1 defines
`Ẑ[q] := lim←_k Z[q]/((q;q)_k)` and states verbatim: *"Every element f(q) ∈ Ẑ[q]
can be considered as a function whose domain is the set of roots of unity"*, with
`J_M` evaluating at any root of unity to the WRT value. Dimofte–Garoufalidis
arXiv:1511.05628 §1 defines a quantum modular form on *"the set of complex roots
of unity"* with formal `φ_ζ(ℏ) ∈ C[[ℏ]]` — asymptotics near, not values at
`|q|>1`. Lovejoy–Osburn–Störzer arXiv:2605.15740 (2026) recasts unified WRT as *"an
identity for a q-hypergeometric series at roots of unity"*, covering Hikami's
**Brieskorn** cases — the keystone's own family, still at roots of unity.

**And the mechanism is sharper than "native domain."** An element is
`Σ_k f_k(q)·(q;q)_k`, so `(q;q)_k` decides convergence. Measured at the canonical
q₀ ([`habiro_domain_substrate_anchor_probe.py`](../../computations/probes/habiro_domain_substrate_anchor_probe.py)):
at a 5th root of unity it is **exactly 0 for k ≥ 5** (the sum terminates — that is
*why* the domain is what it is); at `1/q₀ ≈ 0.9009` it converges to `1.109e-6`; at
the substrate `q₀ ≈ 1.10998` it **diverges super-exponentially**, `|(q₀;q₀)_80| ≈
7.3e140`. The `(q;q)_k`-adic completion that makes roots of unity evaluable is the
same one that makes real `q>1` diverge — so continuing a unified-WRT element to q₀
is not a harder evaluation, it asks for something the object does not have.
Scope-(a) on this route; nothing excluded elsewhere, and nothing said about state
integrals.

**LEAD, not a route (do not record it as one).** `1/q₀ < 1` is in the convergent
regime and the framework already threads `q ↔ q⁻¹` (bar-even/odd, the proved
`θ_{λ′}=θ_λ⁻¹`, the Q_β cosh/sinh split). But bounded `(q;q)_k` is **necessary, not
sufficient** — convergence also needs the `f_k`, which nothing here bounds. Needs
a specific Σ(2,3,5) series before it counts.

**ROUTE SELECTED (2026-08-10, all six papers read).** The two candidate routes
separate cleanly, in opposite directions:

* **Habiro / unified WRT — cannot reach q₀, structurally.** Confirmed above, and
  *strengthened* by the newest extension: 2412.04241 (Garoufalidis–Scholze–
  Wheeler–Zagier) still defines elements as "collections of power series at each
  complex root of unity", and the convergence it adds is **p-adic** on
  `{q ∈ C_p : |q|_p = 1}`. On the complex side it says the series are
  "**factorially divergent series over the complex numbers**". The substrate
  anchor is archimedean and real, so this is the wrong analytic world entirely.
* **State integrals — the anchor IS in the domain.** 1411.6062 §1.1 states
  `I_{A,B}(b) = ∫ Φ_b(x)^B e^{−Aπix²} dx` is "an absolutely convergent integral
  ... for b with `b² ∉ ℝ≤0`". Mapping `q₀` through `q = e^{2πiτ}`, `τ = b²` gives
  `b² = −0.0166063414046 i`, purely imaginary ⇒ **converges**
  ([probe](../../computations/probes/state_integral_domain_substrate_anchor_probe.py)).

⇒ **Attack the keystone's archimedean continuation on the analytic/state-integral
side, not the Habiro side.** The corpus already holds the kernel (Faddeev `Φ_q`,
cheat-sheet §4). Caveats that keep this from being more than route selection:
convergence ≠ identification of `W_λ`; the paper's *evaluation* theorem is at
rational `b²` (roots of unity again) and does not transfer to our purely-imaginary
`b²`; and `τ = b²` is the standard convention, inferred rather than quoted.

Carried as a question, NOT a correspondence: the paper's headline 4₁ identity is
`I_{1,2}(1) = (e^{iπ/6}/√3)·2·sinh(V/2π)` with `V` verified to be the corpus's own
`Vol(4₁) = 2·Cl₂(π/3)` (the CAL-2 anchor) to 3.9e-31 — the anchor volume appearing
inside a **sinh**, next to a framework that carries a bar-odd sinh / bar-even cosh
split. At `b=1`, not the anchor, matched to nothing. Anti-numerology applies.

Ordered reading list (all six now read), the domain claim first because everything turned on it:
[math/0605314](https://arxiv.org/abs/math/0605314),
[1106.6298](https://arxiv.org/abs/1106.6298),
[1511.05628](https://arxiv.org/abs/1511.05628),
[1411.6062](https://arxiv.org/abs/1411.6062),
[2412.04241](https://arxiv.org/abs/2412.04241) (Dec 2024 — most likely to have
relaxed the domain restriction, if anything has),
[2605.15740](https://arxiv.org/abs/2605.15740).

Full scoping + what must not be concluded:
[`2026-08-10-keystone-literature-scoping-wrt-domain.md`](../audits/2026-08-10-keystone-literature-scoping-wrt-domain.md).

**Tooling:** `mcp__paper-search-mcp__search_arxiv` returned empty for every query
including the control "knot theory" — broken/blocked, not a null result. Use
`WebSearch` with `allowed_domains: ["arxiv.org"]`.

## Refutations not to re-walk (canonical-no-negative-result discipline)

1. **210 ppb muon via (1,1,1) sign-block / Wedderburn projector** — the correction is O(16 %) (sign-block)
   to ×15 (channel ratio), 6–8 orders too large for the 209.8 ppb gap; the bare `m_e·Vol(4₁)/ℏ_q²` is
   already good to 209.8 ppb. The structural identity `χ^{(1,1,1)}(β_Bor)=1` is exact but magnitude-wrong.
2. **electron block (3,1,1) = colour ℂ³ ⊗ spin ℂ²** — refuted on the central character (spin parity): (3,1,1)
   is an A₅ rep (central +1), ℂ³⊗ℂ² has central −1. dim-6 = chirality T₁⊕T₂, not a tensor.
3. **Reeb-eigenvalue resonance** — the ℓ=1,2 content matches (`c(λ)=ℓ(ℓ−1)`) are non-unique and fail at ℓ=3
   (tau, multi-block). No parameter-free ≥3-anchor resonance.
4. **Cyclotomic-Galois / `Li₃(ζ₅)` period as a keystone "falsifier"** — recorded 2026-06-20 after a fresh
   agent (`claude/kind-ptolemy-acladr`) independently re-derived the cyclotomic-Galois / fifth-root-of-unity
   period angle and mis-aimed it at the keystone coupling as a falsifier. That angle lives on the **period /
   z-Habiro axis**, which the 2026-06-17 sessions-log note flags as **orthogonal to the keystone coupling — "do
   not conflate"**: the z-side completion `varprojlim ℤ[q^±1][z]/(P_n)` (quantum-dilog Φ_q tower) is parallel-
   but-independent of the q-side Habiro/full-Hecke Markov trace. Forcing the period↔knot bridge is exactly the
   **unfalsifiable correspondence-chain the Habiro lead refused**
   ([`2026-06-16-keystone-habiro-coupling-lead-and-ck-exposition.md`](../audits/2026-06-16-keystone-habiro-coupling-lead-and-ck-exposition.md)).
   Inoculation for the next agent: a period-axis cyclotomic-Galois result is **not** an s5-so3 keystone
   constraint; the keystone's single open object is the q-Plancherel-measure geometric-realization problem
   (below), not a period identity. Verify the axis (period/z vs coupling/q) before treating any Galois fact as
   keystone-bearing.
   **Twice-demonstrated recurrence (strengthened 2026-06-20, PR #2506 / bean `wlk9`).** A *second*, independent
   agent (`claude/tender-darwin-sw4zo1`, the #2506 hyperbolic-hurdle audit) re-derived the identical
   cyclotomic-Galois / `Li₃(ζ₅)` angle from scratch and again mis-aimed it at the keystone as a falsifier — with
   no knowledge of the #2517 record (it was 475 commits stale). Two agents re-walking the same dead end within
   one day is exactly the recurrence the canonical-no-negative-result discipline exists to stop; treat this item
   as high-priority inoculation, not a one-off footnote.
5. **Finite-colour Schur–Weyl *multiplicity* → `W_λ`** — refuted 2026-06-22 (PR #2608). After the #2603
   colour-resolution and the #2604 SU(2) row-count split, the tempting next step is "use a higher colour
   ℂ³/ℂ^d Schur–Weyl weighting to land the Plancherel `W_λ`." Foreclosed for **all** `d`: the gl_d
   colour-multiplicity `m_d(λ) = #SSYT(λ,≤d)` (i) has support `{rows≤d}`, missing `W_λ`'s 4-/5-row blocks
   for `d<5`, and (ii) is strongly conjugation-**asymmetric** (`m₅(5)=126` vs `m₅(1⁵)=1`) while
   `W_λ = W_{λ'}` — so no `d` makes it match. `W_λ` is the **symmetric-pairing** (`d_q²`, `d→∞` full
   Hecke) measure, the production/principal-spec `y_λ` is the colour-multiplicity side; the colour functor
   lands the *wrong weight system*. Inoculation: do not re-attempt a finite-colour-multiplicity → `W_λ`
   map. A colored-WRT-*invariant* route (#2604) is not refuted but is **constrained** — it must reproduce
   the conjugation-symmetric Plancherel measure. Audits:
   [`2026-06-22-keystone-wrt-schurweyl-{plancherel-4count,higher-colour-foreclosure}.md`](../audits/2026-06-22-keystone-wrt-schurweyl-higher-colour-foreclosure.md).

## Sessions log

| Date | PR | What landed |
|---|---|---|
| 2026-07-17 | #3822 | **The LR modulus identification is a CORRECTED EXACT IDENTITY (no fit).** The #3703-refocused open piece `\|S_{0λ}^{Σ(2,3,5)}(ζ)\| = d_ζ(λ)/D(ζ)` holds with three derived corrections: (1) **ζ is the fibre root `e^{mπi/5}`** (order 2p₃=10), **Galois-indexed by the flat connection m=1,2** — not the level root ζ_N, not e^{2πi/30}; (2) a **global factor 2** (Ê₈-node normalizer) resp. √2 (folded MTC): `D_Ê₈² = 2·D_MTC²` exactly (the 9-node set folds 2:1 onto the r=5 alcove, node 5→0); (3) the identity lives at the **folded D=2 level** — the McKay coloring does NOT escape the D=2 collapse, it factors through it: `α ↦ χ^{(1,1,α)}` has the SAME fold kernel/signs as `α ↦ [α]_ζ` (exact: χ⁽¹¹⁴⁾=+χ⁽¹¹¹⁾, χ⁽¹¹³⁾=+χ⁽¹¹²⁾, χ⁽¹¹⁵⁾≡0, χ⁽¹¹⁶⁾=−χ⁽¹¹¹⁾). Per-node exact ℚ(√5): `\|A_m(mark)\|·D_Ê₈(ζ^m) = 2·\|[mark]_{ζ^m}\|` at all 9 nodes, both m; core `(10−2√5)(10+2√5)=80`. Amplitudes `A_m(α)=(2/√5)sin(αmπ/5)` parameter-free-extracted (~1%); bonus exact identities `τ_N(4)−τ_N(1)=1+2cos(2π/N)`, `τ_N(3)−τ_N(2)=e^{−6πi/5N}` (machine zero). Split node: electron `[5]_ζ+1 = 1 = \|[6]_ζ\|` — S₅ and 2I dictionaries agree in modulus; muon class folds to `[5]_ζ=0`. A 9-independent-moduli reading at one ζ is (b)-excluded by D(2,3,5)=2 (Fintushel–Stern). **NOT closed:** the `loc_matches` gate and the archimedean q₀-continuation (the generic-q 4-class separation) — unchanged, per #3652/#3681. Lean sorry-free fold algebra: `KeystoneLRModulusFold.lean`. ([audit](../audits/2026-07-17-lr-modulus-identification.md), [probe](../../computations/lr_modulus_identification_sigma235.py)) |
| 2026-07-12 | #3703 | **The framing is a pure phase — observable framing-free for ALL blocks (f=−1 pinned, no fit).** Refines #3701. Since `d_q(λ)=[mark]_q` is real on the unit circle (`[m]_ζ=sin(mφ)/sin(φ)`, SU(2) character), the twist `θ_λ(ζ)=ζ^{c(λ)}` is a pure phase (`|θ|=1`), so the fibre probability `|S_{0λ}·θ_λ^f|²=|S_{0λ}|²=W_λ(ζ)` for **every** block (verified ζ=e^{2πi/7}). Hence the observable `W_λ(q₀)=d_q₀²/D²` (Habiro-continued per #3681) is framing-free for all 7 blocks, not only the electron; the `q₀^{f·c}` residual of #3701 is an amplitude-ordering artifact. Seifert framing pinned **f=−1** (Σ(2,3,5)=−1 surgery on left trefoil; e=−1/30). **Honest refocus:** the open object is the modulus identification `\|S_{0λ}^{Σ(2,3,5)}\|=d_ζ/D` (the deferred colored-Lawrence–Rozansky compute), NOT the framing. ([audit](../audits/2026-07-12-keystone-wlambda-framing-is-phase.md), [probe](../../computations/probes/keystone_framing_is_phase.py)) |
| 2026-07-12 | #3701 | **q₀ residual = the framing monomial `q₀^{f·c(λ)}`; electron block derived outright (no fit).** Since `d_q(λ)=[mark]_q` (#3685) is a global Laurent polynomial (no Habiro completion for the numerator), the entire fibre→observable residual reduces to the framing factor `θ_λ^f=q₀^{f·c(λ)}`. `c(λ')=−c(λ)`, `c=0` iff self-conjugate; the **only** self-conjugate n=5 block is the **electron (3,1,1)** (A₅-split mark-6 node), so `c=0 ⇒ θ_λ^f=1` for **any** framing f ⇒ `bwS0Concrete((3,1,1))(q₀)=([5]_q₀+1)/D≈0.5477` **EXACTLY, no continuation** — discharging the #3681 Habiro-rigidity carrier concretely for the electron block (rigidity trivial; f-independent). Every other block carries the explicit residual `q₀^{f·c(λ)}` (per-block quantified open piece). ([audit](../audits/2026-07-12-keystone-wlambda-q0-framing-residual.md), [probe](../../computations/probes/keystone_q0_framing_residual.py)) |
| 2026-07-12 | #3699 | **McKay value-map identities formalized sorry-free** (`KeystoneMcKayValueMap.lean`): `qFactorial_shape_32` (`d_q((3,2))=[5]_q`) + `qFactorial_shape_311` (`[2]_q·d_q((3,1,1))=[3]_q[4]_q`, the split-electron node, not `[6]_q`). Convention-independent q-factorial hook cancellations; complements the standard-rep `d_q((n−1,1))=[n−1]_q` (#3640). lean-direct EXIT 0, axioms `[propext, Classical.choice, Quot.sound]`. |
| 2026-07-12 | #3685 | **Geometric `W_λ` value map DERIVED: `d_q(λ)=[mark]_q` via McKay 2I↔Ê₈, no-fit.** The open "colour→λ + normalization" step (named by `keystone_colored_sigma235_wrt`, which refuted `[e]_q`) is derived via McKay 2I↔affine Ê₈ (irrep dims = Coxeter marks; Σmarks=30=h(E₈)=P, Σdim²=120=\|2I\|) ∘ A₅⊂S₅ branching. The 4 bwS0 conjugation classes map explicitly (not a count coincidence) to the 4 A₅-factoring McKay nodes (marks 1,4,5,6). **Value map exact at generic q (machine-zero, q₀ & q=1.37): `d_q(λ)=[mark]_q`** for the 3 unsplit nodes — `d_q((5))=[1]_q`, `d_q((4,1))=[4]_q` (=#3640), **`d_q((3,2))=[5]_q`** (new) — deviating ONLY at the A₅-**split** electron node `(3,1,1)`: `d_q=[5]_q+1=[3]_q[4]_q/[2]_q` (not `[6]_q`; the `+1` = the `3⊕3′` split signature). **Resolves the `[e]_q` refutation as exponent-vs-mark mis-indexing** (false-theta support = E₈ *exponents*; value lives on E₈ *marks*). `bwS0(λ)=[mark]_q/D`, single global D, no fit. Colored Lawrence–Rozansky amplitude + q₀-continuation deferred/open; the two q-integer identities are formalize-first Lean targets (balanced-`qInt` convention). ([audit](../audits/2026-07-12-keystone-wlambda-derivation-mckay-e8-route.md), [probe](../../computations/probes/keystone_mckay_e8_valuemap.py)) |
| 2026-07-17 | #3820 | **Colored Lawrence–Rozansky modulus scope-(a) EXCLUDED at the Σ(2,3,5) fibre root (Front 2 of the three-front spec).** Colouring the p₃=5 fibre by a Wilson line α=1..4 multiplies each flat connection by `[α]_k=sin(αkπ/5)/sin(kπ/5)`; exact fifth-root closed forms (flat1 `(1,φ,φ,1)`, flat2 `(1,1/φ,−1/φ,−1)`). **K1** α=1 recovers the unit anchor; **K2** reflection α=4≡1,α=3≡2 ⇒ ≤2 independent moduli/flat — colouring does NOT escape the D=2 vacuum row; **K3** `|[α]_k|≤1/sin(π/5)=1.7013` < growing target ratios `(1,4.11,5.22,6.22)`; **K4** mark 6 > fibre order 5, and `3⊕3′` two-block `2[3]=3.24 ≠ [5]_q₀+1=6.22` ('[6]_ζ vs [5]_ζ+1' decided). **Refines (not contradicts)** the standing 'q₀-continuation deferred/open' note: `[mark]_q₀` (real-q₀, growing) IS the value map; the root-level modular object is D=2/bounded and can only continue to it, not be it. Carrier (if any) = q₀-continued / larger-D family. No fit; Lean `loc_matches` gate stays open. ([audit](../audits/2026-07-17-colored-lr-modulus-scope-a-exclusion.md), [probe](../../computations/probes/keystone_colored_lr_modulus_s013.py)) |
| 2026-07-12 | #3652 | **Geometric `W_λ` three-vector tranche (gate open), no-fit.** (1) q-Bessel `latticePt` structural-index search — REFUTED scope-(a). (2) colored-WRT per-block vs `d_q` — PARTIAL/FAIL scope-(b) narrow: the framed weight `S_{0λ}·θ_λ^{f}` breaks `d_q`'s conjugation symmetry (`θ_{λ′}=θ_λ⁻¹`), only tautological `f=0` proportional. (3) **PROVED sorry-free:** the modular T-matrix `θ_λ=q^{c(λ)}` + chirality law `θ_{λ′}=θ_λ⁻¹` + the signed content-flip `c(λ′)=−c(λ)` (`KeystoneModularTwist.lean`; corpus had only the squared version). **Interlock:** v3 proves the invariant that kills v2. Net: any `W_λ` carrier must be twist-free; framing-cancellation reduces to the archimedean-continuation restatement of `bwS0_eq_hecke` (frontier-sharpening banner above). ([synthesis](../audits/2026-07-12-keystone-wlambda-construction-three-vectors.md)) |
| 2026-07-12 | #3640 | **`d_q((n−1,1)) = [n−1]_q` proved for ALL n** (`KeystoneStandardRepQDim.lean`, generalizes the n=5-only `shape_41`). Hardens the Step-1 WRT-gate refutation (SU(2) `[2j+1]_q` = `d_q` only on the standard rep) from numeric-at-3,4,5 to a theorem. |
| 2026-07-11 | #3594 | **SYT de-dup + RSK-target unification + Identity-I status correction.** #3580's `QOU/BraidKnot/YoungTableauStandard.lean` had duplicated the canonical `QOU.Mathlib.StandardYoungTableau` (#2871) — grepped Mathlib but not the QOU tree. Refactored to reuse `numStandardYoungTableaux`/`partitionShape`/`dimSYT`; kept only the genuinely-new skew type + C8 corollary. The three C8 sorries (`branching_two_one`/`skew_le_straight`/`sum_dimSYT_eq_involution`) are now sibling targets of the canonical `RSKBurnsideHolds` (Identity-I axiom (i)) — **both keystone frontiers share one RSK engine** (P1–P5). Also corrected the stale "Identity I held as `def twoM`" note (it is conditional-proved #2709 + unconditional n=3..12 #2760). ([dedup audit](../audits/2026-07-11-keystone-syt-dedup-rsk-unification.md)) |
| 2026-07-11 | #3580 | **C8 super-exp lower bound PROVED (arithmetic core) + Tier-1 SYT infra.** `KeystoneC8SuperExpBound.lean`: `w_std(k) ≥ k!/(9·I(k))` via Lean-proved Cauchy–Schwarz (`weighted_cs`) + concrete `involutionNumber` + the sorry-free reduction `c8_lower_bound`; only the two SYT identities (A)/(C) carried. `c8_superexp` corollary unconditional modulo three cited RSK sorries. lean-direct EXIT 0. Owner "open s5-so3 gate". No fit, no `W_λ` construction. |
| 2026-07-11 | #3548 / [C8 note](../audits/2026-07-11-keystone-wlambda-superexp-necessary-condition.md) | **New necessary condition C8 (falsifiable, no fit) + μ/e↔binding cross-link:** the multiplicity-weighted branched sum `w_std(k) = Σ_λ W_λ·mult_(2,1)(λ↓H_3) = E_Planch[f^{λ/(2,1)}]` must grow **super-exponentially** (ratios `1.38→2.88` strictly increasing over `k=3..10`, `w_std/2^k` increasing tail → factorial class; exact at q=1, q₀ preserves class). **Independent of C1/C2/C6** (pointwise/unweighted) and the defect cubic (constrains `1−Z`, the *unweighted* sum) — it constrains how `W_λ` distributes over multiplicity-heavy blocks, which the pointwise gates leave free. Any WRT(S³/2I)/`E_q(2)` q-Bessel candidate must pass it. Cross-link: on the binding side this is the provable core of a **GAP-A-3** result — inverting the super-exp `w_std` vs extensive `B∝A` forces the brane-tower **level-selection `k(A)` logarithmic** (`k∝A`/`k∝`bonds falsified scale-free, R²=0.67/0.49 vs log-type 0.88). So one geometric `W_λ` must jointly meet the μ/e gates *and* super-exp growth. Lean target: super-exp lower bound on `E_Planch[f^{λ/(2,1)}]`. Verified exact k≤10; not a closure. |
| 2026-06-26 | (trB/L2 refresh) | lever-1 `tr B` is `[2]_q`-rational: with `s=[2]_q`, `tr B = 3(3s²+2)/(4(s+2))`, `tr B(q₀)=2.6424` (50-dps symbolic+numeric). `det B=1` + non-integer trace ⇒ hyperbolic q-difference connection, **not** `SL₂(ℤ)` topological monodromy. Rank-2 `W` forced by `A₅`-irreducibility of `H^{1,0}(Bring)` (Sage-free). Target restated; Sage/owner-gated. (Salvaged clean part of the stale #2722.) |
| 2026-06-16 | #2352 | S₅↓S₃ backbone + SO(3)↓A₅↪S₅ bridge verified; ing-4/5 close-out (210 ppb **refuted**) |
| 2026-06-16 | #2361 | propagate refutation to the GAP-A-4 doc; ingredient-4 geometric-leg formalize-first prune |
| 2026-06-16 | #2364 | Schur–Weyl: strand fibre forced to colour ℂ³ (spinor kills electron) |
| 2026-06-16 | #2367 | two-Sasakian decomposition; static coupling Schur-forced |
| 2026-06-16 | #2368 | Reeb-eigenvalue resonance **refuted** (numerology-guarded negative) |
| 2026-06-16 | #2370 | canonical coupling = Hopf moment map μ; round-S⁵ colour Reeb transverse; **selection realized by μ** |
| 2026-06-16 | #2373 | Markov-weighting scope: forced `W_λ` + Wu-manifold Sasakian handoff |
| 2026-06-16 | #2369 (sibling) | coordination note: A≥3 `tr_M` compute = algebraic realization of the open weighting |
| 2026-06-16 | #2398 | **derive-attempt:** SU(3)/SO(3) Wu-manifold arena ruled out — spacetime-fixed Schur-centralizer obstruction ⇒ spacetime ⊥ colour |
| 2026-06-16 | #2406 | **correction:** no finite colour-SU(3) arena — production trace is full-Hecke principal specialization, not SU_q(3) ≤3-row (reconciles sibling #2389) |
| 2026-06-17 | #2416 | **Lean:** Δ_λ = chirality sign × Wedderburn magnitude (sorry-free); `deltaSign_mixed` = the PROBE-4 KL-positivity-prune premise machine-checked |
| 2026-06-17 | #2424 | **Lean:** McKay 2I↔E₈ anchors (Σdim²=120, Σmarks=h=30, \|2I\|=4h, dimE₈=8·31) + A₅ branching content (V₁→T₁, V₂→H, V₃→T₂⊕G; (3,1,1) self-conj T₁⊕T₂) |
| 2026-06-17 | #2431 | **Lean:** S₅↓S₃ restriction dimension-consistency for all 7 blocks (the branching backbone, embedding-independent) |
| 2026-06-17 | #2436 | **Lean:** S₃-rotation branching dimension-consistency (ℓ≤4) — completes the dim-check for the `s3RotBranchingMult` table |
| 2026-06-17 | #2442 | **Lean (full Mathlib):** z-Habiro `c_n` localisation pinned — `eulerCoeff` (Euler `b_n` in `S^{-1}ℤ[q^±1]`, `S=⟨1-q^{-j}⟩`) + `braneMonic_coords_unique` (coordinates unique); analytic↔algebraic identification stays open |
| 2026-06-17 | (this PR) | **Lean (full Mathlib):** z-Habiro `braneMonic_coords_exist` — monic basis spans `R[X]_{≤n}`; with #2442's uniqueness, cyclotomic coordinates are a bijection `R[X]_{≤n} ≅ R^{n+1}` staying in the localised `R` (item 2(i) base-ring half) |
| 2026-06-17 | (coord note) | **z-Habiro on main is ORTHOGONAL to the keystone coupling — do not conflate.** The z-Habiro Lean work (#2417-era: `ZHabiroCompletion`, `zHabiroLimit`, `cyclotomicPartialSum_isCauchy`) builds the **z-side** completion `varprojlim ℤ[q^±1][z]/(P_n)` for the quantum-dilog Φ_q truncation tower. The keystone coupling is the **q-side** Habiro element (full-Hecke Markov trace = WRT(S³/2I) = Lawrence–Zagier). These are parallel-but-independent completions; bridging them needs a simultaneous (q,z)-bicompletion, which the z-Habiro file itself flags "construction open." No fit-free Lean bridge exists yet — forcing one is the unfalsifiable correspondence-chain the Habiro lead (`2026-06-16-keystone-habiro-coupling-lead-and-ck-exposition.md`) explicitly refused. The keystone coupling stays OPEN. |
| 2026-06-20 | (this PR) | **Construction (mechanism, no fit):** the geometric W_λ index = **Beasley–Witten Seifert–CS localization on S³/2I** (Reeb=Seifert S¹). The RT/Verlinde Plancherel weight `d_q²/D²` it produces meets all of C1–C7 (arithmetic verified at q₀,n=5). **Resolves C1**: the geometric normalization is `D²=Σd_q²` (Σ=1 true Plancherel), not `[n]_q!` (Σ=0.98222); gap = `D²/[n]_q!=0.98222`. Reduces the owner-gated build to instantiating a published localization; residual = MTC-matching + Lean Reeb=restriction. 210 ppb untouched (refuted). |
| 2026-06-20 | #2520 | **Scope (consumer side, no fit):** what the mass-ratio needs from the W_λ frontier. Since #2516/#2519 prove the knot layer is null on the generation difference, the geometric frontier carries the **entire O(1) generation skeleton** (consumer weight `y_(3,2)/y_(3,1,1)=3.68` at q₀) and **none** of the 210 ppb fine shift (2.1e-7, anchor artifact). Forward necessary condition complementing producer-side C1–C7; no edit to producer docs. |
| 2026-06-20 | #2519 | **Probe (no fit):** the (2,1)/h⁴ cancellation is **robust to q-deformation**. Generic-q Hecke branching H₃⊂H₅ carries classical multiplicities → `χ_μ^H5(β)=Σ m·χ` exactly (max |Δ|=8.9e-16) and `χ_(3,1,1)−χ_(3,2)=χ_(1,1,1)=1` identically, h-indep up to h⁴≈0.9. Closes the q-deformed-Wenzl escape #2516 left at the **character** level — only surviving μ/e asymmetry is the O(1) `W`/`y` block-weight ratio (#2488 frontier). |
| 2026-06-20 | #2516 | **Probe (no fit):** ran the functor-resolution §4 object via `pyhecke_native` (built in-sandbox, #2511) — the H₃ Borromean Markov-trace shift between muon `E_(3,2)` and electron `E_(3,1,1)` projectors via the classical `S₅→S₃` branchings. The h⁴-bearing `(2,1)` block enters both with the **same** multiplicity 2 (classical, q-indep) → **cancels exactly** in the μ/e difference (6.9e-18). Classical-multiplicity baseline is **null**; residual split is the `(1,1,1)` sign channel (h-indep, ~1.5e-2). Sharpens the W_λ frontier (#2488): the q-deformed `W_λ = d_q(λ)²/[n]_q!` weights are **necessary**, not optional — pure multiplicity counting cannot produce a generation shift. |
| 2026-06-20 | #2517 | **Lead + inoculation:** (a) §Refutations item 4 — cyclotomic-Galois / `Li₃(ζ₅)` period is period-axis, NOT a keystone falsifier; (b) **q-heat-kernel / q-Bessel(2nd-kind) geometric-realization lead** — precheck found `W_λ=d_q²/[n]!` is **sub-normalized** (`Z=0.98222` at q_0, P1 fail; symmetry P2 + audit P3 pass); the mass defect `1−Z` is the geometric quantity to explain. Bridges the existing q-Bessel infra (2026-06-13) to the keystone target. `2026-06-20-keystone-qbessel-heat-kernel-lead.md` + `scripts/keystone_qbessel_plancherel_precheck.py`. NOT a closure. |
| 2026-06-20 | #2506 | **Inoculation + corpus trace:** (a) §Refutations item 4 strengthened — the cyclotomic-Galois falsifier was re-walked a **second** time independently (`claude/tender-darwin`, #2506), now a twice-demonstrated recurrence; (b) pieces-1–3 corpus-object trace consolidated into [`docs/audits/2026-06-20-s5so3-pieces-1-3-corpus-trace.md`](../audits/2026-06-20-s5so3-pieces-1-3-corpus-trace.md) — every settled ingredient mapped to its verified `.md`/`.lean`/checker source. No new math; reporting only. |
| 2026-06-20 | #2528 | **Probe (no fit) — binding-side target for the Step-1 gate:** wired the owner-gated deuteron `f_pn = 0.588` (reproduces AME `B(²H)` exactly) against the gate's `W_λ = d_q²/[n]_q!`. The pn std-channel block is the standard rep `λ=(2,1)` at `n=3`; gate `W_(2,1)=0.661` UNDER-binds (E 1.74), the bare std channel `0.395` OVER-binds (E 3.89) → required `0.58776` (E 2.2246) is **strictly bracketed** `0.395 < 0.588 < 0.661`. REFUTE the naive direct-weight map; algebraic `W_λ` does not land 0.588 but brackets it. Hands the geometric `W_λ` (WRT(S³/2I)) a sharp **second** binding-side target alongside the m_τ tower: any index reproducing `W_λ` must land `f_pn` in `(0.395, 0.661)`. Harness `deuteron_fpn_from_Wmap` consumes any future geometric `W_λ` unchanged. `2026-06-20-deuteron-fpn-wlambda-wiring.md`. |
| 2026-06-18 | #2480 | **Lean (formalization fix):** de-vacuify `BringFiberAction` — remove the provably-false `respects_conjugate` (angle sign-flip) + vacuous `hits_five_conjugacy_classes : True` + trivial instance; correct the fibre-map domain to the 5 A₅ irreps (new `A5Irrep` + `conjugate_same_a5_irrep`), substantive `five_distinct_classes`. Per `2026-06-13-bring-fiber-action-falsification.md`. Formalization correction, **not** a closure — the geometric map stays open. |
| 2026-06-22 | #2605 (re-land #2500) | **colour-arena block-count THEOREM** (`ColourArenaBlockCount.lean`, sorry-free): the colour-`ℂ^N`-missed Wedderburn blocks contain an injected copy of *every* partition of size `n−(N+1)` (`appendUnitRows`/`missedEmbedding`) ⇒ missed-block count **unbounded + monotone** in `A` (verifier `colour_arena_missed_block_count.py`, B1–B5). Upgrades #2406's *weighted* 3.4%→6.0% from data points to a **block-count theorem**; gives **C6 (full support)** quantitative teeth (no finite-`N` Sasakian). Weighted-share monotonicity stays **empirical** (q₀/braid-dependent). Audit `2026-06-19-colour-arena-block-count-theorem.md`. |
| 2026-06-22 | #2605 (re-land #2500) | **combiner branching completeness / non-degeneracy** (`CombinerBranchingCompleteness.lean`, sorry-free): `exists_subpartition_of_size` — every `λ⊢n` (`n≥k`) has a sub-partition of size `n−k`, so `interface_blocks` returns ≥1 child for every block and the operator combiner drops none (Frobenius reciprocity; verifier `combiner_branching_completeness.py` over splits 6/9/12, self-contained). Formalizes the **dual** non-degeneracy of the already-corpus-established per-λ completeness — a correctness guarantee, not a new derivation. Audit `2026-06-19-combiner-branching-completeness.md`. |
| 2026-06-22 | #2605 (re-land #2500) | **C2 chirality involution formalized** (`KeystoneChiralityInvolution.lean`, sorry-free): facets of C2 (`W_λ=W_{λ'}`) — content negates under transpose `c(j,i)=−c(i,j)`, electron `(3,1,1)` self-conjugate (`c=0`, central A₅ rep `T₁⊕T₂`), `[2]↔[1,1]` flip. The strongest pruning lever now machine-checked at the cell/example level; global `W_λ=W_{λ'}` stays cited + witnessed. |
| 2026-06-22 | #2584 | **Probe (no fit) — q-deformed projector shift REFUTED:** E_λ-projected H₅ Markov trace `T_g = y_{λ_g}^{H5}·χ^{λ_g}(ι(β_Bor))` gives non-null `δ = T_μ − T_e = 0.2075` (the q-deformed home-block weighting breaks the (2,1) symmetry classical multiplicity preserved) but 6–7 orders too large + **bar-mixed** → not the 210 ppb mechanism. Markov-trace surface (multiplicity / home-block weight / projected trace) **exhausted**; branching cross-check to 9.6e-50. |
| 2026-06-22 | (audits) | **Reframe + route reduction (no fit):** at real `q₀ > 1` no compact Sasakian / MTC hosts `W_λ` → arena = non-compact `SU_q(2) → E_q(2)` Hahn–Exton q-Bessel contraction; sharpened object = colored Σ(2,3,5) WRT q-series via the `q ↦ q⁻¹` bar involution. `Ψ(1/q₀) = 2.32958` operational (one number, **not** the λ-family — no numerology match). On-main (level,chirality) Lean gives class *separation*, not a mass functional. Falsifiable `q₀`-free sub-target `144·C(n) = −n(n−1)(2n−13)` Lean-proved (`WLambdaDefectClosedForm.lean`); the one carried input **Identity I** `M(n) = n(3n−1)/2` needs SYT/hook-length infra not in Mathlib. Docs: `2026-06-22-keystone-{modular-category-identification,habiro-wrt-s3-2i,geometric-level-route-reduction,geometric-angles-preflight}.md`. |
| 2026-06-22 | `fe3a83d6b4` (capstone) | **Schur–Weyl dual-sides — deflationary capstone (no fit):** WRT↔`W_λ` is a Schur–Weyl **DUALITY**, **not** an equality. Corpus `W_λ` = Hecke (S_n-side) hook-content `d_q(λ)`; WRT/Poincaré modular data = SU(2) (V_λ-side) `[2j+1]_q`. They DIFFER (muon (3,2): `[5]_q=5.22` vs `[2]_q=2.01`; coincide only at (4,1)) ⇒ paired, **not** equal. A direct `WRT=W_λ` equality is a category error; the Poincaré sphere is the icosahedral *selector*, `W_λ` the dual S_n-side q-dims. Deflationary terminus of the WRT line — structural gains, **no closure / no mass prediction**; reinforces the banner's tautology-risk read. Doc: `2026-06-22-keystone-schurweyl-dual-sides.md`. |
| 2026-06-23 | [#2634](https://github.com/litlfred/qou/pull/2634) | **Identity I content decomposition (no fit) — sharpens the line-133 "needs SYT/hook-length infra" note.** The one carried RT input `M(n)=n(3n−1)/2` (to the falsifiable defect `144·C(n)=−n(n−1)(2n−13)`) factors as `binom(n,2)+n²` via **(A)** per-partition `Σ_c h_c²=Σ_c c(c)²+n²` (a single-Young-diagram fact, no dims; exhaustively verified — all 4507 partitions, `n≤22`) + **(B)** the Jucys–Murphy / Plancherel content-square mean `binom(n,2)` (**proved**: `Σ_k X_k²` central, identity-coeff `Σ(k−1)`). Net: the hard **Frame–Robinson–Thrall hook-length FORMULA is OFF the critical path** — residual fill is (A) `YoungDiagram` defs + a combinatorial identity, (B) standard `ℂ[S_n]` Wedderburn/JM (the SYT-*dimension* part of line 133 stands; the *formula* does not). Lean `twoM_content_decomposition` sorry-free (lean-direct exit 0). Docs: `2026-06-23-keystone-identity-I-content-decomposition.md`. |
| 2026-06-24 | [#2655](https://github.com/litlfred/qou/pull/2655) | **Identity-(A) PROVED sorry-free for ALL partitions (closes the (A) half of the line-135 residual fill).** Per-partition `Σ_c h_c² = Σ_c c(c)² + n²` is now Lean-proved for every weakly-decreasing partition (was exhaustive-only `n≤22`) — **merged to main**, superseding the prior `fd724f18` length-≤1 partial. Self-contained `List ℕ` model (no Mathlib `YoungDiagram`): hook-square expansion `H²=P²+Q²+1+2PQ−2P−2Q` → nine cell sums → row forms via reflection / the Fubini cell-transpose / K-moment + λ- and j-weighted min-sums; the `+n²` is the λ-weighted min-sum residue. **Residual for the full carried `twoM` (Identity I) is now ONLY (B)** — the Plancherel content-square mean `binom(n,2)` + `Σ_λ dim(λ)²=n!` (the SYT-*dimension* / `ℂ[S_n]`-Wedderburn infra of line 133 still stands; the (A) combinatorial half is DONE). **Wiring caveat:** (A) is per-partition; `WLambdaDefectClosedForm.twoM` is the *Plancherel-weighted* `M(n)`, so connecting (A) to `twoM` still needs the (B)/`Σdim²=n!` infra — (A) firms the per-partition step, not the weighted mean. `IdentityIContentDecomposition.lean` sorry-free (lean-direct exit 0). **Dedup:** sibling #2689 is a *full* alternative (A) proof (`cellSum_swap`+`abel_tri`, six reduction lemmas) with **no** keystone-consumer delta (3 files = bean + Identity proof + audit doc) → fully superseded by #2655, advised to close; #2700 (`YoungDiagram` scaffold, still sorry'd) closed as superseded. Docs: `2026-06-23-keystone-identity-I-content-decomposition.md`. |
| 2026-06-24 | [#2709](https://github.com/litlfred/qou/pull/2709) | **(B) Plancherel mean made conditional-rigorous (§3b-cond, merged).** `IdentityIPlancherelConditional.lean`: `class PlancherelSnData n` axiomatises the two standard facts the pinned Mathlib lacks — (i) `Σ_λ dim²=n!`, (ii) the JM/OV content-square mean `2·Σ dim²·Σc²=n(n−1)·n!`. `two_sum_dim_sq_hooks` proves Identity I `2·Σ_λ dim²·Σ_c h_c² = n(3n−1)·n!` from (i)+(ii)+the proved (A); `twoM_eq_plancherel_hook_sum` wires it to `WLambdaDefect.twoM`. Non-vacuity instance `PlancherelSnData 2` decide-checked. So `twoM` (Identity I) is no longer a bare carried `def` — it's a theorem modulo two named axioms. Companion scope doc `docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md` plans the multi-PR Specht/JM build to discharge them (honest: rigor hygiene, not frontier). Lean sorry-free (lean-direct exit 0). |
| 2026-06-24 | [#2717](https://github.com/litlfred/qou/pull/2717) | **Step-1 gate RUN (no fit) — SU(2)/WRT(S³/2I) does NOT reproduce `W_λ`; full-Hecke arena forced.** Ran the #2503 gate systematically at n=3,4,5 (was n=5 spot-check only, #2608): compares SU(2)-side `[2j+1]_q` to S_n-side `d_q(λ)` per block. **(b) structural exclusion of the SU(2) sub-route**, two grounds: COVERAGE — all ≥3-row blocks (incl. electron `(3,1,1)`) are outside the GL₂ Schur–Weyl image, no SU(2) weight (rigorous form of #2406); VALUE — `d_q=[2j+1]_q` ONLY on the standard rep `(n−1,1)` ∀n (both `=[n−1]_q`), sharpening #2608's single-point `(4,1)` to the `(n−1,1)` family. ⇒ geometric index must live full-Hecke side (the open object is **unchanged**, just the SU(2) branch pruned). Normalization (owner Q): per-block ratios within fixed n are normalization-invariant; only `Z(n)` (defect `1−Z(n)`) is sensitive → the defect is the fixed falsifiable content; `Z(5)=0.98222` reproduced. Docs: `2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md`. |
| 2026-06-24 | [#2727](https://github.com/litlfred/qou/pull/2727) | **SU(2)-route foreclosure machine-checked + full-Hecke program scoped.** (b) `Su2SchurWeylForeclosure.lean` (sorry-free): `gl2_image_eq_le2row` (GL₂ Schur–Weyl image = `{(5),(4,1),(3,2)}`), `electron_not_in_gl2_image`, capstone `su2_index_ne_wlambda` (any GL₂-supported index ≠ any `W` nonzero on `(3,1,1)`) — the prose/Python foreclosure of #2406/#2608/#2717 now Lean-proved as a **(b) structural exclusion** (row-count invariant; abstract codomain, no q₀). (c)+(d) `docs/scope/2026-06-24-keystone-fullhecke-geometric-index-program.md`: the multi-PR full-Hecke geometric-index program (phases G1–G4 on #2524's Beasley–Witten mechanism; falsifiable targets defect-cubic / `a_D=lw` / `f_pn`-bracket / conjugation-symmetry; foreclosed sub-routes catalogued; **(d)** Bring/Jacobian sub-lead cites #2710/#2722 under a STRICT numerology guardrail — formalize the monodromy *operator*, never fit `τ=2.6424`). Honest: rigor frontier, not a new prediction; the open full-Hecke object is **unchanged**. |
| 2026-06-24 | [#2704](https://github.com/litlfred/qou/pull/2704) | **Residual (ii) DISCHARGED (Lean, no fit):** `Reeb = Res^{S₅}_{S₃}` scaffold formalized sorry-free + axiom-free (`S5SO3FiberAction.lean`: `s3SignTwist`, `restriction_intertwines_conjugation` = `Res(λ')=s3SignTwist(Res(λ))` ∀λ⊢5, `std_irrep_conjugation_fixed` = the `(2,1)`/h⁴-carrier multiplicity is conjugation-fixed, capstone `reeb_eq_restriction_scaffold [BringFiberAction]`). The *algebraic* restriction-commutes-with-conjugation identity only; conjunct (i) still **uses** `BringFiberAction` (geometric map stays open). Residual (i) (MTC-matching) stays owner-gated; **210 ppb stays refuted**. Audit `2026-06-24-keystone-reeb-restriction-lean-formalization.md`. |
| 2026-06-24 | [#2744](https://github.com/litlfred/qou/pull/2744) | **Falsifiable target (1) PINNED EXACTLY (no fit, q₀-free):** cross-checked the `W_λ` defect cubic `C(n) = −n(n−1)(2n−13)/144` (`WLambdaDefectClosedForm.lean`, from Identity I) against the **directly-computed** `1−Z(n)=1−Σ_λ d_q²/[n]_q!` for n=2..10 via Richardson `h=q−1/q→0` (60 dps). Empirical small-h coefficient matches the closed form to **<4e-14** ∀n, **n=7 sign flip identical** (empirical 7 = closed-form 7). Closes the loop the empirical defect script (`keystone_wlambda_Z_defect_n_scaling.py`) left open — it disclaimed a closed form, having refuted a *different* (hook-moment) ansatz; the Identity-I cubic is the real one. Hardens phase-**G2** gate from "Lean derivation" to "exact number cross-checked against direct `W_λ` compute". **Plus a SECOND target:** the sub-leading h⁴ coefficient `D(n)` is *also* an exact degree-6 polynomial — `D(n)=n(n−1)(−100n⁴+1472n³−5273n²−203n−828)/1036800` (`1036800=50·144²`), Taylor-extracted (method-validated: h² coeff reproduces exact `C(n)` to 0.0; Δ⁶ constant to ~1e-120; held-out validated n=9,10). Both `C(n)` and `D(n)` carry the `n(n−1)` factor (vanish for the single-box partition). So G2 now gates on **two** q₀-free polynomial targets (2nd + 4th heat-kernel coeff). `D(n)`'s closed form is now **partially Lean-formalized** (`WLambdaDefectSubleadingD.lean`, sorry-free, lean-direct exit 0: factored↔expanded `ring` identity confirming the witness coeffs, `n(n−1)` vanishing, `1036800=50·144²` + the `144^k` denom ladder, and the `1036800·D(n)` value table n=2..10 incl. held-out 9,10); the *derivation* of `D(n)` from the defect stays deferred — parallel to `C(n)`'s general-`n` Identity I — since the `h⁴`-order moment collapse is not yet symbolic (`D(n)` was numerically Taylor-extracted + interpolated). **And a LADDER:** the h^{2k} coefficient `c_{2k}(n)` is polynomial of degree **3k** (C deg 3, D deg 6, E deg 9; each held-out validated), denominator `m_k·144^k` (m_k∈{1,50,7350}) — so the index's *entire* heat-kernel expansion is polynomial-in-n (unbounded target family, not just two). Expected from Plancherel-moment / Kerov-polynomial theory; QOU content = the sharp `3k` ladder + `144^k` denom. Degree-3k law is a CONJECTURE (k≤3 evidence). Probes `keystone_wlambda_defect_cn_closedform_crosscheck.py` + `keystone_wlambda_defect_dn_subleading.py` + `keystone_wlambda_defect_coeff_ladder.py` + witnesses; audit `2026-06-24-wlambda-defect-cn-closedform-crosscheck.md`. |
| 2026-06-25 | [#2794](https://github.com/litlfred/qou/pull/2794) | **C2 conjugation symmetry PROVED in the genuine q-model — `d_q(λ)=d_q(λ′)` sorry-free (Lean, no fit, q₀-free):** the keystone's necessary condition C2 (the q-Plancherel weight `W_λ=d_q(λ)²/[n]_q!` is **chirality-blind**, `W_λ=W_{λ′}`) is now machine-checked at the **global q-dimension** level, not just the cell/example level (#2605) or the `q=1` Frame–Robinson–Thrall dimension. Culminates a three-PR transpose-invariance build: **#2778** (Σ-core — squared-content `Σc²` and squared-hook `Σh_c²` sums transpose-invariant, via the `colLen`-duality `cell_fubini` + the `colLen (conj l) c = λ_c` involution), **#2785** (`q=1` capstone `dimHLF_conj`: `f^λ=f^{λ′}` from `prodHooks_conj`+`sz_conj`), **#2794** (genuine `qDim_conj`: `qDim q (conjugate λ) = qDim q λ`). The genuine q-version **bridges** the two partition models rather than rebuilding duality: `conjugate_eq_conj` (the `QPartitionCombinatorics` `Partition.conjugate` = the merged `colLen`-conjugate on sorted λ), `hookLength_eq` (`Partition.hookLength` = the `colLen`-hook `(λ_i−j)+(colLen j−i)−1` via a `leg_count` take/drop/filter argument), `qDim_eq_prod` (`qDim`'s nested `foldl` = a `Finset` double product), then `qHookProd_conj` (the `qBracket`-weighted hook product is transpose-invariant) + `sz_conj` ⇒ `qDim_conj`. So C2 is no longer cited/witnessed but **Lean-proved for the actual q-weight** at any real q. **Weight-level capstone:** `qPlancherelWeight q λ := d_q(λ)²/[|λ|]_q!` is defined and `qPlancherelWeight_conj` proves the keystone's literal C2 statement **`W_λ = W_{λ′}`** directly (corollary of `qDim_conj` + `sz_conj`). `#print axioms qDim_conj = [propext, Classical.choice, Quot.sound]` (no sorryAx/custom axiom); transpose combinatorics in `ℕ`, q-dimension in `ℝ`. The remaining keystone object (geometric `W_λ` realization / defect cubic) is **unchanged** — this firms the *necessary condition*, not the open geometric index. `KeystoneC2{ContentTranspose,DimTranspose,QDimTranspose}.lean`. |
| 2026-06-25 | [#2760](https://github.com/litlfred/qou/pull/2760) | **Identity I unconditional at n=3..12 + defect-coeff grounding (Lean, no fit):** the two `PlancherelSnData` axioms (i) `Σ_λ dim²=n!`, (ii) the JM/OV content-square mean were already kernel-`decide`-verified for `n≤12` in `IdentityIContentDecomposition` (`dim_validated_le12`/`idB_verified_le12`) but never instanced — so #2709's Identity I carried the class hypothesis everywhere. Wired them into explicit `PlancherelSnData {3,…,12}` (`dim:=dimHLF`, both axioms by `decide`), collapsing `twoM_eq_plancherel_hook_sum` to **unconditional** at **every `n=3..12`** (incl. deuteron `n=3`, keystone `n=5`, **defect sign-flip `n=7`**). So the keystone's carried Identity I (`WLambdaDefect.twoM`, the input to the falsifiable defect cubic `144·C(n)=−n(n−1)(2n−13)`) rests on proved inputs through `n≤12`. **Plus (option 2):** `n144C_eq_twelve_plancherel` / `defect_closedform_plancherel` ground the keystone defect coeff `n144C` (built from the carried `def twoM`) directly in the genuine Plancherel squared-hook sum, generic in `[PlancherelSnData n]` — so the defect cubic incl. the n=7 sign flip is grounded in real S_n rep theory, not a `def` (the Lean complement to #2744's numerical cross-check). Capstones `twoM_plancherel_{three..seven}`; `#print axioms` = `[propext, Classical.choice, Quot.sound]`. General-`n` stays the multi-session P1–P5 infra program (`docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md`). `IdentityIPlancherelInstances.lean`. |
| 2026-06-25 | [#2811](https://github.com/litlfred/qou/pull/2811) | **Geometric `W_λ` tranche — the tractable slices around the owner-gated G1 (Lean, no fit).** The hard core **G1** (the differential-geometric S³/2I Seifert–CS equivariant-index construction) stays owner-gated/out-of-scope; this PR lands three on-target pieces. **(B) G2 falsifiable gate** (`KeystoneG2Gate.lean`, sorry-free): the program's decisive gate — a candidate index's cleared 2nd heat-kernel coefficient `a₂(n)` must equal the proved cubic `n144C` — formalized as `PassesDefectGate` with **teeth**: `defectGate_unique` (no free constant), `defectGate_forces_cubic`, and `defectGate_forces_sign_flip` (passing ⇒ `a₂ 6 > 0 ∧ a₂ 7 < 0`, the falsifiable **n=7 discriminant** any geometric index must exhibit); `canonicalCandidate_passes` (satisfiable, non-vacuous). Records that target-4 (per-λ `W_λ=W_{λ′}`, #2794) is **independent** (a summed-defect match ≠ per-λ symmetry). **(A) de-vacuify `Cl3Zeta5GeometricRealization`** (bean 5e79/T1): the §3b class carried a *free* `cl3Zeta5 : ℝ` (vacuous `exists_realization`); re-anchored to the **proved** K=5 orbit-sum `Cl₃(2π/5)+Cl₃(4π/5)=−(24/25)ζ(3)` (`realize_orbit_sum` field; `realize_orbit_sum_eq` sorry-free). Residual flagged not faked: no closed Clausen `Cl₃` value in infra (Mathlib gap). **(C) Bring W-plane monodromy** (`BringWPlaneMonodromy.lean`, sorry-free; §(d), numerology-guarded): `unimodular_two_recurrence` proves `det M = 1 ⇒ M² = (tr M)·M − I` — so the depth-2 recurrence kernel `x²−τx+1`'s monic/unit-constant form is **forced** by unimodularity (Cayley–Hamilton, τ = tr M), the *operator-level* content, **never** the value `τ≈2.6424`; `BringWPlaneMonodromy` (§3b-cond class) carries the open geometric identification. All lean-direct EXIT 0 (B/C sorry-free; A one §3b conjectural sorry). G1 unchanged. `docs/workplans/2026-06-25-keystone-geometric-wlambda-tranche.md`. |
| 2026-06-26 | #2819 / #2825 / (f_pn) | **Falsifiable-target gate suite completed (Lean, no fit) + G1-framing correction + sibling coordination.** Extends the #2811 gate work across the program's falsifiable targets. **#2819** (merged, `BringWPlaneMonodromyTower.lean`, sorry-free): the depth-2 SL₂ **power-trace tower** of the Bring monodromy matrix — `unimodular_pow_recurrence` (`M^{n+2}=(tr M)·M^{n+1}−Mⁿ`) + `powTrace_recurrence` (`t_n:=tr(Mⁿ)` obeys the Chebyshev depth-2 *linear* recurrence). The Lean grounding of *why* the depth-2 SL₂ is only the `n≤4` effective fit (linear ⇒ exponential, vs the super-exponential global `a_D=lw`); scope-(a), complements the merged sibling #2800 (`BindingHyperbolicRecurrence`) + #2822 (z2bn: `a_D` = q-involution number). **#2825** (merged, `KeystoneG2LadderGate.lean`, sorry-free): the **full C/D/E heat-kernel ladder gate** — `PassesLadderGate` (match `n144C`/`n1036800D`/`n21946982400E` at every order), `ladderGate_subsumes_G2`, `ladderGate_forces_vanishing` (the `n(n−1)` factor at every order), `ladder_clearing_factors` (the `m_k·144^k` law). **(f_pn)** `KeystoneFpnBracket.lean` (sorry-free): **target-3**, the deuteron `f_pn ∈ (0.39479…, 0.66067…)` bracket gate — `PassesFpnBracket` + `ame_strictly_bracketed` (the AME-exact `0.58776` strictly inside) + non-degeneracy. Archimedean (bounds q₀-derived from the algebraic `W_(2,1)` — lower = LP-dual `a_K/R` ratio, witness `a-K-via-lp-dual`; cited, **not** Lean-derived). So the program's falsifiable targets are now Lean gates: **(1)** defect cubic + ladder (#2811/#2825), **(3)** `f_pn` bracket (this), **(4)** conjugation `W_λ=W_{λ′}` (#2794); **(2)** `a_D=lw` is the sibling z2bn line (#2800/#2822). **G1-framing correction:** G1 (the S³/2I Beasley–Witten DG build, live in **#2524**) is owner-**authorized** (2026-06-19 narrow reversal), **not** owner-gated — the blocker is research-level DG, not authorization; the gates here are the machine-checkable spec #2524's construction must pass (coordination intent posted on #2524 + #2822). |
| 2026-06-29 | (coordination + assist; [#3079](https://github.com/litlfred/qou/pull/3079) / [#2986](https://github.com/litlfred/qou/pull/2986)) | **Identity-I tractable path funnels to ONE Mathlib lemma — race de-conflicted (no fit).** Corpus sweep of the SYT hook-length cone: the *entire* general-`n` Frame–Robinson–Thrall HLF (`numSYTenum_eq_dimHLF`, the carried RT input to the falsifiable defect cubic via Identity I) is now isolated — by [#3079](https://github.com/litlfred/qou/pull/3079) (det_vandermonde route, owner-preferred: `det_vandermonde` is cached, `Mathlib.LinearAlgebra.Lagrange` is not) — to the single lemma `SYTVandermonde.cof_mul_vWeight : cof β i · vWeight β i = (vandermonde β).det` (the Vandermonde cofactor product-split). `powSum`, `interp_leadingCoeff`, the (i) hook side, the (B) corner-deletion bijection ([#2986](https://github.com/litlfred/qou/pull/2986), sorry-free), and the whole composition are sorry-free *given* it. **Dedup:** [#2986](https://github.com/litlfred/qou/pull/2986)'s hand-rolled Lagrange `interp_leadingCoeff` is superseded by [#3079](https://github.com/litlfred/qou/pull/3079)'s det version (both reduce to the same Vandermonde fact); advised [#2986](https://github.com/litlfred/qou/pull/2986) keep its (B)+composition+`decide` n≤7 backstops and yield (A) to [#3079](https://github.com/litlfred/qou/pull/3079) (comments on both). **Assist (no duplicate commit):** verified against restored `v4.24.0` oleans (lean-direct EXIT 0) the reindex sub-lemma `(vandermonde β).submatrix i.succAbove (Fin.last k).succAbove = vandermonde (β ∘ i.succAbove)` + `Fin.card_Ioi i = k − i`, and handed [#3079](https://github.com/litlfred/qou/pull/3079) the full API-matched reduction (peel outer at `i` via `Fin.prod_univ_succAbove`; per-row `Ioi (σ a)` image split; sign close-out `(-1)^{i+k} = (-1)^{k−i}`). **CLOSED + MERGED TO MAIN same session** (`00bd7995`, 2026-06-29 14:57): [#3079](https://github.com/litlfred/qou/pull/3079) landed `cof_mul_vWeight` sorry-free (commit `8d4fd10`) and **merged**, so the keystone Identity-I bottleneck is now **on `main`**; I (a) **independently re-proved the identical statement from scratch sorry-free + axiom-clean** (structurally convergent — same outer peel / per-row split / sign argument), and (b) **independently compiled #3079's `SYTVandermondeKeystone.lean` on a clean restored-olean env** (lean-direct EXIT 0; `cof_mul_vWeight` + `interp_leadingCoeff` `#print axioms` = `[propext, Classical.choice, Quot.sound]`, no `sorryAx`/custom). So the **entire tractable Identity-I path → the falsifiable defect cubic now rests on a verified, axiom-clean lemma** (two independent formalizations agree). Geometric residual (i) unchanged (live in [#3059](https://github.com/litlfred/qou/pull/3059)). No fit, nothing wired. |
| 2026-07-02 | [#3193](https://github.com/litlfred/qou/pull/3193) / [#3220](https://github.com/litlfred/qou/pull/3220) (both merged) | **Abstract (unlabelled) form of `PlancherelSnData` (i)+(ii) PROVED sorry-free (Lean, no fit).** `IdentityBWedderburn.identityB_via_wedderburn_unconditional`: for `ℂ[Sₙ]` there exist Wedderburn block data `(N,d,ω)` with `∑dᵢ² = n!` **and** `∑dᵢ²·ωᵢ = n!·binom(n,2)` — the generic semisimple trace identity (Artin–Wedderburn `exists_algEquiv_pi_matrix_of_isAlgClosed` + `Matrix.center_eq_range` Schur + a Pi-trace decomposition; **no Sₙ-specific OV data**), evaluated on the regular-rep trace `trace(mulLeft C₂) = n!·binom(n,2)`. The one classical input — **Jucys centrality `C₂ = ∑ₖ Xₖ² ∈ Z(ℂ[Sₙ])` — is machine-checked** (`IdentityBCentrality`: the coefficient of `C₂` is a class function — `binom(n,2)` at `1`, exactly `1` at each 3-cycle via the `k=max(supp σ)` unique-triple count, `0` elsewhere — plus general `MonoidAlgebra` class-function⇒center helpers, reusable). `#print axioms` = `[propext, Classical.choice, Quot.sound]` on the whole chain (#3220 closed the last sorry, the 3-cycle count). **Sharpens the P1–P5 program:** the residual content of the two class axioms is now exactly the **partition labelling** of the abstract blocks (blocks ↔ `λ⊢n`, `d = #SYT`, `ω = Σc²`) — the brick-5 OV cores (`seminormalVector_data_exists`, `exists_indep_seminormal_family`) — **not** the trace identity / block / center machinery, which is done. Cross-refs wired into `IdentityIPlancherelConditional.lean` docstrings; scope doc updated. No fit, nothing physical wired. |

## Key artifacts

- Audit docs: `docs/audits/2026-06-16-s5so3-*.md` (branching-backbone-verified, ingredient4-fibre-schur-weyl-constraint,
  two-sasakian-construction-attempt, reeb-resonance-probe-negative, hopf-coupling-and-reeb-obstruction,
  markov-weighting-sasakian-scope) + the corrected `2026-06-13-gap-a4-operator-valued-muon-branching.md`.
- Verifiers (all exit 0): `docs/audits/scripts/s5so3_*.py` (branching backbone, ingredient 4/5 markov shift,
  fibre Schur–Weyl, coupling Schur, Reeb resonance, Hopf coupling obstruction, markov weighting facts).
- Lean scaffold: `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean` (open `irrepToRotation` on the corrected A₅-irrep domain — de-vacuified in #2480; was the falsified `partition_to_rotation`).

## Cross-references

- Synthesis: [`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](../audits/2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md)
- Construction program: [`docs/scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md`](../scope/2026-06-16-icosahedral-reeb-fiber-map-construction.md)
- Sibling A≥3 compute cluster: #2369 / #2371 / #2372 (produces `W_λ` algebraically)

## qbk2 q-Bessel "quadratic action" binding direction — FORECLOSED (2026-06-20, double-sourced)

Two independent routes agree the q-Bessel 2nd-kind "quadratic action" is **not** the
binding mechanism:

- **#2521** (session 01Q34jUc): retired via the `2026-06-14` joint-J⊕I combiner (³He
  +17.4%→+117.9% NO-GO); the legitimate "quadratic action" is the content-Casimir `μ_λ`
  already wired into `prop:q-heat-kernel-peter-weyl`; the precheck "P1 fail" is a
  normalizer artifact (`Z(0)=Σd²`, not `[n]_q!`).
- **#2549** (this session, fresh rigorous arc #2530→#2549): forced `y_λ` Markov weighting
  collapses the rigorous reduction-of-order correction from `2.23×` (unweighted) to
  **1–6%** of `B(D)` (~20–80× too small). Refuted by its own forced weighting.

**Convergent negative** (different methods) ⇒ do not re-walk the q-Bessel binding probe.
**Machinery that stands** (additive, from #2549): the resonance-free reduction-of-order
2nd-solution construction + sorry-free Lean lemma `QOU/QBeta/QCasoratianAbel.lean`
(q-Casoratian/Abel law, axioms `[propext, Quot.sound]` only). The C(n) defect closed
form `−n(n−1)(2n−13)/144` (#2527) is the falsifiable sub-leading target for the
*geometric* W_λ index continuation (#2503/#2524/#2488). bean `qbk2` carries both notes;
owner closes.

---

**`a_D=lw` bridge (2026-06-24, #2674).** Merged #2612 lever-1 established the binding
kernel's SW-period anchors as selection-rule values `a_D^(n)=lw(n−1)`,
`lw(c)=(1/(c+1))·Σ_{λ⊢c+1} dim_q` (canonical q-hook `dim_q`), confirmed c=1,2,3 +
the proved depth-2 `det=1` recurrence `R=x²−τx+1`, τ(q₀)=2.6424
(`binding_selection_rule_tau_closure.py`). The open residual — **SW-period =
selection-rule value** — IS this ledger's W_λ geometric-origin frontier: the
Seifert–CS index (#2524) at q₀ on the partition blocks must reproduce the Hecke
q-hook `lw(c)`. Per #2608, this is a **functional-level** identification (same W_λ
family), NOT a naive ~8%-off number-match. Shared validation target: the
`144·C(n)=−n(n−1)(2n−13)` defect. Coordinated on #2488. c=2 status: `lw(2)=(q+1)²/(3q)`
is derivation-tight but **untested** (no independent c=2 observable; Hopf-diquark the
candidate) — `docs/audits/2026-06-24-lw2-c2-prediction-untested-status.md`.

**Geometric `W` constraint — `H^{1,0}(Bring)` is A₅-irreducible (2026-06-24, #2701).**
Working the `a_D=lw` bridge above, the relevant Bring fact is now computed exactly in
Sage (character theory, no numerics): Bring is the canonical genus-4 curve in
`P³ = P(`std 4-dim S₅ rep`)`, so `H^{1,0}(Bring)` **is** the standard rep — verified
irreducible over S₅ (`⟨χ,χ⟩=1`) and **A₅-irreducible** (`χ|_{A₅}=[4,0,1,−1,−1]`,
`⟨·,·⟩=1`). Two consequences for the geometric `W_λ`/`W` build:
1. **No A₅-invariant rank-2 subspace of the holomorphic differentials** ⇒ the
   cheat-sheet `H¹(Bring)=2W` cannot be an A₅-subrep of the forms; `W` must be an
   **isogeny/CM factor of `Jac(Bring)`** (Riera–Rodríguez decomposition), realized at
   the de Rham / abelian-variety level.
2. **`tr B` (= τ(q₀)=2.6424, the `a_D=lw` recurrence trace) is a q-_family_
   Gauss–Manin _monodromy_ trace**, not a fixed-curve period — so the Seifert–CS index
   at q₀ must come from the q-family matrix `M` (this keystone), confirming the
   "functional-level, not naive number-match" framing. The torus shortcut is separately
   refuted: `τ_torus = 2cosh2η₀ = 2.0437 ≠ 2.6424`. Probe/audit only, no fit:
   [`computations/substrate/lever1_bring_period_trB.sage`](../../computations/substrate/lever1_bring_period_trB.sage),
   audit `docs/audits/2026-06-24-lever1-trB-geometric-target.md`. Coordinated on #2608/#2488.

**The rank-2 `W` is the elliptic curve `Bring/S₄`; `Jac(Bring) ~ E⁴` (2026-06-24, #2710).**
Exact extension of the A₅-irreducibility above (character theory, `genus(Bring/H) =
dim std^H`, no fit): `Bring/S₄` is an **elliptic curve** `E` (8 subgroup classes give
genus-1 quotients). Since `H^{1,0}(Bring) = std` is irreducible, `Jac(Bring)` is
isotypic ⟹ a power of one simple factor; the elliptic quotient pins it: **`Jac(Bring)
~ E⁴`** (Riera–Rodríguez). So the framework's **rank-2 "W-plane" is literally
`E = Bring/S₄`** (period = scale + modulus, 2 real DOF), and `H¹(Bring) = H¹(E)⊗std =
2·std`. **Keystone reduction:** the q-family Gauss–Manin monodromy `M` drops from
genus-4 (`Sp(8)`) to a **2×2 `SL₂` monodromy on a q-family `E(q)`**, with the lever-1
target `tr B = 2.6424` literally `tr M` — and the lever-1 depth-2 `det=1` kernel
`R = x²−τx+1` *is* the `SL₂` characteristic polynomial. **Open keystone, now genus-1:**
identify `E(q)` (the q-deformation of `Bring/S₄`; candidate = the elliptic fibre of the
`S³/2I` Seifert build #2524) and test `tr M(q₀) = 2.6424`. `E ≠` substrate torus
(`τ_torus = 2.0437 ≠ 2.6424`). Probe/audit only, no fit:
[`computations/substrate/bring_jacobian_isogeny_factors.sage`](../../computations/substrate/bring_jacobian_isogeny_factors.sage),
audit `docs/audits/2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`. Coordinated on #2524/#2608.
---

**Residual (ii) DISCHARGED — `Reeb = Res^{S₅}_{S₃}` Lean formalization (2026-06-24, [#2704](https://github.com/litlfred/qou/pull/2704), merged `83edee35`).**
[#2524](https://github.com/litlfred/qou/pull/2524)'s honest scope left residual (ii) — the Lean
formalization of the *"Reeb = Res^{S₅}_{S₃}"* identity at the keystone-scaffold level — open. It now
lands sorry-free + axiom-free in
[`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean):

- **The identity.** The Seifert fibration `S³/2I → S²(2,3,5)` has Reeb = the Seifert `S¹` fibre;
  localization restricts along it, algebraic shadow `Res^{S₅}_{S₃}`. The geometric Reeb symmetry
  (conjugate partitions share a fibre, `conjugate_same_a5_irrep`) matches the exact algebraic symmetry
  **restriction commutes with conjugation**: `V_{λ'}=V_λ⊗sgn_{S₅}`, `sgn_{S₅}|_{S₃}=sgn_{S₃}`, so
  `Res(λ')=s3SignTwist(Res(λ))` — swapping `S₃` triv↔sign, **fixing the standard `(2,1)`** (the
  Borromean `h⁴`-carrier).
- **Decls.** `def s3SignTwist`; `restriction_intertwines_conjugation` (∀λ⊢5);
  `std_irrep_conjugation_fixed`; capstone `reeb_eq_restriction_scaffold [BringFiberAction]`. All three
  theorems `#print axioms` = *does not depend on any axioms*.
- **Scope (honest — this is NOT a keystone closure).** Discharges residual (ii) ONLY: the *algebraic*
  restriction-commutes-with-conjugation identity. The capstone's conjunct (i) still **uses** the
  `BringFiberAction` class (the geometric fibre map stays open). **Residual (i) — MTC-matching: pin the
  Beasley–Witten gauge datum on `S³/2I` to the Hecke `Rep U_q(sl_N)` blocks so the localization
  `W_λ = d_q²/D²` is provably OUR Hecke category's Plancherel measure, not "some MTC's" — stays
  owner-gated**, and IS the live `W_λ` geometric-origin frontier in the banners above. **210 ppb stays
  refuted** (the keystone delivers the O(1) generation skeleton, not the 2×10⁻⁷ fine shift). No fit, no
  production wiring, no registry tier change. Audit
  [`docs/audits/2026-06-24-keystone-reeb-restriction-lean-formalization.md`](../audits/2026-06-24-keystone-reeb-restriction-lean-formalization.md).
---

**Owner reversal extended to the λ_SW side; color E_q Gauss–Manin connection derived (2026-06-25, [#2757](https://github.com/litlfred/qou/pull/2757)).**
**Reversal.** The narrow 2026-06-19 reversal (W_λ-index DG build) is **extended by explicit owner
sign-off (2026-06-25)** to the **λ_SW Seiberg–Witten-period side** of the same keystone — the color
`E_q` elliptic factor. Scope unchanged otherwise: a parameter-free geometric computation, **not** a
fit-based q₀ derivation; the "no 7th fit-based Δ_λ ansatz" rule still stands.
**Result (no fit, nothing wired).** First explicit write-down of the family's Picard–Fuchs / Gauss–Manin
connection `N(q)` for `E_q: y²=x³+p(q)x+r(q)` (Griffiths–Dwork; the object the M-workplan + prior probes
named but never computed):
- `N(q) = −1/(2D)·[[A,Bc],[Cc,−A]]`, `D=(4a³+27b²)/6`, validated: **`tr N=0`** (re-derives `det B=1`
  geometrically) and **`ω=∮dx/y` satisfies the implied 2nd-order PF ODE to `1.2×10⁻⁵`**; `−det N>0`
  (hyperbolic) on `[1,q₀]`.
- **(a)-negative:** the abelianised **transport** integral `θ_spec=∫₁^{q₀}√(−det N)dq = 0.0141 ≠
  θ_binding=0.7815` (undershoots **~55×**, below even `θ_torus=2log q₀=0.2087`) — a *short transport
  cannot source the large rapidity*. Scope (a): rules out the transport reading, does **not** exclude the
  curve or the keystone; `N(q)` is a permanent correct contribution.
- **Keystone REDIRECTED:** all three natural geometric candidates on the color-`E_q`/`λ_SW` side miss —
  loop monodromy (`SL₂(ℤ)` integer trace; prior), path transport (`θ=0.0141`, ~55× small), and intrinsic
  Tate period `2π Im τ_E` (`5.847`, 6.5× large + 6× too q-flat; `τ_E` Klein-`j`-validated). So `θ_binding`
  is **not** a color-`E_q` period at all — its geometric origin is the **`W_λ`-side Plancherel/MTC
  localization (residual i)**, the #2744 frontier. The color `E_q` is the right *curve* (rank-2 `W`); the
  rapidity is the rep-theoretic `tr B`, whose geometric face is the `W_λ` index, not an elliptic period.
Probes `lever1_color_eq_lambda_sw_rapidity.py` + `lever1_color_eq_intrinsic_tau_rapidity.py`; audit
[`docs/audits/2026-06-25-lever1-color-eq-lambda-sw-rapidity.md`](../audits/2026-06-25-lever1-color-eq-lambda-sw-rapidity.md).

---

## Binding-side test routed in (2026-06-29, #3128)

The Δ_λ binding residual's **isovector** coefficient (`b ≈ −1.747` constant,
`κ = b/4`, #3114) is the **chiral residue** of the categorical mass
(`QOU.WedderburnMass.chirality_residue_mass_term`'s `mass_chiral`), homed on the
Bring surface via the Reeb involution `ξ↦−ξ` (`archimedean-chirality`) and the
A₅ Galois `√5↦−√5` twist. **The framing-exponent route for `κ` is refuted**
(audit `2026-06-29-kappa-framing-route-refuted.md`): the canonical `tr_M`
captures the writhe exactly (`σ⁻¹ = σ−h`), so there is no normalization DOF.

**Routing.** `κ` is the chiral weight of the `W_λ` Plancherel measure
`μ(λ)=d_q²/D²`, so its value is the content of **the same single open keystone
conjecture `BWVacuumRowIsHecke`** (#3106). Lean (`BindingIsovectorChiralResidue.lean`,
sorry-free): the §3b-cond class `WLambdaChiralBinding` carries the identification;
`binding_isovector_mirror_from_chiral` derives `b = 4κ` from it. Paper:
`prop:isovector-chiral-residue` (conditional).

**Gift to the keystone program — a binding-side falsification test.** When
`BWVacuumRowIsHecke` is derived and its chiral weight supplied to the binding
`mass_chiral` residue, the isovector residual must vanish: **`residual b → 0`**
(the achiral part already works for light nuclei). A candidate chiral derivation
that leaves `b ≈ −1.7` is wrong. **No fit; CAL-1/2/3 only; the test is `b→0`,
never `b=−√3` (that reproduces the error). Not wired.**

## λ-colored Σ(2,3,5) → E₈-exponent family, 4↔4 to bwS0 (2026-06-30)

The residual frontier's "λ-colored insertions" step (bare probe pinpointed it; only
the closed-manifold number `Ψ(1/q₀)=2.3296` existed) is **taken**. Coloring the
order-5 icosahedral/A₅ fibre of Σ(2,3,5) by SU(2) colour α shifts the Lawrence–Zagier
false-theta support `30(1±1/2±1/3±1/5)→30(1±1/2±1/3±α/5)`: α=1 reproduces the bare
`{1,11,19,29}`; α=2 gives the complementary E₈ exponents `{7,13,17,23}`; together the
two lowest colours generate **all 8 E₈ exponents** (P=30=h(E₈)). The 8 exponents pair
under the Coxeter involution `e↔30−e` into 4 dual pairs, matching the 4 conjugation
classes of `bwS0` at n=5 **monotone in magnitude** (wall `{1,29}`↔(5)/(1⁵) smallest;
center `{13,17}`↔self-conj (3,1,1) largest). The Coxeter ℤ₂ mirrors the transpose/
chirality ℤ₂ `λ↔λ′` of `S_{0λ}=S_{0λ′}` — supplying the very `W_λ=W_{λ′}` symmetry the
bosonic-colour foreclosure showed `m_d` violates. (a) structural advance, no fit; the
exact pair→class normalization (the `D` realizing `bwS0=d_q/D`) is the remaining value
step, now on an explicit colored family. Audit:
[`docs/audits/2026-06-30-keystone-colored-sigma235-e8-family.md`](../audits/2026-06-30-keystone-colored-sigma235-e8-family.md);
probe `computations/probes/keystone_colored_sigma235_wrt.py`.

## Value step SETTLED at the false-theta level — D=2, golden row; bwS0 identification refuted (2026-07-02)

The owner uploaded the primary sources (commit `ece271823`: Hikami math-ph/0405028,
Andersen–Mistegård 1811.05376, Murakami 2205.01282, Lawrence–Zagier 1999). The genuine
per-block amplitude of Σ(2,3,5) is now transcribed and **machine-validated end-to-end**
(Theorem 10 exact to 1e−38 at N=3..11; S²=1; Cor 12 weights reproduced): the
vector-valued modular family has **D(2,3,5)=2** components — every colouring of the
order-5 fibre lands in span{(1,1,1),(1,1,2)} (α=4≡α=1, α=3≡α=2) — and the vacuum row is
`(2/√5)(sin π/5, sin 2π/5)`, **ratio = φ** (golden; √Reidemeister-torsion magnitudes,
CS = −1/120, −49/120). The n=5 target `bwS0 = d_q/D` has 4 classes, ratios
(1, 4.11, 5.22, 6.22): **type (2≠4) + value (φ∉targets) mismatch ⇒ the identification
"bwS0 = vacuum row of the Σ(2,3,5) false-theta S-matrix" is REFUTED** (scope (a): this
geometric object). The 2026-06-30 "4↔4" correspondence survives at SUPPORT level only.
Hikami's χ^{(111)}/χ^{(112)} equal the 2026-07-02 sympy-derived colored characters
exactly (eq. 5.6 = the derived identity) — the two independent validations agree.
Consequence: the geometric route cannot close on S³/2I itself; redirects = larger-D
Seifert data / colored Ẑ-blocks (Murakami now in library/) / non-geometric
`BWVacuumRowIsHecke`. Audit:
[`docs/audits/2026-07-02-keystone-valuemap-genuine-smatrix.md`](../audits/2026-07-02-keystone-valuemap-genuine-smatrix.md);
probe `computations/probes/keystone_valuemap_genuine_smatrix_s013.py`; also the round-2
prune set [`2026-07-02-keystone-valuemap-qbessel-gate.md`](../audits/2026-07-02-keystone-valuemap-qbessel-gate.md)
(residue weights are pure signs; channel amplitudes are the L-value family; single-argument
q-Bessel rows fail the 1-dof gate).

## Route 1 CLOSED (constancy exclusion); route 2 scoped → bean rt2f (2026-07-03)

Owner redirect after #3208: route 1 (larger-D Seifert) executed on the count-matching
Σ(3,4,5) — D=6, γ=4 flat connections = 4 bwS0 classes; full transcription
machine-validated on the second manifold (Theorem 9 exact ≤1.2e−38; S(6×6)²=1; flat row
= printed Cor-11 weights). **Flat-row ratios (1, √2, φ, √2φ) ≈ (1, 1.41, 1.62, 2.29) vs
d_q (1, 4.11, 5.22, 6.22) and classical (1,4,5,6): REFUTED — the count match does not
extend to values.** Then the class-level **constancy exclusion** (scope (b), invariant
cited): every Seifert/plumbed false-theta S-entry is a constant algebraic sine-product
(no q in Hikami 3.8), while d_q(4,1)/d_q(5) = [4]_q is nonconstant in q — no constant
geometric row can realize the fibre-level `BWVacuumRowIsHecke`; single-anchor matches are
the fitted mode. **Route 1 closed for ALL Seifert data, any colouring.** Surviving
type-correct class = q-FUNCTION block families: colored Ẑ / F_K(x,q) knot-complement
blocks (GPPV radial-limit theorem: Murakami 2205.01282, uploaded; Seifert resurgence: AM
1811.05376, uploaded) — successor bean `rt2f` (owner-gated; formalize-first: state the
x-specialization class + invariants before numerics; instantiates-or-refutes the DG
sibling's `QBesselRadialPartRealization` Lean obligation). Bean `s013` CLOSED. Audit:
[`docs/audits/2026-07-03-keystone-route1-closed-route2-scoped.md`](../audits/2026-07-03-keystone-route1-closed-route2-scoped.md);
probe `computations/probes/keystone_route1_sigma345_constancy_s013.py`.

## T1 DONE — conjecture classes de-abstracted, factor-2 anchor fixed (2026-07-04, bean 5e79)

Tier-1 of the keystone de-abstraction epic (bean `08a2`) is complete on
`claude/cheat-sheet-derivation-gaps-if9d38`. `BringTrilogDepth3Witness` is no
longer the `residual : ℝ + residual_eq_zero` placeholder (§3b-tax
`proof-claims-unencoded`): the class now carries the four archimedean
components Cl₃/S₃ at 2π/5, 4π/5, the **K=5 distribution relation (real part)**
tied to the PROVED `Cl3Zeta5OrbitSum.orbit_sum_identity`, and witness-pinned
sign non-degeneracies; derived sorry-free `pair_sum_eq` and `cl3_4pi5_neg`.
`Cl3Zeta5GeometricRealization` is now a **dependent conjecture**
(`[W : BringTrilogDepth3Witness]` binder — the derived `conjecture_graph`
edge) whose candidate invariants must realise the witnessed values;
derived sorry-free `realize_pair_sum`, `cl3Zeta5_pos`.

**Factor-2 bug fixed in passing:** the old `realize_orbit_sum` anchored the
Clausen PAIR Cl₃(2π/5)+Cl₃(4π/5) to the full 4-term orbit sum −(24/25)ζ(3);
each value appears twice in the k=1..4 orbit (Cl₃ even, 2π-periodic), so the
pair sum is **−(12/25)ζ(3)** ≈ −0.577 (the old anchor would force
Cl₃(4π/5) ≈ −1.34, outside Clausen range |·| ≤ ζ(3)). Both modules wired into
the `QOU.BraidKnot` aggregator; lean-direct EXIT 0 (only the intended §3b
open-conjecture `sorry` instances remain).

## Redirect (i) CLOSED — larger-D Seifert (Σ(3,4,5)) refuted; compact-modular route exhausted (2026-07-04)

The 2026-07-02 Σ(2,3,5) refutation listed three redirects; **(i) larger-D
Seifert** is now closed. Σ(3,4,5) — smallest pairwise-coprime Brieskorn sphere
with D=6, γ=4 flat connections (= the 4 bwS0 classes) — was tested by extending
the validated Hikami eq.3.1/3.8 machinery (S²=I to 4.4e-50, unit-row anchors
pass). Its D=6 vacuum row ratios are (1,1,√2,φ,φ,2.288), bounded by ~2.29 and
structurally unable to reach the target's 6.22; best 4-subset 69% off. Scope (a).

**Structural softener (not a hard exclusion):** the modular S-matrix is
rational-angle sines, **q₀-independent**, while bwS0=d_q/D moves with q₀
(∂/∂q₀ = 0,1.91,3.85,3.85). No compact Seifert modular row can *track* the
q₀-dependent target — confirming the redirect to the **non-compact q-Bessel**
(q₀-dependent) vacuum row as the sole viable geometric object. Redirects (ii)
Ẑ/GPPV colored blocks (Murakami 2205.01282) and (iii) non-geometric
`BWVacuumRowIsHecke` stand. Audit:
[`docs/audits/2026-07-04-keystone-sigma345-largerD-seifert-refuted.md`](../audits/2026-07-04-keystone-sigma345-largerD-seifert-refuted.md);
probe `computations/probes/keystone_valuemap_sigma345_dm6.py` (PR #3290).

## Value map GROUNDED: target is compact Hecke quantum-dimension data; redirect (ii)-via-Murakami closed (2026-07-04)

Two machine-verified facts consolidate the whole refutation series. **(1)** bwS0=d_q/D
at n=5 is *exactly* the compact SU_q(2)/Hecke quantum-dimension vector — 3 balanced
q-integers [1],[4],[5] (Laurent polynomials in q₀) + the product [4][3]/[2] = the
Verlinde ratio S₀λ/S₀₀. **(2)** The owner-uploaded Murakami GPPV paper
(`library/arxiv-2205.01282v2/2205.01282v2.pdf`) has **0** colored/decorated/wilson/refined terms — its
Σ(2,3,5) homological block is the undecorated D=2 golden false theta (already refuted).

**Type argument (why every geometric route failed):** the target is compact-algebraic
(Laurent poly); compact modular S-matrices are q₀-independent rational sines (redirect i);
the non-compact q-Bessel J_ν(x;q) is a transcendental ₁φ₁ series — its single-argument
(falsifiable) form is refuted (qbessel-gate §4) and the multi-argument form is an
unfalsifiable ≥4-dof fit without the un-uploaded Koelink–Swarttouw Plancherel kernel.

**Honest resolution:** the value map *is* the compact Verlinde/Hecke identity
S₀λ/S₀₀=d_q (redirect iii, BWVacuumRowIsHecke) — near-definitional. It closes the
value-map *question* but does NOT supply the manifold-side geometric derivation the
Subgoal-2 reversal targeted: the manifold WRT category (D=2 golden) is a *different*
category from the n=5 Hecke category (4-class), so the identity holds tautologically on
the Hecke side and adds no q₀/D constraint. The geometric route is stalled at the
compact-vs-geometric **type mismatch**. Owner fork: (a) upload Koelink–Swarttouw to test
the last disciplined q-Bessel form, (b) accept redirect (iii), or (c) pivot. Audit:
[`docs/audits/2026-07-04-keystone-valuemap-target-is-compact-hecke.md`](../audits/2026-07-04-keystone-valuemap-target-is-compact-hecke.md);
probe `computations/probes/keystone_valuemap_target_is_compact_hecke.py`.

## q-Bessel Tricomi sub-route refuted WITH a source (2026-07-04, bean s013)

Owner uploaded `library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf` (Raza–Fadel–Cesarano 2025, 2-variable
q-Legendre) in response to the redirect-(ii) source ask. It is a q-Bessel paper
but **not** the Koelink–Swarttouw Plancherel source — it cites Koornwinder–
Swarttouw [22] but contains no q-Hankel kernel / E_q(2) measure (scan: 0
`plancherel`/`E_q(2)`/`measure`/`vacuum`). What it gives is the entire, 0-dof
0th-order q-Bessel Tricomi `C_{0,q}(x) = Σ (-1)^k x^k/([k]_q!)²` (eq. 11). Its
positive zeros / q-integer-node values are fixed by q alone, so a falsifiable
check is constructible. Result (`keystone_qbessel_tricomi_c0q_nodes.py`): **no
parameter-free quantity** (zeros ξ_j, √ξ_j, ξ_j/ξ_1, gaps, C_{0,q} at [n]_q)
reproduces the compact target {1,[4]_q,[5]_q,[4][3]/[2]} within 1% (nearest
ξ₂/ξ₁=5.35 vs [5]_q=5.22, 2.4%; √ξ₄=6.30 vs 6.22, 1.3%); 4-vector no-match.
**Scope-(a) refutation, now sourced** — closes the q-Bessel-Tricomi sub-route
with a citation but does NOT exclude a Plancherel-fixed E_q(2) row (still needs
Koornwinder–Swarttouw 1992, TAMS 333, ref [22] — cited by the upload, not
contained). Audit:
[`docs/audits/2026-07-04-keystone-qbessel-tricomi-c0q-sourced-refutation.md`](../audits/2026-07-04-keystone-qbessel-tricomi-c0q-sourced-refutation.md).

## LAST disciplined q-Bessel form REFUTED — E_q(2) q-Hankel vacuum row, fully sourced (2026-07-04, bean s013)

Owner uploaded the decisive source: Koornwinder–Swarttouw 1992 (arXiv:1208.2521 =
TAMS 333), `library/arxiv-1208.2521v1/1208.2521v1.pdf` — the third (Hahn–Exton) q-Bessel eq.(1.2)
+ Hansen–Lommel orthogonality (roots μ_j of C_α(q;μ)=0 = the Plancherel nodes).
This is the one form #3292 named as still-testable. Probe
`keystone_qhankel_eq2_vacuum_row.py` (α∈{0,½,1,2}, 112-candidate parameter-free
menu): **no coherent (α,form) pair reproduces the ORDERED d_q vector
{1,[4],[5],[4][3]/[2]} within 1%**; the 4 scattered single-index 1% grazes
(different α/j/form, none co-locating in one ordered vector) are large-menu
coincidences (PSLQ/entropy caution), recorded as the sharpener. **Scope-(a),
sourced, decisive** for redirect (ii): all four realisation routes now refuted
with sources (Σ(2,3,5) golden D=2; Σ(3,4,5) D=6; colored LR pure-sign; q-Bessel
Tricomi + Hahn–Exton). Does NOT structurally exclude (scope a) a different node
convention. **Standing value-step answer = redirect (iii), the NON-geometric
"why":** S_0λ/S_00 = d_q (Verlinde vacuum row) selected by Markov-trace
uniqueness / Wenzl bridge / Perron–Frobenius (state positivity = confinement
SDP) — already in the corpus (`y-lambda-closed-form-wenzl-bridge.md`,
`wenzl-bridge-applicability-qou.lean`, `intro-markov-axioms-braid-link.md`); a
categorical "why" that needs no geometry, so the geometric program's exhaustion
leaves nothing unexplained. Audit:
[`docs/audits/2026-07-04-keystone-qhankel-eq2-vacuum-row-sourced-refutation.md`](../audits/2026-07-04-keystone-qhankel-eq2-vacuum-row-sourced-refutation.md).

## REFRAME — self-duality narrows the eigenfunction class; node screens retired (2026-07-05, bean s013)

Owner redirect: stop screening off-the-shelf q-Bessel families against `d_q`;
instead use the framework's own structure to narrow the orthogonal-eigenfunction
class. Two inputs settled first:

- **1208.2521 vs Step-9b: NO** (wrong gap). 9b's open legs (per-λ FR weight, κ,
  IMME Δ³=0) are compact algebraic Hecke/Markov objects; the q-Hankel transform
  is a non-compact E_q(2) Plancherel kernel — no mechanism. 1208.2521 is keystone
  redirect-(ii), not 9b.
- **math/9805023 (big q-Bessel / q-Laguerre, Ciccoli–Koelink–Koornwinder)** —
  identified from owner upload `9805023v1.pdf` (commit `8e311cb`). Its discrete
  orthogonality is supported on `{c·q^k : k∈ℤ}` for ANY `c>0` (§4): the scale `c`
  is a FREE parameter ⇒ a node screen is a fit, not 0-dof. **Not run** (would
  violate the discipline). This is diagnostic that the node-screen frame is wrong.

**The (A)+(B)+(C) narrowing** (replaces node screens): (A) Frobenius pairing
supplies the orthogonal system (`χ_λ`, quantum-dimension measure); (B) Verlinde/PF
pins `d_q` as the unique PF-positive fusion ground state (Wenzl); (C) self-duality
`S=Sᵀ`, `S²=C`. The (C) leg is now **Lean-formalized sorry-free**
([`KeystoneSelfDualSpectralNarrowing.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneSelfDualSpectralNarrowing.lean)):
`S⁴=1` (self-reciprocality = the categorical avatar of the self-reciprocal
q-Hankel transform), eigenvalues are 4th roots of unity — `ζ⁴=1` over a field on a
nonzero eigenvector (`ζ⁴•v=v` over any CommRing) — the class narrowing, and the
vacuum row is C-fixed (self-dual sector, where the PF-positive `+1` state is `d_q`).
**Narrowing, not closure** — the value step already has redirect (iii); leg (C) is
the constraint any geometric realisation must meet, and the structural reason a
free-scale q-Bessel family cannot be it. PR #3358; audit
[`docs/audits/2026-07-05-keystone-selfduality-spectral-narrowing.md`](../audits/2026-07-05-keystone-selfduality-spectral-narrowing.md).

## Value-step reframe FORMALIZED across three legs (2026-07-05, bean s013)

The self-duality reframe (owner redirect, 2026-07-05) is formalized as three
sorry-free Lean legs — legs (B) and (C) **merged** (#3380, #3362); leg (A)
pre-existing — plus a capstone introduced by **this PR** (#3391, not yet on
`main` at time of writing):

- **(C) Self-duality** — `KeystoneSelfDualSpectralNarrowing.lean` (**PR #3362**,
  merged): `S²=C ⇒ S⁴=1` (self-reciprocality), eigenvalues 4th-roots-of-unity
  (`ζ⁴=1` over a field on a nonzero eigenvector), sector tightening `ζ²=1` on the
  `C=+1` self-dual sector, vacuum row `C`-fixed.
- **(B) PF selection** — `KeystonePerronFrobeniusGroundState.lean` (**PR #3380**,
  merged): §3b-cond `Prop`-class over explicit `(N, rho, d)` carrying the cited
  PF/Ocneanu–Wenzl up-to-scale uniqueness (`pf_proportional`); derived
  `eq_d_of_normalized` pins a normalised positive ground eigenvector uniquely to
  `d_q`.
- **(A) Frobenius** — the quantum-dimension measure `d²/D²`
  (`KeystoneVerlindeSMatrixBridge.verlindeMeasure_eq_plancherel`, pre-existing);
  its self-duality `d(λ′)=d(λ)` is the `C`-fixed hypothesis of the capstone.
- **Capstone** — `KeystoneValueMapSynthesis.lean` (this PR):
  `keystone_value_map_pinned` composes (A)+(B)+(C) — a positive, `k`-normalised
  fusion-ground `S`-eigenvector is **`= d_q` and its `S`-eigenvalue is `±1`**.

**Status: the value-step narrowing is formalized.** Redirect (iii) (the categorical
"why") remains the standing answer; leg (B) stays conditional on the owner-gated
physical instance (the fusion category whose PF eigenvector is the Hecke `d_q`).
Both q-Bessel uploads (1208.2521, math/9805023) are retired as redirect-(ii)
node-screen material — superseded by this structural narrowing.

## Self-conjugate sector: gate EXACT, no continuation (2026-07-19, PR #4084, bean qou-2v7k)

The de-opaqued gate's remaining open piece is the archimedean continuation of the fibre
root-of-unity modulus out to `q₀ > 1` (`BWVacuumRowConcrete` shows the concrete row
`S₀·θ^f` equals `S₀` **iff** `θ_λ^f = 1`, false off-diagonal at real `q₀`). New sorry-free
Lean (`QOU/BraidKnot/KeystoneElectronBlockExact.lean`) closes that residue **on the
self-conjugate sector, exactly and continuation-free**:

- `selfConj_contentSum_zero`: `contentSum_conjugate` (`c(λ')=−c(λ)`) forces `c(λ)=0` on a
  self-conjugate block (over ℤ).
- `theta_selfConj_eq_one`: hence `θ_λ = q^{c(λ)} = q^0 = 1` for **every** `q` — no `q₀>1`,
  no root-of-unity fibre.
- `bwS0Concrete_selfConj_exact`: so `θ^f = 1` for all framings `f`, and
  `bwS0Concrete_of_twist_pow_one` gives `bwS0Concrete = S₀` **exactly** — the framing
  obstruction that refutes the gate off-diagonal is structurally absent here.
- `bwS0Concrete_electron_block_exact`: flagship instance — the physical **electron block**
  `[3,1,1]` (self-conjugate, `c=0`); value `d_q([3,1,1]) = [3]_q[4]_q/[2]_q`
  (`qFactorial_shape_311`). Lean-izes ledger #3701 (was a Python probe only).

Scope: open-for-all per the 2026-07-11 general Subgoal-2 reversal (the pre-existing
`bwS0_eq_hecke` "owner-gated" docstrings are stale). Does **not** close the
non-self-conjugate blocks (`c(λ)≠0`, `θ^f≠1` at `q₀>1`) — that fibre continuation stays open.
Verification: risky proof steps machine-checked vs real Mathlib via faithful replicas
(exit 0); full lean-direct blocked in-sandbox by the QOU-cone/lake-build-Mathlib-wipe
catch-22; CI to confirm exit 0.

> **Verification cleared (2026-07-26).** The full lean-direct check is no longer
> pending: `KeystoneElectronBlockExact.lean` and its entire 10-module QOU cone
> (`IdentityIContentDecomposition` → `KeystoneC2{Content,Dim,QDim}Transpose` →
> `QPartitionCombinatorics` → `WLambdaMTCLocalizationObligation` →
> `KeystoneVerlindeSMatrixBridge` → `KeystoneModularTwist` → `BWVacuumRowConcrete`
> → keystone) recompiled **lean-direct exit 0, sorry-free** against current `main`
> on the restored `lake-cache/qou-v4-24-0` Mathlib oleans (the catch-22 is
> side-stepped by `lean`-direct against the cache branch, not `lake build`). Survey:
> [`docs/audits/2026-07-26-1ppq-l2-two-front-survey.md`](../audits/2026-07-26-1ppq-l2-two-front-survey.md).

## T(3,5) cross-link (2026-08-01, bean qou-pquk)

The tau-knot discussion review
([`docs/audits/2026-08-01-tau-knot-discussion-review.md`](../audits/2026-08-01-tau-knot-discussion-review.md))
surfaced a structural cross-link into this keystone: the torus knot
**T(3,5)** — the *maximal-genus* (g = 4) member of the embeddable
torus-knot spectrum, the unique one saturating the Bring genus bound on
a 3-strand base — has branched double cover the **Poincaré homology
sphere Σ(2,3,5) = S³/2I**, with fundamental group the binary
icosahedral group 2I. That is exactly the manifold whose WRT invariant
this keystone computes. So the keystone's geometric object is reachable
from *inside* the embeddable spectrum: the W_λ construction and the
maximal embeddable 3-strand knot meet at Σ(2,3,5).

Sibling fact (secondary): T(3,4)'s double cover is governed by the
binary *octahedral* group — the S₄ ⊂ S₅ restriction — giving the
subgroup-chain reading of the two 3-strand embeddable knots.

**Lean feasibility (assessed):** branched covers and Brieskorn spheres
are absent from Mathlib; a faithful formalization of the cover itself
is out of reach. What IS formalizable now: the genus saturation
statement (g(T(3,5)) = 4 = the Bring bound, pure arithmetic) and the
group-theoretic layer (2I as the binary icosahedral group). Neither is
started; this entry records the link and the assessment.
