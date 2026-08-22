---
# qou-8na1
title: y_0* = 0 is forced by the trace-form radical, so the LP shadow price prices nothing
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T13:18:20Z
updated_at: 2026-08-21T16:21:57Z
---


Split out of `qou/k4f8` (#5239), which established the fact. This bean carries
the **content** consequence, which is not a Lean question and needs an owner
decision.

## The fact

Exact in ℚ(q), 18/18 checks, no floating point —
`computations/operator_selection_lp_symbolic_qq.py`. For `H₃(q)`, `d = 6`:

- `t` is row 0 of `G`, structurally: `tⱼ = tr_M(bⱼ) = tr_M(b₀bⱼ) = G₀ⱼ`.
- `det G = 0` **identically**; rank 5; radical `v = (−q³, q², q², −q, −q, 1)`,
  the q-antisymmetriser.
- Pairing the dual equation with `v` gives `0 = ⟨t,v⟩ = y₀⟨𝟙,v⟩`, and
  `⟨𝟙,v⟩ = −(q−1)(q²−q+1)`. So **`y₀ = 0` for every dual-feasible `(y₀,s)` at
  every `q ≠ 1`** — no `s ≥ 0`, no symmetry, no primal feasibility needed.

Lean: `y_0_eq_zero_of_radical` in `operator_selection_lp.lean` (holds over any
commutative ring without zero divisors).

## Why it is a content problem

The dual objective is `n_target · y₀`. With `y₀ ≡ 0` the LP's optimal value is
`0` **for every `n_target`** — the quantity meant to price the net constraint
cannot respond to it. Consequences to adjudicate:

1. `a_K^{dual_ratio} = y₀*_atom / y₀*_free` is `0/0` symbolically.
   `aK_via_lp_dual_hecke_basis.py` guards `abs(u0) > 1e-12` and records
   `a_K^chi_active` as undefined when it trips. **The guard is firing on an
   identity, not on noise** — it is reporting the structure correctly while
   describing it as a numerical edge case.
2. The header of that script says the *previous* Wedderburn-block LP "gave
   degenerate duals (y_0^* = 0 for A ≥ 2)" and moved to the full Hecke basis
   to escape it. The full basis has the same property. `H₂` does **not**
   (`det G = (q⁴+q²+1)/(q²+1)² ≠ 0`), so this is an `H₃` fact, not a
   formulation artifact — the move could not have helped.
3. `prop:mass-coefficient-shadow-price` is the block that reads `y₀*` as a
   shadow price. That reading is what is in question, not the LP algebra.

## `qou/pin3` is NOT this — checked, and my guess was wrong

When this bean was filed I flagged `pin3` ("regeneration picks a DIFFERENT
optimal LP dual vertex") as plausibly the same degeneracy seen from the
numerics side. **It is not**, and the reasoning that suggested it does not
transfer. Checked in `computations/alpha_5_lp_dual_crystal_closed_form.py`:

`alpha_5_lp_dual_crystal.py` builds `G = diag(|weight_λ|)` — a *diagonal*
matrix, not a trace form — and its `t` is `q`-content of shapes, unrelated to
`G`. Neither hypothesis of `y_0_eq_zero_of_radical` holds there: no weight is
zero (min `|w|` = 2.2e-06), so there is **no radical at all**, and `t` is not
a row of `G`, so `⟨t,v⟩ = 0` would fail even if there were one.

That LP is in fact solvable in closed form — `x* = n_target·e_argmin(t)`,
`y₀* = min_j t_j`, `s*_j = (t_j − min t)/|w_j|` — verified against every field
of every stratum of the committed witness. Its dual optimum is a **unique
point**, so `pin3`'s own "different vertex" diagnosis is wrong too. The real
cause there is that `s*` divides by `|w| ~ 1e-06`, amplifying a
solver-tolerance error in `y₀*` by ~1e+05. Written up in `pin3`.

Keep the two separate. The only thing they share is the word "degenerate".

## Not claimed here

That the physics is wrong. The LP may simply be the wrong instrument for the
attribution it is being asked to make, or `n_target` may need to enter
somewhere other than the net constraint. Deciding that is the owner's, not a
mechanical check's.

## Next

- [ ] Owner decision on `prop:mass-coefficient-shadow-price`
- [x] Check `qou/pin3` against this — **different**, see above
- [ ] Re-read the `a_K` extraction chain for other divisions by `y₀*`

---

## 2026-08-21 — confirmed against the corpus's own committed numerics

The ℚ(q) analysis above was symbolic. `computations/a-K-via-lp-dual-hecke-basis.witness.json`
is the committed f64 solve of the same LP, and it agrees **exactly**, for both
atoms:

| predicted in ℚ(q) | witness (proton and neutron) |
|---|---|
| `y₀* = 0`, forced by the radical | `y0_star = -0.0` |
| `s = e₀`, the unique non-negative certificate for `q > 0` | `y_star = [1.0, 0, 0, 0, 0, 0]` |
| optimal value `n_target · y₀* = 0` | `primal_obj ≈ -5e-11`, `dual_obj = 0.0` |
| — | `chi_y_sum = 1.0`, `sc_y_sum = 0.0` |

So this is not a symbolic curiosity that numerics might contradict. The numerics
already showed it and were read as a solver artifact.

### The sharper consequence for `prop:mass-coefficient-shadow-price`

Re-reading the block: it claims `c_λ = y_λ* · m_e`, where `y_λ*` is the dual of
the **Frobenius** constraint on Wedderburn block `λ` — *not* the net-constraint
dual `y₀*`. My earlier note conflated the two, which understated the problem.

`y_star = e₀` says **every Frobenius shadow price except index 0 is exactly
zero**, and index 0 is `𝟙`, the identity element — not a partition block at all.
So if mass coefficients are Frobenius shadow prices, then on this LP **all but
one coefficient is zero**. That is a stronger and more direct contradiction of
the block than the `y₀* = 0` observation, and it does not depend on the
NF-index → Wedderburn-block assignment being exact (the script's own comment
calls that assignment "approximate").

### A tension worth flagging, not resolving

`x_star[0] = -1000000.0` in the witness — exactly `-M_bound`. **The box binds at
the solver's optimum.** Bean `qou/0tjt` concluded the box is non-binding at `x*`,
and `operator_selection_lp.lean` drops the box on that basis.

Both can be true without contradiction: the optimal face here is large (I showed
the radical direction `x* = c·v` is also optimal, with every Frobenius constraint
tight and the box slack), so the LP has many optima and the solver landed on a
box vertex while `0tjt` reasoned about a different one. The *value* and the
*duals* — which are what the content claims rest on — agree either way. But
"the box is non-binding at x*" is true of a particular `x*`, not of the LP, and
the Lean's justification for dropping the box should say so.

## Next

- [ ] **Owner ruling** on `prop:mass-coefficient-shadow-price`, now with the
      numerics confirming the symbolics. The options are unchanged — retract /
      restate, move the extraction off the LP, or change where `n_target`
      enters — but the evidence is no longer contestable as a precision artifact.
- [ ] Re-word the box justification in `operator_selection_lp.lean` and in
      `qou/0tjt`: non-binding **at the radical optimum**, not at every optimum.
- [ ] Re-read the `a_K` chain for other divisions by `y₀*` or by a `y_λ*` that
      is now known to be zero.

---

## 2026-08-22 — box justification re-worded, and the `a_K` chain re-read

Both mechanical follow-ups done. The owner ruling is now the only item left.

### The box: the old reason was wrong, and so was the replacement I expected

`IsFeasible` in `operator_selection_lp.lean` said the box was "absorbed into
the existence of a large `M`" and called the other two "the two binding
constraints". The witness contradicts that — `x*₀ = -1000000.0 = -M` exactly,
both atoms — so the box **is** active at the solver's optimum.

But "non-binding at the radical optimum" is not the right replacement either.
Dropping the box is sound for a reason that does not depend on where the
optimum sits:

1. **The drop only enlarges `IsFeasible`.** Every theorem in the file is
   either "`x*` satisfies these two constraints" (unaffected) or "optimal
   among all feasible points" / a lower bound over all feasible points, which
   admitting more points *strengthens*. Nothing here can be true of the
   relaxation and false of the box.
2. **The certificate, not the box, bounds the program.**
   `dual_bound_le_objective` uses the net constraint, Frobenius positivity and
   `s ≥ 0`, nothing else. The box exists in the narrative to make the
   polyhedron bounded; the dual bound already does that.

### What `0tjt` should have said

`0tjt` closed on "the paper says the multipliers vanish at the optimum, which
makes the `≤` tight". That is right, and it is **not** the same as "the box is
non-binding". At the witness optimum the box at index 0 is *active* with a
*zero multiplier*:

    μⱼ = tⱼ - y₀ - Σᵢ Gⱼᵢ yᵢ = tⱼ - Gⱼ₀ = 0    for every j,

since `y = e₀`, `y₀ = 0`, `t` is row 0 of `G`, and `G` is symmetric. Primal
degeneracy at a box vertex. The multipliers vanish for the structural reason
`t = G₀·`, **not** because `M` was chosen large — which is what the paper's
"driven to zero for large `M`" asserts. Same conclusion, different mechanism,
and the paper's stated mechanism is not the operative one.

`0tjt` also closed saying no witness pins the concrete `x*`, `y₀*`, `t`, `G`,
`M`. `a-K-via-lp-dual-hecke-basis.witness.json` does, and did at the time.

### The `a_K` chain: no unguarded division exists

Four divisions by a dual in the corpus, **all four guarded**:

| script | expression | guard |
|---|---|---|
| `aK_via_lp_dual_full.py:198` | `1 + chirality_dual_sum / abs(u0_star)` | `abs(u0_star) <= 1e-12` → `None` |
| `aK_via_lp_dual_hecke_basis.py:191` | `1 + chi_y_sum / abs(u0)` | `abs(u0) > 1e-12` → else `None` |
| `probes/ak_lp_dual_quotient_probe.py:189` | `1 + chir / abs(y0)` | `abs(y0) > 1e-12` → else `None` |
| `aK_via_lp_dual.py:185` | `1 + chi_contrib / abs_tr_M` | divides by the **trace**, not a dual |

Nothing divides by a `y_λ*`. So the "other divisions by a zero dual" this bean
went looking for **do not exist**. Two things turned up instead.

### (a) `aK_via_lp_dual.py` calls Plancherel weights shadow prices

Its header says a_K is "the **chirality-active dual sum** of the
operator-selection LP per `prop:mass-coefficient-shadow-price`", and its `y_λ`
come from `load_chi_cache` — `chi-proton-h3-at-q0-50dps.witness.json`, whose
own description is *"χ^λ_q(β_atomic) per partition, evaluated at q_0 via the
Hoefsmit seminormal basis"*. Those are **Markov-trace Plancherel weights**, not
LP duals. Checked, not inferred:

    y_[3]·χ^[3] + y_[2,1]·χ^[2,1] + y_[1,1,1]·χ^[1,1,1]
      = 0.505404·1.382494 + 0.247298·1.807703 + 0·(-0.739224)
      = 1.14575969…  =  tr_M_at_q0 ,

exactly the trace decomposition `tr_M(β) = Σ_λ y_λ χ^λ(β)`. The script's own
wiring note concedes it: *"the emitted witness has the LP-dual required fields
… even though the 'primal' is a direct decomposition rather than an LP solve"*,
and `y0_star` / `y_star` are emitted as **strings pointing at other fields**.

The consequence is a reading hazard. The three scripts look like a progression
— B.1a → B.1a-rev.4 → B.1a-rev.5 — in which the later, more rigorous LP solves
return `None` while the first returns finite numbers. The truth is the reverse:
only the later two compute what `prop:mass-coefficient-shadow-price` defines,
and they report it degenerate. The first computes a different quantity that
happens to be well-defined.

Also worth noting inside the Plancherel reading: `y_[1,1,1] = 0` **exactly**.
`Λ^chi = {[3], [1,1,1]}`, so `a_K^{D-sc}` and `a_K^{D-chi}` are one-term sums
presented as sums over the chirality-active set — and the vanishing term is the
sign block, the same q-antisymmetriser that spans the trace-form radical, seen
from the Plancherel side.

### (b) `y₀* = 0` is in **13** committed witnesses, not 2

Swept every `*.witness.json` for a `y0_star` field (`max|y₀*| ≤ 1e-12`):

```
confinement-lp                              lp-duality-check
a-K-via-lp-dual-full                        a-K-via-lp-dual-hecke-basis
all-nuclides-sdp-admissibility              co-bond-order-active-set
he3-pairknot-composite-lp                   molecular-frobenius-lp
pn-alpha-lp-dual                            frobenius-repose
qbeta-confinement-sdp-offset-homogeneity    qbeta-c3-barodd-binding-sdp-dual
qbeta-symbolic-sdp-strict-complementarity   wedderburn-pair-volumes
```

**Not claimed: that all thirteen share this bean's mechanism.** Nine of the
eleven producing scripts build a trace-form/Gram object, which is where the
mechanism lives; `all_nuclides_sdp_admissibility` and `co_bond_order_active_set`
mention neither, so at least two zero duals have a different cause. Whether
each of the nine satisfies `y_0_eq_zero_of_radical`'s actual hypotheses
(`Gv = 0`, `⟨t,v⟩ = 0`, `Σvⱼ ≠ 0`) is a per-script check I have **not** run —
`pin3` is the standing reminder that a shared symptom is not a shared cause.

The useful control: `rho-k-h3a-lp-dual` reports `y₀* = 8.671`. It is a real
`scipy.linprog` solve over a Wedderburn refinement with a Plancherel or
Frobenius cost — trace-adjacent and **not** degenerate. So this is not "every
LP in the corpus".

### The guard threshold sits below where the degeneracy lands

All four guards test `1e-12`. Two committed witnesses report a net-constraint
dual in the band `1e-12 < |y₀*| < 1e-7`:

- `borromean-axial-coupling` — `1.076e-10`
- `habiro-correction-shadow-price-test` — `5.949e-08` (and
  `nucleus-real-sdp-he4`, `5.933e-08`)

Neither divides by it today, so nothing is wrong now. But a guard at `1e-12`
would pass on `1.08e-10` and return a quotient inflated by ~1e10 with no
signal. The guard is calibrated to floating-point zero, not to the scale at
which these solves actually report a vanishing dual.

## Next

- [ ] **Owner ruling** on `prop:mass-coefficient-shadow-price` — the only item
      left on this bean.
- [x] Re-word the box justification in `operator_selection_lp.lean` and `0tjt`
- [x] Re-read the `a_K` chain for other divisions by a zero dual — none exist

---

## 2026-08-22 — CORRECTION to the "sharper consequence" of 2026-08-21

That section overstated the case against `prop:mass-coefficient-shadow-price`,
and re-reading the `a_K` chain is what caught it. **I had the wrong LP.**

It said:

> `y_star = e₀` says **every Frobenius shadow price except index 0 is exactly
> zero**, and index 0 is `𝟙`, the identity element — not a partition block at
> all. So if mass coefficients are Frobenius shadow prices, then on this LP
> **all but one coefficient is zero**.

`y_star = e₀` is from `a-K-via-lp-dual-hecke-basis`, which solves over the
**NF basis of `H₃`** — six basis *elements*. The block indexes its coefficients
by **partition** `λ ⊢ k`. Those are different index sets, and the inference
across them does not go through.

The LP whose duals *are* per-partition is `a-K-via-lp-dual-full`
(`aK_via_lp_dual_full.py`, which emits `u_lambda_star = result.y_star[i]`
alongside each partition). Its committed duals for the proton, `H₃`:

| λ | `y*_λ` | active |
|---|---|---|
| `[3]` | **1.0** | yes |
| `[2,1]` | **1.0** | yes |
| `[1,1,1]` | 0.0 | no |

`active_set = [0, 1]`. **Two of three are nonzero**, not one of six. So
`c_λ = y_λ* · m_e` is *not* contradicted at `H₃` by the committed numerics, and
the factorisation `uStar λ = C_λ · S_λ` is satisfiable with `S_λ` a unit for
both nonzero blocks — which is what `coefficient_nuclear_independent` needs.

And the one zero has a **stated, different cause**. The script's own status
string says so:

> "under convention D the `l(lambda) >= 3` blocks vanish identically, so this
> LP needs re-posing on the two-row quotient"

`[1,1,1]` has three rows. Its Plancherel weight in the chi-cache is `0.0`
exactly for the same convention reason, so `C_[1,1,1] = w̃·h/2 = 0` makes
`uStar = C·S = 0` **consistent** rather than contradictory. That is a
convention artefact worth its own scrutiny; it is not the trace-form radical.

### What survives unchanged

- `y₀* = 0` in **both** LPs, forced by the radical, exact in ℚ(q). Stands.
- The dual objective `n_target · y₀*` is therefore `0` for every `n_target`, so
  the *net-constraint* shadow price prices nothing. Stands — and it is the
  claim this bean's title makes.
- Every `a_K` extraction that **divides** by `y₀*` is undefined:
  `a_K^{dual_ratio}`, `a_K^{chi-active}`. Both scripts return `None` and say
  why. Stands.

### What the owner ruling is actually about, then

Narrower than the 2026-08-21 note implied, and still real: the block ties mass
coefficients to **Frobenius** shadow prices, and those look fine at `H₃`. What
does not work is the surrounding *extraction machinery*, which routes `a_K`
through the **net-constraint** dual — and that one is identically zero. So the
question is not "are the coefficients zero" (they are not) but "can `a_K` be
recovered from this LP at all", and the answer from both committed solves is
no, by a structural identity rather than by numerical noise.

The `[1,1,1]`-vanishes-under-convention-D note is a second, independent thread:
if `ℓ(λ) ≥ 3` blocks vanish identically, an `H₃` LP over three partitions is
really an LP over two, and the script says it "needs re-posing on the two-row
quotient". Nobody has re-posed it.

Recorded on the block as a `caveat` authorNote. `validation` left at
`validated`: the Lean is a §3b conditional carrier
(`MassCoefficientShadowPrice.factor` is a *hypothesis*), its three theorems are
sorry-free consequences, and nothing above shows the class uninhabited.

## 2026-08-22 (second) — lead with the identity, not the radical

`qou/augu` tested the thirteen zero-dual witnesses against
`y_0_eq_zero_of_radical`'s actual hypotheses. The radical is **not** the
operative one, and this bean's framing sent that search the wrong way.

`y₀ = 0` being *attained*, with optimal value 0, needs only `t = G e₀` — the
cost vector is a Gram row because the basis contains the identity. Then
`(0, e₀)` is dual-feasible with objective 0, and `Σⱼtⱼxⱼ = (Gx)₀ ≥ 0` is one of
the constraints. `k4f8` says this and has the Lean lemma
(`dualCertificateExists_of_cost_eq_gram_row`, hypothesis `ht` alone).

`y_0_eq_zero_of_radical` proves something strictly stronger — that `y₀ = 0` is
**forced** for every dual-feasible pair — and that *does* need the radical. It
is the uniqueness refinement, not the cause.

The discriminating datum: `frobenius-repose` reports `gram_rank = 6`,
`gram_invertible = true`, **and** `y* = e₀`. An invertible Gram with the same
certificate. Twelve of thirteen witnesses show `e₀`.

This bean's title stays accurate for `H₃` — `y₀* = 0` *is* forced there by the
radical. But anyone reading it as the explanation of a zero dual elsewhere will
go looking for a radical that need not exist.
