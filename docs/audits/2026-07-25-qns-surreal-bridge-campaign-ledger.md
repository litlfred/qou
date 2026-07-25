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

## Next (this session)

Promote the probe's Model-B finding to a theorem: *fixed Gevrey data ⇒ grade-0
regular on the super-classical side* (`gevrey_grade_zero`), shrinking the open
content to non-Gevrey (sustained/forced) spectra only. Remaining open after
that: whether the QOU's internal q-NS dynamics preserves the Gevrey class for
smooth data as `q → 1⁺` (Gevrey persistence — the analytic core of
`thm:q-ns-wellposedness`), and the sustained-forcing regime.
