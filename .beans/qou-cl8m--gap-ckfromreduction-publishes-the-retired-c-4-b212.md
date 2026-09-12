---
# qou-cl8m
title: 'GAP: ckFromReduction publishes the RETIRED c_4 = b^2+1/2 at the retired POSITION, locked by a := rfl theorem'
status: todo
type: task
priority: high
created_at: 2026-09-12T07:32:12Z
updated_at: 2026-09-12T07:33:08Z
---

Spun out of `qou-54g5` 2026-09-12. That bean is about which `c_5` is current in
the NARRATIVE; this one is the Lean carrier, which nothing tracked — `grep -rl
ckFromReduction .beans/` returns **nothing**.

## What

`content/quantum-observable-universe/mass-theory/ck-extraction-from-algebraic-rules.lean:149-155`

```lean
noncomputable def ckFromReduction (q : ℝ) : ℕ → ℝ
  | 0 => 0
  | 1 => hoefsmitB_local q
  | 2 => (hoefsmitB_local q)^2
  | 3 => jonesHopfLocal
  | 4 => (hoefsmitB_local q)^2 + 1/2      -- ← the RETIRED form, at the RETIRED position
  | _ => 0                                 -- ← so ckFromReduction q 5 = 0
```

and 30 lines down, locking it:

```lean
/-- `c_4 = b² + 1/2` (mixed intra/inter-block, Kashiwara `b²` plus
    Hopf-half rational offset). -/
theorem ckFromReduction_eq_c4 (q : ℝ) :
    ckFromReduction q 4 = (hoefsmitB_local q)^2 + 1/2 := rfl
```

## Three checkable defects, and they disagree with the narrative in BOTH directions

The narrative table `stochastic-mechanics/ck-extraction-from-algebraic-rules-table2-data.md`
says:

| k | narrative | Lean |
|---|---|---|
| 4 | `c_3·b⁴ = −2b⁴` | `b² + 1/2` |
| 5 | `−(b² + ½)` | `0` (catch-all `| _ => 0`) |

1. **k=4: position AND sign both differ.** The supersession moved `b²+½` out of
   the `c_4` slot; the Lean never followed. The table's own annotation says so:
   *"the old `b² + 1/2` value belongs at `k = 5` with a sign flip; superseded"*.
2. **k=5: the Lean returns 0** where the narrative publishes `−(b²+½)` — which
   per `qou-54g5` is the **current** coefficient (6 sites; 2.4 % from the SDP
   extraction `−1.2229`). So the Lean is silent on the one rung that is live.
3. **The table contradicts ITSELF**: row `k = 5` gives `−(b²+½)` and the very
   next row `k ≥ 5` gives `0`.

## The theorem proves nothing

All five `ckFromReduction_eq_cN` are `:= rfl` — definitional restatements of the
match arms, not derivations. AGENTS.md §Strict Lean Discipline item 8 is exact:
*"if the answer is 'no, it's true by definition / by unfolding / by rfl,' then it
is not a theorem — it is notation."* This matters here beyond hygiene: it means
`ckFromReduction_eq_c4` gives the retired coefficient the **appearance** of a
proved result while deriving nothing, so a reader's natural check ("is it
proved?") returns yes for a value the corpus has retired.

Related but distinct: `qou-z3k1` covers definitional restatements as a class.
This bean is the specific wrong-value carrier.

## Already recorded — as a QA note with no tracker

`stochastic-mechanics/ck-extraction-from-algebraic-rules-table2-data.qa.json:1050`
carries all three defects, verbatim, marked *"STRUCTURAL FINDING (do not fix
inline — this is a math/Lean disagreement)"*, and proposes two routes: re-derive
the Lean to the superseded assignment, or re-scope the table + parent `.md` back
to the Lean's values. A sidecar note is not a work item; that proposal has been
sitting unactioned. It also flags that the parent narrative
`mass-theory/ck-extraction-from-algebraic-rules.md:9` prints `−2b⁴` too, so the
disagreement is corpus-wide, not confined to the table.

## NOT FIXED — and it needs the owner

Under the 2026-09-07 ask-first override neither exemption applies: this is not a
precision increase, and the corpus does **not** fix the answer — it holds three
incompatible positions (`−(b²+½)` current per the SDP extraction; `3c_3²+b` in
`_deprecated/`; `b²+½` at `c_4` in the Lean). Picking among them decides a
published ladder number.

Also note the whole ladder is **convention-C-frame** pending `qou-cds1`, so a
re-derivation here should probably wait on that rather than be done twice.

**Recommendation, marked as judgement:** the cheapest honest move is route 2 in
the Lean only — change `| 4 => b²+1/2` to match the narrative's `−2b⁴` and add a
`| 5 => −((hoefsmitB_local q)^2 + 1/2)` arm, then demote the five `:= rfl`
"theorems" to `example`s or delete them. That moves **no published number** (the
Lean has no compute consumer) while removing the retired value from the one
place a reader would trust most. But it is still an owner call, because it
asserts the narrative is the correct side.
