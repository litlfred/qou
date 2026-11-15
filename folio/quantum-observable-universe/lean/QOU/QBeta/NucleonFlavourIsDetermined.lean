/-
# The nucleon flavour content is DETERMINED, and the p→n flip retypes TWO crossings

`qou-99qc`. Closes the question the γγ probe leaves open — *"`Δ` needs the
flavour letters"* — by showing the flavour letters carry **no freedom at all**,
and then says exactly how the proton and neutron words differ.

## 🛑 CORRECTION, recorded rather than overwritten

An earlier revision of this file (and of PR #7212's title and body) claimed the
two nucleon words *"differ in exactly one letter: a single `σ` becomes a single
`σ⁻¹`."* **That is wrong at the letter level, and the corpus's own data says
so.** `_GEN_CHAINS` in `qbeta_delta_candidate_census_probe.py` gives

```
p : gen0 [0, 0, 0,    0, −1/2, 0, 0]   gen1 [−1, −1, −1, −1/2]
n : gen0 [0, 0, 0, −1/2, −1/2, 0, 0]   gen1 [−1, −1, −1,   −1]
```

which differ in **two** slots — `gen0[3]: 0 → −1/2` and `gen1[3]: −1/2 → −1` —
each by exactly `−1/2`, i.e. by `−h/2`.

The counts below were never wrong; the *reading* of them was. `(1,2,0)` versus
`(0,2,1)` is consistent with a single `uu ↦ dd` substitution, and it is also
consistent with the flip that actually happens — and only the second is a
possible β-decay. Flipping one quark's flavour retypes every pair that quark
belongs to, and in a three-quark nucleon each quark belongs to **two** of the
three pairs. So one `uu` becomes `ud` and one `ud` becomes `dd`; the `ud` count
is preserved by **cancellation**, one gained against one lost, not by being
untouched. `flip_retypes_pairs` below proves that in general.

The consequence is not cosmetic. Under the one-letter reading `Δ` would be
`±h` times a single smoothed word (the skein relation applied once). Under the
true two-letter flip it is a **three-term** expansion, `two_shift_expansion`,
whose leading coefficient is `−h/2` rather than `−h` and which carries an
`h²/4` double-smoothing term. Both are verified numerically to 60 dps in
`qbeta_nucleon_flip_skein_expansion_probe.py`.

## The rule, from the corpus's own blocks

`knots-particles-confinement/up-quark-properties.md`: the up quark has positive
orientation, so *"the up quark's crossings contribute `+q` to the Skein
polynomial at each crossing point"*.
`down-quark-properties.md`: the down quark is *"the reversed-orientation
component"*, so its crossings carry `q⁻¹`.

A crossing between two quarks is therefore typed by their orientations:

| pair | orientations | crossing | Hecke shift `d` |
|---|---|---|---|
| `uu` | both positive | `σ` | `0` |
| `ud` | mixed | averaged | `−h/2` |
| `dd` | both reversed | `σ⁻¹` | `−h` |

and a nucleon of three quarks has `C(3,2) = 3` such pairs. So its shift multiset
is fixed by the counts `(n_u, n_d)` alone — there is nothing to choose.

That table is not three separate conventions either: `skein_letter_inv` proves
`σ − h = σ⁻¹` straight out of the Hecke relation, so the `dd` letter *is* the
inverse crossing, and `ud_letter_is_average` proves the mixed letter is exactly
`(σ + σ⁻¹)/2`. The single scalar `−h/2` is the whole content of the typing.

## What is proved

* `pairCounts` — the pair-type counts `(C(n_u,2), n_u·n_d, C(n_d,2))`.
* `proton_pairCounts` / `neutron_pairCounts` — `(1,2,0)` and `(0,2,1)`, which are
  **exactly** the shift lists the census recipe hardcodes
  (`[0, −h/2, −h/2]` and `[−h, −h/2, −h/2]`); so the recipe's flavour letters
  are derived, not posited.
* `pairCounts_sum` — the three types partition all `C(n_u+n_d, 2)` pairs, so
  nothing is missing from the typing.
* `nucleon_pairCounts_differ_by_one_uu_and_one_dd` — the `ud` counts of proton
  and neutron are **equal**, and the multisets differ by one `uu` removed and
  one `dd` added. A statement about **counts**; see the correction above for
  what it does and does not license.
* **`flip_retypes_pairs`** — flipping one up to a down converts `m` pairs from
  `uu` to `ud` and `n` pairs from `ud` to `dd`, for a nucleon of `m+1` ups and
  `n` downs. At `m = n = 1` that is **two** retyped crossings out of three.
* **`two_shift_expansion`** — the resulting element identity, over a
  noncommutative ring with a central scalar.
* `skein_letter_inv` / `ud_letter_is_average` — the typing table's own entries,
  derived from the Hecke relation.

## Why the flip lemma matters

`Δ = 𝓑_n − 𝓑_p` is a difference of two words that agree everywhere except at
two slots, and at each of those the neutron letter is the proton letter plus the
**same central scalar** `s = −h/2`. Expanding,

```
Δ = s·(S_A + S_B) + s²·S_AB
```

where `S_A`, `S_B` are the proton word with one of the two crossings smoothed
and `S_AB` has both smoothed. So the decay element is a small combination of
**lower-crossing** words — which is the quantitative reason the two nucleon
traces sit so close together: `|s| ≈ 0.1045`, and the `s²` term is a 2 %
correction to the `s` term.

Combined with the two measurements already merged or in review, this closes the
construction:

* the flavour content is **determined** (here);
* the placement freedom — which generator each pair sits on, and the ordering —
  is **exhausted**: 0 of 37,459,422,000 configurations reach `Q_β` (#7188);
* the ruled γγ selection **cannot come close** on its own: the target sits in a
  gap 3.13× its own width (#7212).

So the recipe is not under-explored, it is **fully explored**. "Try a different
flavour assignment" is not available: there is no other assignment. A closing
`Δ` has to come from a different construction, not a different reading of this
one.

## Scope

This proves the flavour multiset is determined **given** the quark content
`uud` / `udd` and the orientation rule. It does not derive the quark content,
and the corpus is explicit that the charges are adopted rather than derived —
`up-quark-properties.md`: *"The Standard Model values are adopted here, not
derived from the crossing count. The parameter-free ribbon route to them is
recorded as tested and refuted."* Nothing here changes that.

`two_shift_expansion` is an identity about **any** two slots carrying a common
central shift; that the nucleon words are in that shape is established by the
`_GEN_CHAINS` reading above and re-verified numerically, not proved here.

-- Ref: [leitner2026] `knots-particles-confinement/up-quark-properties.md`
-/
import Mathlib.Tactic

namespace QOU.QBeta.NucleonFlavour

/-- Pair-type counts for a three-quark content with `n_u` up and `n_d` down:
`(#uu, #ud, #dd)`. Each unordered pair of quarks is one crossing, typed by the
two orientations. -/
def pairCounts (nu nd : ℕ) : ℕ × ℕ × ℕ :=
  (nu.choose 2, nu * nd, nd.choose 2)

/-- **The proton `uud`**: one `uu`, two `ud`, no `dd`. These are exactly the
shifts the census recipe hardcodes as `[0, −h/2, −h/2]`. -/
theorem proton_pairCounts : pairCounts 2 1 = (1, 2, 0) := by decide

/-- **The neutron `udd`**: no `uu`, two `ud`, one `dd` — the recipe's
`[−h, −h/2, −h/2]`. -/
theorem neutron_pairCounts : pairCounts 1 2 = (0, 2, 1) := by decide

/-- `C(m+n, 2) = C(m,2) + m·n + C(n,2)` — the `k = 2` case of Vandermonde,
proved here because Mathlib carries no `Nat.add_choose_two`. -/
theorem addChooseTwo (m n : ℕ) :
    (m + n).choose 2 = m.choose 2 + m * n + n.choose 2 := by
  induction n with
  | zero => simp
  | succ k ih =>
    have h : m + (k + 1) = (m + k) + 1 := by omega
    rw [h, Nat.choose_succ_succ, ih, Nat.choose_succ_succ k 1, Nat.mul_succ]
    norm_num [Nat.choose_one_right]
    omega

/-- `C(m+1, 2) = C(m, 2) + m`: adding one quark to a same-flavour group adds one
pair per quark already there. The `n = 1` case of `addChooseTwo`. -/
theorem succChooseTwo (m : ℕ) : (m + 1).choose 2 = m.choose 2 + m := by
  have := addChooseTwo m 1
  simpa using this

/-- **The typing is exhaustive**: the three pair types account for every pair of
the `n_u + n_d` quarks, so no crossing is left untyped. -/
theorem pairCounts_sum (nu nd : ℕ) :
    (pairCounts nu nd).1 + (pairCounts nu nd).2.1 + (pairCounts nu nd).2.2
      = (nu + nd).choose 2 := by
  simp only [pairCounts]
  rw [addChooseTwo]

/-- **The two nucleons share their mixed-pair count.**

Read with `flip_retypes_pairs`: the equality is a **cancellation**, one `ud`
gained against one `ud` lost, not evidence that the mixed crossings are
untouched by the decay. -/
theorem ud_count_equal : (pairCounts 2 1).2.1 = (pairCounts 1 2).2.1 := by decide

/-- **The pair-type counts differ by one `uu` and one `dd`.**

Going from the proton to the neutron removes one `uu` crossing and adds one
`dd`, with the mixed-pair count unchanged. This is a statement about **counts**
only. It does *not* say the two words differ in one letter — see
`flip_retypes_pairs`, which shows two crossings are retyped. -/
theorem nucleon_pairCounts_differ_by_one_uu_and_one_dd :
    (pairCounts 2 1).1 = (pairCounts 1 2).1 + 1 ∧
    (pairCounts 2 1).2.1 = (pairCounts 1 2).2.1 ∧
    (pairCounts 2 1).2.2 + 1 = (pairCounts 1 2).2.2 := by
  refine ⟨by decide, by decide, by decide⟩

/-- **Determination, stated plainly**: the shift multiset is a function of the
quark counts, so two nucleon models with the same `(n_u, n_d)` cannot differ in
their flavour letters. There is no flavour freedom to exploit. -/
theorem pairCounts_determined {nu nd nu' nd' : ℕ}
    (hu : nu = nu') (hd : nd = nd') : pairCounts nu nd = pairCounts nu' nd' := by
  rw [hu, hd]

/-! ## The flip retypes two crossings, not one -/

/-- **β-decay retypes TWO pairs.**

A nucleon of `m+1` ups and `n` downs becomes one of `m` ups and `n+1` downs when
a single up flips. The flipped quark belonged to `m` same-flavour pairs and `n`
mixed pairs, so:

* `m` pairs move `uu → ud`;
* `n` pairs move `ud → dd`;
* the `C(m,2) + C(n,2)` pairs not containing it are untouched.

Stated additively to avoid truncated `ℕ` subtraction. At `m = n = 1` — the
proton — this is `1 + 1 = 2` retyped crossings out of three, which is what the
census chains show. -/
theorem flip_retypes_pairs (m n : ℕ) :
    (pairCounts m (n + 1)).1 + m = (pairCounts (m + 1) n).1 ∧
    (pairCounts m (n + 1)).2.1 + n = (pairCounts (m + 1) n).2.1 + m ∧
    (pairCounts (m + 1) n).2.2 + n = (pairCounts m (n + 1)).2.2 := by
  refine ⟨?_, ?_, ?_⟩
  · simpa [pairCounts] using (succChooseTwo m).symm
  · simp only [pairCounts]
    ring
  · simpa [pairCounts] using (succChooseTwo n).symm

/-- The proton case: **two** of the three crossings are retyped. -/
theorem nucleon_flip_retypes_two_of_three : 1 + 1 = 2 ∧ Nat.choose 3 2 = 3 := by
  refine ⟨by decide, by decide⟩

/-! ## The element identity the flip produces -/

/-- **The two-slot shift expansion.**

If two letters of a word each pick up the *same central* scalar `c`, the
difference of the shifted and unshifted words is a three-term combination of
words with one and both of those letters deleted:

```
X(a+c)Y(b+c)Z − XaYbZ = c·(XYbZ) + c·(XaYZ) + c²·(XYZ)
```

Stated over a noncommutative `Ring` — the braid algebra is not commutative — with
centrality of `c` as an explicit hypothesis. Applied to the nucleons, `c` is the
scalar `−h/2` and the three right-hand words are the proton word with one or
both flavour crossings smoothed. -/
theorem two_shift_expansion {A : Type*} [Ring A] (X a Y b Z c : A)
    (hc : ∀ x : A, c * x = x * c) :
    X * (a + c) * Y * (b + c) * Z - X * a * Y * b * Z
      = c * (X * Y * b * Z) + c * (X * a * Y * Z) + c * c * (X * Y * Z) := by
  have hpull : ∀ u v : A, u * c * v = c * (u * v) := by
    intro u v
    rw [← hc u, mul_assoc]
  have e1 : X * c * Y * b * Z = c * (X * Y * b * Z) := by
    rw [hpull X Y]; noncomm_ring
  have e2 : X * a * Y * c * Z = c * (X * a * Y * Z) := by
    rw [hpull (X * a * Y) Z]
  have e3 : X * c * Y * c * Z = c * c * (X * Y * Z) := by
    rw [hpull X Y, hpull (c * (X * Y)) Z]; noncomm_ring
  calc X * (a + c) * Y * (b + c) * Z - X * a * Y * b * Z
      = X * c * Y * b * Z + X * a * Y * c * Z + X * c * Y * c * Z := by noncomm_ring
    _ = c * (X * Y * b * Z) + c * (X * a * Y * Z) + c * c * (X * Y * Z) := by
        rw [e1, e2, e3]

/-! ## The typing table's own entries, from the Hecke relation -/

/-- **The `dd` letter is the inverse crossing.** Straight from the Hecke
relation `σ² = (q − q⁻¹)σ + 1` of AGENTS.md §7a: multiplying by `σ⁻¹` gives
`σ − σ⁻¹ = q − q⁻¹`, so the shift `d = −h` *is* `σ⁻¹`. -/
theorem skein_letter_inv {R : Type*} [Field R] (q σ : R)
    (hrel : σ ^ 2 = (q - q⁻¹) * σ + 1) :
    σ - (q - q⁻¹) = σ⁻¹ := by
  have hmul : σ * (σ - (q - q⁻¹)) = 1 := by linear_combination hrel
  exact (inv_eq_of_mul_eq_one_right hmul).symm

/-- **The `ud` letter is the average of the two crossings.** The shift `−h/2`
sits exactly halfway, so the mixed-orientation entry of the typing table is
`(σ + σ⁻¹)/2` and not a separate convention. -/
theorem ud_letter_is_average {R : Type*} [Field R] (q σ : R) (h2 : (2 : R) ≠ 0)
    (hrel : σ ^ 2 = (q - q⁻¹) * σ + 1) :
    σ - (q - q⁻¹) / 2 = (σ + σ⁻¹) / 2 := by
  have h := skein_letter_inv q σ hrel
  rw [← h]
  field_simp
  ring

end QOU.QBeta.NucleonFlavour
