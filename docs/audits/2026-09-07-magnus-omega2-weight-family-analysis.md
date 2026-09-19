# Which partition weight should the Magnus Ω₂ pairing use?

**Date:** 2026-09-07 · **Bean:** `qou-za3q` · **Scope:** decision analysis, not a
derivation. Every number below is measured; none is fitted.

`{deuteron,triton}_magnus_omega2_sign_probe.py` and
`he4_magnus_omega2_sign_sparse_probe.py` compute

$$P_\text{total} \;=\; \sum_\lambda w(\lambda)\,\operatorname{tr}\!\big(\rho_\lambda \Omega_{2,\lambda}\big)$$

with $w = d_q(\lambda)^2/[n]_q!$ — the **quantum Plancherel** measure. Their
docstrings call this $y_\lambda$ and call the pairing $\operatorname{tr}_M$,
which is the production **Markov** trace with the Wenzl weight. Those are
different objects. This document establishes how different, what turns on the
choice, and what to do.

---

> # 🛑 SETTLED — OWNER RULING 2026-09-13: **ADOPT WENZL**
>
> This document was written as a decision analysis. **The decision has been
> made.** The Magnus Ω₂ pairing is
> $P = \sum_\lambda y_\lambda^{\text{Wenzl}}\,\operatorname{tr}(\rho_\lambda \Omega_{2,\lambda})$.
> The quantum Plancherel measure is **not** the pairing. Everything below is
> retained as the reasoning that led there, not as an open question.
>
> **What the ruling rests on** is not the argument this document leads with
> (consistency with production, cross-A comparability). It rests on a
> derivation that post-dates this document: bean `qou-gba1`. A nucleus is a
> *link*; a braid word only presents it; and the Markov trace is
> *characterised* by $\operatorname{tr}(1)=1$, cyclicity, and
> $\operatorname{tr}_{n+1}(x\sigma_{n-1}) = z\operatorname{tr}_n(x)$. Wenzl
> realises all three at $z = q^3/(q^2+1)$; Plancherel satisfies neither the
> first nor the third, **having no $z$ at all** — the ratio it would need moves
> from $-10.867$ to $+0.179$ between two stabilisations of the same word. The
> pairing inherits an exact parameter-free stabilisation law under Wenzl,
> confirmed to a relative **4.4e-141** and falsified at $z=q$ and $z=1$.
>
> **The sign never enters that argument**, which is what makes it usable rather
> than fitting.
>
> ## The consequence, which travels with the ruling
>
> | atom | $P$ (Wenzl, **adopted**) | $P$ (Plancherel, rejected) |
> |---|---:|---:|
> | deuteron | −6.921 | −15.095 |
> | triton | **−13.931** | +2.470 |
> | ⁴He | **−20.466** | +34.126 |
>
> ```
> adopted    −, −, −    NO sign change anywhere in A = 2, 3, 4
> rejected   −, +, +    one sign change, deuteron → triton
> ```
>
> **Under the adopted measure the programme's target A-dependent sign change is
> NOT exhibited in A = 2, 3, 4.** Cite that wherever the Magnus sign result is
> cited. The measure was chosen on principle and the phenomenon did not survive
> it; reporting the ruling without its consequence would be exactly the fitting
> the ruling exists to avoid.
>
> **What survives untouched:** sign-indefiniteness at A=2 — the property that
> cleared the non-negativity wall $\|F_q\|^2$ could not — holds under *both*
> weight families and *both* intra-nucleon words, because it is a statement
> about a commutator's trace pairing. `qou-dp32` is unaffected.
>
> Options: A `qou-q2q7` **adopted**; B `qou-94yt` and D `qou-ia4w` **refused**;
> C `qou-smvw` **subsumed** (both arms are emitted, `headline_pairing` names the
> adopted one); E `qou-gba1` is the ruling's basis, with its remaining item —
> identify the functional whose stationarity gives the binding correction —
> still open but no longer blocking.

---

## 1. What each object is

**Wenzl $y_\lambda$ — the Markov trace.** The unique trace on $H_n(q)$ with
$\operatorname{tr}(1)=1$ satisfying the Markov property
$\operatorname{tr}(x\sigma_n) = z\operatorname{tr}(x)$. That property is what
makes it invariant under Markov stabilisation, hence what makes it descend from
*braids* to *links*. It is what the production `tr_M` uses everywhere in this
corpus. Under convention D the Wenzl level is $r = 2$ exactly, which imposes a
**row cap**: $y_\lambda = 0$ for every $\lambda$ with $\ge 3$ rows
(`qou-fq0f`).

