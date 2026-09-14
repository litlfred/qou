# Walking the canonical chain: where do conditions emerge? (2026-09-14)

**Bean** `qou-u96j` · **Probe**
[`computations/audits/canonical_chain_condition_walk_probe.py`](../../computations/audits/canonical_chain_condition_walk_probe.py)
(5/5, exit 0)

## What this asks

[`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
states the chain as eleven steps from the substrate `q₀` to MeV observables, each
written as though its output follows from its input. This walk asks a different
question at each step: **what condition enters that the previous step does not
force?**

A condition being unstated is not the same as its being wrong. Everything below
is scope (a) — measured observations about what the corpus contains, with no
invariant excluding any reading. The reason to surface them anyway is that the
cheat sheet is, in its own words, "the PRIMARY coordination document for the
canonical chain": it is what agents reason from.

## 🛑 This is a PARTIAL walk

Measured here: **steps 5, 6 (partially) and 10**. Step 2's condition is already
documented in the cheat sheet itself and is cited, not re-derived.

**Not yet walked: steps 1, 3, 4, 7, 8, 9, 11.** Named so the gap is visible
rather than implied. Step 3 in particular is expected to carry one (the Markov
trace's "unique" is unique *given* a parameter `z`, which is the fork
`qou-99qc` / `qou-qqm4` have been carrying) but this walk did not establish it
from the corpus and so does not assert it.

---

## Step 2 — the geometry→algebra bridge (already documented)

The cheat sheet's own §2a records it, downgraded from "✅ proved" on 2026-08-25:
the curvature 2-form is **stipulated** to be the Hecke quadratic, so setting it
to zero recovers it tautologically, and `prop:hecke-spectral-sequence` has **0
`label:` declarations** in `content/`. Cited here for completeness of the walk;
nothing in this audit adds to it.

---

## Step 5 — Wedderburn + partitions

The step is stated as

> `H_n(q) ≅ ⊕_{λ ⊢ n} M_{d_λ}(ℚ(q))`;  `tr_M = Σ_λ y_λ χ^λ`

— a sum over **all** partitions of `n`.

### C5a — the sum runs over TWO-ROW partitions only

Measured against the committed `computations/y-lambda-at-q0.witness.json`
(anchor `proton`, `q₀ = 1.1099785827513808…`): at **every `n` from 2 to 12**,
every `y_λ` whose partition has **three or more rows is exactly 0**, and every
nonzero one has **at most two rows**. At `n = 12` that is 7 nonzero against 70
zero.

The production family is `y_lambda_su_n(n, q, 2)` — the trailing `2` is a row
cap. AGENTS.md does say "convention D = the two-row truncation", so the fact is
known; what is missing is that **the chain's own step statement does not carry
it**. An agent reading step 5 would expect a sum over all `p(n)` partitions.

### C5b — `α` is not an ad-hoc ratio; it is a Wenzl weight

`y_(3)` at `n = 3` equals `(q⁴+1)/(q²+1)²` **exactly** (agreement to 45 dps;
`|diff| = 5.0e-47`, at the witness's serialization floor).

That is the same `α` the 2026-09-08 `Q_β` ruling names as the
augmentation-to-`z_D` factor, and the same `α` that
`QOU/Hecke/MarkovCrossingReversal.lean` (#7334) found relating the two admissible
cells of the flavour split. It was the **trivial block's Wenzl weight** all
along. Two arcs that reached `α` independently were both reaching this.

### C5c — the normalisation is dimension-weighted

`Σ_λ d_λ · y_λ = 1` exactly at every `n` from 2 to 12. This is just `tr_M(1) = 1`
expanded, since `χ^λ(1) = d_λ`.

The **unweighted** `Σ_λ y_λ` is 1 only at `n = 2`, where every `d_λ` is 1, and
then falls away: 0.7527, 0.5666, 0.3804, … , 0.0133 at `n = 12`.

**Recorded because the author got it wrong first.** My initial reading of the
witness was the unweighted sum, from which I drew a false "the `y_λ` are not a
probability measure" conclusion. They are one, under the correct weighting. This
is also distinct from the `w_λ(q)` non-normalisation AGENTS.md's notation
register describes (0.987 / 0.982 / … at `n = 3/4/…`) — that is the **quantum
Plancherel** family, a different object with different numbers, and the register's
"never conflate the three weight families" rule is exactly what keeps them apart.

---

## Step 10 — the confinement SDP

### C10a — `n_target` carries three inequivalent production meanings

The spec block
[`mba-step10-confinement-sdp.md`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step10-confinement-sdp.md)
declares *"Target net constraint `n_target ∈ ℤ≥0`"* — an **integer**. Measured at
source, the three production callers pass three different kinds of thing, each
citing a different authority:

| caller | value | kind | cites |
|---|---|---|---|
| `aK_via_lp_dual_hecke_basis.py:175` | `n_target = tr_M_atom` | **real** — a Markov trace | `prop:mass-coefficient-shadow-price` |
| `pn_alpha_lp_dual.py:375` | `target_net = float(pn_vec.sum())` | **real**, and α-dependent | its own `net(pn_α)` |
| `option_b_proton_mass_full_chain.py:588` | `n_target = float(n_gg)` | **integer** — γγ insertions | "AGENTS.md §LP/SDP duals" |

Only the third matches the declared type. `n_target` is the constraint that
*selects* `T_w`, so this is the condition that emerges at step 10 — and the
corpus does not have one definition of it.

*In fairness:* `option_b_proton_mass_full_chain.py` says in its own comment that
its `t = [1,1,1]` and `G = identity` are a "minimal end-to-end demo — replace
with full Gram for real chain", so it should not be read as the production chain.

### C10b — the cheat sheet states an objective the code does not have

The cheat sheet's §1 diagram and §2 table both render step 10 as

> `min ‖tr_M(T_w) 𝔈₀ − B_tgt‖` over GB-NF

The authoritative algorithm block has **no `B_tgt`**:

```
minimize   Σ_i t_i x_i
subject to net(x) = n_target,  G x ≥ 0,  x ≥ 0
```

and the canonical entry point is
`pyhecke.lp_dual_solver.solve_operator_selection_lp(t, G, n_target)` — no
target-binding argument exists in the signature.

**This defect points the safe way** — the document makes the chain look *more*
fitted than the code is — but it is in the primary coordination document, and an
agent reading it would conclude step 10 minimises distance to a measured binding
energy, i.e. that the chain fits AME at its selection step. It does not.

---

## What the walk has produced so far

Two steps, each carrying a condition its own statement omits; one identification
(`α` = Wenzl weight) that retires an apparent coincidence across two arcs; one
documentation defect in the primary coordination document; and one self-correction.

**Next** (not done here): step 3's "unique trace", which is where the `z`
parameter enters and therefore where the `qou-99qc` / `qou-qqm4` fork is most
likely to be rooted.
