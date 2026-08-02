# Hypercharge strand-twist: the candidate `Y` is a function of the total twist alone

**Date:** 2026-08-02
**Branch:** `claude/hypercharge-twist-derivation-2026-08-02` (PR #4561)
**Beans:** `qou-q377` (parent gap), `htw2` (sharpened residual)
**Scope:** Formalize-first attack on SM gap G2 — derive the per-fermion
strand-twist multisets from framework braid words so hypercharge `Y` is
*derived*, not enumerated (`conj:sm-hypercharge-invariant`,
`def:strand-twist-datum`). Follow-up to the 2026-06-02 U(1)→quantum-number
audit ([`2026-06-02-u1-hypercharge-assignment.md`](2026-06-02-u1-hypercharge-assignment.md))
and the 2026-08-01 uploads round-2 reads
([`2026-08-01-sm-uploads-round2-reads.md`](2026-08-01-sm-uploads-round2-reads.md)).
**Lean:** four sorry-free declarations added to
[`strand-twist-datum.lean`](../../content/quantum-observable-universe/appendix-standard-model/strand-twist-datum.lean)
(`QOU.StandardModel.TwistDatum`); `lean`-direct exit 0.
**No fit; nothing wired to production.**

---

## VERDICT (one line)

**The battery over-parametrises the problem.** The candidate hypercharge
`Y = 2(totalTwist/3 − I₃)` is (Lean-proved) a function of the **total
twist alone**, and reproducing the SM spectrum is (Lean-proved) equivalent
to pinning `totalTwist = 3Q` — so the total-twist vector
`(u,d,ν,e) = (2,−1,0,−3) = 3Q` is **unique**, and the enumeration's
"4 of 10 000 survivors" is exactly `1·2·2·1`, the count of `{−1,0,1}`
multisets realising each pinned total. The residual is `Y`-invisible
strand-refinement at fixed total, **not** hypercharge non-uniqueness. The
genuine open object is unchanged and now sharper: **per-chiral-fermion
framed braid words** from which `totalTwist(f)` is *computed* rather than
inverted from the SM target.

---

## 1. The reduction (proved)

Let `t : Fin n → ℤ` be a strand-twist datum, `T(t) = Σᵢ tᵢ` its total
twist (`def:strand-twist-datum`). The `def:strand-twist-datum` candidate
pairs it with the writhe-derived isospin `I₃`:

```
Y_cand(I₃, t) = 2 · (T(t)/3 − I₃),   Q_twist = T(t)/3   (helon 1/3).
```

Three Lean facts (`strand-twist-datum.lean`, sorry-free):

| Lemma | Statement | Content |
|---|---|---|
| `Ycand_factors_totalTwist` | `T t = T t' → Y_cand I₃ t = Y_cand I₃ t'` | `Y` sees only the total, never the multiset. |
| `totalTwist_pinned_of_Ycand` | `Y_cand I₃ t = Y ↔ (T t : ℚ) = 3(I₃ + Y/2)` | The SM target pins the **total** to `3Q` (Gell-Mann–Nishijima), and pins nothing else. |
| `Ycand_bar` | `Y_cand(−I₃, bar t) = −Y_cand(I₃, t)` | Bar-odd antiparticle consistency (from `totalTwist_bar`). |

Concrete witness (also in the file): the two `d`-survivors `{−1,−1,1}` and
`{−1,0,0}` share `T = −1`, hence give identical `Y` at `I₃ = −1/2`.

Base ring `ℚ` — SM quantum numbers are rational; no ordering / `Real.*`,
so this stays below the substrate→archimedean wall (§7c).

## 2. The `1·2·2·1` decomposition of the "4 survivors"

The size-3 `{−1,0,1}`-multisets, counted by total:

| total `T` | multisets (sorted) | count |
|---:|---|---:|
| −3 | `{−1,−1,−1}` | 1 |
| −2 | `{−1,−1,0}` | 1 |
| −1 | `{−1,−1,1}`, `{−1,0,0}` | **2** |
| 0 | `{−1,0,1}`, `{0,0,0}` | **2** |
| +1 | `{−1,1,1}`, `{0,0,1}` | 2 |
| +2 | `{0,1,1}` | 1 |
| +3 | `{1,1,1}` | 1 |

The spectrum pins `(u,d,ν,e)` totals to `(2,−1,0,−3) = 3·(2/3,−1/3,0,−1) = 3Q`.
Survivor count = product of the per-total multiplicities =
`1·2·2·1 = 4` — reproducing the battery exactly
([`strand-twist-y-battery.witness.json`](../../computations/strand-twist-y-battery.witness.json):
`u=[{0,1,1}]`, `e=[{−1,−1,−1}]` unique; `d`, `ν` each two multisets). The
"u, e multisets unique" result is the incidental fact that `+2` and `−3`
are the totals with a unique `{−1,0,1}` realisation — not deeper physics.

## 3. What is derived vs open

- **Derived (Lean sorry-free):** the total-twist vector `(2,−1,0,−3)` is
  the *unique* solution; `Y` is blind to the multiset; the survivor count
  is a combinatorial multiplicity, not residual hypercharge freedom.
- **Open (bean `htw2`):** the framework carries **no per-chiral-fermion
  framed braid words**, so `totalTwist(f)` is currently *pinned by the SM
  target* (an inversion / anchor), not *computed*. `totalTwist = 3Q` is
  the falsifiable consistency `Q_twist = Q`, not a derivation; deriving
  the individual-fermion `Q(f)` (equivalently the framed braid word) is
  the actual object. The `1/3` normalisation is the Bilson-Thompson helon
  precedent, not derived.

## 4. Self-audit (latent-fit flags)

- **No fit.** `totalTwist = 3Q` is forced algebraically from the candidate
  form + Gell-Mann–Nishijima; no coupling, scale, or `h^k` is tuned.
- **No production wiring; no L1/L2 movement; no `sorry` discharged.**
- **No over-claim.** This does not derive `Y`; it proves the enumeration's
  residual is `Y`-invisible and re-scopes the open object to braid words
  (scope-(a): a reduction + a sharpened gap, not a closure).
- **`conj:sm-hypercharge-invariant` stays open.**

## Cross-references

- The candidate + the falsifiable `Q_twist = Q` clause:
  [`strand-twist-datum.md`](../../content/quantum-observable-universe/appendix-standard-model/strand-twist-datum.md),
  [`sm-hypercharge-invariant.md`](../../content/quantum-observable-universe/appendix-standard-model/sm-hypercharge-invariant.md).
- The enumeration probe (unchanged):
  [`strand_twist_y_battery.py`](../../computations/strand_twist_y_battery.py).
- Categorical home for the twist (abelian-H, t=0 crossed module; level-k
  string extension): [`2026-08-01-sm-uploads-round2-reads.md`](2026-08-01-sm-uploads-round2-reads.md).
- `writhe → I₃` derived, `Y` undefined (the second-invariant gap):
  [`2026-06-02-u1-hypercharge-assignment.md`](2026-06-02-u1-hypercharge-assignment.md).
