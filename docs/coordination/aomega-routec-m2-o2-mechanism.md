# A_ω Route C M2 + O2 mechanism + conditional O1-remove

**Branch:** `claude/aomega-routec-m2-stokes-mechanism-2026-08-14`
**Milestone bean:** `qou-fiag`
**Started:** 2026-08-14

Owner directive at the `qou-arc1` decision point: **"3 go; 2 try then 1 remove
from paper if not successful — retain only in audit doc as a last-resort
exploration."** i.e. do O3 unconditionally, attempt O2, and if O2 fails **excise**
`A_ω → S` from the paper (not merely scope it in place), keeping it only in an
audit doc.

## The three tasks

| Bean | Option | What | Disposition rule |
|---|---|---|---|
| `qou-ufms` | O3-M2 | Build the closed-sector `(Q,W)` quiver-with-potential and compute its BPS cohomology. Bankable Route C math — stands regardless of the O2 bridge, like the provenance / chirality results. | land as proved/verified |
| `qou-ws1w` | O2 | Derive a map from an **integer** Stokes constant to the small signed real residuals `S(muon)=+0.00968298`, `S(proton)=−0.03945936`. Must explain (i) why `x+1+x⁻¹` recurs for 5₂, (ii) why the co-occurring **4** and the tower `9,75,642,5580` do **not** surface as observables, (iii) the **sign asymmetry**. **Parameter-free (only already-derived inputs like q₀) or it is a fit, not a derivation.** | success → result; fail → trigger O1-remove |
| `qou-fddz` | O1-remove | If O2 fails: excise every content block asserting/depending on `A_ω → S`; move the numbers + the negative into an audit doc. | conditional on O2 |

## Discipline (STRICT — this is exactly the anti-laundering failure mode)

Per `qou-q3np`: the integrality obstruction (integer tower → non-integer
opposite-signed reals, no literature support) is real. O2 is only a *result* if
the map is **derived parameter-free**; a fit with free reals that hits
`0.00968298` is **not** a derivation and must be labelled one and kept out of
production. "Don't try to please" — if O2 dead-ends, report the negative and
fire O1-remove. The proved core (provenance, chirality obstruction, erratum, and
whatever O3-M2 lands) stands on its own.

## Log

- 2026-08-14 — branch + beans + this doc; corpus maps dispatched (Route C M2
  materials; `A_ω → S` content footprint for the conditional removal).
