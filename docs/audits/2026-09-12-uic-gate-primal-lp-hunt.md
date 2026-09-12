# The primal LP behind the UIC Pass-2 sign gate: it exists, and complementary slackness on it does not give the gate

**Date:** 2026-09-12
**Branch:** `claude/uic-gate-primal-lp-hunt-2026-09-12` · PR #7251
**Beans:** `qou-8urh` (this hunt); appends to `qou-t6be`, `qou-zlra`, `qou-brng`
**Verdict:** **case (b)** — the LP exists; complementary slackness on it yields
something else. **This does not reverse the owner's decision to drop the gate.**

---

## 1. Why this exists

On 2026-09-12 the owner was offered four options for the Pass-2 sign gate in
`hecke_core_legacy.unified_iterative_correction` and selected **two**: *drop the
gate* **and** *hunt the primal LP*. This document is the second. A separate
agent drops the gate; **this branch does not modify
`computations/hecke_core_legacy.py`** — it only reads it.

The question, stated so it can be answered:

> The gate's comment derives it from complementary slackness on a primal linear
> program. Does that LP exist anywhere in the corpus, and if it does, does
> complementary slackness on it yield the sign gate — or something else, or
> nothing?

Three admissible outcomes were fixed in advance:

- **(a)** the LP exists and CS on it yields the sign gate — the gate is
  derivable, and the drop decision should be reversed;
- **(b)** the LP exists and CS on it yields something else;
- **(c)** no such LP exists — the justification never had a referent.

---

## 2. The gate, and its comment quoted in full

The gate itself, `computations/hecke_core_legacy.py:2176-2199`:

```python
    # ── Pass 2: final-state complementary slackness gate ─────────
    # LP duality theorem: on the OPTIMAL primal-dual pair (Φ*, y*),
    #   y_λ* × ⟨Φ*, π_λ⟩_F = 0  for every partition λ.
    # So y_λ* > 0 only when the Frobenius constraint is TIGHT at the
    # atom's FINAL state, i.e. tr(M_λ(W_atom)) ≤ 0.  Partitions with
    # positive final trace are SLACK → y_λ* = 0 → zero contribution.
    # Replace cumul_total with the gated sum over tight partitions.
    gated_total = _mp.mpf(0)
    n_tight = 0
    for s in state:
        if s.get('final_tr_sign', 1) <= 0:
            gated_total += s['cumul_partition']
            n_tight += 1
```

and the gated sum is the function's return value (`:2199` in the
`return_per_step` arm, `:2207` otherwise).

Two companion passages invoke the same argument. At `:2079-2084`, in the
accumulation loop:

```python
            # LP complementary slackness is a FINAL-STATE condition:
            # y_λ* × tr(Φ_λ*) = 0 on the SOLVED LP.  The per-step
            # tightness filter would be a heuristic approximation of
            # this; experimentally it over-gates (k-instability).
```

and at `:1997-2012`, disposing of the q-Gaussian fallback partitions:

```python
        # Per-step tightness gate: sign of approximated trace.  The
        # approximation gives log_trace directly; the TRACE sign is
        # positive (trace ~ exp(log_trace)).  Positive trace ⇒ SLACK
        # Frobenius constraint ⇒ y_λ* = 0 by complementary slackness.
        # In this approximation the trace is always +ve, so by LP
        # duality the partition contributes ZERO at this step.
```

So three sites, one argument. The load-bearing inference is the same each time:
**positive trace ⇒ slack ⇒ `y_λ* = 0` ⇒ zero contribution**, with the gate
keeping the complement.

---

## 3. The surface searched

All six corpus-grep paths, per AGENTS.md §"Before declaring open". The LP might
have been present under another name, so the search was by *constraint shape* as
well as by label.

