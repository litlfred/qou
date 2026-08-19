---
# qou-w4gn
title: 'GAP: eps_m per-ELEMENT representative at m>=3 — residue-level lattice model shown insufficient (Addendum 25)'
status: todo
type: task
created_at: 2026-08-11T11:21:33Z
updated_at: 2026-08-11T11:21:33Z
---


## Single-relation route: RULED OUT (2026-08-11, idle-window probe)

The cheapest route to a per-element representative is one five-term
relation seeded at the offending symbol. xi's symbols are the specific
elements z_1 (mult 2) and z_2 (mult 1), so per-element divisibility
m | n_j e(w_j) fails only where noted:

| m | z_2 needs fixing (m does not divide e(z_2)) | z_1 needs fixing (m does not divide 2 e(z_1)) |
|---|---|---|
| 2 | no | no |
| 3 | yes | no |
| 4, 8, 12, 24 | yes | yes |
| 6 | yes | no |

Fixing z_2 by subtracting a five-term relation seeded at (z_2, y)
cancels z_2 but introduces its other four arguments at multiplicity -1,
each then needing m | e(w). Swept over every admissible y in F_25
(alpha basis, alphabar^2 = 4 alphabar + 3):

    ZERO candidates at every m | 24.

So no single relation clears the obstruction. This does NOT close the
bean: multi-relation combinations (and relations seeded at other
positions, or acting on z_1 as well) are untested, and the search space
of coefficient vectors over the 506 relations is large. The negative is
scope-(a): one route, exhaustively excluded.

Convention note: this run measures e(z_1) = 15, e(z_2) = 22 against an
alpha-basis generator, where the merged probes report 9 and 2 against a
different generator. The dlogs differ by a unit rescaling; every
divisibility verdict agrees, as it must.

### 2026-08-19 (PR #5296, Addendum 32) — the target group, found

CGZ Remark 1.9 (arXiv:1712.04887v3 p. 8): the invariant is
`R_ζ ∈ (F_n^×/(F_n^×)^n)^{χ⁻¹}`, with `P_ζ ∈ H^×/H^{×n}` only its image
and the **lift** flagged unchecked in general. An eigenspace is proper
only when `μ_n ⊄ F`; every field in this programme was `Q₅(μ_{624m}) ⊇
μ_m`, so Lemma 2.4(e) was vacuous throughout.

Correct base is place-dependent: `K = Q(α)`, `α³−α²+1=0`, has two places
over 5. At the degree-1 one `K_v = Q₅ ⊉ μ₃`, `F₃ = Q₂₅`, and the
χ⁻¹-eigenspace of `B^×/(B^×)³` is the Teichmüller line — order 3 of 9,
with `5` outside it. Non-vacuous.

**Reverses half of Addendum 31.** `B = Q₂₅` *is* `F_n` there, and
`χ_B = teich(·)⁸` *is* the eigenspace projection. The root-dependence of
Addenda 27–29 belongs to the lift, not the field.

**Route closed:** Lemma 2.3 is an isomorphism `F^×/F^{×n} ≅ H¹(Φ,μ)`, so
the Kummer-cocycle reformulation computes the same object as Addendum 31.
Dead end; no probe spent on it.

**Still open:** the lift `P_ζ → R_ζ` at the degree-1 place (CGZ §3, via
Chern classes). No ε_m value claimed at m ≥ 3.

### 2026-08-19 (PR #5296, Addendum 33) — a value, at one place

CGZ Prop 2.5 (p. 11) constructs the lift Remark 1.9 flags. At the
degree-1 place of `K = Q(α)` every hypothesis is free: `w_{Q₅} = 4` is
coprime to 3 (Theorem 1.2's hypothesis, stated in §2.3 — Addendum 32's
diagnosis in CGZ's own words); `⋀²(F^×/(F^×)³) = 0` so the obstruction
has nowhere to live; `S^{χ⁻¹} = 0` so the lift is unique.

`H` is not needed — `z₁, z₂, 1−z₁, 1−z₂` are all units of `Z₅`, hence
cubes, so the eqn-(21) shift ratio is a cube **in B**. That is the whole
explanation of the Addenda 27–29 root-dependence: there `1−X` was not a
cube in the field used.

**ε₃(2[z₁] + [z₂]) = ζ₃²** — invariant over all 9 root choices,
satisfies Lemma 2.4(e), identical under either primitive cube root.

**Still open:** CGZ's lift *in general* (the cases where the obstruction
does not vanish for free), and any place where the arithmetic is not
trivial. The m ≥ 3 fields of Addenda 27–29 are not revived — they are
the wrong fields, and `ε_m` was never computable there.

### 2026-08-19 (PR #5296, Addenda 34–35) — validated, and one label of mine corrected

**Validated against the paper.** Every earlier check was internal; a
consistently-wrong `P_ζ` would have passed them all. Four CGZ predictions
now hold: Lemma 2.4(b) (`D_ζ(1) ≡ ζ`, and `= 3(1−ζ²)` exactly), Lemma
2.4(c) on 240 arguments, the reflection relation (a **nonzero** constant),
and the **five-term relation on 400 instances** — with a flipped sign
breaking 99/150 and `ζ→ζ²` breaking 96/150.

