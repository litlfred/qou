# 1 ppQ reevaluation (2026-07-17) — post-week state + two scoped attacks

**Owner directive:** "lots of work in last week — reevaluate path to close 1 ppQ
based on new work on main and active siblings." · **Tier:** strategic
reevaluation (updates [`2026-07-13-onepq-deep-analysis-chain-trace.md`](2026-07-13-onepq-deep-analysis-chain-trace.md)
per its own "update the row, don't fork" rule) + two scoped attack plans.
Scope-(a) throughout; nothing wired.

## 0. Bottom line

The 07-13 three-strand frame (a: calibration-cancelling dimensionless · b: deep
enablers = q₀ substrate + volume conjecture · c: NO-FLOAT L1) **still holds**,
but the last week's net is **one leg closed, one demoted to a wall, two
advanced-but-blocked, and three over-claims retired.** The L2 100× count is
**unchanged at 2 / 7** — no observable moved FAIL→PASS.

| | live state (per-observable-100x dashboard, this branch) |
|---|---|
| **L1 (compute ≤ 1 ppQ)** | **MET** — truncation ~10⁻⁵¹–10⁻⁵⁴ ppb every observable |
| **L2 (accuracy 100×)** | **2 / 7** — ✅ m_e (anchor), m_K/m_π (dimensionless, beats by 11×); ❌ m_p 437×, m_n 416×, Q_β 160×, Δ_pn 159×, m_μ 964× — all floor-limited (CAL-2 ~780 ppb) |

The one *genuinely-met prediction* (m_K/m_π) is a **dimensionless ratio where
the calibration cancels** — which pins the only two levers: **(a)** more
dimensionless predictions, or **(b)** derive q₀ from the substrate to remove the
CAL-2 floor under the five absolute observables.

## 1. Reevaluated strand state — what the week changed

### Strand c — NO-FLOAT / L1 → ✅ CLOSED (the week's real win)
⁴He certified 2026-07-13 (`l1-4he-certification-complete.md`): Rust kernel
in-sandbox, 77/77 partitions → `cross_check_trM_1ppb` **6 / 6 atoms 1 ppQ, 0
uncertified**, no float64 in the hot path. The 07-14 GP-kernel bug hit the GP-χ
Laurent path (caught by the stage-2 cross-check), **not** the seminormal-mpfr
mass-trace certification. Remaining: defense-in-depth only (an independent
color-weighted third method; peel+chi-cache share the `Σ y_λ χ^λ` definition) +
revalidate GP-derived witnesses (bean `qou-b2ie`). **The compute leg of 1 ppQ is
done.**

