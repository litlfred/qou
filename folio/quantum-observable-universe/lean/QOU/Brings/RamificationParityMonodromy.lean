/-
  Ramification-parity monodromy: the Door-v `(−1)^m` bar-parity residual IS the
  branch-point covering monodromy `t ↦ −t`, and the classical Seiberg–Witten
  jet-prolongation `d/dz` provably cannot generate it.

  ## Geometric setting (docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md, S1)

  On the colour spectral curve `Σ` (`P = X³ + (z+1)X² + (z²+z+1)X + …`) at a
  SIMPLE ramification point `z = z_c + t²` (local coordinate `t`, verified a
  genuine simple branch of the colour cubic in the companion probe
  `computations/probes/zgeometric_ramification_parity_probe.py`), two structures
  live on the `t`-punctured disk:

  * the **classical prolongation** `d/dz = (1/(2t)) d/dt`, which sends
    `a_k t^k ↦ (k/2) a_k t^{k-2}` — an exponent shift of **exactly −2**;
  * the **covering monodromy** `t ↦ −t` (one `z`-loop = half a `t`-loop),
    which acts on `a_k t^k` by the character `(−1)^k`.

  Modelling a local Laurent expansion `Σ_e f(e) t^e` by its coefficient function
  `f : ℤ → R`, this file proves, sorry-free and over a generic commutative ring:

  1. **(i) `d/dz` preserves `t`-parity mod 2** — because the −2 exponent shift is
     even, the classical operator `ddz` COMMUTES with the monodromy involution
     `mono` (`ddz_comm_mono`). The `ℤ/2` grading into `mono`-eigenspaces
     (bar-even / bar-odd = cosh / sinh) is preserved by every jet.
  2. **(ii) consequence** — a classical jet tower grown from a fixed-`t`-parity
     seed has a **constant** monodromy eigenvalue in the jet index `n`
     (`classical_jet_monodromy_constant`), so it can never equal a target tower
     whose eigenvalue **alternates** as `(−1)^n` (`classical_jet_no_alternating`,
     and its Door-v specialization `classical_jet_not_door_v`). The `(−1)^m`
     bar-parity that Door-v measured as the SOLE residual between `C1⊗C1` and the
     GGM/Stokes carrier is therefore identified with the ramification covering
     character — carried by `t ↦ −t`, NOT by the classical prolongation.

  ## Relation to `QOU.Mass.DoorVParityNoIdentity`

  That file excludes the `(−1)^m` residual from the tensor-square face by a
  NON-NEGATIVITY invariant (a real square is `≥ 0`, so the squares-cone holds no
  sign flip — a scope-(b) exclusion). This file gives the COMPLEMENTARY geometric
  reading of the same residual: it is the branch-point covering monodromy, and
  the classical `d/dz` is excluded from carrying it by a PARITY-PRESERVATION
  invariant (commutation with `t ↦ −t`). Together: the Door-v bar-parity is a
  geometric datum of the ramified cover, requiring a non-classical (q-difference)
  prolongation to realize.

  ## HONEST SCOPE (§Axiomatization-is-NOT-a-proof; scoping doc §3–§4)

  This proves the finite, algebraic content of sub-claim **S1**: `d/dz` preserves
  `t`-parity, and the arithmetic consequence for the monodromy character. It does
  **NOT** claim the full geometric identification
  `conj:qdifference-kernel-prolongation-symbol` (that `C1` = the prolongation
  symbol) — constructing the q-difference prolongation `D_q` from `Σ` and
  extracting its symbol are the named multi-month research walls **W1–W3**.

  🛑 **Scope correction (2026-09-06, bean `qou-p6m1`).** This sentence
  used to end with the parenthetical "(q-jet-bundle / q-D-module symbol
  calculus, absent from Mathlib and the corpus)". That bundled two objects and
  asserted absence of both; only one of them is absent.

  * **q-D-module symbol calculus — PRESENT.**
    `QOU.Machinery.QuantumTorusSymbol` (QDM-1/2: principal symbol on the q-Weyl
    quantum torus, 19 declarations, sorry-free, on `main` by 2026-07-24) and
    `QOU.Mathlib.RamifiedShiftCalculus` (the same calculus at *this file's own*
    ramified pole `z = z_c + t²`, sorry-free, 2026-09-03). The latter
    **imports this file** — the builder depends on the module that declared
    what it builds to be absent, which is how the claim survived.
  * **q-jet bundle over `Σ` — ABSENT.** W1 (construct `D_q` from
    `Σ`) is genuinely still a wall, as is the lift of `D_q` to the jet
    tower. Nothing in this correction weakens W1, and the 2026-09-03 build says
    so itself: "`D_q` is **not** constructed; W1 stays a wall."

  The keystone stays a conjecture; what is upgraded here is the `(−1)^m` residual
  from a measured sign-sequence fact to a branch-point ramification statement.

  §7c: the parity / commutation content is purely algebraic and stays over a
  generic `[CommRing R]`; only the final no-identity step adds `[NoZeroDivisors R]`
  (an algebraic domain hypothesis, not an archimedean one — `ℝ` is a valid but not
  a required instance).

  -- Ref: [leitner2026] docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md
  -- Ref: [ramis-sauloy-zhang2013] q-difference formal classification / Stokes
