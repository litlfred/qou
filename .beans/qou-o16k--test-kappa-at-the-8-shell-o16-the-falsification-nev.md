---
# qou-o16k
title: 'Test κ at the 8-shell (¹⁶O) — the falsification the anchor-identified form has never faced'
status: in-progress
type: task
created_at: 2026-08-10T02:32:00Z
updated_at: 2026-08-10T03:05:00Z
---

## Result (2026-08-10) — the test is sharper than expected, and partly blocked

[`probe_kappa_shell8_excess_convention.py`](../computations/probe_kappa_shell8_excess_convention.py)
→ `kappa-shell8-excess-convention.witness.json`, 4/4 assertions. No fit, no
tuning; arithmetic only.

**The κ fit is convention-blind by construction.** The corpus carries two
inequivalent definitions of the excess `(n_pp − n_nn)`:

| | definition | in Z |
|---|---|---|
| **C1** | `def:canonical-braid-interface-composition` — `n_pp = max(0, Z−1)` | linear |
| **C2** | `prop:derived-mass-formula-light-isotopes` — `n_pp = Z(Z−1)/2` | quadratic |

They **agree on every anchor κ has ever seen** and diverge everywhere else:

| nuclide | Z | N | shell | C1 | C2 | C2/C1 | role for κ |
|---|---|---|---|---|---|---|---|
| ³He | 2 | 1 | 2 | 1 | 1 | 1× | cross-check |
| ³H | 1 | 2 | 2 | −1 | −1 | 1× | cross-check |
| ⁴He | 2 | 2 | 2 | 0 | 0 | — | identification |
| ¹⁵O | 8 | 7 | 8 | 1 | **7** | **7×** | never tested |
| ¹⁵N | 7 | 8 | 8 | −1 | **−7** | **7×** | never tested |
| ³⁹K | 19 | 20 | 20 | −1 | **−19** | **19×** | never tested |

So the fit that fixed κ **could not have distinguished the two conventions** —
it lives entirely inside the region where they coincide. Since `kappa_closed`
carries **no shell index** (it is a function of `q` and `m_e` alone, verified),
the conjecture predicts one constant for every shell, and that constant
multiplies an excess that differs by 7× at shell 8 depending on which
convention is meant. The block does not say which.

That is a second defect, independent of the anchor-identification one: even
granting the closed form, **the conjecture is not yet a determinate statement**
until the convention is named.

## Producer recovered — and it reframes the test

The removed `probe_kappa_categorical_h7a_closed.py` **is** recoverable: it lived
at `folio-assistant/computations/` before the miga migration, and the witness's
`scriptCommitSha` (`4e17b6b4b5`) fetches into a shallow clone. Three things it
settles:

**1. The normaliser is explicitly A=3-specific, so κ was never a shell-universal
constant even by its own construction.** The producer's own words:

> `[2]_q · [3]_q` — the quantum dimension of `V_2 ⊗ V_3` (the LR fusion of the
> two relevant magic-shell channels **for A=3 anchors**)

But `kappaClosed q m_e` takes no shell index. At shell 8 the "relevant
magic-shell channels" are different channels, so the bracket product should be a
*different* product — the construction says so, and the Lean does not. **This
changes what the 8-shell test is.** It is not "does the same constant hold at
shell 8" (which the construction never claimed); it is *"recompute the normaliser
from the shell-8 channels and see whether the resulting slope matches"*. That is
a derivation-shaped test rather than a fit-shaped one, and it is the better
version of this bean.

**2. The producer never computed the excess or the binding.** It evaluates the
closed form and compares it to a constant. So the decomposition is not hiding in
it — the empirical κ traces to a *"PR #656 v6 single-magic anchor fit"* that is
not in the tree in any form.

**3. The whole cited reference chain is gone from the corpus.** The producer
cites `def:hecke-e0`, `prop:h7a-magic-shell-quantum` and
`prop:magic-shell-coupling-witness`; grep over `content/**/*.ts` returns
**0 files for each**. The `.md` still speaks of the "H7a energy quantum" as a
named structure whose defining block no longer exists. The block's only surviving
`uses[]` edge is `prop:compound-beta-shell-calibration`.

