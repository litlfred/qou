# Bring foundations: the trace sites, and an attack on the genus

PR #8365, issue #8364, bean `qou-qhcr` (open; never close while the derivation is open).

## 1. What the trace sites were, and how each was resolved

The 2026-09-15 rulings make `tr(id_A) = dim_q(A)` a q-dependent quantum dimension
and keep `chi_eu(M_0) = -6` as a separate, topological object
(`rem:three-euler-characteristics`). Five blocks used a trace identity.

| block | what it wrote | resolution | status |
|---|---|---|---|
| `brings-is-qou-verification` | `chi(A) = tr(id_A) = 2-2g = -6` | middle equality removed; nothing used it | resolved |
| `ns-kummer-specialisation` | `tr(kappa_0) = chi(A)` | the integer is `e(xi)[S]`, equal to `chi_eu(S)` by Poincare–Hopf **iff `xi` is the unit tangent bundle**; hypothesis now stated | resolved, conditional on (H_T) |
| `q-bsd-classical-limit` | `tr(kappa_0) = chi(A) = -6` | `kappa_0[M_0] = chi_eu(M_0)`, citing the above | resolved, conditional on (H_T) |
| `archimedean-yekutieli` | `chi(A) = -6` with lepton-generation reading | rename done; the `S_3 < S_5` three-pairs reading stays open | partly |
| `terminal-morphism-brings` | Step 1: `q + q^{-1} = -6` | not resolved: it forces `q = -3 ± 2√2`, and the Descartes condition no longer fixes `q` | **owner choice** |

### The hypothesis (H_T), and where the paper already has it

(H_T): *the circle bundle `xi` whose Euler class gives the Kummer obstructions is the
unit tangent bundle `UT(M_0)` of the base curve.*

- `thm:qu-to-qou` item 2 states it as a conditional ("when `xi` is the unit tangent bundle").
- `def:reeb-bundle` does **not** supply it: that bundle is the Hopf fibration over the
  fibre `S_p ≅ S^2`, Euler number `-1`.
- `lem:bring-cone-reeb-quaternionic-twist` **does** supply it for Bring: the link of the
  canonical cone over `Sigma_4` is `UT(Sigma_4)` with Euler number `-deg K = -6`, and its
  Reeb flow is the geodesic flow.

So for the Descartes universe the Kummer integer is derived, with no trace of `A`
anywhere. For a general QOU, (H_T) is an open hypothesis. **Gap G1:** derive that the
QOU contact form `Θ` restricts on the base to the canonical (Liouville) contact form of
the unit cotangent bundle. If it does, then (H_T) follows, the Reeb flow is the geodesic
flow, and the result holds at every genus, not only for Bring.

### `terminal-morphism-brings` — the options

Step 1 used `[2]_q = -6` to force equal substrate parameters on source and target.
Under the ruling, `[2]_q` is `dim_q(V) > 0` at real `q > 1`, so this step is false.
Options for the owner:

1. Make `q` part of the data of the category `C_{-6}` (objects at a fixed `q`). Step 1
   then holds by definition, and terminality becomes a statement per value of `q`.
2. Let a morphism carry a change of base ring `Z[q,q^{-1}] -> k`. Uniqueness would then
   have to be re-proved, because Step 4 relies on identical `q`.
3. Demote the block to a conjecture until (1) or (2) is chosen.

## 2. The conjecture: derive `g = 4` (`chi_eu(M_0) = -6`) from the axioms

### Where it stands (bean `qou-qhcr`, measured, sorry-free Lean on main)

- Riemann–Roch (Step 3) plus `g ≥ 1` (Step 4) plus observability (`chi ≠ 0`) give
  `g ≥ 2`, and nothing more.
- Transitivity of `Aut` on the Weierstrass points **alone narrows nothing**. This is a
  scope-(b) result: Accola–Maclachlan curves are transitive at every genus
  (Reyes-Carocca–Speziali, held in `library/arxiv-2211.08164v2`).
- (H1) transitivity, plus (H2) all Weierstrass points simple, plus the Hurwitz bound
  give `g ≤ 8`. This is derived and needs no classification
  (`BringsSurface/WeierstrassTransitivityNotForced.lean`).

