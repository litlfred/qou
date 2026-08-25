# The volume–binding four-point test cannot be run (2026-08-08)

**Tier:** compute probe + coordination · **Wired:** nothing · **No fit, no AME inversion.**
Producer: [`volume_binding_four_point.py`](../../computations/volume_binding_four_point.py) ·
witness: `computations/volume-binding-four-point.witness.json`.

Executes the next task set by
[`2026-08-07-l2-volume-binding-cluster.md` §5](../coordination/2026-08-07-l2-volume-binding-cluster.md):

> *"Recompute the volume-binding relation across **all four** L2 binding targets
> (`D`, `T`, `³He`, `⁴He`) under Reading 2, ratio-only, zero free parameters — the
> two-point `≈4` constant is not evidence until it survives four points. Blocked
> on the author's Reading-1-vs-Reading-2 ruling (§2.2)."*

**It is not blocked on the ruling.** It is blocked on data, and it is unrunnable
under *both* readings. Ruling either way produces no additional point.

---

## 1. The point count

| target | A | B_AME (MeV) | Reading-2 link | Vol | usable |
|---|---:|---:|---|---:|---|
| D | 2 | 2.2245662 | Hopf `L2a1` | **0** | **no** |
| T | 3 | 8.4817962 | `8₁₁` | 8.286316818 | yes |
| ³He | 3 | 7.71804132 | `L6a4` = Borromean | 7.327724753 | yes |
| ⁴He | 4 | 28.2956624 | **(none)** | — | **no** |

**2 usable points of the 4 required.**

- **Reading 1** (literal mass-braid `H₉` closures) supplies **zero**. Already on
  record in `he4-link-volume-braid-closure.witness.json`: the ³H closure is
  4-component against `8₁₁`'s 1, the ³He closure is 4-component against
  Borromean's 3, and all closures are non-geometric (Vol → 0).
- **Reading 2** (SDP binding-link registry) supplies **two**. `binding-k-solver.witness.json`
  carries `n_atoms = 3` — deuteron, tritium, he3 — and the deuteron's link is the
  Hopf link, which is Seifert-fibred with `Vol = 0` exactly.

The two survivors, `T` and `³He`, are precisely the mirror pair the original
two-point observation already used. So the falsification criterion the ledger set
for itself cannot be met with anything now in the corpus.

## 2. Why ⁴He is missing, and why it must not be filled in

The SDP solver's scope is `A ≤ 3`. Extending to `A = 4` needs `B₅` Hoefsmit plus
the Clarabel backend — conj #604 / GAP-A-1, explicitly future work in the
registry's own follow-up list (*"Generalise to ⁴He (B_? at H₁₂), ⁶Li (H₁₈)…"*).

The corpus does contain a ⁴He volume, and it is **not** admissible here:

- `Vol₄ ≈ 8.046` is a **back-out** from the bond-count model
  (`theta_mn_bondcount_linearchain.py`), i.e. obtained by assuming the very law
  under test. Using it as a fourth point would be circular.
- The provisional doubly-magic alternative `2·Vol(Borromean) = 14.655`
  **disagrees with it by ~1.8×**. An unresolved factor-of-two-ish tension is not
  a data point either.

The producer therefore excludes both by construction and says so in a witness
caveat, rather than quietly picking whichever lands closer.

## 3. What the two real points do say

Reproduced at 70 dps (the ledger's version was scratch float64 and flagged
NO-FLOAT64):

```
B(T)/B(3He)      = 1.09895708617
Vol(T)/Vol(3He)  = 1.13081714948
ratio of ratios  = 1.02899118055    ->  2.899% miss
```

which confirms the ledger's 2.90% to the digits it quoted.

A sharper reading than "2.9% spread" is available by inverting the corpus's
**existing** bond-count law `B = c·m_e·Vol(K)` at each point — note `c = 2` is the
corpus's own constant (`a3_mirror_residual_reconciliation.py` L59–64:
`B_T_bc = M_E * 2 * VOL_8_11`), not something fitted here:

```
T     c = 2.00311687989      (0.16% from exactly 2)
3He   c = 2.06118960302      (3.06% from exactly 2)
```

**The deviation is not shared between the two isobars — it is essentially all in
³He.** Tritium sits on `B = 2·m_e·Vol(8₁₁)` to 0.16%. That is a more specific
target than a symmetric 2.9% spread, and it points at the ³He assignment
(`L6a4` = Borromean, the same link as the per-nucleon braid `𝓑₃`) rather than at
the law's overall shape. Whether that is signal or a two-point coincidence is
exactly what the missing points would decide — which is the problem.

## 4. Consequence for the pending ruling

The §2.2 escalation still deserves an answer, but its stakes should be restated
honestly: **the ruling does not unblock the four-point test.** What Reading 2
buys is two points and a research programme (extend the SDP to `A = 4`); what
Reading 1 buys is a clean structural negative (the mass-braid closure is
Gromov-norm 0, so binding is not a hyperbolic volume of the mass braid).

Neither delivers the falsification the ledger wanted. Recommend recording the
four-point test as **blocked on the A=4 SDP solve** — a concrete, nameable
prerequisite — rather than as blocked on a ruling it does not actually depend on.

## 5. Scope

Everything above is **scope-(a)**. Nothing here refutes the volume law, and
nothing here supports it. The finding is about the *evidence base*: it is two
points, it was two points before, and it will stay two points until `A = 4` is
solved. Per AGENTS.md §"Before declaring refuted", no ingredient is excluded by
this document.