Also worth recording for the demotion's file: the producer's docstring asserted
*"This closes user work-list item #4: κ derivation — **no empirical fit, purely
from QOU substrate parameters**"* — the overclaim the demotion corrects, now
documented at its source rather than inferred.

## Blocked, and stated rather than guessed

Extracting an *observed* slope at the 8 shell needs a binding decomposition that
**exists nowhere in the tree** — see finding 2 above; it traces to a PR #656 fit,
not to any surviving producer. Checked: the naive route (mirror-pair ΔB over
Δexcess for ³He/³H) gives −0.382 MeV, about 2.8× off `κ_emp = −1.0708`, so κ is
plainly not a bare mirror-pair slope and other terms are in play.
**Reconstructing the decomposition by guesswork would be a new fit** — precisely
what the demotion was about. Blocker recorded instead.

## Step 1 done — the normaliser's index rule is undetermined too, by 32×

[`probe_kappa_normaliser_index_rule.py`](../computations/probe_kappa_normaliser_index_rule.py)
→ `kappa-normaliser-index-rule.witness.json`, 4/4. **No rule selected** —
choosing one on the numbers would be a new fit.

The producer's phrase fixes the normaliser's *value* at A=3 but not its *rule*.
At least three readings reproduce `[2]_q[3]_q` there:

| | index rule | at A=3 | at ¹⁵O (A_magic=8, A=15) | κ there |
|---|---|---|---|---|
| **R1** | `(A_magic, A)` | (2,3) | `[8]_q[15]_q` = 195.7 | −0.0335 |
| **R2** | fixed `(2,3)`, sl₂ irreps | (2,3) | `[2]_q[3]_q` = 6.12 | −1.0704 |
| **R3** | `(A_magic, A_magic+1)` | (2,3) | `[8]_q[9]_q` = 92.7 | −0.0707 |

All three **agree exactly at A=3** — the only place κ has ever been evaluated —
and spread by **32×** at the 8 shell, 1700× at the 20 shell.

## The two ambiguities compound: the ¹⁵O prediction is undetermined by 224×

The index rule (3 readings) and the excess convention (2 readings) are
independent, and *both* degenerate at A=3. The binding term `κ · (n_pp − n_nn)`
at ¹⁵O across the six live combinations:

| | C1 (interface) | C2 (pairs) |
|---|---|---|
| **R1** | −0.0335 | −0.2343 |
| **R2** | −1.0704 | **−7.4929** |
| **R3** | −0.0707 | −0.4947 |

**Range −0.0335 … −7.4929 MeV — a factor of 224**, every entry equally
consistent with everything κ has been tested against.

This is the sharpest statement of the conjecture's current standing, and it is
stronger than "the shape was fitted". The shape was fitted **at a point where
every competing reading of its own structure coincides**, so the 0.034 %
agreement constrains almost nothing about the object away from A=3. Any 8-shell
test must therefore *first* fix the rule and the convention; run before that, it
would measure the choice rather than the physics.

## Derivation step — the normaliser is a q-factorial, and that halves the problem

Formalize-first, Lean before numerics. **`[2]_q · [3]_q = [3]_q!`**, proved
sorry-free:

- `QOU.QInteger.qFactBal` — the canonical q-factorial `∏_{i=1}^n [i]_q`
- `QOU.QInteger.qIntBal_one_of_ne_sing` — `[1]_q = 1` off the singular locus
  (the hypothesis is not removable: at `q = ±1` and `q = 0` it is `0/0 = 0`,
  and every q-factorial collapses — the same locus `qIntBalClSing` guards)
- `QOU.QInteger.qFactBal_three` — the identity
- `QOU.BraidKnot.qBracket_normaliser_eq_qFactorial` — the κ-side corollary

**Why this is a derivation step and not a notational nicety.** The producer's
phrase describes a rule about **two** channel indices, which is what admits R1 /
R2 / R3 and the 32× spread. The object is **one**-index. So the continuation
question narrows from *"which pair of channels?"* to *"which `n` in `[n]_q!`?"*
— a strictly smaller search.