### New this session: adding an order-5 automorphism (H3) gives `g ≤ 6` by arithmetic alone

`|W| = g^3 - g` divides `|Aut|` (H1+H2), `5` divides `|Aut|` (H3), and
`|Aut| ≤ 84(g-1)` (Hurwitz). So `lcm(g^3-g, 5) ≤ 84(g-1)`:

| g | g³−g | lcm with 5 | Hurwitz 84(g−1) | admissible orders | known max \|Aut\| at g | survives |
|---|---|---|---|---|---|---|
| 2 | 6 | 30 | 84 | 30, 60 | 48 | 30 only |
| 3 | 24 | 120 | 168 | 120 | 168 | 120 only |
| 4 | 60 | 60 | 252 | 60…240 | 120 | 60, 120 |
| 5 | 120 | 120 | 336 | 120, 240 | 192 | 120 only |
| 6 | 210 | 210 | 420 | 210, 420 | 150 | **none** |
| 7, 8 | — | — | — | none | — | **none** |

The Hurwitz arithmetic is exact and is computed in the table. The column of maximal
automorphism-group orders per genus is classical (Conder's tables), but **it is not yet
held in `library/`**, so the column is a citation still to be added and not yet a
derivation. With it, `g ≤ 5`. Separating `g = 4` from the survivors needs one fact per
genus:

- `g = 2`: no genus-2 automorphism group has order 30. This is classical: the genus-2
  groups have orders in {2,4,6,8,10,12,16,24,48}.
- `g = 3`: no genus-3 group has order 120.
- `g = 5`: does a genus-5 surface with `|Aut| = 120` act **freely and transitively** on
  120 simple Weierstrass points? Freely, because the stabiliser has order `120/120 = 1`.
  **This is the sharpest open arithmetic question, and Conder's genus-5 list settles it.**

### Attack strategy, ranked by cost

1. **Lean, cheap.** State and prove `H1 ∧ H2 ∧ H3 ∧ Hurwitz ⟹ g ≤ 6` over ℕ, as a
   companion to `WeierstrassTransitivityNotForced.lean`. It has no `sorry` and no
   classification input.
2. **Library, cheap.** Ingest Conder's genus 2–6 automorphism-group lists. Then turn
   `g ∈ {2,3,5}` into theorems taking those lists as hypotheses, with a `-- Ref:` to
   the source. The output would be `H1 ∧ H2 ∧ H3 ⟹ g = 4`, conditional on the lists,
   and Bring's curve then follows from the genus-4 classification.
3. **Paper link.** Add `conj:descartes-genus-from-axioms`, stating: *the five QOU axioms
   imply (H1), (H2) and (H3) for the base curve*. Re-state `ex:chi-minus-six-derivation`
   Step 5 as conditional on it, i.e. §3b-cond with a content-bearing class whose three
   fields are H1, H2 and H3. This turns the one unsourced integer, 6, into three named
   group-theoretic inputs.
4. **Research, hard: source (H3).** Every order-5 structure in the corpus is downstream
   of Bring (`ζ₅` pentad, the Bring–Jerrard quintic, the (2,4,5) triangle group, `2I`).
   Any candidate must come from the axioms and must not be selected because it gives 5
   (§NO FITTING).
5. **Research, hard: source (H2).** Simplicity is a *genericity* condition. In the
   held classification data it is anti-correlated with symmetry: Fermat's quartic fails
   it. So an observability-style axiom is the wrong shape for it. Look for a
   non-degeneracy statement instead. One candidate: the canonical series has an
   everywhere non-vanishing Wronskian of order `g`.
6. **G1** (§1): derive (H_T) from `Θ`. This is independent of 1–5, and it makes the
   Kummer results hold at every genus.

### The honest default

If none of 3–5 is closed, the paper should say plainly that `g = 4` is an **input**,
chosen as the maximally symmetric case satisfying (H1)–(H3). That choice is a selection,
and the §NO FITTING rule asks for it to be stated as one.
