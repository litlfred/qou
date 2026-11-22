/-
Copyright (c) 2026 litlfred. All rights reserved.

# The level-`d` q-Borel kernel `tₙ = q^{n−d}·t_{n−d}` (W2 ∞-Stokes, stage S0)

Generalizes [`QBorelKernel`](QBorelKernel.lean) from level `d = 1` to arbitrary level `d`.
Per Ramis–Sauloy–Zhang (Astérisque 355, §3.3 p. 39) an irregular singularity of level `d`
is resolved by the q-Borel transform `B_{q,d}(∑ fₙ zⁿ) = ∑ (fₙ/tₙ) ξⁿ` with kernel family
`tₙ = q^{n−d}·t_{n−d}` of growth `q^{n²/2d}`. C1's ∞ singularity has slope ½, i.e. level
`d = 2`.

**Design.** The exponent is given in *closed form* and the RSZ recurrence is *proved* from
it, rather than defining by recursion on `n − d` (which would need well-founded recursion
and make every downstream rewrite awkward). Writing `n = d·m + r` with `m = n / d`,
`r = n % d`, the chain `n, n−d, n−2d, …, r` sums to

    exponent(d, n) = m·r + d·C(m, 2).

Sanity: `d = 1` gives `m = n`, `r = 0`, hence `C(n,2)` — exactly `QBorelKernel`
(`qBorelExp_one_eq_choose`, and the kernels agree on the nose:
`qBorelKernelLevel_one_eq`). `d = 2`, `n = 2m` gives `m(m−1) ≈ n²/4`, matching the RSZ
growth `q^{n²/2d}`.

**Scope (stage S0 of `docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md`).** The kernel
family and its degree law only.

🛑 **The onward staging this note used to point at was RETIRED the same week, and this
note did not follow (corrected 2026-09-07, bean `qou-hok7`).** It read: *"The ramified
level-2 construction for C1, the `d`-th roots `B₁,B₂` of the slope blocks, and the two
Stokes multipliers `U ∈ ℂ²` are NOT here — beans `qou-qbr3`, `qou-qbs4`, and the RSZ-wild
residual `qou-xufp`."* **`qou-qbr3`, `qou-qbs4` and `qou-qbg2` were all scrapped in one
batch on 2026-08-08**, because
[`2026-08-08-rsz-c1-infinity-route-closed.md`](../../../../../docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md)
established the chain *"slope ½ ⇒ RSZ level 2 ⇒ `F(P₁,P₂) ≅ ℂ²` ⇒ two multipliers"* as a
**mis-citation**: RSZ §3.3 is titled *"…in the case of **integral slopes**"*, and ½ is not
integral. Every number in that chain was right; the reading was not.

So a reader arriving here is pointed at three scrapped beans as the live carriers. The
live ones are **`qou-wgnx`** (the connection-matrix Stokes multipliers between the
theta-normalised solutions at `0` and `∞` — a *different object* from the local isoformal
moduli, and genuinely open) and **q-native alien calculus**, which the closure audit
argues is right for the reason RSZ was wrong: `F(P₁,…,P_k)` is built on the slope
filtration, whereas alien derivations need none.

**Nothing below changes.** The kernel family, the degree law and the growth budget are
arithmetic and stand; only the note about where the onward work lives was stale.

**Note the growth budget** (bean `qou-qbg2`, stage S1): the degree law proved here, set
against the proved `deg_q(cₙ) = n²` for the C1 ∞ coefficients
([`C1InfDegreeLaw`](../QBeta/C1InfDegreeLaw.lean)), shows no *unramified* level `d` absorbs
the coefficient growth. That is why S1 precedes S2/S3.

§7c: generic `Monoid R` (commutativity unused; no ordering, nothing archimedean).
Sorry-free. No fit; nothing wired.

-- Ref: [ramis-sauloy-zhang2013] https://arxiv.org/abs/0903.0853 (§3.3, q-Borel transform)
-- Ref: [ramis-sauloy2006] https://arxiv.org/abs/math/0611521 (§3.2, Thm 3.8: the level-δ
--      q-Borel values B_q^{(δ)}U(jL) vanish iff the one-level equation has a convergent
--      solution, and form a complete set of analytic invariants in the formal class;
--      Thm 3.9: a θ^{−δ} factor carries them to the alien-derivation invariants). §2.3
--      "one level" assumes two integral slopes, so this gives the kernel's meaning, not
--      C1 Stokes data (C1 at ∞ is isoclinic).
-- Ref: [leitner2026] docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md
-/
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Tactic.Ring
import QOU.MathlibExt.QBorelKernel

namespace QOU.MathlibExt.QBorelKernel

variable {R : Type*} [Monoid R]

/-- **The level-`d` q-Borel kernel exponent.** With `n = d·m + r` (`m = n / d`,
`r = n % d`), summing the chain `n, n−d, …, r` gives `m·r + d·C(m,2)`. -/
def qBorelExp (d n : ℕ) : ℕ := (n / d) * (n % d) + d * ((n / d).choose 2)

/-- Below the level, the kernel exponent vanishes: the chain is empty. -/
theorem qBorelExp_of_lt {d n : ℕ} (h : n < d) : qBorelExp d n = 0 := by
  simp [qBorelExp, Nat.div_eq_of_lt h]

