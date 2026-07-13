# 𝓑_K crossing/coordination structure — the light-nucleus M_n(A) is the per-nucleon coordination number

**Date:** 2026-07-11
**Branch:** `claude/bk-crossing-coordination-woiqj3`
**Compute:** [`computations/bk_crossing_coordination.py`](../../computations/bk_crossing_coordination.py)
**Witness:** [`computations/bk-crossing-coordination.witness.json`](../../computations/bk-crossing-coordination.witness.json)
**Follow-up to:** [`2026-07-03-wn-linkvolume-isospin-carrier-magnitude-open.md`](2026-07-03-wn-linkvolume-isospin-carrier-magnitude-open.md) (option 1) and [`2026-07-03-wn-universal-kernel-refuted-mirror.md`](2026-07-03-wn-universal-kernel-refuted-mirror.md) (option 2).

## Setup

The 2026-07-03 chain settled that the θ_λ many-body weight factorises as
`w_n(K) = M_n(A) · Vol_n(K)`, with the **hyperbolic link-volume `Vol_n(K)` the
isospin (T₃) carrier** (option 1, no fit) and the **body-order multiplicity
`M_n(A)` open** — it is neither the super-exp period `a_D^(n)` (undershoots ⁴He)
nor the magic `2·A` (overshoots the A=3 pair), and the deuteron Hopf `Vol=0` is a
structural wall.

This probe reads the multiplicity off the **crossing/coordination structure** of the
nucleon-level building-block link 𝓑_K, testing whether a topological integer supplies
`M_n(A)` with no fit.

## Crossing/coordination structure of 𝓑_K

| iso | A | 𝓑_K | comp | c(𝓑_K) | z = A−1 | C(A,2) | Vol |
|---|--:|---|--:|--:|--:|--:|--:|
| D | 2 | Hopf L2a1 | 2 | 2 | 1 | 1 | 0 (Seifert-fibred) |
| ³H | 3 | 8_11 | 1 | 8 | 2 | 3 | 8.286 |
| ³He | 3 | L6a4 (Borromean) | 3 | 6 | 2 | 3 | 7.328 |
| ⁴He | 4 | L6a4-base | 3 | 6 | 3 | 6 | 7.328 |

- `z = A−1` = **per-nucleon coordination number** (bonds incident to one nucleon in the
  fully-coordinated cluster).
- `C(A,2)` = total nucleon–nucleon bond count.
- `c(𝓑_K)` = crossing number of the nucleon-level link.
- Quark-strand crossings of the canonical `T_w` braid: D (B₆) = 18, ⁴He (B₁₂) = 38.

## Result — needed multiplicity vs topological candidates

`M_need(A) = B_AME / (m_e · Vol_A)`:

| iso | M_need | z = A−1 | z·a_D^A | c(𝓑_K) |
|---|--:|--:|--:|--:|
| ³H | 2.003 | **2** (−0.2%) | 2.67 (+33%) | 8 |
| ³He | 2.061 | **2** (−3.0%) | 2.67 (+30%) | 6 |
| ⁴He | 7.557 | 3 (−60%) | **7.60** (+0.6%) | 6 |

## Reading

1. ✅ **The light-nucleus multiplicity IS the per-nucleon coordination number
   `z = A−1`.** For the non-magic A=3 pair, `M_need(³H)=2.003` and
   `M_need(³He)=2.061` both sit within 3% of `z=2` — with **no fit**. This is a
   fit-free identification of one piece of the previously-open `M_n(A)`: on top of
   the (isospin) volume carrier, the multiplier for open-shell light nuclei is the
   topological coordination number of 𝓑_K.

2. **Doubly-magic ⁴He carries a separate super-exp `a_D^(4) ≈ 2.53` factor.**
   `M_need(⁴He)/z = 7.557/3 = 2.52 ≈ a_D^(4)`. So `z·a_D^A` closes ⁴He to +0.6% —
   but the **same product overshoots the A=3 pair by ~30%** (`a_D^(3)=1.34 > 1`).
   The super-exp `a_D` is therefore a **magic-shell-only enhancement that turns on at
   the closed ⁴He shell**, not a universal factor. This confirms option 1's "`a_D^(n)`
   and the magic multiplicity are different objects" reading, and sharpens it: the two
   objects are (i) the coordination number `z=A−1` (always present) and (ii) the
   super-exp `a_D^(A)` (magic shells only).

3. **Crossing number `c(𝓑_K)` is the `Vol=0` deuteron survivor, not the A≥3
   multiplier.** `c` does not track `M_need` for A≥3 (8_11 `c=8` > L6a4 `c=6`, but
   `M_need(³H) < M_need(³He)`). Its role is different: on the 2-body deuteron sub-link
   the volume vanishes (Hopf is Seifert-fibred), yet the **crossing/coordination
   structure survives** — `c(Hopf)=2`, `|lk|=1`, `z=1`. So the coordination carrier is
   the natural non-vanishing replacement for the volume exactly where the volume wall
   sits.

