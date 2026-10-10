---
# qou-opjb
title: 'GAP: neutron-prediction-comparison displays p*(A) while naming n_pred(p), and its c = 0.01497 traces to an SEMF ratio, not to a definition in the corpus'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - split-from-6766
    - 8f-decide
created_at: 2026-10-10T08:12:47Z
updated_at: 2026-10-10T08:14:44Z
parent: qou-8lxd
---

Split out of `qou-6766` on 2026-10-10, which packed seven findings into its
title and therefore could not be claimed, worked or closed by anyone. Three were
enacted there; this is residual item (1) of four.

## The display mismatch, measured

`folio/quantum-observable-universe/observations/neutron-prediction-comparison.md`
is a **`proposition`** block. Its opening sentence promises one quantity and its
display defines another:

> "the beta-stability formula predicts a stable neutron number $n_{\mathrm{pred}}(p)$:"

then displays

```
p*(A) = A / (2 + c · A^{2/3}),    c = a_C / (2 a_A) = 0.01497
```

Different symbol (`n` vs `p*`), different argument (`p` vs `A`). The residual it
then reports is `|Δn|` (mean 1.7, max 8 at `p = 102, 103`).

**The parent proposition gives a different route, and the block skips it.**
`prop:beta-stability`
(`folio/quantum-observable-universe/nuclear-interactions/beta-stability.md`)
defines `p*(A) = A/(2 + a_C A^{2/3}/(2 a_A))` and then says: for a given `p`, the
stable mass number is the **fixed point** of `A*(p) = p(2 + (a_C/2a_A)·A*^{2/3})`,
with `n*(p) = A*(p) − p`. So `n_pred(p)` requires solving that fixed point. The
comparison block displays neither the quantity it names nor the route its own
parent specifies — it displays the parent's *first* formula, which is the inverse
map.

## The second defect, which is the one that needs the owner

**`c = 0.01497` is not derivable from the definitions the corpus states.**
`prop:beta-stability` gives `a_C = (q − q⁻¹)·λ_C` with **`λ_C` nowhere defined**,
and calls `a_A` "the Pauli asymmetry coefficient" with **no definition at all**.
So the numeral has to come from outside.

Arithmetic (circumstantial, not proof): the SEMF Coulomb and asymmetry
coefficients give `a_C/(2a_A) = 0.714/(2·23.7) = 0.015063`, 0.6 % from 0.01497;
at `a_A = 23.85` it is `0.014969`, matching to four digits. AGENTS.md's own
extensive-term section quotes `a_A` as "the SEMF asymmetry coefficient (23.7)",
so 23.7 is the value this corpus uses elsewhere.

If that is what it is, then under **§NO FITTING** this is the named case —
*"importing an empirical term … citing a phenomenological formula from the
literature (an empirical Wigner energy, an SEMF coefficient) imports somebody
else's fit"* — sitting inside a `proposition`, whose content is then a mean
discrepancy against observed isotopes across 103 elements.

## Options

1. **Trace `λ_C` and `a_A` and show `0.01497` is derived.** If it is, the
   objection dissolves and only the display mismatch remains. Cost: a corpus
   trace; this bean's author did not find a definition for either symbol.
2. **Keep the comparison, demote the block** `proposition` -> `remark` or
   `example`, state the SEMF import explicitly as an input. Cost: one `.ts` kind
   change plus label-reference updates; risk: the `prop:` label has consumers.
3. **Keep the kind, scope the claim** in prose as a comparison against an
   imported phenomenological ratio, not a prediction.
4. **Nothing.** The block keeps a proposition whose numeral's provenance is
   untraced and whose display defines the inverse of the quantity it names.

**Recommendation (agent judgement, not a finding):** do (1) first — it is cheap
and it decides between the others. If `λ_C`/`a_A` are genuinely undefined, (2).

**Default if unanswered: (4), nothing changes.**

**Blast radius:** `prop:neutron-prediction-comparison` +
`tbl:neutron-prediction-comparison-table-data` + its `-interpretation` sibling,
and whatever cites `prop:beta-stability`. Nothing in the mass / binding / Q_β
chain reads any of them.
