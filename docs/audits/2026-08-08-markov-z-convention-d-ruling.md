# The Markov parameter is convention D — owner ruling, and the forcing argument that backs it

**Bean:** `qou-3qrv` (the `mass`-channel dispute) · **PR:** #4834 ·
**Registry:** [`trace-convention-registry.md`](../coordination/trace-convention-registry.md)

## What was decided

The owner ruled **convention D**, `z = q^3/(q^2+1)`, for the Markov
stabilisation parameter of axiom M3. This closes the `mass` channel's
`disputed` status, which had stood since the registry was opened.

**The resolution moves the definition to meet production, not the reverse.**
The mass channel already ran D. So:

| | before | after |
|---|---|---|
| `mass` definitional | C | **D** |
| `mass` production | D | D (unchanged) |
| `mass` status | disputed | **agreed** |
| `binding` definitional | C (inherited from the line-5 pin) | C (stated in its own right) |
| `binding` production | C | C (unchanged) |

**No production number changes.** Not one `F_Bor` consumer, not `m_p`, not a
binding value. The −197 ppm figure attached to this dispute in the earlier
audits was always the cost of the *opposite* move — switching production from
D to C, the trace the paper named. That move was never made and is now moot.

## Why this is not "deciding by which value matches"

Bean `qou-3qrv` closed with a sharp constraint:

> The answer must not be read off which value matches CODATA.

That constraint is why the dispute stayed open for a day rather than being
closed by pointing at the 1.35 ppb round-trip. It is met here, by two
independent steps, neither of which touches a measured quantity.

### Step 1 — bar-covariance of M3 excludes C (new)

`def:bar-involution` sends `q ↦ q⁻¹` **and** `σᵢ ↦ σᵢ⁻¹`. Axiom M3 is

```
tr_M(x · σ_n) = z · tr_M(x)
```

and contains `σ_n`. So applying the bar involution to M3 does **not** compare
`z` with `z(q⁻¹)`: it compares `z` with the *negative-stabilisation*
parameter. The Hecke relation gives `σ⁻¹ = σ − h` exactly, hence
`tr_M(x·σ_n⁻¹) = (z − h)·tr_M(x)`, and the condition M3 supports is

```
bar(z) = z − h,        h = q − q⁻¹.
```

- **D satisfies it** — both sides are `1/(q³+q)`.
- **C violates it by exactly `h`** — C is invariant under the coefficient half
  alone, so `bar(z_C) = z_C`, and `z_C = z_C − h` forces `h = 0`.

Every prior treatment computed bar-invariance as `z(q⁻¹) = z(q)`, which
applies one half of the involution while holding the algebra fixed. That is
what made C look like the bar-respecting choice, and it is the same
half-an-involution defect PR #4826 found in three other places.

Sorry-free, generic `Field R`, in
[`MarkovParameterFibreRank.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/MarkovParameterFibreRank.lean):
`hecke_inv_eq_sub` (so `z − h` is *derived*, not assumed), `zRank_bar_sub`,
`zD_bar_sub`, `zC_bar`, `zC_ne_bar_sub`, `zC_not_fibre_family`.

**What step 1 does not do.** It does not select D. The law is one equation;
`bar_sub_of_bar_even` proves that if `g` is bar-even then `z_D + g` satisfies
it too, so the solution set is an affine family containing the whole fibre
family `{z_N}` and more. Step 1's force is the **exclusion of C** — and of
every bar-even candidate.

### Step 2 — TL faithfulness picks D out of what remains (already proved)

D is the unique normalised Markov trace on `H₃(q)` factoring through `TL₃` and
faithful on it: the Temperley–Lieb condition `y_(1³)(z) = 0` has exactly two
roots, `z = q` (degenerate — it kills the two-row block as well) and
`z = q³/(q²+1)` = D. Sorry-free in
[`MarkovTraceTLUniqueness.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/MarkovTraceTLUniqueness.lean),
proved under `qou-3qrv` §3.

### Why the pair settles what step 2 alone did not

Step 2 was never the weak half. The forcing audit was explicit that the open
half was step 2's **premise** — *does the mass fibre functor land in
`Rep(SU_q(2)) ≃ TL₃` or in full `H₃(q)`?* — and that the corpus contradicted
itself on it, the canonical scope note naming the full-Hecke trace while
production ran the TL one.

Step 1 does not answer that categorical question either. What it does is make
the answer unnecessary for excluding C: **whatever** the functor lands in, the
stabilisation parameter has to be bar-covariant with respect to the involution
M3 lives under, and C is not. So the dispute is resolvable without settling
the fibre-functor question, and it is resolved the same way the premise would
have resolved it.

The fibre-functor question itself remains open as a categorical fact. It is no
longer load-bearing for the convention.

## What was changed, and what was deliberately not

**Changed — the definitional layer.** Three blocks, chosen because each is a
*pin* rather than a use:

