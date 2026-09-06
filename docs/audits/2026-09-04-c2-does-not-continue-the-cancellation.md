# `c₂` does not continue the cancellation — it is the order at which the expansion stops being one

> **🛑 THE `c_k` BELOW ARE GROUPED-WORD VALUES — CORRECTED 2026-09-06 BY THEIR
> OWN AUTHOR.** `7db032fb48` (owner ruling, bean `qou-hu1f`) made the Borromean
> intra-nucleon ordering canonical, and these coefficients were computed on the
> old default without pinning it. They move — `c₁(⁴He)` by a factor of **37**,
> `259/128 → 7/128` — and `c₁(nn)` becomes **exactly 0**.
>
> **This document's CENTRAL FINDING DOES NOT SURVIVE.** Its headline is that the
> ratio column is monotone through 1 (`0.465, 0.540, 0.597, 0.998, 1.006, 1.464`).
> Under Borromean it is `0.817, 1.239, ∞, 4.905, 0.972` — not monotone, not
> ordered by `A`, already past 1 at `A = 2`. The load-bearing evidence, two `A = 3`
> cases *"agreeing to 0.8 %, so it is signal, not scatter"*, becomes `4.905` vs
> `0.972` — a factor of 5 apart. The `A = 4` crossover specifically is **untested**
> under Borromean (needs `P = 4`), so it is unsettled rather than disproved.
>
> Full table under both orderings, and what survives:
> [`2026-09-06-the-c1-c2-crossover-is-grouped-specific.md`](2026-09-06-the-c1-c2-crossover-is-grouped-specific.md).
> The `c₀` floor IS ordering-invariant, so everything resting on it is untouched.

> **🛑 NAMING CORRECTION (added 2026-09-04).** The `c_k` in this document are
> **NOT** the Q_β precision-ladder `c_k` that
> [`ck-dk-canonical-registry.md` §2](../coordination/ck-dk-canonical-registry.md)
> governs, and not that registry's `a_n` either. They are the `ℏ_q`-expansion
> coefficients of `Δtr = tr_M(W_free) − tr_M(W_atom)` — a **third object with no
> registry row**. The separation is not subtle: ladder `c₂ = −1`, `c₃ = −2.0693`;
> here `c₂ = +29.90`, `c₃ = +247.98`. The registry's `a_n` is excluded by its own
> 3-term recursion (predicts `a₂ = −1.52` against an actual `27.87`). This
> matters because the ladder's headline claim is about **the non-monotonicity of
> a `c_k` series**, and so is this document's — same glyph, same-sounding claim,
> unrelated objects. Full working:
> [`2026-09-04-c3-confirms-the-crossover-comparable-not-diverging.md`](2026-09-04-c3-confirms-the-crossover-comparable-not-diverging.md).
> The glyph came from PR #6492's probe; not checking the registry before
> propagating it across three documents is mine.

**Question asked:** do `c₂`, `c₃` continue the cancellation that takes the strongly
A-dependent leading order to a flat sum by `k = 11`?

**Answer for `c₂`, at A = 2, 3 and 4: no — and the reason is sharper than
"no".** The second-order term does not damp the A-dependence; weighted by the
physical `ℏ_q` it *overtakes* the first, passing equality at A = 3 and reaching
**1.46×** at A = 4. `c₃` is not measured. Beans `qou-brng` / `qou-pdg9`.

## Measured

Re-running `computations/probes/c1_leading_coefficient_derived_probe.py` on
`main` (it already computes `c₂` for the small cases; nothing new was written to
get these):

    case    A       c1        c2      c1·ℏ     c2·ℏ²    ratio
    pp      2   2.3750   11.1562   0.23532   0.10952    0.465
    pn      2   2.3125   12.5938   0.22913   0.12364    0.540
    nn      2   2.2500   13.5625   0.22293   0.13315    0.597
    T       3   2.5469   25.6641   0.25235   0.25195    0.998
    3He     3   2.6562   26.9609   0.26319   0.26468    1.006
    4He     4   2.0234   29.8965   0.20049   0.29350    1.464

at `ℏ_q = 1 − 1/q₀ = 0.099081716044258508` (proton pin, `q₀ = 1.1099785827513808`).
Exact values: `c₂ = 357/32, 403/32, 217/16, 3285/128, 3451/128, 15307/512`.

**The ⁴He row is a second run, at raised precision.** At the committed
`P_OF["4He"] = 3` the probe reports `c₂ = None` — `d.p` does not exceed 2 after
the seminormal quotients, so `a₂` is unavailable. Re-run at `P = 4`: `d.p = 3`,
`a₂ = 14271/512`, `c₂ = 15307/512`, 264 s. The `c₁` it returns is `259/128`,
identical to both the committed value and the closed form, which is the check
that the raised precision did not perturb anything else.

`c₁` was already known to be flat-then-decaying across A (2.31 at A = 2, 2.02 at
A = 4, 0.84 at A = 6). **`c₂` does not follow it down**: ~11–13.6 at A = 2,
~25.7–27.0 at A = 3, **29.9 at A = 4**. It roughly doubles from A = 2 to A = 3,
then largely flattens (+10.9 %) — so the divergence between the two orders comes
from `c₁`'s decay, not from continued growth in `c₂`. See §What that means.

## What that means

**The ratio column is the finding, and it is monotone through 1:**

    A = 2   0.465, 0.540, 0.597     second order is about half the first
    A = 3   0.998, 1.006            the two orders are EQUAL
    A = 4   1.464                   second order EXCEEDS the first by half