And the one index has a categorical handle. `[3]_q!` is already load-bearing in
the corpus twice over: `F_Bor = |tr_M(β_Bor)| · [3]_q! / q³`, and the q-Schur
Markov weight of the trivial partition, `y_{(3)}(q) = q³ / [3]_q!`. So

    normaliser = [3]_q! = q³ / y_{(3)}(q)

is the **inverse Markov weight of `(3) ⊢ 3`**. A derivation now has something
concrete to produce: *which partition's Markov weight appears at a magic anchor,
and why*. That is a categorical question with existing machinery
(`wedderburn_jones_markov.y_lambda_at`), not a shape hunt.

The `.md` is corrected accordingly — it described the denominator as the quantum
dimension of a `V_2 ⊗ V_3` Schur–Weyl tensor product, which fails twice: it
collides with the eightfold chapter's gl₃ Schur–Weyl decomposition (dims 10/8/1,
a different object of the same name), and it presents a one-index q-factorial as
a two-index product. The correction changes what the denominator *is*, not what
it evaluates to.

## The index is the nucleon's strand count — the ambiguity resolves

**The 3 is not a nuclear quantity.** The nucleon *is* the Borromean link, carried
by the braid word `(σ₁σ₂⁻¹)³` (`fundamental-knots-operator-basis`). That word
uses `σ₁, σ₂`, so `β_Bor ∈ B_3` and its Markov trace lives in `H_3(q)`. The 3 is
the strand count **internal to one nucleon**, identical for every nucleus
regardless of `A` or `A_magic`.

Corroborated by the normalisation already in use: `f-bor-borromean-observable`
gives `F_Bor = |tr_M(β_Bor)| / y_{(3)}(q)` — the trace of that same 3-strand
braid, over that same weight. So κ's normaliser is the Markov normalisation of
the **nucleon's own braid**, not of the nucleus, and κ is shell-independent —
exactly what `kappaClosed` already encodes by carrying no shell index. **R1 and
R3 are excluded; R2 stands.**

**The symmetric-vs-mixed tension dissolves.** I flagged that `(3)` is fully
symmetric while the A=3 anchors are `ppn`/`pnn` of mixed symmetry `(2,1)`. The
two partitions index different sets: `(2,1)` partitions the three *nucleons* of
the nucleus, `(3)` partitions the three *strands* of one nucleon. Both being
partitions of 3 at these anchors is a coincidence of the anchors, not a conflict.

**Status: identification, not theorem.** Two quantities numerically equal, both
normalising a Markov trace at `n = 3`. It cannot be promoted to a Lean theorem
because `fBor` in `ProtonBorromeanAssembly` is an abstract structure field, not
the `[3]_q!/q³` formula. What it buys is falsifiability: a three-way ambiguity
becomes the single prediction *κ does not vary with the shell*.

New Lean (sorry-free, exit 0): `QOU.QInteger.yTrivial` and
`qFactBal_eq_pow_div_yTrivial`, pinning `[n]_q! = qⁿ / y_{(n)}(q)` so the
Markov-weight relation is machine-checked rather than prose. Writing that proof
also removed a hypothesis I had assumed was needed — the identity survives
`[n]_q! = 0`, since Lean's `x/0 = 0` sends both sides to `0`.

## The excess resolves too — on corpus evidence, not on numbers

I expected this one to need an owner ruling. It does not.

**C1 and C2 are not competing definitions of one quantity — they are different
quantities sharing a glyph** (the registry §2 overloaded-symbol pattern):

- Corpus-wide, the **difference** `(n_pp − n_nn)` occurs **only** in κ's own
  block. C2's counts occur **only** in the **sum** `(n_pp + n_nn)`, inside
  `Δ_{T=1}`, under a different normalisation (`1/A`) and a different partition
  (`(2,2) ⊢ 4`). **No block forms C2's difference.**
- C1's block states its purpose outright: *"The asymmetric counts `(n_pp, n_nn)`
  encode the Z ↔ N asymmetry directly"*, and *"The interface asymmetry isolates
  the ³He anomaly"*. A difference measures an asymmetry; a sum does not.
