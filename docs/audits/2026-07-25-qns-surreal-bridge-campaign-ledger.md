# q-NS surreal-bridge campaign — ledger (2026-07-18 → 2026-07-25)

**Scope:** the categorical→classical bridge of the q-Navier–Stokes program,
attacked *in-QOU* (owner scope directive 2026-07-24: every statement "Given a
QOU, then…"; no claim about the general classical `ℝ³` problem). Continuation
of [`2026-07-18-q-ns-classical-gap-decomposition.md`](2026-07-18-q-ns-classical-gap-decomposition.md).

## Merged PRs (chronological)

| PR | Landed |
|---|---|
| #3989 | Gap decomposition (5 gaps, 3 findings: NRŠ 1996 self-similar no-go; α over-determined; Levi dichotomy non-exhaustive); Bridge B named as open class; DSS re-scope; α tiering; β-trichotomy; in-QOU reframing (R1–R8); `deligne2007` ref dedup |
| #4159 | Surreal enstrophy at finite modes: infinitesimal calculus, `[k]_{1−ε} − k` infinitesimal, `st(Ω_N(1−ε)) = Ω_N(1)` (S1–S4) |
| #4162 | Both bridge directions: unbounded ⇒ infinite (G1); bounded + UV-exhaustion ⇒ finite (H1). Wall = one hypothesis |
| #4165 | Golden window: `1−ε` inside `1/φ² < q < 1` automatically (U1); uniform damping `[k]_{1−ε} ≤ ε⁻¹` (U2); exhaustion-from-tail (U3) |
| #4169 | **Sub-classical closure**: `[k]_{1−ε} ≤ k` termwise ⇒ biconditional closes on `q = 1−ε` with no spectral hypothesis (V1–V2) |
| #4171 | Super-classical side: forward direction proved; blow-up capped at ω-grade 1 under the dissipation closure (W1–W2) |
| #4177 | **Grade trichotomy**: regular / saturated-α=1 / intermediate; the whole open content = "is `ε·Ω(1+ε)` infinitesimal?" (X1–X2) |
| #4181 | **Numerical probe** of the criterion (exploratory, witness 4/4): sustained Kolmogorov `α = 1.3351 ≈ 4/3` **exceeds the grade-1 cap** (dissipation closure fails for sustained spectra; Finding-2 α tension resolves toward the cascade in-model); Gevrey smooth data `α ≈ 0`, grade-0 regular |

All Lean `lean`-direct exit 0, sorry-free, generic ordered field (§7c, no `ℝ`);
every open item an explicit hypothesis/class with **no instance**.

## State of the bridge

| Piece | Status |
|---|---|
| Sub-classical `q = 1−ε` | **closed**, both directions, inside the golden window |
| Super-classical `q = 1+ε`, forward | **proved** |
| Super-classical blow-up magnitude | **capped** at ω-grade 1 (dissipation closure) |
| Remaining open | which trichotomy regime the *true* flow realises — equivalently, its amplitude class |

## Probe interpretation (in-model, exploratory)

The realized regime is decided by the **amplitude class**, not by further
structure: sustained Kolmogorov forcing exceeds the cap (`α ≈ 4/3` — the
dissipation closure is falsified for sustained spectra); fixed Gevrey data is
grade-0 regular. In-model, **blow-up localises entirely to sustained forcing**.

## Completion of the tractable tranche (2026-07-25, PRs #4186–#4193)

| PR | Landed |
|---|---|
| #4186 | **Gevrey grade-0 theorem** (`gevrey_grade_zero`): geometric amplitudes with `q²r ≤ 1/2` ⇒ finite surreal enstrophy — probe Model B promoted |
| #4190 | **Closure-vs-cascade incompatibility** (`closure_excludes_deep_cascade`): the dissipation closure excludes grade-1-deep cascades — probe Model A promoted |
| #4193 | **Gevrey-persistence epic, bricks 1–4** (14 theorems): discrete Gronwall + rate wall (GP1); q-damping threshold + split persistence (GP2); ε-free local bootstrap, horizon `~1/(cΩ₀)` (GP3); **small-data global persistence** in the sub-threshold basin `cΩ₀ ≤ νμ` (GP4) |

**Final state:** local persistence for all finite data; global persistence for
small data; high modes damped; both probe findings theorem-grade. The sole
open item is **large-data global persistence at the finite-dimensional
low-mode block** — and the framework *predicts it fails* (every QOU is
internally NS-singular), so the open work is exhibiting the blow-up mechanism,
branch A.

## Machinery inventory for the large-data item

1. **Categorical (existence):** the obstruction chain (observability ⇒
   `NS(A) ≠ 0` ⇒ internal blow-up) + Yekutieli–Levi unification identify the
   super-threshold candidate: the anti-parallel vortex pair, linking number 1,
   at the collision locus `Σ`.
2. **Finite-dimensional spectral (computable):** `k_max ≈ 4` active modes at
   `q₀` (`discrete-vortex-spectrum`) — the low-mode block is a ~5-ODE truncated
   Leray system with **`SU_q(2)` Clebsch–Gordan coupling constants**, dominant
   channel `½⊗½ → 0`. Validated-numerics-sized.
3. **SDP/confinement duals:** S₅-invariant-channel positivity
   (`lp_dual_solver`, golden window) prunes the active couplings — makes the
   transfer coefficient `c` and hence the GP4 threshold `νμ/c` computable.
4. **GP calculus, blow-up side (provable next):** the discrete Riccati
   *lower*-bound lemma — `Ω_{n+1} ≥ Ω_n + δc'Ω_n²` forces divergence in
   finitely many steps — would give the mechanism-level branch-A statement.
5. **Surreal grade bookkeeping** to state outcomes in-QOU.

**Genuinely missing:** (a) pinning `c`, `ν·μ` from Clebsch–Gordan/SDP data
(compute session); (b) verifying the colliding-pair data satisfies the Riccati
lower bound — the true residue of the millennium problem in-QOU.

## Status at campaign close (2026-07-25, post-#4202)

**The corpus candidate and the lock tension.** The blow-up candidate is the
anti-parallel pair overlapping into a hyperbolic stagnation-point flow
(`rem:hyperbolic-overlap-saturation`), Levi lock `κ² = πν/Γ > 0`. Verdict on
"does it give the needed example": **yes in-QOU at every fixed `q ≠ 1`** (the
lock keeps the Levi form non-degenerate ⇒ by the Yekutieli–Levi unification the
obstruction survives ⇒ this data realises `qou_internal_ns_singular`); **no for
the classical limit** — the lock's own `ν`-scaling gives `C_L ~ ε⁻¹`, fitted
`β = 0.996 ≈ 1` = branch B (probe witness
`qns-levi-lock-scaling-probe.witness.json`), i.e. this channel *regularises* in
the limit, matching physical vortex reconnection.

**Convergent picture (two independent probes + two theorems):** smooth/Gevrey
data ⇒ regular (theorem); pair-collision channel ⇒ regular in the limit (lock
scaling); dissipation closure ⊥ deep cascade (theorem). The singular regime is
squeezed into **sustained/forced turbulence** — the surviving classical-blow-up
channel.

**Resolution path:** re-scope `conj:levi-degeneracy` to a **per-channel**
branch assignment (pair-collision channel branch-B-conditional-on-lock; the
framework's blow-up claim rides on channels the lock does not cover), or find
a flaw in the lock's uniformity (`Γ` growth during collision, overlap regime
not uniformly reached).

## Bean map for future agents

| Bean | Task | Status |
|---|---|---|
| `qou-a3n3` | EPIC Gevrey persistence — remainder: large-data global at the low-mode block | open (GP1–GP5 done) |
| `qou-nb6l` | Session: per-channel re-scope + pair-Riccati + sustained-forcing | open |
| `qou-js2u` | PC1: authorNote on `conj:levi-degeneracy` — per-channel reading + lock β≈1 tension | todo |
| `qou-6ngr` | PC2: two-regime ODE probe (Biot–Savart → hyperbolic overlap) verifying the Riccati lower bound for pair data at fixed `q` | todo |
| `qou-hy2t` | PC3: sustained-forcing surviving-candidate authorNote on `conj:regularity-breakdown` | todo |
| `qou-innq` | Original walls list (Bridge B context) | superseded in part by this campaign; keep for context |

**Reasonable stopping point (short term):** here — all 15 PRs merged, every
result sorry-free, the tension and the example-status recorded, and PC1–PC3
scoped as one-session bricks. **Next steps in priority order:** PC1 (content
honesty, small), PC2 (the decisive in-QOU mechanism check — a validated
two-regime ODE probe), PC3 (small), then the compute session pinning
`c`, `νμ`, `Γ` from Clebsch–Gordan/SDP data, and finally the A-vs-B
adjudication (lock-uniformity analysis) — the genuine research frontier.