At A = 2 this looks like an expansion should. At A = 3 the two orders contribute
equally — two independent cases (different Z,N) agreeing to **0.8 %**, so it is
signal, not scatter. **At A = 4 the second-order term is 1.46× the first.**

An expansion whose second term has overtaken the first is not ordering anything.
So the honest reading is not "the cancellation continues at second order" nor
"it stops" — it is that **the `ℏ_q` expansion crosses over between A = 3 and
A = 4 and stops being an expansion**, and `c₁` is not the leading behaviour
beyond that point.

**What drives the crossing is `c₁`, not `c₂` — worth stating because it is the
opposite of the obvious reading.** From A = 3 to A = 4:

    c1:  2.6562 -> 2.0234   -23.8 %
    c2: 26.9609 -> 29.8965  +10.9 %

`c₂`'s growth has largely flattened by A = 4; the ratio rises because **`c₁` is
falling**. That is the same decay already recorded for `c₁` (2.31 at A = 2, 2.02
at A = 4, 0.84 at A = 6). So the crossover is not "the second order blows up" —
it is that the *first* order decays away while the second does not follow it
down. Anyone reading the ratio column alone would get the mechanism backwards.

This is consistent with, and independently corroborates, the convergence defect
recorded in PR #6427: `|uic|` at ⁴He runs 1.52 → 2.15 → 3.71 → 5.67 → 8.20 across
`k = 7…11` with the increments still *growing*. Two different objects, two
different methods, the same conclusion — the series is not converged in the
region where the physics is being read off.

## The change of variable, verified rather than assumed

The probe reports `c₂ = a₁ + a₂` where `aₖ` are coefficients in `ε = q − 1`.
That is correct and worth writing out, because it is the kind of step that is
easy to take on trust:

    ℏ = 1 − 1/q = (q−1)/q = ε/(1+ε)   ⟹   ε = ℏ/(1−ℏ) = ℏ + ℏ² + ℏ³ + …

    f = a₀ + a₁ε + a₂ε² + …
      = a₀ + a₁(ℏ + ℏ² + …) + a₂(ℏ + …)² + …
      = a₀ + a₁ℏ + (a₁ + a₂)ℏ² + …

so the `ℏ²` coefficient is `a₁ + a₂`. Checked independently here; it is not
being carried over from the source's own claim.

## Scope, and what is NOT established

**Scope-(a), and narrower than the question asked.**

- **`c₃` is not measured.** Nothing here says anything about third order. The
  question asked about `c₂` *and* `c₃`; only `c₂` is answered.
- **A = 4 is now in hand — the trend is three A values, not two.** An earlier
  revision of this document flagged two points as a thin trend (the weakness
  that sank the `E ≈ 5.4 × C(A,2)` target on #6427). That caveat is **retired**:
  the raised-precision run landed and A = 4 is measured. It is a stronger
  result than the caveat feared, since it is the point that crosses 1.
- **`c₂` is measured at A = 2, 3, 4 only.** Nothing here constrains A ≥ 5, and
  A = 6 is out of reach by this route (`n = 3A = 18` strands against ⁴He's 12,
  and ⁴He at `P = 4` already takes 264 s).
- **This does not contradict #6427's flatness result.** That measured the summed
  `unified_iterative_correction` at matched truncation and found the *total*
  flat. This measures individual coefficients of a different expansion. A
  non-convergent series can still have a flat partial sum; the two facts sit
  together and neither explains the other.

## Provenance of the numbers

**Five of the six `c₂` values are not new compute; the ⁴He one is.** Re-running
`main`'s probe unchanged reproduced **8 assertions, all passed**, and left the
committed witness untouched (`[unchanged — kept on-disk commitSha for
staleness]`) — so the `c₁` column is byte-identical to what `main` already
records, and the A = 2 and A = 3 `c₂` values are what that same run prints.

**The ⁴He `c₂` is genuinely new**: it required a second run at `P = 4`, since the
committed precision returns `None` there. It is stated separately above rather
than folded into the same provenance claim, because "re-ran an existing probe"
and "raised its precision to get a value it does not normally produce" are
different acts and only the first is reproducible by running `main` as-is. Its
`c₁` agreeing with the committed `259/128` is what licenses putting the two on
one line.

## What would settle the rest

**A = 4 is done** (above). What remains open:

- **`c₃`.** The question asked about `c₂` *and* `c₃`; only `c₂` is answered. If
  the crossover reading is right, `c₃·ℏ³` at A = 4 should be comparable to the
  other two rather than small. That is the direct test, and it needs `P = 5` at
  ⁴He — the same lever, one notch further.
- **Whether `P_OF["4He"] = 3` should be raised on `main`.** It is committed at
  the value that yields `c₁` and stops. Raising it to 4 costs 264 s and makes
  `c₂` available at A = 4 permanently. **Not changed here** — that is the
  probe-owner's call (`qou-pdg9`), and this branch touches no code.

**A note on running it, because it cost a run here.** `/tmp` contained a stale
`inspect.py` from a prior session, which shadows the stdlib module and makes
`import mpmath` die with `AttributeError: module 'inspect' has no attribute
'signature'` — nothing to do with this probe. Any script placed in `/tmp` picks
it up via `sys.path[0]`. It has been renamed to `inspect.py.shadowing-landmine.bak`;
run from a clean directory regardless. This is the third stdlib/module shadowing
incident in this session's environment (an earlier one was a stray
`pyhecke_native` `.so` in the scratchpad), so it is worth checking first when an
import fails in a way that has no relation to the code being run.
