# Which `N` the nucleus is a state at: **`N = 2`** — and it does not decide Φ₃

**Date:** 2026-09-05
**Bean:** `qou-oots`
**Probe:** [`computations/probes/which_n_the_nucleus_is_a_state_at_probe.py`](../../computations/probes/which_n_the_nucleus_is_a_state_at_probe.py) — 9/9, exit 0, mpmath 50 dps, exact integer combinatorics, zero builtin-float coercions, no witness
**Closes:** the one item left open by [`2026-09-05-schur-weyl-share-is-a-third-measure.md`](2026-09-05-schur-weyl-share-is-a-third-measure.md) §8
**Retracts:** that note's §0 conclusion, which was mine

---

## 0. The answer

**`N = 2`.** Nothing here derives it — it follows from the **convention-D owner
ruling of 2026-08-15**, and the corpus already records it four independent ways.
The question was closed before it was asked.

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

## 4. What route 1 *does* establish — a constraint, not a selection

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

## 5. Scope

**Established.** `N = 2`, by owner ruling, recorded four ways. The ≥3-row blocks
are `ker(H_n ↠ TL_n)`, verified arithmetically. Depth 3 is vacuous at `N = 2`
and `N = 3` alike, and empty at `n = 3`. Both surviving Φ_k candidates put mass
on the kernel.

**Scope-(b) structural exclusion of Φ₃ as an observable** — not "Φ₃ performs
badly" but "the stratum it integrates over lies in the kernel of the map to the
state space" — resting on sorry-free
`QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff`, not on these numbers.

**NOT established.**

- **That Φ₁ or Φ₂ are vacuous.** Depth 0 and 1 are 1- and 2-row, inside the cap;
  check D shows they carry **all** the `N = 2` mass (1.0 at n = 3, 6, 9). The
  exclusion is specific to `k ≥ 2`.
- **Which family Φ_k should use.** Narrowed by a constraint that eliminates every
  current candidate; not selected.
- **That the TL share is right.** It clears the constraint and is q-independent;
  both facts are stated, neither is a recommendation.
- **Anything about the colour sector.** `N = 3` appears here only as the
  alternative reading being tested, and it fails the same way `N = 2` does.

---

## 6. Method note

The error corrected in §3 was found by reading the Φ_k audit's *definition* of
its own stratification rather than assuming it. The prior note measured a real
quantity, named it after a different one, and drew a conclusion that belonged to
neither — with the correcting sentence sitting three lines from text it quoted.
The general form: **when a claim turns on a stratum, an index set, or a depth,
resolve the definition in the source before measuring**, exactly as the
`da-arity-conflation` criterion asks for propositions.