-/

import Mathlib.Tactic

namespace QOU.Brings.RamificationParityMonodromy

variable {R : Type*} [CommRing R]

/-! ## The covering monodromy `t ↦ −t` and the classical prolongation `d/dz` -/

/-- **Ramification covering monodromy `t ↦ −t`.** On the coefficient model
`Σ_e f(e) t^e`, substituting `t ↦ −t` sends the coefficient at exponent `e` to
`(−1)^e · f(e)`: it fixes even-`t`-degree terms and negates odd ones. This is the
`ℤ/2` grading whose `+1`/`−1` eigenspaces are the bar-even (cosh) and bar-odd
(sinh) sectors. -/
def mono (f : ℤ → R) : ℤ → R := fun e => if Even e then f e else - f e

/-- The monodromy is an involution (`(t ↦ −t)² = id`). -/
theorem mono_involutive (f : ℤ → R) : mono (mono f) = f := by
  funext e
  by_cases h : Even e <;> simp [mono, h]

/-- A degree-`(−2)` exponent shift with arbitrary coefficient weight `c`: the
coefficient of `t^e` is read from `t^{e+2}`. The classical geometric prolongation
`d/dz = (1/(2t)) d/dt` is the member with weight `c(e) = (e+2)/2` (`ddz` below);
the parity structure proved here is **weight-independent**, which is exactly why
the immaterial `½` scalar can be dropped. -/
def shift2 (c : ℤ → R) (f : ℤ → R) : ℤ → R := fun e => c e • f (e + 2)

/-- Even/odd exponents are preserved by the `−2` shift: `Even (e + 2) ↔ Even e`.
This is the arithmetic heart of "`d/dz` preserves `t`-parity". -/
theorem even_shift_two (e : ℤ) : Even (e + 2) ↔ Even e := by
  constructor
  · rintro ⟨k, hk⟩; exact ⟨k - 1, by omega⟩
  · rintro ⟨k, hk⟩; exact ⟨k + 1, by omega⟩

/-- **(i) `d/dz` preserves `t`-parity — module-level form.** Any degree-`(−2)`
shift COMMUTES with the monodromy involution `mono`, hence preserves the `ℤ/2`
grading into `mono`-eigenspaces. -/
theorem shift2_comm_mono (c f : ℤ → R) : shift2 c (mono f) = mono (shift2 c f) := by
  funext e
  simp only [shift2, mono]
  by_cases h : Even e
  · rw [if_pos h, if_pos ((even_shift_two e).mpr h)]
  · rw [if_neg h, if_neg (fun hh => h ((even_shift_two e).mp hh)), smul_neg]

/-- The **classical Seiberg–Witten jet-prolongation** `d/dz` on the branch chart,
presented as a degree-`(−2)` shift. The nonzero integer weight `(e+2)` stands in
for the geometric `(e+2)/2`; only the exponent shift (support / parity) is
load-bearing below, and it is weight-free. -/
def ddz (f : ℤ → R) : ℤ → R := shift2 (fun e => ((e + 2 : ℤ) : R)) f

/-- The classical prolongation commutes with the covering monodromy: it never
mixes the bar-even and bar-odd sectors. This is statement **(i)** for `d/dz`. -/
theorem ddz_comm_mono (f : ℤ → R) : ddz (mono f) = mono (ddz f) :=
  shift2_comm_mono _ f

/-- Concrete `−2` support shift: a monomial `t^k` (`delta k`) maps under `d/dz`
to a monomial supported at exponent `k − 2` — off `{k-2}` the image vanishes.
Since `k` and `k − 2` share parity, this is the monomial witness of (i). -/
def monomialCoeff (k : ℤ) : ℤ → R := fun e => if e = k then (1 : R) else 0

theorem ddz_monomial_support (k e : ℤ) (h : e ≠ k - 2) :
    ddz (monomialCoeff (R := R) k) e = 0 := by
  have hk : e + 2 ≠ k := by omega
  simp [ddz, shift2, monomialCoeff, hk]

/-- The two exponents related by the classical shift share `t`-parity. -/
theorem ddz_shift_preserves_parity (k : ℤ) : Even (k - 2) ↔ Even k := by
  constructor
  · rintro ⟨j, hj⟩; exact ⟨j + 1, by omega⟩
  · rintro ⟨j, hj⟩; exact ⟨j - 1, by omega⟩

/-! ## The classical jet tower and its monodromy character -/