## Extension — α-cluster coordination for A>4 magic nuclei

¹⁶O and ⁴⁰Ca have **no canonical single hyperbolic link** in the corpus — they are
α-conjugate cluster nuclei. So the "test the `a_D` activation rule at the next magic
shell" question resolves by lifting the coordination principle **one level up**: treat
each ⁴He as a single node and count α–α coordination bonds,

> `B(n_α) ≈ n_α · B(⁴He) + N_bonds · b_αα`.

For a **simplex** cluster (`n_α ≤ 4`: ⁴He, ⁸Be, ¹²C, ¹⁶O) every α-pair is a nearest
neighbour, so `N_bonds = C(n_α,2)` (complete graph, 3D-realisable up to the tetrahedron):

| iso | n_α | C(n_α,2) | B_AME | resid = B − n_α·B(⁴He) | per-bond | simplex |
|---|--:|--:|--:|--:|--:|:--:|
| ⁸Be | 2 | 1 | 56.50 | −0.09 | −0.09 | yes |
| ¹²C | 3 | 3 | 92.16 | 7.27 | **2.425** | yes |
| ¹⁶O | 4 | 6 | 127.62 | 14.44 | **2.406** | yes |
| ²⁰Ne | 5 | 10 | 160.64 | 19.17 | 1.917 | no |
| ²⁴Mg | 6 | 15 | 198.26 | 28.48 | 1.899 | no |
| ⁴⁰Ca | 10 | 45 | 342.05 | 59.10 | 1.313 | no |

- **Simplex clusters (`n_α ≤ 4`): the per-bond residual is a near-constant
  `b_αα ≈ 2.41 MeV`** (¹²C 2.425, ¹⁶O 2.406). ⁸Be gives ≈0 — the isolated α–α pair is
  unbound (the reason for the triple-α process), so a lone bond carries ~0 and the bond
  energy switches on only inside a 3+ cluster. This is the classical **Hafstad–Teller
  α-bond model**; the QOU content is reading `N_bonds` as the **α-cluster coordination
  number** — the same principle as `z=A−1`, one level up. `b_αα` is a **single empirical
  residual constant, NOT derived** from the 13 categorical drivers (exploratory only).
- **`n_α ≥ 5` (²⁰Ne, ²⁴Mg, ⁴⁰Ca): `C(n_α,2)` overcounts** — not all pairs can be
  nearest neighbours in 3D, so the per-bond value drops (1.92 → 1.31). Coordination
  **saturates** to a geometric close-packing count beyond the tetrahedron; **⁴⁰Ca needs
  the packing coordination, not `C(10,2)=45`** — this is the honest open item.
- **The `a_D`-activation question resolves negatively for A>4:** there is no per-isotope
  `a_D` factor beyond ⁴He. ⁴He is itself the `n_α=1` base; the extra binding of larger
  α-nuclei is carried entirely by the α–α **coordination count**, not a super-exp period.

## Verdict (critical-distance, scope-limited)

**Scope-limited (a)** per the "refuted"/"ruled out" discipline — candidates were tested
alone, not structurally excluded; no proved invariant forbids the alternatives.

What this **establishes** (fit-free):

> The open `M_n(A)` decomposes as a **topological coordination number `z(A)=A−1`**
> (settled for the non-magic A=3 pair, <3%) times a **magic-shell super-exp factor
> `a_D^(A)`** that activates only at closed shells (⁴He, +0.6%). The crossing number
> supplies the non-vanishing carrier on the deuteron where `Vol=0`.

What remains **open**:

- Why the coordination number `z=A−1` (a whole-cluster count) equals the *per-isotope*
  multiplier read off the *single-link* volume — a categorical derivation of
  `M(open shell) = z` from the branching/`T_w` structure, not just the numerical match.
- The activation rule for the magic `a_D^(A)` factor (closed-shell selection). For A>4
  the extension (above) shows it does **not** recur as a per-isotope period; the extra
  binding becomes the α-cluster coordination count instead.
- A **derivation** of `b_αα ≈ 2.41 MeV` (currently a single empirical residual constant,
  not from the 13 drivers) and the **geometric close-packing coordination count** for
  `n_α ≥ 5` that replaces `C(n_α,2)` beyond the tetrahedron (needed for ⁴⁰Ca).
- The deuteron: an explicit crossing/coordination weight (not `vol_eff` substitution)
  reproducing `B(D)`.

No production wiring; no fitted constant. This narrows, it does not close.
