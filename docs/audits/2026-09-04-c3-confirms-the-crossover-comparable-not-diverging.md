# `c₃` confirms the crossover — the orders are comparable, not diverging

**Completes the question** left half-answered by #6559: do `c₂` **and `c₃`**
continue the cancellation? `c₂` was measured there (it does not — it overtakes
`c₁`). `c₃` is measured here. Beans `qou-brng` / `qou-pdg9`.

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