- **The layers agree.** C1 is a braid object — the `A−1` interface generators
  `σ_{3k+2}` of `β(Z,N) ∈ H_{3A}(q)` — the same categorical layer κ's normaliser
  was just placed in. C2 is a combinatorial pair count with no braid-generator
  realisation in the canonical pppnnn ordering.

No value was consulted in choosing C1, and none of the numbers below were used
to make the choice.

## The 224× band collapses to one number

`probe_kappa_excess_convention_resolution.py` → witness, 3/3.

Since `max(0, m−1) − max(0, m−2) = 1` identically, the C1 excess is **±1 at
every single-magic mirror pair `(m, m−1)` / `(m−1, m)`, at every shell** — it
does not grow with `Z`. With the index already shell-independent, both factors
are shell-invariant and

    κ · (n_pp − n_nn)  ≈  ∓1.0704 MeV   at A_magic = 2, 8, 20, 28, 50, 82, 126

**From 224× undetermined to a single falsifiable number**, via two structural
arguments and no fitting. The first factor does not vary because it counts
strands inside a nucleon; the second because it counts interfaces adjacent to a
closed shell.

**Still not verified, and not claimed to be.** Testing this against measured
masses needs the binding decomposition that isolates the magic-shell term from
Coulomb and pairing, and that is not in the corpus (established earlier in this
bean). The prediction is stated, not confirmed.

## Test design for the remaining step — and where the fit would sneak in

Scoping the last item before running it, per formalize-first: find the
structural constraint before the wide search.

**The mirror-pair route is the right shape.** For a single-magic mirror pair,

    ΔB  :=  B(Z=m, N=m−1) − B(Z=m−1, N=m)

the isoscalar bulk cancels by construction — it depends on `A`, which is equal
across the pair. Under the conjecture the magic-shell term contributes
`κ·(+1) − κ·(−1) = 2κ ≈ −2.1408 MeV` to `ΔB`, **the same at every shell**, since
both factors were shown shell-invariant. So the test is:

    ΔB_observed − ΔB_Coulomb  ≈  −2.1408 MeV   at m = 2, 8, 20, 28, 50, 82, 126

Seven independent evaluations of one number, with no free parameter — a genuine
falsification test rather than a fit.

**And here is exactly where a fit would enter.** `ΔB_Coulomb` needs a charge
radius. The textbook form `ΔE_C ≈ 0.6 e²(2Z−1)/R` with `R = r₀A^{1/3}` carries
`r₀ ≈ 1.2 fm`, which is *empirical*. Three ways to treat it, and they are not
equally honest:

1. **Measured radii, no tuning** — take charge radii from experiment per
   nuclide. Legitimate: an independent measured input used to *test* a
   prediction, not adjusted to make it pass. This is the option I would take.
2. **Fitted `r₀`** — choose `r₀` so the residual lands on `−2.1408`. **This is
   the fit the demotion removed**, re-entering through the test rather than the
   derivation. Forbidden.
3. **Derived radius** — from the framework's own `Vol(K)` machinery. Best if it
   exists, but it must be checked that the radius route is not itself
   κ-anchored, or the test is circular.

The distinction matters because option 2 *looks* like option 1 in a commit diff.
Whoever runs this should state which was used and why, in the witness.

**Not run here.** Choosing between (1) and (3) is a scope call on someone else's
machinery, and running (1) needs a charge-radius table that is not in the tree.
The design is recorded so the next pass starts from a stated method rather than
improvising one at the keyboard — which is how (2) happens.

## Next

1. **Recover or rebuild the binding decomposition** — now the only thing between
   the prediction and a test. Ranked first because everything upstream of it is
   settled: the conjecture is no longer underdetermined, only unverified, and
   this is the single remaining step. Note it must be *rebuilt as a derivation*,
   not reconstructed to fit — reconstructing it against AME would re-import the
   fit the demotion removed.
2. **Historical — superseded by the two resolutions above.** Fix the index rule and the excess convention — both need an owner call or
   a derivation; the anchors provably cannot supply either. This now blocks the
   8-shell test rather than following it, which reverses the order I had.