/-- The `n`-th classical jet: `n`-fold application of `d/dz` (`X^{(n)} = dⁿX/dzⁿ`
read on the branch chart). -/
def jet (X : ℤ → R) : ℕ → (ℤ → R)
  | 0 => X
  | n + 1 => ddz (jet X n)

@[simp] theorem jet_zero (X : ℤ → R) : jet X 0 = X := rfl

theorem jet_succ (X : ℤ → R) (n : ℕ) : jet X (n + 1) = ddz (jet X n) := rfl

/-- `d/dz` is `R`-homogeneous (the weight is a fixed scalar function). -/
theorem ddz_smul (r : R) (f : ℤ → R) : ddz (r • f) = r • ddz f := by
  funext e
  simp only [ddz, shift2, Pi.smul_apply, smul_eq_mul]
  ring

/-- Homogeneity propagates through the jet tower. -/
theorem jet_smul (r : R) (X : ℤ → R) (n : ℕ) : jet (r • X) n = r • jet X n := by
  induction n with
  | zero => rfl
  | succ n ih => rw [jet_succ, jet_succ, ih, ddz_smul]

/-- The whole jet tower commutes with the monodromy: `mono` of the `n`-th jet is
the `n`-th jet of `mono` (induction on `ddz_comm_mono`). -/
theorem jet_mono (X : ℤ → R) (n : ℕ) : jet (mono X) n = mono (jet X n) := by
  induction n with
  | zero => rfl
  | succ n ih => rw [jet_succ, jet_succ, ih, ddz_comm_mono]

/-- **(ii) Constant monodromy eigenvalue.** If the seed `X` is a fixed-`t`-parity
state — an eigenvector of the covering monodromy, `mono X = ε • X` (`ε = 1`
bar-even / cosh, `ε = −1` bar-odd / sinh) — then EVERY jet `X^{(n)}` has the SAME
monodromy eigenvalue `ε`, independent of `n`. The classical prolongation cannot
make the eigenvalue depend on the jet index. -/
theorem classical_jet_monodromy_constant
    (X : ℤ → R) (ε : R) (hX : mono X = ε • X) (n : ℕ) :
    mono (jet X n) = ε • jet X n := by
  have h := jet_mono X n
  rw [hX, jet_smul] at h
  exact h.symm

/-- **No-identity (the geometric core of S1).** A classical jet tower grown from
a fixed-`t`-parity seed (`mono X = ε • X`) cannot reproduce a target tower whose
monodromy eigenvalue `σ n` genuinely differs from `ε` at some jet `n` where the
target is nonzero. Over an integral domain the constant character `ε` of the
classical tower and any nonconstant character `σ` are incompatible. -/
theorem classical_jet_no_alternating [NoZeroDivisors R]
    (X : ℤ → R) (target : ℕ → (ℤ → R)) (ε : R) (hX : mono X = ε • X)
    (σ : ℕ → R) (htar : ∀ n, mono (target n) = σ n • target n)
    (hid : ∀ n, jet X n = target n)
    (n : ℕ) (hne : ε ≠ σ n) (e : ℤ) (hnz : target n e ≠ 0) :
    False := by
  have hc : mono (jet X n) = ε • jet X n := classical_jet_monodromy_constant X ε hX n
  rw [hid n] at hc
  have h2 : ε • target n = σ n • target n := by rw [← hc, htar n]
  have h3 := congrFun h2 e
  simp only [Pi.smul_apply, smul_eq_mul] at h3
  have h4 : (ε - σ n) * target n e = 0 := by rw [sub_mul, h3, sub_self]
  rcases mul_eq_zero.mp h4 with hε | hx
  · exact hne (sub_eq_zero.mp hε)
  · exact hnz hx

/-- **Door-v specialization.** The Door-v residual is exactly a bar-even (cosh)
seed `X` (`mono X = 1 • X`) confronting a target whose `n`-th jet carries the
`(−1)^n` bar-parity character — the measured `(−1)^m` alternation. No classical
jet tower realizes it: already at `n = 1` the classical character `1` disagrees
with `(−1)^1 = −1` (using `1 ≠ −1`, i.e. characteristic `≠ 2`). The `(−1)^m`
residual is therefore the ramification covering monodromy, not a classical jet. -/
theorem classical_jet_not_door_v [NoZeroDivisors R] (hchar : (1 : R) ≠ -1)
    (X : ℤ → R) (target : ℕ → (ℤ → R))
    (hX : mono X = (1 : R) • X)
    (htar : ∀ n, mono (target n) = (-1 : R) ^ n • target n)
    (hid : ∀ n, jet X n = target n)
    (e : ℤ) (hnz : target 1 e ≠ 0) :
    False :=
  classical_jet_no_alternating X target 1 hX (fun n => (-1 : R) ^ n) htar hid 1
    (by simpa using hchar) e hnz

end QOU.Brings.RamificationParityMonodromy