### Strand a — α_EM → ⬇ DEMOTED from "tractable now" to a walled multi-week calc
The θ-graph now *dictates* the 2-loop coefficient (`θ(1,1,2)=[3]_q`, validated),
so the number is the **closest target in the corpus: −0.20 ppb = 1.3σ**. But
07-14 ([`…-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md))
found the load-bearing blocker is a genuine **wall**: the per-loop measure
`1/(πb₁)=1/(8π)` is **underived**, and the week *refuted two previously-claimed
"derived" tiers* — the `(1−h²α)` Schwinger term (phase-3b exact check: wrong
order/sign) and "1/(8π) via Bring" (the "same measure as the zero-mode" comfort;
the proved zero-mode measure `1/Area=1/(12π)` fails at 1-loop by **−1419 ppb ≈
9500σ**). So the 07-13 audit's #1 ("tractable now") is **wrong post-07-14.**
Scoped attack in §2.

### Strand b1 — q₀ substrate / s5-so3 keystone → advanced algebraically, floor NOT removed
The McKay `2I↔Ê₈` value map `d_q(λ)=[mark]_q` (PR #3685) is a genuine
parameter-free polynomial identity (**"no fit" verified** — checked at two
generic q; 2 identities Lean-proved #3699; framing shown a pure phase, f=−1
#3701/#3703). **But it derives the q-*shape* of `W_λ`, not q₀'s value.** The
*geometric* leg — the colored Lawrence–Rozansky manifold amplitude that would
*equal* the value map — is **assumed via McKay, not computed**; the archimedean
q₀-continuation is untouched. "Gate open" = owner *authorized* Subgoal-2
exploration, not gate passed; the "geometric W_λ derivation" commit title
overstates the geometric leg. **The ~780 ppb CAL-2 floor under all 5 absolute
masses stands.** (No keystone commits after 07-12.) Multi-month.

### Strand b2 — volume conjecture / binding scale → net honesty-tightening + one refutation
- **kashaev-surreal figure-eight discharge** = a *special case* (already-classical
  Murakami–Murakami 2001) → backs the **muon anchor** `m_μ=m_e·Vol(4₁)/ℏ_q²` with
  a proved equality, **not** the binding scale (which runs on L6a4/8₁₁/…).
- **`surreal-limit-transfer`** = scaffolding (content-bearing Lean class, **no
  instance** = honest open state).
- **`vol-through-tau` §3b-cond** = a correct *downgrade* (self-assuming projection
  → conditional `[VolumeConjecture]`); honesty tightening, opposite of certification.
- **Ohtsuki Borel–Padé "exact smooth Im 𝔙"** = de-mystification: the κ₁..κ₈ rungs
  are symbolic-exact; the c₃/`S` "wall" is a `1/u³` representation artifact over a
  *smooth* state-integral 𝔙 (Im 𝔙 = 0 at real substrate by amphichirality). It
  produced **no certified Q_β** — Vol/π-as-Borel-action *refuted* (β≈2), β=3/2
  modular weight *fails*, and the Stokes datum **`A_ω` is unidentifiable at 7
  rungs**. And **⁴He's `Vol₄` was falsified** (no ≤14-crossing link at 8.048).
Binding stays conditional. The `A_ω` datum is the shared Q_β blocker — scoped in §3.

## 2. SCOPED ATTACK — the photon 1-loop determinant on the Bring Jacobian (α_EM)

**The wall, stated exactly.** In
$$
  \tfrac{1}{\alpha_{EM}} = q[9]_q[10]_q + \tfrac{b_1}{\mathrm{Area}} + \tfrac{\alpha[2]_q}{\pi b_1} - \tfrac{\alpha^2[3]_q}{(\pi b_1)^2} + \cdots,\quad b_1=2g=8,\ \mathrm{Area}=4\pi(g{-}1)=12\pi,
$$
every factor is derived (tree = Bring force-carrier uniqueness; zero-mode measure
`1/Area` + count `b₁` = proved heat-kernel/Hodge; graph grammar `[L{+}1]_q` +
resummation = derived) **except the per-loop measure `1/(πb₁)=1/(8π)`**. The
data discriminant is decisive: the *proved* `1/Area` measure fails at 1-loop by
−1419 ppb, while `1/(πb₁)` gives +1.67 ppb (1-loop) and −0.20 ppb = 1.3σ
(2-loop). So the loop normalization is set by the **Betti number `b₁` (a mode
count), not the Area** — and closing α_EM to ≤ σ_α = 0.15 ppb ⇒ **derive
`1/(πb₁)` specifically.**

**Why b₁ (the physics target).** The photon is the U(1) gauge field; its flat
connections mod gauge form the **Jacobian torus** `J(M)=H¹(M;ℝ)/H¹(M;ℤ)`, real
dimension `b₁=2g`. The 1-loop photon determinant on `M_Bring` is normalized by
the Jacobian volume — a `b₁`-dimensional object — hence `b₁`, not `Area`.
Turning "governed by b₁" into the *exact* `1/(πb₁)` is the one open computation.

**Decomposition (sub-steps):**
1. **Partition function.** Write the Maxwell/photon 1-loop `Z_γ(M_Bring) =
   [det'Δ₁]^{-1/2} · vol(J(M))` (Ray–Singer analytic torsion × Jacobian volume
   `vol(J(M)) = √det(Im τ)`, τ = period matrix). Standard Riemann-surface Maxwell;
   the `det'` excludes the `b₁` harmonic 1-forms (the proved zero-mode sector).
2. **Isolate the loop measure.** The Gaussian integration over the `b₁`-dim
   flat-moduli yields a `(2π)^{b₁/2}/√det` factor; show a *single-loop insertion*
   picks up `1/(πb₁)` — the `b₁` from the Jacobian dimension (mode count over
   `√det Im τ`), the `π` from the loop-momentum/heat-kernel measure normalization.
3. **Pin the exact constant.** Reconcile the `(2π)` loop factors with the `b₁`
   Jacobian modes → `1/(8π)`. Cross-check it reproduces the *working* 1-loop
   `[2]_q/(8π)` **and** the 2-loop θ-graph `[3]_q/(8π)²` — one derivation
   certifies **every** loop order at once.
4. **Global dressing sign** (the `−` alternation): a dressed-propagator
   convention; lighter, resolve separately.

**Build on (in corpus):** [`x5-bring-prym-jacobian.md`](../../content/quantum-observable-universe/particle-interactions/x5-bring-prym-jacobian.md)
(the Bring Prym–Jacobian / period structure — candidate source of τ),
[`s5_bring_hodge_depth.py`](../../computations/substrate/s5_bring_hodge_depth.py)
(Hodge/Betti data), the **proved contrast object**
`QOU.Archimedean.PhotonIRZeroMode` (`1/Area` zero-mode — parallel target),
`alpha_em_rt_phase4_bring_measure.py` (the imprecise phase-4 measure to correct),
`alpha_em_loop_measure_consistency_probe.py` (the b₁-vs-Area discriminant).

**Deliverable + estimate.** Target = a Lean lemma `loop_measure = 1/(π·b₁)`
parallel to the proved zero-mode lemma, backed by a compute probe (Jacobian-volume
1-loop determinant on Bring using τ from the Prym–Jacobian block). Sub-steps 1–2
(partition-function structure + b₁-vs-Area, mostly known) are **tractable now**;
sub-step 3 (exact constant) is the hard RT-determinant core (**multi-week**).
Payoff: closes α_EM → the **6th** L2 observable (first new dimensionless win).
**Blocker:** nothing in-corpus performs the genus-4 Jacobian 1-loop determinant;
needs the Bring period matrix τ extracted + the RT shadow-world normalization.

## 3. SCOPED ATTACK — the `A_ω` monodromy datum (Q_β exact `S` + Φ_b keystone G3)

Detail source: [`2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md`](2026-07-13-phib-proof-status-and-monodromy-datum-gap-audit.md).

**The gap.** The Ohtsuki Borel–Padé work showed the imaginary volume `Im 𝔙`
is a *smooth* state integral (no singular map), so Q_β's exact `S` (the bar-odd
`sinh` partner of the meson `cosh` scale) is set by the **Stokes/monodromy
normalization constant `A_ω`** of the Faddeev quantum dilogarithm Φ_b across its
Stokes line — a modular-double datum that is **unidentifiable from the κ₁..κ₈
rungs alone** (7 rungs under-determine it; the resummation fixes the *tail*, not
the *Stokes constant*). `A_ω` is the shared blocker for both Q_β's exact `S` and
the Φ_b keystone milestone **G3**.

**Route (scoped, not done):** pin `A_ω` from the Φ_b **modular-double /
quantum-modularity** structure rather than the divergent tower — the bar-parity
decomposition ([`phi-b-bar-parity-decomposition.md`](../../content/quantum-observable-universe/mass-theory/phi-b-bar-parity-decomposition.md),
[`phi-b-unitary-bar-odd.md`](../../content/quantum-observable-universe/mass-theory/phi-b-unitary-bar-odd.md))
+ Écalle–Borel resummation ([`ecalle-borel-resummation.md`](../../content/quantum-observable-universe/appendix-surreals-archimedean/ecalle-borel-resummation.md))
give the analytic structure; `A_ω` is the Stokes jump of Φ_b at `b→b⁻¹`
self-duality. **Deliverable:** a compute probe extracting `A_ω` from the modular
double (independent of the rung ladder) + a proof that it fixes `S`.
**Blocker:** the quantum-modularity Stokes constant of Φ_b is not yet computed in
the corpus; multi-week, but *narrower* than §2 (one constant, not a determinant).

## 4. Corrected priority order (supersedes 07-13 §Priority)

| # | Move | Payoff | Reality (post-week) |
|---|---|---|---|
| 1 | **α_EM loop measure `1/(πb₁)`** (§2) | +1 dimensionless L2 win; certifies *all* loop orders | isolated, sharp; multi-week; sub-steps 1–2 tractable now |
| 2 | **`A_ω` monodromy datum** (§3) | Q_β exact `S`; Φ_b G3 | narrower than §2 (one Stokes constant); multi-week |
| 3 | **q₀ geometric leg** (Lawrence–Rozansky amplitude, strand b1) | unlocks all 5 absolute masses | biggest prize; longest (multi-month) |
| 4 | L1 defense-in-depth + GP-χ revalidation (`qou-b2ie`) | hardens the closed leg | mechanical |

**Not a precision item:** the m_μ 964× miss is the **9.5σ μ–p tension** — a
*physics* discrepancy (which ratio pins q₀), arbitrated by an experimental
σ(Q_β) lever, not by any derivation here.
