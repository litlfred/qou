# The b₄ pole-regulator is not a new d.o.f. — it reduces to qou-9nq9, and `−ln det` is refuted as the carrier (2026-08-08)

Branch `claude/q-deformed-saddle-offsets-bdn992` (PR #4794). Bean qou-tfo1
(successor to the settled qou-fapk scalar-`m` negative). `free_parameters = 0`;
nothing wired. Anti-fit guard held throughout.

## Question

After qou-fapk established that the b₄ scalar `m` has no forward-forced value
(the bijection `b₄(m): (0,1/√5)→(0,∞)` makes `m`-selection a fit machine), the
named open object was the **pole regulator of the near-critical α-condensation
(species-symmetric, ss) mode** — what renders the ss-sector finite so a forward
(non-fitted) b₄ exists. Does such a regulator exist?

## Answer: NO forward-forced regulator (scope-(a)), and the `−ln det` carrier is
## refuted (scope-(b), Lean-proved). The object reduces to qou-9nq9.

### 1. The ss-sector and the pole divergence (concrete)

The ⁴He 4-body object is the connected `[1⁴]` cumulant `b₄ = −ln det(I + m·S)`,
`S` the K₄ `ppnn` writhe-sign matrix, spectrum `{±√5, ±1}`. The `±√5` modes are
**species-symmetric** (pp/nn centre-of-mass — the non-Pauli α-condensation
sector); the `±1` modes are Pauli intra-pair. Deforming the integer pn-degree
`2 → [2]_v` sends `√5 → L = √(1+[2]_v²)`, and

```
det(I + m·S) = (1 − mL)(1 + mL)(1 − m²)   (Lean he4DetViaEig / he4DetViaEig_eq)
```

The derived amplitude `g_reeb = 1/√(1+[2]_v²)` **is the pole by construction**
(`m·L = 1` ⇒ `he4DetViaEig_zero_at_pole`, sorry-free): the `(1−mL)` factor is an
**order-1 zero**, so `b₄ = −ln(1−mL) + finite → +∞` (a log divergence).

### 2. `−ln det` is the wrong carrier — Lean-proved repulsive (scope-(b))

The standard collective-coordinate prescription (drop the vanishing zero-mode
factor) gives the **reduced** determinant `2(1 − m²) > 1` for `m² < ½`, so
`b = −ln det < 0` — **anti-binding**:

> `QOU.MassTheory.he4DetReduced_gt_one_at_pole (L m : F) (h : m·L = 1)
> (hm : m² < ½) : …` — sorry-free (verified this session,
> `B4CumulantBarEven.lean:155`).

This is a **scope-(b) structural negative**: the ⁴He binding magnitude is **not**
a `−ln det` free energy. The exact zero mode signals a **collective-coordinate
(moduli-volume)** contribution — a geometric `Vol·ρ` object — not a loop
determinant.

### 3. Every finite forward candidate carries an unforced knob (scope-(a))

| candidate | finite b₄? | the free knob (why it is a fit) |
|---|---|---|
| classical integer-5 shadow (`L²=5` in det, `L_def` in magnitude) | 26.60 MeV | finiteness is *entirely* the classical-vs-deformed **mismatch**; both consistent-classical and consistent-deformed sit **on** the pole. Mismatch direction unforced. Misses B(⁴He) by −6 %. |
| I1-offset `δ = (q₀−1)²/q₀` | 16.97 MeV | same mismatch pathology; arbitrary pole-offset choice. |
| reduced determinant | `b < 0` | **Lean-proved repulsive** (§2) — refuted. |

No forward candidate forces a finite value; each finite one has a scale the
bijection turns into a fit machine. Post-hoc AME agreement of the classical
shadow (26.60 vs 28.30 MeV) is **not** evidence — not independently forced, not
wired.

### 4. Three pruning invariants (formalize-first, stated before the scan)

1. **Order-1 exact zero.** `g_reeb` is the pole *by its own derivation*
   (`g² = 1/(1+[2]_v²)`), so **no perturbation of q₀ regulates it** — the
   regulating scale must be a categorical datum **orthogonal** to the one that
   fixed `g_reeb`, else the construction is circular. Prunes every
   "small-offset-in-the-same-q₀-sector" candidate (incl. the classical shadow).
2. **ss-locus ⇒ collective coordinate, not loop.** A vanishing fluctuation
   eigenvalue on the species-symmetric centre-of-mass mode is a collective
   coordinate; its contribution is a **moduli volume**, not a `−ln det` factor
   (§2).
3. **Divergence order = 1 ⇒ a single collective coordinate** ⇒ one volume
   factor, not a tower.

## 5. Consequence: qou-tfo1 reduces to qou-9nq9 (and sharpens it)

Invariants (2)+(3) identify the regulator's *form* concretely: the ss zero-mode
must be integrated as the geometric **moduli-volume `Vol·ρ`** object — which is
exactly the qou-9nq9 geometric weight `W_λ = d_q²/D²` (Beasley–Witten). So the
pole analysis produces **no new forward finite value**; it *reduces* qou-tfo1 to
qou-9nq9 and **strengthens** it: the open problem is not a missing regulator
degree of freedom but the **magnitude-normalization of `W_λ`** — a derived
per-block weight strictly between production `y_λ` (undershoots, `E₀·Σ ≈ 0.243`
MeV, 117×) and geometric `d_q²/D²` (overshoots, `E₀·Σ ≈ 60.33` MeV, 2.13×).
`−ln det` is now proved the wrong functional; the moduli-volume `W_λ` is the
right one.

## Disposition

- **qou-tfo1** → scoped/reduced (WALL scope-(a)); folded into **qou-9nq9**. No
  forward-forced finite b₄; `−ln det` refuted as carrier (Lean); the ss-pole
  regulator = the qou-9nq9 geometric `Vol·ρ`/`W_λ` object, not a new d.o.f.
- **qou-9nq9** → live object confirmed + sharpened: derive the `W_λ`
  normalization between `y_λ` and `d_q²/D²` (a *derived* weight, not a tuned
  intermediate).
- **qou-prjo** → unaffected; the transverse NA-Stokes surface-curvature
  `½P∮∮[F_q,F_q]` is the one candidate with **no free knob** (underived, but not
  a fit — the corpus lacks the discretization) and is the natural source of the
  *orthogonal* categorical scale invariant (1) demands. The honest open
  construction.

Nothing fitted, wired, or closed. The settled negatives qou-fapk / qou-k4ud stay
closed.
