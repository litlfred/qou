---
# qou-nmqd
title: q-GoL proof cites the wrong stability threshold (1/phi^2 belongs to P_77, not Phi) and asserts unitarity the Hecke eigenvalues forbid
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T16:24:07Z
updated_at: 2026-08-30T03:49:15Z
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


## 2026-08-29 — RESOLVED. Owner ruled: scope the 't Hooft reading

The open item this bean left with the author ("whether the 't Hooft reading
survives without energy conservation") was decided: scope it. Done in the
interpretation block.

**What made it a real scope change rather than a hedge.** 't Hooft's mechanism
is not "a CA is quantum-mechanics-like"; it is that a deterministic evolution
PERMUTES a distinguished ontological basis, so the induced operator on that
span is automatically unitary and generates a Schrodinger flow. Unitarity is
the load-bearing step, and Finding 2 removed it for `q != 1`. So the
realization claim does not weaken gradually with `q` — it holds at `q = 1` and
is simply unestablished away from it.

**And the sharp consequence, now stated in the block:** `q = 1` is exactly
where the q-Toffoli degenerates to the ordinary Toffoli. So the one place the
't Hooft embedding goes through is the one place the q-deformation contributes
nothing — the classical limit realizes Pena et al.'s construction. The block
now says that outright instead of leaving a reader to notice it.

The Markov-trace-as-coarse-graining sentence was scoped the same way, from an
achievement ("replaces ad hoc information loss") to a suggestion with its
motivation stated and its status marked: a degenerate form has a radical and
quotienting by a radical is an information loss rather than a postulate of one,
but no such identification is derived. Observation, labelled as one.

All five findings in this bean are now either fixed in content (1, 3, 4, 5) or
resolved by ruling (2, and this). Nothing left open on it.


## REOPENED 2026-08-30 — my own fix was convention-C, and it is refuted under D

The merge from `main` brought in sibling bean `qou-3j5m` (PR #6033), which
derived the two Toffoli amplitudes in convention D. Against those, the fix
recorded above is wrong in its conclusion, not merely under-scoped.

**The merge was textually clean and that is the trap.** `qou-3j5m` touched
`toffoli-*.md`; I touched `q-game-of-life*.md`. Disjoint file sets, no
conflict, no signal. The contradiction is visible only by reading what my
proof **cites** — the two edits do not collide, they disagree.

**What I had written.** The proof reads the region off three operator zeros —
`q_⋆ = 1/φ² ≈ 0.3820` for `P_77`, a phase reversal at `q_Φ ≈ 0.4656`, and
`q = 1` — and concludes the common region is `q > 1`, with `q₀` safely inside.

**All three are convention-C.** Under `z_D = q³/(q²+1)`:

    P_77^D(q) = q³(q⁴+1)/(q²+1)²
    Φ^D(q)    = −(q−1)(q+1)(q⁶+q⁴+2q²+1) / (2q(q²+1)²)

`P_77^D` has **no positive root** — numerator and denominator are positive for
every `q > 0` — so the golden-ratio threshold is a property of the excised
frame, not of the gate. `Φ^D` carries its sign entirely in `−(q−1)`, the
sextic having no positive real root, so `Φ^D > 0` **exactly on `0 < q < 1`**.

**So the stability region is `0 < q < 1`, not `q > 1`, and the substrate is
where the q-AND is NEGATIVE:** `Φ^D(q₀) = −0.143769370004`, reproducing main's
`−0.1438`. Verified at 60 dps against the proton pin,
[`computations/probes/qgol_stability_region_convention_d.py`](../computations/probes/qgol_stability_region_convention_d.py),
5/5 assertions. The convention change does not move the arithmetic — it moves
which **side** of `q = 1` the amplitude is positive on.

Corrected at four sites, not the two that named a number: the statement's
stability condition, the proof, the interpretation's summary, and the
statement's reversibility item (which said invertibility "holds throughout the
stable regime" — true, but now ambiguous, since it holds for every `q > 0` and
does not depend on the amplitude signs at all).

### 🟡 Open, and it is the author's — stated as open in the block

**The decision.** The stability condition is written as *both amplitudes
strictly positive*. Is strict positivity what a reversible cellular automaton
actually requires, or is non-vanishing?

- **What it means.** `Φ > 0` vs `Φ ≠ 0` as the condition on the q-AND
  amplitude — the number that says how strongly the two control strands flip
  the target.
- **Why it matters here and nowhere else.** The two agree everywhere except in
  sign, and the substrate is exactly where they disagree: `Φ^D(q₀) < 0`, so
  non-vanishing **holds** at `q₀` (it holds for every `q ≠ 1`) and positivity
  **fails**. Opposite verdicts on the same point.
- **The corpus already uses both.** The universality argument in
  `rem:toffoli-q-and` turns on `P_{7,6}(q) ≠ 0` — *"since `P_{7,6}(q) ≠ 0` for
  every `q ≠ 1`, the substrate's braiding dynamics ... is computationally
  universal away from the classical limit"*. `prop:q-game-of-life` uses
  positivity. They are not the same condition and cannot both be the criterion.
- **Cost of each.** Neither is a compute job; both are one paragraph. Adopting
  non-vanishing restores the substrate to the stable regime and makes the
  q-GoL proposition consistent with the universality claim. Keeping positivity
  means the automaton is stable only in `0 < q < 1`, i.e. **not** at the
  physical substrate, which is a substantive statement about the framework and
  would want saying plainly.
- **Blast radius.** `q-game-of-life.md`, `-proof.md`, `-interpretation.md`, and
  whatever cites the "stable regime". No compute consumer: the region is prose,
  not a wired number.
- **Default if you say nothing.** Nothing breaks. The blocks now state the
  measured D-frame facts and mark the choice open, so the corpus is honest
  either way; it simply does not assert a stability regime.

**My judgement, not a finding:** non-vanishing. It is what the universality
argument three files away already uses, and it is the condition that makes the
automaton's own reversibility argument — which needs invertibility, and `Toff_q`
is invertible for every `q > 0` — line up with the stability claim. But
positivity may encode something about the amplitude's interpretation that I do
not have, which is why I did not just pick it.
