---
# bind
title: 'binding_link_volumes: the Hopf substitution tests the volume, not the hyperbolic flag'
status: completed
type: task
priority: low
tags:
    - computations
    - mass-binding
    - fragility
created_at: 2026-08-10T05:00:00Z
updated_at: 2026-08-10T05:00:00Z
---

`computations/binding_link_volumes.py` handles the degenerate deuteron link correctly and
honestly — `"2H": {"link": "Hopf (L2a1)", "vol": mpf("0"), "hyperbolic": False}`, with the
zero volume triggering a documented `Vol(𝓑₃) = 8G` substitution, printed as
`→ 8G (Hopf=0)`, and the whole thing recorded as an honest negative (+0.2% deuteron,
−60% at A ≥ 3).

**The fragility, which is not a bug today.** The substitution is

```python
v_eff = v if v > mpf("0.01") else VOL_B3
```

— it tests the **volume against a magic threshold** when the semantic flag
`"hyperbolic": False` is in the same dict.

It is safe *only* by a theorem: Cao–Meyerhoff put the minimum volume of a cusped
orientable hyperbolic 3-manifold at `2.0298832…` (the figure-eight and its sibling), so
nothing genuinely hyperbolic can fall under `0.01`. That is a real margin, but the code
does not say so, and the guarantee evaporates if the registry ever gains a non-cusped or
closed manifold, or if someone tunes the threshold.

**Fix:** `if not rec["hyperbolic"]`. One line, tests the thing that is actually meant, and
removes the dependence on a volume bound the file never cites.

While there: the docstring's claim that `Vol(Hopf) = 0` is now backed by a Lean theorem —
`QOU.Knot.FlatTet.BlochWigner_lob_ofReal` gives zero volume for **every** real shape, and
the trefoil case is worked in `QOU/Knot/FlatTetrahedra.lean`. Worth citing.

---
**2026-08-15 — DONE.** Branch `claude/fivetwo-level7-ladder-numerators`.

Both items delivered, plus one defect the bean did not anticipate.

**The fix as specified.** `v_eff = v if v > mpf("0.01") else VOL_B3` →
`v_eff = v if vols[iso]["hyperbolic"] else VOL_B3`, and the same swap in the print
branch that decides whether to show `→ 8G (Hopf=0)`. The Cao–Meyerhoff reasoning the
bean gave — nothing genuinely hyperbolic can fall under 0.01 — is now written into the
file as the *reason the old form was safe*, so a future reader knows the threshold was
load-bearing rather than arbitrary. **stdout is byte-identical before and after**
(verified by diff against a captured baseline), which is the expected result: the
change removes a fragility, it does not alter behaviour.

**The Lean citation as specified.** `QOU.Knot.FlatTet.BlochWigner_lob_ofReal` is now
cited in the docstring for `Vol(Hopf) = 0` — it gives zero volume for *every* real shape
with no hypotheses, so a degenerate link's volume vanishes identically rather than
numerically.

**Not anticipated: the docstring's headline number was wrong.** It claimed the deuteron
"matches at +0.2%". The script produces **−6.3%**, and the committed witness has always
recorded `deuteron_endomorphism_holds` as `"passed": false` with
`computed = 6.306958776805962` against `tolerance = 1`. Traced to its source: +0.2% is
exactly the claim that `Δtr(²H) = 0.5952`, which matches a hardcoded constant in
`binding_per_bond_decomposition.py:126` to four digits, while
`binding_canonical(1,1, use_closed_form=True)` returns `0.5566260326923999` today.
Docstring corrected here; the cross-corpus fix (≥ 7 files quote +0.2%) is **bean
`qou-jdhm`**, because choosing which Δtr is right is a physics judgement, not an edit.

**Witness deliberately not regenerated.** This container's python is weaker than the one
that produced the committed witness (mpmath 1.3.0 vs 1.4.1, sympy 1.14.0 vs 1.12, no
scipy, no pyhecke_native), and re-running shifts `computed` in the 8th digit for purely
environmental reasons. Committing that would have downgraded the recorded environment
and moved a number for a reason unrelated to the change. Reverted; the witness on disk
is the one from the stronger environment.

Guard: `scripts/probe-float64-guard.py --diff computations/binding_link_volumes.py`
reports 16 hits — **identical to the set at HEAD** (verified by stashing), so none were
introduced here. They are `float(...)` calls in print formatting, pre-existing.
