---
# bind
title: 'binding_link_volumes: the Hopf substitution tests the volume, not the hyperbolic flag'
status: todo
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