**$d_q(\lambda)^2/[n]_q!$ — the quantum Plancherel measure.** The $q$-analogue
of the Plancherel measure $d_\lambda^2/n!$, which is the distribution on
partitions induced by the *regular* representation. It is a natural measure for
**averaging over $\lambda$**. It is not built to be a normalised trace, and at
$q \ne 1$ it is not one.

## 2. The measurements

### 2.1 Normalisation — decisive

$\operatorname{tr}(1) = \sum_\lambda w(\lambda)\,d_\lambda$:

| atom | $n$ | Wenzl | Plancherel |
|---|---:|---:|---:|
| deuteron | 6 | **1.0** | 11.139 |
| triton | 9 | **1.0** | 184.233 |
| ⁴He | 12 | **1.0** | 6751.541 |

The Wenzl weight gives exactly 1 at every $n$, by construction. The Plancherel
form grows by a factor of ~600 from $A=2$ to $A=4$. **It is not a normalised
trace, and its scale is $n$-dependent.**

### 2.2 Weight shape — H₆, each family normalised to sum 1

| $\lambda$ | rows | dim | Plancherel | Wenzl | $\operatorname{tr}(\rho\Omega_2)$ |
|---|---:|---:|---:|---:|---:|
| (3,2,1) | 3 | 16 | 0.3619 | **0** | −17.026 |
| (4,1,1) | 3 | 10 | 0.1369 | **0** | −33.367 |
| (3,1,1,1) | 4 | 10 | 0.1369 | **0** | 13.254 |
| (4,2) | 2 | 9 | 0.1125 | 0.1802 | −45.954 |
| (2,2,1,1) | 4 | 9 | 0.1125 | **0** | 4.593 |
| (3,3) | 2 | 5 | 0.0357 | 0.0592 | 26.387 |
| (2,2,2) | 3 | 5 | 0.0357 | **0** | −15.702 |
| (5,1) | 2 | 5 | 0.0328 | 0.3091 | −65.925 |
| (2,1⁴) | 5 | 5 | 0.0328 | **0** | 3.501 |
| (6,) | 1 | 1 | 0.0012 | 0.4515 | 0 |
| (1⁶) | 6 | 1 | 0.0012 | **0** | 0 |

Not a rescaling. Plancherel puts **81.8 %** of its mass on $\ge 3$-row shapes;
Wenzl puts **0 %**. And **62.4 %** of the Plancherel $|{\rm contribution}|$ comes
from shapes the Wenzl cap annihilates outright.

Note the largest Wenzl weight, $(6,)$ at 0.45, contributes **nothing**: on a
1-dimensional block every operator commutes, so a commutator maps to 0. Under
Wenzl the entire H₆ signal is carried by three 2-row shapes — (5,1), (4,2),
(3,3).

### 2.3 The sign is robust at A=2 and **not** at A=3 or A=4

