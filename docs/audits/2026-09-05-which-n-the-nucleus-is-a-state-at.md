# Which `N` the nucleus is a state at: **`N = 2`** — and it does not decide Φ₃

**Date:** 2026-09-05
**Bean:** `qou-oots`
**Probe:** [`computations/probes/which_n_the_nucleus_is_a_state_at_probe.py`](../../computations/probes/which_n_the_nucleus_is_a_state_at_probe.py) — 9/9, exit 0, mpmath 50 dps, exact integer combinatorics, zero builtin-float coercions, no witness
**Closes:** the one item left open by [`2026-09-05-schur-weyl-share-is-a-third-measure.md`](2026-09-05-schur-weyl-share-is-a-third-measure.md) §8
**Retracts:** that note's §0 conclusion, which was mine

---

## 0. The answer

**`N = 2`.** Nothing here derives it, because the corpus already does — **twice,
from framework axioms, sorry-free** — states it for the mass channel by name,
hardcodes it in the canonical weight producer, and **closed it a month ago**
under bean `qou-fvzm` and `main` commit
[`f92a8b1500`](https://github.com/litlfred/qou/commit/f92a8b1500) whose subject
is literally *"N = 2 is LOCKED IN for the mass pipeline — the soft constraint is
hard"*. The question was closed before it was asked.

**And it decides nothing about Φ₃**, which is the half I got wrong. The depth-3
stratum is vacuous at `N = 3` as well.

---

## 1. Four corpus witnesses that `N = 2`

| # | site | what it says |
|---|---|---|
| 1 | [`wedderburn_jones_markov.py:177`](../../computations/wedderburn_jones_markov.py) | `_y_su_n(n, mp.mpf(str(q_val)), 2)` — the third argument **is** `N` |
| 2 | [`wedderburn_jones_markov.py:129-133`](../../computations/wedderburn_jones_markov.py) | *"D's weights are the **SU(2) quantum dimensions** … The defining difference is the row cap: `y_λ = 0` for `ℓ(λ) > 2`"* |
| 3 | [`wedderburn_jones_markov.py:386-391`](../../computations/wedderburn_jones_markov.py) | the vanishing blocks *"span `ker(H_n ↠ TL_n)`, of dimension `n! − Catalan(n)` (1, 10, 78, 588, 4611, 38890 at `n = 3..8`)"*, citing sorry-free `QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff` |
| 4 | [`2026-09-05-phi-k-weight-family.md:105`](2026-09-05-phi-k-weight-family.md) | *"Production is `N = 2` (convention D)"* — stated outright, in the audit whose §7 I was answering |

Witness 4 is the uncomfortable one: **the audit already contained the answer**,
one section above the one that poses the question as open.

---

## 2. The chain, verified independently (check A)

Witness 3 is the load-bearing one, because it upgrades "the weights happen to
vanish" into "the vanishing blocks *are* the kernel". Verified here without
relying on the corpus's arithmetic:

$$
\sum_{\ell(\lambda)\le 2} (f^\lambda)^2 \;=\; C_n \;=\; \dim \mathrm{TL}_n,
\qquad
n! - C_n \;=\; \dim \ker\big(H_n \twoheadrightarrow \mathrm{TL}_n\big)
$$

| n | `Σ_{ℓ≤2}(f^λ)²` | `Catalan(n)` | `n!` | `n! − C_n` | corpus |
|---|---|---|---|---|---|
| 3 | 5 | 5 | 6 | 1 | 1 |
| 4 | 14 | 14 | 24 | 10 | 10 |
| 5 | 42 | 42 | 120 | 78 | 78 |
| 6 | 132 | 132 | 720 | 588 | 588 |
| 7 | 429 | 429 | 5040 | 4611 | 4611 |
| 8 | 1430 | 1430 | 40320 | 38890 | 38890 |

All six kernel dimensions reproduce exactly. So the chain closes:

$$
H_n(q) \;\twoheadrightarrow\; \mathrm{TL}_n(q) \;\cong\; \mathrm{End}_{U_q\mathfrak{sl}_2}\!\big(V^{\otimes n}\big)
$$

and convention D sets `y_λ = 0` **precisely on the kernel**. The corpus's
canonical trace therefore already **factors through** the `N = 2` module's
endomorphism algebra — it is not merely compatible with `N = 2`, it is defined
on the `N = 2` quotient.

**Consequence for §7 of the Φ_k audit.** Horn 1 — *"the nucleus is a state in
`V^{⊗n}`"* — is the corpus's actual position, and it is structural rather than
prose: the row cap is what makes the trace well-defined on `End(V^{⊗n})`. Horn 2
is not a rival; `TL_n` **is** that endomorphism algebra.

---

## 3. 🛑 The retraction: which `N` decides nothing

The prior note ends *"route 1 now turns on exactly one thing: which `N` the
nucleus is a state at."* **False.** Two errors, compounding.

**(a) Depth is off by one.** The Φ_k audit defines *"Depth `k` means `k+1`
rows"* ([line 104](2026-09-05-phi-k-weight-family.md)). So the **depth-3
stratum is exactly 4 rows**, and "≥ 3 rows" — what the prior note measured — is
**depth ≥ 2**.

**(b) On the real stratum, `N = 3` is null too.** Check B, mass on partitions
with **exactly 4 rows**:

| n | #λ at depth 3 | **N = 2** | **N = 3** | N = 4 | Molien | classical Plancherel |
|---|---|---|---|---|---|---|
| 4 | 1 | **0.0** | **0.0** | 0.003505637 | 0.074351 | 0.04166667 |
| 5 | 1 | **0.0** | **0.0** | 0.01402255 | 0.2109275 | 0.1333333 |
| 6 | 2 | **0.0** | **0.0** | 0.03376524 | 0.348728 | 0.2513889 |
| 7 | 3 | **0.0** | **0.0** | 0.0634495 | 0.433403 | 0.3613095 |
| 8 | 5 | **0.0** | **0.0** | 0.1025481 | 0.4438256 | 0.4354415 |
| 9 | 6 | **0.0** | **0.0** | 0.1496872 | 0.3916401 | 0.4614446 |

Both caps sit **below** 4 rows, so both kill depth 3. The first `N` that does
not is `N = 4`, which nothing in the corpus proposes.

At `n = 3` — the proton, `A = 1` — the depth-3 stratum is **empty**: there is no
4-row partition of 3. So Φ₃ is not merely zero-weighted there; it has no index
set at all, for any `N` and any weight family.

**And the Φ_k audit had already said this**, at its lines 107-108:

> at `N = 3` the cap still lands on depth ≥ 3, so **`k = 3` is vacuous under
> `y_λ` at both the mass (`N = 2`) and colour (`N = 3`) readings.**

I quoted the paragraph immediately above that sentence, in the same note, and
did not carry the sentence itself.

---

## 4. ~~What route 1 *does* establish — a constraint, not a selection~~ 🛑 RETRACTED

> **🛑 THIS WHOLE SECTION IS WITHDRAWN (2026-09-05, same day). It was mine, and
> it is a scope error the Φ_k audit already names.** Probe:
> [`phi_k_is_not_a_trace_probe.py`](../../computations/probes/phi_k_is_not_a_trace_probe.py) — 4/4, exit 0.
>
> **The error.** The section imposes: *"any weight family consistent with the
> corpus's canonical trace must vanish on `ker(H_n ↠ TL_n)`"*, and concludes
> *"no candidate currently on the table satisfies the corpus's own consistency
> requirement."* **Φ_k is not a trace, so no such requirement exists.** Three
> independent reasons, any one sufficient:
>
> 1. **The Φ_k audit names this exact error as the one it exists to block.** Its
>    requirement **R3** reads, in the verdict table:
>    *"no Markov property is required — **Φ is not a trace** … it removes the
>    reason to want `y_λ` and **blocks a scope error**."*
> 2. **Φ_k is not linear on the algebra.** It is
>    `Φ_k(β) = Σ_{λ: depth k} w_λ · log(|χ^λ(β)|·d_q(λ))` — a log-weighted sum
>    over one depth stratum. `tr_M = Σ_λ y_λ χ^λ` is a linear functional on
>    `H_n(q)`. A kernel argument about which *algebra elements* act as zero on
>    `V^{⊗n}` says nothing about which *partitions* a separate functional may
>    weight.
> 3. **The constraint annihilates its own subject.** Imposed, it forces
>    `w_λ = 0` on every λ with ≥ 3 rows — every stratum of depth ≥ 2 — so
>    `Φ_k ≡ 0` for **all** `k ≥ 2` by the audit's own R1. A requirement that
>    forbids the object being constructed is a reductio, not a finding.
>
> **And the "fifth measure" this section endorsed fails R1.** It named the TL
> share `(f^λ)²/C_n` over `ℓ(λ) ≤ 2` as *"the one candidate that clears the
> constraint"*. It clears it by being zero off the two-row cap — which is
> precisely what R1 retires `y_λ` for. Measured (check B): it puts **0.9998 of
> its mass on depth 1 and exactly 0.0 on every stratum of depth ≥ 2** at n = 9.
> My proposed solution was the degenerate case.
>
> **What the ruling says.** After this audit merged, the owner ruled
> *"molien. do the two arm reporting"* — **Molien canonical** for Φ_k, with
> `d_q²/D²` retained as a labelled comparison arm (bean `qou-oots`, closed).
> Check C confirms Molien is **nonzero on every depth ≥ 2 stratum** (0.3916 on
> depth 3 at n = 9, the chirality channel) and check D that its total mass is
> exactly 1 at n = 3…9 — so it satisfies R1 and R2 on exactly the strata this
> withdrawn section excluded it for. **This retraction does not re-open the
> family question; it removes a wrong argument against the ruling's answer.**
>
> **What survives in this note, untouched:** §1 (`N = 2` and its four corpus
> witnesses — the question this audit was written to settle), §2 (the
> TL/Catalan arithmetic), §3 (the depth off-by-one and the `N = 3`-is-also-null
> measurement). Only §4's constraint and its endorsed measure are withdrawn.

**Superseded text follows, kept as the record of the error.**

### ~~What route 1 does establish~~

Any weight family consistent with the corpus's canonical trace must **vanish on
`ker(H_n ↠ TL_n)`**, i.e. on every λ with ≥ 3 rows. That is not a preference; it
is what makes the functional well-defined on the state space the trace lives on.

Measured against that constraint (check B), **both surviving candidates fail it**:

| family | mass on ≥ 3 rows | verdict against the TL constraint |
|---|---|---|
| Molien `f^λ q^{−κ_λ} d_q^{hook}/[n]_q!` | 0.223 / 0.902 / 0.998 at n = 3/6/9 | **violates** |
| classical Plancherel `(f^λ)²/n!`, unrestricted | nonzero at every depth-3 row above | **violates** |
| `d_q²/D²` | violates unless `D²` is restricted to ≤ 2 rows | **violates as usually written** |

So route 1 **constrains the family without selecting one**, and the honest
statement is stronger than "the question is open": *no candidate currently on
the table satisfies the corpus's own consistency requirement.*

**The correctly-scoped horn-2 candidate does** (check C): the block share of
`End_{U_q\mathfrak{sl}_2}(V^{⊗n}) = TL_n`, namely

$$
\frac{(f^\lambda)^2}{C_n}\quad\text{over }\ell(\lambda)\le 2,
$$

which is normalised exactly (1.0 at n = 4, 6, 8) and is **zero off the cap by
construction**. This is a *fifth* measure and the properly-scoped version of the
candidate §7 omitted. It is **not** endorsed here — it is named as the one
candidate that clears the constraint, and it inherits classical Plancherel's own
objection of being **q-independent**.

---

## 4a. It is **derived**, not merely ruled — and the same axiom excludes `N = 3`

The convention-D ruling is how `N = 2` is *enforced*; it is not the only reason
to believe it. [`VolumeConstraintForcesFibreTwo.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/VolumeConstraintForcesFibreTwo.lean)
(**0 sorries**) derives it from condition (v) of `def:quantum-observable-universe`
— the non-degenerate epimorphism `ε : Λ²V → 𝟙`. Read at the fibre,
`dim Λ²V = C(N,2)`, so:

```lean
theorem exteriorSquareDim_eq_one_iff (N : ℕ) : exteriorSquareDim N = 1 ↔ N = 2   -- :151
theorem exteriorSquareDim_three_ne_one  : exteriorSquareDim 3 ≠ 1 := by decide    -- :168
```

The second line is the one worth carrying: **the same axiom that gives `N = 2`
positively excludes the colour fibre `N = 3`.** The file is honest about its own
limit (`:68-78`): this is `N = 2` from a *stated axiom of the framework*, and
whether condition (v)'s "non-degenerate epimorphism" should be read as an
isomorphism is an editorial question it flags as unresolved.

A second, independent route: the Wenzl level. Convention D inverts to
`z_W = q⁴/(q²+1)`, hence `X = q⁴ = Q²`, an **integer Wenzl level `r = 2`** on the
nose — and [`2026-08-16-su-r-level-tower-gap-map.md:57-61`](2026-08-16-su-r-level-tower-gap-map.md)
identifies the two indices, *"fibre dimension `N` = Wenzl level `r`"*.

## 4b. The conflation this question was built on, named in the corpus

The `3` in `3A` is the **strand count `n`**, not the fibre dimension. The
eightfold chapter opens by warning against exactly the inference I was
entertaining — [`eightfold-intro.md:11,26`](../../content/quantum-observable-universe/eightfold-way/eightfold-intro.md):

> **Two different `A_2`s.** […] because we have set `n = 3` and would like
> `N = 3`. **Setting `n = 3` does not make `N = 3`.**

and `:34`, *"the single-fibre construction … yields a quantum form of `SU(2)`,
with `dim V = 2`, and no choice of `q` raises it."*

**Colour does not change the fibre either.** The canonical colour-weighted
production path — `bring_color_weighted`, made canonical by owner ruling R3 of
2026-08-15 — runs `z_D = q³/(q²+1)`, the SU(2)/TL parameter, and applies colour
as a **δ-perturbation on the p–n interface** (`closed_form_tau_M.py:305-307`),
not as a change of `N`. The only `N = 3` fibre in `computations/` is a probe
fixture (`ocneanu_param_from_fibre_dimension.py`). So both readings I tested in
§3 are `N = 2` in production, and the `N = 3` one is not a live alternative at
all.

## 4c. 🛑 A second error in the prior note: F4 computes the share of the wrong algebra

[`2026-09-05-schur-weyl-share-is-a-third-measure.md`](2026-09-05-schur-weyl-share-is-a-third-measure.md)
§4 says horn 2's `End(V^{⊗n})` has block share `(f^λ)²/n!`. **At `N = 2` that is
the wrong algebra.** The operator algebra of the pair is `TL_n`, of dimension
`Catalan(n)` — not `H_n`, of dimension `n!`. The correct horn-2 share is the one
in §4 above, `(f^λ)²/C_n` over `ℓ(λ) ≤ 2`.

The root cause is a bare isomorphism where a surjection belongs, and **the corpus
carries it in three places besides my note**:

| site | text |
|---|---|
| [`notation-collisions.md:153`](../../content/quantum-observable-universe/notation/notation-collisions.md) | `H_n(q) \cong \mathrm{End}_{U_q\mathfrak{sl}_N}(V^{\otimes n})` |
| [`MassLeftMulEndomorphism.lean:20`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism/MassLeftMulEndomorphism.lean) | *"`H_n(q) ≅ End_{U_q 𝔰𝔩_N}(V^⊗ⁿ)` (Jimbo), under which a Hecke element is **literally** an endomorphism of `V^⊗ⁿ`"* |
| [`wenzl-bridge-applicability-qou.lean:33`](../../content/quantum-observable-universe/mass-theory/wenzl-bridge-applicability-qou.lean) | *"The centraliser isomorphism `H_n(R, q) ≅ End_H(V^{⊗n})`"* |

`q`-Schur–Weyl is an isomorphism only for **`N ≥ n`**; below that the map is
surjective with kernel the `> N`-row blocks. At `N = 2`, `n = 3A`, it is nowhere
near injective — and the corpus contradicts itself here, because
`TraceBlindSector.lean:11` states `TL_n(q) = End_{U_q(sl₂)}(V^{⊗n})` and
`wedderburn_jones_markov.py:388` gives the kernel dimension outright. Two sites
get it right (`QSchurWeyl.lean:11`, *"the **image of** the Iwahori–Hecke
algebra"*; [`RowCap.lean:48-56`](../../content/quantum-observable-universe/lean/QOU/Hecke/RowCap.lean),
*"It bounds the **carrier**, not the algebra … a number read off `S^λ` for
`ℓ(λ) > N` is a number about the algebra, not about the carrier"*).

The `N ≥ n` condition is stated in a **held but uncited source**:
`library/black-samson-phd2010sp/sections/sec-010-…md` (Black, *Representations
of Hecke Algebras*, pp. 30-31) — *"For `d ≤ n`, the homomorphism `π_d` is
injective. **In the sequel, we will be concerned with the other extreme, where
`π_d` is far from injective**"*, treating `(m|n) = (2|0)` = Jones = `N = 2`.
That is this framework's situation exactly, at `d = 3A ≫ 2`. Nothing outside
`library/` cites it.

## 4d. Two sourcing errors in the prior note, corrected

- **`dim V = 2` is NOT forced by the Descartes condition.** The prior note cites
  `state_space_natural_three_sym2_gate.py:8-17` (*"`dim V = 2` by the Descartes
  condition"*). The value is right and the sourcing is wrong, **and the corpus
  says so**: [`schur-weyl-eightfold.md:53`](../../content/quantum-observable-universe/eightfold-way/schur-weyl-eightfold.md)
  — Descartes *"is compatible with but does not uniquely force `N = 2`"* — and
  [`2026-08-04-ocneanu-trace-parameter-audit.md:114`](2026-08-04-ocneanu-trace-parameter-audit.md)
  — ***"Do not claim `N = 2` is forced by the Descartes condition"***. The live
  sourcing is the volume axiom of §4a.
- **`schur-weyl-mass-decomposition.md` does NOT keep λ with rows beyond 3.** The
  prior note's §3 scope carries that claim second-hand. Read at the source, it is
  **line 18**, and it says the additive-Wedderburn *approximation* *"discards all
  partitions with **rows longer than 3**"* — that is `λ₁ > 3`, part **size**, and
  its own examples `λ = (3A−1, 1)` and `(3A−2, 2)` are **two-row** partitions.
  It is not a statement about the row cap at all, and it describes an
  approximation no live producer runs.

## 4e. What route 1 *does* establish, measured: **both horns vanish**

§4 above claimed route 1 hands down a *constraint* on the weight family. That
was withdrawn. This section replaces it with what route 1 actually yields once
`N = 2` is in hand, and the answer is a **negative**: route 1 cannot supply a
Φ_k weight family for `k ≥ 2` at all, by either horn.

Recall how §7 of
[`2026-09-05-phi-k-weight-family.md`](2026-09-05-phi-k-weight-family.md) poses
it — as a fork whose resolution is the naming:

> If that object is `V^{⊗n}` … the share is `f^λ d_q(λ)/[n]_q!`-shaped
> (Molien) and the question is closed. If it is the endomorphism algebra
> `End(V^{⊗n})`, the share is `d_q²/D²`-shaped and the question is closed the
> other way. **Naming which object the nucleus is a state in is the whole
> content.**

At `N = 2` **both horns are supported on partitions of at most two rows**, i.e.
on depth 0 and depth 1 only, and are **exactly zero** on every stratum of depth
`≥ 2`:

| horn | share | index set | why it dies on depth ≥ 2 |
|---|---|---|---|
| 1 — module `V^{⊗n}` | `f^λ · d_q^{SU(2)}(λ) / [2]_q^n` | `ℓ(λ) ≤ 2` | the cell `(3,1)` has content `−2`, so `[2 + (−2)]_q = [0]_q = 0` kills the product — `RowCapObstruction.lean` arriving as arithmetic |
| 2 — operators `End(V^{⊗n})` | `(f^λ)² / Catalan(n)` | `ℓ(λ) ≤ 2` | `End_{U_q𝔰𝔩₂}(V^{⊗n}) = TL_n(q)`, which *has no blocks* with more than two rows |

Measured at the nuclear `n = 3A`, proton pin, `mp.dps = 50`
([`route_1_is_degenerate_at_n_two_probe.py`](../../computations/probes/route_1_is_degenerate_at_n_two_probe.py),
5/5):

| `n` | `A` | Σ horn 1 | horn 1 on depth ≥ 2 | Σ horn 2 | horn 2 on depth ≥ 2 | Σ Molien | Molien on depth ≥ 2 |
|---|---|---|---|---|---|---|---|
| 3 | 1 | 1.0 | **0.0** | 1.0 | **0.0** | 1.0 | 0.223435 |
| 6 | 2 | 1.0 | **0.0** | 1.0 | **0.0** | 1.0 | 0.902265 |
| 9 | 3 | 1.0 | **0.0** | 1.0 | **0.0** | 1.0 | 0.997609 |
| 12 | 4 | 1.0 | **0.0** | 1.0 | **0.0** | 1.0 | 0.999985 |

By the audit's own **R1** (`phi_eq_zero_of_weights_vanish`: weights vanishing
throughout a stratum make `Φ_k = 0` for *every* braid), each horn therefore
gives `Φ_k ≡ 0` for `k ≥ 2`. So naming the object does not select between two
weight families — it returns the zero functional either way.

**This is a scope-(b) exclusion**, and the invariant is cited: the row cap, in
horn 1 as `[0]_q = 0` and in horn 2 as the absence of the blocks themselves. It
is not "the share scores badly on the ranking"; it is "the share makes the
object identically zero".

**The fork was real — that is what makes the collapse informative.** The two
horns are genuinely different measures, max per-λ gap 0.305 / 0.205 / 0.206 /
0.217 at `n = 3/6/9/12`, so §7 was not offering one option written twice, and
at general `N ≥ 4` naming the object *would* decide. What collapses route 1 is
specifically the `N = 2` ruling, which post-dates the audit. **§7 was a sound
question that the settlement of `N` turned into a dead one.**

**Two things this does not license.**

1. **It is not an argument that Molien is correct.** Molien passes R1 here —
   strictly positive mass on depth `≥ 2` at every nuclear `n`, and it is the
   only one of the three that does — and the owner ruled it canonical. Surviving
   the requirement that kills the alternatives is not a derivation, and this
   measurement supplies none. What it does supply is the reason the ruling was
   *needed*: route 1, the route the audit ranked most decisive, cannot answer.
2. **It says nothing about `k = 0` or `k = 1`.** Both horns are perfectly good
   measures on depth `≤ 1`; the exclusion is only for `k ≥ 2`. Routes 2 (a
   same-`n` within-stratum observable) and 3 (a cross-nucleus metric with more
   than four points) are untouched and remain the live ways to settle the
   family by measurement rather than by ruling.

**"Then pick a larger `N`" is not available, and this is the sharpest thing a
sibling added.** The paragraph above says the fork *would* decide at general
`N`, which invites the rescue: re-choose `N ≥ 4` and both horns come alive on
depth ≥ 2 again. But `N` is not a free label attached to a fixed trace — the
Ocneanu/Markov weights depend on it through a nontrivial rational function of
`q`, so moving `N` **re-weights every surviving channel**. Verified here
independently at the proton `q₀`, `mp.dps = 50`, balanced convention, against
the closed form `y_{(2,1)}/y_{(3)} = [2]_q[N-1]_q/[N+2]_q`:

| `N` | `y_{(2,1)}/y_{(3)}` |
|---|---|
| 2 | 0.48930712047797097007 |
| 3 | 0.77459088135788091778 |
| 4 | 0.95812403128848485757 |

`N = 2 → 3` alone moves that ratio by **58.30 %** (`N = 3 → 4` by 23.69 %) —
[`ocneanu_n_lockin_crosscheck_probe.py`](../../computations/probes/ocneanu_n_lockin_crosscheck_probe.py), 3/3. So a route-1 rescue by re-choosing
`N` is not a change of reading; it is a change of trace, and the trace is fixed
by the convention-D ruling. The stronger form — that **`N` *is* the Ocneanu
trace parameter**, `a = q^{N-1}`, making "choose `N`" and "choose the trace"
literally one act, so the row cap is arithmetic rather than an imposed rule —
is [#6829](https://github.com/litlfred/qou/pull/6829)'s
(`ocneanu_N_lockin_probe`), not mine: **the three ratios above are what I
verified; the identification I am citing, not asserting.**

One convention trap they flag and I confirm: that probe's docstring writes the
closed form as `q·[2][N-1]/[N+2]` in the **asymmetric** convention while
`y_lambda_su_n` computes **balanced**. The two differ by exactly the leading
`q` — the asymmetric values are 0.5431 / 0.8598 / 1.0635 — so a reader
comparing across the two reads a discrepancy where there is none. The table
above is balanced throughout.

One arithmetic caution for anyone extending the table: the depth-3 column
(exactly 4 rows) is `0.0` at `n = 3` for **all three** measures, including
Molien — there is no partition of 3 with four rows. That zero is arithmetic,
not a vanishing weight, and reading it as one would repeat §3's error in a new
place. Molien's depth-3 mass is 0.348728 / 0.391640 / 0.136680 at
`n = 6/9/12`.

---

## 5. Scope

**Established.** `N = 2`, by owner ruling, recorded four ways. The ≥3-row blocks
are `ker(H_n ↠ TL_n)`, verified arithmetically. Depth 3 is vacuous at `N = 2`
and `N = 3` alike, and empty at `n = 3`. Both surviving Φ_k candidates put mass
on the kernel. And (§4e) **both horns of route 1 are exactly zero on depth
`≥ 2`** at every nuclear `n = 3A`, so route 1 cannot supply a Φ_k weight family
for `k ≥ 2` — a scope-(b) exclusion of the *route*, with the row cap cited.

~~**Scope-(b) structural exclusion of Φ₃ as an observable**~~ — **WITHDRAWN with
§4.** The Lean theorem cited is real and says what it says about `y_λ`; what was
wrong was inferring from it a constraint on Φ_k's *own* weight family. Φ₃ is
vacuous **under `y_λ`** (which is R1's finding, not mine) and is **not** vacuous
under Molien, the canonical family.

**NOT established.**

- **That Φ₁ or Φ₂ are vacuous.** Depth 0 and 1 are 1- and 2-row, inside the cap;
  check D shows they carry **all** the `N = 2` mass (1.0 at n = 3, 6, 9). The
  exclusion is specific to `k ≥ 2`.
- **Which family Φ_k should use.** §4e removes route 1 as a way to answer it; it
  does not answer it. Molien is canonical **by owner ruling** (2026-08-05,
  bean `qou-oots`), and passing R1 where both horns fail it is a reason the
  ruling was needed, not a derivation of it.
- **That the TL share is right.** §4c corrects it to `(f^λ)²/Catalan(n)` and
  §4e measures it as identically zero on depth `≥ 2`. Recording what it is is
  not recommending it — under R1 it is excluded for `k ≥ 2` exactly as the
  module share is.
- **Anything about a future `N = 3` construction.** It stays the eightfold
  chapter's principal open problem (live carrier `qou-y7vg`, ledger
  `docs/coordination/eightfold-n3-surface.md`). What §4b establishes is only
  that `N = 3` is not what *production* runs.
- **That `N = 2` is RIGHT.** The corpus says it, derives it from its own axiom
  under the strong reading of condition (v), and locks it in — and the deriving
  file itself flags that reading as editorially unresolved.
- **The strand count.** `H_{A+Z}` (`atomic-braid.md:2`, `wedderburn-mass-formula.md:2`)
  against `H_{3A}` (`schur-weyl-mass-decomposition.md:1`, `hecke_3a_weights.py:5`)
  is still unreconciled by any block. It does not affect this answer: `N = dim V`
  is a property of the fibre, independent of `n`.

---

## 6. Method note

The error corrected in §3 was found by reading the Φ_k audit's *definition* of
its own stratification rather than assuming it. The prior note measured a real
quantity, named it after a different one, and drew a conclusion that belonged to
neither — with the correcting sentence sitting three lines from text it quoted.
The general form: **when a claim turns on a stratum, an index set, or a depth,
resolve the definition in the source before measuring**, exactly as the
`da-arity-conflation` criterion asks for propositions.
