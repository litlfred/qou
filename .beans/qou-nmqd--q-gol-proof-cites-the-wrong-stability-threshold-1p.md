---
# qou-nmqd
title: q-GoL proof cites the wrong stability threshold (1/phi^2 belongs to P_77, not Phi) and asserts unitarity the Hecke eigenvalues forbid
status: todo
type: task
priority: normal
created_at: 2026-08-29T16:24:07Z
updated_at: 2026-08-29T16:24:57Z
---

Found by adversarial review of the q-GoL blocks on `main` (owner asked for a
review of recent landings). Every number below is measured at 40 dps with
mpmath; the upstream block was read before attributing any error.

## Finding 1 (CRITICAL) — the proof's threshold is refuted by direct evaluation

`q-game-of-life-proof.md`:

> The stability condition requires `P_{7,7}(q) != 0` and `Phi(q) != 0`. Both
> inequalities hold for `q > 1/phi^2` by direct evaluation
> ([Toffoli LP-stability]).

**False, and the cited block says so itself.**
[`toffoli-lp-stability.md`](../blob/main/content/quantum-observable-universe/information-theory/toffoli-lp-stability.md)
lists **three distinct** operator zeros and assigns them to different
amplitudes:

| zero | what vanishes there |
|---|---|
| `q_* = 1/phi^2 = (3-sqrt5)/2 ~ 0.38197` | `P_{7,7}` |
| `q_Phi ~ 0.4656` | `Phi` reverses sign |
| `q = 1` | the q-AND vanishes |

and names the stability region as **`q > 1`**. The proof collapses the three
into one and picks the threshold belonging to the *other* amplitude.

Measured `Phi(q) = (q-1)(q^{3/2}+q^{1/2}-1)(q^{3/2}+q+1) / (2(q+1)^2)`:

```
q = 0.30       Phi = +0.0873272     (BELOW the claimed threshold, yet positive)
q = 0.381966   Phi = +0.0381966
q = 0.40       Phi = +0.0289851
q = 0.50       Phi = -0.0124930     <- counterexample: q > 1/phi^2, Phi < 0
q = 0.90       Phi = -0.0306085
q = 0.99       Phi = -0.0036812
q = 1.00       Phi =  0 exactly
q = 1.10997858 Phi = +0.0495377     (matches the LP block's quoted ~0.0495)
```

So `1/phi^2` is not a bound on `Phi`'s positivity from either side: `Phi` is
positive below it and negative above it. `Phi`'s only positive roots are
`~0.46557` (the root of `s^3+s-1` at `s=sqrt q`) and `1` — exactly the two the
LP block names.

**Not a typo in the formula.** I first hypothesised that `q^{3/2}+q^{1/2}-1`
was a mis-transcription of `q+q^{1/2}-1`, whose root IS `1/phi^2` exactly
(`s^2+s-1=0` at `s=1/phi`). Checking the source refuted that: the LP block
independently reports `q_Phi ~ 0.4656`, which is the 3/2 form's root, and its
`Phi(q_0) ~ 0.0495` matches the 3/2 form to 4 digits. **The formula is right;
the proof's threshold is wrong.** Recording the refuted hypothesis because it
is the plausible-looking wrong fix.

Same error in `q-game-of-life-interpretation.md`: *"establish the golden-ratio
threshold `q = 1/phi^2` bounding stability"* — it bounds nothing about
stability.

Note also `.md` statement vs proof disagree on the *predicate*: the statement
requires the amplitudes **strictly positive**, the proof proves only
**non-vanishing**. The statement's `q > 1` is the correct region; the proof
establishes something weaker at the wrong threshold.

## Finding 2 (CRITICAL) — unitarity does not follow, and the eigenvalues forbid it

Statement item 4 and the proof both assert `Toff_q^dagger Toff_q = I` and build
q-energy conservation on it (`H = i hbar_q ln U / t_P`).

The Hecke generator has eigenvalues `q` and `-q^{-1}` (AGENTS.md §7a). At
`q_0 = 1.10997858` those are `1.10998` and `-0.90092`, of modulus `!= 1`. A
unitary operator has every eigenvalue on the unit circle, so `sigma_i` is not
unitary in ANY inner product for `q != 1`.

What the proof actually establishes is **invertibility** —
`sigma_i^{-1} = sigma_i - (q-q^{-1})`, "so every `sigma_i` is a unit" — which is
strictly weaker and does not give `U^dagger U = I`.

The appeal to "unitary with respect to the Markov trace form" does not rescue
it: under production convention D that form is **singular**, as the same
`toffoli-lp-stability` block now states in its own item 3 (*"Under the
production convention D the Markov-Gram form is singular"*). A degenerate form
has no unitary group.

Note this is the same defect class as `2bbc396416` ("correct the false Hecke
involution claim in q-GoL reversibility"), one step over: that commit fixed the
*involution* claim and left the *unitarity* claim standing.

## Finding 3 (MAJOR) — the universality citation cannot support the claim

> Universality follows from Bennett [bennett1973]. ... Adding Hadamard gates
> promotes this to universal quantum computation [fredkin1982, toffoli1980].

Toffoli+Hadamard universality for **quantum** computation is Shi (2002) /
Aharonov (2003). `fredkin1982` and `toffoli1980` are classical
reversible-computation papers predating that result by two decades and cannot
carry it; `bennett1973` is logical reversibility, not Toffoli universality.

Separately, even correctly cited the theorem is about the **standard** Toffoli.
For `Toff_q` with amplitude `Phi(q) != 1` universality needs its own argument —
particularly given Finding 2.

## Finding 4 (MINOR) — ambiguous denominator

`... / 2(q+1)^2` parses two ways in prose. The intended reading is
`/(2(q+1)^2)` — confirmed because only that reading reproduces the LP block's
`Phi(q_0) ~ 0.0495`. Should be bracketed.

## Finding 5 (MAJOR, framing) — "subsumes" is an overclaim

`interpretation.md`: *"This paper subsumes their construction"* (Pena et al.).
Their construction is unitary; per Finding 2 the q-deformed object is not, at
`q != 1`. A construction that loses unitarity does not subsume one that has it.
Scope the claim to the `q -> 1` limit, where the two agree by construction.

## Not fixed here

Filed rather than patched: Finding 2 changes what the proposition can claim, so
it is a content decision, not an edit. Findings 1, 4 and the Finding 3 citations
are mechanical and could ride on any info-theory pass.
`q-game-of-life.ts` also carries `lean: { validation: "not_checked" }`.