> **🛑 SETTLED 2026-09-12 (PR #7197) — ⁴He is no longer "undetermined", and the
> answer completes the pattern rather than breaking it.** This section's table
> and the two open-items that depend on it ("⁴He cannot be judged until its
> witness is regenerated", §4's "⁴He … is needed before even that is settled")
> were written while the ⁴He source was 2026-09-04, i.e. pre-ruling. It was
> regenerated on the canonical word on **2026-09-11** — 77/77 partitions, 8.0 h
> — and the robustness probe re-run with all three sources post-ruling, so
> nothing is excluded from the gate for the first time. The corrected row:
>
> | atom | source | partitions | Wenzl-nonzero | $P$ Plancherel | $P$ Wenzl | agree? |
> |---|---|---:|---:|---:|---:|:---:|
> | ⁴He | **canonical** | 77 | 7 | **+34.126** | **−20.466** | **no** |
>
> Full precision: Plancherel `+34.126027285357652927`, Wenzl
> `−20.466481428076021593`; trace split +33/−42/0×2.
>
> **So read the sign columns of the table below, not its rows:**
>
> ```
> Plancherel   −, +, +    one sign change, between deuteron and triton
> Wenzl        −, −, −    no sign change anywhere in A = 2, 3, 4
> ```
>
> Two consequences, and the second is the one that matters most for this doc.
>
> **(1) §4's honest reading gets stronger, not weaker.** It said the sign change
> is "not *yet* exhibited" at A=3 pending ⁴He. ⁴He has landed and does not
> rescue it: Wenzl is negative there too. The statement is now **not exhibited
> at any of A=2,3,4** — and the "yet" should be dropped.
>
> **(2) The claim that the choice is NOT URGENT is now FALSE.** §4 and the bean
> both recorded *"Safe either way: no published conclusion moves, because the
> sign is robust."* That was load-bearing for deferring the decision, and the
> measurement has removed it. At A=3 **and** A=4 the weight family determines
> whether the programme's target phenomenon is present at all. The option
> ranking (A recommended, C as guard) is unchanged in substance; its urgency is
> not.
>
> **What has NOT changed: Plancherel is not thereby preferred.** It gives the
> wanted sign at A=3 and again at A=4. Under AGENTS.md §"NO FITTING" that is
> *selection against the target* — no continuous parameter is tuned and it is
> still a fit — so being the convenient answer twice is grounds for more
> suspicion, not less. Decision 1 (which measure is the right pairing for a
> Magnus Ω₂ question, which is **not** a Markov trace) remains open; bean
> `qou-za3q`.
>
> The −57.803 / −100.827 figures in the table below are the **pre-ruling**
> values and are kept as the record of what this analysis had available. Do not
> quote them as current, and note §3's "⁴He magnitude nearly doubles" is
> computed from them.


> **Corrected 2026-09-07, later the same day.** The first version of this
> section claimed the sign was robust on all three atoms. It was not: two of the
> three source witnesses predated the 2026-09-05 ordering ruling, so the
> re-weighting compared two contractions of a *superseded braid word*. Triton's
> witness was 2026-09-03. Regenerating it on the canonical word changed 28 of
> its 30 per-partition traces — the only two unmoved being the one-dimensional
> blocks, where a commutator vanishes regardless — and flipped
> $P_\text{total}$ from −108.147 to **+2.470**.

| atom | source | partitions | Wenzl-nonzero | $P$ Plancherel | $P$ Wenzl | agree? |
|---|---|---:|---:|---:|---:|:---:|
| deuteron | canonical | 11 | 4 | −15.095 | −6.921 | yes |
| triton | canonical | 30 | 5 | **+2.470** | **−13.931** | **no** |
| ⁴He | *pre-ruling* | 77 | 7 | −57.803 | −100.827 | undetermined |

The traces are mixed-sign (deuteron +4/−5, triton +14/−14, ⁴He +26/−49), so
each sum is a genuine cancellation. At A=2 both families land negative. **At A=3
they disagree outright**, and ⁴He cannot be judged until its witness is
regenerated — its source is 2026-09-04.

Magnitudes were never robust and still are not.

### 2.4 The probe's stated control cannot discriminate

The docstrings cite `ρ=I ⇒ tr(Ω₂) = 0` as validating the setup. Measured: every
per-$\lambda$ control trace is **exactly 0**, so the control holds *blockwise*,
for any weights whatsoever. It is evidence for the cyclicity of the construction
and **no evidence at all** for the weight choice.

(The cyclicity argument itself survives either way: any non-negative combination
$\sum_\lambda c_\lambda \operatorname{tr}_\lambda$ is a trace and annihilates
commutators. What does *not* survive is calling it $\operatorname{tr}_M$.)

---

## 3. What actually turns on the choice

1. **A published sign.** This was originally recorded here as "nothing
   published changes". That is false. At A=3 the two families give opposite
   signs, so the weight choice determines a headline conclusion. (Separately,
   the ordering correction alone already moved triton's Plancherel sign from
   −1 to +1, independent of any weight question.)
2. **The cross-$A$ programme.** The stated target is a *sign change in $A$* —
   negative at $A=2$, positive at $A\ge3$. Sign is scale-invariant, so the
   existing sign gates are safe. But any comparison of *magnitudes* across $A$
   is invalid under Plancherel, because $\operatorname{tr}(1)$ changes by ~600×
   between $A=2$ and $A=4$. Under Wenzl the scale is fixed at 1.
3. **Whether the answer is about the nucleus or about the word.** A nucleus is a
   link. The Markov trace is the one invariant under stabilisation, so it depends
   on the link; the Plancherel average depends on the braid word chosen to
   present it.
4. **How much of the algebra is in play.** Wenzl discards the entire $\ge3$-row
   sector — 62 % of the A=2 contribution, 70 of 77 shapes at A=4.

---

## 4. Options

### Option A — adopt the Wenzl $y_\lambda$ as the pairing

**Pros.** Makes the code match its own stated derivation ($\operatorname{tr}_M$,
Markov, cyclicity). $\operatorname{tr}(1)=1$ at every $n$, so cross-$A$
magnitudes become comparable — the one thing the programme needs and does not
have. Markov-invariant, so the answer is a property of the nucleus rather than
the presentation. Consistent with production and with the row cap the rest of
the corpus already pays for.

**Cons.** Discards 62 % of the A=2 contribution and 70/77 shapes at A=4. If
Ω₂'s physics lives in the $\ge3$-row sector, this pairing is structurally blind
to it. The cap is a consequence of convention D and level $r=2$; if that level is
wrong the cap is wrong with it. ⁴He magnitude nearly doubles.

### Option B — keep Plancherel, rename it, justify it

**Pros.** Uses the whole algebra; discards nothing. Plancherel is the canonical
measure induced by the regular representation, i.e. the natural "average over
the algebra". Published signs unchanged. Cheapest option — the naming half is
already done.

**Cons.** Not $\operatorname{tr}_M$, so the docstring derivation must be
rewritten, not just renamed. Not normalised, so cross-$A$ magnitude comparison
stays invalid. Not Markov-invariant, so the result is a function of the braid
word. No derivation in this corpus's framework says this is the right pairing.

### Option C — report both, permanently

**Pros.** Honest: makes the weight-dependence visible instead of implicit.
Already implemented and costs nothing, because the per-$\lambda$ traces are
shared and only the contraction differs. Any future claim can state which arm it
rests on.

**Cons.** Defers the decision rather than making it. Two numbers where the
physics wants one. Invites citing whichever arm is convenient.

### Option D — normalise the Plancherel form to $\operatorname{tr}(1)=1$

**Pros.** Fixes cross-$A$ comparability for one line of code while keeping
full-algebra support. Strictly better than Option B on the measurement that
matters most.

**Cons.** Still not Markov, so still not a link invariant. A normalised
non-Markov trace is a perfectly good object but an unmotivated one here — it
would be chosen for convenience, which is the thing this corpus is careful about.

### Option E — derive the pairing from what Ω₂ is

**Pros.** The only option that *answers* the question rather than choosing. Ω₂ is
a curvature-like object; the correct contraction should fall out of whatever
variational principle produces a binding energy, and that would settle the row-cap
concern in Option A on principle rather than by convention.

**Cons.** Open-ended research with no bounded cost, and the arc has a working
sign result without it.

---

## 5. Recommendation

**Option A as the headline, Option C retained as a permanent guard.** Make the
Wenzl-weighted value the reported $P_\text{total}$, and keep the Plancherel arm
beside it, labelled, in the same witness.

The decisive argument is §3.2. The programme's target claim is a sign change *in
$A$*, and Plancherel does not put different $A$ on a common scale — a 600×
normalisation drift between $A=2$ and $A=4$ makes any cross-$A$ magnitude
statement meaningless, while Wenzl fixes $\operatorname{tr}(1)=1$ by
construction. Adopting Wenzl also collapses the gap between what the code does
and what its own docstring says it does, which is the smaller repair than
rewriting the derivation.

**It is no longer "safe" in the sense first claimed here, and that strengthens
rather than weakens the case.** At A=3 the two families disagree, so a choice
must be made rather than deferred — and when a choice determines a published
sign, it should be made on principle, not on which answer is wanted.

Which matters here, because the answers are not symmetric. The programme's
target is negative at A=2 and **positive at A≥3**. Under Plancherel triton is
+2.470 — the wanted sign. Under Wenzl it is −13.931 — the unwanted one. So the
better-motivated object currently does **not** exhibit the sign change the
programme is looking for, while the less-motivated one does.

That is a finding about the physics, not a reason to prefer Plancherel. This
corpus's standing rule is no fitting; choosing a weight family because it
produces the desired sign would be exactly that. The honest reading is that
under the principled pairing the A=2→A=3 sign change is **not yet exhibited**,
and ⁴He — whose witness is still pre-ruling — is needed before even that is
settled.

**The honest counterweight**, and the reason for keeping the second arm: Option A
throws away the sector carrying 62 % of the A=2 contribution. That is defensible
only because the row cap is a corpus-wide commitment already — if it is wrong it
is wrong everywhere, which is `qou-fq0f`'s question and not this probe's. Keeping
the Plancherel arm means that if the cap is ever revised, the evidence needed to
re-evaluate these probes is already recorded rather than needing a re-run.

**Not recommended:** Option B alone (leaves the cross-$A$ defect in place while
implying it is fixed) and Option D (buys comparability at the cost of an
unmotivated object). Option E is worth an entry but should not block A.

---

## Sources

- `computations/deltalambda/magnus_omega2_weight_family_robustness_probe.py`
  (§2.3, §2.4) and its witness.
- `computations/deltalambda/{deuteron,triton}_magnus_omega2_sign_probe.py`,
  `he4_magnus_omega2_sign_sparse_probe.py` — the per-λ traces re-weighted here.
- `y_lambda_wenzl_bridge_numeric` — production Wenzl weight.
- Beans `qou-za3q` (this question), `qou-fq0f` (row cap, level $r=2$),
  `qou-dp32` (the Magnus continuation the probes serve).