/-- At level `1` the exponent is the Jacobi-theta exponent `C(n,2)`. -/
@[simp] theorem qBorelExp_one_eq_choose (n : ℕ) : qBorelExp 1 n = n.choose 2 := by
  simp [qBorelExp, Nat.mod_one]

/-- **The RSZ exponent recurrence**, proved from the closed form:
`exponent(d,n) = (n−d) + exponent(d, n−d)` for `d ≤ n`. -/
theorem qBorelExp_rec {d n : ℕ} (hd : 0 < d) (hn : d ≤ n) :
    qBorelExp d n = (n - d) + qBorelExp d (n - d) := by
  obtain ⟨k, rfl⟩ : ∃ k, n = k + d := ⟨n - d, (Nat.sub_add_cancel hn).symm⟩
  have hdiv : (k + d) / d = k / d + 1 := Nat.add_div_right k hd
  have hmod : (k + d) % d = k % d := Nat.add_mod_right k d
  have hk : d * (k / d) + k % d = k := Nat.div_add_mod k d
  simp only [qBorelExp, hdiv, hmod, Nat.add_sub_cancel]
  rw [Nat.choose_succ_succ, Nat.choose_one_right, Nat.add_mul, Nat.mul_add, one_mul]
  -- Goal is now linear in the atoms `m*r`, `d*m`, `d*C(m,2)`, `r`, `k`; the only
  -- input is `d*m + r = k`. Generalize the products so `omega` can see that.
  set r := k % d with hr
  set P := d * (k / d) with hP
  set A := k / d * r with hA
  set B := d * ((k / d).choose 2) with hB
  omega

/-- **The level-`d` q-Borel kernel** `tₙ = q^{exponent(d,n)}`. -/
def qBorelKernelLevel (d : ℕ) (q : R) (n : ℕ) : R := q ^ qBorelExp d n

@[simp] theorem qBorelKernelLevel_of_lt {d n : ℕ} (q : R) (h : n < d) :
    qBorelKernelLevel d q n = 1 := by
  simp [qBorelKernelLevel, qBorelExp_of_lt h]

/-- **Level `1` reproduces the existing kernel on the nose.** This is the compatibility
check: the generalization is conservative. -/
@[simp] theorem qBorelKernelLevel_one_eq (q : R) (n : ℕ) :
    qBorelKernelLevel 1 q n = qBorelKernel q n := by
  simp [qBorelKernelLevel, qBorelKernel]

/-- **The RSZ kernel family relation** `tₙ = q^{n−d} · t_{n−d}` — the defining property of
the level-`d` q-Borel kernel, for every `d ≥ 1`. -/
theorem qBorelKernelLevel_rec {d n : ℕ} (q : R) (hd : 0 < d) (hn : d ≤ n) :
    qBorelKernelLevel d q n = q ^ (n - d) * qBorelKernelLevel d q (n - d) := by
  simp only [qBorelKernelLevel, qBorelExp_rec hd hn, pow_add]

/-- Specialization to level `1`, recovering `qBorelKernel_succ`'s shape. -/
theorem qBorelKernelLevel_one_rec (q : R) (n : ℕ) :
    qBorelKernelLevel 1 q (n + 1) = q ^ n * qBorelKernelLevel 1 q n := by
  simpa using qBorelKernelLevel_rec (d := 1) (n := n + 1) q Nat.one_pos (by omega)

/-! ### The degree law

`exponent(d, d·m) = d·C(m,2)`, i.e. `≈ n²/2d` — the RSZ growth. For `d = 2` this is
`m(m−1) ≈ n²/4`, the number the S1 growth-budget probe uses. -/

/-- **Degree law on the level lattice.** At `n = d·m` the exponent is exactly `d·C(m,2)`,
which is the `q^{n²/2d}` growth: `d·C(m,2) = d·m(m−1)/2 ≈ (d·m)²/(2d)`. -/
theorem qBorelExp_mul (d m : ℕ) (hd : 0 < d) :
    qBorelExp d (d * m) = d * (m.choose 2) := by
  have h1 : d * m / d = m := by
    rw [Nat.mul_div_cancel_left _ hd]
  have h2 : d * m % d = 0 := Nat.mul_mod_right d m
  simp [qBorelExp, h1, h2]

/-- `2·C(m,2) = m(m−1)` — the standard identity, in the `ℕ`-subtraction form needed
below. -/
theorem two_mul_choose_two (m : ℕ) : 2 * m.choose 2 = m * (m - 1) := by
  induction m with
  | zero => simp
  | succ k ih =>
      rw [Nat.choose_succ_succ, Nat.choose_one_right, Nat.mul_add, ih,
        Nat.succ_sub_one]
      cases k with
      | zero => simp
      | succ j => simp only [Nat.succ_sub_one]; ring

/-- Level `2`, even index: `exponent(2, 2m) = m(m−1)`. The concrete C1 case: with
`n = 2m` this is `≈ n²/4`, the number the S1 growth-budget probe uses. -/
theorem qBorelExp_two_even (m : ℕ) : qBorelExp 2 (2 * m) = m * (m - 1) := by
  rw [qBorelExp_mul 2 m (by omega), two_mul_choose_two]

end QOU.MathlibExt.QBorelKernel
