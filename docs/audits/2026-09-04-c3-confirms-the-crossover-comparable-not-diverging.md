# `c₃` confirms the crossover — the orders are comparable, not diverging

> **🛑 THE `c_k` BELOW ARE GROUPED-WORD VALUES — CORRECTED 2026-09-06 BY THEIR
> OWN AUTHOR.** `7db032fb48` (owner ruling, bean `qou-hu1f`) made the Borromean
> intra-nucleon ordering canonical, and these coefficients were computed on the
> old default without pinning it. They move — `c₁(⁴He)` by a factor of **37**,
> `259/128 → 7/128` — and `c₁(nn)` becomes **exactly 0**.
>
> **Convention-scoped, not refuted:** `c₃` has not been re-measured under
> Borromean (it needs `P = 5`). **UPDATE 2026-09-06 — `c₃` HAS now been re-measured under Borromean
> at `A = 2` and `A = 3`, and THIS DOCUMENT'S CONCLUSION SURVIVES** (bean
> `qou-yaig`). Four of five `c₃ℏ³/c₂ℏ²` ratios are well below 1 — `0.4023`,
> `0.6817`, `0.8087`, `0.5295` — so the third order does NOT overtake the
> second: the expansion overshoots once, at order 2, and then settles. The
> sole exception is `nn` at `10.7008`, and that is the degenerate case where
> `c₁ = 0`, which has no scale for later orders to be measured against.
>
> Its premise fared differently: #6559's crossover reading is **split** — the
> ENDPOINT survives (`c₂(⁴He) = 439/512`, ratio `1.5535 > 1`), the LOCATION
> does not (already above 1 at `A = 2` and `A = 3`), the argument stays
> refuted (#6931).
>
> **`A = 4` — where this document's interest lies — is now MEASURED, and
> THIS DOCUMENT'S CONCLUSION HOLDS THERE TOO**: `c₃(⁴He) = 1329/256`, ratio
> **`0.5999 < 1`** (352 s at `P = 5`, three controls reproduced). Its grouped
> counterpart was `0.8219`, likewise below 1 — so the conclusion is robust to
> the convention change even though every number moved. The `c₃` column also
> turns out to have **no `A` trend at all** (`0.4023, 0.6817, 0.8087, 0.5295,
> 0.5999`), which is sharper than "comparable": the ratio is not drifting
> toward 1 as `A` grows. Table and caveats:
> [`2026-09-06-c3-under-borromean-the-second-order-is-the-only-bad-one.md`](2026-09-06-c3-under-borromean-the-second-order-is-the-only-bad-one.md).
>
> Full table under both orderings, and what survives:
> [`2026-09-06-the-c1-c2-crossover-is-grouped-specific.md`](2026-09-06-the-c1-c2-crossover-is-grouped-specific.md).
> The `c₀` floor IS ordering-invariant, so everything resting on it is untouched.

**Completes the question** left half-answered by #6559: do `c₂` **and `c₃`**
continue the cancellation? `c₂` was measured there (it does not — it overtakes
`c₁`). `c₃` is measured here. Beans `qou-brng` / `qou-pdg9`.

## 🛑 NAMING — these `c_k` are NOT the Q_β ladder `c_k`, and not the z-recursion `a_n` either

**`c_k` is the most overloaded glyph in this corpus**, and
[`ck-dk-canonical-registry.md` §2](../coordination/ck-dk-canonical-registry.md)
exists to keep its meanings apart. This document, and its two predecessors
(`2026-09-03-c1-leading-order-vs-uic-flatness.md`,
`2026-09-04-c2-does-not-continue-the-cancellation.md`), use `c_k` for an object
that has **no row in that registry**. Read them with this note.

**What these `c_k` are here:** the `ℏ_q`-expansion coefficients of the trace
difference `Δtr = tr_M(W_free) − tr_M(W_atom)`, at a fixed nucleus. The name
comes from `c1_leading_coefficient_derived_probe.py` (PR #6492), whose docstring
defines `c₁ = lim (Δtr − c₀(A))/ℏ_q`. That probe mentions the ladder and the
registry **zero times**.

**Measured separations — this is not a stylistic quibble:**

| | `c₂` | `c₃` |
|---|---|---|
| Q_β precision ladder (registry §3, governed) | `−1` | `−2.0693` |
| **this document** | **`+29.8965`** | **`+247.98`** |

Different sign, different magnitude, different object.

**They are also NOT the registry's `a_n`** ("ℏ-Taylor coefficients of `Δtr_M`"),
which is the nearest-looking row and which a reader would reasonably land on.
That `a_n` satisfies a 3-term recursion
`a_{n+1} = −3n/(2(n+1))·a_n − (2n−1)/(4(n+1))·a_{n−1}`. Tested against the
ε-Taylor coefficients here (⁴He: `a₀ = 7/128`, `a₁ = 259/128`,
`a₂ = 14271/512`, `a₃ = 97389/512`):

    n=1:  predicted a₂ = −1561/1024 = −1.5244   actual = 27.8730   NO
    n=2:  predicted a₃ = −7265/256  = −28.3789  actual = 190.2129  NO

So it is a **third object**, distinct from both registry entries.

**Why this matters beyond bookkeeping.** The corpus has already renamed one
colliding family off `c_k` — `cl_k`, the cluster/Ursell coefficients, renamed
2026-08-07 *"because it sat within ~12 % of the ladder `c_3 = −2` with no signal
they were unrelated objects"*. And the confusable claim here is not hypothetical:
the AGENTS.md ladder banner discusses **the non-monotonicity of a `c_k` series**
(N=4 → N=5) as a fit signature, while this document discusses **the
non-monotonicity of a `c_k` series** (order 2 → 3) as a convergence property.
Same glyph, same-sounding claim, unrelated objects.

**Disposition.** Renaming is the probe owner's call (`qou-pdg9`) since the name
originates in their probe and a rename touches their code, their witness and its
assertion names — not something to do unilaterally from an audit doc. What is
done here is to state the separation wherever the symbol is used. A registry row
for this object, or a rename off `c_k`, is the durable fix.

**My share of this.** I inherited the glyph from #6492, but propagating it into
three audit documents and two merged PRs without running the registry check is
mine — AGENTS.md says plainly to *"check registry §2 before asserting a property
of `a₁`/`Φ₂`/`c_k`-like symbols"*, and I did not, across the whole arc.

## Measured — `c₃` at A = 4

    P=5   d.p=4   c1 = 259/128 (gate PASSED)
                  a2 = 14271/512
                  a3 = 97389/512
                  c3 = 126967/512 = 247.98242…       314 s

Weighted by `ℏ_q = 0.099081716044258508` (proton pin):

    order        c_k       c_k·ℏ^k    vs previous order
      1       2.0234       0.20049
      2      29.8965       0.29350         1.464
      3     247.9824       0.24121         0.822

    sum of the three orders = 0.73520

## The finding, and where it differs from what I predicted

**All three orders contribute comparably at A = 4** — 0.200, 0.294, 0.241,
spanning a factor of **1.46** between largest and smallest. There is no leading
order at A = 4. That is the crossover of #6559 confirmed at third order.

**But it peaks at order 2 and comes back down.** `c₃·ℏ³` is **0.822×** `c₂·ℏ²`,
not larger.

#6559's PR body predicted that if the crossover reading were right, `c₃·ℏ³`
"should be comparable to the other two rather than small". It is comparable, so
the prediction holds as stated — **but that prediction would also have been
satisfied by monotone growth, and the data is not monotone.** The honest
statement is the narrower one:

> over orders 1–3 at A = 4 the terms are **comparable**, not **diverging**.

"The expansion blows up" is *not* supported. What is supported is that the
`ℏ_q`-ordering carries no information at A = 4 — which is the claim that
matters for reading `c₁` as a leading behaviour, and is weaker than a
divergence claim. Three orders cannot distinguish a series that has plateaued
from one that will turn over and converge slowly; that would need `c₄`.

## Two checks that make the number trustworthy

**The `c₁` gate.** `c₁` comes back `259/128` at `P = 5` — identical to `P = 4`,
to the committed value, and to the closed form. Raising precision perturbed
nothing else, which is the condition under which the new coefficients mean
anything.

**`a₂` reproduces across independent precisions.** The `P = 4` run gave
`a₂ = 14271/512`; the `P = 5` run gives the same `14271/512`. Two different
truncations of the same series agreeing exactly on a shared coefficient is a
real cross-check, not a restatement.

## The change of variable was derived, not guessed

`c₂ = a₁ + a₂` is stated by the probe. `c₃` is **not**, and guessing it is
exactly how a wrong number enters. It was derived symbolically from
`ε = h/(1−h) = h + h² + h³ + …`:

    eps    = h + h² + h³
    eps²   =     h² + 2h³
    eps³   =          h³

    ⟹  c₁ = a₁ ,  c₂ = a₁ + a₂ ,  c₃ = a₁ + 2a₂ + a₃

and the script **asserted that this same derivation reproduces `c₁ = a₁` and
`c₂ = a₁ + a₂`** before using the `c₃` row — so a bad change of variable would
have aborted the run rather than produced a plausible-looking `c₃`.

## Δtr has just been refuted as the binding law — what that does and does not do to this

**Landed while this was open:** [#6611](https://github.com/litlfred/qou/pull/6611)
(`0537eb98cf`) closes `B = Q_β·Δtr` — **p5–p95 1592× at its own optimal scale** —
and derives the replacement `B = E₀·log(tr_free/tr_atom)` at **1.225×**, same
bond factors, zero fitted constants.

**This document's claims are unaffected in truth-value.** They are about the
*expansion structure* of `Δtr` — whether `c₁` is a leading behaviour at A = 4 —
not about whether `Δtr` is the binding law. The scope note below already said
"says nothing about whether the underlying physics is right", and that now reads
as load-bearing rather than boilerplate.

**But the motivation has moved, and a later reader should be told so.** The
object expanded here is no longer the candidate binding law. The survivor is a
**different function of the same two traces**: `Δtr = tr_free − tr_atom` is a
difference; `log(tr_free/tr_atom)` is a log-ratio. Nothing measured here
transfers to it — the coefficients of a difference are not the coefficients of a
log-ratio.

**A connection worth flagging, stated as a suggestion and not a finding.** The
two results are consistent in a way that may not be coincidence: an object whose
`ℏ_q` expansion has **no leading order at A = 4** (this document) is a poor basis
for a law, and `Δtr` failed as one by 1592× (#6611). That is *suggestive* of a
structural reason for the failure — but it is **not established here**, and the
honest caveats are:

- #6611's failure is measured against **AME binding energies**; this document's
  crossover is about a **series ordering**. No derivation links them.
- The failure is at all scales including A = 2 and A = 3, where this document
  finds the expansion *does* still order (ratios 0.47–0.60 at A = 2). So the
  crossover cannot be the whole explanation.

Whether `log(tr_free/tr_atom)` has a better-ordered expansion at A = 4 is the
obvious next question and is **not answered here**.

## Scope, and what is NOT established

- **One nucleus.** `c₃` is measured at **A = 4 only**. Nothing here says how
  `c₃` behaves across A, which is the question `c₂` was interesting for. The
  A = 2 and A = 3 cases would each need their own raised-`P` run.
- **Three orders, not a limit.** No claim is made about `c₄` or the radius of
  convergence. Comparable-over-three-orders is what was measured.
- **Not a refutation.** Scope-(a) throughout: this is about one expansion of one
  computational object, and says nothing about whether the underlying physics is
  right.
- **`P_OF` unchanged on `main`.** Getting `c₂` needs `P = 4` and `c₃` needs
  `P = 5` at ⁴He, against the committed `3`. Raising it is the probe owner's
  call (`qou-pdg9`); this branch touches no code.

## Cost, for whoever runs `c₄`

    P = 3   (committed)   c2 = None          — d.p does not exceed 2
    P = 4                 c2 available       264 s
    P = 5                 c3 available       314 s

So the marginal cost per order is currently mild at A = 4. `c₄` would need
`P = 6`. The expensive direction is **A**, not `P`: A = 6 is `n = 18` strands
against ⁴He's 12 and is out of reach by this route.