| file | why it was in scope |
|---|---|
| [`markov-axioms-primitive.md`](../../content/quantum-observable-universe/braids-and-knots/markov-axioms-primitive.md) | the registry names this block as the reason the mass channel read C. Now pins D, and carries the two-step forcing argument. |
| [`jones-markov-trace.md`](../../content/quantum-observable-universe/braids-and-knots/jones-markov-trace.md) (+ `.lean` docstring) | stated `z = 1/(q^{1/2}+q^{-1/2})` **and** that the trace computes the Jones polynomial. Those are inconsistent — the Jones-polynomial trace is D. Flipping `z` makes the block internally consistent, and the closing clause now says why `z` is forced. |
| [`notation-register-table3-data.md`](../../content/quantum-observable-universe/notation/notation-register-table3-data.md) | the symbol table, highest-visibility. Now gives D as the Markov parameter and names C as the binding channel's member, with the "convention-silent trace values are not comparable" rule attached. |

**Not changed — 68 further files carrying the C form.** By chapter:
`mass-theory` 26, `lean/QOU` 21, `mass-endomorphism` 7, `braids-and-knots` 4,
`appendix-transfer-matrices` 4, `observations` 3, `stochastic-mechanics` 1,
`predicted-spectra` 1, `content/values/registry.ts` 1.

These are **not** a mechanical find-and-replace, and treating them as one would
be a defect. The C form appears in at least three distinct roles:

> **Correction (same day).** An earlier revision of this audit, and of the
> registry rows it edits, described binding as simply "keeping C", as though
> that were settled. It is not. Open sibling PR #4766 argues C is excluded for
> **binding** too — the Wenzl bridge's own fractional rank inverts to
> `N_eff ≈ 2.5995`, not an integer — and beans the live question as
> `qou-rm47`: *which integer fibre dimension does the binding channel trace?*
> So binding **runs** C today, and this PR changes nothing there, but "binding
> is fine on C" is not a claim this audit makes or is entitled to.
>
> The two results converge rather than conflict, and this PR strengthens
> #4766's: `QOU.BraidKnot.zC_not_fibre_family` proves C is the parameter of
> **no** rank, for every `N`, functionally — turning a pointwise numerical
> inversion at one `q₀` into a theorem. `zRank_eq_qpow_div_qInt` supplies the
> bridge, proving this file's family is exactly `qᴺ/[N]_q`, the fibre quantum
> dimension #4766 derives from the bridge code.

1. **Genuinely C-specific and load-bearing on binding** — the Wenzl bridge
   (`y-lambda-closed-form-wenzl-bridge*`), `centered-hecke-variance-positive*`
   (whose whole statement is the Wenzl positivity regime
   $q^{1/2}+q^{-1/2} > 2$), `h3-markov-wenzl-weights*`. These **must stay C**.
   Flipping them would change binding numbers.
2. **Mass-channel definitional, should follow the pin to D** — e.g.
   `markov-trace-factorization`, `markov-trace-frobenius-selection`,
   `mass-endomorphism-tower`.
3. **Convention-neutral, needs a label not a value** — blocks that use `z`
   symbolically and merely illustrate it with the C form.

Each file needs a per-file channel call, and the registry's own discipline
(*"convention-silent trace values are not comparable"*) means the right output
for many of them is an explicit convention label rather than a changed formula.
Tracked as bean `qou-ql2a`. Doing this blind in one sweep is precisely the
failure mode the registry was built to catch.

The 21 open R5 validator warnings — Borromean tracers in `computations/` that
declare no convention — are the compute-side twin of the same backlog and were
already tracked before this ruling.

## Scope

- Scope **(a)** on everything downstream: no numeric conclusion changes,
  because no production path changes.
- Scope **(b)** on C as the M3 stabilisation parameter: this is a proved
  exclusion, and the named invariant is bar-covariance of axiom M3 under
  `def:bar-involution`. C remains a perfectly good normalised Markov trace and
  remains in production for the binding channel; what is excluded is C *as the
  bar-covariant stabilisation parameter*, which is the only claim step 1 makes.
- The `.qa.json` agent-judgement criteria for the edited block are refreshed
  separately; the block's script-reviewer criteria are re-run in this PR.

## Verification

CI auto-triggers are disabled repo-wide, so these are agent-run:

- `scripts/lean-verify.sh` on `MarkovParameterFibreRank.lean` — **exit 0**
  against the real import cone (6990 mathlib oleans restored from
  `lake-cache/qou-v4-24-0`). `sorry`/`admit`/`native_decide` greps **0**.
  `#print axioms` on all 8 new declarations →
  `[propext, Classical.choice, Quot.sound]`; `hecke_inv_eq_sub` needs only
  `[propext]`. No `sorryAx`.
- `trace_convention_registry_validate.py --selftest --lint-docs` — **PASS**,
  0 errors, 21 warnings (the pre-existing R5 backlog; unchanged count).
  R3 live-value checks confirm both C and D against the code that produces
  them; the selftest still catches all three recorded regression cases,
  including RC3, the synthetic silently-disputed-channel case.
- Render-QA grep battery on the edited `.md` — `$`/`$$`/braces balanced, no
  `\operatorname`, no list-parser hijack inside display math.
- Numeric check at the proton pin `q₀ = 1.1099785827513808`:
  `bar(z_D) − (z_D − h) = 0`, `bar(z_C) − (z_C − h) = h = 0.2090602987956393`.