| path | what was searched | result |
|---|---|---|
| 1 — `docs/audits/` | `operator-selection-lp`, `operator_selection_lp`, `complementary slackness` | 30+ hits; `lp-duality-feasibility.md`, `2026-05-09-paper-simplification-iterative-lp-dual.md` |
| 2 — `content/` | same | **`mass-theory/operator-selection-lp.md`** — the LP, stated in full; plus `knot-operator-lp-selection`, `spin-involution-lp-dual-invariance`, `mba-step10-confinement-sdp` |
| 3 — `computations/` | `solve_operator_selection_lp`, `solve_psd_operator_selection_sdp`, partition-indexed LP | 20+ consumers; **`probes/h6_block_selection_lp_probe.py`** is the on-point one |
| 4 — coordination ledgers | `ck-dk-canonical-registry`, LP-dual ledgers | no separate partition-indexed program |
| 5 — `library/` | not reached: the LP is authored corpus, not a citation question | n/a |
| 6 — `.beans/` | `final_tr_sign`, `unified_iterative_correction`, `complementary slackness` | 25 hits; **`qou-k4ul`**, `qou-2zr3`, `qou-cxgx`, `qou-k4f8`, `qou-fr4d` |

Two candidates were checked and are **not** the LP, recorded so the next agent
does not re-check them:

- **`computations/audits/lp_accumulator_kernel_gate.py`** — the name is a
  coincidence. It verifies that the Rust kernel
  `pyhecke_native.lp_accumulator_step_traces_mpfr` reproduces a pure-mpmath
  reference of the *matrix recurrence*. It solves no program and says nothing
  about the gate.
- **A partition-indexed LP.** There is none. Every operator-selection program in
  the corpus is indexed by **basis elements of `H_n(q)`**, not by partitions —
  see §4.

---

## 4. The LP exists, and what it actually says

**`prop:operator-selection-lp`**
(`content/quantum-observable-universe/mass-theory/operator-selection-lp.md`),
formalised sorry-free as `QOU.ParticleInteractions.operator_selection_lp`
(`content/quantum-observable-universe/lean/QOU/ParticleInteractions/operator_selection_lp.lean`).
Let `{b_1, …, b_d}` be a basis of `H_n(q)` with `d = n!`, `t_i = tr_M(b_i)`, and
`G_{ij} = tr_M(b_i b_j)` the Frobenius Gram. The program is

$$
\min_{x \in \mathbb{R}^d} \sum_i t_i x_i
\quad\text{s.t.}\quad
\sum_i x_i = n_{\text{target}},\qquad
(Gx)_i \geq 0 \ \forall i,\qquad
x_i \geq -M .
$$

Complementary slackness, as the Lean states it
(`OperatorSelectionLpContext.complementary_slackness_x_star`):

```lean
∀ i, ctx.s i * (Finset.univ.sum fun j => ctx.G i j * ctx.x_star j) = 0
```

