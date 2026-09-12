/-
# The nucleon flavour content is DETERMINED, and `Δ` differs in exactly one letter

`qou-99qc`. Closes the question the γγ probe leaves open — *"`Δ` needs the
flavour letters"* — by showing the flavour letters carry **no freedom at all**.

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

## What is proved

* `pairCounts` — the pair-type counts `(C(n_u,2), n_u·n_d, C(n_d,2))`.
* `proton_pairCounts` / `neutron_pairCounts` — `(1,2,0)` and `(0,2,1)`, which are
  **exactly** the shift lists the census recipe hardcodes
  (`[0, −h/2, −h/2]` and `[−h, −h/2, −h/2]`); so the recipe's flavour letters
  are derived, not posited.
* `pairCounts_sum` — the three types partition all `C(n_u+n_d, 2)` pairs, so
  nothing is missing from the typing.
* **`nucleon_difference_is_one_letter`** — the `ud` counts of proton and
  neutron are **equal**, and the multisets differ by one `uu` removed and one
  `dd` added.

## Why the last one matters

`Δ = 𝓑_n − 𝓑_p` is a difference of two words whose flavour content differs in
**exactly one letter**: a single `σ` becomes a single `σ⁻¹`. Everything else —
the `B₃` confinement core, both `ud` crossings, the gluon letters — is common to
both and cancels in no naive way but is structurally identical.

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

-- Ref: [manuscript] `knots-particles-confinement/up-quark-properties.md`
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

/-- **The typing is exhaustive**: the three pair types account for every pair of
the `n_u + n_d` quarks, so no crossing is left untyped. -/
theorem pairCounts_sum (nu nd : ℕ) :
    (pairCounts nu nd).1 + (pairCounts nu nd).2.1 + (pairCounts nu nd).2.2
      = (nu + nd).choose 2 := by
  simp only [pairCounts]
  rw [addChooseTwo]

/-- **The two nucleons share their mixed-pair count.** -/
theorem ud_count_equal : (pairCounts 2 1).2.1 = (pairCounts 1 2).2.1 := by decide

/-- **`Δ`'s flavour content differs in exactly ONE letter.**

Going from the proton to the neutron removes one `uu` crossing and adds one
`dd`; the mixed-pair count is unchanged. In shift terms a single `d = 0`
becomes a single `d = −h` — one `σ` becoming one `σ⁻¹` — and every other
flavour letter is common to both words. -/
theorem nucleon_difference_is_one_letter :
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

end QOU.QBeta.NucleonFlavour
