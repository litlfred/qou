# The CCG cosimplicial-identities declaration is a self-assuming projection, declared as a `def`

**Date:** 2026-08-26 · **Bean:** `qou-6tcn` (found while answering "do we need
more work on the groupoid?") · **Scope:** corpus hygiene, one declaration.

## Finding

[`ccg-cosimplicial-identities.lean`](../../content/quantum-observable-universe/lifting-and-descent/ccg-cosimplicial-identities.lean)
line 43 declares

```lean
def ccg_cosimplicial_identities
    {M : Type*} (ccg : CosimplicialCrossedGroupoid M) :
    (∀ n t, (ccg.coface (n+1) (ccg.coface n t)).level
          = (ccg.coface n (ccg.coface n t)).level)
    ∧ (∀ n t, (ccg.codegeneracy n (ccg.codegeneracy (n+1) t)).level
            = (ccg.codegeneracy n (ccg.codegeneracy n t)).level) :=
  ⟨ccg.coface_coface, ccg.codegen_codegen⟩
```

and `coface_coface` / `codegen_codegen` are **fields of the structure**
`CosimplicialCrossedGroupoid`
([`cosimplicial-crossed-groupoid.lean`](../../content/quantum-observable-universe/lifting-and-descent/cosimplicial-crossed-groupoid.lean)
lines 135 and 139). The body projects two assumed fields straight back out.

Two AGENTS.md rules meet here:

- **§3b-cond item 5** — *"A class that carries the block's own conclusion as a
  field, with a 'theorem' that merely projects it (`:= ctx.claim_foo`), is a
  vacuous self-assuming projection."* This is that, exactly.
- **§1a** — *"`theorem X : True := trivial` → `def X : True := trivial`. Every
  vacuity detector keyed on the provable kinds … re-declaring the same vacuous
  body as a `def` hid it from the entire audit."* This is a `def`, so the
  vacuity audit's provable-kind detectors do not see it.

The sole instance discharges both fields with `by simp` (lines 169–170), which
it can because the identities are stated on `.level` only and `.level` is
preserved by construction.

## What this is NOT

**Not deception, and not a `: True` vacuity.** The stated proposition is real,
and the docstring is honest about scope: *"this lemma packages the level-based
fragment that is immediately discharged from the structure."* The author knew.
The defect is that the **declaration's name** reads as a proved lemma about the
cosimplicial identities while its **content** restates them, and the `def` kind
keeps it out of the audit that would otherwise surface the gap.

**Not a claim about anyone else's groupoid work.** Two sibling commits read
*"the groupoid gate is ALREADY a theorem — second route added, no new claim"*
(`qou-5t4b`) and *"Route A: the groupoid must supply NON-SELF-DUALITY — one
checkable property"* (`qou-8pl3`). **I do not know which gate those refer to**,
and this note does not contradict them — it reports what one named declaration
in the corpus does. Route A's non-self-duality item is claimed by that sibling
and is deliberately untouched here.

## Honest dispositions

Per §1a the options are prove, queue, or demote:

1. **Prove** — derive the cosimplicial identities from the jet-prolongation /
   descent geometry rather than assuming them as fields. Real work.
2. **Queue** — restate as a `theorem` with `sorry` + a `-- Ref:` citation, which
   is the honest "stated, not yet proved" marker.
3. **Demote** — rename so the name matches the content (it *is* a legitimate
   accessor), and drop the "lemma" framing from the docstring.

**Nothing is changed here.** (3) is the cheapest and is probably right, but it
touches a file in an area a sibling is actively working, so it is recorded for
the owner rather than done unilaterally.

## Answering the question that prompted this

*"Do we need to do more work on the groupoid?"* — **not from this branch, and
not the work the sibling is doing.** The one thing this branch found is the
declaration above, and it is a hygiene item rather than a mathematical gap: the
cosimplicial identities are **assumed**, honestly documented as such in a
docstring, and merely mis-framed by a declaration name and kind.