i.e. `s_i · (Gx*)_i = 0`, where `s` is the vector of Frobenius multipliers (the
narrative's `y*`) and `(Gx*)_i` is the constraint value at the LP's own
optimiser.

### The four mismatches

Each is independently fatal to the comment's inference.

1. **Index set.** The LP's constraints are indexed by NF basis elements,
   `d = n!` of them. The gate is indexed by partitions, `p(n)` of them. At
   `n = 3` that is 6 against 3. No LP in the corpus has partition-indexed
   Frobenius constraints, and §5 explains why one would not help.

2. **Argument.** `(Gx*)_i` is a function of the LP's *decision variable* — the
   operator being selected. `tr(M_λ(W_atom))` is a datum of the atom, fixed
   before any optimisation, entering the LP only as a cost coefficient.
   Complementary slackness constrains an optimiser; the gate reads an input.

3. **Direction — the sharpest one.** `IsFeasible` requires `0 ≤ (Gx)_i` for
   every `i`. "Tight" therefore means `= 0`, never `≤ 0` non-trivially: on any
   feasible point `(Gx)_i ≤ 0` and `(Gx)_i = 0` are **the same predicate**
   (`frobeniusValue_nonpos_iff_eq_zero`, proved). So if the gate's quantity
   really were a Frobenius constraint value, the sign gate *would be* the
   tightness gate — and the tightness gate keeps only blocks sitting exactly at
   zero. The producer keeps 4 of 10 at `A = 2` and returns `−0.0896`, so its
   quantity is not a constraint value of any feasible point of this LP.

4. **The optimum is not unique, so "the OPTIMAL primal-dual pair" is not well
   defined.** On the NF basis the block proves its own optimal value is
   identically zero for every `n`, `q` and trace convention — the basis contains
   the identity, so `G`'s first row *is* the cost vector and the program
   minimises `t·x` subject to `t·x ≥ 0` — and strong duality then forces
   `y_0* = 0` (`QOU.ParticleInteractions.y_0_eq_zero_of_radical`). The minimiser
   set is a positive-dimensional face carrying at least six vertices at `n = 3`,
   in mirror pairs, none mirror-symmetric. So which `y*` a solver returns is a
   property of its pivoting rule, and the comment's "`(Φ*, y*)`" does not name a
   unique object.

   > **Scope this to the NF basis — I did not, and the measurement corrected
   > me.** The draft of this document asserted `y_0* = 0` of the
   > Wedderburn-block instance too. **It is false there, and measurably so:**
   > the probe records `y_0* = 0.0347` (²H) and `0.0130` (⁴He), identical across
   > all five targets. The reason is the hypothesis, not the arithmetic —
   > `y_0_eq_zero_of_radical` requires `t_j = G_{i₀ j}`, the cost vector to *be*
   > a row of the Gram. A diagonal Gram has row `λ` equal to
   > `(0, …, t_λ, …, 0)`, which is the cost vector only when `d = 1`. So the
   > degeneracy is a property of the identity-containing NF basis and does not
   > transfer.
   >
   > This **strengthens** the separation rather than weakening it: the two
   > programs differ in their dual behaviour as well as their index set. It is
   > recorded because the failing assertion was mine, and because "the LP's
   > `y_0*` is zero" is exactly the kind of claim that gets quoted one basis
   > over.

---

## 5. Why a partition-indexed version would not rescue it either

The natural repair — re-index the LP by Wedderburn blocks so `y_λ` is literally
per-partition — fails structurally, and this was already measured in the corpus
before this hunt began.

Wedderburn block projectors are **orthogonal idempotents**, `P_λ P_μ = δ_{λμ} P_λ`.
The Frobenius Gram on that basis is therefore

$$
G_{\lambda\mu} = \mathrm{tr}_M(P_\lambda P_\mu) = \delta_{\lambda\mu}\,\mathrm{tr}_M(P_\lambda),
$$

**diagonal by construction**. Complementary slackness then decouples to
`s_λ · G_{λλ} · x_λ = 0` (`complementarySlackness_diagonal_iff`, proved) — an
equation in the multipliers, the block norms and the *selected operator's*
coefficients. **The atom's traces do not occur in it at all**, so no predicate
on `t_λ` follows from it.

`computations/probes/h6_block_selection_lp_probe.py` reached the same place from
the numerical side on the `H_6` blocks: sweeping the net constraint across the
whole reachable range, the active set is never fewer than 10 of 11, and a
controlled diagnostic (same `t`, same target, only `G` changed) gives 5-of-6
active for `G = diag(t)` against 3-of-6 for a dense PSD `G`. Its conclusion —
*"the LP's discriminating power comes from the OVERLAP between candidate
operators … orthogonal blocks have none, so there is nothing to select on"* — is
the same fact this document proves.

---

## 6. The refutation, exhibited

`QOU.MassTheory.UICGateLP.exists_lpData_activeSet_gateSet_disjoint` (proved,
`decide`) exhibits data satisfying **every** hypothesis of the operator-selection
LP — non-negative multipliers, dual feasibility `t_j = y_0 + Σ_i s_i G_{ij}`, the
net constraint, Frobenius positivity, and complementary slackness — in which the
active set and the gate set are **disjoint**:

| | value |
|---|---|
| `d` | 2 |
| `G` | identity |
| `x*` | `(1, 0)` |
| `n_target` | 1 |
| `s` (multipliers) | `(0, 2)` |
| `y_0*` | `−1` |
| `t` (forced by dual feasibility) | `(−1, 1)` |
| active set `{i : 0 < s_i}` | `{1}` |
| gate set `{i : t_i ≤ 0}` | `{0}` |

Both sets are non-empty; their intersection is empty. So on the very program the
comment cites, **`y_λ* > 0` does not imply `t_λ ≤ 0`.**

The same data are packaged as `ctxW`, built through the corpus's own
`OperatorSelectionLpContext.ofCertificate`, which *derives* the zero duality gap
from the certificate rather than taking it as a field — so the witness is a
genuine instance of the LP, not a restatement of it. `ctxW_t`, `ctxW_s` and
`ctxW_G` identify its fields with the data above by `rfl`.

---

## 7. Verdict, and scope

**Case (b).** The LP the gate's comment invokes **exists** and is formalised
sorry-free. Complementary slackness on it does **not** yield the sign gate. What
it yields instead is a condition on the selected operator's Frobenius constraint
values — non-negative on every feasible point, hence the "`≤ 0`" reading
collapses to the tightness gate, which keeps only blocks at exactly zero.

**Scope classification, per AGENTS.md §"Before declaring refuted": this is a
scope-(b) structural exclusion, and the invariant is named.** The invariant is
**primal feasibility of the Frobenius constraints** — `0 ≤ (Gx)_i`, a defining
conjunct of `IsFeasible` — together with the **orthogonality of the Wedderburn
projectors**, which makes the block-indexed Gram diagonal. Neither depends on
`n`, on `q`, or on the trace convention, so the exclusion holds for all of them.

**What this does NOT claim.** It does not say the gate's *numbers* are wrong. It
does not exclude some other selection principle for the blocks — `h6_block_…`
explicitly leaves a non-orthogonal operator basis open, and that remains the
natural next thing to try. It says only that *this* justification has no
referent, which is what the hunt asked.

**Does it reverse the drop decision? No.** Outcome (a) was the only one that
would have, and (a) is refuted by §6 with an explicit counterexample inside the
LP. The gate may be dropped on the owner's ruling without losing a derivation,
because there was none to lose.

---

## 8. A finding for the file itself

The producer already carries an owner-ruled correction saying exactly what this
document proves — and it never reached the gate.

`lp_shadow_price` (`hecke_core_legacy.py:328-374`), corrected 2026-09-05 under
owner ruling in PR #6752:

> NAMED for the LP shadow price; it is not one. … This docstring said `y_0` "is
> the dual variable of the normalisation constraint `1ᵀx = n_target`". That is
> false, in two independent ways: … The actual net-constraint dual of
> `prop:operator-selection-lp` is IDENTICALLY ZERO, for every `n_target`, at
> every `n` and `q`. … Proved in the content block (commit `6b7d2ec4a8`) and in
> Lean (`y_0_eq_zero_of_radical`); confirmed by every committed solve.

So **one file asserts both**: at line 330 that its `y_λ` are not LP duals and its
`y_0` is not a shadow price, and at line 2177 that `y_λ* × ⟨Φ*, π_λ⟩_F = 0` "on
the SOLVED LP" justifies the gate 1 800 lines below. The 2026-09-05 correction
was applied at the naming function and stopped there.

This is worth recording as a *class*, not an incident: a correction landed at the
site that carries the offending **name**, while the site that carries the
offending **reasoning** used a different vocabulary (`final_tr_sign`,
`complementary slackness`) and was missed by whatever grep found the first one.
The same shape recurs throughout AGENTS.md's own correction history.

**Also noted in passing, not acted on** (it is outside this hunt's scope and
belongs to the owner): `hecke_core_legacy.py:397-400` states that *"Empirical
sweep with q-heat resolvent damping shows K = 6 is the OPTIMAL partition
cutoff"*. AGENTS.md §"NO FITTING, EXCEPT CAL-1/2/3" names that construction
verbatim as fitting — *"Sweeping a discrete parameter for accuracy. 'Empirical
sweep shows K = 6 is the OPTIMAL cutoff' is a fitted parameter. Optimal against
what? The data."* Flagging it here so it is on the record; no change made.

---

## 9. Artifacts

| artifact | what it carries |
|---|---|
| `content/quantum-observable-universe/lean/QOU/MassTheory/UICGateNotFromComplementarySlackness.lean` | 8 declarations, `lean`-direct exit 0, all sorry-free |
| `computations/probes/uic_gate_vs_lp_complementary_slackness_probe.py` | the gate measured from the producer; the LP solved on the same ten blocks through `lp_dual_solver`, emitting `y0_star` / `y_star` / `active_set` / `primal_obj` / `dual_obj` / `duality_gap` |
| `computations/probes/uic-gate-vs-lp-complementary-slackness.witness.json` | the numbers |

### Lean declarations

| declaration | statement |
|---|---|
| `frobeniusValue_nonpos_iff_eq_zero` | on a feasible point, `(Gx)_i ≤ 0 ↔ (Gx)_i = 0` |
| `gateSet_eq_tightSet` | the same at the corpus context's own `x*` |
| `frobeniusValue_of_diagonal` | a diagonal Gram collapses `(Gx)_i` to `G_{ii} x_i` |
| `complementarySlackness_diagonal_iff` | CS then decouples, and the cost vector does not occur |
| `exists_lpData_activeSet_gateSet_disjoint` | the refutation (§6) |
| `ctxW_t` / `ctxW_s` / `ctxW_G` | the witness is a genuine `OperatorSelectionLpContext` |

Verification: `lean -DautoImplicit=false -s 65536`, toolchain `v4.24.0`, against
the restored olean cache with the corpus LP module shadow-compiled first.
`#print axioms` on all eight reports `[propext, Classical.choice, Quot.sound]` —
no `sorryAx`.

---

## 10. Independent confirmation from the sibling branch, and one bean that could not be appended

**A second agent reached "tight means `tr = 0`, not `tr ≤ 0`" by a different
route, and this was verified rather than taken on trust.** The task framing named
`QOU.MassTheory.UICFunctionalSelection.uicGated_cs_eq` as already established.
It is **not on `main`** — `git ls-tree origin/main` finds no
`UICFunctionalSelection` — so it was read where it actually lives, on
`origin/claude/uic-functional-resolution-2026-09-12` (PR #7237). Its own
docstring, lines 31-32 and 129:

> `uicGated_cs_eq` — under **genuine** complementary slackness for a constraint
> `⟨Φ, π_λ⟩ ≥ 0`, "tight" means `tr = 0`, and then the gated functional collapses
> …
> makes "tight" mean `tr = 0` — not `tr ≤ 0`, which is what the producer codes.

That is the same conclusion as §4 item 3 here, reached from the **functional's
own structure**. This document reaches it from the **corpus LP's feasible set**:
`IsFeasible` carries `0 ≤ (Gx)_i` as a defining conjunct, so `le_antisymm` gives
`(Gx)_i ≤ 0 ↔ (Gx)_i = 0` directly. Two independent confirmations of one
negative, which AGENTS.md §"Parallel exploration" counts as strengthening it.

What this document adds beyond that overlap: the index-set mismatch (§4.1), the
diagonal-Gram exclusion of any partition-indexed repair (§5), and the explicit
in-LP counterexample (§6).

**`qou-t6be` could not be appended, and that is recorded rather than silently
skipped.** It does not exist on `main` either — it is
`.beans/qou-t6be--resolve-the-uic-functional-mismatch-under-the-owne.md` on that
same unmerged branch. Creating it here would mint a second copy that conflicts on
merge, so the append was posted as a comment on PR #7237 instead
(`#7237#issuecomment-5648945079`). `qou-zlra` and `qou-brng` are on `main` and
were appended normally. All three stay **open** per AGENTS.md rule 13a.