**Corrected value.** The readout `teich(·)⁸` is a power of the μ₂₄
generator, not of `ζ₃` (`cls(ζ₃) = 2`). So `ε₃(a[z₁]+b[z₂]) = ζ₃^{−a}`
and `ε₃(2[z₁]+[z₂]) = ζ₃`, **not** `ζ₃²`. The same conflation was one step
from a false report of a discrepancy with Lemma 2.4(b). Structure
(linearity, `c₂ = 0`, dependence on `a` alone) unaffected.

**Also:** `d(ξ) = 0` exactly in `K` (the α-line is the exceptional unit
relation `1−α = α⁻²`), but it vanishes for *every* coefficient pair — so
the Bloch condition does **not** pin `(2,1)`.

**Still open:** CGZ's lift where the obstruction does *not* vanish for
free; any place where the arithmetic is not trivial; and `m ≥ 4`.

### 2026-08-19 (PR #5296, Addendum 37) — the census, and m=2 is empty

Live set over `F = Q₅`: **`m ∈ {3, 6, 8, 12, 24}`**. `m = 3` alone gets a
*unique* lift (`gcd(3, w_{Q₅}) = gcd(3,4) = 1`); 6, 8, 12, 24 have a proper
eigenspace but only `R^{w_F}` defined — still nontrivial there, so
information survives. `m | 4` is vacuous. Eigenspace sizes measured by
brute force, then checked against `m·gcd(m,4)`.

**Corrected my own queued guess:** `μ_m ⊂ Q₅` iff `m | 4`, not "m coprime
to 4" — so 8, 12, 24 qualify.

**Corrected a claim I repeated all arc:** `m = 2` is vacuous in *every*
field of char ≠ 2. `−1` forces `F₂ = F`, `Gal` trivial, `w_F` even, so
`gcd(2, w_F) > 1`, Theorem 1.2 never applies at `n = 2`, and only
`R^{w_F} = 1` is defined. **There was never a non-vacuous CGZ target at
m = 2.** PR #4968's `+1` is forced by the group, not measured — not wrong,
but empty as a CGZ value. Stop citing it as the programme's solid result.

**Next:** `m = 6` at `v₁` — smallest live case beyond 3, and the first
where only `R^{w_F}` exists, so it tests whether the `R^{w_F}` route
carries a computable value in practice and not just in principle.

### 2026-08-19 (PR #5296, Addenda 38–39) — the v₁ m-sweep CLOSES on ε₃

`m = 6` computes (all four CGZ gates re-run, five-term on 300 instances,
both controls firing) but its `R^{w_F}` re-expresses the `m = 3` invariant:
`w_F = 4` kills the 2-part of `Z/6` and the surviving 3-part *is* the
`m = 3` group. Consistency check, not a datum.

And only `m ∈ {3, 6}` are computable in `B` at all. An `m`-th root of a
`Z₅` unit stays in `B` iff `gcd(m,24)` divides its Teichmüller dlog; the
four arguments have dlogs 6, 12, 12, 6, so 8, 12, 24 all fail — **correcting
my own prediction, made minutes earlier, that 12 and 24 would merely be
redundant.** Obstruction is per-symbol (at m=12 the dlog-12 arguments do
have roots in B; z₁ and 1−z₂ block).

**Terminal: the degree-1 place yields exactly one computable non-redundant
CGZ invariant, `ε₃`.** 8/12/24 need the Kummer extension `B(z^{1/m})` —
the unchecked H-side descent. Not a claim that they are trivial.

**Next:** the second-Bloch-element test is now the only cheap live option —
`c₂ = 0` at `m = 3` is a single data point, and whether `ε` separates
elements or is generically carried by one symbol is unanswered. Needs a
second exceptional-unit field with a degree-1 place at 5.

### 2026-08-19 (PR #5296, Addendum 40) — `c₂ = 0` deflated; and a preflight I had been skipping

**Addendum 34's reading withdrawn.** "The invariant is carried entirely by
`[z₁]`" rested on `c₂ = 0` — one observation in a group of order 3. The
class of `P_ζ` splits **exactly 80/80/80** over 240 arguments, so that is a
1-in-3 event; and the reflection relation pins `c(X) + c(1−X)` across the
anharmonic orbit, so `c₁`/`c₂` were never two free observations. The value
`ε₃ = ζ₃^{−a}` stands; the interpretation does not.

**A second field is cheap after all** — 46 candidates in `|a|,|b| ≤ 12`
(`c = ±1`, `f(1) = ±1`, irreducible, simple root mod 5 lifting to a
degree-1 place with all four arguments `Z₅`-units), discriminants 169, 257,
697, 2777, … and `κ` varies across them. Available if the comparison is
ever wanted, but the motivating question has lost its force.

**Process defect, found via a sibling.** `55ac29d946` fixed a raw-float64
red in *my* m3-closure witness. That prompted me to run
`scripts/precision-gates.sh` — required before any witness-touching commit
and **not run once across eight probes this session**. All blocking gates
are green, but the omission is the defect. It also surfaced that my eight
witnesses sat in `Q0_ANCHOR_MISSING`, which the audit calls
"indistinguishable from a producer that simply forgot"; they now declare
`q0Anchor: "independent"` with per-probe reasons
(`Q0_INDEPENDENT` 9 → 17, `Q0_ANCHOR_MISSING` 1912 → 1904, `Q0_FLIP` 0).

**Status: the α-line at `v₁` is worked out.** One computable invariant
(`ε₃`), validated against four CGZ predictions, with its interpretation
correctly scoped. No obvious next increment that isn't either the
unconstructed H-side lift or a second field whose motivating question just
evaporated.