2. **Name the excess convention** in the block — a one-line fix that makes the
   conjecture determinate. Needs an owner call on which of C1/C2 κ was fitted
   against; the anchors provably cannot say.
3. **Decide the fate of the dangling reference chain** — `def:hecke-e0`,
   `prop:h7a-magic-shell-quantum`, `prop:magic-shell-coupling-witness` are all
   absent while the `.md` still names the H7a quantum. Either they were renamed
   (find the successors) or the conjecture rests on vanished blocks.
4. Corroboration for the premise, from the corpus itself:
   `def:canonical-braid-interface-composition` already states *"A linear fit
   across the interfaces evaluates the 4-atom set, requiring evaluation against
   larger $A$ to verify structural predictions."*

Follow-up to `qou-k4dm`. Answers the owner's question *"deprecated magic shell —
did any align with 8-fold? anything in paper corpus to relook at?"*

## The 8-fold question: no

Checked numerically. The magic-shell slope needs a normaliser

    N = E₀·log(1/h) / |κ_obs| = 6.118482

against which every octet-flavoured candidate is far away:

| candidate | value | rel. err |
|---|---|---|
| `[2]_q[3]_q` — the current fit | 6.120579 | **0.034 %** |
| `[2]_q + [4]_q` | 6.120579 | 0.034 % |
| flat 6 | 6 | 1.94 % |
| `[6]_q` | 6.388087 | 4.41 % |
| flat 8 | 8 | 30.75 % |
| `[2]_q³` | 8.131476 | 32.90 % |
| **`[2]_q[4]_q` — sl₃ adjoint, the OCTET** | 8.264148 | **35.07 %** |
| `[8]_q` | 8.945690 | 46.21 % |

The corpus's octet is `V_(2,1)` at `dim = 8` in the `n = 3, N = 3` quantum
Schur–Weyl decomposition (`content/.../eightfold-way/schur-weyl-eightfold.md`),
and it carries the same 8, so the same ~35 % mismatch. **The octet does not
normalise κ**, and no rescue is close.

## One structural reading worth recording

`[2]_q·[3]_q = [2]_q + [4]_q` **exactly** — verified to machine precision above,
and it is the sl₂ fusion `V₂ ⊗ V₃ ≅ V₂ ⊕ V₄`. So κ's normaliser is a *sum over
fusion channels*, the doublet plus the quartet, not an opaque product. The block
currently calls it "the quantum dimension of the `V₂ ⊗ V₃` Schur–Weyl tensor
product", which is loose: the eightfold chapter's Schur–Weyl decomposition is the
gl₃ one with dims 10/8/1, a different object that happens to share the name.
Worth stating the fusion form — a derivation is likelier to produce a channel sum
than a product.

## The actual relook: κ has never met a second shell

`compound-beta-shell-calibration` — κ's own parent — declares the magic anchors
`A_magic ∈ {2, 8, 20, 28, 50, 82, 126}`. κ was **identified** at (2,2) = ⁴He and
**cross-checked** at (2,1)/(1,2) = ³He/³H. Every one of those sits in the
`A_magic = 2` shell.

**The 8 shell has never been evaluated.** ¹⁶O (Z = N = 8) is doubly magic, is
already named in the corpus, and is the obvious falsification test: a form fitted
in one shell either predicts the next shell or it does not. Running it costs
nothing and settles the conjecture's standing in one direction or the other.

Do it as a *prediction*, not a fit — compute `κ` from the closed form at the
8-shell anchors and compare, with no re-tuning permitted. Either outcome is
publishable: agreement is the first genuine evidence the form is derived,
disagreement scopes the conjecture to the 2-shell (a scope-(a) negative, per the
refutation-scoping rule — not a structural exclusion).

## Two adjacent gaps found while looking

Both flagged live by `run-validate` right now, both in `eightfold-way/`:

- `prop:meson-octet-decomposition` — no Lean declaration
- `prop:borromean-decuplet` — no Lean declaration

The eightfold chapter's two central claims are unformalised. Separate work, but
they are the formal backing any octet-route attack on κ would need.
